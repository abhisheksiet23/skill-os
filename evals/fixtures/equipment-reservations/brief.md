# Shared equipment reservations

Fixture ER-1, version 1.0, 2026-11-18. **Entirely synthetic.** Adapted from case A in `evals/requirements-density-tasks.md`; no customer, deployment or measured benefit is represented. This file is the canonical product input for the continuing experiment case. An experiment supplies its requested task, selected slice, candidate and execution boundary separately. This brief does not itself request implementation or prescribe a stack.

## Goal and scope

An employee reserves one physical asset for inclusive office-calendar dates and views their own confirmed reservations. The facilities team wants to avoid conflicting bookings without losing a confirmation when its response is lost.

The initial increment includes reservation creation and viewing one's own reservations. Collection, returns, cancellation, charging, account administration, administrator visibility, notifications and vendor integrations are excluded. Existing identity and a stable confirmation-operation identifier are available; do not invent an identity system. No database, framework, component library or release mechanism is selected.

## Confirmed scenario facts

- The employee chooses one physical asset and inclusive start/end dates. The start cannot be before office today; the end cannot precede the start. Duration counts both endpoints, includes weekends and has no weekend exemption.
- Recorder reservations last at most seven calendar days, camera reservations three, and projector reservations two. These limits were confirmed by the fictional scenario owner in the source case.
- Only employees with current camera training may reserve cameras. Check training at confirmation, even if it was current when the catalogue was displayed.
- A physical asset can have at most one confirmed reservation for any overlapping date interval. Two concurrent conflicting confirmations can produce at most one new confirmed reservation. A rejected confirmation leaves existing reservations and availability unchanged.
- Success shows the asset, inclusive dates and confirmation reference. Employees can view only their own reservations. Existing identity/access scope applies to reads and confirmation results.
- Repeating the same confirmation operation after a lost response returns its existing confirmation without another reservation.
- Whether an availability conflict preserves the entered dates is unresolved in the original case. Retaining the draft and offering another asset is an analyst proposal, not accepted behavior. Do not silently settle this choice or block unrelated settled work on it.

## Explicit synthetic additions for reproducible experiments

These additions define the new fixture, not facts recovered from an application or decisions made by a real facilities owner.

- Office time zone is `Asia/Kolkata`. Tests supply office today explicitly; the wall clock must not change the expected result. Use local calendar dates, not elapsed 24-hour intervals, for reservation duration.
- A confirmation-operation identity is scoped to its authenticated employee and exact identifier. An identical replay returns that employee's existing confirmation. Reusing it with a different asset or dates is a conflict with no mutation. A replay cannot expose another employee's confirmation. A successful replay returns the existing result even if training or office today has changed; it does not create or revalidate a new booking.
- Asset IDs and employee IDs are stable exact identifiers. Display labels are not identities. Behavior for blank/malformed identifiers and dates must be made explicit before implementing the affected interface; no exception type, HTTP status or storage strategy is implied here.
- User-entered dates, confirmed reservation state and confirmation-operation state are distinct concepts. An experiment may establish their implementation using its own explicit design contract.

## Deterministic starting data

Scenario office today is **2026-11-18**. All rows are invented fixture inputs, not test results.

| Kind | ID | Data |
| --- | --- | --- |
| Employee | `EMP-01` | Maya; current camera training at initial catalogue display |
| Employee | `EMP-02` | Dev; no current camera training |
| Asset | `REC-01` | Recorder; seven-day limit |
| Asset | `CAM-01` | Camera; three-day limit |
| Asset | `PROJ-01` | Projector; two-day limit |
| Existing reservation | `CONF-SEED-01` | EMP-02; REC-01; 2026-11-20 through 2026-11-21 inclusive |

All other asset/date combinations start without confirmed reservations. Reset each independent experiment to these inputs unless its prompt explicitly supplies a different starting snapshot. Identifiers for newly created confirmations need not have a prescribed textual format; they must identify the same logical confirmation on replay.

## Product journey

1. Employee reviews available assets and chooses one asset and dates.
2. Employee confirms; the system evaluates date, duration, training, access and overlap rules against current authoritative state.
3. A successful confirmation is recorded once and its reference is shown. Rejected confirmations preserve authoritative reservation state.
4. Employee views their own confirmations. A lost success response can be recovered using the same operation identity.

This describes the product behavior, not a mandatory screen sequence. Loading, errors, keyboard/focus, responsive layout and actual transport/persistence behavior need task-specific contracts and proof when exercised.

## Optional controlled changes

Supply only a selected change to a performer, at the intended point in an experiment. Each change is a separate synthetic branch from ER-1 v1.0 unless the prompt explicitly combines them; none silently rewrites the baseline.

- **ER-DRAFT:** fictional owner clarification: after an availability conflict, keep entered dates and asset selection; explain the conflict and let the employee choose another asset or edit dates. Do not automatically submit another confirmation. Other rejection behavior is unchanged.
- **ER-LIMIT:** fictional owner changes the projector limit from two to three inclusive calendar days, effective for new confirmations. Existing confirmations and their replays remain unchanged. No other asset limit changes.
- **ER-RECOVERY:** the confirmation commits, its response is lost, and the client retries using the same operation identity. For a persistence experiment, restart the service between commit and retry. If no persistent executable service exists, report that boundary untested.
- **ER-RACE:** two employees with valid eligibility confirm overlapping dates for the same physical asset concurrently. Inject a controlled race only when the implementation/test environment supports it; sequential calls do not establish concurrent safety.

For needs beyond these facts, provide an explicit task-specific supplement. Missing vendor, business-demand, pricing, integration or deployment evidence stays missing.
