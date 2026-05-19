# Custom Node Documentation

## comfyui-multi-subtitle

Location: `custom_nodes/comfyui-multi-subtitle/`

A ComfyUI wrapper for [Modelscope_Faster_Whisper_Multi_Subtitle](https://github.com/v3ucn/Modelscope_Faster_Whisper_Multi_Subtitle) that provides audio/video transcription, translation, TTS dubbing, and subtitle merging.

---

### Recent Changes (2026-05-19)

#### 1. SRT Pass-Through Outputs

Two nodes now expose an additional `srt` output so subtitles can be wired directly to preview nodes:

- **`MultiSubtitleMerge`**
  - `RETURN_TYPES = ("STRING", "STRING")`
  - `RETURN_NAMES = ("output_video", "srt")`
  - Passes through the SRT it receives as input.

- **`MultiSubtitleTTS_GPTSoVITS`**
  - `RETURN_TYPES = ("AUDIO", "STRING", "STRING")`
  - `RETURN_NAMES = ("audio", "audio_path", "srt")`
  - Passes through the SRT it receives as input.

Existing connections to `audio` (slot 0) and `audio_path` (slot 1) remain valid; the new `srt` output is slot 2.

#### 2. GPT-SoVITS Stable Clone

To avoid breaking when the development repo at `~/github/GPT-SoVITS` is modified, the node now uses a pinned stable clone:

```
custom_nodes/comfyui-multi-subtitle/GPT-SoVITS  (tag: v1)
```

**Setup on a fresh machine:**

```bash
cd /path/to/ComfyUI/custom_nodes/comfyui-multi-subtitle/GPT-SoVITS

# 1. Install Python dependencies via uv
uv sync

# 2. Download pretrained models & assets
python download_pretrained.py --source HF
# Alternatives: --source HF-Mirror  or  --source ModelScope
```

The `download_pretrained.py` script fetches:
- **Pretrained models** → `GPT_SoVITS/pretrained_models/`
- **G2PWModel** → `GPT_SoVITS/text/G2PWModel/`
- **NLTK data** → `nltk_data/`
- **Open JTalk dictionary** → pyopenjtalk package directory

The script skips anything already present, so it is safe to re-run.

#### 3. Monkey-Patches in `_run_tts`

The `_run_tts` helper in `nodes/multisubtitle_node.py` applies several runtime patches to the multi-subtitle engine:

| Patch | Purpose |
|-------|---------|
| `_generate_audio_gpt_sovits` → `_patched_gpt_sovits` | Routes GPT-SoVITS inference through `api_v2.py` (port 9880) so models stay loaded on GPU |
| `_stretch_audio_to_fit` → `_ffmpeg_stretch` | Replaces librosa phase-vocoder stretching with `ffmpeg -filter:a atempo=...` |
| `subprocess.run` → `_ffmpeg_run` | Intercepts `sox` calls inside `_build_audio_from_srt` and redirects them to `ffmpeg` |

These patches remove the dependency on `sox` and keep GPU models warm between subtitle lines.

#### 4. Path Updates

`multisubtitle_node.py` now resolves GPT-SoVITS root to the stable clone:

```python
gpt_root = "/home/yumeko/github/ComfyUI/custom_nodes/comfyui-multi-subtitle/GPT-SoVITS"
```

Previously this pointed to `~/github/GPT-SoVITS`.

---

### Nodes Reference

| Node | Category | Inputs | Outputs |
|------|----------|--------|---------|
| `MultiSubtitleTranscribe` | Multi-Subtitle | video_file, model, language, vad_filter | `srt`, `detected_language`, `audio`, `audio_path` |
| `MultiSubtitleTranslate` | Multi-Subtitle | srt, target_language | `srt` |
| `MultiSubtitleTTS_Piper` | Multi-Subtitle/TTS | srt, voice_idx | `audio`, `audio_path` |
| `MultiSubtitleTTS_OmniVoice` | Multi-Subtitle/TTS | srt, mode, instruct, ref_audio_path, ref_text, speed | `audio`, `audio_path` |
| `MultiSubtitleTTS_GPTSoVITS` | Multi-Subtitle/TTS | srt, ref_audio_path, ref_text, ref_lang, text_lang, top_p, temperature, top_k, repetition_penalty, speed_factor, speaker_voice_map_json, gpt_weights, sovits_weights | `audio`, `audio_path`, `srt` |
| `MultiSubtitleTTS_VoxCPM` | Multi-Subtitle/TTS | srt, ref_audio_path, ref_text, control_instruction | `audio`, `audio_path` |
| `MultiSubtitleTTS_IndexTTS2` | Multi-Subtitle/TTS | srt, ref_audio_path, target_duration_sec | `audio`, `audio_path` |
| `MultiSubtitleMerge` | Multi-Subtitle | video_file, mode, srt, audio | `output_video`, `srt` |
| `MultiSubtitlePreviewSRT` | Multi-Subtitle/Preview | srt | `srt` (displays in widget) |
| `MultiSubtitlePreviewJSON` | Multi-Subtitle/Preview | json_str | `json_str` (displays in widget) |
| `ABTestTextToSRT` | Multi-Subtitle/AB Test | text, duration_sec | `srt` |

---

### Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `api_v2.py failed to start within 60 seconds` | Missing pretrained models in `GPT_SoVITS/pretrained_models/` | Run `python download_pretrained.py --source HF` inside the stable clone |
| `No such file or directory: 'sox'` | Old multi-subtitle code calls `sox` directly | Already patched — ensure ComfyUI is restarted after node updates |
| `tuple index out of range` on TTS node | Workflow JSON has stale output slot indices after RETURN_TYPES changed | Delete the TTS node from the workflow and re-add it |
| `Reference audio not found` | Empty or invalid path passed to `ref_audio_path` | Verify the path exists and is a valid WAV file |

---

### Workflow Example

`user/default/workflows/gpt-sovits-ab-test.json`

An A/B test workflow that generates 4 GPT-SoVITS audio variants from a single SRT input with different temperature/speed parameters, plus a `👁 Preview SRT` node to inspect the subtitle text.
