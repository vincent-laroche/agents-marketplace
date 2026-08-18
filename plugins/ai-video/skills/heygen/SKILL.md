---
name: heygen
description: "Create AI avatar videos with HeyGen — generate personalized videos at scale, create AI clones, build interactive avatars, use photo avatars, and manage video generation via API. Use when creating AI avatar videos."
---

# HeyGen AI Video Generation

Generate professional AI avatar videos at scale — from personalized outreach to scalable content production.

## Authentication

```bash
export HEYGEN_API_KEY="your-heygen-api-key"
```

Get key at: app.heygen.com → Settings → API

## Core Workflows

### Generate a Video

```bash
curl -X POST "https://api.heygen.com/v2/video/generate" \
  -H "X-Api-Key: $HEYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "video_inputs": [{
      "character": {
        "type": "avatar",
        "avatar_id": "avatar_id_here",
        "avatar_style": "normal"
      },
      "voice": {
        "type": "text",
        "voice_id": "voice_id_here",
        "input_text": "Hello! Welcome to Hair Solutions. I'"'"'m excited to share our latest hair restoration treatment that has helped over 500 clients in Toronto."
      },
      "background": {
        "type": "color",
        "value": "#f8f4f0"
      }
    }],
    "dimension": {"width": 1280, "height": 720},
    "aspect_ratio": "16:9"
  }'
```

### Check Video Status

```bash
curl "https://api.heygen.com/v1/video_status.get?video_id={video_id}" \
  -H "X-Api-Key: $HEYGEN_API_KEY"
```

Response states: `processing`, `completed`, `failed`

### List Available Avatars

```bash
curl "https://api.heygen.com/v2/avatars" \
  -H "X-Api-Key: $HEYGEN_API_KEY"
```

### List Available Voices

```bash
curl "https://api.heygen.com/v2/voices" \
  -H "X-Api-Key: $HEYGEN_API_KEY"
```

## Personalized Video at Scale

Generate unique videos for each customer or prospect:

```python
import requests
import time

def generate_personalized_video(customer_name, treatment, heygen_api_key):
    script = f"""
    Hi {customer_name}! I'm reaching out from Hair Solutions Co.
    Based on your interest in {treatment}, I wanted to personally walk you 
    through what the treatment involves and what results you can expect.
    Book your free consultation at the link below — I'd love to meet you!
    """
    
    payload = {
        "video_inputs": [{
            "character": {
                "type": "avatar",
                "avatar_id": "YOUR_AVATAR_ID",
                "avatar_style": "normal"
            },
            "voice": {
                "type": "text",
                "voice_id": "YOUR_VOICE_ID",
                "input_text": script.strip()
            }
        }],
        "dimension": {"width": 1280, "height": 720}
    }
    
    response = requests.post(
        "https://api.heygen.com/v2/video/generate",
        headers={"X-Api-Key": heygen_api_key, "Content-Type": "application/json"},
        json=payload
    )
    
    video_id = response.json()["data"]["video_id"]
    
    # Poll for completion
    while True:
        status_response = requests.get(
            f"https://api.heygen.com/v1/video_status.get?video_id={video_id}",
            headers={"X-Api-Key": heygen_api_key}
        ).json()
        
        if status_response["data"]["status"] == "completed":
            return status_response["data"]["video_url"]
        elif status_response["data"]["status"] == "failed":
            raise Exception("Video generation failed")
        
        time.sleep(10)
```

## Interactive Avatar (Streaming)

HeyGen's Streaming API enables real-time interactive avatars:

```javascript
// Initialize streaming session
const sessionResponse = await fetch('https://api.heygen.com/v1/streaming.new', {
  method: 'POST',
  headers: {
    'X-Api-Key': process.env.HEYGEN_API_KEY,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    quality: 'high',
    avatar_name: 'YOUR_AVATAR_ID',
    voice: { voice_id: 'YOUR_VOICE_ID' }
  })
});

const { session_id, sdp } = await sessionResponse.json();

// Connect via WebRTC
// Use the sdp to establish WebRTC peer connection
// Then send text to make avatar speak in real-time
```

## Photo Avatar Creation

Upload a photo to create a custom avatar:
1. Go to app.heygen.com → Avatars → Create Avatar
2. Upload a high-quality face photo (forward-facing, good lighting)
3. Record 2–3 minutes of consent video
4. Avatar creation takes 24–48 hours
5. Use the avatar_id in all API calls

## Video Use Cases for Hair Solutions Co.

### Client Onboarding
- Personalized welcome video for new bookings
- Pre-appointment preparation instructions
- Treatment overview with avatar

### Marketing Content
- Product explainer videos (60–90 seconds)
- Before/after story narration
- Educational content (hair care tips)
- Social media content at scale

### Sales Outreach
- Personalized video follow-ups for leads
- Re-engagement videos for cold clients

## Best Practices

- Keep scripts under 90 seconds for engagement
- Use natural, conversational language (avoid corporate speak)
- Test voice and avatar combination before scaling
- Add captions for silent viewing (85% of social video watched silent)
- Upload to Cloudinary or Mux for reliable delivery

## Rate Limits

- Video generation: depends on plan
- Free plan: 1 credit/video
- Pro plan: 15 credits/month
- API plan: Pay-as-you-go
