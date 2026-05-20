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

## Handling Subgraphs in Workflow Conversions

Many workflows use **subgraphs** (collapsed node groups) to keep the main graph clean. Subgraph instances appear as UUID-typed nodes (e.g., `f7abaa3a-5e87-4354-bab6-f43320cd490f`) in the main graph, with their internal definitions stored in `definitions.subgraphs`.

### When to Keep vs Flatten Subgraphs

| Approach | When to Use | Trade-off |
|----------|------------|-----------|
| **Keep subgraphs** | User wants visual similarity to original; frontend editing is important | Frontend must support subgraph expansion; harder to validate from CLI |
| **Flatten subgraphs** | Backend validation needed; subgraph contains cloud nodes that must be replaced | More nodes in main graph ("duplicate nodes"), but easier to debug |

**Default preference:** Keep the subgraph structure if the original workflow used it. Users prefer the clean main graph.

### Subgraph JSON Structure

```json
{
  "definitions": {
    "subgraphs": [
      {
        "id": "f7abaa3a-...",
        "nodes": [
          {"id": 304, "type": "ImageFromBatch", "pos": [7550, 660], ...},
          {"id": 306, "type": "GeminiNode", ...}
        ],
        "links": [
          {"id": 125, "origin_id": -10, "origin_slot": 0, "target_id": 304, "target_slot": 0, "type": "IMAGE"},
          {"id": 282, "origin_id": 304, "origin_slot": 0, "target_id": 306, "target_slot": 0, "type": "IMAGE"}
        ],
        "inputNode": {"id": -10, "bounding": [...]},
        "outputNode": {"id": -20, "bounding": [...]}
      }
    ]
  }
}
```

Key points:
- `-10` = subgraph **input** pseudo-node. Links from `-10[N]` receive the N-th input of the subgraph instance.
- `-20` = subgraph **output** pseudo-node. Links to `-20[N]` feed the N-th output of the subgraph instance.
- Subgraph internal links use **dict format** (`{"origin_id": ..., "target_id": ...}`), not the main graph's array format.

### Replacing Nodes Inside Subgraphs

When converting a cloud API node (e.g., `GeminiNode`) to a local node (`GoogleGeminiDirect`) **inside a subgraph**:

1. **Replace the `type`** in the subgraph's `nodes` array.
2. **Rebuild `inputs`/`outputs`** to match the new node's `INPUT_TYPES` signature.
3. **Remap internal links** — old slot indices won't match new slot indices.
4. **Update `widgets_values`** to match the new node's widget order.
5. **Remove unused subgraph inputs** — e.g., if the original Kling node accepted `model.resolution` but the local FAL Kling node doesn't, remove the `-10[2]` link and update the main graph to disconnect the external wire.

### Frontend-Only Nodes to Remove for Backend Validation

| Node | Type | Why Remove |
|------|------|-----------|
| `PrimitiveNode` | comfy-core frontend | Not a real backend node; its value is injected by the frontend |
| `Reroute` | core frontend | Pass-through node; frontend collapses it before sending to backend |

If you keep them in the saved workflow JSON (for frontend editing), the frontend will handle them. But when **flattening for backend validation** or **building a prompt payload**, strip them out and wire their targets directly to their sources (or set widget values on the target nodes).

### Common Pattern: "Crop Images" Subgraph

A frequent comfy-core subgraph is **"Crop Images"**, which takes a single image (e.g., a 2×2 grid from Gemini) and outputs 4 cropped quadrants. It internally uses:
- `GetImageSize` → gets original dimensions
- `SimpleMath+` → calculates `width / 2` and `height / 2`
- `ImageCrop+` → 4 instances with positions: `top-left`, `top-right`, `bottom-left`, `bottom-right`

If this subgraph is missing, flatten it by creating the individual nodes directly in the main workflow and rewiring the 4 outputs to the respective `SaveImage` nodes.

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
