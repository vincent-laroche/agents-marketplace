# Action gates

## Read without approval

- Inspect authentication, account identity, plan, domains, senders, campaigns, templates, groups,
  segments, fields, forms, automations, ecommerce resources, webhooks, and aggregate analytics.
- Read local briefs, copy, HTML, manifests, ledgers, and validation output.
- Draft plans, copy, HTML, audience manifests, automation specifications, and release checklists locally.
- Run local validators and read-only account snapshots.

## Write only when the task explicitly asks for the named change

- Create or update a MailerLite campaign draft.
- Create a disabled automation or update steps in a disabled automation.
- Create a draft form or reusable template in the dashboard.
- Create or rename a group, segment, or field.
- Update MailerLite ecommerce data or connect a shop.

After every write, re-fetch the exact resource and prove its account, name, state, audience, and
changed fields. Do not broaden an approved draft change into release.

## Require fresh explicit approval in the current conversation

- Import, update, unsubscribe, remove, forget, or delete subscribers.
- Send a test email, schedule or send a campaign, resend to non-openers, or activate an automation.
- Publish or embed a form or landing page.
- Change DNS, sender authentication, Shopify integration state, webhooks, credentials, or permissions.
- Delete campaigns, automations, groups, segments, fields, forms, templates, webhooks, shops, products,
  customers, orders, carts, or categories.

A previous approval does not carry into a new release or destructive action. A test send is still a
send. A disabled automation is not live. A draft campaign is not scheduled.

## Never infer

- Never treat no audience selection as zero recipients. MailerLite may interpret it as all active
  subscribers; verify the returned human-readable filter and recipient count.
- Never reactivate unsubscribed, bounced, junk, or suppressed contacts through an import.
- Never invent consent, product, pricing, discount, shipping, return, timing, support, or testimonial
  claims.
- Never expose or persist an API token in commands, logs, manifests, screenshots, or plugin files.
