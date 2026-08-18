---
name: higgsfield-mcp-cli
description: "Install, authenticate, inspect, and safely use Higgsfield's official MCP and CLI interfaces for AI agents. Use for Higgsfield MCP, mcp.higgsfield.ai, Higgsfield CLI, @higgsfield/cli, agent integrations."
---

# Higgsfield MCP and CLI

Read `../../references/production-contract.md` and `../../references/official-source-map.md` first. Use only the official connector URL, current CLI documentation, and visible OAuth flow; never invent an API key, scrape a private endpoint, or replay browser traffic.

## Official connection paths

- **MCP:** the official page currently publishes `https://mcp.higgsfield.ai/mcp`. Authenticate through the supported account flow; the official guidance says no API key is required for this connection.
- **CLI:** verify the latest instructions in the official CLI page/repository before installing. The current official page lists `npm i -g @higgsfield/cli`, then `higgsfield auth login`, and a separate companion-skills installation. Treat these as current-source commands to recheck, not durable shell assumptions.

## Connection workflow

1. Inspect whether an existing Higgsfield installation or MCP server already exists. Reuse it rather than adding a duplicate.
2. Install or update only from the official source after Vincent authorizes the local machine change.
3. Complete browser OAuth without exposing tokens or copying credentials into project files.
4. Run a read-only command such as help, version, model/preset listing, or authenticated account-status equivalent before any generation.
5. Inspect the live tool/CLI schema for the requested job. Model aliases, arguments, formats, and supported controls can change.
6. Resolve the model through `../higgsfield-model-selector`, then apply the shared authorization and review contract before `generate create`, a workflow run, training, download, or any publish command.

## CLI conventions

Use `--wait` only when a bounded interactive task needs the completed result; otherwise retain the job identifier and poll via documented status commands. Prefer machine-readable output when a later step needs structured handoff. Treat URLs and generated download locations as sensitive account-bound material; do not commit them.

For model comparisons, send the same brief and protected inputs through each candidate, then compare against one rubric. Use the matching model skill for creative direction. This skill owns connection, command discovery, authentication, structured execution, and job retrieval.
