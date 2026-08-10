---
name: onboarding-agent-teams
description: Use when starting a first Agent Teams run, choosing a safe starter project, or checking that a small team can produce reviewable work before scaling.
---

# Onboarding Agent Teams

Treat the first run as a proof of control, not a productivity contest. Prove that the project opens, one small team launches, tasks become visible, and a human can review a diff before expanding scope.

## First-run contract

1. Pick a readable Git-tracked project and record its baseline with `git status --short`.
2. Validate one runtime binary and its authentication before launching.
3. Create only Lead, Builder, and Reviewer roles.
4. Give the lead one bounded, verifiable goal.
5. Inspect one task through review before calling the workflow usable.

| Surface | Operating purpose |
| --- | --- |
| Project/team selector | Choose the repository and team responsible for it. |
| Team editor | Set roles, model lanes, instructions, and worktree choice. |
| Task board | Observe Todo, In Progress, Review, Done, and Approved. |
| Task detail/review | Inspect description, logs, attachments, diff, and result comment. |

Use a first goal shaped like this:

```text
Outcome: Improve one documentation path.
Scope: Keep edits in one known folder.
Boundaries: Do not alter runtime or product code.
Verification: Run the relevant docs build.
Review: State changed files and wait for review before approval.
```

Healthy progress is: small tasks, visible plan/progress comments, movement into Review, a task-scoped diff, and a final comment containing the verification command and result.

## Error Handling

Pause rather than add agents when the board fills with vague tasks, verification is absent, unexpected files are touched, or runtime errors recur. Ask the lead to split work and name files plus verification before resuming. If a team does not launch, use `troubleshooting-agent-teams`; if data is sensitive, use `protecting-agent-teams-data` before attaching files or sending the brief.
