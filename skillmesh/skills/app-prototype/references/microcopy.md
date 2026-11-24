# Write interface copy from the actual state

Use this reference when wording defines state, consequence or recovery.

Before editing a string, identify the user's task, the actual system state, the known facts and the supported actions. Then:
- Decide what the message must preserve: validation rules, scope, consequences and uncertainty.
- Treat a shorter message that changes the behavior's meaning as a regression.
- Infer no cause from a generic failure.
- Promise no data safety, payment status, recovery time or progress without supporting behavior or evidence.

## Choose the pattern from the state

| Situation | Useful content | Distinction to preserve |
| --- | --- | --- |
| Field validation | Requirement and how to meet it, next to the field | Match the actual rule. An email containing @ is not necessarily valid |
| Recoverable failure | What failed, known context, supported next action | Retry only when appropriate. An unknown payment outcome needs a status check before another payment |
| Blocking failure | What is unavailable, and the alternative or next step | Give a restoration estimate or reassurance only when established |
| Success | What completed, and any consequential next step | Accepted, queued, sent and delivered are different states |
| First-use empty state | What belongs here, and a useful starting action | Offer creation only when the user can create |
| Completed work | What is complete, and when more work appears if known | An empty list alone does not establish completion |
| No results | Which search or filters found nothing, and how to adjust them | Do not imply the underlying collection is empty |
| Restricted access | What the user can know, and how access can be obtained | Do not expose protected content. Do not disguise a restriction as no results |
| Permission request | Specific benefit, permission needed, available choice | Explain in context. Distinguish optional from prerequisite. Keep platform-owned wording |
| Destructive confirmation | Affected object, scope, consequences, reversibility, explicit action | Keep retention exceptions and recovery windows. Do not exaggerate permanence |

These are prompts for judgment, not mandatory title, body and button formulas. A routine confirmation may need only a short completion message. An unavailable action needs no invented call to action.

## Voice, tone and editing
- Use the project's terminology, house style and voice, especially representative approved strings.
- Examples illustrate choices. They do not prescribe wording or a universal voice.
- When consistency needs clarification, record project-specific contrasts.
- New voice: use known customer circumstances and company values where they resolve a writing choice. Keep proposals provisional and surface conflicts.
- Do not manufacture a brand exercise for a contained correction.
- Keep the voice recognizable and adapt tone to the task:
  - Routine completion: brief.
  - First use: explanatory.
  - Failure: calm and practical.
  - High-stakes choice: explicit about consequences.
- Avoid forced celebration, blame, artificial urgency and guilt for declining. Conversational language need not be casual or less precise.
- Review wording through four lenses: serves the task, loses nothing when words are removed, sounds natural for the audience, has an unambiguous meaning.
- Preserve useful specialist vocabulary.
- Fixed sentence lengths, reading grades and active-voice percentages are not acceptance criteria. Do not truncate essential instructions to meet them.
- Write for scanning. Lead with the meaningful state, outcome or action. Make labels understandable independently.
- If extensive explanation is needed to make a flow usable, reconsider the interaction.

## Check copy in the interface
- Use visible field labels and descriptive actions and links.
- Read labels, helper text and errors together for repetition or missing context.
- Accessible names preserve visible wording. Add hidden context only where needed.
- Alternative text conveys an image's purpose without repeating adjacent content. Decorative images need no redundant announcement.
- Good wording alone does not establish correct semantic association or announcement behavior.
- Localization in scope: test realistic expanded labels, plural and count variants, dates and long values in the represented layouts.
- Avoid idioms and sentence fragments assembled from translated pieces.
- Use actual locale conventions and available translations, not universal expansion percentages.

## Keep the evidence behind the revision
- Inspect the copy in its actual state and layout.
- Record meaningful before and after wording, the rule or evidence preserved, and any unresolved factual dependency, using existing project records.
- Editorial judgment can explain a revision. Comprehension and task-success improvements need observed user evidence.
