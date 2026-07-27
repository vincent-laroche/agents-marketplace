# Hair Solutions Co. — AI Toolkit

A vendor-neutral marketplace of **Hair Solutions Co.** plugins, skills, agents, commands, and MCP servers for Claude Code / Cowork, Codex, Cursor, Gemini CLI, and Google Antigravity. Plugin content is shared; thin client-specific manifests expose it to each supported agent.

- **Marketplace slug:** `hairsolutionsco`
- **Owner:** Vincent Laroche
- **Repo:** `vincent-laroche/hairsolutionsco-ai-toolkit`

## Install (Claude Code / Cowork)

**Cowork:** + → Plugins → **Add plugin** → **Add marketplace** → enter `vincent-laroche/hairsolutionsco-ai-toolkit` → **Sync**, then install any plugin from the list.

**Claude Code terminal:**

```shell
/plugin marketplace add vincent-laroche/hairsolutionsco-ai-toolkit
/plugin install shopify-theme-dev@hairsolutionsco
/reload-plugins
```

## Install (Codex)

```shell
codex plugin marketplace add vincent-laroche/hairsolutionsco-ai-toolkit
codex plugin add shopify-theme-dev@hairsolutionsco
```

Restart Codex after installing or updating a plugin.

## Install (Cursor)

Use **Install Plugin From Source** and enter:

```text
vincent-laroche/hairsolutionsco-ai-toolkit
```

Cursor reads `.cursor-plugin/marketplace.json` and each plugin's native
`.cursor-plugin/plugin.json`.

## Install (Gemini CLI)

Gemini CLI currently installs one extension root at a time. Clone this repository,
then install or link the required plugin directory:

```shell
git clone https://github.com/vincent-laroche/hairsolutionsco-ai-toolkit.git
gemini extensions install ./hairsolutionsco-ai-toolkit/plugins/chrome-devtools-mcp
```

Use `gemini extensions link <plugin-directory>` during local development.

## Install (Google Antigravity)

Clone this repository, then run the non-destructive installer for the required
toolkit:

```shell
# Preview all skill and MCP changes.
./scripts/install-antigravity-plugin.sh

# Install or update all marketplace plugins.
./scripts/install-antigravity-plugin.sh --apply
```

The installer namespaces duplicate skill names, adopts identical existing
skills, preserves local modifications, backs up Antigravity's MCP configuration
before writing, and reports same-name MCP conflicts without exposing config
values.

## Plugins in this marketplace

| Plugin | What it does |
|--------|--------------|
| **shopify-theme-dev** | Designer-in-Chief / Creative Director / Liquid toolkit for the hairsolutions.co storefront — brand system, OS 2.0 sections, Cloudinary AssetLink media, Notion change-tracker, ship-to-`main` workflow. |
| **shopify-liquid-designer** | Liquid/theme design + frontend skills for the Hair Solutions storefront. |
| **shopify-design** | Shopify design skills. |
| **shopify-developer** | Shopify developer skills. |
| **ai-video** | AI video generation workflow skills. |
| **analytics-ads** | Analytics + paid-ads skills. |
| **marketing-content** | Marketing content creation skills. |
| **business-integrations** | Business/SaaS integration skills. |
| **chrome-devtools-mcp** | Official Chrome DevTools MCP server plus browser debugging, accessibility, performance, memory, and troubleshooting skills. |
| **hubspot** | HubSpot CMS / CRM skills. |
| **atelier-zero-design-system** | Atelier Zero v7 brand application plus a strict web, email, and social compliance agent. |

Each plugin lives under `plugins/<name>/` with shared `skills/`, `commands/`,
`agents/`, hooks, scripts, and references. Client-specific manifests live
alongside the shared content:

- Claude: `.claude-plugin/plugin.json`
- Codex: `.codex-plugin/plugin.json`
- Cursor: `.cursor-plugin/plugin.json`
- Gemini CLI: `gemini-extension.json`

Root marketplace catalogs:

- Claude: `.claude-plugin/marketplace.json`
- Codex: `.agents/plugins/marketplace.json`
- Cursor: `.cursor-plugin/marketplace.json`

## Structure

```
hairsolutionsco-ai-toolkit/
├── Brand/
│   ├── design-system/
│   │   ├── master/
│   │   └── reference/
│   └── logos/
│       ├── current/
│       └── archive/
├── .claude-plugin/
│   └── marketplace.json
├── .agents/plugins/
│   └── marketplace.json
├── .cursor-plugin/
│   └── marketplace.json
├── plugins/
│   └── <plugin>/               ← one folder per plugin
│       ├── .claude-plugin/plugin.json
│       ├── .codex-plugin/plugin.json
│       ├── .cursor-plugin/plugin.json
│       ├── gemini-extension.json
│       ├── skills/  commands/  agents/  hooks/ ...
├── scripts/
│   ├── sync-client-manifests.py
│   └── install-antigravity-plugin.sh
└── README.md
```

## Adding a new plugin later

1. Add the plugin under `plugins/<name>/` with a canonical `.claude-plugin/plugin.json`.
2. Add it to `.claude-plugin/marketplace.json`.
3. Run `python3 scripts/sync-client-manifests.py`.
4. Validate each client surface, commit, and push.
