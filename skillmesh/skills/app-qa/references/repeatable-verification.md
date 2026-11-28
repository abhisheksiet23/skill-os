# Make valuable checks repeatable

Invest when reuse, failure impact and debugging value justify setup and maintenance. Start with existing suites. Put rule permutations in unit/API tests and reserve browser automation for important integrated journeys and experience risks. A typo does not warrant a new platform.

## Establish a trustworthy runner

When persistent test changes are authorized, keep tests in the application's repository with its runner and conventions. Otherwise run existing checks and use authorized disposable probes without installing or changing a project harness. Without an existing browser runner, compatible Playwright Test is a reasonable option, not a requirement. Reuse useful journey functions and avoid imposing a browser matrix, MCP server or CI migration merely because QA was requested.

Provide prerequisites and one runnable command. Use controlled fixtures, fresh browser contexts, readiness assertions instead of fixed sleeps and cleanup after failure. Missing credentials, services or required fixtures block coverage; they must not produce a passing suite. Identify the environment and distinguish mocked contracts from real integration. Keep authentication state and secrets out of committed files/reports.

Run a new harness twice to expose leaked state; preserve and explain the first failure even if a retry passes. For a regression fix, demonstrate the assertion catches the original failure where feasible. A working-looking command is not execution evidence.

## Return useful evidence without drowning the reader

Aim to reduce total effort across runs. Link an existing runnable check and capture only missing setup, fixtures or failure steps that would be costly to rediscover. For evidence you expect to reuse, record the candidate, relevant environment and what would invalidate the result. Use existing tests or handoff records. In review-only work, include any necessary reproduction steps in the findings. Do not retain private data or credentials to save setup time.

On a repeat request, start from that record. For an unchanged candidate and environment, reuse collected evidence where acceptable, or rerun the saved check directly when fresh execution is requested or needed. After a change, identify affected guarantees and consumers, reuse the rest, and keep any required integrated or release checks. If the impact is unclear, widen coverage until the uncertainty is resolved. Compare equivalent runs using observed setup, execution and review effort, including maintenance and rework. A cheaper run is a goal, not a reason to skip necessary checks or claim unmeasured savings.

Prefer standard runner reports: concise structured results plus a human summary with candidate identity including uncommitted changes, environment, command, executed/passed/failed/blocked counts and duration. Report retries/flakiness explicitly. Retain safe failure artifacts, remembering that auth traces and network payloads can expose secrets; inspect detailed logs only for relevant failures.

Reuse valid unchanged proof, rerun affected checks after changes and assess combined acceptance before release. Preserve visual/exploratory review for design judgment, unfamiliar behavior and assertion gaps. Automated semantics/reflow checks do not prove actual screen-reader or browser-zoom behavior.

A CLI and structured report usually suffice. Expose the same runner through MCP only for a demonstrated access/coordination gap; do not create shared orchestration/state services merely to avoid reading reports. Project fixtures, facts and tests belong in the project, not reusable instructions.

Judge the investment by setup, repeated execution, maintenance, owner corrections and escaped defects. Token/time/cost savings are unknown unless measured; lower token use with greater downstream rework is not improvement.
