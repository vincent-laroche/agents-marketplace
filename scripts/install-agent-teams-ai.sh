#!/usr/bin/env bash
set -euo pipefail

VERSION="2.7.0"
REPO="777genius/agent-teams-ai"
BASE_URL="https://github.com/${REPO}/releases/download/v${VERSION}"

if [[ "$(uname -s)" != "Darwin" ]]; then
  printf '%s\n' "This helper currently installs the macOS desktop build only." >&2
  printf '%s\n' "See https://github.com/${REPO}/releases/tag/v${VERSION} for Windows/Linux packages." >&2
  exit 1
fi

case "$(uname -m)" in
  arm64)
    ASSET="Agent.Teams.AI-${VERSION}-arm64.dmg"
    ;;
  x86_64)
    ASSET="Agent.Teams.AI-${VERSION}-x64.dmg"
    ;;
  *)
    printf 'Unsupported macOS architecture: %s\n' "$(uname -m)" >&2
    exit 1
    ;;
esac

DEST="${TMPDIR:-/tmp}/${ASSET}"
URL="${BASE_URL}/${ASSET}"

printf 'Downloading Agent Teams AI v%s from upstream...\n' "${VERSION}"
curl --fail --location --proto '=https' --tlsv1.2 --output "${DEST}" "${URL}"

printf '\nDownloaded installer:\n  %s\n' "${DEST}"
printf 'Opening disk image...\n'
open "${DEST}"
printf '\nDrag Agent Teams AI into Applications from the mounted disk image.\n'
printf 'The application will detect supported local Claude Code and Codex runtimes itself.\n'
