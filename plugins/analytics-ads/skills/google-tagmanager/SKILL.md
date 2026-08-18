---
name: google-tagmanager
description: "Implement and manage Google Tag Manager — set up tags, triggers, variables, deploy tracking pixels, manage GA4 configuration, and audit GTM containers. Use when implementing tracking pixels."
---

# Google Tag Manager

Manage all tracking and marketing tags through GTM without requiring code deployments.

## GTM Container Setup

### Install GTM on Shopify

Add to `theme.liquid`:
```liquid
{# In <head> — first line after opening tag #}
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>

{# In <body> — immediately after opening tag #}
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

### Data Layer

Push events from Liquid to the data layer:

```liquid
{# In theme.liquid <head> — before GTM script #}
<script>
  window.dataLayer = window.dataLayer || [];
  
  {% if template.name == 'product' %}
  dataLayer.push({
    'event': 'view_item',
    'ecommerce': {
      'items': [{
        'item_id': '{{ product.id }}',
        'item_name': '{{ product.title | escape }}',
        'item_category': '{{ product.type | escape }}',
        'price': {{ product.price | divided_by: 100.0 }},
        'currency': '{{ shop.currency }}'
      }]
    }
  });
  {% endif %}
  
  {% if template.name == 'index' %}
  dataLayer.push({
    'pageType': 'homepage',
    'storeLanguage': '{{ shop.locale }}'
  });
  {% endif %}
  
  {% if customer %}
  dataLayer.push({
    'customerEmail': '{{ customer.email }}',
    'customerId': '{{ customer.id }}',
    'customerTags': '{{ customer.tags }}'
  });
  {% endif %}
</script>
```

## Standard Tag Configurations

### GA4 Configuration Tag

- **Tag Type**: Google Analytics: GA4 Configuration
- **Measurement ID**: `G-XXXXXXXXXX`
- **Trigger**: All Pages
- **Fields to Set**:
  - `send_page_view` → `true`

### GA4 Event Tag (Purchase)

- **Tag Type**: Google Analytics: GA4 Event
- **Event Name**: `purchase`
- **Event Parameters**:
  - `transaction_id` → `{{DLV - transaction_id}}`
  - `value` → `{{DLV - order_total}}`
  - `currency` → `{{DLV - currency}}`
  - `items` → `{{DLV - items}}`
- **Trigger**: Custom Event = `purchase`

### Meta Pixel

- **Tag Type**: Custom HTML
- **Trigger**: All Pages
```html
<script>
!function(f,b,e,v,n,t,s){...}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{{Meta Pixel ID}}');
fbq('track', 'PageView');
</script>
```

### Meta Purchase Event

- **Tag Type**: Custom HTML
- **Trigger**: Custom Event = `purchase`
```html
<script>
fbq('track', 'Purchase', {
  value: {{DLV - order_total}},
  currency: '{{DLV - currency}}',
  content_ids: [{{DLV - product_ids}}],
  content_type: 'product'
});
</script>
```

## Variables Setup

### Data Layer Variables

Create these DLV (Data Layer Variable) variables:
- `DLV - transaction_id` → `transactionId`
- `DLV - order_total` → `orderTotal`
- `DLV - currency` → `currency`
- `DLV - items` → `items`
- `DLV - product_ids` → `productIds`

### JavaScript Variable
```javascript
// Variable Type: Custom JavaScript
// Name: CJS - Current Page Type
function() {
  return document.body.getAttribute('data-page-type') || 'unknown';
}
```

## Trigger Types

| Trigger | Use Case |
|---------|---------|
| All Pages | GA4 config, Meta Pixel PageView |
| DOM Ready | Page-specific events needing DOM |
| Custom Event | Purchase, add_to_cart, etc. |
| Click - All Elements | CTA clicks |
| Click - Just Links | External link tracking |
| Form Submission | Newsletter, contact forms |
| Timer | Engagement time tracking |
| Scroll Depth | Content engagement |

## GTM Container Audit Checklist

- [ ] No duplicate tags firing (check "Tag Firing Summary" in preview)
- [ ] All triggers use specific conditions, not "All Pages" unless needed
- [ ] Variables named consistently (type prefix: DLV-, CJS-, CON-)
- [ ] Tags have descriptive names: `GA4 - Event - Purchase`
- [ ] Old/unused tags are paused, not deleted (for history)
- [ ] Preview mode tested before every publish
- [ ] Container has notes on major changes
- [ ] Folders used to organize tags by category

## Preview & Debug

1. Click "Preview" in GTM
2. Enter your store URL
3. GTM debugger shows which tags fire on each page
4. Check "Tag Firing Summary" for any unexpected fires
5. Click specific tags to see the exact data pushed

## Publishing Workflow

1. Create all tags/triggers/variables in draft
2. Preview and test thoroughly
3. Fix any issues found in preview
4. Add version note describing changes
5. Submit → Publish
6. Verify in GA4 DebugView / Meta Events Manager

## Common Issues

**Tag firing multiple times**
- Add "Once per page" firing frequency to single-fire tags
- Check for duplicate trigger configurations

**Purchase not tracking**
- Verify data layer push fires on /thank-you page
- Check variable names match between data layer and GTM variables
- Confirm `purchase` event reaches GA4 via DebugView

**Slow page speed from GTM**
- Audit tags — remove old/unused ones
- Consolidate: replace multiple vendor pixels with server-side GTM
- Use async loading wherever possible
