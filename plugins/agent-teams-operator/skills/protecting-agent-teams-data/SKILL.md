---
name: protecting-agent-teams-data
description: Use when running Agent Teams on a sensitive repository, deciding what context or attachments may be sent to a provider-backed runtime, or setting autonomy and review boundaries for private work.
---

# Protecting Agent Teams Data

Agent Teams is local-first orchestration, not a cloud code-sync service. Its local board, tasks, inboxes, launch state, logs, review metadata, and app settings remain on the machine. Provider-backed model calls may still receive task text, selected source, tool outputs, command errors, diffs, attachments, and surrounding context.

| Location | Typical local data |
| --- | --- |
| `~/.claude/teams/<team>/` | Team config, inboxes, launch/boot evidence, diagnostics, messages, kanban/review files. |
| `~/.claude/tasks/<team>/` | Durable task JSON. |
| `~/.claude/projects/<encoded-project>/` | Available project-session/transcript data. |

## Sensitive-repository gate

1. Remove secrets from working tree, attachments, prompts, comments, and command output.
2. Confirm the selected provider/runtime is allowed for the repository.
3. Use low autonomy, a small team, narrow tasks, and explicit human review.
4. Check the exact prompt/attachments before the agent runs.
5. Keep diagnostic evidence local unless intentionally shared.

Do not rely on Agent Teams to override provider retention, training, billing, regional processing, or runtime logging policies. Do not paste credentials into `.mcp.json`, messages, agent blocks, or task comments. Prefer project-scoped and read-only external MCP credentials.

## Error Handling

If secrets or sensitive data have entered an attachment, comment, prompt, or provider-bound context, stop expansion, assess the provider/runtime exposure path, and follow the affected system's incident process. Do not attempt to hide the issue by editing task history. If safe scope cannot be defined, do not launch the team.
