# HubSpot Email Modules Deployment Playbook

Use this playbook for Hair Solutions Co. Design Manager email-module deploys.

## Local Checks

Work from:

```bash
cd "/Users/vMac/03_agents/Projects/Email Marketing/Email Marketing Studio"
```

Regenerate inventory after module structural changes:

```bash
npm run generate:hubspot-modules
```

Validate:

```bash
npm run lint
npm run build
```

Common residue scans:

```bash
rg -n 'hsc_|hsc-|legacy|archive|not found|global": true|"locked": true' hubspot/design-manager/email_modules
rg -n 'A1-wordmark|wm_|mono_|placeholder logo|Old vs new brand' hubspot/design-manager/email_modules lib
rg -n '#333533|#E06A2A|Deep Charcoal' hubspot/design-manager/email_modules
```

The third scan catches the pre-migration six-color palette (old "Deep Charcoal" `#333533`, old Copper Clay `#E06A2A`). Current Core Palette v1 is seven colors — see `SKILL.md` Design Baseline and `specs/PLATFORM_EMAIL.md` in `brand-design-system` for the authoritative hex table. Adapt palette scans to the current brand guide and the task.

## Upload Changed Modules

Upload only intended changed folders. Do not use `--clean` for normal changes.

```bash
hs cms upload \
  hubspot/design-manager/email_modules/core/email_header.module \
  email_modules/core/email_header.module \
  --account 50966981 \
  --cms-publish-mode publish
```

For multiple folders, loop over an explicit allowlist. Avoid broad folder uploads when unrelated local changes exist.

## Fetch Live Verification

Always verify live Design Manager source after upload:

```bash
rm -rf /tmp/hsc-email-modules-verify
hs cms fetch email_modules /tmp/hsc-email-modules-verify --account 50966981
```

Then verify:

- module count and expected folders;
- labels follow naming grammar;
- Light/Dark pair parity;
- `global: false`;
- no `locked: true`;
- approved palette/logo URLs only;
- no `hsc_`, `hsc-`, `legacy`, `archive`, or `not found` in active modules.

## File Manager Logos

Approved logo folder:

`/Users/vMac/08_brand/Hair Solutions Co Logos`

Upload source logos if needed:

```bash
hs filemanager upload \
  "/Users/vMac/08_brand/Hair Solutions Co Logos" \
  brand/hair-solutions-co-logos \
  --account 50966981
```

The source PNGs are square. For email display, use cropped email-safe exports derived from those files; otherwise wordmarks render as tall empty squares.

Verify public file URLs with HTTP 200 before using them in module defaults.

## Known Failure Modes

### "The creator prevented editing this module"

Likely causes:

- `global: true` in `meta.json`;
- field entries have `locked: true`;
- the email draft inserted the module as a module-id-only widget;
- the draft widget still carries `module_id` instead of path-based module body.

Fix modules first:

- set `global: false`;
- set all fields `locked: false`;
- upload only corrected `meta.json` or `fields.json` when that is the only intended change.

Fix existing drafts only with explicit approval:

- use path-based widget body;
- include `body.path`;
- include `schema_version: 2`;
- include `css_class: dnd-module`;
- remove custom-module `module_id` from wrapper/body;
- include editable field payloads.

Do not publish or send the email while repairing a draft.

### Local source passes, HubSpot still differs

Upload success is not enough. Fetch the Design Manager folder back and inspect live source. Local validation does not prove HubSpot accepted the intended structure.

### Existing emails still show old defaults

Module default changes do not always update already-dropped email instances. Existing drafts can retain saved field values. The fix is to reinsert the module or patch that specific draft instance.

### Product/cart modules

Use HubSpot native Shopify/cart/product integration sections for actual cart/product data. Delete fake custom modules that mimic product integration with static editable images/text unless the user explicitly wants mockup-only modules.

## Safe Report Format

End with:

- files/modules changed;
- HubSpot paths uploaded;
- validation commands run;
- live fetch verification result;
- what was not touched, especially marketing email drafts, sends, CRM data, workflows, or unrelated local changes.
