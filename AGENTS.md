# Skill Ecosystem Instructions

Treat installed skills as a cooperating library of specialist expertise, not as isolated prompts and not as a workflow that must always run in full.

## Core behaviour

For substantial tasks:

1. Identify the user's actual objective before selecting skills.
2. Inspect available skill names/descriptions before recreating an existing methodology manually.
3. Select only skills that materially improve the task.
4. Multiple skills may contribute to one objective, but do not invoke skills merely because they are available.
5. Prefer one clear primary skill for the main job when one exists. Supporting skills contribute focused expertise; cross-cutting skills challenge, audit, transform, or improve other work. These are loose role labels, not required metadata; their contributions should serve the objective, including challenging the primary skill's conclusions when warranted.
6. Let findings from completed work change what expertise is needed next.
7. Reassess after meaningful new evidence instead of following a fixed chain blindly.
8. Preserve important evidence, assumptions, uncertainties, constraints, and explicit user decisions in the working context or artifacts.
9. Distinguish evidence from assumptions and recommendations from decisions.
10. If a specialist exposes a missing evidence type or expertise need, treat that as a recommendation to the agent, not an instruction that must be followed.
11. Codex owns orchestration. Skills may recommend named expertise with the gap and useful evidence, but must never invoke other skills. A user-requested fixed workflow is executed by the agent, not by skills calling skills.
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

For complex work, keep a concise working summary of the objective, selected skills and their purpose, consequential findings, unresolved gaps, and the next action or stopping reason. Reuse the working context or existing project records; do not create a separate log or report by default. User-visible progress should contain concise decisions and useful findings, not private chain-of-thought.

## Automatic project context and session assessment

The owner has adopted automatic maintenance. Establish the active project's identity/root and task/branch; use its small context map and retrieve relevant records only. Maintain accepted owner decisions, source/revision-bound facts, provisional assumptions and superseded choices in authoritative project records after consequential changes. Link evidence rather than copying conversations; implementation drift does not silently replace accepted intent. Keep continuation state per workstream and re-read before editing to preserve concurrent work. Local maintenance does not authorize commits, pushes, deployment or external writes.

At each project work-period completion, explicit pause or handoff, refresh its checkpoint and fill its session assessment: observed continuity, decision fidelity, evidence freshness, retrieval economy, project/workstream separation and review independence. Score observed factors 0=failed, 1=partial, 2=evidenced success; use unknown when unobserved and N/A when not exercised, with reasons. Provider-token/time/cost savings remain unknown unless measured. A session is a coherent work period, not each reply. Recover an abrupt closeout as a gap on resumption; do not invent historical scores. Respect no-write scope by reporting pending updates. Assessments stay in the owning project; only authorized sanitized lessons return to the toolkit. The optional project-context skill provides the full method; no other skill must invoke it.

For this repository, README.md maps the library, EVOLUTION.md governs added mechanisms, docs/project-context-pilot.md preserves this decision and pending pilot work, and docs/toolkit-session-assessments.md holds toolkit-authoring session assessments. Application facts and assessments stay in their own projects. Fresh reviewers receive the target and selected evidence, excluding authoring notes, broad context recovery and session assessments; no-history dispatch does not isolate shared files or configured memory.

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

## Source and project boundaries

Author maintained skills in `skillmesh/skills/`, one self-contained folder per skill. Required references stay inside the owning skill. Do not require siblings, a shared external toolkit, a phase-status ledger or a previous invocation. Optional named recommendations must describe the underlying need so the skill works without them.

Adapt to adequate existing project records. Company facts, decisions and implementation belong in the project, not in reusable instructions. Installed copies are deployment artifacts; this repository is the authoring source.

Run application work in the application's own directory. Keep its prototypes, scripts, reference extractions and temporary build/review artifacts there as well; do not stage them inside skill-os. Only reusable skill authoring and isolated skill evaluations belong in this repository.

For substantive changes use representative before/after evals. Metadata checks and simulated test artifacts are not live behavioral passes. Report unavailable metrics as unknown.
