---
name: metaobjects-metafields
description: Work with Hair Solutions Co. Shopify metaobjects and metafields in Liquid — product specs, hair colors, order-picker options, product/collection page content blocks, FAQ sets. Use when reading or wiring metaobject/metafield data into theme code.
---

# Metaobjects & metafields

Full live map (24 definitions, fields, namespaces) in `references/metaobjects.md`. Re-verify against Shopify before relying on a field — definitions evolve.

## Liquid access rules
- Always read with `.value`: `product.metafields.custom.product_page_profile.value`.
- Resolve a metaobject reference, then a field: `...product_page_profile.value.content_block_1.value.title.value`.
- Never pipe inside bracket expressions — assign first.
- For lists (`list.metaobject_reference`), loop and read each `.value`.

## The spine
- PDP content comes from `custom.product_page_profile` → specs (`spec_*`) + `content_block_1/2` (each `title, body, image, cta_*`).
- Collection content from `collection_page_profile` → `content_block_1..3` (block 1 also has `cloudinary_image` URL).
- Order-picker options are metaobjects `curl_pattern`, `front_contour`, `hair_direction` (+ `haircolor` swatches), each with `label, value, image, addon_product, price, sort_order` — see the `custom-order-options-picker` skill.

## FAQ
Visible FAQ uses `faq_item` / `faq_set`. The `component-faq` section renders `faq_item` blocks. Add FAQ JSON-LD only when the FAQ is visible on the page. Legacy `kb_faq` is dead — ignore it.

## Editing definitions
Use the Shopify connector GraphQL (`metaobjectDefinitions`, `metafieldDefinitions`) to inspect; get explicit approval before creating/changing definitions (it affects live data). Don't touch `shopify--*` taxonomy objects.
