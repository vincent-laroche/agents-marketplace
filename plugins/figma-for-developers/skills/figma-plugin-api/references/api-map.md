# Plugin API map

Use `rg -n "^interface SYMBOL|MEMBER" references/plugin-api.d.ts` from the skill directory. The bundled file is an official `figma/plugin-typings` snapshot fetched 2026-08-02; prefer a newer project-installed copy when present.

## Global values

- `figma`: `PluginAPI`, the primary editor surface.
- `__html__`: bundled single UI file contents.
- `__uiFiles__`: named UI-file map when `manifest.ui` is an object.

## `PluginAPI` areas

- Identity/context: `apiVersion`, `command`, `editorType`, `mode`, `pluginId`, `fileKey`.
- Document: `root`, `currentPage`, selection events, async node/style lookup, page switching.
- Creation: frames, components, shapes, text, sections, pages, images, SVG/JSX nodes, FigJam/Slides/Buzz-specific nodes.
- Libraries: component/style imports and `teamLibrary`.
- Lifecycle: events, undo, version history, notifications, external URLs, close.
- Resources: fonts, images, video, SVG, export, variables, styles.

## Sub-APIs

- `figma.ui` → `UIAPI`
- `figma.clientStorage` → `ClientStorageAPI`
- `figma.viewport` → `ViewportAPI`
- `figma.variables` → `VariablesAPI`
- `figma.teamLibrary` → `TeamLibraryAPI`
- `figma.codegen` → `CodegenAPI`
- `figma.textreview` → `TextReviewAPI`
- `figma.parameters` → `ParametersAPI`
- `figma.payments` → `PaymentsAPI`
- `figma.timer` → `TimerAPI`
- `figma.annotations` → `AnnotationsAPI`
- `figma.buzz` → `BuzzAPI`
- `figma.motion` → `MotionAPI`
- `figma.constants` → `ConstantsAPI`
- `figma.util` → `UtilAPI`

## Search patterns

```sh
rg -n '^interface PluginAPI|^interface VariablesAPI' references/plugin-api.d.ts
rg -n '^interface (FrameNode|TextNode|InstanceNode)' references/plugin-api.d.ts
rg -n '^interface .*Mixin' references/plugin-api.d.ts
rg -n 'memberName\(' references/plugin-api.d.ts
rg -n '@deprecated|enableProposedApi|Note: This API is only available' references/plugin-api.d.ts
```

Use the live [Global Objects](https://developers.figma.com/docs/plugins/api/global-objects/), [Node Types](https://developers.figma.com/docs/plugins/api/nodes/), [Shared Node Properties](https://developers.figma.com/docs/plugins/api/node-properties/), and [Data Types](https://developers.figma.com/docs/plugins/api/data-types/) indexes when freshness matters.
