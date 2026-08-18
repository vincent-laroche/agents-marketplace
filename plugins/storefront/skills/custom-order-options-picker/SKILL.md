---
name: custom-order-options-picker
description: Build and evolve the advanced Custom Order Options Picker for hairsolutions.co — the guided full-page flow (product.advanced-order template, hs-advanced-order-flow section) that lets customers spec a custom hair system. Use when working on the order picker, its question steps, or its metaobject-driven options. Work in progress.
---

# Custom Order Options Picker (advanced order flow)

A guided, full-page configurator for ordering a custom hair system. WORK IN PROGRESS — evolve it alongside Vincent. Distinct from inline PDP options (`custom-product-options`).

## Architecture
- Template: `templates/product.advanced-order.json`.
- Section: `hs-advanced-order-flow` with `question` blocks. Section settings: `intro_text`, `start_label`, `submit_label`.
- Each `question` block: `heading`, `description`, `property_key` (the cart line-item property written), `render_as` (`images` | `swatches`), `image_ratio`, `option_source` (`metaobject` | `color`), `metaobject_type`.

## Current steps (block_order)
1. Curl pattern — `metaobject_type: curl_pattern`, images, property "Curl Pattern" (straight included; waves/curls add the perm service at checkout).
2. Front contour — `front_contour`, images, property "Front Contour".
3. Hair direction — `hair_direction`, images, property "Hair Direction".
4. Hair colour — `option_source: color`, swatches, property "Hair Color".

## Data source
Options come from the metaobjects `curl_pattern` / `front_contour` / `hair_direction` (`label, value, image, addon_product, price, sort_order`) and the colour set. Images live in Cloudinary `03_shopify_assets/02_products_assets/product-specs/{curl-pattern,hairline-shape,hair-direction}` (see `cloudinary-media`). Add/edit options by editing the metaobjects, not by hardcoding.

## When extending
- Add a step = add a `question` block + (if metaobject-sourced) the metaobject entries with images and any `addon_product`/`price`.
- Keep `property_key` values stable and human-readable — fulfillment reads them off the order line item.
- Validate that selected add-ons resolve to real add-on products before charging.
- Follow `storefront-build` DoD; mobile-first (this flow is heavily used on phones — test 320/375/390/430). Ship via `storefront-release`.

## Reference
Inspect `sections/hs-advanced-order-flow.liquid` and `blocks/question.liquid` before editing.
