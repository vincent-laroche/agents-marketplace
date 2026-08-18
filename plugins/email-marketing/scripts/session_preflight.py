#!/usr/bin/env python3
"""Emit the Email Marketing session boundary without reading secrets."""

from pathlib import Path

PROJECT = Path("/Users/vMac/07_design/email")
ENV_FILE = Path("/Users/vMac/.env")


def main() -> None:
    print("Email Marketing plugin: MailerLite is the live marketing and lifecycle platform.")
    print(f"Project available: {'yes' if PROJECT.is_dir() else 'no'}")
    print(f"Master environment file available: {'yes' if ENV_FILE.is_file() else 'no'}")
    print("Start with email-marketing-preflight before any live MailerLite write.")
    print("Drafting is separate from test sends, scheduling, activation, import, DNS, and deletion.")


if __name__ == "__main__":
    main()
