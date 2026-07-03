# email-marketing-modules (v1.0.0)

HubSpot Design Manager email-module toolkit for **Hair Solutions Co.** — account `50966981`.

## What's inside

**Skills (1)**
- `hubspot-email-modules` — local module source, naming grammar, light/dark variant parity, editability rules (`global`/`locked`), logo policy, cleanup residue scans, standard edit workflow, and deployment/verification steps.

**References**
- `references/module-inventory.md` — the active folder system (`core/`, `launch/`, `newsletter/`), naming grammar, the full 36-module (18 light/dark family) inventory table, forbidden structures, and logo rules.
- `references/deployment-playbook.md` — local validation commands, `hs cms upload` usage, live fetch verification, known HubSpot editability failure modes and fixes, and the safe report format.

## Canonical source this plugin points at
- Local repo: `/Users/vMac/03_agents/Projects/Email Marketing/Email Marketing Studio`
- Module source: `hubspot/design-manager/email_modules`
- HubSpot Design Manager destination: `email_modules/` in account `50966981`

## Non-negotiables (see SKILL.md for the full list)
- Active modules live only under `core/`, `launch/`, `newsletter/` unless a real new journey is being created.
- Every active module family needs exactly one Light and one Dark variant.
- Every module must be drag-and-drop editable: `global: false`, every field `locked: false`.
- Never send, schedule, publish marketing emails, mutate CRM records, or alter HubSpot workflows from this skill — it is module-source work only.
- Deployment is a live write. Upload only intended module folders; never `--clean` without explicit instruction.

## Palette
`SKILL.md` ("Design Baseline") reflects the current seven-color Core Palette v1 (`specs/PLATFORM_EMAIL.md` in `brand-design-system` is the authority: Ink Black `#0F0F0F`, Body Black `#1B1B1B`, Soft Black `#2A2929`, Harbor Navy `#14213D`, Soft Silver `#E5E5E5`, Muted Silver `#D6D6D6`, Copper Clay `#A63E1B`). The deployment playbook's residue scans include a check for the retired pre-migration hex values (`#333533`, `#E06A2A`) so any live or local module still on the old palette gets caught.

## Install
Settings → Capabilities → add marketplace by GitHub repo (`vincent-laroche/hairsolutionsco-ai-toolkit`), then enable the `email-marketing-modules` plugin.
