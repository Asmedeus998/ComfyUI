---
name: image-prompt-guide
description: Reference system prompt and best practices for multi-image prompt synthesis. Use when building or tuning an AI agent that analyzes multiple reference images and videos, audits an existing generated prompt, and outputs a refined prompt optimized for image or video generation across OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, Qwen image edit, and Dreamina Seedance 2.0. Covers Reference Element Fusion (single-subject composite), Art Director Presentation Boards, Cinematic Action Storyboards, TV Commercial Storyboards, Cinematic Lifestyle Storyboards, Environment Reference Locks (I2V scene anchors), 3D CGI Animation Character Bibles, Ad Character Reference Sheets, Seedance Video Prompt Engineering, Seedance Ad Video Prompt Engineering, single-subject locks, anti-collage enforcement, cross-model compatibility, and domain-agnostic prompt engineering. All templates follow a universal 6+1+1-slot reference mapping standard — 6 core semantic slots plus 1 optional creative/freeform slot plus 1 optional brand slot (8-BRAND).
---

# Image Prompt Guide

Concise index for the **Prompt Synthesizer / Evolver / Auditor** agent used in ComfyUI multi-image workflows.

## When to Use This Skill

- Building a new prompt-synthesis node or agent that takes **multiple reference images + an optional existing prompt** as input.
- **Reference Element Fusion**: Tuning composite subject workflows (subject identity from Image A + outfit from Image B + prop from Image C + brand aesthetic from Image D) that output a **single photograph of one subject**.
- **Art Director Presentation Board**: Generating **multi-section pre-production documents** (character turnarounds, prop sheets, environments, movie posters, color palettes) in a single polished board image.
- **Cinematic Action Storyboard**: Generating **multi-panel rough sketch grids** for action choreography with colored motion annotations, per-panel shot notes, and sequential beats.
- **TV Commercial Storyboard**: Generating **structured production tables** for TV advertisements with embedded shot thumbnails, dialogue/voiceover, SFX, audio, camera, transitions, and durations. Polished photorealistic frames — NOT sketches.
- **Cinematic Lifestyle Storyboard**: Generating **photorealistic multi-panel mood boards** depicting one character across quiet, contemplative daily life scenes. Cinematic film-still quality with poetic captions — NOT sketches or commercial photography.
- **Environment Reference Lock (I2V Scene Anchor)**: Generating **spatial consistency boards** with multi-angle room views, prop detail callouts, and technical specs to anchor backgrounds for image-to-video generation.
- **3D CGI Animation Character Bible**: Generating **character design bibles** for animated films — hero line-ups, expression sheets, action pose galleries, prop details, color palettes & materials, scale references, and character bios. Pixar-quality 3D CGI with strict cross-section consistency locks.
- **Ad Character Reference Sheet**: Generating **stripped-down character reference sheets** specifically for commercial video ads — hero line-ups, ad-relevant expressions (serene, delighted, confident), product interaction poses, costume/prop details, color palettes, and turnarounds. NO bios, NO scale references, NO generic action poses.
- Targeting multiple backend models from a single prompt output.
- Debugging why generated images contain **collages, grids, multiple panels, or duplicate subjects** when they should be single-subject photographs.
- Debugging why **presentation boards** have overlapping sections, missing panels, inconsistent art styles, or gibberish typography.
- Debugging why **cinematic storyboards** look too polished (sketch quality drift), lack annotation arrows, have character drift between panels, or break spatial continuity.
- Debugging why **commercial storyboards** look like rough sketches instead of photorealistic frames, miss audio columns, have weak CTAs, inconsistent branding, or duration mismatches.
- Debugging why **lifestyle storyboards** have character face drift between panels, mood breaks (one panel suddenly bright/cheerful), sketch/illustration quality instead of photorealism, missing captions, or commercial photography drift.
- Debugging why **environment lock boards** have spatial drift between camera views, missing prop callouts, inconsistent lighting, or absent technical spec bars.
- Debugging why **3D CGI character bibles** have character drift between turnaround/expression/action sections, missing prop details, flat rendering in some panels, inconsistent materials, or missing scale references.
- Converting full animation bibles into **ad-focused character reference sheets** by stripping bios, scale references, and generic action poses in favor of product interaction poses and commercial expressions.
- Fixing why generated images ignore outfit swaps, omit props, or fail to integrate brand aesthetics.

## Core Patterns

