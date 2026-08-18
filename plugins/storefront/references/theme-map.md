# Theme map — Hair Solutions Co. storefront

- Store: `one-head-hair.myshopify.com` → `hairsolutions.co`. Theme: Horizon **4.1.1** (GitHub sync).
- **Git repo (the only thing that deploys):** `/Users/vMac/06_storefront/shopify_github_synched_theme_files` → `github.com/vincent-laroche/storefront`.
  - `main` = live. `dev` = experimental (kept fast-forwarded to main by `sync-dev.yml`).
  - Parent `/Users/vMac/06_storefront` is the project root (design system, brand, tooling) — NOT the deploy repo. Edits there do not deploy.
- **No Shopify CLI. No theme dev server.** Ever. Only local repo ↔ GitHub.

## Horizon 4.1.1 — what changed
- Color schemes are gone. There is ONE **Color Palette**: reference `settings.color_palette.background` and `settings.color_palette.foreground` (seen throughout `product.hair-systems.json`). Do not reintroduce scheme settings.

## Product templates (templates/)
- `product.hair-systems.json` — main PDP. `product-information` section; specs/content from `metafields.custom.product_page_profile`; renders `hs-custom-product-subtitle`, `hs-custom-product-specs`, `hs-custom-breadcrumbs`; add-on services (ai_gen block); variant picker; FAQ via `component-faq`; product recommendations.
- `product.advanced-order.json` — **Custom Order Options Picker**. Section `hs-advanced-order-flow` with `question` blocks → metaobjects `curl_pattern`, `front_contour`, `hair_direction` + colour swatches. Writes line-item properties (Curl Pattern, Front Contour, Hair Direction, Hair Color). Perm add-on charged at checkout.
- `product.custom-hair-systems.json`, `product.json` (default).

## Help Center (custom, page-per-item)
- `page.help-center.json` — section `hs-help-home` (9 categories → `/pages/help-center-*`, search, contact footer).
- `page.hc-category.liquid` — category template.
- `page.hc-article.liquid` — article template.

## Custom product options (on PDPs)
Blocks: `hs-custom-product-options-module.liquid`, `hs-custom-product-options-modal.liquid`, `hs-custom-property-radio/checkbox/swatch.liquid`, `hs-custom-system-configurator.liquid`, `option_group.liquid`, `product-custom-property.liquid`, `question.liquid`.
Engine: `assets/hs-customization-engine.js`. Read the current Liquid blocks, engine source, project `AGENTS.md`, and relevant tests together as the contract.

## Key custom sections (sections/, prefix hs-custom-* / hs-*)
Home: `hs-custom-hero`, `hs-custom-hero-floating`, `hs-home-*`, `hs-custom-collections-bento`, `hs-custom-process-steps`, `hs-custom-feature-grid`, `hs-custom-big-statement`, `hs-custom-cta`, `hs-custom-testimonials`, `hs-custom-stats-band`, `hs-custom-press-logos`, `hs-custom-editorial-fullbleed`.
PDP/specs: `hs-custom-product-specs` (snippet), `hs-custom-product-page-content`, `hs-custom-product-model-card`.
Contact/help: `hs-contact-support-cards`, `hs-contact-faqs`, `hs-custom-help-center`, `hs-kb-*`.
FAQ: `component-faq` (block type `faq_item`).

## Collections (smart, tag-driven)
By base: `lace-hair-systems`, `skin-hair-systems`, `mono-hair-systems`, `frontal-hair-systems`, `hybrid-hair-systems`. Plus `mens-hair-systems` (`type:hair-system`), `stock-hair-systems` (Ready-to-Wear = `type:hair-system` AND NOT `custom`), `custom-hair-systems` (`type:hair-system` AND `custom`), `light-density`, `indian-remy-hair`, `best-sellers`.
Tag taxonomy: `type:hair-system`, `custom`, `base:{lace,skin,mono}`, `material:{french-lace,swiss-lace,monofilament}`, `front:{lace,skin}`, `perimeter:skin`, `coverage:front-only`, `density:{90,100}`, `hair.quality:remy`, `collection:*`.
Accessory collections (tapes, liquid-adhesives, removers-and-solvents, hair-care, scalp-prep, maintenance) exist but are currently empty.

## Theme rules (enforced)
Preserve `block.shopify_attributes`, schema/setting IDs, dynamic sources, metafields, app blocks. Don't touch app-managed `ecom-*`, `ss-*`, `foxify-*`. New components use `hs-custom-*`. Mobile QA at 320/375/390/430. OKLCH tokens only; design system `styles.css` is the only CSS to link.
