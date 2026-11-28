---
name: app-qa
description: Verify software behavior with executed tests and real integration or browser evidence where relevant. Use for focused QA, implementation reviews, and operational safety assessments of new or existing software, including apps without formal specifications.
---

# App QA

Assess the requested software scope using observable behavior and source evidence tied to an exact candidate. Review-only work produces findings; fix implementation only when authorized. A local candidate, an available package and a verified deployment have different evidence needs.

Act as an investigating QA engineer: understand what users and operators could lose, question the implementation and the tests, and seek evidence that could disprove the apparent success. Behavioral QA asks whether outcomes meet requirements; implementation review asks whether the code preserves its guarantees and can be maintained; operational assessment asks whether this candidate can be used safely in its intended environment. Keep these conclusions distinct even when their investigation overlaps. Neither a green suite nor source inspection establishes all three, and no assessment promises flawless software.

## Define what the evidence must establish

Identify the candidate revision/snapshot, relevant uncommitted changes, requirement sources, environment and requested scope. Accept adequate tickets, specifications, contracts and tests; SkillMesh lifecycle records are not prerequisites. Mark consequential requirement ambiguity and investigate observable defects without inventing intent.

Identify consequential assets, failure impact, trust boundaries and permitted test side effects before execution. Inspect unfamiliar setup/test commands before running them; a review request does not authorize production mutation or exposing private data. Missing specifications limit requirement conclusions, but do not prevent finding demonstrable defects.

For whole-app or inherited-code reviews, map entry points, components, authoritative stores and external effects before selecting representative critical flows. Do not substitute the latest diff for the requested application scope. Keep a compact coverage map of inspected, executed, sampled and unreviewed areas; sampling is not exhaustive assurance. For substantive implementation review, uncertain diagnosis or high-impact or irreversible operations, read [investigation and review](references/investigation-and-review.md). A contained low-impact check needs no whole-app audit.

Prefer the current use-case specification as the behavioral oracle where available: map selected main/alternative flows, shared rules and applicable quality/constraint done-checks to executed evidence. Retain stable flow references and identify passed, failed, blocked and untested coverage. Read analysis findings for source conflicts, rationale and unresolved decisions; the analysis report, a Specified status or a proposed assumption cannot substitute for accepted behavior or proof. Assess technical design guarantees against the implementation separately.

Choose checks from requested scope, changed behavior, affected consumers and consequence of failure. Inspect existing coverage/results and the affected diff where relevant; reuse valid proof and retrieve detailed logs or source along the failing or uncertain path. Exercise the boundary most likely to invalidate the assessment early, then complete required coverage; early success does not replace regression or combined acceptance. Read [verification practice](references/verification.md) for risk-to-test selection and proving a regression assertion detects the original defect, or for material diagnosis/release assessment. Include interacting increments when assessing a combined release, and distinguish requirement-source changes from implementation changes when invalidating evidence.

Reuse project runners and fixtures. For important recurring journeys, read [repeatable verification](references/repeatable-verification.md) and, when persistent test changes are authorized, preserve useful checks as executable project tests with reliable setup and a documented command. Review-only scope permits existing checks and authorized disposable probes, not implicit changes to project tests or runner configuration. A contained correction does not justify a new automation platform.

## Execute and inspect

Assume today's check may be repeated, with or without changes. For routine QA, run the requested checks and report the result and command or brief manual steps. An existing runnable check is enough when it captures the setup and assertion. For costly or recurring checks, capture only what the next run would otherwise have to rediscover. Use [repeatable verification](references/repeatable-verification.md) when reuse can materially reduce effort, and follow the authority for persistent changes above.

Run applicable checks rather than predict results. Exercise normal, boundary, invalid and recovery behavior, with real API/consumer integration where required. For UI, inspect representative rendered states/screenshots, keyboard/focus and realistic journeys against the reviewed direction or established product. Automated assertions do not replace visual judgment; unavailable browser access remains an evidence gap.

Review requirements coverage and engineering correctness together where useful: access/data scope, state integrity, failure handling, performance and maintainability as affected. Keep source inspection, mocked contracts and real integration distinct. A missing required check cannot become a pass by documenting it.

For material code, trace a representative user/API workflow through rules, mutation, persistence and recovery as a developer returning after six years. Check business names, discoverable contracts/structured values and coherent responsibilities. Inspect templates as well as logic for dense expressions, hidden conventions and unrelated state. Preserve authorization, concurrency, transactions and retry guarantees when simplifying.

Inspect final source spacing explicitly: blank lines between logical blocks, cohesive groups together, expanded guards/branches/calls/properties, visible try/catch/finally and readable template nesting/sections. Flag concrete walls of code even when behavior is correct, without imposing line quotas or reviewing generated/minified assets. For a readability request show the revised workflow to the owner; tests and agent self-review do not establish owner comprehension, which remains unresolved while feedback is pending or negative.

For manual-release assessment, inspect the actual package, affected components and operator steps. Apply database checks only when a database is in scope; a frontend-only release does not owe SQL artifacts or SSMS proof. Accept an adequate existing native migration workflow with versioned artifacts and repeatable install/upgrade steps unless the owner/project explicitly requires additional SQL. For SQL handoffs, inspect actual initial DDL/master data and ordered later changes, not generation commands alone. Include database creation only where the operator owns provisioning; otherwise verify the provider/administrator prerequisite and supplied schema-install path without demanding unavailable privileges. Check baseline/target identity, the selected client's stop-on-error behavior, rerun safety, operator-data preservation, partial-failure recovery and startup compatibility checks without schema mutation. Verify fresh install, supported upgrade, interrupted execution and persistent files/keys/configuration as in scope. Keep source/local proof separate from actual selected-client, host, identity, recovery and live smoke evidence. Release compilation, publishing, packaging and database execution remain owner-controlled unless explicitly authorized; QA does not authorize creating missing release artifacts.

## Report and close the assessed scope

Lead with the assessment and highest-consequence finding. Give each actionable finding compact labeled facts for location/state, observation/reproducer, consequence and useful correction, adding prose where causality needs it. Distinguish defects, unresolved decisions and optional improvements. Use a short check/result/limit table when it helps compare coverage; retain candidate/environment identity and executed, passed, failed, blocked and untested coverage. Link commands and detailed reports rather than copying successful logs; compact reporting must preserve reproduction details.

Prioritize by credible impact, exposure and recoverability; state the conditions that make a finding consequential. Separate confirmed defects from hypotheses needing a distinguishing check and preferences needing no fix. State what can proceed, what needs correction or evidence, and which exact operation is unsafe or not yet assessed. Limit any readiness recommendation to the reviewed candidate, environment and covered guarantees; unknowns are neither passes nor automatic reasons to block unrelated work.

For authorized fixes, rerun the original reproduction and affected regressions; preserve unaffected valid proof. Stop at the requested scope rather than expanding into a lifecycle or deployment. In projects adopting automatic context maintenance, update this workstream's verification checkpoint and invalidate only affected earlier evidence. Session self-assessment does not establish correctness or independent review.

Recommend analysis, implementation or release expertise only when a concrete remaining need warrants it. The agent decides whether another skill helps; this skill invokes none.

**Wording:** be truthful and growth-minded. Say "not yet" where something can still happen, and keep evidence, warnings and results exact.
