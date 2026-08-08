# Hair Solutions Co. context

## Canonical sources

- Full-design individual pages: `/Users/vMac/06_storefront/atelier-zero-storefront/workspace/full`
- Wireframe individual pages: `/Users/vMac/06_storefront/atelier-zero-storefront/workspace/wireframes`
- Full-design review board: `/Users/vMac/06_storefront/atelier-zero-storefront/workspace/reference/workspace-page-review-boards/full-design-review-board.html`
- Wireframe review board: `/Users/vMac/06_storefront/atelier-zero-storefront/workspace/reference/workspace-page-review-boards/wireframes-review-board.html`
- Brand source of truth: `/Users/vMac/08_brand`
- Creative Production status log: `/Users/vMac/01_projects/creative_production_and_media/PROJECT.md`

Verify all paths before use. The individual page folders are import sources. The review boards are visual indexes only.

## Intended Figma architecture

Use one Figma project for the storefront visualization system, with separate files for wireframes, editable full-design source, and the Figma Sites presentation. Keep wireframes in Figma Design by default. Use one Figma Sites webpage per full-design Shopify route.

```text
Shopify Storefront
├── Wireframes (Figma Design)
│   ├── Home
│   ├── Collection
│   └── ...
├── Full Design Source (Figma Design)
│   ├── Home
│   ├── Collection
│   └── ...
└── Storefront Simulator (Figma Sites, unpublished)
    ├── Home
    ├── Collection
    └── ...
```

Each full-design webpage contains responsive layouts, and each layout contains independently movable sections.

```text
Home
├── Desktop — 1440 (primary)
├── Desktop — 1280
├── Mobile — 480
└── Mobile — 375
```

The current HTML folders each contain 40 files but only 19 logical routes: 20 desktop files and 20 mobile files, with `index.html` and `mobile/index.html` acting as Home aliases. Prefer `home.html` and `mobile/home.html`; never create separate Index webpages.

The inventory script groups routes using `body[data-page]`. Treat its selected desktop/mobile files as the import manifest. A filename is not automatically a final Shopify URL slug; verify route URLs against the current theme or live navigation before adding interactions.

## Section naming

Use two-digit ordering so the Layers panel remains scannable and rearrangement is safe:

```text
Desktop / Page Background
Desktop / 00 Header
Desktop / 01 Hero
Desktop / 02 Brand Story
Desktop / 03 Collections
...
Desktop / 11 Footer
```

Use the equivalent `Mobile /` prefix inside mobile layouts. Keep header and hero separate even if the source HTML visually overlays them.

## Breakpoint policy

For captured HTML, preserve four visual targets: 1440, 1280, 480, and 375. They document exact existing renderings.

For a later native Figma Sites rebuild, two responsive breakpoints—Desktop and Mobile—may be enough if every section is fluid and verified across the intervening widths. Do not delete fidelity captures merely to make the panel look smaller.

## Safety boundary

This workflow is a Figma visualization and design-management task. It does not authorize:

- Shopify theme edits
- Shopify CLI or theme preview usage
- production deployment or publication
- customer, product, order, or storefront-data changes
- Figma Sites publication

Leave all Figma Sites work unpublished until Vincent explicitly approves publication.
