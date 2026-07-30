---
name: magnific-image-production
description: "Plan and execute Magnific image creation and editing safely: generation, reference-led work, editing, variations, background removal, relighting, camera changes, crop/resize, skin work, vectorization, and upscaling."
---

# Magnific image production

## Choose the operation before choosing a model

| Need | Start with |
|---|---|
| New concept or campaign visual | Image Generator |
| Preserve a supplied person, character, product, pose, or packaging | Reference-led generation or focused edit |
| Isolate product or bust | Remove Background; inspect alpha edge and missing hair detail |
| Change light, crop, framing, or camera while retaining subject | Relight, Crop/Resize, or Change Camera |
| Explore controlled alternatives | Variations; keep the approved source explicit |
| Improve a supplied image | Precision or creative Upscaler after deciding whether invented detail is acceptable |
| Turn flat art into editable or responsive design | Designer auto-layers or auto-resize, not a new image generation |

## Operating sequence

1. Read `magnific-production-safety`; select the destination project before doing anything else.
2. Inspect the current image-model list and settings rather than carrying forward a model recommendation from a prior task.
3. Define what must remain invariant: identity, face, hair, garment, logo, product geometry, typography, crop, palette, lighting, or transparency.
4. Use `magnific-prompt-craft` for hair systems, busts, mannequins, people, or other identity-sensitive inputs.
5. Attach only the references the selected model visibly supports, in purposeful order. Recheck them after switching models because limits can change.
6. Draft the exact prompt and settings, then simulate current cost and obtain approval for the exact run.
7. Run one output first for a new model, transformation, or protected source. Inspect pixels at useful zoom; do not accept metadata as visual proof.
8. File accepted outputs in the chosen project and, if reusable, in the governed Library. Keep the provenance from source to final output.

## Quality checks by operation

- **Background removal:** subject edge, flyaway hair, translucency, shadow treatment, canvas dimensions, nonempty alpha.
- **Reference work:** facial architecture, ethnicity, product dimensions, hairline, hairstyle, texture, logos, and crop.
- **Upscale:** text, logo fidelity, facial geometry, hair strands, noise, invented product features, and whether creative detail exceeded the brief.
- **Relight/camera:** original identity and object geometry remain intact; no unrequested background or wardrobe replacement.
- **Variations:** identify the accepted parent and a clearly stated variation axis; do not use a “variation” as a covert redesign.

## Model and browser notes

Use `magnific-model-limits` before browser image generation, and `magnific-browser-generate` only for a user-authorised browser run. For API/MCP work, inspect the live `images_models_list`, model settings, and `simulate_cost`; browser unlimited availability does not transfer automatically.

Use the official docs search before requesting a less-common tool such as image-to-SVG, expand, mockup generation, or skin enhancement. Exact endpoints and parameters are deliberately not memorised here.
