---
name: design-fidelity-qa
description: "Compare a rendered implementation against a source visual such as a Figma frame, screenshot, mockup, or reference image. Use when the user asks whether an implementation matches the design, looks as good as the mock."
---

# Design Fidelity QA

Compare source visual truth to the rendered implementation. This is not a broad aesthetic critique; it is a fidelity check.

## Preconditions

Require:

- a source visual target
- a rendered implementation representing the same intended state

If either is unavailable, state that the comparison is blocked rather than inventing a result.

## Normalize before judging

Match or explicitly account for:

- viewport and crop
- route/screen
- theme
- content
- authentication state
- interaction state
- device density where relevant

## Required fidelity surfaces

Always inspect:

1. Typography: family, fallback, weight, size, line height, letter spacing, hierarchy, wrapping, and truncation.
2. Spacing/layout: frame proportions, alignment, margins, padding, grid, section gaps, radii, shadows, and vertical rhythm.
3. Color/tokens: palette, gradients, opacity, contrast, semantic states, and foreground/background balance.
4. Imagery/assets: subject, crop, scale, sharpness, compression, masks, logos, icons, and overall art direction.
5. Copy/content: visible text and content density.
6. Responsive/state fidelity when corresponding source states exist.

## Severity

- P0: broken or unusable presentation.
- P1: major mismatch likely to be noticed immediately.
- P2: moderate visual drift or polish gap.
- P3: minor refinement.

Separate objective source mismatches from subjective polish suggestions.

## Output

For each finding include:

- severity
- location
- source vs implementation difference
- why it matters
- concrete fix

End with an ordered implementation checklist and any comparison limits. Do not say the implementation matches until every required fidelity surface has been checked.

Adapted from OpenAI Product Design `design-qa`; see `../../SOURCES.md`.
