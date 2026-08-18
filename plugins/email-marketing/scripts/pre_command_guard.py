#!/usr/bin/env python3
"""Block secret exposure and ad-hoc MailerLite mutations in shell commands."""

from __future__ import annotations

import json
import re
import sys


def decision(kind: str, reason: str) -> None:
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": kind, "permissionDecisionReason": reason}}))


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return
    command = str((payload.get("tool_input") or {}).get("command") or "")
    lower = command.lower()
    if not command:
        return
    secret_reader = re.search(r"\b(cat|head|tail|less|more|strings|xxd|od|printenv|env)\b", lower)
    secret_target = re.search(r"(/users/vmac/)?\.env(?:\s|$)|mailer(?:lite)?_api_token", lower)
    if secret_reader and secret_target:
        decision("deny", "Blocked secret exposure. Load /Users/vMac/.env without printing values.")
        return
    if "connect.mailerlite.com/api" in lower:
        mutating = bool(
            re.search(r"(?:\s|^)(?:-x|--request)\s*(?!get\b)\w+", lower)
            or re.search(r"(?:--data|-d\s|--form|-f\s|--upload-file|-t\s)", lower)
        )
        if mutating:
            decision("deny", "Blocked ad-hoc MailerLite mutation. Use the OAuth MCP or a bounded reviewed adapter.")
            return
    if re.search(r"(?:^|[;&|]\s*)mailerlite\s+", lower):
        mutating_words = (" create ", " update ", " delete ", " schedule ", " cancel ", " upsert ", " assign ", " unassign ", " import ", " forget ", " enable ", " disable ")
        padded = f" {lower} "
        if any(word in padded for word in mutating_words):
            decision("ask", "This MailerLite CLI command changes external state. Confirm the exact resource and action.")


if __name__ == "__main__":
    main()
