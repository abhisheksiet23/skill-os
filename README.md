# SkillMesh

One source library and one installable Codex plugin for Abhishek's business, website and software-engineering practices. Every skill remains independently usable.

## Three responsibilities

| Layer | Owns |
| --- | --- |
| Agent | Objective, expertise selection, synthesis, sequencing and stopping |
| Skills | Reusable methods, preferences and lessons |
| Project | Facts, constraints, decisions, artifacts, code and observed evidence |

Skills may recommend named expertise with a concrete reason, but never invoke other skills. Even for a user-requested sequence, the agent executes it. Native descriptions provide discovery; [SKILLS.md](SKILLS.md) is a human review aid, not a routing database. No registry, blackboard, state engine, dependency graph or orchestration runtime is included.

## Layout

```text
skill-os/
  skillmesh/                   Installable plugin; folder matches its identifier
    .codex-plugin/plugin.json
    skills/<name>/SKILL.md
    skills/<name>/references/  Optional detail local to the owning skill
  SKILLS.md                   Human-readable inventory
  docs/                       Source reconciliation and migration
  evals/                      Scenarios, fixtures and results
  scripts/                    Validation and migration, not agent routing
```

The nested `skillmesh/` folder preserves the workspace name while giving the plugin its proper identifier. Author here; installed copies are deployment artifacts. Projects need neither a copied library nor a new documentation tree.

## Use

Ask for the outcome normally. Codex selects expertise from descriptions; explicitly select a skill when you want its method. Installation exposes individual skills rather than loading the entire library for every task.

Examples:

- Review this API change against the ticket; findings only.
- Design pricing options with unvalidated willingness to pay explicit.
- Improve this contact journey using the existing design.
- Investigate this business idea; stop when more analysis would not change the decision.

Every skill accepts adequate project evidence regardless of its author. No previous invocation, phase ledger, preferred framework or in-app wiki is required. Material design, data and release risks still need real decisions and proof.

## Install and replace

For cloning on another device and editing in Codex cloud, see [GitHub and cloud setup](docs/github-and-cloud.md).

See [migration](docs/migration.md). Validate first, install one plugin, then archive only the superseded individual skill copies. Keep old source repositories and specialized toolkit tools available until separately migrated.

The migration helper defaults to inspection. Installation uses the official plugin scaffold helper for personal-marketplace registration and the Codex CLI. Retirement is explicit and follows verified installation. Unrelated plugins, global instructions and projects remain untouched.

## Verify and evolve

The plugin is Markdown and a manifest. Python 3.10+ and PowerShell 7 are used only by local validation/migration helpers.

```powershell
python scripts/validate_library.py
python -m unittest discover -s tests -v
pwsh -File scripts/Test-Migration.ps1
```

Also run the installed skill-creator and plugin-creator validators as described in [migration](docs/migration.md). Static checks establish packaging/reference integrity, not improved reasoning. [Evals](evals/README.md) describe behavioral comparison and honest reporting of unavailable metrics.

[Source reconciliation](docs/source-review.md) records what was kept, changed and not recovered. Improve observed failures, put reusable lessons in the owning skill and keep company facts in projects. [EVOLUTION.md](EVOLUTION.md) retains the high bar for added architecture.

Let pain create architecture. Keep SkillMesh as simple as it can be, but no simpler.
