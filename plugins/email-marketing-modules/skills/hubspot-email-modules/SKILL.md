---
name: hubspot-email-modules
description: Work on Hair Solutions Co. HubSpot Design Manager email modules, including local module source, naming, light/dark variants, editability, logos, cleanup, validation, deployment to account 50966981, and troubleshooting locked or broken HubSpot drag-and-drop modules. Use for Email Marketing Studio, HubSpot Design Manager email_modules, module inventory, module renaming, module cleanup, or email module deployment work.
---

# HubSpot Email Modules

Use this skill for Hair Solutions Co. email-module work in HubSpot Design Manager.

## Canonical Source

- Local repo: `/Users/vMac/03_agents/Projects/Email Marketing/Email Marketing Studio`
- Module source: `hubspot/design-manager/email_modules`
- Generated inventory: `lib/hubspotModuleInventory.generated.ts`
- HubSpot account: `50966981`
- HubSpot Design Manager destination: `email_modules/`
- Primary checks: `npm run generate:hubspot-modules`, `npm run lint`, `npm run build`

Do not use old paths under `/Users/vMac/01_projects`, `/Users/vMac/04_marketing`, or legacy Email Studio folders without verifying current filesystem state.

## Required References

Read only what the task needs:

- `references/module-inventory.md`: current active module folders, naming grammar, deleted/forbidden structures.
- `references/deployment-playbook.md`: validation, HubSpot upload/fetch, editability failures, draft repair warnings.

## Non-Negotiable Rules

1. Inspect current local source before editing. Do not rely on remembered module names.
2. Active custom modules live only under `email_modules/core`, `email_modules/launch`, and `email_modules/newsletter` unless a real new journey is being created.
3. No active module/folder/file should use `hsc_`, `hsc-`, `legacy`, `archive`, `not found`, fake `shop`, or unmanaged `warm` naming.
4. Every active module family needs exactly one Light and one Dark variant.
5. Every custom email module must be editable in the HubSpot drag-and-drop editor:
   - `global: false` in `meta.json`
   - every field has `locked: false`
   - module fields expose text, URLs, images, labels, choices, or booleans, not required raw HTML.
6. Do not make reusable headers journey-specific. Headers are CORE modules.
7. Do not create loose left-aligned rich-text modules. Every module must have a contained card/frame or deliberate table structure.
8. Do not use fake product/shop modules that only mimic Shopify. Use native HubSpot/Shopify integration sections for carts/products when needed.
9. Do not send, schedule, publish marketing emails, mutate CRM records, or alter HubSpot workflows from this skill.
10. HubSpot Design Manager deployment is a live write. Upload only the intended module folders/files, and do not use `--clean` unless replacing the whole destination by explicit instruction.

## Design Baseline

Email is not web. Use table-based structure, inline critical styles, 600px wrapper, 568px internal cards where applicable, 480px mobile breakpoint, and readable behavior with images blocked.

Current email-module palette is Core Palette v1 (seven colors), per `specs/PLATFORM_EMAIL.md` in `brand-design-system` — the authoritative source, verified against the brand guide 2026-07-03:

- `#0F0F0F` Ink Black — highest-contrast ink, wordmark text, primary CTA fill on light surfaces.
- `#1B1B1B` Body Black — primary body text, footer authority, default dark email panel.
- `#2A2929` Soft Black — secondary text, dark card surface, footer text hierarchy.
- `#14213D` Harbor Navy — dark authority panels, structured support modules, selected-state emphasis.
- `#E5E5E5` Soft Silver — email body background, light card surface, text on dark.
- `#D6D6D6` Muted Silver — borders, dividers, muted fields, secondary light fills.
- `#A63E1B` Copper Clay — small accent only: eyebrow, focus cue, proof marker, small rule. Never the default CTA fill.

This replaces the pre-migration six-color palette. If a module (local source or live Design Manager) is still on the old values — `#333533` (old "Deep Charcoal", now split into Body Black `#1B1B1B` / Soft Black `#2A2929`) or `#E06A2A` (old Copper Clay) — that is exactly the kind of residue the standard workflow's cleanup scans (step 6 below) should catch and migrate.

Approved logo masters live in `/Users/vMac/08_brand/Hair Solutions Co Logos`. Email-safe cropped exports were uploaded to HubSpot File Manager under `brand/hair-solutions-co-logos/email-exports/`. Light modules use ink logos; dark modules use soft-silver logos.

## Standard Workflow

1. Read `references/module-inventory.md` and inspect the relevant module folder.
2. Check repo status; preserve unrelated local changes.
3. Make focused edits to module `fields.json`, `meta.json`, and/or `module.html`.
4. Regenerate inventory:

```bash
npm run generate:hubspot-modules
```

5. Validate:

```bash
npm run lint
npm run build
```

6. Run targeted residue scans for the task, usually old palette names/hexes, old logo URLs, `hsc_`, `hsc-`, `legacy`, `archive`, `not found`, `global": true`, and `"locked": true`.
7. Deploy only changed module folders/files when explicitly approved or when the current task already includes deployment.
8. Fetch the live HubSpot copy back to `/tmp` and verify live source, not just upload success.
9. Summarize changed files, deployed paths, checks, and residual risks. Separate Design Manager module updates from existing email draft instances.

## When Existing Emails Stay Broken

Changing module defaults does not always fix already-dropped module instances in existing HubSpot emails. Existing drafts may retain saved body values, stale `module_id`, or module-id-only widget shapes.

If the user reports a specific draft still locked or stale, inspect that email draft separately. Repair drafts only with explicit approval and never publish/send.
