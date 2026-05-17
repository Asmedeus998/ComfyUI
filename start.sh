#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

# ─── Nix Shell Check ─────────────────────────────────────────────────
if [ -z "$IN_NIX_SHELL" ] && [ -z "$COMFYUI_NIX_GUARD" ]; then
    echo "[!] Not inside nix-shell. Entering nix-shell automatically..."
    export COMFYUI_NIX_GUARD=1
    exec nix-shell --run "bash '$0'"
fi

# ─── Virtualenv (uv) ─────────────────────────────────────────────────
if [ ! -d ".venv" ]; then
    echo "[+] Creating Python virtualenv with uv..."
    uv venv
fi

source .venv/bin/activate

# ─── Install deps ────────────────────────────────────────────────────
echo "[+] Checking / installing Python packages..."
uv pip install -r requirements.txt

# Optional extras (soft fail if unavailable)
# uv pip install voxcpm || echo "[!] voxcpm skipped (optional)"
uv pip install librosa soundfile || echo "[!] Optional audio packages skipped"

# ─── Run ComfyUI ─────────────────────────────────────────────────────
echo "[+] Starting ComfyUI..."
echo "    URL: http://127.0.0.1:8195"
echo ""

exec python main.py \
    --listen 127.0.0.1 \
    --port 8195 \
    --max-upload-size 10240 \
    --enable-manager \
    "$@"
