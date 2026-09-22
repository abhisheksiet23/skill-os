# Work across devices and in Codex cloud

GitHub is the shared authoring source. Commit and push work before switching devices; pull before starting work elsewhere. Installed plugin copies do not sync automatically.

## Another device

Clone your private `skill-os` repository using its GitHub clone URL, then open the checkout in Codex. Read `AGENTS.md` and `SKILLS.md`; author maintained skills under `skillmesh/skills/`.

Python 3.10+ is sufficient for the portable checks (use `python3` if that is your Python command):

```sh
python scripts/validate_library.py
python -m unittest discover -s tests -v
```

For local plugin installation, follow [migration.md](migration.md). The existing installer targets Windows and requires PowerShell 7, RTK, Codex CLI and the installed system plugin-creator helpers. Cloning alone does not install the plugin. Do not assume that installer works unchanged on macOS or Linux.

Use a branch for changes, push it, and review/merge through GitHub. On other devices, update a clean checkout with `git pull --ff-only`; commit or stash local changes before switching branches. Refresh the locally installed plugin after pulling skill changes.

## Codex cloud

1. Open Codex on the web and connect your GitHub account.
2. Allow access to the private `skill-os` repository and create an environment for it.
3. Select manual setup and use `python3 scripts/setup_cloud.py` as both the setup and maintenance script. It creates ignored relative links under `.agents/skills/` to the source folders, without copying or overwriting existing skills. Use Python 3.10+ for the two portable checks above. No package installation or secrets are needed for those checks. Do not run the Windows plugin migration installer as a cloud setup script.
4. Select the environment and request a repository change. Ask Codex to read `AGENTS.md`, inspect `SKILLS.md`, and open only the relevant skill source files.
5. Review the resulting diff and checks, then open and merge a pull request. Pull the merged changes on your other devices.

Example task:

> Read AGENTS.md and SKILLS.md. Improve the requested skill in skillmesh/skills/, keep required references inside its own folder, and run the packaging validator and unit tests. For substantive methodology changes, collect representative before/after behavioral evidence and label unavailable metrics unknown.

Cloud repository access enables editing the source. It does not transfer this computer's installed plugins, connectors, credentials or personal instructions. External services and behavioral evaluations need their own available tools and authorization in each environment.

The setup script exposes skills only within this checkout. Other application environments require their own installation of the library; merely connecting this repository does not install it account-wide. Avoid running this cloud setup locally if the SkillMesh plugin is already installed, since both discovery paths can expose duplicate skills.

Official setup reference: [Codex cloud](https://learn.chatgpt.com/docs/cloud).
