# Requirements lenses

Use these to find gaps that change the contract in the affected behavior. They are not an outline or a questionnaire.
- Small correction: cover only its changed contract.
- Broad work: start with a shallow capability map.
- Record a finding once, even when several lenses reveal it.

| Lens | Recover what changes the contract |
| --- | --- |
| Behavior | Actor and trigger, intended outcome, state transitions, validation, alternate and error paths, observable completion |
| Access | Capability permission, record and data scope, authority for exceptional actions, enforced by the authoritative system |
| Data | Ownership, identifiers, calculations, history and retention, migration, transactions, concurrency |
| Integration | API shapes, authentication, errors, paging, filter and sort, timeouts, retries, idempotency, partial failure |
| Experience | Journey and navigation, density, meaningful states, accessibility, supported devices, customer terminology and tone |
| Consequential copy | Wording and state conditions where a message defines behavior or consequences; queued work is not completed work |
| Domain risk | Who else can be the subject of or act in the transaction (proxies, minors, delegates, third parties); consent or regulatory regime for the data and messages involved; misuse and fraud paths; safety or eligibility limits on who may receive an outcome. These raise questions for the owner, never compliance claims |
| Quality | Performance and load, recovery and reliability, security, compatibility, observability, auditability. Ground targets in applicable evidence or mark them assumptions; a compliance claim needs actual evidence |

Scope quality targets to the subsystem and actual usage. Business audit history identifies consequential actions and actors; diagnostic logs do not replace it.

## Resolve ambiguity with contrasting behavior
When settled rules do not answer it, ask a question only if plausible answers produce different observable behavior.
- State the accepted outcome and the nearest rejected or alternate outcome, using only the starting state, actor and input, result and side effect that distinguish them. Mark them proposed until supported.
- Example: before dispatch, cancellation confirms and requests one refund; after dispatch, the order is unchanged and the return route is explained.
- A refund-call timeout leaves an uncertain external outcome; it does not prove the cancellation failed.
- A missing answer blocks that decision, not unrelated discovery.
- Do not enumerate permutations or invent examples for precise rules.

## Account convention
When accounts are required, start from the owner's convention:
- one role on each Users row;
- separate local Roles, Modules and module-role grants;
- bcrypt local credentials.

- Assess real exceptions before proposing multi-role identity tables.
- Keep authentication, application permissions and team, clinic or record scope distinct.
- A future central identity must preserve local users, permissions and business history.
- A public site needs no accounts without a use case.

Treat this as an owner constraint, not a request to design account infrastructure. Specify actors, permissions, record scope and preservation obligations; leave mechanisms and justified exceptions to design.

## Representation and depth
- Deferred work: a brief actor and goal description. Active workflows: an outline.
- Clarify actor and system responsibilities where ambiguous; describe fully only what complexity, consequences or lack of expert access require.
- A chosen test scenario needs enough conditions, inputs and expected outcomes to verify the slice. A test idea alone is not enough.
- A slice is an end-to-end outcome and may need several tasks.
- Shared definitions and system-wide constraints have one home.

Basis: Jacobson, Spence and de Mendonca, *Use-Case 3.0* (2024), pp. 35, 40, 66-72, adapted for graduated detail and balanced narrative and test coverage. [EARS](https://alistairmavin.com/ears/) supplies condition and response sentence patterns when useful.
