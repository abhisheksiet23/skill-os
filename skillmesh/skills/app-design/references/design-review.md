# Assess design comprehension, grounding and readiness

Answer three separate questions about a design:
- Can a reader understand the proposed change?
- Do its claims match the available system evidence?
- Can its consequential guarantees be implemented and checked?

Use this for consequential technical designs, implementation plans or a requested standalone review.
- Choose the checks that can affect readiness.
- Require no document template, full-codebase review or extra agent for a contained change.
- Accept adequate project records from any author.
- A review-only request produces findings and a readiness assessment. It authorizes no design edits and no production implementation.

## Read the artifact on its own terms
From the target and its linked baseline evidence, restate briefly the current system, proposed behavior and important constraints or guarantees.
- An explanation that sounds plausible but differs from the accepted intent is a finding.
- Look for missing relationships and side effects, not only undefined terms.
- Requirements known elsewhere in project records may reveal an omission. Do not supply them from memory and call the artifact ready.
- When edits are authorized, put consequential clarification in the authoritative record or a link.
- Ordinary engineering vocabulary needs no glossary.
- Keep this comprehension check apart from verifying implementation claims. A clear document can still describe a nonexistent component or promise a guarantee the code does not provide.

## Verify the existing foundations and proposed proof
Existing foundations:
- Verify the paths, symbols, interfaces, stored identifiers and behavior the plan depends on, using current source or runtime evidence.
- Follow links and call paths only as far as they can change the assessment.
- Separate verified existing capabilities, proposed additions and unverified assumptions.
- A stale symbol alone may need only a corrected reference. Missing enforcement of a promised guarantee is a design gap.
- Source inspection does not establish deployed behavior.

Proposed proof:
- For each important guarantee, identify the responsible boundary and an observable acceptance check. Include consequential failure and compatibility behavior.
- Distinguish checks to run from executed proof.
- Resolve expensive-to-reverse and cross-component decisions before dependent implementation.
- Leave routine helper names and local code structure to the implementer.
- Do not require a complete file list or zero remaining implementation choices.

## Reconcile findings without adding unnecessary machinery
After material fixes:
- Check that the design still addresses the original problem and accepted scope.
- Ask what observed requirement justifies each added queue, cache, service, abstraction or operational dependency, and whether existing capabilities suffice.
- Check that the fix creates no new contradiction and weakens no guarantee.
- Concrete constraints can justify complexity. Do not remove required authorization, data integrity or recovery mechanisms to shorten a design.

Report findings:
- Consolidate by consequence, with location, evidence, impact and a useful correction.
- Distinguish defects, unresolved decisions and optional improvements.
- Respect accepted trade-offs unless evidence or scope changes.
- Recheck affected fixes when warranted. Do not repeat full reviews to chase a zero-finding round or reopen settled preferences.

## Use independent reading when it changes confidence
Use a fresh reviewer when authoring-context bias or a consequential handoff warrants it, and delegation is available and authorized.
- Pass absolute paths, the review scope and relevant project constraints. Leave out the authoring transcript, desired answers and suspected defects.
- Use the native tool's no-history option. A new agent is not isolated by default.
- A fresh context still shares the filesystem and project instructions. Do not retrieve memory or earlier chat to fill document gaps.
- Keep the reviewer read-only. The authoring agent reconciles findings with accepted decisions.
- Wait for the actual report. A timeout, missing required evidence or inaccessible file means an incomplete review, not zero findings.
- Claim independence only when a fresh context was established.
- Delegation unavailable: continue direct review and state the limitation only where relevant.
- No extra reviewer, fixed number of rounds or ceremony is required.
