# Microcopy guidance change assessment

## Scope and source

Selectively adapted concepts from the user-supplied ux-writing-skill.zip: state-specific patterns, concrete voice examples, contextual tone, four editing lenses and contextual accessibility/localization checks. Wording is newly authored for the existing skills. No new skill, dependency, workflow gate or tool setup was added. Unsupported comprehension statistics, fixed length/voice quotas, editorial scores and unverified operational promises were excluded.

## Representative before/after instruction comparison

This is a static comparison of instructions, not generated baseline/candidate behavior or a live behavioral pass.

| Case | Before | Candidate |
| --- | --- | --- |
| Unknown payment result | General errors and recovery guidance | Explicit uncertainty preservation and status checking before another payment |
| Password simplification | General real-word and clarity guidance | Explicit preservation of every validation requirement while shortening |
| Filtered empty state | Representative empty states requested | Distinguishes no matches, first use, completion and restricted access; respects available actions |
| Account deletion | Confirmations proportional to consequence | Preserves scope, retention exceptions and recovery windows |
| Outage reassurance | General evidence discipline | Names unsupported cause, data-safety and recovery-time promises as copy risks |
| Localization and accessible labels | Long content and general accessibility checks | Contextual names/labels, associations, announcements and locale variants without automatic ARIA or expansion quotas |

## Evidence limits

The repeatable before/after task set is in ../microcopy-tasks.md. Independent baseline/candidate behavioral runs have not been executed. Behavioral improvement, user comprehension, task-success effect and token overhead are unknown. Metadata and local-reference checks establish packaging only. No installed copies were changed.

Validation executed: scripts/validate_library.py passed across 18 skills with zero packaging errors using the bundled Python runtime. The skill-creator quick_validate.py checks were attempted for all four affected skills but could not run because that runtime lacks PyYAML. The default Python executable was inaccessible. This workspace has no Git repository metadata, so Git diff/status evidence is unavailable.
