# TV Commercial Storyboard

Full system prompt, user templates, and anti-patterns for the **TV Commercial Storyboard** (also called Advertisement Shot List, Product Commercial Board, or Campaign Storyboard).

## Overview

A highly structured multi-column production document used to plan TV commercials, product advertisements, or branded content. The output is a single board image containing a table with embedded shot thumbnails, production metadata per shot (dialogue/voiceover, SFX, audio, camera, transitions, duration), plus header branding, scene objectives, and a bottom summary strip.

| Output Type | Single board image — a structured table with embedded shot thumbnails and per-shot production metadata |
|-------------|------------------------------------------------------------------------------------------------------|
| Art Style | Polished, photorealistic, cinematic — each shot thumbnail looks like a finished commercial frame |
| Table Columns | SHOT #, VISUAL DESCRIPTION, DIALOGUE/VOICEOVER, SFX, AUDIO/MUSIC, CAMERA/MOVEMENT, TRANSITION, DURATION |
| Header | Product name, campaign theme, scene info, duration, media type, visual style, pacing, brand logo |
| Footer Strip | Key Message, Visual Notes, Branding Elements, Next Scene Preview |
| Typography | Heavy — shot numbers, column headers, brand copy, dialogue quotes, duration callouts, offer text |

## Visual Assets (Reference Image + Video)

| File | Description |
|------|-------------|
| `assets/tv-commercial-storyboard.jpg` | Static reference image (1536×1024) showing a complete TV commercial storyboard for "MAGIC BLENDER". Header contains: product name "MAGIC BLENDER", campaign theme "Blend Magic. Live Better.", scene 3 of 3, 15 seconds duration, media type "TV COMMERCIAL", visual style "Premium / Modern / High Energy", pacing "FAST", and a brand logo. Below the header is a scene objective bar. The main body is a 5-row table (shots 11–15) with columns: SHOT, VISUAL/SHOT DESCRIPTION (with embedded thumbnail images), DIALOGUE/VOICEOVER, SFX, AUDIO/MUSIC, CAMERA/MOVEMENT, TRANSITION, DURATION. Shot 11 shows a family enjoying smoothies at a kitchen table. Shot 12 shows a product beauty shot with "ALL-IN-ONE. DO IT ALL." overlay and feature checklist (BLEND, CHOP, GRIND, MIX, PUREE). Shot 13 shows a before/after split-screen comparison (cluttered vs clean kitchen). Shot 14 shows a close-up of a woman drinking a green smoothie with satisfaction. Shot 15 shows a hero end card with the product on a dark reflective surface, purple magical energy effects, "MAGIC BLENDER" branding, "BLEND MAGIC. LIVE BETTER." tagline, "LIMITED TIME OFFER! 25% OFF" in large type, and an "ORDER NOW!" call-to-action button. The bottom strip contains: KEY MESSAGE ("Real people, real results. All-in-one benefits. Save time, space, and effort. Strong offer and call to action."), VISUAL NOTES (warm bright natural kitchen lighting, fast pace with energetic cuts, focus on happiness and transformation), BRANDING ELEMENTS (logo top-right, product color purple, clean modern typography, consistent brand identity), and NEXT SCENE PREVIEW (end card / brand bumper or scene change to social proof / testimonials). |
| `assets/tv-commercial-storyboard.mp4` | Reference video (~15 seconds, 16:9 aspect ratio) showing the actual TV commercial that corresponds to the storyboard. Sequence: family at kitchen table enjoying breakfast smoothies → product beauty shot with feature checklist text animating in → before/after split screen → woman drinking green juice smiling → hero end card with 25% off offer. The video demonstrates how the storyboard translates to final commercial footage. |
| `assets/tv-commercial-storyboard-frame.jpg` | First frame extracted from the video for quick visual reference without playing the video. |

### What the Storyboard Looks Like (Visual Specification)

The storyboard is a **single rectangular production document** with a clean corporate design:

- **Header bar** (top ~15%):
  - Left: "TV COMMERCIAL STORYBOARD" in bold, "PRODUCT: MAGIC BLENDER" in purple, "CAMPAIGN THEME: Blend Magic. Live Better." in purple
  - Center: "SCENE: 3 of 3", "DURATION: 15 SECONDS" in purple, "TOTAL SCENE DURATION: 15s / 45s"
  - Right: "MEDIA TYPE: TV COMMERCIAL", "VISUAL STYLE: Premium / Modern / High Energy", "PACING: FAST", and a brand logo icon (purple blender silhouette with "MAGIC BLENDER" text)
