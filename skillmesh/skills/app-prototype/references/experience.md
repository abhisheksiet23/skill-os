# Shape and inspect the experience

Use this reference to choose the hardest decision, compose layout and words, and inspect the represented states.

## Start with the task and visual language
- Map entry, user decisions, anxiety or friction, completion and recovery.
- Group information around tasks, not database entities.
- Choose navigation that supports the work. A card dashboard is not the default answer.
- Identify the hardest decision and the observation that would show whether the design supports it.
- Build enough realistic context to make that decision before polishing a family of screens.
- A working click is not enough if the user cannot tell what to choose or what will happen.

| Hard decision | Representative slice | Inspect before expanding |
| --- | --- | --- |
| Choose between similar records | Populated results, distinguishing details, selection confirmation | Can visible evidence distinguish records without opening every row? |
| Commit an expensive or irreversible action | Review, consequence, confirmation, recovery from an uncertain result | Are scope, cost and reversibility clear before commitment? |
| Resolve conflicting edits | Original and current values, conflict choice, preserved draft | Can the user recover work and see which version survives? |

Contrast pair:
- Not this: a polished appointment calendar with empty slots. It does not resolve provider choice.
- This: realistic overlapping availability, location, duration and a fully booked option. Exercise choosing and changing a slot.
- Then: inspect whether selection and consequence stay clear at realistic density. Apply the successful pattern elsewhere.

Alternatives and evidence:
- When alternatives are needed, vary the decision-driving interaction. Do not recolor the same layout.
- Record the observed design issue separately from assumptions about user comprehension.
- An agent walkthrough is not a user study.

## Explore a choice when users must compare its effects
Applies to a consequential choice. Add no preview flow to a routine choice that is already clear.

- Show proposed and committed state distinctly.
- Allow revision or cancellation without committing the business change or sending its notifications.
- Show relevant consequences, assumptions and unavailable data. Do not present a scenario as a guaranteed forecast.
- Include the case where data or permissions change before Apply.
- Final commitment uses the authoritative contract's current validation.

## Resume incomplete work when the domain permits it
Applies where unfinished work is allowed. Where partial work is prohibited, add no draft support.

- Show saving and resuming a draft separately from final submission or approval.
- Preserve permitted entered values. Distinguish unknown from zero, false and not applicable.
- Show what remains required, and how changed access, source records or concurrent edits affect resumption.
- Draft saving never replaces required final validation and never implies approval.
- Keep a direct completion path for a complete task.
- Label simulated persistence and commit behavior. An inspected prototype does not prove durable recovery or server enforcement.

## Compose layout and words together
- Establish a scanning path, clear primary actions, appropriate density, readable measure, consistent spacing and meaningful surface roles.
- Preserve brand and mature patterns.
- Greenfield: fit the audience and task. Avoid a universal pastel palette, a hover-only sidebar or a framework preference.
- Use real domain labels, action verbs and recovery language. Confirmations reflect consequences.
- Use existing customer language and voice guidance. Missing guidance does not require a research project.
- Keep provisional tone distinct from an approved brand change.

## Inspect the represented states
- Exercise long labels, large values, dense results, empty states and permission differences.
- Check small-screen reflow and touch access, and deliberately composed larger layouts.
- Check focus order, keyboard access, contrast and reduced motion.
- Critique actual screens for hierarchy, readability, alignment, density, clipping, feedback and recovery.
- Record viewport, route or state, finding, correction and limitation. Checklists and aesthetic scores do not prove quality.
- Fidelity: implementation preserves the reviewed experience. Reuse styles and assets where appropriate, with framework and accessibility adaptations. Require verified fidelity, not byte-identical markup.
