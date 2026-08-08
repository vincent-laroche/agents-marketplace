---
name: clone-audit
description: Audit an imported, cloned, or reimplemented website for fidelity gaps, source-brand and language residue, placeholders, trackers, risky links, and external dependencies. Use before handoff or deployment of a site influenced by a reference. Prefer static inspection; do not execute untrusted code, install packages, or make network requests without approval.
---

# Audit a Reimplemented Website

## Establish scope

1. Confirm the target root, intended output locale, known source/reference materials, and explicit exclusions.
2. Inventory HTML, CSS, scripts, assets, metadata, dependencies, and configuration.
3. Mark visual fidelity as unverified when reference evidence is missing; never guess.

## Check categories

Inspect and retain evidence for:

1. Fidelity assets/styles: substituted fonts or imagery, broken paths, and material layout/color drift.
2. Tracking: analytics, pixels, tag managers, telemetry, and unexpected third-party scripts.
3. Source-brand residue: names, domains, metadata, social links, comments, asset paths, and copy.
4. Language residue outside the required locale, excluding legitimate identifiers and names.
5. TODOs, template copy, dummy links, test credentials, and unfinished states.
6. External dependencies: remote assets, CDNs, development endpoints, fonts, media, and packages that create availability, privacy, or licensing risk.

## Report

For each finding, include severity (`blocker`, `high`, `medium`, `low`), repository-relative `file:line`, evidence, impact, and a concrete remediation. Keep `confirmed finding`, `checked; none found`, and `not checked/unverifiable` distinct.

Conclude with `ready`, `ready with follow-ups`, or `not ready`, and never deploy or delete content as part of the audit.
