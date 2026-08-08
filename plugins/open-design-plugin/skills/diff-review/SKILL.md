---
name: diff-review
description: Prepare a human-reviewable, scope-bounded diff and capture an explicit accept, reject, or partial decision before handoff. Use after implementation, migration, or generated edits when a user must retain control over what ships. Do not assume acceptance or roll back files outside the agreed change boundary.
---

# Review a Change Set

## Procedure

1. Confirm the planned file boundary and compare the current working tree with the agreed baseline.
2. Produce a unified diff and a concise per-file explanation of intent, user effect, risk, and validation status.
3. Identify out-of-scope changes separately; do not bundle them into the decision.
4. Ask for or record an explicit `accept`, `reject`, or `partial` decision.
5. For `partial`, list accepted and rejected files or hunks precisely.
6. Never revert, commit, push, deploy, or publish solely because a diff was generated.

## Output contract

```text
review/
├── diff.patch
├── summary.md
├── decision.json
└── meta.json
```

State any unreviewed or unvalidated changes before handoff. A review is complete only when the decision is explicit.
