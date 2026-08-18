# Hair Solutions Co. Agents Marketplace

A Codex-native marketplace of production skills, specialized subagents, MCP servers, and deterministic tools for Hair Solutions Co.

- Marketplace: `agents-marketplace`
- Repository: `vincent-laroche/agents-marketplace`
- Runtime: Codex

## Install

```shell
codex plugin marketplace add vincent-laroche/agents-marketplace
```

The subagent-bearing plugins are marked installed by default. A local CLI marketplace add may still require these explicit installs:

```shell
codex plugin add email-marketing@agents-marketplace
codex plugin add storefront@agents-marketplace
codex plugin add figma-workspace@agents-marketplace
codex plugin add visual-design-review@agents-marketplace
```

Codex 0.147 does not consistently register every plugin-bundled TOML in `/agents` and `/subagents`. Synchronize the marketplace roles into the active profile after installation:

```shell
python3 /Users/vMac/.code/agents-marketplace/scripts/install-subagents.py --apply
```

The tool adopts an existing same-name role, installs missing roles with namespaced filenames, and refuses ambiguous duplicates. Use `--check` to verify the registry later.

Restart Codex after synchronization. All 18 native roles then appear in `/agents` and `/subagents`.

## Packages

| Plugin | Capabilities |
|---|---|
| `email-marketing` | 13 MailerLite skills, 8 specialized subagents, official OAuth MCP, HTML validator, read-only account snapshot |
| `storefront` | Shopify storefront skills and 8 scoped architecture, implementation, review, evidence, brand, mobile, and SEO subagents |
| `figma-workspace` | Hair Solutions Figma workflow plus the Figma Shopify operator subagent |
| `visual-design-review` | Five visual QA skills plus a read-only finish-gate subagent |
| `chrome-devtools-mcp` | Chrome DevTools MCP and browser debugging skills |
| `figma-for-developers` | Figma Plugin API, REST API, integration, and web-capture skills |
| `higgsfield-ai` | Image, video, audio, identity, continuity, model selection, and production skills |
| `magnific-ai` | Magnific image, video, audio, Spaces, Flows, Designer, Library, and safety skills |
| `hubspot` | CRM model, operations, developer integration, and UI procedure skills |
| `ai-video` | HeyGen, Video-Cog, and Mux workflows |
| `analytics-ads` | GA4, GTM, and Google Ads workflows |
| `business-integrations` | SaaS integration workflows |
| `marketing-content` | Content, SEO, paid, social, and email-sequence skills |
| `open-design-plugin` | Design extraction, token mapping, critique, review, and verification skills |
| `seo-tools` | Google Search Console operations and local CLI tool |

## Native structure

```text
.agents/plugins/marketplace.json
plugins/<plugin>/
  .codex-plugin/plugin.json
  skills/<skill>/SKILL.md
  agents/<role>.toml
  .mcp.json
  scripts/
vendor/<plugin>/
scripts/validate-marketplace.py
scripts/install-subagents.py
```

Only components that exist are present in a plugin. This repository intentionally contains no compatibility manifests or copied brand library.

## Validate

```shell
python3 scripts/validate-marketplace.py
```

The validator checks catalog parity, Codex manifests, repository URLs, skill frontmatter, subagent TOML schema, MCP configuration, and banned non-Codex packaging surfaces.
