# Compile analysis into a use-case specification

Adapted from the owner-supplied `Requirements to usecase spec-v3.zip`, skill `requirements-to-usecase-spec`. Preserve its layered baseline, goal/event coverage, stable flow references and observable done-checks. The changes below keep draft defaults and readiness labels from becoming unsupported scope or approval.

## Choose depth and reuse the product layer

| Depth | Useful boundary | Include |
| --- | --- | --- |
| Sketch | Early idea or brief analysis | Outcome, scope, actors/goals, candidate use cases, main-path outlines with observable completion, top gaps; sweep frames 1–3 |
| Standard | Default for the next implementation increment | Product/model deltas, shared rules, sparse coverage, detailed use cases and consequential alternatives, flow tracking, gaps/decisions; sweep frames 1–5 |
| Full | Broad specification or requested release coverage | Standard plus frames 6–9 and useful release/source/change/test references |

State depth and coverage limits. Preserve all known requirements at any depth, including quality, access, environment and lifecycle obligations outside the swept frames. Sweep additional frames whenever the increment's consequence warrants it. Only the selected increment needs implementable detail; do not claim exhaustive coverage for deferred work.

Reuse the product layer: actors, entities/states, shared behavior/rules, terminology and existing IDs. If none exists, establish only the supported shared baseline in an authoritative product section/file; the module links it and lists deltas. A separate product file is useful when several modules reuse it, not mandatory for one small correction.

The supplied method suggests CRUD/archive/search/audit, role-based visibility, input-preserving errors, performance/browser targets, no import/export, and atomic-save/concurrency/outage defaults. These are elicitation prompts, **not accepted product behavior**. Retain supported conventions; otherwise mark a proposed baseline `Draft: confirm` and link consequential gaps. Do not grant every entity CRUD, hide every denied action, forbid hard deletion, infer import/export exclusions or promise retry/atomicity without evidence. An unknown or draft baseline cannot mark a coverage cell complete.

## Specification contents

Use project names and adequate existing structure. For a module, present the following in readable order; omit irrelevant sections rather than manufacturing content:

1. **Header:** module/scope, version/date or source revision, depth, sources, responsible role if known, outcome and success measure. Unknown measures stay `?`; proposed outcomes are tagged. Link the analysis and authoritative decisions/gaps.
2. **Model deltas:** new/changed actors, entities/states, external/time events and responding use cases, and rules. Include system actors or hostile actions when relevant. Use a decision table when interacting conditions make prose ambiguous.
3. **Sparse coverage:** every relevant entity appears, listing exceptions to the confirmed baseline or `all confirmed baseline`. Useful operations are Create, Read, Edit, Archive, Search, Import/Export, Audit and Permissions; adapt these to the domain rather than implying all are needed. Symbols: `✓` confirmed baseline, `–` confirmed N/A with reason, named UC reference for custom behavior, named rule reference, `?` gap. Unlisted cells inherit only an applicable confirmed baseline; otherwise they are unknown. Group a shared unanswered import/export question once when relevant.
4. **Use cases:** goal-oriented behavior, main and alternative flows, shared rule references, and observable done-checks.
5. **Tracking:** one row per selected flow and applicable quality/constraint item, with priority and evidenced status. Link shared source/owner values once instead of repeating constant columns.
6. **Gaps/decisions:** embed their authoritative register here or link existing entries; do not copy the analysis register. When updating a Must flow already at Specified or beyond, record what changed, why, approval/decision standing and source/version/date in the project's change history, linking affected checks for revalidation. Reuse existing change references rather than creating competing logs.

The sparse matrix is a coverage index; flows/rules own the behavior. Render a grid only when useful/requested; do not maintain competing copies. Spreadsheet output can use separate tracking and coverage tabs.

## Use cases and acceptance

Reuse existing stable identifiers. For new module specifications use named references such as `UC-03 Renew contract`, `UC-03.M Main` and `UC-03.A1 Already renewed`; never a bare ID. Keep flow IDs stable, do not address step numbers from elsewhere, and retire rather than renumber referenced alternatives. A contained ticket can retain its existing identity rather than creating a new ID scheme.

