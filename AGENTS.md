# Agent Guidelines for ComfyUI

## Environment

- **Python environment**: This project uses `uv` for package management. Use `uv pip install ...` instead of `pip install ...`.
- **Download tool**: Always use `aria2c` for downloading files (models, LoRAs, datasets, etc.). Do **not** use `wget` or `curl` for large/binary downloads.
  - Preferred flags: `aria2c -x 4 -s 4 --dir=<output_dir> --out=<filename> <url>`
- **Custom nodes**: Clone into `custom_nodes/`. This directory is gitignored; do not commit custom node sub-repos.

## Model Storage (IMPORTANT)

- **All models MUST be saved to the NAS**, not directly into the local repo's `models/` folders.
  - NAS base path: `/mnt/storage/comfyui_data/CivitAI/`
  - The project uses `scripts/link_nas_models.sh` to symlink from the NAS into `models/`.
- **Existing categories** on the NAS (save to the appropriate folder):
  - `Model/` → `models/checkpoints`
  - `NSFW_model/` → `models/checkpoints`
  - `VAE/` → `models/vae`
  - `LORA/`, `NSFW_LORA/`, `LORA_character/`, `Lora_clothes/`, `Lora_style/` → `models/loras`
  - `Embedding/` → `models/embeddings`
  - `upscale/` → `models/upscale_models`
  - `ControlNet/` → `models/controlnet`
- **If a category doesn't exist yet**:
  1. Create the folder under `/mnt/storage/comfyui_data/CivitAI/<Category>/`
  2. Save the downloaded model there.
  3. Symlink it into the corresponding `models/` directory.
  4. Update `scripts/link_nas_models.sh` so future models of that type are auto-linked.
