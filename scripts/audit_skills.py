#!/usr/bin/env python3
"""Lightweight audit for a directory of Codex-style skills.

This intentionally validates only the basics needed for ecosystem discovery.
It does not enforce a capability schema.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
FIELD = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    data: dict[str, str] = {}
    for line in m.group(1).splitlines():
        fm = FIELD.match(line.strip())
        if fm:
            data[fm.group(1)] = fm.group(2).strip().strip('"').strip("'")
    return data


def audit(root: pathlib.Path) -> int:
    skill_files = sorted(root.rglob("SKILL.md"))
    if not skill_files:
        print(f"No SKILL.md files found under {root}")
        return 1

    problems = 0
    rows = []
    for path in skill_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        meta = parse_frontmatter(text)
        name = meta.get("name", "")
        desc = meta.get("description", "")
        issues = []
        if not name:
            issues.append("missing name")
        if not desc:
            issues.append("missing description")
        elif len(desc) < 40:
            issues.append("description may be too vague")
        elif len(desc) > 500:
            issues.append("description may be too long for routing")
        if name and not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", name):
            issues.append("name is not a simple stable identifier")

        status = "OK" if not issues else "; ".join(issues)
        problems += bool(issues)
        rows.append((name or "(unnamed)", str(path.relative_to(root)), status))

    widths = [max(len(r[i]) for r in rows + [("Skill", "Path", "Status")]) for i in range(3)]
    header = ("Skill", "Path", "Status")
    print(" | ".join(header[i].ljust(widths[i]) for i in range(3)))
    print("-+-".join("-" * w for w in widths))
    for row in rows:
        print(" | ".join(row[i].ljust(widths[i]) for i in range(3)))

    print(f"\nFound {len(rows)} skill(s); {problems} with metadata warnings.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=pathlib.Path, help="Directory containing one or more skills")
    args = parser.parse_args()
    return audit(args.root.expanduser().resolve())


if __name__ == "__main__":
    sys.exit(main())
