# Repeatable verification

Invest when expected reuse, failure impact and debugging value justify creation and maintenance. Existing suites come first. Prefer unit/API tests for rules and permutations; keep browser coverage focused on important integrated journeys and experience risks. A typo does not justify a new automation platform.

Persist checks in the application repository, using its runner and conventions. For browser journeys without a runner, a standard Playwright Test setup is a reasonable option when compatible with the project. Reuse useful existing journey functions. Do not mandate a framework, MCP server, browser matrix or CI migration merely because this skill is invoked.

Make tests independently runnable: documented prerequisites and one command, controlled fixtures, fresh browser contexts, readiness assertions instead of fixed sleeps, and cleanup even after failure. Keep authentication state and secrets out of committed files and reports. Missing credentials, unavailable services or missing required fixtures are blocked coverage, not a passing suite. Separate mock contracts from real integration and identify which environment was tested.

Return concise machine-readable results and a human summary with candidate identity (including uncommitted changes), environment, command, executed/passed/failed/blocked counts and duration. Use standard runner reports first. Retain diagnostic artifacts for failures where safe; authentication traces and network payloads may contain secrets. Report retries/flakiness explicitly rather than hiding failures behind eventual success. Fetch detailed logs or traces only for relevant failures.

Run a new harness twice to expose state leakage and verify repeatability; a clean rerun is not permission to discard the first failure. For a regression fix, demonstrate the relevant assertion detects the original failure where feasible. Reuse unchanged proof, rerun checks affected by a change, and include combined acceptance before release. A working command is not evidence until actually executed.

MCP can expose the same runner/results if a demonstrated tool-access or coordination gap justifies it. A CLI plus structured report often suffices. Keep project facts, fixtures and tests in the project rather than reusable skill instructions. Do not build a shared orchestration/state service to avoid reading a report.

Preserve visual and exploratory review for design judgment, unfamiliar behavior and gaps in assertions. Automated semantics/reflow checks do not establish real screen-reader or browser-zoom behavior. Measure initial setup plus repeat execution, maintenance, user corrections and escaped defects; fewer tokens with more downstream rework is a regression.
