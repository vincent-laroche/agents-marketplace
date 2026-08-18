---
name: figma-web-capture-import
description: "Plan or perform a bounded web-page capture to editable-ish Figma reference import using a JSON node-tree and a local Figma development plugin. Use for isolated competitor research, owned-page recovery."
---

# Import a Web Capture into Figma

## Establish the boundary

1. Confirm the URL/page is authorized for capture and whether it is owned content, public research, or a competitor reference.
2. Confirm the destination Figma file, page, and purpose. Keep captures on an isolated reference page; never import over production components or a Figma Site.
3. Verify the current Figma desktop session and development-plugin availability before starting.
4. Record that the result is a best-effort reference reconstruction, not a verified native Figma design.

## Capture and import

1. Capture the page into an `.od-figma.json` node-tree using an approved capture path. Do not install a browser extension with broad permissions without explicit approval.
2. In Figma desktop, use the local development plugin manifest and import the JSON through the plugin UI.
3. Keep the imported frame named with source, date, and `Reference` status.
4. Validate in the Layers panel: frames, text, fills, images, and hierarchy should be individually selectable where conversion succeeded.

## Fidelity limits and recovery

- Fonts may fall back; complex gradients, transforms, blend modes, pseudo-elements, SVG internals, and inaccessible cross-origin images may be simplified or omitted.
- SVG/WebP/GIF/AVIF may be rasterized for Figma; do not describe them as editable vectors.
- Do not infer missing node structure from screenshots.
- If a reference needs production-quality editability, rebuild it natively from approved content and the active design system rather than layering workarounds onto the import.

## Output

Report destination file/page, source URL, import outcome, simplified/omitted items, Layers-panel validation, and any follow-up native rebuild recommendation. Do not publish, change sharing, or upload assets as part of this skill.
