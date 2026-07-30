---
name: higgsfield-kling-motion-control
description: Transfer a specific human performance from reference video to a prepared character image with Kling Motion Control on Higgsfield. Use for dances, gestures, presenter movement, mascot animation, digital humans, product demonstrations, localized character variants, repeatable motion templates, or Kling Motion Control 2.6 versus 3.0 decisions.
---

# Higgsfield Kling Motion Control

Read `../../references/production-contract.md`. Prefer the current 3.x route when available; its durable advantage over 2.6 is improved face stability, tighter motion capture, and stronger alignment to the driving reference.

## Prepare the character image

- Show the face clearly and match the intended crop.
- Expose every limb and hand required by the performance.
- Leave negative space in the direction of arm, leg, or body travel.
- Use a stable, uncluttered silhouette.
- Match close-up performance with a close-up character image and full-body performance with a full-body image.
- Avoid pockets, crossed limbs, occlusion, or a crop that forces the model to invent anatomy.

## Choose the driving video

Use one clearly visible subject, clean lighting, minimal occlusion, and a background that separates the silhouette. The reference video is the source of truth for movement, expression, timing, and pacing. Choose a performance whose framing, scale, and orientation match the character image.

## Configure the transfer

1. Upload the motion reference and character image.
2. Choose whether scene appearance follows the motion video or the character image.
3. Set orientation to follow the source that should own framing.
4. Use text only for background, lighting, atmosphere, or contextual details; do not fight the driving motion with contradictory choreography.
5. Generate one proof before reusing the motion across characters or styles.

## Diagnose failures

- **Warped or shaking face:** framing or scale mismatch, excessive facial motion, or weak face visibility.
- **Broken hands or limbs:** missing anatomy in the source image, occlusion, or insufficient negative space.
- **Weak motion match:** cluttered driving footage, multiple subjects, low contrast, or a motion outside the source image's visible body.
- **Clipped movement:** crop too tight for the performance.
- **Wrong scene:** scene-source or orientation choice conflicts with the intended output.

Reuse an approved motion reference as a template across characters only after one transfer passes face, anatomy, timing, and crop review.
