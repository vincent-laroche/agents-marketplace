---
name: figma-plugin-development
description: Designs, builds, migrates, debugs, secures, and prepares Figma plugins across Design, FigJam, Dev Mode, Slides, and Buzz. Use when working on plugin manifests, runtime lifecycle, iframe UI, messaging, network access, OAuth, parameters, build tooling, dynamic page loading, codegen, text review, payments, publishing, frozen plugins, or editor-specific behavior. Do not use for direct Figma REST integrations, widget-only products, or ordinary Figma canvas edits that do not involve authoring a plugin.
---

# Develop Figma Plugins

Build user-triggered editor extensions with explicit permissions, bounded network access, and editor-specific behavior.

## Procedure

1. Confirm the target editor types, user action, read/write scope, UI requirement, network requirement, and distribution model.
2. Inspect the existing repository, `manifest.json`, build scripts, typings version, and current errors before editing.
3. Read [references/build-runtime-manifest.md](references/build-runtime-manifest.md) for runtime, manifest, UI, async, bundling, and debugging rules.
4. Read [references/editor-modes-and-specializations.md](references/editor-modes-and-specializations.md) when targeting FigJam, Dev Mode, Slides, Buzz, codegen, inspect, text review, parameters, or editor-specific nodes.
5. Read [references/distribution-security.md](references/distribution-security.md) before OAuth, external requests, payments, private APIs, publication, analytics, or user-data handling.
6. Use `$figma-plugin-api` for exact current signatures, node compatibility, property types, and error diagnosis.
7. Implement the smallest vertical slice:
   - register a minimal valid manifest;
   - establish the main-code lifecycle;
   - add UI only if the action cannot remain parameter-only or immediate;
   - add domains and permissions only when exercised;
   - close the plugin after work completes unless a UI or async task must remain active.
8. Prefer async document APIs and `documentAccess: "dynamic-page"`. Load pages, fonts, and other resources deliberately.
9. Validate manifest shape, type-check against the installed `@figma/plugin-typings`, build the final JavaScript/UI assets, and run the plugin in every declared editor mode.
10. Reproduce and test failure paths: unavailable fonts, mixed values, missing nodes, denied domains, malformed messages, rejected promises, unsupported editor types, and large documents.
11. Record the exact Figma environment tested and any proposed/private API dependency.

## Safety and approvals

- Never broaden `networkAccess`, permissions, capabilities, or editor types without a demonstrated need.
- Never embed client secrets in plugin code or iframe assets. Use a backend for secrets and OAuth exchanges.
- Treat `enablePrivatePluginApi` as restricted, not a shortcut.
- Treat `enableProposedApi` as unstable and require a fallback or explicit acceptance of breakage risk.
- Do not publish, change sharing, require payment, or collect analytics without explicit approval.

## Error Handling

- If the runtime and typings disagree, capture the Figma client, manifest API, and typings versions, then reduce to a minimal reproduction.
- If a declared editor or capability is unavailable, remove the declaration or stop with the exact eligibility requirement; do not silently substitute a private/proposed API.
- If a plugin freezes, terminate it through Figma, bound the traversal or loop, and rerun only the reduced case.

## Completion

Report files changed, declared capabilities/domains, build and type-check results, editor modes tested, remaining restrictions, and publication state.

For the complete audited page set, read [references/official-source-map.md](references/official-source-map.md).
