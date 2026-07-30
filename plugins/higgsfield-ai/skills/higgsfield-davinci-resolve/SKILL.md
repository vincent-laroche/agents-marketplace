---
name: higgsfield-davinci-resolve
description: Generate, import, and finish Higgsfield assets inside DaVinci Resolve. Use for missing B-roll, cutaways, inserts, generated backgrounds or overlays, prompt-based clip edits, Draw to Edit, reframing, background removal, upscaling, AI LUT creation, reference-led color matching, or assembling short generated clips into a longer edit.
---

# Higgsfield for DaVinci Resolve

Read `../../references/production-contract.md`. Use the integration to solve a specific timeline gap, not to generate disconnected footage without edit context.

## Tool map

- **Generate Video:** create a scene, character shot, B-roll insert, or camera move from text and references.
- **Generate Image:** create a background, overlay, title-card source, or scene element.
- **Edit Video:** apply one prompt-led change to the active clip.
- **Draw to Edit:** mark an area to remove, add, or replace.
- **Reframe:** adapt to common vertical, square, standard, and widescreen formats while tracking the subject.
- **Remove Background:** create a clean key without a green screen.
- **Upscale:** recover detail for a higher-resolution finish.
- **AI LUT Creator:** match a clip to a reference frame and return a `.cube` LUT or Resolve color nodes.
- **Last Generations / Import to Resolve:** retrieve Higgsfield output and place it in the Media Pool or Timeline.

The integration uses Nano Banana 2 as the default still route and Seedance 2 as the default video route, with other models available. Use `../higgsfield-model-selector` when the default is not the best fit.

## Generate B-roll from the edit

1. Identify the exact timeline gap, shot duration, crop, eyeline, camera direction, lighting, and edit handles.
2. Use an adjacent frame as a visual reference when continuity matters.
3. Generate a short insert that performs one editorial function.
4. Import it to the Media Pool or Timeline and assess it between the surrounding shots.
5. If motion works but color does not, fix color separately with the AI LUT Creator instead of regenerating the shot.
6. Build longer sequences by assembling reviewed short clips; do not expect one generated master shot to carry an extended scene.

## Match color

Choose a representative source frame from the generated clip and one approved reference frame from the sequence. Evaluate skin tone, neutral balance, contrast curve, saturation, highlight rolloff, and shadow color after applying the LUT or nodes. Treat the generated look as a starting point and retain manual grade control.

Use background removal, reframe, and upscale only after the underlying shot has passed motion, identity, and continuity review.
