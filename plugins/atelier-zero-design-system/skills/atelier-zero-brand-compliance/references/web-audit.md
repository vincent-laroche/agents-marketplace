# Web and Shopify audit

Read the canonical tokens, component contracts, composition rules, decision trees, voice rules, and `specs/PLATFORM_SHOPIFY.md`.

Classify the target as `static web`, `web application`, or `Shopify`. Apply the shared web checks to all three. Apply Shopify integrity checks only to Shopify artifacts; mark them `N/A — non-Shopify target` for static sites and other applications. Missing relevant source or runtime evidence remains `NOT VERIFIED`.

## Evidence

Prefer both source and rendered behavior. Inspect at minimum:

- 375px mobile;
- 768px tablet;
- 1440px desktop;
- keyboard focus and navigation;
- hover, active, disabled, error, loading, open/closed, empty, and sold-out states when applicable;
- reduced-motion behavior;
- image loading and stable dimensions.

For a page family, sample every distinct template and shared section type. For Shopify, work from the GitHub-synced theme repository and live/read-only surfaces; never use Shopify CLI.

## Authority and assets

- All design values resolve to current `--az-*` tokens or platform-required approved literals.
- Logos come from `/Users/vMac/08_brand/logos`, preserve aspect ratio and clear space, and match the manifest hash.
- Only the four approved fonts appear.
- Media is approved and truthful; no generated brand imagery, stock photography, copied storefront logo, or altered product/customer result.

## Visual system

- Paper grain is present without visible tiling.
- Paper-family surfaces follow their documented roles.
- Ink Panel is deliberate; full-width dark sections do not stack.
- Coral is the only saturated UI color and stays controlled.
- Essential text uses readable Ink or Wash; low-contrast muted/faint tokens stay nonessential.
- Cards, media, forms, pills, spacing, container, gutter, and section rhythm follow their fixed roles.
- Light cards are borderless and shadowless.
- Primary/secondary action hierarchy, focus, disabled, and hover behavior follow component contracts.
- Signature devices are selective and structurally useful, not repeated decoration.

## Structure and responsiveness

- One H1 per page and one H2 per section.
- Headings follow semantic order and v7 type roles.
- Sections leading to grids/lists/media/tables are left-aligned.
- One hero starts the page; dark interruption and CTA band follow composition limits.
- No page-level horizontal overflow.
- Touch targets are at least 44px.
- Text, images, tables, drawers, modals, menus, filters, product forms, and cart-adjacent surfaces remain usable at all required sizes.
- Editorial rails/frame hide below 1024px and never obstruct commerce.

## Shopify integrity

- Preserve theme-editor settings, section schemas, blocks, dynamic sources, app blocks, metafields, localization, SEO, variant logic, sold-out logic, cart, subscriptions, and checkout-adjacent behavior.
- Product names, prices, variants, availability, shipping, returns, guarantees, and policy links come from live owning data.
- No fake rating, stock, badge, countdown, urgency, or unsupported commerce claim.

## Accessibility and performance

- Landmarks, labels, headings, controls, tables, and disclosure semantics are correct.
- Focus is visible on Paper, Raised, Coral, and Ink Panel.
- State does not rely on color alone.
- Media has meaningful alt text, stable width/height, responsive sources, and truthful crops.
- Reduced motion disables nonessential movement.
- No hidden critical content, focus loss, or layout shift.

Mark SEO, analytics, performance, policy, or consent as `NOT VERIFIED` unless the relevant evidence was actually inspected.
