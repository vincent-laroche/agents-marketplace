---
name: notion
description: "Work with Notion workspaces using the official API — read pages, query databases, create and update content, manage blocks. Use when reading Notion pages, writing to Notion databases, building knowledge bases."
---

# Notion Integration

Use the Notion API to read and write pages, query databases, manage blocks, and automate workspace workflows.

## Authentication

```bash
export NOTION_API_KEY="secret_xxxxx"
```

Get your key at: https://www.notion.so/profile/integrations

## API Version

```
Notion-Version: 2025-09-03
```

**Important for v2025-09-03**: Databases are now called "data sources" — use `/data_sources/` endpoints for queries.

## Core Operations

### Search

```bash
curl -X POST https://api.notion.com/v1/search \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hair Solutions", "filter": {"value": "page", "property": "object"}}'
```

### Get Page

```bash
curl https://api.notion.com/v1/pages/{page_id} \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03"
```

### Get Page Blocks (Content)

```bash
curl https://api.notion.com/v1/blocks/{page_id}/children \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03"
```

### Query Database

```bash
curl -X POST https://api.notion.com/v1/databases/{database_id}/query \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "filter": {
      "property": "Status",
      "select": {"equals": "In Progress"}
    },
    "sorts": [{"property": "Created", "direction": "descending"}]
  }'
```

### Create Page in Database

```bash
curl -X POST https://api.notion.com/v1/pages \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"database_id": "{database_id}"},
    "properties": {
      "Name": {"title": [{"text": {"content": "New Entry"}}]},
      "Status": {"select": {"name": "To Do"}},
      "Tags": {"multi_select": [{"name": "urgent"}]},
      "Due Date": {"date": {"start": "2026-03-15"}}
    }
  }'
```

### Update Page Properties

```bash
curl -X PATCH https://api.notion.com/v1/pages/{page_id} \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "properties": {
      "Status": {"select": {"name": "Done"}}
    }
  }'
```

### Append Blocks to Page

```bash
curl -X PATCH https://api.notion.com/v1/blocks/{page_id}/children \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "children": [
      {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
          "rich_text": [{"type": "text", "text": {"content": "New paragraph content"}}]
        }
      },
      {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
          "rich_text": [{"type": "text", "text": {"content": "New Section"}}]
        }
      }
    ]
  }'
```

## Property Types Reference

| Type | JSON Format |
|------|-------------|
| Title | `{"title": [{"text": {"content": "value"}}]}` |
| Rich text | `{"rich_text": [{"text": {"content": "value"}}]}` |
| Number | `{"number": 42}` |
| Select | `{"select": {"name": "option"}}` |
| Multi-select | `{"multi_select": [{"name": "tag1"}, {"name": "tag2"}]}` |
| Date | `{"date": {"start": "2026-01-15"}}` |
| Checkbox | `{"checkbox": true}` |
| URL | `{"url": "https://example.com"}` |
| Email | `{"email": "user@example.com"}` |
| People | `{"people": [{"id": "user_id"}]}` |
| Relation | `{"relation": [{"id": "page_id"}]}` |

## Best Practices

- Always paginate with `start_cursor` when results may exceed 100 items
- Cache database IDs rather than searching repeatedly
- Use `filter` + `sorts` in database queries to minimize data transfer
- Integration must be shared with pages to access them — add via page "Share" menu
