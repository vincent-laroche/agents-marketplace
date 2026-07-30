#!/usr/bin/env python3
"""Search the bundled Magnific llms-full documentation by section."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


DOCS_PATH = Path(__file__).resolve().parents[1] / "references" / "llms-full.txt"
HEADING_RE = re.compile(r"^# (.+)$")
ENDPOINT_RE = re.compile(
    r"^(get|post|put|patch|delete) (/\S+)$",
    re.IGNORECASE | re.MULTILINE,
)


@dataclass(frozen=True)
class Section:
    title: str
    start_line: int
    text: str

    @property
    def source(self) -> str:
        match = re.search(r"^Source: (https://\S+)$", self.text, re.MULTILINE)
        return match.group(1) if match else ""

    @property
    def endpoint(self) -> str:
        match = ENDPOINT_RE.search(self.text)
        return f"{match.group(1).upper()} {match.group(2)}" if match else ""


def parse_sections(text: str) -> list[Section]:
    lines = text.splitlines()
    starts = [index for index, line in enumerate(lines) if HEADING_RE.match(line)]
    sections: list[Section] = []
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        title = HEADING_RE.match(lines[start]).group(1)  # type: ignore[union-attr]
        sections.append(Section(title, start + 1, "\n".join(lines[start:end]).strip()))
    return sections


def score(section: Section, terms: list[str]) -> int:
    title = section.title.casefold()
    endpoint = section.endpoint.casefold()
    body = section.text.casefold()
    total = 0
    for term in terms:
        if term in title:
            total += 20
        if term in endpoint:
            total += 15
        total += min(body.count(term), 10)
    if all(term in body for term in terms):
        total += 25
    return total


def snippet(section: Section, terms: list[str], width: int = 280) -> str:
    flattened = re.sub(r"\s+", " ", section.text)
    lowered = flattened.casefold()
    positions = [lowered.find(term) for term in terms if lowered.find(term) >= 0]
    start = max(0, min(positions, default=0) - 80)
    end = min(len(flattened), start + width)
    prefix = "…" if start else ""
    suffix = "…" if end < len(flattened) else ""
    return prefix + flattened[start:end].strip() + suffix


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", help="Words or phrase to search for")
    parser.add_argument("--limit", type=int, default=8, help="Maximum matching sections")
    parser.add_argument("--show", action="store_true", help="Print matching section content")
    parser.add_argument("--max-chars", type=int, default=12000, help="Maximum characters per shown section")
    parser.add_argument("--list", action="store_true", help="List every top-level section")
    args = parser.parse_args()

    if not DOCS_PATH.is_file():
        parser.error(f"documentation snapshot is missing: {DOCS_PATH}")

    sections = parse_sections(DOCS_PATH.read_text(encoding="utf-8"))
    if args.list:
        for section in sections:
            suffix = f" — {section.endpoint}" if section.endpoint else ""
            print(f"{section.start_line}: {section.title}{suffix}")
        return 0

    if not args.query:
        parser.error("query is required unless --list is used")

    terms = [term.casefold() for term in re.findall(r"[\w./-]+", args.query) if term]
    ranked = sorted(
        ((score(section, terms), section) for section in sections),
        key=lambda item: (-item[0], item[1].start_line),
    )
    matches = [(value, section) for value, section in ranked if value > 0][: max(args.limit, 1)]
    if not matches:
        print("No matching documentation sections.")
        return 1

    for index, (value, section) in enumerate(matches, start=1):
        print(f"[{index}] {section.title} (line {section.start_line}, score {value})")
        if section.endpoint:
            print(f"    {section.endpoint}")
        if section.source:
            print(f"    {section.source}")
        if args.show:
            content = section.text[: args.max_chars]
            print(content)
            if len(section.text) > args.max_chars:
                print(f"… clipped {len(section.text) - args.max_chars} characters")
        else:
            print(f"    {snippet(section, terms)}")
        if index != len(matches):
            print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
