#!/usr/bin/env python3
"""
Convert ComfyUI workflow JSON from comfy_api_nodes Gemini nodes
(GeminiImage2Node, GeminiNanoBanana2) to local_api GoogleGeminiDirect nodes.

Usage:
    python convert_gemini_nodes.py input_workflow.json output_workflow.json
"""

import json
import sys
from copy import deepcopy

# Mapping of comfy_api_nodes → local_api node type
GEMINI_NODE_MAP = {
    "GeminiImage2Node": "GoogleGeminiDirect",
    "GeminiNanoBanana2": "GoogleGeminiDirect",
    "GeminiNanoBanana2V2": "GoogleGeminiDirect",
}

# Map display names to actual API model names
MODEL_MAP = {
    "Nano Banana 2 (Gemini 3.1 Flash Image)": "gemini-3.1-flash-image-preview",
}

# Default system prompt for image generation
GEMINI_IMAGE_SYS_PROMPT = (
    "You are an expert image-generation engine. You must ALWAYS produce an image.\n"
    "Interpret all user input—regardless of "
    "format, intent, or abstraction—as literal visual directives for image composition.\n"
    "If a prompt is conversational or lacks specific visual details, "
    "you must creatively invent a concrete visual scenario that depicts the concept.\n"
    "Prioritize generating the visual representation above any text, formatting, or conversational requests."
)


def _build_input(name: str, type_name: str, link, widget_name: str | None = None) -> dict:
    """Build a ComfyUI input dict."""
    inp = {
        "name": name,
        "type": type_name,
        "link": link,
    }
    if widget_name:
        inp["widget"] = {"name": widget_name}
        inp["localized_name"] = widget_name
    else:
        inp["localized_name"] = name
    return inp


