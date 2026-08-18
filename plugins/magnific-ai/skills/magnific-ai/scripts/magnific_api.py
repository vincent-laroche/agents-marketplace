#!/usr/bin/env python3
"""Dry-run-first JSON client for the Magnific API."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from env_utils import load_named_secret


BASE_URL = "https://api.magnific.com"
ALLOWED_METHODS = ("GET", "POST", "PUT", "PATCH", "DELETE")


def compact(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: compact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [compact(item) for item in value]
    if isinstance(value, str) and len(value) > 160:
        return f"{value[:80]}…[{len(value)} chars]…{value[-40:]}"
    return value


def load_payload(data: str | None, data_file: str | None) -> Any | None:
    if data and data_file:
        raise ValueError("use either --data or --data-file, not both")
    if data_file:
        return json.loads(Path(data_file).read_text(encoding="utf-8"))
    if data:
        return json.loads(data)
    return None


def build_url(path: str, query_items: list[str]) -> str:
    if not path.startswith("/") or path.startswith("//"):
        raise ValueError("path must start with one slash")
    query: list[tuple[str, str]] = []
    for item in query_items:
        if "=" not in item:
            raise ValueError(f"query must be KEY=VALUE: {item}")
        query.append(tuple(item.split("=", 1)))  # type: ignore[arg-type]
    suffix = f"?{urllib.parse.urlencode(query)}" if query else ""
    return f"{BASE_URL}{path}{suffix}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("method", choices=ALLOWED_METHODS)
    parser.add_argument("path", help="API path beginning with /v1/")
    parser.add_argument("--query", action="append", default=[], metavar="KEY=VALUE")
    parser.add_argument("--data", help="Inline JSON request body")
    parser.add_argument("--data-file", help="Path to a JSON request body")
    parser.add_argument("--output", help="Write the response body to this file")
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--execute", action="store_true", help="Perform the request")
    args = parser.parse_args()

    try:
        payload = load_payload(args.data, args.data_file)
        url = build_url(args.path, args.query)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))

    if not args.execute:
        print("DRY RUN — no network request sent")
        print(f"{args.method} {url}")
        if payload is not None:
            print(json.dumps(compact(payload), indent=2, ensure_ascii=False))
        print("Add --execute only after the action/cost gate is satisfied.")
        return 0

    api_key = load_named_secret("MAGNIFIC_API_KEY")
    if not api_key:
        print("MAGNIFIC_API_KEY is not set in the environment or /Users/vMac/.env.", file=sys.stderr)
        return 2

    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {
        "Accept": "application/json",
        "x-magnific-api-key": api_key,
        "User-Agent": "agents-marketplace/magnific-ai",
    }
    if body is not None:
        headers["Content-Type"] = "application/json"

    request = urllib.request.Request(url, data=body, headers=headers, method=args.method)
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            response_body = response.read()
            content_type = response.headers.get("Content-Type", "")
            status = response.status
    except urllib.error.HTTPError as error:
        response_body = error.read()
        print(f"Magnific API returned HTTP {error.code}.", file=sys.stderr)
        try:
            print(json.dumps(json.loads(response_body), indent=2, ensure_ascii=False), file=sys.stderr)
        except (UnicodeDecodeError, json.JSONDecodeError):
            print(response_body[:2000].decode("utf-8", errors="replace"), file=sys.stderr)
        return 1
    except urllib.error.URLError as error:
        print(f"Magnific API request failed: {error.reason}", file=sys.stderr)
        return 1

    print(f"HTTP {status}")
    if args.output:
        output_path = Path(args.output)
        output_path.write_bytes(response_body)
        print(f"Wrote {len(response_body)} bytes to {output_path}")
        return 0

    if "json" in content_type.casefold():
        try:
            print(json.dumps(json.loads(response_body), indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print(response_body.decode("utf-8", errors="replace"))
        return 0

    if len(response_body) > 2000:
        print("Response is non-JSON and too large for stdout; rerun with --output.", file=sys.stderr)
        return 3
    print(response_body.decode("utf-8", errors="replace"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
