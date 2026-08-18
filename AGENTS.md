# hairsolutionsco-ai-toolkit — Agent Instructions

The Hair Solutions Co. plugin marketplace: agents, skills, and commands for Claude
Code, Cursor, Codex, and Gemini. This repository **is** the `hairsolutionsco`
marketplace — it is the source that `~/.claude/plugins/marketplaces/hairsolutionsco`
clones from.

Written 2026-08-08; the repo previously had only a `README.md`.

## What this is

15 first-party plugins in `plugins/` carrying roughly 100 skills that encode the
operating knowledge of the business — the storefront, HubSpot, brand system, email
modules, and the AI production stack. Plus 3 third-party plugins in `vendor/`.

Repository: `https://github.com/vincent-laroche/hairsolutionsco-ai-toolkit`

## The one rule that will bite you: the catalog is generated

`.claude-plugin/marketplace.json` is the **single source of truth**. These are all
generated from it by `scripts/sync-client-manifests.py` and must never be hand-edited:

- `.cursor-plugin/marketplace.json`
- `.agents/plugins/marketplace.json` (Codex)
- every plugin's `.cursor-plugin/plugin.json`, `.codex-plugin/plugin.json`, `gemini-extension.json`

After changing the catalog or adding a plugin:

```bash
python3 scripts/sync-client-manifests.py
```

The script fails loudly if a plugin's `plugin.json` name disagrees with its catalog
entry. That check is deliberate — let it fail rather than working around it.

## Layout

| Path | Contents |
|---|---|
| `plugins/` | **First-party.** Written here, owned here, `Proprietary` or `MIT`. |
| `vendor/` | **Third-party.** Not ours. See `vendor/README.md` before touching. |
| `.claude-plugin/marketplace.json` | The catalog — source of truth |
| `scripts/sync-client-manifests.py` | Regenerates every other manifest |

Each plugin: `.claude-plugin/plugin.json` (hand-written), `skills/<name>/SKILL.md`,
optionally `hooks/hooks.json`, `.mcp.json`, `agents/`, `commands/`.

## Adding a plugin

1. Create `plugins/<name>/.claude-plugin/plugin.json` with `name`, `description`,
   `version`, `author`, `license`.
2. Add skills as `plugins/<name>/skills/<skill>/SKILL.md`, each with YAML frontmatter
   carrying `name` and a `description` that states **when to trigger**, not just what
   it does — the description is the routing signal.
3. Register it in `.claude-plugin/marketplace.json`.
4. Run the sync script.
5. Commit. The weekly `agent-config-audit` asserts `plugins/` and the catalog agree.

## Hard rules

- **Never commit a credential.** `.mcp.json` files holding real tokens are gitignored;
  commit a `.mcp.example.json` using `${ENV_VAR}` instead. This repo leaked a live
  bearer token in plaintext on 2026-08-08 while public (the plugin that held it,
  `vendor/mcpmarket-me`, was removed the same day). History was rewritten, but that
  only prevents future clones from seeing it. Assume anything ever committed here is
  public forever.
- **Never edit `vendor/` in place.** Fork into `plugins/` under a new name instead.
- **Never hand-edit a generated manifest.** Change the catalog, run the sync script.
- **Never edit the marketplace cache** at `~/.claude/plugins/marketplaces/hairsolutionsco`.
  It is a throwaway clone. Edits there are silently reverted on refresh and do not
  reach this repo. Fix it here, commit, push, then refresh the cache.

## The copy problem — read this before debugging plugin behaviour

Claude Code loads the **cache**, not this repo. A change here does not take effect until
it is committed, pushed, and the cache refreshed. Conversely a change made in the cache
appears to work and then vanishes.

On 2026-08-08 a one-line bugfix in `shopify-theme-dev/scripts/pre_command_guard.py` had
to be applied in five separate locations before it took effect, and existed in no git
history at all until it was committed. If plugin behaviour disagrees with the source
you are reading, you are almost certainly looking at a stale copy.

## Related

- `~/.claude/PROJECT-CONFIG-STANDARD.md` — the machine-wide agent-config standard
- `~/08_brand/brand-design-system/` — the only brand authority; `atelier-zero-design-system` reads it by pointer and must never copy token values in
- `~/.claude/audits/latest.txt` — weekly audit, includes this repo's manifest-drift check
