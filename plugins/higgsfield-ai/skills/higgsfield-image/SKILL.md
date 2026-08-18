---
name: higgsfield-image
description: "Create, edit, iterate, upscale, or review images in Higgsfield, including reference-led product, character, mascot, editorial, and motion-design frames. Use for Higgsfield image generation, image editing, inpainting."
---

# Higgsfield image

Read `../../references/production-contract.md` first when the task can generate or edit. Read `../../references/model-selection.md` when the model has not been chosen.

## Choose the smallest useful image job

- **New frame:** write a visual production brief from the desired use, not generic quality adjectives.
- **Targeted edit:** keep a protected source and name one intended change. Prefer a surgical edit over regenerating a good frame.
- **Reference-led composition:** identify which reference is identity, product/geometry, style, or layout. Do not ask a model to infer a role from an unlabelled pile of files.
- **Upscale/finalize:** use only after the composition has passed review. Upscaling is not a repair for bad anatomy, identity drift, or wrong product geometry.

## Build the brief

Specify, in this order: intended output/use and crop; subject or product; protected identity/geometry; setting and composition; materials; lighting; style; exclusions. State where text must be absent, exact, or added later in a native tool.

For Hair Solutions work, inspect the live brand authority and supplied references before describing color, typography, product construction, hairline, ethnicity, or hairstyle. Do not invent medical, performance, or product claims.

## Run and review

1. Select the actual model and inspect its visible support for aspect ratio, resolution, reference count, edit inputs, and text rendering.
2. Run one image first when continuity or product fidelity matters.
3. Compare the result against every protected reference: face, hairline, texture, base construction, crop, marks/logos, and lighting direction.
4. Keep the accepted source and record the model/settings used. Make variants from that approved master rather than a random later generation.

Use `../higgsfield-asset-continuity` for reusable characters and `../higgsfield-canvas` for a repeatable multi-model image-to-video pipeline.

Use `../higgsfield-soul-id` for a real recurring person, `../higgsfield-soul-cast` for a fictional actor, and `../higgsfield-nano-banana-2` for structured marketing, text, localization, or rapid layout work.
