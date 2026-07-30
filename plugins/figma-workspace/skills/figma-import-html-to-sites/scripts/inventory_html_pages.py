#!/usr/bin/env python3
"""Inventory individual HTML pages before importing them into Figma."""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


BOARD_MARKERS = ("review-board", "review_board", "dashboard", "contact-sheet")
ASSET_ATTRS = {"src", "href", "poster"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_title = False
        self.title_parts: list[str] = []
        self.asset_refs: list[str] = []
        self.body_data_page: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "title":
            self.in_title = True
        if tag.lower() == "body":
            self.body_data_page = next(
                (value for key, value in attrs if key.lower() == "data-page" and value),
                None,
            )
        for key, value in attrs:
            if key.lower() in ASSET_ATTRS and value:
                self.asset_refs.append(value.strip())

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data.strip())

    @property
    def title(self) -> str:
        return " ".join(part for part in self.title_parts if part).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inventory local HTML pages and flag Figma import risks."
    )
    parser.add_argument("root", type=Path, help="Directory containing HTML files")
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    return parser.parse_args()


def humanize(stem: str) -> str:
    return re.sub(r"[-_]+", " ", stem).strip().title()


def infer_kind(path: Path) -> str:
    lowered = str(path).lower()
    if any(marker in lowered for marker in BOARD_MARKERS):
        return "board"
    if "wireframe" in lowered:
        return "wireframe"
    if "/full" in lowered or "full-design" in lowered:
        return "full-design"
    return "unknown"


def local_asset_status(html_path: Path, ref: str) -> tuple[str, str] | None:
    if not ref or ref.startswith(("#", "data:", "mailto:", "tel:", "javascript:")):
        return None
    parsed = urlparse(ref)
    if parsed.scheme in {"http", "https"} or ref.startswith("//"):
        return ("remote", ref)
    if parsed.scheme == "file" or Path(unquote(parsed.path)).is_absolute():
        return ("absolute-local", ref)
    clean = unquote(parsed.path)
    if not clean:
        return None
    target = (html_path.parent / clean).resolve()
    return ("local-ok" if target.exists() else "missing-local", ref)


def inspect_page(path: Path, root: Path) -> dict[str, object]:
    relative = path.relative_to(root)
    is_mobile = bool(relative.parts) and relative.parts[0].lower() == "mobile"
    route_relative = Path(*relative.parts[1:]) if is_mobile else relative
    text = path.read_text(encoding="utf-8", errors="replace")
    parser = PageParser()
    parser.feed(text)
    statuses = [status for ref in parser.asset_refs if (status := local_asset_status(path, ref))]
    counts: dict[str, int] = {}
    samples: dict[str, list[str]] = {}
    for status, ref in statuses:
        counts[status] = counts.get(status, 0) + 1
        samples.setdefault(status, [])
        if len(samples[status]) < 5:
            samples[status].append(ref)
    kind = infer_kind(path)
    route_key = parser.body_data_page or str(route_relative.with_suffix(""))
    return {
        "relative_path": str(relative),
        "absolute_path": str(path),
        "proposed_name": parser.title or humanize(path.stem),
        "route_key": route_key,
        "variant": "mobile" if is_mobile else "desktop",
        "body_data_page": parser.body_data_page,
        "has_figma_capture_script": any(
            "mcp.figma.com/mcp/html-to-design/capture.js" in ref for ref in parser.asset_refs
        ),
        "kind": kind,
        "import_as_page": kind != "board",
        "bytes": path.stat().st_size,
        "asset_reference_counts": counts,
        "asset_reference_samples": samples,
    }


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")
    files = sorted(root.rglob("*.html"))
    pages = [inspect_page(path, root) for path in files]
    route_map: dict[str, dict[str, list[dict[str, object]]]] = {}
    for page in pages:
        variants = route_map.setdefault(str(page["route_key"]), {})
        variants.setdefault(str(page["variant"]), []).append(page)

    def choose_candidate(candidates: list[dict[str, object]]) -> dict[str, object] | None:
        if not candidates:
            return None
        return max(
            candidates,
            key=lambda page: (
                bool(page["has_figma_capture_script"]),
                Path(str(page["relative_path"])).stem == str(page["route_key"]),
                Path(str(page["relative_path"])).stem != "index",
            ),
        )

    routes = []
    for key, variants in sorted(route_map.items()):
        desktop_candidates = variants.get("desktop", [])
        mobile_candidates = variants.get("mobile", [])
        desktop = choose_candidate(desktop_candidates)
        mobile = choose_candidate(mobile_candidates)
        selected = {
            str(page["relative_path"])
            for page in (desktop, mobile)
            if page is not None
        }
        aliases = [
            str(page["relative_path"])
            for page in desktop_candidates + mobile_candidates
            if str(page["relative_path"]) not in selected
        ]
        routes.append(
            {
                "route_key": key,
                "desktop": str(desktop["relative_path"]) if desktop else None,
                "mobile": str(mobile["relative_path"]) if mobile else None,
                "aliases_not_separate_webpages": aliases,
                "complete_pair": desktop is not None and mobile is not None,
            }
        )
    payload = {
        "root": str(root),
        "summary": {
            "html_files": len(pages),
            "importable_html_files": sum(bool(page["import_as_page"]) for page in pages),
            "route_groups": len(routes),
            "complete_desktop_mobile_pairs": sum(route["complete_pair"] for route in routes),
            "alias_html_files": sum(len(route["aliases_not_separate_webpages"]) for route in routes),
            "selected_route_html_files": sum(
                int(route["desktop"] is not None) + int(route["mobile"] is not None)
                for route in routes
            ),
            "desktop_files": sum(page["variant"] == "desktop" for page in pages),
            "mobile_files": sum(page["variant"] == "mobile" for page in pages),
            "figma_capture_enabled_files": sum(
                bool(page["has_figma_capture_script"]) for page in pages
            ),
            "board_files": sum(page["kind"] == "board" for page in pages),
            "pages_with_missing_local_assets": sum(
                page["asset_reference_counts"].get("missing-local", 0) > 0 for page in pages
            ),
            "pages_with_absolute_local_assets": sum(
                page["asset_reference_counts"].get("absolute-local", 0) > 0 for page in pages
            ),
        },
        "routes": routes,
        "pages": pages,
    }
    rendered = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.expanduser().write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
