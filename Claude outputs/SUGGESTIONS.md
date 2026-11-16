# Running suggestions (skill-os) — notes only, nothing applied
1. app-qa: skill improved report rigor (evidence, ambiguity, untested areas) not detection on small case (case 1).
2. Candidate: add to app-qa a one-line reminder to state counts/commands for every probe set (baseline omitted).
3. Candidate: note that a passing probe on a failing-condition path ("R4") should not be reported as partial/failing; baseline mislabeled.
4. business-validate: thresholds should come from the decision; performer supplied an unexplained "2 of 10". Consider an explicit prompt: "state why this number would change the decision".
5. Packaging: build_claude_plugin.py done; consider a unit test for it.
6. Eval hygiene: keep run results out of repo (.eval-runs ignored) and strip skill-identifying paths before blinding.
7. Case 3 (6 defects, 2 runs per side, blinded): no detection difference; skill vs no-skill within noise. Skill runs cost ~8 tool calls vs ~4 and ~40s vs ~30s, tokens ~+8%.
8. Possible app-qa addition (hypothesis, untested): when a check is a boundary/arith bug, characterize the full failure range ("never refunds") rather than the sample points tried; 3 of 4 reports under-stated the .seconds bug.
9. Possible app-qa addition: require that probe counts reconcile (pass+fail = total) — one skill run and one baseline run had arithmetic slips.
10. Do not add padding: speculative "fragile but harmless" findings (skill run) cost a point; consider a line in app-qa: report only defects with a demonstrated or specified failure.
11. Eval design: spec-planted defects saturate; next case should have a defect NOT enumerated by any spec line (e.g., engineering/maintainability or an implied requirement) to test the skill's extra guidance.
