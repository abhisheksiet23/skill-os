---
name: app-deliver
description: Prepare or execute an authorized software release, verify the deployed candidate and reconcile project knowledge. Use for application delivery, migration readiness or release handoff; preparing a release does not itself authorize deployment.
---

# App Deliver

Bring a specific application candidate to the requested release state and make that state unambiguous. Preparation, artifact production, installation and verified live behavior are different outcomes. Use existing authorization; this skill adds no permission to build or deploy.

## Identify the candidate and authorized outcome

Establish release scope, exact candidate including relevant uncommitted work, destination, live baseline and the project's existing release process. Use adequate requirement, test and review evidence from any source. Check that required proof covers the combined candidate, not only its separately tested increments.

Default to owner-controlled release compilation, publishing, package generation, database application and server changes. A preparation request produces settings, profiles, configuration templates and operator instructions. An explicit build/package request authorizes that named artifact and its local verification, not deployment or publication. Honor already granted authority without asking again; resolve genuinely missing authority against the prepared candidate immediately before the dependent action.

## Prepare an executable handoff

Prepare build inputs, configuration by name rather than secret value, complete migrations, operator steps, smoke checks and recovery. Missing, stale or failed required evidence blocks its dependent release action while independent preparation continues. Read [release risks](references/release.md) for migration, coexistence and candidate-readiness concerns.

Use `releases/<version>/` at the application root for release packages and handoff by default. Add component folders only for distinct deliverables and preserve explicit project conventions. A justified layout change updates producer scripts, publish profiles, ignore rules and commands together without discarding old releases.

For database handoff or backend/frontend hosting, read [manual release packages](references/manual-release-packages.md), including its relevant IIS sections. Repository-owned initial and ordered change SQL are backend deliverables: review actual bodies and candidate identity, not just generation commands. SQL authoring and safe local generation do not authorize SQL execution or release compilation. New EF Core/SQL Server projects retain migration-derived SQL and manual SSMS execution; other stacks retain appropriate native migrations and clients. Application startup must not mutate production schema or seed data; administrator bootstrap is separate.

A recipe is not a built, tested or deployed package. Keep pending artifact and environment checks explicit rather than substituting development serving for the eventual production candidate.

## Execute and verify within authority

Use the project's authorized mechanism. For interrupted or uncertain external operations, reconcile actual remote state before retrying. Diagnose failures and use only authorized recovery; repeated deployment without understanding current state is not progress.

Verify candidate identity at the destination, critical behavior, integration/configuration differences and health signals. Confirm recovery eligibility against current schema, data and persistent files. An upload or successful command does not establish a healthy release.

Lead the handoff with the actual state: released, not released or partially verified, and the consequence for users/operators. Record revision, destination/time, executed checks, limitations and recovery information in existing project records. Promote only verified shipped behavior into current product knowledge; keep pending scope, unsynced local state and historical decisions distinct. Update user-facing help only where needed; do not invent an in-app wiki or documentation tree.

For adopted automatic context maintenance, refresh this release workstream's checkpoint, verified live baseline and session assessment before handoff. The assessment is not release approval. Finish with a usable artifact or recipe and any precise dependency preventing the requested outcome. Missing proof or an unresolved data decision may warrant QA, analysis or backend expertise; recommend the gap without invoking another skill or requiring a phase sequence.
