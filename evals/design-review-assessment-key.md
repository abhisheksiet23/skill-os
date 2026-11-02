# Design review assessment key

Keep this file from performers. Score actual baseline and candidate outputs without requiring particular wording, a table or a prescribed skill path. Use 0 for absent/incorrect, 1 for partial and 2 for supported and actionable on each applicable dimension: consequential gap detection, evidence/claim discipline, useful correction and proportionality. Record false positives separately. A candidate that ties the baseline has not demonstrated improved behavior.

## Case 1: Portal requirements

The new shell's signed-in state and correct Menu URLs do not establish retained-page session compatibility. The accepted decision supplies the missing intended behavior, but the handoff artifact does not explain or link it. A useful finding locates the gap, explains the separate-sign-in regression, and calls for the existing session contract and acceptance that a new sign-in reaches retained pages without another login. It must not claim observed runtime failure, rewrite the draft against the findings-only request, or demand all Home widgets be analyzed. A paraphrase is useful when it reveals this mismatch; its presence alone earns no credit.

## Case 2: Account-disable plan

The claimed existing methods `DisableAsync`, `RevokeAllForUserAsync` and `FindActiveAsync` do not exist in the complete supplied source. Distinguish stale/invented references from the substantive gap: middleware ignores `Enabled`, so the plan's no-auth-change premise cannot enforce the requirement. A correction must make the enabled check authoritative for subsequent protected requests, using the real repository capabilities or clearly proposed changes. Revocation alone cannot be assumed sufficient. The plan already includes an old-session test; do not report it as absent. No current runtime defect has been executed. Exact new helper names, a complete file inventory or a new identity architecture are unnecessary.

## Case 3: Revised report design

The reproduced issue is browser result retention. The accepted scope and measured query latency supply no need for Redis, a broker or a worker, and another browser cache adds competing freshness state. The revision also leaves the actual feedback about refresh failure and response ordering unanswered. Recommend retaining the focused invalidation/refetch approach, explicit failure/retry behavior and a way to prevent older responses replacing newer ones. Propose observable failure/ordering checks without claiming execution. Do not promise a measured speedup or remove access checks to simplify the design. Rejecting complexity without addressing the original review findings is incomplete.

## Case 4: Settled correction

Keep validation first and preserve an integer result; clamp the calculated difference to zero. Relevant checks include below-limit, exactly-at-limit, over-limit and retained invalid-count behavior. Proposed checks are not executed proof. Do not require a new spec, architectural analysis, extra reviewer, approval gate, platform dependency or unrelated refactor.

## Comparison limits

Record loaded skills/references, whether cases shared context, model/settings when observable, supplied tools and actual outputs. Do not infer broad superiority from a single pair. Fresh evaluators of skill variants test instruction behavior; they do not by themselves prove isolation from every memory source or measure the added value of an independently delegated reviewer. Provider tokens, user interruptions, real delivery rework, cost and latency savings remain unknown unless measured. Ground added instruction overhead in actual content sizes only, not invented provider-token counts.