| Pattern | Output | Description | Full Reference |
|---------|--------|-------------|----------------|
| **Reference Element Fusion (REF)** | Single-subject photo | Multiple refs each supply one element (subject, outfit, prop, brand) that fuse into **one final image of one subject**. Grids and collages are strictly forbidden. | [`reference/reference-element-fusion.md`](reference/reference-element-fusion.md) |
| **Subject Swap** | Single-subject photo | Subject ref + Outfit ref. Same person, new clothes. | [`reference/reference-element-fusion.md`](reference/reference-element-fusion.md) |
| **Prop Integration** | Single-subject photo | Subject ref + Prop ref. Subject holding/wearing the prop. | [`reference/reference-element-fusion.md`](reference/reference-element-fusion.md) |
| **Brand Campaign** | Single-subject photo | Subject ref + Product/Brand ref + Style ref. Lifestyle shot with brand aesthetic. | [`reference/reference-element-fusion.md`](reference/reference-element-fusion.md) |
| **Art Director Presentation Board** | Multi-section document | Pre-production film bible with character turnarounds, prop sheets, environments, poster, color palette, mood text, materials, and notes. **Polished, realistic, grid required.** | [`reference/art-director-presentation-board.md`](reference/art-director-presentation-board.md) |
| **Cinematic Action Storyboard** | Multi-panel sketch grid | Rough gestural planning board for action choreography with colored annotation arrows, per-panel camera/action/focus notes, and sequential beats. **Sketchy, unfinished, grid required.** | [`reference/cinematic-storyboard.md`](reference/cinematic-storyboard.md) |
| **TV Commercial Storyboard** | Structured production table OR 3×3 contact sheet | Polished photorealistic commercial shot list with embedded thumbnails, dialogue/VO, SFX, audio, camera, transitions, durations, and summary strip. **Photorealistic, table format OR 3×3 edge-to-edge contact sheet for keyframe extraction.** | [`reference/tv-commercial-storyboard.md`](reference/tv-commercial-storyboard.md) |
| **Cinematic Lifestyle Storyboard** | 3×3 contact sheet | Photorealistic character-driven daily life montage with cinematic film stills, poetic captions inside panel frames, and mood-locked color grade. **Photorealistic, NOT sketches, 3×3 edge-to-edge contact sheet.** | [`reference/cinematic-lifestyle-storyboard.md`](reference/cinematic-lifestyle-storyboard.md) |
| **Environment Reference Lock** | Multi-section reference board | Spatial anchor for I2V: multi-angle room views, prop detail callouts, technical spec bar. **Locks background consistency for video generation.** | [`reference/environment-reference-lock.md`](reference/environment-reference-lock.md) |
| **3D CGI Animation Character Bible** | Multi-section design document | Pre-production character bible with hero line-ups, expression sheets, action poses, prop details, color palette & materials, scale reference, and bios. **Pixar-quality 3D CGI with strict consistency locks.** | [`character/3d-cgi-animation-character-bible.md`](character/3d-cgi-animation-character-bible.md) |
| **Ad Character Reference Sheet** | Multi-section reference sheet | Stripped-down character reference for ad video generation — hero line-ups, ad expressions, product interaction poses, costume/prop details, color palette, turnaround. **NO bios, NO scale refs.** | [`character/ad-character-reference-sheet.md`](character/ad-character-reference-sheet.md) |
| **Seedance Video Prompt Engineer** | Video generation prompt | Single continuous video segment prompt for Dreamina Seedance 2.0. Subject + motion + camera + audio + reference locks. **150–800 words, flowing paragraph.** | [`templates_prompt/video/seedance_video_prompt_engineer.md`](../../../templates_prompt/video/seedance_video_prompt_engineer.md) |
| **Seedance Ad Video Prompt Engineer** | Advertisement video prompt | Commercial video segment prompt with product placement, branding, CTA, and timed narrative arcs for Seedance 2.0. **200–700 words, flowing paragraph.** | [`templates_prompt/video/seedance_ad_video_prompt_engineer.md`](../../../templates_prompt/video/seedance_ad_video_prompt_engineer.md) |
| **Seedance Ad Video Prompt Engineer (Flat Keyframes)** | Advertisement video prompt | Same as above, but optimized for a **flat array of 9 sequential keyframes** (NOT a 3×3 grid). Enforces strict 1→9 sequential order, zero repetition, no visual-content reordering. **200–700 words, flowing paragraph.** | [`templates_prompt/video/seedance_ad_video_prompt_engineer_15s_keyframes_flat.md`](../../../templates_prompt/video/seedance_ad_video_prompt_engineer_15s_keyframes_flat.md) |
| **Prompt Audit** | Refined prompt | Multiple refs + Existing prompt. Corrected and enriched prompt. | Depends on target pattern above |

