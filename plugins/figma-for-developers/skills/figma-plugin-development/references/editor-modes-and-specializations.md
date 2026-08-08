# Editor modes and specialized plugins

## Manifest routing

Declare only the editors the plugin supports: `figma`, `figjam`, `dev`, `slides`, and `buzz`. At runtime branch on `figma.editorType` and, when relevant, `figma.mode`.

## Design

- Full read/write Plugin API access is centered on the current open design file.
- Use Design for components, instances, styles, variables, prototyping, and general visual nodes.

## FigJam

- Use FigJam-specific nodes and APIs for stickies, connectors, shapes with text, stamps, embeds, media, code blocks, and timer workflows.
- Components/styles differ from Design. Check the exact typings before creating or mutating a node.
- Do not assume a Design-only node can be created in FigJam even if it can be inspected there.

## Dev Mode

- Dev Mode plugins are read-oriented and operate through inspect, codegen, and related modes.
- Document access is deliberately limited compared with ordinary Design plugins.
- Codegen plugins register the codegen event and return one or more language-labelled code sections.
- Declare required capabilities and `codegenLanguages`; declare codegen preferences when supporting scale, units, or framework choices.
- Account for responsive iframe behavior and the optional VS Code host.

## Slides

- Support Slides explicitly and handle `SLIDE`, `SLIDE_ROW`, `SLIDE_GRID`, and `INTERACTIVE_SLIDE_ELEMENT` where applicable.
- Slides has grid and focused-slide concepts and editor-specific transition behavior.
- Do not assume every Design or FigJam API exists in Slides.

## Buzz

- Support Buzz explicitly and use focused-node access plus Buzz media/text field APIs as documented.
- Respect unsupported features and node restrictions rather than falling back to broad document traversal.

## Text review

- Declare the `textreview` capability and handle the text review event contract.
- Return review ranges and suggestions in the required structure; do not mutate text unless the selected workflow explicitly calls for it.

## Parameters and relaunch

- Use `parameters` for quick-action inputs. Keys are stable identifiers passed in `ParameterValues`.
- Use `parameterOnly` when the plugin should never launch without parameter entry.
- Use `relaunchButtons` plus `node.setRelaunchData()` to attach repeatable commands to nodes. Keep command names in sync with manifest menu handling.

Official pages: [Editor type](https://developers.figma.com/docs/plugins/setting-editor-type/), [FigJam](https://developers.figma.com/docs/plugins/working-in-figjam/), [Dev Mode](https://developers.figma.com/docs/plugins/working-in-dev-mode/), [Codegen](https://developers.figma.com/docs/plugins/codegen-plugins/), [Slides](https://developers.figma.com/docs/plugins/working-in-slides/), [Buzz](https://developers.figma.com/docs/plugins/working-in-buzz/), [Text review](https://developers.figma.com/docs/plugins/textreview-plugins/), [Parameters](https://developers.figma.com/docs/plugins/plugin-parameters/).
