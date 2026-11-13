# Shape and inspect the experience

## Start with the task and existing visual language

Map entry, user decisions, anxiety/friction, completion and recovery. Group information around tasks rather than database entities. Choose navigation that supports the work; a card dashboard is not the default answer for every application.

Identify the hardest user decision and the observation that would show whether the design supports it. Build enough realistic context to make that decision before polishing a family of screens. A working click is insufficient if the user cannot tell what to choose or what will happen.

| Hard decision | Representative prototype slice | Inspect before expanding |
| --- | --- | --- |
| Choose between similar records | Populated results, distinguishing details and selection confirmation. | Can the visible evidence distinguish records without opening every row? |
| Commit an expensive or irreversible action | Review, consequence, confirmation and uncertain-result recovery. | Are scope, cost and reversibility clear before commitment? |
| Resolve conflicting edits | Original/current values, conflict choice and preserved draft. | Can the user recover work and understand which version will survive? |

For example, a polished appointment calendar with empty slots does not resolve provider choice. Use realistic overlapping availability, location, duration and a fully booked option; exercise choosing and changing a slot. Inspect whether the selection and consequence remain clear at realistic density, then apply the successful pattern elsewhere. If alternatives are needed, vary the decision-driving interaction rather than recoloring the same layout. Record the observed design issue separately from assumptions about user comprehension; an agent walkthrough is not a user study.

### Explore a choice or resume incomplete work when the task warrants it

For a consequential choice whose effects users need to compare, represent proposed and committed state distinctly. Allow revision or cancellation without committing the business change or sending its notifications. Show relevant consequences, assumptions and unavailable data without presenting a scenario as a guaranteed forecast. Include the case where data or permissions change before Apply; final commitment must use the authoritative contract's current validation. Do not add a preview flow to a routine choice that is already clear.

Where the domain permits unfinished work, represent saving and resuming a draft separately from final submission or approval. Preserve permitted entered values and distinguish unknown from zero, false or not applicable. Show what remains required and how changed access, source records or concurrent edits affect resumption. Draft saving cannot stand in for required final validation or imply approval. Keep a direct completion path for a complete task; do not invent draft support where partial work is prohibited. Label simulated persistence and commit behavior honestly: an inspected prototype does not prove durable recovery or server enforcement.

Inspect component documentation, package dependencies, theme tokens and representative product screens before drawing bespoke controls. Suitable mature accessible components reduce implementation risk, but their actual semantics, supported variants, responsive behavior and extension points must fit the journey. A catalog constrains the solution space; it does not replace information architecture.

Use the library directly when practical. For a deliberately disposable prototype in another format, reproduce enough of its visual and interaction contract to make implementation credible and record mappings or intentional deviations. Do not build a review around nonexistent component states. Sorting/filtering/paging needs real behavior and documented component limits; a static table needs no grid dependency.

## Compose layout and words together

Establish a scanning path, clear primary actions, appropriate density, readable measure, consistent spacing and meaningful surface roles. Preserve brand and mature patterns. Greenfield choices should fit audience/task, not a universal pastel palette, hover-only sidebar or framework preference.

Use real domain labels, action verbs and recovery language. Confirmations should reflect consequences. Existing customer language and voice guidance are useful; missing guidance does not require a research project. Keep provisional tone distinct from an approved brand change. Read [microcopy craft](microcopy.md) for consequential wording, actual states and supported actions.

## Inspect the represented states

Exercise long labels, large values, dense results, empty states and permission differences. Check small-screen reflow/touch access and deliberately composed larger layouts, including focus order, keyboard access, contrast and reduced motion.

Critique actual screens for hierarchy, readability, alignment, density, clipping, feedback and recovery. Record viewport, route/state, finding, correction and limitation; checklists and aesthetic scores do not prove quality.

Retain useful tokens and component treatments so implementation preserves the reviewed experience. Reuse styles/assets where appropriate while allowing framework and accessibility adaptations; require verified fidelity rather than byte-identical markup.
