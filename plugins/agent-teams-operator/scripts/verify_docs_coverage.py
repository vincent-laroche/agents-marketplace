#!/usr/bin/env python3
"""Validate that the Agent Teams plugin keeps full published-doc coverage."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
COVERAGE_PATH = ROOT / "assets" / "docs-coverage.json"
REQUIRED_SKILLS = {
    "onboarding-agent-teams",
    "configuring-agent-teams-runtimes",
    "designing-agent-teams-teams",
    "writing-agent-teams-briefs",
    "operating-agent-teams-tasks",
    "reviewing-agent-teams-changes",
    "coordinating-agent-teams-worktrees",
    "integrating-agent-teams-mcp",
    "troubleshooting-agent-teams",
    "protecting-agent-teams-data",
    "developing-agent-teams",
}
REQUIRED_PAGES = {
    "index.md",
    "developers/index.md",
    "guide/agent-workflow.md",
    "guide/beginner-workflow.md",
    "guide/code-review.md",
    "guide/create-first-team.md",
    "guide/create-team.md",
    "guide/git-worktree-strategy.md",
    "guide/installation.md",
    "guide/mcp-integration.md",
    "guide/quickstart.md",
    "guide/review-and-approve.md",
    "guide/run-and-monitor-work.md",
    "guide/runtime-setup.md",
    "guide/team-brief-examples.md",
    "guide/troubleshooting.md",
    "reference/concepts.md",
    "reference/contributor-architecture.md",
    "reference/faq.md",
    "reference/privacy-local-data.md",
    "reference/providers-runtimes.md",
    "reference/release-notes.md",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


if not COVERAGE_PATH.is_file():
    fail("missing assets/docs-coverage.json")

coverage = json.loads(COVERAGE_PATH.read_text())
pages = {entry["path"] for entry in coverage.get("pages", [])}
if pages != REQUIRED_PAGES:
    missing = sorted(REQUIRED_PAGES - pages)
    unexpected = sorted(pages - REQUIRED_PAGES)
    fail(f"page coverage mismatch; missing={missing}; unexpected={unexpected}")

for skill_name in REQUIRED_SKILLS:
    skill_path = ROOT / "skills" / skill_name / "SKILL.md"
    if not skill_path.is_file():
        fail(f"missing {skill_path.relative_to(ROOT)}")
    text = skill_path.read_text()
    if not text.startswith("---\nname: "):
        fail(f"invalid frontmatter in {skill_path.relative_to(ROOT)}")
    if "description: Use when" not in text:
        fail(f"missing discovery description in {skill_path.relative_to(ROOT)}")
    if "## Error Handling" not in text:
        fail(f"missing Error Handling in {skill_path.relative_to(ROOT)}")

print(f"PASS: 22 canonical documentation pages mapped across {len(REQUIRED_SKILLS)} skills")