## Critical Distinction

| | Reference Element Fusion | Art Director Presentation Board | Cinematic Action Storyboard | TV Commercial Storyboard | Cinematic Lifestyle Storyboard | Environment Reference Lock |
|--|-------------------------|--------------------------------|----------------------------|---------------------------|-------------------------------|---------------------------|
| **Desired Output** | One photograph | One polished document / board | One rough planning sketch sheet | One structured production table OR 3×3 contact sheet | One photorealistic mood board / contact sheet | One spatial anchor board |
| **Layout** | Single scene, no grids | Multi-section grid required | Multi-panel grid required | Multi-row table with columns OR 3×3 edge-to-edge grid | 3×3 contact sheet — edge-to-edge, no chrome | Multi-view + callouts + spec bar |
| **Art Quality** | Photorealistic / finished | Polished, realistic renders | Rough, gestural, unfinished | Photorealistic / commercial-grade | Photorealistic / film-still / arthouse | Photorealistic / cinematic |
| **Typography** | None or minimal | Heavy — titles, labels, credits | Light — shot names, notes per panel | Heavy (table) or light (grid) — text inside panels only | Light — poetic captions inside panels only | Medium — headers, prop labels, specs |
| **Annotations** | None | Minimal | Heavy colored arrows (camera, body, prop, impact, timing) | None — audio/camera metadata in table cells, or captions inside panels for grid mode | None — poetic captions inside panel frames only | None — prop callout panels instead |
| **Word Count** | 150–300 words | 300–600 words | 400–800 words | 500–900 words | 500–900 words | 300–600 words |
| **Anti-Pattern** | Collages / grids | Section overlap / missing panels | Polish drift / character drift / missing arrows | Sketch drift / missing audio / weak CTA / bad branding / caption overflow / grid dimension drift | Face drift / mood break / sketch quality / caption overflow / grid dimension drift | Spatial drift / missing callouts / no spec bar |

## Universal Reference Slot Standard

All templates in `templates_prompt/` follow a **strict 6+1+1-slot reference mapping standard**. This ensures that when a user swaps templates in the ComfyUI `PromptTemplateLoader` dropdown, the images wired to `Image 1` through `Image 6` (and videos wired to `Video 1`–`Video 3`) always carry the **same semantic meaning**. The LLM never has to guess what a reference image represents.

Image 7 is an **optional extended slot** for unstructured creative inspiration — landing pages, mood boards, composite references, or any visual that doesn't fit the 6 core semantics. It is explicitly freeform: the LLM interprets color, layout, typography, mood, and composition holistically rather than locking a single element.

### The 6 Core Image Slots + 1 Creative Slot + 1 Continuation Slot

Every user prompt template must open with:

```
Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional — not used if no creative reference provided)
- Image 8: Brand logo / label / packaging reference — [describe brand logo, typography style, label design, or packaging element] (labeled **8-BRAND**) (optional — not used if no brand reference provided)
```

### Slot Semantics (Fixed Across All Templates)

| Slot | Meaning | Always Maps To |
|------|---------|---------------|
| **Image 1** | Primary subject / character | Face, hair, body proportions, skin tone, distinguishing features |
| **Image 2** | Costume / outfit / product packaging | Clothing, garments, product shape, colors, fabrics, materials |
| **Image 3** | Prop / accessory / secondary subject | Weapons, tools, jewelry, secondary character, additional visual element |
| **Image 4** | Environment / scene / background | Setting, architecture, lighting, atmosphere, spatial context |
| **Image 5** | Product / brand / commercial element | Product hero shot, logo, brand color, packaging, commercial visual lock |
| **Image 6** | Style / aesthetic / mood / material | Art direction, color palette, material quality, mood tone, CGI style |
| **Image 7** | Creative / freeform / composite | Landing page, mood board, unstructured inspiration — holistic creative direction (optional) |
| **Image 8** | Brand logo / label / packaging | Brand logo, typography style, label design, or packaging element for consistent brand lock across all frames (optional) |

### Rules for Template Authors

