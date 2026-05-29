---
name: image-prompt-guide
description: Reference system prompt and best practices for multi-image prompt synthesis. Use when building or tuning an AI agent that analyzes multiple reference images and videos, audits an existing generated prompt, and outputs a refined prompt optimized for image or video generation across OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, Qwen image edit, and Dreamina Seedance 2.0. Covers Reference Element Fusion (single-subject composite), Art Director Presentation Boards, Cinematic Action Storyboards, TV Commercial Storyboards, Cinematic Lifestyle Storyboards, Environment Reference Locks (I2V scene anchors), 3D CGI Animation Character Bibles, Seedance Video Prompt Engineering, Seedance Ad Video Prompt Engineering, single-subject locks, anti-collage enforcement, cross-model compatibility, and domain-agnostic prompt engineering. All templates follow a universal 6+1-slot reference mapping standard — 6 core semantic slots plus 1 optional creative/freeform slot.
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
- **3D CGI Animation Character Bible**: Generating **character design bibles** for animated films and ads — hero line-ups, expression sheets, action pose galleries, prop details, color palettes & materials, scale references, and character bios. Pixar-quality 3D CGI with strict cross-section consistency locks.
- Targeting multiple backend models from a single prompt output.
- Debugging why generated images contain **collages, grids, multiple panels, or duplicate subjects** when they should be single-subject photographs.
- Debugging why **presentation boards** have overlapping sections, missing panels, inconsistent art styles, or gibberish typography.
- Debugging why **cinematic storyboards** look too polished (sketch quality drift), lack annotation arrows, have character drift between panels, or break spatial continuity.
- Debugging why **commercial storyboards** look like rough sketches instead of photorealistic frames, miss audio columns, have weak CTAs, inconsistent branding, or duration mismatches.
- Debugging why **lifestyle storyboards** have character face drift between panels, mood breaks (one panel suddenly bright/cheerful), sketch/illustration quality instead of photorealism, missing captions, or commercial photography drift.
- Debugging why **environment lock boards** have spatial drift between camera views, missing prop callouts, inconsistent lighting, or absent technical spec bars.
- Debugging why **3D CGI character bibles** have character drift between turnaround/expression/action sections, missing prop details, flat rendering in some panels, inconsistent materials, or missing scale references.
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
| **TV Commercial Storyboard** | Structured production table | Polished photorealistic commercial shot list with embedded thumbnails, dialogue/VO, SFX, audio, camera, transitions, durations, and summary strip. **Photorealistic, table format, grid required.** | [`reference/tv-commercial-storyboard.md`](reference/tv-commercial-storyboard.md) |
| **Cinematic Lifestyle Storyboard** | Multi-panel photo grid | Photorealistic character-driven daily life montage with cinematic film stills, poetic captions, and mood-locked color grade. **Photorealistic, NOT sketches, grid required.** | [`reference/cinematic-lifestyle-storyboard.md`](reference/cinematic-lifestyle-storyboard.md) |
| **Environment Reference Lock** | Multi-section reference board | Spatial anchor for I2V: multi-angle room views, prop detail callouts, technical spec bar. **Locks background consistency for video generation.** | [`reference/environment-reference-lock.md`](reference/environment-reference-lock.md) |
| **3D CGI Animation Character Bible** | Multi-section design document | Pre-production character bible with hero line-ups, expression sheets, action poses, prop details, color palette & materials, scale reference, and bios. **Pixar-quality 3D CGI with strict consistency locks.** | [`reference/3d-cgi-animation-character-bible.md`](reference/3d-cgi-animation-character-bible.md) |
| **Seedance Video Prompt Engineer** | Video generation prompt | Single continuous video segment prompt for Dreamina Seedance 2.0. Subject + motion + camera + audio + reference locks. **150–800 words, flowing paragraph.** | [`templates_prompt/video/seedance_video_prompt_engineer.md`](../../../templates_prompt/video/seedance_video_prompt_engineer.md) |
| **Seedance Ad Video Prompt Engineer** | Advertisement video prompt | Commercial video segment prompt with product placement, branding, CTA, and timed narrative arcs for Seedance 2.0. **200–700 words, flowing paragraph.** | [`templates_prompt/video/seedance_ad_video_prompt_engineer.md`](../../../templates_prompt/video/seedance_ad_video_prompt_engineer.md) |
| **Prompt Audit** | Refined prompt | Multiple refs + Existing prompt. Corrected and enriched prompt. | Depends on target pattern above |

