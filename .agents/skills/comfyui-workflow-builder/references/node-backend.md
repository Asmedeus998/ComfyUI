# Node Backend (Python)

## Minimum Viable Node

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

## Critical Rules

- `INPUT_TYPES()` returns `{"required": {...}, "optional": {...}}`
- `RETURN_TYPES` must be a **tuple** — one output: `("STRING",)`
- The `FUNCTION` method must return a **tuple** matching `RETURN_TYPES`
- **Never** return `None` for a slot — return ` ""` or `0`
- Key order in `required`/`optional` = top-to-bottom widget order = `slot_index` order
- Optional inputs come after required inputs in internal ordering

## Widget Types

| Type | Python Arg | Notes |
|------|-----------|-------|
| `("STRING", {"multiline": True})` | `str` | Text area. Use `forceInput: True` to make socket-only |
| `("INT", {"min": 0, "max": 100})` | `int` | Spinner |
| `("FLOAT", {"min": 0.0, "max": 1.0, "step": 0.1})` | `float` | Decimal spinner |
| `("BOOLEAN", {"default": True})` | `bool` | Toggle |
| `(["a", "b"], {"default": "a"})` | `str` | Dropdown (COMBO) |
| `("AUDIO",)` | `dict` | Native ComfyUI audio: `{"waveform": tensor, "sample_rate": 22050}` |
| `("IMAGE",)` | `tensor` | Batch, channels, height, width |
| `("VIDEO",)` | `object` | ComfyUI video object from `InputImpl.VideoFromFile(path_or_bytes)` |

**COMBO widgets cannot accept connections.** If you need to wire a value in, change to `STRING` or add a separate `STRING` optional input.

## Hidden Inputs (for updating widget values after execution)

```python
"hidden": {
    "unique_id": "UNIQUE_ID",
    "extra_pnginfo": "EXTRA_PNGINFO",
}
```

Use these to update `extra_pnginfo["workflow"]["nodes"][i]["widgets_values"]` so the frontend displays computed text.