def convert_node(node: dict) -> dict:
    """Convert a single comfy_api_nodes Gemini node to GoogleGeminiDirect."""
    old_type = node["type"]
    if old_type not in GEMINI_NODE_MAP:
        return node

    new_node = deepcopy(node)
    new_node["type"] = GEMINI_NODE_MAP[old_type]

    old_widget_values = list(node.get("widgets_values", []))

    # The original Gemini nodes use control_after_generate on seed, which adds
    # an extra widget value right after the seed value in widgets_values.
    # Because this extra widget isn't reflected in the input definitions, we
    # hard-code the mapping based on node type.
    #
    # GeminiImage2Node widget order (8 values):
    #   [0] prompt, [1] model, [2] seed, [3] seed_control, [4] aspect_ratio,
    #   [5] resolution, [6] response_modalities, [7] system_prompt
    #
    # GeminiNanoBanana2 widget order (9 values):
    #   [0] prompt, [1] model, [2] seed, [3] seed_control, [4] aspect_ratio,
    #   [5] resolution, [6] response_modalities, [7] thinking_level, [8] system_prompt
    #
    # GoogleGeminiDirect widget order (9 values with control_after_generate):
    #   [0] api_key, [1] prompt, [2] model, [3] seed, [4] seed_control,
    #   [5] aspect_ratio, [6] resolution, [7] response_modalities, [8] system_prompt

    def _safe_get(idx: int, default=""):
        return old_widget_values[idx] if idx < len(old_widget_values) else default

    prompt_val = _safe_get(0, "")
    model_val = _safe_get(1, "gemini-3-pro-image-preview")
    seed_val = _safe_get(2, 42)
    seed_control_val = _safe_get(3, "randomize")
    aspect_ratio_val = _safe_get(4, "auto")
    resolution_val = _safe_get(5, "1K")
    response_modalities_val = _safe_get(6, "IMAGE+TEXT")
    # Index 7 is either thinking_level (NanoBanana2) or system_prompt (GeminiImage2Node)
    if old_type == "GeminiNanoBanana2" and len(old_widget_values) >= 9:
        system_prompt_val = _safe_get(8, GEMINI_IMAGE_SYS_PROMPT)
    else:
        system_prompt_val = _safe_get(7, GEMINI_IMAGE_SYS_PROMPT)

    # Map display names to API names
    if model_val in MODEL_MAP:
        model_val = MODEL_MAP[model_val]

    # --- Build new inputs ---
    # Order must match GoogleGeminiDirect.INPUT_TYPES:
    # api_key, prompt, model, seed, aspect_ratio, resolution, response_modalities, images, system_prompt
    old_inputs_by_name = {inp.get("name", ""): inp for inp in node.get("inputs", [])}

    new_inputs = [
        _build_input("api_key", "STRING", None, "api_key"),
        _build_input("prompt", "STRING", old_inputs_by_name.get("prompt", {}).get("link"), "prompt"),
        _build_input("model", "COMBO", None, "model"),
        _build_input("seed", "INT", None, "seed"),
        _build_input("aspect_ratio", "COMBO", None, "aspect_ratio"),
        _build_input("resolution", "COMBO", None, "resolution"),
        _build_input("response_modalities", "COMBO", None, "response_modalities"),
    ]

    # Map original "images" input to "images"
    images_link = old_inputs_by_name.get("images", {}).get("link")
    new_inputs.append(_build_input("images", "IMAGE", images_link))

    new_inputs.append(_build_input("system_prompt", "STRING", None, "system_prompt"))

    new_node["inputs"] = new_inputs

    # --- Build new outputs ---
    # GoogleGeminiDirect RETURN_TYPES = ("STRING", "IMAGE")
    # Slot 0 = response (STRING), Slot 1 = image (IMAGE)
    old_outputs = node.get("outputs", [])
    string_links = []
    image_links = []

    for i, out in enumerate(old_outputs):
        if out.get("type") == "STRING" and out.get("links"):
            links = out["links"]
            if isinstance(links, list):
                string_links.extend(links)
            else:
                string_links.append(links)
        elif out.get("type") == "IMAGE" and out.get("links"):
            links = out["links"]
            if isinstance(links, list):
                image_links.extend(links)
            else:
                image_links.append(links)

    # Deduplicate and remove None
    string_links = list(dict.fromkeys([l for l in string_links if l is not None]))
    image_links = list(dict.fromkeys([l for l in image_links if l is not None]))

    new_outputs = [
        {"name": "response", "type": "STRING", "links": string_links if string_links else None},
        {"name": "image", "type": "IMAGE", "links": image_links if image_links else None},
    ]
    new_node["outputs"] = new_outputs

    # --- Build new widget values ---
    new_node["widgets_values"] = [
        "",                       # api_key
        prompt_val,               # prompt
        model_val,                # model
        seed_val,                 # seed
        seed_control_val,         # seed_control (auto-generated by control_after_generate)
        aspect_ratio_val,         # aspect_ratio
        resolution_val,           # resolution
        response_modalities_val,  # response_modalities
        system_prompt_val,        # system_prompt
    ]

    # Update properties
    props = new_node.get("properties", {})
    props["Node name for S&R"] = "GoogleGeminiDirect"
    new_node["properties"] = props

    return new_node, node["id"]


def convert_workflow(data: dict) -> dict:
    """Convert all Gemini comfy_api_nodes in a workflow to local equivalents."""
    converted_count = 0
    converted_node_ids = {}

    for node in data.get("nodes", []):
        old_type = node.get("type", "")
        if old_type in GEMINI_NODE_MAP:
            node_id = node["id"]
            new_node, _ = convert_node(node)
            node.clear()
            node.update(new_node)
            converted_count += 1
            converted_node_ids[node_id] = True

    # Fix link origin_slots for converted nodes.
    # Original GeminiImage2Node outputs: slot 0 = IMAGE, slot 1 = STRING
    # GoogleGeminiDirect outputs:       slot 0 = STRING, slot 1 = IMAGE
    # So we swap origin_slot 0 <-> 1 for all links originating from converted nodes.
    for link in data.get("links", []):
        if link[1] in converted_node_ids:
            if link[2] == 0:      # was IMAGE slot
                link[2] = 1       # now IMAGE is slot 1
            elif link[2] == 1:    # was STRING slot
                link[2] = 0       # now STRING is slot 0
            # Slot 2+ (e.g. thought_image from NanoBanana2) — drop or remap
            # thought_image was slot 2, but GoogleGeminiDirect only has 2 outputs.
            # Links from slot 2 will dangle; we could remap to slot 1 (image).
            elif link[2] == 2:
                link[2] = 1

    print(f"Converted {converted_count} Gemini node(s).")
    return data


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} input.json output.json")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r") as f:
        data = json.load(f)

    data = convert_workflow(data)

    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved converted workflow to {output_path}")


if __name__ == "__main__":
    main()
