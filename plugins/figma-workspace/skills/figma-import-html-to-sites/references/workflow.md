# HTML to editable Figma Sites workflow

## Contents

1. Preflight
2. Inventory the HTML
3. Serve local pages safely
4. Capture into Figma Design
5. Normalize editable structure
6. Separate header and hero
7. Build Figma Sites webpages
8. Validate
9. Scale to all routes

## 1. Preflight

1. Read the relevant `PROJECT.md` and `AGENTS.md` files.
2. Verify the source directories and inspect a representative individual HTML page.
3. Confirm linked images, fonts, stylesheets, and scripts resolve locally.
4. Confirm an existing Figma Design file or create one before capture.
5. Confirm the Figma connector can import a local webpage and edit Figma nodes.
6. Confirm Figma Desktop is available for Figma Sites actions.
7. Record the current publication state. Keep the site unpublished.

Do not start with the review-board HTML. It is a dashboard of pages and will become one giant block instead of independent pages.

## 2. Inventory the HTML

Run the bundled inventory script against each source directory:

```bash
python3 scripts/inventory_html_pages.py \
  "/Users/vMac/06_storefront/atelier-zero-storefront/workspace/full"

python3 scripts/inventory_html_pages.py \
  "/Users/vMac/06_storefront/atelier-zero-storefront/workspace/wireframes"
```

Review:

- individual page count
- logical route count and desktop/mobile pairing
- aliases that must not become separate webpages
- inferred page names and kinds
- board-like files that must not be imported as pages
- missing local asset references
- absolute local paths that may fail in Figma capture

Choose one representative route—normally Home—as the pilot. Prefer `home.html` and `mobile/home.html`; `index.html` files are Home aliases. Do not batch the whole site before proving the structure.

## 3. Serve local pages safely

Use a lightweight static HTTP server rooted at the HTML source directory because browser capture commonly rejects or mishandles `file://` assets. Use any free local port and retain the process only for the capture session.

Use the static server rather than `shopify theme dev` or port 9292 for this capture — the source here is exported HTML, not the live theme. (`shopify theme dev` itself is permitted in the storefront repo; Vincent's ruling, 2026-08-17.)

Open the pilot URL locally and verify that images, fonts, backgrounds, and responsive behavior match the source before sending it to Figma.

Do not assume every HTML file is already capture-enabled. At the time this skill was created, only the full-design Home desktop/mobile files contained Figma's capture script. Follow the current import tool's generated capture instructions for each URL. Prefer a temporary staged copy or a reversible tool-managed injection; do not permanently modify every canonical HTML source file just to add the capture script.

## 4. Capture into Figma Design

Use editable design capture, not a screenshot upload.

1. Resolve the destination Figma Design file key.
2. Start one capture for one page URL.
3. Poll the capture until it completes. Use a fresh capture ID for every page.
4. Target the same Figma Design file for all routes.
5. Name the imported top-level frame with the route and width.
6. Capture the source at the four target widths when the HTML contains responsive differences that cannot be reconstructed reliably from one capture.

Treat the captured result as raw source material. Do not transfer it to Figma Sites before normalizing the layer tree.

## 5. Normalize editable structure

Create or normalize one top-level layout frame per target width:

```text
Desktop — 1440
Desktop — 1280
Mobile — 480
Mobile — 375
```

Use vertical auto layout for the page stack. Convert every major HTML section into a direct named child. Keep background treatment at the layout-frame level whenever possible; a full-page background image or frame must remain behind all content and locked.

Use numbered section names. Preserve actual text and image layers inside each section. Do not flatten sections into images.

Verify section order in the Layers panel, not only on the canvas. Figma Sites uses layer structure when matching responsive variants.

## 6. Separate header and hero

The header must be a direct sibling immediately before the hero.

When the raw capture nests the header inside the hero:

1. Identify the page wrapper, hero frame, header frame, and hero-body frame.
2. Move the header out of the hero and insert it immediately before the hero in the wrapper.
3. Rename it `Desktop / 00 Header` or `Mobile / 00 Header`.
4. Give the header its own explicit width and fixed height.
5. Inspect whether the header background is transparent. If it relied on the hero's dark background, apply the same inspected source or brand-backed fill to the header itself.
6. Subtract the header height from the hero height so the combined page height does not grow.
7. Reset inherited minimum-height constraints on the hero and hero body before resizing.
8. Keep the hero body inside the hero and preserve its internal padding.
9. Repeat the operation independently for every responsive layout.

Equivalent node-edit logic:

```javascript
wrapper.insertChild(heroIndex, header)
header.name = "Desktop / 00 Header"
body.minHeight = null
body.layoutSizingVertical = "FIXED"
body.resize(body.width, correctedBodyHeight)
hero.minHeight = null
hero.layoutSizingVertical = "FIXED"
hero.resize(hero.width, correctedHeroHeight)
```

Use measured values from the actual nodes. Never paste hardcoded node IDs or heights from another page.

## 7. Build Figma Sites webpages

Create one Figma Sites webpage for each Shopify route. Responsive layouts are children of that webpage, not separate webpages.

Keep the wireframe set in a separate Figma Design file/page by default. Create a second unpublished Figma Sites file for wireframes only when explicitly requested; never mix wireframe and full-design breakpoints under the same route page.

For the pilot Home page:

1. Create or select the Home webpage.
2. Add `Desktop — 1440` once and make it primary.
3. Add `Desktop — 1280` once.
4. Add `Mobile — 480` once.
5. Add `Mobile — 375` once.
6. Confirm the layout widths in the right sidebar. Labels alone are not authoritative.
7. Collapse the layer tree after verification so the four layouts are easy to scan.

Avoid repeated `Paste Over Selection`. Pasting a 1440 frame over an existing 1440 layout can create another desktop breakpoint instead of replacing content. If a duplicate appears, undo immediately and recount before proceeding.

Turn off `Always select matching layers` while repairing one breakpoint. Select the explicit breakpoint row, not the webpage label, because selecting the webpage may select matching nodes in every layout.

## 8. Validate

Perform structural and visual checks.

### Structure

- One webpage exists for the route.
- Exactly four layouts exist for the captured-HTML strategy.
- Actual widths are 1440, 1280, 480, and 375.
- Header and hero are separate direct siblings.
- Header is first, hero is second, and footer is last.
- Desktop and mobile sections do not coexist visibly in the wrong breakpoint.
- Every section is individually selectable and movable.

### Visuals

- Compare the full Figma layout with the local HTML at the same width.
- Inspect the header in isolation; it must still have the correct background.
- Check the header-to-hero boundary for a blank strip, overlap, or double height.
- Check the page background and z-order.
- Use full preview and resize around breakpoint boundaries.
- Confirm images, fonts, CTA styling, and section spacing.

### Safety

- Confirm the Figma Site is still unpublished.
- Confirm Shopify was not modified.
- Stop the temporary local static server after captures are complete.

## 9. Scale to all routes

Only after Home passes validation:

1. Repeat capture and normalization for the remaining individual HTML files.
2. Reuse naming and section-order conventions.
3. Create one Figma Sites webpage per route.
4. Validate every route at all intended widths.
5. Update the project status log with completed routes, limitations, and next work.

Do not assume a successful Home import proves pages with product forms, accordions, video, or complex interactions. Validate those route types separately.