1. **Always include all 6 core slots** in every template, even if some are not applicable. Mark unused slots with `(optional — not used in this template)`.
2. **Always include Image 7** in every template, marked as `(optional — not used if no creative reference provided)`.
3. **Always include Image 8** in every template, marked as `(optional — not used if no brand reference provided)`. For multi-segment video workflows, continuation frames are handled separately via individual image inputs (`image_1`, `image_2`, `image_3`) or the `creative_video` passthrough.
4. **Never redefine slot semantics.** Image 1 is always "Character / subject reference" — never "Logo reference" or "Background reference." Image 7 is always "Creative / freeform / composite reference." Image 8 is always "Brand logo / label / packaging reference."
5. **Video slots are flexible** but should follow the convention:
   - Video 1: Primary motion / choreography / action reference
   - Video 2: Camera motion reference
   - Video 3: VFX, pacing, timing, transition, or creative mood reference
6. **Creative video passthrough**: `SlotImageBatch` provides a `creative_video` input (VIDEO type) that passes straight through to downstream video nodes. Use this for unstructured motion references — mood clips, pacing inspiration, or B-roll that informs the overall energy without locking a specific action.
7. **Explicit reference locks** must follow the slot mapping in the prompt body: "The character must match Image 1 exactly" / "The product must match Image 2 exactly" / "The environment must match Image 4 exactly." For Image 7, use holistic locks: "The overall visual approach follows the creative reference in Image 7 — adopt its color palette, layout energy, and compositional style." For Image 8 (brand), use brand locks: "The brand logo and packaging must match Image 8 exactly — use the same typography, colors, and logo placement across all frames where the brand appears."
8. **Template naming** in `PromptTemplateLoader` uses the format: `category/file_name: Template Letter - Template Name`. The system prompt uses `category/file_name: system_prompt`.

### Slot Numbering & Batch Position (CRITICAL)

**The batch position does NOT equal the slot number.** `SlotImageBatch` outputs a sparse batch containing only the filled slots. If a user provides:
- Slot 1 (character) and Slot 7 (creative)

The batch has **2 images** at positions `[0, 1]`, but they are **Image 1** and **Image 7**, not Image 1 and Image 2.

**All system prompts MUST include this instruction** (copy verbatim):

```
2. **Slot Format & Image Numbering (CRITICAL — DO NOT IGNORE)**:
   - The reference images use a **fixed 8-slot semantic system**. Each image has a slot label burned into its top-left corner: **1-CHAR, 2-COSTUME, 3-PROP, 4-ENV, 5-PRODUCT, 6-STYLE, 7-CREATIVE, 8-BRAND**.
   - You will receive a **SUBSET** of these slots — not always all 7. Some slots may be empty/missing.
   - **When referring to images in your output prompt, you MUST use the SLOT NUMBER from the label** (e.g., "Image 1", "Image 7", "Image 5").
   - **NEVER use positional counting** like "the first image", "the second image", or "Image 2" when the label says 7-CREATIVE. The batch position does NOT determine the image number — the slot label does.
   - **Example**: If you receive only Image 1 (1-CHAR / character) and Image 7 (7-CREATIVE / creative reference), refer to them as "Image 1" and "Image 7" in your prompt. Do NOT call the creative reference "Image 2" just because it happens to be the second image in the batch.
   - **Empty slots**: If a slot is not provided, simply omit it from your prompt. Do not invent or hallucinate references for missing slots.
```

**All reference integration sections MUST start with**:
```
   - **ALWAYS refer to images by their SLOT NUMBER** (Image 1, Image 2, Image 7, etc.), never by batch position. If you received Image 1 and Image 7, write "as shown in Image 1" and "as shown in Image 7" — never "as shown in Image 2" for the creative reference.
```

### SlotImageBatch → KimiCliDirect Wiring

To prevent Kimi from mislabeling images due to sparse batch positions:

**`SlotImageBatch` outputs:**
- `batch` — batched IMAGE tensor with yellow slot labels burned into previews
- `image_1` … `image_7` — individual images for direct wiring to Seedance / other nodes
- `slot_map` — **STRING** human-readable text mapping batch positions to slot numbers
- `slot_labels` — **STRING** newline-separated slot numbers (e.g. `1\n7`) for exact @path labeling
- `creative_video` — VIDEO passthrough for unstructured motion references

**`KimiCliDirect` inputs:**
- `images` — batched IMAGE from `SlotImageBatch.batch`
- `slot_map` — STRING from `SlotImageBatch.slot_map`, prepended to the prompt before `system_prompt`
- `slot_labels` — STRING from `SlotImageBatch.slot_labels`, used to label each `@path` with its slot number instead of batch position
- `system_prompt` — loaded from `PromptTemplateLoader: system_prompt`
- `prompt` — loaded from `PromptTemplateLoader: A - Template Name`

