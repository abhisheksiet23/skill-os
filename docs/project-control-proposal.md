# Project control proposal — 2026-11-03

Current status — 2026-11-03: the owner authorized a tailored source implementation after the activity inventory and governance review, followed by a focused refinement of delivery-time upkeep, useful forecasts, work selection and management overhead. Source implementation and bounded local evaluation are complete; [candidate-specific results and limitations](../evals/project-manage-assessment.md) include an initial placement failure and its corrected rerun. Installation, actual application adoption, real billing visibility and project-outcome improvement remain unproved. The proposal and skeptical review below preserve the earlier alternatives rather than describe current authoring state. Financial scope remains **AI/tool spend only**; no human labor cost model is requested. The application is a separate project and has not been changed here.

## The abstract gap

Context continuity preserves facts, decisions and the next action. Project control maintains an accountable relationship between intended outcomes, planned work, actual progress, remaining dependencies and forecasts. A WBS, a list of passing tests and session assessments do not provide that control by themselves.

Observed supporting evidence: the application plan's headline retains its first two increments while a later continuation reports subsequent verified and blocked increments; its WBS enumerates deliverables but the selected records do not expose an integrated schedule/cost forecast. This is evidence of a visibility/control gap in those inspected records, not proof that no other tracker exists. No historical overall completion percentage, spend or delivery date has been reconstructed or invented. Detailed application observations and future control records belong in the application.

PMI's current [PMBOK guidance](https://www.pmi.org/standards/pmbok) covers governance, scope, schedule, finance, stakeholders, resources and risk with tailoring to project context. The proposal applies those concerns proportionately; it does not claim certification, official compliance or that every project needs all possible process artifacts.

## Recommended toolkit boundary

Add one independently usable `project-manage` skill, provisionally named, for establishing/recovering plans, controlling delivery, forecasting and answering status/cost/schedule questions. Its reusable methods belong in SkillMesh. Each project's scope, dates, budget, control records and actuals stay in that project or its existing tracker. Preserve specialist ownership of requirements, design, implementation, verification and release. The agent selects expertise; the new skill does not invoke other skills or become a mandatory lifecycle router.

Keep `project-context` focused on finding and preserving authoritative knowledge. Its map should point to the project's control sources; it should not acquire a second set of schedule/cost calculations. For projects adopting ongoing management, project instructions should require the agent to keep controls current during work, even when the management skill is not loaded on every turn. Use existing adequate trackers and records, one authoritative value for each fact, and a compact current view. Start with ordinary project records; a dashboard is a view over them. Do not introduce a PM platform, synchronization engine or background monitor before a real access/maintenance failure justifies it.

## Actual management activities

| Activity | Work the agent performs | Decision it supports |
| --- | --- | --- |
| Establish direction | Recover objective, release boundary, acceptance, stakeholders/decision authority, constraints and success measures. Reconcile competing scope statements. | What constitutes delivery, and who can decide? |
| Plan deliverables | Adapt the WBS/backlog into work packages with observable completion rules; separate enabling work from delivered outcomes; identify dependencies, responsible party and required inputs. | What remains and what can proceed? |
| Plan schedule | Estimate remaining work in ranges, account for capacity/calendar, external waiting and meaningful sequencing/parallelism. Detail near-term work; keep distant work coarser with explicit uncertainty. Establish authorized milestones/baseline. | What is the next milestone, when is it forecast, and what controls it? |
| Plan AI/tool budget | Define cost boundary/currency, available usage/billing sources, allocation method, forecast assumptions and agreed spending limits. | What can be spent, and what measurement is actually possible? |
| Control execution | Reconcile actual deliverables and acceptance evidence with planned work; record starts/finishes, remaining estimates, blockers, risks and decisions. Update forecasts after material changes. | Are we progressing against the same scope? |
| Control change | Show scope/date/cost/quality consequences of changes; preserve the original baseline and accepted revisions rather than silently moving targets. Resolve changes using existing authority. | Should we change scope, sequencing or investment? |
| Communicate and optimize | Maintain a concise status view, highlight exceptions and recommend the next decision/action. Compare similar completed work to diagnose delay, retries, rework and waste. | What should we do differently next? |
| Close | Reconcile delivered acceptance, unresolved work, handover and final actuals against the agreed boundary. | What is complete, deferred or still owed? |

