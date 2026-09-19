# Architecture Escalation Triggers

Do not move up the maturity ladder without repeated evidence.

## Add structured handoffs when

Repeated runs show that specialist results are difficult to reuse because key findings, assumptions, evidence gaps, or artifacts are lost in prose.

Start with a small convention, for example:

- findings
- evidence
- assumptions
- open questions
- artifacts

Avoid a mandatory schema until needed.

## Add shared task state when

Repeated long-running tasks show one or more of:

- explicit user decisions are forgotten;
- assumptions mutate into facts;
- multiple specialists create inconsistent context;
- important evidence gets lost between phases;
- the task spans sessions or artifacts and conversation context is insufficient.

If added, keep state curated. Detailed work remains in artifacts.

## Add a capability registry when

Repeated routing failures occur because:

- there are many skills;
- several skills provide similar expertise;
- names/descriptions no longer reliably distinguish providers;
- implementations need to be replaced without changing callers.

Until then, semantic model routing is simpler.

## Add a dynamic runtime when

Model-driven orchestration repeatedly fails even after metadata, instructions, handoffs, and state are improved.

A runtime should solve concrete failures such as deterministic prerequisite enforcement, durable multi-step jobs, concurrency control, or provider selection at large scale.
