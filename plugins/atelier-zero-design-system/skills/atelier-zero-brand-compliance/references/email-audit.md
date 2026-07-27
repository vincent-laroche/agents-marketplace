# Email marketing audit

Read the canonical voice rules and `specs/PLATFORM_EMAIL.md`. Email constraints override web conventions where inbox rendering, dark mode, editability, accessibility, or compliance would otherwise weaken.

## Evidence

Inspect source and rendered previews where available:

- desktop at the 600px wrapper;
- mobile at or below 480px;
- real-contact personalization preview with fallbacks;
- image-blocked state;
- plain-text version;
- Gmail web and mobile;
- Apple Mail light and dark;
- Outlook Windows;
- iOS Mail;
- every link and CTA destination.

Missing client previews remain `NOT VERIFIED`; do not infer them from one browser render.

## Structure and rendering

- Table-based wrapper and module rows.
- Critical styles inline.
- No JavaScript, forms, sticky UI, CSS Grid as primary structure, or hover-only meaning.
- Wrapper is no wider than 600px.
- Mobile body text is at least 16px and controls are approximately 44px high or larger.
- Images have width, height, and meaningful alt text.
- The message remains understandable with images blocked.

## Email palette and type

- Use literal approved uppercase hex values.
- Paper is the outer canvas; Raised/Wash/Canvas Shaded follow module roles; Ink Panel is limited to footer and one authority panel.
- Coral is the one primary CTA fill/signal and remains controlled.
- CTA labels use Text Ink on Coral.
- Use Arial/Helvetica for headings, body, buttons, captions, and product details; Georgia/Times italic for short emphasis only; Courier for metadata.
- Do not load or depend on webfonts.

## HubSpot editability

- Operators edit fields, not raw HTML.
- Approved defaults are present without arbitrary palette exposure.
- Personalization tokens have truthful fallback text.
- Optional fields collapse cleanly.
- CTA label and URL are separate fields.
- Image fields provide alt-text guidance.
- Existing field identifiers needed for module compatibility remain intact.

## Message and compliance

- One dominant message and one primary CTA.
- Subject and preheader are truthful and distinct.
- No pressure, pity, shame, fake urgency, medical framing, guarantee, or invented offer.
- Product facts, prices, availability, dates, and policy details are verified live.
- Testimonial and customer media have channel-specific consent.
- Footer includes required sender identity, postal address, unsubscribe, and preference links.
- Subscription type and consent cannot be proven by design alone; mark them `NOT VERIFIED` until account evidence is checked.

Structural validity, successful HubSpot upload, and inbox rendering are separate from brand approval. Report each independently.
