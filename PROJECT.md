# Project status

## Current state

`agents-marketplace` is the canonical Codex-native Hair Solutions Co. marketplace. Its source catalog is `.agents/plugins/marketplace.json`; plugin manifests are `.codex-plugin/plugin.json`; native subagents are direct `agents/*.toml` files.

Canonical local checkout: `/Users/vMac/.code/agents-marketplace`.

Current package surface: 15 plugins, 111 skills, 18 specialized subagents, and 2 MCP servers. The four subagent-bearing plugins are installed and enabled in the active Codex profile; `scripts/install-subagents.py` synchronizes their TOMLs into the profile registry used by `/agents` and `/subagents`.

## Session log

- 2026-08-18 — Codex: preserved the pre-cleanup dirty state in `stash@{0}`, fast-forwarded to `origin/main`, moved the canonical checkout to `/Users/vMac/.code/agents-marketplace`, removed multi-client and Claude-oriented packaging, removed copied brand assets and obsolete HubSpot email-module/Agent Teams bundles, added 18 valid native Codex subagents, rebuilt the catalog and docs, added deterministic marketplace and registry validation, removed stale local plugin registrations/hooks, installed the four subagent plugins, synchronized both Codex profiles, and verified all 18 role names in a fresh process. Next: restart existing Codex windows so `/agents` and `/subagents` refresh from the new registry.