- **Scene objective bar**: Full-width strip below header with "SCENE OBJECTIVE:" label and one-sentence goal
- **Main table** (~65% of the board):
  - Column headers in bold: SHOT, VISUAL / SHOT DESCRIPTION, DIALOGUE / VOICEOVER, SFX, AUDIO / MUSIC, CAMERA / MOVEMENT, TRANSITION, DURATION
  - Each row = one shot with:
    - Shot number (large, e.g., "11") and shot name (e.g., "REAL PEOPLE ENJOYING") and timecode (e.g., "0:00 - 0:02.5")
    - A thumbnail image showing the commercial frame
    - Text description of the visual
    - Dialogue or voiceover text in quotes
    - SFX description
    - Audio/music cue
    - Camera angle and movement
    - Transition type (e.g., "Quick Cut", "Match Cut", "Smash Cut", "Fade Out")
    - Duration (e.g., "2.5s" in purple)
- **Bottom summary strip** (~20%):
  - Four sub-sections side by side with icons:
    - KEY MESSAGE: bullet points summarizing the scene's selling points
    - VISUAL NOTES: lighting, pacing, mood direction
    - BRANDING ELEMENTS: logo placement, color, typography rules
    - NEXT SCENE PREVIEW: what follows this scene
- **Footer bar**: "NOTE: TOTAL SCENE DURATION = 15 SECONDS | TOTAL COMMERCIAL = 45 SECONDS (3 SCENES)"

This serves as the **gold standard** for what a TV Commercial Storyboard should look like: structured, branded, production-ready, with every shot containing full audio-visual metadata.

---

## The Master System Prompt

Copy-paste this directly into the system prompt field of your commercial storyboard-generation agent.

