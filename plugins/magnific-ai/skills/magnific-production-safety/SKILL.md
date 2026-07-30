---
name: magnific-production-safety
description: "Apply Magnific cost, consent, asset, output, and publication controls before any creation, edit, Space run, Flow run, download, share, or account-changing action. Use whenever a Magnific request could change remote state or spend credits."
---

# Magnific production safety

Magnific is a production surface. A creation, edit, upscale, voice render, Space run, Flow run, stock download, share, move, or deletion changes account state even when it is not visible as a traditional checkout.

## Classify before acting

| Class | Examples | Permission |
|---|---|---|
| Read-only | List models, inspect a Space, view a project, check a creation, simulate cost | Safe to inspect |
| Reversible account change | Create a draft Space, add a Library record, move an asset, change a design page | Ask when it changes agreed organisation or shared work |
| Credit or download action | Generate, edit, upscale, synthesize voice/music, run a Space/Flow, stock download | Exact current-turn approval after preflight |
| External/public action | Share, publish, export for delivery, schedule, replace a customer-facing asset | Exact current-turn approval and destination confirmation |
| Destructive | Delete a creation, Library record, Folder, Space, Flow, or history | Explicit confirmation of exact target |

## Mandatory preflight for anything that may cost credits

1. Identify the exact input, destination project, tool/model, resolution or duration, count, and intended output.
2. Query the current tool/model schema. Never rely on a remembered model menu or plan benefit.
3. Run the relevant official cost simulation:
   - single tool: `simulate_cost`
   - Space: `simulate_spaces`
   - Flow: `simulate_flows`
4. Check `account_balance`. `unlimitedAppliesHere` is authoritative for an MCP action; a browser unlimited badge does not make an API/MCP action free.
5. State the bounded action: number of outputs/runs, displayed cost or unlimited result, input and output location, and what will not happen.
6. Obtain explicit current-turn approval unless the user already authorised that exact preflighted action.
7. Execute the smallest useful proof first when identity, product geometry, continuity, or a new model is involved.
8. Inspect the rendered result and final remote state. Do not infer success from a submitted form.

## Asset and identity controls

- Confirm the source is the intended file and that its project filter is correct before recreating anything that merely appears absent.
- Preserve Hair Solutions product geometry, logos, facial architecture, hairline, hairstyle, texture, and framing when the brief identifies them as protected.
- Use `magnific-prompt-craft` for people, mascots, hair systems, mannequin heads, and marble busts.
- Treat signed upload and asset URLs, access tokens, internal IDs, and user emails as confidential. Do not place them in prompts, project documents, or chat output.
- Do not infer commercial rights from a search result, a template, or a Stock preview. Confirm the current surface's license before customer-facing use.

## Review and handoff

Record: source, chosen tool/model, prompt version, settings, cost result, output creation, visual QC decision, and destination. Keep rejected versions unless the user explicitly asks to remove them. Do not publish or share merely because the render passed visual review.

For browser image work, also read `magnific-model-limits` and `magnific-browser-generate`. For any graph run, read `magnific-spaces-and-flows`.
