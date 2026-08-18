---
name: mcp-n8n
description: "Build and manage n8n automation workflows — create multi-step automations connecting any apps, set up triggers, data transformations, conditional logic, and scheduled jobs. Use when designing workflow automations."
---

# n8n Workflow Automation

n8n is a self-hosted or cloud workflow automation tool that connects apps and services with visual logic flows. Build no-code/low-code automations that run on schedule or trigger from events.

## Connection

n8n exposes a REST API and can receive webhooks. Connect via:

```bash
export N8N_URL="https://your-n8n-instance.com"
export N8N_API_KEY="n8n_api_xxxxx"
```

## Core Concepts

| Term | Meaning |
|------|---------|
| Workflow | A sequence of connected nodes |
| Node | An action step (e.g., HTTP Request, Slack, HubSpot) |
| Trigger | The starting node (webhook, schedule, app event) |
| Execution | A single run of a workflow |
| Expression | Dynamic value using `{{ }}` syntax |

## Workflow Patterns for Hair Solutions Co.

### New Booking → CRM + Notification
```
Trigger: Webhook (from booking system)
→ Node: HubSpot — Create/Update Contact
→ Node: HubSpot — Create Deal
→ Node: Slack — Notify team
→ Node: Gmail — Send confirmation to client
```

### Daily Review Digest
```
Trigger: Schedule (8am daily)
→ Node: Google Sheets — Fetch yesterday's appointments
→ Node: Google Analytics — Pull website traffic
→ Node: OpenAI — Summarize insights
→ Node: Slack — Post digest to #daily-review
```

### E-commerce Order Processing
```
Trigger: Shopify — New Order
→ Node: Notion — Create order record
→ Node: HubSpot — Update contact purchase history
→ Node: Gmail — Send thank-you email
→ Node: IF Node — If order > $100: add "VIP" tag
```

### Instagram → Content Calendar Sync
```
Trigger: Schedule (weekly)
→ Node: Notion — Read upcoming content calendar
→ Node: Cloudinary — Fetch approved images
→ Node: Instagram Graph API — Schedule posts
→ Node: Slack — Confirm scheduled posts
```

## API Operations

### List Workflows

```bash
curl "$N8N_URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"
```

### Execute Workflow

```bash
curl -X POST "$N8N_URL/api/v1/workflows/{workflowId}/execute" \
  -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data": {"key": "value"}}'
```

### Create Webhook Trigger

```bash
# Webhook URL format for n8n
https://your-n8n.com/webhook/{webhook-path}
```

## n8n Expression Syntax

```javascript
// Access previous node output
{{ $json["fieldName"] }}

// Format date
{{ $now.format('YYYY-MM-DD') }}

// Conditional
{{ $json.amount > 100 ? "VIP" : "standard" }}

// Merge from specific node
{{ $node["HubSpot"].json["id"] }}
```

## Data Transformation Nodes

- **Set**: Rename/restructure fields
- **Function**: Custom JavaScript transformations
- **Merge**: Combine data from multiple branches
- **Split In Batches**: Process large arrays in chunks
- **IF / Switch**: Conditional routing

## Best Practices

- Test workflows with sample data before activating
- Use the Error Trigger node for failed execution alerts
- Add wait nodes between API calls to respect rate limits
- Use credentials manager for all API keys — never hardcode
- Enable execution logging for audit trails
- Keep workflows focused — one workflow per business process
