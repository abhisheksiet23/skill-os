# Code navigation assessment key (draft)

Keep this file and `code-navigation-variants.json` from performers. Performers receive only a case's `scenario` plus the file's `response_format`, and their frozen skill variant.

## Status

Draft. Cases are synthetic decisions, not observations from a live provider. The regex scoring is coarse and has been self-tested on a handful of hand-written good and bad answers only; it has not been checked against real performer output. Before trusting scores, run both the baseline skill and a candidate on the full set, read 5–10 responses against their scores, and correct regexes that mis-score. A candidate that ties the baseline has not shown improved behavior.

## Baseline run 1

The unchanged `code-navigation` skill, performed by fresh Haiku contexts (4 batches of 9 cases, skill text and scenarios only), scored 28/36 on the first scoring pass. Reading all 8 failures showed every one was a scorer fault: missed wording ("review-only", "unresolved", "fresh ... process") and "Skip ..." or "if a query fails, recheck" lines wrongly counted as forbidden actions. After fixing the regexes the baseline scores 36/36 and 8 hand-written bad answers still score 0. The regexes were tuned on these same responses, so treat 36/36 as a ceiling, not a validated pass rate. Main finding: the skill already passes these cases, so they leave no headroom to show improvement. Harder or more adversarial cases are needed before they can discriminate between variants, and before an optimizer such as SkillOpt has a gradient.

## Hard set and baseline run 2

`code-navigation-hard-variants.json` adds 20 cases (H01–H20; 12 train, 4 val, 4 test) built to beat the baseline: rule conflicts (write scope vs stale provider), social pressure, distractor facts, tempting shortcuts (bump TargetFramework, kill an idle provider, run a README curl script, save to Serena memory), overclaiming and savings claims, and one skip case where the skill should not apply. Same format and scoring as above.

Baseline (unchanged skill, fresh Haiku contexts, 4 batches of 5) scored 18/20 on the first pass. Both failures were scorer faults (an `all` substring match inside "semantically", and a harmless extra text search flagged as a semantic recheck); after fixing them the baseline scores 20/20. Again the regexes were tuned on these responses. Conclusion: decision-level cases do not separate this skill from a perfect score even with adversarial framing, because the skill text already states each rule and a reader can apply it. Real failures, if any, are more likely in live tool sessions (Serena responses, partial states, long contexts) than in written decisions, so the next evidence has to come from live runs or the historical failures in `docs/lessons-learned.md`.

## Scoring

`code-navigation-variants.json` holds 36 cases (9 patterns x 4). Each has `must` groups (a group passes if any regex in it matches the response) and `must_not` regexes (a violation if one matches an ACTIONS line without a negation word). `hard` is 1 only when every group passes with no violation; `soft` is passed groups over total, minus 0.5 per violation, floored at 0. Where the pattern's expected answer is judgment-heavy, a person or agent may score 0/1/2 on correct decision, evidence discipline and proportionality instead, and use the regexes only as a first pass.

## Splits

Variants `a` and `b` of each pattern are `train`, `c` is `val`, `d` is `test` (18/9/9). Variant `b` and `d` of most patterns are flips: the surface looks the same but the correct decision differs, so a candidate that just learns "never activate" or "never recheck" fails them. The original four cases in `code-navigation-tasks.md` correspond to P1a, P2a, P3a and P4a.

## Patterns

| ID | Pattern | Correct decision | Flips |
|---|---|---|---|
| P1 | stale-config | Saved config and successful reactivation do not prove reload. Use the host refresh or a fresh task-owned provider, recheck the affected lookup, and keep working via search meanwhile. Never terminate another chat's provider or install dependencies unprompted. | b: no refresh path, so search and report the gap. d: fresh provider needs unauthorized dependency setup, so search, report and ask. |
| P2 | confined-scope | Validated known definition/reference for the affected language is enough. Use overview, body, then references, scoped; do not probe unrelated languages or repeat checks. | b: the change crosses into the sibling, so validate it first. d: relationship question needs one known caller/reference check. |
| P3 | write-scope | Review-only scope means search and reads with an explicit semantic gap, not activation. | b: writable task, so inspect existing project config, activate the absolute root, confirm and validate. d: unexpected activation command, so do not run it; search and surface it. |
| P4 | no-repeat | Unchanged binding, config and candidate inputs need no refresh, new process, setup or repeated checks. | b: config changed, so recheck the affected lookup. d: worktree/project switch, so recheck the root. |
| P5 | empty-result | An empty response is not proof of no usages: check initialization, support, ignore rules and corroborate by search, including templates, routes, DI and configuration. | d: semantic and text evidence agree, so conclude no usages with stated scope. |
| P6 | root-binding | Bind the task's absolute root (not the plugin path), confirm with `get_current_config`, recheck after a switch, do not share a mutable provider across unrelated chats. | d: unchanged binding needs no recheck. |
| P7 | line-numbers | Provider line numbers are zero-based; convert before citing. | d: `rg -n` is already one-based. |
| P8 | framework-edges | Verify Angular template relationships, SQL, routes and configuration separately by search. Do not install dependencies or change target frameworks without authorization; report the gap. | a/b/c/d each probe a different edge. |
| P9 | startup | Warm a newly installed backend before simultaneous cold activations. Activation can return before initialization finishes, so wait and retry before blaming config. | b: already warm, no special step. d: checks passed, proceed. |

## Known limits

- Regexes cannot tell a recommendation from a mention; the ACTIONS/LIMITS split and the negation rule reduce but do not remove this.
- Cases test the skill's decision rules, not real Serena behavior or token/time savings. Report those as unknown.
- 36 cases is enough for a first signal, not for strong claims of improvement. Add variants wherever scoring disagreement shows a gap.
