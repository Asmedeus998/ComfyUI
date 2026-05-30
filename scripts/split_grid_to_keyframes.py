#!/usr/bin/env python3
"""
Split a 3x3 storyboard grid into 9 individual panels saved to output/keyframes/.
Usage: python split_grid_to_keyframes.py <input_grid.png> [output_prefix]
"""

import sys
import os
from PIL import Image

# Add ComfyUI root to path so we can use folder_paths if needed
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def split_grid(image_path: str, rows: int = 3, cols: int = 3, margin: int = 0):
    img = Image.open(image_path).convert("RGB")
    w, h = img.size
    cell_w = w // cols
    cell_h = h // rows

    panels = []
    for r in range(rows):
        for c in range(cols):
            x1 = c * cell_w + margin
            y1 = r * cell_h + margin
            x2 = (c + 1) * cell_w - margin
            y2 = (r + 1) * cell_h - margin
            panel = img.crop((x1, y1, x2, y2))
            panels.append(panel)
    return panels


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input_grid.png> [output_prefix]")
        print(f"Example: {sys.argv[0]} output/ads_frame_00001_.png storyboard")
        sys.exit(1)

    input_path = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) > 2 else "storyboard_panel"

    if not os.path.exists(input_path):
        print(f"Error: file not found: {input_path}")
        sys.exit(1)

    # Resolve output directory
    comfy_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(comfy_root, "output", "keyframes")
    os.makedirs(output_dir, exist_ok=True)

    panels = split_grid(input_path, rows=3, cols=3, margin=0)

    base_name = os.path.splitext(os.path.basename(input_path))[0]

    for idx, panel in enumerate(panels, start=1):
        # filename: storyboard_panel_00001_.png
        out_name = f"{prefix}_{idx:05d}_.png"
        out_path = os.path.join(output_dir, out_name)
        panel.save(out_path)
        print(f"  Saved panel {idx}/9 -> {out_path}")

    print(f"\nDone. {len(panels)} panels saved to {output_dir}/")


if __name__ == "__main__":
    main()