**Required wiring:**
```
SlotImageBatch.batch        → KimiCliDirect.images
SlotImageBatch.slot_map     → KimiCliDirect.slot_map
SlotImageBatch.slot_labels  → KimiCliDirect.slot_labels
PromptTemplateLoader (system) → KimiCliDirect.system_prompt
PromptTemplateLoader (user)   → KimiCliDirect.prompt
```

Without `slot_map` + `slot_labels`, Kimi will default to positional counting (`Image 1`, `Image 2`) which breaks when slots are sparse (e.g. only slot 1 and slot 7 are filled).

### New Template Checklist

When creating a new template in `templates_prompt/`:

- [ ] File is a `.md` in the correct subfolder (`video/`, `storyboard/`, `character/`, `presentation/`)
- [ ] Contains `## The System Prompt` section with a code block for `PromptTemplateLoader: system_prompt`
- [ ] Contains `### Template A: Name` (or A1, A2, B, C, etc.) with a code block for `PromptTemplateLoader: A - Name`
- [ ] Every user template code block starts with the **exact** 6+1+1-slot `Reference mapping (SLOT FORMAT — swap any images into these slots):` block
- [ ] All 6 core image slots + Image 7 use the **exact** universal semantics listed above
- [ ] Unused core slots are marked `(optional — not used in this template)`
- [ ] Image 7 is marked `(optional — not used if no creative reference provided)`
- [ ] Video slots mention pacing / mood / creative reference for Video 3
- [ ] System prompt contains the **Slot Format & Image Numbering** section with the exact 6-bullet text (subset handling, slot-number referencing, anti-positional-counting, Image 1+7 example, empty-slot guidance)
- [ ] System prompt's reference integration section starts with **"ALWAYS refer to images by their SLOT NUMBER"**
- [ ] **If flat-array keyframe template**: System prompt contains **"STRICT SEQUENTIAL ORDER MANDATE"** — no reordering by visual content, no "best character keyframe" language
- [ ] **If flat-array keyframe template**: Every `@Image1` through `@Image9` appears **exactly once** in the example prompt and in all user templates
- [ ] **If flat-array keyframe template**: `@Image10` (continuation frame) is isolated to `CONTINUE:` beats only
- [ ] Prompt output is wrapped in `[[PROMPT]]` / `[[/PROMPT]]` tags (or `[[SEGMENT_N]]` for multi-segment)
- [ ] No markdown, bullets, or line breaks inside the prompt body
- [ ] Word count guidance is provided per pattern

## Flat Array Keyframe Standard (Seedance Video Workflows)

When building templates for **Dreamina Seedance 2.0 video generation** that accept a flat array of sequential keyframes, a separate strict standard applies. These templates live in `templates_prompt/video/seedance_ad_video_prompt_engineer_*_keyframes_flat.md`.

> **Critical distinction from slot-based templates**: The 6+1+1 slot standard assigns images by **semantic role** (Image 1 = character, Image 2 = product, etc.). Flat-array templates assign images by **strict narrative sequence** (`@Image1` = opening frame, `@Image9` = closing frame). **Never mix these paradigms in one template.**

### Core Rules (Non-Negotiable)

1. **Strict Sequential Order**: Keyframes MUST be used in ascending array position. `@Image1` is always first, `@Image9` is always last. The LLM is strictly forbidden from analyzing visual content and reordering based on "best character" or "best product."
2. **Zero Repetition**: Each `@ImageN` appears **exactly once** in the entire prompt. No image may be referenced in multiple time slices or across segments.
3. **No Visual Content Override**: Unlike slot-based templates, flat-array templates do NOT allow the LLM to pick the "best" image for a role. The assignment is deterministic by position.
4. **Continuation Frame Isolation**: `@Image10` (if provided) is a **separate continuation frame**. It appears ONLY in `CONTINUE:` beats for multi-segment workflows. It is never mixed into the 9-keyframe sequence. Continuation frames are handled independently of the 8-slot semantic batch.

### Mandatory Segment Distribution

