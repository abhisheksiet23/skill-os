# Handoff: continuing Skill OS on another computer

Paste the "Starter prompt" below into a fresh Claude Code session opened in the skill-os repo, then let it read the files listed.

## Starter prompt

> I'm continuing work on Skill OS (SkillMesh), a library of specialist agent skills. Read `AGENTS.md`, `README.md`, `EVOLUTION.md`, `docs/project-context.md`, `docs/handoff-new-device.md` and the current checkpoint in `docs/toolkit-session-assessments.md` first. Do not reload older run conclusions as current evidence. Work on `main` only (no feature branches). Run experiments, eval runs and drafts in `skill-os-test` (a sibling folder to this repo), never here. Show me planned skill wording before editing a skill. Commit or push only when I ask. Next task: <say what you want>.

## What Skill OS is

Skills are authored in `skillmesh/skills/`, one self-contained folder per skill. Installed copies are deployment artifacts. This repo is the authoring source. There are 23 skills, grouped as `app-*` (analyze, design, prototype, backend, frontend, qa, deliver), `business-*`, `website-*` and supporting ones (project-context, project-manage, code-navigation, naming-architect, and others).

## How we are transforming it

- **Compile, don't append.** Fold inputs into a coherent skill and its references. Preserve behavior, authority and safeguards, and keep detail that improves correctness. Don't cut for word count.
- **Rewrite to the authoring standard.** A short top statement, then references loaded only when needed. Already done for app-analyze, app-design and app-prototype. Done so far, newest first:
  - `6c8b61b` app-prototype inspects where the prototype runs and records lessons in project artifacts. Owner brief IDs and on-defaults are explained.
  - `79d3abf` Top statements rewritten for analyze, design and prototype. Design access and data standards moved to a reference.
  - `044a943` and `079d1a9` app-prototype compares against references, measures by script and keeps scaffolding aside. It adds a visual-system trigger and a light default theme.
  - `8e0ea95` app-prototype rewrite, with jobs and journey, visual system and iconography.
  - `b84b8a2` and `ab97fb7` app-analyze reworked, then app-design rewritten.
- **app-analyze output.** Three documents: owner brief, findings and spec. The decision register lives in the brief ("Decide now" / "Later"). Facts get F-ids. The spec opens with a decisions-and-facts table. Status words are Identified, Drafted, Specified, Built, Verified. Readiness appears only in the tracking table.
  - Retest results: owner probe 2.2 to 4.5 out of 5, builder probe 3.8 out of 5 (n=2, noisy).
  - Known open issue: Haiku sometimes adds a separate product-rules file and over-outlines flows. You chose to stop iterating. Details are in `skill-os-test\retest\results.md`.
- **Owner design preferences.** Directional guidance over transactional rules (one line plus its reason). Light, tinted off-white default theme. Dark only on request, soft and tinted, never near-black.
- **Authorization model (accepted).** Users, Roles, Permissions, UserRoles and RolePermissions, or the equivalent existing framework relations. One role is enough when it fits. Detail is in `skillmesh/skills/app-backend/references/identity-and-authorization.md`, with the decision history in `docs/lessons-learned.md`.
- **Process economy.** Read outlines before whole files, keep sessions bounded (hand off around 120k context or 100 model calls), use cheaper models for bounded work, and add a new mechanism only if it solves a repeated observed failure.

## State at handoff (2026-11-25)

- `main` is at `6c8b61b`. The only uncommitted change is `docs/toolkit-session-assessments.md` (the checkpoint) plus this file.
- The package was rebuilt and reinstalled locally: release `0.2.0+codex.20261125063121379`, validation 23 skills and zero errors. The other device needs its own install. See `docs/installation-status.local.md` for device paths (local only, not committed).
- Not established: real-application adoption, cross-device rollout, provider-token savings.
- Open roadmap items (CR-02 and CR-03 and others) are still proposals. See `docs/opportunity-roadmap.md`.

## On the new machine

1. Clone or pull the repo. Also clone or create the sibling `skill-os-test` folder if you plan to run experiments.
2. Copy this file over if you haven't committed it.
3. Install the package with the repo's installer, then start a new chat so the skill catalog loads.
