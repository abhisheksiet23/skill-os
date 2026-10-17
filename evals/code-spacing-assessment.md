# Code spacing assessment — 2026-10-17

Owner readability is **unresolved, awaiting review of the new example**. The owner reported that regenerated code remained dense; previous structural improvements are not evidence of acceptance. This change adds explicit visual spacing to app/backend/frontend, website implementation and both prototype skills, with source-spacing checks in app QA and website review. Generated/minified dependencies are excluded. Cohesive statements stay grouped; no blanket gap-after-every-statement rule was introduced.

## Executed comparison

Two separate performers received the same spacing request and six frozen source files from the earlier isolated Medcross candidate. Baseline used HEAD `024649d` frontend/backend guidance; candidate used revised working-tree guidance. Neither performer saw peer outputs or assessment criteria. A third reviewer inspected both variants and a small website exercise. This is a single paired trial; the explicit user request itself asked for spacing in both variants, so differences cannot be attributed solely to the new skill wording.

Both produced actual code with more visible workflow groups. The candidate expands payload/retry handling, API error messages, backend guards and query/assignment/persistence blocks, directory assignment projection and shared dialog markup. Independent review found retained dense adjacent action handling and shared dialog text; these were sent back for expansion before owner presentation. The adjacent handler was already dense in the frozen input, so it was not a newly introduced regression. Untouched login, administration and other paths still contain density; the example is not a whole-application refactor or pass.

Actual outputs and commands remain locally under ignored `.eval-runs/spacing/`: baseline/candidate source folders, result files, independent assessment, verification harnesses, frozen-input hashes and `review.md` with complete method excerpts. The active Medcross application was not edited. Input hashes identify the earlier regenerated example rather than a live project revision.

## Checks and limitations

- Baseline: existing action-handler checks passed before/after; TypeScript source check reported zero diagnostics. Backend compilation and rendered template behavior were not verified in that variant.
- Candidate: strict TypeScript/Angular template development compilation and offline Debug backend compilation passed, with zero backend warnings/errors. Original/revised action mock checks passed for payload, retries, conflicts, refresh/version and recovery; seven API parity scenarios passed for CSRF/JSON/credentials/error/empty responses. These tests execute actual method/client code with doubles, not SQL-backed integration.
- Website exercise: an isolated formatted synthetic HTML/script copy passed markup-token and simulated initial/first/repeated-click comparison. Its fake delivery message and unsupported marketing guarantee remain deliberately unfixed and explicitly out of scope. It is not a publication-ready example. Indentation introduces whitespace text nodes; visual equivalence was not claimed or tested.
- Library packaging check: 19 skills and zero errors. Official validators passed all seven changed skills; whitespace checks passed. These establish packaging only.

No SQL Server, real authentication/CSRF session, concurrent database update, browser rendering or deployed behavior was exercised. No release build, publishing, SQL generation or deployment occurred. Source inspection supports retained backend rule/order behavior but does not prove it at runtime. Owner comprehension, preferred spacing and readability satisfaction remain unknown until the owner reviews the actual code. A negative response means the spacing standard still needs adjustment, not that tests overrule it.