| Duration | Segment 1 | Segment 2 | Segment 3 | Segment 4 |
|----------|-----------|-----------|-----------|-----------|
| **15s** | Global: `@Image1–@Image3`; 0-3s: `@Image4`; 3-7s: `@Image5`; 7-11s: `@Image6+@Image7`; 11-15s: `@Image8+@Image9` | — | — | — |
| **30s** | Global + slices: `@Image1–@Image5` | `CONTINUE:` + global + slices: `@Image6–@Image9` (+ `@Image10`) | — | — |
| **60s** | Global + slices: `@Image1–@Image2` | `CONTINUE:` + global + slices: `@Image3–@Image4` (+ `@Image10`) | `CONTINUE:` + global + slices: `@Image5–@Image6` (+ `@Image10`) | `CONTINUE:` + global + slices: `@Image7–@Image9` (+ `@Image10`) |

### Flat Array vs Slot Format: When to Use Which

| Paradigm | Use When | Image Count | Ordering |
|----------|----------|-------------|----------|
| **6+1+1 Slot Standard** | Single-image generation, reference element fusion, presentation boards, character bibles | 1–7 images | Semantic role (Image 1 = character, etc.) |
| **Flat Array Keyframes** | Seedance video ad generation from sequential storyboard panels | Exactly 9 keyframes + optional `@Image10` | Strict narrative sequence 1→9 |

## Quick Reference

### Model Behavior

| Model                | Type                | Prompt Style                               | Key Quirk                                           |
| -------------------- | ------------------- | ------------------------------------------ | --------------------------------------------------- |
| **OpenAI GPT Image** | Generation          | Natural language, descriptive, atmospheric | Under 600 words; hates fragmented tag spam          |
| **Seedream**         | Generation / Edit   | Natural language + explicit purpose/type   | Subject + action + environment structure works best |
| **Google Gemini**    | Generation          | Natural language, detailed                 | Tolerates longer prompts but benefits from focus    |
| **Grok Image Edit**  | Image-to-Image Edit | Preservation + modification clauses        | Must clearly state what to _keep_ vs _change_       |
| **Qwen image edit**  | Image-to-Image Edit | Preservation + modification clauses        | Similar to Grok; preserve identity, edit context    |

### Output Delimiters

The synthesized prompt must always be wrapped in:

```
[[PROMPT]]
... prompt text ...
[[/PROMPT]]
```

### Target Length

| Pattern | Target Length |
|---------|--------------|
| Reference Element Fusion | **150–300 words** as a single flowing paragraph |
| Art Director Presentation Board | **300–600 words** as one or two connected paragraphs |
| Cinematic Action Storyboard | **400–800 words** as one or two connected paragraphs |
| TV Commercial Storyboard | **500–900 words** as one or two connected paragraphs |
| Cinematic Lifestyle Storyboard | **500–900 words** as one or two connected paragraphs |
| Environment Reference Lock | **300–600 words** as one or two connected paragraphs |
| 3D CGI Animation Character Bible | **300–600 words** as one or two connected paragraphs |
| Ad Character Reference Sheet | **300–600 words** as one or two connected paragraphs |

No markdown, no bullets, no line breaks inside the prompt body.

### 3×3 Contact-Sheet Grid Standard (for TV Commercial Grid Mode & Cinematic Lifestyle Storyboards)

When generating **3×3 grids** that will be split into individual keyframes/panels, the prompt MUST enforce this contact-sheet standard to prevent headers, footers, and borders from breaking automated cropping:

- [ ] **EXACTLY 3 rows × 3 columns = 9 panels total.** Never 4×3, 3×4, or any other grid size.
- [ ] **LANDSCAPE orientation** — the overall board is wider than it is tall. Set generation size to landscape (e.g., 1536×1024).
- [ ] **NO header strip.** NO title bar. NO branding banner at the top.
- [ ] **NO footer strip.** NO key message bar. NO legal text strip at the bottom.
- [ ] **NO borders, gutters, or margins between panels.** Panels must tile edge-to-edge. A 1-pixel hairline separator is acceptable.
- [ ] **NO outer margin or padding** around the entire grid. The grid must touch all four edges of the canvas.
- [ ] **Panel numbers** are small and subtle in the top-left corner **INSIDE** each panel frame only.
- [ ] **NO captions, metadata, or text of any kind BELOW or BESIDE individual panels.** Any text must be inside the panel frame as part of the image content.
- [ ] **Background is not visible** — the 9 panels fill the entire canvas.

**Why this matters:** If the model generates a header bar (e.g., "Product BOTANIKA..."), a footer bar (e.g., "KEY MESSAGE..."), or white gutters between panels, a naive `1536÷3 / 1024÷3` split will cut through the text and produce unusable panels. The contact-sheet standard ensures clean `512×341` (or `512×336` with custom sizes) panels that require zero post-processing.

