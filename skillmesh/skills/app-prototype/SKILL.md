---
name: app-prototype
description: Design and build an inspectable, high-fidelity software prototype with realistic content, interactions and states. Use to resolve material application UX before production implementation; skip backend-only work and contained corrections to an established design.
---

# App Prototype

Make the intended experience concrete enough to judge before production code hardens it. Work from the existing brief, behavior, constraints and design system, regardless of their author. Missing skill-specific records are not missing requirements.

Identify the user's journey and important decisions, then arrange information by how the user thinks. Work structure, visual design and real microcopy together as evidence changes; do not polish a confusing flow. For material design work use [experience craft](references/experience.md).

Prototype the smallest representative journey that exposes the hard parts. Use realistic density, long content, permissions, loading, empty, success, validation, error and recovery states where relevant. Build browser-inspectable HTML/CSS/JS or the project's appropriate prototype format. Label simulated data and operations. Keep prototype work separate from production changes.

Preserve the existing identity unless redesign is authorized. Before choosing UI patterns, inspect the project's component library, design-system documentation or component catalog when available; treat its tokens, variants, composition rules and interaction conventions as design inputs, not merely implementation details. Reuse those components in the prototype when practical, and keep a recognizable component mapping when the prototype format cannot consume them directly. Do not let a library's catalog dictate a poor journey or invent unsupported variants without making the deviation explicit.

Establish concrete typography, spacing, color, surface, layout and interaction choices. For a new direction, choose a reasoned starting point; ask about preferences only when they materially affect the outcome. Use mature components when they represent difficult interactions accurately.

Render and inspect representative narrow, intermediate and wide layouts. Exercise the primary journey, keyboard/focus and recovery. Fix visible problems and re-inspect before presenting. A screenshot file not examined is not visual review; source inspection is not browser proof.

Keep the inspectable prototype primary. Present the concrete revision with the important experience choices, why they matter for the journey and the observed review evidence; link detailed state coverage instead of describing an unseen experience as verified. Save the prototype, launch instructions and durable direction using the project's conventions. Honor an existing approval or delegated design authority; do not infer a reserved approval from silence. Keep unavailable verification explicit.

The output is a reviewed experience and reusable design assets, not production integration. Missing behavior may justify recommending `app-analyze`; a settled prototype may help `app-frontend`. Recommendations explain the gap; only the agent decides whether to invoke another skill or continue.
