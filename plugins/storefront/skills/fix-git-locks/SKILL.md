---
name: fix-git-locks
description: Clear stale .git/*.lock files left by the FUSE sandbox so git can proceed in the hairsolutions.co repo. Use only when git reports index.lock/HEAD.lock or "another git process" errors. Never auto-runs.
---

# Fix git locks

The bash sandbox runs over a FUSE mount that cannot `unlink()`, so git lock files (`.git/index.lock`, `.git/HEAD.lock`, `.git/refs/**/*.lock`) get orphaned and block every later git command.

## Fix (Desktop Commander only)
1. Confirm no real git process is running: `mcp__Desktop_Commander__list_processes` → look for `git`.
2. In `/Users/vMac/06_storefront/shopify_github_synched_theme_files`, remove stale locks:
   ```
   find .git -name '*.lock' -print
   find .git -name '*.lock' -delete
   ```
   Run via `mcp__Desktop_Commander__start_process` (native, no FUSE).
3. Re-run `git status` to confirm git is healthy.

## Rules
- Only delete `*.lock` under `.git/`. Never touch tracked files.
- If a real git process IS running, wait for it — do not delete its lock.
- This is separate from releasing; it does not commit or push.
