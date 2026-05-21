# Workflow JSON Format

## Link Format (Main Graph)

```json
[link_id, origin_node_id, origin_slot_index, target_node_id, target_slot_index, "TYPE"]
```

Example: `[1, 2, 0, 4, 1, "STRING"]` = Node 2 output slot 0 → Node 4 input slot 1.

## Link Format (Inside Subgraphs)

Subgraphs use **dict links** with `origin_id` / `target_id` instead of arrays:

```json
{"id": 125, "origin_id": -10, "origin_slot": 0, "target_id": 304, "target_slot": 0, "type": "IMAGE"}
```

- `-10` = subgraph input pseudo-node (receives external inputs)
- `-20` = subgraph output pseudo-node (feeds external outputs)
- `origin_slot` / `target_slot` map to the slot indices on those pseudo-nodes

## Subgraph Structure

```json
{
  "definitions": {
    "subgraphs": [
      {
        "id": "f7abaa3a-...",
        "nodes": [...],
        "links": [
          {"origin_id": -10, "origin_slot": 0, "target_id": 304, "target_slot": 0}
        ],
        "inputNode": {"id": -10, "bounding": [x, y, w, h]},
        "outputNode": {"id": -20, "bounding": [x, y, w, h]}
      }
    ]
  }
}
```

## Subgraph Execution Patterns

| Pattern | Dependencies | Use Case |
|---------|-------------|----------|
| **Parallel** (default) | No inter-subgraph links | Fastest total time; good when order doesn't matter and APIs can handle concurrency |
| **Sequential** | Chain subgraph N output → subgraph N+1 `trigger` input | Deterministic 1→2→3 order; prevents API rate-limiting; slower total time |

### Parallel (Default)

Independent subgraph instances have no links between each other. ComfyUI's scheduler executes them in arbitrary order (e.g., 7, 3, 6, 4, 1, 5, 2). All internal nodes across subgraphs become eligible as soon as their local dependencies are met.

```
BatchImagesNode ──→ Subgraph 1 (Gemini + Kling)
              ──→ Subgraph 2 (Gemini + Kling)
              ──→ Subgraph 3 (Gemini + Kling)
```

### Sequential (Chained)

Add an optional `trigger` input `(("*", {}))` to every node inside the subgraph that should wait for the previous subgraph. Wire the subgraph's external `trigger` input (`-10[trigger_slot]`) to each of those nodes. Then chain the subgraphs in the main graph by connecting each subgraph's output to the next subgraph's `trigger` input.

```
BatchImagesNode ──→ Subgraph 1 ──→ Subgraph 2 ──→ Subgraph 3
              (trigger)          (trigger)          (trigger)
```

**Implementation steps:**

1. **Node backend** — Add optional `trigger` to `INPUT_TYPES` and accept `trigger=None` in the `FUNCTION` method:
   ```python
   "optional": {
       "trigger": ("*", {}),  # accepts any type; ignored by the node
   }
   ```

2. **Subgraph definition** — Add a `trigger` input to the subgraph, then create internal links from `-10[trigger_slot]` to every node that should wait:
   ```json
   // Subgraph input definition
   {"name": "trigger", "type": "*", "linkIds": [400, 450]}
   
   // Internal links: -10[3] → Gemini trigger (slot 9) AND Kling trigger (slot 11)
   {"id": 400, "origin_id": -10, "origin_slot": 3, "target_id": 310, "target_slot": 11, "type": "*"}
   {"id": 450, "origin_id": -10, "origin_slot": 3, "target_id": 306, "target_slot": 9, "type": "*"}
   ```

3. **Main graph chain** — Connect subgraph N's output to subgraph N+1's trigger input. For subgraph 1, connect any upstream node (e.g., `BatchImagesNode`) to its trigger so it starts immediately:
   ```json
   // Subgraph 1 trigger gets IMAGE from BatchImagesNode (type '*' accepts anything)
   [364, 225, 0, 309, 3, "*"]
   
   // Subgraph 2 trigger gets VIDEO from Subgraph 1 output
   [358, 309, 0, 345, 3, "VIDEO"]
   ```

4. **First subgraph** — Its trigger input must have a real connection (even if just to an upstream node that already runs). If left disconnected, the frontend drops the input during expansion and the internal trigger links vanish.

**Gotcha:** Do NOT use `PreviewAny` or other sink nodes as the internal trigger target. `PreviewAny` requires its `source` input to be connected; if the first subgraph's trigger has no external source, validation fails with `Required input is missing: source`. Wire the trigger directly into the actual compute nodes (e.g., `GoogleGeminiDirect`, `FALKlingImage2Video`) instead.

**Flattening subgraphs for backend validation:** The ComfyUI frontend expands subgraphs before sending to `/prompt`. To validate from CLI, you must manually flatten:

1. For each subgraph instance in the main graph, copy its internal nodes with **new unique IDs**.
2. Remap internal links: replace old IDs with new IDs.
3. Remap external links:
   - Main graph link `A → Subgraph[N]` → find subgraph link `-10[N] → B`, then create `A → B(new_id)`.
   - Main graph link `Subgraph[N] → A` → find subgraph link `B → -20[N]`, then create `B(new_id) → A`.
4. Remove the subgraph instance node and its `definitions` entry.

## Node Input Slots

`slot_index` in the JSON **must match** the argument position in `INPUT_TYPES["required"]` + `INPUT_TYPES["optional"]`.

If you change the number/order of inputs in Python, **delete and re-add the node** in the workflow — old `slot_index` values will cause `"tuple index out of range"` validation errors.

## Outputs

```json
"outputs": [
  {"name": "srt", "type": "STRING", "links": [1, 2, 3], "slot_index": 0},
  {"name": "audio", "type": "AUDIO", "links": null, "slot_index": 1}
]
```

`slot_index` must match `RETURN_TYPES` order. `links: null` = unconnected.
