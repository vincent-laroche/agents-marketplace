---
name: higgsfield-cinema-studio
description: "Build controlled Higgsfield Cinema Studio productions with projects, cast, locations, props, multi-image references, Elements, cinematic reasoning, genre, camera and lens controls, speed ramps, native audio, shot lists."
---

# Higgsfield Cinema Studio

Read `../../references/production-contract.md` and `../../references/academy-course-map.md` before production work. Cinema Studio is the project-first surface for directorial control and continuity.

## Establish the production structure

1. Reuse an existing project when it is the intended production; do not create a look-alike duplicate.
2. Make a small folder plan before generating: for example `01-references`, `02-characters`, `03-locations`, `04-props`, `05-shots`, `06-approved`.
3. Write a project brief that separates story/world rules, continuity rules, formats, prohibited changes, and output use.
4. Treat a completed image as a rough cut until it passes review.

## Use Elements for continuity, not convenience

An Element is an approved reusable character, location, or prop. Save an Element only after the chosen frame actually passes the identity, geometry, texture, and crop review. Name it predictably, then confirm the target model visibly supports the `@` Element control before relying on it in a shot.

Use a project-specific naming pattern such as `@character_ep01_miles_master`, `@location_ep01_studio_day`, and `@prop_ep01_task-card`. Do not replace an approved Element with a weaker variation.

## Direct each shot

Let the prompt state the story beat. Set the world through the director panels: genre, style, light, palette or color, camera, sensor, lens or focal length, aperture, camera movement, timing, and audio intent.

Current Cinema Studio generations may reason over several combined character and location references, physics-aware action, synchronized audio, genre behavior, and speed-ramp choices such as linear, automatic, slow motion, bullet time, impact, or ramping. Recheck the live controls, then choose only the controls that serve the beat.

Use high-level cinematic reasoning when the story intent and approved references already define the world. Use manual camera and lens controls when composition is a protected requirement. Native audio is useful for timing and atmosphere, but decide whether the final production needs an independent sound pass.

The AI Director can turn a brief into a proposed shot list, but review its model, Elements, camera, prompt, reference, timing, and audio choices before any generation.

Use the Academy's production test sequence: establish one dependable location; make an approved character sheet; make any story-critical prop; test the smallest Seedance shot; inspect the result; then expand the sequence.

## Review gate

Inspect each proposed master for its actual downstream crop and motion use. Reject visible slop before it becomes an Element or a video reference. One repair per edit; recheck the protected attributes after each repair. Use `../higgsfield-video` for isolated motion troubleshooting and `../higgsfield-canvas` for a reusable multi-model pipeline.
