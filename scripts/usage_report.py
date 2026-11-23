#!/usr/bin/env python3
"""Summarize Claude Code usage from local session transcripts for skill-os planning.

Reads ~/.claude/projects/*/*.jsonl, writes one metadata record per session to
.use-tracking/sessions.jsonl (upsert by session_id, so records survive transcript
pruning), and prints a summary. Local only; no network.

Captured: project basename, UTC interval, models, token counts, tool-call counts,
tool-error count, skill names invoked (with timestamp), subagent spawns.
Never captured: prompt text, assistant text, skill arguments, tool inputs/outputs, paths.

Usage: python scripts/usage_report.py [--projects-dir DIR] [--out DIR] [--since YYYY-MM-DD] [--no-write]
"""
import argparse, json, os, re, sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

TOKEN_KEYS = ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")


def parse_session(path):
    s = {"source": "claude", "session_id": path.stem, "project": None, "started_utc": None, "ended_utc": None,
         "models": Counter(), "tokens": Counter(), "assistant_turns": 0, "user_turns": 0,
         "tools": Counter(), "tool_errors": 0, "skills": [], "subagents": 0, "entrypoint": None}
    seen_msgs = set()
    skill_ids = {}
    with path.open(encoding="utf8", errors="replace") as f:
        for line in f:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            ts = d.get("timestamp")
            if ts:
                s["started_utc"] = min(filter(None, [s["started_utc"], ts]))
                s["ended_utc"] = max(filter(None, [s["ended_utc"], ts]))
            if d.get("cwd") and not s["project"]:
                s["project"] = Path(d["cwd"].replace("\\", "/")).name
            if d.get("entrypoint") and not s["entrypoint"]:
                s["entrypoint"] = d["entrypoint"]
            t = d.get("type")
            msg = d.get("message") or {}
            content = msg.get("content")
            if t == "assistant":
                mid = msg.get("id") or d.get("uuid")
                if mid in seen_msgs and not isinstance(content, list):
                    continue
                first = mid not in seen_msgs
                seen_msgs.add(mid)
                if first:
                    s["assistant_turns"] += 1
                    s["models"][msg.get("model") or "unknown"] += 1
                    u = msg.get("usage") or {}
                    for k in TOKEN_KEYS:
                        s["tokens"][k] += u.get(k) or 0
                for b in content if isinstance(content, list) else []:
                    if b.get("type") != "tool_use":
                        continue
                    name = b.get("name", "unknown")
                    s["tools"][name] += 1
                    if name == "Skill":
                        sk = (b.get("input") or {}).get("skill", "unknown")
                        s["skills"].append({"skill": sk, "at": ts})
                    elif name in ("Agent", "Task"):
                        s["subagents"] += 1
            elif t == "user":
                if isinstance(content, list):
                    for b in content:
                        if b.get("type") == "tool_result" and b.get("is_error"):
                            s["tool_errors"] += 1
                elif isinstance(content, str) and not d.get("isMeta"):
                    s["user_turns"] += 1
    if not s["assistant_turns"]:
        return None
    s["models"] = dict(s["models"])
    s["tokens"] = dict(s["tokens"])
    s["tools"] = dict(s["tools"])
    return s


SERENA_RE = re.compile(r"serena__(\w+)")
SKILL_READ_RE = re.compile(r"skills[/\\]+([\w.-]+)[/\\]+SKILL\.md")


