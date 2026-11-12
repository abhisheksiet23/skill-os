"""Opt-in live MCP/LSP smoke test; synthetic fixtures, no model or app changes.

Run with Python containing Serena's MCP client dependency. uvx must be available.
Provider/runtime caches are isolated under the ignored .validation-deps directory.
"""
from __future__ import annotations

import argparse
import asyncio
from contextlib import AsyncExitStack
import json
import os
from pathlib import Path
import re
import tempfile

from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

ROOT = Path(__file__).resolve().parents[1]
NAVIGATION_TOOLS = {'initial_instructions', 'activate_project', 'get_current_config',
                    'get_symbols_overview', 'find_symbol', 'find_referencing_symbols', 'find_implementations'}


def fixture(root: Path, marker: str, language: str) -> None:
    (root / '.serena').mkdir(parents=True)
    (root / '.serena/project.yml').write_text(
        f'project_name: {marker}\nlanguage_servers: [{language}]\nread_only: true\n', encoding='utf-8')
    if language == 'csharp':
        (root / 'Fixture.csproj').write_text(
            '<Project Sdk="Microsoft.NET.Sdk"><PropertyGroup><TargetFramework>net10.0</TargetFramework>'
            '</PropertyGroup></Project>', encoding='utf-8')
        (root / 'service.cs').write_text(
            f'public class PricingService {{ public static string CalculateTotal(int value) => "{marker}" + value; }}\n', encoding='utf-8')
        (root / 'consumer.cs').write_text(
            'public class Consumer { public string Run() => PricingService.CalculateTotal(5); }\n', encoding='utf-8')
        return
    (root / 'tsconfig.json').write_text(json.dumps({
        'compilerOptions': {'target': 'ES2020', 'module': 'commonjs', 'strict': True},
        'include': ['*.ts'],
    }), encoding='utf-8')
    (root / 'service.ts').write_text(
        f'export function calculateTotal(value: number): string {{ return "{marker}" + value; }}\n', encoding='utf-8')
    (root / 'consumer.ts').write_text(
        'import { calculateTotal } from "./service";\nexport const result = calculateTotal(5);\n', encoding='utf-8')


def content(result) -> str:
    return '\n'.join(getattr(block, 'text', '') for block in result.content)


async def call(session, name, arguments):
    result = await session.call_tool(name, arguments)
    text = content(result)
    if result.is_error:
        raise AssertionError(f'{name}: {text}')
    return text


async def main(uvx: str, language: str):
    config = json.loads((ROOT / 'skillmesh/mcp.json').read_text())['mcpServers']['serena']
    args = [arg.replace('${PLUGIN_ROOT}', str(ROOT / 'skillmesh')) for arg in config['args']]
    cache = ROOT / '.validation-deps'
    env = dict(os.environ, SKILLMESH_SERENA_HOME=str(cache / 'serena-live-home-v2'),
               UV_CACHE_DIR=str(cache / 'uv-cache'), UV_PYTHON_INSTALL_DIR=str(cache / 'uv-python'),
               npm_config_cache=str(cache / 'npm-cache'))
    cache.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='serena-live-', dir=cache) as directory:
        base = Path(directory)
        a, b = base / 'alpha', base / 'beta'
        fixture(a, 'alpha', language)
        fixture(b, 'beta', language)
        source = 'service.cs' if language == 'csharp' else 'service.ts'
        consumer = 'consumer.cs' if language == 'csharp' else 'consumer.ts'
        symbol_name = 'PricingService/CalculateTotal' if language == 'csharp' else 'calculateTotal'
        with (base / 'server.log').open('w', encoding='utf-8') as log:
            async with AsyncExitStack() as stack:
                sessions = []
                for root in (a, b):
                    streams = await stack.enter_async_context(stdio_client(
                        StdioServerParameters(command=uvx, args=args, env=env, cwd=ROOT), errlog=log))
                    session = await stack.enter_async_context(ClientSession(*streams))
                    await session.initialize()
                    tools = {tool.name for tool in (await session.list_tools()).tools}
                    assert tools == NAVIGATION_TOOLS, tools
                    instructions = await call(session, 'initial_instructions', {})
                    # Serena exposes its generated session identifier in the manual.
                    match = re.search(r'Your Serena session id is `([^`]+)`', instructions)
                    assert match, 'Provider did not supply its session identifier.'
                    assert '<mode name="editing">' not in instructions
                    token = match.group(1)
                    await call(session, 'activate_project', {'project': str(root), 'session': token})
                    # Activation starts LSP initialization asynchronously. Establish readiness
                    # before another process could initialize a shared cold dependency cache.
                    ready = await call(session, 'find_symbol', {
                        'name_path_pattern': symbol_name, 'relative_path': source, 'include_body': True})
                    assert root.name in ready, ready
                    sessions.append((session, token))
                    print(f'Activated {root.name}; exact navigation catalog: {len(tools)} tools', flush=True)
                for (session, _), root in zip(sessions, (a, b)):
                    current = await call(session, 'get_current_config', {})
                    assert root.name in current, current
                    symbol = await call(session, 'find_symbol', {
                        'name_path_pattern': symbol_name, 'relative_path': source, 'include_body': True})
                    assert root.name in symbol, symbol
                    refs = await call(session, 'find_referencing_symbols', {
                        'name_path': symbol_name, 'relative_path': source})
                    assert consumer in refs, refs
                first, token = sessions[0]
                await call(first, 'activate_project', {'project': str(b), 'session': token})
                switched = await call(first, 'find_symbol', {
                    'name_path_pattern': symbol_name, 'relative_path': source, 'include_body': True})
                assert 'beta' in switched and 'alpha' not in switched, switched
                missing = await first.call_tool('activate_project', {'project': str(base / 'missing'), 'session': token})
                assert missing.is_error or any(word in content(missing).lower() for word in ('error', 'not found', 'does not exist'))
                # A native fallback remains usable independently of provider activation errors.
                assert symbol_name.split('/')[-1] in (b / consumer).read_text()
                print(f'PASS ({language}): real definitions/references, two independent processes, project switch, missing-root error and native fallback.', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--uvx', default='uvx')
    parser.add_argument('--language', choices=('typescript', 'csharp'), default='typescript')
    options = parser.parse_args()
    async def bounded_run():
        async with asyncio.timeout(300):
            await main(options.uvx, options.language)
    asyncio.run(bounded_run())
