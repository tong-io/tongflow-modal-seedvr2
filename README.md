# tongflow-modal-seedvr2

Official [TongFlow](https://github.com/tong-io/tongflow) plugin. Image and video super-resolution with **SeedVR2** (`ByteDance-Seed/SeedVR2-3B` by default, `SeedVR2-7B` via `SEEDVR2_MODEL_SIZE=7b`), running on a GPU via [Modal](https://modal.com).

## Capabilities

- **Image upscaling** (`image-upscale`) — enlarge an image for sharper detail.
- **Video upscaling** (`video-upscale`) — render a higher-resolution version of a video.

## Credentials

Add in TongFlow **Settings** (gear icon, top-right):

| Key | Required | Notes |
| --- | --- | --- |
| `MODAL_TOKEN_ID` | ✅ | Create at [modal.com/settings/tokens](https://modal.com/settings/tokens). |
| `MODAL_TOKEN_SECRET` | ✅ | Paired with `MODAL_TOKEN_ID`. |
| `HF_TOKEN` | Optional | Only helps avoid Hugging Face rate limits; SeedVR2 weights are public. |

On first use the plugin deploys to your Modal account automatically and caches the build. If set in Settings, `HF_TOKEN` is injected into the Modal download job at deploy time — no manual `modal secret create` needed.
