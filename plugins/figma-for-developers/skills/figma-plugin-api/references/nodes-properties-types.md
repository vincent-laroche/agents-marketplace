# Nodes, shared properties, and data types

## Tree model

`DocumentNode` contains `PageNode` children. Pages contain `SceneNode` trees. `BaseNode` and `SceneNode` are unions; narrow by `type` before node-specific access.

Core families include containers (`FRAME`, `GROUP`, `SECTION`), shapes/vectors, text, components/sets/instances, tables, slices, FigJam nodes, Slides nodes, Buzz nodes, widgets, media, and embedded/resource nodes. Availability and mutability vary by editor.

## Mixin model

Node interfaces compose shared behavior through mixins. Search the typings for:

- `BaseNodeMixin`: identity, parent, remove, relaunch, plugin data.
- `ChildrenMixin`: child access, append/insert, traversal.
- `SceneNodeMixin`: visibility, lock, opacity, variable modes, motion.
- `LayoutMixin`: position, bounds, transforms, resize/rescale.
- `AutoLayoutMixin` and grid mixins: layout mode, sizing, alignment, spacing, padding, tracks.
- `GeometryMixin`: fills, strokes, weights, caps, joins.
- `BlendMixin`: opacity, blend mode, effects, masks.
- `CornerMixin`: radii and smoothing.
- `ExportMixin`: settings and async export.
- `PluginDataMixin`: private/shared plugin data.
- component, variant, prototyping, reaction, publishable, and text mixins.

## Mutation rules

- Width and height are generally readonly; call `resize()` or `rescale()`.
- Many arrays and composite values are readonly snapshots. Clone, modify, and reassign fills, strokes, effects, grids, and similar properties.
- Append a child before assigning child auto-layout sizing properties that depend on its parent.
- Use async page switching/loading under dynamic page access.
- Treat removed node handles as invalid and handle `null` from lookup APIs.
- Avoid root-wide scans. Scope traversal to a known page or ancestor and use criteria-based lookup where supported.

## Text

- Load every font used by the affected range before changing characters or text properties.
- A selection can produce `figma.mixed`; handle it instead of casting.
- Use range APIs or styled text segments for mixed formatting.
- Distinguish missing fonts from fonts that are available but not loaded.

## Components and instances

- Components and component sets are publishable sources; instances reference component structure and expose overrides/properties.
- Capture the key returned by component-property creation helpers; do not guess generated property keys.
- Use import-by-key async methods for library assets that are not already in the file.
- Confirm whether an operation is valid on a component, component set, instance, or detached node.

## Variables and styles

- Variables support collections, modes, aliases, scopes, code syntax, bound variables, and extended collections.
- New collections already contain a mode; rename it before adding additional modes.
- Binding helpers can return a new paint/effect/grid object; assign the return value.
- Styles and variables are separate systems. Import and mutation rules differ.

## Images, paints, effects, and export

- Color channels use normalized values.
- `Paint` is a discriminated union covering solid, gradient, image, video, pattern, and shader paints in current typings.
- Create or fetch image bytes/hash asynchronously and assign an image paint.
- Export is async and format/options depend on node and editor support.

## Events and plugin data

- Register only needed events and unregister long-lived handlers where appropriate.
- Keep close-event work minimal and synchronous.
- Namespaced shared plugin data is visible to other plugins; private plugin data is not a secret vault.

Canonical indexes: [Nodes](https://developers.figma.com/docs/plugins/api/nodes/), [Shared properties](https://developers.figma.com/docs/plugins/api/node-properties/), [Data types](https://developers.figma.com/docs/plugins/api/data-types/).
