# SkillMesh: human-readable outputs — implementation plan

Finalized: 2026-09-25  
Scope: implement and evaluate narrow improvements to skill outputs when this plan is submitted as an implementation task. This planning session has not modified skills.

## Objective

Make each skill's result easy for a human to understand, assess and act on, with minimal reading effort and concise but meaningful text.

Preserve SkillMesh's breadth: product management, project management, apps and websites; multiple projects within a product and multiple distinct products. Improve output philosophy within the owning skills. Develop our own formats only where needed.

## Settled decisions

- Explain consequential findings with evidence, meaning and implications.
- Choose the best representation for the information; no universal report format.
- Keep recommendations, accepted decisions, assumptions and verification distinguishable.
- Reuse adequate project records and preserve prior answers.
- Keep app, website, prototype, code or model primary when it is the requested result.
- Make a substantive result durable when review or continuity needs it; do not create a document for every run.
- Borrow no application-specific formats, governance, folder structures or workflow from the reference toolkit.
- Do not add a reporting skill, central formatting dependency, registry, runtime, shared-state schema or required sequence.
- No mandatory HTML companion, fixed section count, word quota or blanket changes to every skill.

These choices are settled for this task. Proceed with reasonable reversible authoring decisions; do not wait for the owner to select headings, approve examples or revisit these principles.

## Basis and limits

The owner prefers the reference toolkit's concrete, reviewable outputs. Its reports connect findings, consequences, changes, decisions and evidence. However, that toolkit has deep knowledge of one application and multi-round reports. Our saved efficiency exercises impose a 350-word cap and often request only an approach. The comparison does not establish causation.

The exact installed versions behind the disliked runs are unknown. This task targets the maintained authoring library, not installed copies. Do not diagnose an installation defect without evidence.

The original archive and desktop conversation are not required inputs. This plan contains the transferable observations. Do not retrieve private application material or depend on Windows paths. If actual liked/disliked outputs are available in the checkout, use them as context; their absence does not block the work.

## Output philosophy to apply

Use this as intent, adapting wording to each skill rather than pasting it everywhere:

> Make the result understandable and reviewable for its intended reader. Explain consequential findings or choices with concrete evidence, why they matter, and the decision or action they support. Distinguish recommendations, accepted decisions, assumptions and verification. Choose the form and depth that fit the task and its product/project context; reuse adequate records and preserve prior decisions.

Optimize the reader's effort, not word count alone. Remove repetition, generic introductions, tool-call diaries and empty sections. Preserve explanations and qualifications that change interpretation. Avoid dense fragments, unexplained abbreviations and prose compressed into jargon.

Lead with the outcome and important implication. Give enough supporting substance to inspect the conclusion. Keep critical limitations near their claims; link detailed evidence rather than copying it repeatedly. A short final message must still tell the user the result, even when it links a larger artifact.

| Information | Preferred starting point | Avoid |
| --- | --- | --- |
| Outcome or recommendation | Short opening statement | Repeated summaries |
| Cause, rationale or implication | Connected prose; an example if useful | Dense paragraphs or disconnected fragments |
| Comparable options/attributes | Compact table | Wide tables and paragraphs inside cells |
| Independent findings/actions | Short bullets in priority order | Deep nesting |
| Sequence or timing | Numbered steps or a meaningful timeline | Invented mandatory phases |
| Relationships/dependencies | Small diagram when clearer | Decorative complexity |
| Quantities/trends/sensitivity | Chart with units and evidence | Invented precision |
| Visual experience | Actual prototype, screenshot or annotation | Describing an unseen result as verified |

Use a mix only when it helps. Tables are encouraged for real comparisons, not as the default for every paragraph. Existing user/project format preferences take precedence over suggested shapes.

## Preserve product and project boundaries

Distinguish these scopes when relevant, without creating a new schema:

- **Product:** opportunity hypothesis, customer problem, differentiation, outcome and learning evidence.
- **Project/initiative:** bounded scope, exclusions, dependencies, resources, cost/timeline estimates and commitments.
- **Delivery surface:** app, website, service or shared component and its implementation/verification.

Connect supported implications across them. For example, differentiation can affect an app workflow, a website promise and delivery effort. Do not invent scope to complete that story.

Retain shared product decisions through multiple projects without duplicating authority. Keep project-specific estimates and facts separate. Never carry one product's facts into another.

