#!/usr/bin/env python3
"""
Convert SEEDANCE 2.0 workflows from ByteDance comfy_api_nodes to local FAL Seedance nodes.
Also converts GeminiNode to GoogleGeminiDirect where present.
Outputs new files with '_local.json' suffix; never overwrites originals.
"""

import json
import copy
import sys
from pathlib import Path

WORKFLOW_DIR = Path("/home/yumeko/github/ComfyUI/user/default/workflows/SEEDANCE2.0")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path: Path, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def find_node(nodes: list, node_id: int) -> dict | None:
    for n in nodes:
        if n["id"] == node_id:
            return n
    return None

def remove_node_and_links(wf: dict, node_id: int):
    """Remove a node and any links connected to it."""
    wf["nodes"] = [n for n in wf["nodes"] if n["id"] != node_id]
    wf["links"] = [lk for lk in wf["links"] if lk[1] != node_id and lk[3] != node_id]

def sync_links_to_nodes(wf: dict):
    """
    Rebuild every node's input 'link' and output 'links' fields
    so they exactly match the global 'links' array.
    """
    # Reset all link references
    for n in wf["nodes"]:
        for inp in n.get("inputs", []):
            inp["link"] = None
        for out in n.get("outputs", []):
            out["links"] = None

    # Re-apply from global links
    for lk in wf["links"]:
        link_id, origin_id, origin_slot, target_id, target_slot, link_type = lk

        # Update target node's input
        target_node = find_node(wf["nodes"], target_id)
        if target_node:
            inputs = target_node.get("inputs", [])
            if 0 <= target_slot < len(inputs):
                inputs[target_slot]["link"] = link_id

        # Update origin node's output
        origin_node = find_node(wf["nodes"], origin_id)
        if origin_node:
            outputs = origin_node.get("outputs", [])
            if 0 <= origin_slot < len(outputs):
                out = outputs[origin_slot]
                if out.get("links") is None:
                    out["links"] = []
                if link_id not in out["links"]:
                    out["links"].append(link_id)


def cleanup_stale_links(wf: dict):
    """Remove link IDs from node outputs that no longer exist in the global links array."""
    link_ids = {lk[0] for lk in wf["links"]}
    for n in wf["nodes"]:
        for out in n.get("outputs", []):
            if out.get("links"):
                out["links"] = [lid for lid in out["links"] if lid in link_ids]
                if not out["links"]:
                    out["links"] = None


def remove_empty_groups(wf: dict):
    """Remove groups that no longer contain any nodes."""
    if "groups" not in wf:
        return
    # Build a set of node positions to check group containment
    # ComfyUI groups use bounding [x, y, width, height]
    kept_groups = []
    for g in wf["groups"]:
        bx, by, bw, bh = g["bounding"]
        has_nodes = False
        for n in wf["nodes"]:
            nx, ny = n.get("pos", [0, 0])
            # Allow a small margin; nodes exactly on the edge count as inside
            if bx <= nx <= bx + bw and by <= ny <= by + bh:
                has_nodes = True
                break
        if has_nodes:
            kept_groups.append(g)
    wf["groups"] = kept_groups


def remove_outdated_markdown(wf: dict, keywords: list[str]):
    """Remove MarkdownNote nodes whose text contains any of the keywords."""
    to_remove = []
    for n in wf["nodes"]:
        if n["type"] == "MarkdownNote":
            text = " ".join(n.get("widgets_values", []))
            if any(kw.lower() in text.lower() for kw in keywords):
                to_remove.append(n["id"])
    for nid in to_remove:
        remove_node_and_links(wf, nid)


# ---------------------------------------------------------------------------
# Node builders
# ---------------------------------------------------------------------------

