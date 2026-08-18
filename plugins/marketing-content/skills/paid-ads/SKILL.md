---
name: paid-ads
description: "Plan, write, and optimize paid advertising campaigns across Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, and TikTok. Use when creating ad campaigns, writing ad copy, structuring audience targeting."
---

# Paid Advertising

End-to-end paid ads framework covering campaign structure, copy, targeting, bidding, and optimization across all major platforms.

## Platform Selection Guide

| Goal | Best Platform |
|------|--------------|
| High-intent buyers (searching) | Google Search Ads |
| Visual brand discovery | Instagram, TikTok |
| B2B professional targeting | LinkedIn |
| Retargeting website visitors | Google Display, Meta |
| Video storytelling | YouTube, TikTok, Reels |
| Local service discovery | Google LSA (Local Service Ads) |

## Campaign Structure

### Account → Campaign → Ad Set → Ad

```
Account: Hair Solutions Co.
├── Campaign: [Objective — Awareness / Traffic / Conversions]
│   └── Ad Set: [Audience + Budget + Placement]
│       └── Ad: [Creative + Copy]
```

### Google Ads Structure

```
Campaign: Booking Conversions
├── Ad Group: Hair Treatments Toronto
│   ├── Keywords: [hair treatment toronto], [hair salon near me]
│   └── Ad: "Book Your Hair Transformation Today"
├── Ad Group: Hair Loss Solutions
│   ├── Keywords: [hair loss treatment], [hair restoration salon]
│   └── Ad: "Stop Hair Loss — Professional Treatment"
```

### Meta Campaign Structure

```
Campaign: Lead Generation (Conversion objective)
├── Ad Set 1: Lookalike 1% (seed: past buyers)
│   └── Budget: $30/day
├── Ad Set 2: Interest targeting (hair care, beauty)
│   └── Budget: $20/day
└── Ad Set 3: Retargeting (website visitors 30 days)
    └── Budget: $15/day
```

## Ad Copy Frameworks

### PAS (Problem-Agitate-Solution)
```
Headline: [State the specific problem]
Body: [Make the problem more vivid/painful]
CTA: [Present the solution + clear action]

Example:
"Bad Hair Days Ruining Your Confidence?"
"Dull, damaged hair makes you want to hide — not show up as your best self."
"Book a Transformation Treatment → First visit 20% off"
```

### BAB (Before-After-Bridge)
```
Before: [Current frustrating state]
After: [Desired outcome state]
Bridge: [How your product/service gets them there]

Example:
"Before: Thin, lifeless hair you're embarrassed about"
"After: Full, shiny hair that turns heads"
"Bridge: Our Keratin Restoration Treatment — book today"
```

### Social Proof Formula
```
"[N] clients in [city] have [achieved result] with [product/service]"
"⭐⭐⭐⭐⭐ '[Customer quote about transformation]' — [First name, Location]"
```

### Urgency + Scarcity
```
"Only [N] spots left this month"
"[Offer] ends [date]"
"Book before [date] — pricing increases [date]"
```

## Google Ads

### Search Ad Best Practices

- Include primary keyword in Headline 1
- Dynamic keyword insertion: `{KeyWord:Default Text}`
- Use all 15 headlines and 4 descriptions
- Pin critical headlines to positions 1 & 2
- Asset groups: sitelinks, callouts, structured snippets, call extension

### Keyword Match Types

| Type | Format | When to Use |
|------|--------|-------------|
| Broad | `keyword` | Maximize reach, Discovery phase |
| Phrase | `"keyword"` | Balanced intent + reach |
| Exact | `[keyword]` | Highest intent, efficiency |
| Negative | `-keyword` | Block irrelevant traffic |

### Bidding Strategy Selection

| Objective | Bid Strategy |
|-----------|-------------|
| New campaign, limited data | Manual CPC or Max Clicks |
| Have conversion history (50+/mo) | Target CPA |
| E-commerce with revenue tracking | Target ROAS |
| Brand awareness | Target Impression Share |

### Quality Score Optimization

- Keyword → Ad → Landing Page relevance triangle
- CTR is the #1 quality score signal
- Landing page load speed matters (under 3 seconds)
- Maintain 1 topic per ad group (SKAG approach for high-value terms)

## Meta Ads (Facebook/Instagram)

### Audience Targeting Layers

```
Core Audiences (Interest/Behavior)
+ Custom Audiences (website visitors, email list, video viewers)
+ Lookalike Audiences (1–5% lookalike of best customers)
```

### Campaign Budget Optimization (CBO)
- Set budget at campaign level
- Meta auto-distributes to best-performing ad sets
- Minimum: $10/ad set/day for meaningful data

### Creative Best Practices

- **Hook**: First 3 seconds must stop the scroll
- **Aspect ratio**: 9:16 for Stories/Reels, 1:1 for feed
- **Captions**: Always on — 85% of videos watched silent
- **UGC style**: Outperforms polished ads 2–5x for cold audiences
- **Test**: 3–5 creatives per ad set minimum

### Facebook Pixel Events

```javascript
// Purchase
fbq('track', 'Purchase', {value: 75.00, currency: 'CAD'});

// Lead
fbq('track', 'Lead');

// View Content (product page)
fbq('track', 'ViewContent', {content_ids: ['SKU-123'], content_type: 'product'});

// Add to Cart
fbq('track', 'AddToCart', {value: 35.00, currency: 'CAD'});
```

## Retargeting Sequences

### E-commerce Funnel
```
Day 1–7: Viewed product → Show product + testimonial
Day 8–14: Added to cart → Show urgency + discount offer
Day 15–30: Purchased → Cross-sell complementary product
Day 31+: Exclude from purchase campaign
```

### Service Business Funnel
```
Day 1–3: Visited booking page → "Still thinking about it? Here's what our clients say"
Day 4–7: Viewed services page → Specific service showcase + CTA
Day 8–14: General visitor → Brand story + social proof
Day 15–30: 3+ visits → Direct offer with incentive
```

## Budget Allocation Framework

| Business Stage | Search | Social | Display/Retargeting |
|---------------|--------|--------|---------------------|
| New business | 60% | 30% | 10% |
| Growing | 40% | 40% | 20% |
| Scaling | 30% | 40% | 30% |

## Naming Convention

```
[Platform]-[Campaign Type]-[Audience]-[Offer]-[Date]

Examples:
META-CONV-LLA1-BookingOffer-2026Q1
GOOG-SEARCH-HairTreatments-BrandedKWs-2026Q1
META-RETARG-30DayVisitors-CarabanDiscount-2026Q1
```

## Key Performance Benchmarks (Beauty/Hair Industry)

| Metric | Good | Great |
|--------|------|-------|
| Google Search CTR | >4% | >8% |
| Meta CTR (Feed) | >1.5% | >3% |
| Conversion Rate (Booking) | >3% | >7% |
| CPA (Appointment) | <$25 | <$12 |
| ROAS (Product) | >3x | >6x |

## Common Mistakes

- Pausing campaigns before the learning phase completes (50+ conversions needed)
- Too many ad sets competing for same audience (audience overlap)
- No exclusion audiences (showing ads to existing customers)
- Changing bid strategy during active learning phase
- Not separating prospecting and retargeting into different campaigns
