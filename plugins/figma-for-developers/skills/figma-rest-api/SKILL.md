---
name: figma-rest-api
description: Builds and diagnoses direct integrations with Figma's HTTP REST and SCIM APIs, including authentication, scopes, files, nodes, images, comments, projects, libraries, webhooks, variables, Dev Resources, analytics, activity logs, payments, oEmbed, and enterprise endpoints. Use when creating scripts, services, CI jobs, cross-file reads, webhooks, audits, or resolving REST errors and rate limits. Do not use for in-editor Plugin API methods, Widget API code, MCP-mediated canvas edits, or arbitrary node writes that REST does not support.
---

# Use the Figma REST API

Use the supplied comprehensive reference as the baseline, then verify unstable scopes, availability, limits, and enterprise entitlements against current official documentation before shipping.

## Procedure

1. Confirm the integration runs outside the Figma editor and identify the resource, operation, file/team/org scope, and required write behavior.
2. Read [references/rest-api-reference.md](references/rest-api-reference.md), jumping to the relevant resource section.
3. Select OAuth, a plan access token, or a personal access token according to ownership, lifetime, user delegation, and endpoint support.
4. Request the narrowest supported scopes. Never infer a scope from a similarly named Plugin API capability.
5. Confirm the endpoint supports the intended write. REST is largely read-only outside comments, reactions, variables, Dev Resources, webhooks, and other explicitly documented write endpoints.
6. Implement pagination, response-size controls, rate-limit handling based on `Retry-After`, typed error handling, and token-safe logging.
7. For node JSON, distinguish REST node/property models from Plugin API interfaces and methods.
8. Use a dry-run or read-only smoke test before bulk writes, webhook registration, or enterprise-wide collection.
9. Verify returned IDs, pagination completion, partial failures, and post-write state.

## Safety and freshness

- Never print or commit tokens.
- Never use personal tokens for a multi-user product.
- Never claim arbitrary visual node editing through REST.
- Recheck live official docs when scope names, entitlements, endpoint availability, or rate limits affect production behavior.

## Error Handling

- On 401/403, distinguish token type, missing scope, resource access, plan entitlement, and endpoint-specific authentication support.
- On 429, honor `Retry-After` and retain pagination state rather than restarting an unsafe write batch.
- On partial or ambiguous writes, stop, read back the resource, and reconcile by stable IDs before retrying.

## Completion

Report the authentication model, scopes, endpoints, pagination/rate-limit behavior, verification performed, and any plan or seat dependency.
