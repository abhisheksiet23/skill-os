---
name: app-analyze
description: Clarify, challenge and review software requirements, recover relevant existing behavior, and define use cases and behavioral contracts before implementation. Use for material product changes, ambiguous defects, modernization analysis or standalone requirements review; skip mechanical fixes, technical architecture review and business-demand validation.
---

# App Analyze

Produce a requirements contract that implementers and verifiers can use without guessing consequential behavior. Separate the requested solution, underlying problem and desired outcome; challenge unsupported choices, then preserve the owner's decision. This skill analyzes requirements; it does not implement production code. A review reports gaps without editing the contract unless authorized.

## Establish the boundary

Recover project instructions, accepted decisions and adequate existing contracts before rediscovering requirements. Identify affected actors, entry points and the next useful outcome. Trace a defect's path; for broad work, map the major capabilities and dependencies shallowly, then detail the next coherent increment. Settle scope or compatibility choices that could invalidate the investigation. Keep deferred capabilities visible without specifying their future internals.

Recover consequential existing behavior with [existing-system evidence](references/existing-systems.md); inspect the affected rules using the [requirements lenses](references/requirements.md). Load only the relevant material. Reuse source/revision-bound evidence while it remains applicable; distinguish observed behavior from intended behavior, inference and implementation drift. An existing defect is not automatically a compatibility obligation.

## Resolve consequential uncertainty

Investigate before asking. Deepen only where evidence could change the increment or protect affected behavior. Recover the actor/data scope, transitions, exceptions, external effects and quality constraints needed for that decision.

Ask when missing evidence or an owner preference changes useful work or could cause substantial rework. Give the recommended boundary, its consequence and the exact work affected. Resolve reversible details within delegation; defer unrelated questions with a revisit condition and continue independent work. Preserve disagreement until its assumptions, evidence or scope can be reconciled. Demand, interaction or architecture gaps may need other expertise; explain the gap. These are optional recommendations to the agent, never skill invocations or a mandatory sequence.

A worthwhile discovery can remain open beyond the current increment. Check readily available evidence within scope; if future value justifies retaining it, preserve the observation/source, tentative interpretation and useful question in existing product records, separate from accepted scope. Continue the settled path without requiring an answer or adding a speculative feature. Keep required correctness evidence as a dependency; do not turn every curiosity into retained work or claim a possible benefit as fact.

## Compile the contract

Reconstruct the behavior from the evidence instead of accumulating notes or copying a discovery checklist. Give every distinct rule, qualification and decision one authoritative home in the project's existing records. Keep its source and confirmed/proposed/assumed standing attached; keep verification claims separate from required future proof.

- State actor/trigger, intended outcome and the increment's scope boundary once.
- Describe the shortest complete path to that outcome and its consequential alternatives, including necessary UX, API, data, authorization and deployment boundaries. Use a bulleted flow when sequence matters, condition/result rows for independent rules, and tables for genuine variants. Factor common constraints instead of repeating them in every case.
- Compile behavior and acceptance together. A rule with its starting conditions and observable result already defines acceptance: do not restate it in a separate acceptance section. Cover the selected end-to-end paths and consequential exceptions once. Add only a missing discriminating input, fixture, oracle or proof method; supplied precise conditions need no invented examples. Keep executed evidence and its limits distinct from these required outcomes.
- Keep unresolved choices beside the work they block. Record future dependencies only to the depth needed to explain the boundary. Preserve exact limitations; do not invent policies, schemas, thresholds or integration guarantees.

Start with an outline; expand only the parts whose ambiguity, consequences or unavailable expert clarification require more detail. Do not manufacture IDs, headings, documents or examples. Concision must preserve distinct facts and useful rationale; neither a word cap nor moving repetition to references is an optimization.

## Check and hand over

Keep one current contract, updating material decisions without silently replacing accepted intent with implementation. Reopen settled choices only for changed scope or relevant new evidence. Remove semantic repetition across scope, behavior, acceptance and exclusions; retain details that change interpretation.

For a consequential handoff, check that a reader can recover the current/target distinction, rules, dependencies and acceptance without the authoring conversation. A reader's restatement can expose a different interpretation; resolve it in the contract. Self-review is not independent review, and routine corrections need no separate reviewer.

Finish when the next increment is implementable and verifiable without consequential guesses. Preserve the release boundary, accepted choices, applicable evidence and precise gaps for continuation. If blocked, name the work blocked and complete independent analysis; do not claim unexecuted checks or an unproved boundary as complete.
