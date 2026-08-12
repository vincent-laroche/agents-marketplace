---
name: atelier-zero-design-system
description: Apply, translate, audit, or verify the optimized Hair Solutions Co. Atelier Zero v7 design system for customer-facing web pages, Shopify sections, email templates, social posts, presentations, prototypes, copy, logos, imagery, and design-system decisions. Use whenever work must follow the current brand authority, when reviewing brand compliance, or when resolving conflicting brand values. Read the live repository and approved asset sources before acting; never use cached brand values.
---

# Atelier Zero design system

Operate from the live system at `/Users/vMac/08_brand/brand-design-system`. Use `/Users/vMac/06_design/brand/logos/masterfile-approved` as the only approved logo directory. Current filesystem evidence outranks copied guides, project-local tokens, screenshots, and memory.

## Choose the mode

- **Create or translate:** apply Atelier Zero while preserving the destination platform’s functional constraints.
- **Audit:** inspect source and rendering before judging. Invoke `$atelier-zero-brand-compliance` for the dedicated audit workflow.
- **Fix:** make the smallest compliant change only when the user asks for implementation.
- **Govern:** update the master, tokens, specs, verifier, repository skill, packaged skill, and installed skill together.

## Establish authority

1. Read `PROJECT.md`, `AGENTS.md`, and the relevant section of `brand-design-system.html`.
2. Read the canonical repository `SKILL.md`.
3. For visual work, inspect the relevant section of `brand-design-system.html`, then read `tokens/tokens.json`, `tokens/tokens.css`, and `styles/atelier-zero.css` directly from the canonical repository.
4. Load only the relevant governed sources:
   - tokens and web reference: `tokens/` and `styles/atelier-zero.css`;
   - components and layouts: `specs/COMPONENT_CONTRACTS.md`, `COMPOSITION_RULES.md`, and `DECISION_TREES.md`;
   - voice and audience: `specs/brand_voice.md`, `CUSTOMER_AVATARS.md`, and `COMPETITORS.md`;
   - channel: `specs/PLATFORM_SHOPIFY.md`, `PLATFORM_EMAIL.md`, or `PLATFORM_SOCIAL.md`.
5. Inspect the destination project and its local instructions.
6. Run this skill’s `scripts/check_sources.py`.

Stop on source-check failure. Report the exact drift instead of selecting a value by date.

## Resolve authority

- The masterfile defines Hair Solutions Co. intent, identity, audience, voice, safety, visual direction, and governance.
- The canonical token exports and `styles/atelier-zero.css` control implementation values. Never cache their literal values in this skill or substitute project-local copies.
- The component, composition, decision-tree, and platform specifications control how those values are applied to a particular surface.
- Production accessibility overrides low-contrast reference decoration: use Text Ink on Coral controls and readable Ink for essential metadata.

## Apply Atelier Zero v7

Do not treat this packaged skill as a token or component-value authority. Resolve palette, typography, geometry, spacing, responsive rules, components, interaction, motion, and signature devices from the live sources above for every task. If a remembered value conflicts with the canonical repository, the canonical repository wins and the discrepancy must be reported.

## Protect assets, truth, and dignity

- Use only logos from `/Users/vMac/06_design/brand/logos/masterfile-approved`; verify filenames and hashes against `manifests/logos.json`.
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
