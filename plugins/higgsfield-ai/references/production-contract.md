# Higgsfield production contract

This plugin stores durable production knowledge: model strengths, input strategy, prompting, continuity, review, and workflow routing. The live Higgsfield interface remains authoritative for the controls exposed by the selected model and surface.

## Required action classification

| Action | Default handling |
| --- | --- |
| Read official guidance, inspect a project, analyze references, compare models, or draft a brief | Proceed without generation. |
| Create or transform an image, video, voice, character, batch, or upscale | Resolve the exact model, inputs, settings, count, and destination. Run only when the current request authorizes that concrete operation. |
| Connect an account, enable an automation, upload private media, publish, share, send, or schedule | State the data flow and external effect, then obtain explicit approval. |

## Model-selection contract

1. Start from the production problem, not from the newest model name.
2. Separate identity, appearance, product geometry, motion, scene, camera, audio, copy, and delivery requirements.
3. Choose the model whose native controls match the hardest requirement.
4. Use a controlled comparison only when two models plausibly fit. Hold the brief, input assets, aspect ratio, and review rubric constant.
5. Do not infer one model's inputs or controls from another model or integration surface.
6. Recheck the live model panel before execution because model menus and exact limits evolve.

## Prompt and review contract

- Write one shot or one still at a time. Separate subject, action, setting, light, camera or composition, audio, and exclusions from model controls.
- Assign every reference a role: identity, appearance, product, location, motion, first frame, last frame, or style.
- Preserve source assets. Never replace a master with an unreviewed variation.
- Run one proof before a batch or multi-shot production.
- Inspect the output at its real delivery crop and duration. Reject identity drift, unwanted text, malformed anatomy, product changes, continuity breaks, unstable motion, mismatched audio, or errors at edit points.
- Record the accepted model, inputs, prompt, settings, and output so the result can become a reusable production asset.

## Source routing

- Read `model-selection.md` before choosing between supported model families.
- Read `official-source-map.md` for official product and education sources.
- Use the model-specific skill for input preparation, prompting, failure diagnosis, and review.
