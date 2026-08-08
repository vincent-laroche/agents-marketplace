#!/usr/bin/env python3
"""PreToolUse(Bash) guard for the hairsolutions.co storefront.

Blocks Shopify CLI deploys and the theme dev server. The deploy path is
strictly: local repo -> GitHub (main/Dev). Git itself runs through Desktop
Commander, not Bash, so raw `git push` in Bash is also blocked with a hint.

Exit 0 = allow. Exit 2 = block (stderr is shown to the model).
"""
import json, re, sys

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # never block on a parse error
    cmd = (data.get("tool_input") or {}).get("command", "") or ""
    low = cmd.lower()

    # Only match a real command invocation, never the same words appearing inside a
    # path or a quoted string. Without this, any command touching the directory
    # `06_storefront/Shopify Theme Dev/` -- including `ls` and `cat` -- was blocked,
    # because the path lowercases to "shopify theme dev".
    # Rejects a preceding word char, path separator, dot, dash or quote.
    CMD = r"(?<![\w/.\"'\\-])"

    blocked = [
        (CMD + r"shopify\s+theme\s+(dev|push|publish|delete|pull|serve)\b",
         "Shopify CLI theme deploy/dev is forbidden. Use the local repo -> GitHub workflow (storefront-release)."),
        (CMD + r"shopify\s+theme\b[^;&|]*--(live|allow-live)\b",
         "No CLI publishing to the live theme. Push to GitHub main instead."),
        (CMD + r"npm\s+run\s+(dev|push|deploy|start)\b",
         "No theme dev server / npm deploy. Local repo -> GitHub only."),
        (CMD + r"git\s+push\b",
         "Run git through Desktop Commander, not the Bash sandbox (FUSE breaks git locks). Use storefront-release."),
    ]
    for pat, msg in blocked:
        if re.search(pat, low):
            print(f"[storefront guard] Blocked: {msg}", file=sys.stderr)
            sys.exit(2)
    sys.exit(0)

if __name__ == "__main__":
    main()
