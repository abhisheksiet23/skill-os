# Current toolkit checkpoint

**Workstream, 2026-11-26:** editorial review of the seven website skills. Branch `main`. The local commit holding this record also holds the approved wording; Git owns its identity. The owner asked for a commit and push; it was not pushed when written. `96ee11b` was on `origin/main` before it.

## Done

- **Fixes:** website-deliver's publication-authority sentence is whole again and it defines a Blocking finding; the post-launch crawler check no longer asks a prelaunch question; website-build no longer implies authorization permits purchases or domain registration; website-review reports verification beside readiness; the page-text rule names only approved price ranges.
- **Gaps closed:** the never-ships gate covers any simulated primary conversion; website-operate keeps the launch baseline unchanged and adds dated results; discover, deliver, operate and review report an unqueried AI assistant as unknown, and the agent's own reply is not an observation.
- **Cleanup:** website-brief description; repeated handoff lines in the release reference; overlap in creative practice; website-review evidence reuse and short-summary contents; vague references; two filler phrases; the review row in [SKILLS.md](../SKILLS.md).
- **Readiness decisions:** only Blocking findings make a site need changes; ready requires the main conversion path and central claims to be checked; website-review and website-deliver encourage the owner to close other material problems. Exposed secrets, unauthorized private data, known false claims and simulated primary conversions never ship. website-deliver checks the essentials before publishing, reviewed or not.
- **Known trims:** the removed creative-practice bullet had suggested comparison columns and a "small number" of concepts. Smaller assets no longer ask for role and crop. The library grew from 17,413 to 17,508 words by `wc`, then to 17,806 with the readiness decisions.
- **Earlier, committed:** business findings, website-review's right-customer goal and business-work recommendations, the website rewrite, findability, website-operate and the identity reference.

## Accepted owner decisions

| Decision | Boundary or revisit condition |
| --- | --- |
| Test whether business-skill output should feed the website skills | A hypothesis under test, not an established benefit. Skills only recommend expertise |
| Apply the revised business-findings wording | Approved 2026-11-26. Local commit authorized; push not authorized |
| Judge website design by effect: what colors connote and how well type works, not how distinctive fonts are | Owner direction, 2026-11-26. The wording matched the owner's meaning but showed no visible difference in testing and is not applied |
| website-review's goal is helping the site win more of the right customers | Owner choice and approved wording, 2026-11-26. A review cannot show that a change will win customers |
| website-review makes the case for missing business work | Wording approved 2026-11-26. Persuade honestly; never block or push |
| Close the website-looks workstream | Owner, 2026-11-26. Reopen only on request |
| Search and AI search are part of the existing process, not a new skill | None set |
| `website` is renamed `website-brief` | Legacy migration names keep the old `website` |
| `website-operate` covers post-launch work | More post-launch processes can join it. Recurring review needs owner authorization |
| Brand identity lives in website-create | Reconsider a separate skill if standalone identity requests appear |
| Ongoing content program is deferred | Think it over later |
| Skill OS never purchases anything | The rule is in [AGENTS.md](../AGENTS.md). Per-skill blocks were removed at the owner's request. Short in-line reminders remain; the website-build line was approved 2026-11-26 |
| Only blocking problems make a site not ready; encourage the owner to close the rest | Wording approved 2026-11-26. Do not press again without new evidence |
| Never publish exposed secrets, unauthorized private data or known false claims | Owner, 2026-11-26. No risk acceptance covers them |
| Check the main conversion path and central claims before publishing, or get explicit acceptance of the gap | Owner, 2026-11-26. A fake conversion still cannot ship |
| Readiness wording choices | Approved 2026-11-26: unproven receipt may remain a named gap; unsupported central claims and inaccessible main journeys block; an unfinished look blocks only if it defeats safe intended use |
| Apply the editorial review draft | Approved 2026-11-26, including the wider never-ships gate and the short-summary contents. Commit and push not requested |
| Working rules | `main` only; experiments in the sibling `skill-os-test` folder; show planned skill wording before editing; commit or push only when asked |

The accepted permission model is unchanged. See [retained decisions](lessons-learned.md) and the [owning contract](../skillmesh/skills/app-backend/references/identity-and-authorization.md).

## Evidence

