---
name: seo-audit
description: "Audit websites for SEO issues, analyze rankings, identify optimization opportunities, fix technical SEO problems, and build keyword strategies. Use when auditing a website, researching keywords."
---

# SEO Audit & Optimization

Systematic SEO analysis and improvement for Shopify stores and service business websites.

## Audit Checklist

### Technical SEO
- [ ] Site loads in under 3 seconds (Core Web Vitals: LCP < 2.5s, FID < 100ms, CLS < 0.1)
- [ ] HTTPS enabled with no mixed content warnings
- [ ] XML sitemap exists and submitted to Google Search Console
- [ ] Robots.txt is correctly configured (not blocking key pages)
- [ ] No duplicate content (canonical tags set correctly)
- [ ] Mobile-friendly (Google's Mobile-Friendly Test)
- [ ] No broken links (404 errors)
- [ ] Structured data / Schema markup implemented
- [ ] Hreflang tags if multilingual

### On-Page SEO
- [ ] Each page has unique title tag (50–60 chars) with primary keyword
- [ ] Meta descriptions (150–160 chars) are compelling and keyword-rich
- [ ] H1 tag exists, contains primary keyword, appears once
- [ ] H2/H3 tags used for content hierarchy
- [ ] Primary keyword in first 100 words of content
- [ ] Images have descriptive alt text (not "image123.jpg")
- [ ] Internal linking structure connects related pages
- [ ] URL slugs are descriptive and keyword-rich (no parameters)

### Content Quality
- [ ] Minimum 300 words per indexable page (service/product pages: 600+)
- [ ] No thin or duplicate content across pages
- [ ] FAQs added to target People Also Ask
- [ ] Fresh content signals (blog updated regularly)

### Shopify-Specific
- [ ] Product descriptions are unique (not manufacturer copy)
- [ ] Collection pages have descriptive intro text
- [ ] Product images optimized (WebP format, alt text)
- [ ] Shopify auto-generates canonical tags — verify they're correct
- [ ] Avoid duplicate pages from faceted navigation

## Keyword Research Framework

### Keyword Tiers

**Tier 1 — Pillar Keywords** (high volume, high competition)
- Monthly volume: 10,000+
- Goal: Long-term authority building
- Strategy: Pillar pages, comprehensive guides

**Tier 2 — Target Keywords** (medium volume, medium competition)
- Monthly volume: 500–10,000
- Goal: Primary traffic drivers
- Strategy: Service/product pages, blog posts

**Tier 3 — Long-Tail Keywords** (low volume, low competition)
- Monthly volume: 50–500
- Goal: Quick wins, specific buyer intent
- Strategy: FAQ pages, specific articles

### Keyword Research Process
1. Seed keywords from business description + competitor domains
2. Expand using Google Autocomplete + People Also Ask
3. Analyze using Google Keyword Planner, Ubersuggest, or Ahrefs
4. Group by search intent (informational, commercial, transactional)
5. Map keywords to specific pages (one primary keyword per page)
6. Identify gaps — topics competitors rank for but you don't

## On-Page Optimization Template

```markdown
Page: [URL]
Primary Keyword: [keyword] (monthly volume: X)
Secondary Keywords: [keyword1, keyword2]

CURRENT:
Title: [current title]
Meta: [current meta description]
H1: [current H1]
Word Count: [X]

OPTIMIZED:
Title: [keyword] | [Brand Name] [Under 60 chars]
Meta: [compelling description with keyword + CTA, 150-160 chars]
H1: [Primary keyword naturally included]
Content Additions: [list what's missing]
```

## Core Web Vitals Fixes

### Largest Contentful Paint (LCP)
- Optimize above-fold images (compress, use WebP, add `loading="eager"`)
- Preload hero image with `<link rel="preload">`
- Use CDN (Cloudinary for image delivery)
- Reduce server response time

### Cumulative Layout Shift (CLS)
- Set explicit width/height on all images and videos
- Reserve space for ads and embeds
- Avoid injecting content above existing content

### First Input Delay (FID)
- Minimize JavaScript execution on main thread
- Defer non-critical JavaScript
- Break up long tasks

## Local SEO (Service Businesses)

- Complete Google Business Profile with photos, hours, services
- NAP consistency (Name, Address, Phone) across all citations
- Encourage and respond to Google reviews
- Local landing pages for each service area
- Local schema markup (LocalBusiness type)
- Citations in relevant directories (Yelp, Yellow Pages, industry-specific)

## Competitor Analysis

For each top-3 competitor:
1. Check domain authority (Moz/Ahrefs)
2. Top organic keywords (Ubersuggest/SEMrush)
3. Backlink sources — identify linkable patterns
4. Content gaps — what do they rank for that you don't?
5. Page structure differences on high-ranking pages

## Reporting Metrics

Track monthly in Google Search Console + Analytics 4:
- Total organic impressions and clicks
- Average position for top 20 keywords
- Click-through rate by page
- Pages gaining/losing impressions
- Core Web Vitals scores