```
You are an elite commercial pre-production director specializing in TV advertisement storyboards and product campaign planning. Your sole function is to generate structured commercial storyboard boards — single images containing a multi-row production table with embedded shot thumbnails, dialogue/voiceover, SFX, audio, camera, transitions, and durations.

## CORE TASK

1. **Document Structure — Header + Table + Footer**: The output is a SINGLE IMAGE containing a complete commercial storyboard document.
   - **Header bar**: Product name, campaign theme/tagline, scene number (e.g., "Scene 3 of 3"), scene duration, total commercial duration, media type (TV COMMERCIAL / SOCIAL AD / PRODUCT VIDEO), visual style descriptor, pacing (FAST / MODERATE / SLOW), and a small brand logo or icon.
   - **Scene objective bar**: One clear sentence stating what this scene must accomplish.
   - **Main table**: Multi-row table with these exact column headers: SHOT, VISUAL / SHOT DESCRIPTION, DIALOGUE / VOICEOVER, SFX, AUDIO / MUSIC, CAMERA / MOVEMENT, TRANSITION, DURATION.
   - **Bottom summary strip**: Four sections — KEY MESSAGE (selling points), VISUAL NOTES (lighting, mood, pacing), BRANDING ELEMENTS (logo placement, colors, typography), NEXT SCENE PREVIEW (what comes after).
   - **Footer bar**: Total duration note and scene count.

2. **Shot Row Structure**: Every row contains:
   - Shot number (sequential, may continue from previous scenes) and shot name in bold
   - Timecode range (e.g., "0:00 - 0:02.5")
   - A thumbnail image showing the commercial frame — photorealistic, cinematic, polished
   - Visual description text
   - Dialogue or voiceover text in quotation marks, prefixed with "VO:" for voiceover
   - SFX description
   - Audio/music cue description
   - Camera angle and movement description
   - Transition type (Quick Cut, Match Cut, Smash Cut, Fade In, Fade Out, Cross Dissolve, Wipe, etc.)
   - Duration in seconds (e.g., "2.5s")

3. **Art Quality — Polished & Photorealistic**: Unlike action storyboards, commercial storyboards show finished-quality frames.
   - Each thumbnail is a photorealistic commercial-grade image — cinematic lighting, shallow depth of field, professional color grading.
   - Product shots must look like hero beauty shots: clean backgrounds, dramatic lighting, premium materials visible.
   - Lifestyle shots must look aspirational: warm natural lighting, happy authentic moments, premium environments.
   - Text overlays within thumbnails (offer text, feature lists, taglines) must be clean, readable, and professionally designed.
   - The overall document aesthetic is corporate-premium: clean lines, organized grids, professional typography.

4. **Audio-Visual Integration**: Every shot row must include complete audio metadata:
   - DIALOGUE/VOICEOVER: Exact spoken lines in quotes. Keep concise — commercial VO is punchy and brief.
   - SFX: Specific sound effects that reinforce the visual (product sounds, transitions, ambient audio).
   - AUDIO/MUSIC: Music cues — build, peak, soften, hit, continues, ends.
   - The audio column should show how music and sound design support the visual narrative arc.

5. **Commercial Narrative Arc**: The shots must follow proven advertising structure:
   - **Hook**: Immediate emotional connection or problem statement (lifestyle shot, relatable moment, or striking product reveal).
   - **Product Reveal / Benefit Demonstration**: Hero product shot showing features, benefits, or transformation. Use text overlays to highlight selling points.
   - **Proof / Comparison**: Before/after, testimonial reaction, or problem-solution visualization.
   - **Emotional Payoff**: Satisfied user, happy moment, result enjoyment.
   - **Call to Action (CTA)**: End card with offer, discount, urgency, and clear next step. Large typography, brand logo, offer text, button-style CTA.
   - Pacing must escalate: lifestyle shots are calm and warm; product shots are dynamic; CTA is bold and urgent.

6. **Branding Consistency**: Brand elements must be consistent across all shots:
   - Logo placement follows a rule (e.g., "top right corner of CTA shots").
   - Brand color appears in UI elements, text highlights, or product accents.
   - Typography style is consistent — modern sans-serif, bold weights for headlines.
   - Tagline/slogan appears at least once in full form.
   - Product name is clearly visible on the product or in text overlays.

7. **Column Formatting Lock**: The table must look like a professional production document.
   - Column widths are balanced — visual description column is widest, duration column is narrowest.
   - Text is readable at document scale — no microscopic fonts.
   - Headers are bold and distinct from row content.
   - Duration values are visually emphasized (color, bold, or larger size).
   - Transition types are called out clearly per shot.

## MODEL-AWARE OPTIMIZATION
The refined prompt feeds into: OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit.
- For **generation models** (GPT Image, Seedream, Gemini): Emphasize the document-as-table structure. Because commercial storyboards need MORE words than single-subject prompts (header + 5+ rows + columns + audio + camera + bottom strip), target **500–900 words**. Describe the header, each shot row individually, and the bottom strip explicitly.
- For **editing models** (Grok Image Edit, Qwen image edit): If modifying an existing board, prepend: "Preserve the table structure, column headers, and document layout. Modify only the shot thumbnails, dialogue text, and product imagery within each row."
- **Explicit Purpose / Type**: Always open with: "A TV commercial storyboard document," "advertisement shot list board," or "product campaign planning sheet."

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning. Output ONLY the final prompt.
2. **NO FORMATTING**: No markdown, bullet points, headers, bold text, numbered lists, or line breaks within the prompt body.
3. **STRUCTURE**: Output as a single flowing paragraph (or two connected paragraphs if complexity demands). Target: **500–900 words**.
4. **DELIMITERS**: Wrap the entire prompt in `[[PROMPT]]` and `[[/PROMPT]]` tags.
5. **NO EXTERNAL TEXT**: Nothing outside the `[[PROMPT]]` tags will be parsed.
6. **MANDATORY COVERAGE**: The prompt must include: header structure (product, theme, scene, duration, style, pacing, logo), scene objective, table column headers, per-shot structure (number, name, timecode, thumbnail, visual, dialogue/VO, SFX, audio, camera, transition, duration), commercial narrative arc (hook/benefit/proof/CTA), branding consistency rules, bottom summary strip (key message, visual notes, branding elements, next scene), and footer duration note.
7. **QUALITY ENFORCEMENT**: Explicitly state that thumbnails are photorealistic commercial frames, not sketches. If the model drifts toward illustration quality, anchor with "photorealistic commercial frame," "cinematic product photography," "premium lifestyle photography," and "professional advertising visual."

## PROHIBITIONS
- NEVER generate rough sketches, gesture drawings, or unfinished thumbnails. Commercial storyboards show polished final-quality frames.
- NEVER omit the audio columns (SFX, AUDIO/MUSIC) or dialogue/voiceover column.
- NEVER use inconsistent branding — logo placement, colors, and typography must follow a unified rule.
- NEVER create a storyboard without a clear call-to-action shot at the end.
- NEVER let shot durations fail to sum correctly to the stated scene total.
- Do not include aspect ratios, resolution specs, model names, or UI instructions inside the prompt.
- Do not output multiple prompt variants; output one unified optimized prompt.
```

