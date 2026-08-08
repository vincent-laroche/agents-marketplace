---
name: figma-api-selector
description: Selects the correct Figma developer surface and designs single-API or hybrid architectures across the Plugin API, Widget API, REST API, MCP tools, and embeds. Use when a request asks which Figma API to use, compares capabilities, crosses file/runtime boundaries, or risks choosing a read-only or user-present surface for the wrong job. Do not use for implementation that already has a confirmed API boundary unless that boundary must be revalidated.
---

# Select a Figma API

Choose the execution model before choosing endpoints or methods.

## Procedure

1. Identify whether the work runs inside an open Figma editor, persists as an on-canvas multiplayer object, runs outside Figma, or is delegated through an available MCP connector.
2. Identify whether the work must read one open file, edit the open file, read many files, write supported REST resources, or present a persistent collaborative UI.
3. Read [references/api-comparison.md](references/api-comparison.md) when the boundary is not obvious or a hybrid is plausible.
4. Select the smallest sufficient surface:
   - Use the Plugin API for user-triggered, rich read/write access to the current open file.
   - Use the Widget API for persistent, multiplayer on-canvas experiences.
   - Use the REST API for unattended or cross-file work, subject to endpoint-specific write limits.
   - Use an MCP tool when the goal is agent-mediated Figma work and the connector exposes the required operation.
5. Route implementation to `$figma-plugin-development`, `$figma-plugin-api`, or `$figma-rest-api` as appropriate.
6. For hybrids, define the trust boundary, authentication owner, data flow, failure handling, and which surface is authoritative.
7. State limitations explicitly. Do not imply that the Plugin API runs in the background, that REST can edit arbitrary nodes, or that a widget can operate across files.

## Stop conditions

- Stop before selecting a surface if the user-presence requirement or write requirement is unknown and the alternatives would produce materially different products.
- Stop before proposing a public OAuth app, paid plugin, or publication flow if ownership, privacy, or approval requirements are unresolved.
- Never treat MCP availability as proof that the underlying Plugin or REST API capability exists.

## Error Handling

- If requirements map to incompatible surfaces, propose an explicit hybrid instead of pretending one API covers both.
- If connector or entitlement availability is unknown, label the dependency unverified and provide the API-native fallback.

## Output

Report the recommended surface first, then the decisive reason, missing capability if any, authentication model, and any hybrid boundary.