**Anti-patterns to watch for:**
- **Grid Dimension Drift**: Model generates 4×3 (12 panels) or 3×4 instead of 3×3. Fix: enumerate Panel 1 through Panel 9 explicitly.
- **Panel Caption Overflow**: Text appears below panels instead of inside. Fix: state "NO captions below panels" and "all text inside panel frames only."
- **Orientation Drift**: Model outputs portrait instead of landscape. Fix: add "LANDSCAPE orientation, wider than tall" and use landscape generation size.

### Anti-Collage Checklist (for REF only)

If your **single-subject** outputs show split-screens, grids, or multi-panel layouts:

- [ ] Remove phrases: "multiple angles," "various poses," "different perspectives," "split into panels," "grid layout," "collage style," "four quadrants," "series of shots"
- [ ] Anchor with: "single full-body portrait," "one person," "solo subject," "single frame," "single cohesive photograph"
- [ ] Add explicit prohibition: "No grids, no collages, no multiple panels, no split-screens."
- [ ] Verify the user template also states "ONE image containing exactly ONE subject"

### Board Structure Checklist (for Presentation Boards only)

If your **presentation board** outputs have overlapping sections or missing panels:

- [ ] Describe spatial layout explicitly: "left panel," "top-right grid," "bottom strip"
- [ ] Specify dividers: "thin gold lines," "clean white gutters"
- [ ] Add anti-overlap language: "sections do not overlap," "separated by clear gutters"
- [ ] Group minor sections: "a full-width bottom strip containing color swatches, mood text, material samples, and notes"
- [ ] Provide exact text strings for titles, taglines, and labels to avoid gibberish typography

### Storyboard Checklist (for Action Storyboards only)

If your **storyboard** outputs look too polished, miss annotations, or have inconsistent characters:

- [ ] Add anti-polish language: "rough pencil thumbnails," "gesture sketches," "visible construction lines," "unfinished strokes," "do not clean the drawing"
- [ ] Add character consistency lock: "The SAME character appears in every panel — identical costume silhouette, hair shape, body proportions. Only the pose changes."
- [ ] Specify annotation colors explicitly: "RED arrows for camera, BLUE for body motion, GREEN for weapon arc, ORANGE for impact, PURPLE for timing"
- [ ] State that every panel must include visible hand-drawn annotation arrows
- [ ] Add spatial continuity rule: "Preserve spatial continuity between panels — no teleporting"
- [ ] Provide panel-by-panel sequence in order (hook → escalation → ending)

### Commercial Storyboard Checklist (for TV Commercial Storyboards only)

If your **commercial storyboard** outputs look like sketches, miss audio info, or lack a strong CTA:

- [ ] Anchor quality: "photorealistic commercial frames," "cinematic product photography," "NOT sketches"
- [ ] For **Table Mode**: List all 8 columns explicitly: SHOT, VISUAL DESCRIPTION, DIALOGUE/VO, SFX, AUDIO/MUSIC, CAMERA, TRANSITION, DURATION
- [ ] For **Grid Mode (3×3 contact sheet)**: "EXACTLY 3 rows × 3 columns = 9 panels total, LANDSCAPE, NO headers, NO footers, NO borders, edge-to-edge panels"
- [ ] Enforce CTA end card: final shot must contain offer text, discount, "ORDER NOW" button, brand logo, tagline
- [ ] Add branding consistency rules: logo position, brand color, typography style
- [ ] Verify durations sum correctly and footer states total scene + commercial duration (table mode only)
- [ ] For grid mode: NO captions below panels — all text must be INSIDE panel frames

### Lifestyle Storyboard Checklist (for Cinematic Lifestyle Storyboards only)

If your **lifestyle storyboard** outputs have different faces per panel, sketch quality, or broken mood:

- [ ] Character lock: Describe face, hair, clothing, and distinguishing features in extreme detail at the prompt start. Reference "the same man/woman" for every panel.
- [ ] Mood lock: Define emotional temperature and color grade upfront. Add "ALL panels share the same mood and color grade."
- [ ] Anti-sketch anchors: "photorealistic cinematic photographs," "film still," "shot on 35mm," "arthouse cinema aesthetic," "NOT sketches or illustrations"
- [ ] Grid lock: "EXACTLY 3 rows × 3 columns = 9 panels total, LANDSCAPE, NO headers, NO footers, NO borders, edge-to-edge panels"
- [ ] Caption voice: "poetic, reflective, understated — one sentence reading like literary fiction or a diary entry, rendered INSIDE the panel frame only"
- [ ] Scene curation: Mix exterior and interior daily life scenes. Progress from external activity to internal reflection. Final panel is a close-up detail.
- [ ] Anti-commercial: "NOT commercial photography or advertising. Candid, unposed moments. Natural lighting. Film grain."
- [ ] Anti-caption-overflow: "NO captions below panels. NO text outside panel frames."