---

## User Prompt Templates

### Template A: Full Commercial with All Shots Defined

```
Generate a TV commercial storyboard document for a 15-second product advertisement.

Header: Product "MAGIC BLENDER", campaign theme "Blend Magic. Live Better.", Scene 3 of 3, duration 15 seconds, total commercial 45 seconds (3 scenes), media type TV COMMERCIAL, visual style Premium / Modern / High Energy, pacing FAST. Include a purple blender brand logo top-right.

Scene objective: Show real people enjoying the results, highlight the all-in-one benefits, and finish with a strong call to action.

Table columns: SHOT, VISUAL / SHOT DESCRIPTION, DIALOGUE / VOICEOVER, SFX, AUDIO / MUSIC, CAMERA / MOVEMENT, TRANSITION, DURATION.

Shot 11 — REAL PEOPLE ENJOYING (0:00 - 0:02.5): Family of three enjoying smoothies together at a modern kitchen table. Warm natural lighting, happy healthy lifestyle moment. VO: "Delicious results. Every time." SFX: Happy ambient kitchen sounds. Audio: Upbeat music continues. Camera: Wide shot, slight push-in. Transition: Quick Cut. Duration: 2.5s.

Shot 12 — ALL-IN-ONE BENEFITS (0:02.5 - 0:05.0): Hero product beauty shot of black blender filled with colorful fruits on a kitchen island. Text overlay "ALL-IN-ONE. DO IT ALL." with checkmarks for BLEND, CHOP, GRIND, MIX, PUREE. Product and attachments displayed. VO: "Blend, chop, grind, mix, puree — all in one powerful machine." SFX: Whoosh + UI pop sound. Audio: Music builds with energy. Camera: Product beauty shot, orbit around, slow motion. Transition: Match Cut. Duration: 2.5s.

Shot 13 — TIME & SPACE SAVING (0:05.0 - 0:07.5): Split-screen before/after comparison. Left: cluttered dark kitchen with multiple appliances. Text "BEFORE. CLUTTERED. SLOW." Right: clean bright kitchen with single blender. Text "AFTER. CLEAN. FAST." Purple dividing line. VO: "Less clutter. More space. Faster results. That's magic." SFX: Swish transition sound. Audio: Music hits positive peak. Camera: Split screen, static to slight zoom. Transition: Smash Cut. Duration: 2.5s.

Shot 14 — HAPPINESS REACTION (0:07.5 - 0:10.0): Close-up of woman taking a sip of green smoothie, smiling with satisfaction, eyes closed. VO: "Feel the difference. Love the results." SFX: Sip sound + satisfied exhale. Audio: Music softens momentarily. Camera: Close-up, shallow focus, slight handheld. Transition: Quick Cut. Duration: 2.5s.

Shot 15 — STRONG CTA & OFFER (0:10.0 - 0:15.0): Hero product shot on black reflective surface with purple magical energy effects swirling around. Text "MAGIC BLENDER" large left, "BLEND MAGIC. LIVE BETTER." below, "LIMITED TIME OFFER! 25% OFF" large right, "ORDER NOW!" button. Blender surrounded by fresh fruits. VO: "Magic Blender. Blend Magic. Live Better. Get yours today!" SFX: Magical whoosh + chime. Audio: Music rises big and inspiring, ends on hit. Camera: Low angle hero shot, slow dolly in. Transition: Fade Out (End). Duration: 5.0s.

Bottom strip: KEY MESSAGE — Real people, real results. All-in-one benefits. Save time, space, and effort. Strong offer and call to action. VISUAL NOTES — Warm, bright, natural kitchen lighting. Fast pace with energetic cuts. Focus on happiness and transformation. BRANDING ELEMENTS — Logo top-right on CTA shots, product color purple, clean modern typography, consistent brand identity. NEXT SCENE PREVIEW — End card / brand bumper or scene change to social proof / testimonials.

Footer: TOTAL SCENE DURATION = 15 SECONDS | TOTAL COMMERCIAL = 45 SECONDS (3 SCENES)

Art quality: Photorealistic commercial frames. Cinematic lighting. Premium product photography. Professional advertising visuals. Polished text overlays.
```

### Template B: Minimal Template with Auto-Sequence

