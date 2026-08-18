---
name: magnific-library-and-projects
description: "Operate Magnific Library, Projects, folders, creations, reusable agents, and durable uploads. Use for reusable characters/styles/elements/locations/colours/context, project organisation, asset discovery, provenance."
---

# Magnific Library and Projects

## Keep the layers distinct

| Layer | Purpose |
|---|---|
| Creation / History | A generated, uploaded, or derived result; often one-off |
| Project / Folder | Operational home, ownership, and discovery boundary |
| Library record | Governed reusable reference: character, style, element, location, colour, agent, or context |
| Space / Flow | Production logic that consumes the above; not an asset registry |

Do not create duplicate Library records merely to make an asset easier to find. First search Library and the relevant Project, then inspect the existing record before adding or editing.

## Library workflow

1. Use the user-facing picker/show surface when the user needs to choose a record; use the list/search surface for internal reasoning.
2. Give each reusable record a clear role, source/provenance, intended scope, protected attributes, and review status.
3. Use the appropriate type: `character`, `style`, `element`, `locations`, `color`, `agent`, or `context`.
4. Confirm which tools actually accept the selected Library reference and whether they expect its visible/numeric identifier.
5. Edit, share, or delete records only after checking where they are used. A reusable record can affect several projects or Flows.

## Project and folder workflow

1. List current Projects/Folders first. Compare exact names before creating anything.
2. Set the target project explicitly; browser history/reference pickers are commonly project-filtered.
3. Use the supported durable upload path when filenames and provenance matter. REST staging or a temporary signed URL is not durable project storage.
4. File accepted creations intentionally. Move only the stated targets after verifying names and current membership.
5. For a substantial upload/import, paginate current project creations and compare a filename multiset to the approved source manifest. Use the bundled verifier where it fits.

## Explore and reports

Use Explore for inspiration and discovery, never as evidence that an asset is approved, licensed, on-brand, or owned. Use project reports to describe activity and state; they are a diagnostic aid, not a substitute for visually inspecting an output.

Never expose creation identifiers, signed URLs, or collaborator details in a user-facing handoff. Read `magnific-production-safety` before a move/share/delete and `magnific-spaces-and-flows` before wiring an asset into reusable production logic.
