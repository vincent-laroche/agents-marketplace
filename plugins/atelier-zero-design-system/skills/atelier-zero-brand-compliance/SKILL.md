---
name: atelier-zero-brand-compliance
description: Perform a strict, evidence-backed Hair Solutions Co. Atelier Zero v7 brand-compliance audit of a web page, Shopify surface, HTML or HubSpot email marketing template, social post, carousel, Story, Reel cover, thumbnail, or complete branded social series. Use before shipping, publishing, sending, scheduling, or approving customer-facing work, or whenever the user asks whether an artifact is on-brand. Audit only by default; do not edit unless explicitly asked.
---

# Atelier Zero brand compliance

Act as an independent brand guardian. Inspect the artifact that actually exists. Do not infer compliance from a brief, mock description, or clean build result.

## Default boundary

- Audit only unless the user explicitly asks for fixes.
- Do not publish, deploy, send, schedule, approve consent, or mutate production.
- Do not generate missing brand imagery or substitute stock photography.
- Never downgrade a missing evidence requirement to a pass.

## Open the authority gate

1. Read the adjacent `atelier-zero-design-system` skill.
2. Run its `scripts/check_sources.py`.
3. Read:
   - `/Users/vMac/08_brand/brand-design-system/PROJECT.md`;
   - `/Users/vMac/08_brand/brand-design-system/AGENTS.md`;
   - the relevant section of `brand-design-system.html`;
   - `brand-design-system.html`, `tokens/tokens.json`, `tokens/tokens.css`, and `styles/atelier-zero.css` for visual judgments;
   - `specs/COMPONENT_CONTRACTS.md`, `specs/COMPOSITION_RULES.md`, and `specs/DECISION_TREES.md` for application rules;
   - the canonical repository `SKILL.md`;
   - the task-relevant tokens, component, composition, decision, voice, audience, and platform specifications.
4. Inspect the destination project’s instructions and the real artifact.

Stop if canonical verification fails. Report source drift as a blocker instead of auditing against uncertain rules.

## Classify the target

- **Web:** URL, local HTML, screenshot, component, Shopify section/template, or page family.
- **Email:** rendered email, source HTML/HubL, HubSpot module/template, preview, or screenshot.
- **Social:** individual asset, carousel, Story set, Reel/TikTok cover, video frame sequence, caption set, thumbnail, or campaign series.
- **Mixed:** audit each channel independently, then add cross-channel consistency findings.

Load only the matching reference:

- Web: `references/web-audit.md`
- Email: `references/email-audit.md`
- Social: `references/social-audit.md`

Always load `references/report-contract.md`.

Within a channel, classify the implementation subtype before applying checks. Mark genuinely irrelevant requirements `N/A` with a short reason—for example, Shopify schema and cart logic are `N/A` for a standalone static web page. Do not use `N/A` for evidence that should exist but was not inspected; that is `NOT VERIFIED`.

## Inspect evidence

Use every supplied form of evidence:

- inspect source for literal colors, tokens, fonts, structure, semantics, alt text, motion, and hidden states;
- inspect rendered output at the required dimensions;
- inspect copy, claims, product facts, CTA posture, and consent dependencies;
- inspect the full series or page sequence when adjacency and rhythm matter;
- verify changing facts against the live owner when access is available;
- record inaccessible requirements as `NOT VERIFIED`, not `PASS`.

For screenshots without source, audit what is visible and explicitly list source-only checks that remain unverified. For source without rendering, audit implementation evidence and explicitly list visual checks that remain unverified.

## Apply the compliance matrix

Evaluate every applicable category:

1. authority and source provenance;
2. logo and font provenance;
3. palette, contrast, and Coral discipline;
4. typography roles and hierarchy;
5. spacing, container, grid, radii, surfaces, and elevation;
6. components, states, focus, motion, and responsive behavior;
7. imagery truth, consent, and artwork restrictions;
8. voice, dignity, claims, and changing business facts;
9. platform-specific structure and compliance;
10. final rendering, accessibility, and operational readiness.

Do not equate structural validity, successful builds, or platform acceptance with brand compliance.

## Severity

- **BLOCKER:** unapproved logo/media, fabricated or unsupported claim, missing required consent, unreadable critical content, broken primary task, absent legal email content, canonical-source failure, or customer harm/trust risk.
- **MAJOR:** clear token/type/layout/component/platform violation that materially changes the brand, accessibility, comprehension, or conversion flow.
- **MINOR:** localized deviation with limited customer impact and a straightforward correction.
- **NOTE:** improvement or observation that is not a brand-rule violation.

## Verdict

- `COMPLIANT`: no blockers or majors, all release-critical evidence verified, and only optional notes remain.
- `CONDITIONAL`: no blocker is proven, but one or more required checks are not verified or minor fixes remain.
- `NON-COMPLIANT`: any blocker or major violation exists.

Never issue `COMPLIANT` when source, rendering, consent, live facts, or required platform states are unavailable.

## Report

Follow `references/report-contract.md` exactly. Lead with the verdict, then evidence. Give each finding:

- severity and stable ID;
- channel and location;
- observed evidence;
- governing source and rule;
- customer/brand impact;
- exact remediation;
- verification needed after remediation.

When asked to fix after the audit, preserve the report as the baseline, change only approved scope, and rerun every failed and release-critical check.