def build_fal_seedance_text2video(old_node: dict, wf: dict = None) -> dict:
    """ByteDance2TextToVideoNode -> FALSeedanceText2Video"""
    old_wv = old_node.get("widgets_values", [])
    # old widgets: [model, prompt, resolution, ratio, duration, generate_audio, seed, seed_control, watermark]
    prompt = old_wv[1] if len(old_wv) > 1 else ""
    resolution = old_wv[2] if len(old_wv) > 2 else "720p"
    aspect_ratio = old_wv[3] if len(old_wv) > 3 else "16:9"
    duration = old_wv[4] if len(old_wv) > 4 else 5
    generate_audio = old_wv[5] if len(old_wv) > 5 else True
    seed = old_wv[6] if len(old_wv) > 6 else 0
    seed_control = old_wv[7] if len(old_wv) > 7 else "randomize"
    watermark = old_wv[8] if len(old_wv) > 8 else False

    node = copy.deepcopy(old_node)
    node["type"] = "FALSeedanceText2Video"
    node["inputs"] = [
        {"name": "api_key", "type": "STRING", "widget": {"name": "api_key"}, "link": None},
        {"name": "prompt", "type": "STRING", "widget": {"name": "prompt"}, "link": None},
        {"name": "resolution", "type": "COMBO", "widget": {"name": "resolution"}, "link": None},
        {"name": "aspect_ratio", "type": "COMBO", "widget": {"name": "aspect_ratio"}, "link": None},
        {"name": "duration", "type": "INT", "widget": {"name": "duration"}, "link": None},
        {"name": "generate_audio", "type": "BOOLEAN", "widget": {"name": "generate_audio"}, "link": None},
        {"name": "seed", "type": "INT", "widget": {"name": "seed"}, "link": None},
        {"name": "watermark", "type": "BOOLEAN", "widget": {"name": "watermark"}, "link": None},
        {"name": "fast", "type": "BOOLEAN", "widget": {"name": "fast"}, "link": None},
    ]
    node["outputs"] = [{"name": "video", "type": "VIDEO", "links": old_node.get("outputs", [{}])[0].get("links", [])}]
    node["widgets_values"] = ["", prompt, resolution, aspect_ratio, duration, generate_audio, seed, seed_control, watermark, False]
    if "properties" in node:
        node["properties"]["Node name for S&R"] = "FALSeedanceText2Video"
    return node


def build_fal_seedance_image2video(old_node: dict, wf: dict) -> dict:
    """ByteDance2FirstLastFrameNode -> FALSeedanceImage2Video"""
    old_wv = old_node.get("widgets_values", [])
    # old: [model, prompt, resolution, ratio, duration, generate_audio, seed, seed_control, watermark, first_frame_asset_id, last_frame_asset_id]
    prompt = old_wv[1] if len(old_wv) > 1 else ""
    resolution = old_wv[2] if len(old_wv) > 2 else "720p"
    aspect_ratio = old_wv[3] if len(old_wv) > 3 else "16:9"
    duration = old_wv[4] if len(old_wv) > 4 else 5
    generate_audio = old_wv[5] if len(old_wv) > 5 else True
    seed = old_wv[6] if len(old_wv) > 6 else 0
    seed_control = old_wv[7] if len(old_wv) > 7 else "randomize"
    watermark = old_wv[8] if len(old_wv) > 8 else False

    node = copy.deepcopy(old_node)
    node["type"] = "FALSeedanceImage2Video"

    # Preserve image links
    old_inputs = old_node.get("inputs", [])
    first_frame_link = None
    last_frame_link = None
    for inp in old_inputs:
        if inp.get("name") == "first_frame":
            first_frame_link = inp.get("link")
        elif inp.get("name") == "last_frame":
            last_frame_link = inp.get("link")

    node["inputs"] = [
        {"name": "api_key", "type": "STRING", "widget": {"name": "api_key"}, "link": None},
        {"name": "prompt", "type": "STRING", "widget": {"name": "prompt"}, "link": None},
        {"name": "image", "type": "IMAGE", "link": first_frame_link},
        {"name": "end_image", "type": "IMAGE", "link": last_frame_link},
        {"name": "resolution", "type": "COMBO", "widget": {"name": "resolution"}, "link": None},
        {"name": "aspect_ratio", "type": "COMBO", "widget": {"name": "aspect_ratio"}, "link": None},
        {"name": "duration", "type": "INT", "widget": {"name": "duration"}, "link": None},
        {"name": "generate_audio", "type": "BOOLEAN", "widget": {"name": "generate_audio"}, "link": None},
        {"name": "seed", "type": "INT", "widget": {"name": "seed"}, "link": None},
        {"name": "watermark", "type": "BOOLEAN", "widget": {"name": "watermark"}, "link": None},
        {"name": "fast", "type": "BOOLEAN", "widget": {"name": "fast"}, "link": None},
    ]
    node["outputs"] = [{"name": "video", "type": "VIDEO", "links": old_node.get("outputs", [{}])[0].get("links", [])}]
    node["widgets_values"] = ["", prompt, resolution, aspect_ratio, duration, generate_audio, seed, seed_control, watermark, False]
    if "properties" in node:
        node["properties"]["Node name for S&R"] = "FALSeedanceImage2Video"
    return node


