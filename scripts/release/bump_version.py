"""Calcula (e opcionalmente aplica) o bump de versao no pyproject.toml.

Uso:
    python scripts/release/bump_version.py major|minor|patch [--dry-run]

Imprime a nova versao em stdout. Com --dry-run, so calcula e imprime,
sem escrever no arquivo (usado para checar a branch antes de commitar).
"""

import re
import sys
from pathlib import Path

PYPROJECT = Path(__file__).resolve().parents[2] / "pyproject.toml"
VERSION_RE = re.compile(r'version = "(\d+)\.(\d+)\.(\d+)"')


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] not in ("major", "minor", "patch"):
        sys.exit("ERRO: parametro invalido. Uso: bump_version.py major|minor|patch [--dry-run]")

    bump = args[0]
    dry_run = "--dry-run" in args[1:]

    text = PYPROJECT.read_text(encoding="utf-8")
    match = VERSION_RE.search(text)
    if not match:
        sys.exit(f'ERRO: nao encontrei \'version = "x.y.z"\' em {PYPROJECT}')

    major, minor, patch = (int(g) for g in match.groups())
    if bump == "major":
        major, minor, patch = major + 1, 0, 0
    elif bump == "minor":
        minor, patch = minor + 1, 0
    else:
        patch += 1
    new_version = f"{major}.{minor}.{patch}"

    if not dry_run:
        new_text = text[: match.start()] + f'version = "{new_version}"' + text[match.end() :]
        PYPROJECT.write_text(new_text, encoding="utf-8")

    print(new_version)


if __name__ == "__main__":
    main()
