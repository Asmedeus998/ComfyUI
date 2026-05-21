# Testing & Debugging

## Testing via ComfyUI API (Not Just Direct Python)

Direct Python execution (`python -c "from my_node import ...; node.run(...)"`) tests the backend logic but **not** the workflow serialization, frontend cache, or slot-index mapping. Always verify through the actual ComfyUI `/prompt` API.

### Step 1: Create a Minimal Test Workflow JSON

Save to `user/default/workflows/test-<feature>.json`:

```json
{
  "last_node_id": 2,
  "last_link_id": 1,
  "nodes": [
    {
      "id": 1,
      "type": "MyNode",
      "pos": [80, 160],
      "size": [360, 200],
      "flags": {},
      "order": 0,
      "mode": 0,
      "inputs": [],
      "outputs": [
        {"name": "result", "type": "STRING", "links": [1], "slot_index": 0}
      ],
      "properties": {"Node name for S&R": "MyNode"},
      "widgets_values": ["widget_value_a", "widget_value_b"]
    },
    {
      "id": 2,
      "type": "MultiSubtitlePreviewSRT",
      "pos": [520, 160],
      "size": [400, 300],
      "flags": {},
      "order": 1,
      "mode": 0,
      "inputs": [
        {"name": "srt", "type": "STRING", "link": 1, "slot_index": 0}
      ],
      "outputs": [],
      "properties": {"Node name for S&R": "MultiSubtitlePreviewSRT"},
      "widgets_values": []
    }
  ],
  "links": [
    [1, 1, 0, 2, 0, "STRING"]
  ],
  "groups": [],
  "config": {},
  "extra": {"ds": {"scale": 1, "offset": [0, 0]}},
  "version": 0.4
}
```

### Step 2: Build the Prompt Payload

Use `/object_info/NodeName` to get `input_order`, then map `widgets_values` to input names:

```python
import json, urllib.request

# 1. Load workflow
with open('user/default/workflows/test-<feature>.json') as f:
    wf = json.load(f)

# 2. Get input ordering from backend
obj_info = json.loads(urllib.request.urlopen(
    'http://127.0.0.1:8195/object_info/MyNode'
).read())
input_order = (obj_info['MyNode']['input_order']['required'] +
               obj_info['MyNode']['input_order'].get('optional', []))

# 3. Build prompt dict
prompt = {}
for n in wf['nodes']:
    nid = str(n['id'])
    inputs = {}
    widgets = n.get('widgets_values', [])
    for i, wv in enumerate(widgets):
        if i < len(input_order):
            inputs[input_order[i]] = wv
    # Resolve linked inputs (override widgets)
    for inp in n.get('inputs', []):
        if inp.get('link') is not None:
            for l in wf['links']:
                if l[0] == inp['link']:
                    inputs[inp['name']] = [str(l[1]), l[2]]
                    break
    prompt[nid] = {
        'inputs': inputs,
        'class_type': n['type'],
        '_meta': {'title': n['type']}
    }

payload = {'prompt': prompt}
```

### Step 3: Submit and Monitor

```bash
# Submit
curl -s -X POST http://127.0.0.1:8195/prompt \
  -H "Content-Type: application/json" \
  -d @/tmp/test_prompt.json

# Check queue
curl -s http://127.0.0.1:8195/queue | python3 -m json.tool

# Check history after completion
curl -s http://127.0.0.1:8195/history | python3 -m json.tool

# Interrupt if stuck
curl -s -X POST http://127.0.0.1:8195/interrupt
```

### Step 4: Compare Outputs

For SRT/audio/text outputs, always compare the **actual generated files** side-by-side:

```bash
# Word/block counts
wc -w output/videos/video.srt
wc -w /native/app/output/video.srt

# First difference
python3 -c "
with open('output/videos/video.srt') as f: a = f.read()
with open('/native/app/output/video.srt') as f: b = f.read()
print(f'A: {len(a)} chars, B: {len(b)} chars')
# ...diff logic...
"
```

## Common Pitfalls

| Symptom | Cause | Fix |
|---------|-------|-----|
| `tuple index out of range` on validation | Workflow `slot_index` doesn't match `INPUT_TYPES` | Delete node, re-add fresh |
| `tuple index out of range` on execute | `RETURN_TYPES` changed, old workflow has wrong output indices | Regenerate node in workflow |
| Node shows red box | Frontend cached old node definition | `Ctrl+Shift+R` or `localStorage.clear()` |
| Widget not visible | `forceInput: True` or input is connected | Disconnect link to see widget, or use JS extension |
| JS extension not loading | Missing `WEB_DIRECTORY` in `__init__.py` | Add `WEB_DIRECTORY = "./js"` |
| Preview text blank | No custom JS frontend to render `ui.text` | Use rgthree-comfy `Display Any` node, or add JS extension |
| `Reference audio not found` | Empty string passed to path arg | Check link connections, verify node outputs |
| `Required input missing: source` | `PreviewAny` node disconnected during conversion | Rewire `LoadImage` output to BOTH the new FAL node AND the orphaned `PreviewAny` sink |
| `Failed to validate prompt` | Stale per-node link references after global `links` mutation | Call `sync_links_to_nodes(wf)` to rebuild `input.link` and `output.links` from global `links` array |

## Debugging Checklist

1. **Backend schema**: `curl -s http://127.0.0.1:8188/object_info/NodeName | python -m json.tool`
2. **Frontend cache**: `Ctrl+Shift+R` hard refresh
3. **Tmux logs**: `tmux capture-pane -p -t comfyui-dev -S -1000 | tail -50`
4. **Slot indices**: Compare workflow JSON `slot_index` against `/object_info` `input_order`
5. **Link topology**: Verify `[link_id, src_node, src_slot, dst_node, dst_slot, type]` format
6. **Queue status**: `curl -s http://127.0.0.1:8195/queue` — check if prompt is running/pending
7. **History**: `curl -s http://127.0.0.1:8195/history` — check completed prompt outputs
8. **Test via API**: Create minimal workflow, submit to `/prompt`, compare actual output files
