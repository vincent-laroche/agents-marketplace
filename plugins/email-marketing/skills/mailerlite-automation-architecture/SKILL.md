---
name: mailerlite-automation-architecture
description: "Design or review complete Hair Solutions Co. MailerLite lifecycle automation specifications before implementation. Use for welcome, post-purchase, fulfillment, cart recovery, browse recovery, reorder, education."
---

# MailerLite automation architecture

1. Run email-marketing-preflight and read ../../references/authority-map.md and action-gates.md.
2. Start with the customer event and business outcome. Identify the subscription purpose and why this
   person is eligible.
3. Specify trigger, re-enrolment, prerequisites, entry suppression, each delay or condition, email and
   non-email actions, success exits, failure exits, cross-flow suppression, sunset, and ownership.
4. Map every merge field and ecommerce event to its source. Mark unavailable, stale, or dashboard-only
   data as a blocker.
5. Check loops, duplicate sends, races with campaigns, unreachable branches, lying sunset copy, absent
   purchase exits, and automations that match the whole audience.
6. Produce a linear and branch-aware flow, email inventory, data contract, test matrix, measurement
   plan, build order, and release gates.

Hand an accepted specification to mailerlite-automation-assembly. Do not create a shell from this skill.
