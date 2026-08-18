---
name: mailerlite-campaign-drafting
description: Create, update, inspect, or validate Hair Solutions Co. MailerLite campaign drafts with exact sender, subject, preview, HTML or native-editor content, audience filters, tracking, and internal naming. Use for newsletters, broadcasts, promotions, A/B drafts, resends prepared but not sent, and lifecycle content parked safely as drafts. Do not use it to schedule, send, activate, import contacts, or delete campaigns.
---

# MailerLite campaign drafting

1. Run email-marketing-preflight and read ../../references/action-gates.md.
2. Resolve the campaign by exact name and ID in the verified account. Decide create versus update;
   never duplicate silently.
3. Require an approved brief or clearly label content draft. Validate HTML before upload.
4. Set internal name, language, subject, sender, reply-to, preheader, content type, tracking, and the
   exact intended group or segment.
5. For lifecycle content that belongs in an automation, park the draft in the verified zero-member
   do-not-send group. Resolve the group by exact name, never by copied ID.
6. Re-fetch the campaign. Prove status is draft, all-active-subscribers is false, the human-readable
   filter is correct, and the recipient count is expected. Stop immediately if MailerLite broadens the
   audience.
7. Return the dashboard link, changed fields, audience proof, missing-data warnings, and next release
   gate.

Scheduling and sending belong only to mailerlite-release with fresh explicit approval.
