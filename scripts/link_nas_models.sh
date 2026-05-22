#!/usr/bin/env bash
#
# link_nas_models.sh
# Replicates Google Colab model linking workflow for local ComfyUI.
# Run this on any new machine after setup_nas_models.sh has run once.
#

set -euo pipefail

NAS_BASE="${NAS_BASE:-/mnt/storage/comfyui_data/CivitAI}"
HF_BASE="${HF_BASE:-/mnt/storage/comfyui_data/Huggingface}"
COMFYUI="${COMFYUI:-$(cd "$(dirname "$0")/.." && pwd)}"
DRY_RUN="${DRY_RUN:-0}"

# ─── Helpers ─────────────────────────────────────────────────────────
run() {
    if [[ "$DRY_RUN" == "1" ]]; then
        echo "[DRY-RUN] $*"
    else
        "$@"
    fi
}

link_flat() {
    local src_dir="$1"
    local dest_dir="$2"
    local label="$3"

    if [[ ! -d "$src_dir" ]]; then
        echo "[!] Skipping $label: $src_dir not found"
        return 0
    fi

    echo "[+] Linking $label (flat files) from $src_dir -> $dest_dir"
    mkdir -p "$dest_dir"
    shopt -s nullglob
    for f in "$src_dir"/*; do
        local name
        name=$(basename "$f")
        [[ "$name" == "desktop.ini" ]] && continue
        [[ "$name" == ".ipynb_checkpoints" ]] && continue
        if [[ -L "$dest_dir/$name" ]]; then
            continue
        fi
        if [[ -e "$dest_dir/$name" ]]; then
            echo "    [!] Exists (not a symlink), skipping: $name"
            continue
        fi
        run ln -s "$f" "$dest_dir/$name"
        echo "    -> $name"
    done
    shopt -u nullglob
}

link_folder() {
    local src="$1"
    local dest_dir="$2"
    local label="$3"

    if [[ ! -d "$src" ]]; then
        echo "[!] Skipping $label: $src not found"
        return 0
    fi

    local name
    name=$(basename "$src")
    if [[ -L "$dest_dir/$name" ]]; then
        echo "[+] $label already linked: $name"
        return 0
    fi
    if [[ -e "$dest_dir/$name" ]]; then
        echo "[!] $label exists (not a symlink), skipping: $name"
        return 0
    fi

    echo "[+] Linking $label folder: $name"
    run ln -s "$src" "$dest_dir/$name"
}

# ─── Parse args ──────────────────────────────────────────────────────
for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=1 ;;
    esac
done

echo "NAS_BASE : $NAS_BASE"
echo "HF_BASE  : $HF_BASE"
echo "COMFYUI  : $COMFYUI"
echo ""

# ═══════════════════════════════════════════════════════════════════════
# OLD STRUCTURE (backward compat with existing CivitAI folders)
# ═══════════════════════════════════════════════════════════════════════
echo "=== Legacy CivitAI links ==="
link_flat "$NAS_BASE/Model"       "$COMFYUI/models/checkpoints"   "Legacy Checkpoints"
link_flat "$NAS_BASE/NSFW_model"  "$COMFYUI/models/checkpoints"   "Legacy NSFW Checkpoints"
link_flat "$NAS_BASE/VAE"         "$COMFYUI/models/vae"           "Legacy VAE"
link_flat "$NAS_BASE/ControlNet"  "$COMFYUI/models/controlnet"    "ControlNet"

link_folder "$NAS_BASE/LORA"          "$COMFYUI/models/loras"  "Legacy LoRA"
link_folder "$NAS_BASE/NSFW_LORA"     "$COMFYUI/models/loras"  "Legacy NSFW LoRA"
link_folder "$NAS_BASE/LORA_character" "$COMFYUI/models/loras" "Legacy LoRA Character"
link_folder "$NAS_BASE/Lora_clothes"  "$COMFYUI/models/loras"  "Legacy LoRA Clothes"

link_folder "$NAS_BASE/Embedding/Embedding001"      "$COMFYUI/models/embeddings" "Legacy Embedding001"
link_folder "$NAS_BASE/Embedding/nixeu-embeddings"  "$COMFYUI/models/embeddings" "Legacy nixeu-embeddings"

link_folder "$NAS_BASE/upscale" "$COMFYUI/models/upscale_models" "Legacy Upscalers"

# ═══════════════════════════════════════════════════════════════════════
# HUGGINGFACE
# ═══════════════════════════════════════════════════════════════════════
echo "=== HuggingFace links ==="
link_flat "$HF_BASE/ControlNet"  "$COMFYUI/models/controlnet"  "HF ControlNet"
link_flat "$HF_BASE/Model"       "$COMFYUI/models/checkpoints" "HF Checkpoints"
link_flat "$HF_BASE/clip_vision" "$COMFYUI/models/clip_vision" "HF CLIP Vision"
link_flat "$HF_BASE/ipadapter"   "$COMFYUI/models/ipadapter"   "HF IPAdapter"
link_flat "$HF_BASE/text_encoders" "$COMFYUI/models/text_encoders" "HF Text Encoders"
link_flat "$HF_BASE/vae"         "$COMFYUI/models/vae"          "HF VAE"
link_flat "$HF_BASE/diffusion_models" "$COMFYUI/models/diffusion_models" "HF Diffusion Models"
link_flat "$HF_BASE/latent_upscale_models" "$COMFYUI/models/latent_upscale_models" "HF Latent Upscalers"
link_flat "$HF_BASE/LORA"        "$COMFYUI/models/loras"       "HF LoRAs"

# ═══════════════════════════════════════════════════════════════════════
# GPT-SoVITS
# ═══════════════════════════════════════════════════════════════════════
echo "=== GPT-SoVITS links ==="
link_folder "/mnt/storage/comfyui_data/GPTSOVITS-data" "$COMFYUI/models" "GPT-SoVITS Data"

# ═══════════════════════════════════════════════════════════════════════
# EXTRAS
# ═══════════════════════════════════════════════════════════════════════
if [[ -d "$NAS_BASE/scripts" ]]; then
    mkdir -p "$COMFYUI/scripts"
    link_flat "$NAS_BASE/scripts" "$COMFYUI/scripts" "Scripts"
fi

DYNAMIC_PROMPT_DIR="$COMFYUI/custom_nodes/comfyui-dynamicprompts/wildcards"
if [[ -d "$NAS_BASE/DynamicPromptsWildcard" ]]; then
    if [[ -d "$COMFYUI/custom_nodes/comfyui-dynamicprompts" ]]; then
        mkdir -p "$DYNAMIC_PROMPT_DIR"
        link_flat "$NAS_BASE/DynamicPromptsWildcard" "$DYNAMIC_PROMPT_DIR" "Dynamic Prompts"
    else
        echo "[!] Skipping DynamicPrompts: comfyui-dynamicprompts not installed"
    fi
fi

echo ""
echo "Done. Current symlinks:"
find "$COMFYUI/models" -maxdepth 2 -type l 2>/dev/null | sort || true
