# Magnific Platform Setup

Use this workflow for MCP connection, project creation, custom agents, durable project uploads, and final account verification. Re-check the live official documentation and current client behavior before relying on version-specific workarounds.

## Contents

- Connect the official MCP server and recover from affected Codex OAuth failures.
- Inventory projects without creating duplicates.
- Create project-exclusive custom agents and recover from partial saves.
- Choose between REST staging, live MCP creation uploads, and durable project UI storage.
- Upload in bounded batches with targeted retries.
- Verify complete filename multisets, counts, failures, and duplicates.
- Preserve the no-credits and no-secrets safety boundary.

## 1. Connect the official MCP server

The official endpoint is:

```text
https://mcp.magnific.com
```

Magnific MCP uses streamable HTTP and OAuth 2.0. It does not use `MAGNIFIC_API_KEY`. The first connection opens a browser sign-in, and the OAuth session should persist.

For a current Codex CLI whose `mcp add --help` exposes `--url`, try the direct configuration first:

```bash
codex mcp add magnific --url https://mcp.magnific.com
```

Do not copy another client's CLI syntax blindly. For example, `--transport http` from other client documentation was not accepted by Codex CLI `0.144.0`.

### Codex macOS OAuth fallback

As of 2026-07-26, affected Codex `0.144.x` macOS builds can discover the server and open OAuth but then fail with either:

- `No authorization support detected`
- `Authorization server response missing required issuer`

