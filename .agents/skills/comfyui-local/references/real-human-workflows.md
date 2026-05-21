# Real-Human Workflow Conversion Rules

Some Seedance workflows (e.g., `api_seedance2_0_flf2v_real_human.json`) contain **asset creation chains** for real-human verification compliance. These chains use `ByteDanceCreateImageAsset` and `ByteDanceCreateVideoAsset` nodes that are cloud-only and not needed for local FAL API calls.

## What to Remove vs Keep

| Node | Action | Reason |
|------|--------|--------|
| `ByteDanceCreateImageAsset` | **Remove** | Cloud-only asset verification; FAL does not use asset IDs |
| `ByteDanceCreateVideoAsset` | **Remove** (or leave bypassed) | Same as above |
| `LoadImage` | **Keep** | Still needed as image source for FAL nodes |
| `PreviewAny` | **Keep** | Displays image previews; removing them causes `Required input missing: source` |
| `MarkdownNote` | **Keep** | Documentation; no backend impact |
| `SaveVideo` | **Keep** | Saves the output video |
| `ByteDance2*Node` | **Replace** with FAL equivalent | Main video generation node |

## Rewiring Pattern

When `ByteDanceCreateImageAsset` nodes are removed, their downstream `PreviewAny` nodes lose their `source` input connection. You must rewire:

1. **`LoadImage` → FAL node**: Connect the `LoadImage` `IMAGE` output to the FAL node's image input (e.g., `image` slot 2 for `FALSeedanceImage2Video`, or `image_1` slot 9 for `FALSeedanceReference2Video`).
2. **`LoadImage` → `PreviewAny`**: ALSO connect the same `LoadImage` `IMAGE` output to any orphaned `PreviewAny` nodes so they don't error with `Required input missing`.

### Example: FALSeedanceImage2Video Real-Human Workflow

```
LoadImage (first_frame) ──→ FALSeedanceImage2Video.image  (slot 2)
                        ──→ PreviewAny (group_id preview)
LoadImage (last_frame)  ──→ FALSeedanceImage2Video.end_image (slot 3)
                        ──→ PreviewAny (asset_id preview)
```

## Preserving Workflow Structure

- Keep all **groups** intact.
- Keep all **node positions** (`pos`) and **sizes**.
- Only modify `type`, `inputs`, `outputs`, `widgets_values`, and `links`.
- After any link mutation, call `sync_links_to_nodes(wf)` to rebuild per-node `input.link` and `output.links` from the global `links` array.

## Fast Endpoints

All Seedance nodes have a `fast` boolean widget (last widget, no hidden control). When `fast=True`, the endpoint changes:
- `bytedance/seedance-2.0/text-to-video` → `bytedance/seedance-2.0/fast/text-to-video`
- `bytedance/seedance-2.0/image-to-video` → `bytedance/seedance-2.0/fast/image-to-video`
- `bytedance/seedance-2.0/reference-to-video` → `bytedance/seedance-2.0/fast/reference-to-video`

Leave `fast=False` (default) for full quality.