### Environment Lock Checklist (for I2V Scene Anchors only)

If your **environment board** outputs have shifting backgrounds or inconsistent prop positions:

- [ ] Add cross-view consistency lock: "Both wide shots show the SAME room from opposite angles"
- [ ] Specify spatial relationships explicitly: "If a lamp is on the left in Camera A, it must be on the right in Camera B (reverse perspective)"
- [ ] List 4–8 key props with numbers and visual descriptions for detail callouts
- [ ] Include technical spec bar: aspect, color temp, lens, format
- [ ] Prioritize light-emitting props and interactive objects in the callouts
- [ ] Add lighting lock: "Identical color temperature and weather across all panels"

### Flat Array Keyframe Checklist (for Seedance Video Ad Templates only)

If your **Seedance video ad prompt** references the same image twice, skips images, or reorders them:

- [ ] Remove phrases: "best character keyframe," "best product keyframe," "analyze visual content and assign," "visual content override"
- [ ] Enforce: "STRICT SEQUENTIAL ORDER MANDATE: @Image1 first, @Image2 second, through @Image9 last"
- [ ] Enforce: "Each @ImageN appears exactly once. NO repetitions. NO omissions."
- [ ] Verify the example prompt uses every `@Image1` through `@Image9` exactly once in ascending order
- [ ] For 15s: Global = `@Image1–@Image3`, 0-3s = `@Image4`, 3-7s = `@Image5`, 7-11s = `@Image6+@Image7`, 11-15s = `@Image8+@Image9`
- [ ] For 30s: Segment 1 = `@Image1–@Image5`, Segment 2 = `@Image6–@Image9`, CONTINUE = `@Image10`
- [ ] For 60s: Seg 1 = `@Image1–@Image2`, Seg 2 = `@Image3–@Image4`, Seg 3 = `@Image5–@Image6`, Seg 4 = `@Image7–@Image9`, CONTINUE = `@Image10`
- [ ] Ensure `@Image10` never appears in a 15s template (no continuation frame in single-segment)

## Full Documentation

All system prompts, user templates, anti-patterns, and examples live in the reference directory:

- **[`reference/reference-element-fusion.md`](reference/reference-element-fusion.md)** — Master system prompt, 4 user templates, 4 common anti-patterns with fixes, and good/bad examples for single-subject composite workflows.
- **[`reference/art-director-presentation-board.md`](reference/art-director-presentation-board.md)** — Master system prompt, 3 user templates, 4 common anti-patterns with fixes, model-specific notes, and good/bad examples for film pre-production board workflows.
- **[`reference/cinematic-storyboard.md`](reference/cinematic-storyboard.md)** — Master system prompt, 3 user templates, 5 common anti-patterns with fixes, model-specific notes, and good/bad examples for action choreography storyboard workflows.
- **[`reference/tv-commercial-storyboard.md`](reference/tv-commercial-storyboard.md)** — Master system prompt, 3 user templates, 5 common anti-patterns with fixes, model-specific notes, and good/bad examples for TV advertisement storyboard workflows.
- **[`reference/cinematic-lifestyle-storyboard.md`](reference/cinematic-lifestyle-storyboard.md)** — Master system prompt, 3 user templates, 5 common anti-patterns with fixes, model-specific notes, good/bad examples, and 3-step workflow integration notes for character-driven narrative montage workflows.
- **[`reference/environment-reference-lock.md`](reference/environment-reference-lock.md)** — Master system prompt, 3 user templates, 4 common anti-patterns with fixes, model-specific notes, good/bad examples, and I2V connection notes for spatial consistency board workflows.
- **[`reference/3d-cgi-animation-character-bible.md`](reference/3d-cgi-animation-character-bible.md)** — Master system prompt, 3 user templates, 6 common anti-patterns with fixes, model-specific notes, and good/bad examples for 3D CGI animation character design bible workflows.

## Usage in ComfyUI

See `AGENTS.md` in the project root for ComfyUI runtime conventions.
