# Current toolkit checkpoint

**Workstream, 2026-11-26:** website skill set rewrite and findability (search and AI-answer visibility). Branch `main`. Commit `38883ed` holds the work. The local `origin/main` ref records a push of it; the agent did not push. A following local commit holds the publish-gate fix in [website-deliver](../skillmesh/skills/website-deliver/SKILL.md) and this record; Git owns its identity. That commit and later ones were not pushed.

## Done

- **Rewrite:** the website skills now follow the authoring standard (short lead, Terms, "Label: action" bullets, conditional references).
- **Findability:** added across brief, discover, create, build, review and deliver, with a launch baseline, crawler-policy decision, publish gate on Blocking findings, and form-mail and consent checks.
- **New:** [website-operate](../skillmesh/skills/website-operate/SKILL.md) for post-launch review, and an [identity reference](../skillmesh/skills/website-create/references/identity.md) in website-create. The library has 24 skills.
- **Gate fix:** a simulated primary form never ships, even with owner acceptance.

## Accepted owner decisions

| Decision | Boundary or revisit condition |
| --- | --- |
| Search and AI search are part of the existing process, not a new skill | None set |
| `website` is renamed `website-brief` | Legacy migration names keep the old `website` |
| `website-operate` covers post-launch work | More post-launch processes can join it. Recurring review needs owner authorization |
| Brand identity lives in website-create | Reconsider a separate skill if standalone identity requests appear |
| Ongoing content program is deferred | Think it over later |
| Skill OS never purchases anything | The rule lives only in [AGENTS.md](../AGENTS.md). Per-skill blocks were removed at the owner's request |
| Working rules | `main` only; experiments in the sibling `skill-os-test` folder; show planned skill wording before editing; commit or push only when asked |

The accepted permission model is unchanged. See [retained decisions](lessons-learned.md) and the [owning contract](../skillmesh/skills/app-backend/references/identity-and-authorization.md).

## Evidence

- **Structure:** with the gate fix applied, library validation reports 24 skills and 0 errors. The unit suite ran 49 tests, 48 passed and one skipped. Migration and live-host checks were not run.
- **Restatement checks:** Haiku readers answered questions written by the editing agent. They show the text can be restated, not that behavior improved.
- **Independent review:** one fresh Sonnet review gave 25 findings before the three fix passes. Paraphrased duplicates and the readability wording were left as they were. The final text has had no independent review.
- **Scenario, bound to `38883ed`:** one fictional launch task, one Haiku run per version, current text against the pre-search rewrite, both given the AGENTS.md purchase rule. A Sonnet grader scored version-label-scrubbed outputs; the editing agent spot-checked them.

| Comparative score, 13 items | Pre-search | `38883ed` |
| --- | --- | --- |
| Grader scoring | 6 | 12 |
| Every part of each item required | 3 | 11 |

- **Scenario limits:** the key came mostly from the added text, so the result is partly circular. n=1, fictional, both outputs over the 900-word limit, and vocabulary may have hinted at the version. No real-site, ranking or citation benefit is established.
- **Scenario observations:** neither output named a post-launch search and analytics reviewer. The older output covered keyboard and form-error checks, measurement events, content-editing handover and testimonial permissions better. The current skills still hold that guidance; crowding by new text is an untested guess.
- **Scenario finding:** the publish gate conflicted with the simulated-form rule. The gate fix addresses it; no behavior check ran on the fix.
- **Local test material:** `skill-os-test/library-pass/` on this device holds drafts, questions, the scenario key and outputs. It is not committed and no scenario was added to `evals/`.

## Open

1. Fresh independent review of the final website text.
2. Unapplied wording for discover and deliver: if no AI assistant can be queried, report unknown and never write an unobserved answer. Neither scenario run invented one.
3. Push the local commits only when the owner asks.
4. Reinstall the package. Installed copies predate this work, including the rename and the new skill.
5. Purchase-rule reach: AGENTS.md is not plugin payload, so installed skills do not carry the rule. A few inline purchase guards remain in the website skills. Adding the rule to the [portable project instructions](../skillmesh/skills/project-context/assets/project-instructions.md) is a proposal only.
6. [Roadmap](opportunity-roadmap.md) items such as CR-02/03 remain proposals.

**Installation:** not performed or verified in this workstream. A pasted owner handoff reported release `0.2.0+codex.20261125063121379` installed on another device; that is unverified here. Its referenced `docs/handoff-new-device.md` was not found in this checkout.

**Next:** start a fresh session from this checkpoint. Real-application adoption, cross-device rollout, provider tokens, elapsed effort, charges, rework and savings remain unknown.

## Latest session assessment, 2026-11-26, self-assessment

One work period covering 2026-11-25 and 2026-11-26.

| Factor | Score | Reason |
| --- | --- | --- |
| Continuity | 1 | Work resumed from a pasted handoff and across a day break. The handoff file was missing, and this record stayed stale until closeout |
| Decision fidelity | 1 | Owner decisions and commit authority were followed, and most skill wording was previewed. The requested removal of purchase blocks was applied without a preview |
| Evidence freshness | 1 | The scenario is bound to `38883ed`. The later gate fix has structural checks only, and the independent review predates the fix passes |
| Retrieval economy | 0 | The session far exceeded the AGENTS.md session bound, and the owner was told only at the end |
| Project/workstream separation | 2 | Drafts and eval runs stayed in the sibling test folder; no application project was touched |
| Review independence | 1 | One fresh review and a label-scrubbed grader were used. The editing agent wrote the questions and scoring key |

Provider usage, cost and savings were not measured and are unknown.
