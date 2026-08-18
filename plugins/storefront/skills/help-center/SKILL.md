---
name: help-center
description: Build and maintain the custom Hair Solutions Co. Help Center — the three templates (Home, Category, Article) and their sections. Use when adding/editing help categories, category pages, or articles, or wiring FAQ content into them.
---

# Help Center (custom, page-per-item)

A bespoke 3-level Help Center: Home → Category → Article. Built page-per-item (metaobject URL templates don't route on this theme), so each category/article is a real Shopify page using a custom template.

## The three templates (templates/)
- `page.help-center.json` — Home. Section `hs-help-home`: eyebrow/heading/subheading, optional search, a `category` block per topic (title, description, url, optional `coming_soon`/`soon_label`), and a contact footer (contact + editorial links).
- `page.hc-category.liquid` — Category landing. Lists the articles within one category.
- `page.hc-article.liquid` — Single article.

## Current categories (Home blocks → pages)
Getting started, Products & selection, Orders & shipping, Billing & payment, Account & support, Troubleshooting, Quick tips, Affiliate program, Pro & wholesale (coming soon). Each links to `/pages/help-center-<slug>`.

## How to add content
1. Create the Shopify page and assign the matching template (`page.hc-category` or `page.hc-article`).
2. For a new category, add a `category` block to `hs-help-home` pointing at the new page URL.
3. FAQ-style content uses `faq_item`/`faq_set` metaobjects (see `metaobjects-metafields`). Add FAQ JSON-LD only where the FAQ is visibly rendered.

## Rules
- Keep the IA consistent: Home is the canonical entry; don't fork parallel FAQ systems. Legacy `kb_*` templates/metaobjects are being retired — don't extend them.
- Follow `storefront-build` design system + DoD. Inspect the liquid templates before editing.
- Contact page leads with self-service; Help Center is the canonical FAQ owner.
