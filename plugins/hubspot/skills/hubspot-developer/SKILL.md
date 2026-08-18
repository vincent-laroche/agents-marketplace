---
name: hubspot-developer
description: "HubSpot developer integrations for Hair Solutions Co. — Agent Tools, Custom Channels API, Breeze Customer Agent, and The Hair Concierge app architecture. Use when building HubSpot integrations, writing hsmeta."
---

# HubSpot Developer — Hair Solutions Co.

## The Hair Concierge Architecture

```
Mobile App (React Native/Expo)
        ↓
Custom Channels API  →  HubSpot Platform
                              ↓
                     Breeze Customer Agent
                              ↓
                        Agent Tools (custom)
                         ├── Shopify Product Query  (GET_DATA)
                         ├── Reorder Hair System    (TAKE_ACTION)
                         ├── Check Subscription     (GET_DATA)
                         └── KB Deep Search         (GENERATE)
                              ↓
                     Node.js Backend + Shopify Storefront API
```

**Why this architecture:**
- Breeze handles the AI — no custom LLM pipeline needed
- Custom Channel = conversations appear natively in HubSpot with full CRM context
- Agent Tools extend Breeze with Shopify/subscription capabilities
- All customer data lives in HubSpot CRM as single source of truth

## Agent Tools — Quick Reference

**Tool types:**
- `GET_DATA` — retrieve info, no user review required
- `GENERATE` — create content/summaries, no user review required
- `TAKE_ACTION` — performs actions (create/update/delete), requires user review

**Key constraints:**
- All output values must be **strings** — no arrays or objects
- No HubSpot Functions (serverless) — must use external `actionUrl`
- Agent has NO CRM data access unless you give it tools to get it
- `isRequired: false` to start — required fields cannot be removed after upload
- Platform version: always `"2025.2"` in hsproject.json

**Deploy commands:**
```bash
hs project upload
hs project deploy
```

## Custom Channels — Quick Reference

**Register a channel:**
```
POST /conversations/v3/custom-channels?hapikey={KEY}&appId={ID}
```
Requires public app + Sales/Service Hub Professional+

**Message flow:**
```
User → POST /messages (INCOMING) → HubSpot → Breeze → Agent Tools
Breeze response → Webhook (OUTGOING) → Node.js backend → WebSocket → Mobile app
```

Threading model: `INTEGRATION_THREAD_ID` — you manage thread IDs, supports concurrent conversations.

## Breeze Customer Agent — Quick Reference

- **Pricing:** 100 credits per conversation (reopened = 0 credits)
- **Auto-deploys** to connected custom channels (as of Jan 2026)
- **Knowledge sources:** KB articles, blog posts, website pages, uploaded files
- Feed it: all hairsolutions.co product pages, 1,200+ blog articles, KB articles, maintenance guides

## Execution States

| State | Behaviour |
|-------|-----------|
| `SUCCESS` | Done, agent continues |
| `FAIL_CONTINUE` | Failed, agent continues anyway |
| `BLOCK` | Paused — waiting for callback or expiration |

## Security — Signature Validation

```javascript
const hash = crypto.createHash('sha256')
  .update(clientSecret + JSON.stringify(req.body))
  .digest('hex');
// compare hash === req.headers['x-hubspot-signature']
```
Validate `x-hubspot-signature` v2 on every incoming agent tool request.

## Reference Files

- `references/agent-tools.md` — full hsmeta.json schema, input/output types, testing
- `references/custom-channels.md` — register, connect, message payloads, threading
- `references/breeze-agent.md` — setup, knowledge sources, personality, pricing
- `references/code-examples.md` — complete JSON blueprints for all 4 Hair Concierge tools

## Essential Links

| Resource | URL |
|----------|-----|
| Agent Tools overview | https://developers.hubspot.com/docs/apps/developer-platform/add-features/agent-tools/overview |
| Agent Tools create | https://developers.hubspot.com/docs/apps/developer-platform/add-features/agent-tools/create |
| Custom Channels guide | https://developers.hubspot.com/docs/api-reference/conversations-custom-channels-v3/guide |
| Customer Agent setup | https://knowledge.hubspot.com/customer-agent/create-a-customer-agent |
| HubSpot CLI docs | https://developers.hubspot.com/docs/platform/project-cli-commands |
