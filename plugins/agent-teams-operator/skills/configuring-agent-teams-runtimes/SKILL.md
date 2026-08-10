---
name: configuring-agent-teams-runtimes
description: Use when choosing Claude, Codex, OpenCode, or multimodel lanes; diagnosing missing binaries, auth, model availability, rate limits, or runtime-specific setup failures.
---

# Configuring Agent Teams Runtimes

Agent Teams orchestrates tasks; the runtime performs model work. Do not try to repair an unavailable binary, rejected model, or missing login with a better team prompt.

## Choose the first lane

| Situation | Start with |
| --- | --- |
| Existing Claude Code or Anthropic access | Claude |
| Codex-native workflow or OpenAI access | Codex |
| No signup/API key or broad provider routing | OpenCode free model first |
| Several models/providers | OpenCode, after one lane works |

Validate the selected path in the same environment that launches the desktop app:

```bash
command -v claude && claude --version
command -v codex && codex --version
command -v opencode && opencode --version
```

For account-backed paths, authenticate with the native CLI (`claude login` or `codex login`). For OpenCode provider routing, the provider block must match the model prefix—for example, `openrouter/moonshotai/kimi-k2.6` requires an `openrouter` configuration.

## Conservative multimodel pattern

| Role | Lane | Reason |
| --- | --- | --- |
| Lead | Most reliable configured provider | Coordination must remain dependable. |
| Builder | Suitable low-cost/fast lane | Work remains scoped and reviewable. |
| Reviewer | Separate careful lane | Reduces shared blind spots. |

Keep model IDs exact. Provider availability, account state, rate limits, tool behavior, and transcript evidence remain runtime responsibilities. Start one teammate/one model first; add lanes only after the launch and a tiny task work.

## Error Handling

Binary missing: repair installation or `PATH`. Terminal login works but app says unauthenticated: compare app and terminal home/config environments and inspect the auth diagnostic log. Model rejected: select a runtime-visible ID. Repeated 429: reduce concurrency or switch a lane. OpenCode `registered`/bootstrap-unconfirmed: use `troubleshooting-agent-teams`; do not assume the model ignored its prompt.
