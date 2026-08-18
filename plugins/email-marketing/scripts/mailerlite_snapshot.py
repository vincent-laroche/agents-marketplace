#!/usr/bin/env python3
"""Return a read-only, non-PII MailerLite account fingerprint."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

BASE = "https://connect.mailerlite.com/api"
DEFAULT_EXPECTED_ACCOUNT = "2582639"


def get_json(token: str, path: str) -> tuple[int, dict]:
    request = urllib.request.Request(
        BASE + path,
        method="GET",
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status, json.loads(response.read() or b"{}")
    except urllib.error.HTTPError as error:
        try:
            payload = json.loads(error.read() or b"{}")
        except json.JSONDecodeError:
            payload = {}
        return error.code, payload


def resource_count(token: str, path: str) -> dict:
    status, payload = get_json(token, path)
    if status >= 300:
        return {"available": False, "status": status}
    data = payload.get("data", [])
    total = payload.get("total")
    if total is None:
        total = (payload.get("meta") or {}).get("total")
    if total is None:
        total = len(data)
    return {"available": True, "count": total, "data": data}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--expected-account",
        default=os.environ.get("MAILERLITE_ACCOUNT_ID", DEFAULT_EXPECTED_ACCOUNT),
        help="Fail if the live account differs from this ID",
    )
    parser.add_argument("--compact", action="store_true", help="Emit one-line JSON")
    args = parser.parse_args()

    token = os.environ.get("MAILERLITE_API_TOKEN")
    if not token:
        print("MAILERLITE_API_TOKEN is not set", file=sys.stderr)
        return 2

    campaigns = resource_count(token, "/campaigns?limit=100")
    if not campaigns.get("available"):
        print(f"MailerLite campaign read failed with HTTP {campaigns.get('status')}", file=sys.stderr)
        return 3

    account_ids = sorted(
        {str(item.get("account_id")) for item in campaigns.get("data", []) if item.get("account_id")}
    )
    account_id = account_ids[0] if len(account_ids) == 1 else None
    if not account_id:
        print(f"Could not resolve one account ID from campaign data: {account_ids}", file=sys.stderr)
        return 4
    if args.expected_account and account_id != str(args.expected_account):
        print(
            f"Account mismatch: expected {args.expected_account}, received {account_id}",
            file=sys.stderr,
        )
        return 5

    groups = resource_count(token, "/groups?limit=100")
    fields = resource_count(token, "/fields?limit=100")
    segments = resource_count(token, "/segments?limit=100")
    automations = resource_count(token, "/automations?limit=100")
    subscribers = resource_count(token, "/subscribers?limit=0")

    campaign_states: dict[str, int] = {}
    for campaign in campaigns.get("data", []):
        state = str(campaign.get("status") or "unknown")
        campaign_states[state] = campaign_states.get(state, 0) + 1

    automation_data = automations.get("data", []) if automations.get("available") else []
    summary = {
        "account_id": account_id,
        "verified_expected_account": True,
        "campaigns": {"count": campaigns.get("count"), "states": campaign_states},
        "groups": {"available": groups.get("available"), "count": groups.get("count")},
        "fields": {"available": fields.get("available"), "count": fields.get("count")},
        "segments": {"available": segments.get("available"), "count": segments.get("count")},
        "automations": {
            "available": automations.get("available"),
            "count": automations.get("count"),
            "enabled": sum(1 for item in automation_data if item.get("enabled") is True),
            "disabled": sum(1 for item in automation_data if item.get("enabled") is False),
        },
        "subscribers": {
            "available": subscribers.get("available"),
            "count": subscribers.get("count"),
        },
    }
    print(json.dumps(summary, indent=None if args.compact else 2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
