#!/usr/bin/env python3
"""Offline packaging and repository conflict checks, not a behavioral grader."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


CONFLICT_MARKER = re.compile(rb"(?:<{7,}|\|{7,}|>{7,})(?:[ \t].*)?|={7,}[ \t]*")


def conflict_markers(paths: list[Path]) -> list[str]:
    """Detect complete Git marker lines, including diff3 ancestors and orphan markers."""
    errors = []
    for path in sorted(set(paths)):
        if path.is_symlink() or not path.is_file():
            continue
        content = path.read_bytes().removeprefix(b"\xef\xbb\xbf")
        if b"\0" in content:
            continue  # Binary files are outside this text check.
        for number, line in enumerate(content.splitlines(), 1):
            if CONFLICT_MARKER.fullmatch(line):
                errors.append(f"{path}:{number}: unresolved conflict marker")
    return errors


def repository_conflicts(root: Path) -> list[str]:
    """Use Git's file inventory so ignored local records and generated runs stay local."""
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            check=True, capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        return [f"repository conflict scan unavailable: {exc}"]
    paths = [root / name.decode("utf-8", errors="surrogateescape")
             for name in result.stdout.split(b"\0") if name]
    return conflict_markers(paths)


def metadata(path: Path) -> dict[str, str]:
    """Read this library's deliberately flat name/description frontmatter."""
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        raise ValueError("missing frontmatter")
    result = {}
    for line in match[1].splitlines():
        key, sep, value = line.partition(":")
        if not sep or key not in ("name", "description") or key in result:
            raise ValueError("expected one flat name and description; use the official validator for general YAML")
        value = value.strip()
        if not value or value in ("|", ">"):
            raise ValueError(f"empty or multiline {key}")
        result[key] = value
    if set(result) != {"name", "description"}:
        raise ValueError("name and description are required")
    return result


def validate(plugin: Path) -> tuple[list[str], list[dict]]:
    plugin = plugin.resolve()
    errors = conflict_markers(list(plugin.rglob("*")))
    rows: list[dict] = []
    try:
        manifest = json.loads((plugin / ".codex-plugin/plugin.json").read_text(encoding="utf-8-sig"))
        if manifest.get("name") != plugin.name:
            errors.append("plugin folder and manifest name differ")
        if manifest.get("skills") != "./skills/":
            errors.append("this package must expose ./skills/")
        target = manifest.get("mcpServers")
        if (plugin / "plugin.json").is_file():
            portable = json.loads((plugin / "plugin.json").read_text(encoding="utf-8-sig"))
            if portable.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
                errors.append("portable plugin schema is missing or unsupported")
            for key in ("name", "version", "description", "author"):
                if portable.get(key) != manifest.get(key):
                    errors.append(f"portable and compatibility manifest {key} differ")
            if portable.get("extensions", {}).get("com.openai", {}).get("interface") != manifest.get("interface"):
                errors.append("portable and compatibility presentation differ")
            if (plugin / "mcp.json").is_file():
                target = "./mcp.json"
        if target is not None:
            if not isinstance(target, str):
                raise ValueError("mcpServers must reference a packaged JSON file")
            mcp_path = (plugin / target).resolve()
            if not mcp_path.is_relative_to(plugin):
                raise ValueError("MCP definition must stay inside the plugin")
            servers = json.loads(mcp_path.read_text(encoding="utf-8-sig"))["mcpServers"]
            if not isinstance(servers, dict) or not servers:
                raise ValueError("MCP definition must contain servers")
            for server in servers.values():
                if not server.get("command") or not isinstance(server.get("args", []), list):
                    raise ValueError("local MCP server requires a command and argument list")
                for argument in server.get("args", []):
                    if not isinstance(argument, str):
                        raise ValueError("MCP arguments must be strings")
                    root_prefix = next((prefix for prefix in ("${PLUGIN_ROOT}/", "${CLAUDE_PLUGIN_ROOT}/")
                                        if argument.startswith(prefix)), None)
                    if root_prefix:
                        asset = (plugin / argument[len(root_prefix):]).resolve()
                        if not asset.is_relative_to(plugin) or not asset.is_file():
                            raise ValueError("missing or escaping MCP asset")
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f"manifest: {exc}")
    skill_root = plugin / "skills"
    folders = sorted(p for p in skill_root.iterdir() if p.is_dir()) if skill_root.is_dir() else []
    if not folders:
        errors.append("no skills found")
    names = set()
    for folder in folders:
        entry = folder / "SKILL.md"
        try:
            meta = metadata(entry)
            name = meta["name"]
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                errors.append(f"{folder.name}: invalid name")
            if name != folder.name or name in names:
                errors.append(f"{folder.name}: duplicate or mismatched name")
            names.add(name)
            if len(meta["description"]) > 1024:
                errors.append(f"{name}: description exceeds native limit")
            rows.append({"name": name, "description": meta["description"], "words": len(entry.read_text(encoding="utf-8-sig").split())})
        except (OSError, ValueError) as exc:
            errors.append(f"{folder.name}: {exc}")
        for path in folder.rglob("*"):
            if path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction()):
                errors.append(f"{path}: linked resources are not portable")
            if path.suffix != ".md" or not path.is_file():
                continue
            text = path.read_text(encoding="utf-8-sig")
            if "[TODO:" in text:
                errors.append(f"{path}: unfinished placeholder")
            # Inline Markdown links in authored files; not a universal Markdown parser.
            for target in re.findall(r"\]\(([^)]+)\)", text):
                url = urlsplit(target.strip("<>"))
                if url.scheme or not url.path:
                    continue
                resolved = (path.parent / unquote(url.path)).resolve()
                if not resolved.is_relative_to(folder.resolve()):
                    errors.append(f"{path}: nonlocal required reference {target}")
                elif not resolved.is_file():
                    errors.append(f"{path}: missing reference {target}")
    return errors, rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin", nargs="?", type=Path,
                        help="Validate only this package; omit to also scan repository source for conflicts")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors, rows = validate(args.plugin if args.plugin is not None else root / "skillmesh")
    if args.plugin is None:
        errors = list(dict.fromkeys(errors + repository_conflicts(root)))
    for row in rows:
        print(f"{row['name']}: {row['words']} entrypoint words")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"{len(rows)} skills; {len(errors)} validation errors. Behavior is evaluated separately.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
