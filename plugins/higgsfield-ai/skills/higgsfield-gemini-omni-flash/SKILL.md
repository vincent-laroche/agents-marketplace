---
name: higgsfield-gemini-omni-flash
description: "Build fast multimodal video iterations with Gemini Omni Flash on Higgsfield. Use when text, images, audio, and source video must be reasoned over together; for multi-shot prototypes, reference-driven VFX."
---

# Higgsfield Gemini Omni Flash

Read `../../references/production-contract.md`. Use Gemini Omni Flash when connecting several input types in one request is more important than maximum finishing fidelity.

## Assign every modality a job

- **Text:** action, relationships, camera, and exclusions.
- **Character image:** appearance and identity.
- **Location or product image:** world and geometry.
- **Audio:** timing, rhythm, dialogue, or mood.
- **Source video:** motion, edit context, or the material to transform.

State which input wins if two signals conflict. Do not upload a mixed reference set without role labels.

## Best uses

- fast multimodal concept and revision loops;
- multi-shot prototypes built from character and location references;
- VFX or scene transformations of existing footage;
- development passes where the team is still discovering the correct action, look, or input combination.

Use Kling 3 when human motion, physics, and explicit scene structure are the harder requirements. Use a higher-fidelity audio-native route when final sound and image finish outweigh iteration speed.

## Review

Check whether every modality was actually used, identity and location stayed coherent, audio timing matches action, edits preserve protected footage, and the output is good enough for its role. Treat it as a development route when the final-delivery quality bar exceeds the live model's output.
