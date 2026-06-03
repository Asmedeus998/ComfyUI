# Agent Guidelines for ComfyUI

## Environment

- **Python environment**: This project uses `uv` for package management. Use `uv pip install ...` instead of `pip install ...`.
- **Download tool**: Always use `aria2c` for downloading files (models, LoRAs, datasets, etc.). Do **not** use `wget` or `curl` for large/binary downloads.
  - Preferred flags: `aria2c -x 4 -s 4 --dir=<output_dir> --out=<filename> <url>`
- **Custom nodes**: Clone into `custom_nodes/`. This directory is gitignored; do not commit custom node sub-repos.

## Runtime & Logs

- **ComfyUI runs inside a tmux session named `comfyui-dev`**.
- **After installing new custom nodes or patching node code, restart ComfyUI** so the changes are picked up:
  ```bash
  # Stop current instance
  tmux send-keys -t comfyui-dev C-c
  sleep 2
  # Restart
  tmux send-keys -t comfyui-dev "cd /home/yumeko/github/ComfyUI && ./start.sh" Enter
  ```
  Then wait ~20s and verify it's up: `curl -s http://127.0.0.1:8195/system_stats`
- To check live logs / errors, always inspect the tmux session first:
  ```bash
  tmux capture-pane -p -t comfyui-dev -S -1000 | tail -100
  ```
  Or attach interactively: `tmux attach -t comfyui-dev`
- Common issues visible in the tmux log:
  - `ClipVision model not found` → missing `clip_vision` model
  - `IPAdapter model not found` → missing `ipadapter` model
  - `ERROR lora ... shape '...' is invalid` → LoRA base model mismatch (e.g. SD 1.5 LoRA on SDXL checkpoint)
  - `lora key not loaded` → LoRA has extra keys for a different architecture (usually harmless if partial)
  - `Failed to validate prompt` → workflow nodes have disconnected/missing required inputs
  - `warning, embedding:... does not exist` → missing Textual Inversion embedding (non-blocking)

## Model Storage (IMPORTANT)

- **All models MUST be saved to the NAS**, not directly into the local repo's `models/` folders.
- **Source determines the NAS base path**:
  - **CivitAI downloads** → `/mnt/storage/comfyui_data/CivitAI/`
  - **HuggingFace downloads** → `/mnt/storage/comfyui_data/Huggingface/`
- The project uses `scripts/link_nas_models.sh` to symlink from the NAS into `models/`.
- **Existing CivitAI categories** (save to the appropriate folder):
  - `Model/` → `models/checkpoints`
  - `NSFW_model/` → `models/checkpoints`
  - `VAE/` → `models/vae`
  - `LORA/`, `NSFW_LORA/`, `LORA_character/`, `Lora_clothes/`, `Lora_style/` → `models/loras`
  - `Embedding/` → `models/embeddings`
  - `upscale/` → `models/upscale_models`
  - `ControlNet/` → `models/controlnet` (only for CivitAI-sourced controlnets)
- **Checkpoint organization by base model**: Inside `Model/` and `NSFW_model/`, organize checkpoints into subfolders by their base model type so ComfyUI can group them logically:
  - `Model/SDXL/` — for SDXL-based checkpoints
  - `Model/pony/` — for Pony Diffusion-based checkpoints
  - `Model/SD1.5/` — for SD 1.5-based checkpoints
  - (Create additional subfolders as needed for other base models)
  - The same rule applies to `NSFW_model/SDXL/`, `NSFW_model/pony/`, etc.
