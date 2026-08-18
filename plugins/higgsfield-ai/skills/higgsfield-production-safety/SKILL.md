---
name: higgsfield-production-safety
description: "Plan Higgsfield image, video, Canvas, Cinema Studio, Supercomputer, MCP, or CLI work without unapproved generation or external-state changes. Use before a Higgsfield generation, edit, upscale, batch, automation."
---

# Higgsfield production safety

Read `../../references/production-contract.md` before any action that can render, upload, share, or act outside Higgsfield.

## Live preflight

1. Establish the exact surface and project. A Canvas node, CLI call, MCP request, and Supercomputer workflow are distinct execution paths.
2. Resolve the concrete output: model, format, resolution, duration, audio, count, references, and destination.
3. Confirm that the current request authorizes that exact generation or transformation.
4. For connectors, scheduled tasks, uploads, sharing, or publishing, state the data flow and external effect first. Never treat a creative brief as approval to send, publish, or schedule.

## Approval record

Report: `surface → project → model → inputs → settings → count → destination → approval status`.

If the live UI conflicts with this skill or an older note, follow the UI and update the knowledge source after the task. Use `../higgsfield-mcp-cli` for official connection/setup work.
