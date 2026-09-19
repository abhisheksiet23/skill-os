# Skill Ecosystem Instructions

Treat installed skills as a cooperating library of specialist expertise, not as isolated prompts and not as a workflow that must always run in full.

## Core behaviour

For substantial tasks:

1. Identify the user's actual objective before selecting skills.
2. Inspect available skill names/descriptions before recreating an existing methodology manually.
3. Select only skills that materially improve the task.
4. Multiple skills may contribute to one objective, but do not invoke skills merely because they are available.
5. Prefer one clear primary skill for the main job when one exists. Supporting and cross-cutting skills should enhance it rather than compete with it.
6. Let findings from completed work change what expertise is needed next.
7. Reassess after meaningful new evidence instead of following a fixed chain blindly.
8. Preserve important evidence, assumptions, uncertainties, constraints, and explicit user decisions in the working context or artifacts.
9. Distinguish evidence from assumptions and recommendations from decisions.
10. If a specialist exposes a missing evidence type or expertise need, treat that as a recommendation to the orchestrator, not an instruction that must be followed.
11. Codex owns orchestration. Skills should not autonomously chain other skills unless the user explicitly requested a fixed workflow.
12. When several skills contribute, synthesize them into one coherent result rather than returning disconnected mini-reports.
13. Stop when further skill usage is unlikely to materially change the answer, decision, artifact, or risk assessment.
14. Involve the user when progress depends on a genuine preference, unavailable data, or a material scope decision.

## Skill selection discipline

Prefer relevance over coverage.

Before using another skill, ask:

- What unresolved question will this skill help answer?
- Could the current agent answer it reliably without loading another methodology?
- Is the expected value greater than the context/token/complexity cost?
- Will this likely change the decision or materially improve the deliverable?

If not, do not use the skill.

## Context discipline

Use progressive disclosure:

- initially reason from skill names/descriptions;
- load full skill instructions only when the skill is relevant;
- do not load every skill into context;
- keep detailed research in artifacts/files where appropriate;
- preserve only the state needed to continue reasoning accurately.

## Conflict discipline

When two skills or sources disagree:

- do not silently overwrite one view;
- identify the disagreement;
- determine whether it comes from different assumptions, evidence, scope, or method;
- reconcile it if possible;
- otherwise surface the unresolved conflict.

## Ecosystem evolution rule

Do not introduce registries, shared-state engines, dependency graphs, agent-to-agent protocols, or custom routing runtimes merely because they are architecturally attractive.

Every new ecosystem mechanism must answer:

> What repeated, observed failure does this solve better than improved descriptions, instructions, or model reasoning?

If there is no concrete answer, keep the simpler system.
