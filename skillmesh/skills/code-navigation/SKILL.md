---
name: code-navigation
description: Locate definitions, references and implementations or trace code impact across an existing project using available semantic tools and search. Use for unfamiliar code or cross-file navigation; skip simple known-file edits and non-code research.
---

# Code Navigation

Answer the current code question using the smallest useful source slice. Available semantic tools can reduce ambiguous text matches; their presence does not establish complete coverage or replace source verification. Work with existing tools when Serena is unavailable.

Establish the active repository/worktree root from the task, not the plugin path. Before Serena activation, inspect existing `.serena/project.yml` and `project.local.yml` when present for activation commands, language settings and ignored paths. Follow project instructions and task authorization; do not execute an unexpected activation command merely to enable navigation. Activation may create provider configuration/caches in a writable project. Respect review-only/no-write scope: use search if activation would write outside the allowed boundary.

Read Serena's initial instructions when exposed, pass its supplied session ID when activating the absolute project root, and confirm the root with `get_current_config`. Validate a known symbol before trusting semantic results; activation may return before language-server initialization finishes. Warm a newly installed backend before simultaneous cold activations, which can collide while extracting shared dependencies. Use overviews to locate symbols, fetch relevant bodies, then references/implementations to trace impact. Scope queries by file or subtree where practical. Recheck the root after a project switch; do not share a mutable active-project server between unrelated sessions. Serena's reported line numbers are zero-based; verify/convert them for one-based source citations.

An empty response is not proof of no usages. Check initialization, language support, dependencies and ignore rules. Use `rg` and file reads for unsupported paths, routes, configuration, reflection, SQL and framework relationships. For Angular, verify template relationships separately; the language server needs resolvable Angular dependencies. For C#, verify backend/runtime compatibility without changing the application's target framework.

Keep application facts and navigation findings in the owning project. This bundle exposes navigation, not Serena editing, shell execution or memory management. Continue the authorized task through ordinary tools; tool failure must not block useful work. Report consequential coverage gaps and count fallback/correction effort before claiming savings.
