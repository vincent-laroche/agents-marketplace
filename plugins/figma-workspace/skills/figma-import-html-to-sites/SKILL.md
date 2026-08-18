---
name: figma-import-html-to-sites
description: Import individual local HTML storefront pages into Figma Design, normalize them into editable named sections and responsive layouts, and assemble them as Figma Sites webpages. Use for Hair Solutions Co. wireframes or full-design HTML, Shopify page visualization in Figma, breakpoint cleanup, header/hero separation, or repairing a Figma Sites import that became flattened, duplicated, mixed across breakpoints, or visually incorrect.
---

# Import HTML to Figma Sites

Build a visual storefront workspace, not a production Shopify site. Preserve editability, section-level rearrangement, responsive fidelity, and a clean one-webpage-per-route structure.

## Load the right guidance

- Read [references/hair-solutions-context.md](references/hair-solutions-context.md) for canonical paths, naming, safety boundaries, and target structure.
- Read [references/workflow.md](references/workflow.md) before performing an import or repair.
- Read [references/troubleshooting.md](references/troubleshooting.md) whenever the layer tree, header, backgrounds, breakpoints, or Figma Sites behavior differs from the expected result.

## Required capabilities

Use the Figma connector for editable design capture and node edits. Use Computer Use only for Figma Desktop or Figma Sites actions that the connector cannot perform. Prefer these operations when available:

- Generate/import design from a local webpage URL into an existing Figma Design file.
- Inspect and edit Figma nodes programmatically.
- Capture Figma screenshots for visual verification.
- Control Figma Desktop for Figma Sites setup and breakpoint management.

If editable capture is unavailable, stop and name the missing capability. Do not silently substitute a PNG. Use PNGs only as visual references or user-approved temporary placeholders.

## Core workflow

1. Inspect the current project status and real source paths before touching Figma.
2. Inventory individual HTML files with `scripts/inventory_html_pages.py`. Group desktop/mobile files by `body[data-page]`, exclude aliases such as `index.html` from separate webpage creation, and treat combined review boards as references.
3. Select one route as a pilot. Capture its individual HTML into Figma Design before scaling to all routes.
4. Normalize the imported layer tree into explicit responsive page frames and numbered sibling sections.
5. Separate the header from the hero. Give the header its own background, sizing, and responsive variant.
6. Create one Figma Sites webpage per Shopify route. Add only the intentional responsive layouts.
7. Verify layer structure, visual parity, responsive behavior, and breakpoint count.
8. Leave the Sites file unpublished unless Vincent explicitly approves publication.
9. Update the relevant `PROJECT.md` after meaningful work.

## Import contract

For static HTML parity, create exactly these four layouts unless the source defines a different deliberate target:

- `Desktop — 1440` (primary)
- `Desktop — 1280`
- `Mobile — 480`
- `Mobile — 375`

Use two native responsive breakpoints only when rebuilding the page responsively by hand. Do not pretend four fixed HTML captures are a fluid two-breakpoint implementation.

Inside every layout, use this sibling order:

```text
Page Background
00 Header
01 Hero
02 ...
03 ...
...
11 Footer
```

Never nest `00 Header` inside `01 Hero`. Never leave the header transparent if its original appearance depended on the hero background.

## Operating rules

- Import individual HTML pages one at a time. Do not import a combined dashboard or review board as the page source.
- Preserve text, images, containers, and sections as editable layers.
- Keep desktop and mobile variants in separate responsive layout frames.
- Keep wireframes in a separate Figma Design file/page by default. Build Figma Sites webpages from the full-design HTML unless Vincent explicitly requests an interactive wireframe Site.
- Inspect `/Users/vMac/08_brand` before creating new customer-facing styling. Existing imported styling may be preserved without reinterpretation.
- Prefer a lightweight static server for local HTML in this workflow — it is the right tool for a static export. (`shopify theme dev` is permitted in the storefront repo; Vincent's ruling, 2026-08-17. It is simply not needed here.)
- Never modify, deploy, or publish the Shopify storefront as part of this workflow.
- Never publish the Figma Site without explicit approval.
- Re-query the Figma Desktop state after every meaningful UI action. Do not reuse stale UI element identifiers.
- Prefer undo or a clean rebuild when Figma Sites auto-matching contaminates several breakpoints. Do not keep layering workarounds onto a corrupted page.

## Completion checklist

- Confirm there is one webpage per route, not one webpage per breakpoint.
- Confirm the expected breakpoint count and actual widths.
- Confirm `00 Header` and `01 Hero` are separate siblings in every layout.
- Confirm the header has its own visible background and is first in the page stack.
- Confirm sections are individually selectable and movable.
- Confirm no combined board or full-page PNG is masquerading as editable content.
- Confirm desktop-only layers are not visible in mobile layouts and vice versa.
- Confirm visual parity with the source HTML at all target widths.
- Confirm the Figma Site remains unpublished unless approval was given.

Report the Figma file/site name, routes imported, responsive layouts, structural fixes, verification performed, remaining limitations, and publication status.
