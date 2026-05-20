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
- `comfyui-local-gemini` → `FALKlingImage2Video`, `FALKlingOmniVideo`

**Important:** `comfyui-local-gemini` is a **separate git repository** (`custom_nodes/comfyui-local-gemini/`) with its own remote. Changes to its `nodes.py` must be committed and pushed independently from the main ComfyUI repo. The main repo's `custom_nodes/` directory is gitignored, so changes there do not appear in the main ComfyUI commit.

## Node Mapping

| comfy_api_nodes (remove) | local_api replacement | Notes |
|--------------------------|----------------------|-------|
| `GeminiImage2Node` | `GoogleGeminiDirect` | Maps `prompt`→`prompt`, `images`→`images`. Preserves **both** STRING and IMAGE outputs. See `references/node-mapping.md` for full widget index mapping. |
| `GeminiNanoBanana2` | `GoogleGeminiDirect` | Same as above. `thinking_level` is dropped (not supported in direct API). Merges multiple IMAGE outputs into the single `image` output. |
| `GeminiNanoBanana2V2` | `GoogleGeminiDirect` | Same as above. |
| `KlingOmniProImageToVideoNode` | `FALKlingOmniVideo` | Wraps FAL `kling-video/o3/pro/reference-to-video`. Supports `reference_images`, `subject_description`, and up to 3 scene storyboards via `scene_N_text/duration`. Drops cloud-only widgets: `model`, `resolution`, `mode`. See full mapping in `references/node-mapping.md`. |

## Conversion Steps

1. **Load the workflow JSON** and list all node types.
2. **Identify `comfy_api_nodes`** using the mapping table above.
3. **Replace each node** in the JSON:
   - Change `type` from the old node ID to the new local node ID.
   - Update `inputs` to match the local node's signature (names and types).
   - Update `widgets_values` to match the local node's widget order. **CRITICAL:** See [Widget Mapping Mechanics](#widget-mapping-mechanics) below.
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
- `FAL_KEY` → used by `FALKlingImage2Video` and `FALKlingOmniVideo`

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

### Execution Order: Parallel vs Sequential for API Subgraphs

When multiple subgraphs each call external APIs (Gemini, Kling, ElevenLabs, etc.), ComfyUI runs them in **parallel by default** because they have no inter-dependencies. This is fastest but can cause:
- **API rate-limiting** (429 errors from concurrent calls)
- **Nondeterministic output order** (scheduler may run 7→3→6→4→1→5→2)
- **Harder debugging** when one subgraph fails

**Sequential chaining** forces `1 → 2 → 3 → 4 → 5 → 6 → 7` order.

#### Parallel (Default — No Changes Needed)
```
BatchImagesNode ──→ Subgraph 1 (Gemini prompt → Kling video)
              ──→ Subgraph 2 (Gemini prompt → Kling video)
              ──→ Subgraph 3 (Gemini prompt → Kling video)
```
All Gemini prompts generate simultaneously. All Kling videos generate simultaneously.

#### Sequential (Chained Trigger Inputs)
```
BatchImagesNode ──→ Subgraph 1 ──→ Subgraph 2 ──→ Subgraph 3
              (trigger)          (trigger)          (trigger)
```
Subgraph 1 runs to completion, then Subgraph 2, then Subgraph 3.

**How to implement sequential chaining:**

1. **Add `trigger` to every API node inside the subgraph** that should wait:
   ```python
   "optional": {
       "trigger": ("*", {}),  # ignored by the node; only creates dependency
   }
   ```
   Both `GoogleGeminiDirect` and `FALKlingImage2Video` need this if you want the **entire** subgraph to wait. If you only chain Kling, the Gemini prompts still run in parallel.

2. **Wire the subgraph's trigger input to all those nodes**:
   ```json
   // Subgraph definition: trigger input feeds both Gemini and Kling
   {"name": "trigger", "type": "*", "linkIds": [400, 450]}
   
   // Link 400: -10[3] → Kling slot 11
   // Link 450: -10[3] → Gemini slot 9
   ```

