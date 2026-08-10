---
name: integrating-agent-teams-mcp
description: Use when configuring Agent Teams board MCP tools, adding project or user scoped external MCP servers, installing a custom server, or extending the built-in Agent Teams MCP server.
---

# Integrating Agent Teams MCP

Keep two MCP layers distinct: the app-injected `agent-teams` server controls board coordination; external servers provide optional domain tools.

| Layer | Purpose | Scope choice |
| --- | --- | --- |
| Built-in `agent-teams` | Tasks, messages, reviews, processes, runtime/cross-team operations | App-owned temporary launch config. |
| External MCP | Browser, design, docs, internal systems, read-only inspection | Project when repo-specific; user when truly reusable. |

For task work, use built-in tools in a durable sequence: retrieve task → start → work/verify → add plan/result comments → complete → message stakeholders. Common tools include `task_get`, `task_start`, `task_add_comment`, `task_complete`, `message_send`, review tools, and `process_register/list/stop/unregister`.

For an external server, choose the narrowest scope; keep secrets out of committed `.mcp.json`; run diagnostics; prove its tool surface with one read-only task; then name required tool use, write boundary, and verification in the task.

When extending Agent Teams itself, add a FastMCP implementation in `mcp-server/src/tools/`, list it in `agent-teams-controller/src/mcpToolCatalog.js`, use Zod validation, call the controller API, and add focused tool/transport tests. Never bypass controller validation or grant broad filesystem/process access for convenience.

## Error Handling

MCP diagnostic failure is a setup issue, not an agent issue—fix command, config path, auth, headers, or scope before retrying. Do not edit app-generated `agent-teams-mcp-*.json` launch artifacts. Keep production-mutating tools out of broad teams and behind explicit task comments/review.
