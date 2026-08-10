---
name: developing-agent-teams
description: Use when changing the Agent Teams application itself, extending its feature or MCP architecture, validating a contributor change, or preparing a release-aware review.
---

# Developing Agent Teams

Use the Electron desktop app as the development target: `pnpm dev`. Browser mode is not equivalent because it lacks desktop IPC, terminal/runtime auth, and team lifecycle behavior.

## Architectural boundaries

| Concern | Expected home |
| --- | --- |
| Medium/large feature | `src/features/<feature-name>/` |
| Main-process orchestration | `src/main/` |
| Safe renderer bridge | `src/preload/` |
| UI/application state | `src/renderer/` |
| Shared types/pure helpers | `src/shared/` |
| Built-in board MCP server | `mcp-server/` |
| Board data controller | `agent-teams-controller/` |

Start from the relevant canonical source: root `AGENTS.md`, `CLAUDE.md`, hard guardrails, feature architecture standard, and launch-debugging runbook. Keep main, preload, renderer, shared, and feature responsibilities separate; avoid deep cross-feature imports. Use `wrapAgentBlock(text)` rather than hand-built markers.

## Verification selection

| Change | Evidence |
| --- | --- |
| Docs | `pnpm --dir landing docs:build` and `git diff --check -- landing/product-docs` |
| Focused team behavior | Relevant unit/e2e test then `pnpm typecheck` |
| Lifecycle/runtime | Desktop smoke in a disposable Git project with narrow cleanup |

Avoid broad formatters or `lint:fix` unless formatting is the assigned change. Treat parsing, lifecycle, provider detection, persistence, IPC, Git, and review as high-risk and require focused tests/evidence.

## Error Handling

For launch hangs, missing replies, or OpenCode bootstrap issues, invoke `troubleshooting-agent-teams` and inspect artifact packs before edits. Never test live team behavior on a real user project without fresh permission. Do not convert a runtime setup failure into a code change until persisted evidence identifies a product defect.
