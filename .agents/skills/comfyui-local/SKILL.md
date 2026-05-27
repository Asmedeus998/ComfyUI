---
name: comfyui-local
description: Convert ComfyUI workflows from comfy_api_nodes (cloud/third-party engine nodes like GeminiImage2Node, KlingOmniProImageToVideoNode, ByteDance2TextToVideoNode) to local custom nodes that call APIs directly with user's own keys (GoogleGeminiDirect, ElevenLabsDirectTTS, FALSeedanceText2Video, GrokImageEditDirect, KimiCliDirect, etc.). Use when the user wants to remove ComfyUI cloud API dependencies, convert .app.json or regular workflows to use local API nodes, replace cloud nodes with local equivalents, or make workflows run without ComfyUI account/proxy.
---

# ComfyUI Local API Workflow Converter

Replace ComfyUI's built-in `comfy_api_nodes` (cloud API nodes that require ComfyUI account/proxy) with `local_api` custom nodes that call external APIs directly using the user's own API keys.

## User Preferences (CRITICAL)

1. **Always create NEW files** — never overwrite original workflows. Save converted workflows with `_local.json` suffix (e.g., `workflow.json` → `workflow_local.json`).
2. **Apply to ALL requested workflows** — do not just test on one file. Convert every workflow the user mentions.
3. **GoogleGeminiDirect supports IMAGE output** — preserve all image output links when converting. The node returns both `STRING` and `IMAGE`.
4. **App mode workflows** — if the source was `.app.json`, also set `extra.linearMode = false` in the converted JSON so it opens in node graph mode.
5. **Proactive execution** — do not ask for confirmation on every file. Just do it and report results.

## Quick Reference

### Supported Cloud → Local Mappings

