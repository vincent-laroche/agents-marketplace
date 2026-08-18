---
name: custom-product-options
description: "Build and edit the Hair Solutions Co. custom product options on PDPs — non-variant choices rendered as radios, checkboxes, and swatches that write cart line-item properties."
---

# Custom product options (PDP)

Custom, non-variant product options on hair-system PDPs. Choices render as radios/checkboxes/swatches and attach as **cart line-item properties** (not Shopify variants), with optional add-on pricing.

## Building blocks (blocks/)
- `hs-custom-product-options-module.liquid` — the options container on the PDP.
- `hs-custom-product-options-modal.liquid` — modal variant of the picker.
- `hs-custom-property-radio.liquid`, `hs-custom-property-checkbox.liquid`, `hs-custom-property-swatch.liquid` — individual inputs.
- `hs-custom-system-configurator.liquid`, `option_group.liquid`, `product-custom-property.liquid`, `question.liquid` — grouping/config.

## Engine contract (read before editing)
- JS: `assets/hs-customization-engine.js` — state, price recompute, line-item property assembly, validation.
- Treat the current Liquid blocks, engine source, project `AGENTS.md`, and relevant tests as the contract. If they disagree or leave order-critical behavior unclear, stop and request a scoped decision before changing it.

## Conventions
- Options source from metaobjects (see `metaobjects-metafields`) — `label/value/image/addon_product/price/sort_order`. Don't hardcode option lists.
- Line-item property keys are human-readable (e.g. "Front Contour"). Keep keys stable — orders and fulfillment depend on them.
- Add-on price changes happen via `addon_product` line items / checkout, not by faking variant prices.
- Inspect the existing block + engine before adding inputs; preserve `block.shopify_attributes` and the engine's expected `data-*` hooks.

## Related
For the full-page guided flow (separate from PDP inline options), use `custom-order-options-picker`.
Follow `storefront-build` design system + DoD; accessibility: real labels, keyboard, ≥44px targets.
