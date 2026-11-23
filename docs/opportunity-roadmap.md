# Opportunity roadmap

As of 2026-11-23. This is the live backlog for Skill OS. See [product improvement use cases](product-improvement-use-cases.md) for standing behavior, authority and evidence gaps, [lessons learned](lessons-learned.md) for retained decisions and conclusions, and [environmental factors](environmental-factors.md) for conditions that affect execution and proof. Keep tooling work in the [tooling roadmap](tooling-roadmap.md) and application evidence in its owning project. Each proposed increment requires applicable task authorization.

## Recommended next source increment

### CR-02 · Reassess proof when its subject changes · P0

**Proposal for app-qa and project-context.** When fixtures become real content, media revisions change, a new entry point bypasses a tested service, or shared behavior changes, identify the affected claim and execute the necessary checks. Tie claims to the relevant content/data revision, build, exercised path and environment. Keep valid passes for their original subjects and reuse unaffected proof.

**Acceptance.** A fixture offline pass stays valid for fixtures. Real-item offline/resume needs an exercised real path. An unrelated copy change leaves valid integration proof intact. Distinguish failed, blocked and untested checks. Physical-device and editorial acceptance need their own evidence.

Current guidance already limits candidate-bound claims. The observed fixture/real-path mismatch warrants testing whether a specific transition cue improves check selection and execution.

### CR-03 · Check shared ownership at integration time · P0

**Proposal for app-frontend and app-backend, with app-qa for proof.** When a second entry point uses a shared resource or mutable state, inspect the existing owner and contract before adding a path. Exercise both directions of interaction, plus relevant navigation, teardown and recovery. Playback, unsaved edits, shared selection, downloads and concurrent writes are examples. Use app-design when consequential ownership is genuinely unresolved.

**Acceptance.** In the playback case, mini-player, route, collapse and supported media actions respect session ownership. Run representative interaction checks before replicating the pattern. A local stateless control stays within its contained scope.

The original case exposed playback, lifecycle and focus defects despite proposed ownership. Preventive benefit remains a hypothesis. Evaluate CR-02 and CR-03 together with a fixture-to-real transition, a second shared-state entry point and an unrelated copy edit as the restraint case. Check existing guidance first and add only the missing behavior. A caveat alone leaves affected proof pending.

## Remaining questions from the two-month review

The review's host-discovery, manual-release and identity inconsistencies have been corrected in source under the owner's clarified policy; see [retained decisions](lessons-learned.md). Current verification boundaries belong in the [checkpoint](toolkit-session-assessments.md), not future backlog.

Two narrower evaluation questions remain: whether copy-only website requests retrieve existing writing expertise without expanding into prototypes, and whether naming evaluations exercise live shortlist checks and lookup failure as well as offline restraint. Establish an actual selection/coverage gap before adding permanent evaluation inputs or another skill. Broad instruction growth is a loading diagnostic, not a reason to trim useful guarantees. CR-02/03 remains the next proposed behavioral increment, outside the current consistency correction.

## Independent pilots

### CR-06 · Diagnose avoidable model work and establish usage evidence · P0

The owner prioritizes selective model mix alongside retrieval and rework improvements. Native worker selection is feasible for a bounded maintenance task. Comparative quality, attributable spend and net savings are still open. The owner reported a five-hour allowance exhausted in about 40 minutes. The historical trace and cause are unavailable. Repeated reads, oversized outputs, duplicate reviews, discarded work and excess reasoning are hypotheses to check against actual work. See [environmental factors](environmental-factors.md) for measurement and host limits.

**Next observation.** Use a useful bounded task to compare direct execution and an authorized mixed-model path with equivalent acceptance, comparable evidence and confirmed model selection where observable. Include setup, lead review, worker effort, retries, integration, elapsed time and owner rework. Avoid giving one path the other's solution. Act on an observed recurring burden using existing retrieval, reuse and affected-check discipline.