3. **Chain subgraphs in the main graph**:
   - Subgraph 1 `trigger` ← connect to `BatchImagesNode` (or any upstream node)
   - Subgraph 2 `trigger` ← connect to Subgraph 1 `VIDEO` output
   - Subgraph 3 `trigger` ← connect to Subgraph 2 `VIDEO` output
   - ...and so on

4. **Critical:** Subgraph 1's trigger **must** have a real external connection. If left disconnected, ComfyUI's frontend prunes the input during expansion and the internal trigger links disappear. Use `type: "*"` on the trigger input so it can accept `IMAGE` from `BatchImagesNode` as its dummy start signal.

**When to use which:**
| Scenario | Recommendation |
|----------|---------------|
| Fastest total time; APIs support concurrency | **Parallel** (default) |
| Avoiding rate limits; deterministic order; debugging | **Sequential** |
| Mix: parallel Gemini (cheap) + sequential Kling (expensive) | Chain trigger **only to Kling**, leave Gemini unchained |

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

## Widget Mapping Mechanics

ComfyUI's frontend maps `widgets_values` to node inputs using a specific set of rules. Getting this wrong causes backend validation errors like `Failed to convert an input value to a INT value` because strings end up in numeric slots.

### The Three Rules

1. **Only inputs with `"widget": {"name": "..."}` markers consume `widgets_values` slots.**
   Connection-only inputs (like `images`, `trigger`) must NOT have a `widget` marker and do NOT consume a slot.

2. **Hidden widgets consume slots too.**
   Any input with `"control_after_generate": True` in its `INPUT_TYPES` config (e.g., `seed`) causes the frontend to auto-insert a hidden control widget immediately after it in `widgets_values`. The hidden value is at index `parent_widget_index + 1`.

3. **Optional widget inputs MUST stay in the JSON `inputs` array.**
   If you remove an optional widget input from the `inputs` array (to "clean up" the JSON), the frontend cannot map values to it. The remaining values shift and land in the wrong slots.

### Example: Correct vs Broken `widgets_values`

**Node:** `FALKlingOmniVideo` — 12 visible widgets + 1 hidden `seed_control` = 13 values.

```
Visible widget inputs (in inputs array order):
  [0] api_key              (widget)
  [1] subject_description  (widget)
  [2] aspect_ratio         (widget)
  [3] duration             (widget)
  [4] generate_audio       (widget)
  [5] seed                 (widget)  ← has control_after_generate
  [6] reference_images     (NO widget — connection only)
  [7] scene_1_text         (widget)
  [8] scene_1_duration     (widget)
  [9] scene_2_text         (widget)
  [10] scene_2_duration    (widget)
  [11] scene_3_text        (widget)
  [12] scene_3_duration    (widget)

widgets_values mapping:
  [0] → api_key
  [1] → subject_description
  [2] → aspect_ratio
  [3] → duration
  [4] → generate_audio
  [5] → seed
  [6] → seed_control (hidden, inserted after seed)
  [7] → scene_1_text
  [8] → scene_1_duration
  [9] → scene_2_text
  [10] → scene_2_duration
  [11] → scene_3_text
  [12] → scene_3_duration
```

**Common mistake:** Removing optional scene inputs from the `inputs` array and using only 12 `widgets_values`. The frontend then maps `scene_1_text` to `seed_control`'s slot and every subsequent value shifts by one, causing type mismatches.

### Building a `/prompt` API payload manually

When flattening a workflow JSON into a `prompt` dict for the `/prompt` REST API:

1. Iterate the node's `inputs` array in order.
2. For each input with a `widget` marker, consume the next `widgets_values`.
3. If the widget name is `seed` AND the node type is known to have `control_after_generate`, **skip the next `widgets_values` entry** (that's the hidden `seed_control`).
4. For inputs without a `widget` marker but with a `link`, resolve the link to `[origin_node_id, origin_slot]`.
5. For nodes with no `inputs` array at all (e.g., `LoadImage` with only `widgets_values`), use `object_info` to map `widgets_values[0]` → the first required input name.

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
