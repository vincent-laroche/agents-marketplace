---
name: google-analytics
description: "Work with Google Analytics 4 — run reports, analyze traffic, track e-commerce conversions, build custom dimensions, set up events, interpret metrics, and export data via the GA4 API. Use when analyzing website traffic."
---

# Google Analytics 4 (GA4)

Analyze website traffic, user behavior, and conversions using GA4's event-based measurement model.

## Authentication

```bash
export GA4_PROPERTY_ID="properties/123456789"
export GA4_KEY_FILE="path/to/service-account-key.json"
```

GA4 API uses Google OAuth 2.0 or Service Account authentication.

## Data API — Run Reports

### Basic Traffic Report

```python
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, RunReportRequest
)

client = BetaAnalyticsDataClient.from_service_account_file(GA4_KEY_FILE)

request = RunReportRequest(
    property=GA4_PROPERTY_ID,
    date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    dimensions=[
        Dimension(name="sessionDefaultChannelGroup"),
        Dimension(name="deviceCategory")
    ],
    metrics=[
        Metric(name="sessions"),
        Metric(name="engagedSessions"),
        Metric(name="totalRevenue"),
        Metric(name="conversions")
    ]
)

response = client.run_report(request)

for row in response.rows:
    print([dim.value for dim in row.dimension_values],
          [metric.value for metric in row.metric_values])
```

### E-commerce Performance Report

```python
request = RunReportRequest(
    property=GA4_PROPERTY_ID,
    date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
    dimensions=[
        Dimension(name="itemName"),
        Dimension(name="itemCategory")
    ],
    metrics=[
        Metric(name="itemsPurchased"),
        Metric(name="itemRevenue"),
        Metric(name="itemsAddedToCart"),
        Metric(name="cartToViewRate")
    ],
    order_bys=[{"metric": {"metric_name": "itemRevenue"}, "desc": True}]
)
```

### Landing Page Performance

```python
request = RunReportRequest(
    property=GA4_PROPERTY_ID,
    date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    dimensions=[Dimension(name="landingPage")],
    metrics=[
        Metric(name="sessions"),
        Metric(name="bounceRate"),
        Metric(name="averageSessionDuration"),
        Metric(name="conversions")
    ],
    limit=25
)
```

## Key GA4 Metrics Reference

| Metric Name | Description |
|-------------|-------------|
| `sessions` | Total sessions |
| `activeUsers` | Users who had at least 1 engaged session |
| `engagedSessions` | Sessions > 10s or with conversion/2+ page views |
| `engagementRate` | Engaged sessions / total sessions |
| `bounceRate` | Non-engaged sessions / total sessions |
| `averageSessionDuration` | Avg seconds per session |
| `screenPageViews` | Total page views |
| `conversions` | Events marked as conversions |
| `totalRevenue` | E-commerce revenue |
| `purchaseRevenue` | Revenue from purchases |
| `transactions` | Number of purchases |
| `ecommercePurchases` | Purchase events |

## Key Dimensions Reference

| Dimension | Values |
|-----------|--------|
| `sessionDefaultChannelGroup` | Organic Search, Paid Search, Direct, Social, Email, Referral |
| `deviceCategory` | desktop, mobile, tablet |
| `country` | Country name |
| `city` | City name |
| `landingPage` | URL path |
| `pagePath` | Current page URL path |
| `sessionSourceMedium` | `google / organic`, `facebook / cpc` |
| `firstUserMedium` | Acquisition medium for new users |

## Event Tracking

GA4 collects events automatically. Key automatic events:

| Event | Trigger |
|-------|---------|
| `page_view` | Every page load |
| `scroll` | User scrolls 90% of page |
| `click` | Outbound link clicks |
| `view_search_results` | Site search |
| `video_start / video_complete` | YouTube embeds |
| `purchase` | E-commerce purchase |
| `add_to_cart` | Add to cart |
| `begin_checkout` | Checkout initiated |

### Custom Events (via gtag.js)

```javascript
// Book appointment click
gtag('event', 'book_appointment_click', {
  'appointment_type': 'keratin_treatment',
  'page_location': window.location.href
});

// Product video play
gtag('event', 'product_video_play', {
  'product_name': 'Hair Restoration Kit',
  'video_title': 'Product Demo'
});

// Newsletter signup
gtag('event', 'newsletter_signup', {
  'signup_location': 'footer'
});
```

## Conversion Configuration

Mark key events as conversions in GA4 Admin → Events → Toggle "Mark as conversion":
- `purchase` (automatic for e-commerce)
- `generate_lead`
- `book_appointment_click`
- `form_submit`

## Funnel Analysis (Exploration Reports)

Build funnel in GA4 → Explore → Funnel Exploration:
```
Step 1: page_view (where: /products)
Step 2: add_to_cart
Step 3: begin_checkout
Step 4: purchase
```

## Regular Reporting Schedule

**Weekly (Monday)**
- Sessions and engagement rate vs. prior week
- Top landing pages by sessions
- Conversions by channel
- E-commerce revenue

**Monthly**
- Channel performance trend (4-week rolling)
- Top/bottom performing products
- Geo performance
- Device split
- New vs. returning user ratio

## GA4 Debugging

Use `?gtm_debug=x` URL parameter with GTM preview mode to verify events fire correctly. Or enable GA4 DebugView: Admin → DebugView (requires `debug_mode: true` in gtag config).
