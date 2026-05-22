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

## Batched Image Inputs

To accept a batched IMAGE tensor and unroll it:

```python
"optional": {
    "images": ("IMAGE",),          # batched input (B, H, W, C)
    "image_1": ("IMAGE",),         # individual fallback slots
    "image_2": ("IMAGE",),
}

def process(self, images=None, image_1=None, image_2=None):
    flat_tensors = []
    if images is not None:
        if images.ndim == 4:
            flat_tensors.extend(images[i] for i in range(images.shape[0]))
        else:
            flat_tensors.append(images)
    for t in [image_1, image_2]:
        if t is not None:
            if t.ndim == 4:
                flat_tensors.extend(t[i] for i in range(t.shape[0]))
            else:
                flat_tensors.append(t)
    # flat_tensors now contains all images in order
```

**Pattern:** Unroll `images` first, then append individual `image_N` inputs. This lets users mix batched tensors from `BatchImagesNode` with manually wired individual images.

## Video Input / Output

### Receiving VIDEO

ComfyUI's `VIDEO` type is a `VideoInput` object (typically `VideoFromFile` or `VideoFromComponents`). It is NOT a tensor — it's an object with methods:

```python
def process(self, video=None):
    if video is not None:
        # Option 1: Get the underlying file path / BytesIO
        source = video.get_stream_source()  # str path or io.BytesIO

        # Option 2: Get decoded components (frames tensor, audio, fps)
        components = video.get_components()
        # components.images  → (F, H, W, 3) tensor
        # components.audio   → {"waveform": tensor, "sample_rate": int}
        # components.frame_rate → Fraction
```

### Saving VIDEO to File

```python
import folder_paths
import os

def save_video_temp(video, suffix=".mp4"):
    temp_path = os.path.join(
        folder_paths.get_temp_directory(),
        f"vid_{os.urandom(4).hex()}{suffix}"
    )
    video.save_to(temp_path, format="mp4", codec="h264")
    return temp_path
```

The `save_to` method handles:
- Re-encoding via PyAV (`av` library)
- H.264 / AAC output
- Preserving metadata

### Creating VIDEO Output

```python
from comfy_api.input_impl import InputImpl

# From an existing file path
video = InputImpl.VideoFromFile("/path/to/video.mp4")
return (video,)

# From components (frames tensor + audio)
from comfy_api.latest._input_impl import VideoFromComponents
video = VideoFromComponents(components)
return (video,)
```

## Subprocess-Based Nodes

For nodes that wrap external CLIs (e.g., `kimi-cli`), use `subprocess.Popen`:

```python
import subprocess
import json

def generate(self, prompt: str, timeout: int = 300):
    cmd = ["kimi", "--print", "--output-format", "stream-json", "--yolo"]

    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )
    process.stdin.write(prompt + "\n")
    process.stdin.close()

    texts = []
    for line in process.stdout:
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("role") == "assistant":
            for block in event.get("content", []):
                if block.get("type") == "text":
                    texts.append(block.get("text", ""))

    process.wait(timeout=timeout)
    return ("".join(texts),)
```

**Key points:**
- Always use `text=True` and `bufsize=1` for line-by-line streaming
- Pass prompt via `stdin` to avoid shell escaping issues
- Parse stdout as structured output (JSONL, etc.)
- Read `stderr` on non-zero exit codes for error messages
- Clean up temp files in a `finally` block

## Inline Preview Nodes (OUTPUT_NODE)

To show results directly inside the node without requiring a downstream `PreviewImage`:

```python
class MyPreviewNode:
    RETURN_TYPES = ()
    FUNCTION = "preview"
    OUTPUT_NODE = True

    def preview(self, images, prompt=None, extra_pnginfo=None):
        # Save image to temp directory
        output_dir = folder_paths.get_temp_directory()
        filename = f"preview_{os.urandom(4).hex()}.png"
        filepath = os.path.join(output_dir, filename)
        # ... save image to filepath ...

        return {"ui": {"images": [{
            "filename": filename,
            "subfolder": "",
            "type": "temp",
        }]}}
```

`OUTPUT_NODE = True` + returning `{"ui": {"images": [...]}}` makes ComfyUI display the image inline in the node panel after execution.

## Hidden Inputs (for updating widget values after execution)

```python
"hidden": {
    "unique_id": "UNIQUE_ID",
    "extra_pnginfo": "EXTRA_PNGINFO",
}
```

Use these to update `extra_pnginfo["workflow"]["nodes"][i]["widgets_values"]` so the frontend displays computed text.
