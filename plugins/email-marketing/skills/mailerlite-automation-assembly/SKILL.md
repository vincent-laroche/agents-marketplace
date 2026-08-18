---
name: mailerlite-automation-assembly
description: Build, update, inspect, dry-run, or repair disabled Hair Solutions Co. MailerLite automations from an approved architecture, including triggers, email content, delays, branches, field and group actions, ecommerce conditions, exits, and step linkage. Use when implementing lifecycle flows or diagnosing broken, incomplete, disconnected, or incorrectly ordered automation steps. Never enable an automation from this skill.
---

# MailerLite automation assembly

1. Run email-marketing-preflight. Require an accepted automation specification.
2. Verify every trigger dependency, field, group, segment, shop, product event, sender, and email asset
   in the intended account before building.
3. Create or update only a disabled automation. Resolve existing automation by exact name and ID; do
   not duplicate silently.
4. Prefer the MailerLite MCP. Use browser or a bounded REST adapter only for documented gaps.
5. After every structural write, re-fetch the full graph. Prove exactly one root, correct parent links,
   intended order, reachable branches, purchase or goal exits, re-enrolment, and no broken trigger.
6. Upload validated content, then prove each email is designed, sender-authenticated, and attached to
   the correct step. A step count alone is not evidence of a connected sequence.
7. Run MailerLite dry-run or equivalent structural validation. Return dashboard link, graph, emails
   designed versus missing, warnings, untested events, and exact activation blockers.

Do not send a test or enable the automation. Route those actions to mailerlite-release.
