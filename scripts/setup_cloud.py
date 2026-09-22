#!/usr/bin/env python3
"""Expose the source skills to Codex in a Linux cloud checkout, without copying."""
from pathlib import Path


def setup(repo: Path) -> int:
    source = repo.resolve() / "skillmesh" / "skills"
    skills = sorted(p for p in source.iterdir() if (p / "SKILL.md").is_file())
    if not skills:
        raise RuntimeError(f"No skills found in {source}")
    destination = repo.resolve() / ".agents" / "skills"
    if destination.is_symlink():
        raise RuntimeError(f"Refusing linked destination: {destination}")
    # Check every collision before creating any links; never overwrite local skills.
    for skill in skills:
        link = destination / skill.name
        if link.is_symlink() and link.resolve() == skill.resolve():
            continue
        if link.exists() or link.is_symlink():
            raise RuntimeError(f"Existing skill must be reviewed: {link}")
    destination.mkdir(parents=True, exist_ok=True)
    for skill in skills:
        link = destination / skill.name
        if not link.is_symlink():
            link.symlink_to(Path("../../skillmesh/skills") / skill.name, target_is_directory=True)
    print(f"Exposed {len(skills)} source skills through {destination}")
    return len(skills)


if __name__ == "__main__":
    setup(Path(__file__).resolve().parents[1])