def build_fal_seedance_reference2video(old_node: dict, wf: dict) -> dict:
    """ByteDance2ReferenceNode -> FALSeedanceReference2Video"""
    old_wv = old_node.get("widgets_values", [])
    # old: [model, prompt, resolution, ratio, duration, generate_audio, auto_downscale, seed, seed_control, watermark]
    prompt = old_wv[1] if len(old_wv) > 1 else ""
    resolution = old_wv[2] if len(old_wv) > 2 else "720p"
    aspect_ratio = old_wv[3] if len(old_wv) > 3 else "16:9"
    duration = old_wv[4] if len(old_wv) > 4 else 5
    generate_audio = old_wv[5] if len(old_wv) > 5 else True
    seed = old_wv[7] if len(old_wv) > 7 else 0
    seed_control = old_wv[8] if len(old_wv) > 8 else "randomize"
    watermark = old_wv[9] if len(old_wv) > 9 else False

    node = copy.deepcopy(old_node)
    node["type"] = "FALSeedanceReference2Video"

    # Map old image/video/audio inputs to new slots
    old_inputs = old_node.get("inputs", [])
    image_links = {}
    video_link = None
    audio_link = None
    for inp in old_inputs:
        name = inp.get("name", "")
        if "reference_images.image_" in name:
            idx = name.split("image_")[-1]
            image_links[f"image_{idx}"] = inp.get("link")
        elif "reference_videos.video_1" in name:
            video_link = inp.get("link")
        elif "reference_audios.audio_1" in name:
            audio_link = inp.get("link")

    inputs = [
        {"name": "api_key", "type": "STRING", "widget": {"name": "api_key"}, "link": None},
        {"name": "prompt", "type": "STRING", "widget": {"name": "prompt"}, "link": None},
        {"name": "resolution", "type": "COMBO", "widget": {"name": "resolution"}, "link": None},
        {"name": "aspect_ratio", "type": "COMBO", "widget": {"name": "aspect_ratio"}, "link": None},
        {"name": "duration", "type": "INT", "widget": {"name": "duration"}, "link": None},
        {"name": "generate_audio", "type": "BOOLEAN", "widget": {"name": "generate_audio"}, "link": None},
        {"name": "seed", "type": "INT", "widget": {"name": "seed"}, "link": None},
        {"name": "watermark", "type": "BOOLEAN", "widget": {"name": "watermark"}, "link": None},
        {"name": "fast", "type": "BOOLEAN", "widget": {"name": "fast"}, "link": None},
    ]
    # Add optional image inputs image_1..image_9
    for i in range(1, 10):
        key = f"image_{i}"
        inputs.append({"name": key, "type": "IMAGE", "link": image_links.get(key)})
    # Optionally preserve video/audio links if they exist (node will error at runtime if used)
    if video_link is not None:
        inputs.append({"name": "video_1", "type": "VIDEO", "link": video_link})
    if audio_link is not None:
        inputs.append({"name": "audio_1", "type": "AUDIO", "link": audio_link})

    node["inputs"] = inputs
    node["outputs"] = [{"name": "video", "type": "VIDEO", "links": old_node.get("outputs", [{}])[0].get("links", [])}]
    node["widgets_values"] = ["", prompt, resolution, aspect_ratio, duration, generate_audio, seed, seed_control, watermark, False]
    if "properties" in node:
        node["properties"]["Node name for S&R"] = "FALSeedanceReference2Video"
    return node


