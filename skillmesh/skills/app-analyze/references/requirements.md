# Requirements that change decisions

Use this as a scan, not a questionnaire or mandatory artifact.

- **Behavior:** actor and trigger, intended outcome, important alternate/error paths, state transitions, validation and observable acceptance.
- **Access:** distinguish capability access, record/data scope and exceptional action permission. Enforce at authoritative boundaries.

- **Data:** ownership, identifiers, calculations, retention/history, migration, transactions and concurrent changes.
- **Integration:** API shapes, errors, auth, paging/filter/sort, timeouts, retries, idempotency and partial failure where relevant.
- **Experience:** journey, navigation, density, meaningful states, accessibility, supported devices, customer terminology and tone.
- **Consequential interface copy:** include representative strings and their state conditions in acceptance criteria where wording defines behavior or consequences, such as queued versus completed work.
- **Quality:** performance under representative data/load; reliability and recovery; security; accessibility; compatibility; observability and auditability. Specify measurable targets only when grounded in requirements or explicitly identified assumptions. A named compliance obligation needs actual applicable evidence, not a generic checklist claim.

For applications that need accounts, the owner's starting convention is one role directly on each Users row, separate local Roles/Modules/module-role grants, and bcrypt for local credentials. Confirm exceptions from actual requirements rather than proposing multi-role identity tables automatically. Separate who authenticated the user from what the application permits; future central identity must preserve local users, permissions and business history. Existing team/clinic/record scopes remain separate from module access. Do not add account infrastructure to a public website without a need.

Scope targets to the affected subsystem. A business-hours back office need not inherit a clinical workflow's availability target. An audit trail records consequential business actions and their actors; ordinary diagnostic logs do not replace it.

An adequate use case can be a compact paragraph: who, why, main behavior, important exceptions/rules and how completion is observed. Preserve a shallow coverage map for large work without manufacturing IDs or documents for trivial edits.

When a material choice needs the owner, state what changes depending on the answer. Low-risk implementation details can be resolved and recorded by the agent. Existing authorization and explicit delegation remain valid.
