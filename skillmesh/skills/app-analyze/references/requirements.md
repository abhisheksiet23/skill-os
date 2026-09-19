# Requirements that change decisions

Use this as a scan, not a questionnaire or mandatory artifact.

- **Behavior:** actor and trigger, intended outcome, important alternate/error paths, state transitions, validation and observable acceptance.
- **Access:** distinguish capability access, record/data scope and exceptional action permission. Enforce at authoritative boundaries.
- **Data:** ownership, identifiers, calculations, retention/history, migration, transactions and concurrent changes.
- **Integration:** API shapes, errors, auth, paging/filter/sort, timeouts, retries, idempotency and partial failure where relevant.
- **Experience:** journey, navigation, density, meaningful states, accessibility, supported devices, customer terminology and tone.
- **Quality:** performance under representative data/load; reliability and recovery; security; accessibility; compatibility; observability and auditability. Specify measurable targets only when grounded in requirements or explicitly identified assumptions. A named compliance obligation needs actual applicable evidence, not a generic checklist claim.

Scope targets to the affected subsystem. A business-hours back office need not inherit a clinical workflow's availability target. An audit trail records consequential business actions and their actors; ordinary diagnostic logs do not replace it.

An adequate use case can be a compact paragraph: who, why, main behavior, important exceptions/rules and how completion is observed. Preserve a shallow coverage map for large work without manufacturing IDs or documents for trivial edits.

When a material choice needs the owner, state what changes depending on the answer. Low-risk implementation details can be resolved and recorded by the agent. Existing authorization and explicit delegation remain valid.
