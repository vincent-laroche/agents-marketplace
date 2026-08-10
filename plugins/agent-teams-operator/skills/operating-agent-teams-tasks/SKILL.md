---
name: operating-agent-teams-tasks
description: Use when monitoring the Agent Teams kanban board, managing task state, assigning/reassigning work, posting durable task comments, resolving blockers, or interpreting task logs.
---

# Operating Agent Teams Tasks

Operate from the board, task detail, and task-scoped evidence—not from a broad session transcript alone. Work status and review state are independent.

| Dimension | States |
| --- | --- |
| Work | `pending` → `in_progress` → `completed` |
| Review | `none` → `review` → `needsFix` → `approved` |

## Agent task protocol

```text
task_get → task_start → work and verify → task_add_comment → task_complete → message_send
```

An agent starts only when work begins, adds task comments for plan/blocker/result, and completes only after posting the final result. A comment preserves task history; a direct message is for coordination.

## Board operating loop

1. Scan Todo for ambiguous tasks and blocked dependencies.
2. Scan In Progress for duplicate owners, long-running work, or missing updates.
3. Open Review/Done tasks and compare description, expected files, result comment, logs, and diff.
4. Stop or pause the team when review backlog exceeds human capacity, scope drifts, or runtime failures repeat.

Task logs should establish owner, task reference, runtime activity, changed files, and verification. Native runtime tool rows show session work but do not alone prove correct task attribution.

## Error Handling

If a task is detached from its diff, verify ownership, `task_start`, comments, task ID/reference, and session bounds. If a task is blocked, request the smallest next action with the exact file/command. If the board says a lane is stuck, use `troubleshooting-agent-teams` and persisted evidence before manipulating process state.
