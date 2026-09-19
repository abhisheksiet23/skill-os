---
name: app-analyze
description: Clarify and challenge software requirements, recover relevant existing behavior, and define use cases and technical contracts before implementation. Use for material product changes, ambiguous defects or modernization analysis; skip mechanical fixes and business-demand validation.
---

# App Analyze

Catch expensive mistakes while decisions are still cheap to change. Separate the requested solution, underlying problem and desired outcome; challenge the solution when evidence warrants it.

## Work from evidence

Inspect the project's instructions, current implementation and existing decisions. Accept adequate briefs and contracts from any author or tool. No earlier skill invocation, phase ledger or prescribed documentation tree is required. For existing-system uncertainty or replacement, read [existing systems](references/existing-systems.md) only as relevant.

Trace the affected actors, permissions and data scope, business rules, states, alternate/error paths, concurrency, history and side effects. Scan material quality needs with [requirements](references/requirements.md). Separate observed behavior from intended behavior; an old defect is not automatically a requirement.

Ask only about consequential choices that evidence cannot resolve. Present the recommended answer and trade-off. Mark unresolved blockers, user decisions and reasonable assumptions distinctly. Preserve the user's decision after constructive challenge; do not quietly change it later.

## Shape enough to implement

Define observable acceptance and the necessary UX, API, data, auth and deployment boundaries. For broad work, map major use cases and cross-cutting constraints, then detail the next coherent increment. Avoid both a giant speculative specification and a narrow first increment that misses shared architectural consequences.

Reuse project records. Record current behavior separately from proposed changes, with evidence, decisions and remaining unknowns. A short task may need only the response; material work needs enough durable context for another session to continue without inventing requirements.

This skill produces analysis and contracts, not production code. Finish when consequential behavior is sufficiently defined, or identify the precise unresolved decision and continue independent analysis.

## Recommendations, not handoffs

Uncertain demand may benefit from `business-validate`; unresolved material experience from `app-prototype`. Explain the need and relevant evidence. These are optional recommendations to the agent, never instructions to invoke another skill. The agent owns selection, sequencing and continuation under the user's scope.
