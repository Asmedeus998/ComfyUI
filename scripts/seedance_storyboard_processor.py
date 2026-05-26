#!/usr/bin/env python3
"""
Seedance 2.0 Storyboard Processor
=================================
Extracts individual shot frames from a TV commercial storyboard image
and generates optimized Seedance 2.0 prompts + ComfyUI workflow configs.

Usage:
    cd /home/yumeko/github/ComfyUI
    source .venv/bin/activate
    python scripts/seedance_storyboard_processor.py \
        --input output/GPT_Image_2_00009_.png \
        --output output/seedance_botanika

The script auto-detects the 5 shot thumbnails, crops them, and writes:
    - shot_01.png ... shot_05.png          (cropped frames)
    - prompts.json                          (Seedance 2.0 prompts per shot)
    - workflow_single_video.json            (First-Last-Frame approach)
    - workflow_individual_clips.json        (Per-shot clips approach)
    - workflow_reference.json               (Multi-reference approach)

Seedance 2.0 Prompt Best Practices (from BytePlus docs):
    - Keep prompts between 30-100 words
    - Lead with the subject
    - Describe camera movement explicitly
    - Include style/film references
    - Use temporal storytelling for multi-shot narratives
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image


def detect_storyboard_dividers(brightness: np.ndarray) -> list[int]:
    """Find horizontal divider lines in a storyboard by looking for uniform dark rows."""
    row_mean = np.mean(brightness, axis=1)
    row_std = np.std(brightness, axis=1)

    # A divider should be relatively uniform (low std) and darker than surrounding photo rows
    potential = [
        (y, float(row_mean[y]), float(row_std[y]))
        for y in range(brightness.shape[0])
        if row_std[y] < 35 and row_mean[y] < 90
    ]

    if not potential:
        return []

    # Group consecutive rows
    groups: list[tuple[int, int, int]] = []
    start_y = potential[0][0]
    prev_y = start_y
    for y, _, _ in potential[1:]:
        if y - prev_y <= 2:
            prev_y = y
        else:
            groups.append((start_y, prev_y, (start_y + prev_y) // 2))
            start_y = y
            prev_y = y
    groups.append((start_y, prev_y, (start_y + prev_y) // 2))

    # Filter out the very top header dividers, keep only table-area dividers
    # Typically storyboards have dividers after header, scene obj, col headers, then each shot
    center_y = [g[2] for g in groups if 150 < g[2] < 1450]
    return center_y


def find_photo_x_bounds(brightness: np.ndarray, y0: int, y1: int) -> tuple[int, int]:
    """Find left/right boundaries of the photo thumbnail within a storyboard row.

    Storyboard layout: [shot label | PHOTO THUMBNAIL | text columns ... ]
    The photo ends where there's a sharp jump from photo content to the white
    text-column background. We prioritize that jump over sustained white.
    """
    region = brightness[y0:y1, :]
    col_mean = np.mean(region, axis=0)
    col_std = np.std(region, axis=0)

    # Left boundary: skip the shot label column (white, low std) then find photo
    left_photo = 80  # default safe offset for shot-number column
    in_label = True
    for x in range(min(120, len(col_mean))):
        if in_label:
            # Label column is bright and uniform; photo is darker or more varied
            if col_mean[x] < 220 or col_std[x] > 30:
                left_photo = x
                in_label = False
                break

    # Right boundary: look for the first big brightness jump (>40) after the photo region.
    # This marks the transition from photo to the white text-column background.
    right_photo = brightness.shape[1]
    diff = np.diff(col_mean)
    big_jumps = np.where(diff > 40)[0]
    for jx in big_jumps:
        if jx > left_photo + 100:
            right_photo = jx
            break

    # Fallback: sustained white region (>60 consecutive cols, mean>235, std<20)
    if right_photo == brightness.shape[1]:
        count = 0
        white_start = None
        for x in range(left_photo + 50, len(col_mean)):
            if col_mean[x] > 235 and col_std[x] < 20:
                if white_start is None:
                    white_start = x
                count += 1
                if count >= 60:
                    right_photo = white_start
                    break
            else:
                count = 0
                white_start = None

    # Clamp
    right_photo = min(right_photo, brightness.shape[1] - 1)
    left_photo = min(left_photo, right_photo - 100)

    return int(left_photo), int(right_photo)


def extract_shots(img: Image.Image) -> list[dict[str, Any]]:
    """Extract shot thumbnails and metadata from a storyboard image."""
    arr = np.array(img.convert("RGBA"))
    brightness = np.mean(arr[:, :, :3], axis=2)

    dividers = detect_storyboard_dividers(brightness)
    print(f"[INFO] Detected {len(dividers)} potential divider lines: {dividers}")

    # Heuristic: storyboards typically have dividers in this pattern:
    # header_bottom, scene_obj_bottom, col_header_bottom, shot1_bottom, shot2_bottom, ...
    # We want the shot boundaries. In the BOTANIKA board, the pattern is:
    # y=186 (bottom of headers), y=439, 683, 915, 1127, 1352 (shot dividers)
    # We keep dividers from ~180 onward and group them into shot rows.

    shot_dividers = [d for d in dividers if d >= 180]
    if len(shot_dividers) < 5:
        print(
            f"[WARN] Only {len(shot_dividers)} shot-level dividers found. "
            "Falling back to estimated equal rows."
        )
        # Fallback: estimate 5 equal rows between y=200 and y=1400
        top = 200
        bottom = 1400
        step = (bottom - top) // 5
        shot_dividers = [top + step * i for i in range(1, 6)]

    # Use the divider just above the first shot as the top boundary.
    # We want the last header-level divider before the first shot divider.
    header_candidates = [d for d in dividers if 150 <= d < shot_dividers[0]]
    # Prefer the divider closest to the first shot (usually column-headers bottom)
    top_y = header_candidates[-1] if header_candidates else 180

    # Build shot row boundaries
    rows: list[tuple[int, int]] = []
    prev = top_y + 1
    for d in shot_dividers:
        if d - prev > 50:  # At least 50px tall
            rows.append((prev, d))
            prev = d + 1
        if len(rows) >= 5:
            break

    if len(rows) < 5:
        print(f"[WARN] Only {len(rows)} rows extracted. Using remaining space for last row.")
        if prev < brightness.shape[0] - 50:
            rows.append((prev, brightness.shape[0] - 50))

    shots = []
    for idx, (y0, y1) in enumerate(rows[:5], 1):
        x0, x1 = find_photo_x_bounds(brightness, y0, y1)
        crop = img.crop((x0, y0, x1, y1))
        shots.append(
            {
                "shot_number": idx,
                "crop_box": (x0, y0, x1, y1),
                "size": crop.size,
                "image": crop,
            }
        )
        print(f"[INFO] Shot {idx}: crop=({x0},{y0},{x1},{y1}), size={crop.size}")

    return shots


# =============================================================================
# Seedance 2.0 Prompts (tailored for the BOTANIKA storyboard)
# =============================================================================

SHOT_METADATA = [
    {
        "name": "Timeless Beauty",
        "timecode": "0:00 - 0:03.0",
        "duration": 3.0,
        "vo": "Some traditions never fade. They evolve.",
        "camera": "Medium shot with slow push-in toward mirror reflection.",
        "prompt": (
            "A young East Asian woman in an ornate red embroidered qipao takes an elegant mirror selfie "
            "in a luxurious marble bathroom adorned with dried botanicals and gold accents. "
            "Slow push-in camera movement toward the mirror reflection. "
            "Soft warm golden lighting, shallow depth of field, premium beauty commercial aesthetic. "
            "Her hair is styled in an elaborate updo with decorative pins. "
            "Calm, timeless atmosphere with subtle fabric rustle motion."
        ),
    },
    {
        "name": "The Ritual Begins",
        "timecode": "0:03.0 - 0:05.5",
        "duration": 2.5,
        "vo": "BOTANIKA. Nature's secret to radiant skin.",
        "camera": "Macro close-up with shallow depth of field and slow dolly in.",
        "prompt": (
            "A delicate feminine hand slowly reaches for and gently touches a warm amber BOTANIKA moisturizer "
            "pump bottle on a reflective black marble counter. "
            "Macro close-up with extreme shallow depth of field, slow dolly in. "
            "Soft dramatic side lighting highlights the glass bottle and silver pump. "
            "A vase of dried pampas grass in the soft-focus background. "
            "Premium product photography aesthetic, tactile and luxurious."
        ),
    },
    {
        "name": "Pure Hydration",
        "timecode": "0:05.5 - 0:08.5",
        "duration": 3.0,
        "vo": "Plant-powered. Deeply hydrating. Uniquely you.",
        "camera": "Low angle product hero shot with slow orbit around the bottle.",
        "prompt": (
            "Hero product shot of a warm amber BOTANIKA moisturizer bottle centered on a clean marble surface, "
            "surrounded by fresh green botanical leaves and crystal sphere decorations. "
            "Low angle with slow orbit camera movement around the bottle. "
            "Bright soft natural lighting, dewy water droplets on the bottle surface. "
            "Premium skincare commercial aesthetic, clean and botanical. "
            "Text overlay reads HYDRATING MOISTURIZER, NATURAL INGREDIENTS, PLANT-POWERED."
        ),
    },
    {
        "name": "The Glow",
        "timecode": "0:08.5 - 0:11.5",
        "duration": 3.0,
        "vo": "Feel the hydration. Embrace the glow.",
        "camera": "Extreme close-up with shallow focus and slight handheld intimacy.",
        "prompt": (
            "Extreme close-up of a young East Asian woman with dewy glowing skin gently touching her cheek, "
            "eyes closed with a serene satisfied smile. "
            "Warm golden backlighting creates a radiant halo effect on her skin. "
            "Slight subtle handheld camera intimacy, shallow focus on her face. "
            "Premium beauty commercial aesthetic, authentic natural glow. "
            "Soft ambient light, tranquil and aspirational mood."
        ),
    },
    {
        "name": "Call to Glow",
        "timecode": "0:11.5 - 0:15.0",
        "duration": 3.5,
        "vo": "BOTANIKA. Glow rooted in nature. Shop now.",
        "camera": "Static hero frame with slight zoom in on bottle.",
        "prompt": (
            "Static hero frame of a warm amber BOTANIKA moisturizer bottle centered on a clean cream background "
            "with elegant botanical leaf motifs and the BOTANIKA leaf logo. "
            "Text overlay reads GLOW ROOTED IN NATURE, BOTANIKA, LIMITED TIME OFFER 20 PERCENT OFF, "
            "YOUR FIRST ORDER, and a SHOP NOW button. "
            "Soft even product photography lighting, slight slow zoom in on the bottle. "
            "Premium commercial end-card aesthetic, warm amber and cream color palette."
        ),
    },
]


def build_single_video_prompt() -> str:
    """Build a unified 15-second commercial prompt for First-Last-Frame approach."""
    return (
        "A premium BOTANIKA skincare commercial. "
        "Opening: a young East Asian woman in an ornate red qipao takes an elegant mirror selfie in a luxurious "
        "marble bathroom with gold accents and dried botanicals. "
        "She reaches for a warm amber BOTANIKA moisturizer pump bottle on a black marble counter. "
        "The camera reveals a hero product shot surrounded by fresh green botanical leaves and crystal spheres. "
        "She gently applies the hydrator to her cheek, eyes closed with a serene glowing smile. "
        "Closing on a clean product frame with the BOTANIKA bottle, botanical motifs, and offer text. "
        "Soft golden lighting throughout, premium beauty commercial aesthetic, elegant moderate pacing, "
        "smooth cinematic transitions, shallow depth of field, warm amber and cream color palette."
    )


def build_reference_prompt() -> str:
    """Build a multi-reference prompt for the Reference-to-Video approach."""
    return (
        "Create a premium BOTANIKA skincare TV commercial using all reference images. "
        "Image 1: the woman in red qipao taking a mirror selfie. "
        "Image 2: hand reaching for the BOTANIKA bottle. "
        "Image 3: hero product shot with botanicals and crystals. "
        "Image 4: close-up of glowing skin with satisfied smile. "
        "Image 5: clean product end card with offer text. "
        "Sequence the shots in order with smooth cinematic transitions between each moment. "
        "Soft golden lighting, warm amber tones, premium beauty commercial aesthetic, "
        "elegant moderate pacing, shallow depth of field."
    )


# =============================================================================
# ComfyUI Workflow JSON Builders
# =============================================================================

NODE_ID_COUNTER = 1


def next_id() -> int:
    global NODE_ID_COUNTER
    nid = NODE_ID_COUNTER
    NODE_ID_COUNTER += 1
    return nid


def make_load_image_node(image_path: str) -> dict:
    return {
        "id": next_id(),
        "type": "LoadImage",
        "pos": [0, 0],
        "size": {"0": 315, "1": 314},
        "flags": {},
        "order": 0,
        "mode": 0,
        "inputs": [],
        "outputs": [
            {"name": "IMAGE", "type": "IMAGE", "links": [], "shape": 3},
            {"name": "MASK", "type": "MASK", "links": [], "shape": 3},
        ],
        "properties": {"Node name for S&R": "LoadImage"},
        "widgets_values": [image_path, "image"],
    }


def make_seedance2_firstlast_node(
    first_frame_id: int,
    last_frame_id: int | None = None,
    prompt: str = "",
    model: str = "Seedance 2.0",
    resolution: str = "1080p",
    ratio: str = "16:9",
    duration: int = 15,
    seed: int = 42,
    watermark: bool = False,
    generate_audio: bool = True,
) -> dict:
    """Build a ByteDance2FirstLastFrameNode JSON stub.

    NOTE: This is a simplified workflow stub. In practice you must load it
    into ComfyUI and wire the image connections manually, or use the
    frontend to connect the LoadImage nodes to the first_frame / last_frame
    inputs.
    """
    inputs = [
        {"name": "first_frame", "type": "IMAGE", "link": first_frame_id},
    ]
    if last_frame_id is not None:
        inputs.append({"name": "last_frame", "type": "IMAGE", "link": last_frame_id})

    return {
        "id": next_id(),
        "type": "ByteDance2FirstLastFrameNode",
        "pos": [400, 200],
        "size": {"0": 400, "1": 400},
        "flags": {},
        "order": 1,
        "mode": 0,
        "inputs": inputs,
        "outputs": [{"name": "VIDEO", "type": "VIDEO", "links": [], "shape": 3}],
        "properties": {"Node name for S&R": "ByteDance2FirstLastFrameNode"},
        "widgets_values": [
            {"model": model, "resolution": resolution, "ratio": ratio, "duration": duration, "generate_audio": generate_audio},
            seed,
            watermark,
        ],
    }


def make_seedance2_reference_node(
    image_ids: list[int],
    prompt: str = "",
    model: str = "Seedance 2.0",
    resolution: str = "1080p",
    ratio: str = "16:9",
    duration: int = 15,
    seed: int = 42,
    watermark: bool = False,
    generate_audio: bool = True,
) -> dict:
    inputs = []
    for img_id in image_ids:
        inputs.append({"name": "reference_image", "type": "IMAGE", "link": img_id})

    return {
        "id": next_id(),
        "type": "ByteDance2ReferenceNode",
        "pos": [400, 200],
        "size": {"0": 400, "1": 500},
        "flags": {},
        "order": 1,
        "mode": 0,
        "inputs": inputs,
        "outputs": [{"name": "VIDEO", "type": "VIDEO", "links": [], "shape": 3}],
        "properties": {"Node name for S&R": "ByteDance2ReferenceNode"},
        "widgets_values": [
            {"model": model, "resolution": resolution, "ratio": ratio, "duration": duration, "generate_audio": generate_audio},
            seed,
            watermark,
        ],
    }


def build_workflow_single_video(output_dir: Path, first_frame_path: str, last_frame_path: str) -> dict:
    """Build a ComfyUI workflow JSON for the single-video first-last-frame approach."""
    global NODE_ID_COUNTER
    NODE_ID_COUNTER = 1

    first_node = make_load_image_node(first_frame_path)
    last_node = make_load_image_node(last_frame_path)
    video_node = make_seedance2_firstlast_node(
        first_frame_id=first_node["id"],
        last_frame_id=last_node["id"],
        prompt=build_single_video_prompt(),
        model="Seedance 2.0",
        resolution="1080p",
        ratio="16:9",
        duration=15,
        seed=42,
        watermark=False,
        generate_audio=True,
    )

    # Link first_frame
    video_node["inputs"][0]["link"] = first_node["outputs"][0]["links"].append(
        video_node["id"]
    ) or video_node["id"]
    # Link last_frame
    video_node["inputs"][1]["link"] = last_node["outputs"][0]["links"].append(
        video_node["id"]
    ) or video_node["id"]

    return {
        "last_node_id": NODE_ID_COUNTER,
        "last_link_id": NODE_ID_COUNTER,
        "nodes": [first_node, last_node, video_node],
        "links": [],
        "groups": [],
        "config": {},
        "extra": {},
        "version": 0.4,
    }


def build_workflow_reference(output_dir: Path, image_paths: list[str]) -> dict:
    """Build a ComfyUI workflow JSON for the multi-reference approach."""
    global NODE_ID_COUNTER
    NODE_ID_COUNTER = 1

    image_nodes = [make_load_image_node(p) for p in image_paths]
    video_node = make_seedance2_reference_node(
        image_ids=[n["id"] for n in image_nodes],
        prompt=build_reference_prompt(),
        model="Seedance 2.0",
        resolution="1080p",
        ratio="16:9",
        duration=15,
        seed=42,
        watermark=False,
        generate_audio=True,
    )

    # Wire links
    for i, img_node in enumerate(image_nodes):
        video_node["inputs"][i]["link"] = img_node["outputs"][0]["links"].append(
            video_node["id"]
        ) or video_node["id"]

    return {
        "last_node_id": NODE_ID_COUNTER,
        "last_link_id": NODE_ID_COUNTER,
        "nodes": image_nodes + [video_node],
        "links": [],
        "groups": [],
        "config": {},
        "extra": {},
        "version": 0.4,
    }


# =============================================================================
# Main
# =============================================================================


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract storyboard shots and prepare Seedance 2.0 assets")
    parser.add_argument("--input", "-i", required=True, help="Path to storyboard PNG")
    parser.add_argument("--output", "-o", required=True, help="Output directory")
    parser.add_argument("--duration", "-d", type=int, default=15, help="Total commercial duration in seconds")
    parser.add_argument("--resolution", "-r", default="1080p", choices=["480p", "720p", "1080p"])
    parser.add_argument("--ratio", default="16:9", choices=["16:9", "4:3", "1:1", "3:4", "9:16", "21:9"])
    parser.add_argument("--seed", "-s", type=int, default=42, help="Seed for generation")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"[ERROR] Input file not found: {input_path}")
        return 1

    print(f"[INFO] Loading storyboard: {input_path}")
    img = Image.open(input_path)
    print(f"[INFO] Image size: {img.size}")

    shots = extract_shots(img)
    if len(shots) != 5:
        print(f"[WARN] Expected 5 shots, got {len(shots)}. Adjusting...")

    # Save cropped frames
    shot_paths: list[str] = []
    for shot, meta in zip(shots, SHOT_METADATA):
        fname = f"shot_{shot['shot_number']:02d}_{meta['name'].lower().replace(' ', '_')}.png"
        fpath = output_dir / fname
        shot["image"].save(fpath)
        shot_paths.append(str(fpath))
        print(f"[SAVED] {fpath}")

    # Build prompts metadata
    prompts_data = {
        "storyboard": str(input_path),
        "total_duration_sec": args.duration,
        "resolution": args.resolution,
        "ratio": args.ratio,
        "seed": args.seed,
        "approaches": {
            "single_video_first_last_frame": {
                "description": "One 15s video using Shot 1 as first frame and Shot 5 as last frame.",
                "recommended_node": "ByteDance2FirstLastFrameNode",
                "first_frame": shot_paths[0],
                "last_frame": shot_paths[4],
                "duration": args.duration,
                "prompt": build_single_video_prompt(),
            },
            "individual_clips": {
                "description": "Generate each shot as a separate video clip, then edit together.",
                "recommended_node": "ByteDance2FirstLastFrameNode (per shot)",
                "shots": [],
            },
            "multi_reference": {
                "description": "One 15s video using all 5 shots as reference images.",
                "recommended_node": "ByteDance2ReferenceNode",
                "reference_images": shot_paths,
                "duration": args.duration,
                "prompt": build_reference_prompt(),
            },
        },
        "seedance_2_0_best_practices": [
            "Keep prompts between 30-100 words for best results.",
            "Lead with the subject (character, product, or scene).",
            "Describe camera movement explicitly (push-in, dolly, orbit, handheld).",
            "Include style references (premium beauty commercial, cinematic, etc.).",
            "Use temporal storytelling for multi-shot narratives (opening, middle, closing).",
            "For First-Last-Frame: the prompt should bridge the visual gap between frames.",
            "For Reference mode: mention 'Image N' in the prompt to guide which reference to follow.",
        ],
    }

    for shot, meta in zip(shots, SHOT_METADATA):
        prompts_data["approaches"]["individual_clips"]["shots"].append(
            {
                "shot_number": shot["shot_number"],
                "name": meta["name"],
                "timecode": meta["timecode"],
                "duration_sec": meta["duration"],
                "first_frame": shot_paths[shot["shot_number"] - 1],
                "vo": meta["vo"],
                "camera": meta["camera"],
                "prompt": meta["prompt"],
            }
        )

    prompts_json = output_dir / "prompts.json"
    with open(prompts_json, "w", encoding="utf-8") as f:
        json.dump(prompts_data, f, indent=2, ensure_ascii=False)
    print(f"[SAVED] {prompts_json}")

    # Build workflow stubs
    wf_single = build_workflow_single_video(output_dir, shot_paths[0], shot_paths[4])
    wf_single_path = output_dir / "workflow_single_video.json"
    with open(wf_single_path, "w", encoding="utf-8") as f:
        json.dump(wf_single, f, indent=2)
    print(f"[SAVED] {wf_single_path}")

    wf_ref = build_workflow_reference(output_dir, shot_paths)
    wf_ref_path = output_dir / "workflow_reference.json"
    with open(wf_ref_path, "w", encoding="utf-8") as f:
        json.dump(wf_ref, f, indent=2)
    print(f"[SAVED] {wf_ref_path}")

    # Write a simple per-shot workflow template (users duplicate this for each shot)
    wf_individual = build_workflow_single_video(output_dir, shot_paths[0], shot_paths[0])
    wf_individual["nodes"][0]["widgets_values"][0] = shot_paths[0]  # will be overwritten per shot
    wf_individual_path = output_dir / "workflow_individual_template.json"
    with open(wf_individual_path, "w", encoding="utf-8") as f:
        json.dump(wf_individual, f, indent=2)
    print(f"[SAVED] {wf_individual_path}")

    # Write a human-readable production brief
    brief_path = output_dir / "production_brief.md"
    with open(brief_path, "w", encoding="utf-8") as f:
        f.write("# BOTANIKA Commercial — Seedance 2.0 Production Brief\n\n")
        f.write(f"**Source Storyboard:** `{input_path}`\n\n")
        f.write("## Extracted Shot Frames\n\n")
        for shot, meta in zip(shots, SHOT_METADATA):
            f.write(f"### Shot {shot['shot_number']}: {meta['name']}\n")
            f.write(f"- **Timecode:** {meta['timecode']}\n")
            f.write(f"- **Duration:** {meta['duration']}s\n")
            f.write(f"- **VO:** \"{meta['vo']}\"\n")
            f.write(f"- **Camera:** {meta['camera']}\n")
            f.write(f"- **Frame:** `{shot_paths[shot['shot_number'] - 1]}`\n")
            f.write(f"- **Seedance Prompt:**\n```\n{meta['prompt']}\n```\n\n")

        f.write("## Approach A: Single 15s Video (First-Last-Frame)\n\n")
        f.write(f"**Node:** `ByteDance2FirstLastFrameNode`\n")
        f.write(f"**First Frame:** Shot 1 (`{shot_paths[0]}`)\n")
        f.write(f"**Last Frame:** Shot 5 (`{shot_paths[4]}`)\n")
        f.write(f"**Duration:** {args.duration}s\n")
        f.write(f"**Prompt:**\n```\n{build_single_video_prompt()}\n```\n\n")

        f.write("## Approach B: Multi-Reference Video\n\n")
        f.write(f"**Node:** `ByteDance2ReferenceNode`\n")
        f.write(f"**References:** All 5 shots\n")
        f.write(f"**Duration:** {args.duration}s\n")
        f.write(f"**Prompt:**\n```\n{build_reference_prompt()}\n```\n\n")

        f.write("## Approach C: Individual Clips + Edit\n\n")
        f.write("Generate each shot as a separate video using `ByteDance2FirstLastFrameNode` ")
        f.write("with the shot frame as both first and last frame (or just first frame). ")
        f.write("Combine in your video editor to match the storyboard timing.\n\n")
        f.write("| Shot | Duration | Suggested Resolution |\n")
        f.write("|------|----------|---------------------|\n")
        for meta in SHOT_METADATA:
            f.write(f"| {meta['name']} | {meta['duration']}s | {args.resolution} |\n")

        f.write("\n## Seedance 2.0 Settings\n\n")
        f.write(f"- **Model:** Seedance 2.0\n")
        f.write(f"- **Resolution:** {args.resolution}\n")
        f.write(f"- **Aspect Ratio:** {args.ratio}\n")
        f.write(f"- **Seed:** {args.seed}\n")
        f.write(f"- **Audio:** Enabled (recommended for commercials)\n")
        f.write(f"- **Watermark:** Disabled\n")

    print(f"[SAVED] {brief_path}")
    print("\n[INFO] Done! Next steps:")
    print(f"  1. Review extracted shots in: {output_dir}/")
    print(f"  2. Load workflow JSON into ComfyUI (or use the prompts manually)")
    print(f"  3. For API nodes, ensure you're authenticated with ComfyUI")
    return 0


if __name__ == "__main__":
    sys.exit(main())
