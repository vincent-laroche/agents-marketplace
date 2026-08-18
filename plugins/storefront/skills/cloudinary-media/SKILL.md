---
name: cloudinary-media
description: Select, link, and deliver Hair Solutions Co. media from Cloudinary (cloud dtmizxj1n) for the storefront. Use whenever choosing imagery, building delivery URLs/srcset, or wiring media into sections, products, collections, blogs, or pages. AssetLink for products/collections/blogs; Files CDN for pages.
---

# Cloudinary media

Cloudinary is the source of truth for ALL website media. Full folder tree + rules in `references/cloudinary-map.md`. Cloud: `dtmizxj1n`. Use the `cloudinary` / Cloudinary Asset Management connector to search and verify assets before referencing them.

## The rule
- **Products, collections, blogs → AssetLink.** Link the Cloudinary asset to the Shopify object. Do not duplicate into theme `assets/`.
- **Pages / section image settings → push the Cloudinary file to the Shopify Files CDN, then use that URL.**
- Never copy media into the theme repo `assets/`.

## Finding assets
Search by folder/tag with the connector (e.g. `search-assets`, `visual-search-assets`, `list-images`). Product spec imagery for the order picker lives in `03_shopify_assets/02_products_assets/product-specs/{hairline-shape,hair-direction,curl-pattern}`. Model shots in `factory-models/<base>`. About-us in `03_shopify_assets/02_about_us/*`.

## Delivery URLs
`https://res.cloudinary.com/dtmizxj1n/image/upload/<transforms>/<public_id>.<ext>`
- Baseline: `f_auto,q_auto,c_fill,g_auto,w_<width>`. Provide responsive `srcset`.
- LCP/hero: explicit width, `fetchpriority="high"`, no lazy-load.
- Preserve public IDs, alt text, crop intent, aspect ratio. Confirm a transform exists before hardcoding (the `cloudinary-transformations` skill can validate syntax).

## Secrets
`CLOUDINARY_ASSET_LINK_API_KEY` in `/Users/vMac/.env` (read via Desktop Commander). Needed only for raw Admin API calls outside the connector. Never expose it.
