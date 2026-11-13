# Protect data across integration boundaries

## Derive enforcement and proof from the invariant

State the business condition that must remain true, identify every writer capable of breaking it, then choose the authoritative enforcement boundary. Request validation improves errors; it cannot alone protect an invariant against another caller, concurrent write or worker. Use the existing transaction/storage capabilities before adding coordination machinery.

| Invariant | Authoritative enforcement | Distinguishing check |
| --- | --- | --- |
| At most one active reservation per resource/time | Database constraint or transactional locking/version strategy covering all writers. | Two synchronized attempts: only one commits; the loser receives the defined outcome. |
| A transition cannot skip approval | State/version and permission check at the mutation boundary. | Call the endpoint directly from an invalid state; neither state nor external effects change. |
| Retrying one accepted operation cannot repeat its effect | Stable operation key plus atomic result/pending-work recording and recipient support where needed. | Lose the first response, then retry; inspect effect count and returned operation identity. |
| Owned writes commit together or leave no committed partial state | A transaction covering those writes, with the appropriate isolation/reader behavior. | Inject failure between mutations; inspect committed records from another transaction and verify the defined rollback outcome. |
| Cross-system partial work remains identifiable and recoverable, never falsely complete | Durable operation identity and explicit pending/recovering state, recipient idempotency where supported, and reconciliation or intervention ownership. | Crash around local commits and remote acceptance; inspect permitted intermediate states, duplicate effects, terminal recovery and the defined operator path when automation cannot finish. |
| A preview cannot commit its proposed business change or trigger that change's external effects | Separate evaluation from the mutation boundary; Apply rechecks current permission, record version and relevant constraints atomically where required. | Compare/revise/cancel leave business records and effect recipients unchanged; change availability or authority after preview and verify Apply cannot silently use stale permission or validity. |
| A permitted draft can remain incomplete without becoming a finalized action | Distinct draft/finalization contracts with authorized persistence, explicit missing-value semantics, concurrency checks and authoritative final validation. | Save and reload incomplete permitted values, including legitimate zero; deny unauthorized resume, reject conflicting overwrite and block finalization with missing evidence without emitting final-action effects. |

For example, checking “remaining stock > 0” and then decrementing in a separate unguarded write passes sequential tests while two buyers can oversell the final unit. Enforce a conditional atomic update or an equivalent supported transaction/locking scheme, then synchronize competing requests at that boundary. Assert the invariant and the losing caller's contract, not a particular helper call. If a remote charge was already accepted, rolling back local rows is incomplete; retain enough durable identity to reconcile it. Recovery is not atomic rollback: define which intermediate states the product permits and prove reconciliation separately. Do not promise no partial external effects merely because recovery exists.

## Define what a successful write means

Locate the authoritative server-side checks for permissions, record scope and exceptional actions. Preserve a business audit trail when required, separate from diagnostic logs, using existing project conventions before inventing an audit subsystem.

For external operations, define the observable result and reconcile an uncertain outcome before retrying. Use idempotency or unique business keys when duplication could cause harm. Local transaction rollback cannot undo an effect another system has already accepted.

Preview and draft support are conditional on the product contract, not default features. Define any allowed draft-specific effects separately from final-action effects; never treat saving incomplete work as approval. On resume or Apply, enforce current authority and relevant data/version constraints. Reuse existing state and persistence mechanisms; do not introduce a workflow engine or relax a genuine finalization invariant to accommodate unfinished input.

## Evolve stored data and consumer contracts together

Inspect representative existing records, defaults, nullability, identifiers, constraints and affected queries. Verify fresh-create and upgrade paths, including invalid/boundary data; retain an executable sanitized reproduction when useful.

For independently deployed consumers, prefer compatible expansion before removing old shapes. Record actual models, validation, errors, authentication, paging/filter/sort and relevant retry semantics. Follow project error conventions rather than imposing a vendor format.

For old/new coexistence, identify routing/auth trust, authoritative writers, shared schema and retained jobs, reports and integrations. Demonstrate old readers can handle new writes, or define and test reconciliation/forward recovery. Reverting routing does not reverse data.

## Diagnose the boundary that failed

Separate setup/environment failure from the reported behavior. Use a bounded reproduction and observations that distinguish competing explanations; one lucky pass cannot establish an intermittent defect is fixed. Remove temporary instrumentation after verification, and retain the candidate/environment identity and unresolved limits with the result.
