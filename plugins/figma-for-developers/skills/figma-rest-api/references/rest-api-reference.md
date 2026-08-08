# Figma REST API Reference

Comprehensive reference for the Figma REST API (`https://api.figma.com`), covering authentication, every resource area, the file/node/property data model, and the separate SCIM API. Use this skill whenever the user wants to call the Figma REST API directly (as opposed to using the Figma MCP server tools) — writing scripts against `api.figma.com`, building integrations, webhooks, CI checks on file structure, bulk variable edits, activity-log/audit pulls, or anything referencing Figma API endpoints, tokens, scopes, node types, or the Variables/Webhooks/SCIM APIs. Also use it to explain how a piece of the API works (e.g. "why does my variable collection show `hiddenFromPublishing`", "what's the difference between a plan token and a personal access token") even without code being written.

This is a large reference. Skim the table of contents, jump to the relevant section, and use it as ground truth over prior training knowledge — this was captured directly from developers.figma.com and includes newer features (Extended variable collections, Plan access tokens, granular scopes) that may postdate general knowledge.

## Table of contents

1. [Base URL & versioning](#base-url--versioning)
2. [Authentication](#authentication)
3. [Scopes](#scopes)
4. [Rate limits](#rate-limits)
5. [Errors](#errors)
6. [The file/node data model](#the-filenode-data-model)
7. [Node types](#node-types)
8. [Property types (key ones)](#property-types-key-ones)
9. [Files API](#files-api)
10. [Images API](#images-api)
11. [Comments API](#comments-api)
12. [Users API](#users-api)
13. [Version History API](#version-history-api)
14. [Projects API](#projects-api)
15. [Components & Styles API](#components--styles-api)
16. [Webhooks API (V2)](#webhooks-api-v2)
17. [Variables API](#variables-api)
18. [Dev Resources API](#dev-resources-api)
19. [Library Analytics API](#library-analytics-api)
20. [Activity Logs API (Enterprise)](#activity-logs-api-enterprise)
21. [Developer Logs API (Enterprise+Governance)](#developer-logs-api)
22. [AI Usage API (Enterprise)](#ai-usage-api)
23. [Discovery API (Enterprise+Governance)](#discovery-api)
24. [Payments API](#payments-api)
25. [oEmbed API](#oembed-api)
26. [SCIM API (separate from REST API)](#scim-api)

---

## Base URL & versioning

All REST API requests (except SCIM) go to:

```
https://api.figma.com
```

Figma for Government customers use `https://api.figma-gov.com` instead. There is no version segment in the path — the API is not versioned like `/v1/` or `/v2/`; endpoints just live under `/v1/...`.

---

## Authentication

Three ways to authenticate, in order of what Figma recommends:

### 1. OAuth 2 apps (recommended for acting on behalf of other users)
Standard OAuth2 authorization-code flow. Use when building an app/integration that many different users will install and that needs to act as each user. Token is short-lived with refresh tokens. This is the only method that supports the Activity Logs and Discovery APIs (`org:activity_log_read`, `org:discovery_read` are OAuth-only scopes).

### 2. Plan access tokens (beta)
Org/enterprise-scoped tokens — **not tied to an individual user**. Created in Admin Settings by an org admin. Useful for org-wide automation that shouldn't break when an employee leaves. Up to 1 year expiry. Required for the Developer Logs API and the AI Usage API (both are plan-access-token-only, not available via OAuth or PAT).

### 3. Personal access tokens (PAT)
Tied to an individual Figma account. Max 90-day expiry (Figma enforces token rotation). Simplest to set up for scripts/one-off tooling — generate in Figma account settings. Sent as a header:

```
X-Figma-Token: <token>
```

(OAuth and plan tokens are sent as `Authorization: Bearer <token>` instead.)

**Practical guidance:** for one-off scripts or a single internal tool acting as yourself (e.g. auditing your own files, bulk-editing variables in files you own), a PAT is simplest. For anything org-wide/long-lived, prefer a plan access token. For a multi-tenant product other people install, use OAuth.

---

## Scopes

Figma has moved to granular, resource-specific scopes. The old broad `files:read` scope is **deprecated** — new integrations should request the narrowest scope that does the job. Scopes follow a `resource:read` / `resource:write` pattern, e.g.:

- `file_content:read` — read file contents/nodes
- `file_variables:read` / `file_variables:write` — read/write Variables
- `file_comments:read` / `file_comments:write`
- `file_dev_resources:read` / `file_dev_resources:write`
- `library_content:read` — published components/styles/variables
- `library_analytics:read`
- `webhooks:read` / `webhooks:write`
- `org:activity_log_read` — Activity Logs (OAuth only)
- `org:discovery_read` — Discovery API (OAuth only)
- `org:ai_metering_usage_read` — AI Usage API (plan token only)

When registering an OAuth app or generating a PAT, only grant the scopes the integration actually needs — this is enforced and also just good practice since a leaked broad-scope token is a much bigger blast radius.

---

## Rate limits

Rate limits are tiered by three things combined: **seat type** of the token owner (View/Collab seats get less than Dev/Full seats), **endpoint tier** (some endpoints, like image rendering, are more expensive and rate-limited more strictly than metadata reads), and **plan** (Starter/Professional get lower ceilings than Organization/Enterprise).

On a 429, Figma returns these response headers:

- `Retry-After` — seconds to wait before retrying
- `X-Figma-Plan-Tier` — the plan tier that determined your limit
- `X-Figma-Rate-Limit-Type` — which limit was hit (per-minute, per-endpoint-tier, etc.)
- `X-Figma-Upgrade-Link` — a link to upgrade the plan if the limit is plan-driven

Build retry logic around `Retry-After` rather than a fixed backoff — Figma tells you exactly how long to wait.

---

## Errors

| Code | Meaning |
|---|---|
| 400 | Bad request — malformed params, or the request/response would be too large (e.g. asking for an image render of an enormous frame) |
| 403 | Forbidden — includes the case of calling over plain HTTP instead of HTTPS |
| 404 | Not found |
| 429 | Rate limited — see headers above |
| 500 | Internal error — includes render timeouts on the Images API for very complex nodes |

---

## The file/node data model

Every Figma file is a tree:

```
DOCUMENT
 └─ CANVAS (one per page)
     └─ arbitrary node subtree (FRAME, GROUP, VECTOR, TEXT, COMPONENT, INSTANCE, ...)
```

`DOCUMENT` is the root node returned by `GET /v1/files/:key`. Each `CANVAS` child is a page in the file. Everything below a canvas is the actual design content, arbitrarily nested. Every node has at minimum `id`, `name`, `type`, and `visible`; most have `children` (except leaf types like TEXT, VECTOR).

Node IDs look like `1401:2114` (used in file URLs as `?node-id=1401-2114`, with the colon becoming a hyphen).

---

## Node types

Full catalog of `type` values you'll see on nodes, with their type-specific fields:

- **DOCUMENT** — root node. `children`: array of CANVAS.
- **CANVAS** — a page. `children`, `backgroundColor`, `prototypeStartNodeID`, `flowStartingPoints`, `exportSettings`.
- **FRAME** — the general-purpose container (also used for what the UI calls "frames," artboards). Has layout (auto-layout props like `layoutMode`, `primaryAxisSizingMode`, `itemSpacing`, `paddingLeft/Right/Top/Bottom`), `clipsContent`, `background`/`fills`, `strokes`, `cornerRadius`, `effects`, `constraints`, `layoutGrids`, `overflowDirection`.
- **GROUP** — same shape as FRAME but no layout/clip semantics of its own; just a grouping.
- **TRANSFORM_GROUP** — an internal grouping node used for certain transforms.
- **SECTION** — the "Section" organizational node (not a frame): `sectionContentsHidden`, `children`.
- **VECTOR** — arbitrary vector shape. `vectorPaths` (array of SVG-like path data + `windingRule`), `strokeCap`, `strokeJoin`, `strokeMiterAngle`.
- **BOOLEAN_OPERATION** — result of Union/Subtract/Intersect/Exclude. `booleanOperation`, `children` (the operands).
- **STAR**, **LINE**, **ELLIPSE**, **REGULAR_POLYGON** — vector-like shapes with type-specific extras (e.g. ELLIPSE has `arcData` for pie/ring shapes; STAR/REGULAR_POLYGON count implied by geometry, not an explicit field beyond path data).
- **RECTANGLE** — `cornerRadius` or per-corner `rectangleCornerRadii`, `fills`, `strokes`.
- **TABLE** — `children` of TABLE_CELL/TABLE_ROW-like structure; table-specific sizing.
- **TABLE_CELL** — individual cell; text + fill properties similar to a text/shape node.
- **TEXT** — `characters` (the string), `style` (a `TypeStyle` object — font, size, weight, line height, letter spacing, alignment, decoration, etc.), `characterStyleOverrides` + `styleOverrideTable` for per-range formatting, `lineTypes`, `lineIndentations`.
- **TEXT_PATH** — text that flows along a path; adds `TextPathTypeStyle` and path reference.
- **SLICE** — an export-only region, no visual rendering; just `exportSettings` and bounds.
- **COMPONENT** — a master component. Same visual fields as FRAME plus componentness (referenced by INSTANCEs via `componentId`).
- **COMPONENT_SET** — the parent of component variants; `children` are COMPONENT nodes, each with `componentPropertyDefinitions` values that make up its variant key.
- **INSTANCE** — an instance of a COMPONENT. `componentId` (which master), `componentProperties` (current override values), `overrides` (array of per-node property overrides vs. the master), `isExposedInstance`.
- **STICKY** — FigJam sticky note. `authorVisible`, text content similar to TEXT.
- **SHAPE_WITH_TEXT** — FigJam shape with embedded text.
- **CONNECTOR** — FigJam/diagram connector line. `connectorStart`/`connectorEnd` (each a `ConnectorEndpoint`: either a fixed point or attached to a node+magnet position), `connectorLineType` (ELBOWED/STRAIGHT), `connectorStartStrokeCap`/`connectorEndStrokeCap`, `text`/`textBackground`.
- **WASHI_TAPE** — FigJam decorative tape node.

---

## Property types (key ones)

These are the reusable structs referenced throughout node JSON:

- **Color** — `{r, g, b, a}` floats 0–1.
- **Paint** — a fill/stroke entry: `type` (SOLID/GRADIENT_LINEAR/GRADIENT_RADIAL/GRADIENT_ANGULAR/GRADIENT_DIAMOND/IMAGE/EMOJI/PATTERN), `color`, `gradientStops` (array of `ColorStop`), `opacity`, `blendMode`, `visible`, `imageRef`/`scaleMode` for images, and (relevant to design-token work) `boundVariables` mapping a paint field to a bound Variable.
- **Effect** — shadows/blurs: `type` (INNER_SHADOW/DROP_SHADOW/LAYER_BLUR/BACKGROUND_BLUR), `color`, `offset`, `radius`, `spread`, `visible`, `blendMode`, `boundVariables`.
- **TypeStyle** — full text formatting: `fontFamily`, `fontPostScriptName`, `fontWeight`, `fontSize`, `textAlignHorizontal`/`Vertical`, `letterSpacing`, `lineHeightPx`/`Percent`/`Unit`, `textCase`, `textDecoration`, `textAutoResize`, plus `boundVariables` for tokenized type styles.
- **Style** — a published style reference (`key`, `name`, `styleType` of FILL/TEXT/EFFECT/GRID, `description`).
- **Component / ComponentSet** — metadata objects returned in `components`/`componentSets` maps at the top of a file response: `key`, `name`, `description`, `componentSetId` (for COMPONENT), `documentationLinks`.
- **ComponentPropertyDefinition / ComponentProperty** — the variant/property system: `type` (BOOLEAN/TEXT/INSTANCE_SWAP/VARIANT), `defaultValue`, `variantOptions` (for VARIANT type), `preferredValues` (for INSTANCE_SWAP).
- **Constraint** — `{vertical, horizontal}` each one of SCALE/MIN/MAX/CENTER/STRETCH — layout resize behavior relative to parent.
- **LayoutGrid** — column/row/grid guide config: `pattern` (COLUMNS/ROWS/GRID), `sectionSize`, `gutterSize`, `count`, alignment.
- **ExportSetting** — `suffix`, `format` (JPG/PNG/SVG/PDF), `constraint` (scale/width/height).
- **Overrides** — for INSTANCE nodes, per-node override records vs. the source component.
- **VariableAlias** — `{type: "VARIABLE_ALIAS", id: <variableId>}` — how one variable references another, or how a bound field points at a variable.
- **Annotation** — Dev Mode annotations on nodes: `label`, `properties` (array of `AnnotationProperty`, e.g. spacing/sizing/text-content annotations).
- **Interaction / Trigger / Action** — prototyping: `trigger` (ON_CLICK/ON_HOVER/ON_DRAG/AFTER_TIMEOUT/etc.), `actions` (array; each `Action` has a `type` like NODE/URL/BACK/CLOSE/SET_VARIABLE/SET_VARIABLE_MODE/CONDITIONAL plus type-specific fields), `navigation` (NAVIGATE/SWAP/OVERLAY), `transition` (`SimpleTransition` or `DirectionTransition`, with `easing`).
- **Easing** — `easingType` (built-in curves) or a custom `EasingFunctionCubicBezier`/`EasingFunctionSpring`.
- **VariableData** — used inside prototype SET_VARIABLE actions: `type` (a `ResolvedDataType`: BOOLEAN/FLOAT/STRING/COLOR), and either a literal value or an `Expression` (for computed values, referencing `ExpressionFunction`s and `ConditionalBlock`s).
- **StrokeWeights / ComplexStrokeProperties** — per-side stroke width, plus Basic/Dynamic/Brush(Scatter/Stretch) stroke style variants for advanced pen strokes; `VariableWidthPoint` for variable-width strokes.

---

## Files API

Base path prefix: `/v1/files/:file_key`. The `file_key` is the id in a Figma URL, e.g. `figma.com/design/:file_key/...`.

- **`GET /v1/files/:file_key`** — full document tree (DOCUMENT → CANVAS → nodes) plus `components`, `componentSets`, `styles` maps, `schemaVersion`, `mainFileKey` (if it's a branch), `branches`. Supports `geometry=paths` to include vector path data, `depth` to limit tree depth, `ids` to scope to a subtree, `version` to fetch a specific version.
- **`GET /v1/files/:file_key/nodes?ids=1:2,3:4`** — fetch specific nodes by ID without pulling the whole file. Much cheaper for targeted reads.
- **`GET /v1/files/:file_key/images`** — URLs for all images referenced by `imageRef` in the file's fills.
- **`GET /v1/files/:file_key/meta`** — lightweight file metadata (name, last modified, thumbnail, editor type) without the node tree.

---

## Images API

- **`GET /v1/images/:file_key?ids=1:2,3:4&format=png&scale=2`** — renders the given node IDs to images and returns short-lived S3 URLs. `format` is jpg/png/svg/pdf. `scale` 0.01–4 for raster formats. `svg_include_id`, `svg_simplify_stroke`, `use_absolute_bounds` are SVG-specific options. Rendering large/complex trees can hit a 500 timeout — render smaller subtrees if that happens.

---

## Comments API

- **`GET /v1/files/:file_key/comments`** — all comments on a file, threaded via `parent_id`, each with `client_meta` (pin position — either a node offset or a FrameOffset/Region), `order_id`.
- **`POST /v1/files/:file_key/comments`** — post a comment; body includes `message`, `client_meta`, optional `comment_id` to reply.
- **`DELETE /v1/files/:file_key/comments/:comment_id`**
- **`GET/POST/DELETE .../comments/:comment_id/reactions`** — emoji reactions on comments.

---

## Users API

- **`GET /v1/me`** — the authenticated user's profile (id, email, handle, img_url).

---

## Version History API

- **`GET /v1/files/:file_key/versions`** — paginated list of saved versions (id, created_at, label, description, user who saved it). Use with the `version` query param on the Files endpoints to read a file as of a specific version.

---

## Projects API

- **`GET /v1/teams/:team_id/projects`** — list projects in a team.
- **`GET /v1/projects/:project_id/files`** — list files in a project (name, key, thumbnail, last_modified).

Note there's no "list all teams for the authenticated user" endpoint — team IDs have to come from somewhere else (a URL, or org-level tooling). This matches what we found earlier: the REST/MCP surface doesn't offer a full account-wide file inventory.

---

## Components & Styles API

Separate from the per-file `components`/`styles` maps, these hit a **team's published library**:

- **`GET /v1/teams/:team_id/components`** / **`GET /v1/teams/:team_id/component_sets`** / **`GET /v1/teams/:team_id/styles`** — published components/component sets/styles for a team.
- **`GET /v1/files/:file_key/components`** / **`.../component_sets`** / **`.../styles`** — components/sets/styles defined directly in one file (published or not).
- **`GET /v1/components/:key`** / **`GET /v1/component_sets/:key`** / **`GET /v1/styles/:key`** — metadata for a single published component/set/style by its published key.

---

## Webhooks API (V2)

Webhooks are registered against a **context**: `team`, `project`, or `file` — the webhook fires for events happening within that scope.

- **`POST /v2/webhooks`** — create. Body: `event_type`, `team_id`/`project_id`/`file_id` (whichever context), `endpoint` (your receiving URL), `passcode` (a shared secret Figma echoes back in every payload so you can verify authenticity), `description`.
- **`GET /v2/webhooks/:webhook_id`**, **`GET /v2/teams/:team_id/webhooks`** — read.
- **`PUT /v2/webhooks/:webhook_id`** — update.
- **`DELETE /v2/webhooks/:webhook_id`** — remove.
- **`GET /v2/webhooks/:webhook_id/requests`** — recent delivery attempts (for debugging).

**Event types:** `PING` (test), `FILE_UPDATE`, `FILE_DELETE`, `FILE_VERSION_UPDATE`, `LIBRARY_PUBLISH`, `FILE_COMMENT`, `DEV_MODE_STATUS_UPDATE`.

**Security:** every payload includes the `passcode` you registered — verify it matches before trusting the payload, since your endpoint is a public URL anyone could POST to.

---

## Variables API

This is the API behind Figma Variables (colors, numbers, strings, booleans bound to design properties) — directly relevant to building/maintaining a design-system file like the Atelier Zero one.

### Core types

- **VariableCollection** — a named group of variables sharing a set of modes (e.g. "Light/Dark", "Density"). Fields: `id`, `name`, `modes` (array of `{modeId, name}`), `defaultModeId`, `variableIds`, `hiddenFromPublishing`.
- **Variable** — `id`, `name`, `variableCollectionId`, `resolvedType` (COLOR/FLOAT/STRING/BOOLEAN), `valuesByMode` (map of modeId → value, where a value can be a literal or a `VariableAlias` pointing at another variable), `remote` (true if it comes from a published library), `description`, `hiddenFromPublishing`, `scopes` (`VariableScope[]` — restricts where in the UI the variable is offered, e.g. `ALL_FILLS`, `TEXT_CONTENT`, `CORNER_RADIUS`), `codeSyntax` (per-platform name overrides via `VariableCodeSyntax`: `WEB`/`ANDROID`/`iOS` keys).
- **VariableAlias** — `{type: "VARIABLE_ALIAS", id}` — this is how one variable's value can just be "equal to" another variable (variable-to-variable references, e.g. a semantic token pointing at a primitive).

### Extended collections (newer feature)

Lets a collection **extend** another collection — inherit its variables and override specific values per-mode, without duplicating the whole set. Relevant fields:

- `parentVariableCollectionId` — the base collection being extended.
- `isExtension` — true on the extending collection.
- `variableOverrides` — the specific overridden values in the extension.
- Extended mode IDs have a compound format: `VariableCollectionId:X:Y/A:B` (encodes both the parent collection's mode and the extension's own mode).

This is useful for things like a base "AZ" token collection extended per-brand or per-theme without forking every variable.

### Read endpoints

- **`GET /v1/files/:file_key/variables/local`** — all variables/collections defined *in this file* (whether or not published). This is the ground truth for "what variables exist in this specific file," including ones not yet published to the library.
- **`GET /v1/files/:file_key/variables/published`** — the variables/collections *from this file that have been published* to the team library (what other files can consume).

### Write endpoint

- **`POST /v1/files/:file_key/variables`** — bulk create/update/delete in one call. Body has up to four arrays, each entry tagged with an `action` of CREATE/UPDATE/DELETE:
  - `variableCollections` — create/update/delete collections.
  - `variableModes` — add/rename/delete modes within a collection.
  - `variables` — create/update/delete variables (name, resolvedType, scopes, codeSyntax, hiddenFromPublishing, description).
  - `variableModeValues` — set a variable's value for a specific mode.

  Because everything happens in one call, **new objects use temporary string IDs** you invent (e.g. `"temp_collection_1"`) so later entries in the same payload can reference them before they have real Figma-assigned IDs; the response maps temp IDs to real IDs. This is how you can, in one request, create a new collection, a new mode on it, and a new variable with a value in that mode.

### Practical notes for design-system cleanup work

- A variable collection with **zero variables actually bound to visible node properties** will still show up in `variables/local` — the API doesn't tell you "unused," you have to cross-reference variable `id`s against `boundVariables` fields across the node tree (or rely on the Dev Mode UI / Figma's own "unused" indicators, which the REST API doesn't directly expose as a flag).
- `hiddenFromPublishing` on a collection or variable is what controls whether it's offered to files that consume the published library — a collection can exist and be "live" in the source file while being hidden from downstream consumers, which is one possible explanation for a collection existing but not appearing where you'd expect it in a *different* file's variable picker.
- Color/Text/Effect **Styles** (the older, non-Variables mechanism — `styles` map in the Files API, `/v1/files/:file_key/styles`) are a separate system from Variables. A file can have both live Variables and legacy Styles simultaneously, and they don't automatically reconcile — this is consistent with seeing extra "AZ"/heading/body/emphasis/metadata/UI style groups in the Styles panel that don't correspond to anything in the Variables panel: they're two independent systems, populated separately, possibly by different tooling/agents at different times.

---

## Dev Resources API

Attaches developer-facing URLs to specific nodes (surfaced in Dev Mode, e.g. a "View in Storybook" or "Jira ticket" link on a component).

- **`GET /v1/files/:file_key/dev_resources`** — list dev resources in a file, optionally filtered by `node_ids`.
- **`POST /v1/dev_resources`** — bulk create (array of `{file_key, node_id, name, url}`).
- **`PUT /v1/dev_resources`** — bulk update.
- **`DELETE /v1/files/:file_key/dev_resources/:dev_resource_id`**

---

## Library Analytics API

Enterprise-only. Reports on how a published library's components/styles/variables are actually used across the org.

- **Actions** (time series) — e.g. `GET /v1/analytics/libraries/:file_key/component/actions` — insertions/detachments over time, groupable `by=component` or `by=team`.
- **Usages** (snapshot) — `GET /v1/analytics/libraries/:file_key/component/usages` — current usage counts, similarly groupable.
- Equivalent endpoints exist for `style` and `variable` in place of `component`.

---

## Activity Logs API (Enterprise)

OAuth-only (`org:activity_log_read` scope), Enterprise plan.

- **`GET /v1/activity_logs`** — paginated org-wide audit events. Query by `event_type`, `actor_id`, date range, `cursor` for pagination.

### Event structure

Each entry has `actor` (who did it — user, or `null`/system for automated events), `action` (the event name — see below), `entity` (what was affected), and `context` (surrounding info like IP address, org/team/file context).

### Entity types

`file`, `file_repo`, `idp_user`, `policy_acknowledgement_config`, `org`, `plugin`, `project`, `team`, `user`, `widget`, `workspace`.

### Action types

This is a very large enum (300+ distinct action names) covering essentially every settings toggle and lifecycle event in an Enterprise org: file/branch lifecycle (`fig_file_create`, `fig_file_rename`, `fig_file_move`, `fig_file_permanent_delete`, `branch_create`, `branch_archive`, ...), membership/permission changes on files/branches/teams/workspaces (`*_member_add`, `*_member_permission_change`, `*_member_remove`), org-wide security/policy toggles (`ai_features_enable/disable`, `ai_content_training_enable/disable`, `cursor_chat_setting_change`, `external_collaboration_controls_setting_change`, `autogen_password_controls_setting_change`, `configurable_upgrade_request_*`), Community publishing (`community_hub_file_publish/update/delete`, `community_plugin_*`, `community_widget_*`), link-sharing changes (`fig_file_link_access_change`, `fig_file_link_expiration_change`, `fig_file_proto_link_access_change`), and more.

Each action's `Properties` column in the docs describes an `old_x`/`new_x` pair of fields for settings-change events, or resource identifiers (`resource_type`, `resource_id_or_key`, `permission`) for membership events.

**Because this enum is huge and enterprise-admin-focused (not design-system-relevant), don't try to memorize it — when a specific action name shows up in a payload and its meaning isn't obvious from the name, fetch `https://developers.figma.com/docs/rest-api/activity-logs-action-types/` directly and search for it.**

---

## Developer Logs API

Enterprise + Governance add-on, **plan access token only** (not OAuth, not PAT). Granular audit log of individual API calls made against the org's Figma resources — useful for security review of what integrations are actually doing. Endpoint returns per-call records (caller, endpoint hit, timestamp, response status).

---

## AI Usage API

Enterprise, **plan access token only**, `org:ai_metering_usage_read` scope. Reports per-user, per-day AI credit consumption across Figma's AI features org-wide.

---

## Discovery API

Enterprise + Governance add-on, OAuth-only, `org:discovery_read` scope. Extracts **text-bearing events** from across the org for compliance/DLP purposes: in-file text content, cursor chat messages, comments, component documentation, Dev Mode annotations, and AI prompts. Rather than returning data inline, it hands back links to hourly-generated JSON files (`GET /v1/discovery` type endpoint returns file links; you download and parse those separately). Each record has a `text_type` classifying which of the above categories it came from.

---

## Payments API

Verifies purchases of paid plugins/widgets/Community files.

- Verify via a **plugin payment token** (passed to your plugin at runtime by Figma) — `GET /v1/payments` with the token confirms entitlement.
- Or verify via explicit `user_id` + `resource` (plugin/widget/file) IDs for server-side checks outside the plugin runtime.

---

## oEmbed API

- **`GET /v1/oembed?url=<figma-file-or-make-site-url>`** — returns oEmbed 1.0-spec-compliant metadata (title, thumbnail, embed HTML) for a Figma file or Figma Make site, for use in rich-embed contexts (Slack unfurls, blog embeds, etc.).

---

## SCIM API

**Entirely separate system from the REST API above** — different base URL, different auth, different purpose (user lifecycle provisioning from an identity provider). Not available on Starter/Professional plans — Enterprise (with SSO) only.

### Base URL & auth

```
https://www.figma.com/scim/v2/:tenantid
```

`:tenantid` is org-specific. Auth is a Bearer token generated in Figma Admin Settings (not a PAT, not OAuth, not a plan token) — `Authorization: Bearer <scim-token>`.

Used to connect an IdP (Entra ID / Azure AD, Okta, OneLogin, Google SSO, AD FS) so that provisioning/deprovisioning users and groups in the IdP automatically reflects in Figma.

### Configuration endpoints

- **`GET :baseURL/ServiceProviderConfig`** — capability discovery (what SCIM operations Figma supports: patch, filter, etc.)
- **`GET :baseURL`** — validates the tenant ID (200 valid / 400 invalid).

### Users endpoints

- **`GET :baseURL/Users`** — list/filter (`?filter=userName eq "email@domain.com"` or by `externalId`), paginated via `count`/`startIndex` (max 3000/page).
- **`POST :baseURL/Users`** — provision a new/existing user. Key fields: `userName` (email — this *is* the account identifier, changing it changes the Figma account's email), `active` (false = deactivate & remove from org), `roles` (`[{type: "seatType", value: "Full"|"Dev"|"Collab"|"View"}]`, Enterprise-only), `externalId`, `displayName`, `title`, `givenName`, `familyName`, plus Enterprise-schema extras (`employeeNumber`, `costCenter`, `organization`, `division`, `department`, `managerValue`, `managerDisplayName`) and the Figma-specific `figmaAdmin` boolean (org admin flag).
- **`PUT :baseURL/Users/:figmaUserId`** — full overwrite of a user's attributes.
- **`PATCH :baseURL/Users/:figmaUserId`** — partial update via SCIM `PatchOp` operations (e.g. `{op: "replace", path: "roles", value: [...]}`).
- **`DELETE :baseURL/Users/:figmaUserId`** — permanent delete (204 on success). Note: `PUT`/`PATCH` with `active: false` is a **soft** delete (deprovisions from Figma but keeps the SCIM record, so `GET Users` still lists them) — use `DELETE` for a hard delete.

### Groups endpoints

SCIM groups link to a Figma **workspace or billing group** by matching `displayName` (case-sensitive) — members of the SCIM group automatically inherit that workspace/billing group membership.

- **`GET :baseURL/Groups`** — list/filter by `displayName` or `externalId`.
- **`POST :baseURL/Groups`** — create, with `displayName`, `externalId`, `members` (array of `{value: userId, display: email}`).
- **`PUT :baseURL/Groups/:figmaGroupId`** — full overwrite (add/remove members → they gain/lose the linked workspace/billing group).
- **`PATCH :baseURL/Groups/:figmaGroupId`** — partial update (e.g. rename via `{op: "replace", value: {displayName: "new name"}}`).
- **`DELETE :baseURL/Groups/:figmaGroupId`** — permanent delete (204).

### Supported schemas

- `urn:ietf:params:scim:schemas:core:2.0:User` — `roles`, `givenName`, `familyName`, `displayName` (≤100 chars), `title`, `userName` (≤100 chars, the email), `active`, `externalId` (≤255 chars).
- `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User` — `employeeNumber`, `costCenter`, `organization`, `division`, `department`, `managerValue`, `managerDisplayName`.
- `urn:ietf:params:scim:schemas:core:2.0:Group` — `displayName` (≤255 chars), `members`, `externalId` (≤255 chars).
- `urn:ietf:params:scim:schemas:extension:figma:enterprise:2.0:User` (custom) — `figmaAdmin` boolean. Note: product seats used to be a custom parameter here too, but are now managed via the standard `roles` field on the Core User schema instead.

---

## Source

Captured from `https://developers.figma.com/docs/rest-api/` (all pages and subpages) in full on 2026-08-02. If something looks like it might have changed (new endpoint, changed field), it's worth re-fetching the specific page rather than assuming this is stale — Figma ships API changes fairly often and there's a `/docs/rest-api/changelog/` page that tracks them.