def build_google_gemini_direct(old_node: dict, wf: dict) -> dict:
    """GeminiNode -> GoogleGeminiDirect"""
    old_wv = old_node.get("widgets_values", [])
    # old: [prompt, model, seed, seed_control, system_prompt]
    prompt = old_wv[0] if len(old_wv) > 0 else ""
    model = old_wv[1] if len(old_wv) > 1 else "gemini-3.1-pro-preview"
    # Map old model names to new ones
    model_map = {
        "gemini-3-1-pro": "gemini-3.1-pro-preview",
        "gemini-3-pro": "gemini-3-pro-preview",
        "gemini-3.1-flash-image": "gemini-3.1-flash-image-preview",
    }
    model = model_map.get(model, model)
    seed = old_wv[2] if len(old_wv) > 2 else 0
    seed_control = old_wv[3] if len(old_wv) > 3 else "randomize"
    system_prompt = old_wv[4] if len(old_wv) > 4 else ""

    # Preserve image link
    old_inputs = old_node.get("inputs", [])
    image_link = None
    for inp in old_inputs:
        if inp.get("name") == "images":
            image_link = inp.get("link")

    node = copy.deepcopy(old_node)
    node["type"] = "GoogleGeminiDirect"
    node["inputs"] = [
        {"name": "api_key", "type": "STRING", "widget": {"name": "api_key"}, "link": None},
        {"name": "prompt", "type": "STRING", "widget": {"name": "prompt"}, "link": None},
        {"name": "model", "type": "COMBO", "widget": {"name": "model"}, "link": None},
        {"name": "seed", "type": "INT", "widget": {"name": "seed"}, "link": None},
        {"name": "aspect_ratio", "type": "COMBO", "widget": {"name": "aspect_ratio"}, "link": None},
        {"name": "resolution", "type": "COMBO", "widget": {"name": "resolution"}, "link": None},
        {"name": "response_modalities", "type": "COMBO", "widget": {"name": "response_modalities"}, "link": None},
        {"name": "images", "type": "IMAGE", "link": image_link},
        {"name": "system_prompt", "type": "STRING", "widget": {"name": "system_prompt"}, "link": None},
    ]
    # Output 0 = STRING (response), Output 1 = IMAGE
    old_output_links = old_node.get("outputs", [{}])[0].get("links", [])
    node["outputs"] = [
        {"name": "response", "type": "STRING", "links": old_output_links},
        {"name": "image", "type": "IMAGE", "links": None},
    ]
    node["widgets_values"] = ["", prompt, model, seed, seed_control, "auto", "1K", "IMAGE+TEXT", system_prompt]
    if "properties" in node:
        node["properties"]["Node name for S&R"] = "GoogleGeminiDirect"
    return node


# ---------------------------------------------------------------------------
# Workflow-specific conversions
# ---------------------------------------------------------------------------

def convert_simple(wf: dict, old_type: str, builder) -> dict:
    """Replace all nodes of old_type with builder in a straightforward way."""
    wf = copy.deepcopy(wf)
    for node in wf["nodes"]:
        if node["type"] == old_type:
            new_node = builder(node, wf)
            node.clear()
            node.update(new_node)
    return wf


def convert_flf2v(wf: dict) -> dict:
    """api_seedance2_0_flf2v.json"""
    return convert_simple(wf, "ByteDance2FirstLastFrameNode", build_fal_seedance_image2video)


def convert_t2v(wf: dict) -> dict:
    """api_seedance2_0_t2v.json"""
    return convert_simple(wf, "ByteDance2TextToVideoNode", build_fal_seedance_text2video)


def convert_r2v(wf: dict) -> dict:
    """api_seedance2_0_r2v.json"""
    return convert_simple(wf, "ByteDance2ReferenceNode", build_fal_seedance_reference2video)


