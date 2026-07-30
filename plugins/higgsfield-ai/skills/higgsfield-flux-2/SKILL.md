---
name: higgsfield-flux-2
description: Use FLUX.2 Pro or Flex on Higgsfield for precise prompt following, multi-reference consistency, counting, color control, complex edits, and structured image prompting. Use for product-plus-person scenes, fashion catalogs, identity-stable pairs, diagrams, UI concepts, controlled object counts, or JSON-like production briefs.
---

# Higgsfield FLUX.2

Read `../../references/production-contract.md`. Use FLUX.2 when the brief benefits from explicit structural control and several references must remain coherent in one image.

## Prepare the prompt

FLUX.2 responds well to explicit constraints such as:

- exact object and person counts;
- named camera and angle;
- top-down or other spatial layouts;
- precise color values;
- clothing and product assignments;
- separate identity, outfit, product, and setting references.

For complex work, organize the brief into subject, references, composition, camera, light, palette, required elements, and exclusions. A JSON-like structure can improve auditability, but use the live interface's supported prompt format.

## Multi-reference workflow

1. Assign each input a role.
2. State which attributes transfer and which remain protected.
3. Test the most difficult combination first, such as two people plus a product.
4. Compare faces, hairstyle, clothing, product geometry, and spatial relationships to every source.
5. Make one local correction per iteration.

Choose the current Pro variant for maximum precision. Use Flex only after inspecting its current positioning and controls; do not infer that the variants are interchangeable.
