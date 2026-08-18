#!/usr/bin/env python3
"""Run targeted, non-mutating validation after Email Marketing source edits."""

from __future__ import annotations

import json
import py_compile
import subprocess
import sys
from pathlib import Path


def context(message: str) -> None:
    print(json.dumps({"additionalContext": message}))


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return
    tool_input = payload.get("tool_input") or {}
    raw_path = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not raw_path:
        return
    path = Path(str(raw_path)).expanduser().resolve()
    project = Path("/Users/vMac/07_design/email")
    try:
        relative = path.relative_to(project)
    except ValueError:
        return
    if path.suffix.lower() == ".html" and path.is_file():
        validator = Path(__file__).with_name("validate_email.py")
        result = subprocess.run([sys.executable, str(validator), str(path)], capture_output=True, text=True, timeout=12, check=False)
        context(result.stdout.strip() or f"Email validation exited {result.returncode}")
    elif relative.parts and relative.parts[0] == "mailerlite" and path.suffix == ".py" and path.is_file():
        try:
            py_compile.compile(str(path), doraise=True)
            context(f"Python syntax check passed: {relative}")
        except py_compile.PyCompileError as error:
            context(f"Python syntax check failed: {error.msg}")


if __name__ == "__main__":
    main()
