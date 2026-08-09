---
name: designer-eye-review
description: Perform a rigorous designer-eye audit of a live interface or implementation. Use for visual QA, design polish, visual inconsistency, spacing and hierarchy problems, generic AI-looking design, or requests to make an interface feel more intentional and distinctive. Emphasize concrete observations, prioritized fixes, and verification after changes.
---

# Designer Eye Review

Review the interface as a designer, not as a generic QA checker.

## Core principle

Every finding must include:

- observation: what is visibly happening
- diagnosis: why it weakens the design
- fix: the specific change to make
- expected effect: how the change improves hierarchy, coherence, or perceived quality

## Audit lenses

Evaluate at minimum:

- composition and focal hierarchy
- alignment and spacing rhythm
- typography system and text density
- palette discipline and contrast
- component consistency
- image crops and art direction
- visual noise and unnecessary decoration
- interaction latency or awkward visual state changes when observable
- responsive behavior
- generic AI-design patterns: excessive gradients, arbitrary glow, repetitive cards, weak hierarchy, default-looking typography, decorative clutter, or interchangeable SaaS aesthetics

## Method

1. Inspect the current rendered state or supplied visual.
2. Start with macro composition before pixel-level details.
3. Run a squint test for dominant hierarchy.
4. Check whether each major region has a clear purpose and visual role.
5. Look for repeated inconsistencies instead of treating each instance as unrelated.
6. Rank findings by impact.
7. If the user asks for implementation changes, change one coherent issue at a time and verify the result visually before calling it fixed.

## Output

Lead with the most consequential findings. For each, provide location, observation, diagnosis, fix, and expected effect. End with:

- strongest existing design decisions to preserve
- top five fixes in execution order
- residual polish items

Avoid generic praise and generic criticism.

Adapted from gstack's `design-review` workflow; see `../../SOURCES.md`.
