---
name: higgsfield-canvas
description: Assemble reusable Higgsfield Canvas workflows that chain prompts, references, image models, video models, and outputs on a collaborative node graph. Use for Canvas boards, node pipelines, campaign variants, storyboard-to-render workflows, visual assembly, or template design.
---

# Higgsfield Canvas

Read `../../references/production-contract.md` before running a node.

## Build the graph before running it

1. Start with a named brief node or a controlled source asset.
2. Separate reusable inputs: identity/character, product geometry, style, copy/layout direction, and output format.
3. Build one proof branch from input to output. Make dependencies visible rather than packing every instruction into one prompt.
4. Keep native title cards, diagrams, labels, and approval notes as distinct nodes from generative imagery.
5. Add variants as explicit branches with a named variable: hairstyle, colorway, pose, aspect ratio, or shot—not a generic "v2".

## Run safely

- Creating, connecting, moving, annotating, and saving a graph is non-generative work.
- Resolve the exact model, inputs, settings, and output destination before running an image or video node.
- Run a node only when the current request authorizes that concrete generation.
- Run one branch, inspect the actual output, then fan out only after it passes.
- Record accepted output nodes and preserve the source/master node. Use comments for review decisions and expose any failed branch rather than reusing it silently.

## Good Canvas shapes

- **Campaign:** brand/style + product + character → still master → video branches → aspect-ratio adaptations.
- **Episode:** beat/brief nodes → one visual insert per beat → native diagrams/titles → approved sequence.
- **Wardrobe:** approved character master + one named hair/style input → a single controlled variation → review → accepted library node.

Use Cinema Studio when the job needs a production project with Elements and directorial controls. Use Canvas when the job needs a reusable visual graph, branching, or a clear assembly board.
