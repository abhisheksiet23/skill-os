"""Opt-in native plugin/catalog check: no chat creation or model invocation."""
import json
import os
from pathlib import Path
import queue
import subprocess
import threading
import time

root = Path(__file__).resolve().parents[1]
messages = queue.Queue()
with (root / '.validation-deps/host-probe.log').open('w', encoding='utf-8') as log:
    process = subprocess.Popen(['codex', 'app-server'], cwd=root, env=dict(os.environ, RUST_LOG='info'), stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=log, text=True, encoding='utf-8')
    def reader():
        for line in process.stdout:
            try:
                messages.put(json.loads(line))
            except ValueError:
                pass
    threading.Thread(target=reader, daemon=True).start()
    def send(value):
        process.stdin.write(json.dumps(value) + '\n')
        process.stdin.flush()
    def request(identifier, method, params):
        send({'id': identifier, 'method': method, 'params': params})
        deadline = time.monotonic() + 150
        while time.monotonic() < deadline:
            message = messages.get(timeout=max(.1, deadline-time.monotonic()))
            if message.get('id') == identifier:
                if 'error' in message:
                    raise RuntimeError(message['error'])
                return message['result']
        raise TimeoutError(method)
    try:
        request(1, 'initialize', {'clientInfo': {'name': 'skillmesh-verification', 'version': '1.0'},
                                  'capabilities': {'experimentalApi': True}})
        send({'method': 'initialized'})
        details = request(2, 'plugin/read', {'pluginName': 'skillmesh', 'marketplacePath': str(Path.home()/'.agents/plugins/marketplace.json')})['plugin']
        print('Native plugin/read:', details['mcpServers'], len(details['skills']), 'skills', flush=True)
        assert 'serena' in details['mcpServers']
        # Query only this provider: enumerating every connected server may start
        # unrelated integrations and exhaust resources on a configured workstation.
        for identifier, candidate in enumerate(('serena',), 3):
            status = request(identifier, 'mcpServerStatus/list', {'serverName': candidate, 'limit': 10, 'detail': 'toolsAndAuthOnly'})
            print('Targeted native probe:', candidate, [(s.get('name'),len(s.get('tools',{}))) for s in status['data']], flush=True)
            if status['data']:
                server = status['data'][0]
                print('Tool names:', sorted(server.get('tools', {})), flush=True)
                assert set(server.get('tools', {})) == {
                    'initial_instructions', 'activate_project', 'get_current_config',
                    'get_symbols_overview', 'find_symbol', 'find_referencing_symbols', 'find_implementations'}, server
                break
        else:
            raise AssertionError('Native Serena server name unresolved')
    finally:
        process.stdin.close()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.terminate()
            process.wait(timeout=10)
