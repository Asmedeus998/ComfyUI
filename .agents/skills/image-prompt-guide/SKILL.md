---
name: image-prompt-guide
description: Reference system prompt and best practices for multi-image prompt synthesis. Use when building or tuning an AI agent that analyzes multiple reference images, audits an existing generated prompt, and outputs a refined prompt optimized for image generation across OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit. Covers Reference Element Fusion (single-subject composite), Art Director Presentation Boards (multi-section documents), Cinematic Action Storyboards (multi-panel rough sketch grids with motion annotations), TV Commercial Storyboards (structured production tables with audio-visual metadata), Cinematic Lifestyle Storyboards (photorealistic character-driven daily life montages), Environment Reference Locks (I2V scene anchors), single-subject locks, anti-collage enforcement, cross-model compatibility, and domain-agnostic prompt engineering.
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
- Targeting multiple backend models from a single prompt output.
- Debugging why generated images contain **collages, grids, multiple panels, or duplicate subjects** when they should be single-subject photographs.
- Debugging why **presentation boards** have overlapping sections, missing panels, inconsistent art styles, or gibberish typography.
- Debugging why **cinematic storyboards** look too polished (sketch quality drift), lack annotation arrows, have character drift between panels, or break spatial continuity.
- Debugging why **commercial storyboards** look like rough sketches instead of photorealistic frames, miss audio columns, have weak CTAs, inconsistent branding, or duration mismatches.
- Debugging why **lifestyle storyboards** have character face drift between panels, mood breaks (one panel suddenly bright/cheerful), sketch/illustration quality instead of photorealism, missing captions, or commercial photography drift.
- Debugging why **environment lock boards** have spatial drift between camera views, missing prop callouts, inconsistent lighting, or absent technical spec bars.
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

## Usage in ComfyUI

See `AGENTS.md` in the project root for ComfyUI runtime conventions.