These are responsibilities to tailor, not a demand to generate a document for every row. Risk and issue records need owners, consequences and useful actions; a list of risks without response ownership is insufficient. Stakeholder communication can be an update to the owner; it does not authorize contacting others. Resource planning includes availability and concurrency constraints even though human labor cost is excluded.

## The project view available on request

Reuse a project's existing status page or tracker; when absent, establish one concise project-owned overview linked to authoritative detail. It should answer:

- As of when and for which scope/candidate is this view current?
- What outcome are we delivering, and which milestone comes next?
- What has met its agreed completion/acceptance condition, what is in progress, and what is blocked?
- What is the remaining path, including prerequisites, external decisions and who owns them?
- What were the baseline milestones/budget, what is the current forecast range, and why did it change?
- What AI/tool spend is measured, estimated or unavailable; what remains forecast; and what is the expected total?
- What action or decision would most improve the forecast now?

Do not require a single overall percentage. If shown, define its denominator and completion rule. Task counts, imported scenarios and local test counts do not establish accepted progress. Use agreed deliverable weighting only when useful and evidence-backed; separate scope coverage and acceptance from implementation effort. A critical-path claim requires a sufficiently defined dependency/capacity model; otherwise identify the current milestone-driving chain with limitations. A newly recovered plan is a baseline from its adoption date, not a fabricated original commitment.

## Time and cost measurement

Maintain baseline, actual and forecast separately. Calendar elapsed time, active execution time and time waiting on external inputs are distinct. Forecast completion from remaining dependencies, capacity and uncertainty rather than multiplying the last task's duration across heterogeneous work. A known unresolved dependency may justify a conditional date or an unbounded upper range. Do not label it late without an agreed comparison date.

For AI/tool spend, distinguish provider-reported charges from usage-based estimates and allocated subscription cost. Capture source, period, currency, model/tool, work package where attributable and coverage gaps. Use available exports/reports or authorized local telemetry; no billing access or usage availability is presumed. Preserve project overhead and unattributed amounts rather than forcing invented task allocation, and deduplicate parent/child agent charges. Subscription allocation requires an explicit rule and must not be represented as marginal per-task billing.

Forecast total = actual-to-date + estimated remaining AI/tool spend, with a range and its assumptions. If actuals are incomplete, identify observed subtotal and missing coverage; do not present the subtotal as total project cost. If no credible spend source exists, report cost unavailable and establish the smallest useful collection method. Token counts alone are not charges; model/rate/version, caching and any other billed usage dimensions matter when calculating an estimate. Chat timestamps do not measure active effort.

PMI's [WBS-to-performance-baseline guidance](https://www.pmi.org/learning/library/earned-value-wbs-performance-measurement-baseline-7465) connects earned value to planned work, schedule and budget. Do not display CPI/SPI or earned-value percentages without a meaningful baseline, defensible completion measurement and actual cost coverage. AI spend alone can poorly represent delivery value. Begin with honest milestone/scope variance, remaining-work forecasts and cost coverage; add earned value only if it improves a decision under valid inputs.

## Operating cadence and optimization

At resumption, recover the current control view and check freshness. During work, update affected facts after accepted scope changes, new blockers, completed work or forecast changes. At coherent closeout/handoff, reconcile the view with evidence and show the next path. Avoid another report after every tool call. Existing project-context assessments remain continuity/method checks, not project performance indicators. Every view carries an as-of time; a skill does not by itself provide unattended monitoring or continuously live billing.

