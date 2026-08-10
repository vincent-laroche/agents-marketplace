---
name: coordinating-agent-teams-worktrees
description: Use when deciding between the main worktree, a feature branch, or OpenCode worktree isolation for parallel Agent Teams editing and review.
---

# Coordinating Agent Teams Worktrees

Choose the least complex isolation that prevents concurrent-edit risk.

| Strategy | Best use | Tradeoff |
| --- | --- | --- |
| Main worktree | Solo, docs-only, one editor | Lowest overhead; parallel edits collide. |
| Feature branch | One coherent team change | Clear review target; shared files still collide. |
| OpenCode worktree isolation | Parallel OpenCode editors on one Git repo | Separate diffs/branches; integration discipline required. |

Before starting parallel work, inspect the baseline:

```bash
git status --short
git branch --show-current
```

Use branch names such as `agent/<team-or-task>/<short-purpose>`. Tell agents to preserve unrelated user changes and declare one integration owner when tasks touch the same file.

## Review and merge contract

1. Task result names changed scope and verification.
2. Reviewer examines the worktree/task diff.
3. Unexpected changes receive a task-level fix request.
4. A human or assigned integrator deliberately merges/applies approved work.

Task completion is not merge authorization. Broad generators/formatters require a comment naming the command and rationale.

## Error Handling

Same file: pause one task or assign integration ownership. Dirty main worktree: preserve user changes and review only task-owned changes. Divergent worktree: rebase or merge manually after review, never through an unscoped agent request. Do not enable worktrees for non-Git or read-only tasks; OpenCode is the supported isolation path.
