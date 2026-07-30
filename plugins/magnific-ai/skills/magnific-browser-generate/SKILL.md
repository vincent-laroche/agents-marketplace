---
name: magnific-browser-generate
description: Safely operate Magnific's Image Generator in a browser after a user authorizes the run. Use for browser-based Magnific generation, unlimited-mode questions, reference attachment, or preventing accidental credit use.
---

# Magnific browser generation

Use `magnific-model-limits` before this skill. A browser generation changes the user's account and may create paid work, so do not execute it merely because this skill is loaded.

## Required sequence

1. Resolve and inspect source images; choose the output project before opening the generator.
2. Draft the prompt outside the UI. For identity-sensitive work, use `magnific-prompt-craft`.
3. Open `https://www.magnific.com/app/ai-image-generator` and wait for the panel to hydrate. Work from fresh screenshots because controls reflow after references or a long prompt are added.
4. Choose model, reference images, count, aspect ratio, and resolution **before** entering a long prompt. The observed UI can push controls out of reach after the prompt expands.
5. Turn off AI prompt rewriting if preserving deliberate wording matters.
6. Attach references in the intended order. Their click order may define their sequence in the prompt; confirm the displayed count and model reference limit.
7. Run the credit preflight from `magnific-model-limits`. If the live panel does not explicitly show unlimited status, stop and seek approval for the displayed cost.
8. Re-read the prompt, selected project, model, resolution, count, and reference count. For a paid run, show this exact proposed action and await approval.
9. Only after approval, click Generate. Wait for completion, inspect actual image output, file it deliberately, and compare account balance when the run was expected to be unlimited.

## Observed interface pitfalls — recheck live

- The model-name control and its nearby chevron were separate targets in the 2026-07-26 UI; the chevron could collapse the panel. Screenshot before clicking.
- Project filtering controls which History assets appear in the reference picker. Missing items often indicate the wrong project filter, not lost assets.
- Changing model can reduce the allowed reference count and silently remove attached references. Recheck them after every model change.
- A model's unlimited badge is not enough. Resolution and the final panel's unlimited indicator must agree.
- Do not batch blindly through the Generate click. Confirm the immediately preceding UI state first.

## Completion and review

- Browser-generated results should appear in the selected project's History/Creations view. Use current MCP tools or UI inspection to retrieve and file them; inspect the rendered image, not only metadata.
- Create or update a review Space only when the user asks or when the task already calls for a comparison set. Add source and output together so review is meaningful.
- Signed output URLs can expire. Re-fetch through the supported surface rather than saving credentials or signed URLs into project files.

Never substitute an undocumented private browser endpoint, injected request interceptor, or automated replay for the visible, user-authorized UI flow.
