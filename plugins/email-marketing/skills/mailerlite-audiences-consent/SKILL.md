---
name: mailerlite-audiences-consent
description: "Inspect, design, validate, or explicitly apply Hair Solutions Co. MailerLite subscriber, group, segment, field, suppression, preference, and consent changes. Use for audience definitions, segmentation, custom fields."
---

# MailerLite audiences and consent

1. Run email-marketing-preflight. Read ../../references/action-gates.md and authority-map.md.
2. Define the subscription purpose and lawful source before selecting people. Separate operational,
   service, guidance, and promotional permissions.
3. Inspect current groups, segments, fields, suppressions, subscriber status distribution, and plan
   headroom. Use exact names and current IDs.
4. For imports, require a local manifest with source, approval status, row count, SHA-256, exclusions,
   target groups, field mapping, dry-run result, and rollback or containment plan.
5. Exclude opted-out, bounced, junk, suppressed, invalid, and unproven-consent records. Never reactivate
   them through API upsert.
6. Apply only the exact approved change. Batch conservatively, stop on unexpected errors or cap
   pressure, and never log raw email lists.
7. Re-fetch aggregate counts and sampled redacted states. Report added, updated, skipped, failed, and
   remaining headroom.

Deletion, forgetting, unsubscription, bulk import, and group removal require fresh explicit approval.
