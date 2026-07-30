---
name: magnific-video-production
description: "Plan and operate Magnific video creation, image-to-video, reference-to-video, video editing, scene continuity, speech, combining, VFX, and video upscaling with cost and review controls."
---

# Magnific video production

## Start with a shot plan, not a model

Before selecting a model, write the runtime, aspect ratio, delivery surface, scene count, visual continuity facts, starting/ending frames, audio plan, and acceptance test. Use the current `video_plan` surface when available before `video_generate`; this is mandatory unless the user explicitly asks for a one-shot experiment.

## Source choice

| Starting point | Use when |
|---|---|
| Text-to-video | The scene is genuinely new and no controlled first frame is needed |
| Image-to-video | A still must anchor character/product/setting appearance |
| Reference-to-video | One or more character/style references must persist across a scene |
| Video-to-video or video edit | Motion/source footage should remain the basis while content or style changes |
| Video combiner | Accepted clips need a defined order into one finished sequence |

Do not select a model from this table. Read the current `video_models_list` and settings because model availability, durations, reference support, and audio behaviour change.

## Scene-continuity contract

Every scene in a sequence should carry the same explicit facts: character/reference, hairstyle and wardrobe, setting, material treatment, palette, lighting direction, lens/camera grammar, motion intensity, and forbidden changes. Put changing action only in each scene’s unique clause.

For Hair Solutions characters, protect face, marble/skin material boundary, hairline, hairstyle, texture, colour, and crop. Use image references from the governed Library, and use `magnific-prompt-craft` for exact prompt language.

## Execution sequence

1. Read `magnific-production-safety` and select project/folder output.
2. Create or inspect the plan; select one current model and its valid settings.
3. Simulate exact cost. For a multi-scene board, use `simulate_spaces`, not a guessed per-scene multiplication.
4. Obtain approval for the bounded test or batch.
5. Generate a proof scene. Review visual identity, camera motion, timing, sound, and any unwanted object changes.
6. Generate the remaining approved scenes. Track individual completion, then re-run only failed or rejected scenes.
7. Combine only accepted scene outputs. Confirm clip order, transition expectations, audio ownership, total duration, aspect ratio, and output destination.
8. Upscale, apply VFX, or edit only after deciding whether it may alter protected details; simulate and approve each extra pass separately.

## Voice and sound

Use `magnific-audio-production` for TTS, music, sound effects, audio isolation, and consent. Treat in-model sound as an intentional scene choice; never assume it will yield reusable narration. Keep scene audio ownership clear so a combiner does not accidentally stack music, dialogue, or ambience.

For reusable five-scene episodes, read `magnific-spaces-and-flows` and promote the graph to a Flow only after it has a stable input/output contract.
