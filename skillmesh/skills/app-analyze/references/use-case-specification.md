# Use-case specification

Adapted from the owner-supplied `requirements-to-usecase-spec` method: layered baseline, goal and event coverage, stable flow references, observable done-checks. A draft default or readiness label never becomes scope or approval.

## Choose the depth
| Depth | Use for | Include |
| --- | --- | --- |
| Sketch | Early idea or brief analysis | Outcome, scope, actors and goals, candidate use cases, main-path outlines with observable completion, top decisions; frames 1-3 |
| Standard (default) | The next implementation increment | Model deltas, shared rules, detailed use cases and alternatives, flow tracking, decision links; frames 1-5 |
| Full | Broad specification or release coverage | Standard plus the sparse coverage index, frames 6-9, release, source, change and test references |

Depth rules:
- State the depth and coverage limits.
- Keep every known requirement at any depth, including quality, access, environment and lifecycle obligations outside the swept frames.
- Sweep more frames when the increment's consequence warrants it.
- Detail only the selected increment. Claim no exhaustive coverage for deferred work.

## Reuse the product layer
- Reuse existing actors, entities and states, shared rules, terminology and IDs.
- None exist: establish only the supported shared baseline, in one authoritative section. Modules link to it and list deltas.
- Several modules reuse the rules, or a second decision-maker owns them: use a separate product-rules document. It owns decision tables and boundary examples for shared rules.
- One module: rules stay in the specification, never in a separate file.
- The supplied method suggests defaults (CRUD, archive, search, audit, role-based visibility, input-preserving errors, performance targets, no import/export, atomic save, outage handling). Treat them as prompts, not accepted behavior.
- Supported convention: keep it. Anything else: label it `Draft: confirm` and link its decision.
- An unknown or draft baseline never marks a coverage cell complete.

## Contents
Omit sections that do not apply. Use project names and existing structure.
1. **Header:** scope, version or revision, depth, sources, responsible role, links to brief and findings.
2. **Decisions and facts this spec depends on:** the opening table (see below).
3. **Model deltas:** new or changed actors, entities and states, external and time events with their responding use cases, rules. Include system actors and hostile actions when relevant.
4. **Use cases:** see below.
5. **Tracking:** one row per selected flow and applicable quality item.
6. **Sparse coverage:** Full depth or on request.

When a Must flow already at Specified or beyond changes:
- Record what changed, why, decision standing, and source, version and date in the project's change history.
- Link the checks to revalidate.

## Decisions and facts table
Open the specification with a table:
- Reference (D-n or F-n).
- One-line gloss.
- The default or assumed value the flows use.
- Status.

Then:
- Cite decisions and facts elsewhere by reference only.
- Never cite a reference missing from the table.
- Link the brief's register. Do not copy it.

## Use cases and acceptance
**Identifiers:**
- Reuse existing stable IDs.
- New module: use named references (`UC-03 Renew contract`, `UC-03.M Main`, `UC-03.A1 Already renewed`). Never a bare ID.
- Keep flow IDs stable. Do not address step numbers from elsewhere.
- Retire a referenced alternative instead of renumbering it.
- A contained ticket can keep its own identity.

```text
UC-03 Renew contract · Actor: Account manager · Priority: Must · Source: R-2
Goal: renew the contract while preserving the previous term
Precondition: an eligible contract exists and the actor may renew it
1. Account manager requests renewal for the contract.
2. System creates the renewal using the confirmed copy rules.
3. System retains the previous term and confirms the renewal reference.
Done when: the renewal follows the copy rules, the previous term is unchanged,
and the actor sees the renewal reference.
A1 When the contract already has a renewal: show that renewal without creating another.
```

This shows a format, not renewal requirements.

**Flow detail:**
- State starting conditions, observable state and side effects.
- Job and journey: when the findings record them, name the job or stage the flow serves in its goal line.
- Main flow: short, typically six steps or fewer. Split by distinct actor goal, not by step count. Keep necessary sequence and cause.
- Alternative: state it as condition → outcome, naming its point in words if needed. That pair is its done-check.
- Add only a missing input, fixture, oracle or proof method to a done-check.
- Do not repeat precise acceptance in a separate checklist.

**Full or outline:**
- Full, marked "on defaults": every decision and fact it depends on is settled or has a safe revisable default.
- Outline (goal, trigger, observable outcome, blocking decision): a High decision with no safe default, or a missing fact that changes its behavior, blocks it.
- An unconfirmed decision alone is not a reason to outline.

