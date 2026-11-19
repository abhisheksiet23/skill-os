# ER-1 executable specimen

Synthetic Python 3.12+ standard-library service for the [ER-1 v1.0 brief](../brief.md), currently applying its **ER-LIMIT** branch: new projector confirmations allow three inclusive calendar days; four days are rejected. The canonical base brief retains its original two-day rule. This is a maintained evaluation fixture, not a production backend or reusable SkillMesh runtime. Its continuing consumers are the common-case experiments and their regression checks. Temporary baseline/mutation copies belong under the ignored `.eval-runs/` area.

## Selected slice and local contract

Recorder, camera and projector confirmations share one authoritative service path. The public boundary uses named immutable request/result values and employee-scoped reads. Existing authentication is represented by a trusted host-supplied employee ID; no credential/token validation is implemented. Unknown employee IDs fail with `AccessDenied`. The public confirmation body cannot select an employee.

This experiment settles the fixture's interface details as follows, without changing product policy: identifiers must be nonblank strings, remain exact and are never trimmed; unknown assets and malformed requests/dates raise `InvalidRequest`; dates must be Python calendar `date` values, excluding `datetime`; overlap and changed operation payload raise `ReservationConflict`. Rejections do not mutate reservation/operation state or consume a reference. Exceptions carry no other employee's confirmation details. Training changes are a trusted fixture control, not an administrative API.

Office today is injected as a local calendar date (the fixture uses Asia/Kolkata); the service does no timestamp conversion. Replay returns the accepted result before current date/training checks. Both reservation and operation records are prepared and published under one shared-instance lock, which also covers catalogue reads and training updates. No other writer exists in this specimen. Results are immutable to prevent callers modifying authoritative state.

The service is intentionally in memory. Threaded checks exercise one service instance only. T-10 adds a loopback HTTP adapter and one rendered ER-DRAFT example; it does not establish production HTTP/authentication, process-restart durability, multi-process/storage coordination, deployment or live provider behavior. The canonical brief keeps its original unresolved draft choice; this specimen explicitly selects ER-DRAFT for its rendered path.

## T-08 extraction decision

Keep `ReservationPolicy` as the bounded domain pattern: each asset type supplies its duration limit and whether camera training is required. The recorder, camera and projector paths execute this policy through `Reservations.confirm`; no per-type subclasses, generic rule engine or plugin extension mechanism is needed. Date shape/order, actor scope, overlap and operation replay remain at their authoritative service boundary instead of being pushed into the policy.

The starting implementation had three explicit rule branches. The same contract tests run against that frozen baseline and the extracted candidate. This establishes preserved behavior within this synthetic specimen, not that the extracted version is faster, cheaper, easier for its owner to read or appropriate to every domain. A future rule that does not fit these two meaningful variation points is a reason to reconsider composition, not add opaque flags or a generic framework.

## Run

From the repository root with Python 3.12+ (prefix commands with `rtk proxy` when required by host instructions):

```powershell
python -B -m unittest discover -s evals/fixtures/equipment-reservations/specimen -v
```

The same test file accepts an absolute implementation path through `ER1_IMPLEMENTATION` for a frozen baseline/candidate comparison. Keep environment overrides out of subsequent unrelated runs. The initial comparison's exact identities and results belong in the toolkit checkpoint; this file does not import historical passes as current evidence.

For frozen domain variants, run `test_reservations.py` directly with that override. The separate HTTP tests always exercise the maintained server and its current service; do not report them as proof of a different frozen implementation.

## T-09 recurring rule-change verification

The existing unittest runner is sufficient; no wrapper or new platform is needed. Its maintained contract suite now checks three-day projector acceptance, four-day rejection, unchanged recorder/camera limits and training requirements, and accepted-result replay. It also creates a two-day projector confirmation under the legacy policy, restores the current policy, and verifies the same confirmation survives and replays without another effect before accepting a new three-day booking.

The legacy-policy context is a controlled in-process simulation using the same service state. It does not establish database upgrade, service restart or durable recovery. The original T-08 sources/tests were frozen before editing; they remain comparison inputs, not the acceptance oracle for this changed rule. [Current executed evidence](../../../../docs/toolkit-session-assessments.md#t-09-er-limit-repeatable-verification) separates the old-contract pass, expected failure under new acceptance and final candidate passes.

## T-10 rendered conflict example

**Decision:** retain one working form/recovery example, not a state gallery. No existing UI or rendered example was present. ER-DRAFT's conflict-retention behavior needed an inspectable consumer: the form keeps selected asset and typed dates, names the conflict without exposing another employee's booking, and offers focus-based recovery with explicit reconfirmation. This is a bounded synthetic build decision, not measured proof of avoided downstream errors.

The example uses the maintained service through real loopback HTTP. Its UI combines ER-DRAFT with the already selected ER-LIMIT branch; new projector bookings allow three days. Rule hints come from the actual server policy. Semantic native select/date/button controls fit this small form without a component package or framework. A light neutral surface, forest-green primary action and amber conflict message distinguish draft, rejected and confirmed states. The synthetic/in-memory label and fixed office date stay visible.

From the repository root, run:

```powershell
python -B evals/fixtures/equipment-reservations/specimen/example_server.py
```

Open the printed `ER1_URL`. The server binds only `127.0.0.1` on a free port, uses fixed trusted employee EMP-01 and resets on restart. Initial recorder dates Nov 20–21 conflict with the seeded booking after you explicitly press Confirm reservation. Choose another asset or edit dates; neither action submits. On a lost response, fields remain locked to the uncertain request and Check confirmation explicitly reuses its operation ID. Nothing retries automatically. This is not a production server or authentication flow.

The existing Python command now includes six real HTTP adapter tests alongside the 26 domain tests. Browser checks use an already available Playwright package and Chromium; they do not install either:

```powershell
# ER1_PYTHON can select a non-default Python executable.
# ER1_PLAYWRIGHT_MODULE can select an existing Playwright-compatible module path.
node evals/fixtures/equipment-reservations/specimen/test_example_ui.cjs
```

With no module override, the browser runner resolves `playwright` normally. Missing browser prerequisites or restricted loopback access are failures, not skipped passes. Each scenario starts a fresh local server and browser context, cleans them up, and checks for browser runtime errors. Screenshots go to the ignored `.eval-runs/er1-t10/` area, overridable with `ER1_ARTIFACT_DIR`.

Nine browser scenarios cover three viewport widths (1280, 768, 360), non-default typed-date retention, explicit alternative confirmation, keyboard edit recovery, duplicate-submit suppression, accepted-then-lost response recovery and server-side duration rejection. Keyboard/focus, semantics, reflow and inspected screenshots do not establish assistive-technology usability or owner comprehension. [T-10 evidence](../../../../docs/toolkit-session-assessments.md#t-10-rendered-conflict-example) records observations, setup correction and proof limits.

**Upkeep:** keep one page, stylesheet, client module and narrow loopback adapter with tests. Recheck changed UI states after rule/API changes; the shared policy/catalogue prevents a separate hardcoded limit list. Setup/maintenance effort and benefit economics are unmeasured. A real application should reuse/adapt the verified behavior in its own directory and prove its own authentication, persistence and rendering.
