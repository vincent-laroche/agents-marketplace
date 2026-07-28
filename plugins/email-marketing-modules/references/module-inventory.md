# Hair Solutions Co. HubSpot Email Module Inventory

Current local source:

`/Users/vMac/03_agents/Projects/Email Marketing/Email Marketing Studio/hubspot/design-manager/email_modules`

HubSpot destination:

`email_modules/` in account `50966981`.

## Active Folder System

Only these active top-level folders are expected:

- `core/`: reusable modules used across journeys and templates.
- `launch/`: launch-specific modules and copy structures.
- `newsletter/`: recurring editorial/newsletter modules.

Do not revive old wrapper folders, archived folders, `reference markdown files`, fake shop folders, or `hsc_*` names.

## Naming Grammar

HubSpot labels must follow:

`{Scope} - {Block type} - {Descriptor} - {Light|Dark}`

Examples:

- `CORE - Header - Centered logo - Light`
- `Launch - Text - Founder pillars - Dark`
- `Newsletter - Two-column - Image and text - Light`

Rules:

- `CORE` means reusable across journeys.
- Journey names like `Launch`, `Newsletter`, `Welcome`, `Cart`, or future campaigns mean journey/campaign-specific.
- Block type should be functional and close to HubSpot primitives: Header, Footer, Text, Image, Products, Button, Two-column.
- Descriptor must explain the job. Avoid vague names such as `steps`, `reassurance`, `urgency queue`, `status badge`, `legacy`, or abbreviations.
- Light/Dark suffix is required on every active module.

## Active Modules

There are 36 active modules, 18 light/dark families.

| Label | Folder |
|---|---|
| CORE - Text - Base type guidance - Light | `core/base_type_guidance.module` |
| CORE - Text - Base type guidance - Dark | `core/base_type_guidance_dark.module` |
| CORE - Text - Customer snapshot - Light | `core/customer_snapshot.module` |
| CORE - Text - Customer snapshot - Dark | `core/customer_snapshot_dark.module` |
| CORE - Footer - Standard - Light | `core/email_footer.module` |
| CORE - Footer - Standard - Dark | `core/email_footer_dark.module` |
| CORE - Header - Centered logo - Light | `core/email_header.module` |
| CORE - Header - Centered logo - Dark | `core/email_header_dark.module` |
| CORE - Products - Goal-based recommendation - Light | `core/goal_based_recommendation.module` |
| CORE - Products - Goal-based recommendation - Dark | `core/goal_based_recommendation_dark.module` |
| CORE - Text - Lifespan next step - Light | `core/lifespan_next_step.module` |
| CORE - Text - Lifespan next step - Dark | `core/lifespan_next_step_dark.module` |
| Launch - Text - Belief list - Light | `launch/launch_belief_list.module` |
| Launch - Text - Belief list - Dark | `launch/launch_belief_list_dark.module` |
| Launch - Text - Five changes - Light | `launch/launch_feature_list_5.module` |
| Launch - Text - Five changes - Dark | `launch/launch_feature_list_5_dark.module` |
| Launch - Text - Founder pillars - Light | `launch/launch_founder_pillars.module` |
| Launch - Text - Founder pillars - Dark | `launch/launch_founder_pillars_dark.module` |
| Launch - Products - Three product grid - Light | `launch/launch_product_grid3.module` |
| Launch - Products - Three product grid - Dark | `launch/launch_product_grid3_dark.module` |
| Launch - Text - Question list - Light | `launch/launch_question_list.module` |
| Launch - Text - Question list - Dark | `launch/launch_question_list_dark.module` |
| Launch - Image - Logo system - Light | `launch/launch_wordmark_pair.module` |
| Launch - Image - Logo system - Dark | `launch/launch_wordmark_pair_dark.module` |
| Newsletter - Button - Primary CTA - Dark | `newsletter/newsletter_cta_dark.module` |
| Newsletter - Button - Primary CTA - Light | `newsletter/newsletter_cta_light.module` |
| Newsletter - Image - Feature story - Dark | `newsletter/newsletter_feature_dark.module` |
| Newsletter - Image - Feature story - Light | `newsletter/newsletter_feature_light.module` |
| Newsletter - Footer - Standard - Dark | `newsletter/newsletter_footer_dark.module` |
| Newsletter - Footer - Standard - Light | `newsletter/newsletter_footer_light.module` |
| Newsletter - Text - Masthead - Dark | `newsletter/newsletter_masthead_dark.module` |
| Newsletter - Text - Masthead - Light | `newsletter/newsletter_masthead_light.module` |
| Newsletter - Text - Pull quote - Dark | `newsletter/newsletter_pullquote_dark.module` |
| Newsletter - Text - Pull quote - Light | `newsletter/newsletter_pullquote_light.module` |
| Newsletter - Two-column - Image and text - Dark | `newsletter/newsletter_two_column_dark.module` |
| Newsletter - Two-column - Image and text - Light | `newsletter/newsletter_two_column_light.module` |

## Deleted Or Forbidden Structures

These were intentionally removed or should not be recreated:

- Global modules that lock drag-and-drop editing.
- Field-level `locked: true` settings.
- `hsc_`, `hsc-`, or other HSC-prefixed module names.
- `legacy`, archived, not-found, and duplicated folder systems.
- Fake custom `shop` modules that only simulate product/cart content with editable images/text.
- Newsletter `warm` variants.
- Launch-specific headers; the good launch centered-header design became CORE header light/dark.
- Old A1 wordmark defaults and old placeholder logo pair defaults.

## Logo Rules

Approved master logos:

`/Users/vMac/08_brand/logos` (see `/Users/vMac/08_brand/brand-design-system/manifests/logos.json` for the current approved filenames and hashes)

The final approved set (2026-07-28) is the `stacked-*` (full lockup) and `monogram-*` families, each in dark/light ink on light/dark/transparent backgrounds. For a HubSpot email-safe re-export, use as source:

- Light-canvas header: `stacked-dark-on-transparent-bg-1000x500.png`
- Dark-canvas header: `stacked-light-on-transparent-bg-1000x500.png`
- Light-canvas monogram: `monogram-dark-on-transparent-bg-1200x1200.png`
- Dark-canvas monogram: `monogram-light-on-transparent-bg-1200x1200.png`

NOTE: the previously documented `brand/hair-solutions-co-logos/email-exports/` path and its `wordmark-ink-black-email.png` / `wordmark-soft-silver-email.png` / `monogram-*-email.png` filenames do not exist anywhere in this repository or its HubSpot destination as far as this toolkit can verify. Treat those as stale until a real HubSpot-hosted email-safe export is regenerated from the files above and this section is updated with its real location.

Headers display the cropped wordmark at `width="320"` with `max-width:100%`.

## Design Notes

- Every module should have a contained frame/card or deliberate table structure.
- Loose left-aligned text directly on the email canvas is not acceptable.
- Transparent outer wrappers are preferred so the email body controls gray/background; the module itself still needs an internal visual container.
- Use native HubSpot/Shopify integration sections for real cart/product blocks. Do not create fake product integration modules.