```text
UC-03 Renew contract · Actor: Account manager · Priority: Must
Goal: renew the contract while preserving the previous term
Precondition: an eligible contract exists and the actor may renew it
1. Account manager requests renewal for the contract.
2. System creates the renewal using the confirmed copy rules.
3. System retains the previous term and confirms the renewal reference.
Done when: the renewal follows the copy rules, the previous term is unchanged,
and the actor sees the renewal reference.
A1 When the contract already has a renewal: show that renewal without creating another.
```

This illustrates a format, not a source of renewal requirements. Include starting conditions and observable state/side effects. Aim for a short main flow, typically six steps or fewer; split by distinct actor goals, not an arbitrary step quota. Keep necessary sequence and causal detail. State each alternative as condition → outcome, naming its point in words when necessary. Its condition/outcome is its done-check; add only a missing discriminating input, fixture, oracle or proof method. Do not repeat precise acceptance in a separate checklist.

Check invalid input, denied access, duplicates, concurrent changes, timeout, dependency outage and partial completion once per relevant use case. Explicitly specify deviations from confirmed shared rules; link applicable shared failure behavior instead of repeating it. A consequential unspecified result becomes a linked gap or labeled proposal, never an implicit success/failure promise. Simple references replace include/extend hierarchies.

Keep functional utility (UC), quality/warranty (NW), experience (NX), manageability (NM) and compliance constraints (C) distinguishable when these prefixes help. Quality items state the target, applicability and observable check/method; numeric targets are required where the property is quantitative, while accessibility or security rules may need categorical criteria. Missing consequential targets become gaps, not invented numbers. A constraint states the obligation and how it will be checked, without an artificial actor flow. Use existing product terminology instead of imposing ITIL labels.

## Coverage frames

| Frame | Check |
| --- | --- |
| 1. Actors × goals | Relevant actors have goals; identify unsupported proposed actors/goals |
| 2. Goals → use cases | Goals connect to use cases and the outcome; flag unserved goals and unjustified use cases |
| 3. Events → responses | Relevant external/time events have a defined response |
| 4. Data | Required entity operations and state transitions have behavior or an explicit gap/N/A reason |
| 5. Rules | Each rule has an enforcing flow or a clear shared applicability reference |
| 6. Quality | Known quality needs have criteria; group relevant unanswered quality questions instead of inventing per-attribute requirements |
| 7. Environment | Integrations, platforms, data sources and domain constraints are covered |
| 8. Lifecycle | Relevant install/configure/migrate/upgrade/backup/support/retire obligations are covered |
| 9. Operations feedback | Incidents, problems and service requests with requirement consequences are addressed |

Record actual misses in the swept frames. Do not create a gap for every imaginable entity, quality attribute or lifecycle activity. A confirmed N/A needs a reason; silence does not mean N/A.

## Gaps, tracking and readiness

Gap entries need a stable reference/name, severity, coverage frame when relevant, question/evidence conflict, affected flow/work, owner if known and a supported proposal or `needs input`. H blocks a Must flow; M changes a rule, test or scope; L is a detail. Distinguish current blockers from future dependencies. Confirmed proposals move into their authoritative rule/flow; close and link the gap without erasing its decision rationale. Record decision standing as proposed or confirmed, including N/A decisions.

Track `Flow | Priority | Status` using existing conventions where adequate. Add Release, Source, Change and external Test ref only when useful; Full normally needs these trace links. Priority is Must/Should/Could when supported; label proposed priorities. Status distinguishes Identified, Specified, Built and Verified. Specified requires complete behavior and done-checks, no consequential unknowns, and accepted or explicitly delegated decisions; a labeled assumption alone does not settle a consequential policy. Built/Verified require candidate-bound implementation/executed evidence; authoring a spec cannot advance them.

If useful, derive the supplied method's coverage labels from evidence: Basic = main flow verified, Sufficient = every Must flow verified, All = all scoped flows verified. Label the scope and unverified remainder. These are coverage summaries, never permission to ship; required quality, compliance, migration, recovery and reserved acceptance still apply.

Before handoff check goal/event/transition coverage, referenced rules, stable IDs/links, done-checks and gap/status honesty. Preserve source identity and assumptions once with links. Summarize actual open gaps by frame/severity when useful, consequential proposals needing decisions, assumptions and evidence limits. Link the two artifacts and name precisely which flows are ready or blocked; do not call planned acceptance executed verification.
