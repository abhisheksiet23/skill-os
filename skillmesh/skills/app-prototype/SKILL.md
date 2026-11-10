---
name: app-prototype
description: Design and build an inspectable, high-fidelity software prototype with realistic content, interactions and states. Use to resolve material application UX before production implementation; skip backend-only work and contained corrections to an established design.
---

# App Prototype

Make the experience inspectable before production implementation hardens it. The deliverable is a realistic prototype, observed review evidence and reusable design direction. It does not establish production integration.

## Choose what the prototype must resolve

Start from the actual brief, intended behavior, constraints and design system, regardless of author. Missing skill-specific records are not missing requirements. Identify the user's journey, important decisions and hardest interaction; prototype the smallest representative path that exposes those questions.

Work structure, visual design and real microcopy together. Arrange information around the user's task, not the database, and reconsider a confusing flow before polishing it. Read [experience craft](references/experience.md) for material design, and its linked microcopy guidance when wording defines state, consequence or recovery.

Inspect the project's component catalog, design-system guidance, tokens and representative screens before inventing controls. Use supported variants and interaction conventions as design inputs. Reuse components when practical; when the prototype format cannot consume them, record the recognizable mapping or deliberate deviation. A component catalog must not dictate a poor journey.

Preserve existing identity unless redesign is authorized. Establish concrete typography, spacing, color, surface, layout and interaction choices. For a new direction choose a reasoned starting point; ask preferences only when they materially change the outcome. Use mature controls where they represent difficult interactions accurately.

## Build the evidence, not just the happy screen

Create browser-inspectable HTML/CSS/JS or the project's suitable prototype format. Keep prototype changes separate from production code and label simulated data and operations. Include realistic density and long content, plus permission, loading, empty, success, validation, error and recovery states that affect the journey.

Keep authored source readable: blank lines between logical handlers and UI sections, expanded branches/error handling and object literals, visible template nesting/attributes and separated CSS rules. Group cohesive statements instead of spacing every line. Disposable code and formatter success do not establish readability; generated/minified third-party output is outside this source review.

Render narrow, intermediate and wide layouts appropriate to the product. Exercise the primary journey, keyboard/focus and recovery, inspect the actual output, correct visible defects and re-inspect. A saved screenshot that was never examined is not visual review; source inspection cannot replace browser evidence.

## Present the concrete revision

Keep the inspectable prototype primary. Explain consequential experience choices and their effect on the journey, with observed viewport/state evidence and remaining limitations. Save launch instructions, useful tokens, component treatments and durable direction using project conventions; link detailed coverage rather than describing unseen states as verified.

Honor existing approval and delegated design authority. Do not infer a reserved owner approval from silence, or claim a mock as production proof. Missing consequential behavior may need analysis; an established direction may support frontend implementation. Explain the gap and let the agent choose whether further expertise changes the result.