```
Generate a TV commercial storyboard document for a [DURATION]-second product advertisement.

Header: Product "[PRODUCT NAME]", campaign theme "[TAGLINE]", Scene [X] of [Y], media type TV COMMERCIAL, visual style [STYLE], pacing [PACING]. Include brand logo.

Scene objective: [One sentence goal].

Table: SHOT, VISUAL DESCRIPTION, DIALOGUE/VO, SFX, AUDIO/MUSIC, CAMERA/MOVEMENT, TRANSITION, DURATION.

Shot structure: [NUMBER] shots following commercial arc — Hook → Product/Benefit → Proof/Comparison → Emotional Payoff → CTA.

Per shot provide: shot number, name, timecode, visual description, VO line, SFX, audio cue, camera angle, transition, duration.

Bottom strip: KEY MESSAGE, VISUAL NOTES, BRANDING ELEMENTS, NEXT SCENE PREVIEW.

Art quality: Photorealistic commercial frames. Cinematic product photography. Premium lifestyle shots. Professional typography and text overlays.

Reference images attached for product, lifestyle context, and brand style.
```

### Template C: Editing an Existing Board (for Grok / Qwen)

```
Base commercial storyboard image attached. Preserve the table structure, column headers, header bar, bottom summary strip, and document layout.

Reference images for product update, new lifestyle shots, and revised branding attached.

Task: Modify the shot thumbnails, dialogue/voiceover text, and product imagery within each row to match the new campaign. Keep the same table format, column headers, duration column styling, and bottom strip structure. Update the header with new product name, campaign theme, and scene info. Maintain branding consistency across all shots. Output a prompt describing the updated commercial storyboard.
```

---

## Common Anti-Patterns

### Sketch Quality Drift

**Symptom:** Shot thumbnails look like rough pencil sketches, storyboard thumbnails, or unfinished illustrations instead of polished commercial frames.

**Cause:** Model confuses commercial storyboard with cinematic action storyboard (which uses rough sketches).

**Fix:** Add explicit quality anchors: "photorealistic commercial frames," "cinematic product photography," "premium lifestyle photography," "professional advertising visuals," "polished final-quality frames," "NOT sketches or rough drawings." Open the prompt with: "A TV commercial storyboard document with photorealistic shot thumbnails."

### Missing Audio Columns

**Symptom:** Table only has shot numbers and visual descriptions — no dialogue, SFX, or audio columns.

**Cause:** Prompt doesn't explicitly list all required columns.

**Fix:** List all eight columns explicitly in order: "SHOT, VISUAL / SHOT DESCRIPTION, DIALOGUE / VOICEOVER, SFX, AUDIO / MUSIC, CAMERA / MOVEMENT, TRANSITION, DURATION." Emphasize that every row must include all columns.

### Weak or Missing CTA

**Symptom:** Final shot is just another lifestyle frame without offer text, discount, or call-to-action button.

**Cause:** Commercial narrative arc not enforced; model treats all shots equally.

**Fix:** Explicitly require the final shot to be a "Call to Action end card" with: large offer text, percentage discount, "ORDER NOW" or "BUY NOW" button-style text, brand logo, and tagline. State: "The final shot MUST be a bold CTA end card with promotional offer text."

### Inconsistent Branding

**Symptom:** Logo appears in different positions shot-to-shot, brand color changes, typography style varies between thumbnails.

**Cause:** No branding consistency rule specified.

**Fix:** Add branding rules: "Logo always appears [position] on [which shots]," "Brand color [color] appears in text highlights and UI elements," "Typography: modern sans-serif, bold for headlines." Include a BRANDING ELEMENTS section in the bottom strip.

### Duration Mismatch

**Symptom:** Shot durations don't add up to the stated scene total, or durations are missing/uneven.

**Cause:** Durations not specified per shot or not summed.

**Fix:** Specify exact duration for every shot and verify the total. Add: "Shot durations must sum to [TOTAL] seconds." Use the duration column format: "2.5s", "5.0s" etc. Emphasize that the footer must state the total scene and commercial duration.

---

## Good vs Bad Examples

### Good — Full Commercial Storyboard Prompt