Strategy Canvas factors and scores need a stated evidence or hypothesis basis. Separate current alternatives from the proposed curve and explain eliminate/reduce/raise/create trade-offs. Differentiation is not demand proof.

For cost, scope and timeline, show relevant assumptions, estimate ranges, capacity and dependencies. Distinguish effort from elapsed time and estimates from commitments. Business economics does not substitute for a project budget. If a complete estimation/scheduling capability is missing, record the gap for later; do not add a new methodology or skill within this output-quality task.

## Authoring scope

Inspect all 18 maintained skill entrypoints using the catalog first. Change only skills with an actual output-guidance gap. Preserve strong existing instructions and replace weak/redundant wording instead of appending a generic block.

| Area | Skills to inspect | Output intent |
| --- | --- | --- |
| Opportunity and strategy | venture-investigate, market-research, business-challenge | Evidence-backed hypothesis/assessment, differentiation, consequential uncertainty and decision |
| Learning and commercial choices | business-validate, business-pricing, business-model | Experiment/results, comparable options or transparent model with assumptions and implications |
| App analysis and experience | app-analyze, app-prototype | Explained proposal or inspectable experience, scope, important choices and acceptance |
| App implementation | app-frontend, app-backend | Delivered behavior, consequential choices, actual integration/proof and remaining work |
| App verification and release | app-qa, app-deliver | Prioritized findings or actual release state, evidence and actionable dependencies |
| Website direction | website, website-discover, website-create | Coherent offer/story, evidence, page implications and inspectable creative direction |
| Website delivery | website-build, website-review, website-deliver | Delivered journeys, buyer/visual/functional findings, real verification and practical handoff |

Allowed source changes:
- Relevant files within `skillmesh/skills/<owning-skill>/`.
- Evaluation tasks, rubric and honest results under `evals/`.
- A concise implementation assessment in `docs/`; README/catalog changes only if behavior descriptions need reconciliation.

Prefer a few inline lines. Add a small original example or local reference only when a concrete recurring need warrants it; link it with a relevant read condition. Keep skills self-contained. This plan is authoring context, not a required runtime reference for skills.

Do not modify global/installed instructions, deployment configuration, application repositories or plugin discovery names. Do not install, publish, merge, contact others or create external resources as part of this task.

## Execution sequence

1. **Inspect and establish baseline.** Read repository instructions, README, SKILLS.md and relevant source. Preserve baseline skill versions in an ignored isolated evaluation area before editing. Record which instructions already satisfy the objective and where a narrow correction is justified.
2. **Prepare matched tasks.** Create self-contained synthetic fixtures for the cases below. Keep expected facts separate from task inputs. Use the same task, evidence, tools, model settings and output request for baseline and candidate. Do not impose the old 350-word cap on substantial-output cases.
3. **Run a baseline when fresh execution is available.** Use fresh evaluator contexts rather than an author pretending to be the baseline. Independent evaluation agents may be used for these bounded cases when available. Give them only the task, raw fixture and assigned skill variant, not desired conclusions or competing outputs.
4. **Draft the smallest changes.** Apply the settled philosophy in the appropriate skills. Do not turn explanation guidance into additional user questions or approval gates. Improve representation and substance together while preserving task scope.
5. **Evaluate the candidate and revise.** Use matched fresh runs. Inspect actual artifacts, claims and reader-facing results. Keep well-supported improvements; remove additions that only increase length, ceremony or repetition.
6. **Check the final library and record evidence.** Run portable checks below and available skill validators. Record changed/unchanged skills, rationale, representative comparisons and limitations.
7. **Leave a reviewable result.** Finish with source changes, evidence and a short final summary linking representative results. User satisfaction remains pending owner review; do not fabricate approval or wait for it during the unattended task.

Do not require every skill to change. A supported partial set of edits is preferable to an untested uniform rollout. Preserve useful existing records; do not rewrite unrelated instructions.

## Representative evaluation cases

Use bounded fixtures; no live market research, customer contact, paid services or production systems are needed.

