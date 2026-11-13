---
name: app-analyze
description: Analyze software needs and existing behavior, producing separate business-analysis findings and a use-case specification with flows, rules, acceptance and gaps. Use for material product changes, ambiguous defects, modernization or requirements review; skip mechanical fixes, technical architecture design/review and business-demand validation.
---

# App Analyze

Produce two distinct artifacts: **analysis findings** explaining the need, evidence and unresolved choices, and a **use-case specification** defining observable behavior for design, implementation and verification. Separate the requested solution, underlying problem and desired outcome; challenge unsupported choices, then preserve the owner's decision. Architecture and technical mechanism choices belong in a separate design, outside this skill; record the required guarantee and the design question without choosing its mechanism. Do not implement production code.

For analysis-and-specification work, deliver both artifacts separately and link them, using adequate existing project records where possible. Default to two Markdown documents in the application project, not one blended analysis report. An explicit analysis-only request delivers findings; a specification-only request uses adequate existing analysis; review-only work reports findings without editing the reviewed records. A contained correction can use brief linked records rather than a full module dossier. Do not force a prior skill invocation or duplicate adequate artifacts.

## Establish the boundary

Recover project instructions, accepted decisions and adequate existing contracts before rediscovering requirements. Identify affected actors, entry points and the next useful outcome. Trace a defect's path; for broad work, map the major capabilities and dependencies shallowly, then detail the next coherent increment. Settle scope or compatibility choices that could invalidate the investigation. Keep deferred capabilities visible without specifying their future internals.

Recover consequential existing behavior with [existing-system evidence](references/existing-systems.md); inspect the affected rules using the [requirements lenses](references/requirements.md). Load only the relevant material. Reuse source/revision-bound evidence while it remains applicable; distinguish observed behavior from intended behavior, inference and implementation drift. An existing defect is not automatically a compatibility obligation.

## Resolve consequential uncertainty

Investigate before asking. Deepen only where evidence could change the increment or protect affected behavior. Recover the actor/data scope, transitions, exceptions, external effects and quality constraints needed for that decision.

Ask when missing evidence or an owner preference changes useful work or could cause substantial rework. Give the recommended boundary, its consequence and the exact work affected. Resolve reversible details within delegation; defer unrelated questions with a revisit condition and continue independent work. Preserve disagreement until its assumptions, evidence or scope can be reconciled. Demand, interaction or architecture gaps may need other expertise; explain the gap. These are optional recommendations to the agent, never skill invocations or a mandatory sequence.

A worthwhile discovery can remain open beyond the current increment. Check readily available evidence within scope; if future value justifies retaining it, preserve the observation/source, tentative interpretation and useful question in existing product records, separate from accepted scope. Continue the settled path without requiring an answer or adding a speculative feature. Keep required correctness evidence as a dependency; do not turn every curiosity into retained work or claim a possible benefit as fact.

## Artifact 1: analysis findings

Explain what was learned and what it changes, rather than presenting the specification as the analysis. Recover the following to the depth the requested decision needs:

- Problem, affected actors/goals, desired outcome and agreed scope/exclusions; distinguish an accepted boundary from a recommendation.
- Relevant current behavior and target changes, with source/revision/environment identity and the limits of available evidence.
- Candidate use cases linked to actor goals and events; explain missing goals, contradictory requests, unsupported solution assumptions and consequential dependencies.
- Gaps and decisions needed, with consequence, affected use case/work, owner when known and a proposal when justified. Keep confirmed decisions, proposals and assumptions distinct.
- Recommended next increment and analysis limits; preserve deferred discoveries only when they have a useful revisit condition.

Use short findings, actor/goal or current/target comparisons where useful, and prose for causal reasoning. Candidate use cases here are an index and analysis of coverage, not a second copy of their detailed flows. Existing source-bound evidence and decisions retain their authoritative homes.

## Artifact 2: use-case specification

Compile the analysis and accepted choices into behavior that implementers and verifiers can use without consequential guesses. Read [use-case specification](references/use-case-specification.md) when authoring or updating this artifact; it defines depth, product baseline, coverage, flows, tracking and gap handling adapted from the owner's supplied method. Keep consequential quality, security, compatibility and failure requirements visible at every depth; depth limits exploration, not preservation of known obligations.

Give each rule and decision one authoritative home. Link the analysis for evidence and rationale; make starting conditions, actor actions, observable outcomes, shared rules and consequential alternatives recoverable from the specification and its explicit links. Include required UX, API, data, authorization and deployment constraints as behavior, not invented architecture. A done-check defines required acceptance, not executed proof. Do not repeat it in another acceptance narrative.

Keep one authoritative gap/decision entry and link it from both artifacts and affected flows. Record where a gap was found, what it blocks and whether it affects this increment or later work. Unknown behavior stays unknown; a proposed default is not permission to build it. Do not invent policies, schemas, numeric thresholds or external guarantees to complete a template. Start with the useful outline and expand ambiguity and consequential behavior, rather than padding settled rules.

## Check and hand over

Keep a current version of each artifact with their distinct purpose intact. When a decision changes, update the authoritative rule/gap and affected links and flows; do not silently replace accepted intent with implementation. Reopen settled choices only for changed scope or relevant new evidence. Remove duplicated rules across analysis, specification and design while retaining rationale and qualifications that change interpretation.

For a consequential handoff, check that a reader can recover the current/target distinction, rules, dependencies and acceptance without the authoring conversation. A reader's restatement can expose a different interpretation; resolve it in the authoritative artifact. Self-review is not independent review, and routine corrections need no separate reviewer.

Use the specification as the primary behavioral input for technical design, prototypes, backend/frontend implementation, QA, release checks and delivery slicing. Use analysis selectively for problem framing, evidence, rationale, scope disputes and unresolved choices. A specification's existence or flow status does not establish owner acceptance, tested behavior or release authority. Other skills need no output from this particular skill when adequate equivalent requirements already exist. The agent chooses expertise; this skill invokes none.

Finish at the requested boundary: supported analysis/review findings, or selected flows implementable and verifiable without consequential guesses. Preserve the release boundary, accepted choices, applicable evidence and precise gaps for continuation. If one alternative remains blocked, hand over settled flows separately; do not make its decision a gate for all implementation unless a shared dependency actually blocks that work. Complete independent analysis and state partial readiness precisely; do not claim unexecuted checks or an unproved boundary as complete.