| Cloud Node | Local Replacement | Details |
|-----------|-------------------|---------|
| `OpenAIGPTImage1` | `OpenAIGPTImageDirect` | → [node-mapping.md](./references/node-mapping.md#openaigptimagedirect-from-comfyui-local-gemini) |
| `OpenAIGPTImageNodeV2` | `OpenAIGPTImageDirect` | → [node-mapping.md](./references/node-mapping.md#openaigptimagedirect-from-comfyui-local-gemini) |
| `GeminiImage2Node` | `GoogleGeminiDirect` | → [node-mapping.md](./references/node-mapping.md#googlegeminidirect-from-comfyui-local-gemini) |
| `GeminiNanoBanana2` | `GoogleGeminiDirect` | → [node-mapping.md](./references/node-mapping.md#googlegeminidirect-from-comfyui-local-gemini) |
| `KlingOmniProImageToVideoNode` | `FALKlingOmniVideo` | → [node-mapping.md](./references/node-mapping.md#falklingomnivideo-from-comfyui-local-gemini) |
| `ByteDance2TextToVideoNode` | `FALSeedanceText2Video` | → [node-mapping.md](./references/node-mapping.md#falseedancetext2video-from-comfyui-local-gemini) |
| `ByteDance2FirstLastFrameNode` | `FALSeedanceImage2Video` | → [node-mapping.md](./references/node-mapping.md#falseedanceimage2video-from-comfyui-local-gemini) |
| `ByteDance2ReferenceNode` | `FALSeedanceReference2Video` | → [node-mapping.md](./references/node-mapping.md#falseedancereference2video-from-comfyui-local-gemini) |

### Conversion Topics

| Topic | File |
|-------|------|
| Widget mapping, subgraph handling, JSON examples | → [conversion-mechanics.md](./references/conversion-mechanics.md) |
| Real-human workflows, asset chain cleanup, fast endpoints | → [real-human-workflows.md](./references/real-human-workflows.md) |
| Full input/output/widget index tables for all nodes | → [node-mapping.md](./references/node-mapping.md) |

## Environment Variables for API Keys

Local API nodes support env vars so keys are not saved in workflow JSON:
- `OPENAI_API_KEY` → used by `OpenAIGPTImageDirect`
- `GOOGLE_GEMINI_API_KEY` → used by `GoogleGeminiDirect`
- `ELEVENLABS_API_KEY` → used by `ElevenLabsDirectTTS`
- `FAL_KEY` → used by `FALKlingImage2Video`, `FALKlingOmniVideo`, and all `FALSeedance*` nodes
- `XAI_API_KEY` → used by `GrokImageEditDirect`, `GrokVideoDirect`, `GrokVideoReferenceDirect`, `GrokVideoExtendDirect`
- `Kimi CLI` → uses existing `kimi-cli` auth (no env var needed; runs `kimi --print` subprocess)

Always leave the `api_key` widget empty in the workflow when using env vars.

## Newer Local Nodes (Not Cloud Replacements)

These nodes do NOT have comfy_api_nodes equivalents — they are unique local capabilities:

| Node | Category | What It Does |
|------|----------|--------------|
| `GrokImageEditDirect` | `local_api/grok` | xAI Grok image editing (`grok-imagine-image`, `grok-imagine-image-pro`, `grok-imagine-image-quality`). Supports `images` batched input + `image_1`..`image_3`. |
| `GrokVideoDirect` | `local_api/grok` | xAI Grok video generation (`grok-imagine-video`). Single image-to-video. |
| `GrokVideoReferenceDirect` | `local_api/grok` | xAI Grok video with up to 7 reference images. |
| `GrokVideoExtendDirect` | `local_api/grok` | xAI Grok video extension (continues existing video). |
| `FALSeedreamImageDirect` | `local_api/fal_seedream` | FAL Seedream image generation + editing. Supports `images` batched input + `image_1`..`image_9`. |
| `KimiCliDirect` | `local_api/kimi` | **Subprocess-based** kimi-cli integration. Text/image/video prompts using user's existing kimi auth. Supports `images` batched input + up to 4 video inputs (`video`, `video_1`, `video_2`, `video_3`). Returns `response` + `thinking`. |
| `BatchImagePreview` | `local_api/utils` | Draws index numbers on each image in a batched tensor. Output connected to `PreviewImage` or `SaveImage` for individual numbered files. |
| `BatchImageSelect` | `local_api/utils` | Selects specific indices from a batched IMAGE tensor (e.g. `"2,4"` returns images 2 and 4). |

### Batched `images` Input Pattern

All image-capable API nodes now support a batched `images` (IMAGE) input **alongside** numbered `image_1`..`image_N` inputs:

```
Batch Images.IMAGE ──► API Node.images
                 └──► API Node.image_1  (optional, for mixing)
```

- `images` accepts a 4-D tensor `(B, H, W, C)` from ComfyUI batch nodes
- The node unrolls the batch first, then appends any individual `image_N` inputs
- Use `BatchImagePreview` to verify batch order before sending to API
- Use `BatchImageSelect` to pick specific indices (e.g. only image 2 and 5)

**Image limits:**
- `GoogleGeminiDirect`: up to 14 total
- `GrokImageEditDirect`: up to 3
- `OpenAIGPTImageDirect`: up to 4
- `FALSeedreamImageDirect`: up to 9
- `FALKlingOmniVideo`: up to 9
- `GrokVideoReferenceDirect`: up to 7
- `GrokVideoDirect`: 1 only

## How to Identify comfy_api_nodes

`comfy_api_nodes` live in `/home/yumeko/github/ComfyUI/comfy_api_nodes/` and are distributed with ComfyUI. They call ComfyUI's proxy endpoints (e.g., `/proxy/vertexai/gemini/...`, `/proxy/kling/...`).

Local custom nodes live in `/home/yumeko/github/ComfyUI/custom_nodes/` and are installed separately.

**Important:** `comfyui-local-gemini` is a **separate git repository** (`custom_nodes/comfyui-local-gemini/`) with its own remote. Changes to its `nodes.py` must be committed and pushed independently from the main ComfyUI repo. The main repo's `custom_nodes/` directory is gitignored, so changes there do not appear in the main ComfyUI commit.

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/convert_gemini_nodes.py` | Auto-convert Gemini-related comfy_api_nodes to `GoogleGeminiDirect` |
| `scripts/convert_openai_nodes.py` | Auto-convert OpenAI GPT Image comfy_api_nodes to `OpenAIGPTImageDirect` |
| `scripts/convert_seedance_to_local.py` | Auto-convert ByteDance Seedance 2.0 comfy_api_nodes to local FAL equivalents |
