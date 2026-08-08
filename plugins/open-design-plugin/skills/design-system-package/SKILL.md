---
name: design-system-package
description: Create, audit, or migrate a portable design-system package with a stable manifest, canonical semantic tokens, component inventory, and source evidence. Use when a team needs a durable design-system handoff, needs to make tokens traceable to their source, or must distinguish canonical files from generated indexes. Do not use to replace a brand authority without approval.
---

# Package a Design System

Treat a design system as a versioned package, not a loose `DESIGN.md` or a screenshot board.

## Establish authority

1. Identify the current brand authority and the target consumers (Figma, storefront, email, app, or agent).
2. Inventory the actual sources: token files, live styles, component code, Figma variables/styles, approved assets, and measurable references.
3. Record provenance for each imported or inferred value. Never promote inspiration, a third-party system, or a screenshot into brand truth.
4. Stop before replacing an existing token source, publishing a library, or changing customer-facing assets without explicit approval.

## Build the package

Create this minimum shape in the selected repository:

```text
<system>/
├── manifest.json
├── DESIGN.md
├── tokens.css
├── components.manifest.json
└── source/
    └── evidence.md
```

- Make `manifest.json` identify the package, its canonical files, version, consumer scope, and source provenance.
- Make `tokens.css` the compiled semantic-token surface. Use semantic properties in component code; do not repeat raw values ad hoc.
- Make `DESIGN.md` explain intent, typography, color roles, layout, components/states, motion, accessibility, imagery, and anti-patterns. Keep it synchronized with tokens.
- Make `components.manifest.json` an inventory derived from actual components or Figma sources: name, variants, states, token dependencies, and owning surface.
- Make `source/evidence.md` a compact audit trail of source file/node, date inspected, confidence, and whether a value is measured, inherited, or pending review.

## Validate

1. Confirm every manifest path is safe, relative, and present.
2. Confirm each token has one canonical definition and an explicit consumer mapping.
3. Check components use declared semantic tokens, keyboard/focus states, contrast, and reduced-motion behavior.
4. Mark derived indexes as generated; do not hand-edit them as competing truth.
5. Report unknown, duplicate, and inferred values separately from confirmed values.

## Output

Lead with the authoritative source, package location, validation result, and unresolved approval gates. Include a migration plan before changing any existing system.
