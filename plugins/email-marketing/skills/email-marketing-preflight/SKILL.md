---
name: email-marketing-preflight
description: Verify the exact Hair Solutions Co. MailerLite account, authentication, plan headroom, sender and domain status, audiences, disabled or live automations, campaign release state, Shopify ecommerce connection, and current local authority before any email-marketing work. Use at the start of MailerLite campaign, audience, automation, form, template, deliverability, analytics, or release tasks and whenever account identity or readiness is uncertain.
---

# Email marketing preflight

1. Read PROJECT.md then AGENTS.md in /Users/vMac/07_design/email.
2. Read ../../references/authority-map.md and ../../references/action-gates.md.
3. Check MailerLite MCP authentication. If unavailable, use the read-only snapshot script after
   loading MAILERLITE_API_TOKEN without printing it.
4. Verify the target account ID before any write. Stop on a mismatch.
5. Inspect plan limits, subscriber headroom, verified senders, domain authentication, groups,
   segments, fields, campaign states, enabled automations, shop status, and broken ecommerce triggers
   relevant to the task.
6. Compare live facts with current local ledgers. Report conflicts; do not silently choose stale IDs.
7. Return: account verified, safe scope, blockers, approval class, and next exact action.

Do not mutate MailerLite during preflight. Do not expose subscriber PII or credentials.
