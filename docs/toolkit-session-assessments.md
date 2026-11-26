# Current toolkit checkpoint

**Workstream, 2026-11-26:** make the website skills beat a no-skill run on looks and judgment at acceptable cost. Branch `main`, fast-forwarded to `9605049` (`origin/main`). The commit holding this record also holds the business-findings wording; Git owns its identity. It was not pushed when written.

## Done

- **Business findings:** [website-brief](../skillmesh/skills/website-brief/SKILL.md) uses existing findings, names gaps and recommends matching expertise, and keeps provisional prices and packaging off the page. [website-create](../skillmesh/skills/website-create/SKILL.md) states which sources can support a claim. [website-discover](../skillmesh/skills/website-discover/SKILL.md) applies its reuse conditions to findings.
- **Source:** a patch pasted from a cloud session, which names commit `9ef9a84` (not present here). Its file hashes matched before the wording was revised. The revision replaced "describe how it will be set", stopped confirmed facts being limited to findings files, and kept hypotheses as hypotheses.
- **Earlier, committed:** the website rewrite and findability, [website-operate](../skillmesh/skills/website-operate/SKILL.md), the [identity reference](../skillmesh/skills/website-create/references/identity.md) and the simulated-form publish gate.

## Accepted owner decisions

| Decision | Boundary or revisit condition |
| --- | --- |
| Test whether business-skill output should feed the website skills | A hypothesis under test, not an established benefit. Skills only recommend expertise |
| Apply the revised business-findings wording | Approved 2026-11-26. Local commit authorized; push not authorized |
| Search and AI search are part of the existing process, not a new skill | None set |
| `website` is renamed `website-brief` | Legacy migration names keep the old `website` |
| `website-operate` covers post-launch work | More post-launch processes can join it. Recurring review needs owner authorization |
| Brand identity lives in website-create | Reconsider a separate skill if standalone identity requests appear |
| Ongoing content program is deferred | Think it over later |
| Skill OS never purchases anything | The rule lives only in [AGENTS.md](../AGENTS.md). Per-skill blocks were removed at the owner's request |
| Working rules | `main` only; experiments in the sibling `skill-os-test` folder; show planned skill wording before editing; commit or push only when asked |

The accepted permission model is unchanged. See [retained decisions](lessons-learned.md) and the [owning contract](../skillmesh/skills/app-backend/references/identity-and-authorization.md).

## Evidence

- **Structure:** with the new wording, validation reports 24 skills and 0 errors. The unit suite ran 49 tests: 48 passed, one skipped. Migration and live-host checks were not run.
- **Price guard, one run:** one Sonnet worker, fictional bookkeeping firm with recreated fixtures, current wording. All four price criteria passed: neither provisional price hypothesis reached the page, no other unconfirmed price or package appeared, and the confirmed free call stayed. 122.5k subagent tokens, 28 tool calls, 234s, including web search and browser checks.
- **Price guard limits:** n=1, no run with the original wording, criteria written and graded by the editing agent. Looks were not graded and the worker's transcript was not audited.
- **Not shown:** the worker listed gaps but did not recommend pricing, market research or demand validation by name. A findings file was present, so the "When missing" rule was barely exercised.
- **Prior experiments, reported by the pasted handoff and not verified here:** one run per arm, lead-graded, not blind, same fictional firm. Business input changed content modestly, not looks; findings plus site used about 178k tokens against 78k with no skill. The handoff judged visual craft the weak link. The original files are not on this device.
- **Earlier website rewrite:** one scenario run per version favored the rewrite (12 against 6 of 13) with a partly circular key. One independent review predates the final fixes.
- **Local test material:** `skill-os-test/website-guard/` (patches, criteria, results, backup of the replaced local checkpoint) and `skill-os-test/tidewater-run1/` (the run).

## Open

1. Push this change only when the owner asks.
2. Add concrete visual-craft guidance to website-create. Show the wording first.
3. Cut tokens: lighter website-brief, conditional reference loading, at most two critique rounds, less guidance the base model already follows.
4. Larger test: multi-page brief, 3 runs per arm (no skill; website skills; with business findings), rubric written first, a separate blind grader; record tokens, tool calls and time. Add to `evals/` only if the owner wants it kept. Include a case with no findings file.
5. Fresh independent review of the final website text.
6. Unapplied wording for discover and deliver: if no AI assistant can be queried, report unknown and never write an unobserved answer.
7. Reinstall the package. Installed copies predate the website rewrite and this change.
8. Purchase-rule reach: installed skills do not carry the AGENTS.md rule. Adding it to the [portable project instructions](../skillmesh/skills/project-context/assets/project-instructions.md) is a proposal only.
9. [Roadmap](opportunity-roadmap.md) items such as CR-02/03 remain proposals.

**Installation:** not performed in this workstream. An earlier local record reports release `0.2.0+codex.20261125063121379`, built from `6c8b61b`, installed on this device; it was not rechecked. The untracked `docs/handoff-new-device.md` is an older 2026-11-25 handoff.

**Next:** visual-craft guidance; push when the owner asks. Real-application adoption, cross-device rollout, account usage, charges, rework and savings remain unknown.

## Latest session assessment, 2026-11-26, self-assessment

| Factor | Score | Reason |
| --- | --- | --- |
| Continuity | 1 | Recovered from a pasted handoff. The cloud commit, experiment files and original fixtures were unavailable |
| Decision fidelity | 2 | Revised wording was shown and approved before editing; commit only on request and no push; local files backed up before the update |
| Evidence freshness | 1 | Structural checks and the guard run match the current wording. The run is single and uncontrolled; older results are unverified or predate it |
| Retrieval economy | 2 | Reads were limited to the affected skills, records and run output |
| Project/workstream separation | 2 | Test copies, fixtures and the run stayed in the sibling test folder |
| Review independence | 1 | The worker was not told the criteria; the editing agent wrote and graded them |

Subagent usage for the guard run is reported above. Total session usage, cost and savings are unknown.
