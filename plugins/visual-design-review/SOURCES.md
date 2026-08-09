# Sources and adaptation notes

This plugin contains first-party portable adaptations of five public design-review workflows. The adaptations keep the useful review methods while removing runtime-specific dependencies and narrowing the skills to reusable visual/design judgment.

## 1. visual-polish-review

Upstream inspiration: Jezweb `design-review`

- Repository: `jezweb/claude-skills`
- Path: `plugins/frontend/skills/design-review/SKILL.md`
- Purpose retained: visual polish review separated from broad UX auditing; layout, spacing, typography, color, hierarchy, consistency, interaction states, and responsive quality.
- Adaptation: removed Claude-Code-only/browser-specific assumptions and artifact-path requirements.

## 2. designer-eye-review

Upstream inspiration: gstack `design-review`

- Repository: `garrytan/gstack`
- Path: `design-review/SKILL.md`
- Purpose retained: designer-eye QA, prioritized concrete fixes, visual inconsistency detection, and generic/AI-looking design detection.
- Adaptation: removed gstack preamble, telemetry, local binaries, execution scaffolding, and commit automation. This is a portable critique workflow, not a vendored gstack runtime.

## 3. frontend-craft-review

Upstream inspiration: Microsoft `frontend-design-review`

- Repository: `microsoft/skills`
- Path: `.github/skills/frontend-design-review/SKILL.md`
- Purpose retained: distinctive frontend craft, design-system compliance, typography, palette, composition, motion, responsive behavior, and anti-generic-design guidance.
- Adaptation: simplified to a portable review skill without assuming Storybook or Figma tools are always available.

## 4. product-design-audit

Upstream inspiration: OpenAI Product Design `audit`

- Repository: `openai/role-specific-plugins`
- Path: `plugins/product-design/skills/audit/SKILL.md`
- Purpose retained: evidence-first product-flow critique tied to actual screenshots/screens, with explicit limits on accessibility claims.
- Adaptation: removed dependencies on the surrounding Product Design plugin router, browser-selection skills, local preflight scripts, and Figma board-generation workflow.

## 5. design-fidelity-qa

Upstream inspiration: OpenAI Product Design `design-qa`

- Repository: `openai/role-specific-plugins`
- Path: `plugins/product-design/skills/design-qa/SKILL.md`
- Purpose retained: source-vs-rendered comparison, required fidelity surfaces, severity levels, and evidence-based fix lists.
- Adaptation: removed internal Product Design build dependencies and retained the portable visual comparison methodology.

## Why this is not a verbatim vendor bundle

The toolkit's `AGENTS.md` separates third-party `vendor/` content from first-party portable workflows. These files are therefore written as original adaptations with source attribution instead of copying upstream runtime-specific skill files into `vendor/` and pretending their dependencies exist here.

The previously discussed fifth source, an OpenAI `frontend-skill` path, could not be verified in the current `openai/skills` repository. `design-qa` is used instead because it is current, verifiable, and directly relevant to visual fidelity review.
