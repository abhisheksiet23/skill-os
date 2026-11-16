# Choose a pattern for the task

Use this reference when an unresolved interaction-pattern choice would benefit from comparison. Start with the actor's goal, information needed to decide, realistic content density and required states. Adequate accepted designs and suitable existing components remain the starting point; there is no required catalog pass for every prototype.

## Candidate patterns and reasons to depart

These are starting hypotheses. Combine or replace them when the task requires it; records do not inherently imply a table, and a domain interaction need not match an entry.

| Task and conditions | Candidate pattern | Limitation / reason to choose differently |
| --- | --- | --- |
| Compare many items across the same short attributes | Aligned table with meaningful columns and a detail view | Long narratives and heterogeneous attributes undermine scanning. Use structured summaries or a reading view; verify narrow-screen priorities rather than squeezing every column |
| Read a long explanation or assess a case in context | Document-like reading view with headings and adjacent decision evidence | Cards can fragment the narrative; dense tables hide reasoning. Add a compact comparison only for attributes that actually need alignment |
| Choose exactly one mutually exclusive option | Radios for a visible manageable set; select or searchable combobox for a larger set | Hidden options make comparison harder. Rich alternatives may need selectable summaries with explicit single-selection semantics; check actual keyboard and focus support |
| Include several independent options | Checkboxes or a multi-select with visible selected items | A single-choice control changes the rule. Large sets may need search, grouping and a selected-items review; distinguish selection from immediate execution |
| Review information before a consequential commitment | Review surface showing scope and consequence, followed by an explicit action | A modal can conceal necessary context. Use an inline or full-page review when content is long; routine clear actions need no invented confirmation step |
| Edit a short local value or a related set of fields | Inline edit for a local change; grouped form for related validation | Inline editing can hide cross-field constraints. Use a larger edit surface when relationships, drafts or recovery require context; do not invent draft persistence |
| Reason about time, position or relationships | Calendar, timeline, spatial view or a domain composition | A conventional list may hide the deciding relationship; a visual view may exclude keyboard or assistive-technology users. Preserve an operable way to inspect and act on the same information |

## Fit the project's real components

For an existing system, verify actual component documentation, supported states, semantics, responsive behavior and extension points. Do not assume a mock's appearance proves a component API or state exists. If a required capability is unavailable or stale, verify the contract, choose a fitting alternative or surface the affected gap while continuing unrelated work.

For new UI without an adequate system, compare established libraries against the project's stack, accessibility requirements, theming and interaction needs. A familiar library is a starting preference, not a universal vendor or permission to install or migrate. Compose, extend or create when available components cannot represent required behavior faithfully. Check keyboard operation, accessible names/roles, focus movement, selection and error/recovery states in the resulting prototype; a library's reputation does not verify this composition.

## Decision examples

- **Routine comparison:** an operator compares 40 deliveries by due time, location and status. Start with aligned rows and a detail view; prioritize deciding attributes on narrow screens. If the actual decision depends on long exception explanations, reconsider the reading/comparison balance rather than forcing them into cells.
- **New domain composition:** a reviewer must connect passages in a long incident account to evidence and unresolved contradictions. Compose a reading pane, linked evidence and an annotation/decision surface instead of a record table. Preserve keyboard access and context when moving between them; a sequential reading/evidence view may fit a narrow screen better. This is a legitimate departure from the suggestions without map-specific approval.
- **Settled design:** an accepted project journey already uses accessible expandable summaries. Reuse it when adequate; the table suggestion and library preference do not reopen that decision or justify replacing the system.

Record only consequential choices, supported-component mappings and deliberate deviations in the project's existing design artifacts. Keep the inspectable prototype and its observed interaction/viewport evidence primary. These suggestions do not replace rendering and exercising the actual journey, prove user comprehension or establish production integration or savings.

## Refine suggestions from development feedback

Use feedback gathered during prototyping, implementation, QA and actual use to refine this reference as well as the application. Look for unsuitable pattern choices, useful compositions, accessibility or responsive failures, unsupported component assumptions and corrections that changed the design. Keep owner/user feedback, agent observations and executed evidence distinguishable; a preference or one local result is not a universal rule.

Keep raw feedback, application facts, component versions and source-bound evidence in the owning project. Extract only a reusable lesson with its task conditions, deciding reason, evidence limits and exceptions. Revise the affected suggestion, limitation or example in place; add an entry only when it fills a useful gap. Conflicting feedback may reveal different conditions rather than invalidate a pattern everywhere. Correct a demonstrated problem without waiting for a usage quota; leave uncertain benefits provisional.

When authoring-source changes are authorized and accessible, apply the lesson here and check the affected semantics and representative behavior. Otherwise preserve a concise proposed correction and evidence pointer in the project's existing handoff; do not silently edit installed copies or imply the reference was updated. Preserve adequate accepted application decisions and required behavior/accessibility while improving the reusable guidance. Avoid accumulating a feedback transcript or a separate tracking system in this reference.
