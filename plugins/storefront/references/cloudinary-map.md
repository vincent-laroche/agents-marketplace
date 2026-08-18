# Cloudinary map — Hair Solutions Co.

Cloud name: `dtmizxj1n`. Source of truth for ALL website media. Key in `/Users/vMac/.env` as `CLOUDINARY_ASSET_LINK_API_KEY` (read via Desktop Commander; never expose).

## The media rule (non-negotiable)
- **Products, collections, blogs → Cloudinary AssetLink.** Link the Cloudinary asset to the Shopify object; do not duplicate into theme `assets/`.
- **Pages (and section settings that take an image_picker) → push the Cloudinary file to the Shopify Files CDN, then reference the Files CDN URL.** Pages can't use AssetLink the same way.
- Never copy media into the theme repo `assets/` folder.
- Preserve public IDs, alt text, crop intent, aspect ratio. Use `f_auto,q_auto` and responsive widths.

## Folder taxonomy (numbered, ~250 folders)
- `01_media_library/` — `people-lifestyle/{hsc-models,before-after,stock-photos}`, `videos/{reels,raw-video,edited-video,b-roll,product-videos,...}`, `brand/fonts/...`, `design_components/{icons-ui,backgrounds-textures,graphics-design}`, `ai-generated/`, `competitors/`, `screenshots/`
- `02_marketing_assets/`
- `03_shopify_assets/`
  - `blog/`
  - `02_about_us/{hero,founder,process,testimonials,rebrand,lifestyle}`
  - `02_products_assets/`
    - `00_storefront_products/`
    - `factory-models/{HS1,HS7,HS1V,FRONTAL,...}` (per-base model shots)
    - `product-specs/{hairline-shape, hair-direction, curl-pattern}` ← **source images for the custom-order picker metaobjects**
- `shopify_assets/homepage/{hero,video}` — legacy homepage path (candidate for consolidation into `03_shopify_assets`)

## Delivery
Build URLs as `https://res.cloudinary.com/dtmizxj1n/image/upload/<transforms>/<public_id>.<ext>`.
Baseline transform: `f_auto,q_auto,c_fill,g_auto` + a width. Use srcset for responsive. Hero/LCP images: explicit width + `fetchpriority="high"`, no lazy.
Prefer named transformations if defined in the account; otherwise inline. Verify with the `cloudinary` connector/skills before hardcoding.
