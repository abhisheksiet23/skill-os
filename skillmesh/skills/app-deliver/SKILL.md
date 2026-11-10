---
name: app-deliver
description: Prepare or execute an authorized software release, verify the deployed candidate and reconcile project knowledge. Use for application delivery, migration readiness or release handoff; preparing a release does not itself authorize deployment.
---

# App Deliver

Identify the exact release candidate, intended scope, destination, current live baseline and existing release process. Read relevant requirement/test/review evidence from any adequate source; no SkillMesh phase ledger is required. Confirm checks cover the candidate actually being released, including relevant uncommitted work and combined increments.

Prepare the build, configuration by name (never secret values), migrations, operator steps, smoke checks and recovery approach. Missing, failed or stale required proof blocks the dependent release action, not independent preparation. For migrations and coexistence, read [release risks](references/release.md).

Use predictable, purpose-named paths: release packages and their operator handoff belong in `releases/<version>/` at the application root by default, rather than under a generic `artifacts/` directory. Add component folders only when they distinguish actual deliverables. Honor explicit project choices; a layout correction must update producing scripts, publish profiles, ignore rules and documented commands together without discarding existing releases.

Default to owner-controlled release compilation, publishing and deployment. Prepare build settings, publish profiles, configuration templates and operator instructions; the owner initiates release compilation, publishing, database application and server changes. Repository-owned initial and incremental SQL scripts are backend implementation deliverables, not merely owner-run generation commands; review their completeness and candidate identity before handoff. Their authoring or safe local generation does not authorize release builds, dotnet publish, package generation or deployment; execute those steps only when explicitly requested. Distinguish development verification from release production. Keep database execution separate from application startup. For EF Core/SQL Server projects retain migration-derived SQL for manual SSMS execution; other stacks keep appropriate native migrations and clients. Preserve explicit project choices. Use [manual release packages](references/manual-release-packages.md) for database handoff and backend deployment, including Windows Server/IIS. A prepared recipe is not a built, tested or deployed package.

Use existing user authorization. An explicit build-only request authorizes the named compilation or package within its scope, not deployment or publication; produce the requested artifact and verify what can be checked locally. A preparation-only request authorizes the recipe, not release production. Resolve any genuinely missing deployment authority against the prepared candidate; do not request the same approval again. Preserve host permissions and existing project controls.

Execute through the project's authorized mechanism. Reconcile uncertain external results before retrying. Verify the actual deployed candidate, critical behavior, integration/configuration differences and health signals. Diagnose failures and apply only authorized recovery. A successful upload is not a verified release.

Lead the handoff with the actual release state—released, not released or partially verified—and the consequence for users or operators. Record revision, destination/time, actual verification, remaining limitations and recovery information. Separate preparation, execution and observed live proof so a reader need not reconstruct status from a command log. Promote only shipped behavior into current product knowledge; leave pending scope and historical decisions distinct. Use the project's existing documentation and update user-facing help only where the product needs it. No mandatory in-app wiki or new documentation tree.

Finish with a usable release/handoff and precise remaining dependency, if any. Missing proof may justify recommending `app-qa`; an unresolved data decision may benefit from `app-analyze` or `app-backend`. These are recommendations to the agent, not skill invocations or required transitions.

For adopted automatic context maintenance, update only this release workstream's checkpoint and the verified live baseline; leave pending scope and unsynced local state explicit. Prepare the session assessment before handoff without treating it as release approval.
