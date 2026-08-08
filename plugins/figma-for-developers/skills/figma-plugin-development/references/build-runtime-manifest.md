# Plugin build, runtime, and manifest

## Runtime contract

- Main plugin code runs in Figma's sandbox and reaches the editor through the global `figma` object.
- Optional UI runs in an iframe. Communicate with `figma.ui.postMessage(...)` and `parent.postMessage({ pluginMessage: ... }, '*')`; validate message shape on both sides.
- Only one plugin action runs at a time. Close with `figma.closePlugin()` when complete; keep it open only for active UI or awaited work.
- Pages load dynamically. New plugins must declare `documentAccess: "dynamic-page"` and use async page/node access outside the current page.
- Load fonts before text mutations. Await image, export, library import, page, and other async operations.
- Long synchronous loops freeze the plugin. Chunk work, yield between batches, show progress, and avoid unbounded traversal.

## Minimum manifest

```json
{
  "name": "My Plugin",
  "id": "figma-assigned-id",
  "api": "1.0.0",
  "main": "dist/code.js",
  "editorType": ["figma"],
  "documentAccess": "dynamic-page",
  "networkAccess": { "allowedDomains": ["none"] }
}
```

Add `ui`, `menu`, `parameters`, `parameterOnly`, `relaunchButtons`, `permissions`, `capabilities`, `codegenLanguages`, `codegenPreferences`, `build`, `enableProposedApi`, or `enablePrivatePluginApi` only when used.

## Network access

- Declare the smallest `networkAccess.allowedDomains` set. Use `["none"]` for no network.
- Use `devAllowedDomains` only for development hosts.
- A domain rule can include supported schemes and subdomain wildcards; avoid `*` unless the product genuinely requires arbitrary destinations and the review/privacy implications are accepted.
- Test denied as well as allowed requests.
- Keep secrets on a backend. Plugin and UI bundles are client-distributed code.

## UI

- Use `ui` as a string for one HTML entry or a name-to-file map exposed through `__uiFiles__` for multiple UI documents.
- Use `figma.showUI(__html__, options)` or an entry from `__uiFiles__`.
- Treat messages as an untrusted boundary. Validate type, required fields, length, URLs, and node IDs.
- Request theme CSS variables with the supported UI option when the UI should track light/dark Figma themes.
- Prefer parameters for short, keyboard-first input instead of building a modal.

## Build and TypeScript

- Install the latest compatible `@figma/plugin-typings` as a development dependency.
- Compile/bundle all dependencies into browser/sandbox-compatible output. Do not rely on Node built-ins in the Figma runtime.
- Keep main code and iframe code as separate entry points with an explicit message contract.
- Type-check before bundling; inspect final artifacts for accidental credentials and unsupported dynamic imports.
- Use a build tool already present in the repo. Official guidance covers simple TypeScript scripts plus webpack, esbuild, Plugma, and Create Figma Plugin patterns.

## Debugging

- Reproduce with the developer console open and capture the complete error plus the smallest code path.
- Confirm `figma.editorType`, `figma.mode`, current page, node type, font state, permissions, domains, and typings version.
- Reduce to a minimal development plugin when the runtime disagrees with types.
- Infinite or long-running plugins can be stopped from Figma's plugin controls; fix the loop or split work before rerunning.

Official pages: [Manifest](https://developers.figma.com/docs/plugins/manifest/), [How plugins run](https://developers.figma.com/docs/plugins/how-plugins-run/), [Creating UI](https://developers.figma.com/docs/plugins/creating-ui/), [Network requests](https://developers.figma.com/docs/plugins/making-network-requests/), [Async tasks](https://developers.figma.com/docs/plugins/async-tasks/), [TypeScript](https://developers.figma.com/docs/plugins/typescript/), [Build scripts](https://developers.figma.com/docs/plugins/build-script/), [Libraries and bundling](https://developers.figma.com/docs/plugins/libraries-and-bundling/), [Debugging](https://developers.figma.com/docs/plugins/debugging/).
