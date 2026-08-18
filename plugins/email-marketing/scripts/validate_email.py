#!/usr/bin/env python3
"""Validate MailerLite-ready HTML without network access."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path


class EmailParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.images: list[dict[str, str | None]] = []
        self.links: list[str] = []
        self.text: list[str] = []
        self.has_table = False
        self.has_script = False
        self.ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "img":
            self.images.append(values)
        elif tag == "a" and values.get("href"):
            self.links.append(str(values["href"]))
        elif tag == "table":
            self.has_table = True
        elif tag == "script":
            self.has_script = True
            self.ignored_depth += 1
        elif tag in {"style", "title"}:
            self.ignored_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "title"} and self.ignored_depth:
            self.ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.ignored_depth and data.strip():
            self.text.append(data.strip())


def validate(path: Path) -> tuple[list[str], list[str]]:
    html = path.read_text(encoding="utf-8")
    lower = html.lower()
    parser = EmailParser()
    parser.feed(html)
    errors: list[str] = []
    warnings: list[str] = []
    if "<html" not in lower or "</html>" not in lower:
        errors.append("missing complete html document")
    if 'lang="' not in lower and "lang='" not in lower:
        warnings.append("html language is not declared")
    if not parser.has_table:
        errors.append("no email-safe table structure found")
    if parser.has_script:
        errors.append("script elements are not email safe")
    if not any(token in html for token in ("{$unsubscribe}", "{$unsubscribe_url}", "unsubscribe_url")):
        errors.append("missing MailerLite unsubscribe token")
    if re.search(r"\{\{[^{}]+\}\}", html):
        errors.append("non-MailerLite double-brace merge token remains")
    if len(html.encode("utf-8")) > 100 * 1024:
        warnings.append("HTML exceeds 100 KB and risks Gmail clipping")
    if not re.search(r"display\s*:\s*none|max-height\s*:\s*0", lower):
        warnings.append("hidden preheader pattern not detected")
    if not parser.links:
        errors.append("no links found")
    for index, image in enumerate(parser.images, start=1):
        if image.get("alt") is None:
            errors.append(f"image {index} has no alt attribute")
        if not image.get("width"):
            warnings.append(f"image {index} has no explicit width")
    visible_text = " ".join(parser.text)
    if "!" in visible_text:
        warnings.append("visible copy contains an exclamation mark; verify brand voice")
    if re.search(r"\b(wig|toupee)\b", visible_text, re.IGNORECASE):
        errors.append("visible copy uses a prohibited product term")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.paths:
        if not path.is_file():
            print(f"FAIL {path}: file not found")
            failed = True
            continue
        errors, warnings = validate(path)
        state = "FAIL" if errors else "PASS"
        print(f"{state} {path} ({len(errors)} errors, {len(warnings)} warnings)")
        for item in errors:
            print(f"  error: {item}")
        for item in warnings:
            print(f"  warning: {item}")
        failed = failed or bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
