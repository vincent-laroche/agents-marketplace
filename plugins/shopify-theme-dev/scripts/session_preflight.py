#!/usr/bin/env python3
"""SessionStart slim preflight for the hairsolutions.co storefront.

Prints a single compact status line (repo, branch, tree, main<->origin,
Dev-behind) so a session starts oriented. Read-only, defensive, fast.
Never blocks (always exits 0).
"""
import os, subprocess, sys

REPO = "/Users/vMac/06_storefront/shopify_github_synched_theme_files"

def git(*args):
    return subprocess.run(["git", "-C", REPO, *args],
                          capture_output=True, text=True, timeout=4).stdout.strip()

def main():
    if not os.path.isdir(os.path.join(REPO, ".git")):
        sys.exit(0)
    try:
        branch = git("rev-parse", "--abbrev-ref", "HEAD") or "?"
        dirty = git("status", "--porcelain")
        tree = "clean" if not dirty else f"{len(dirty.splitlines())} changed"
        ahead_behind = ""
        try:
            git("fetch", "--quiet", "origin")
            ab = git("rev-list", "--left-right", "--count", "HEAD...origin/main")
            if ab:
                a, b = ab.split()
                ahead_behind = f", {branch} {a}↑/{b}↓ vs origin/main"
            devb = git("rev-list", "--count", "origin/dev..origin/main")
            if devb and devb.isdigit() and int(devb) > 0:
                ahead_behind += f", dev {devb} behind main (sync-dev should fast-forward)"
        except Exception:
            pass
        print(f"[storefront] repo OK · branch {branch} · {tree}{ahead_behind} · theme CLI allowed incl. push/publish — main is LIVE")
    except Exception:
        pass
    sys.exit(0)

if __name__ == "__main__":
    main()
