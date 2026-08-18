---
name: mailerlite-release
description: Perform the final controlled release of an explicitly approved Hair Solutions Co. MailerLite campaign, test send, automation, form, or related email change. Use only when Vincent asks to send a test, schedule or send a specific campaign, activate a specific automation, publish a form, or release a named email asset. Requires current account, audience, content, consent, deliverability, rendering, timing, and rollback evidence; never infer release approval from drafting or review work.
---

# MailerLite release

1. Require a fresh explicit instruction naming the resource and release action. Read
   ../../references/action-gates.md and email-quality-gates.md.
2. Run email-marketing-preflight immediately before release. Re-fetch the exact campaign, automation,
   form, sender, audience, exclusions, and account.
3. Verify approved content, links, merge-field fallbacks, plain text, mobile and desktop rendering,
   unsubscribe and preference behavior, sender authentication, tracking, plan headroom, and no broken
   ecommerce dependency.
4. For a test send, confirm exact recipients and state that it sends email. For a campaign, confirm
   group or segment, recipient count, date, clock time, and time zone. For an automation, confirm
   trigger, re-enrolment, existing queue behavior, exits, and suppression.
5. Execute only the named action. Do not bundle unrelated releases.
6. Re-fetch and prove the resulting scheduled, sent, enabled, or published state. Record resource ID,
   timestamp, audience or trigger, and monitoring plan without exposing recipients.
7. Watch the explicitly requested initial window or first cohort when authorized; otherwise hand off
   the exact metrics and time for the next check.

If any value differs from the approved release summary, stop before execution and request direction.
