"""Launch the pinned upstream CLI with SkillMesh-owned settings, not user-global modes."""
from __future__ import annotations

import os
from pathlib import Path
import sys


def main() -> None:
    home = Path(os.environ.get('SKILLMESH_SERENA_HOME', str(Path.home() / '.serena' / 'skillmesh')))
    home.mkdir(parents=True, exist_ok=True)
    os.environ['SERENA_HOME'] = str(home.resolve())
    os.environ['SERENA_USAGE_REPORTING'] = 'false'
    # Concurrent chat startup must not read a partially initialized configuration.
    from filelock import FileLock
    with FileLock(str(home / '.bootstrap.lock'), timeout=30):
        config = home / 'serena_config.yml'
        if not config.exists():
            config.write_text('projects: []\nbase_modes: []\ndefault_modes: []\n'
                              'trusted_project_path_patterns: []\n', encoding='utf-8')
    from serena.cli import top_level
    top_level.main(args=sys.argv[1:], prog_name='serena')


if __name__ == '__main__':
    main()
