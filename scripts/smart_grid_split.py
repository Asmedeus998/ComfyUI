#!/usr/bin/env python3
"""
Smart 3x3 grid splitter.
Auto-detects and crops out headers, footers, and side margins,
then splits the remaining content into 9 clean panels.

Usage:
    python smart_grid_split.py <input_grid.png> [output_prefix]
    python smart_grid_split.py output/ads_frame_00002_.png storyboard
"""

import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def find_content_bounds(arr, white_threshold=248, var_threshold=500):
    """
    Find the bounding box of actual image content by detecting
    white margins (headers, footers, side bars).

    A row/column is considered "margin" if it is BOTH very bright
    (near-white) AND has low variance (uniform or text-on-white).
    var_threshold=500 works well for separating text-on-white headers
    from actual photographic image content.
    """
    h, w, _ = arr.shape
    gray = arr.mean(axis=2)

    row_mean = gray.mean(axis=1)
    row_var = gray.var(axis=1)
    row_is_content = (row_mean < white_threshold) | (row_var > var_threshold)

    col_mean = gray.mean(axis=0)
    col_var = gray.var(axis=0)
    col_is_content = (col_mean < white_threshold) | (col_var > var_threshold)

    y1 = 0
    for i in range(h):
        if row_is_content[i]:
            y1 = i
            break

    y2 = h
    for i in range(h - 1, -1, -1):
        if row_is_content[i]:
            y2 = i + 1
            break

    x1 = 0
    for i in range(w):
        if col_is_content[i]:
            x1 = i
            break

    x2 = w
    for i in range(w - 1, -1, -1):
        if col_is_content[i]:
            x2 = i + 1
            break

    # Sanity check
    if y2 - y1 < h * 0.4:
        y1 = int(h * 0.05)
        y2 = int(h * 0.95)
    if x2 - x1 < w * 0.4:
        x1 = int(w * 0.02)
        x2 = int(w * 0.98)

    return x1, y1, x2, y2


def split_grid_smart(image_path: str, rows: int = 3, cols: int = 3):
    img = Image.open(image_path).convert("RGB")
    arr = np.array(img)
    h, w, _ = arr.shape

    print(f"Input: {w}x{h}")

    x1, y1, x2, y2 = find_content_bounds(arr)
    print(f"Detected content bounds: ({x1}, {y1}) -> ({x2}, {y2})")
    print(f"  Cropped away top={y1}px, bottom={h-y2}px, left={x1}px, right={w-x2}px")

    content = arr[y1:y2, x1:x2]
    ch, cw = content.shape[:2]
    print(f"Content size: {cw}x{ch}")

    cell_h = ch // rows
    cell_w = cw // cols
    print(f"Cell size: {cell_w}x{cell_h} (remainder w={cw % cols}, h={ch % rows})")

    panels = []
    for r in range(rows):
        for c in range(cols):
            cy1 = r * cell_h
            cy2 = (r + 1) * cell_h
            cx1 = c * cell_w
            cx2 = (c + 1) * cell_w
            panel = content[cy1:cy2, cx1:cx2]
            panels.append(Image.fromarray(panel))

    return panels


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input_grid.png> [output_prefix]")
        sys.exit(1)

    input_path = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) > 2 else "storyboard_panel"

    if not os.path.exists(input_path):
        print(f"Error: file not found: {input_path}")
        sys.exit(1)

    comfy_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(comfy_root, "output", "keyframes")
    os.makedirs(output_dir, exist_ok=True)

    panels = split_grid_smart(input_path, rows=3, cols=3)

    for idx, panel in enumerate(panels, start=1):
        out_name = f"{prefix}_{idx:05d}_.png"
        out_path = os.path.join(output_dir, out_name)
        panel.save(out_path)
        print(f"  Saved panel {idx}/9 -> {out_path} ({panel.size[0]}x{panel.size[1]})")

    print(f"\nDone. {len(panels)} panels saved to {output_dir}/")


if __name__ == "__main__":
    main()
