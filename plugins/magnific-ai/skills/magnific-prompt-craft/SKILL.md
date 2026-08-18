---
name: magnific-prompt-craft
description: "Write and review Magnific prompts for Hair Solutions Co. references, hair systems, mannequins, and marble-bust work. Use when fidelity to a particular face, hairstyle, hair texture, product geometry."
---

# Magnific prompt craft

## Identity preservation is a safety requirement

Material-swap edits can alter facial architecture, including narrowing a broad nose, thinning lips, or otherwise changing the subject's ethnic presentation. Treat that as a failed output, not an acceptable variation. Inspect the source first and describe only real, visible features.

For identity-sensitive edits, use clear language such as:

> Preserve the subject's exact facial architecture from the first reference: [specific, visible features]. Do not alter the facial proportions, ethnicity, or expression. Only [the stated material, background, or hair change] may change.

Never use a generic feature list without comparing it to the source. Use high-reasoning mode only if it is visibly available and the user approved the run; it does not replace output review.

## Hair realism

State the actual cut, texture, density, and hairline behavior. A useful starting clause is:

> The hair remains real human hair: individually resolved strands, soft natural sheen, a clean natural hairline, and no plastic, glossy, or synthetic appearance.

Preserve logos, product construction, and haircut geometry where a reference establishes them. Do not invent a product claim or a hairstyle that is not supported by the supplied source.

## Marble-bust treatment

For the approved concept of a marble bust with photoreal hair, make the transformation boundary explicit:

> Transform face, neck, and shoulders into white Carrara marble with restrained grey veining, polished planes, and a matte fractured truncation; keep the hair photoreal and unchanged in identity, cut, texture, and hairline.

Also specify preserved framing, head turn, eye state, lighting direction, and the intended material reference. This avoids an unnecessary full re-render of the subject.

## Prompt template

> Using the first reference as the subject and the second as the material and lighting target, [requested transformation]. Preserve [specific facial architecture, pose, crop, and eye state]. Do not alter identity or ethnicity. [Hair treatment with actual cut and texture.] [Material, setting, lighting, and output intent.] Photorealistic, high detail.

Use plain prose for attached image references. Do not assume text mention syntax is supported by the current browser; test it on a noncritical run before relying on it.

## Review gate

Before filing or using an output, compare source and result for facial structure, identity, hairstyle, hairline, product geometry, framing, and lighting. Reject an output that drifts on any protected attribute. This is especially important for a diverse customer base.
