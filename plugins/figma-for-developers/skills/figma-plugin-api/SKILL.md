---
name: figma-plugin-api
description: "Implement or diagnose the current Figma Plugin API from official TypeScript typings and reference maps. Use for nodes, variables, styles, events, iframe UI, and plugin runtime behavior."
---

# Use the Figma Plugin API

Treat the bundled typings snapshot as the exhaustive local contract and the live official docs as the freshness check.

## Procedure

1. Identify the editor type, plugin mode, target node types, read/write operation, and whether the file uses dynamic page loading.
2. Inspect the installed `@figma/plugin-typings` version and existing `tsconfig.json`; do not assume the bundled snapshot exactly matches the project.
3. Read [references/api-map.md](references/api-map.md) to locate the relevant global or sub-API.
4. Search `references/plugin-api.d.ts` by exact symbol or member name. Prefer the project-installed typings when they are newer.
5. Read [references/nodes-properties-types.md](references/nodes-properties-types.md) before traversing, creating, moving, resizing, styling, editing text, binding variables, or handling editor-specific nodes.
6. Read [references/typings-errors-and-updates.md](references/typings-errors-and-updates.md) when resolving type errors, runtime API errors, deprecations, proposed APIs, or version drift.
7. Narrow node unions with `node.type` or a type guard before accessing node-specific members.
8. Use async alternatives for page loading, node/style lookup, library imports, variables, and other APIs that are async or deprecated synchronously.
9. Load every font used by affected text ranges before changing text or text style properties.
10. Clone and reassign readonly paint/effect/style arrays; capture helper return values that produce new objects.
11. Add null, mixed-value, removed-node, unsupported-editor, and rejected-promise handling.
12. Type-check, build, and run a minimal reproduction in the declared editor type.

## Verification rules

- Confirm a member exists in the current typings before using it.
- Confirm the member belongs to the narrowed node or sub-API, not merely to a related REST model.
- Confirm required manifest permissions/capabilities and editor restrictions.
- Confirm mutations survive a read-back and that created/mutated node IDs are reported for follow-up validation.
- If live docs and bundled typings disagree, treat the installed typings plus observed runtime as decisive and document the drift.

## Error Handling

- On a missing member, verify symbol spelling, node narrowing, package version, editor/mode gating, permissions, and proposed/private status before changing code.
- On a mutation error, confirm font loading, readonly reassignment, numeric ranges, mixed/null values, and whether the node was removed.
- If the current typings are unavailable, use the bundled snapshot but label it as the 2026-08-02 fallback.

For coverage boundaries and canonical index pages, read [references/official-source-map.md](references/official-source-map.md).
