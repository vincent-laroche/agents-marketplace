#!/usr/bin/env python3
"""Refresh the bundled Magnific documentation and generated API index."""

from __future__ import annotations

import hashlib
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


SOURCE_URL = "https://docs.magnific.com/llms-full.txt"
SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCE_DIR = SKILL_ROOT / "references"
DOCS_PATH = REFERENCE_DIR / "llms-full.txt"
INDEX_PATH = REFERENCE_DIR / "api-index.md"
HEADING_RE = re.compile(r"^# (.+)$")
SOURCE_RE = re.compile(r"^Source: (https://\S+)$")
ENDPOINT_RE = re.compile(r"^(get|post|put|patch|delete) (/\S+)$", re.IGNORECASE)


def build_index(text: str, digest: str, fetched_at: str) -> str:
    lines = text.splitlines()
    starts = [index for index, line in enumerate(lines) if HEADING_RE.match(line)]
    rows = []
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        section = lines[start:end]
        title = HEADING_RE.match(section[0]).group(1)  # type: ignore[union-attr]
        source = next((m.group(1) for line in section if (m := SOURCE_RE.match(line))), "")
        endpoint_match = next((m for line in section if (m := ENDPOINT_RE.match(line))), None)
        endpoint = (
            f"`{endpoint_match.group(1).upper()} {endpoint_match.group(2)}`"
            if endpoint_match
            else ""
        )
        escaped_title = title.replace("|", "\\|")
        source_link = f"[docs]({source})" if source else ""
        rows.append(f"| {start + 1} | {escaped_title} | {endpoint} | {source_link} |")

    return "\n".join(
        [
            "# Magnific API documentation index",
            "",
            f"- Source: [{SOURCE_URL}]({SOURCE_URL})",
            f"- Fetched: `{fetched_at}`",
            f"- SHA-256: `{digest}`",
            f"- Sections: `{len(rows)}`",
            "",
            "Use `../scripts/search_docs.py` for ranked full-text search.",
            "",
            "| Line | Section | Endpoint | Official page |",
            "|---:|---|---|---|",
            *rows,
            "",
        ]
    )


def main() -> int:
    request = urllib.request.Request(
        SOURCE_URL,
        headers={"User-Agent": "hairsolutionsco-ai-toolkit/magnific-ai-doc-sync"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = response.read()

    text = payload.decode("utf-8")
    required_markers = ("# Authentication", "# Quickstart", "# Upload files", "# Webhooks")
    missing = [marker for marker in required_markers if marker not in text]
    if missing:
        raise RuntimeError(f"download failed validation; missing: {', '.join(missing)}")

    REFERENCE_DIR.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(payload).hexdigest()
    fetched_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    DOCS_PATH.write_bytes(payload)
    INDEX_PATH.write_text(build_index(text, digest, fetched_at), encoding="utf-8")
    print(f"Updated {DOCS_PATH} ({len(payload)} bytes, sha256 {digest})")
    print(f"Updated {INDEX_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
