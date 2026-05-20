---
name: comfyui-local
description: Convert ComfyUI workflows from comfy_api_nodes (cloud/third-party engine nodes like GeminiImage2Node, KlingOmniProImageToVideoNode) to local custom nodes that call APIs directly with user's own keys (GoogleGeminiDirect, ElevenLabsDirectTTS, etc.). Use when the user wants to remove ComfyUI cloud API dependencies, convert .app.json or regular workflows to use local API nodes, replace GeminiImage2Node/GeminiNanoBanana2/KlingOmniProImageToVideoNode with local equivalents, or make workflows run without ComfyUI account/proxy.
---

# ComfyUI Local API Workflow Converter

## Goal

Replace ComfyUI's built-in `comfy_api_nodes` (cloud API nodes that require ComfyUI account/proxy) with `local_api` custom nodes that call external APIs directly using the user's own API keys.

## User Preferences (CRITICAL)

1. **Always create NEW files** — never overwrite original workflows. Save converted workflows with `_local.json` suffix (e.g., `workflow.json` → `workflow_local.json`).
2. **Apply to ALL requested workflows** — do not just test on one file. Convert every workflow the user mentions.
3. **GoogleGeminiDirect supports IMAGE output** — preserve all image output links when converting. The node returns both `STRING` and `IMAGE`.
4. **App mode workflows** — if the source was `.app.json`, also set `extra.linearMode = false` in the converted JSON so it opens in node graph mode.
5. **Proactive execution** — do not ask for confirmation on every file. Just do it and report results.

## How to Identify comfy_api_nodes

`comfy_api_nodes` live in `/home/yumeko/github/ComfyUI/comfy_api_nodes/` and are distributed with ComfyUI. They call ComfyUI's proxy endpoints (e.g., `/proxy/vertexai/gemini/...`, `/proxy/kling/...`).

Common `comfy_api_nodes` to replace:
- `GeminiImage2Node`
- `GeminiNanoBanana2`
- `GeminiNanoBanana2V2`
- `KlingOmniProImageToVideoNode`

Local custom nodes live in `/home/yumeko/github/ComfyUI/custom_nodes/` and are installed separately. Currently available local API nodes:
- `comfyui-local-gemini` → `GoogleGeminiDirect`
- `comfyui-local-gemini` → `ElevenLabsDirectTTS`, `ElevenLabsDirectVoiceSelector`

## Node Mapping

| comfy_api_nodes (remove) | local_api replacement | Notes |
|--------------------------|----------------------|-------|
| `GeminiImage2Node` | `GoogleGeminiDirect` | Maps `prompt`→`prompt`, `images`→`images`. Preserves **both** STRING and IMAGE outputs. See `references/node-mapping.md` for full widget index mapping. |
| `GeminiNanoBanana2` | `GoogleGeminiDirect` | Same as above. `thinking_level` is dropped (not supported in direct API). Merges multiple IMAGE outputs into the single `image` output. |
| `GeminiNanoBanana2V2` | `GoogleGeminiDirect` | Same as above. |
| `KlingOmniProImageToVideoNode` | **No direct local equivalent installed** | Options: (1) Use LTX-2.3 local video generation subgraph (see example workflow), (2) Build a custom direct-API node for Kling, (3) Keep as cloud node if local replacement is not required. |

## Conversion Steps

1. **Load the workflow JSON** and list all node types.
2. **Identify `comfy_api_nodes`** using the mapping table above.
3. **Replace each node** in the JSON:
   - Change `type` from the old node ID to the new local node ID.
   - Update `inputs` to match the local node's signature (names and types).
   - Update `widgets_values` to match the local node's widget order. **IMPORTANT:** The original nodes have `control_after_generate` on `seed`, which adds a hidden widget value. The conversion script handles this automatically.
   - Update `outputs` — **preserve all IMAGE links** by merging them into the single `image` output.
4. **Preserve links** by keeping the same `link` IDs on connections that still exist.
5. **Add API key widgets** if the local node requires them. Leave them empty and instruct the user to set env vars (`GOOGLE_GEMINI_API_KEY`, `ELEVENLABS_API_KEY`).
6. **If source was `.app.json`**, set `"linearMode": false` in `extra`.
7. **Save as NEW file** with `_local.json` suffix. Never overwrite the original.
8. **Apply to ALL files** the user mentions.

## Environment Variables for API Keys

Local API nodes support env vars so keys are not saved in workflow JSON:
- `GOOGLE_GEMINI_API_KEY` → used by `GoogleGeminiDirect`
- `ELEVENLABS_API_KEY` → used by `ElevenLabsDirectTTS`

Always leave the `api_key` widget empty in the workflow when using env vars.

## Handling Missing comfy-core Subgraphs & Nodes

Some workflows contain **subgraphs** (UUID-typed nodes like `68c58c16-e698-45a4-97f9-54ae8eb9dee9`) or other comfy-core nodes that may not exist in the local environment.

**DO NOT assume missing nodes are simple duplicators.** Always inspect the subgraph definition in `definitions.subgraphs` inside the workflow JSON.

### Common Pattern: "Crop Images" Subgraph

