# Ecosystem Evals

Run these against the baseline ecosystem and again after changes.

The purpose is not to force identical execution paths. The goal is consistently competent skill selection and composition.

## Score each scenario (0-2)

### Discovery recall
0 = misses important relevant skill(s)
1 = partially discovers useful skills
2 = discovers the important skill(s)

### Selection precision
0 = substantial unnecessary skill usage
1 = some unnecessary usage
2 = uses a focused set

### Composition
0 = skills operate as disconnected reports
1 = partial integration
2 = findings naturally inform later work

### Reassessment
0 = follows fixed chain regardless of findings
1 = limited adaptation
2 = meaningfully changes next steps based on findings

### Stopping
0 = keeps expanding work without value
1 = stops imperfectly
2 = stops when further work is unlikely to matter

### Synthesis
0 = fragmented / contradictory
1 = mostly coherent
2 = unified and decision-useful

### Human correction burden
0 = frequent user correction needed
1 = some correction
2 = little or no correction

Also record approximate context/token overhead if available.

### Context transfer
0 = loses or promotes assumptions/decisions incorrectly
1 = preserves some but loses a consequential limitation
2 = preserves evidence, assumptions, authority and remaining uncertainty in later output

### Contradiction handling
0 = silently chooses a view or blends incompatible claims
1 = notices disagreement but does not locate the cause
2 = distinguishes evidence/scope/assumptions and resolves or proposes targeted evidence

### Final output quality
0 = incorrect, misleading or unusable
1 = useful with material omissions
2 = correct and actionable within the stated evidence and scope

### Reader effort and decision usability
For output-quality work, also score the outcome/consequence, meaningful economy, checkability, actionability, continuity/boundaries and proportionality criteria in [deliverable-quality-rubric.md](deliverable-quality-rubric.md). A heading, table, file or longer response earns no credit by itself.

Use N/A when a task does not exercise a dimension. A direct answer can receive full selection/stopping marks without loading a skill. Metadata/packaging checks are not behavioral evidence; word counts are not provider tokens.

## Matched task runs

For instruction trimming, use [the matched prompts](trimming-tasks.md). Earlier paired runs covered an aggressive candidate, not the later conservative revision; do not treat them as proof for the current source. Execution-result archives were removed from the working tree at the owner's request.

For interface-copy work, use [the microcopy scenarios](microcopy-tasks.md) and keep the separate [assessment key](microcopy-assessment.md) from task performers. The suite spans product types and pairs empty states, draft voices and processing states across products; assess factual correctness and product adaptation separately. Freeze the scenarios with the skill variants; results from earlier fixture versions do not validate revised requests.

For decision ordering, contained-change restraint, recurring QA and early legacy integration, use [efficiency-tasks.md](efficiency-tasks.md). Historical committed assessments and outputs remain accessible through Git history; for example, the 2026-09-20 assessment is available with `git show f8daa37:evals/results/efficiency-assessment.md`. It separates planning-only responses from the executed browser pilot and does not establish measured token savings.

For first-write feasibility, clarification timing, early dense-screen inspection and contained-change restraint, use [automation-feedback-tasks.md](automation-feedback-tasks.md) with its separate [assessment key](automation-feedback-assessment-key.md). The [2026-11-02 comparison](automation-feedback-assessment.md) records an observed ordering improvement and its limits. The first task executes a harmless local boundary simulator; the other tasks assess written decisions. Neither the simulator nor a stated plan proves live application integration, visual quality or credential non-retention.

For tailored outcome control, actual status-record recovery/change, incomplete AI/tool costs, delegation, improvement claims and real operator boundaries, use [project-manage-tasks.md](project-manage-tasks.md) with its separate [assessment key](project-manage-assessment-key.md). The [2026-11-03 comparison](project-manage-assessment.md) records executed local edits and bounded findings. Local synthetic edits and arithmetic test reasoning/maintenance; they do not establish real project outcomes or billing access.

For ordinary implementation with adopted upkeep, useful positive forecasts, next-action choice, small-correction restraint and unchanged unavailable spend sources, use [project-manage-delivery-tasks.md](project-manage-delivery-tasks.md) with its separate [assessment key](project-manage-delivery-assessment-key.md). A fresh recipient can then recover the actual synthetic implementation/checkpoint without performer conclusions. This remains a bounded local exercise, not unattended monitoring or live project optimization.

Use [task-pack.md](task-pack.md) for bounded, offline before/after tasks spanning standalone review, existing contracts, business economics, context transfer, contradictions, restraint and stale release proof. Use [deliverable-quality-tasks.md](deliverable-quality-tasks.md) for matched output-quality cases spanning strategy, two initiatives, executable backend work, website review, cross-product isolation and restraint; keep its separate assessment key from task performers. Dispatch the task pack and the available variant's descriptions to fresh evaluators; let them load only relevant skills. Do not give evaluators the intended answers or each other's outputs. Keep scope, model and tools as comparable as possible and record differences.

Capture actual outputs and an assessment when needed to substantiate a comparison, using ignored task scratch such as `.eval-runs/`. Retain repository evidence only when needed for review rather than accumulating execution logs by default. [RESULT_TEMPLATE.md](RESULT_TEMPLATE.md) is optional recording guidance, not production state. Repeat meaningful scenarios and add real implementation/browser journeys before claiming general superiority. The original eight business scenarios remain available in [scenarios.md](scenarios.md); live market research needs sources and should not be simulated as completed evidence.

For requirements comprehension, source-grounded technical plan review, complexity introduced by review fixes and contained-change restraint, use [design-review-tasks.md](design-review-tasks.md). Keep [the assessment key](design-review-assessment-key.md) from performers. These offline design assessments do not establish application behavior or deployed guarantees; distinguish fresh performer contexts from a measured comparison of independent versus author-context review.

## Escalation rule

For automatic project maintenance, actual local record updates, fresh-session recovery, workstream separation and bounded reviewer isolation, use [project-context-tasks.md](project-context-tasks.md) with its separate [assessment key](project-context-assessment-key.md). The packaged [session rubric](../skillmesh/skills/project-context/references/session-assessment.md) is also the ongoing assessment factor for every adopted project session. Project records stay in their owning projects; [the pilot note](../docs/project-context-pilot.md) tracks sanitized lessons and real-project evidence still pending. Do not count synthetic exercises as the live pilot or unobserved factors as passed.

Do not add a new architecture layer after one bad run. Look for a repeated failure pattern across multiple scenarios.
