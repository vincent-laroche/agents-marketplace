---
name: instagram
description: "Manage Instagram presence via the Instagram Graph API — publish posts, reels, stories, carousels, schedule content, analyze metrics, manage comments, and run DM campaigns. Use when posting to Instagram."
---

# Instagram Graph API

Manage a professional Instagram presence through the Meta Graph API. Requires a Business or Creator account connected to a Facebook Page.

## Prerequisites

1. Instagram Business or Creator account
2. Connected Facebook Page
3. Meta Developer App with Instagram Graph API permissions
4. `instagram_business_basic`, `instagram_content_publish`, `instagram_manage_comments` scopes

## Authentication

```bash
export IG_ACCESS_TOKEN="EAAxxxxx"
export IG_USER_ID="17841400000000000"
```

## Content Publishing

### Single Image Post

```bash
# Step 1: Create media container
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media" \
  -F "image_url=https://your-cdn.com/hair-product.jpg" \
  -F "caption=Transform your hair care routine ✨ Shop link in bio." \
  -F "access_token=$IG_ACCESS_TOKEN"

# Step 2: Publish (use returned creation_id)
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media_publish" \
  -F "creation_id=17889615814797252" \
  -F "access_token=$IG_ACCESS_TOKEN"
```

### Reel

```bash
# Step 1: Create reel container
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media" \
  -F "media_type=REELS" \
  -F "video_url=https://your-cdn.com/hair-tutorial.mp4" \
  -F "caption=60-second hair transformation 💆‍♀️ Save this for your next appointment!" \
  -F "share_to_feed=true" \
  -F "access_token=$IG_ACCESS_TOKEN"

# Step 2: Poll for ready status
curl "https://graph.facebook.com/v21.0/{creation_id}?fields=status_code&access_token=$IG_ACCESS_TOKEN"

# Step 3: Publish when status_code = FINISHED
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media_publish" \
  -F "creation_id={creation_id}" \
  -F "access_token=$IG_ACCESS_TOKEN"
```

### Carousel Post

```bash
# Step 1: Create child containers for each image
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media" \
  -F "image_url=https://cdn.com/slide1.jpg" \
  -F "is_carousel_item=true" \
  -F "access_token=$IG_ACCESS_TOKEN"

# Step 2: Create carousel container
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media" \
  -F "media_type=CAROUSEL" \
  -F "children=child_id_1,child_id_2,child_id_3" \
  -F "caption=Before & After: Our signature treatment 👑 Swipe to see the full transformation!" \
  -F "access_token=$IG_ACCESS_TOKEN"

# Step 3: Publish
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media_publish" \
  -F "creation_id={carousel_id}" \
  -F "access_token=$IG_ACCESS_TOKEN"
```

## Analytics

### Account Insights

```bash
curl "https://graph.facebook.com/v21.0/$IG_USER_ID/insights?metric=reach,impressions,profile_views,follower_count&period=day&since=2026-02-01&until=2026-02-27&access_token=$IG_ACCESS_TOKEN"
```

### Media Insights

```bash
curl "https://graph.facebook.com/v21.0/{media_id}/insights?metric=reach,impressions,saved,video_views,shares&access_token=$IG_ACCESS_TOKEN"
```

### Audience Demographics

```bash
curl "https://graph.facebook.com/v21.0/$IG_USER_ID/insights?metric=audience_city,audience_country,audience_gender_age&period=lifetime&access_token=$IG_ACCESS_TOKEN"
```

## Comment Management

### Get Comments

```bash
curl "https://graph.facebook.com/v21.0/{media_id}/comments?fields=text,username,timestamp&access_token=$IG_ACCESS_TOKEN"
```

### Reply to Comment

```bash
curl -X POST "https://graph.facebook.com/v21.0/{comment_id}/replies" \
  -F "message=Thank you! Book your appointment at the link in bio 💙" \
  -F "access_token=$IG_ACCESS_TOKEN"
```

### Hide Comment

```bash
curl -X POST "https://graph.facebook.com/v21.0/{comment_id}?hidden=true&access_token=$IG_ACCESS_TOKEN"
```

## Best Posting Times for Beauty/Hair Industry

- Tuesday–Friday: 11am–1pm and 7pm–9pm (local time)
- Saturday: 10am–12pm
- Avoid: Monday mornings, late Sunday nights

## Content Strategy for Hair Solutions Co.

- **Feed posts**: Before/after transformations, product showcases, team spotlights
- **Reels**: Tutorials (30–60s), behind-the-scenes, trending audio hooks
- **Stories**: Daily engagement — polls, Q&As, flash promos, appointment reminders
- **Carousels**: Multi-step tutorials, product comparisons, tip lists (saves = reach boost)

## Rate Limits

- Content publishing: 50 posts per 24 hours
- API calls: 200/hour per token
