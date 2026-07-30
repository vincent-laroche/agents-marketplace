---
name: magnific-ai
description: "Set up and operate Magnific safely from official documentation and the current product surface. Trigger for Magnific, magnific.com, Magnific MCP, Assistant, Spaces, Flows, templates, Designer, Library, Projects, Stock, 3D Scenes, image/video/voice generation, editing, upscaling, creative assembly, custom agents, durable uploads, or API integration work."
---

# Magnific AI

Use the bundled official documentation snapshot and live MCP tool schemas as the source of truth. Do not invent endpoint paths, model names, parameters, limits, costs, or response fields.

## Start with the right production hub

Route a request before acting. The specialised skills are the operating manual; this core skill owns official-documentation lookup, OAuth/API setup, durable uploads, and integration work.

| Need | Use |
|---|---|
| Cost, approval, ownership, or publication decision | `magnific-production-safety` |
| Assistant-built boards, Spaces, reusable Flows, or episode assembly | `magnific-assistant-orchestration` and `magnific-spaces-and-flows` |
| Image generation, enhancement, variations, image editing, background removal, relight, camera, or crop | `magnific-image-production` plus `magnific-model-limits` |
| Video generation, image-to-video, video editing, continuity, combining, VFX, or upscale | `magnific-video-production` |
| Voice, TTS, music, sound effects, audio isolation, or speech video | `magnific-audio-production` |
| Canvas-style layouts, editable layers, design pages, resize, or brand books | `magnific-designer` |
| Reusable characters/styles/elements/agents, project trees, folders, uploads, or creation filing | `magnific-library-and-projects` |
| Template adoption, Stock, or 3D Scenes | `magnific-templates-stock-3d` |
| Hair-system or marble-bust prompt fidelity | `magnific-prompt-craft` |
| One authorised browser image run | `magnific-browser-generate` |

Live account observations are routing evidence only. Re-read current tool schemas and UI before actions because Magnific changes models, entitlements, and interfaces frequently.

## Core workflow

1. Classify the request: account/project setup, discovery, generation/editing, task status, asset retrieval, analytics, or integration.
2. For MCP connection, projects, custom agents, durable project uploads, or upload verification, read `references/platform-setup.md` before acting.
3. Search the documentation before choosing an endpoint:

   ```bash
   python3 scripts/search_docs.py "creative upscaler"
   python3 scripts/search_docs.py "kling 3 image to video" --show
   python3 scripts/search_docs.py "webhook security" --show
   ```

4. Read only the relevant section from `references/llms-full.txt`. Use `references/api-index.md` when browsing categories or exact endpoint names.
5. Confirm required inputs, accepted formats, model/version, output settings, rate limits, and whether the operation consumes credits.
6. Choose the correct upload surface:
   - Use REST Upload Files only as temporary staging for an AI endpoint.
   - Use the Magnific project UI for durable library storage when filenames and provenance matter.
   - Use live MCP creation-upload/finalize/move tools only after inspecting their current schemas.
7. Draft the exact request payload. If it can consume credits, create a paid download, or start an asynchronous job, state that clearly and obtain approval unless the user explicitly authorized execution in the current turn.
8. Execute only after authorization. Use `scripts/magnific_api.py` for JSON API calls or the exact documented upload/download flow when raw bytes or pre-signed URLs are involved.
9. Capture the task ID, poll the documented status endpoint with bounded backoff, or use a verified webhook for production integrations.
10. Verify the final remote state rather than inferring success from a closed form, upload panel, or temporary URL.
11. Return the connection/action used, task/result status, project membership, asset counts, failed items, duplicates, and any unresolved cost, expiry, or retention caveat.

## Browser-operation routing

Use the specialised skills above before interacting with a production surface. `magnific-assets-and-spaces` remains a compact legacy routing skill; prefer `magnific-library-and-projects` for filing and `magnific-spaces-and-flows` for graph work.

The official REST API and MCP documentation remain authoritative for endpoints and schemas. Do not use undocumented browser endpoints or try to bypass a UI, policy, approval, or credit gate.

## MCP, projects, agents, and durable uploads

