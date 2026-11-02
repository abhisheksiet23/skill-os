# Solution design evaluation — 2026-10-17

Compared three synthetic offline design requests from `solution-design-tasks.md` in two separate subagent contexts. Baseline read `app-analyze`, `app-backend` and relevant references at HEAD `c8b7611aa6e7b7c8345765d5a11d6f117f083c57`; candidate read the new working-tree `app-solution-design` and its reference. Both had the same prompts and tool restrictions and inherited the parent model/settings. Cases within each variant shared a context. Performers did not inspect peer outputs or receive assessment criteria. The author assessed both outputs; this was not a blind independent assessment.

Actual responses are retained locally in ignored `.eval-runs/solution-design/baseline.md` and `candidate.md`. They are design outputs from executed evaluations, not application execution or live integration evidence.

| Case | Observed baseline | Observed candidate | Assessment |
| --- | --- | --- | --- |
| Carrier timeout | Local durable work, unknown-outcome state, authoritative/manual reconciliation; explicitly rejected exactly-once claims | Same safe approach; additionally called out SDK/proxy retries, local-only fencing and a decision-changing carrier check | Both credible; candidate made several boundary assumptions more explicit |
| Internal approvals | Proportional monolith, existing-tool alternative, SSO authorization distinction, concurrency and restore checks | Comparable design with explicit sole data writer, conditional tool choice and conditions for revisiting topology | Both credible; no demonstrated general quality advantage |
| Contained clamp fix | Focused implementation and regression checks without architecture phase | Same restraint, preserving integer and validation contracts | Both respected scope |

The new skill provides an explicit discoverable owner for technical design. This limited comparison supports its intended behavior; it does not prove that the prior library was incapable of solution design or that the candidate is generally superior. No application tests, carrier/SSO integrations, usability studies or production checks were executed. Provider tokens, correction counts, operating cost, latency savings and production reliability are unknown.

Static validation: library validator reported 19 skills and zero packaging errors; official skill-creator validator passed using the existing local PyYAML dependency directory. Static checks establish packaging only.
