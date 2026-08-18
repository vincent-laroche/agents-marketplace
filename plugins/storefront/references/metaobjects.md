# Metaobjects & metafields map — Hair Solutions Co.

Live as of 2026-06-27 (24 metaobject definitions). Access values in Liquid with `.value`; never pipe inside bracket expressions (assign first). Metaobject references resolve via `.value` then field key.

## Custom-order picker options (drive `hs-advanced-order-flow`)
Each: `label`, `value`, `image` (file_reference), `addon_product` (product_reference), `price` (money), `sort_order` (int).
- `curl_pattern` — Product Data - Curl Pattern (straight included; waves/curls add perm service)
- `front_contour` — Product Data - Front Contour (hairline shape)
- `hair_direction` — Product Data - Hair Direction
- `haircolor` — Product Data - Hair Color (`color_code, color_name, gray_percentage, color_family, swatch_image, preview_image`)

## Product data
- `base_size` (`size, code`)
- `density` (`label, percentages_range`)
- `material` (`name, type, image, summary, pros[], cons[], care_tips`)
- `specs_hair_colors_available` (`label, key, numero, color_with_gray, percentage_gay, swatch_image, related_product, hair_color_options[]`)

## Product page
- `product_page_profile` — specs (`spec_base_thickness, spec_density, spec_average_lifespan, spec_base_material, spec_hair_length, spec_curl_pattern, spec_hairline_shape, spec_base_size, spec_hairline_details, spec_care_recommendations, spec_hair_type, spec_hair_direction`) + `title, subtitle, content_block_1, content_block_2` (metaobject refs)
- `product_page_content_block_1` / `product_page_content_block_2` — `title, body (rich_text), image (file_reference), cta_label, cta_url`
  - Bound on PDP via `closest.product.metafields.custom.product_page_profile.value.content_block_1.value.*`

## Collection page
- `collection_page_profile` — `title, content_block_1..3`
- `collection_page_content_block_1` — includes `cloudinary_image` (url) in addition to `image` (file_reference)
- `collection_page_content_block_2` / `_3` — `title, body, image, cta_label, cta_url`

## FAQ
- `faq_item` — `question, answer, category, tags[], display_order, object_type, object_handle`
- `faq_set` — `set_title, description, faq_items[] (refs), display_style`
- NOTE: legacy `kb_faq` is dead — do not build against it.

## Services
- `service` — `label, price (money), description, applies_to[] (products), addon_product, group, sort_order`
- `guide` — `title, body, cta_label, cta_url`

## Shopify standard (do not edit)
`shopify--hair-type, shopify--age-group, shopify--fabric, shopify--target-gender, shopify--color-pattern` (taxonomy-managed).

## Key product metafield namespace
`custom.product_page_profile` (metaobject_reference) — the spine of the hair-systems PDP.
