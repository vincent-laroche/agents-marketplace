# vendor/

Third-party plugins bundled into this toolkit for convenience. **Nothing here was
written by Hair Solutions Co.** — everything in `../plugins/` was.

Separated 2026-08-08. Previously these sat alongside first-party work in `plugins/`,
which made two questions unanswerable at a glance: *did I write this?* and *what
licence governs it?*

| Directory | Author | Licence | Registered in the catalog? |
|---|---|---|---|
| `chrome-devtools-mcp/` | Chrome DevTools Team | Apache-2.0 | **Yes** — `./vendor/chrome-devtools-mcp` |
| `mcpmarket-me/` | MCPmarket | MIT | No |
| `glassmorphism/` | typeui.sh | (unstated) | No — has no `plugin.json`; it is a bare skill directory, not a loadable plugin |

## Rules

- **Do not edit these in place.** Local edits are silently lost on the next upstream
  update and make it impossible to tell your changes from theirs. If you need
  different behaviour, fork it into `../plugins/` under a new name and own it.
- Their licences are theirs. Do not relicense, and do not assume the `Proprietary`
  licence used by first-party plugins applies to anything in here.
- To register one in the catalog, add an entry to `../.claude-plugin/marketplace.json`
  with a `./vendor/<name>` source path, then run `../scripts/sync-client-manifests.py`.

## Notes on the unregistered two

**`mcpmarket-me`** is unregistered deliberately. Its `.mcp.json` (gitignored, local
only) holds an MCPmarket bearer token. An earlier version of that file was committed
in plaintext while this repo was public; it was purged from history on 2026-08-08, but
**the token value itself still needs rotating at mcpmarket.com** — a history rewrite
does not reach clones, forks, or caches made during the exposure window. Do not
register this plugin until a fresh token is in place.

**`glassmorphism`** has no `plugin.json`, so the marketplace cannot load it as a
plugin even if registered. It is a `SKILL.md` plus 27 component reference files. Either
give it a manifest or treat it as reference material. Note it is *not* the same content
as `~/.claude/skills/glassmorphism`, which is a different, smaller typeui.sh export.
