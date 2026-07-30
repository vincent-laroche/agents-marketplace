# Magnific API documentation index

- Source: [https://docs.magnific.com/llms-full.txt](https://docs.magnific.com/llms-full.txt)
- Fetched: `2026-07-30T12:26:30+00:00`
- SHA-256: `5879644ce97c10669471bc874b75ac53c0bd24144576e2891e86c8bbb6975438`
- Sections: `537`

Use `../scripts/search_docs.py` for ranked full-text search.

| Line | Section | Endpoint | Official page |
|---:|---|---|---|
| 1 | Analytics API |  | [docs](https://docs.magnific.com/api-reference/analytics/overview) |
| 164 | List team API keys | `GET /v1/analytics/team-api-keys` | [docs](https://docs.magnific.com/api-reference/analytics/team-api-keys) |
| 172 | Get team credit usage over time | `POST /v1/analytics/team-credit-usage` | [docs](https://docs.magnific.com/api-reference/analytics/team-credit-usage/query) |
| 180 | List team groups | `GET /v1/analytics/team-groups` | [docs](https://docs.magnific.com/api-reference/analytics/team-groups) |
| 188 | List team members | `GET /v1/analytics/team-members` | [docs](https://docs.magnific.com/api-reference/analytics/team-members) |
| 196 | List team projects | `GET /v1/analytics/team-projects` | [docs](https://docs.magnific.com/api-reference/analytics/team-projects) |
| 204 | Audio Isolation - List tasks | `GET /v1/ai/audio-isolation` | [docs](https://docs.magnific.com/api-reference/audio-isolation/audio-isolation-tasks) |
| 212 | Audio Isolation - Extract sounds from audio/video | `POST /v1/ai/audio-isolation` | [docs](https://docs.magnific.com/api-reference/audio-isolation/isolate) |
| 236 | SAM Audio - Audio Isolation API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/audio-isolation/overview) |
| 353 | Audio Isolation - Get task status | `GET /v1/ai/audio-isolation/{task-id}` | [docs](https://docs.magnific.com/api-reference/audio-isolation/task-by-id) |
| 361 | AI Image Classifier - Detection API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/classifier/overview) |
| 482 | Analyzes an image to determine its likelihood of being AI-generated | `POST /v1/ai/classifier/image` | [docs](https://docs.magnific.com/api-reference/classifier/post-ai-classifier) |
| 490 | Creations API |  | [docs](https://docs.magnific.com/api-reference/creations/overview) |
| 598 | Get the user's most recent creations | `GET /v1/creations/recent` | [docs](https://docs.magnific.com/api-reference/creations/recent-creations) |
| 606 | Flows - Get flow definition | `GET /v1/ai/flows/{flow-id}` | [docs](https://docs.magnific.com/api-reference/flows/get-flow) |
| 625 | Flows - Get run status | `GET /v1/ai/flows/runs/{run-id}` | [docs](https://docs.magnific.com/api-reference/flows/get-run) |
| 656 | Flows - List flows | `GET /v1/ai/flows` | [docs](https://docs.magnific.com/api-reference/flows/list-flows) |
| 671 | Flows - List my flows | `GET /v1/ai/me/flows` | [docs](https://docs.magnific.com/api-reference/flows/list-my-flows) |
| 685 | Flows API |  | [docs](https://docs.magnific.com/api-reference/flows/overview) |
| 819 | Flows - Run a flow | `POST /v1/ai/flows/{flow-id}/run` | [docs](https://docs.magnific.com/api-reference/flows/run-flow) |
| 845 | AI Icon Generation - Text-to-Icon API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/icon-generation/overview) |
| 970 | AI Icon generation | `POST /v1/ai/text-to-icon` | [docs](https://docs.magnific.com/api-reference/icon-generation/post-generate-icon) |
| 981 | AI Icon preview generation | `POST /v1/ai/text-to-icon/preview` | [docs](https://docs.magnific.com/api-reference/icon-generation/post-preview) |
| 989 | Download an icon preview | `POST /v1/ai/text-to-icon/{task-id}/render/{format}` | [docs](https://docs.magnific.com/api-reference/icon-generation/post-{format}-by-id) |
| 997 | Download an icon | `GET /v1/icons/{id}/download` | [docs](https://docs.magnific.com/api-reference/icons/download-an-icon) |
| 1006 | Search and filter icons by specified order | `GET /v1/icons` | [docs](https://docs.magnific.com/api-reference/icons/get-all-icons-by-order) |
| 1015 | Get detailed icon information by ID | `GET /v1/icons/{id}` | [docs](https://docs.magnific.com/api-reference/icons/get-one-icon-by-id) |
| 1024 | Icons API |  | [docs](https://docs.magnific.com/api-reference/icons/icons-api) |
| 1076 | Ideogram Image Edit - List tasks | `GET /v1/ai/ideogram-image-edit` | [docs](https://docs.magnific.com/api-reference/ideogram-image-edit/get-ideogram-image-edit) |
| 1084 | Ideogram Image Edit - Get task status | `GET /v1/ai/ideogram-image-edit/{task-id}` | [docs](https://docs.magnific.com/api-reference/ideogram-image-edit/get-{task-id}-by-id) |
| 1092 | Ideogram Inpainting API |  | [docs](https://docs.magnific.com/api-reference/ideogram-image-edit/overview) |
| 1216 | Ideogram Image Edit - Edit an image using inpainting | `POST /v1/ai/ideogram-image-edit` | [docs](https://docs.magnific.com/api-reference/ideogram-image-edit/post-ideogram-image-edit) |
| 1234 | Change Camera - Transform image perspective | `POST /v1/ai/image-change-camera` | [docs](https://docs.magnific.com/api-reference/image-change-camera/change-camera) |
| 1252 | Change Camera - List tasks | `GET /v1/ai/image-change-camera` | [docs](https://docs.magnific.com/api-reference/image-change-camera/change-camera-tasks) |
| 1260 | Change Camera API |  | [docs](https://docs.magnific.com/api-reference/image-change-camera/overview) |
| 1377 | Change Camera - Get task status | `GET /v1/ai/image-change-camera/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-change-camera/task-by-id) |
| 1385 | Get the status of all image expand tasks | `GET /v1/ai/image-expand/flux-pro` | [docs](https://docs.magnific.com/api-reference/image-expand/get-flux-pro) |
| 1392 | Get the status of all image expand seedream v4.5 tasks | `GET /v1/ai/image-expand/seedream-v4-5` | [docs](https://docs.magnific.com/api-reference/image-expand/get-seedream-v4-5) |
| 1399 | Get the status of one image expand seedream v4.5 task | `GET /v1/ai/image-expand/seedream-v4-5/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-expand/get-seedream-v4-5-task) |
| 1406 | Get the status of one image expand task | `GET /v1/ai/image-expand/flux-pro/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-expand/get-{task-id}-by-id) |
| 1413 | Ideogram - Expand image | `POST /v1/ai/image-expand/ideogram` | [docs](https://docs.magnific.com/api-reference/image-expand/ideogram/expand-image) |
| 1423 | Get the status of all image expand ideogram tasks | `GET /v1/ai/image-expand/ideogram` | [docs](https://docs.magnific.com/api-reference/image-expand/ideogram/ideogram-tasks) |
| 1430 | Ideogram Image Expand API |  | [docs](https://docs.magnific.com/api-reference/image-expand/ideogram/overview) |
| 1545 | Get the status of one image expand ideogram task | `GET /v1/ai/image-expand/ideogram/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-expand/ideogram/task-by-id) |
| 1552 | Flux Pro Image Expand - Outpainting API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/image-expand/overview) |
| 1662 | Flux Pro - Expand image | `POST /v1/ai/image-expand/flux-pro` | [docs](https://docs.magnific.com/api-reference/image-expand/post-flux-pro) |
| 1671 | Seedream V4.5 - Expand image | `POST /v1/ai/image-expand/seedream-v4-5` | [docs](https://docs.magnific.com/api-reference/image-expand/post-seedream-v4-5) |
| 1681 | Seedream V4.5 Image Expand API |  | [docs](https://docs.magnific.com/api-reference/image-expand/seedream-v4-5-overview) |
| 1794 | Relight - Get task status | `GET /v1/ai/image-relight/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-relight/get-image-relight) |
| 1802 | Relight - List tasks | `GET /v1/ai/image-relight` | [docs](https://docs.magnific.com/api-reference/image-relight/get-image-relight-task) |
| 1810 | Overview |  | [docs](https://docs.magnific.com/api-reference/image-relight/image-relight) |
| 1911 | Relight - Adjust image lighting | `POST /v1/ai/image-relight` | [docs](https://docs.magnific.com/api-reference/image-relight/post-image-relight) |
| 1924 | Style Transfer - List tasks | `GET /v1/ai/image-style-transfer` | [docs](https://docs.magnific.com/api-reference/image-style-transfer/get-image-style-transfer) |
| 1932 | Style Transfer - Get task status | `GET /v1/ai/image-style-transfer/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-style-transfer/get-image-style-transfer-task) |
| 1940 | Overview |  | [docs](https://docs.magnific.com/api-reference/image-style-transfer/image-styletransfer) |
| 2028 | Style Transfer - Transform image style | `POST /v1/ai/image-style-transfer` | [docs](https://docs.magnific.com/api-reference/image-style-transfer/post-image-style-transfer) |
| 2035 | Image to Prompt - List tasks | `GET /v1/ai/image-to-prompt` | [docs](https://docs.magnific.com/api-reference/image-to-prompt/get-image-to-prompt) |
| 2043 | Image to Prompt - Get task status | `GET /v1/ai/image-to-prompt/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-prompt/get-{task-id}-by-id) |
| 2051 | Image to Prompt - AI Image Analysis API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/image-to-prompt/overview) |
| 2167 | Image to Prompt - Generate prompt | `POST /v1/ai/image-to-prompt` | [docs](https://docs.magnific.com/api-reference/image-to-prompt/post-image-to-prompt) |
| 2175 | Get all Veo 3.1 I2V tasks | `GET /v1/ai/image-to-video/veo-3-1` | [docs](https://docs.magnific.com/api-reference/image-to-video/get-veo-3-1) |
| 2182 | Get all Veo 3.1 I2V Fast tasks | `GET /v1/ai/image-to-video/veo-3-1-fast` | [docs](https://docs.magnific.com/api-reference/image-to-video/get-veo-3-1-fast) |
| 2189 | Get Veo 3.1 I2V Fast task by ID | `GET /v1/ai/image-to-video/veo-3-1-fast/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/get-veo-3-1-fast-task) |
| 2196 | Get all Veo 3.1 Lite I2V tasks | `GET /v1/ai/image-to-video/veo-3-1-lite` | [docs](https://docs.magnific.com/api-reference/image-to-video/get-veo-3-1-lite) |
| 2203 | Get Veo 3.1 Lite I2V task by ID | `GET /v1/ai/image-to-video/veo-3-1-lite/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/get-veo-3-1-lite-task) |
| 2210 | Get Veo 3.1 I2V task by ID | `GET /v1/ai/image-to-video/veo-3-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/get-veo-3-1-task) |
| 2217 | Happy Horse 1.1 - Create video from image | `POST /v1/ai/image-to-video/happy-horse-1-1` | [docs](https://docs.magnific.com/api-reference/image-to-video/happy-horse-1-1/generate) |
| 2231 | Happy Horse 1.1 I2V - List tasks | `GET /v1/ai/image-to-video/happy-horse-1-1` | [docs](https://docs.magnific.com/api-reference/image-to-video/happy-horse-1-1/happy-horse-1-1-i2v-tasks) |
| 2239 | Happy Horse 1.1 Image To Video API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/happy-horse-1-1/overview) |
| 2351 | Happy Horse 1.1 I2V - Get task status | `GET /v1/ai/image-to-video/happy-horse-1-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/happy-horse-1-1/task-by-id) |
| 2359 | Happy Horse 1.0 - Create video from image | `POST /v1/ai/image-to-video/happy-horse-1` | [docs](https://docs.magnific.com/api-reference/image-to-video/happy-horse-1/generate) |
| 2373 | Happy Horse 1.0 I2V - List tasks | `GET /v1/ai/image-to-video/happy-horse-1` | [docs](https://docs.magnific.com/api-reference/image-to-video/happy-horse-1/happy-horse-1-i2v-tasks) |
| 2381 | Happy Horse 1.0 Image To Video API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/happy-horse-1/overview) |
| 2492 | Happy Horse 1.0 I2V - Get task status | `GET /v1/ai/image-to-video/happy-horse-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/happy-horse-1/task-by-id) |
| 2500 | Kling Elements Pro - List tasks | `GET /v1/ai/image-to-video/kling-elements-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-elements-pro/get-kling-elements-pro) |
| 2508 | Kling Elements - Get task status | `GET /v1/ai/image-to-video/kling-elements/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-elements-pro/get-kling-elements-pro-task) |
| 2516 | Kling Elements Pro - Create video from image | `POST /v1/ai/image-to-video/kling-elements-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-elements-pro/post-kling-elements-pro) |
| 2527 | Kling Elements Standard - List tasks | `GET /v1/ai/image-to-video/kling-elements-std` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-elements-std/get-kling-elements-std) |
| 2535 | Kling Elements - Get task status | `GET /v1/ai/image-to-video/kling-elements/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-elements-std/get-kling-elements-std-task) |
| 2543 | Kling Elements Standard - Create video from image | `POST /v1/ai/image-to-video/kling-elements-std` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-elements-std/post-kling-elements-std) |
| 2554 | Kling O1 Pro - Create video from image | `POST /v1/ai/image-to-video/kling-o1-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-o1-pro) |
| 2561 | Kling O1 Pro - Create video with reference | `POST /v1/ai/image-to-video/kling-o1-pro-video-reference` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-o1-pro-video-reference) |
| 2568 | Kling O1 Standard - Create video from image | `POST /v1/ai/image-to-video/kling-o1-std` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-o1-std) |
| 2575 | Kling O1 Standard - Create video with reference | `POST /v1/ai/image-to-video/kling-o1-std-video-reference` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-o1-std-video-reference) |
| 2582 | Kling O1 - List tasks | `GET /v1/ai/image-to-video/kling-o1` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-o1-tasks) |
| 2590 | Kling O1 – Image-to-Video API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-o1/overview) |
| 2726 | Kling 1.6 Pro - List tasks | `GET /v1/ai/image-to-video/kling-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-pro/get-kling-pro) |
| 2734 | Kling 1.6 - Get task status | `GET /v1/ai/image-to-video/kling/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-pro/get-kling-pro-task) |
| 2742 | Kling 1.6 Pro - Create video from image | `POST /v1/ai/image-to-video/kling-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-pro/post-kling-pro) |
| 2753 | Kling 1.6 Pro - List tasks | `GET /v1/ai/image-to-video/kling-std` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-std/get-kling-std) |
| 2761 | Kling 1.6 - Get task status | `GET /v1/ai/image-to-video/kling/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-std/get-kling-std-task) |
| 2769 | Kling 1.6 Standard - Create video from image | `POST /v1/ai/image-to-video/kling-std` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-std/post-kling-std) |
| 2780 | Kling 2.6 Pro - Create video from text or image | `POST /v1/ai/image-to-video/kling-v2-6-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2-6-pro) |
| 2787 | Kling 2.6 Pro - List tasks | `GET /v1/ai/image-to-video/kling-v2-6` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2-6-pro-tasks) |
| 2794 | Kling 2.6 Pro - Get task status | `GET /v1/ai/image-to-video/kling-v2-6/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2-6/task-by-id) |
| 2801 | Kling 2.1 Standard - List tasks | `GET /v1/ai/image-to-video/kling-v2-1-master` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-master/get-kling-v2-1-master) |
| 2809 | Kling 2.1 Master - Get task status | `GET /v1/ai/image-to-video/kling-v2-1-master/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-master/get-kling-v2-1-master-task) |
| 2817 | Kling 2.1 Master - Create video from image | `POST /v1/ai/image-to-video/kling-v2-1-master` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-master/post-kling-v2-1-master) |
| 2825 | Kling 2.1 Pro - List tasks | `GET /v1/ai/image-to-video/kling-v2-1-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-pro/get-kling-v2-1-pro) |
| 2833 | Kling 2.1 - Get task status | `GET /v1/ai/image-to-video/kling-v2-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-pro/get-kling-v2-1-pro-task) |
| 2841 | Kling Pro v2.1 – Image‑to‑Video API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-pro/overview) |
| 2920 | Kling 2.1 Pro - Create video from image | `POST /v1/ai/image-to-video/kling-v2-1-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-pro/post-kling-v2-1-pro) |
| 2928 | Kling 2.1 Standard - List tasks | `GET /v1/ai/image-to-video/kling-v2-1-std` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-std/get-kling-v2-1-std) |
| 2936 | Kling 2.1 - Get task status | `GET /v1/ai/image-to-video/kling-v2-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-std/get-kling-v2-1-std-task) |
| 2944 | Kling Std v2.1 – Image‑to‑Video API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-std/overview) |
| 3023 | Kling 2.1 Standard - Create video from image | `POST /v1/ai/image-to-video/kling-v2-1-std` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.1-std/post-kling-v2-1-std) |
| 3031 | Kling 2.5 Pro - List tasks | `GET /v1/ai/image-to-video/kling-v2-5-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.5-pro/get-kling-v2-5-pro) |
| 3039 | Kling 2.5 Pro - Get task status | `GET /v1/ai/image-to-video/kling-v2-5-pro/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.5-pro/get-{task-id}-by-id) |
| 3047 | Kling 2.5 Turbo Pro – Image‑to‑Video API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.5-pro/overview) |
| 3110 | Kling 2.5 Pro - Create video from image | `POST /v1/ai/image-to-video/kling-v2-5-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2.5-pro/post-kling-v2-5-pro) |
| 3118 | Kling 2.0 - List tasks | `GET /v1/ai/image-to-video/kling-v2` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2/get-kling-v2) |
| 3126 | Kling 2.0 - Get task status | `GET /v1/ai/image-to-video/kling-v2/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2/get-kling-v2-task) |
| 3134 | Kling 2.0 - Create video from image | `POST /v1/ai/image-to-video/kling-v2` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v2/post-kling-v2) |
| 3145 | Kling 3.0 Turbo I2V 1080p - Generate video | `POST /v1/ai/image-to-video/kling-v3-turbo-1080p` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v3-turbo/generate-1080p) |
| 3166 | Kling 3.0 Turbo I2V 720p - Generate video | `POST /v1/ai/image-to-video/kling-v3-turbo-720p` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v3-turbo/generate-720p) |
| 3187 | Kling 3.0 Turbo Image To Video API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v3-turbo/overview) |
| 3299 | Kling 3.0 Turbo I2V - Get task status | `GET /v1/ai/image-to-video/kling-v3-turbo/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v3-turbo/task-by-id) |
| 3307 | Kling 3.0 Turbo I2V - List tasks | `GET /v1/ai/image-to-video/kling-v3-turbo` | [docs](https://docs.magnific.com/api-reference/image-to-video/kling-v3-turbo/tasks) |
| 3315 | LTX Video 2.0 Fast - Create video from image | `POST /v1/ai/image-to-video/ltx-2-fast` | [docs](https://docs.magnific.com/api-reference/image-to-video/ltx-2-fast) |
| 3331 | LTX Video 2.0 Fast I2V - List tasks | `GET /v1/ai/image-to-video/ltx-2-fast` | [docs](https://docs.magnific.com/api-reference/image-to-video/ltx-2-fast-tasks) |
| 3338 | LTX Video 2.0 Fast I2V - Get task status | `GET /v1/ai/image-to-video/ltx-2-fast/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/ltx-2-fast/task-by-id) |
| 3345 | LTX Video 2.0 Pro - Create video from image | `POST /v1/ai/image-to-video/ltx-2-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/ltx-2-pro) |
| 3361 | LTX Video 2.0 Pro I2V - List tasks | `GET /v1/ai/image-to-video/ltx-2-pro` | [docs](https://docs.magnific.com/api-reference/image-to-video/ltx-2-pro-tasks) |
| 3368 | LTX Video 2.0 Pro I2V - Get task status | `GET /v1/ai/image-to-video/ltx-2-pro/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/ltx-2-pro/task-by-id) |
| 3375 | MiniMax Hailuo 02 1080p - List tasks | `GET /v1/ai/image-to-video/minimax-hailuo-02-1080p` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-02-1080p/get-minimax-hailuo-02-1080p) |
| 3383 | MiniMax Hailuo 02 1080p - Get task status | `GET /v1/ai/image-to-video/minimax-hailuo-02-1080p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-02-1080p/get-minimax-hailuo-02-1080p-task) |
| 3391 | MiniMax Hailuo 02 1080p - Create video from text or image | `POST /v1/ai/image-to-video/minimax-hailuo-02-1080p` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-02-1080p/post-minimax-hailuo-02-1080p) |
| 3399 | MiniMax Hailuo 02 768p - List tasks | `GET /v1/ai/image-to-video/minimax-hailuo-02-768p` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-02-768p/get-minimax-hailuo-02-768p) |
| 3407 | MiniMax Hailuo 02 768p - Get task status | `GET /v1/ai/image-to-video/minimax-hailuo-02-768p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-02-768p/get-minimax-hailuo-02-768p-task) |
| 3415 | MiniMax Hailuo 02 768p - Create video from text or image | `POST /v1/ai/image-to-video/minimax-hailuo-02-768p` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-02-768p/post-minimax-hailuo-02-768p) |
| 3423 | MiniMax Hailuo 2.3 1080p Fast - List tasks | `GET /v1/ai/image-to-video/minimax-hailuo-2-3-1080p-fast` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-1080p-fast/get-minimax-hailuo-2-3-1080p-fast) |
| 3431 | MiniMax Hailuo 2.3 1080p Fast - Get task status | `GET /v1/ai/image-to-video/minimax-hailuo-2-3-1080p-fast/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-1080p-fast/get-minimax-hailuo-2-3-1080p-fast-task) |
| 3439 | MiniMax Hailuo 2.3 1080p Fast - Create video from text or image | `POST /v1/ai/image-to-video/minimax-hailuo-2-3-1080p-fast` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-1080p-fast/post-minimax-hailuo-2-3-1080p-fast) |
| 3447 | MiniMax Hailuo 2.3 1080p - List tasks | `GET /v1/ai/image-to-video/minimax-hailuo-2-3-1080p` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-1080p/get-minimax-hailuo-2-3-1080p) |
| 3455 | MiniMax Hailuo 2.3 1080p - Get task status | `GET /v1/ai/image-to-video/minimax-hailuo-2-3-1080p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-1080p/get-minimax-hailuo-2-3-1080p-task) |
| 3463 | MiniMax Hailuo 2.3 1080p - Create video from text or image | `POST /v1/ai/image-to-video/minimax-hailuo-2-3-1080p` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-1080p/post-minimax-hailuo-2-3-1080p) |
| 3471 | MiniMax Hailuo 2.3 768p Fast - List tasks | `GET /v1/ai/image-to-video/minimax-hailuo-2-3-768p-fast` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-768p-fast/get-minimax-hailuo-2-3-768p-fast) |
| 3479 | MiniMax Hailuo 2.3 768p Fast - Get task status | `GET /v1/ai/image-to-video/minimax-hailuo-2-3-768p-fast/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-768p-fast/get-minimax-hailuo-2-3-768p-fast-task) |
| 3487 | MiniMax Hailuo 2.3 768p Fast - Create video from text or image | `POST /v1/ai/image-to-video/minimax-hailuo-2-3-768p-fast` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-768p-fast/post-minimax-hailuo-2-3-768p-fast) |
| 3495 | MiniMax Hailuo 2.3 768p - List tasks | `GET /v1/ai/image-to-video/minimax-hailuo-2-3-768p` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-768p/get-minimax-hailuo-2-3-768p) |
| 3503 | MiniMax Hailuo 2.3 768p - Get task status | `GET /v1/ai/image-to-video/minimax-hailuo-2-3-768p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-768p/get-minimax-hailuo-2-3-768p-task) |
| 3511 | MiniMax Hailuo 2.3 768p - Create video from text or image | `POST /v1/ai/image-to-video/minimax-hailuo-2-3-768p` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-hailuo-2-3-768p/post-minimax-hailuo-2-3-768p) |
| 3519 | MiniMax Video 01 Live - Create video from image | `POST /v1/ai/image-to-video/minimax-live` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-live) |
| 3533 | MiniMax Video 01 Live - List tasks | `GET /v1/ai/image-to-video/minimax-live` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-live-tasks) |
| 3540 | MiniMax Video 01 Live - Get task status | `GET /v1/ai/image-to-video/minimax-live/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/minimax-live/task-by-id) |
| 3547 | Video Generation API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/overview) |
| 3604 | PixVerse V5 Transition - List tasks | `GET /v1/ai/image-to-video/pixverse-v5-transition` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-transition/get-pixverse-v5-transition) |
| 3612 | PixVerse V5 Transition - Get task status | `GET /v1/ai/image-to-video/pixverse-v5-transition/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-transition/get-{task-id}-by-id) |
| 3619 | PixVerse V5 - Video transition | `POST /v1/ai/image-to-video/pixverse-v5-transition` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-transition/post-pixverse-v5-transition) |
| 3627 | PixVerse V5.5 - Video transition | `POST /v1/ai/image-to-video/pixverse-v5-5-transition` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-v5-5-transition/create) |
| 3638 | PixVerse V5.5 Transition API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-v5-5-transition/overview) |
| 3744 | PixVerse V5.5 Transition - List tasks | `GET /v1/ai/image-to-video/pixverse-v5-5-transition` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-v5-5-transition/pixverse-v5-5-transition-tasks) |
| 3752 | PixVerse V5.5 Transition - Get task status | `GET /v1/ai/image-to-video/pixverse-v5-5-transition/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-v5-5-transition/task-by-id) |
| 3759 | PixVerse V6 - Video transition | `POST /v1/ai/image-to-video/pixverse-v6-transition` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-v6-transition/create) |
| 3770 | PixVerse V6 Transition API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-v6-transition/overview) |
| 3878 | PixVerse V6 Transition - List tasks | `GET /v1/ai/image-to-video/pixverse-v6-transition` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-v6-transition/pixverse-v6-transition-tasks) |
| 3886 | PixVerse V6 Transition - Get task status | `GET /v1/ai/image-to-video/pixverse-v6-transition/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse-v6-transition/task-by-id) |
| 3893 | PixVerse V5 - List tasks | `GET /v1/ai/image-to-video/pixverse-v5` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse/get-pixverse-v5) |
| 3901 | PixVerse V5 - Get task status | `GET /v1/ai/image-to-video/pixverse-v5/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse/get-{task-id}-by-id) |
| 3908 | PixVerse V5 – Image‑to‑Video API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse/overview) |
| 3966 | PixVerse V5 - Create video from image | `POST /v1/ai/image-to-video/pixverse-v5` | [docs](https://docs.magnific.com/api-reference/image-to-video/pixverse/post-pixverse-v5) |
| 3974 | Create video from image - Veo 3.1 | `POST /v1/ai/image-to-video/veo-3-1` | [docs](https://docs.magnific.com/api-reference/image-to-video/post-veo-3-1) |
| 3982 | Create video from image - Veo 3.1 Fast | `POST /v1/ai/image-to-video/veo-3-1-fast` | [docs](https://docs.magnific.com/api-reference/image-to-video/post-veo-3-1-fast) |
| 3990 | Create video from image - Veo 3.1 Lite | `POST /v1/ai/image-to-video/veo-3-1-lite` | [docs](https://docs.magnific.com/api-reference/image-to-video/post-veo-3-1-lite) |
| 3998 | RunWay Gen4 Turbo - Create video from image | `POST /v1/ai/image-to-video/runway-gen4-turbo` | [docs](https://docs.magnific.com/api-reference/image-to-video/runway-gen4-turbo) |
| 4006 | RunWay Gen4 Turbo - List tasks | `GET /v1/ai/image-to-video/runway-gen4-turbo` | [docs](https://docs.magnific.com/api-reference/image-to-video/runway-gen4-turbo-tasks) |
| 4013 | RunWay Gen4 Turbo - Get task status | `GET /v1/ai/image-to-video/runway-gen4-turbo/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/runway-gen4-turbo/task-by-id) |
| 4020 | Veo 3.1 Lite – Image-to-Video API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/veo-3-1-lite/overview) |
| 4130 | Veo 3.1 – Image-to-Video API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/veo-3-1/overview) |
| 4262 | WAN 2.5 1080p - Create video from image | `POST /v1/ai/image-to-video/wan-2-5-i2v-1080p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-5-i2v-1080p) |
| 4270 | WAN 2.5 I2V 1080p - List tasks | `GET /v1/ai/image-to-video/wan-2-5-i2v-1080p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-5-i2v-1080p-tasks) |
| 4278 | WAN 2.5 480p - Create video from image | `POST /v1/ai/image-to-video/wan-2-5-i2v-480p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-5-i2v-480p) |
| 4286 | WAN 2.5 I2V 480p - List tasks | `GET /v1/ai/image-to-video/wan-2-5-i2v-480p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-5-i2v-480p-tasks) |
| 4294 | WAN 2.5 720p - Create video from image | `POST /v1/ai/image-to-video/wan-2-5-i2v-720p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-5-i2v-720p) |
| 4302 | WAN 2.5 I2V 720p - List tasks | `GET /v1/ai/image-to-video/wan-2-5-i2v-720p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-5-i2v-720p-tasks) |
| 4310 | WAN 2.5 I2V 1080p - Get task status | `GET /v1/ai/image-to-video/wan-2-5-i2v-1080p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-5/task-by-id-1080p) |
| 4318 | WAN 2.5 I2V 480p - Get task status | `GET /v1/ai/image-to-video/wan-2-5-i2v-480p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-5/task-by-id-480p) |
| 4326 | WAN 2.5 I2V 720p - Get task status | `GET /v1/ai/image-to-video/wan-2-5-i2v-720p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-5/task-by-id-720p) |
| 4334 | WAN 2.7 - Create video from image | `POST /v1/ai/image-to-video/wan-2-7` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-7/generate) |
| 4353 | WAN 2.7 Image To Video API |  | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-7/overview) |
| 4478 | WAN 2.7 I2V - Get task status | `GET /v1/ai/image-to-video/wan-2-7/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-7/task-by-id) |
| 4486 | WAN 2.7 I2V - List tasks | `GET /v1/ai/image-to-video/wan-2-7` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-2-7/wan-2-7-i2v-tasks) |
| 4494 | WAN 2.2 480p - List tasks | `GET /v1/ai/image-to-video/wan-v2-2-480p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-2-480p/get-wan-v2-2-480p) |
| 4502 | WAN 2.2 480p - Get task status | `GET /v1/ai/image-to-video/wan-v2-2-480p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-2-480p/get-wan-v2-2-480p-task) |
| 4510 | WAN 2.2 480p - Create video from image | `POST /v1/ai/image-to-video/wan-v2-2-480p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-2-480p/post-wan-v2-2-480p) |
| 4518 | WAN 2.2 580p - List tasks | `GET /v1/ai/image-to-video/wan-v2-2-580p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-2-580p/get-wan-v2-2-580p) |
| 4526 | WAN 2.2 580p - Get task status | `GET /v1/ai/image-to-video/wan-v2-2-580p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-2-580p/get-wan-v2-2-580p-task) |
| 4534 | WAN 2.2 580p - Create video from image | `POST /v1/ai/image-to-video/wan-v2-2-580p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-2-580p/post-wan-v2-2-580p) |
| 4542 | WAN 2.2 720p - List tasks | `GET /v1/ai/image-to-video/wan-v2-2-720p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-2-720p/get-wan-v2-2-720p) |
| 4550 | WAN 2.2 720p - Get task status | `GET /v1/ai/image-to-video/wan-v2-2-720p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-2-720p/get-wan-v2-2-720p-task) |
| 4558 | WAN 2.2 720p - Create video from image | `POST /v1/ai/image-to-video/wan-v2-2-720p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-2-720p/post-wan-v2-2-720p) |
| 4566 | WAN 2.6 1080p - Create video from image | `POST /v1/ai/image-to-video/wan-v2-6-1080p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-6-1080p) |
| 4574 | WAN 2.6 I2V 1080p - List tasks | `GET /v1/ai/image-to-video/wan-v2-6-1080p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-6-1080p-tasks) |
| 4582 | WAN 2.6 720p - Create video from image | `POST /v1/ai/image-to-video/wan-v2-6-720p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-6-720p) |
| 4590 | WAN 2.6 I2V 720p - List tasks | `GET /v1/ai/image-to-video/wan-v2-6-720p` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-6-720p-tasks) |
| 4598 | WAN 2.6 I2V 1080p - Get task status | `GET /v1/ai/image-to-video/wan-v2-6-1080p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-6/task-by-id-1080p) |
| 4606 | WAN 2.6 I2V 720p - Get task status | `GET /v1/ai/image-to-video/wan-v2-6-720p/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-to-video/wan-v2-6/task-by-id-720p) |
| 4614 | Upscaler Creative - Get task status | `GET /v1/ai/image-upscaler/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-upscaler-creative/get-image-upscaler) |
| 4622 | Upscaler Creative - List tasks | `GET /v1/ai/image-upscaler` | [docs](https://docs.magnific.com/api-reference/image-upscaler-creative/get-image-upscaler-task) |
| 4630 | Magnific Upscaler Creative API |  | [docs](https://docs.magnific.com/api-reference/image-upscaler-creative/image-upscaler) |
| 4737 | Upscaler Creative - Upscale image | `POST /v1/ai/image-upscaler` | [docs](https://docs.magnific.com/api-reference/image-upscaler-creative/post-image-upscaler) |
| 4751 | Upscaler Precision V2 - List tasks | `GET /v1/ai/image-upscaler-precision-v2` | [docs](https://docs.magnific.com/api-reference/image-upscaler-precision-v2/get-image-upscaler-precision-v2) |
| 4759 | Upscaler Precision V2 - Get task status | `GET /v1/ai/image-upscaler-precision-v2/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-upscaler-precision-v2/get-{task-id}-by-id) |
| 4767 | Upscaler Precision V2 – AI Image Upscaling API |  | [docs](https://docs.magnific.com/api-reference/image-upscaler-precision-v2/overview) |
| 4889 | Upscaler Precision V2 - Upscale image | `POST /v1/ai/image-upscaler-precision-v2` | [docs](https://docs.magnific.com/api-reference/image-upscaler-precision-v2/post-image-upscaler-precision-v2) |
| 4899 | Upscaler Precision - List tasks | `GET /v1/ai/image-upscaler-precision` | [docs](https://docs.magnific.com/api-reference/image-upscaler-precision/get-image-upscaler-precision) |
| 4907 | Upscaler Precision - Get task status | `GET /v1/ai/image-upscaler-precision/{task-id}` | [docs](https://docs.magnific.com/api-reference/image-upscaler-precision/get-{task-id}-by-id) |
| 4915 | Upscaler Precision – High‑Fidelity Super‑Resolution (No Hallucinations) |  | [docs](https://docs.magnific.com/api-reference/image-upscaler-precision/image-upscaler) |
| 5042 | Upscaler Precision - Upscale image | `POST /v1/ai/image-upscaler-precision` | [docs](https://docs.magnific.com/api-reference/image-upscaler-precision/post-image-upscaler-precision) |
| 5052 | Improve Prompt - List tasks | `GET /v1/ai/improve-prompt` | [docs](https://docs.magnific.com/api-reference/improve-prompt/get-improve-prompt) |
| 5060 | Improve Prompt - Get task status | `GET /v1/ai/improve-prompt/{task-id}` | [docs](https://docs.magnific.com/api-reference/improve-prompt/get-{task-id}-by-id) |
| 5068 | Improve Prompt - AI Prompt Enhancement API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/improve-prompt/overview) |
| 5179 | Improve Prompt - Enhance prompt | `POST /v1/ai/improve-prompt` | [docs](https://docs.magnific.com/api-reference/improve-prompt/post-improve-prompt) |
| 5190 | Kling O1 - Get task status | `GET /v1/ai/image-to-video/kling-o1/{task-id}` | [docs](https://docs.magnific.com/api-reference/kling-o1/task-by-id) |
| 5197 | Latent Sync - List tasks | `GET /v1/ai/lip-sync/latent-sync` | [docs](https://docs.magnific.com/api-reference/lip-sync/latent-sync/get-latent-sync) |
| 5205 | Latent Sync - Get task status | `GET /v1/ai/lip-sync/latent-sync/{task-id}` | [docs](https://docs.magnific.com/api-reference/lip-sync/latent-sync/get-{task-id}-by-id) |
| 5213 | Latent Sync – Lip Sync API |  | [docs](https://docs.magnific.com/api-reference/lip-sync/latent-sync/overview) |
| 5281 | Latent Sync - Lip-sync video generation | `POST /v1/ai/lip-sync/latent-sync` | [docs](https://docs.magnific.com/api-reference/lip-sync/latent-sync/post-latent-sync) |
| 5289 | Veed Fabric 1.0 Fast - Generate talking video | `POST /v1/ai/lip-sync/veed-fabric-1-0-fast` | [docs](https://docs.magnific.com/api-reference/lip-sync/veed-fabric-1-0-fast/generate) |
| 5300 | Veed Fabric 1.0 Fast API |  | [docs](https://docs.magnific.com/api-reference/lip-sync/veed-fabric-1-0-fast/overview) |
| 5405 | Veed Fabric 1.0 Fast - Get task status | `GET /v1/ai/lip-sync/veed-fabric-1-0-fast/{task-id}` | [docs](https://docs.magnific.com/api-reference/lip-sync/veed-fabric-1-0-fast/task-by-id) |
| 5413 | Veed Fabric 1.0 Fast - List tasks | `GET /v1/ai/lip-sync/veed-fabric-1-0-fast` | [docs](https://docs.magnific.com/api-reference/lip-sync/veed-fabric-1-0-fast/veed-fabric-1-0-fast-tasks) |
| 5421 | Veed Fabric 1.0 - Generate talking video | `POST /v1/ai/lip-sync/veed-fabric-1-0` | [docs](https://docs.magnific.com/api-reference/lip-sync/veed-fabric-1-0/generate) |
| 5432 | Veed Fabric 1.0 API |  | [docs](https://docs.magnific.com/api-reference/lip-sync/veed-fabric-1-0/overview) |
| 5536 | Veed Fabric 1.0 - Get task status | `GET /v1/ai/lip-sync/veed-fabric-1-0/{task-id}` | [docs](https://docs.magnific.com/api-reference/lip-sync/veed-fabric-1-0/task-by-id) |
| 5544 | Veed Fabric 1.0 - List tasks | `GET /v1/ai/lip-sync/veed-fabric-1-0` | [docs](https://docs.magnific.com/api-reference/lip-sync/veed-fabric-1-0/veed-fabric-1-0-tasks) |
| 5552 | Music Generation - Generate from text | `POST /v1/ai/music-generation` | [docs](https://docs.magnific.com/api-reference/music-generation/generate) |
| 5569 | Google Lyria - Generate music from text | `POST /v1/ai/music-generation/google-lyria` | [docs](https://docs.magnific.com/api-reference/music-generation/google-lyria/generate) |
| 5588 | Google Lyria - List tasks | `GET /v1/ai/music-generation/google-lyria` | [docs](https://docs.magnific.com/api-reference/music-generation/google-lyria/google-lyria-tasks) |
| 5596 | Google Lyria API |  | [docs](https://docs.magnific.com/api-reference/music-generation/google-lyria/overview) |
| 5717 | Google Lyria - Get task status | `GET /v1/ai/music-generation/google-lyria/{task-id}` | [docs](https://docs.magnific.com/api-reference/music-generation/google-lyria/task-by-id) |
| 5725 | Lyria 3 - Generate music from text | `POST /v1/ai/music-generation/lyria-3` | [docs](https://docs.magnific.com/api-reference/music-generation/lyria-3/generate) |
| 5742 | Lyria 3 - List tasks | `GET /v1/ai/music-generation/lyria-3` | [docs](https://docs.magnific.com/api-reference/music-generation/lyria-3/lyria-3-tasks) |
| 5750 | Lyria 3 API |  | [docs](https://docs.magnific.com/api-reference/music-generation/lyria-3/overview) |
| 5877 | Lyria 3 - Get task status | `GET /v1/ai/music-generation/lyria-3/{task-id}` | [docs](https://docs.magnific.com/api-reference/music-generation/lyria-3/task-by-id) |
| 5885 | Music Generation - List tasks | `GET /v1/ai/music-generation` | [docs](https://docs.magnific.com/api-reference/music-generation/music-generation-tasks) |
| 5893 | ElevenLabs Music API |  | [docs](https://docs.magnific.com/api-reference/music-generation/overview) |
| 6013 | Music Generation - Get task status | `GET /v1/ai/music-generation/{task-id}` | [docs](https://docs.magnific.com/api-reference/music-generation/task-by-id) |
| 6021 | Download music | `GET /v1/music/{music-id}/download` | [docs](https://docs.magnific.com/api-reference/music/download-music) |
| 6030 | Get detailed music information by ID | `GET /v1/music/{music-id}` | [docs](https://docs.magnific.com/api-reference/music/get-music-by-id) |
| 6039 | Magnific Music API |  | [docs](https://docs.magnific.com/api-reference/music/overview) |
| 6117 | Search and filter music | `GET /v1/music` | [docs](https://docs.magnific.com/api-reference/music/search-music) |
| 6126 | Get loras | `GET /v1/ai/loras` | [docs](https://docs.magnific.com/api-reference/mystic/get-loras) |
| 6133 | Mystic - List tasks | `GET /v1/ai/mystic` | [docs](https://docs.magnific.com/api-reference/mystic/get-mystic) |
| 6141 | Mystic - Get task status | `GET /v1/ai/mystic/{task-id}` | [docs](https://docs.magnific.com/api-reference/mystic/get-mystic-task) |
| 6149 | Magnific Mystic API |  | [docs](https://docs.magnific.com/api-reference/mystic/mystic) |
| 6256 | LoRAs training for custom characters | `POST /v1/ai/loras/characters` | [docs](https://docs.magnific.com/api-reference/mystic/post-loras-characters) |
| 6267 | Mystic LoRA Styles - Train custom style | `POST /v1/ai/loras/styles` | [docs](https://docs.magnific.com/api-reference/mystic/post-loras-styles) |
| 6278 | Mystic - Create image from text | `POST /v1/ai/mystic` | [docs](https://docs.magnific.com/api-reference/mystic/post-mystic) |
| 6291 | Happy Horse 1.1 - Create video from reference images | `POST /v1/ai/reference-to-video/happy-horse-1-1` | [docs](https://docs.magnific.com/api-reference/reference-to-video/happy-horse-1-1/generate) |
| 6332 | Happy Horse 1.1 R2V - List tasks | `GET /v1/ai/reference-to-video/happy-horse-1-1` | [docs](https://docs.magnific.com/api-reference/reference-to-video/happy-horse-1-1/happy-horse-1-1-r2v-tasks) |
| 6340 | Happy Horse 1.1 Reference To Video API |  | [docs](https://docs.magnific.com/api-reference/reference-to-video/happy-horse-1-1/overview) |
| 6486 | Happy Horse 1.1 R2V - Get task status | `GET /v1/ai/reference-to-video/happy-horse-1-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/reference-to-video/happy-horse-1-1/task-by-id) |
| 6494 | Happy Horse 1.0 - Create video from reference images | `POST /v1/ai/reference-to-video/happy-horse-1` | [docs](https://docs.magnific.com/api-reference/reference-to-video/happy-horse-1/generate) |
| 6515 | Happy Horse 1.0 R2V - List tasks | `GET /v1/ai/reference-to-video/happy-horse-1` | [docs](https://docs.magnific.com/api-reference/reference-to-video/happy-horse-1/happy-horse-1-r2v-tasks) |
| 6523 | Happy Horse 1.0 Reference To Video API |  | [docs](https://docs.magnific.com/api-reference/reference-to-video/happy-horse-1/overview) |
| 6653 | Happy Horse 1.0 R2V - Get task status | `GET /v1/ai/reference-to-video/happy-horse-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/reference-to-video/happy-horse-1/task-by-id) |
| 6661 | Create video with reference images - Veo 3.1 | `POST /v1/ai/reference-to-video/veo-3-1` | [docs](https://docs.magnific.com/api-reference/reference-to-video/veo-3-1/generate) |
| 6669 | Veo 3.1 Reference-to-Video API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/reference-to-video/veo-3-1/overview) |
| 6814 | Get Veo 3.1 Reference-to-Video task by ID | `GET /v1/ai/reference-to-video/veo-3-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/reference-to-video/veo-3-1/task-by-id) |
| 6822 | Get all Veo 3.1 Reference-to-Video tasks | `GET /v1/ai/reference-to-video/veo-3-1` | [docs](https://docs.magnific.com/api-reference/reference-to-video/veo-3-1/veo-3-1-tasks) |
| 6830 | WAN 2.7 - Create video from reference characters | `POST /v1/ai/reference-to-video/wan-2-7` | [docs](https://docs.magnific.com/api-reference/reference-to-video/wan-2-7/generate) |
| 6850 | WAN 2.7 Reference To Video API |  | [docs](https://docs.magnific.com/api-reference/reference-to-video/wan-2-7/overview) |
| 6979 | WAN 2.7 R2V - Get task status | `GET /v1/ai/reference-to-video/wan-2-7/{task-id}` | [docs](https://docs.magnific.com/api-reference/reference-to-video/wan-2-7/task-by-id) |
| 6987 | WAN 2.7 R2V - List tasks | `GET /v1/ai/reference-to-video/wan-2-7` | [docs](https://docs.magnific.com/api-reference/reference-to-video/wan-2-7/wan-2-7-r2v-tasks) |
| 6995 | Remove Background - Image Cutout API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/remove-background/overview) |
| 7109 | Remove the background of an image | `POST /v1/ai/beta/remove-background` | [docs](https://docs.magnific.com/api-reference/remove-background/post-beta-remove-background) |
| 7124 | Download an resource | `GET /v1/resources/{resource-id}/download` | [docs](https://docs.magnific.com/api-reference/resources/download-a-resource) |
| 7132 | Get available download formats for resource | `GET /v1/resources/{resource-id}/download/{resource-format}` | [docs](https://docs.magnific.com/api-reference/resources/download-resource-by-id-and-format) |
| 7140 | Search and filter resources with advanced options | `GET /v1/resources` | [docs](https://docs.magnific.com/api-reference/resources/get-all-resources) |
| 7148 | Get detailed resource information by ID | `GET /v1/resources/{resource-id}` | [docs](https://docs.magnific.com/api-reference/resources/get-the-detail-of-a-resource-psd-vector-or-photo) |
| 7156 | Images and templates API |  | [docs](https://docs.magnific.com/api-reference/resources/images-and-templates-api) |
| 7212 | Stock content API |  | [docs](https://docs.magnific.com/api-reference/resources/stock-content) |
| 7283 | Download a sound effect | `GET /v1/sound-effects/{sfx-id}/download` | [docs](https://docs.magnific.com/api-reference/sfx/download-sfx) |
| 7292 | Get detailed sound effect information by ID | `GET /v1/sound-effects/{sfx-id}` | [docs](https://docs.magnific.com/api-reference/sfx/get-sfx-by-id) |
| 7301 | Magnific Sound Effects API |  | [docs](https://docs.magnific.com/api-reference/sfx/overview) |
| 7412 | Search and filter sound effects | `GET /v1/sound-effects` | [docs](https://docs.magnific.com/api-reference/sfx/search-sfx) |
| 7421 | Skin Enhancer - List tasks | `GET /v1/ai/skin-enhancer` | [docs](https://docs.magnific.com/api-reference/skin-enhancer/get-skin-enhancer) |
| 7428 | Skin Enhancer - Get task status | `GET /v1/ai/skin-enhancer/{task-id}` | [docs](https://docs.magnific.com/api-reference/skin-enhancer/get-{task-id}-by-id) |
| 7435 | Skin Enhancer - AI Portrait Enhancement API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/skin-enhancer/overview) |
| 7575 | Skin Enhancer Creative - Enhance skin | `POST /v1/ai/skin-enhancer/creative` | [docs](https://docs.magnific.com/api-reference/skin-enhancer/post-creative) |
| 7584 | Skin Enhancer Faithful - Enhance skin | `POST /v1/ai/skin-enhancer/faithful` | [docs](https://docs.magnific.com/api-reference/skin-enhancer/post-faithful) |
| 7593 | Skin Enhancer Flexible - Enhance skin | `POST /v1/ai/skin-enhancer/flexible` | [docs](https://docs.magnific.com/api-reference/skin-enhancer/post-flexible) |
| 7602 | Sound Effects - List tasks | `GET /v1/ai/sound-effects` | [docs](https://docs.magnific.com/api-reference/sound-effects/get-sound-effects) |
| 7610 | Sound Effects - Get task status | `GET /v1/ai/sound-effects/{task-id}` | [docs](https://docs.magnific.com/api-reference/sound-effects/get-{task-id}-by-id) |
| 7618 | ElevenLabs Sound Effects - Text-to-Audio API |  | [docs](https://docs.magnific.com/api-reference/sound-effects/overview) |
| 7754 | Sound Effects - Generate from text | `POST /v1/ai/sound-effects` | [docs](https://docs.magnific.com/api-reference/sound-effects/post-sound-effects) |
| 7765 | List Tasks | `GET /v1/ai/text-to-image/flux-2-flex` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-2-flex/flux-2-flex-tasks) |
| 7773 | Create Image | `POST /v1/ai/text-to-image/flux-2-flex` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-2-flex/generate) |
| 7797 | FLUX.2 Flex - Text To Image API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-2-flex/overview) |
| 7926 | Get Task by ID | `GET /v1/ai/text-to-image/flux-2-flex/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-2-flex/task-by-id) |
| 7934 | List Tasks | `GET /v1/ai/text-to-image/flux-2-klein` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-2-klein/flux-2-klein-tasks) |
| 7942 | Create Image | `POST /v1/ai/text-to-image/flux-2-klein` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-2-klein/generate) |
| 7964 | FLUX.2 Klein - Fast Text-to-Image API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-2-klein/overview) |
| 8092 | Get Task by ID | `GET /v1/ai/text-to-image/flux-2-klein/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-2-klein/task-by-id) |
| 8100 | Flux Dev - List tasks | `GET /v1/ai/text-to-image/flux-dev` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-dev/get-flux-dev) |
| 8108 | Flux Dev - Get task status | `GET /v1/ai/text-to-image/flux-dev/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-dev/get-flux-dev-task) |
| 8116 | Flux Dev - Create image from text | `POST /v1/ai/text-to-image/flux-dev` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-dev/post-flux-dev) |
| 8124 | Edit Image | `POST /v1/ai/text-to-image/flux-kontext-max` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-kontext-max/edit-image) |
| 8137 | List Tasks | `GET /v1/ai/text-to-image/flux-kontext-max` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-kontext-max/flux-kontext-max-tasks) |
| 8145 | Flux Kontext Max - Image Editing API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-kontext-max/overview) |
| 8288 | Get Task by ID | `GET /v1/ai/text-to-image/flux-kontext-max/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-kontext-max/task-by-id) |
| 8296 | Flux Kontext Pro - List tasks | `GET /v1/ai/text-to-image/flux-kontext-pro` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-kontext-pro/get-flux-kontext-pro) |
| 8304 | Flux Kontext Pro - Get task status | `GET /v1/ai/text-to-image/flux-kontext-pro/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-kontext-pro/get-flux-kontext-pro-task) |
| 8312 | Flux Kontext Pro – Text-to-Image API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-kontext-pro/overview) |
| 8415 | Flux Kontext Pro - Create image from text | `POST /v1/ai/text-to-image/flux-kontext-pro` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-kontext-pro/post-flux-kontext-pro) |
| 8427 | Flux Pro 1.1 - List tasks | `GET /v1/ai/text-to-image/flux-pro-v1-1` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-pro-v1-1/get-flux-pro-v1-1) |
| 8435 | Flux Pro 1.1 - Get task status | `GET /v1/ai/text-to-image/flux-pro-v1-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-pro-v1-1/get-flux-pro-v1-1-detail) |
| 8443 | Flux Pro 1.1 - Create image from text | `POST /v1/ai/text-to-image/flux-pro-v1-1` | [docs](https://docs.magnific.com/api-reference/text-to-image/flux-pro-v1-1/post-flux-pro-v1-1) |
| 8451 | Flux 2 Pro - List tasks | `GET /v1/ai/text-to-image/flux-2-pro` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-flux-2-pro) |
| 8459 | Flux 2 Pro - Get task status | `GET /v1/ai/text-to-image/flux-2-pro/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-flux-2-pro-task) |
| 8467 | Flux 2 Turbo - List tasks | `GET /v1/ai/text-to-image/flux-2-turbo` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-flux-2-turbo) |
| 8475 | Flux 2 Turbo - Get task status | `GET /v1/ai/text-to-image/flux-2-turbo/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-flux-2-turbo-task) |
| 8483 | Gemini 2.5 Flash - List tasks | `GET /v1/ai/gemini-2-5-flash-image-preview` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-gemini-2-5-flash-image-preview) |
| 8490 | Gemini 2.5 Flash - Get task status | `GET /v1/ai/gemini-2-5-flash-image-preview/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-gemini-2-5-flash-image-preview-task) |
| 8497 | HyperFlux - List tasks | `GET /v1/ai/text-to-image/hyperflux` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-hyperflux) |
| 8504 | Create image from text - Classic fast | `POST /v1/ai/text-to-image` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-image-from-text) |
| 8512 | Imagen 3 - List tasks | `GET /v1/ai/text-to-image/imagen3` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-imagen3) |
| 8521 | Imagen 3 - Get task status | `GET /v1/ai/text-to-image/imagen3/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-imagen3-task) |
| 8530 | Get the status of all Nano Banana Pro tasks | `GET /v1/ai/text-to-image/nano-banana-pro` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-nano-banana-pro) |
| 8538 | Get the status of a Nano Banana Pro task | `GET /v1/ai/text-to-image/nano-banana-pro/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-nano-banana-pro-task) |
| 8546 | Get the status of all RunWay text-to-image tasks | `GET /v1/ai/text-to-image/runway` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-runway) |
| 8554 | Get RunWay text-to-image task by ID | `GET /v1/ai/text-to-image/runway/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-runway-task) |
| 8562 | Seedream 4.5 - List tasks | `GET /v1/ai/text-to-image/seedream-v4-5` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v4-5) |
| 8570 | Seedream 4.5 Edit - List tasks | `GET /v1/ai/text-to-image/seedream-v4-5-edit` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v4-5-edit) |
| 8578 | Seedream 4.5 Edit - Get task status | `GET /v1/ai/text-to-image/seedream-v4-5-edit/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v4-5-edit-task) |
| 8586 | Seedream 4.5 - Get task status | `GET /v1/ai/text-to-image/seedream-v4-5/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v4-5-task) |
| 8594 | Seedream V5 Lite - List tasks | `GET /v1/ai/text-to-image/seedream-v5-lite` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v5-lite) |
| 8602 | Seedream V5 Lite Edit - List tasks | `GET /v1/ai/text-to-image/seedream-v5-lite-edit` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v5-lite-edit) |
| 8610 | Seedream V5 Lite Edit - Get task status | `GET /v1/ai/text-to-image/seedream-v5-lite-edit/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v5-lite-edit-task) |
| 8618 | Seedream V5 Lite - Get task status | `GET /v1/ai/text-to-image/seedream-v5-lite/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v5-lite-task) |
| 8626 | Seedream 5.0 Pro - List tasks | `GET /v1/ai/text-to-image/seedream-v5-pro` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v5-pro) |
| 8634 | Seedream 5.0 Pro Edit - List tasks | `GET /v1/ai/text-to-image/seedream-v5-pro-edit` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v5-pro-edit) |
| 8642 | Seedream 5.0 Pro Edit - Get task status | `GET /v1/ai/text-to-image/seedream-v5-pro-edit/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v5-pro-edit-task) |
| 8650 | Seedream 5.0 Pro - Get task status | `GET /v1/ai/text-to-image/seedream-v5-pro/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-seedream-v5-pro-task) |
| 8658 | Get the status of all Z-Image tasks | `GET /v1/ai/text-to-image/z-image` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-z-image) |
| 8666 | Get the status of a Z-Image task | `GET /v1/ai/text-to-image/z-image/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-z-image-task) |
| 8674 | HyperFlux - Get task status | `GET /v1/ai/text-to-image/hyperflux/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/get-{task-id}-by-id) |
| 8681 | Create Image | `POST /v1/ai/text-to-image/imagen4-fast` | [docs](https://docs.magnific.com/api-reference/text-to-image/imagen4-fast/generate) |
| 8690 | List Tasks | `GET /v1/ai/text-to-image/imagen4-fast` | [docs](https://docs.magnific.com/api-reference/text-to-image/imagen4-fast/imagen4-fast-tasks) |
| 8699 | Get Task by ID | `GET /v1/ai/text-to-image/imagen4-fast/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/imagen4-fast/task-by-id) |
| 8708 | Create Image | `POST /v1/ai/text-to-image/imagen4-ultra` | [docs](https://docs.magnific.com/api-reference/text-to-image/imagen4-ultra/generate) |
| 8717 | List Tasks | `GET /v1/ai/text-to-image/imagen4-ultra` | [docs](https://docs.magnific.com/api-reference/text-to-image/imagen4-ultra/imagen4-ultra-tasks) |
| 8726 | Get Task by ID | `GET /v1/ai/text-to-image/imagen4-ultra/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/imagen4-ultra/task-by-id) |
| 8735 | Imagen 4 API |  | [docs](https://docs.magnific.com/api-reference/text-to-image/imagen4/overview) |
| 8893 | Create Image | `POST /v1/ai/text-to-image/nano-banana-pro-flash` | [docs](https://docs.magnific.com/api-reference/text-to-image/nano-banana-pro-flash/generate) |
| 8914 | List Tasks | `GET /v1/ai/text-to-image/nano-banana-pro-flash` | [docs](https://docs.magnific.com/api-reference/text-to-image/nano-banana-pro-flash/nano-banana-pro-flash-tasks) |
| 8922 | Nano Banana Pro Flash API |  | [docs](https://docs.magnific.com/api-reference/text-to-image/nano-banana-pro-flash/overview) |
| 9030 | Get Task by ID | `GET /v1/ai/text-to-image/nano-banana-pro-flash/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/nano-banana-pro-flash/task-by-id) |
| 9038 | Flux 2 Pro - Create image from text | `POST /v1/ai/text-to-image/flux-2-pro` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-flux-2-pro) |
| 9061 | Flux 2 Turbo - Create image from text | `POST /v1/ai/text-to-image/flux-2-turbo` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-flux-2-turbo) |
| 9084 | Gemini 2.5 Flash - Create or edit image | `POST /v1/ai/gemini-2-5-flash-image-preview` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-gemini-2-5-flash-image-preview) |
| 9093 | HyperFlux - Create image from text | `POST /v1/ai/text-to-image/hyperflux` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-hyperflux) |
| 9102 | Imagen 3 - Create image from text | `POST /v1/ai/text-to-image/imagen3` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-imagen3) |
| 9111 | Create image from text - Nano Banana Pro | `POST /v1/ai/text-to-image/nano-banana-pro` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-nano-banana-pro) |
| 9132 | Create image from text - RunWay | `POST /v1/ai/text-to-image/runway` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-runway) |
| 9152 | Seedream 4.5 - Create image from text | `POST /v1/ai/text-to-image/seedream-v4-5` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-seedream-v4-5) |
| 9173 | Seedream 4.5 - Edit image | `POST /v1/ai/text-to-image/seedream-v4-5-edit` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-seedream-v4-5-edit) |
| 9193 | Seedream V5 Lite - Create image from text | `POST /v1/ai/text-to-image/seedream-v5-lite` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-seedream-v5-lite) |
| 9213 | Seedream V5 Lite - Edit image | `POST /v1/ai/text-to-image/seedream-v5-lite-edit` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-seedream-v5-lite-edit) |
| 9233 | Seedream 5.0 Pro - Create image from text | `POST /v1/ai/text-to-image/seedream-v5-pro` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-seedream-v5-pro) |
| 9254 | Seedream 5.0 Pro - Edit image | `POST /v1/ai/text-to-image/seedream-v5-pro-edit` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-seedream-v5-pro-edit) |
| 9274 | Create image from text - Z-Image | `POST /v1/ai/text-to-image/z-image` | [docs](https://docs.magnific.com/api-reference/text-to-image/post-z-image) |
| 9294 | Flux Reimagine - Transform image | `POST /v1/ai/beta/text-to-image/reimagine-flux` | [docs](https://docs.magnific.com/api-reference/text-to-image/reimagine-flux/post-reimagine-flux) |
| 9302 | Seedream 4 Edit - List tasks | `GET /v1/ai/text-to-image/seedream-v4-edit` | [docs](https://docs.magnific.com/api-reference/text-to-image/seedream-4-edit/get-seedream-v4-edit) |
| 9310 | Seedream 4 Edit - Get task status | `GET /v1/ai/text-to-image/seedream-v4-edit/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/seedream-4-edit/get-seedream-v4-edit-detail) |
| 9318 | Seedream 4 Edit – Image Editing API |  | [docs](https://docs.magnific.com/api-reference/text-to-image/seedream-4-edit/overview) |
| 9377 | Seedream 4 - Edit image | `POST /v1/ai/text-to-image/seedream-v4-edit` | [docs](https://docs.magnific.com/api-reference/text-to-image/seedream-4-edit/post-seedream-v4-edit) |
| 9385 | Seedream 4 - List tasks | `GET /v1/ai/text-to-image/seedream-v4` | [docs](https://docs.magnific.com/api-reference/text-to-image/seedream-4/get-seedream-v4) |
| 9393 | Seedream 4 - Get task status | `GET /v1/ai/text-to-image/seedream-v4/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-image/seedream-4/get-seedream-v4-detail) |
| 9401 | Seedream 4 - Text To Image API |  | [docs](https://docs.magnific.com/api-reference/text-to-image/seedream-4/overview) |
| 9479 | Seedream 4 - Create image from text | `POST /v1/ai/text-to-image/seedream-v4` | [docs](https://docs.magnific.com/api-reference/text-to-image/seedream-4/post-seedream-v4) |
| 9487 | Get all Veo 3.1 T2V tasks | `GET /v1/ai/text-to-video/veo-3-1` | [docs](https://docs.magnific.com/api-reference/text-to-video/get-veo-3-1) |
| 9494 | Get all Veo 3.1 T2V Fast tasks | `GET /v1/ai/text-to-video/veo-3-1-fast` | [docs](https://docs.magnific.com/api-reference/text-to-video/get-veo-3-1-fast) |
| 9501 | Get Veo 3.1 T2V Fast task by ID | `GET /v1/ai/text-to-video/veo-3-1-fast/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/get-veo-3-1-fast-task) |
| 9508 | Get all Veo 3.1 Lite T2V tasks | `GET /v1/ai/text-to-video/veo-3-1-lite` | [docs](https://docs.magnific.com/api-reference/text-to-video/get-veo-3-1-lite) |
| 9515 | Get Veo 3.1 Lite T2V task by ID | `GET /v1/ai/text-to-video/veo-3-1-lite/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/get-veo-3-1-lite-task) |
| 9522 | Get Veo 3.1 T2V task by ID | `GET /v1/ai/text-to-video/veo-3-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/get-veo-3-1-task) |
| 9529 | Happy Horse 1.1 - Create video from text | `POST /v1/ai/text-to-video/happy-horse-1-1` | [docs](https://docs.magnific.com/api-reference/text-to-video/happy-horse-1-1/generate) |
| 9544 | Happy Horse 1.1 T2V - List tasks | `GET /v1/ai/text-to-video/happy-horse-1-1` | [docs](https://docs.magnific.com/api-reference/text-to-video/happy-horse-1-1/happy-horse-1-1-t2v-tasks) |
| 9552 | Happy Horse 1.1 Text To Video API |  | [docs](https://docs.magnific.com/api-reference/text-to-video/happy-horse-1-1/overview) |
| 9666 | Happy Horse 1.1 T2V - Get task status | `GET /v1/ai/text-to-video/happy-horse-1-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/happy-horse-1-1/task-by-id) |
| 9674 | Happy Horse 1.0 - Create video from text | `POST /v1/ai/text-to-video/happy-horse-1` | [docs](https://docs.magnific.com/api-reference/text-to-video/happy-horse-1/generate) |
| 9689 | Happy Horse 1.0 T2V - List tasks | `GET /v1/ai/text-to-video/happy-horse-1` | [docs](https://docs.magnific.com/api-reference/text-to-video/happy-horse-1/happy-horse-1-t2v-tasks) |
| 9697 | Happy Horse 1.0 Text To Video API |  | [docs](https://docs.magnific.com/api-reference/text-to-video/happy-horse-1/overview) |
| 9810 | Happy Horse 1.0 T2V - Get task status | `GET /v1/ai/text-to-video/happy-horse-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/happy-horse-1/task-by-id) |
| 9818 | Kling 3.0 Turbo T2V 1080p - Generate video | `POST /v1/ai/text-to-video/kling-v3-turbo-1080p` | [docs](https://docs.magnific.com/api-reference/text-to-video/kling-v3-turbo/generate-1080p) |
| 9839 | Kling 3.0 Turbo T2V 720p - Generate video | `POST /v1/ai/text-to-video/kling-v3-turbo-720p` | [docs](https://docs.magnific.com/api-reference/text-to-video/kling-v3-turbo/generate-720p) |
| 9860 | Kling 3.0 Turbo API |  | [docs](https://docs.magnific.com/api-reference/text-to-video/kling-v3-turbo/overview) |
| 10043 | Kling 3.0 Turbo T2V - Get task status | `GET /v1/ai/text-to-video/kling-v3-turbo/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/kling-v3-turbo/task-by-id) |
| 10051 | Kling 3.0 Turbo T2V - List tasks | `GET /v1/ai/text-to-video/kling-v3-turbo` | [docs](https://docs.magnific.com/api-reference/text-to-video/kling-v3-turbo/tasks) |
| 10059 | LTX Video 2.0 Fast - Create video from text | `POST /v1/ai/text-to-video/ltx-2-fast` | [docs](https://docs.magnific.com/api-reference/text-to-video/ltx-2-fast) |
| 10074 | LTX Video 2.0 Fast T2V - List tasks | `GET /v1/ai/text-to-video/ltx-2-fast` | [docs](https://docs.magnific.com/api-reference/text-to-video/ltx-2-fast-tasks) |
| 10081 | LTX Video 2.0 Fast T2V - Get task status | `GET /v1/ai/text-to-video/ltx-2-fast/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/ltx-2-fast/task-by-id) |
| 10088 | LTX Video 2.0 Pro - Create video from text | `POST /v1/ai/text-to-video/ltx-2-pro` | [docs](https://docs.magnific.com/api-reference/text-to-video/ltx-2-pro) |
| 10103 | LTX Video 2.0 Pro T2V - List tasks | `GET /v1/ai/text-to-video/ltx-2-pro` | [docs](https://docs.magnific.com/api-reference/text-to-video/ltx-2-pro-tasks) |
| 10110 | LTX Video 2.0 Pro T2V - Get task status | `GET /v1/ai/text-to-video/ltx-2-pro/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/ltx-2-pro/task-by-id) |
| 10117 | PixVerse V5.5 - Create video from text | `POST /v1/ai/text-to-video/pixverse-v5-5` | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v5-5/create) |
| 10132 | PixVerse V5.5 Text to Video API |  | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v5-5/overview) |
| 10236 | PixVerse V5.5 Text-to-Video - List tasks | `GET /v1/ai/text-to-video/pixverse-v5-5` | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v5-5/pixverse-v5-5-tasks) |
| 10244 | PixVerse V5.5 Text-to-Video - Get task status | `GET /v1/ai/text-to-video/pixverse-v5-5/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v5-5/task-by-id) |
| 10251 | PixVerse V5 - Create video from text | `POST /v1/ai/text-to-video/pixverse-v5` | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v5/create) |
| 10259 | PixVerse V5 Text to Video API |  | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v5/overview) |
| 10359 | PixVerse V5 Text-to-Video - List tasks | `GET /v1/ai/text-to-video/pixverse-v5` | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v5/pixverse-v5-tasks) |
| 10367 | PixVerse V5 Text-to-Video - Get task status | `GET /v1/ai/text-to-video/pixverse-v5/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v5/task-by-id) |
| 10374 | PixVerse V6 - Create video from text | `POST /v1/ai/text-to-video/pixverse-v6` | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v6/create) |
| 10389 | PixVerse V6 Text to Video API |  | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v6/overview) |
| 10493 | PixVerse V6 Text-to-Video - List tasks | `GET /v1/ai/text-to-video/pixverse-v6` | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v6/pixverse-v6-tasks) |
| 10501 | PixVerse V6 Text-to-Video - Get task status | `GET /v1/ai/text-to-video/pixverse-v6/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/pixverse-v6/task-by-id) |
| 10508 | Create video from text - Veo 3.1 | `POST /v1/ai/text-to-video/veo-3-1` | [docs](https://docs.magnific.com/api-reference/text-to-video/post-veo-3-1) |
| 10516 | Create video from text - Veo 3.1 Fast | `POST /v1/ai/text-to-video/veo-3-1-fast` | [docs](https://docs.magnific.com/api-reference/text-to-video/post-veo-3-1-fast) |
| 10524 | Create video from text - Veo 3.1 Lite | `POST /v1/ai/text-to-video/veo-3-1-lite` | [docs](https://docs.magnific.com/api-reference/text-to-video/post-veo-3-1-lite) |
| 10532 | Veo 3.1 Lite – Text-to-Video API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/text-to-video/veo-3-1-lite/overview) |
| 10641 | Veo 3.1 – Text-to-Video API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/text-to-video/veo-3-1/overview) |
| 10770 | WAN 2.5 1080p - Create video from text | `POST /v1/ai/text-to-video/wan-2-5-t2v-1080p` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-2-5-t2v-1080p) |
| 10778 | WAN 2.5 T2V 1080p - List tasks | `GET /v1/ai/text-to-video/wan-2-5-t2v-1080p` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-2-5-t2v-1080p-tasks) |
| 10786 | WAN 2.5 480p - Create video from text | `POST /v1/ai/text-to-video/wan-2-5-t2v-480p` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-2-5-t2v-480p) |
| 10794 | WAN 2.5 T2V 480p - List tasks | `GET /v1/ai/text-to-video/wan-2-5-t2v-480p` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-2-5-t2v-480p-tasks) |
| 10802 | WAN 2.5 720p - Create video from text | `POST /v1/ai/text-to-video/wan-2-5-t2v-720p` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-2-5-t2v-720p) |
| 10810 | WAN 2.5 T2V 720p - List tasks | `GET /v1/ai/text-to-video/wan-2-5-t2v-720p` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-2-5-t2v-720p-tasks) |
| 10818 | WAN 2.7 - Create video from text | `POST /v1/ai/text-to-video/wan-2-7` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-2-7/generate) |
| 10834 | WAN 2.7 Text To Video API |  | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-2-7/overview) |
| 10954 | WAN 2.7 T2V - Get task status | `GET /v1/ai/text-to-video/wan-2-7/{task-id}` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-2-7/task-by-id) |
| 10962 | WAN 2.7 T2V - List tasks | `GET /v1/ai/text-to-video/wan-2-7` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-2-7/wan-2-7-t2v-tasks) |
| 10970 | WAN 2.6 1080p - Create video from text | `POST /v1/ai/text-to-video/wan-v2-6-1080p` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-v2-6-1080p) |
| 10978 | WAN 2.6 T2V 1080p - List tasks | `GET /v1/ai/text-to-video/wan-v2-6-1080p` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-v2-6-1080p-tasks) |
| 10986 | WAN 2.6 720p - Create video from text | `POST /v1/ai/text-to-video/wan-v2-6-720p` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-v2-6-720p) |
| 10994 | WAN 2.6 T2V 720p - List tasks | `GET /v1/ai/text-to-video/wan-v2-6-720p` | [docs](https://docs.magnific.com/api-reference/text-to-video/wan-v2-6-720p-tasks) |
| 11002 | Happy Horse 1.0 - Edit video | `POST /v1/ai/video-edit/happy-horse-1` | [docs](https://docs.magnific.com/api-reference/video-edit/happy-horse-1/generate) |
| 11021 | Happy Horse 1.0 Video Edit - List tasks | `GET /v1/ai/video-edit/happy-horse-1` | [docs](https://docs.magnific.com/api-reference/video-edit/happy-horse-1/happy-horse-1-video-edit-tasks) |
| 11029 | Happy Horse 1.0 Video Edit API |  | [docs](https://docs.magnific.com/api-reference/video-edit/happy-horse-1/overview) |
| 11149 | Happy Horse 1.0 Video Edit - Get task status | `GET /v1/ai/video-edit/happy-horse-1/{task-id}` | [docs](https://docs.magnific.com/api-reference/video-edit/happy-horse-1/task-by-id) |
| 11157 | WAN 2.7 - Edit video | `POST /v1/ai/video-edit/wan-2-7` | [docs](https://docs.magnific.com/api-reference/video-edit/wan-2-7/generate) |
| 11177 | WAN 2.7 Video Edit API |  | [docs](https://docs.magnific.com/api-reference/video-edit/wan-2-7/overview) |
| 11300 | WAN 2.7 Video Edit - Get task status | `GET /v1/ai/video-edit/wan-2-7/{task-id}` | [docs](https://docs.magnific.com/api-reference/video-edit/wan-2-7/task-by-id) |
| 11308 | WAN 2.7 Video Edit - List tasks | `GET /v1/ai/video-edit/wan-2-7` | [docs](https://docs.magnific.com/api-reference/video-edit/wan-2-7/wan-2-7-video-edit-tasks) |
| 11316 | Kling 4K I2V - List tasks | `GET /v1/ai/video/kling-4k-i2v` | [docs](https://docs.magnific.com/api-reference/video/get-kling-4k-i2v) |
| 11324 | Kling 4K I2V - Get task status | `GET /v1/ai/video/kling-4k-i2v/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/get-kling-4k-i2v-task) |
| 11332 | Kling 4K T2V - List tasks | `GET /v1/ai/video/kling-4k-t2v` | [docs](https://docs.magnific.com/api-reference/video/get-kling-4k-t2v) |
| 11340 | Kling 4K T2V - Get task status | `GET /v1/ai/video/kling-4k-t2v/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/get-kling-4k-t2v-task) |
| 11348 | Kling 2.6 Pro - Motion control video | `POST /v1/ai/video/kling-v2-6-motion-control-pro` | [docs](https://docs.magnific.com/api-reference/video/kling-v2-6-motion-control-pro) |
| 11356 | Kling 2.6 Standard - Motion control video | `POST /v1/ai/video/kling-v2-6-motion-control-std` | [docs](https://docs.magnific.com/api-reference/video/kling-v2-6-motion-control-std) |
| 11364 | Kling 2.6 Pro - Get task status | `GET /v1/ai/image-to-video/kling-v2-6/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/kling-v2-6-motion-control-task-by-id) |
| 11371 | Kling 2.6 Pro - List tasks | `GET /v1/ai/image-to-video/kling-v2-6` | [docs](https://docs.magnific.com/api-reference/video/kling-v2-6-motion-control-tasks) |
| 11378 | Kling 3 Pro - Motion control video | `POST /v1/ai/video/kling-v3-motion-control-pro` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-motion-control/generate-pro) |
| 11386 | Kling 3 Standard - Motion control video | `POST /v1/ai/video/kling-v3-motion-control-std` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-motion-control/generate-std) |
| 11394 | Kling 3 Motion Control API |  | [docs](https://docs.magnific.com/api-reference/video/kling-v3-motion-control/overview) |
| 11529 | Kling 3 Pro Motion Control - Get task status | `GET /v1/ai/video/kling-v3-motion-control-pro/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-motion-control/pro-task-by-id) |
| 11537 | Kling 3 Pro Motion Control - List tasks | `GET /v1/ai/video/kling-v3-motion-control-pro` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-motion-control/pro-tasks) |
| 11545 | Kling 3 Standard Motion Control - Get task status | `GET /v1/ai/video/kling-v3-motion-control-std/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-motion-control/std-task-by-id) |
| 11553 | Kling 3 Standard Motion Control - List tasks | `GET /v1/ai/video/kling-v3-motion-control-std` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-motion-control/std-tasks) |
| 11561 | Kling 3 Omni Pro - Generate video from text or image | `POST /v1/ai/video/kling-v3-omni-pro` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-omni/generate-pro) |
| 11581 | Kling 3 Omni Pro - Video-to-video generation | `POST /v1/ai/reference-to-video/kling-v3-omni-pro` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-omni/generate-pro-video-reference) |
| 11604 | Kling 3 Omni Standard - Generate video from text or image | `POST /v1/ai/video/kling-v3-omni-std` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-omni/generate-std) |
| 11624 | Kling 3 Omni Standard - Video-to-video generation | `POST /v1/ai/reference-to-video/kling-v3-omni-std` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-omni/generate-std-video-reference) |
| 11647 | Kling 3 Omni - List tasks | `GET /v1/ai/video/kling-v3-omni` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-omni/kling-v3-omni-tasks) |
| 11655 | Kling 3 Omni API |  | [docs](https://docs.magnific.com/api-reference/video/kling-v3-omni/overview) |
| 11813 | Kling 3 Omni - Get task status | `GET /v1/ai/video/kling-v3-omni/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-omni/task-by-id) |
| 11821 | Kling 3 Omni Reference-to-Video - Get task status | `GET /v1/ai/reference-to-video/kling-v3-omni/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-omni/video-reference-task-by-id) |
| 11829 | Kling 3 Omni Reference-to-Video - List tasks | `GET /v1/ai/reference-to-video/kling-v3-omni` | [docs](https://docs.magnific.com/api-reference/video/kling-v3-omni/video-reference-tasks) |
| 11837 | Kling 3 Pro - Generate video | `POST /v1/ai/video/kling-v3-pro` | [docs](https://docs.magnific.com/api-reference/video/kling-v3/generate-pro) |
| 11855 | Kling 3 Standard - Generate video | `POST /v1/ai/video/kling-v3-std` | [docs](https://docs.magnific.com/api-reference/video/kling-v3/generate-std) |
| 11873 | Kling 3 - List tasks | `GET /v1/ai/video/kling-v3` | [docs](https://docs.magnific.com/api-reference/video/kling-v3/kling-v3-tasks) |
| 11881 | Kling 3 API |  | [docs](https://docs.magnific.com/api-reference/video/kling-v3/overview) |
| 12026 | Kling 3 - Get task status | `GET /v1/ai/video/kling-v3/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/kling-v3/task-by-id) |
| 12034 | OmniHuman 1.5 - Create human animation | `POST /v1/ai/video/omni-human-1-5` | [docs](https://docs.magnific.com/api-reference/video/omni-human-1-5) |
| 12042 | OmniHuman 1.5 - List tasks | `GET /v1/ai/video/omni-human-1-5` | [docs](https://docs.magnific.com/api-reference/video/omni-human-1-5-tasks) |
| 12049 | OmniHuman 1.5 - Get task status | `GET /v1/ai/video/omni-human-1-5/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/omni-human-1-5/task-by-id) |
| 12056 | Kling 4K I2V - Generate video from image | `POST /v1/ai/video/kling-4k-i2v` | [docs](https://docs.magnific.com/api-reference/video/post-kling-4k-i2v) |
| 12073 | Kling 4K T2V - Generate video from text | `POST /v1/ai/video/kling-4k-t2v` | [docs](https://docs.magnific.com/api-reference/video/post-kling-4k-t2v) |
| 12089 | RunWay Act Two Character Performance | `POST /v1/ai/video/runway-act-two` | [docs](https://docs.magnific.com/api-reference/video/runway-act-two) |
| 12097 | RunWay Act Two - List tasks | `GET /v1/ai/video/runway-act-two` | [docs](https://docs.magnific.com/api-reference/video/runway-act-two-tasks) |
| 12104 | RunWay Act Two - Get task status | `GET /v1/ai/video/runway-act-two/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/runway-act-two/task-by-id) |
| 12111 | Create video from image - RunWay Gen 4.5 | `POST /v1/ai/image-to-video/runway-4-5` | [docs](https://docs.magnific.com/api-reference/video/runway-gen-4-5/generate-i2v) |
| 12136 | Create video from text - RunWay Gen 4.5 | `POST /v1/ai/text-to-video/runway-4-5` | [docs](https://docs.magnific.com/api-reference/video/runway-gen-4-5/generate-t2v) |
| 12160 | Runway Gen 4.5 API |  | [docs](https://docs.magnific.com/api-reference/video/runway-gen-4-5/overview) |
| 12293 | RunWay Gen 4.5 I2V - List tasks | `GET /v1/ai/image-to-video/runway-4-5` | [docs](https://docs.magnific.com/api-reference/video/runway-gen-4-5/runway-4-5-i2v-tasks) |
| 12301 | RunWay Gen 4.5 T2V - List tasks | `GET /v1/ai/text-to-video/runway-4-5` | [docs](https://docs.magnific.com/api-reference/video/runway-gen-4-5/runway-4-5-t2v-tasks) |
| 12309 | RunWay Gen 4.5 I2V - Get task status | `GET /v1/ai/image-to-video/runway-4-5/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/runway-gen-4-5/task-by-id-i2v) |
| 12317 | RunWay Gen 4.5 T2V - Get task status | `GET /v1/ai/text-to-video/runway-4-5/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/runway-gen-4-5/task-by-id-t2v) |
| 12325 | Seedance 2.0 Fast 480p - Create video from text or image | `POST /v1/ai/video/seedance-2-fast-480p` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-fast/generate-480p) |
| 12333 | Seedance 2.0 Fast 720p - Create video from text or image | `POST /v1/ai/video/seedance-2-fast-720p` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-fast/generate-720p) |
| 12341 | Seedance 2.0 Fast API |  | [docs](https://docs.magnific.com/api-reference/video/seedance-2-fast/overview) |
| 12503 | Seedance 2.0 Fast - Get task status | `GET /v1/ai/video/seedance-2-fast/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-fast/task-by-id) |
| 12510 | Seedance 2.0 Fast - List all tasks | `GET /v1/ai/video/seedance-2-fast` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-fast/tasks) |
| 12517 | Seedance 2.0 Mini 480p - Create video from text or image | `POST /v1/ai/video/seedance-2-mini-480p` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-mini/generate-480p) |
| 12525 | Seedance 2.0 Mini 720p - Create video from text or image | `POST /v1/ai/video/seedance-2-mini-720p` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-mini/generate-720p) |
| 12533 | Seedance 2.0 Mini API |  | [docs](https://docs.magnific.com/api-reference/video/seedance-2-mini/overview) |
| 12691 | Seedance 2.0 Mini - Get task status | `GET /v1/ai/video/seedance-2-mini/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-mini/task-by-id) |
| 12698 | Seedance 2.0 Mini - List all tasks | `GET /v1/ai/video/seedance-2-mini` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-mini/tasks) |
| 12705 | Seedance 2.0 Pro 1080p - Create video from text or image | `POST /v1/ai/video/seedance-2-pro-1080p` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-pro/generate-1080p) |
| 12713 | Seedance 2.0 Pro 480p - Create video from text or image | `POST /v1/ai/video/seedance-2-pro-480p` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-pro/generate-480p) |
| 12721 | Seedance 2.0 Pro 4K - Create video from text or image | `POST /v1/ai/video/seedance-2-pro-4k` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-pro/generate-4k) |
| 12729 | Seedance 2.0 Pro 720p - Create video from text or image | `POST /v1/ai/video/seedance-2-pro-720p` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-pro/generate-720p) |
| 12737 | Seedance 2.0 Pro API |  | [docs](https://docs.magnific.com/api-reference/video/seedance-2-pro/overview) |
| 12904 | Seedance 2.0 Pro - Get task status | `GET /v1/ai/video/seedance-2-pro/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-pro/task-by-id) |
| 12911 | Seedance 2.0 Pro - List all tasks | `GET /v1/ai/video/seedance-2-pro` | [docs](https://docs.magnific.com/api-reference/video/seedance-2-pro/tasks) |
| 12918 | VFX - Apply visual effects to video | `POST /v1/ai/video/vfx` | [docs](https://docs.magnific.com/api-reference/video/vfx/apply-effects) |
| 12939 | VFX – Video Visual Effects API \| Magnific API |  | [docs](https://docs.magnific.com/api-reference/video/vfx/overview) |
| 13059 | VFX - Get task status | `GET /v1/ai/video/vfx/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/vfx/task-by-id) |
| 13067 | VFX - List tasks | `GET /v1/ai/video/vfx` | [docs](https://docs.magnific.com/api-reference/video/vfx/vfx-tasks) |
| 13075 | Video Upscaler Precision API |  | [docs](https://docs.magnific.com/api-reference/video/video-upscaler-precision/overview) |
| 13182 | Video Upscaler Precision - Get task status | `GET /v1/ai/video-upscaler-precision/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/video-upscaler-precision/task-by-id) |
| 13190 | Video Upscaler Precision - Upscale video | `POST /v1/ai/video-upscaler-precision` | [docs](https://docs.magnific.com/api-reference/video/video-upscaler-precision/upscale-video) |
| 13201 | Video Upscaler Precision - List tasks | `GET /v1/ai/video-upscaler-precision` | [docs](https://docs.magnific.com/api-reference/video/video-upscaler-precision/video-upscaler-precision-tasks) |
| 13209 | AI Video Upscaling - Magnific API |  | [docs](https://docs.magnific.com/api-reference/video/video-upscaler/overview) |
| 13370 | Video Upscaler - Get task status | `GET /v1/ai/video-upscaler/{task-id}` | [docs](https://docs.magnific.com/api-reference/video/video-upscaler/task-by-id) |
| 13378 | Video Upscaler - Upscale video | `POST /v1/ai/video-upscaler` | [docs](https://docs.magnific.com/api-reference/video/video-upscaler/upscale-video) |
| 13388 | Video Upscaler Turbo - Upscale video | `POST /v1/ai/video-upscaler/turbo` | [docs](https://docs.magnific.com/api-reference/video/video-upscaler/upscale-video-turbo) |
| 13399 | Video Upscaler - List tasks | `GET /v1/ai/video-upscaler` | [docs](https://docs.magnific.com/api-reference/video/video-upscaler/video-upscaler-tasks) |
| 13407 | Download a video by option id. | `GET /v1/videos/{id}/options/{option-id}/download` | [docs](https://docs.magnific.com/api-reference/videos/download-an-option-video) |
| 13414 | Download a video by ID. | `GET /v1/videos/{id}/download` | [docs](https://docs.magnific.com/api-reference/videos/download-an-video) |
| 13421 | Search and filter videos by specified order | `GET /v1/videos` | [docs](https://docs.magnific.com/api-reference/videos/get-all-videos-by-order) |
| 13428 | Get detailed video information by ID | `GET /v1/videos/{id}` | [docs](https://docs.magnific.com/api-reference/videos/get-one-video-by-id) |
| 13435 | Videos API |  | [docs](https://docs.magnific.com/api-reference/videos/videos-api) |
| 13487 | Voiceover - Generate speech from text | `POST /v1/ai/voiceover/elevenlabs-turbo-v2-5` | [docs](https://docs.magnific.com/api-reference/voiceover/generate) |
| 13499 | ElevenLabs Voiceover - Text-to-Speech API |  | [docs](https://docs.magnific.com/api-reference/voiceover/overview) |
| 13611 | Voiceover - Get task status | `GET /v1/ai/voiceover/elevenlabs-turbo-v2-5/{task-id}` | [docs](https://docs.magnific.com/api-reference/voiceover/task-by-id) |
| 13619 | Voiceover - List tasks | `GET /v1/ai/voiceover/elevenlabs-turbo-v2-5` | [docs](https://docs.magnific.com/api-reference/voiceover/voiceover-tasks) |
| 13627 | WAN 2.5 Text-to-Video API |  | [docs](https://docs.magnific.com/api-reference/wan-2-5-t2v/overview) |
| 13782 | WAN 2.5 T2V 1080p - Get task status | `GET /v1/ai/text-to-video/wan-2-5-t2v-1080p/{task-id}` | [docs](https://docs.magnific.com/api-reference/wan-2-5-t2v/task-by-id-1080p) |
| 13790 | WAN 2.5 T2V 480p - Get task status | `GET /v1/ai/text-to-video/wan-2-5-t2v-480p/{task-id}` | [docs](https://docs.magnific.com/api-reference/wan-2-5-t2v/task-by-id-480p) |
| 13798 | WAN 2.5 T2V 720p - Get task status | `GET /v1/ai/text-to-video/wan-2-5-t2v-720p/{task-id}` | [docs](https://docs.magnific.com/api-reference/wan-2-5-t2v/task-by-id-720p) |
| 13806 | WAN 2.6 Video – Image-to-Video & Text-to-Video API |  | [docs](https://docs.magnific.com/api-reference/wan-v2-6-i2v/overview) |
| 13980 | WAN 2.6 T2V 1080p - Get task status | `GET /v1/ai/text-to-video/wan-v2-6-1080p/{task-id}` | [docs](https://docs.magnific.com/api-reference/wan-v2-6-t2v/task-by-id-1080p) |
| 13988 | WAN 2.6 T2V 720p - Get task status | `GET /v1/ai/text-to-video/wan-v2-6-720p/{task-id}` | [docs](https://docs.magnific.com/api-reference/wan-v2-6-t2v/task-by-id-720p) |
| 13996 | Authentication |  | [docs](https://docs.magnific.com/authentication) |
| 14065 | Changelog |  | [docs](https://docs.magnific.com/changelog/2024) |
| 14111 | Changelog |  | [docs](https://docs.magnific.com/changelog/2025) |
| 14299 | Changelog |  | [docs](https://docs.magnific.com/changelog/2026) |
| 14884 | Welcome to Magnific API |  | [docs](https://docs.magnific.com/introduction) |
| 14970 | Magnific MCP |  | [docs](https://docs.magnific.com/modelcontextprotocol) |
| 15180 | Pricing |  | [docs](https://docs.magnific.com/pricing) |
| 15211 | Quickstart |  | [docs](https://docs.magnific.com/quickstart) |
| 15245 | Rate limiting |  | [docs](https://docs.magnific.com/ratelimits) |
| 15301 | Upload files |  | [docs](https://docs.magnific.com/upload-files) |
| 15467 | Webhooks |  | [docs](https://docs.magnific.com/webhooks) |
