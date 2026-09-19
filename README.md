# Codex Skill Ecosystem v1

A deliberately small ecosystem layer for independently maintained Codex skills.

## Goal

Help Codex discover, select, combine, reassess, and stop using skills intelligently without introducing a custom orchestration runtime.

## Design rules

1. Skills remain independent and directly usable.
2. Codex owns orchestration. Skills do not invoke other skills autonomously.
3. Skill descriptions are the primary routing surface.
4. Global instructions define ecosystem behaviour.
5. Natural-language handoffs come before machine-readable dependency graphs.
6. Add state, registries, or a runtime only when evals demonstrate a concrete failure.
7. Every additional abstraction must solve an observed problem.

## Suggested installation

Keep each skill in its own repository. Expose them through Codex's supported user-level skill discovery mechanism for your environment. If symlinks are supported in your setup, prefer links over copying repositories.

Copy or merge `AGENTS.md` into your global Codex instruction layer.

Install `orchestrator-skill/` alongside the other skills only if you find it useful. It is intentionally advisory: it helps Codex choose skills but does not implement a separate router.

## Skill metadata convention

Existing skills do not need a schema migration. Improve the front of each `SKILL.md` so it clearly answers:

- What does this skill do?
- When should it be used?
- When should it not be used?
- What does it usually produce?
- What limitations should be surfaced rather than guessed through?

Optionally use the template in `templates/SKILL_TEMPLATE.md`.

## Evaluation-first evolution

Run representative tasks from `evals/` before and after ecosystem changes.

Evaluate:

- discovery recall
- selection precision
- composition quality
- reassessment quality
- stopping behaviour
- contradiction handling
- synthesis quality
- human corrections required
- context/token overhead

Only introduce the next architectural layer if a repeated failure justifies it.

## Maturity ladder

### Level 0 — Independent skills
No ecosystem behaviour.

### Level 1 — Discovery
Good names, descriptions, and global availability.

### Level 2 — Lightweight ecosystem
Global instructions, optional orchestration skill, collaboration conventions, evals.

**This repository implements Level 2.**

### Level 3 — Structured handoffs
Add a compact findings/evidence/assumptions/open-questions convention only if natural handoffs fail.

### Level 4 — Shared task state
Add curated state only if longer tasks lose decisions/evidence or develop contradictions.

### Level 5 — Capability registry
Add abstract capabilities/providers only if routing becomes unreliable at scale or multiple skills provide similar capabilities.

### Level 6 — Dynamic orchestration runtime
Only if model-driven orchestration is demonstrably insufficient.

## Non-goals for v1

- no capability ontology
- no dependency graph
- no state machine
- no message bus
- no multi-agent swarm
- no confidence scoring framework
- no mandatory shared storage
- no custom runtime
