---
name: app-qa
description: Verify software behavior and review implementation against requirements using executed tests, real integration and browser evidence where relevant. Use for existing or newly changed software, including standalone QA and review-only requests; no lifecycle records are required.
---

# App QA

Establish the exact candidate, requested review scope, relevant requirements and environment. Include relevant uncommitted work. Accept existing tickets, specifications, contracts and tests; absence of SkillMesh records does not block useful QA. Mark ambiguous requirements as limitations and investigate observable defects.

Inspect the implementation and choose checks proportional to affected risk. Use [verification practice](references/verification.md) for consequential changes, failures or release-readiness assessment.

Run the applicable tests rather than predict results. Exercise important normal, boundary, invalid and recovery behavior. Test real API/consumer integration when required. For UI, use available browser tools and inspect representative screenshots, keyboard/focus and journeys with realistic data. Automated assertions do not replace visual inspection.

Review both requirement coverage and engineering correctness: access, data integrity, failure handling, performance and maintainability where affected. These are two lenses, not mandatory separate agents. For material visual changes compare the actual experience with its reviewed direction; for contained corrections use the established product.

Each finding needs a location/state, observation or reproducer, consequence, and useful correction. Fix defects only within authorized scope; review-only work reports them without editing implementation. After changes, rerun affected checks and relevant regressions. Preserve unaffected valid evidence.

Report what was executed, passed, failed, blocked or untested, tied to the candidate and environment. Missing required proof cannot become a pass merely because it is documented. Distinguish observed defects from assumptions and optional improvements. A combined release requires evidence across interacting increments.

Stop when the requested scope is assessed; do not expand into a full lifecycle or deployment. Recommend `app-analyze`, implementation expertise or `app-deliver` only when a concrete need warrants it. The agent decides whether to use another skill; this skill does not invoke one.
