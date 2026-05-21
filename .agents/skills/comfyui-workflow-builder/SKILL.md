---
name: comfyui-workflow-builder
description: Build and modify ComfyUI custom nodes, workflows, and frontend extensions. Use when the user asks to create nodes, modify node definitions, wire workflow JSON, add preview/display nodes, or fix ComfyUI validation/runtime errors. Covers node Python backend, workflow JSON topology, JS frontend extensions, and common debugging patterns.
---

# ComfyUI Workflow Builder

Build, modify, and debug ComfyUI custom nodes, workflows, and frontend extensions.

## Quick Reference

### By Topic

| Topic | File |
|-------|------|
| Python node backend, INPUT_TYPES, widget types | → [node-backend.md](./references/node-backend.md) |
| Workflow JSON format, links, subgraphs, slot indices | → [workflow-format.md](./references/workflow-format.md) |
| JS frontend extensions, widget updates after execution | → [frontend-extensions.md](./references/frontend-extensions.md) |
| Testing via `/prompt` API, debugging checklist, common pitfalls | → [testing-debugging.md](./references/testing-debugging.md) |
| Audio tensor ↔ WAV conversion helpers | → [audio-helpers.md](./references/audio-helpers.md) |
| Seedance slot indices, workflow preservation during conversion | → [seedance-slots.md](./references/seedance-slots.md) |

### Common Tasks

- **Creating a new node** → Read [node-backend.md](./references/node-backend.md), then [testing-debugging.md](./references/testing-debugging.md#testing-via-comfyui-api-not-just-direct-python)
- **Fixing `tuple index out of range`** → Check [workflow-format.md#node-input-slots](./references/workflow-format.md#node-input-slots) and [testing-debugging.md#common-pitfalls](./references/testing-debugging.md#common-pitfalls)
- **Adding a display widget after execution** → Read [frontend-extensions.md](./references/frontend-extensions.md)
- **Converting cloud workflows to local** → Read [seedance-slots.md#preserving-workflow-structure-during-conversion](./references/seedance-slots.md#preserving-workflow-structure-during-conversion)
- **Wiring subgraphs sequentially** → Read [workflow-format.md#subgraph-execution-patterns](./references/workflow-format.md#subgraph-execution-patterns)
- **Building a `/prompt` payload manually** → Read [testing-debugging.md#step-2-build-the-prompt-payload](./references/testing-debugging.md#step-2-build-the-prompt-payload)

## Project-Specific Conventions

This project uses:
- **Python env**: `uv pip install ...` (not `pip`)
- **ComfyUI port**: `8195`
- **Custom node path**: `custom_nodes/comfyui-multi-subtitle/`
- **Local API nodes**: `custom_nodes/comfyui-local-gemini/` (separate git repo)
- **Model storage**: NAS at `/mnt/storage/comfyui_data/` (symlinked via `scripts/link_nas_models.sh`)
- **Restart command**: `tmux send-keys -t comfyui-dev C-c && sleep 3 && tmux send-keys -t comfyui-dev "cd /home/yumeko/github/ComfyUI && ./start.sh" Enter`
- **Verify up**: `curl -s http://127.0.0.1:8195/system_stats`

See `AGENTS.md` in project root for full conventions.
