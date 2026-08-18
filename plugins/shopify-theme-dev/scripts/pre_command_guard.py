#!/usr/bin/env python3
"""PreToolUse(Bash) guard for the hairsolutions.co storefront.

The Shopify CLI theme commands are ALLOWED, including deploys. Vincent ruled
on this in two steps:

  2026-08-17 - `theme dev` / `theme serve` permitted: they render a local
               preview and publish nothing.
  2026-08-18 - `theme push` / `publish` / `pull` / `share` permitted too,
               with the live-theme consequence stated and accepted.

This guard previously blocked all of them, which silently overrode the
project's own permission set — plugin hooks run regardless of
.claude/settings.json — and made authorized commands unusable. Do not re-add
`dev`, `serve`, `push`, `publish` or `pull` here.

Note what `push` and `publish` now mean: `atelier-zero-storefront/main` is the
LIVE theme, so a CLI push writes straight to hairsolutions.co with no commit,
no diff and no GitHub record. Prefer the local repo -> GitHub path when the
change should be reviewable; use the CLI when speed matters more.

Still blocked, because neither is a deploy:
  - `theme delete`  destroys a theme irreversibly
  - `app deploy` / `app release` / `hydrogen deploy`  different product surface

`git push` used to be blocked here. Vincent retired that on 2026-08-18 along
with the whole edit/commit/push escalation: a request carries through to the
end of the work it names. Because a plugin hook overrides .claude/settings.json,
leaving it here made the project's own `allow` entry a dead letter -- push was
unreachable no matter what the repo said. Do not re-add it.

Exit 0 = allow. Exit 2 = block (stderr is shown to the model).
"""
import json, re, sys


def strip_literals(text):
    """Blank out quoted spans and heredoc bodies before scanning.

    A command that merely *mentions* a blocked command -- a commit message
    explaining why `theme delete` is denied, a grep for it, a doc being
    written -- is discussing it, not invoking it. Scanning the raw string
    blocks that, which is how a commit whose message named a blocked command
    got rejected on 2026-08-18.

    Only the heredoc *body* is blanked, never the tail, so a real command
    chained after the terminator is still seen.
    """
    m = re.search(r"<<-?\s*(['\"]?)(\w+)\1", text)
    if m:
        term = re.escape(m.group(2))
        text = re.sub(
            r"(<<-?\s*['\"]?" + term + r"['\"]?).*?^\s*" + term + r"\s*$",
            r"\1 ",
            text,
            flags=re.S | re.M,
        )
    return re.sub(r"'[^']*'|\"[^\"]*\"", " ", text)

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # never block on a parse error
    cmd = (data.get("tool_input") or {}).get("command", "") or ""
    low = strip_literals(cmd.lower())

    # Only match a real command invocation, never the same words appearing inside a
    # path or a quoted string. Without this, any command touching the directory
    # `06_storefront/Shopify Theme Dev/` -- including `ls` and `cat` -- was blocked,
    # because the path lowercases to "shopify theme dev".
    # Rejects a preceding word char, path separator, dot, dash, quote or
    # backtick. The backtick matters: a command that greps or writes markdown
    # prose mentioning `npm run push` or `shopify theme push` is discussing the
    # command, not invoking it, and blocking that makes the guard's own
    # documentation unmaintainable.
    CMD = r"(?<![\w/.\"'`\\-])"

    blocked = [
        # dev, serve, check, push, publish, pull and share are deliberately
        # absent: all are authorized. Only irreversible destruction remains.
        (CMD + r"shopify\s+theme\s+delete\b",
         "`shopify theme delete` destroys a theme irreversibly and is not a deploy. Ask Vincent explicitly if you need it."),
        (CMD + r"shopify\s+(app\s+(deploy|release)|hydrogen\s+deploy)\b",
         "App and Hydrogen deploys are a different product surface and are not authorized here."),
    ]
    for pat, msg in blocked:
        if re.search(pat, low):
            print(f"[storefront guard] Blocked: {msg}", file=sys.stderr)
            sys.exit(2)
    sys.exit(0)

if __name__ == "__main__":
    main()
