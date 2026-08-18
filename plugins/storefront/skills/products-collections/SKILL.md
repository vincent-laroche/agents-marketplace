---
name: products-collections
description: Understand the Hair Solutions Co. product catalog and collection structure — hair-system bases, tag taxonomy, smart collection rules, and which product template each uses. Use when building/editing PDPs, collection pages, merchandising, or anything keyed to product type/tags.
---

# Products & collections

Full map in `references/theme-map.md` (collections + tag taxonomy) and `references/metaobjects.md` (PDP data). Re-verify live with the Shopify connector (`search_products`, `search_collections`, `graphql_query`).

## Catalog shape (live)
42 active products: ~22 Hair System, ~15 Order Add-on, 2 Service Add-on. Add-ons back the PDP add-on-services and the order picker (perm, haircut, cut-to-size).

## Collections (smart, tag-driven)
- By base: `lace-hair-systems`, `skin-hair-systems`, `mono-hair-systems`, `frontal-hair-systems`, `hybrid-hair-systems`.
- `mens-hair-systems` = `type:hair-system`.
- `stock-hair-systems` (Ready-to-Wear) = `type:hair-system` AND NOT `custom`.
- `custom-hair-systems` = `type:hair-system` AND `custom`.
- Attribute collections: `light-density`, `indian-remy-hair`, `best-sellers`.
- Accessory collections (tapes, liquid-adhesives, removers-and-solvents, hair-care, scalp-prep, maintenance) exist but are empty.

## Tag taxonomy (drives collections + filters)
`type:hair-system`, `custom`, `base:{lace,skin,mono}`, `material:{french-lace,swiss-lace,monofilament}`, `front:{lace,skin}`, `perimeter:skin`, `coverage:front-only`, `density:{90,100}`, `hair.quality:remy`, `collection:*`.
When adding a product to a collection, set the tags the smart rule expects — don't hand-add to smart collections.

## Templates
- `product.hair-systems.json` — main PDP (see `storefront-build` + `metaobjects-metafields`).
- `product.advanced-order.json` — custom order picker (see `custom-order-options-picker`).
- `product.custom-hair-systems.json`, default `product.json`.

## Rules
Never change product/inventory/price data without explicit approval. Read-only browsing is fine; mutations need a go-ahead.
