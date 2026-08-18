---
name: email-html-production
description: Build, edit, validate, or review production-grade HTML for Hair Solutions Co. MailerLite campaigns and automation emails, including table layout, responsive behavior, merge tags, preheaders, unsubscribe requirements, tracking, accessibility, dark mode, and client constraints. Use when creating Custom HTML emails, converting approved briefs or modules into MailerLite HTML, fixing render problems, or preparing content for a draft campaign or disabled automation.
---

# Email HTML production

1. Read ../../references/authority-map.md, ../../references/tool-routing.md, and
   ../../references/email-quality-gates.md.
2. Inspect the active renderer and nearby source files before editing. In generated systems, edit the
   content or component source and regenerate; do not hand-edit generated HTML.
3. Use the current brand email specification. Do not copy colors or fonts from old email files as
   authority.
4. Preserve email-safe tables, inline critical styles, a hidden preheader, explicit image sizes,
   plain-language alt text, merge-field fallbacks, tracking, unsubscribe, and sender identity.
5. Run scripts/validate_email.py against every output. Run the project renderer or validator when one
   exists.
6. Review at phone and desktop widths plus image-blocked and dark-mode states. Name clients not tested.
7. Report source files changed, outputs generated, validation, rendering evidence, and unresolved
   dynamic blocks.

Creating HTML is local work. Uploading it, sending a test, scheduling, or activating requires the
corresponding campaign, automation, or release skill.
