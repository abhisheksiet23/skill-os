---
name: app-analyze
description: Clarify, challenge and review software requirements, recover relevant existing behavior, and define use cases and behavioral contracts before implementation. Use for material product changes, ambiguous defects, modernization analysis or standalone requirements review; skip mechanical fixes, technical architecture review and business-demand validation.
---

# App Analyze

Catch expensive mistakes while decisions are still cheap to change. Separate the requested solution, underlying problem and desired outcome; challenge the solution when evidence warrants it.

Optimize total delivery effort, including user decisions, implementation, verification and rework. Preserve valuable strategy and design work; a shorter analysis that exports consequential uncertainty downstream is not an improvement.

## Work from evidence

Inspect the project's instructions, current implementation and existing decisions. Accept adequate briefs and contracts from any author or tool. No earlier skill invocation, phase ledger or prescribed documentation tree is required. For existing-system uncertainty or replacement, read [existing systems](references/existing-systems.md) only as relevant.

After shallow discovery, settle choices that could invalidate substantial investigation: the product's purpose, which capabilities belong in the next release, what must remain compatible, and how retained workflows will be reached. Recommend a boundary with its consequences; do not infer approval or turn this into a standard questionnaire. Deepen discovery where it can change a decision or protect affected behavior. Continue independent analysis while a consequential choice is pending.

Trace the affected actors, permissions and data scope, business rules, states, alternate/error paths, concurrency, history and side effects. Scan material quality needs with [requirements](references/requirements.md). Separate observed behavior from intended behavior; an old defect is not automatically a requirement.

Ask when evidence cannot resolve a consequential choice whose answer changes the next useful increment or could invalidate substantial investigation. Discover facts first, resolve reversible details within delegated authority and defer unrelated questions. Present the recommended answer and trade-off. Mark unresolved blockers, user decisions and reasonable assumptions distinctly. Preserve the user's decision after constructive challenge; do not quietly change it later.

## Shape enough to implement

Define observable acceptance and the necessary UX, API, data, auth and deployment boundaries. For broad work, map major use cases and cross-cutting constraints, then detail the next coherent increment. Avoid both a giant speculative specification and a narrow first increment that misses shared architectural consequences.

Reuse project records. Lead the result with the recommended boundary and its important consequence, then connect consequential requirements to the observed behavior or decision that supports them. Keep accepted decisions, working assumptions, verification and unresolved questions visibly distinct. Use a compact comparison for genuine alternatives, not as a container for narrative. A short task may need only the response; material work needs enough durable context for another session to continue without inventing requirements.

Keep one authoritative current contract, which may link focused supporting contracts and baseline evidence. Update it after material decisions; avoid copying the same requirements into multiple summaries. Reopen settled choices only for changed scope or relevant new evidence. On resumption, carry forward the release boundary, decisions, evidence locations and precise gaps, not the full investigation history.

For consequential contracts crossing sessions or implementers, check whether the artifact and its linked evidence explain the current behavior, proposed behavior and important constraints without the authoring conversation. A reader's brief restatement can expose a different interpretation; resolve consequential differences in the authoritative contract, not only in chat. In standalone requirements review, report the gaps and consequences without rewriting the contract unless authorized. A reread in the authoring context is useful but is not independent review. Routine corrections do not need another reviewer or a separate document.

This skill produces analysis and contracts, not production code. Finish when consequential behavior is sufficiently defined, or identify the precise unresolved decision and continue independent analysis.

Completion means the next increment can be implemented and verified without guessing consequential behavior, with material dependencies and acceptance understood. Defer unrelated uncertainty with the condition that would make it relevant. Do not use an arbitrary time/token cap to omit architectural or product risks.

## Recommendations, not handoffs

Optional expertise: `business-validate` for uncertain demand; `app-prototype` for unresolved experience; `app-solution-design` for material architecture choices, component responsibilities or cross-system guarantees before implementation. Analysis owns intended behavior and constraints; solution design develops the technical approach without requiring requirements to be rewritten. Explain the gap and relevant evidence. Recommendations do not invoke skills or prescribe transitions; the agent decides.