Optimize toward accepted outcomes within cost, schedule, quality and risk constraints. Start with the actual constraint: repeated discovery, avoidable retries, rework, review delay, external waiting or unsuitable work-package size. Explain the expected effect of resequencing, reducing WIP or reusing valid evidence; measure afterward. Less AI spend with more escaped defects is not demonstrated improvement. Do not claim savings from unmatched runs or optimize against unknown cost data.

## Validation before broad adoption

First recover one existing project without inventing its past baseline or changing its agreed scope. An owner should be able to answer current position, next milestone, blockers, available spend and forecast limitations from the control view without rereading chats. Reuse existing WBS/verification records; keep the recovery in the owning application under its authorization.

Test the reusable method on contrasting projects: broad software delivery with blocked dependencies; a short fixed-deadline deliverable; parallel workstreams with capacity limits and scope change; incomplete cost exports/subscription allocation; and a trivial task where formal control adds no value. Check arithmetic, provenance, change history, freshness and authority as well as the usefulness of the status view. Evaluate before/after recovery and maintenance burden; source packaging or dashboard appearance is not proof of control quality.

## Current decisions and next action

Accepted: the owner requests serious project-management capability and first-version AI/tool-spend visibility only. Proposed: independently usable project-management expertise plus project-owned controls and an event-driven maintenance rule. Exact scope of a new skill, any project adoption instructions, budget/date commitments and data integrations have not been approved through this proposal. No new skill or application control records were created. The earlier feedback patch remains local/uninstalled and its abstraction review remains unresolved; this proposal does not silently settle or expand it.

Next useful step: implement the bounded management capability with representative evaluations, then adopt it in the application and recover its first honest current control view. Establish available spend evidence and realistic near-term forecast inputs there. Do not promise an automatic timeline/cost dashboard before those sources are known.

## Skeptical review — 2026-11-03

Scope: owner requested devil's advocacy before implementation. Reviewed the proposal and existing visibility evidence; no new application inspection, cost collection, management skill, project adoption or experiment was executed. This is the author's same-context challenge, not independent review. Owner intent remains improved project control and AI/tool-only cost visibility; the recommendation below does not retract that intent.

The strongest case for management capability survives: someone must reconcile intended outcomes, remaining work, external dependencies and actual evidence, then communicate the current path. The observed stale headline and dispersed newer records justify correcting visibility. They do not, by themselves, prove that a broad new skill is the necessary correction.

### Decisive objections

1. **Visibility failure is not yet proof of a methodology gap.** Existing analysis, WBS, acceptance and continuation guidance produced relevant records. Poor reconciliation, maintenance or presentation can explain the owner's confusion. A new skill that produces another plan may leave the same failure untouched. Inspect which necessary facts are missing versus merely dispersed before deciding what expertise to add.
2. **Instructions do not guarantee operating discipline.** Automatic context upkeep already exists as adopted agent guidance. Another instruction to update controls at closeout shares the same activation/interruption/staleness risks. Management needs named responsibility, one authoritative value per fact, update triggers and visible freshness. A skill can describe these, but its installation does not prove they happen.
3. **Forecasts may be numerically impressive and decision-poor.** Unstable scope, heterogeneous work and unresolved external dependencies can defeat a precise completion date or percentage. Neither a WBS nor two days of work establishes a usable throughput model. Start with the next meaningful milestone and conditional remaining path. Full-project forecast limitations should remain visible rather than be hidden in a nominal range with no supported upper bound.
4. **Cost visibility depends on a data capability we have not established.** No credible project-attributable billing feed/export has been inspected. Usage estimates, subscriptions and provider charges are different measures; task allocation may be unavailable. The skill may truthfully report unknown cost. That is useful diagnosis, but not fulfillment of automatic spend visibility. Test data access before promising this capability. AI/tool spend remains the chosen financial scope; calendar delay and owner decision burden can still be measured operationally without inventing human labor cost.
5. **The management machinery can consume the capacity it seeks to optimize.** WBS refinement, forecasts, risk registers, change records, reporting and session assessments add reconciliation work. Multiple artifacts can disagree even when every individual artifact is sensible. Adding a dashboard does not resolve conflicting authority. Keep only control information that supports an actual decision, and observe its upkeep and owner correction burden rather than assuming more structure saves time.
6. **Baselines can become friction or movable targets.** Early detail can freeze uncertainty into apparent commitments; frequent replanning can erase meaningful comparison. Scope/acceptance needs a stable authority, while remaining-work forecasts should change as evidence changes. Formal change approval should apply to consequential decisions outside existing delegation, not every task adjustment or forecast update.
7. **Visible metrics can optimize the wrong outcome.** Lower spend, more completed tasks or higher test counts can coexist with weaker acceptance and slower delivery. Extra checking may increase AI spend while reducing rework. Choose measures around accepted outcomes, bottlenecks and decision needs; do not let easily collected counts become the objective.

