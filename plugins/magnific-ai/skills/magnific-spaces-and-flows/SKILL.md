---
name: magnific-spaces-and-flows
description: "Design, inspect, cost, run, review, and promote Magnific Spaces and Flows. Use for connected creative boards, scene assembly, episode pipelines, video combiners, reusable production templates, or Flow execution."
---

# Magnific Spaces and Flows

## The distinction that prevents bad automation

- A **Space** is an editable visual board: nodes, connections, page layout, and in-progress creative decisions.
- A **Flow** is a saved Space workflow that exposes defined inputs and can be rerun as a tool.

Do not call an editable Space a reusable Flow. Inspect current state first: use read-only Space tools to see the graph, and use `flows_list` plus `flows_get` to see whether a true Flow exists and what input/output contract it exposes.

## Assistant-built episode pattern

The live five-scene example establishes a useful starting pattern, not a default model prescription:

```text
Brief / outline
  -> Scene 1: hook
  -> Scene 2: problem and core concept
  -> Scene 3: deep dive
  -> Scene 4: case study or example
  -> Scene 5: summary and CTA
  -> Video combiner
  -> final episode
```

The observed Space used five video-generator nodes connected to one video-combiner node. The scene contract was 16:9, 8 seconds, 720p, with sound intentionally enabled only where needed. Treat those settings as a worked example: choose the current model, duration, resolution, aspect ratio, and sound plan for the brief after checking the current picker and cost.

## Build and operate a Space

1. Define the production contract outside the board: audience, platform, total runtime, scene beats, narration/sound ownership, reusable characters/references, format, and acceptance criteria.
2. Use `magnific-assistant-orchestration` when the Assistant should draft the initial graph. Ask it to create named nodes and connections, not to start generation or publishing.
3. Inspect the created graph with the current supported Space inspection tool. Verify page, nodes, connection direction, source assets, destination, and every scene setting.
4. Replace generic prompts with scene-specific prompts; keep protected identity, character, product, lighting, camera, and audio facts consistent across all scenes.
5. Simulate the **entire Space** with `simulate_spaces`. Then request approval for the exact run boundary.
6. Run one proof scene when continuity or a new model is at risk. Review it before running the remaining scenes.
7. Run the remaining nodes only after the proof is accepted. Confirm each output completes; repair only the failed node rather than rebuilding a working graph.
8. Feed only accepted scene outputs into the video combiner. Confirm ordering, audio behavior, duration, and final output before calling the episode done.

## Promote a Space to a Flow only when it is repeatable

Promotion test:

- Inputs are real variables, not buried in a hand-edited scene prompt.
- Output is unambiguous and named.
- Every required reference and destination is accounted for.
- A fresh operator can run it without editing hidden nodes.
- A simulated run has a known cost boundary.

After promotion, call `flows_get` and record the published input/output contract. Run it through `flows_run` only after `simulate_flows` and approval. Poll with the supported Flow status/wait mechanism; inspect resulting creations rather than assuming the Flow submitted successfully.

## Templates and versioning

Use a copied Template Space as a starting point, not as proof of a finished production workflow. Keep the working Space editable while experimenting. Freeze the approved graph only after accepted output and a documented input contract. A Flow should be treated as a small internal production product: it needs a name, purpose, inputs, output, owner, cost expectation, and QA rule.

Always read `magnific-production-safety` before a run, `magnific-video-production` for scene/video work, and `magnific-library-and-projects` when references or output filing matter.
