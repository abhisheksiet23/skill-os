# Find the requirements that change the next decision

Use this scan on affected behavior, not as a questionnaire or mandatory artifact. A compact use case can state actor, trigger, purpose, main behavior, consequential exceptions/rules and observable completion. Broad work needs a shallow coverage map; trivial changes need no manufactured IDs or documents.

| Boundary | Recover or define what matters |
| --- | --- |
| Behavior | Intended outcome, state transitions, validation, alternate/error paths and observable acceptance. |
| Access | Capability access, record/data scope and exceptional-action permission, with authoritative enforcement. |
| Data | Ownership, identifiers, calculations, history/retention, migration, transactions and concurrent changes. |
| Integration | API shapes, errors, authentication, paging/filter/sort, timeouts, retries, idempotency and partial failure. |
| Experience | Journey, navigation, density, meaningful states, accessibility, supported devices, customer terminology and tone. |
| Consequential copy | Representative strings and their state conditions where wording defines behavior or consequences; queued and completed work differ. |
| Quality | Representative performance/load, reliability/recovery, security, compatibility, observability and auditability. Ground measurable targets in requirements or label assumptions. A compliance claim needs actual applicable evidence. |

Scope targets to the affected subsystem. A business-hours back office need not inherit a clinical workflow's availability requirement. Business audit records identify consequential actions and actors; diagnostic logs are not a substitute.

For applications requiring accounts, the owner's starting convention is one role on each Users row, separate local Roles/Modules/module-role grants and bcrypt local credentials. Assess exceptions from actual requirements before proposing multi-role identity tables. Separate authentication from application permission; future central identity must preserve local users, permissions and business history. Team/clinic/record scope remains distinct from module access. Public websites need no account infrastructure without a use case.

For an unresolved owner choice, explain what changes depending on the answer and recommend a boundary. Resolve low-risk implementation details within existing authorization/delegation. Record accepted choices, provisional assumptions and remaining blockers separately.
