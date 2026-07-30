#!/usr/bin/env python3
"""Verify a Magnific webhook signature against the exact raw request body."""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import hmac
import sys
import time
from pathlib import Path

from env_utils import load_named_secret


def parse_signatures(header: str) -> list[tuple[str, str]]:
    signatures: list[tuple[str, str]] = []
    for item in header.split():
        version, separator, signature = item.partition(",")
        if not separator or not version or not signature:
            raise ValueError("webhook-signature must contain space-delimited version,signature pairs")
        signatures.append((version, signature))
    if not signatures:
        raise ValueError("webhook-signature is empty")
    return signatures


def verify(
    *,
    secret: str,
    webhook_id: str,
    timestamp: str,
    raw_body: bytes,
    signature_header: str,
    tolerance_seconds: int,
    now: int,
) -> tuple[bool, str | None]:
    try:
        timestamp_value = int(timestamp)
    except ValueError as error:
        raise ValueError("webhook-timestamp must be Unix seconds") from error

    if tolerance_seconds >= 0 and abs(now - timestamp_value) > tolerance_seconds:
        raise ValueError(
            f"webhook timestamp is outside the {tolerance_seconds}-second tolerance"
        )

    signed_content = (
        webhook_id.encode("utf-8")
        + b"."
        + timestamp.encode("utf-8")
        + b"."
        + raw_body
    )
    expected = base64.b64encode(
        hmac.new(secret.encode("utf-8"), signed_content, hashlib.sha256).digest()
    ).decode("ascii")

    for version, supplied in parse_signatures(signature_header):
        try:
            base64.b64decode(supplied, validate=True)
        except (binascii.Error, ValueError):
            continue
        if hmac.compare_digest(expected, supplied):
            return True, version
    return False, None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True, help="webhook-id header")
    parser.add_argument("--timestamp", required=True, help="webhook-timestamp header")
    parser.add_argument("--signature", required=True, help="webhook-signature header")
    parser.add_argument("--body-file", required=True, help="file containing the exact raw body bytes")
    parser.add_argument(
        "--tolerance-seconds",
        type=int,
        default=300,
        help="maximum timestamp age/skew; set -1 to disable",
    )
    parser.add_argument("--now", type=int, default=None, help=argparse.SUPPRESS)
    args = parser.parse_args()

    secret = load_named_secret("MAGNIFIC_WEBHOOK_SIGNING_SECRET")
    if not secret:
        print(
            "MAGNIFIC_WEBHOOK_SIGNING_SECRET is not set in the environment or /Users/vMac/.env.",
            file=sys.stderr,
        )
        return 2

    try:
        raw_body = Path(args.body_file).read_bytes()
        valid, matched_version = verify(
            secret=secret,
            webhook_id=args.id,
            timestamp=args.timestamp,
            raw_body=raw_body,
            signature_header=args.signature,
            tolerance_seconds=args.tolerance_seconds,
            now=args.now if args.now is not None else int(time.time()),
        )
    except (OSError, ValueError) as error:
        print(f"Webhook verification failed: {error}", file=sys.stderr)
        return 2

    if not valid:
        print("Webhook signature is invalid.", file=sys.stderr)
        return 1
    print(f"Webhook signature is valid ({matched_version}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