def parse_codex_session(path):
    """One Codex rollout file -> session record. Tokens are the final cumulative totals."""
    s = {"source": "codex", "session_id": None, "project": None, "started_utc": None, "ended_utc": None,
         "models": {}, "tokens": {}, "model_calls": 0, "peak_context_tokens": 0, "context_window": None,
         "assistant_turns": 0, "user_turns": 0, "tools": Counter(), "tool_errors": 0, "skills": [],
         "subagents": 0, "serena": Counter(), "rate_limit": {}, "entrypoint": "codex"}
    best_total = -1
    prim = []
    sec = []
    with path.open(encoding="utf8", errors="replace") as f:
        for line in f:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            ts = d.get("timestamp")
            if ts:
                s["started_utc"] = min(filter(None, [s["started_utc"], ts]))
                s["ended_utc"] = max(filter(None, [s["ended_utc"], ts]))
            t, p = d.get("type"), d.get("payload") or {}
            pt = p.get("type")
            if t == "session_meta":
                s["session_id"] = p.get("id") or p.get("session_id")
                if p.get("cwd"):
                    s["project"] = Path(p["cwd"].replace("\\", "/")).name
            elif t == "token_usage_record":
                s["model_calls"] += 1
            elif t == "event_msg" and pt == "token_count":
                info = p.get("info") or {}
                tot = info.get("total_token_usage") or {}
                if tot.get("total_tokens", 0) > best_total:
                    best_total = tot.get("total_tokens", 0)
                    s["tokens"] = {k: v for k, v in tot.items() if isinstance(v, int)}
                last = info.get("last_token_usage") or {}
                s["peak_context_tokens"] = max(s["peak_context_tokens"], last.get("input_tokens", 0))
                s["context_window"] = info.get("model_context_window") or s["context_window"]
                rl = p.get("rate_limits") or {}
                if (rl.get("primary") or {}).get("used_percent") is not None:
                    prim.append(rl["primary"]["used_percent"])
                if (rl.get("secondary") or {}).get("used_percent") is not None:
                    sec.append(rl["secondary"]["used_percent"])
            elif t == "event_msg" and pt == "task_started":
                s["user_turns"] += 1
            elif t == "event_msg" and pt == "task_complete":
                s["assistant_turns"] += 1
            elif t == "turn_context" and p.get("model"):
                s["models"][p["model"]] = s["models"].get(p["model"], 0) + 1
            elif t == "response_item" and pt in ("custom_tool_call", "function_call"):
                name = p.get("name", "unknown")
                s["tools"][name] += 1
                text = p.get("input") or p.get("arguments") or ""
                if not isinstance(text, str):
                    text = json.dumps(text)
                if name == "spawn_agent":
                    s["subagents"] += 1
                for m in SERENA_RE.findall(text):
                    s["serena"][m] += 1
                for m in set(SKILL_READ_RE.findall(text)):
                    s["skills"].append({"skill": m, "at": ts})
    if not s["session_id"] or not s["model_calls"]:
        return None
    if prim:
        s["rate_limit"] = {"primary_start_pct": prim[0], "primary_end_pct": prim[-1],
                           "weekly_start_pct": sec[0] if sec else None, "weekly_end_pct": sec[-1] if sec else None}
    for k in ("tools", "serena"):
        s[k] = dict(s[k])
    return s


def minutes(r):
    try:
        a = datetime.fromisoformat(r["started_utc"].replace("Z", "+00:00"))
        b = datetime.fromisoformat(r["ended_utc"].replace("Z", "+00:00"))
        return (b - a).total_seconds() / 60
    except (TypeError, ValueError, KeyError):
        return 0.0


