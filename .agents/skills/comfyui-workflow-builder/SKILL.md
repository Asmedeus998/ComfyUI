---
name: comfyui-workflow-builder
description: Build and modify ComfyUI custom nodes, workflows, and frontend extensions. Use when the user asks to create nodes, modify node definitions, wire workflow JSON, add preview/display nodes, or fix ComfyUI validation/runtime errors. Covers node Python backend, workflow JSON topology, JS frontend extensions, and common debugging patterns.
---

# ComfyUI Workflow Builder

## Node Backend (Python)

### Minimum Viable Node

```python
class MyNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
                "number": ("INT", {"default": 1, "min": 0, "max": 100}),
                "mode": (["a", "b", "c"], {"default": "a"}),  # COMBO dropdown
            },
            "optional": {
                "flag": ("BOOLEAN", {"default": False}),
                "audio": ("AUDIO",),  # connection-only, no widget
            }
        }

    RETURN_TYPES = ("STRING", "INT")   # tuple, even for single output
    RETURN_NAMES = ("result", "count")
    FUNCTION = "process"
    CATEGORY = "MyCategory/SubFolder"
    # OUTPUT_NODE = True  # set if node displays results in UI panel

    def process(self, text, number, mode, flag=False, audio=None):
        return (text.upper(), number * 2)
```

### Critical Rules

- `INPUT_TYPES()` returns `{"required": {...}, "optional": {...}}`
- `RETURN_TYPES` must be a **tuple** — one output: `("STRING",)`
- The `FUNCTION` method must return a **tuple** matching `RETURN_TYPES`
- **Never** return `None` for a slot — return ` ""` or `0`
- Key order in `required`/`optional` = top-to-bottom widget order = `slot_index` order
- Optional inputs come after required inputs in internal ordering

### Widget Types

| Type | Python Arg | Notes |
|------|-----------|-------|
| `("STRING", {"multiline": True})` | `str` | Text area. Use `forceInput: True` to make socket-only |
| `("INT", {"min": 0, "max": 100})` | `int` | Spinner |
| `("FLOAT", {"min": 0.0, "max": 1.0, "step": 0.1})` | `float` | Decimal spinner |
| `("BOOLEAN", {"default": True})` | `bool` | Toggle |
| `(["a", "b"], {"default": "a"})` | `str` | Dropdown (COMBO) |
| `("AUDIO",)` | `dict` | Native ComfyUI audio: `{"waveform": tensor, "sample_rate": 22050}` |
| `("IMAGE",)` | `tensor` | Batch, channels, height, width |

**COMBO widgets cannot accept connections.** If you need to wire a value in, change to `STRING` or add a separate `STRING` optional input.

### Hidden Inputs (for updating widget values after execution)

```python
"hidden": {
    "unique_id": "UNIQUE_ID",
    "extra_pnginfo": "EXTRA_PNGINFO",
}
```

Use these to update `extra_pnginfo["workflow"]["nodes"][i]["widgets_values"]` so the frontend displays computed text.

## Workflow JSON Format

### Link Format

```json
[link_id, origin_node_id, origin_slot_index, target_node_id, target_slot_index, "TYPE"]
```

Example: `[1, 2, 0, 4, 1, "STRING"]` = Node 2 output slot 0 → Node 4 input slot 1.

### Node Input Slots

`slot_index` in the JSON **must match** the argument position in `INPUT_TYPES["required"]` + `INPUT_TYPES["optional"]`.

If you change the number/order of inputs in Python, **delete and re-add the node** in the workflow — old `slot_index` values will cause `"tuple index out of range"` validation errors.

### Outputs

```json
"outputs": [
  {"name": "srt", "type": "STRING", "links": [1, 2, 3], "slot_index": 0},
  {"name": "audio", "type": "AUDIO", "links": null, "slot_index": 1}
]
```

`slot_index` must match `RETURN_TYPES` order. `links: null` = unconnected.

## Frontend JS Extensions

To update node UI after execution (e.g. display text), create a JS extension:

```javascript
// custom_nodes/<pack>/js/my_extension.js
import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

app.registerExtension({
    name: "my_pack.my_extension",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "MyDisplayNode") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                onNodeCreated?.apply(this, arguments);
                this.showValueWidget = ComfyWidgets["STRING"](
                    this, "value", ["STRING", { multiline: true }], app
                ).widget;
                this.showValueWidget.inputEl.readOnly = true;
            };

            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                onExecuted?.apply(this, arguments);
                if (message.text && this.showValueWidget) {
                    this.showValueWidget.value = message.text[0];
                }
            };
        }
    }
});
```

Python backend must return:
```python
return {"ui": {"text": (value,)}, "result": (value,)}
```

### Registering JS

Add to `custom_nodes/<pack>/__init__.py`:
```python
WEB_DIRECTORY = "./js"
```

Verify loaded: `curl http://127.0.0.1:8188/extensions | grep <pack>`

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

## Debugging Checklist

1. **Backend schema**: `curl -s http://127.0.0.1:8188/object_info/NodeName | python -m json.tool`
2. **Frontend cache**: `Ctrl+Shift+R` hard refresh
3. **Tmux logs**: `tmux capture-pane -p -t comfyui-dev -S -1000 | tail -50`
4. **Slot indices**: Compare workflow JSON `slot_index` against `/object_info` `input_order`
5. **Link topology**: Verify `[link_id, src_node, src_slot, dst_node, dst_slot, type]` format
6. **Queue status**: `curl -s http://127.0.0.1:8195/queue` — check if prompt is running/pending
7. **History**: `curl -s http://127.0.0.1:8195/history` — check completed prompt outputs
8. **Test via API**: Create minimal workflow, submit to `/prompt`, compare actual output files

## Audio Helpers

```python
import soundfile as sf
import numpy as np
import torch

def _wav_to_audio(path: str) -> dict:
    """Load WAV → ComfyUI AUDIO dict."""
    data, sr = sf.read(path, dtype="float32")
    if data.ndim == 1:
        data = data[np.newaxis, :]
    else:
        data = data.T
    data = data[np.newaxis, ...]
    return {"waveform": torch.from_numpy(data), "sample_rate": sr}

def _audio_to_wav(audio_dict: dict, path: str) -> str:
    """ComfyUI AUDIO dict → WAV file."""
    wav = audio_dict["waveform"]
    sr = int(audio_dict.get("sample_rate", 22050))
    if isinstance(wav, torch.Tensor):
        wav = wav.cpu().numpy()
    wav = np.asarray(wav)
    if wav.ndim == 3:
        wav = wav[0]
    if wav.ndim == 1:
        wav = wav[np.newaxis, :]
    sf.write(path, wav.T, sr)
    return path
```

## Project-Specific Conventions

This project uses:
- **Python env**: `uv pip install ...` (not `pip`)
- **ComfyUI port**: `8195`
- **Custom node path**: `custom_nodes/comfyui-multi-subtitle/`
- **Model storage**: NAS at `/mnt/storage/comfyui_data/` (symlinked via `scripts/link_nas_models.sh`)
- **Restart command**: `tmux send-keys -t comfyui-dev C-c && sleep 3 && tmux send-keys -t comfyui-dev "cd /home/yumeko/github/ComfyUI && ./start.sh" Enter`
- **Verify up**: `curl -s http://127.0.0.1:8195/system_stats`

See `AGENTS.md` in project root for full conventions.
