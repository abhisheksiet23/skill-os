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

## Resolve ambiguity with contrasting behavior

Start with the ambiguity most likely to change the increment. Inspect existing rules and examples first, then ask a discriminating question: two plausible answers should produce different observable behavior. Avoid asking for preferences that the current contract already settles.

| Ambiguity | Discriminating question | Behavior to settle |
| --- | --- | --- |
| “Cancel an order” | Can cancellation succeed after dispatch has started? | Allowed source states, rejection and any compensating action. |
| “Show my team's records” | Does a transferred record follow its current team or retain the original team's access? | Scope at read/write time and any history exception. |
| “Prevent duplicates” | Is repeating the same request a retry, or can it represent another legitimate purchase? | Identity of the business operation and repeated-request outcome. |
| “Keep the old workflow” | Must old clients still write, or only read historical results? | Compatibility boundary and retirement condition. |

Express the answer with a representative accepted example and the nearest rejected or alternate example. Include the prior state, actor/input, expected result and observable side effect only as needed to distinguish them. This is a behavioral contract, not a demand for exhaustive permutations.

For example, “owners may cancel” leaves the dispatch boundary unresolved. A useful pair is: an owner cancelling a paid, undispatched order receives a cancellation confirmation and one refund request; the same action after dispatch starts leaves the order unchanged and explains the supported return route. A timeout while requesting the refund is a separate uncertain outcome, not evidence that cancellation failed. Mark this pair proposed until supported by the owner or an authoritative rule. If the answer remains unavailable, identify exactly which implementation decision depends on it rather than inventing a default.

For applications requiring accounts, the owner's starting convention is one role on each Users row, separate local Roles/Modules/module-role grants and bcrypt local credentials. Assess exceptions from actual requirements before proposing multi-role identity tables. Separate authentication from application permission; future central identity must preserve local users, permissions and business history. Team/clinic/record scope remains distinct from module access. Public websites need no account infrastructure without a use case.

For an unresolved owner choice, explain what changes depending on the answer and recommend a boundary. Resolve low-risk implementation details within existing authorization/delegation. Record accepted choices, provisional assumptions and remaining blockers separately.
