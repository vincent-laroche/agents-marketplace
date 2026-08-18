---
name: storefront-build
description: Write or edit Liquid sections/blocks/snippets for the hairsolutions.co storefront (Horizon 4.1.1) with the Hair Solutions design system. Use for any .liquid section, block, snippet, schema, or theme-editor wiring. Single Color Palette, OKLCH tokens, Instrument Serif/Geist.
---

# Storefront build (Horizon 4.1.1 + design system)

Everyday skill for writing theme code. Read `references/theme-map.md` for the section/template/collection map. For customer-facing visual/copy work, also load the `hair-solutions-co-design` skill (`/Users/vMac/06_storefront/Hair Solutions Co. Design System/SKILL.md`) and link its `styles.css` — never hardcode tokens.

## Horizon 4.1.1 rules
- ONE **Color Palette** (color schemes are gone): use `settings.color_palette.background` / `settings.color_palette.foreground`. Do not add scheme settings.
- OS 2.0 architecture: sections + theme blocks (`{% content_for 'blocks' %}`), `{% schema %}` with stable setting IDs and presets. Preserve `block.shopify_attributes` on every rendered block.
- New custom components use the `hs-custom-*` prefix. Reuse existing blocks/snippets (see theme-map) before inventing.
- Liquid: use `.value` for metaobject/metafield values; never pipe inside `[ ]` (assign first); use whitespace control.
- Inspect nearby files first; make small focused diffs. Don't modify app-managed `ecom-*`/`ss-*`/`foxify-*`.

## Definition of Done (check every item before committing)
- Corners ≤4px UI / ≤8px cards. Pills only for badges/chips.
- Colors: OKLCH design-system tokens only. No hardcoded hex.
- Type: Instrument Serif (display/H1/H2), Geist (H3↓/body/UI), Geist Mono (prices/specs/eyebrows). Nothing else.
- Shadows: two-layer card token (light + obsidian variants). No single-layer/glow/colored shadows.
- Spacing: 4px scale; `clamp()` for fluid sizing.
- Backgrounds: flat `--off-white` or `--obsidian`. No gradients/patterns/glass.
- Mobile: side padding 20–28px, no horizontal scroll, touch targets ≥44px. QA at 320/375/390/430.
- Accent `--clay`: once per view max, never on body text or light backgrounds.
- Schema/IDs stable, dynamic sources intact, theme-editor compatible.
- SEO: one H1, logical headings, semantic HTML, metadata/JSON-LD/internal links preserved, FAQ schema only for visible FAQ.

## Media
Cloudinary only — see `cloudinary-media` skill. AssetLink for products/collections/blogs; Files CDN for pages. Never duplicate into theme `assets/`.

When done, ship via `storefront-release`.
