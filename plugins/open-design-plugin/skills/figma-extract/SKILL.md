---
name: figma-extract
description: "Create a structured, read-only snapshot of a Figma file or selected node tree, including hierarchy, variables/styles, component references, exportable assets, and unsupported features. Use before Figma migrations."
---

# Extract a Figma Snapshot

## Procedure

1. Verify authentication, file URL/key, node scope, and read/write boundary.
2. Extract the node tree with ids, types, parent/child relationships, bounds, fills/strokes, text styles, component references, variants, and prototype-relevant properties.
3. Extract variables, styles, and export settings separately from geometry.
4. Export only explicitly exportable assets, recording format and node id. Do not upload or alter Figma content.
5. Record unsupported node types or unavailable properties instead of omitting them silently.

## Output contract

```text
figma/
├── tree.json
├── tokens.json
├── assets/
└── meta.json
```

`meta.json` must record source file, extraction time, scope, authentication limitations, and unsupported nodes. `tree.json` is the canonical downstream pivot; pass its token inventory to `$token-map` when a target system exists.

## Stop conditions

Stop and report rather than fabricate ids, hierarchy, or editability when authentication, entitlement, or source access fails.