- Treat `https://mcp.magnific.com` as the only official MCP endpoint. Authenticate with Magnific OAuth; do not invent a bearer token or reuse the REST API key.
- Prefer direct streamable HTTP configuration. On affected Codex macOS builds, use the verified `mcp-remote` fallback only when direct OAuth fails with the documented client-side discovery or issuer error. Re-test direct OAuth after Codex updates.
- Inspect live `tools/list`; it overrides remembered tool names and schemas.
- Before creating projects, call `folders_list` with `onlyProjects=true` and compare exact names. Magnific may include a default Personal project.
- Create a custom agent once, attach it only to the intended project, and verify its `Available in projects` field after saving. If visibility saving fails after the agent itself was created, retry Save; do not create a duplicate agent.
- Keep agent instructions source-grounded and project-specific. Include explicit approval gates for generation, editing, upscaling, animation, training, paid downloads, and publication.
- Treat REST `upload_url` and `asset_url` values as temporary secrets and REST uploads as staging. They are not proof of durable project storage.
- For durable UI uploads, use conservative batches, retry only failed rows, and isolate repeatedly failing files into single-file uploads.
- Always verify durable uploads through `creations_search` with `from=project-root`, paginate all results, and compare a filename multiset to the source manifest. Use `scripts/verify_project_uploads.mjs` for the standard check.

## Authentication

- Use `MAGNIFIC_API_KEY` from the environment.
- Use `MAGNIFIC_WEBHOOK_SIGNING_SECRET` only to verify incoming webhook signatures.
- The bundled helpers check the process environment first, then load only the requested variable from `/Users/vMac/.env`.
- Send it only in the `x-magnific-api-key` header to `https://api.magnific.com`.
- Never paste, print, commit, or log the key.
- Do not add or change credentials in `/Users/vMac/.env` without Vincent's explicit approval.
- If the key is absent, stop before execution and explain how to generate one from the Magnific dashboard.

## Safe request helper

The helper is dry-run by default:

```bash
python3 scripts/magnific_api.py POST /v1/ai/mystic \
  --data-file /absolute/path/to/payload.json
```

Execute only after the cost/action gate is satisfied:

```bash
python3 scripts/magnific_api.py POST /v1/ai/mystic \
  --data-file /absolute/path/to/payload.json \
  --execute
```

For read-only list or status calls, still pass `--execute`; this prevents accidental network activity during planning. Use `--output` for binary or large responses.

## Webhook verification

Preserve the raw body bytes and pass the three Magnific webhook headers exactly:

```bash
python3 scripts/verify_webhook.py \
  --id "$WEBHOOK_ID" \
  --timestamp "$WEBHOOK_TIMESTAMP" \
  --signature "$WEBHOOK_SIGNATURE" \
  --body-file /absolute/path/to/raw-body.bin
```

The verifier uses HMAC-SHA256, constant-time comparison, all versioned signatures in the header, and a five-minute timestamp tolerance. Persist processed `webhook-id` values in the receiving application and reject duplicates; signature verification alone does not provide durable replay protection.

## Selection guidance

- Prefer precision/faithful tools when preserving product geometry, logos, text, or identity matters.
- Prefer creative tools only when controlled reinterpretation is acceptable.
- Use the specific model endpoint requested by the user. When none is specified, compare the documented input constraints, output resolution, speed/quality modes, and credit impact before recommending one.
- Use webhooks for production-scale asynchronous workflows. Verify signatures from the raw request body exactly as documented.
- Use polling only for interactive or low-volume work. Bound retries, honor `429`, and use exponential backoff for transient `503` responses.
- Treat AI-classifier scores as confidence signals, not definitive proof.
- Treat REST Upload Files media as staging, not durable storage. Respect both upload URL expiry and file retention.
- Do not expose team-member emails or other analytics data beyond the user's requested scope.

## Reference routing

- `references/api-index.md`: generated list of documentation sections, source URLs, methods, and paths.
- `references/llms-full.txt`: verbatim official documentation snapshot supplied from `https://docs.magnific.com/llms-full.txt`.
- `references/platform-setup.md`: proven OAuth MCP, project, custom-agent, durable-upload, retry, and verification workflow.
- `scripts/search_docs.py`: ranked local documentation search; use this first.
- `scripts/sync_docs.py`: refresh the snapshot and index from the official source. Run only when current documentation is required and review the resulting diff.
- `scripts/magnific_api.py`: authenticated, dry-run-first JSON request helper.
- `scripts/verify_project_uploads.mjs`: read-only MCP comparison of one project against a local manifest; it never prints project references or creation identifiers.
- `scripts/verify_webhook.py`: verify versioned webhook signatures from the exact raw body.

When the snapshot and live official documentation disagree, prefer the live official documentation and refresh the snapshot before implementing.
