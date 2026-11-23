"""Opt-in native plugin/catalog check with no chat creation or model invocation."""
import argparse
from collections import Counter
import json
import os
from pathlib import Path
import queue
import re
import subprocess
import threading
import time


ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = (Path("plugin.json"), Path(".codex-plugin/plugin.json"))
SERENA_TOOLS = {
    "initial_instructions", "activate_project", "get_current_config",
    "get_symbols_overview", "find_symbol", "find_referencing_symbols",
    "find_implementations",
}


def read_manifest(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def package_version(package):
    manifests = [read_manifest(package / path) for path in MANIFESTS]
    version = manifests[0].get("version")
    if (
        not isinstance(version, str)
        or not re.fullmatch(r"[0-9A-Za-z.+-]+", version)
        or version in {".", ".."}
        or any(m.get("name") != "skillmesh" or m.get("version") != version for m in manifests)
    ):
        raise ValueError(f"Inconsistent SkillMesh manifests in {package}")
    return version


def compare_packages(candidate, package):
    candidate_files = {p.relative_to(candidate) for p in candidate.rglob("*") if p.is_file()}
    package_files = {p.relative_to(package) for p in package.rglob("*") if p.is_file()}
    if candidate_files != package_files:
        missing = sorted(str(p) for p in candidate_files - package_files)
        extra = sorted(str(p) for p in package_files - candidate_files)
        raise ValueError(f"Package files differ in {package}: missing={missing}, extra={extra}")

    for path in sorted(candidate_files):
        expected, actual = candidate / path, package / path
        if path in MANIFESTS:
            expected_manifest, actual_manifest = read_manifest(expected), read_manifest(actual)
            # The installer rewrites the manifests as JSON and stamps the release version.
            expected_manifest.pop("version")
            actual_manifest.pop("version")
            matches = (
                json.dumps(expected_manifest, sort_keys=True)
                == json.dumps(actual_manifest, sort_keys=True)
            )
        else:
            matches = expected.read_bytes() == actual.read_bytes()
        if not matches:
            raise ValueError(f"Package content differs in {package}: {path}")


def absolute_path(value, field):
    if not isinstance(value, str) or not Path(value).is_absolute():
        raise ValueError(f"Cannot verify absolute {field}: {value!r}")
    return Path(value).resolve(strict=True)


def verify_plugin(details, candidate, marketplace, codex_home):
    """Verify the requested package, the materialized copy and the reported skill paths."""
    expected_marketplace = marketplace.resolve(strict=True)
    marketplace_name = read_manifest(expected_marketplace).get("name")
    summary = details.get("summary")
    if (
        not isinstance(marketplace_name, str)
        or not re.fullmatch(r"[A-Za-z0-9_-]+", marketplace_name)
        or details.get("marketplaceName") != marketplace_name
        or absolute_path(details.get("marketplacePath"), "marketplace path") != expected_marketplace
        or not isinstance(summary, dict)
        or summary.get("id") != f"skillmesh@{marketplace_name}"
        or summary.get("name") != "skillmesh"
        or summary.get("installed") is not True
        or summary.get("enabled") is not True
    ):
        raise ValueError("Cannot verify the enabled SkillMesh installation in the requested marketplace")

    source = summary.get("source")
    if not isinstance(source, dict) or source.get("type") != "local":
        raise ValueError("Cannot verify SkillMesh without a local marketplace source")
    published = absolute_path(source.get("path"), "marketplace source path")
    expected_version = package_version(candidate)
    published_version = package_version(published)
    release_version = expected_version.split("+", 1)[0]
    stamped_version = re.escape(release_version) + r"\+codex\.\d+"
    if published_version != expected_version and not (
        not re.fullmatch(stamped_version, expected_version)
        and re.fullmatch(stamped_version, published_version)
    ):
        raise ValueError(f"Marketplace version {published_version!r} differs from candidate {expected_version!r}")
    if summary.get("localVersion") != published_version:
        raise ValueError(
            f"Installed version {summary.get('localVersion')!r} differs from marketplace {published_version!r}"
        )

    # localVersion and codexHome identify the materialized local package even
    # when plugin/read reports marketplace paths for its catalog entries.
    cache = absolute_path(codex_home, "Codex home") / "plugins/cache" / marketplace_name / "skillmesh"
    cached_release = cache / published_version
    if not cached_release.is_dir():
        raise ValueError(f"Cannot locate the materialized SkillMesh package at {cached_release}")
    installed = cached_release.resolve(strict=True)
    if package_version(installed) != published_version:
        raise ValueError(f"Installed manifest version differs from host localVersion in {installed}")
    for package in {published, installed}:
        compare_packages(candidate, package)

    definitions = {
        path.parent.name: path.relative_to(candidate)
        for path in candidate.glob("skills/*/SKILL.md") if path.is_file()
    }
    catalog = details.get("skills")
    if not isinstance(catalog, list) or any(
        not isinstance(skill, dict) or not isinstance(skill.get("name"), str) for skill in catalog
    ):
        raise ValueError("Cannot verify the skill catalog without named entries")
    catalog_names = [skill["name"].removeprefix("skillmesh:") for skill in catalog]
    counts = Counter(catalog_names)
    if not definitions or counts != Counter(definitions.keys()):
        missing = sorted(definitions.keys() - counts.keys())
        extra = sorted(repr(name) for name in counts.keys() - definitions.keys())
        duplicate = sorted(repr(name) for name, count in counts.items() if count > 1)
        raise ValueError(f"Unexpected skill catalog: missing={missing}, extra={extra}, duplicate={duplicate}")
    for skill, name in zip(catalog, catalog_names):
        path = absolute_path(skill.get("path"), f"{name} skill path")
        if skill.get("enabled") is not True or path not in {
            package / definitions[name] for package in (published, installed)
        }:
            raise ValueError(f"Unexpected or disabled catalog entry {name!r} at {path}")
    servers = details.get("mcpServers")
    if (
        not isinstance(servers, list) or any(not isinstance(name, str) for name in servers)
        or "serena" not in servers
    ):
        raise ValueError("SkillMesh does not register Serena")
    return published_version, len(catalog)


def verify_serena(status, plugin_id):
    servers = status.get("data") if isinstance(status, dict) else None
    if (
        not isinstance(servers, list) or len(servers) != 1
        or not isinstance(servers[0], dict) or servers[0].get("name") != "serena"
        or servers[0].get("pluginId") != plugin_id or status.get("nextCursor") is not None
    ):
        raise ValueError("Native Serena registration did not uniquely resolve to SkillMesh")
    tools = servers[0].get("tools")
    if not isinstance(tools, dict) or any(
        not isinstance(tool, dict) or tool.get("name") != name or "inputSchema" not in tool
        for name, tool in tools.items()
    ):
        raise ValueError("Cannot verify Serena tools without named tool definitions")
    if tools.keys() != SERENA_TOOLS:
        raise ValueError(f"Unexpected Serena tools: {sorted(tools)}")
    return sorted(tools)


def probe(candidate, marketplace):
    messages = queue.Queue()
    log_dir = ROOT / ".validation-deps"
    log_dir.mkdir(exist_ok=True)
    with (log_dir / "host-probe.log").open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            ["codex", "app-server"], cwd=ROOT, env=dict(os.environ, RUST_LOG="info"),
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=log, text=True, encoding="utf-8",
        )

        def reader():
            for line in process.stdout:
                try:
                    messages.put(json.loads(line))
                except ValueError:
                    pass
            messages.put(None)

        def send(value):
            process.stdin.write(json.dumps(value) + "\n")
            process.stdin.flush()

        def request(identifier, method, params):
            send({"id": identifier, "method": method, "params": params})
            deadline = time.monotonic() + 150
            while time.monotonic() < deadline:
                try:
                    message = messages.get(timeout=max(0, deadline - time.monotonic()))
                except queue.Empty:
                    raise TimeoutError(f"Timed out waiting for {method}") from None
                if message is None:
                    raise RuntimeError(f"App server stopped during {method}. See {log.name}")
                if message.get("id") == identifier:
                    if "error" in message:
                        raise RuntimeError(message["error"])
                    return message["result"]
            raise TimeoutError(f"Timed out waiting for {method}")

        threading.Thread(target=reader, daemon=True).start()
        try:
            host = request(1, "initialize", {
                "clientInfo": {"name": "skillmesh-verification", "version": "1.0"},
                "capabilities": {"experimentalApi": True},
            })
            send({"method": "initialized"})
            details = request(2, "plugin/read", {
                "pluginName": "skillmesh", "marketplacePath": str(marketplace),
            })["plugin"]
            version, count = verify_plugin(details, candidate, marketplace, host.get("codexHome"))
            print(f"Native plugin/read verified SkillMesh {version} with {count} skills", flush=True)

            # A broad listing can start unrelated integrations.
            status = request(3, "mcpServerStatus/list", {
                "serverName": "serena", "limit": 10, "detail": "toolsAndAuthOnly",
            })
            tools = verify_serena(status, details["summary"]["id"])
            print("Native Serena tools:", ", ".join(tools), flush=True)
        finally:
            process.stdin.close()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.terminate()
                process.wait(timeout=10)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, default=ROOT / "skillmesh")
    parser.add_argument("--marketplace", type=Path, default=Path.home() / ".agents/plugins/marketplace.json")
    args = parser.parse_args()
    try:
        probe(args.candidate.resolve(strict=True), args.marketplace.resolve(strict=True))
    except (OSError, RuntimeError, ValueError) as error:
        parser.exit(1, f"SkillMesh host probe failed: {error}\n")


if __name__ == "__main__":
    main()
