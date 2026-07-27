# Compliance report contract

Use this format for every audit. Keep the report usable by an operator who must decide whether the artifact can ship.

## 1. Verdict

Start with:

```text
VERDICT: COMPLIANT | CONDITIONAL | NON-COMPLIANT
Scope: [artifact and channel]
Evidence inspected: [source, URL, rendered sizes, screenshots, copy, live facts]
Evidence missing: [none or exact missing items]
Findings: [blocker count] blocker · [major count] major · [minor count] minor
```

Do not soften the verdict with vague language.

## 2. Release blockers

List blockers first. If none, say `No release blockers found`.

For each finding use:

```text
[BLOCKER|MAJOR|MINOR]-[WEB|EMAIL|SOCIAL]-NN
Location: file:line, selector, module, slide/frame, or visible region
Observed: concrete evidence
Rule: exact canonical file and rule
Impact: customer, accessibility, trust, or operational consequence
Fix: smallest exact remediation
Recheck: evidence required to close the finding
```

Never report a generic concern without a locator and governing rule.

## 3. Compliance matrix

Use `PASS`, `FAIL`, `NOT VERIFIED`, or `N/A`.

| Category | Status | Evidence |
| --- | --- | --- |
| Canonical source verified |  |  |
| Logo provenance and handling |  |  |
| Font provenance and roles |  |  |
| Palette and Coral discipline |  |  |
| Contrast and legibility |  |  |
| Typography hierarchy |  |  |
| Spacing, layout, and surfaces |  |  |
| Components and interaction |  |  |
| Responsive/channel rendering |  |  |
| Accessibility |  |  |
| Imagery truth and consent |  |  |
| Voice and buyer dignity |  |  |
| Claims and changing facts |  |  |
| Platform-specific requirements |  |  |

Every `PASS` needs evidence. `NOT VERIFIED` must name what would resolve it.
Use `N/A` only when a rule does not apply to the classified artifact subtype, and state why.

## 4. Findings

Order by severity, then by customer impact. Merge repeated instances only when they share one cause and one remediation; list all affected locations.

## 5. Verified strengths

List only meaningful passes supported by evidence. Do not pad the report.

## 6. Remediation order

Give the shortest safe sequence:

1. blockers and trust/safety;
2. accessibility and core task;
3. systemic token/type/layout fixes;
4. local visual corrections;
5. release-only evidence checks.

## 7. Final release statement

End with one sentence:

- `Ship: the inspected artifact is compliant within the verified scope.`
- `Hold: complete the missing evidence and minor corrections before release.`
- `Block: resolve the listed blocker or major findings before release.`

An audit never authorizes publishing, sending, scheduling, deployment, or production mutation.
