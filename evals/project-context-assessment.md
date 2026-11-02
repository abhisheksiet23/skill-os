# Automatic project context assessment — 2026-11-02

## Outcome

Implemented the project-owned maintenance method and ongoing six-factor session assessment. The new independently usable `project-context` skill bundles the method, rubric and adaptable project-instruction/assessment examples. Toolkit AGENTS.md adopts maintenance and maps this author's project records. Targeted implementation/design/QA/release guidance preserves the consequential decisions and evidence each produces. No memory service, new database, custom routing runtime, global host instruction change or bulk application-project edit was added.

Actual agents updated local synthetic records and separate fresh agents recovered the maintained state. Both baseline and final candidate retained the important scope, unknowns and candidate-specific evidence. The experiment does **not** demonstrate a general quality or efficiency advantage: common actual host instructions already required automatic maintenance and assessment, contaminating baseline attribution. The comparison is useful behavioral evidence for these bounded operations, not proof that the earlier library could not do them.

## Inputs and execution

Baseline snapshot was taken before this patch at merge revision `92b98f0d293e1665b87e28e5a541b06e1e53e3f9`, including the existing uncommitted design-review changes from the earlier authorized work. Candidate snapshots contain the changed skills and instructions. Isolated inputs are the synthetic [Atlas records](fixtures/project-context/AGENTS.md) and [task requests](project-context-tasks.md); the separate [key](project-context-assessment-key.md) was withheld from performers.

Seven native subagents were launched with `fork_turns: "none"`, inherited model/settings and no override: baseline closeout, initial candidate closeout, final candidate closeout, baseline resumption, final candidate resumption, one bounded reviewer probe and one small read-only session. Each received only its assigned variant paths/project inputs and task. No performer saw the authoring chat, expected answers, peer outputs or key. Applicable common host instructions remained available. Separate agents handled maintenance and resumption; the latter did not receive the closeout prompt or response. Model version/provider tokens were not exposed in the returned evaluation records.

Closeout performers could modify only their assigned synthetic project and write a result summary. Resumption, probe and small-session performers were read-only. All were prohibited from browsing, installing, delegating, editing production code, running application tests, committing or accessing external systems. Model responses are actual outputs, and closeout documents are actual local edits; the historical test claims in the input fixture remain synthetic and unexecuted.

## Observations and correction

| Check | Observed result | Interpretation |
| --- | --- | --- |
| Record maintenance | Baseline and both candidate runs updated only decisions, the export checkpoint and the assessment record | All retained own-team approval, superseded company-wide rationale, unchanged credentials/schema, provisional email and unknown SSO |
| Evidence freshness | All kept historical A checks separate from unchecked B and identified limits of owner-reported state | No application correctness or runtime pass was inferred |
| Workstream separation | Parent byte comparison confirmed report-layout unchanged in all three project copies | Bounded preservation succeeded; simultaneous writers and foreign-project retrieval were not exercised |
| Initial scoring | Baseline and initial candidate each scored continuity 2 from record maintenance while noting later recovery was unobserved | Assessment inflation was observed; do not count that score as successful fresh recovery |
| Revised scoring | Added an explicit distinction between maintenance-only closeout and separately observed resumption; a new candidate performer scored closeout continuity unknown | Targeted correction worked in this one repeat; broader scoring consistency remains unproved |
| Fresh continuation | Both separate resumption agents recovered accepted scope, B, unknowns, stale A proof and next action from the actual maintained records | Both useful; no demonstrated general advantage. Each returned pending assessments instead of writing under no-write scope |
| Small read-only session | Explained the typo, wrote nothing, avoided architecture work, left continuity unknown and unexercised checks N/A | Respected write scope and proportionate closeout. Method-loading overhead was not compared with an unaided answer |
| Reviewer probe | Actual no-history dispatch; child found the missing team filter/acceptance and reported the parent-only marker unknown | Bounded evidence against obvious transcript leakage; not filesystem, configured-memory or adversarial isolation proof |

The parent's artifact audit recorded hashes and confirmed final candidate skill snapshots match maintained skill files. That check establishes artifact identity/preservation, not reasoning quality. Actual child read scopes are reported in their outputs; the parent did not receive complete native tool traces for independent verification of every read. Neither directory separation nor a prompt restriction enforced filesystem isolation.

Local evidence lives in ignored `.eval-runs/project-context/`: baseline/candidate/candidate-final snapshots; their project copies and closeout outputs; baseline and final candidate resumption responses; small-session and isolation reports; `artifact-evidence.json`. The parent preserved returned read-only reports without authorizing the children to write. The random parent-only marker was never written to files or child prompts. Real project records and assessments are not copied into toolkit evidence by default.

## Validation and remaining uncertainty

- Library validator: 20 skills, zero packaging errors, including the new skill's local links.
- Repository unit suite: eight passed, one skipped because Windows symlink privilege was unavailable. Process-local TEMP/TMP used ignored workspace scratch to avoid sandbox temporary-directory restrictions.
- Whitespace check: passed.
- Official skill-creator validation was attempted for the new skill but could not execute because PyYAML is absent. No dependency was installed; no official-validator pass is claimed.

Provider tokens, latency, cost savings, user correction burden and real delivery rework remain unknown. Word counts and self-reported retrieval scores are not those measurements. Cross-device sync, actual loading in other agent products, real concurrent edits, abrupt-closure recovery and a real application/business-project pilot remain untested. No plugin installation/reload, remote sync or external project adoption was performed by this patch. The [pilot note](../docs/project-context-pilot.md) carries those next observations, and the project-local [session rubric](../skillmesh/skills/project-context/references/session-assessment.md) is the assessment to fill at every adopted project-session closeout.