| Case | Required challenge | Evidence to examine |
| --- | --- | --- |
| Opportunity and Strategy Canvas | Supplied customer/competitor evidence includes a weak assumption and unknown factor | Explanation of opportunity, supported comparison, explicit uncertainty, useful next learning decision |
| Product with two projects | App and website share a product decision, but have different scope, estimates and dependencies; follow-up changes one decision | Shared decision preserved, local estimates separate, meaningful cost/scope/timeline trade-offs, no invented commitments |
| Backend implementation and review | Small executable fixture, behavior change and regression affecting another consumer | Actual implementation/test evidence; concise explanation; review distinguishes defects from an unavailable integration check |
| Website experience/review | Local page or prototype with representative content and an observable journey | Reader can inspect the experience and understand prioritized findings; unavailable browser evidence stays unknown |
| Different product | A fresh unrelated brief following the multi-project case | No inherited facts, budgets, conventions or decisions |
| Restraint | Tiny correction and chat-only request | Direct useful result without an unnecessary report or workflow |

Synthetic fixtures are inputs for genuine task execution, not a license to fabricate execution results. Run changed methodology across more than one relevant case before claiming a repeated benefit. Repeat any surprising or contradictory result when feasible; do not claim general superiority from one run.

Do not build a general evaluation platform or new API integration. Reuse available evaluation tools. If fresh model/agent execution is unavailable, complete the source changes, task fixtures and static/manual assessment; explicitly mark matched behavioral evaluation unavailable. Never present hand-authored examples as baseline/candidate runs. Leave changes review-ready but behaviorally unverified where necessary.

## Assess outcomes, not formatting compliance

Retain existing evidence, scope, selection, contradiction and stopping checks. Add only missing reader-focused criteria to the current rubric:

- Can the reader find the outcome and understand its consequence quickly?
- Is the text concise but meaningful, with the best representation for each information type?
- Can consequential claims be checked, and decisions distinguished from assumptions?
- Can the reader compare choices and identify the next action without reconstructing the investigation?
- Do revisions preserve decisions and product/project boundaries?
- Does the response stay proportional, without report inflation or missing essential detail?

Use the repository's 0–2 scale where helpful, explaining observed differences. A file, heading, table or longer response earns no credit by itself. Unsupported claims, lost decisions, fabricated checks or scope expansion outweigh presentation gains.

Record owner satisfaction as **pending**, not passed. Record token/time/cost metrics only if actually available; otherwise unknown. Distinguish static validity, executed fixture checks, model-output assessments and human preference.

## Validation and completion

From the repository root, using Python 3.10+:

```sh
python3 scripts/validate_library.py
python3 -m unittest discover -s tests -v
```

Use `python` if that is the available interpreter. Apply the repository's command wrapper when available. Run applicable skill validation if its tool is present; record absence rather than installing unrelated dependencies. Windows-only migration tests and installation are outside this source-authoring task.

Before finishing:
- Confirm required references stay inside their owning skill and discovery descriptions remain accurate.
- Inspect the diff for repeated boilerplate, unintended requirements and unrelated changes.
- Check representative output links and any rendered artifacts actually produced.
- Ensure evidence distinguishes observed improvements from hypotheses and unexecuted checks.

Deliver:
1. Focused source changes, with no requirement to touch all 18 skills.
2. Reusable bounded evaluation tasks and actual results/limitations.
3. `docs/deliverable-quality-assessment.md`: concise rationale, comparisons, checks and remaining gaps.
4. A short final response naming the outcome and linking the best representative artifacts.

If a tool or optional input is unavailable, continue unaffected work and state the precise limitation. Pause only work requiring genuinely missing authority or a material product decision beyond this scope. Do not ask routine formatting questions.

## Cloud handoff

This file must be present in the cloud checkout or supplied with the task. Desktop-only files and installed tools are not prerequisites. Follow applicable repository instructions; if a referenced local Windows file is absent, report that fact and continue under the instructions available in the checkout without claiming to have read it.

Task prompt:

> Implement docs/deliverable-quality-plan.md. Read AGENTS.md and SKILLS.md first. Improve the maintained skills' human-readable output philosophy across product/project management, apps and websites, using the smallest justified edits. Choose task-appropriate formats, minimize cognitive load, and preserve evidence and scope. Run representative matched evaluations where tools permit and the portable repository checks; label unavailable proof honestly. Complete the work without routine clarification and leave a reviewable diff with docs/deliverable-quality-assessment.md. Do not install, publish or merge.

Current status: plan finalized only. No skill changes or behavioral evaluations have been performed in this planning session.
