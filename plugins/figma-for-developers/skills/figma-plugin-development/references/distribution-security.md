# Distribution, authentication, security, and operations

## OAuth and external services

- Use Authorization Code with PKCE or a backend-assisted flow appropriate to a public client. Never place a client secret in the plugin.
- Restrict redirect URIs, state, code verifier handling, token scope, and token lifetime.
- Store only necessary user-local data in `figma.clientStorage`; do not treat it as a server-side secret vault or shared database.
- Define logout/revocation and expired-token recovery.

## Payments

- Declare the payments permission and use the payments API only when the product and Figma's current commerce requirements support it.
- Gate premium behavior on verified entitlement, not UI state alone.
- Keep billing decisions reversible and obtain explicit approval before enabling paid distribution.

## Publication

- Test the production bundle, manifest, declared domains, editor types, permissions, support contact, listing assets, and security/data disclosures.
- Explain data collection, external requests, storage, retention, and deletion accurately.
- Figma can publish updates without a full re-review; users cannot select an older version. Preserve a tested rollback build so an earlier version can be republished if needed.
- Do not publish or update a Community plugin without explicit approval.

## Reliability

- Capture errors and performance outside Figma if needed; Figma's built-in plugin analytics and crash reporting are limited.
- Avoid logging tokens, document content, user data, or node/plugin data unless necessary and disclosed.
- For long work, expose progress and cancellation. Keep the close handler synchronous and minimal.
- If a plugin freezes, terminate it through Figma's controls, isolate the loop or oversized traversal, then rerun a bounded reproduction.

## Proposed and private APIs

- `enableProposedApi` opts into unstable capabilities that may change without normal stability guarantees.
- `enablePrivatePluginApi` is limited to eligible private/Figma-owned contexts. Do not design a public plugin around it without confirmed access.

Official pages: [OAuth](https://developers.figma.com/docs/plugins/oauth-with-plugins/), [Requiring payment](https://developers.figma.com/docs/plugins/requiring-payment/), [Publishing](https://developers.figma.com/docs/plugins/publishing/), [Frozen plugins](https://developers.figma.com/docs/plugins/frozen-plugins/), [Stability and updates](https://developers.figma.com/docs/plugins/stability-updates/), [Proposed API](https://developers.figma.com/docs/plugins/proposed-api/), [Get help](https://developers.figma.com/docs/plugins/get-help/).
