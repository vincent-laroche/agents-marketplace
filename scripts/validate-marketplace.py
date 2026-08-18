#!/usr/bin/env python3
"""Validate the Codex-native marketplace, plugins, skills, agents, and MCP configs."""

from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / ".agents" / "plugins" / "marketplace.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
BANNED_NAMES = {
    ".claude-plugin",
    ".cursor-plugin",
    "CLAUDE.md",
    "GEMINI.md",
    "gemini-extension.json",
    "ANTIGRAVITY_GUIDANCE.md",
    "copilot-instructions.md",
}
REQUIRED_AGENT_FIELDS = {"name", "description", "developer_instructions", "sandbox_mode"}
VALID_SANDBOX_MODES = {"read-only", "workspace-write"}
VALID_INSTALLATION = {"NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"}
VALID_AUTHENTICATION = {"ON_INSTALL", "ON_USE"}


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {error}")
        return {}


def validate_skill(skill_dir: Path, errors: list[str]) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
        return
    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append(f"{skill_file.relative_to(ROOT)}: missing YAML frontmatter")
        return
    frontmatter = match.group(1)
    if not re.search(r"^name:\s*\S", frontmatter, re.MULTILINE):
        errors.append(f"{skill_file.relative_to(ROOT)}: missing frontmatter name")
    if not re.search(r"^description:\s*\S", frontmatter, re.MULTILINE):
        errors.append(f"{skill_file.relative_to(ROOT)}: missing frontmatter description")


def validate_agent(path: Path, seen_names: set[str], errors: list[str]) -> None:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        errors.append(f"{path.relative_to(ROOT)}: invalid TOML: {error}")
        return
    missing = sorted(REQUIRED_AGENT_FIELDS - data.keys())
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing {', '.join(missing)}")
    for field in REQUIRED_AGENT_FIELDS - {"sandbox_mode"}:
        if field in data and (not isinstance(data[field], str) or not data[field].strip()):
            errors.append(f"{path.relative_to(ROOT)}: {field} must be a non-empty string")
    if data.get("sandbox_mode") not in VALID_SANDBOX_MODES:
        errors.append(f"{path.relative_to(ROOT)}: invalid sandbox_mode {data.get('sandbox_mode')!r}")
    name = data.get("name")
    if isinstance(name, str):
        if name in seen_names:
            errors.append(f"{path.relative_to(ROOT)}: duplicate agent name {name!r}")
        seen_names.add(name)


def validate_plugin(plugin_root: Path, catalog_name: str, seen_agents: set[str], errors: list[str]) -> tuple[int, int]:
    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    manifest = load_json(manifest_path, errors)
    required = ("name", "version", "description", "author", "interface")
    for field in required:
        if not manifest.get(field):
            errors.append(f"{manifest_path.relative_to(ROOT)}: missing {field}")
    if manifest.get("name") != catalog_name:
        errors.append(f"{manifest_path.relative_to(ROOT)}: name does not match catalog entry {catalog_name!r}")
    if not SEMVER.fullmatch(str(manifest.get("version", ""))):
        errors.append(f"{manifest_path.relative_to(ROOT)}: version must be strict semver")
    if not isinstance(manifest.get("author"), dict) or not manifest.get("author", {}).get("name"):
        errors.append(f"{manifest_path.relative_to(ROOT)}: author.name is required")
    interface = manifest.get("interface") if isinstance(manifest.get("interface"), dict) else {}
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category", "capabilities", "defaultPrompt"):
        if not interface.get(field):
            errors.append(f"{manifest_path.relative_to(ROOT)}: interface.{field} is required")
    repository = manifest.get("repository")
    if (
        plugin_root.parent == ROOT / "plugins"
        and repository
        and "vincent-laroche/agents-marketplace" not in repository
    ):
        errors.append(f"{manifest_path.relative_to(ROOT)}: repository must point to agents-marketplace")
    if "hooks" in manifest:
        errors.append(f"{manifest_path.relative_to(ROOT)}: hooks are not supported by Codex plugin ingestion")

    skill_count = 0
    skills_dir = plugin_root / "skills"
    if manifest.get("skills"):
        if not skills_dir.is_dir():
            errors.append(f"{manifest_path.relative_to(ROOT)}: skills path does not exist")
        else:
            for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
                validate_skill(skill_dir, errors)
                skill_count += 1

    agent_paths = sorted((plugin_root / "agents").glob("*.toml")) if (plugin_root / "agents").is_dir() else []
    for agent_path in agent_paths:
        validate_agent(agent_path, seen_agents, errors)
    capabilities = interface.get("capabilities", [])
    if agent_paths and "Subagents" not in capabilities:
        errors.append(f"{manifest_path.relative_to(ROOT)}: agents exist but Subagents capability is missing")
    if (plugin_root / ".codex" / "agents").exists():
        errors.append(f"{plugin_root.relative_to(ROOT)}: move .codex/agents/*.toml to agents/*.toml")

    mcp_reference = manifest.get("mcpServers")
    if mcp_reference:
        if isinstance(mcp_reference, str):
            mcp_path = plugin_root / mcp_reference
            mcp_data = load_json(mcp_path, errors)
            if not mcp_data.get("mcpServers"):
                errors.append(f"{mcp_path.relative_to(ROOT)}: mcpServers must be non-empty")
            raw = mcp_path.read_text(encoding="utf-8") if mcp_path.is_file() else ""
            if re.search(r"Bearer\s+(?!\$\{)[A-Za-z0-9._-]{12,}", raw, re.IGNORECASE):
                errors.append(f"{mcp_path.relative_to(ROOT)}: possible committed bearer token")
        elif not isinstance(mcp_reference, dict):
            errors.append(f"{manifest_path.relative_to(ROOT)}: mcpServers must be a path or object")
        if "MCP" not in capabilities:
            errors.append(f"{manifest_path.relative_to(ROOT)}: MCP config exists but MCP capability is missing")

    return skill_count, len(agent_paths)


