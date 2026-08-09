# Agent Teams AI

Third-party agent orchestration application maintained by `777genius/agent-teams-ai`.
It is **not** a Hair Solutions Co. plugin and is not registered in the Claude/Codex/Cursor marketplace catalogs.

## Purpose

Agent Teams AI provides a desktop control plane for multi-agent teams using Claude Code, Codex, OpenCode, Cursor, and other supported runtimes. It can create teams with differentiated roles, coordinate work across agents, track tasks and reviews, and expose usage/budget information.

## Upstream

- Repository: `https://github.com/777genius/agent-teams-ai`
- License: GNU AGPL-3.0
- Pinned upstream commit: `5f462d2db7a93bcb69c4ddedf4e6e42ca83b4c98`
- Upstream release referenced at integration time: `v2.7.0`
- Added to this toolkit: 2026-08-09

No upstream source code is vendored here. This directory contains only Hair Solutions Co. integration metadata and helper scripts so the upstream project remains clearly separated and can be updated without local forks or accidental relicensing.

## Install

From the toolkit root:

```bash
./scripts/install-agent-teams-ai.sh
```

The script detects macOS architecture and downloads the matching upstream release installer. It does not alter Claude Code, Codex, or toolkit configuration.

## Update policy

1. Review the upstream release and changelog.
2. Update the pinned release/commit in this README and the installer script.
3. Verify the download URL against the upstream GitHub release.
4. Do not modify upstream code in this directory. If Hair Solutions Co. ever needs a maintained fork, create a separate repository and document that fork here.
