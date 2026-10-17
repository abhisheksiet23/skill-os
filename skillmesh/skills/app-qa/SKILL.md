---
name: app-qa
description: Verify software behavior and review implementation against requirements using executed tests, real integration and browser evidence where relevant. Use for existing or newly changed software, including standalone QA and review-only requests; no lifecycle records are required.
---

# App QA

Establish the exact candidate, requested review scope, relevant requirements and environment. Include relevant uncommitted work. Accept existing tickets, specifications, contracts and tests; absence of SkillMesh records does not block useful QA. Mark ambiguous requirements as limitations and investigate observable defects.

Inspect the implementation and choose checks proportional to affected risk. Use [verification practice](references/verification.md) for consequential changes, failures or release-readiness assessment.

When important journeys will be repeated, turn useful checks into project-owned executable tests with a documented command and reliable setup. Reuse the existing runner and fixtures. Prefer durable assertions over repeatedly directing the same browser steps, without imposing a new harness on a trivial correction. See [repeatable verification](references/repeatable-verification.md) when establishing or improving recurring checks.

Run the applicable tests rather than predict results. Exercise important normal, boundary, invalid and recovery behavior. Test real API/consumer integration when required. For UI, use available browser tools and inspect representative screenshots, keyboard/focus and journeys with realistic data. Automated assertions do not replace visual inspection.

Review both requirement coverage and engineering correctness: access, data integrity, failure handling, performance and maintainability where affected. These are two lenses, not mandatory separate agents. For material visual changes compare the actual experience with its reviewed direction; for contained corrections use the established product.

Review readability explicitly for a developer returning to code after six years. Trace a representative changed workflow from user/API entry through rules, state changes, persistence and recovery. Check that names express business intent, contracts and structured values are discoverable, and responsibility boundaries let the reader follow the action without decoding dense expressions, hidden conventions or unrelated state. Inspect templates as well as source logic. Identify concrete obstacles with locations and useful corrections; a formatter, build or test pass does not establish comprehension. Preserve security, concurrency, transaction and retry guarantees while recommending simplification. Report this source assessment separately from behavioral correctness and actual owner feedback; do not infer human readability from an agent's self-review. Scope findings to affected work rather than imposing a whole-project rewrite or arbitrary size limits.

Lead with the assessment outcome and the highest-consequence issue. Order independent findings by severity or decision impact; each needs a location/state, observation or reproducer, consequence, and useful correction. Keep supporting commands compact and separate executed proof from unavailable checks. Fix defects only within authorized scope; review-only work reports them without editing implementation. After changes, rerun affected checks and relevant regressions. Preserve unaffected valid evidence.

Report what was executed, passed, failed, blocked or untested, tied to the candidate and environment. Missing required proof cannot become a pass merely because it is documented. Distinguish observed defects from assumptions and optional improvements. A combined release requires evidence across interacting increments.

Stop when the requested scope is assessed; do not expand into a full lifecycle or deployment. Recommend `app-analyze`, implementation expertise or `app-deliver` only when a concrete need warrants it. The agent decides whether to use another skill; this skill does not invoke one.
