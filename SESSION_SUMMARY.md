# Session Summary

## Date: 2026-05-21

### Task: Convert SEEDANCE 2.0 Workflows to Local FAL API Nodes

Converted all 6 SEEDANCE 2.0 workflows in `user/default/workflows/SEEDANCE2.0/` from ByteDance cloud API nodes (`comfy_api_nodes`) to local custom nodes that call **fal.ai** directly using the user's own `FAL_KEY`.

#### New Local Nodes Added

Added three new nodes to `custom_nodes/comfyui-local-gemini/nodes.py`:

- **`FALSeedanceText2Video`** — Calls `bytedance/seedance-2.0/text-to-video` (or `/fast` variant). Replaces `ByteDance2TextToVideoNode`.
- **`FALSeedanceImage2Video`** — Calls `bytedance/seedance-2.0/image-to-video` (or `/fast` variant). Supports `image` + optional `end_image`. Replaces `ByteDance2FirstLastFrameNode`.
- **`FALSeedanceReference2Video`** — Calls `bytedance/seedance-2.0/reference-to-video` (or `/fast` variant). Supports up to 9 reference images via `image_1` … `image_9`. Replaces `ByteDance2ReferenceNode`.

All nodes:
- Use the `FAL_KEY` environment variable (leave `api_key` widget empty).
- Support `fast` toggle for fast endpoints.
- Return standard ComfyUI `VIDEO` type via `InputImpl.VideoFromFile`.

#### Workflow Conversions

| Original Workflow | Converted Workflow | Changes |
|-------------------|-------------------|---------|
| `api_seedance2_0_t2v.json` | `api_seedance2_0_t2v_local.json` | `ByteDance2TextToVideoNode` → `FALSeedanceText2Video` |
| `api_seedance2_0_flf2v.json` | `api_seedance2_0_flf2v_local.json` | `ByteDance2FirstLastFrameNode` → `FALSeedanceImage2Video` |
| `api_seedance2_0_r2v.json` | `api_seedance2_0_r2v_local.json` | `ByteDance2ReferenceNode` → `FALSeedanceReference2Video` |
| `api_seedance2_0_flf2v_real_human.json` | `api_seedance2_0_flf2v_real_human_local.json` | Removed `ByteDanceCreateImageAsset` + preview/markdown nodes; wired `LoadImage` directly to `FALSeedanceImage2Video` |
| `api_seedance2_0_r2v_real_human.json` | `api_seedance2_0_r2v_real_human_local.json` | Removed `ByteDanceCreateImageAsset` + preview/markdown nodes; wired `LoadImage` directly to `FALSeedanceReference2Video` |
| `template_seedance_2_0_plus_llm_prompt_helper.json` | `template_seedance_2_0_plus_llm_prompt_helper_local.json` | `ByteDance2ReferenceNode` → `FALSeedanceReference2Video`; `GeminiNode` → `GoogleGeminiDirect`; rewired image/prompt links accordingly |

#### Testing & Fixes

1. **Node registration**: Verified all new nodes appear in `/object_info` after ComfyUI restart.
2. **Backend validation**: Queued minimal test prompts for `FALSeedanceText2Video`, `FALSeedanceImage2Video`, `FALSeedanceReference2Video`, and `GoogleGeminiDirect` via the `/prompt` API. All returned `"node_errors": {}`, confirming prompt validation passes.
3. **Real-human workflow fixes**: Rewrote conversions for `api_seedance2_0_flf2v_real_human_local.json` and `api_seedance2_0_r2v_real_human_local.json` to preserve the original workflow structure:
   - Kept all `PreviewAny`, `MarkdownNote`, `LoadImage`, and `SaveVideo` nodes.
   - Kept original groups.
   - Replaced `ByteDanceCreateImageAsset` with direct `LoadImage` → `PreviewAny` wires so preview nodes don't error.
   - Replaced the main ByteDance video node with the FAL equivalent.
   - Removed only the active `ByteDanceCreateImageAsset` nodes; kept bypassed `ByteDanceCreateVideoAsset` in the r2v workflow.
4. **Link sync**: All node input `link` and output `links` fields are synchronized with the global `links` array.
5. **Orphan link check**: All converted workflows have zero orphaned links.

#### Environment Variables

- `FAL_KEY` — Required for all Seedance local nodes.
- `GOOGLE_GEMINI_API_KEY` — Required for `GoogleGeminiDirect` in the template workflow.
