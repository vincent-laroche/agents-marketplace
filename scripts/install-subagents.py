#!/usr/bin/env python3
"""Manage marketplace subagents in a Codex profile without touching unrelated roles."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
import tomllib
from datetime import UTC, datetime
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ".agents-marketplace-state.json"
TRASH_DIR = ".agents-marketplace-trash"
REQUIRED = {
    "name",
    "description",
    "developer_instructions",
    "model",
    "model_reasoning_effort",
    "sandbox_mode",
}


def parse_agent(path: Path) -> dict:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ValueError(f"{path}: invalid TOML: {error}") from error
    missing = sorted(REQUIRED - data.keys())
    if missing:
        raise ValueError(f"{path}: missing {', '.join(missing)}")
    return data


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_catalog(root: Path) -> dict:
    path = root / ".agents" / "plugins" / "marketplace.json"
    return json.loads(path.read_text(encoding="utf-8"))


def load_state(registry: Path) -> dict:
    path = registry / STATE_FILE
    if not path.is_file():
        return {"schema_version": 1, "selected_plugins": [], "managed": {}}
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"{path}: invalid state file: {error}") from error
    if state.get("schema_version") != 1 or not isinstance(state.get("managed"), dict):
        raise ValueError(f"{path}: unsupported state schema")
    state.setdefault("selected_plugins", [])
    return state


def atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
        Path(temporary).replace(path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def selected_plugin_names(catalog: dict, requested: list[str], state: dict) -> set[str]:
    entries = catalog.get("plugins", [])
    known = {entry.get("name") for entry in entries}
    unknown = sorted(set(requested) - known)
    if unknown:
        raise ValueError(f"unknown plugin(s): {', '.join(unknown)}")
    defaults = {
        entry["name"]
        for entry in entries
        if entry.get("policy", {}).get("installation") == "INSTALLED_BY_DEFAULT"
    }
    return defaults | set(state.get("selected_plugins", [])) | set(requested)


def marketplace_agents(root: Path, selected: set[str]) -> list[dict]:
    catalog = load_catalog(root)
    agents: list[dict] = []
    for entry in catalog.get("plugins", []):
        plugin = entry.get("name")
        if plugin not in selected:
            continue
        plugin_root = (root / entry["source"]["path"]).resolve()
        agents_dir = plugin_root / "agents"
        if not agents_dir.is_dir():
            continue
        for source in sorted(agents_dir.glob("*.toml")):
            text = source.read_text(encoding="utf-8")
            agents.append(
                {
                    "plugin": plugin,
                    "source": source,
                    "source_path": str(source.relative_to(root)),
                    "target": f"{plugin}-{source.name}",
                    "data": parse_agent(source),
                    "text": text,
                    "sha256": digest(text),
                }
            )
    return agents


def registered_by_name(registry: Path) -> dict[str, list[Path]]:
    found: dict[str, list[Path]] = {}
    if not registry.is_dir():
        return found
    for path in sorted(registry.glob("*.toml")):
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError):
            continue
        name = data.get("name")
        if isinstance(name, str) and name.strip():
            found.setdefault(name, []).append(path)
    return found


def state_record(agent: dict) -> dict:
    return {
        "name": agent["data"]["name"],
        "plugin": agent["plugin"],
        "source": agent["source_path"],
        "sha256": agent["sha256"],
    }


def move_to_trash(registry: Path, path: Path) -> Path:
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    destination = registry / TRASH_DIR / stamp / path.name
    suffix = 1
    while destination.exists():
        destination = destination.with_name(f"{path.stem}-{suffix}{path.suffix}")
        suffix += 1
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(path), str(destination))
    return destination


def inspect(root: Path, registry: Path, requested: list[str]) -> tuple[dict, set[str], list[dict], dict[str, list[Path]], list[str]]:
    state = load_state(registry)
    catalog = load_catalog(root)
    selected = selected_plugin_names(catalog, requested, state)
    agents = marketplace_agents(root, selected)
    registered = registered_by_name(registry)
    desired_targets = {agent["target"] for agent in agents}
    issues: list[str] = []
    managed = state["managed"]

    for agent in agents:
        target = registry / agent["target"]
        matches = registered.get(agent["data"]["name"], [])
        unmanaged_matches = [path for path in matches if path.name not in managed and path != target]
        if unmanaged_matches:
            issues.append(
                f"unmanaged same-name role {agent['data']['name']!r}: "
                + ", ".join(str(path) for path in unmanaged_matches)
            )
        if target.is_file() and target.name not in managed and target.read_text(encoding="utf-8") != agent["text"]:
            issues.append(f"unmanaged target would be overwritten: {target}")
    for filename in managed:
        if filename not in desired_targets:
            issues.append(f"stale managed role: {registry / filename}")
    return state, selected, agents, registered, issues


def status(root: Path, registry: Path, requested: list[str]) -> int:
    state, selected, agents, _registered, issues = inspect(root, registry, requested)
    managed = state["managed"]
    for agent in agents:
        target = registry / agent["target"]
        if not target.is_file():
            issues.append(f"missing managed role: {target}")
        elif target.read_text(encoding="utf-8") != agent["text"]:
            issues.append(f"drift in managed role: {target}")
        elif target.name not in managed:
            issues.append(f"untracked marketplace role: {target}")
    if issues:
        print(f"DRIFT: {len(issues)} issue(s) in {registry}")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(f"OK: {len(agents)} managed subagents are current for {', '.join(sorted(selected)) or 'no plugins'}")
    return 0


def synchronize(root: Path, registry: Path, requested: list[str], adopt_existing: bool) -> int:
    state, selected, agents, registered, issues = inspect(root, registry, requested)
    blocking = [issue for issue in issues if not issue.startswith("stale managed role:")]
    if blocking and not adopt_existing:
        print(f"FAILED: {len(blocking)} unmanaged conflict(s); no files changed", file=sys.stderr)
        for issue in blocking:
            print(f"- {issue}", file=sys.stderr)
        print("Re-run with --adopt-existing only after reviewing those files.", file=sys.stderr)
        return 1

    registry.mkdir(parents=True, exist_ok=True)
    changed = 0
    for agent in agents:
        target = registry / agent["target"]
        if adopt_existing:
            for existing in registered.get(agent["data"]["name"], []):
                if existing != target and existing.is_file() and existing.name not in state["managed"]:
                    backup = move_to_trash(registry, existing)
                    print(f"BACKUP: {existing} -> {backup}")
        if target.is_file() and target.read_text(encoding="utf-8") != agent["text"] and target.name not in state["managed"]:
            if not adopt_existing:
                continue
            backup = move_to_trash(registry, target)
            print(f"BACKUP: {target} -> {backup}")
        if not target.is_file() or target.read_text(encoding="utf-8") != agent["text"]:
            target.write_text(agent["text"], encoding="utf-8")
            print(f"SYNC: {agent['source_path']} -> {target}")
            changed += 1
        state["managed"][target.name] = state_record(agent)
    state["selected_plugins"] = sorted(selected - {
        entry["name"]
        for entry in load_catalog(root).get("plugins", [])
        if entry.get("policy", {}).get("installation") == "INSTALLED_BY_DEFAULT"
    })
    state["marketplace"] = str(root)
    atomic_json(registry / STATE_FILE, state)
    print(f"OK: {len(agents)} managed subagents; {changed} file(s) synchronized")
    return 0


def prune(root: Path, registry: Path, requested: list[str]) -> int:
    state = load_state(registry)
    catalog = load_catalog(root)
    selected = selected_plugin_names(catalog, requested, state)
    desired = {agent["target"] for agent in marketplace_agents(root, selected)}
    stale = sorted(set(state["managed"]) - desired)
    for filename in stale:
        target = registry / filename
        if target.is_file():
            destination = move_to_trash(registry, target)
            print(f"PRUNE: {target} -> {destination}")
        state["managed"].pop(filename, None)
    atomic_json(registry / STATE_FILE, state)
    print(f"OK: pruned {len(stale)} stale managed subagent(s)")
    return 0


def uninstall(registry: Path) -> int:
    state = load_state(registry)
    removed = 0
    for filename in sorted(state["managed"]):
        target = registry / filename
        if target.is_file():
            destination = move_to_trash(registry, target)
            print(f"UNINSTALL: {target} -> {destination}")
            removed += 1
    state_path = registry / STATE_FILE
    state_path.unlink(missing_ok=True)
    print(f"OK: uninstalled {removed} managed subagent(s); unrelated roles were preserved")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", nargs="?", choices=("install", "update", "status", "prune", "uninstall"))
    legacy = parser.add_mutually_exclusive_group()
    legacy.add_argument("--apply", action="store_true", help="Compatibility alias for install")
    legacy.add_argument("--check", action="store_true", help="Compatibility alias for status")
    parser.add_argument("--plugin", action="append", default=[], help="Also manage an AVAILABLE plugin; repeatable")
    parser.add_argument("--adopt-existing", action="store_true", help="Back up and replace reviewed same-name conflicts")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Marketplace repository root")
    parser.add_argument(
        "--codex-home",
        type=Path,
        default=Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")),
        help="Codex profile root; defaults to CODEX_HOME or ~/.codex",
    )
    args = parser.parse_args()
    command = args.command or ("install" if args.apply else "status" if args.check else "status")
    root = args.root.expanduser().resolve()
    registry = args.codex_home.expanduser().resolve() / "agents"

    try:
        if command == "status":
            return status(root, registry, args.plugin)
        if command in {"install", "update"}:
            return synchronize(root, registry, args.plugin, args.adopt_existing)
        if command == "prune":
            return prune(root, registry, args.plugin)
        return uninstall(registry)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
