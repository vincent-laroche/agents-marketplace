---
name: designing-agent-teams-teams
description: Use when creating an Agent Teams team, assigning lead/builder/reviewer roles, selecting per-member models, autonomy, effort, fast mode, context limits, or worktree isolation.
---

# Designing Agent Teams Teams

Design for a reviewable flow before optimizing for parallelism. A team is a project-bound group of agents with a lead, member instructions, provider/model settings, local state, tasks, and inboxes.

## Default team shape

| Role | Owns | Instruction focus |
| --- | --- | --- |
| Lead | Task decomposition, assignment, blockers, review queue | Small tasks, visible status, no broad refactors. |
| Builder | Narrow implementation | Assigned scope only; report files and verification. |
| Reviewer | Regression/scope check | Specific review rubric and concrete fix requests. |

Use short responsibility-based member prompts; put project-wide outcome and boundaries in the team brief. Select the most reliable lane for the lead. Use Medium effort by default, Low only for routine lookups/formatting, High for cross-cutting/risky paths. Fast mode trades depth for speed; leave it off for careful work. Limit context only where the task does not need extended context.

## Isolation decision

Enable OpenCode worktree isolation only when multiple teammates may edit the same Git repository and their changes benefit from separate branches/diffs. Keep it off for a UI-only test, non-Git project, a single editor, or a read-only task.

## Error Handling

If a required provider/model is unavailable, use `configuring-agent-teams-runtimes` before changing the team. If tasks overlap, pause one owner or make one integration owner. For risky data, auth, IPC, persistence, Git, or release work, lower autonomy and require explicit human review.