**Decision.** Promote a task-class default only when observed outcomes and the available economic evidence support it. Keep direct execution when handoff outweighs the gain. Record source and cutoff for any usage data. Allowance, tokens and attributable charges answer different questions. Output size and command compression are diagnostic proxies. Leave unavailable measures unknown. Missing cost evidence allows a feasibility or quality conclusion. It leaves savings unknown. Keep required proof and existing spend authority.

### CR-07 · Strengthen visual direction and concrete craft critique · P1

**Pilot for app-prototype and app-frontend.** Inspect actual screens at the next suitable authorized UI task. Select one consequential observed weakness and revise a representative path with realistic content. Compare matched state and viewport. Inspect typography and script rendering, hierarchy, density, spacing, control prominence and identity where they affect the task. A reading-heavy product needs realistic long text and enlarged text. A task-heavy product needs realistic decisions and density. Existing prototype guidance already covers much of this method.

**Acceptance.** Owner feedback identifies a concrete task-relevant preference and the revision preserves functional and accessibility behavior. The owner reports improved UI with room for improvement. This roadmap has no current screen diagnosis or preference comparison. The pilot can proceed independently of the source increment.

### CR-08 · Preserve design quality through production and combined states · P1

**Include in CR-07 acceptance.** Carry the selected direction into production and compare the rendered implementation at target widths. Inspect applicable long content, resumed state, loading/error/offline, keyboard focus and persistent controls. Correct observed fidelity drift or cross-feature conflicts and reuse valid unchanged evidence. The owner judges preference separately from technical verification. Pursue a standalone instruction change only if the comparison exposes a consequential gap in existing frontend/QA guidance.

## Ordinary-use observations

### T-04 · Observe an actual prototype pattern decision

The owner chose the next natural prototype task with a real pattern choice. The optional map is provisionally retained on the established-library preference and source review. Local rollout and catalog loading establish availability at their original boundary. Actual consultation, avoided corrections, comparative effort and upkeep remain open.

Establish the source actually consulted and apply R-07 in the [use-case specification](product-improvement-use-cases.md#shared-rules). Record the choice, useful or misleading guidance and attributable corrections in the owning application. Use a comparable baseline if available and report the exposure and evidence limits. Review when the evidence can change a decision; there is no usage quota. A material regression can prompt an immediate correction. Normal project needs determine when an eligible task occurs.

### Conditional improvements during normal work

| Trigger | Smallest useful response |
| --- | --- |
| Recurring wrong change paths or repeated rediscovery on unfamiliar work | Compare the adequate existing map with a focused entry-point addition or one real working example. Check complete-task effort, correction and upkeep. |
| An actual stale contract link, repeated domain behavior or recurring verification gap | Repair at the authoritative source, extract only demonstrably shared behavior, or make one consequential boundary executable through the existing runner. |
| Consequential rendered state that existing examples fail to explain | Try one representative state with an identified consumer. Consider a gallery only if repeated benefit can justify upkeep. |
| Demonstrated repeated selection or loading failure | Inspect the actual trace. Correct execution or a specific description before considering structural changes. |
| Questioning materially shapes a decision or helps recovery | Notice the effect in normal work and retain useful questions only while they have a live purpose. Current inquiry guidance stands. General benefit and savings remain unproved. |

A2UI remains parked by owner decision. Revisit only if a concrete agent-composed interface needs protocol capabilities. The established-component preference, task fit, accessibility and freedom to compose, extend or create remain in force. Compare any future selection aid with the library held constant. The bounded application trial left faster or cheaper authoring unestablished. See [lessons learned](lessons-learned.md) for its decision and limits.

For proposed skill edits, compare representative baseline and candidate behavior with equivalent inputs and required proof. Preserve existing guarantees and authority. Start with a positive case and a boundary case and expand only if a result can change adoption. Source inspection and metadata checks provide source-level evidence. Usable applications, deployment, actual skill consultation and economic benefit each need their own proof. No delivery date, provider-token budget or spend forecast is established.
