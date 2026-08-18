---
name: design-extract
description: "Extract an evidence-backed source token inventory from code, Figma exports, or screenshots before a redesign or migration. Use when colors, typography, spacing, radii, shadows."
---

# Extract Design Evidence

## Procedure

1. Confirm target root, source type, and whether read-only extraction is required.
2. Inspect stylesheets, theme settings, Tailwind/config files, component code, Figma variables/styles, and supplied screenshots as applicable.
3. Create a token bag grouped as `color`, `typography`, `spacing`, `radius`, and `shadow`.
4. Give every entry its source location, raw value, source name when available, usage locations, and confidence (`measured`, `declared`, or `inferred`).
5. Preserve inline values as candidates with synthetic names rather than silently dropping them.
6. Deduplicate only true duplicates; retain distinct values that have distinct semantic roles.

## Output contract

Write or report a portable JSON inventory with this shape:

```json
{
  "tokens": [{
    "kind": "color",
    "name": "primary-500",
    "value": "#5b8def",
    "sources": ["assets/theme.css:42"],
    "usage": ["components/Button.tsx"],
    "confidence": "declared"
  }],
  "unresolved": []
}
```

Do not modify the source system. Route the inventory to `$token-map` only after the receiving system is identified.