[OpenAI Codex issue #34684](https://github.com/openai/codex/issues/34684) tracks the macOS OAuth/discovery and RFC 9207 issuer-callback defects. If direct OAuth produces one of those errors:

```bash
codex mcp remove magnific
codex mcp add magnific -- npx -y mcp-remote https://mcp.magnific.com
```

This still connects to Magnific's official endpoint and completes Magnific OAuth; `mcp-remote` only bridges Codex stdio to the remote streamable HTTP server.

Do not use the fallback preemptively on unaffected clients. After a Codex upgrade, test the direct `--url` configuration again.

Verify the saved configuration without exposing OAuth data:

```bash
codex mcp get magnific
```

Then verify a real connection by initializing the server and inspecting live `tools/list`, or by calling a read-only tool such as `folders_list`. A configuration entry alone is not connection proof. Reconnect once more to confirm that OAuth persisted.

Never print authorization codes, callback URLs, tokens, signed URLs, or OAuth storage.

## 2. Inventory projects before creating anything

Call live MCP `folders_list` with:

```json
{"onlyProjects": true}
```

Compare exact project names and counts before creating shells. Magnific commonly includes a default Personal project; do not treat it as a duplicate of a named work project.

After any creation:

1. Re-list projects.
2. Confirm each intended name appears exactly once.
3. Record only names and counts in user-facing evidence unless internal references were explicitly requested.

## 3. Create and assign custom agents

The verified UI path is:

1. Open a project.
2. Open **AI Assistant**.
3. Open **Select agent**.
4. Choose **New agent**.
5. Fill Name, Description, and Instructions.
6. Under **Available in projects**, choose **Add project**.
7. Select exactly the matching project.
8. Create the agent.

Observed UI limits on 2026-07-26 were:

- Name: 120 characters.
- Description: 240 characters.
- Instructions: 20,000 characters.

Treat these as observed UI values, not permanent API guarantees.

Each instruction set should define:

- one project-specific role;
- the live source files or repositories that control decisions;
- domain/platform rules;
- truth, safety, privacy, and publication boundaries;
- a requirement to inspect exact references before acting;
- explicit current-turn approval before any credit-consuming generation, enhancement, training, animation, upscale, flow, or paid download;
- a review checklist for the returned work.

### Agent save recovery

Magnific can save the agent record but fail while updating project visibility, showing:

`Agent saved, but updating who can see it failed. Try saving again.`

When that happens:

1. Do not click New agent again.
2. Retry **Save** in the existing edit form.
3. Wait for the form to close.
4. Open Settings → Agents and confirm the agent appears once.
5. Edit it and verify **Available in projects** contains exactly the intended project and no others.

Final verification must prove both agent existence and assignment. The global agent list alone does not prove project exclusivity.

## 4. Choose the correct upload surface

### REST Upload Files is staging

`POST /v1/ai/uploads/request-url` returns a short-lived signed `upload_url` and a readable `asset_url`. Official documentation says:

- the signed upload URL is short-lived;
- the asset URL is typically valid for about one day;
- the file is generally eligible for deletion after about seven days.

Use this REST flow only to feed local media into an AI endpoint. Do not claim it is durable project storage.

### MCP creation uploads

Live MCP may expose `creations_request_upload`, an upload/finalize step, `creations_finalize_upload`, `creations_move`, and/or `projects_move`. Inspect current `tools/list` because names and schemas can evolve.

The durable pattern is:

1. Request an upload target.
2. PUT bytes without logging the signed URL.
3. Finalize the temporary path into a Magnific creation.
4. Move the creation into the intended project.
5. Search that project and verify the result.

If the current finalize schema has no original filename or metadata fields and provenance matters, use the project UI instead. Do not invent unsupported metadata fields.

### Durable project UI

The verified UI path is:

1. Open the exact project.
2. Choose **Add** → **Upload files**.
3. Select only manifest-approved absolute paths.
4. Keep the upload panel open until it reaches a terminal state.

The project UI preserves filenames in the creation prompt/name and is the preferred route when filename-based manifest verification is required.

## 5. Upload reliably

- Start with batches of 10–20 files.
- A multi-file selection being accepted only means the queue received the files.
- Wait for the queue to finish.
- Use **Retry failed** for transient batch failures.
- If one or more files continue failing under concurrency, close the terminal queue and upload only those failed files individually.
- Never resubmit a whole batch when only some rows failed.
- Do not infer success solely because the upload panel closed. A retry can appear complete without the project count changing.
- Before retrying an apparently missing file, query the project by its expected filename to avoid creating a duplicate.

For Chrome extension browser control, file upload requires **Allow access to file URLs** in the extension's Details page. If that permission is not enabled, use the Codex in-app browser when it can authenticate to the same Magnific account, or ask the user to enable the permission. Do not change extension permissions silently.

## 6. Verify counts, membership, failures, and duplicates

For each project:

1. Call `creations_search` with `from=project-root` and the project reference.
2. Request up to 50 items per page.
3. Follow pagination through the last page.
4. Compare the complete filename multiset to the approved manifest.
5. Report:
   - manifest count;
   - Magnific total;
   - fetched count;
   - missing filenames;
   - unexpected filenames;
   - duplicate filename counts.

Magnific removes only the final extension from the displayed upload prompt. For a local filename such as `asset.webp.webp`, compare it to `asset.webp`.

Use the bundled verifier after OAuth is working:

```bash
node scripts/verify_project_uploads.mjs \
  --project-name "Product Photos" \
  --manifest /absolute/path/to/manifest.json
```

The default manifest shape is:

```json
{
  "assets": [
    {"local_path": "/absolute/path/to/file.jpg"}
  ]
}
```

Override `--assets-key` or `--path-field` when the manifest uses different field names.

The verifier uses only read-only MCP tools, retries transient search errors, and prints no project references, creation identifiers, signed URLs, or OAuth data. A successful result requires:

- manifest count equals Magnific total and fetched count;
- `missing`, `unexpected`, and `duplicateNames` are empty.

Verify custom agents separately through the UI because the current live MCP tool list may not expose agent management.

## 7. Safety boundary

- Uploading and organizing source assets is distinct from generation.
- Do not invoke generation, enhancement, upscale, animation, training, flow, or paid-download tools during setup.
- Inspect `account_balance` and use `simulate_cost` before a paid operation.
- Obtain explicit current-turn approval for the exact credit-consuming action.
- Never edit credentials merely to make OAuth work.
- Never expose signed URLs, OAuth tokens, API keys, or callback data.
