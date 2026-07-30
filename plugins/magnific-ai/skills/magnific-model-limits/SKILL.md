---
name: magnific-model-limits
description: Determine whether a Magnific image-generation choice can spend credits, how many reference slots it supports, and which path best fits the job. Use before every Magnific generation, model choice, or resolution choice. Treat its field observations as historical and verify the live browser UI before execution.
---

# Magnific model limits and credit safety

## Non-negotiable preflight

This skill contains field observations collected from a Premium+ account on 2026-07-26. They are useful shortlists, not a current pricing promise. Magnific can change plan entitlements, model availability, limits, and credit treatment at any time.

Before every generation:

1. Open the exact tool and choose the model, resolution, count, and references.
2. Confirm the live UI shows both the `∞ ON` control and an **Unlimited generations** indicator.
3. If either indicator is absent, stop. State the displayed cost and obtain current-turn approval before generating.
4. For a user-authorized zero-credit run, compare account credit balance before and after. Do not infer that a run was free from the model name alone.

Browser unlimited entitlement was observed not to apply to MCP generation. Treat any API or MCP generation as credit-consuming unless the current documented surface explicitly says otherwise and the user approved it.

## Observed model shortlist — recheck before use

| Need | Observed browser-safe starting point | Constraints to verify live |
| --- | --- | --- |
| Maximum reference fidelity | Nano Banana 2 (`imagen-nano-banana-2-flash`) at 1K | 14 reference slots; 2K/4K previously removed unlimited status |
| Free high-resolution exploration | Seedream 4.5 at 2K/4K or Seedream 5 Lite at 2K/3K/4K | 8 reference slots; identity fidelity was not measured |
| Fast iteration | Flux.2 Klein at 1K/2K | 4 reference slots |
| High-resolution fixed pass | Seedream 4 4K | Confirm it still carries unlimited status |
| Typography or UI-like composition | Recraft V4.1 or Ideogram | Inspect current text/ref support before use |

The following families were observed as paid in the browser and therefore always require approval when a cost is displayed: GPT variants, Nano Banana Pro, Cinematic, Flux.2 Max/Flex, Ideogram 4, Krea 2, Luma Uni-1.1, MAI Image 2.5, and Recraft V4 Pro. This list is deliberately conservative: if a live badge disagrees, the live badge wins.

## Decision rules

- Preserve a particular person, face, or product geometry: prioritize reference fidelity, keep the reference count within the visible limit, and run a one-image review before batching.
- Need a free large output: begin with a currently unlimited Seedream option, but compare the face and product geometry against the source before accepting it.
- Need a paid final asset: draft the exact model, resolution, count, and displayed cost; do not click Generate until approved this turn.
- Need a model absent from this guide: inspect the live picker and current official documentation instead of extrapolating.

## Reverification procedure

1. Open `https://www.magnific.com/app/ai-image-generator` and allow the page to finish loading.
2. Open the model picker and inspect the relevant model row. A visible credit range means paid; do not treat an absent range as sufficient proof of free access.
3. Select the model, inspect each offered resolution, then verify the current panel's unlimited controls.
4. Take a fresh screenshot or record the visible state for the proposed action. Recheck after changing the model, resolution, count, or reference set.

Do not claim that a generation is zero-credit until the before/after account balance proves it.
