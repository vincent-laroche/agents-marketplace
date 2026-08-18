---
name: magnific-assets-and-spaces
description: "Legacy compact routing for Magnific assets and review Spaces. Use for source-image discovery, project routing, durable filing, review batches, or verifying browser-picker visibility."
---

# Magnific assets and review Spaces

For complete current procedures, use `magnific-library-and-projects` for reusable records, Projects, folders, uploads, and provenance; use `magnific-spaces-and-flows` for visual graphs, assembly, cost simulation, and Flow promotion. This skill remains deliberately short for basic routing.

## Establish current state first

Project trees, folder references, review Spaces, and selected projects are account state, not durable skill facts. Before creating, moving, or claiming anything:

1. List current projects/folders with the official MCP or visible UI.
2. Compare exact names and references to the requested destination.
3. Reuse the existing destination when it exists; do not create a duplicate because an older guide named it.
4. Report stale local instructions instead of acting on them.

## Source and output routing

- Use a project/folder reference explicitly when the supported tool accepts one. Output without an explicit destination may land in a Personal/default project rather than the currently viewed project.
- Browser reference pickers are often project-filtered. If an asset appears missing, inspect the selected project before uploading or recreating it.
- Use REST upload only as documented temporary staging. For durable project storage where filenames and provenance matter, use the supported project workflow and then verify membership.
- Signed asset URLs are temporary secrets. Never paste them into logs, manifests, prompts, or handoff notes.

## Library references and review Spaces

Use a curated library reference only when it should be reusable and governed. Use ordinary History/Uploads references for one-off work.

Use a Space for an explicit review batch, not as an automatic side effect of generation. Add source and output together, respect the current tool's batch limit, and verify the resulting Space state. Do not claim a Space graph or connection exists until the supported inspection tool shows it.

## Verification

For a durable project upload, paginate the project's current creations and compare a filename multiset against the approved source manifest. The included `scripts/verify_project_uploads.mjs` is the standard read-only verifier. For a visual review, retrieve a current preview through an approved surface and inspect the actual image; metadata alone cannot prove a faithful result.
