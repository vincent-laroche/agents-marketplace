---
name: critique-theater
description: Run a bounded, evidence-based design review using design, brand, accessibility, and copy perspectives, then produce a ranked fix list and explicit ship decision. Use before handoff or release of a visual artifact, page, email, or interface. Do not score without inspecting the current artifact and its governing source of truth.
---

# Run a Design Jury

## Review setup

1. Confirm the artifact, its intended audience, its governing brand/design system, target breakpoints, and release context.
2. Inspect the current artifact before judging it. Use rendered evidence and source evidence together.
3. Review through five fixed lenses: design hierarchy, brand fidelity, accessibility, copy/content integrity, and implementation/interaction quality.
4. Score each lens from 0–10, list concrete evidence, and write only actionable must-fix items.

## Bounded convergence

- Run at most three rounds unless the user expands scope.
- A ship recommendation requires the agreed threshold and no open blocker/high must-fix item.
- Never use a numerical composite to hide unresolved accessibility, brand, or customer-trust failures.

## Output

Provide: current-round scores, evidence, must-fix items ranked by severity, checked-without-findings, limitations, and one of `ship`, `ship with follow-ups`, or `do not ship`. Do not publish, deploy, or edit production state merely because the review passes.
