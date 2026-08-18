---
name: hubspot-integration
description: "Work with HubSpot CRM using best-practice patterns for contacts, deals, companies, pipelines, custom objects, and marketing automation. Use when managing CRM data, building HubSpot workflows, syncing contacts."
---

# HubSpot Integration

Interact with HubSpot CRM using modern API patterns. Covers contact management, deal pipelines, companies, email campaigns, custom objects, and webhook automation.

## Authentication

**Private App Token (recommended):**
```bash
export HUBSPOT_ACCESS_TOKEN="pat-na1-xxxxx"
```

**OAuth 2.0 (for user-facing apps):**
- Auth URL: `https://app.hubspot.com/oauth/authorize`
- Token URL: `https://api.hubapi.com/oauth/v1/token`
- Scopes: `crm.objects.contacts.read crm.objects.contacts.write`

## Base URL
```
https://api.hubapi.com
```

## Core CRM Operations

### Contacts

**Search contacts:**
```bash
curl -X POST https://api.hubapi.com/crm/v3/objects/contacts/search \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "filterGroups": [{
      "filters": [{
        "propertyName": "email",
        "operator": "EQ",
        "value": "customer@example.com"
      }]
    }],
    "properties": ["firstname", "lastname", "email", "phone", "lifecyclestage"]
  }'
```

**Create contact:**
```bash
curl -X POST https://api.hubapi.com/crm/v3/objects/contacts \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "properties": {
      "firstname": "Jane",
      "lastname": "Doe",
      "email": "jane@example.com",
      "phone": "+1-555-0100",
      "lifecyclestage": "lead"
    }
  }'
```

**Update contact:**
```bash
curl -X PATCH https://api.hubapi.com/crm/v3/objects/contacts/{contactId} \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"properties": {"lifecyclestage": "customer"}}'
```

### Batch Operations (preferred for volume)

**Batch create contacts:**
```bash
curl -X POST https://api.hubapi.com/crm/v3/objects/contacts/batch/create \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": [
      {"properties": {"email": "a@example.com", "firstname": "Alice"}},
      {"properties": {"email": "b@example.com", "firstname": "Bob"}}
    ]
  }'
```

### Deals

**Create deal:**
```bash
curl -X POST https://api.hubapi.com/crm/v3/objects/deals \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "properties": {
      "dealname": "Hair Solutions Package - Jane Doe",
      "amount": "1200",
      "dealstage": "appointmentscheduled",
      "pipeline": "default",
      "closedate": "2026-03-31"
    }
  }'
```

**Associate deal with contact:**
```bash
curl -X PUT https://api.hubapi.com/crm/v3/objects/deals/{dealId}/associations/contacts/{contactId}/3 \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN"
```

### Companies

**Create company:**
```bash
curl -X POST https://api.hubapi.com/crm/v3/objects/companies \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "properties": {
      "name": "ACME Corp",
      "domain": "acmecorp.com",
      "industry": "HEALTH_BEAUTY_FITNESS",
      "numberofemployees": "50"
    }
  }'
```

## Pipelines

**List deal pipelines:**
```bash
curl https://api.hubapi.com/crm/v3/pipelines/deals \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN"
```

## Marketing

**Send transactional email:**
```bash
curl -X POST https://api.hubapi.com/marketing/v3/transactional/single-email/send \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "emailId": 12345,
    "message": {"to": "jane@example.com"},
    "contactProperties": {"firstname": "Jane"}
  }'
```

## Webhooks

Register webhook to receive real-time events:
```bash
curl -X POST https://api.hubapi.com/webhooks/v3/{appId}/subscriptions \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "eventType": "contact.creation",
    "propertyName": "email",
    "active": true
  }'
```

## Anti-Patterns to Avoid

- **Don't use deprecated API keys** — use Private App Tokens
- **Don't make individual requests for bulk operations** — use batch endpoints
- **Don't poll for changes** — use webhooks for real-time events
- **Don't ignore rate limits** — HubSpot allows 100 requests/10 seconds

## Rate Limits

- Free/Starter: 100 req/10 sec
- Professional/Enterprise: 150 req/10 sec
- Always include retry logic with exponential backoff
