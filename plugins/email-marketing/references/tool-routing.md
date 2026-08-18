# Tool routing

## Official MailerLite MCP

Use the OAuth server at https://mcp.mailerlite.com/mcp for authentication status, discovery, reads,
campaign drafts, audiences, fields, forms, automations, ecommerce, webhooks, test operations, and
dashboard links. Prefer exact resource reads before and after any mutation.

## Local read-only scripts

Use scripts/mailerlite_snapshot.py for a non-PII account fingerprint and counts. It reads
MAILERLITE_API_TOKEN from the environment, never prints it, performs GET requests only, and fails if
the account ID does not match the expected target.

Use scripts/validate_email.py for deterministic HTML checks before any upload or test send.

## Browser control

Use a signed-in browser only for MailerLite dashboard capabilities the MCP cannot complete safely:
native drag-and-drop composition, saving email templates, inspecting exact domain DNS values,
connecting Shopify, and visual verification. Report a login page as a blocker, not as success.

## Direct REST API

Use direct REST only when the official MCP lacks a required operation and local project evidence
documents the exact endpoint and payload. Default to GET. Put any repeated mutation behind a bounded,
reviewable local script before use. Never issue an ad-hoc authenticated delete, send, schedule, import,
or activation request.

## Figma and brand

Use Figma as a visual review surface when requested. It is not the content store or sending surface.
Read the live brand repository before applying color, typography, components, imagery, or voice.
