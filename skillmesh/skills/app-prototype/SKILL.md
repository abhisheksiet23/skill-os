---
name: app-prototype
description: Design and build an inspectable, high-fidelity software prototype with realistic content, interactions and states. Use to resolve material application UX before production implementation; skip backend-only work and contained corrections to an established design.
---

# App Prototype

Answer the open UX questions of a software change with a realistic, clickable prototype that the owner can react to and the frontend implementer can build from, before production code exists. Choose the questions first and build only the path that answers them. Inspect the result where it runs and hand over the prototype, what you observed and the design direction to keep. It proves the experience, not production behavior.

## Terms
- **Consequential:** changes observable behavior, cost, risk or rework.
- **Hardest decision:** the user decision most likely to be misunderstood or costly to get wrong.
- **Representative path:** the smallest path through the journey that exposes the hardest decision.
- **Inspected:** run where the prototype runs (a browser for web, otherwise the simulator, emulator or device its format targets), exercised, and the actual output examined. A saved screenshot nobody examined, or source reading, is not inspection.
- **Design artifacts:** the project's existing design records, such as design-system notes, tokens and handoff notes.
- **Simulated:** data or an operation with no production backing.
- **Job and journey:** what the user is trying to get done, and the stages they pass through to do it. Each carries an evidence label: owner-stated, observed or inferred.

## Always
1. Inspect what you build where it runs, a browser for web. States, viewports and devices you did not see stay unverified.
2. Label simulated data and operations. A prototype never proves production integration, durable recovery, server enforcement or user comprehension.
3. Keep accepted behavior. Record a gap or a better interaction as a proposal, and do not change accepted behavior silently.
4. Preserve existing identity and settled designs unless redesign is authorized.
5. Honor existing approval and delegated design authority. Never infer a reserved owner approval from silence.

## Choose what the prototype must resolve
Start from the brief, intended behavior, constraints and design system, whoever wrote them.

Inputs:
- Adequate briefs and existing journeys are enough. A formal specification is not required, and missing records from earlier work are not missing requirements.
- Use-case specification, when one exists: choose journeys and states from its actor goals, selected flows, alternatives, shared rules and done-checks.
- Analysis findings: consult for the problem, rationale and open choices.
- Owner brief, if one exists: link the decisions (D-n) and facts (F-n) the prototype touches. A flow resting on a recommended default the owner has not confirmed is marked "on defaults", and its prototype is provisional.
- Job and journey: the primary lens for choosing the path. When absent and the UX is material, derive a provisional one from the brief and label each part inferred.
- Unstated business rules, such as limits, windows and thresholds, are open facts. Mark them simulated and list them in the handoff.
- Existing evidence: reuse settled behavior and design evidence. Retrieve only the journey, component and state details the open question needs.

Scope:
- Identify the user's journey, important decisions and hardest decision.
- Prototype the representative path first. Inspect it before adding screens or polishing secondary states.
- Design structure, visual design and wording together. Arrange information around the user's task, not the database. Reconsider a confusing flow before polishing it.
- Read [experience craft](references/experience.md) to select and inspect the hardest decision before expanding material design.
- Read [microcopy craft](references/microcopy.md) for every user-visible state string: error, empty, confirmation, permission, restricted and unknown outcome.

Direction:
- Existing identity: keep it. Redesign only when authorized.
- Reference products: study two or three products the audience already uses for the same job. Take the reason behind what works, not the look.
- New direction: choose a reasoned starting point. Ask about preferences only when they materially change the outcome.
- Fix concrete typography, spacing, color, surface, shape, icons, layout and interaction choices.
- No existing design system or tokens, a new direction or a material visual change: read [visual system](references/visual-system.md).
- Use mature controls where they represent difficult interactions accurately.

## Choose components
Inspect the project's component catalog, design-system guidance, tokens and representative screens before inventing controls.

- Existing system: keep adequate accepted designs and suitable components, with their supported variants and conventions.
- Verification: check that a component's semantics, variants, responsive behavior and extension points fit the journey. Check package dependencies too.
- No adequate system: prefer an established library that fits the stack, accessibility needs and visual direction. This preference does not authorize package installation or framework migration.
- Reuse: use the library directly when practical.
- Prototype format cannot use the components: reproduce enough of the visual and interaction contract to make implementation credible. Record the recognizable mapping or deliberate deviation in design artifacts.
- Review scope: build no review around component states that do not exist.
- Data controls: sorting, filtering and paging need real behavior within the component's documented limits. A static table needs no grid dependency.
- Uncertain pattern: when guidance could change an interaction-pattern choice, read [component selection](references/component-selection.md).
- Its suggestions are hypotheses. They are not an allowed-component list and not a reason to reopen settled choices.
- No approval and no separate catalog artifact is required to reuse, compose, extend or create a component for task fit. Keep required behavior and accessibility.
- A component catalog must not dictate a poor journey.
- Reference unreadable: report the broken link and continue from the task and design evidence. Do not claim to have consulted it.

## Build the evidence
Build more than the happy screen.

- Format: browser-inspectable HTML/CSS/JS, or the project's suitable prototype format.
- Separation: keep prototype changes apart from production code.
- Scaffolding: keep controls for simulated conditions out of the product's viewport, collapsed or docked at the edge. They must not hide the design.
- Content integrity: content that carries authority, such as scripture, law, medicine or prices, comes from a named source or is plainly placeholder. A prototype must not lend credibility to invented material.
- States: include realistic density and long content. Include permission, loading, empty, success, validation, error and recovery states that affect the journey.
- Layouts: render narrow, intermediate and wide layouts appropriate to the product.
- Exercise: run the primary journey, keyboard and focus, and recovery.
- Review loop: inspect the actual output, correct visible defects, then inspect again.
- Compare: set the output beside the reference products and the job. Name where yours is harder to scan, heavier or less oriented, and fix the largest gap.
- Measure: check with a script what the environment can measure, such as contrast, tap-target size and focus order. State what you measured and what you did not.

Source readability:
- Put blank lines between logical handlers and UI sections.
- Expand branches, error handling and object literals. Show template nesting and attributes. Separate CSS rules.
- Group cohesive statements. Do not space every line.
- Disposable code and formatter success do not establish readability.
- Generated or minified third-party output is outside this review.

## Present the revision
Keep the inspectable prototype primary. Add compact labeled facts:
- The job the prototype serves, in one line, with its evidence label.
- Launch.
- Consequential choices, with the reason for those that affect the journey.
- Observed states and viewports.
- Limitations.

Then:
- Comparing coverage: a short state, viewport and result table helps.
- Detailed evidence: link it. Do not narrate every screen.
- Durable direction: save useful tokens, component treatments, icon mapping and direction using project conventions.
- After a change: reuse review evidence for unchanged states and inspect the affected states again.
- Lessons: record pattern-selection lessons from review and later development in the project's design artifacts, even when the original choice was settled.
- Missing consequential behavior: it may need analysis. An established direction may support frontend implementation. Name the gap and why. The agent decides whether more expertise changes the result.

**Wording:** be truthful and growth-minded. Say "not yet" where something can still happen, and keep evidence, warnings and results exact.
