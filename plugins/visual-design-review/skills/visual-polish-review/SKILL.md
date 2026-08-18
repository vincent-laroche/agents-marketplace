---
name: visual-polish-review
description: "Review an existing web page, app screen, screenshot, Figma frame, email, or digital interface for visual polish. Use when the user asks whether something looks good, polished, professional, harmonious, balanced."
---

# Visual Polish Review

Judge the visible design like a senior visual designer. Separate aesthetic quality from usability unless usability directly affects the visual result.

## Review process

1. Inspect the actual visual evidence before judging.
2. Identify the intended focal point and perform a squint test: what dominates first, second, and third?
3. Evaluate:
   - layout, grid, alignment, and spatial balance
   - spacing scale and vertical rhythm
   - typography hierarchy, line length, line height, weight, tracking, and pairing
   - color harmony, contrast, saturation balance, and semantic consistency
   - negative space and grouping
   - radii, borders, shadows, icons, and component consistency
   - hover, focus, active, loading, and disabled states when visible
   - mobile/tablet/desktop proportions when multiple breakpoints exist
4. Distinguish objective defects from taste-based recommendations.
5. Prioritize the smallest set of changes with the largest visual impact.

## Severity

- High: visibly broken, incoherent, or unprofessional.
- Medium: clearly reduces polish or consistency.
- Low: refinement that improves craft but does not change the overall impression.

## Output

Return:

- Overall impression in 1-2 sentences.
- Findings grouped High / Medium / Low.
- What already works and should be preserved.
- Top 3 changes by visual impact.
- Specific replacement suggestions when useful: font pairing, scale, spacing, color, alignment, crop, radius, shadow, or component treatment.

Do not hide behind vague language such as "it feels off." State the visible reason and the concrete fix.

Adapted from Jezweb's `design-review` skill; see `../../SOURCES.md`.
