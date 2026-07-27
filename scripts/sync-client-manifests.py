#!/usr/bin/env python3
"""Generate native Codex, Cursor, and Gemini metadata from the Claude catalog."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAUDE_MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
CODEX_MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
CURSOR_MARKETPLACE = ROOT / ".cursor-plugin" / "marketplace.json"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def category_for(name: str) -> str:
    if name.startswith("shopify") or name == "chrome-devtools-mcp":
        return "Developer Tools"
    if name in {"marketing-content", "analytics-ads", "ai-video", "atelier-zero-design-system"}:
        return "Marketing"
    return "Productivity"


def component_metadata(plugin_root: Path) -> dict:
    components: dict[str, object] = {}
    if (plugin_root / "skills").is_dir():
        components["skills"] = "./skills/"
    if (plugin_root / "commands").is_dir():
        components["commands"] = "./commands/"
    if (plugin_root / "agents").is_dir():
        components["agents"] = "./agents/"
    if (plugin_root / "hooks" / "hooks.json").is_file():
        components["hooks"] = "./hooks/hooks.json"

    mcp_path = plugin_root / ".mcp.json"
    if mcp_path.is_file() and read_json(mcp_path).get("mcpServers"):
        components["mcpServers"] = "./.mcp.json"
    return components


def build_cursor_manifest(source: dict, plugin_root: Path) -> dict:
    manifest = {
        key: source[key]
        for key in (
            "name",
            "version",
            "description",
            "author",
            "homepage",
            "repository",
            "license",
            "keywords",
        )
        if source.get(key) is not None
    }
    manifest.update(component_metadata(plugin_root))
    return manifest


def build_codex_manifest(source: dict, plugin_root: Path) -> dict:
    description = source["description"]
    short_description = description if len(description) <= 120 else description[:117].rstrip() + "..."
    manifest = {
        "name": source["name"],
        "version": source["version"],
        "description": description,
        "author": source.get("author", {"name": "Hair Solutions Co."}),
        "homepage": source.get("homepage", "https://hairsolutions.co"),
        "repository": source.get(
            "repository",
            f"https://github.com/vincent-laroche/hairsolutionsco-ai-toolkit/tree/main/plugins/{source['name']}",
        ),
        "license": source.get("license", "Proprietary"),
        "keywords": source.get("keywords", []),
    }
    if (plugin_root / "skills").is_dir():
        manifest["skills"] = "./skills/"
    if (plugin_root / ".app.json").is_file():
        manifest["apps"] = "./.app.json"
    mcp_path = plugin_root / ".mcp.json"
    if mcp_path.is_file() and read_json(mcp_path).get("mcpServers"):
        manifest["mcpServers"] = "./.mcp.json"
    manifest["interface"] = {
        "displayName": source["name"].replace("-", " ").title(),
        "shortDescription": short_description,
        "longDescription": description,
        "developerName": source.get("author", {}).get("name", "Hair Solutions Co."),
        "category": category_for(source["name"]),
        "capabilities": [
            label
            for key, label in (
                ("skills", "Skills"),
                ("apps", "Apps"),
                ("mcpServers", "MCP"),
            )
            if key in manifest
        ],
        "defaultPrompt": [f"Use {source['name']} for this task."],
    }
    return manifest


def build_gemini_manifest(source: dict, plugin_root: Path) -> dict:
    manifest = {
        "name": source["name"],
        "version": source["version"],
    }
    mcp_path = plugin_root / ".mcp.json"
    if mcp_path.is_file():
        servers = read_json(mcp_path).get("mcpServers", {})
        if servers:
            manifest["mcpServers"] = servers
    return manifest


def main() -> None:
    claude = read_json(CLAUDE_MARKETPLACE)
    cursor_plugins = []
    codex_plugins = []

    for entry in claude["plugins"]:
        plugin_root = ROOT / entry["source"]
        source = read_json(plugin_root / ".claude-plugin" / "plugin.json")
        if source["name"] != entry["name"]:
            raise ValueError(f"Plugin name mismatch for {plugin_root}")

        write_json(plugin_root / ".cursor-plugin" / "plugin.json", build_cursor_manifest(source, plugin_root))
        write_json(plugin_root / ".codex-plugin" / "plugin.json", build_codex_manifest(source, plugin_root))
        write_json(plugin_root / "gemini-extension.json", build_gemini_manifest(source, plugin_root))

        cursor_plugins.append(
            {
                "name": source["name"],
                "source": entry["source"],
                "description": source["description"],
                "version": source["version"],
                "author": source.get("author", {"name": "Hair Solutions Co."}),
                "category": category_for(source["name"]),
            }
        )
        codex_plugins.append(
            {
                "name": source["name"],
                "source": {
                    "source": "local",
                    "path": entry["source"],
                },
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                },
                "category": category_for(source["name"]),
            }
        )

    write_json(
        CURSOR_MARKETPLACE,
        {
            "name": claude["name"],
            "owner": claude["owner"],
            "metadata": claude.get("metadata", {}),
            "plugins": cursor_plugins,
        },
    )
    write_json(
        CODEX_MARKETPLACE,
        {
            "name": claude["name"],
            "interface": {"displayName": "Hair Solutions Co. AI Toolkit"},
            "plugins": codex_plugins,
        },
    )


if __name__ == "__main__":
    main()
