---
name: writing-agent-teams-briefs
description: Use when turning a business or engineering goal into an Agent Teams launch brief, task plan, agent-only instruction block, or intervention message with clear scope and verification.
---

# Writing Agent Teams Briefs

A brief must let the lead create small, testable tasks without giving it permission to broaden the work. Write the contract before launch.

```text
Outcome: [observable result]
Scope: [allowed files, feature, or surface]
Boundaries: [what must not change]
Coordination: [task split, comments, handoffs]
Verification: [focused command or manual evidence]
Review: [acceptance owner and required result summary]
```

## Examples by risk

| Situation | Required boundary |
| --- | --- |
| Docs/content | Name the doc folder and build command; preserve navigation owned elsewhere. |
| Feature work | Name the feature area; forbid storage/review-semantics changes unless explicit. |
| Investigation | Request evidence first; do not modify code until cause is established. |
| High-risk paths | Start from artifacts/logs; require a diagnostic task, focused tests, and lead review. |

Use task comments for plans, blockers, changed scope, review findings, and verification because they remain attached to the work. Use direct messages only to redirect a person or coordinate the lead.

Use `<info_for_agent>...</info_for_agent>` only for concise hidden coordination instructions, such as an explicit task split. Do not place secrets, customer data, or decisions the human reviewer must see in an agent block.

## Intervention templates

```text
Split this into independently reviewable tasks. For each, post allowed files and the verification command before editing.
```

```text
Pause new work. Clear the existing review queue and report unexpected files before creating more tasks.
```

## Error Handling

If the brief is broad, launch a solo/small planning task rather than a broad implementation team. If the task depends on a tool or runtime, verify setup first with `integrating-agent-teams-mcp` or `configuring-agent-teams-runtimes`. Escalate sensitive repositories to `protecting-agent-teams-data` before attaching context.
