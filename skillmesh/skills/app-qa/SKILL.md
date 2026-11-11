---
name: app-qa
description: Verify software behavior and review implementation against requirements using executed tests, real integration and browser evidence where relevant. Use for existing or newly changed software, including standalone QA and review-only requests; no lifecycle records are required.
---

# App QA

Assess the requested software scope using observable behavior and source evidence tied to an exact candidate. Review-only work produces findings; fix implementation only when authorized. A local candidate, an available package and a verified deployment have different evidence needs.

## Define what the evidence must establish

Identify the candidate revision/snapshot, relevant uncommitted changes, requirement sources, environment and requested scope. Accept adequate tickets, specifications, contracts and tests; SkillMesh lifecycle records are not prerequisites. Mark consequential requirement ambiguity and investigate observable defects without inventing intent.

Choose checks from changed behavior, affected consumers and consequence of failure. Inspect existing coverage/results and the affected diff first; reuse valid proof and retrieve detailed logs or source along the failing or uncertain path. Exercise the boundary most likely to invalidate the assessment early, then complete required coverage; early success does not replace regression or combined acceptance. Read [verification practice](references/verification.md) for risk-to-test selection and proving a regression assertion detects the original defect, or for material diagnosis/release assessment. Include interacting increments when assessing a combined release, and distinguish requirement-source changes from implementation changes when invalidating evidence.

Reuse project runners and fixtures. For important recurring journeys, read [repeatable verification](references/repeatable-verification.md) and preserve useful checks as executable project tests with reliable setup and a documented command. A contained correction does not justify a new automation platform.

## Execute and inspect

Run applicable checks rather than predict results. Exercise normal, boundary, invalid and recovery behavior, with real API/consumer integration where required. For UI, inspect representative rendered states/screenshots, keyboard/focus and realistic journeys against the reviewed direction or established product. Automated assertions do not replace visual judgment; unavailable browser access remains an evidence gap.

Review requirements coverage and engineering correctness together where useful: access/data scope, state integrity, failure handling, performance and maintainability as affected. Keep source inspection, mocked contracts and real integration distinct. A missing required check cannot become a pass by documenting it.

For material code, trace a representative user/API workflow through rules, mutation, persistence and recovery as a developer returning after six years. Check business names, discoverable contracts/structured values and coherent responsibilities. Inspect templates as well as logic for dense expressions, hidden conventions and unrelated state. Preserve authorization, concurrency, transactions and retry guarantees when simplifying.

Inspect final source spacing explicitly: blank lines between logical blocks, cohesive groups together, expanded guards/branches/calls/properties, visible try/catch/finally and readable template nesting/sections. Flag concrete walls of code even when behavior is correct, without imposing line quotas or reviewing generated/minified assets. For a readability request show the revised workflow to the owner; tests and agent self-review do not establish owner comprehension, which remains unresolved while feedback is pending or negative.

For manual-release assessment, inspect the actual package and operator steps. Require initial SQL with database creation, required DDL/master data and ordered later changes; commands alone are incomplete. Check baseline/target identity, client stop-on-error, rerun safety, operator-data preservation, partial-failure recovery and startup compatibility checks without schema mutation. Verify fresh install, supported upgrade, interrupted execution and persistent files/keys/configuration as in scope. Keep source/local proof separate from actual SSMS, host, identity, recovery and live smoke evidence. Release compilation, publishing, packaging and database execution remain owner-controlled unless explicitly authorized; QA does not authorize creating missing release artifacts.

## Report and close the assessed scope

Lead with the assessment and highest-consequence finding. Give each actionable finding compact labeled facts for location/state, observation/reproducer, consequence and useful correction, adding prose where causality needs it. Distinguish defects, unresolved decisions and optional improvements. Use a short check/result/limit table when it helps compare coverage; retain candidate/environment identity and executed, passed, failed, blocked and untested coverage. Link commands and detailed reports rather than copying successful logs; compact reporting must preserve reproduction details.

For authorized fixes, rerun the original reproduction and affected regressions; preserve unaffected valid proof. Stop at the requested scope rather than expanding into a lifecycle or deployment. In projects adopting automatic context maintenance, update this workstream's verification checkpoint and invalidate only affected earlier evidence. Session self-assessment does not establish correctness or independent review.

Recommend analysis, implementation or release expertise only when a concrete remaining need warrants it. The agent decides whether another skill helps; this skill invokes none.
