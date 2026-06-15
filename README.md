# tongflow-modal-seedvr2

Official TongFlow plugin. Image and video super-resolution with **SeedVR2** (`ByteDance-Seed/SeedVR2-3B` by default, `SeedVR2-7B` via `SEEDVR2_MODEL_SIZE=7b`), running on a GPU via [Modal](https://modal.com).

## Capabilities

- **Image upscaling** (`image-upscale`) — enlarge an image for sharper detail.
- **Video upscaling** (`video-upscale`) — render a higher-resolution version of a video.

## Credentials

Add in TongFlow **Settings** (gear icon, top-right):

| Key | Required | Notes |
| --- | --- | --- |
| `MODAL_TOKEN_ID` | ✅ | Create at [modal.com/settings/tokens](https://modal.com/settings/tokens). |
| `MODAL_TOKEN_SECRET` | ✅ | Paired with `MODAL_TOKEN_ID`. |

On first use the plugin deploys to your Modal account automatically and caches the build. The SeedVR2 weights are public; an `HF_TOKEN` (via Modal secret `huggingface`) is optional and only helps avoid Hugging Face rate limits.
