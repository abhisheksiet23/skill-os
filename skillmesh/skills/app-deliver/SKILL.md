---
name: app-deliver
description: Prepare or execute an authorized software release, verify the deployed candidate and reconcile project knowledge. Use for application delivery, migration readiness or release handoff; preparing a release does not itself authorize deployment.
---

# App Deliver

Identify the exact release candidate, intended scope, destination, current live baseline and existing release process. Read relevant requirement/test/review evidence from any adequate source; no SkillMesh phase ledger is required. Confirm checks cover the candidate actually being released, including relevant uncommitted work and combined increments.

Prepare the build, configuration by name (never secret values), migrations, operator steps, smoke checks and recovery approach. Missing, failed or stale required proof blocks the dependent release action, not independent preparation. For migrations and coexistence, read [release risks](references/release.md).

Use existing user authorization. Build-only requests permit a concrete release plan, not publication. Resolve any genuinely missing deployment authority against the prepared candidate; do not request the same approval again. Preserve host permissions and existing project controls.

Execute through the project's authorized mechanism. Reconcile uncertain external results before retrying. Verify the actual deployed candidate, critical behavior, integration/configuration differences and health signals. Diagnose failures and apply only authorized recovery. A successful upload is not a verified release.

Lead the handoff with the actual release state—released, not released or partially verified—and the consequence for users or operators. Record revision, destination/time, actual verification, remaining limitations and recovery information. Separate preparation, execution and observed live proof so a reader need not reconstruct status from a command log. Promote only shipped behavior into current product knowledge; leave pending scope and historical decisions distinct. Use the project's existing documentation and update user-facing help only where the product needs it. No mandatory in-app wiki or new documentation tree.

Finish with a usable release/handoff and precise remaining dependency, if any. Missing proof may justify recommending `app-qa`; an unresolved data decision may benefit from `app-analyze` or `app-backend`. These are recommendations to the agent, not skill invocations or required transitions.
