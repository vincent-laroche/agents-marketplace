---
name: token-map
description: "Map an extracted source token inventory onto an approved target design system with explicit role evidence, collisions, and unmatched values. Use during Figma-to-code, code-to-design-system."
---

# Map Tokens Safely

## Procedure

1. Read the source token bag and the approved target system's canonical tokens.
2. Infer a source token's semantic role from usage, component/state labels, hierarchy, contrast pairs, and reuse topology—not color proximity alone.
3. Map only when role and target token both have clear evidence.
4. Put ambiguous, missing, and target-collision cases into `unmatched` with their candidates and reasons.
5. Preserve one-to-many mappings where a source value serves different roles in different contexts.
6. Obtain approval before proposing new semantic tokens or changing existing values.

## Output contract

Produce four reviewable buckets:

```text
token-map/
├── colors.json
├── typography.json
├── spacing.json
└── unmatched.json
```

Every mapped row must include source evidence and target token. Every unmatched row must include a non-empty reason such as `no-target-equivalent`, `ambiguous-role`, or `target-collision`.

## Completion rule

Report mapped, unmatched, and approval-required counts. A non-empty unmatched list is a valid outcome; do not claim a completed migration until a human resolves it.
