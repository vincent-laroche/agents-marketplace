---
name: frontend-craft-review
description: Review or guide frontend interfaces for distinctive visual craft and design-system quality. Use for frontend design reviews, component reviews, design-system compliance, responsive checks, accessibility-aware visual review, or when a UI looks generic and needs a stronger aesthetic direction. Focus on typography, palette, composition, motion, spacing, tokens, and implementation fidelity.
---

# Frontend Craft Review

Evaluate the interface through three lenses: clarity of action, quality of craft, and trustworthy presentation.

## Establish direction

Before judging details, infer or identify the intended aesthetic direction. Ask whether the interface has a coherent point of view appropriate to its purpose. Do not reward novelty for its own sake.

## Review

Evaluate:

- typography: hierarchy, pairing, optical weight, measure, and distinctiveness
- color: cohesive palette, dominant/secondary/accent roles, contrast, and token consistency
- composition: grid, asymmetry/symmetry, negative space, density, overlap, and visual flow
- motion: purposeful transitions and state changes; avoid decorative motion without hierarchy value
- components: consistent states, radii, shadows, borders, icons, and controls
- design system: use of established tokens/components versus arbitrary one-off values
- responsive behavior: intentional reflow rather than compressed desktop layouts
- accessibility-visible issues: contrast, focus visibility, touch target appearance, and readability
- generic design signals: predictable card grids, weak type hierarchy, timid palettes, gratuitous gradients, and context-free decoration

## Findings

Classify as:

- Blocking: broken hierarchy, severe readability/accessibility issue, or major design-system violation.
- Major: noticeable craft or consistency problem.
- Minor: refinement.

For each finding, describe what should change and why. When implementation context is available, give token/component/CSS-level guidance without inventing unavailable design-system names.

## Output

Return:

1. Aesthetic direction and whether it is coherent.
2. Highest-impact findings first.
3. Design-system deviations.
4. Distinctiveness/generic-design assessment.
5. Prioritized implementation recommendations.

Adapted from Microsoft's `frontend-design-review`; see `../../SOURCES.md`.
