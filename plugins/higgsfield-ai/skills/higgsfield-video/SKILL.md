---
name: higgsfield-video
description: Plan, generate, continue, edit, reframe, upscale, or review Higgsfield AI video shots. Use for text-to-video, image-to-video, Seedance, Kling, Wan, Veo, Gemini Omni, Sora, video audio, start/end frames, lip-sync, short-form, UGC, or cinematic motion tasks outside Cinema Studio-specific project work.
---

# Higgsfield video

Read `../../references/production-contract.md` before running anything. Read `../../references/model-selection.md` when the model has not been chosen. Use `../higgsfield-cinema-studio` when the request is a sequence or scene production rather than an isolated shot.

## Define one shot before choosing a model

Write the shot as: **purpose → subject → action → setting → camera/motion → light → duration → sound**. Keep title cards, captions, precise labels, and legal copy outside the generated shot unless the current model is intentionally being tested for that job.

## Choose controls from the live model row

The available controls change with the selected model. Recheck visible duration, resolution, aspect ratio, audio, start/end frame, and element/reference support after every model switch. Use a start frame to anchor a known look; use an end frame only when the selected model exposes it and the destination state matters. Shorten a test before extending a shot.

## Production loop

1. Make a short proof clip at the intended aspect ratio.
2. Inspect continuity, motion physics, camera behavior, visual artifacts, sound, and whether the first/last frames can carry the next edit.
3. Diagnose one failure at a time: reference/master, prompt, model, camera/motion, or duration.
4. Promote only a reviewed shot to the sequence. Do not overwrite the master still or silently use a failed continuation.

## Hand-off

Use `../higgsfield-canvas` to orchestrate repeatable branches and `../higgsfield-cinema-studio` for cast, locations, props, and director controls. Use `../higgsfield-marketing-studio` when the output is a product/advertising campaign.

Use `../higgsfield-seedance-2` for a coherent cinematic shot, `../higgsfield-kling-3` for explicit scene structure and frame constraints, and `../higgsfield-kling-motion-control` when a driving performance video should own the motion.