- **HuggingFace models**: Save to `/mnt/storage/comfyui_data/Huggingface/<Category>/` and symlink into the appropriate `models/` directory.
  - `Model/SDXL/`, `Model/pony/`, `Model/SD1.5/`, `Model/LTX/` → `models/checkpoints` (same base-model subfolder rule as CivitAI)
  - `ControlNet/` → `models/controlnet`
  - `clip_vision/` → `models/clip_vision` (CLIP Vision encoders for IPAdapter, e.g. `CLIP-ViT-H-14-laion2B-s32B-b79K.bin`)
  - `ipadapter/` → `models/ipadapter` (IPAdapter models, e.g. `ip-adapter_sdxl_vit-h.safetensors`)
  - `text_encoders/` → `models/text_encoders`
  - `vae/` → `models/vae`
  - `diffusion_models/` → `models/diffusion_models`
  - `latent_upscale_models/` → `models/latent_upscale_models`
  - `LORA/` → `models/loras`
  - `unet/` → `models/unet` (IC-Light models, e.g. `iclight_sd15_fc.safetensors`, `iclight_sd15_fbc.safetensors`)
- **Custom-node-internal models** (e.g. IndexTTS2): Some nodes store their own checkpoints inside the custom node folder (e.g. `custom_nodes/ComfyUI-IndexTTS2/checkpoints/`). For these:
  1. Download to a NAS subfolder (e.g. `Huggingface/IndexTTS2/`).
  2. Symlink the individual files into the custom node's expected `checkpoints/` directory.
  3. Document in `AGENTS.md` under **Known Custom Nodes**.
- **If a category doesn't exist yet**:
  1. Create the folder under the correct NAS base path.
  2. Save the downloaded model there.
  3. Symlink it into the corresponding `models/` directory.
  4. **Mandatory**: Update `scripts/link_nas_models.sh` to auto-link the new category, then **commit and push** the script change alongside any `AGENTS.md` updates.

## Workflows & App Mode

- **`.app.json` workflows always open in App Mode** (Linear Mode). The ComfyUI frontend treats this extension as an app workflow, and it also looks at `extra.linearMode` inside the JSON.
- **To convert an app workflow to normal node-graph mode:**
  1. Rename the file from `.app.json` → `.json`
  2. Edit the JSON and set `"linearMode": false` under the `extra` object

## Frontend Development (Local Fork)

This repo uses a **local frontend fork** at `ComfyUI_frontend/` (gitignored, pushed to `origin/master` on the frontend repo).

### Build & Deploy Pipeline

```bash
cd ComfyUI_frontend
rm -rf dist/ .nx/cache
NX_SKIP_NX_CACHE=true pnpm build          # outputs to dist/
rm -rf comfyui_frontend_package/comfyui_frontend_package/static/*
cp -r dist/* comfyui_frontend_package/comfyui_frontend_package/static/
```

### Critical: Stale Venv Static Files

`uv pip install -e ./ComfyUI_frontend/comfyui_frontend_package` does **NOT** create a true editable install for package data. Python resolves `importlib.resources.files(comfyui_frontend_package)` to `.venv/lib/python3.14/site-packages/comfyui_frontend_package/`, which contains **stale copied static files** from the first install.

**Symptom:** Patches are in source → build output has patches → browser still runs old JS.

**Verify where Python serves from:**
```bash
uv run python3 -c "import importlib.resources, comfyui_frontend_package; print(importlib.resources.files(comfyui_frontend_package) / 'static')"
# If this points to site-packages instead of the source, it's stale.
```

**Fix:** Delete the stale copy and symlink to the source static directory:
```bash
rm -rf .venv/lib/python3.14/site-packages/comfyui_frontend_package/static
ln -s /home/yumeko/github/ComfyUI/ComfyUI_frontend/comfyui_frontend_package/comfyui_frontend_package/static \
  .venv/lib/python3.14/site-packages/comfyui_frontend_package/static
```

**Verify served files:**
```bash
curl -s http://127.0.0.1:8195/ | grep -o 'src="[^"]*index-[^"]*"' | head -1
curl -sI http://127.0.0.1:8195/assets/dialogService-XXXX.js | head -1
```

### Frontend Debugging Checklist

