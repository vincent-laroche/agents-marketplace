---
name: mailerlite-deliverability-domain
description: Audit Hair Solutions Co. MailerLite sender verification, sending-domain authentication, SPF, DKIM, DMARC, alignment, sender reputation, bounce and complaint signals, plan limits, and test-send readiness. Use when sends are blocked, a sender is unauthenticated, DNS records are requested, deliverability declines, or campaign and automation release needs domain proof. DNS, credential, and sender changes require explicit approval and the Cloudflare operations boundary.
---

# MailerLite deliverability and domain

1. Run email-marketing-preflight and read ../../references/action-gates.md.
2. Inspect MailerLite domain and sender status. Use a signed-in dashboard when account-specific DNS
   values are not exposed through the MCP.
3. Read current public DNS and distinguish SPF, DKIM, DMARC, return-path, and sender verification.
   Preserve existing providers; do not replace an SPF record blindly.
4. Check alignment, duplicate SPF records, DKIM selector collisions, DMARC policy, plan or subscriber
   caps, bounce rate, complaints, unsubscribes, and recent volume changes.
5. Return exact current state, required records with source, conflicts, propagation check, and release
   consequence.
6. Route any Cloudflare change through hair-solutions-cloudflare-ops and require fresh explicit
   approval. Verify DNS and MailerLite status after an approved change.

Do not print account-unique tokens in chat or commit them to the toolkit.