def convert_flf2v_real_human(wf: dict) -> dict:
    """api_seedance2_0_flf2v_real_human.json"""
    wf = copy.deepcopy(wf)
    bd_node = None
    asset_nodes = []
    for n in wf["nodes"]:
        if n["type"] == "ByteDance2FirstLastFrameNode":
            bd_node = n
        elif n["type"] == "ByteDanceCreateImageAsset":
            asset_nodes.append(n)

    if bd_node is None:
        raise ValueError("ByteDance2FirstLastFrameNode not found")

    # Map asset node -> LoadImage node that feeds it
    asset_to_loadimage = {}
    for asset in asset_nodes:
        for lk in wf["links"]:
            if lk[3] == asset["id"] and lk[5] == "IMAGE":
                src_node = find_node(wf["nodes"], lk[1])
                if src_node and src_node["type"] == "LoadImage":
                    asset_to_loadimage[asset["id"]] = src_node["id"]

    # Map asset node -> PreviewAny nodes it feeds
    asset_to_previews = {}
    for asset in asset_nodes:
        previews = []
        for lk in wf["links"]:
            if lk[1] == asset["id"]:
                tgt = find_node(wf["nodes"], lk[3])
                if tgt and tgt["type"] == "PreviewAny":
                    previews.append(tgt["id"])
        asset_to_previews[asset["id"]] = previews

    # Replace ByteDance node with FAL node
    new_bd = build_fal_seedance_image2video(bd_node, wf)
    bd_node.clear()
    bd_node.update(new_bd)

    # Remove links that go TO the old ByteDance node (asset_id inputs)
    wf["links"] = [lk for lk in wf["links"] if not (lk[3] == bd_node["id"] and lk[4] in (10, 11))]

    # Remove links that go TO asset creation nodes
    for asset in asset_nodes:
        wf["links"] = [lk for lk in wf["links"] if not (lk[3] == asset["id"])]

    # Remove links that come FROM asset creation nodes (will rewire to LoadImage)
    for asset in asset_nodes:
        wf["links"] = [lk for lk in wf["links"] if not (lk[1] == asset["id"])]

    # Remove dangling links (links targeting non-existent nodes)
    node_ids = {n["id"] for n in wf["nodes"]}
    wf["links"] = [lk for lk in wf["links"] if lk[1] in node_ids and lk[3] in node_ids]

    # Add direct links: LoadImage -> FAL node
    first_load = asset_to_loadimage.get(asset_nodes[0]["id"]) if asset_nodes else None
    last_load = asset_to_loadimage.get(asset_nodes[1]["id"]) if len(asset_nodes) > 1 else None
    next_link_id = max((l[0] for l in wf["links"]), default=0) + 1

    if first_load is not None:
        wf["links"].append([next_link_id, first_load, 0, bd_node["id"], 2, "IMAGE"])
        next_link_id += 1
    if last_load is not None:
        wf["links"].append([next_link_id, last_load, 0, bd_node["id"], 3, "IMAGE"])
        next_link_id += 1

    # Rewire LoadImage -> PreviewAny (replacing asset node -> PreviewAny)
    for asset in asset_nodes:
        load_id = asset_to_loadimage.get(asset["id"])
        if load_id is None:
            continue
        for preview_id in asset_to_previews.get(asset["id"], []):
            wf["links"].append([next_link_id, load_id, 0, preview_id, 0, "IMAGE"])
            next_link_id += 1

    # Remove asset creation nodes only
    for asset in asset_nodes:
        wf["nodes"] = [n for n in wf["nodes"] if n["id"] != asset["id"]]

    # Sync node input/output link references with global links
    sync_links_to_nodes(wf)

    return wf


def convert_r2v_real_human(wf: dict) -> dict:
    """api_seedance2_0_r2v_real_human.json"""
    wf = copy.deepcopy(wf)
    bd_node = None
    asset_node = None
    for n in wf["nodes"]:
        if n["type"] == "ByteDance2ReferenceNode":
            bd_node = n
        elif n["type"] == "ByteDanceCreateImageAsset":
            asset_node = n
    if bd_node is None:
        raise ValueError("ByteDance2ReferenceNode not found")

    # Find LoadImage that feeds the asset node
    load_image_id = None
    if asset_node:
        for lk in wf["links"]:
            if lk[3] == asset_node["id"] and lk[5] == "IMAGE":
                load_image_id = lk[1]
                break

    # Find PreviewAny nodes fed by the asset node
    preview_ids = []
    if asset_node:
        for lk in wf["links"]:
            if lk[1] == asset_node["id"]:
                tgt = find_node(wf["nodes"], lk[3])
                if tgt and tgt["type"] == "PreviewAny":
                    preview_ids.append(tgt["id"])

    # Replace ByteDance node with FAL node
    new_bd = build_fal_seedance_reference2video(bd_node, wf)
    bd_node.clear()
    bd_node.update(new_bd)

    # Remove asset link to the old ByteDance node (asset_1 input)
    wf["links"] = [lk for lk in wf["links"] if not (lk[3] == bd_node["id"] and lk[4] == 9)]

    # Remove links TO asset creation node
    if asset_node:
        wf["links"] = [lk for lk in wf["links"] if not (lk[3] == asset_node["id"])]

    # Remove links FROM asset creation node
    if asset_node:
        wf["links"] = [lk for lk in wf["links"] if not (lk[1] == asset_node["id"])]

    # Add direct link: LoadImage -> FAL node image_1
    next_link_id = max((l[0] for l in wf["links"]), default=0) + 1
    if load_image_id is not None:
        wf["links"].append([next_link_id, load_image_id, 0, bd_node["id"], 9, "IMAGE"])
        next_link_id += 1

    # Rewire LoadImage -> PreviewAny nodes
    for preview_id in preview_ids:
        if load_image_id is not None:
            wf["links"].append([next_link_id, load_image_id, 0, preview_id, 0, "IMAGE"])
            next_link_id += 1

    # Remove only the active asset creation node
    if asset_node:
        wf["nodes"] = [n for n in wf["nodes"] if n["id"] != asset_node["id"]]

    # Sync node input/output link references with global links
    sync_links_to_nodes(wf)

    return wf


