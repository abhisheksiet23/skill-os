# Check that a design survives outside its authoring conversation

Use this for consequential technical designs, implementation plans or a requested standalone review. Choose the checks that can affect readiness; do not require a document template, full-codebase review or another agent for a contained change. Accept adequate project records from any author. Review-only requests produce findings and a readiness assessment; they do not authorize design edits or production implementation.

## Understand the artifact before filling its gaps

From the target and its linked baseline evidence, briefly restate the current system, proposed behavior and important constraints or guarantees. An explanation that sounds plausible but differs from the accepted intent is a finding. Look for missing relationships and side effects, not only undefined terms. Known requirements elsewhere in project records may reveal an omission, but do not silently supply it from memory and call the artifact ready. Put consequential clarification in the authoritative record or a useful link when edits are authorized. Ordinary engineering vocabulary needs no glossary.

Keep this comprehension check distinct from verifying implementation claims. A clear document can still describe a nonexistent component or promise a guarantee the current code does not provide.

## Ground consequential claims

Verify the existing paths, symbols, interfaces, stored identifiers and behavior on which the plan depends, using current source or appropriate runtime evidence. Follow relevant links and call paths only as far as they can change the assessment. Separate verified existing capabilities, proposed additions and unverified assumptions. A stale symbol alone may need a corrected reference; missing enforcement of the promised guarantee is a design gap. Source inspection does not establish deployed behavior.

For each important guarantee, identify the responsible boundary and an observable acceptance check, including consequential failure or compatibility behavior. Distinguish checks to run from executed proof. Resolve expensive-to-reverse or cross-component decisions before dependent implementation, while leaving routine helper names and local code structure to the implementer. Do not require a complete file list or zero remaining implementation choices.

## Reassess the revised solution

After material fixes, check that the design still addresses the original problem and accepted scope. Ask what observed requirement justifies each added queue, cache, service, abstraction or operational dependency, whether existing capabilities suffice, and whether the fix creates new contradictions or weakens a guarantee. Complexity can be justified by concrete constraints; do not remove required authorization, data integrity or recovery mechanisms merely to shorten a design.

Consolidate findings by consequence with the affected location, evidence, impact and useful correction. Distinguish defects, unresolved decisions and optional improvements. Respect accepted trade-offs unless evidence or scope changes. Recheck affected fixes when warranted; avoid repeated full reviews to chase a zero-finding round or reopen settled preferences.

## Optional independent reading

When authoring-context bias or a consequential handoff warrants it and delegation is available and authorized, the agent may ask a fresh reviewer to read the artifact and selected evidence. Pass absolute paths, the review scope and relevant project constraints without the authoring transcript, desired answers or a list of suspected defects. Use the native tool's no-history option rather than assuming a new agent is isolated. Fresh conversation context still shares the filesystem and project instructions; do not retrieve memory or earlier chat to fill document gaps.

Keep the reviewer read-only and let the authoring agent reconcile findings with accepted decisions. Wait for its actual report; a timeout, missing required evidence or an inaccessible file means incomplete review, not zero findings. Do not claim independence if no fresh context was established. Continue useful direct review when delegation is unavailable, stating the limitation only where relevant. No extra reviewer, fixed number of rounds or ceremony is required by this method.
