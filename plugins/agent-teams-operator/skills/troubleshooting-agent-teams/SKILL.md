---
name: troubleshooting-agent-teams
description: Use when an Agent Teams launch hangs, a runtime is unconfirmed, replies or task logs are missing, changes are detached, auth fails, or a provider is rate-limited.
---

# Troubleshooting Agent Teams

Evidence first: correlate the UI with persisted team, task, and runtime artifacts before changing prompts, models, or processes.

```bash
TEAM="<team-name>"
TEAM_DIR="$HOME/.claude/teams/$TEAM"
TASKS_DIR="$HOME/.claude/tasks/$TEAM"
test -d "$TEAM_DIR" && find "$TEAM_DIR" -maxdepth 2 -type f | sort | sed -n '1,80p'
test -d "$TASKS_DIR" && find "$TASKS_DIR" -maxdepth 1 -name '*.json' | sort | sed -n '1,40p'
```

## Diagnostic order

1. Runtime binary, PATH, provider auth, exact model ID, readable project path, network/VPN.
2. `launch-state.json`, `bootstrap-state.json`, `bootstrap-journal.jsonl`, `config.json`, inboxes, and sent messages.
3. Newest `launch-failure-artifacts/latest.json`, then its manifest: classification, bootstrap breadcrumb, spawn statuses, redacted logs.
4. For OpenCode: lane index, each lane manifest `activeRunId`/entries, and `opencode-sessions.json`.
5. For task attribution: search task ID across task JSON, inboxes, journal, and lane evidence.

| Evidence | Proves | Does not prove |
| --- | --- | --- |
| Delivered message | Prompt was relayed | Agent progressed. |
| Task comment | Board text was posted | Work is correct. |
| Native tool rows | Runtime session worked | It belongs to this task. |
| Change ledger | Files changed | Implementation is acceptable. |

OpenCode `registered` or `runtime_pending_bootstrap` is not readiness. Look for committed lane/session evidence plus `bootstrapConfirmed`; an empty manifest entry list is an evidence-commit problem.

## Error Handling

Never kill all shared OpenCode hosts or tmux panes. Identify a PID/lane/team owned by the smoke run and stop only that. Rate limits: wait for a known reset or lower concurrency/switch lane. Terminal login vs app mismatch: compare home/PATH and inspect the auth diagnostic log. Use a small disposable Git project for a live smoke, not a real customer project.