def convert_template(wf: dict) -> dict:
    """template_seedance_2_0_plus_llm_prompt_helper.json"""
    wf = copy.deepcopy(wf)

    # Replace GeminiNode
    gemini_node = None
    for n in wf["nodes"]:
        if n["type"] == "GeminiNode":
            gemini_node = n
            break
    if gemini_node:
        new_gemini = build_google_gemini_direct(gemini_node, wf)
        gemini_node.clear()
        gemini_node.update(new_gemini)

    # Replace ByteDance2ReferenceNode
    bd_node = None
    for n in wf["nodes"]:
        if n["type"] == "ByteDance2ReferenceNode":
            bd_node = n
            break
    if bd_node:
        new_bd = build_fal_seedance_reference2video(bd_node, wf)
        bd_node.clear()
        bd_node.update(new_bd)

    # Update links for ImageStitch -> GeminiNode images
    # Old: ImageStitch output 0 -> GeminiNode input 0
    # New: ImageStitch output 0 -> GoogleGeminiDirect input 7 (images)
    if gemini_node:
        for lk in wf["links"]:
            if lk[3] == gemini_node["id"] and lk[4] == 0 and lk[5] == "IMAGE":
                lk[4] = 7

    # Update links for LoadImage -> ByteDance reference images
    # Old: LoadImage output 0 -> ByteDance input slot 6 (image_1), slot 7 (image_2)
    # New: LoadImage output 0 -> FAL input slot 9 (image_1), slot 10 (image_2)
    if bd_node:
        for lk in wf["links"]:
            if lk[3] == bd_node["id"]:
                if lk[4] == 6:
                    lk[4] = 9  # image_1
                elif lk[4] == 7:
                    lk[4] = 10  # image_2
                elif lk[4] == 8:
                    lk[4] = 11  # image_3
                elif lk[4] == 9:
                    lk[4] = 12  # image_4

    sync_links_to_nodes(wf)
    return wf


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    conversions = [
        ("api_seedance2_0_flf2v.json", convert_flf2v),
        ("api_seedance2_0_flf2v_real_human.json", convert_flf2v_real_human),
        ("api_seedance2_0_r2v.json", convert_r2v),
        ("api_seedance2_0_r2v_real_human.json", convert_r2v_real_human),
        ("api_seedance2_0_t2v.json", convert_t2v),
        ("template_seedance_2_0_plus_llm_prompt_helper.json", convert_template),
    ]

    for filename, converter in conversions:
        src = WORKFLOW_DIR / filename
        dst = WORKFLOW_DIR / filename.replace(".json", "_local.json")
        if not src.exists():
            print(f"SKIP: {src} not found")
            continue
        wf = load_json(src)
        try:
            wf_new = converter(wf)
            cleanup_stale_links(wf_new)
            save_json(dst, wf_new)
            print(f"OK: {dst}")
        except Exception as e:
            print(f"FAIL: {src} -> {e}")
            raise


if __name__ == "__main__":
    main()
