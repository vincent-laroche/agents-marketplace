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

The email palette is the Atelier Zero set, per `specs/PLATFORM_EMAIL.md` in `brand-design-system` — the authoritative source, re-verified 2026-08-18:

Only three values may be a **main surface** — the background of a header, a footer, or any main section:

- `#EFE7D2` Paper — the light section surface, and the email body behind it.
- `#15140F` Ink — the dark section surface.
- `#ED6F5C` Coral — accent block. At most one per email, never on a header or footer.

Everything else is **supporting**: permitted on inset elements inside a section, on dividers, or as text, never as a section background.

- `#F7F1DE` Bone — text on Ink; a raised inset panel on Paper.
- `#DDD2B6` Paper Dark — dividers and rules on Paper; secondary text on Ink; a recessed inset panel on Paper.
- `#2A2620` Ink Soft — dividers and rules on Ink; an inset panel on Ink.
- `#5A5448` Ink Mute — muted body copy and captions on light.
- `#F08E7C` Coral Soft — limited emphasis on Ink panels.
- `#6E7448` Olive — success or structured utility state only.
- `#E9B94A` Mustard — focus/caution utility only; not decorative.

**Core Palette v1 is retired.** If a module — local source or live Design Manager — is still on `#0F0F0F` Ink Black, `#1B1B1B` Body Black, `#2A2929` Soft Black, `#14213D` Harbor Navy, `#E5E5E5` Soft Silver, `#D6D6D6` Muted Silver or `#A63E1B` Copper Clay, that is residue the cleanup scans (step 6 below) should catch and migrate. The older `#333533` Deep Charcoal and `#E06A2A` Copper Clay are residue too.

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