A frequent comfy-core subgraph is **"Crop Images"**, which takes a single image (e.g., a 2×2 grid from Gemini) and outputs 4 cropped quadrants. It internally uses:
- `GetImageSize` → gets original dimensions
- `SimpleMath+` → calculates `width / 2` and `height / 2`
- `ImageCrop+` → 4 instances with positions: `top-left`, `top-right`, `bottom-left`, `bottom-right`

If this subgraph is missing, flatten it by creating the individual nodes directly in the main workflow and rewiring the 4 outputs to the respective `SaveImage` nodes.

### Other Missing Nodes to Watch For

| Missing Node | What It Actually Does | Local Replacement |
|--------------|----------------------|-------------------|
| `PrimitiveNode` (comfy-core) | Provides shared widget values to multiple nodes | Remove if the target nodes already have correct `widgets_values`; otherwise use `PrimitiveStringMultiline` |
| UUID subgraphs | Varies — inspect `definitions.subgraphs` | Flatten into individual nodes |

## Workflow JSON Structure Differences

- `comfy_api_nodes` use `IO.Schema` definitions with camelCase input names like `aspect_ratio`, `response_modalities`.
- Local custom nodes use standard ComfyUI `INPUT_TYPES` with lowercase names like `prompt`, `images`, `model`.
- The `extra` metadata (`linearMode`, `linearData`) should be preserved or adjusted based on the user's preference (see `comfyui-workflow-builder` skill if needed).
- **Hidden widgets:** `GoogleGeminiDirect` has a hidden `seed_control` widget at `widgets_values[4]` (auto-generated by `control_after_generate`). When manually constructing a prompt for the `/prompt` API, skip this index — it does not map to any input.

## Example: GeminiImage2Node → GoogleGeminiDirect

### Before (comfy_api_node)
```json
{
  "type": "GeminiImage2Node",
  "inputs": [
    {"name": "images", "type": "IMAGE", "link": 101},
    {"name": "files", "type": "GEMINI_INPUT_FILES", "link": null},
    {"name": "prompt", "type": "STRING", "widget": {"name": "prompt"}, "link": 100},
    {"name": "model", "type": "COMBO", "widget": {"name": "model"}, "link": null},
    {"name": "seed", "type": "INT", "widget": {"name": "seed"}, "link": null},
    {"name": "aspect_ratio", "type": "COMBO", "widget": {"name": "aspect_ratio"}, "link": null},
    {"name": "resolution", "type": "COMBO", "widget": {"name": "resolution"}, "link": null},
    {"name": "response_modalities", "type": "COMBO", "widget": {"name": "response_modalities"}, "link": null},
    {"name": "system_prompt", "type": "STRING", "widget": {"name": "system_prompt"}, "link": null}
  ],
  "outputs": [
    {"name": "IMAGE", "type": "IMAGE", "links": [200]},
    {"name": "STRING", "type": "STRING", "links": [201]}
  ],
  "widgets_values": ["prompt text", "gemini-3-pro-image-preview", 42, "randomize", "auto", "1K", "IMAGE+TEXT", "You are an expert..."]
}
```

### After (local_api)
```json
{
  "type": "GoogleGeminiDirect",
  "inputs": [
    {"name": "api_key", "type": "STRING", "widget": {"name": "api_key"}, "link": null},
    {"name": "prompt", "type": "STRING", "widget": {"name": "prompt"}, "link": 100},
    {"name": "model", "type": "COMBO", "widget": {"name": "model"}, "link": null},
    {"name": "seed", "type": "INT", "widget": {"name": "seed"}, "link": null},
    {"name": "aspect_ratio", "type": "COMBO", "widget": {"name": "aspect_ratio"}, "link": null},
    {"name": "resolution", "type": "COMBO", "widget": {"name": "resolution"}, "link": null},
    {"name": "response_modalities", "type": "COMBO", "widget": {"name": "response_modalities"}, "link": null},
    {"name": "images", "type": "IMAGE", "link": 101},
    {"name": "system_prompt", "type": "STRING", "widget": {"name": "system_prompt"}, "link": null}
  ],
  "outputs": [
    {"name": "response", "type": "STRING", "links": [201]},
    {"name": "image", "type": "IMAGE", "links": [200]}
  ],
  "widgets_values": ["", "prompt text", "gemini-3-pro-image-preview", 42, "randomize", "auto", "1K", "IMAGE+TEXT", "You are an expert..."]
}
```

Note: `GoogleGeminiDirect` returns **both** `STRING` (slot 0) and `IMAGE` (slot 1). To generate images, use a model like `gemini-3-pro-image-preview` or `gemini-3.1-flash-image-preview` and set `response_modalities` to `IMAGE` or `IMAGE+TEXT`.

## Scripts

- `scripts/convert_gemini_nodes.py` — Auto-convert Gemini-related comfy_api_nodes to `GoogleGeminiDirect` in a workflow JSON file. Outputs to a new file; does not overwrite originals. Handles `control_after_generate` widget mapping automatically.

## References

- `references/node-mapping.md` — Full mapping of inputs, outputs, and widget indexes for all supported conversions.