def main() -> int:
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.name in BANNED_NAMES:
            errors.append(f"{path.relative_to(ROOT)}: banned non-Codex packaging surface")
        if path.is_file() and path.name == "hooks.json" and path.parent.name == "hooks":
            errors.append(f"{path.relative_to(ROOT)}: non-Codex hook manifest is not supported")

    catalog = load_json(CATALOG, errors)
    if catalog.get("name") != "agents-marketplace":
        errors.append(".agents/plugins/marketplace.json: name must be agents-marketplace")
    entries = catalog.get("plugins") if isinstance(catalog.get("plugins"), list) else []
    catalog_names: set[str] = set()
    catalog_roots: set[Path] = set()
    seen_agents: set[str] = set()
    total_skills = 0
    total_agents = 0
    for entry in entries:
        name = entry.get("name")
        if not isinstance(name, str) or not name:
            errors.append("catalog entry is missing name")
            continue
        if name in catalog_names:
            errors.append(f"catalog contains duplicate plugin {name!r}")
        catalog_names.add(name)
        source = entry.get("source") if isinstance(entry.get("source"), dict) else {}
        if source.get("source") != "local" or not isinstance(source.get("path"), str):
            errors.append(f"catalog {name}: source must be a local path")
            continue
        plugin_root = (ROOT / source["path"]).resolve()
        try:
            plugin_root.relative_to(ROOT)
        except ValueError:
            errors.append(f"catalog {name}: source escapes marketplace root")
            continue
        catalog_roots.add(plugin_root)
        if not plugin_root.is_dir():
            errors.append(f"catalog {name}: source path does not exist")
            continue
        policy = entry.get("policy") if isinstance(entry.get("policy"), dict) else {}
        if policy.get("installation") not in VALID_INSTALLATION:
            errors.append(f"catalog {name}: invalid installation policy")
        if policy.get("authentication") not in VALID_AUTHENTICATION:
            errors.append(f"catalog {name}: invalid authentication policy")
        if not entry.get("category"):
            errors.append(f"catalog {name}: category is required")
        skills, agents = validate_plugin(plugin_root, name, seen_agents, errors)
        total_skills += skills
        total_agents += agents

    discovered_roots = {
        manifest.parent.parent.resolve()
        for base in (ROOT / "plugins", ROOT / "vendor")
        if base.is_dir()
        for manifest in base.glob("*/.codex-plugin/plugin.json")
    }
    for root in sorted(discovered_roots - catalog_roots):
        errors.append(f"{root.relative_to(ROOT)}: Codex plugin is missing from catalog")
    for root in sorted(catalog_roots - discovered_roots):
        errors.append(f"{root.relative_to(ROOT)}: catalog entry is missing .codex-plugin/plugin.json")

    if errors:
        print(f"FAILED: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK: {len(entries)} plugins, {total_skills} skills, {total_agents} subagents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
