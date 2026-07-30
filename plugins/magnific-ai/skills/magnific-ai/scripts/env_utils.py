"""Load only named Magnific secrets without sourcing or exposing the full env file."""

from __future__ import annotations

import os
from pathlib import Path


MASTER_ENV_PATH = Path("/Users/vMac/.env")


def load_named_secret(name: str, env_path: Path = MASTER_ENV_PATH) -> str | None:
    current = os.environ.get(name)
    if current:
        return current
    if not env_path.is_file():
        return None

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        key, separator, value = line.partition("=")
        if not separator or key.strip() != name:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        return value or None
    return None