def codex_report(rows):
    if not rows:
        print("\nCodex: no sessions")
        return
    print(f"\nCodex sessions: {len(rows)}")
    print("\nTop 10 by total tokens (M = million):")
    print(f"{'session':10} {'project':20} {'min':>5} {'calls':>6} {'tokM':>7} {'cached%':>8} {'peakCtxK':>9} {'subag':>5} {'serena':>6} {'5h% used':>9}")
    for r in sorted(rows, key=lambda r: -r["tokens"].get("total_tokens", 0))[:10]:
        t = r["tokens"]
        inp = t.get("input_tokens", 0) or 1
        rl = r.get("rate_limit") or {}
        d = (rl.get("primary_end_pct", 0) or 0) - (rl.get("primary_start_pct", 0) or 0)
        print(f"{r['session_id'][:8]:10} {(r['project'] or '?')[:20]:20} {minutes(r):5.0f} {r['model_calls']:6} "
              f"{t.get('total_tokens', 0)/1e6:7.2f} {100*t.get('cached_input_tokens', 0)/inp:8.0f} "
              f"{r['peak_context_tokens']//1000:9} {r['subagents']:5} {sum(r['serena'].values()):6} {d:+9.0f}")
    calls = sum(r["model_calls"] for r in rows)
    tot = sum(r["tokens"].get("total_tokens", 0) for r in rows)
    print(f"\nAvg tokens per model call: {tot // max(calls, 1):,} (each call resends the running context)")
    ser = Counter()
    for r in rows:
        ser.update(r["serena"])
    if ser:
        print("Serena calls by tool:", dict(ser.most_common()))
    else:
        print("Serena calls: none")
    with_s = [r for r in rows if r["serena"]]
    without = [r for r in rows if not r["serena"]]
    for label, grp in (("with Serena", with_s), ("without Serena", without)):
        if grp:
            ct = sum(r["model_calls"] for r in grp)
            print(f"  {label}: {len(grp)} sessions, avg {sum(r['tokens'].get('total_tokens', 0) for r in grp)/len(grp)/1e6:.2f}M tokens/session, "
                  f"{sum(r['tokens'].get('total_tokens', 0) for r in grp)//max(ct, 1):,} tokens/call (not matched for task size)")
    print("Rate-limit % is account-wide, so a session's delta can include other concurrent use.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--codex-dir", default=str(Path.home() / ".codex" / "sessions"))
    ap.add_argument("--projects-dir", default=str(Path.home() / ".claude" / "projects"))
    ap.add_argument("--out", default=".use-tracking")
    ap.add_argument("--since", default="")
    ap.add_argument("--no-write", action="store_true")
    ap.add_argument("--compare", nargs=2, metavar=("A", "B"), help="session ID prefixes to compare side by side")
    a = ap.parse_args()

    out_file = Path(a.out) / "sessions.jsonl"
    store = {}
    if out_file.exists():
        for line in out_file.read_text(encoding="utf8").splitlines():
            try:
                r = json.loads(line)
                store[r["session_id"]] = r
            except (ValueError, KeyError):
                pass

    for p in Path(a.projects_dir).glob("*/*.jsonl"):
        r = parse_session(p)
        if r:
            store[r["session_id"]] = r
    for p in Path(a.codex_dir).glob("**/rollout-*.jsonl"):
        r = parse_codex_session(p)
        if r:
            store[r["session_id"]] = r

    if not a.no_write:
        Path(a.out).mkdir(exist_ok=True)
        with out_file.open("w", encoding="utf8") as f:
            for r in sorted(store.values(), key=lambda r: r["started_utc"] or ""):
                f.write(json.dumps(r, separators=(",", ":")) + "\n")

    if a.compare:
        pick = []
        for pre in a.compare:
            m = [r for r in store.values() if r["session_id"].startswith(pre)]
            if len(m) != 1:
                sys.exit(f"{pre!r} matches {len(m)} sessions")
            pick.append(m[0])
        print(f"{'':26}{'A':>14}{'B':>14}")
        def row(label, f):
            print(f"{label:26}{f(pick[0]):>14}{f(pick[1]):>14}")
        row("session", lambda r: r["session_id"][:8])
        row("serena calls", lambda r: sum(r.get("serena", {}).values()))
        row("model calls", lambda r: r.get("model_calls", r["assistant_turns"]))
        row("total tokens", lambda r: f"{r['tokens'].get('total_tokens', 0):,}")
        row("peak context tokens", lambda r: f"{r.get('peak_context_tokens', 0):,}")
        row("minutes", lambda r: f"{minutes(r):.1f}")
        row("tool calls", lambda r: sum(r["tools"].values()))
        row("tool errors", lambda r: r["tool_errors"])
        row("5h limit used (pts)", lambda r: f"{(r.get('rate_limit') or {}).get('primary_end_pct', 0) - (r.get('rate_limit') or {}).get('primary_start_pct', 0):+.0f}")
        return
    allrows = [r for r in store.values() if (r["started_utc"] or "") >= a.since]
    rows = [r for r in allrows if r.get("source", "claude") == "claude"]
    codex_rows = [r for r in allrows if r.get("source") == "codex"]
    print("== Claude Code ==")
    print(f"Sessions: {len(rows)}  ({min((r['started_utc'] or '' for r in rows), default='-')[:10]} .. "
          f"{max((r['ended_utc'] or '' for r in rows), default='-')[:10]})")

    by_proj = defaultdict(Counter)
    for r in rows:
        c = by_proj[r["project"] or "unknown"]
        c["sessions"] += 1
        c["turns"] += r["assistant_turns"]
        c["errors"] += r["tool_errors"]
        c["skills"] += len(r["skills"])
        for k, v in r["tokens"].items():
            c[k] += v
    print("\nBy project (tokens in thousands):")
    print(f"{'project':32} {'sess':>5} {'turns':>6} {'in':>8} {'out':>8} {'cacheR':>9} {'cacheW':>9} {'errs':>5} {'skills':>6}")
    for p, c in sorted(by_proj.items(), key=lambda kv: -kv[1]["output_tokens"]):
        print(f"{p[:32]:32} {c['sessions']:5} {c['turns']:6} {c['input_tokens']//1000:8} {c['output_tokens']//1000:8} "
              f"{c['cache_read_input_tokens']//1000:9} {c['cache_creation_input_tokens']//1000:9} {c['errors']:5} {c['skills']:6}")

    sk = Counter(); sk_proj = defaultdict(set)
    for r in rows:
        for x in r["skills"]:
            sk[x["skill"]] += 1; sk_proj[x["skill"]].add(r["project"])
    print("\nSkill invocations:")
    for k, v in sk.most_common():
        print(f"  {v:4}  {k}  ({len(sk_proj[k])} project{'s' if len(sk_proj[k]) != 1 else ''})")
    if not sk:
        print("  none recorded")

    # Skills with no recorded use are planning candidates; names come from the repo.
    repo = Path(__file__).resolve().parent.parent / "skillmesh" / "skills"
    if repo.is_dir():
        used = {k.split(":")[-1] for k in sk}
        unused = sorted(d.name for d in repo.iterdir() if d.is_dir() and d.name not in used)
        print(f"\nskillmesh skills with no recorded invocation ({len(unused)}): {', '.join(unused)}")

    models = Counter()
    for r in rows:
        models.update(r["models"])
    print("\nAssistant turns by model:", dict(models.most_common()))
    print("\n== Codex ==")
    codex_report(codex_rows)
    print(f"\nRecords: {out_file if not a.no_write else '(not written)'}")


if __name__ == "__main__":
    sys.exit(main())
