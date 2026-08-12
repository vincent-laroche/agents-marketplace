#!/usr/bin/env python3
"""Run the canonical Atelier Zero repository's read-only integrity verifier."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


BRAND = Path("/Users/vMac/08_brand/brand-design-system")
VERIFY = BRAND / "scripts" / "verify-brand-system.mjs"
SKILL_ROOT = Path(__file__).resolve().parents[1]
COMPLIANCE_SKILL = SKILL_ROOT.parent / "atelier-zero-brand-compliance" / "SKILL.md"

VISUAL_AUTHORITIES = (
    BRAND / "brand-design-system.html",
    BRAND / "tokens" / "tokens.json",
    BRAND / "tokens" / "tokens.css",
    BRAND / "styles" / "atelier-zero.css",
    BRAND / "specs" / "COMPONENT_CONTRACTS.md",
    BRAND / "specs" / "COMPOSITION_RULES.md",
    BRAND / "specs" / "DECISION_TREES.md",
    BRAND / "specs" / "PLATFORM_SHOPIFY.md",
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify the live Atelier Zero v7 master, authority, assets, tokens, and repository shape."
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    required = (
        BRAND / "PROJECT.md",
        BRAND / "AGENTS.md",
        BRAND / "DESIGN.md",
        BRAND / "SKILL.md",
        *VISUAL_AUTHORITIES,
        BRAND / "manifests" / "logos.json",
        BRAND / "manifests" / "fonts.json",
        SKILL_ROOT / "SKILL.md",
        COMPLIANCE_SKILL,
        VERIFY,
    )
    missing = [str(path) for path in required if not path.is_file()]

    if missing:
        result = {
            "status": "fail",
            "canonical_repository": str(BRAND),
            "missing_sources": missing,
        }
        if args.json:
            print(json.dumps(result, indent=2, sort_keys=True))
        else:
            print("FAIL: Atelier Zero canonical sources are missing.")
            for path in missing:
                print(f"Missing: {path}")
        return 1

    marker_failures = []
    marker_sources = {
        SKILL_ROOT / "SKILL.md": (
            "Atelier Zero v7",
            "$atelier-zero-brand-compliance",
            "brand-design-system.html",
            "tokens/tokens.json",
            "styles/atelier-zero.css",
            "specs/PLATFORM_SHOPIFY.md",
            "/Users/vMac/06_design/brand/logos/masterfile-approved",
        ),
        COMPLIANCE_SKILL: (
            "NOT VERIFIED",
            "COMPLIANT",
            "CONDITIONAL",
            "NON-COMPLIANT",
            "references/web-audit.md",
            "references/email-audit.md",
            "references/social-audit.md",
        ),
    }
    for path, markers in marker_sources.items():
        text = path.read_text(encoding="utf-8")
        marker_failures.extend(
            f"{path}: missing marker {marker}" for marker in markers if marker not in text
        )

    if marker_failures:
        result = {
            "status": "fail",
            "canonical_repository": str(BRAND),
            "skill_drift": marker_failures,
        }
        if args.json:
            print(json.dumps(result, indent=2, sort_keys=True))
        else:
            print("FAIL: Atelier Zero packaged skill contract drifted.")
            for failure in marker_failures:
                print(failure)
        return 1

    process = subprocess.run(
        ["node", str(VERIFY)],
        cwd=BRAND,
        capture_output=True,
        text=True,
        check=False,
    )
    result = {
        "status": "pass" if process.returncode == 0 else "fail",
        "canonical_repository": str(BRAND),
        "visual_authorities": [str(path) for path in VISUAL_AUTHORITIES],
        "verifier": str(VERIFY),
        "output": process.stdout.strip(),
        "error": process.stderr.strip(),
    }

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        if process.stdout:
            print(process.stdout.rstrip())
        if process.stderr:
            print(process.stderr.rstrip())

    return process.returncode


if __name__ == "__main__":
    raise SystemExit(main())
