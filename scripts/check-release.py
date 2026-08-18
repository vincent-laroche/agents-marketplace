#!/usr/bin/env python3
"""Check repository and plugin versions before a marketplace release."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def run(root: Path) -> int:
    errors: list[str] = []
    version_path = root / "VERSION"
    try:
        version = version_path.read_text(encoding="utf-8").strip()
    except OSError as error:
        errors.append(f"VERSION: {error}")
        version = ""
    if not SEMVER.fullmatch(version):
        errors.append(f"VERSION must contain strict semver, got {version!r}")

    manifests = sorted(root.glob("plugins/*/.codex-plugin/plugin.json"))
    manifests.extend(sorted(root.glob("vendor/*/.codex-plugin/plugin.json")))
    if not manifests:
        errors.append("no plugin manifests found")
    for manifest_path in manifests:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f"{manifest_path.relative_to(root)}: {error}")
            continue
        plugin_version = str(manifest.get("version", ""))
        if not SEMVER.fullmatch(plugin_version):
            errors.append(f"{manifest_path.relative_to(root)}: invalid version {plugin_version!r}")

    if os.environ.get("GITHUB_REF_TYPE") == "tag":
        expected = f"v{version}"
        actual = os.environ.get("GITHUB_REF_NAME", "")
        if actual != expected:
            errors.append(f"release tag must be {expected!r}, got {actual!r}")

    if errors:
        print(f"FAILED: {len(errors)} release issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK: marketplace {version}; {len(manifests)} plugin version(s) valid")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Marketplace repository root")
    args = parser.parse_args()
    return run(args.root.expanduser().resolve())


if __name__ == "__main__":
    raise SystemExit(main())
