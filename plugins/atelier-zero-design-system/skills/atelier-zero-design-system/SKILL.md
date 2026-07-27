---
name: atelier-zero-design-system
description: Apply, translate, audit, or verify the optimized Hair Solutions Co. Atelier Zero v7 design system for customer-facing web pages, Shopify sections, email templates, social posts, presentations, prototypes, copy, logos, imagery, and design-system decisions. Use whenever work must follow the current brand authority, when reviewing brand compliance, or when resolving conflicting brand values. Read the live repository and approved asset sources before acting; never use cached brand values.
---

# Atelier Zero design system

Operate from the live system at `/Users/vMac/08_brand/brand-design-system`. Use `/Users/vMac/08_brand/logos` as the only approved logo directory. Current filesystem evidence outranks copied guides, project-local tokens, screenshots, and memory.

## Choose the mode

- **Create or translate:** apply Atelier Zero while preserving the destination platform’s functional constraints.
- **Audit:** inspect source and rendering before judging. Invoke `$atelier-zero-brand-compliance` for the dedicated audit workflow.
- **Fix:** make the smallest compliant change only when the user asks for implementation.
- **Govern:** update the master, tokens, specs, verifier, repository skill, packaged skill, and installed skill together.

## Establish authority

1. Read `PROJECT.md`, `AGENTS.md`, and the relevant section of `brand-design-system.html`.
2. For visual work, read `/Users/vMac/08_brand/atelier-zero-design-system-from-theme.md`.
3. Read the canonical repository `SKILL.md`.
4. Load only the relevant portable sources:
   - tokens and web reference: `tokens/` and `styles/atelier-zero.css`;
   - components and layouts: `specs/COMPONENT_CONTRACTS.md`, `COMPOSITION_RULES.md`, and `DECISION_TREES.md`;
   - voice and audience: `specs/brand_voice.md`, `CUSTOMER_AVATARS.md`, and `COMPETITORS.md`;
   - channel: `specs/PLATFORM_SHOPIFY.md`, `PLATFORM_EMAIL.md`, or `PLATFORM_SOCIAL.md`.
5. Inspect the destination project and its local instructions.
6. Run this skill’s `scripts/check_sources.py`.

Stop on source-check failure. Report the exact drift instead of selecting a value by date.

## Resolve authority

- The masterfile defines Hair Solutions Co. intent, identity, audience, voice, safety, and governance.
- The measured theme source controls visual palette, geometry, signature motifs, interaction posture, and responsive reconstruction.
- Do not transfer its original technical-product copy, product names, coordinates, or licensing language.
- Production accessibility overrides low-contrast reference decoration: use Text Ink on Coral controls and readable Ink for essential metadata.

## Apply Atelier Zero v7

### Palette and surfaces

- Paper `#EAE0C9` is the grain-bearing canvas.
- Wash `#EDE3CC`, Canvas Shaded `#E4DBC4`, and Raised `#F6EFD9` form the light surface ramp.
- Text Ink `#151411` owns headings and controls; Body Ink `#25221D` owns running copy.
- Ink Panel `#181714` is the one deliberate dark interruption.
- Coral `#EA6452` is the only saturated UI color and stays under roughly 10% of a composition.
- Printed ochre `#C0893B` and printed coral `#DA6F4B` are commissioned-artwork colors only.
- Do not introduce gradients, glass effects, pure-white cards, arbitrary status colors, or undocumented aliases.

### Type

- Inter Tight: H1–H4, navigation, labels, buttons, and UI.
- Inter: body, leads, forms, and functional copy.
- Playfair Display italic: one short inline phrase inside H1 or H2 only.
- JetBrains Mono: 13px metadata, dates, SKUs, specs, and compact evidence.
- Scale: display/H1 up to 70px; H2 32px; H3 32px; H4 22px; body 18px; small 14px; micro/eyebrow 11px.
- End display headlines with one Coral terminal period.

### Geometry and composition

- Use the spacing ladder 4, 8, 12, 16, 24, 32, 48, 64, 96, 128px.
- Use a 1300px maximum container, responsive 20–64px side padding, and a 24px gutter.
- Use 96px desktop and 72px mobile section rhythm.
- Radius roles: 4px forms/gallery plates, 8px stage/nested surfaces, 16px cards/major media/Ink panels, 999px actions and pills.
- Use the 37px inset frame and 11px micro-cap rails only on suitable desktop editorial surfaces at 1024px and above.
- Start with one hero. Left-align content leading to grids, lists, media, or tables. Center only a single statement, pull quote, focused CTA band, or simple hero.
- Never stack full-width dark sections.

### Components and interaction

- Primary: 56px Coral pill, Text Ink label, no border, shadow, lift, or scale.
- Secondary: transparent pill, Text Ink label, 1px Hairline border.
- Keep one primary action per decision area.
- Light cards use Raised, 16px radius, no border, and no shadow.
- Wash cards inside Ink Panel may rotate up to ±2° and use the one approved true shadow.
- Forms need persistent labels, 4px radius, at least 44px height, clear errors, and visible focus.
- Focus: 2px Coral on light, 2px Wash inside Ink Panel, both with 2px offset.
- Hover may change color/border, invert a nested arrow, or scale a clipped image up to 1.03. Never lift cards or buttons.
- Use 180ms color/border transitions and at most 420ms movement. Respect reduced motion.
- Preserve semantic headings, keyboard order, touch targets, alt text, stable media dimensions, and non-color state meaning.

### Signature devices

Use selectively: Coral folio and terminal period, route/status micro-caps, inset frame and rails, asymmetric hero, 2×2 capability cards, four-up method row, five-up editorial plates, two-up testimonials, Coral sequence numerals, one active Coral filter/progress mark, square registered plates, dotted-circle annotation, and dashed footer progress rule.

## Protect assets, truth, and dignity

- Use only logos from `/Users/vMac/08_brand/logos`; verify filenames and hashes against `manifests/logos.json`.
- Use only the four font binaries in `manifests/fonts.json`.
- Use approved photography or owner-approved commissioned artwork. Never generate brand imagery or use stock photography.
- Preserve identity, skin, hair, hairline, base construction, density, color, texture, scale, and truthful results.
- Require exact-use consent for customer media, testimonials, DMs, voice, and before/after assets.
- Speak as “we” to “you” with calm, specific, adult language.
- Never use pity, shame, rescue, urgency, scarcity, hype, emoji, exclamation marks, medical framing, guarantees, or invented facts.
- Verify changing commerce and policy facts from their live owner.
- A compliant draft is not permission to publish, send, schedule, deploy, or modify production.

## Route by channel

- **Web and Shopify:** preserve editor behavior, dynamic sources, SEO, accessibility, mobile behavior, and commerce logic. Do not use Shopify CLI or publish without approval.
- **Email:** follow the inbox-specific literal-hex, table, inline-style, safe-font, fallback, image-blocked, plain-text, and compliance rules.
- **Social:** keep one idea per asset; choose product, person, or message; protect safe zones, grid rhythm, compression legibility, consent, captions, and alt text.
- **Documents and prototypes:** translate the system without importing a generic template aesthetic; label non-production placeholders.

## Completion gate

Run the canonical verifier, inspect the real output at relevant sizes and states, confirm logo/font provenance, verify live claims, check accessibility/consent/truthful media, separate violations from unavailable evidence, and state every remaining production approval.
