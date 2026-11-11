---
name: app-analyze
description: Clarify, challenge and review software requirements, recover relevant existing behavior, and define use cases and behavioral contracts before implementation. Use for material product changes, ambiguous defects, modernization analysis or standalone requirements review; skip mechanical fixes, technical architecture review and business-demand validation.
---

# App Analyze

Turn a request into intended behavior that can be implemented and verified without guessing consequential decisions. Separate the proposed solution, underlying problem and desired outcome; challenge the proposal when evidence warrants it, then preserve the owner's decision. This skill produces analysis and contracts, not production code.

## Bound the question before deep discovery

Inspect project instructions, existing decisions and the affected implementation. Accept adequate briefs and contracts from any author or tool; locate their relevant sections and source identities before retrieving more. Reuse still-valid behavior and acceptance evidence, investigating the changed or uncertain boundary rather than rediscovering the system. No prior invocation, phase ledger or prescribed documentation tree is required.

For a defect, trace its affected path. For broad change or replacement, first make a shallow capability/dependency map. Settle choices that could invalidate substantial investigation: product purpose, next-release capabilities, compatibility obligations and how retained workflows remain reachable. Recommend a boundary and explain its consequences rather than issuing a standard questionnaire. Use [existing-system recovery](references/existing-systems.md) when current behavior or coexistence is uncertain.

Deepen discovery where it could change a decision or protect affected behavior. Trace actors, permissions and data scope, rules, state transitions, alternate/error paths, concurrency, history and external effects. Distinguish what the system does from what it should do; an old defect is not automatically a compatibility requirement. Use [requirements scan](references/requirements.md) for material quality, experience, integration and account constraints.

Discover facts before asking the owner. Ask only when unavailable evidence or a consequential preference changes the next useful increment or could invalidate substantial work. Present the recommended answer and trade-off, continue independent analysis, and keep decisions, assumptions and blockers distinct. Resolve reversible details within delegated authority and defer unrelated uncertainty with a condition for revisiting it.

## Establish an implementable contract

For broad work, retain a shallow map of major use cases and shared constraints, then detail the next coherent increment. Do not let a narrow first feature hide architectural consequences, or create a speculative specification for every future capability.

Define observable acceptance and the necessary UX, API, data, authorization and deployment boundaries. A use case needs enough actor/trigger, outcome, main behavior, consequential exceptions and completion evidence to resolve ambiguity; trivial work needs no invented IDs or document set. Connect important requirements to their supporting observation or owner decision.

Keep one authoritative current contract in adequate project records, linking focused supporting contracts and baseline evidence. Update it after material decisions. Preserve accepted intent separately from implementation drift, working assumptions, verification and open questions. Compare genuine alternatives when useful; do not copy the same narrative into several summaries. Reopen a settled choice only for relevant new evidence or changed scope.

For consequential handoffs, check whether the contract and linked evidence explain current behavior, proposed behavior and constraints without the authoring conversation. A reader's brief restatement can expose a different interpretation; resolve material differences in the authoritative record. A self-reread is useful but is not independent review. Standalone review reports gaps and consequences without editing the contract unless authorized; routine corrections need no separate reviewer.

## Finish at the decision boundary

Lead with the recommended scope and its important consequence. Keep the contract scannable with labeled facts such as actor/trigger, behavior, exceptions, acceptance and decision needed; use a short list for one flow or a table when comparing behaviors. Link evidence beside the claim and keep observed, assumed and accepted behavior distinct. These are useful shapes, not required sections. Completion means implementers and verifiers can proceed with the next increment without guessing consequential behavior and understand its dependencies. If a blocker remains, identify the work it blocks and complete independent analysis.

Preserve enough durable context to resume: release boundary, accepted decisions, source/revision-bound evidence and exact gaps. Optimize total delivery effort, including owner decisions, verification and rework; neither brevity nor a time/token cap justifies exporting consequential uncertainty downstream.

Uncertain demand may need business validation; unresolved experience may need a prototype; architecture, responsibilities or cross-system guarantees may need solution design. Explain the concrete gap and useful evidence. These are optional recommendations to the agent, not invocations or required phases.
