#!/usr/bin/env python3
"""Offline packaging checks, not a router or a behavioral grader (stdlib only)."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


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
    errors: list[str] = []
    rows: list[dict] = []
    try:
        manifest = json.loads((plugin / ".codex-plugin/plugin.json").read_text(encoding="utf-8-sig"))
        if manifest.get("name") != plugin.name:
            errors.append("plugin folder and manifest name differ")
        if manifest.get("skills") != "./skills/":
            errors.append("this package must expose ./skills/")
    except (OSError, ValueError) as exc:
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
    parser.add_argument("plugin", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "skillmesh")
    args = parser.parse_args()
    errors, rows = validate(args.plugin)
    for row in rows:
        print(f"{row['name']}: {row['words']} entrypoint words")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"{len(rows)} skills; {len(errors)} packaging errors. Behavior is evaluated separately.")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