1. Source patched? `grep "patch" src/...`
2. Build has patch? `grep "patch" dist/assets/*.js`
3. Package static dir has patch? `grep "patch" comfyui_frontend_package/.../static/assets/*.js`
4. **Python serves from source?** (see stale venv check above)
5. Browser loaded new JS? Check `index.html` references correct hashed filenames.

### Committing Frontend Changes

The frontend fork uses `husky` / `lint-staged` / `knip` pre-commit hooks that are broken on Node v20. Always commit with `--no-verify`:
```bash
git commit --no-verify -m "message"
git push --no-verify origin master
```

## Known Custom Nodes

| Node Pack | Status | Notes |
| --------- | ------ | ----- |
| `cg-use-everywhere` | ✅ Installed | Allows connecting nodes without physical links (wireless connections). |
| `comfyui-advanced-controlnet` | ✅ Installed | ControlNet scheduling across timesteps and batched latents. |
| `comfyui-art-venture` | ✅ Installed | Image processing utilities and art-focused nodes. |
| `ComfyUI_Comfyroll_CustomNodes` | ✅ Installed | General utility nodes by Suzie1 and RockOfFire. |
| `comfyui_controlnet_aux` | ✅ Installed | Plug-and-play ControlNet preprocessors (OpenPose, Canny, Depth, etc.). |
| `ComfyUI-Crystools` | ✅ Installed | Dev tools: resource monitor, progress bar, pipe nodes. |
| `comfyui-easy-use` | ✅ Installed | Simplified node workflows and pipe systems. |
| `comfyui_essentials` | ✅ Installed | Essential nodes missing from ComfyUI core. |
| `comfyui-ic-light` | ✅ Installed | IC-Light relighting models. |
| `ComfyUI-Image-Filters` | ✅ Installed | Image processing and filter nodes. |
| `comfyui-impact-pack` | ✅ Installed | Detection, segmentation, and detailer nodes (FaceDetailer, etc.). |
| `comfyui-impact-subpack` | ✅ Installed | Complements Impact Pack with additional detectors. |
| `ComfyUI-IndexTTS2` | ✅ Installed | Voice cloning + emotion control. Requires `wetext` (not `pynini`). Models in `Huggingface/IndexTTS2/` → `custom_nodes/ComfyUI-IndexTTS2/checkpoints/`. Patched for `transformers 5.8.1` compat. |
| `ComfyUI-Inspire-Pack` | ✅ Installed | Various utility nodes. |
| `comfyui_ipadapter_plus` | ✅ Installed | IPAdapter for SDXL. Requires `clip_vision/` + `ipadapter/` models. |
| `comfyui-kjnodes` | ✅ Installed | Utility, model optimization, and QoL nodes. |
| `comfyui-local-gemini` | ✅ Installed | **Private direct API nodes** for Google Gemini, ElevenLabs TTS, FAL Kling, and **FAL Seedance 2.0**. Uses user's own API keys. Separate git repo (gitignored). |
| `comfyui-multi-subtitle` | ✅ Installed | Whisper-based multi-language subtitle generation. |
| `comfyui_tinyterranodes` | ✅ Installed | Small utility node collection. |
| `comfyui_ultimatesdupscale` | ✅ Installed | Ultimate SD Upscale for high-res image generation. |
| `comfyui-various` | ✅ Installed | General-purpose utility nodes. |
| `comfyui-video-matting` | ✅ Installed | Robust Video Matting (RVM) for background removal. |
| `comfyui-voxcpm-pipeline` | ✅ Installed | VoxCPM voice cloning TTS pipeline. |
| `comfyui-wd14-tagger` | ✅ Installed | WD14 image tagging for prompt generation. |
| `comfyui-ycyy-lorainfo` | ✅ Installed | LoRA metadata display and info nodes. |
| `efficiency-nodes-comfyui` | ✅ Installed | Efficiency-focused workflow nodes (KSampler variants, etc.). |
| `rgthree-comfy` | ✅ Installed | rgthree's utility nodes: progress bars, display nodes, bookmarks. |