- **Editorial review:** a text read of all 16 website files, not a behavior test. The patch applied cleanly and matched the tested copy, ignoring line endings. The agent challenged its own findings; this was not independent, and it had read this checkpoint first. Four past review outputs all reported verification status, so that gap was minor. All four said "needs changes", one with no blocking defect seen; their samples had real problems. Patch and script: `skill-os-test/website-editorial/`.
- **Structure:** with the new wording, validation reports 24 skills and 0 errors. The unit suite ran 49 tests: 48 passed, one skipped. Migration and live-host checks were not run.
- **Price guard, one run:** one Sonnet worker, fictional bookkeeping firm with recreated fixtures, current wording. All four price criteria passed: neither provisional price hypothesis reached the page, no other unconfirmed price or package appeared, and the confirmed free call stayed. 122.5k subagent tokens, 28 tool calls, 234s, including web search and browser checks.
- **Price guard limits:** n=1, no run with the original wording, criteria written and graded by the editing agent. Looks were not graded and the worker's transcript was not audited.
- **Visual comparison, 2026-11-26:** one page each from no skills, current skills (the guard-run page) and current skills plus a draft visual-craft reference (test copy only). The owner judged shuffled screenshots: no-skill colors a bit better on desktop, its phone fonts weak; the draft's content and logo better; full desktop pages almost the same. No overall ranking or client-ready judgment. Tokens: 88.0k, 122.5k and 124.3k. The draft showed no visible change in overall look and is not adopted; its worker did read it. n=1 each. Details: `skill-os-test/website-craft/results-compare.md`.
- **Design-method test, 2026-11-26:** one no-skill worker inspected reference sites, rendered alternative openings and could use web fonts and image files. Against the first no-skill page, the owner judged it not better, with fonts too fancy. 151.3k tokens against 88.0k. Not blind, n=1, several changes at once. Not adopted. Details: `skill-os-test/website-craft/results-method.md`.
- **Color and type wording test, 2026-11-26:** two runs each of current website-create and the same with the owner-approved color and type wording, pass rule written first, pages shuffled. The owner judged all four much the same and all OK, so the rule was not met. Tokens: current 139.3k and 139.5k, new 115.5k and 126.1k; too few runs to claim a saving. Details: `skill-os-test/website-effect/` (patch, rule, results).
- **Real-site review comparison, 2026-11-26:** one run each of website-review before and after the right-customer rewrite on a public bookkeeping site. The owner liked the new review's findings-by-consequence section and found the rest much the same. The editing agent, not blind, judged neither clearly better: the new one framed customer, trust, keep and measurement better; the old one ranked a cut-off booking calendar first, which the new one buried. Tokens: 207.9k new, 200.6k old. Details: `skill-os-test/site-compare/results.md`.
- **Not shown:** the worker listed gaps but did not recommend pricing, market research or demand validation by name. A findings file was present, so the "When missing" rule was barely exercised.
- **Prior experiments, reported by the pasted handoff and not verified here:** one run per arm, lead-graded, not blind, same fictional firm. Business input changed content modestly, not looks; findings plus site used about 178k tokens against 78k with no skill. The handoff judged visual craft the weak link. The original files are not on this device.
- **Earlier website rewrite:** one scenario run per version favored the rewrite (12 against 6 of 13) with a partly circular key. One independent review predates the final fixes.
- **Local test material:** `skill-os-test/website-guard/` (patches, criteria, results, backup of the replaced local checkpoint) and `skill-os-test/tidewater-run1/` (the run).

## Open

1. Larger test: multi-page brief, 3 runs per arm (no skill; website skills; with business findings), rubric written first, a separate blind grader; record tokens, tool calls and time. Include a case with no findings file. Add to `evals/` only if the owner wants it kept. The review recommends this over further editing.
2. Fresh independent review of the final website text.
3. Untested behavior: the editorial and readiness wording, the website-brief description's effect on skill selection, website-review's summary and main-action lines, and a harder business-recommendation hold-back case. The website-review rewrite showed no clear overall gain on one real site.
4. Whether website-brief earns its place is unsettled. Do not remove it without a test.
5. Website looks: closed by the owner. Three attempts showed no clear overall improvement, and a skill advantage over no-skill is not established. Token cuts and the visual part of item 1 are parked with it.
6. Reinstall the package. Installed copies predate the website rewrite and later changes.
7. Purchase-rule reach: installed skills do not carry the AGENTS.md rule. Adding it to the [portable project instructions](../skillmesh/skills/project-context/assets/project-instructions.md) is a proposal only.
8. [Roadmap](opportunity-roadmap.md) items such as CR-02/03 remain proposals.

**Installation:** not performed in this workstream. An earlier local record reports release `0.2.0+codex.20261125063121379`, built from `6c8b61b`, installed on this device; it was not rechecked. The untracked `docs/handoff-new-device.md` is an older 2026-11-25 handoff.

**Next:** further commits or pushes only when asked. Real-application adoption, cross-device rollout, account usage, charges, rework and savings remain unknown.

## Latest session assessment, 2026-11-26, self-assessment

| Factor | Score | Reason |
| --- | --- | --- |
| Continuity | 2 | The checkpoint and local test material were enough to resume and to test findings against past outputs |
| Decision fidelity | 2 | Both drafts were built on a test copy and applied after approval. Commit and push followed the owner's request |
| Evidence freshness | 1 | Validation and tests match the applied text. Its behavior is untested, and past outputs used earlier wording |
| Retrieval economy | 1 | All website files were read once, as an editorial review needs. Some history searches returned much unrelated output |
| Project/workstream separation | 2 | The draft copy, patch and script stayed in the sibling test folder |
| Review independence | 0 | The same agent reviewed, challenged its own findings and wrote the fixes. The first review claimed too much on two points and mislabelled a cross-skill repeat |

Total session usage, cost and savings are unknown.
