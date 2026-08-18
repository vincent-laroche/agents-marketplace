---
name: mux-video
description: "Host, stream, and deliver video using Mux — upload videos, generate playback URLs, monitor performance, create live streams, and add video to Shopify stores or websites. Use when hosting video infrastructure."
---

# Mux Video Infrastructure

Host, stream, and deliver professional video using Mux's developer-friendly video API.

## Authentication

```bash
export MUX_TOKEN_ID="your-token-id"
export MUX_TOKEN_SECRET="your-token-secret"
```

## Upload a Video

### Direct Upload (from URL)
```bash
curl -X POST "https://api.mux.com/video/v1/assets" \
  -u "$MUX_TOKEN_ID:$MUX_TOKEN_SECRET" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "https://example.com/my-video.mp4",
    "playback_policy": ["public"],
    "mp4_support": "standard"
  }'
```

### Direct Upload (from browser/client)
```bash
# Step 1: Create upload URL
curl -X POST "https://api.mux.com/video/v1/uploads" \
  -u "$MUX_TOKEN_ID:$MUX_TOKEN_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"cors_origin": "https://your-site.com", "new_asset_settings": {"playback_policy": ["public"]}}'

# Step 2: PUT the video file to the returned upload_url (from client)
```

## Playback

```javascript
// HLS playback URL format
const playbackId = "your-playback-id";
const hlsUrl = `https://stream.mux.com/${playbackId}.m3u8`;

// Thumbnail
const thumbnailUrl = `https://image.mux.com/${playbackId}/thumbnail.jpg`;
const thumbnailWithTimestamp = `https://image.mux.com/${playbackId}/thumbnail.jpg?time=5`;

// Animated GIF preview
const gifUrl = `https://image.mux.com/${playbackId}/animated.gif`;
```

## Embed with Mux Player

```html
<!-- Via CDN -->
<script src="https://cdn.jsdelivr.net/npm/@mux/mux-player@2"></script>

<mux-player
  playback-id="your-playback-id"
  metadata-video-title="Hair Transformation Tutorial"
  metadata-viewer-user-id="user-123"
  accent-color="#d4a853"
  autoplay="muted"
  loop
  muted
></mux-player>
```

## Shopify Integration

Add Mux video to Shopify product pages:

```liquid
{# In product template or section #}
{% if product.metafields.custom.mux_playback_id %}
  <script src="https://cdn.jsdelivr.net/npm/@mux/mux-player@2"></script>
  <mux-player
    playback-id="{{ product.metafields.custom.mux_playback_id.value }}"
    metadata-video-title="{{ product.title | escape }} — Demo Video"
    accent-color="{{ settings.color_accent }}"
    style="width: 100%; aspect-ratio: 16/9;"
  ></mux-player>
{% endif %}
```

## Get Asset Details

```bash
curl "https://api.mux.com/video/v1/assets/{asset_id}" \
  -u "$MUX_TOKEN_ID:$MUX_TOKEN_SECRET"
```

Response includes: status, duration, resolution, aspect_ratio, playback_ids

## Video Analytics

```bash
# Get video views
curl "https://api.mux.com/data/v1/metrics/video_views/breakdown?dimension=asset_id&timeframe=7:days" \
  -u "$MUX_TOKEN_ID:$MUX_TOKEN_SECRET"

# Get playback quality metrics
curl "https://api.mux.com/data/v1/metrics/video_quality_score/overall?timeframe=7:days" \
  -u "$MUX_TOKEN_ID:$MUX_TOKEN_SECRET"
```

## Live Streaming

```bash
# Create live stream
curl -X POST "https://api.mux.com/video/v1/live-streams" \
  -u "$MUX_TOKEN_ID:$MUX_TOKEN_SECRET" \
  -H "Content-Type: application/json" \
  -d '{
    "playback_policy": ["public"],
    "new_asset_settings": {"playback_policy": ["public"]},
    "reconnect_window": 60
  }'

# Response includes stream_key for OBS/streaming software
# And playback_id for embedding the live stream
```

## Image & GIF API

```bash
# Custom thumbnail (time in seconds)
https://image.mux.com/{playback_id}/thumbnail.jpg?time=3&width=1280&height=720

# Storyboard (sprite of thumbnails for scrubbing)
https://image.mux.com/{playback_id}/storyboard.jpg

# Animated GIF preview
https://image.mux.com/{playback_id}/animated.gif?start=2&end=8&fps=15&width=320
```

## Pricing Notes

- Storage: $0.0059/minute stored
- Delivery: $0.0025/minute delivered
- Encoding: $0.015/minute for HD
- Image: free within fair use
- Live stream: $0.015/minute

## Best Practices for Hair Solutions Co.

- Store `mux_playback_id` as a product metafield for product demo videos
- Use animated GIF previews on collection pages (hover effect)
- Custom thumbnail with branded frame
- Autoplay muted loop for hero videos (engagement without friction)
- Upload raw footage — Mux handles encoding/optimization automatically
