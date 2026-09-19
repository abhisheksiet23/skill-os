---
name: skill-ecosystem-orchestrator
description: Helps coordinate multiple installed specialist skills for complex tasks. Use when a task spans several areas of expertise, requires iterative reassessment, or risks overusing/underusing available skills. Do not use for simple tasks that one skill or direct reasoning can handle.
---

# Skill Ecosystem Orchestrator

Historical advisory example, not installed by SkillMesh. The agent owns selection and continuation. Never invoke another skill from this one, including for a user-requested sequence; the agent executes that sequence.

## Purpose

Help Codex compose existing skills without creating a separate orchestration runtime.

This skill does not perform domain analysis itself. It helps decide which expertise is useful, in what order, and when to stop.

## Operating model

For a substantial task:

1. Clarify the objective from existing context. Do not ask the user to repeat information already available.
2. Identify the primary job to be done.
3. Inspect available skills and select a likely primary skill if one exists.
4. Identify at most a few supporting skills that address real gaps.
5. Start with the highest-value unresolved question rather than attempting exhaustive coverage.
6. After meaningful findings, reassess:
   - what changed?
   - what remains uncertain?
   - what decision or artifact is blocked?
   - would another skill materially help?
7. Use supporting or challenger skills only when they add decision value.
8. Synthesize the work into one coherent result.
9. Stop when additional skill usage has diminishing returns.

## Roles

Use these as loose mental categories, not mandatory metadata:

- **Primary**: owns the main job to be done.
- **Supporting**: contributes focused expertise.
- **Cross-cutting**: challenges, audits, transforms, or improves work from other skills.

## Skill recommendation rule

A specialist may surface statements such as:

- customer evidence is missing;
- financial viability is uncertain;
- competitor evidence is weak;
- assumptions should be challenged.

Treat these as *needs*, not hard-coded skill calls. Decide whether an available skill should address them.

## Restraint

Do not create a chain simply because one is possible.

Do not invoke every related skill.

Do not repeat the same analysis through multiple overlapping skills unless comparison is explicitly useful.

Do not turn a skill recommendation into a mandatory workflow step.

## Lightweight trace

For complex work, maintain a concise internal working summary of:

- Objective
- Relevant skills considered
- Skill(s) selected
- Reason selected
- Important findings
- Remaining uncertainty
- Why continuing or stopping makes sense

Do not expose private chain-of-thought. User-visible progress should contain only concise decisions and useful findings.
