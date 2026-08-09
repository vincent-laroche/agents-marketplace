# vendor/

Third-party plugins bundled into this toolkit for convenience. **Nothing here was
written by Hair Solutions Co.** — everything in `../plugins/` was.

Separated 2026-08-08. Previously these sat alongside first-party work in `plugins/`,
which made two questions unanswerable at a glance: *did I write this?* and *what
licence governs it?*

| Directory | Author | Licence | Registered in the catalog? |
|---|---|---|---|
| `chrome-devtools-mcp/` | Chrome DevTools Team | Apache-2.0 | **Yes** — `./vendor/chrome-devtools-mcp` |
| `glassmorphism/` | typeui.sh | (unstated) | No — has no `plugin.json`; it is a bare skill directory, not a loadable plugin |

## Rules

- **Do not edit these in place.** Local edits are silently lost on the next upstream
  update and make it impossible to tell your changes from theirs. If you need
  different behaviour, fork it into `../plugins/` under a new name and own it.
- Their licences are theirs. Do not relicense, and do not assume the `Proprietary`
  licence used by first-party plugins applies to anything in here.
- To register one in the catalog, add an entry to `../.claude-plugin/marketplace.json`
  with a `./vendor/<name>` source path, then run `../scripts/sync-client-manifests.py`.

## Removed: mcpmarket-me (2026-08-08)

Its `.mcp.json` held an MCPmarket bearer token, and an earlier version of that file was
committed in plaintext while this repo was public — purged from history the same day.
No longer used, so the plugin was deleted outright rather than left unregistered. If
MCPmarket integration is ever wanted again, treat it as a fresh install, not a restore —
review its old `.claude-plugin/plugin.json` and `hooks/hooks.json` from git history
first (`git log --all -- vendor/mcpmarket-me`) rather than trusting the deleted config.

**`glassmorphism`** has no `plugin.json`, so the marketplace cannot load it as a
plugin even if registered. It is a `SKILL.md` plus 27 component reference files. Either
give it a manifest or treat it as reference material. Note it is *not* the same content
as `~/.claude/skills/glassmorphism`, which is a different, smaller typeui.sh export.
