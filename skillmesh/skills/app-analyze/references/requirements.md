# Requirements lenses

Use these to find decision-changing gaps in affected behavior, not as an output outline or questionnaire. A small correction needs only its changed contract; broad work needs a shallow capability map before increment-level detail. Record a finding once even when several lenses reveal it.

| Lens | Recover what changes the contract |
| --- | --- |
| Behavior | Actor/trigger, intended outcome, state transitions, validation, alternate/error paths and observable completion. |
| Access | Capability permission, record/data scope and exceptional-action authority, enforced by the authoritative system. |
| Data | Ownership, identifiers, calculations, history/retention, migration, transactions and concurrency. |
| Integration | API shapes, authentication, errors, paging/filter/sort, timeouts, retries, idempotency and partial failure. |
| Experience | Journey/navigation, density, meaningful states, accessibility, supported devices and customer terminology/tone. |
| Consequential copy | Wording and state conditions where a message defines behavior or consequences: queued work is not completed work. |
| Quality | Performance/load, recovery/reliability, security, compatibility, observability and auditability. Ground targets in applicable evidence or mark assumptions; compliance claims need actual evidence. |

Scope quality targets to the subsystem and actual usage. Business audit history identifies consequential actions and actors; diagnostic logs do not replace it.

## Resolve ambiguity with contrasting behavior

Inspect settled rules first. Ask a question only when plausible answers produce different observable behavior: cancellation before/after dispatch; transferred records following current/original team access; a repeated request being a retry/new purchase; old clients needing write/read-only compatibility.

Define an accepted outcome and the nearest rejected or alternate outcome using only the starting state, actor/input, result and side effect that distinguish them. For example, cancellation before dispatch might confirm cancellation and request one refund; after dispatch it might leave the order unchanged and explain the return route. Mark these proposed until supported. A refund-call timeout leaves an uncertain external outcome; it does not prove cancellation failed. Missing answers block specific decisions, not unrelated discovery. Do not enumerate permutations or invent examples for already-precise rules.

## Account convention

When accounts are required, the owner's starting convention is one role on each Users row, separate local Roles/Modules/module-role grants and bcrypt local credentials. Assess actual exceptions before proposing multi-role identity tables. Authentication, application permissions and team/clinic/record scope are distinct. Future central identity must preserve local users, permissions and business history. Public sites need no accounts without a use case.

## Representation and depth

Use brief actor/goal descriptions for deferred work and an outline for active workflows. Clarify actor/system responsibilities where ambiguous; fully describe only the parts whose complexity, consequences or unavailable expert access require it. A chosen test scenario needs enough conditions/inputs and expected outcomes to verify the slice; a test idea alone is insufficient. A slice is an end-to-end outcome and may require several implementation tasks. Shared definitions and system-wide constraints have one home.

Basis: Jacobson, Spence and de Mendonca, *Use-Case 3.0: The Guide to Succeeding with Use Cases — Refreshed*, May 2024, pp. 35, 40, 66–72. This guidance adapts graduated detail and balanced narrative/test coverage; no particular template or full lifecycle is required. [Mavin's EARS](https://alistairmavin.com/ears/) supplies condition/response sentence patterns when useful. Original synthesis; neither method itself proves compression.
