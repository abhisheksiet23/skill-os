# Recover the right next action

Use this reference when a checkpoint is incomplete, a source changed or two records disagree. It supplies a focused recovery method, not a new storage format or a demand to read every project record.

## Choose the next read by what it can change

Start with the project map and this workstream's current checkpoint. Recover the requested outcome, accepted boundary, candidate, relevant proof and unresolved dependency. Follow a link or inspect implementation only when it can change one of those facts or expose a consequential inconsistency. Installation and file presence do not prove guidance loading or runtime behavior.

| Observation | Discriminating check | Useful action |
| --- | --- | --- |
| Summary says complete, acceptance still names an unproved boundary | Compare the stated completion rule with candidate-bound check coverage | Report implemented/verified/accepted separately; name the missing check |
| Tests passed before the relevant code or environment changed | Inspect the changed boundary and recorded tested identity | Invalidate affected proof and select its rerun; preserve unrelated valid evidence |
| Current code contradicts the accepted decision | Check the decision's authority and scope, then the relevant implementation path | Record drift; do not rewrite intent to match code or revert code without scope authority |
| Two branches changed the same requirement | Compare accepted sources and branch/workstream boundaries | Reconcile the real decision; newest timestamp alone does not choose the winner |
| A dependency is unknown and a nearby task is available | Ask whether the task advances the accepted outcome or reduces its driving uncertainty | Continue bounded useful work; avoid an expanding unrelated backlog |
| A fresh reviewer cannot understand the artifact | Inspect the target and its selected evidence without supplying the authoring conversation | Treat the missing relationship as an artifact gap, not a reason to preload memory |

## Preserve distinctions in the correction

Example: an accepted billing rule requires account-scoped invoices. A checkpoint says an updated query is complete, but its only test report covers the preceding query. A weak recovery promotes the old pass and starts UI polish. A useful recovery keeps the accepted scope, identifies the updated query as unverified and selects a focused account-isolation check. It does not reopen credentials, redesign billing or reread unrelated workstreams.

When editing, change the authoritative fact and its affected summary, linking detailed evidence once. Re-read the destination and reconcile concurrent changes; this is not atomic locking. Keep source-reported facts distinct from directly observed behavior. State what is unknown and how it affects the next action.

## Stop with usable continuation

Leave a compact result: current boundary; candidate; accepted decision links; relevant proof/gap; next action and owner/dependency where known. A subsequent recipient should be able to choose the right work without inventing facts. Do not declare successful continuity merely because the checkpoint was written.

Respect adopted retention and explicit reset/no-write instructions. A clean-state reset preserves current accepted policy and required attribution, not old run outcomes. Missing historical scores do not block present work, and local upkeep does not authorize remote synchronization or publication.
