#!/usr/bin/env python3
"""Synchronize marketplace subagents into a Codex profile's agent registry."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / ".agents" / "plugins" / "marketplace.json"
REQUIRED = {"name", "description", "developer_instructions", "sandbox_mode"}


def parse_agent(path: Path) -> dict:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ValueError(f"{path}: invalid TOML: {error}") from error
    missing = sorted(REQUIRED - data.keys())
    if missing:
        raise ValueError(f"{path}: missing {', '.join(missing)}")
    return data


def marketplace_agents() -> list[tuple[str, Path, dict]]:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    agents: list[tuple[str, Path, dict]] = []
    for entry in catalog["plugins"]:
        plugin = entry["name"]
        plugin_root = (ROOT / entry["source"]["path"]).resolve()
        agents_dir = plugin_root / "agents"
        if not agents_dir.is_dir():
            continue
        for path in sorted(agents_dir.glob("*.toml")):
            agents.append((plugin, path, parse_agent(path)))
    return agents


def registered_agents(registry: Path) -> dict[str, list[Path]]:
    by_name: dict[str, list[Path]] = {}
    if not registry.is_dir():
        return by_name
    for path in sorted(registry.glob("*.toml")):
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError):
            continue
        name = data.get("name")
        if isinstance(name, str) and name.strip():
            by_name.setdefault(name, []).append(path)
    return by_name


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="Write missing or drifted registry files")
    mode.add_argument("--check", action="store_true", help="Fail if the registry differs from the marketplace")
    parser.add_argument(
        "--codex-home",
        type=Path,
        default=Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")),
        help="Codex profile root; defaults to CODEX_HOME or ~/.codex",
    )
    args = parser.parse_args()
    registry = args.codex_home.expanduser().resolve() / "agents"

    try:
        sources = marketplace_agents()
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    existing = registered_agents(registry)
    changes: list[tuple[str, Path, Path]] = []
    adopted = 0
    current = 0
    errors: list[str] = []

    for plugin, source, data in sources:
        name = data["name"]
        matches = existing.get(name, [])
        if len(matches) > 1:
            errors.append(f"{name}: duplicate registry files: {', '.join(str(path) for path in matches)}")
            continue
        target = matches[0] if matches else registry / f"{plugin}-{source.name}"
        source_text = source.read_text(encoding="utf-8")
        target_text = target.read_text(encoding="utf-8") if target.is_file() else None
        if target_text == source_text:
            current += 1
            continue
        action = "update" if target.is_file() else "install"
        changes.append((action, source, target))
        if matches:
            adopted += 1

    if errors:
        print(f"FAILED: {len(errors)} duplicate registration issue(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    if args.check:
        if changes:
            print(f"DRIFT: {len(changes)} of {len(sources)} marketplace subagents need synchronization")
            for action, source, target in changes:
                print(f"- {action}: {source.relative_to(ROOT)} -> {target}")
            return 1
        print(f"OK: {len(sources)} marketplace subagents are synchronized in {registry}")
        return 0

    if args.apply:
        registry.mkdir(parents=True, exist_ok=True)
        for action, source, target in changes:
            target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"{action.upper()}: {source.relative_to(ROOT)} -> {target}")
        print(
            f"OK: {len(sources)} subagents; {len(changes)} changed, "
            f"{adopted} adopted by name, {current} already current"
        )
        return 0

    print(f"PREVIEW: {len(sources)} subagents; {len(changes)} change(s) for {registry}")
    for action, source, target in changes:
        print(f"- {action}: {source.relative_to(ROOT)} -> {target}")
    print("Run again with --apply to synchronize or --check for CI-style verification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
