---
name: magnific-assistant-orchestration
description: "Use the Magnific Assistant to draft useful creative structures without surrendering review, cost, asset, or publication control. Trigger for Assistant-led Space building, multi-scene episode setup, prompt-to-workflow requests, or workflow troubleshooting."
---

# Magnific Assistant orchestration

The Assistant is best treated as a graph and draft builder. It can turn a concise creative brief into nodes, connections, text blocks, and an initial production structure. Its work is not automatically an approved run, a paid action, or a reusable Flow.

## Write an Assistant brief that produces an inspectable board

Provide:

- Objective and delivery surface.
- Exact scene/story beats or design sections.
- Required inputs and protected references.
- Format, runtime, number of outputs, and audio intent.
- Desired node names and final output name.
- Explicit limits: “Create/edit the Space only. Do not generate, download, share, publish, or delete.”

For the observed five-scene episode pattern, ask for named scene nodes plus a final video-combiner node. Do not ask vaguely for “an episode”; generic nodes hide the decisions that need review.

## Verify what the Assistant actually did

1. Inspect the Space graph with the supported read-only Space state/nodes tools or visible UI.
2. Confirm it created the right page, named nodes, and directed connections—not merely text placeholders.
3. Check model, duration, aspect ratio, resolution, sound, inputs, project destination, and output wiring on every generation node.
4. Replace generated generic prompts with the approved brief and grounded Library references.
5. Run `simulate_spaces` before requesting any execution approval.
6. Test a single scene first if the work includes identity, product, character, or continuity risk.

## Use Assistant for structure, not unbounded authority

Assistant requests must never authorise:

- paid generation, enhancement, or downloads;
- bulk mutation of existing projects/Library records;
- publication, sharing, or scheduling;
- deletion or replacement of source assets;
- use of a person’s likeness or voice without the required right/consent.

When a graph stabilises, hand it to `magnific-spaces-and-flows` for Flow-promotion testing. Use `magnific-production-safety` before any account-changing action.