## Critical Distinction

| | Reference Element Fusion | Art Director Presentation Board | Cinematic Action Storyboard | TV Commercial Storyboard | Cinematic Lifestyle Storyboard | Environment Reference Lock |
|--|-------------------------|--------------------------------|----------------------------|---------------------------|-------------------------------|---------------------------|
| **Desired Output** | One photograph | One polished document / board | One rough planning sketch sheet | One structured production table | One photorealistic mood board | One spatial anchor board |
| **Layout** | Single scene, no grids | Multi-section grid required | Multi-panel grid required | Multi-row table with columns | Multi-panel grid with captions | Multi-view + callouts + spec bar |
| **Art Quality** | Photorealistic / finished | Polished, realistic renders | Rough, gestural, unfinished | Photorealistic / commercial-grade | Photorealistic / film-still / arthouse | Photorealistic / cinematic |
| **Typography** | None or minimal | Heavy — titles, labels, credits | Light — shot names, notes per panel | Heavy — headers, VO text, offer text, durations | Light — poetic captions only | Medium — headers, prop labels, specs |
| **Annotations** | None | Minimal | Heavy colored arrows (camera, body, prop, impact, timing) | None — audio/camera metadata in table cells instead | None — poetic captions below panels instead | None — prop callout panels instead |
| **Word Count** | 150–300 words | 300–600 words | 400–800 words | 500–900 words | 500–900 words | 300–600 words |
| **Anti-Pattern** | Collages / grids | Section overlap / missing panels | Polish drift / character drift / missing arrows | Sketch drift / missing audio / weak CTA / bad branding | Face drift / mood break / sketch quality / missing captions | Spatial drift / missing callouts / no spec bar |

## Universal Reference Slot Standard

All templates in `templates_prompt/` follow a **strict 6+1-slot reference mapping standard**. This ensures that when a user swaps templates in the ComfyUI `PromptTemplateLoader` dropdown, the images wired to `Image 1` through `Image 6` (and videos wired to `Video 1`–`Video 3`) always carry the **same semantic meaning**. The LLM never has to guess what a reference image represents.

Image 7 is an **optional extended slot** for unstructured creative inspiration — landing pages, mood boards, composite references, or any visual that doesn't fit the 6 core semantics. It is explicitly freeform: the LLM interprets color, layout, typography, mood, and composition holistically rather than locking a single element.

### The 6 Core Image Slots + 1 Creative Slot

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

### Rules for Template Authors

1. **Always include all 6 core slots** in every template, even if some are not applicable. Mark unused slots with `(optional — not used in this template)`.
2. **Always include Image 7** in every template, marked as `(optional — not used if no creative reference provided)`.
3. **Never redefine slot semantics.** Image 1 is always "Character / subject reference" — never "Logo reference" or "Background reference." Image 7 is always "Creative / freeform / composite reference."
4. **Video slots are flexible** but should follow the convention:
   - Video 1: Primary motion / choreography / action reference
   - Video 2: Camera motion reference
   - Video 3: VFX, pacing, timing, transition, or creative mood reference
5. **Creative video passthrough**: `SlotImageBatch` provides a `creative_video` input (VIDEO type) that passes straight through to downstream video nodes. Use this for unstructured motion references — mood clips, pacing inspiration, or B-roll that informs the overall energy without locking a specific action.
6. **Explicit reference locks** must follow the slot mapping in the prompt body: "The character must match Image 1 exactly" / "The product must match Image 2 exactly" / "The environment must match Image 4 exactly." For Image 7, use holistic locks: "The overall visual approach follows the creative reference in Image 7 — adopt its color palette, layout energy, and compositional style."
7. **Template naming** in `PromptTemplateLoader` uses the format: `category/file_name: Template Letter - Template Name`. The system prompt uses `category/file_name: system_prompt`.

