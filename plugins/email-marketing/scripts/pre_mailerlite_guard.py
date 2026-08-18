#!/usr/bin/env python3
"""Ask before MailerLite MCP mutations and destructive actions."""

from __future__ import annotations

import json
import sys

READ_PREFIXES = ("get_", "list_", "search", "fetch", "select_", "discover_", "validate_", "suggest_", "dry_run_", "generate_email_content", "get_auth_status")


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return
    tool_name = str(payload.get("tool_name") or payload.get("tool") or "")
    if "mailerlite" not in tool_name.lower():
        return
    short = tool_name.rsplit("__", 1)[-1]
    if short.startswith(READ_PREFIXES):
        return
    tool_input = payload.get("tool_input") or {}
    action = str(tool_input.get("action") or "").lower()
    destructive = short.startswith("delete_") or action in {"delete", "forget"}
    reason = (
        "This MailerLite action is destructive. Confirm the exact resource and current-conversation approval."
        if destructive
        else "This MailerLite action changes external account state. Confirm the exact target and approved scope."
    )
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "ask", "permissionDecisionReason": reason}}))


if __name__ == "__main__":
    main()
