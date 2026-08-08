# Figma developer surface comparison

Source: [Figma's official API comparison](https://developers.figma.com/compare-apis/), audited 2026-08-02.

| Surface | Runs where | User present | File reach | Write model | Best fit |
|---|---|---:|---|---|---|
| Plugin API | Open Figma editor file | Yes | Current file; imported library assets | Rich current-file edits | Interactive tools, generators, linters, imports, codegen |
| Widget API | Persistent canvas node in Design/FigJam | For interaction | Current file/widget instance | Widget state and supported canvas behavior | Multiplayer voting, templates, persistent annotations |
| REST API | Script, backend, CI, external app | No | One or many accessible files | Mostly read-only; documented resource writes only | Cross-file sync, audits, exports, webhooks, integrations |
| MCP connector | Agent tool surface | Depends on connector | Whatever its tools expose | Tool-specific | Agent-mediated inspection or edits without authoring a product |
| Embed/oEmbed | External product UI | No editor session required | Published/shared resource | Presentation, not general editing | Showing Figma content in another product |

## Decision sequence

1. If the experience must persist visibly on the canvas and support multiplayer interaction, use a widget.
2. If it must edit the open file while a user invokes it, use a plugin.
3. If it must run unattended, on a schedule, in CI, or across files, use REST.
4. If the task is performed by an agent and an installed connector already exposes the exact action, use MCP rather than building a new product.
5. If requirements span these boundaries, use a hybrid and assign one owner to each responsibility.

## Common hybrids

- Plugin + backend: plugin owns current-file interaction; backend owns secrets, OAuth exchanges, durable jobs, and third-party APIs.
- Plugin + REST: plugin edits the open file; REST reads other files or library metadata. Never ship a broad long-lived token inside plugin assets.
- Widget + REST: widget owns persistent collaboration; a manually refreshed external service supplies remote data.
- MCP + REST: MCP handles interactive agent work; REST handles deterministic cross-file verification or scheduled collection.

## Hard limitations

- Plugins are user-triggered and cannot run as background daemons.
- Plugins and widgets do not automatically gain cross-file access.
- REST does not provide arbitrary write access to visual nodes.
- An MCP connector is not identical to the public API and may expose a narrower, broader, or differently authorized tool surface.
