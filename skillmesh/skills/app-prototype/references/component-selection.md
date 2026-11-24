# Choose a pattern for the task

Use this reference when an unresolved interaction-pattern choice would benefit from comparison. No catalog pass is required for every prototype.

Start with:
- The actor's goal and the information needed to decide.
- Realistic content density and required states.
- Adequate accepted designs and suitable existing components.

## Candidate patterns and reasons to depart
These are starting hypotheses. Combine or replace them when the task requires. Records do not imply a table, and a domain interaction need not match an entry.

| Task and conditions | Candidate pattern | Reason to choose differently |
| --- | --- | --- |
| Compare many items across the same short attributes | Aligned table with meaningful columns and a detail view | Long narratives and mixed attributes defeat scanning. Use structured summaries or a reading view. Check narrow-screen priorities instead of squeezing every column |
| Read a long explanation or assess a case in context | Reading view with headings and adjacent decision evidence | Cards fragment the narrative. Dense tables hide reasoning. Add a compact comparison only for attributes that need alignment |
| Choose exactly one option | Radios for a visible manageable set. Select or searchable combobox for a larger set | Hidden options hinder comparison. Rich alternatives may need selectable summaries with explicit single-selection semantics. Check keyboard and focus support |
| Include several independent options | Checkboxes, or a multi-select with visible selected items | A single-choice control changes the rule. Large sets may need search, grouping and a selected-items review. Distinguish selection from immediate execution |
| Review before a consequential commitment | Review surface showing scope and consequence, then an explicit action | A modal can hide needed context. Use an inline or full-page review for long content. A routine clear action needs no invented confirmation |
| Edit a short local value or a related set of fields | Inline edit for a local change. Grouped form for related validation | Inline editing can hide cross-field constraints. Use a larger surface when relationships, drafts or recovery need context. Invent no draft persistence |
| Reason about time, position or relationships | Calendar, timeline, spatial view or a domain composition | A list may hide the deciding relationship. A visual view may exclude keyboard or assistive-technology users. Keep an operable way to inspect and act on the same information |

## Fit the project's real components
Existing system:
- Verify actual documentation, supported states, semantics, responsive behavior and extension points.
- A mock's appearance does not prove that a component API or state exists.
- Capability unavailable or stale: verify the contract. Then choose a fitting alternative, or surface the affected gap and continue unrelated work.

New UI without an adequate system:
- Compare established libraries against the stack, accessibility requirements, theming and interaction needs.
- A familiar library is a starting preference. It is not a universal vendor and not permission to install or migrate.
- Compose, extend or create when available components cannot represent the required behavior faithfully.
- Check keyboard operation, accessible names and roles, focus movement, selection and error and recovery states in the resulting prototype. A library's reputation does not verify the composition.

## Decision examples
- **Routine comparison:** an operator compares 40 deliveries by due time, location and status. Start with aligned rows and a detail view. Prioritize deciding attributes on narrow screens. If the decision depends on long exception explanations, rebalance reading and comparison instead of forcing them into cells.
- **New domain composition:** a reviewer connects passages in a long incident account to evidence and unresolved contradictions. Compose a reading pane, linked evidence and an annotation or decision surface, not a record table. Keep keyboard access and context while moving between them. A sequential reading and evidence view may fit a narrow screen better. This departure needs no approval.
- **Settled design:** an accepted journey already uses accessible expandable summaries. Reuse it when adequate. The table suggestion and library preference do not reopen it or justify replacing the system.

Record in design artifacts only consequential choices, supported-component mappings and deliberate deviations. The inspectable prototype and its observed interaction and viewport evidence stay primary. These suggestions do not replace rendering and exercising the journey. They do not prove user comprehension, production integration or savings.

## Refine suggestions from development feedback
Use feedback from prototyping, implementation, QA and actual use to refine this reference as well as the application.

What to look for:
- Unsuitable pattern choices and useful compositions.
- Accessibility or responsive failures.
- Unsupported component assumptions.
- Corrections that changed the design.

How to treat it:
- Keep owner or user feedback, agent observations and executed evidence distinguishable.
- A preference or one local result is not a universal rule.
- Conflicting feedback may reflect different conditions. It does not invalidate a pattern everywhere.
- Raw feedback, application facts, component versions and source-bound evidence stay in the owning project.
- Extract only the reusable lesson, with its task conditions, deciding reason, evidence limits and exceptions.

How to apply it:
- Revise the affected suggestion, limitation or example in place. Add an entry only when it fills a useful gap.
- Correct a demonstrated problem without waiting for a usage quota. Leave uncertain benefits provisional.
- Authoring-source changes authorized and accessible: apply the lesson here and check the affected semantics and representative behavior.
- Otherwise: preserve a concise proposed correction and evidence pointer in the project's existing handoff. Do not silently edit installed copies. Do not imply the reference was updated.
- Preserve accepted application decisions and required behavior and accessibility.
- Do not accumulate a feedback transcript or a separate tracking system here.
