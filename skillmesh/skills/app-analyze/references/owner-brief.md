# Owner brief and decision register

The owner reads this and acts on it. Keep it to about two pages.
- Write for a non-technical owner.
- Evidence and rationale: findings. Flows and rules: specification.
- Use the project's own names and any existing record that already holds an item.

## Language
- Use plain business words. Name flows by what they do ("Cancel appointment"), not by code alone.
- Leave out process terms: Specified, Identified, severity labels, frames, skill or agent names.
- Do not point to documents the owner does not have.
- Keep each table cell to one sentence. Move detail to the findings.

## Order
1. **Outcome, measure, why now:** about five lines.
2. **Decide now** and **Later:** the decision register as one table, sorted by rank.
3. **Facts we need:** things only someone else can supply. A short table with an ID (F-1, F-2), a one-line gloss, who supplies it and needed-by.
4. **Release cut.**
5. **Non-goals and decision-makers.**

Rules for the register table:
- Decide now: every decision needed before design starts or blocking a Must flow. At most five, ranked.
- Later: the rest.
- A decision needed before design starts never sits under Later.
- List no decision twice anywhere in the brief.

## Outcome, measure, why now
- Outcome: the user or business problem in one sentence.
- Measure: success measure with baseline and target, or `?`. Never invent a number. Propose a measure and label it proposed.
- Why now: the deadline or trigger, and the cost if missed. If unknown, say so.

## Release cut
- List flows as v1, next or later. Give each a relative size (small, medium, large) and value (low, medium, high).
- Label everything proposed until the owner confirms.
- Must means release-blocking. The owner assigns it.
- Costly capability: name the cheapest viable alternative, such as manual entry in place of automated extraction.
- Build time and cost: write "unknown, needs an engineering estimate" unless evidence exists.

## Decision or fact?
- **Decision:** a choice with a sensible default the owner can accept or change.
- **Fact:** a value or system detail nobody on the team knows. It has no default.
- A default that contains `?` is a fact. List it under "Facts we need".

## Decision register
One row per decision. Other documents cite its reference.

| Column | Content |
| --- | --- |
| Ref and question | Stable ID and the question in the owner's words |
| Decider (consulted) | A role, not a guessed person |
| Needed by | A real date, or a milestone or relative time ("before design starts", "week 2"). Never a placeholder |
| Blocks | The flows that stay unspecified until it is confirmed |
| Default | What the team proposes, and whether it is reversible |
| If wrong | What changes if the default is wrong or the owner picks the nearest alternative |
| Status | Proposed, confirmed, rejected or deferred, with date and decider |

Ranking:
- Must flows blocked, then whether it blocks the release cut, then needed-by.

Severity:
- **High:** no default is safe to proceed on until the owner confirms. Still give your recommended default.
- **Medium:** changes a rule, test or scope, or has a safe default that can be revised.
- **Low:** does not change behavior.
- "Blocks" and severity differ. A decision can block a flow without being High.
- Write no totals ("12 decisions", "7 High"). The table is the count.

Defaults:
- A default is the team's proposal, not accepted scope.
- It becomes a delegated decision only when the owner says so.
- No delegation: write "needs your answer before <milestone>".
- Delegation exists: "we will proceed on this unless you object" is allowed.

Upkeep:
- Confirmed decision: move it into its rule or flow. The row keeps its rationale and standing.
- Unanswered past needed-by: send it to the named decider.
- Raise a gap only when plausible answers change behavior, cost or risk.
- Group unrequested operations (archive, search, import/export) into one question.
