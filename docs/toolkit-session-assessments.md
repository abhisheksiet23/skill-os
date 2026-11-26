# Current toolkit checkpoint

**Workstream, 2026-11-26:** make the website skills beat a no-skill run on looks and judgment at acceptable cost. Branch `main`, fast-forwarded to `9605049` (`origin/main`). Local commit `7fb84fd` holds the business-findings wording. A following local commit holds this record; Git owns its identity. Neither was pushed when written.

## Done

- **Business findings:** [website-brief](../skillmesh/skills/website-brief/SKILL.md) uses existing findings, names gaps and recommends matching expertise, and keeps provisional prices and packaging off the page. [website-create](../skillmesh/skills/website-create/SKILL.md) states which sources can support a claim. [website-discover](../skillmesh/skills/website-discover/SKILL.md) applies its reuse conditions to findings.
- **Source:** a patch pasted from a cloud session, which names commit `9ef9a84` (not present here). Its file hashes matched before the wording was revised. The revision replaced "describe how it will be set", stopped confirmed facts being limited to findings files, and kept hypotheses as hypotheses.
- **Earlier, committed:** the website rewrite and findability, [website-operate](../skillmesh/skills/website-operate/SKILL.md), the [identity reference](../skillmesh/skills/website-create/references/identity.md) and the simulated-form publish gate.

## Accepted owner decisions

| Decision | Boundary or revisit condition |
| --- | --- |
| Test whether business-skill output should feed the website skills | A hypothesis under test, not an established benefit. Skills only recommend expertise |
| Apply the revised business-findings wording | Approved 2026-11-26. Local commit authorized; push not authorized |
| Judge website design by effect: what colors connote and how well type works, not how distinctive fonts are | Owner direction, 2026-11-26. The wording matched the owner's meaning but showed no visible difference in testing and is not applied |
| Close the website-looks workstream | Owner, 2026-11-26. Reopen only on request |
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
- **Visual comparison, 2026-11-26:** one page each from no skills, current skills (the guard-run page) and current skills plus a draft visual-craft reference (test copy only). The owner judged shuffled screenshots: no-skill colors a bit better on desktop, its phone fonts weak; the draft's content and logo better; full desktop pages almost the same. No overall ranking or client-ready judgment. Tokens: 88.0k, 122.5k and 124.3k. The draft showed no visible change in overall look and is not adopted; its worker did read it. n=1 each. Details: `skill-os-test/website-craft/results-compare.md`.
- **Design-method test, 2026-11-26:** one no-skill worker inspected reference sites, rendered alternative openings and could use web fonts and image files. Against the first no-skill page, the owner judged it not better, with fonts too fancy. 151.3k tokens against 88.0k. Not blind, n=1, several changes at once. Not adopted. Details: `skill-os-test/website-craft/results-method.md`.
- **Color and type wording test, 2026-11-26:** two runs each of current website-create and the same with the owner-approved color and type wording, pass rule written first, pages shuffled. The owner judged all four much the same and all OK, so the rule was not met. Tokens: current 139.3k and 139.5k, new 115.5k and 126.1k; too few runs to claim a saving. Details: `skill-os-test/website-effect/` (patch, rule, results).
- **Not shown:** the worker listed gaps but did not recommend pricing, market research or demand validation by name. A findings file was present, so the "When missing" rule was barely exercised.
- **Prior experiments, reported by the pasted handoff and not verified here:** one run per arm, lead-graded, not blind, same fictional firm. Business input changed content modestly, not looks; findings plus site used about 178k tokens against 78k with no skill. The handoff judged visual craft the weak link. The original files are not on this device.
- **Earlier website rewrite:** one scenario run per version favored the rewrite (12 against 6 of 13) with a partly circular key. One independent review predates the final fixes.
- **Local test material:** `skill-os-test/website-guard/` (patches, criteria, results, backup of the replaced local checkpoint) and `skill-os-test/tidewater-run1/` (the run).

## Open

1. Push this change only when the owner asks.
2. Website looks: closed by the owner. Three attempts (visual-craft draft, reference-and-alternatives method, color and type wording) showed no clear overall improvement. A skill advantage over no-skill on looks is not established. Items 3 and 4 below are parked with it.
3. Cut tokens: lighter website-brief, conditional reference loading, at most two critique rounds, less guidance the base model already follows.
4. Larger test: multi-page brief, 3 runs per arm (no skill; website skills; with business findings), rubric written first, a separate blind grader; record tokens, tool calls and time. Add to `evals/` only if the owner wants it kept. Include a case with no findings file.
5. Fresh independent review of the final website text.
6. Unapplied wording for discover and deliver: if no AI assistant can be queried, report unknown and never write an unobserved answer.
7. Reinstall the package. Installed copies predate the website rewrite and this change.
8. Purchase-rule reach: installed skills do not carry the AGENTS.md rule. Adding it to the [portable project instructions](../skillmesh/skills/project-context/assets/project-instructions.md) is a proposal only.
9. [Roadmap](opportunity-roadmap.md) items such as CR-02/03 remain proposals.

**Installation:** not performed in this workstream. An earlier local record reports release `0.2.0+codex.20261125063121379`, built from `6c8b61b`, installed on this device; it was not rechecked. The untracked `docs/handoff-new-device.md` is an older 2026-11-25 handoff.

**Next:** the owner picks new work, in a fresh session; push when asked. Real-application adoption, cross-device rollout, account usage, charges, rework and savings remain unknown.

## Latest session assessment, 2026-11-26, self-assessment

| Factor | Score | Reason |
| --- | --- | --- |
| Continuity | 1 | Recovered from a pasted handoff. The cloud commit, experiment files and original fixtures were unavailable |
| Decision fidelity | 2 | Revised wording was shown and approved before editing; commit only on request and no push; local files backed up before the update |
| Evidence freshness | 1 | Structural checks and runs match their stated candidates. Samples are one or two runs per setup; older results are unverified or predate the wording |
| Retrieval economy | 1 | Reads were targeted, but the session ran long past the AGENTS.md bound; a fresh session was suggested late |
| Project/workstream separation | 2 | Test copies, fixtures and runs stayed in the sibling test folder |
| Review independence | 1 | Workers were not told the criteria. The owner judged looks, blind in two of three comparisons; the editing agent wrote and graded the price check |

Subagent usage per run is reported above. Total session usage, cost and savings are unknown.
