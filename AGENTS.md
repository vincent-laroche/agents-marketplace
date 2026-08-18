# agents-marketplace — Codex operating contract

This repository is Vincent Laroche's Codex-native marketplace for Hair Solutions Co. It packages reusable skills, specialized subagents, MCP servers, and deterministic local tools for Codex.

Repository: `https://github.com/vincent-laroche/agents-marketplace`

## Codex-only boundary

- `.agents/plugins/marketplace.json` is the marketplace catalog and source of truth.
- Every registered plugin must have `.codex-plugin/plugin.json`.
- Skills live under `skills/<skill-name>/SKILL.md`.
- Discoverable subagents live directly under `agents/*.toml`, never `.codex/agents/`.
- MCP servers live in a credential-free `.mcp.json` and are referenced by the plugin manifest.
- This repo does not ship Claude, Cursor, Gemini, Antigravity, or Copilot manifests, commands, agents, installers, or compatibility generators.
- `agents/openai.yaml` inside a skill is Codex skill-interface metadata and is valid here.

## Subagent contract

Every `agents/*.toml` file must include:

- `name`
- `description`
- `developer_instructions`
- `sandbox_mode` set to `read-only` or `workspace-write`
- `model_reasoning_effort` when the role benefits from an explicit reasoning level

Agent instructions must state the role's scope, write boundary, required evidence, forbidden actions, and handoff format. Read-only reviewers must not edit, delegate, commit, push, publish, or mutate external systems.

## Plugin contract

Every `.codex-plugin/plugin.json` must include real values for `name`, `version`, `description`, `author.name`, and all required `interface` fields. Use strict semver. Repository URLs must point to `vincent-laroche/agents-marketplace`.

The marketplace catalog and plugin folders must agree exactly. A plugin with agents should list `Subagents` in `interface.capabilities`; a plugin with `.mcp.json` should declare `mcpServers` and list `MCP`.

Native Codex hooks may live at `hooks/hooks.json` or be referenced by the manifest. Hook commands must be credential-free, portable, use `${PLUGIN_ROOT}` for plugin-local files, and pass the marketplace validator. Never restore old Claude hook formats or compatibility shims. Users still decide whether to trust installed hooks.

## Secrets

Credentials live only in `/Users/vMac/.env`. Never print, log, commit, or paste secret values. Committed MCP configs must contain no bearer tokens or inline credentials. Prefer OAuth endpoints or environment-variable placeholders.

## Validation

After any catalog, manifest, skill, agent, or MCP change, run:

```bash
python3 scripts/validate-marketplace.py
```

After changing subagents, synchronize and verify the active Codex profile:

```bash
python3 scripts/install-subagents.py --apply
python3 scripts/install-subagents.py --check
```

For every changed plugin, also run the official validator:

```bash
python3 /Users/vMac/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/<plugin-name>
```

Use the cachebuster helper before reinstalling an updated plugin:

```bash
python3 /Users/vMac/.codex/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py plugins/<plugin-name>
```

## Working rules

- Read before editing and preserve unrelated work.
- Use the smallest reversible change.
- Never edit `vendor/` in place; replace or fork a vendored package deliberately.
- Do not copy brand systems or other external authorities into this repo. Plugins point to their canonical source.
- Before committing, inspect `git diff --cached --stat` and include only task-owned files.
- Update `PROJECT.md` after meaningful work.
- Completed repository changes are committed and pushed to `main` unless Vincent explicitly asks otherwise.
