#!/usr/bin/env python3
"""Cheap structure view of a markdown, JSON or JSONL file so an agent can read only what it needs.

  python outline.py FILE                       outline (headings with line ranges / key sizes)
  python outline.py FILE.md --section TEXT     print the first section whose heading contains TEXT (case-insensitive)
  python outline.py FILE.json --path a.b.0     print the value at a dotted path, truncated to --max-chars
  python outline.py FILE.jsonl --path 3.key    JSONL: first path part is the zero-based line number

Read-only, standard library only. Output is intentionally compact; it never prints a whole large file.
"""
import argparse, json, re, sys
from pathlib import Path

HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")


def md_sections(lines):
    sections, in_fence = [], False
    for i, line in enumerate(lines, 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        m = None if in_fence else HEADING.match(line)
        if m:
            sections.append({"level": len(m.group(1)), "title": m.group(2), "start": i})
    for n, s in enumerate(sections):
        end = len(lines)
        for t in sections[n + 1:]:
            if t["level"] <= s["level"]:
                end = t["start"] - 1
                break
        s["end"] = end
        s["chars"] = sum(len(x) + 1 for x in lines[s["start"] - 1:end])
    return sections


def human(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)


def md_outline(path, lines):
    secs = md_sections(lines)
    total = sum(len(x) + 1 for x in lines)
    print(f"{path.name}: {len(lines)} lines, {human(total)} chars, {len(secs)} headings")
    first = secs[0]["start"] if secs else len(lines) + 1
    if first > 1:
        print(f"  L1-{first - 1} (preamble)")
    for s in secs:
        print(f"{'  ' * s['level']}L{s['start']}-{s['end']} ({human(s['chars'])}) {'#' * s['level']} {s['title'][:80]}")


def md_section(path, lines, text):
    secs = md_sections(lines)
    hit = next((s for s in secs if text.lower() in s["title"].lower()), None)
    if not hit:
        sys.exit(f"no heading containing {text!r}; run without --section to list headings")
    print(f"[{path.name} L{hit['start']}-{hit['end']}]")
    print("\n".join(lines[hit["start"] - 1:hit["end"]]))


def describe(v, depth, max_depth, indent):
    pad = "  " * indent
    if isinstance(v, dict):
        for k, x in list(v.items())[:40]:
            size = len(json.dumps(x, ensure_ascii=False))
            kind = type(x).__name__
            if isinstance(x, (list, dict)):
                print(f"{pad}{k}: {kind}, {len(x)} items, {human(size)} chars")
            elif size <= 40:
                print(f"{pad}{k}: {json.dumps(x, ensure_ascii=False)}")
            else:
                print(f"{pad}{k}: {kind}, {human(size)} chars")
            if depth < max_depth and isinstance(x, (dict, list)):
                describe(x, depth + 1, max_depth, indent + 1)
        if len(v) > 40:
            print(f"{pad}... {len(v) - 40} more keys")
    elif isinstance(v, list) and v:
        first = v[0]
        print(f"{pad}[0] of {len(v)}: {type(first).__name__}")
        if isinstance(first, (dict, list)) and depth < max_depth:
            describe(first, depth + 1, max_depth, indent + 1)


def walk(v, path):
    for part in [p for p in path.split(".") if p != ""]:
        if isinstance(v, list):
            v = v[int(part)]
        elif isinstance(v, dict):
            v = v[part]
        else:
            sys.exit(f"cannot descend into {type(v).__name__} at {part!r}")
    return v


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--section")
    ap.add_argument("--path")
    ap.add_argument("--max-chars", type=int, default=4000)
    ap.add_argument("--depth", type=int, default=2)
    a = ap.parse_args()
    path = Path(a.file)
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    ext = path.suffix.lower()

    if ext in (".md", ".markdown"):
        lines = text.splitlines()
        return md_section(path, lines, a.section) if a.section else md_outline(path, lines)

    if ext == ".jsonl":
        recs = [l for l in text.splitlines() if l.strip()]
        if a.path is not None:
            first, _, rest = a.path.partition(".")
            val = walk(json.loads(recs[int(first)]), rest)
            out = json.dumps(val, ensure_ascii=False, indent=1)
            print(out[: a.max_chars] + ("\n...[truncated]" if len(out) > a.max_chars else ""))
            return
        print(f"{path.name}: {len(recs)} records, {human(len(text))} chars")
        try:
            describe(json.loads(recs[0]), 1, a.depth, 1)
        except (ValueError, IndexError):
            print("  (first record is not JSON)")
        return

    if ext == ".json":
        data = json.loads(text)
        if a.path is not None:
            out = json.dumps(walk(data, a.path), ensure_ascii=False, indent=1)
            print(out[: a.max_chars] + ("\n...[truncated]" if len(out) > a.max_chars else ""))
            return
        print(f"{path.name}: {type(data).__name__}, {human(len(text))} chars")
        describe(data, 1, a.depth, 1)
        return

    sys.exit(f"unsupported file type {ext!r}; use sed/Get-Content ranges for other files")


if __name__ == "__main__":
    main()
