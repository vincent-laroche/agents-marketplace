# Authority map

Read only the authorities relevant to the task.

- Current work and operational state: /Users/vMac/07_design/email/PROJECT.md
- Durable project rules: /Users/vMac/07_design/email/AGENTS.md
- MailerLite implementation: /Users/vMac/07_design/email/mailerlite/
- Approved campaign and lifecycle copy: /Users/vMac/07_design/email/emails_master/
- Current brand authority: /Users/vMac/08_brand/brand-design-system/
- Email platform rules: route from the current brand repository to its email platform specification.
- Secrets: /Users/vMac/.env. Inspect variable names only; never print values.

Current filesystem and live MailerLite reads override copied account facts in old documents. Resolve
resource IDs by exact name in the target account. Never carry campaign, group, automation, segment,
form, shop, or field IDs from a previous account or stale ledger.

The intended MailerLite account must be verified before a write. The known account at plugin creation
was 2582639, but treat that as an assertion to check, not a permanent constant.

The legacy email-marketing-modules plugin is HubSpot-only reference material. Do not route new
campaign, automation, audience, or module work through HubSpot unless Vincent explicitly asks.
