---
name: reviewing-agent-teams-changes
description: Use when reviewing Agent Teams task results, task-scoped diffs, hunk decisions, verification evidence, review-state transitions, or requests for changes before approval.
---

# Reviewing Agent Teams Changes

Completion is an agent claim; approval is a review decision. Review task-scoped changes in this order:

1. Read task goal, owner, status, and final result comment.
2. Confirm changed files are in scope.
3. Inspect logs for actual verification and relevant coordination.
4. Review every changed file and hunk against the task.
5. Keep correct narrow hunks; reject risky or unrelated hunks.
6. Approve only when scope, evidence, diff, and risk level agree.

| Review outcome | Action |
| --- | --- |
| Correct scoped change | Accept hunk and continue review. |
| Good intent, wrong scope/file | Reject that hunk; request a narrower follow-up. |
| Unclear behavior | Comment with the needed evidence. |
| Formatting churn | Reject unless formatting was in scope. |

Use an explicit task comment for requested fixes:

```text
Keep [correct portion]. Revert [unexpected portion]. Run [verification] and post the result before resubmitting.
```

Comments do not transition the board. The appropriate tool must do it: `review_request_changes` moves the task to `needsFix`; `review_approve` moves it to `approved`. Do not use Accept All before reading the full changed-file list.

## Error Handling

If logs and the final comment conflict, request clarification rather than approving. If verification is missing, require it unless the task documents a concrete reason and manual evidence. For auth, IPC, filesystem, persistence, Git, parsing, lifecycle, and release changes, use a focused review rubric and require targeted tests; use `coordinating-agent-teams-worktrees` for isolated-branch work.