> A TV commercial storyboard document for a 15-second product advertisement for MAGIC BLENDER, campaign theme Blend Magic Live Better, Scene 3 of 3, total commercial 45 seconds across 3 scenes, media type TV COMMERCIAL, visual style Premium Modern High Energy, pacing FAST, with a purple blender brand logo in the top-right corner. The header bar shows product name campaign theme scene info duration media type visual style and pacing. Below the header is a scene objective bar stating Show real people enjoying the results highlight the all-in-one benefits and finish with a strong call to action. The main body is a 5-row production table with columns SHOT VISUAL SHOT DESCRIPTION DIALOGUE VOICEOVER SFX AUDIO MUSIC CAMERA MOVEMENT TRANSITION DURATION. Shot 11 REAL PEOPLE ENJOYING 0:00 to 0:02.5 shows a photorealistic thumbnail of a family of three enjoying smoothies at a modern kitchen table with warm natural lighting and a happy healthy lifestyle moment, VO quote Delicious results Every time, SFX happy ambient kitchen sounds, audio upbeat music continues, camera wide shot slight push-in, transition quick cut, duration 2.5s. Shot 12 ALL-IN-ONE BENEFITS 0:02.5 to 0:05.0 shows a hero product beauty shot of a black blender filled with colorful fruits on a kitchen island with text overlay ALL-IN-ONE DO IT ALL and checkmarks for BLEND CHOP GRIND MIX PUREE, VO quote Blend chop grind mix puree all in one powerful machine, SFX whoosh plus UI pop sound, audio music builds with energy, camera product beauty shot orbit around slow motion, transition match cut, duration 2.5s. Shot 13 TIME AND SPACE SAVING 0:05.0 to 0:07.5 shows a split-screen before-after comparison with left side cluttered dark kitchen text BEFORE CLUTTERED SLOW and right side clean bright kitchen text AFTER CLEAN FAST separated by a purple dividing line, VO quote Less clutter More space Faster results That's magic, SFX swish transition sound, audio music hits positive peak, camera split screen static to slight zoom, transition smash cut, duration 2.5s. Shot 14 HAPPINESS REACTION 0:07.5 to 0:10.0 shows a close-up of a woman taking a sip of green smoothie smiling with satisfaction eyes closed, VO quote Feel the difference Love the results, SFX sip sound plus satisfied exhale, audio music softens momentarily, camera close-up shallow focus slight handheld, transition quick cut, duration 2.5s. Shot 15 STRONG CTA AND OFFER 0:10.0 to 0:15.0 shows a hero product shot on a black reflective surface with purple magical energy effects swirling around the blender surrounded by fresh fruits, large text MAGIC BLENDER left side tagline BLEND MAGIC LIVE BETTER below it, right side LIMITED TIME OFFER 25 PERCENT OFF in large type and an ORDER NOW button, VO quote Magic Blender Blend Magic Live Better Get yours today, SFX magical whoosh plus chime, audio music rises big and inspiring ends on hit, camera low angle hero shot slow dolly in, transition fade out end, duration 5.0s. The bottom summary strip contains four sections KEY MESSAGE with bullet points Real people real results All-in-one benefits Save time space and effort Strong offer and call to action, VISUAL NOTES with warm bright natural kitchen lighting fast pace with energetic cuts focus on happiness and transformation, BRANDING ELEMENTS with logo top-right on CTA shots product color purple clean modern typography consistent brand identity, NEXT SCENE PREVIEW with end card brand bumper or scene change to social proof testimonials. The footer bar states TOTAL SCENE DURATION EQUALS 15 SECONDS TOTAL COMMERCIAL EQUALS 45 SECONDS 3 SCENES. All thumbnails are photorealistic commercial frames with cinematic lighting and premium product photography quality. Professional advertising visual style throughout.

### Bad — Too Vague

> A storyboard for a blender commercial. 5 shots. Family eating, product shot, before/after, woman drinking, end card with discount.

### Bad — Wrong Art Style (Sketch Instead of Photorealistic)

> A rough sketch storyboard for a TV commercial showing 5 hand-drawn panels of a family with a blender, product demonstration, and sale end card. Pencil thumbnails with loose gesture lines.

---

## Model-Specific Notes

| Model | Commercial Storyboard Generation Tip |
|-------|-------------------------------------|
| **GPT Image** | Excellent at following complex table structures and generating photorealistic commercial frames. Provide explicit per-shot descriptions. |
| **Seedream** | Good at product photography and lifestyle aesthetics. Emphasize "premium commercial photography" and "advertising visual." |
| **Gemini** | Handles long prompts well. Can manage 800+ word commercial storyboard descriptions with full audio-visual metadata. |
| **Grok / Qwen** | Best for editing existing boards. Always preserve table structure and column headers first, then modify shot content and branding. |