### Slot Numbering & Batch Position (CRITICAL)

**The batch position does NOT equal the slot number.** `SlotImageBatch` outputs a sparse batch containing only the filled slots. If a user provides:
- Slot 1 (character) and Slot 7 (creative)

The batch has **2 images** at positions `[0, 1]`, but they are **Image 1** and **Image 7**, not Image 1 and Image 2.

**All system prompts MUST include this instruction** (copy verbatim):

```
2. **Slot Format & Image Numbering (CRITICAL — DO NOT IGNORE)**:
   - The reference images use a **fixed 7-slot semantic system**. Each image has a slot label burned into its top-left corner: **1-CHAR, 2-COSTUME, 3-PROP, 4-ENV, 5-PRODUCT, 6-STYLE, 7-CREATIVE**.
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
- [ ] Every user template code block starts with the **exact** 6+1-slot `Reference mapping (SLOT FORMAT — swap any images into these slots):` block
- [ ] All 6 core image slots + Image 7 use the **exact** universal semantics listed above
- [ ] Unused core slots are marked `(optional — not used in this template)`
- [ ] Image 7 is marked `(optional — not used if no creative reference provided)`
- [ ] Video slots mention pacing / mood / creative reference for Video 3
- [ ] System prompt contains the **Slot Format & Image Numbering** section with the exact 6-bullet text (subset handling, slot-number referencing, anti-positional-counting, Image 1+7 example, empty-slot guidance)
- [ ] System prompt's reference integration section starts with **"ALWAYS refer to images by their SLOT NUMBER"**
- [ ] Prompt output is wrapped in `[[PROMPT]]` / `[[/PROMPT]]` tags
- [ ] No markdown, bullets, or line breaks inside the prompt body
- [ ] Word count guidance is provided per pattern

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

No markdown, no bullets, no line breaks inside the prompt body.

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
- [ ] List all 8 columns explicitly: SHOT, VISUAL DESCRIPTION, DIALOGUE/VO, SFX, AUDIO/MUSIC, CAMERA, TRANSITION, DURATION
- [ ] Enforce CTA end card: final shot must contain offer text, discount, "ORDER NOW" button, brand logo, tagline
- [ ] Add branding consistency rules: logo position, brand color, typography style
- [ ] Verify durations sum correctly and footer states total scene + commercial duration
- [ ] Include bottom summary strip: KEY MESSAGE, VISUAL NOTES, BRANDING ELEMENTS, NEXT SCENE PREVIEW

### Lifestyle Storyboard Checklist (for Cinematic Lifestyle Storyboards only)

If your **lifestyle storyboard** outputs have different faces per panel, sketch quality, or broken mood:

- [ ] Character lock: Describe face, hair, clothing, and distinguishing features in extreme detail at the prompt start. Reference "the same man/woman" for every panel.
- [ ] Mood lock: Define emotional temperature and color grade upfront. Add "ALL panels share the same mood and color grade."
- [ ] Anti-sketch anchors: "photorealistic cinematic photographs," "film still," "shot on 35mm," "arthouse cinema aesthetic," "NOT sketches or illustrations"
- [ ] Caption voice: "poetic, reflective, understated — one sentence reading like literary fiction or a diary entry"
- [ ] Scene curation: Mix exterior and interior daily life scenes. Progress from external activity to internal reflection. Final panel is a close-up detail.
- [ ] Anti-commercial: "NOT commercial photography or advertising. Candid, unposed moments. Natural lighting. Film grain."

### Environment Lock Checklist (for I2V Scene Anchors only)

If your **environment board** outputs have shifting backgrounds or inconsistent prop positions:

- [ ] Add cross-view consistency lock: "Both wide shots show the SAME room from opposite angles"
- [ ] Specify spatial relationships explicitly: "If a lamp is on the left in Camera A, it must be on the right in Camera B (reverse perspective)"
- [ ] List 4–8 key props with numbers and visual descriptions for detail callouts
- [ ] Include technical spec bar: aspect, color temp, lens, format
- [ ] Prioritize light-emitting props and interactive objects in the callouts
- [ ] Add lighting lock: "Identical color temperature and weather across all panels"

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
