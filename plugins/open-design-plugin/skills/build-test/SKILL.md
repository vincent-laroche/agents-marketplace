---
name: build-test
description: "Verify a completed change set using the repository's declared build, typecheck, lint, and test commands, with bounded logs and an honest result record. Use before handoff, release review."
---

# Verify the Build

## Procedure

1. Confirm the target repository and inspect its documented scripts, CI configuration, and current working-tree state.
2. Select the smallest relevant declared checks: typecheck/build, lint, unit/integration tests, and any requested visual or browser validation.
3. Run checks only after the intended change set is complete; retain failure output with sensitive values redacted.
4. Record commands, exit outcomes, duration, skipped checks and reasons, plus failures linked to affected files where possible.
5. Do not edit test expectations, suppress failures, or claim coverage that was not executed.

## Output

Report `passing`, `failing`, or `skipped` for every selected check. Treat a skipped check as non-passing until its reason and risk are accepted. Never deploy or publish as a side effect of verification.
