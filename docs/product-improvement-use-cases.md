# Skill OS product improvement: use cases and tasks

Version 0.6, 2026-11-16. Analysis baseline: `a402cfe`. T-01/T-02, including the owner's feedback-to-reference clarification, were committed as `a89c815`; T-03 assesses those unchanged sources at `main`, `4fbf4cbdc715a73d07f59ca36b433e8e8220bfb4`. T-04 has begun an exposure/evidence review; natural eligible use is not yet confirmed. The later Claude packaging commit is outside this selected verification scope. **Depth:** Standard for the selected first increments; Sketch for conditional later opportunities. Skill OS and SkillMesh name the same product, which uses its own skills to develop itself. This is its behavioral specification and work breakdown, not an application UI/API specification.

**Analysis and intent:** [App Analyze findings](opportunity-roadmap.md#app-analyze-findings-and-readiness) and the [product improvement plan](opportunity-roadmap.md#skill-os-product-improvement-plan). Existing [evolution policy](../EVOLUTION.md) and project instructions remain authoritative until changed within authorization.

**Current authority:** the owner authorized T-01/T-02, their completed commit/push, T-03 verification and now T-04 observation/evidence collection. Available exposure checks and existing record maintenance are in scope. Installation, new application work, release and later backlog implementation are not implied. T-03 retains its candidate-bound proof; T-04 needs actual eligible exposure and cannot create it by relabelling synthetic tests. `Specified` means behavior is defined for handoff, not accepted delivery, verified behavior or permission to execute.

## Task backlog

Priorities are recommended delivery priorities, not commitments to implement every opportunity. T-01/T-02 source increments are implemented; verification and later-use boundaries are distinct below. **Conditional** tasks are retained opportunities, not a hidden prerequisite chain. Shared acceptance belongs to the referenced flows/rules rather than a second task-specific checklist.

| Task | Outcome / action | Route / priority | Dependency and done-check |
| --- | --- | --- | --- |
| T-01 Clarify Skill OS product evolution | Compile owner product/bootstrapping intent and proportionate learning choices into existing README/EVOLUTION paragraphs | Direct build; Implemented | README/EVOLUTION updated; document/link/identity and semantic-preservation checks complete. UC-01.M and A1-A4, R-01/R-02/R-05/R-06 covered by source review and scoped policy decision exercises; ordinary-use benefit remains unproved |
| T-02 Add suggestive prototype selection guidance | Revise the existing app-prototype component paragraph; author its optional owning reference, including the established-library preference and escape routes; reconcile overlap only where needed | Direct build, then observe; Source implemented | Paragraph/reference authored for UC-02.M and UC-02.A1-A5, R-03/R-04/R-05. Candidate-bound checks and limits: [checkpoint](toolkit-session-assessments.md#current-toolkit-checkpoint). Deployment and ordinary-use benefit remain unproved |
| T-03 Verify the selected source candidate | Preserve baseline, check semantic coverage and representative behavior, inspect affected consumers and validate source/reference/package integrity | Complete for selected source; 2026-11-16 | UC-03.M/A1-A3 covered by final-candidate comparison, feedback-copy edit, missing-reference recovery, independent source/output review and structural checks; [verification evidence](toolkit-session-assessments.md#selected-candidate-verification) owns identity, coverage and limits. No rendered application, deployed identity or benefit proof |
| T-04 Observe eligible use and collect benefit evidence | Establish candidate exposure and comparison boundary, then capture actual pattern-choice/rework observations in existing records | Started; owner selected next natural prototype task | Exposure/evidence check executed; checked cache differs from candidate and lacks the map. No eligible-use record confirmed in the inspected sources; actual total use is unknown. [Current observation boundary](toolkit-session-assessments.md#t-04-exposure-and-benefit-observation) records evidence, comparison limits and owner-selected dependency under UC-04.A1/A2 and R-07 |
| T-05 Review the benefit and choose the next action | Assess observed outcomes, upkeep and alternative explanations; retain, revise, remove or leave benefit inconclusive | Benefits review; Conditional on relevant evidence or a guardrail regression | Depends on available T-04 observations, not a manufactured usage quota. Done: UC-04.M/A1-A4, including an honest inconclusive result when warranted |
| T-06 Improve a focused project map/example where needed | Identify a real unfamiliar-code navigation difficulty; repair the smallest useful existing map or link one working path | Observe, then bounded direct improvement; Conditional | G-02 must identify the owning project/task. Done: fewer wrong paths/repeated retrieval on relevant use, or an explicit inconclusive result; adequate existing maps are reused |
| T-07 Repair a contract/traceability gap | Locate a specific ambiguity, stale authoritative link or missed use-case-to-check connection; repair it at its owning source | Bounded direct fix; Conditional | G-02. Done: affected behavior/API/check can be traced without conflicting authorities; verify the affected correction, without a new duplicate matrix |
| T-08 Extract a useful domain pattern | Identify meaningful actual reuse; decide whether composition/extraction serves the work and implement only that bounded pattern | Ordinary work as evidence, then direct build if useful; Conditional | G-02. Done: real consumers preserve their behavior with understandable variation points; reject an abstraction that requires awkward exceptions |
| T-09 Make a recurring verification boundary executable | Select a consequential check repeatedly performed manually; integrate it into the existing project runner | Bounded direct build; Conditional | G-02. Done: the check executes the required boundary reproducibly, catches the relevant failure where feasible and preserves real integration/visual evidence requirements |
| T-10 Evaluate one rendered-state example | Identify an actual state/documentation gap, check existing examples, and test whether one example prevents a consequential integration/visual error | Verify need first; Conditional | G-02. Done: a supported build/defer decision with creation/upkeep included; no comprehensive gallery is implied |
| T-11 Diagnose a skill-discovery/loading failure | Inspect actual irrelevant loading, missed expertise or repeated reading; choose a bounded description/reference correction or defer structural change | Observe/targeted verification first; Conditional | Requires a real source-bound trace, G-02. Done: specific failure and correction/deferral are supported without weakening expertise or creating a routing runtime |

T-01 and T-02 are separate coherent outcomes; T-03 can verify each candidate when ready. T-04/T-05 do not block an otherwise correct direct-build increment merely because long-term benefit is unobserved. Actual exposure may require separately authorized installation; writing a source candidate does not establish exposure. There is no current task to revive A2UI or build a registry/runtime.

## Shared product baseline

### Actors, objects and events

| Actor | Goal / authority |
| --- | --- |
| Owner | Sets product direction, preferences and task scope; boundaries beyond authorized T-01/T-02 implementation, T-03 verification and T-04 observation remain binding |
| Codex working on Skill OS | Selects useful expertise, analyzes opportunities, chooses proportionate work within authority, authors/verifies when permitted and preserves evidence |
| Codex using app-prototype in an application | Designs an inspectable experience against that project's actual task, constraints and adequate existing decisions |

Relevant objects are an opportunity/hypothesis, an authorized work item, an authoring candidate/reference, an application design decision and source-bound usage evidence. These are concepts in existing records, not new database entities or mandatory schemas. An idea/feedback event invokes UC-01; a genuine prototype choice invokes UC-02; an authorized source change invokes UC-03; eligible use or a material regression invokes UC-04.

### Shared rules

- **R-01 Authority and ownership:** keep owner intent, recommendations, assumptions, implementation and proof distinguishable. T-01/T-02 implementation, T-03 verification and T-04 observation are authorized; this does not authorize other backlog implementation or new application work. Agent orchestration remains native; skills do not invoke other skills. Local authoring does not authorize installation, release, external communication, spending or application changes outside the task.
- **R-02 Proportionate learning:** choose verify-first, direct-build/observe-later, ordinary-use observation or defer/reshape/stop according to the consequential uncertainty and investment. Do not require every idea to run an experiment or every task to load every specialist. Preserve EVOLUTION's stronger evidence conditions for new ecosystem mechanisms. Direct build is not an exemption from R-05.
- **R-03 Prototype suggestions:** start with the user's task and adequate established design. Consult the optional map when uncertainty could change the interaction-pattern choice. Entries describe candidates, conditions, limitations and alternatives, not a permitted-component list. No mandatory catalog consultation or new catalog artifact for every prototype.
- **R-04 Existing systems and library preference:** preserve adequate existing project components/conventions. For new UI lacking an adequate system, prefer an established library that fits actual stack, accessibility and visual constraints. This is not a universal vendor, automatic install/migration rule or guarantee of savings. Reuse, compose, extend or create as task fit requires, preserving accessibility and required behavior. Record consequential choices in adequate existing application artifacts.
- **R-05 Verification and compatibility:** preserve intended semantics, safeguards, exceptions and conditional loading. Substantive skill changes receive representative before/after evaluation and affected structural/consumer checks. Existing accurate contracts/decisions are not reopened without cause. Instruction verification, application acceptance, benefit evidence and deployed candidate identity are different claims.
- **R-06 Self-contained expertise and project boundaries:** keep the proposed reference inside app-prototype. It must work without sibling skills or a runtime. Company/app facts, library versions, decisions and raw behavior/usage evidence stay in their owning projects. Retain only authorized reusable lessons in Skill OS. No parallel authority, duplicate tracker or mandatory document tree.
- **R-07 Honest benefit observation:** primary map benefit is less avoidable rework caused by an unsuitable interaction-pattern choice among eligible decisions where guidance was consulted. Distinguish that from wiring defects, harmless exploration, map loading and owner preference. Record actual exposure, source/candidate/environment, corrections and known preparation/upkeep. Use comparable baseline evidence only when valid; otherwise movement is unknown. Provider usage/cost is unknown unless measured; reads/word counts do not establish billing. Preference-backed retention may be justified without a speed gain, but must not be labelled measured savings.

### Sparse coverage and applicable constraints

| Object / concern | Applicable behavior | Confirmed exclusions for this increment |
| --- | --- | --- |
| Product direction and opportunity | UC-01; existing records retain decisions/evidence and next action | No new registry, product database or mandatory lifecycle |
| Prototype selection guidance and application decision | UC-02; conditional retrieval and project-owned design output | No replacement of adequate designs, universal vendor or required UI runtime |
| Authoring candidate and proof | UC-03; source-bound verification and ordinary repository history | No installation/deployment by implication; no app/database migration |
| Eligible-use observation and learning decision | UC-04; existing records, R-07 | No invented users/measurements, automatic monitoring or forced usage campaign |
| Accounts/API/storage/security infrastructure | Existing project boundaries remain applicable through R-01/R-06 | No new accounts, API endpoints, persistence schema, CRUD/search/export UI or permission system is required by these instruction changes |

## Selected use cases and done-checks

### UC-01 Handle a Skill OS improvement opportunity

**Actor:** Owner/Codex. **Trigger:** idea, feedback, preference or observed failure. **Priority:** recommended Must for the selected product-framing increment. **Precondition:** actual task authority and relevant existing decisions are recoverable.

**UC-01.M Main**
1. Codex retrieves the supported need, relevant existing method and source-bound evidence without repeating adequate prior work.
2. Codex identifies the intended outcome and the uncertainty that could change the next investment.
3. Within authority, Codex chooses a learning route under R-02, names the deciding reason and retains an appropriate observation/quality boundary.
4. Codex advances authorized work or records the bounded next task, keeping accepted intent and unverified benefit distinct.

**Done when:** README/EVOLUTION identify Skill OS and SkillMesh as the same product and bootstrapping as using its own skills to develop that product, while preserving R-01/R-02/R-05/R-06. A reader can distinguish a cheap reversible direct improvement, a decision-critical premise needing prior verification, and a deferred opportunity without inferring a mandatory specialist chain, a second product or an experiment gate.

- **UC-01.A1 Planning hold or unavailable execution authority:** record/specify the next work; do not implement, install or claim completion. T-01 and T-02 were separately authorized; other backlog work still requires applicable authority.
- **UC-01.A2 Missing evidence affects only one premise:** identify its precise dependency; preserve unknowns and advance unrelated settled work. Missing cost evidence cannot become a fabricated saving.
- **UC-01.A3 Low value, contradicted premise or adequate existing solution:** defer, reshape, stop or reuse with a reason/revisit condition; do not manufacture a feature merely to keep the opportunity active.
- **UC-01.A4 Mechanism escalation:** a proposed registry/shared-state/runtime remains subject to EVOLUTION's stronger evidence, even though small expertise improvements can be built directly.

### UC-02 Select a prototype interaction with suggestive guidance

**Actor:** Codex using app-prototype. **Trigger:** an authorized prototype task with an interaction-pattern decision. **Priority:** recommended Must for the prototype increment. **Precondition:** adequate behavior/task and actual project design constraints exist; unsupported product behavior stays a gap.

**UC-02.M Main**
1. Codex recovers the user task, actual content/states, adequate accepted design and suitable existing components.
2. If a pattern choice is uncertain and guidance could change it, Codex retrieves the owning suggestive reference under R-03.
3. Codex considers candidate patterns and their limitations against the actual task; it may reuse, compose, extend or create under R-04.
4. Codex preserves required states/accessibility, develops the prototype within task authority and records consequential choices/mappings in existing design artifacts.

**Done when:** the app-prototype paragraph conditionally exposes a self-contained reference; a reader can choose differently from its suggestions for a concrete task-fit reason, preserve an adequate design without extra analysis, and identify the selected pattern's consequences without requiring a sibling skill, preferred vendor or new catalog file. Existing prototype rendering/interaction verification obligations remain intact.

- **UC-02.A1 Adequate design or settled component choice:** use it; the map is not a reason to reopen the decision or add a consultation step.
- **UC-02.A2 No suggested pattern fits:** compose/extend/create a suitable domain interaction with required semantics/accessibility; no map-specific approval is required.
- **UC-02.A3 New UI without an adequate component system:** apply the established-library preference to actual project constraints, without automatically installing packages or migrating a framework.
- **UC-02.A4 Component state/API is unavailable, unsupported or stale:** verify the actual project/component contract, use a fitting alternative or surface the affected gap; do not base a prototype on nonexistent states. Continue unrelated work.
- **UC-02.A5 Optional reference fails to load:** preserve the task and existing guarantees using other adequate evidence, report the broken reference and do not imply the map was consulted. Source/package repair is required before claiming T-03 complete.

### UC-03 Verify a changed Skill OS source candidate

**Actor:** Codex author/verifier. **Trigger:** an authorized bounded T-01/T-02 candidate. **Priority:** Must under repository policy. **Precondition:** baseline and changed candidate can be identified; changed behavior and applicable constraints are known.

**UC-03.M Main**
1. Codex maps old/new semantic coverage, including safeguards, exceptions and loading conditions.
2. Codex selects representative baseline/candidate cases: an uncertain routine pattern choice; long narrative content or a new composition; and an adequate accepted design that must remain settled. Include the contrast between preserving an existing component system and preferring a fitting library for genuinely new UI.
3. Codex executes relevant behavioral comparisons and affected structural/reference/consumer checks; it identifies the source/environment and actual result.
4. Codex corrects consequential regressions within authority, reruns affected checks and records source readiness separately from benefit and installation.

**Done when:** no known consequential semantic loss or unjustified restriction remains in the selected scope; the proposed reference is reachable/self-contained; cases can demonstrate useful suggestions and justified departure without reopening settled work; changed source and affected checks are identified. Intended future checks are not reported as executed, and source validation does not claim host deployment or economic benefit.

- **UC-03.A1 Evaluator/environment fails:** diagnose the failed test delivery, retain its limit and rerun only affected proof when available; it is not automatically a product defect or hypothesis failure.
- **UC-03.A2 An authoring candidate contradicts owner intent or a known invariant:** revise or retain the prior behavior; do not revise acceptance merely to pass the candidate.
- **UC-03.A3 Installation/release is not authorized:** hand over the source candidate and exact proof boundary without installing or claiming active-host behavior.

### UC-04 Observe benefit and choose the next product action

**Actor:** Codex/owner. **Trigger:** actual eligible use, a planned evidence review or material guardrail regression. **Priority:** required when making a benefit claim; observation timing depends on real exposure. **Precondition:** the candidate actually used and the intended observation can be identified, otherwise apply A1/A2.

**UC-04.M Main**
1. Codex establishes actual guidance exposure, task context and the relevant comparable baseline if available.
2. In the owning project record, Codex captures the decision and any subsequent correction attributable to poor pattern fit, separately from ordinary implementation bugs, preference and test-harness failures.
3. At a useful review, Codex evaluates R-07 evidence, quality/innovation guardrails and available preparation/upkeep against the intended outcome, preserving alternative explanations.
4. Codex records a supported retain/revise/remove/defer decision within authority; any next implementation respects its current scope.

**Done when:** the next product decision states what was actually observed, whether intended movement is supported or unknown, the remaining limitations and the reason for retention/change. It must permit an inconclusive outcome and preference-backed retention without claiming speed/cost savings. It must not require another test merely because the first result was unfavorable.

- **UC-04.A1 No eligible use or uncertain candidate exposure:** benefit remains unobserved; do not count installation/file presence as use or manufacture tasks to fill a quota. G-03 applies.
- **UC-04.A2 No valid baseline, provider metrics or enough comparable observations:** preserve unknown movement/cost and use the evidence only for its actual scope. G-01 applies; correctness or a bounded owner preference can still support retaining an inexpensive improvement.
- **UC-04.A3 Material task-fit/accessibility/authority regression:** address the affected behavior when authorized without waiting for a scheduled benefit review or expanding unrelated work.
- **UC-04.A4 Useful local result with uncertain transfer:** retain locally or test a specific new premise when relevant; do not promote it to a universal catalog, workflow or savings claim. Development feedback also informs the owning component-selection reference: compile transferable lessons into affected suggestions, limitations or examples with conditions and evidence limits when source changes are authorized; otherwise preserve a proposed correction in the existing project handoff. Raw feedback/application facts stay project-owned; no transcript or new tracker is required.

## Flow and constraint tracking

`Specified` rows define the analysis handoff only. T-01's policy source is Built and document-checked; T-02's paragraph/reference are Built in authoring source. Neither status establishes application acceptance, deployment or benefit. Candidate-bound verification and its limits live in the [checkpoint](toolkit-session-assessments.md#current-toolkit-checkpoint); earlier application trials do not verify these source changes. Priorities below express the selected increment and existing guarantees.

| Flow / applicable constraint | Priority | Evidenced status |
| --- | --- | --- |
| UC-01.M and A1-A4 | Must for T-01 | Built in README/EVOLUTION; document/semantic review complete; live behavioral verification not claimed |
| UC-02.M and A1-A5 | Must for T-02 | Final-candidate instruction exercises and independent review cover suggestions, departure, settled choice, library preference, unsupported capability and missing-reference recovery; no rendered prototype proof |
| UC-03.M and A1-A3 | Must for changed selected source | Complete at selected source boundary: exact snapshots, semantic/consumer review, executed comparisons and package checks; harness-only faults corrected without changing acceptance; no installation or benefit proof |
| UC-04.M and A1-A4 | Required for benefit claims; conditional exposure | T-04 exposure review executed under A1/A2; M's actual-use/correction collection awaits an eligible task. A3/A4 have no new real-use evidence; G-01/G-03 remain open |
| R-01 Authority / R-06 ownership and self-containment | Must throughout | Specified; preserved existing obligations |
| R-03/R-04 task fit, innovation and compatibility | Must for prototype increment | Implemented in the T-02 source candidate; verification limits in checkpoint |
| R-05 verification / R-07 evidence honesty | Must where applicable | Specified; benefit and deployment unproved |
| T-06-T-11 application-specific scopes | Conditional | Identified, not implementation-ready until G-02 is resolved for the selected item |

## Gaps and future dependencies

This is the authoritative gap location for the analysis/specification pair. None of these gaps blocks writing/verifying the bounded T-01/T-02 source candidate once implementation is authorized.

| Gap | Question / current limit | Affected work / consequence | Next resolution |
| --- | --- | --- | --- |
| G-01 Benefit comparison and economics (M; data/quality) | Comparable pattern-correction baseline, recurrence/upkeep and provider billing are not established | T-04/T-05; prevents quantitative savings/ROI conclusions, not a bounded direct build | Codex captures valid available evidence in real eligible use; owner feedback remains separately labelled; otherwise retain unknown |
| G-02 Conditional task context (M; actor/data/rules) | No specific owning project, recurring failure or candidate is selected for T-06-T-11 | Those tasks remain identified opportunities; no implementation scope or estimate can be invented | Select an actual relevant task/evidence, then define only its consequential contract and checks |
| G-03 Review trigger and actual candidate use (M; events/environment) | T-04 found no confirmed eligible-use record in inspected sources; checked cache lacks the map. Active-host exposure and actual total use remain unestablished. Three natural uses remains a proposed early review trigger, not proof or quota | Actual-use collection and T-05 benefit attribution await exposure; missing observations are inconclusive, not failure | Identify the next real task and the source actually consulted; direct authorized authoring-source use can establish exposure without installation. Keep evidence in its owning project; react earlier to material regression. No automatic monitor or install implied |

**Authority boundary:** T-04 observation is authorized under R-01; new application work, installation and later backlog implementation are not implied. **Forecast:** no delivery date, task-duration estimate or provider budget is established. **Handoff:** T-03 remains complete. T-04 exposure review and collection boundary are recorded; actual-use collection remains pending the first confirmed eligible task. T-05 awaits relevant evidence, and T-06-T-11 require their own concrete context.

## Change boundary

Version 0.1 created the specification/task backlog under the owner's App Analyze request. Version 0.2 recorded T-01 implementation and the narrower authority/tracking state. Version 0.3 corrects the agent's unsupported product/distribution split after explicit owner clarification: Skill OS and SkillMesh are the same product; bootstrapping uses its own skills to develop it. UC-01's done-check and corresponding source/records are corrected; opportunity-routing behavior and the remaining task hold are unchanged. Document checks and source review do not claim T-03 execution or measured benefits. Future material edits must retain the reason, decision standing and affected checks here or in adequate existing change records, without a parallel history system.

Version 0.4 records the owner's T-02 implementation request and the paragraph/reference candidate. Acceptance is unchanged: conditional suggestions, existing-system preservation, fitting-library preference and escape routes remain required. Necessary affected verification is recorded separately from deployment and later benefit observation in the checkpoint; prior authority holds above describe their original versions, not the current T-02 request.

Owner clarification to version 0.4: development feedback must also improve the component-selection reference. UC-04.A4 and the owning skill/reference now carry the bounded feedback-to-guidance path, preserving project evidence, source authority and provisional transfer/benefit claims.

Version 0.5 records the explicit T-03 request and completed verification of the committed final candidate, including that clarification. Acceptance was preserved; no skill correction was required. Independent source/output assessment, actual isolated feedback edits, controlled missing-reference recovery and structural proof supersede the earlier partial T-03 status. Application acceptance, installation and economic benefit remain separate and unproved.

Version 0.6 records the explicit T-04 request, bounded exposure review and precise actual-use dependency. No confirmed natural observation was found in the inspected sources; neither an older installed cache nor synthetic T-03 output counts as exposure. T-04 is started, not declared complete. Existing G-01/G-03 retain unknown comparisons/economics; no new skill, tracker, experiment, application change or installation was introduced.
