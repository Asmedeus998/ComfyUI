# Agent Guidelines for ComfyUI

## Environment

- **Python environment**: This project uses `uv` for package management. Use `uv pip install ...` instead of `pip install ...`.
- **Download tool**: Always use `aria2c` for downloading files (models, LoRAs, datasets, etc.). Do **not** use `wget` or `curl` for large/binary downloads.
  - Preferred flags: `aria2c -x 4 -s 4 --dir=<output_dir> --out=<filename> <url>`
- **Custom nodes**: Clone into `custom_nodes/`. This directory is gitignored; do not commit custom node sub-repos.
