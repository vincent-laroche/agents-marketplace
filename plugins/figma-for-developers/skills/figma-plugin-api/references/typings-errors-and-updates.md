# Typings, API errors, and version drift

## Typings

- Install with `npm install --save-dev @figma/plugin-typings` and configure TypeScript to include the package declarations.
- The typings are the most exhaustive contract for members, overloads, unions, editor restrictions, proposed APIs, and deprecations.
- Search the installed package first. The bundled snapshot is a fallback and audit artifact.
- Use Figma's plugin-specific ESLint rules where practical to catch invalid synchronous API usage and migration issues.

## Error diagnosis

1. Preserve the full error message and stack.
2. Confirm editor type and mode.
3. Confirm the node has not been removed and narrow `node.type`.
4. Confirm the member exists in the current typings and is not gated by permissions, capabilities, proposed/private API access, or an editor restriction.
5. Confirm the current page/resource is loaded and all async calls are awaited.
6. Confirm fonts are loaded before text mutation.
7. Confirm values satisfy discriminated unions, numeric ranges, readonly/reassignment rules, and non-null constraints.
8. Reduce to a minimal plugin and reproduce against the current desktop/web Figma build.

Figma API errors commonly contain a source location and message. Runtime validation may be stricter than a stale local type package, while newer typings may describe APIs not yet available to every environment. Record all three versions: manifest API version, typings package version, and observed Figma client.

## Deprecation and migration

- Prefer async alternatives marked in typings, especially under dynamic page loading.
- Do not enable the proposed API merely to silence a missing-member error.
- Read the current official page plus relevant release/update entry before adopting a new or changed member.
- Keep a small compatibility layer when supporting materially different client/API generations.

Official pages: [Typings](https://developers.figma.com/docs/plugins/api/typings/), [API errors](https://developers.figma.com/docs/plugins/api/api-errors/), [Dynamic loading migration](https://developers.figma.com/docs/plugins/migrating-to-dynamic-loading/), [Stability](https://developers.figma.com/docs/plugins/stability-updates/), [Update archive](https://developers.figma.com/docs/plugins/updates/), [official typings repository](https://github.com/figma/plugin-typings).
