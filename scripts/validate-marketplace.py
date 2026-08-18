#!/usr/bin/env python3
"""Validate the Codex-native marketplace, plugins, skills, agents, hooks, and MCP configs."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
MAX_SKILL_DESCRIPTION_CHARS = 220
DEFAULT_SKILL_DISCOVERY_BUDGET = 8000
BANNED_NAMES = {
    ".claude-plugin",
    ".cursor-plugin",
    "CLAUDE.md",
    "GEMINI.md",
    "gemini-extension.json",
    "ANTIGRAVITY_GUIDANCE.md",
    "copilot-instructions.md",
}
REQUIRED_AGENT_FIELDS = {
    "name",
    "description",
    "developer_instructions",
    "model",
    "model_reasoning_effort",
    "sandbox_mode",
}
VALID_MODELS = {"gpt-5.6-sol", "gpt-5.6-terra", "gpt-5.6-luna"}
VALID_REASONING = {"low", "medium", "high", "xhigh", "max", "ultra"}
VALID_SANDBOX_MODES = {"read-only", "workspace-write"}
VALID_INSTALLATION = {"NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"}
VALID_AUTHENTICATION = {"ON_INSTALL", "ON_USE"}


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def load_json(path: Path, errors: list[str], *, root: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"{relative(path, root)}: invalid JSON: {error}")
        return {}


def skill_description(frontmatter: str) -> str | None:
    match = re.search(r"^description:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value


def validate_skill(skill_dir: Path, errors: list[str], *, root: Path = DEFAULT_ROOT) -> int:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"{relative(skill_dir, root)}: missing SKILL.md")
        return 0
    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append(f"{relative(skill_file, root)}: missing YAML frontmatter")
        return 0
    frontmatter = match.group(1)
    if not re.search(r"^name:\s*\S", frontmatter, re.MULTILINE):
        errors.append(f"{relative(skill_file, root)}: missing frontmatter name")
    description = skill_description(frontmatter)
    if not description:
        errors.append(f"{relative(skill_file, root)}: missing frontmatter description")
        return 0
    if len(description) > MAX_SKILL_DESCRIPTION_CHARS:
        errors.append(
            f"{relative(skill_file, root)}: description exceeds {MAX_SKILL_DESCRIPTION_CHARS} characters "
            f"({len(description)})"
        )
    return len(description)


def validate_agent(path: Path, seen_names: set[str], errors: list[str], *, root: Path = DEFAULT_ROOT) -> None:
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        errors.append(f"{relative(path, root)}: invalid TOML: {error}")
        return
    missing = sorted(REQUIRED_AGENT_FIELDS - data.keys())
    if missing:
        errors.append(f"{relative(path, root)}: missing {', '.join(missing)}")
    for field in REQUIRED_AGENT_FIELDS - {"sandbox_mode"}:
        if field in data and (not isinstance(data[field], str) or not data[field].strip()):
            errors.append(f"{relative(path, root)}: {field} must be a non-empty string")
    if data.get("model") not in VALID_MODELS:
        errors.append(f"{relative(path, root)}: invalid model {data.get('model')!r}")
    if data.get("model_reasoning_effort") not in VALID_REASONING:
        errors.append(f"{relative(path, root)}: invalid model_reasoning_effort {data.get('model_reasoning_effort')!r}")
    if data.get("sandbox_mode") not in VALID_SANDBOX_MODES:
        errors.append(f"{relative(path, root)}: invalid sandbox_mode {data.get('sandbox_mode')!r}")
    name = data.get("name")
    if isinstance(name, str):
        if name in seen_names:
            errors.append(f"{relative(path, root)}: duplicate agent name {name!r}")
        seen_names.add(name)


def validate_hook_command(command: str, plugin_root: Path, hook_path: Path, errors: list[str], root: Path) -> None:
    label = relative(hook_path, root)
    if "/Users/" in command or re.search(r"(^|\s)~/", command):
        errors.append(f"{label}: hook command must be portable and use ${{PLUGIN_ROOT}}")
    if ("scripts/" in command or "hooks/" in command) and "${PLUGIN_ROOT}" not in command:
        errors.append(f"{label}: plugin-local hook command must use ${{PLUGIN_ROOT}}")
    for match in re.finditer(r"\$\{PLUGIN_ROOT\}/([^\s\"']+)", command):
        referenced = match.group(1).rstrip(";,)")
        if not (plugin_root / referenced).is_file():
            errors.append(f"{label}: referenced hook file does not exist: {referenced}")


def validate_hooks(
    plugin_root: Path,
    hook_reference: object,
    errors: list[str],
    *,
    root: Path = DEFAULT_ROOT,
) -> None:
    references = hook_reference if isinstance(hook_reference, list) else [hook_reference]
    for reference in references:
        if not isinstance(reference, str) or not reference.strip():
            errors.append(f"{relative(plugin_root, root)}: hooks must be a path or list of paths")
            continue
        hook_path = (plugin_root / reference).resolve()
        try:
            hook_path.relative_to(plugin_root.resolve())
        except ValueError:
            errors.append(f"{relative(plugin_root, root)}: hooks path escapes plugin root")
            continue
        data = load_json(hook_path, errors, root=root)
        events = data.get("hooks")
        if not isinstance(events, dict) or not events:
            errors.append(f"{relative(hook_path, root)}: hooks must be a non-empty object")
            continue
        for event, groups in events.items():
            if not isinstance(event, str) or not isinstance(groups, list) or not groups:
                errors.append(f"{relative(hook_path, root)}: each hook event must contain a non-empty list")
                continue
            for group in groups:
                hooks = group.get("hooks") if isinstance(group, dict) else None
                if not isinstance(hooks, list) or not hooks:
                    errors.append(f"{relative(hook_path, root)}: each hook group must contain hooks")
                    continue
                for hook in hooks:
                    if not isinstance(hook, dict) or hook.get("type") != "command":
                        errors.append(f"{relative(hook_path, root)}: only command hooks are supported")
                        continue
                    command = hook.get("command")
                    if not isinstance(command, str) or not command.strip():
                        errors.append(f"{relative(hook_path, root)}: command hook is missing command")
                        continue
                    validate_hook_command(command, plugin_root, hook_path, errors, root)


def validate_selection_evals(path: Path, plugin_names: set[str], errors: list[str], *, root: Path = DEFAULT_ROOT) -> None:
    data = load_json(path, errors, root=root)
    fixtures = data.get("plugins") if isinstance(data.get("plugins"), dict) else {}
    missing = sorted(plugin_names - set(fixtures))
    extra = sorted(set(fixtures) - plugin_names)
    if missing:
        errors.append(f"{relative(path, root)}: missing plugin fixtures: {', '.join(missing)}")
    if extra:
        errors.append(f"{relative(path, root)}: unknown plugin fixtures: {', '.join(extra)}")
    for plugin in sorted(plugin_names & set(fixtures)):
        fixture = fixtures[plugin]
        if not isinstance(fixture, dict):
            errors.append(f"{relative(path, root)}: {plugin} fixture must be an object")
            continue
        for kind in ("direct", "indirect", "negative"):
            prompts = fixture.get(kind)
            if not isinstance(prompts, list) or not prompts or not all(isinstance(prompt, str) and prompt.strip() for prompt in prompts):
                errors.append(f"{relative(path, root)}: {plugin}.{kind} must contain prompts")


def validate_plugin(
    plugin_root: Path,
    catalog_name: str,
    seen_agents: set[str],
    errors: list[str],
    *,
    root: Path,
) -> tuple[int, int, int]:
    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    manifest = load_json(manifest_path, errors, root=root)
    required = ("name", "version", "description", "author", "interface")
    for field in required:
        if not manifest.get(field):
            errors.append(f"{relative(manifest_path, root)}: missing {field}")
    if manifest.get("name") != catalog_name:
        errors.append(f"{relative(manifest_path, root)}: name does not match catalog entry {catalog_name!r}")
    if not SEMVER.fullmatch(str(manifest.get("version", ""))):
        errors.append(f"{relative(manifest_path, root)}: version must be strict semver")
    if not isinstance(manifest.get("author"), dict) or not manifest.get("author", {}).get("name"):
        errors.append(f"{relative(manifest_path, root)}: author.name is required")
    interface = manifest.get("interface") if isinstance(manifest.get("interface"), dict) else {}
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category", "capabilities", "defaultPrompt"):
        if not interface.get(field):
            errors.append(f"{relative(manifest_path, root)}: interface.{field} is required")
    short_description = interface.get("shortDescription")
    if isinstance(short_description, str) and short_description.rstrip().endswith("..."):
        errors.append(f"{relative(manifest_path, root)}: interface.shortDescription must not end with an ellipsis")
    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or len(prompts) < 2 or not all(isinstance(prompt, str) and prompt.strip() for prompt in prompts):
        errors.append(f"{relative(manifest_path, root)}: interface.defaultPrompt must contain at least two starter prompts")
    repository = manifest.get("repository")
    if plugin_root.parent == root / "plugins" and repository and "vincent-laroche/agents-marketplace" not in repository:
        errors.append(f"{relative(manifest_path, root)}: repository must point to agents-marketplace")

    skill_count = 0
    description_chars = 0
    skills_dir = plugin_root / "skills"
    if manifest.get("skills"):
        if not skills_dir.is_dir():
            errors.append(f"{relative(manifest_path, root)}: skills path does not exist")
        else:
            for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
                description_chars += validate_skill(skill_dir, errors, root=root)
                skill_count += 1

    agent_paths = sorted((plugin_root / "agents").glob("*.toml")) if (plugin_root / "agents").is_dir() else []
    for agent_path in agent_paths:
        validate_agent(agent_path, seen_agents, errors, root=root)
    capabilities = interface.get("capabilities", [])
    if agent_paths and "Subagents" not in capabilities:
        errors.append(f"{relative(manifest_path, root)}: agents exist but Subagents capability is missing")
    if (plugin_root / ".codex" / "agents").exists():
        errors.append(f"{relative(plugin_root, root)}: move .codex/agents/*.toml to agents/*.toml")

    hook_reference = manifest.get("hooks")
    default_hook = plugin_root / "hooks" / "hooks.json"
    if hook_reference:
        validate_hooks(plugin_root, hook_reference, errors, root=root)
    elif default_hook.is_file():
        validate_hooks(plugin_root, "./hooks/hooks.json", errors, root=root)

    mcp_reference = manifest.get("mcpServers")
    if mcp_reference:
        if isinstance(mcp_reference, str):
            mcp_path = plugin_root / mcp_reference
            mcp_data = load_json(mcp_path, errors, root=root)
            if not mcp_data.get("mcpServers"):
                errors.append(f"{relative(mcp_path, root)}: mcpServers must be non-empty")
            raw = mcp_path.read_text(encoding="utf-8") if mcp_path.is_file() else ""
            if re.search(r"Bearer\s+(?!\$\{)[A-Za-z0-9._-]{12,}", raw, re.IGNORECASE):
                errors.append(f"{relative(mcp_path, root)}: possible committed bearer token")
        elif not isinstance(mcp_reference, dict):
            errors.append(f"{relative(manifest_path, root)}: mcpServers must be a path or object")
        if "MCP" not in capabilities:
            errors.append(f"{relative(manifest_path, root)}: MCP config exists but MCP capability is missing")

    return skill_count, len(agent_paths), description_chars


def run(root: Path) -> int:
    errors: list[str] = []
    catalog_path = root / ".agents" / "plugins" / "marketplace.json"
    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.name in BANNED_NAMES:
            errors.append(f"{relative(path, root)}: banned non-Codex packaging surface")

    catalog = load_json(catalog_path, errors, root=root)
    if catalog.get("name") != "agents-marketplace":
        errors.append(".agents/plugins/marketplace.json: name must be agents-marketplace")
    entries = catalog.get("plugins") if isinstance(catalog.get("plugins"), list) else []
    catalog_names: set[str] = set()
    catalog_roots: set[Path] = set()
    seen_agents: set[str] = set()
    total_skills = 0
    total_agents = 0
    default_description_chars = 0
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
        plugin_root = (root / source["path"]).resolve()
        try:
            plugin_root.relative_to(root)
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
        skills, agents, chars = validate_plugin(plugin_root, name, seen_agents, errors, root=root)
        total_skills += skills
        total_agents += agents
        if policy.get("installation") == "INSTALLED_BY_DEFAULT":
            default_description_chars += chars

    if default_description_chars > DEFAULT_SKILL_DISCOVERY_BUDGET:
        errors.append(
            f"default-installed skill descriptions use {default_description_chars} characters; "
            f"budget is {DEFAULT_SKILL_DISCOVERY_BUDGET}"
        )
    validate_selection_evals(root / "evals" / "plugin-selection.json", catalog_names, errors, root=root)

    discovered_roots = {
        manifest.parent.parent.resolve()
        for base in (root / "plugins", root / "vendor")
        if base.is_dir()
        for manifest in base.glob("*/.codex-plugin/plugin.json")
    }
    for discovered in sorted(discovered_roots - catalog_roots):
        errors.append(f"{relative(discovered, root)}: Codex plugin is missing from catalog")
    for catalog_root in sorted(catalog_roots - discovered_roots):
        errors.append(f"{relative(catalog_root, root)}: catalog entry is missing .codex-plugin/plugin.json")

    if errors:
        print(f"FAILED: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"OK: {len(entries)} plugins, {total_skills} skills, {total_agents} subagents, "
        f"{default_description_chars}/{DEFAULT_SKILL_DISCOVERY_BUDGET} default discovery characters"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="Marketplace repository root")
    args = parser.parse_args()
    return run(args.root.expanduser().resolve())


if __name__ == "__main__":
    raise SystemExit(main())
