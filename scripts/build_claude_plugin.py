#!/usr/bin/env python3
"""Build the Claude plugin package (<name>.plugin) from the skillmesh authoring source.

Reads skillmesh/plugin.json, skillmesh/mcp.json, skills/ and serena/; writes a
deterministic zip. The source is never modified. Usage:

    python scripts/build_claude_plugin.py [--out dist/skillmesh.plugin]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'skillmesh'
CONTENT_DIRS = ('skills', 'serena')
TEXT_SUFFIXES = {'.md', '.yml', '.yaml', '.py', '.json'}
MANIFEST_KEYS = ('name', 'version', 'description', 'author')
FIXED_TIME = (2020, 1, 1, 0, 0, 0)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def claude_manifest(source: dict) -> bytes:
    manifest = {key: source[key] for key in MANIFEST_KEYS}
    return (json.dumps(manifest, indent=2) + '\n').encode('utf-8')


def claude_mcp(source_text: str) -> bytes:
    converted = source_text.replace('${PLUGIN_ROOT}', '${CLAUDE_PLUGIN_ROOT}')
    config = json.loads(converted)
    config.pop('$schema', None)
    return (json.dumps(config, indent=2) + '\n').encode('utf-8')


def content_files() -> list[Path]:
    files = []
    for name in CONTENT_DIRS:
        for path in (SOURCE / name).rglob('*'):
            if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
                files.append(path)
    return sorted(files, key=lambda p: p.relative_to(SOURCE).as_posix())


def file_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    # Windows checkouts may carry CRLF; keep the package identical on every device.
    return data.replace(b'\r\n', b'\n') if path.suffix in TEXT_SUFFIXES else data


def package_entries(name: str, source: dict) -> dict[str, bytes]:
    entries = {
        f'{name}/.claude-plugin/plugin.json': claude_manifest(source),
        f'{name}/.mcp.json': claude_mcp((SOURCE / 'mcp.json').read_text(encoding='utf-8')),
    }
    for path in content_files():
        entries[f'{name}/{path.relative_to(SOURCE).as_posix()}'] = file_bytes(path)
    return entries


def write_zip(out: Path, entries: dict[str, bytes]) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as archive:
        for arcname in sorted(entries):
            info = zipfile.ZipInfo(arcname, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, entries[arcname])


def verify(out: Path, name: str) -> int:
    expected = sorted(p.name for p in (SOURCE / 'skills').iterdir() if p.is_dir())
    with zipfile.ZipFile(out) as archive:
        names = set(archive.namelist())
        missing = [s for s in expected if f'{name}/skills/{s}/SKILL.md' not in names]
        manifest = json.loads(archive.read(f'{name}/.claude-plugin/plugin.json'))
        mcp_text = archive.read(f'{name}/.mcp.json').decode('utf-8')
        json.loads(mcp_text)
    problems = []
    if missing:
        problems.append(f'missing skills: {missing}')
    if manifest['name'] != name:
        problems.append('manifest name mismatch')
    if '${PLUGIN_ROOT}' in mcp_text:
        problems.append('unconverted ${PLUGIN_ROOT} in .mcp.json')
    if problems:
        raise SystemExit('Package check failed: ' + '; '.join(problems))
    return len(expected)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--out', type=Path, help='output file (default: dist/<name>.plugin)')
    args = parser.parse_args()

    source = read_json(SOURCE / 'plugin.json')
    name = source['name']
    out = (args.out or ROOT / 'dist' / f'{name}.plugin').resolve()
    write_zip(out, package_entries(name, source))
    skills = verify(out, name)
    digest = hashlib.sha256(out.read_bytes()).hexdigest()[:16]
    print(f'{out}\n{name} {source["version"]}: {skills} skills, sha256 {digest}')


if __name__ == '__main__':
    sys.exit(main())
