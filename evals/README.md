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

Use N/A when a task does not exercise a dimension. A direct answer can receive full selection/stopping marks without loading a skill. Metadata/packaging checks are not behavioral evidence; word counts are not provider tokens.

## Matched task runs

Use [task-pack.md](task-pack.md) for bounded, offline before/after tasks spanning standalone review, existing contracts, business economics, context transfer, contradictions, restraint and stale release proof. Dispatch the task pack and the available variant's descriptions to fresh evaluators; let them load only relevant skills. Do not give evaluators the intended answers or each other's outputs. Keep scope, model and tools as comparable as possible and record differences.

Save actual outputs and a separate assessment under `results/`. [RESULT_TEMPLATE.md](RESULT_TEMPLATE.md) is optional recording guidance, not production state. Repeat meaningful scenarios and add real implementation/browser journeys before claiming general superiority. The original eight business scenarios remain available in [scenarios.md](scenarios.md); live market research needs sources and should not be simulated as completed evidence.

## Escalation rule

Do not add a new architecture layer after one bad run. Look for a repeated failure pattern across multiple scenarios.