These objections constrain the proposal rather than establish that project management is unnecessary. Concrete management can be warranted while the appropriate packaging, depth and data source remain unresolved. Likewise, the project's current frustration is sufficient reason to improve its own controls now; repeated cross-project failures are not a prerequisite for helping that project. Stronger evidence is needed before imposing broad reusable defaults.

### Smaller experiment and decision rule

Reverse the original implementation-first sequence. Under the application's authorization, recover one concise current control view using its existing records: agreed boundary, evidence-backed completion, in-progress work, blockers/owners, next milestone and conditional remaining path. Add baseline/forecast comparisons only where there is a legitimate baseline; do not reconstruct historical commitments. Inspect available spend sources and show observed amounts, estimates, coverage gaps or unavailable data honestly. Keep the underlying record ownership clear and avoid copying full reports.

Maintain that view through actual meaningful increments, including a blocker/scope change and a resumption when they naturally occur. The owner should be able to explain the project position and next decision without rereading chats. The view should remain consistent with underlying acceptance evidence, survive recovery and identify a real decision or corrective action. Observe update effort, stale fields, duplicate entry and owner corrections. Do not manufacture project work to exercise a rubric.

Predefined outcomes: if consolidation/upkeep of existing records solves visibility, improve that existing practice without a broad new management skill. If planning, dependency analysis, forecasting or change-control reasoning repeatedly supplies missing decisions, extract that expertise into a self-contained management skill and test it on contrasting projects. If actual cost data is inaccessible, solve or explicitly bound that integration separately; more methodology cannot supply it. If updates add burden without decisions or clarity, simplify the controls. Synthetic skill evaluations can test reasoning/arithmetic, but cannot establish real adoption, current billing access or usefulness to this owner.

Verdict: **reshape and pilot; do not implement the full proposal yet**. This supersedes the author's recommendation to build the new skill first, not an accepted owner decision. No additional approval or system architecture is being introduced by this review. The management need is supported; the proposed solution and its promised financial/schedule visibility remain hypotheses. The next useful action is a bounded project-owned control pilot if requested, with toolkit packaging following observed expertise gaps.

Planning continuation: the owner requested a build plan. The [implementation plan](project-management-build-plan.md) sequences project recovery/current visibility, actual controls and measurement, real pilot operation, conditional toolkit extraction, evaluation and adoption. It preserves AI/tool-only cost scope and the skeptical review's pilot-first recommendation. This is a plan, not execution of a new skill or application changes.

Coverage correction: the owner subsequently requested the full PMP activity inventory before further solution work. The [activity inventory](project-management-activity-inventory.md) now separates the 49-process baseline, broader practical responsibilities and current PMP domain/task coverage. Reassess this proposal and the build plan after that discipline review; no implementation choice is inferred from the inventory.

Implementation decision: following the inventory and AI-led minimum-governance tailoring, the owner explicitly authorized changing Skill OS. Source implementation now follows that tailored selection; it supersedes the proposal's provisional recommendation to defer all skill authoring until a live pilot. No application controls, billing integration, purchase or installation are implied. The original broad proposal is not adopted wholesale; the deliverable is independently usable management reasoning with proportional activation and compatible current-record maintenance.
