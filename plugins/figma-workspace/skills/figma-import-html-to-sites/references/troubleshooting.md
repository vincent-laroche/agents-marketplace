# Figma import troubleshooting

## Contents

1. One giant immovable block
2. Duplicate desktop or mobile layouts
3. Header appears blank or cream
4. Header is still part of the hero
5. Header detachment creates extra height
6. Background covers or displaces the header
7. Desktop and mobile layers become mixed
8. Selecting one layout selects several
9. Width labels show 1281 or 376
10. Delete or replace affects the wrong breakpoint
11. Temporary image layers appear in the header
12. UI automation clicks the wrong item
13. When to rebuild instead of patch
14. Duplicate Home or Index webpages
15. Capture works only for Home

## 1. One giant immovable block

**Cause:** The combined review board or a full-page PNG was imported.

**Fix:** Import each individual HTML file separately with editable design capture. Normalize its major sections into direct named children. Keep the board only as a visual reference.

**Do not:** Break a board screenshot into arbitrary crops and call them editable sections.

## 2. Duplicate desktop or mobile layouts

**Cause:** `Paste Over Selection` or a repeated paste created a new breakpoint at an existing width.

**Fix:** Undo immediately or remove the newly created duplicate while its identity is certain. Then verify the actual width and recount all layouts.

**Expected captured-HTML result:** one 1440 desktop, one 1280 desktop, one 480 mobile, and one 375 mobile layout.

## 3. Header appears blank or cream

**Cause:** The imported header was transparent and originally relied on the hero's dark background. Once separated, the page background shows through.

**Fix:** Give the header frame its own opaque fill using the inspected source value or current brand source. Verify the header in isolation.

**Do not:** Use an opaque header PNG as the finished solution. It hides the symptom while sacrificing editability.

## 4. Header is still part of the hero

**Cause:** Visual capture preserved the DOM nesting even though the desired Figma structure differs.

**Fix:** Move the header node out of the hero and insert it immediately before the hero in the page wrapper. Rename both sections explicitly and verify their indentation in Layers.

## 5. Header detachment creates extra height

**Cause:** The hero retained its original height after the header was removed, or a minimum-height constraint prevented resizing.

**Fix:** Clear inherited `minHeight` on the hero and hero body, set vertical sizing to fixed where appropriate, and subtract the measured header height from the hero/body height. Recheck the next section boundary.

## 6. Background covers or displaces the header

**Cause:** A captured page-background frame remains in the content stack or has a higher z-order.

**Fix:** Prefer the layout frame's background fill. If a background layer is required, move it behind content, make it absolute if appropriate, lock it, and verify it does not participate in vertical auto layout.

## 7. Desktop and mobile layers become mixed

**Cause:** Figma Sites matched same-named layers across breakpoints, or desktop and mobile source layers were copied into the same layout.

**Fix:** Disable `Always select matching layers`, isolate one breakpoint, and verify visibility. Use distinct top-level layout names while keeping corresponding section names consistent inside the correct layout only.

If several layouts are already contaminated, revert or rebuild the Home webpage from the clean Figma Design source.

## 8. Selecting one layout selects several

**Cause:** The webpage label or a matching-layer group was selected instead of the explicit breakpoint row.

**Fix:** Press Escape, click the exact breakpoint row, confirm the right sidebar shows its width, and only then edit. Re-query the UI state before the next action.

## 9. Width labels show 1281 or 376

**Cause:** Figma generated names from scaled copies or rounded bounds.

**Fix:** Inspect the actual width field. If it is 1280 or 375, rename the layout to the real width. If the actual width is wrong, resize the top-level layout before renaming.

Labels are descriptive; the right-sidebar dimensions are authoritative.

## 10. Delete or replace affects the wrong breakpoint

**Cause:** Multiple matching layouts were selected, the UI element reference was stale, or the page wrapper was selected.

**Fix:** Undo, collapse the tree, refresh the Figma Desktop state, isolate the exact row, and confirm one-item selection. Prefer context actions whose target name and width are visible.

## 11. Temporary image layers appear in the header

**Cause:** A screenshot or opaque header PNG was pasted while troubleshooting transparency.

**Fix:** Remove the temporary image after reconstructing the header with native editable layers and a real frame fill. Verify logo, navigation, actions, and background remain editable.

## 12. UI automation clicks the wrong item

**Cause:** Figma Desktop accessibility indices changed after rendering, expanding layers, switching tabs, or user interaction.

**Fix:** Fetch a fresh application state after every meaningful action. Prefer current accessibility targets; use coordinates only after inspecting a fresh screenshot. Never reuse stale element indices.

If Figma reports that the user changed the app, assume the previous action may have executed and inspect before retrying.

## 13. When to rebuild instead of patch

Rebuild the affected Figma Sites webpage from the clean Figma Design source when any of these are true:

- more than one duplicate breakpoint exists
- desktop and mobile sections are interleaved across several layouts
- headers contain several image workarounds
- auto-matching propagates edits unpredictably
- the breakpoint count or primary layout cannot be stated confidently
- visual fixes keep breaking another breakpoint

Keep the clean normalized Figma Design source as the recovery point. Figma Sites is the presentation layer, not the only copy of the editable design.

## 14. Duplicate Home or Index webpages

**Cause:** `index.html` and `home.html` were treated as separate routes even though both declare `data-page="home"`.

**Fix:** Group files by `body[data-page]`. Prefer `home.html` and `mobile/home.html` as the Home sources and record both Index files as aliases, not webpages.

## 15. Capture works only for Home

**Cause:** Only the Home desktop/mobile HTML files currently contain the Figma HTML-to-design capture script.

**Fix:** Follow the import tool's fresh capture setup for every page. Use a staged copy or reversible injection when a script tag is required. Do not conclude that the other 18 routes are incompatible, and do not permanently modify all canonical HTML files without approval.
