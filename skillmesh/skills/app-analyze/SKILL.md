---
name: app-analyze
description: Analyze software needs and existing behavior, producing an owner brief with ranked decisions, business-analysis findings and a use-case specification with flows, rules, acceptance and gaps. Use for material product changes, ambiguous defects, modernization or requirements review; skip mechanical fixes, technical architecture design/review and business-demand validation.
---

# App Analyze

Turn an unclear software request into decisions the owner can make and behavior the team can build and verify without consequential guesses. Work from the problem and the people's goals, not from the proposed solution. Write no production code. Choose no architecture.

## Terms
- **Consequential:** changes observable behavior, cost, risk or rework.
- **Authoritative home:** the one document that owns a rule or decision. Others link to it.
- **Increment:** the next coherent slice to specify in detail.
- **Delegated decision:** a choice the owner has said the team may make. A recommended default is not one until the owner says so.
- **Fact:** a value or system detail nobody on the team knows. It has no default. Request it from whoever can supply it.
- **Job:** what a user is trying to get done: their situation, motivation, current workaround and desired outcome.
- **Journey:** the stages a user passes through to get a job done, with the decision and the pain at each stage.
- **Evidence label:** owner-stated, observed or inferred. Mark every job and journey stage with one.

## Always
1. Separate the requested solution, the underlying problem and the desired outcome. Challenge unsupported choices with presented evidence. Supplement what the owner has not said. Then keep the owner's decision.
2. Keep unknown facts unknown. Propose and label; never invent policy, numbers, schemas or guarantees. User needs and experience may be inferred, as labeled hypotheses.
3. Separate observed behavior, inference and intended behavior.
4. Leave architecture and mechanism to design. Record the required guarantee and the design question.
5. Treat a planned check as unexecuted. Writing a document never marks anything Built or Verified.

## Choose the document set
Use existing project records first. Link instead of copying.

| Work | Documents |
| --- | --- |
| Contained correction or single flow | One short record: need, rule, flow with done-check, open decisions |
| One module or feature | Exactly three Markdown files in the application project: owner brief, findings, specification. Rules stay inside the specification |
| Several modules reusing rules, or a second decision-maker (never for one module) | Add a shared product-rules document (see the specification reference) |

When the request is narrower:
- Analysis only: deliver the owner brief and findings.
- Specification only: reuse adequate existing analysis.
- Review only: report findings and leave the reviewed records unedited.

## Establish the boundary
Before specifying anything:
- Recover project instructions, accepted decisions and existing contracts.
- Identify affected actors, entry points and the next useful outcome.
- Material UX or a solution-shaped request: find the job and journey before specifying flows. Users often cannot state what they need.
- Defect: trace its path.
- Broad work: map capabilities and dependencies shallowly, then detail the increment.
- Scope or compatibility choice that could invalidate the work: settle it first.
- Deferred capability: keep it visible and leave its internals unspecified.

When existing behavior matters:
- Read [existing-system evidence](references/existing-systems.md).
- Inspect affected rules with the [requirements lenses](references/requirements.md).
- Load only what applies.
- Reuse evidence only while its source, revision and question still apply.
- Do not treat an existing defect as a compatibility obligation by default.

## Resolve uncertainty
Investigate before asking. Go deeper only where evidence could change the increment or protect existing behavior.

When the owner is in the conversation, ask before writing the documents:
- Send one batch: the decisions needed now and the facts you need.
- Question form: one plain line, your recommended default, what it changes.
- Facts: ask as ordinary questions ("Which phone do you use?"), not as decisions.
- Use the host's question tool if it has one. Otherwise a numbered list in chat.
- Let the owner accept all defaults at once.
- Record each answer as confirmed, with date and decider.
- Do not wait for the owner to read the documents to collect these answers.

Ask the owner only when the answer is consequential. When you ask:
- Include your recommended answer, what it changes and the work it affects.
- Reversible details: decide within your delegation and note them.
- Unrelated questions: record with a revisit condition and keep working.
- Conflicting views: keep both until the assumption or evidence is settled.

When the owner cannot answer now:
- Bundle the open decisions into one ranked set in the [owner brief](references/owner-brief.md), each with a recommended default.
- More than half the High decisions unanswered: leave the flows they block as outlines. Write every other flow in full, marked "on defaults".
- No High decisions: write every flow in full, marked "on defaults".

When a gap needs other expertise (demand, interaction, architecture):
- Name the gap and why, and ask the agent to bring that expertise in. Unevidenced demand or adoption is a gap of this kind.
- The agent decides. This skill invokes none.

When a discovery is worth keeping beyond the increment:
- Record source, tentative reading and a revisit question in existing product records, apart from accepted scope.
- Keep correctness evidence as a dependency.
- Do not retain every curiosity. Do not present a possible benefit as fact.

## Write the documents
**Owner brief** (read [owner brief](references/owner-brief.md)):
- One page, plain language, actionable without the other documents.
- Contents: outcome and measure, why now, decisions needed now, release cut, decision register.
- It is the authoritative home for gaps and decisions.

**Findings:**
- Problem, actors, goals, outcome and agreed scope. Mark accepted versus recommended.
- Jobs and journey, for material UX or a solution-shaped request: each job and journey stage with its evidence label. Treat inferred ones as hypotheses, not accepted scope. Link flows to their stage.
- Current behavior and target changes, with source, revision, environment and evidence limits.
- Candidate use cases: an index of coverage linked to goals and events.
- Contradictions, unsupported solution assumptions and dependencies.
- Assumptions and constraints. For each untested business assumption, its cheapest test.
- Domain risks that need an owner call, linked to their decision.
- Recommended next increment and the limits of the analysis.

**Specification** (read [use-case specification](references/use-case-specification.md)). Flows, rules, alternatives and done-checks that an implementer and tester can use without consequential guesses:
- Keep quality, security, compatibility and failure requirements visible at every depth.
- Express UX, API, data, authorization and deployment constraints as behavior.
- Give each flow one source reference. Name the flow each quality item constrains.
- Done-check: required acceptance, not executed proof. State it once.
- Flow in full: its decisions and facts are settled or have a safe revisable default.
- Flow outline: a High decision with no safe default, or a missing fact that changes its behavior, blocks it.
- Decisions and facts: link them, never copy them.

## Check and hand over
After a decision changes:
- Update the authoritative rule or decision and its links.
- Reopen a settled choice only for changed scope or new evidence.

Before a consequential handoff:
- Confirm a reader can recover current versus target, rules, dependencies and acceptance without this conversation.
- Ask a fresh reader to state the rules back. Resolve any difference in the authoritative document.
- Owner brief test: its reader can say which decisions they can make now.
- Specification test: its reader meets no undefined reference.
- Outside the tracking table, describe content, never readiness ("ready", "specified in full").
- Remove duplicated rules across documents. Keep rationale that changes interpretation.
- Self-review is not independent review.

How the documents are used:
- The specification is the main input to design, prototype, build, QA, release and delivery slicing.
- Findings serve rationale, evidence and scope disputes.
- A specification's existence or flow status does not establish owner acceptance, tested behavior or release authority.
- Do not require a prior skill run. Do not duplicate adequate existing requirements.

Finish at the requested boundary: supported findings, or flows that can be built and verified without consequential guesses.
- One alternative stays blocked: hand over the settled flows separately. Its decision gates others only when a shared dependency blocks them.
- State partial readiness precisely.
- Preserve the release boundary, accepted choices, evidence and gaps for continuation.

**Wording:** be truthful and growth-minded. Say "not yet" where something can still happen, and keep evidence, warnings and results exact.
