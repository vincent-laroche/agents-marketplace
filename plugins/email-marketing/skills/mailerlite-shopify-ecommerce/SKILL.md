---
name: mailerlite-shopify-ecommerce
description: Inspect, reconcile, or explicitly update the Shopify ecommerce data available inside Hair Solutions Co. MailerLite, including shop connection, customers, products, categories, orders, carts, cart items, trigger eligibility, sync freshness, and field mappings. Use when purchase, abandoned-cart, product, category, reorder, fulfillment, revenue, or customer-segmentation flows depend on MailerLite ecommerce data. Connecting or mutating a shop is approval-gated.
---

# MailerLite Shopify ecommerce

1. Run email-marketing-preflight and read ../../references/tool-routing.md and action-gates.md.
2. Inspect the MailerLite shop through the official MCP. Verify shop identity, enabled state, sync
   timestamps, customer/product/order counts, and trigger eligibility.
3. Compare representative aggregate facts with current Shopify authority without exposing customer
   data. Distinguish native Shopify integration data from custom REST imports.
4. For an automation, trace every required field and event from Shopify to MailerLite and prove its
   update cadence, null behavior, and exit behavior.
5. Report missing catalog categories, stale products, unsynced customers, disabled shop state, cap
   pressure, and triggers that would remain broken.
6. Apply ecommerce mutations only when the user explicitly requests the exact connection or resource
   change. Re-fetch and verify after every write.

Do not change products, orders, customers, fulfillment, billing, or Shopify production state outside
the expressly approved MailerLite integration operation.
