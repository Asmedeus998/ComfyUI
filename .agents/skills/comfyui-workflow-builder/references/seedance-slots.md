# Seedance Node Input Slots & Workflow Preservation

## Preserving Workflow Structure During Conversion

When converting cloud API workflows to local nodes, **do not broadly strip auxiliary nodes**. Follow this priority:

1. **Identify the cloud node** to replace (e.g., `ByteDance2FirstLastFrameNode` → `FALSeedanceImage2Video`).
2. **Remove ONLY cloud-only infrastructure nodes** (e.g., `ByteDanceCreateImageAsset`, `ByteDanceCreateVideoAsset`).
3. **Keep ALL other nodes**: `LoadImage`, `PreviewAny`, `MarkdownNote`, `SaveVideo`, `PreviewImage`, `ImageStitch`, groups, etc.
4. **Rewire orphaned sinks**: When a removed node was feeding a `PreviewAny` or similar sink, wire the original source (`LoadImage`) directly to the sink as well as to the new compute node.
5. **Sync links**: After mutating the global `links` array, rebuild per-node references with `sync_links_to_nodes(wf)`.

### Why This Matters

Real-human workflows often have `PreviewAny` nodes that display `group_id` and `asset_id` strings. When asset creation chains are removed, these previews become orphaned. If you delete the `PreviewAny` nodes, the user loses the visual layout they expect. If you leave them disconnected, ComfyUI validation fails with `Required input missing: source`. The correct fix is to wire the `LoadImage` output to both the new FAL node AND the preview.

## Seedance Node Input Slots (for Workflow JSON)

### FALSeedanceText2Video

| Slot | Name | Type | Widget | Notes |
|------|------|------|--------|-------|
| 0 | `api_key` | STRING | yes | Leave empty; uses `FAL_KEY` env var |
| 1 | `prompt` | STRING | yes | Multiline |
| 2 | `resolution` | COMBO | yes | `480p`, `720p`, `1080p` |
| 3 | `aspect_ratio` | COMBO | yes | `auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| 4 | `duration` | INT | yes | 4–15 seconds |
| 5 | `generate_audio` | BOOLEAN | yes | Default `True` |
| 6 | `seed` | INT | yes | Has `control_after_generate=True` |
| 7 | `watermark` | BOOLEAN | yes | Default `False` |
| 8 | `fast` | BOOLEAN | yes | Default `False`; routes to `/fast/...` endpoint when `True` |

**Widget order:** `[api_key, prompt, resolution, aspect_ratio, duration, generate_audio, seed, seed_control, watermark, fast]` (10 values)

The hidden `seed_control` widget is auto-inserted by the frontend at index 7 (immediately after `seed`). It does NOT have its own input slot.

### FALSeedanceImage2Video

| Slot | Name | Type | Widget | Notes |
|------|------|------|--------|-------|
| 0 | `api_key` | STRING | yes | |
| 1 | `prompt` | STRING | yes | |
| 2 | `image` | IMAGE | no | **Required** first frame (connection only) |
| 3 | `end_image` | IMAGE | no | Optional last frame (connection only) |
| 4 | `resolution` | COMBO | yes | |
| 5 | `aspect_ratio` | COMBO | yes | |
| 6 | `duration` | INT | yes | |
| 7 | `generate_audio` | BOOLEAN | yes | |
| 8 | `seed` | INT | yes | |
| 9 | `watermark` | BOOLEAN | yes | |
| 10 | `fast` | BOOLEAN | yes | |

**Widget order:** 10 values (same as Text2Video above)

**Link wiring from converted workflows:**
- `LoadImage.IMAGE` (output slot 0) → `FALSeedanceImage2Video.image` (input slot 2)
- `LoadImage.IMAGE` (output slot 0) → `FALSeedanceImage2Video.end_image` (input slot 3)

### FALSeedanceReference2Video

| Slot | Name | Type | Widget | Notes |
|------|------|------|--------|-------|
| 0 | `api_key` | STRING | yes | |
| 1 | `prompt` | STRING | yes | |
| 2 | `resolution` | COMBO | yes | |
| 3 | `aspect_ratio` | COMBO | yes | |
| 4 | `duration` | INT | yes | |
| 5 | `generate_audio` | BOOLEAN | yes | |
| 6 | `seed` | INT | yes | |
| 7 | `watermark` | BOOLEAN | yes | |
| 8 | `fast` | BOOLEAN | yes | |
| 9 | `image_1` | IMAGE | no | Optional reference (connection only) |
| 10 | `image_2` | IMAGE | no | Optional reference (connection only) |
| 11 | `image_3` | IMAGE | no | Optional reference (connection only) |
| 12 | `image_4` | IMAGE | no | Optional reference (connection only) |
| 13 | `image_5` | IMAGE | no | Optional reference (connection only) |
| 14 | `image_6` | IMAGE | no | Optional reference (connection only) |
| 15 | `image_7` | IMAGE | no | Optional reference (connection only) |
| 16 | `image_8` | IMAGE | no | Optional reference (connection only) |
| 17 | `image_9` | IMAGE | no | Optional reference (connection only) |

**Widget order:** 10 values (same as Text2Video above)

**Link wiring from converted workflows:**
- `LoadImage.IMAGE` (output slot 0) → `FALSeedanceReference2Video.image_1` (input slot 9)
- `LoadImage.IMAGE` (output slot 0) → `FALSeedanceReference2Video.image_2` (input slot 10)
- etc.

**Important:** All three Seedance nodes share the same 10-value `widgets_values` sequence. Connection-only image inputs (no `widget` marker) do NOT consume `widgets_values` slots. When building `widgets_values`, always provide exactly 10 values.