**Thresholds and conditions:**
- Numeric, amount or time threshold: give examples just below, at and just above it (23h59m, 24h00m, 24h01m before a start). The inclusive side is never inferred.
- Three or more interacting conditions (for example a fee depending on timing, exemption and prior outcome): use a decision table, one row per combination.

**Failure behavior.** Check once per relevant use case: invalid input, denied access, duplicates, concurrent change, timeout, dependency outage, partial completion.
- Deviation from a confirmed shared rule: specify it.
- Shared failure behavior: link it instead of repeating it.
- Unspecified consequential result: make it a linked gap or labeled proposal, never an implied success or failure.
- Use simple references, not include and extend hierarchies.

**Stories.** On request, render flows as user stories with Given/When/Then.
- The flow stays authoritative. The story links to it.

**Quality items:**
- Keep functional (UC), quality (NW), experience (NX), manageability (NM) and compliance (C) items distinguishable when prefixes help. Use existing terminology, not ITIL labels.
- State target, applicability and observable check.
- Quantitative property: numeric target. Accessibility and security: categorical criteria are allowed.
- Missing consequential target: a gap, never an invented number.
- Constraint: state the obligation and how it is checked. No artificial actor flow. Name the flow it constrains.

## Coverage frames
| Frame | Check |
| --- | --- |
| 1. Actors × goals | Relevant actors have goals; flag unsupported proposed actors or goals |
| 2. Goals → use cases | Goals connect to use cases and the outcome; flag unserved goals and unjustified use cases |
| 3. Events → responses | Relevant external and time events have a defined response |
| 4. Data | Required entity operations and state transitions have behavior, or a gap or N/A reason |
| 5. Rules | Each rule has an enforcing flow or a shared applicability reference |
| 6. Quality | Known quality needs have criteria; group unanswered quality questions |
| 7. Environment | Integrations, platforms, data sources and domain constraints are covered |
| 8. Lifecycle | Relevant install, configure, migrate, upgrade, backup, support and retire obligations are covered |
| 9. Operations feedback | Incidents, problems and requests with requirement consequences are addressed |

- Record actual misses in the swept frames. Do not create a gap for every imaginable entity, attribute or activity.
- A confirmed N/A needs a reason. Silence is not N/A.

## Sparse coverage index
Use at Full depth or on request.
- List every relevant entity with its exceptions to the confirmed baseline, or `all confirmed baseline`.
- Operations to consider: Create, Read, Edit, Archive, Search, Import/Export, Audit, Permissions. Adapt them to the domain.
- Symbols: `✓` confirmed baseline, `–` N/A with reason, a UC or rule reference, `?` gap.
- Unlisted cells inherit only an applicable confirmed baseline.
- Flows and rules own behavior. The index is only a map.
- Group an unanswered import/export question once.

## Tracking and readiness
Track `Flow | Priority | Status`:
- Use existing conventions where adequate.
- Add Release, Source, Change and Test reference columns only when useful. Full usually needs them.
- Link shared source and owner values once.
- Priority: Must, Should or Could when supported. Label proposed priorities. Must means release-blocking, assigned by the owner.

Status words:
- **Identified:** the flow exists, as an outline.
- **Drafted:** complete behavior and done-checks written on proposed defaults. Not Specified until those decisions are accepted or delegated.
- **Specified:** complete behavior and done-checks, no consequential unknowns, decisions accepted or delegated. A labeled assumption alone does not settle a consequential policy.
- **Built** and **Verified:** need candidate-bound implementation and executed evidence. Authoring cannot set them.

Readiness wording:
- The tracking table is the only readiness statement. Use its status words.
- Elsewhere describe content ("main flow and alternatives written"), never readiness ("ready", "specified in full").
- Handoff summaries link to the table.
- State any rule list, such as what voids an approval, once. Reference it elsewhere.

Gaps:
- Gaps and decisions live in the brief's register.
- Note the frame where a gap was found.
- Separate current blockers from future dependencies.
- Record N/A decisions with their standing.

Coverage labels (Full depth, optional), derived from evidence:
- Basic: main flow verified. Sufficient: every Must flow verified. All: all scoped flows verified.
- Label the scope and the unverified remainder.
- They are summaries, not permission to ship. Quality, compliance, migration, recovery and reserved acceptance still apply.

Before handoff:
- Check goal, event and transition coverage, referenced rules, stable IDs and links, done-checks and status honesty.
- State source identity and assumptions once.
- Name precisely which flows are ready or blocked, in the tracking table. Do not call planned acceptance executed verification.
