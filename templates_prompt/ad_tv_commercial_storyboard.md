# Ad TV Commercial Storyboard

System prompt and user templates for creating **TV commercial storyboards** — structured, multi-row production tables with embedded photorealistic shot thumbnails, dialogue/voiceover, SFX, audio cues, camera directions, transitions, and durations. Used for TV ads, product videos, branded content, and social media commercial planning.

---

## When to Use

- TV commercial pre-production planning
- Product launch video storyboards
- Social media ad campaign shot lists (Instagram Reels, TikTok, YouTube ads)
- Branded content production documents
- Client pitch decks with visual shot breakdowns
- Direct-response advertisement planning (infomercials, DRTV)

## Output

**A single board image** containing a structured production table with embedded shot thumbnails, per-shot audio-visual metadata, header branding, scene objectives, and a bottom summary strip.

| Element | Description |
|---------|-------------|
| **Art Style** | Polished, photorealistic, cinematic — each shot thumbnail looks like a finished commercial frame |
| **Table Columns** | SHOT #, VISUAL DESCRIPTION, DIALOGUE/VOICEOVER, SFX, AUDIO/MUSIC, CAMERA/MOVEMENT, TRANSITION, DURATION |
| **Header** | Product name, campaign theme, scene info, duration, media type, visual style, pacing, brand logo |
| **Footer Strip** | KEY MESSAGE, VISUAL NOTES, BRANDING ELEMENTS, NEXT SCENE PREVIEW |
| **Typography** | Heavy — shot numbers, column headers, brand copy, dialogue quotes, duration callouts, offer text |

---

## The System Prompt

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

### Template A: Full Commercial with All Shots Defined (Recommended)

```
Generate a TV commercial storyboard document for a [DURATION]-second product advertisement.

Header: Product "[PRODUCT NAME]", campaign theme "[TAGLINE]", Scene [X] of [Y], duration [DURATION] seconds, total commercial [TOTAL DURATION] ([SCENES] scenes), media type [TV COMMERCIAL / SOCIAL AD / PRODUCT VIDEO], visual style [STYLE], pacing [FAST / MODERATE / SLOW]. Include [COLOR] brand logo [POSITION].

Scene objective: [One sentence goal].

Table columns: SHOT, VISUAL / SHOT DESCRIPTION, DIALOGUE / VOICEOVER, SFX, AUDIO / MUSIC, CAMERA / MOVEMENT, TRANSITION, DURATION.

Shot [N] — [SHOT NAME] ([TIMECODE]): [Visual description]. [VO line in quotes]. SFX: [sound effect]. Audio: [music cue]. Camera: [angle/movement]. Transition: [type]. Duration: [X.X]s.

[Repeat for each shot, following Hook → Product/Benefit → Proof/Comparison → Emotional Payoff → CTA arc.]

Bottom strip: KEY MESSAGE — [selling points]. VISUAL NOTES — [lighting, mood, pacing]. BRANDING ELEMENTS — [logo placement, colors, typography]. NEXT SCENE PREVIEW — [what follows].

Footer: TOTAL SCENE DURATION = [DURATION] SECONDS | TOTAL COMMERCIAL = [TOTAL DURATION] ([SCENES] SCENES)

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

### Good — Full Commercial Storyboard Prompt (Abbreviated)

> A TV commercial storyboard document for a 15-second product advertisement for MAGIC BLENDER, campaign theme Blend Magic Live Better, Scene 3 of 3, total commercial 45 seconds across 3 scenes, media type TV COMMERCIAL, visual style Premium Modern High Energy, pacing FAST, with a purple blender brand logo in the top-right corner. The header bar shows product name campaign theme scene info duration media type visual style and pacing. Below the header is a scene objective bar stating Show real people enjoying the results highlight the all-in-one benefits and finish with a strong call to action. The main body is a 5-row production table with columns SHOT VISUAL SHOT DESCRIPTION DIALOGUE VOICEOVER SFX AUDIO MUSIC CAMERA MOVEMENT TRANSITION DURATION. Shot 11 REAL PEOPLE ENJOYING 0:00 to 0:02.5 shows a photorealistic thumbnail of a family of three enjoying smoothies at a modern kitchen table with warm natural lighting and a happy healthy lifestyle moment, VO quote Delicious results Every time, SFX happy ambient kitchen sounds, audio upbeat music continues, camera wide shot slight push-in, transition quick cut, duration 2.5s. Shot 12 ALL-IN-ONE BENEFITS 0:02.5 to 0:05.0 shows a hero product beauty shot of a black blender filled with colorful fruits on a kitchen island with text overlay ALL-IN-ONE DO IT ALL and checkmarks for BLEND CHOP GRIND MIX PUREE, VO quote Blend chop grind mix puree all in one powerful machine, SFX whoosh plus UI pop sound, audio music builds with energy, camera product beauty shot orbit around slow motion, transition match cut, duration 2.5s. [Continue for remaining shots...] Bottom strip contains KEY MESSAGE Real people real results all-in-one benefits save time space and effort strong offer and call to action, VISUAL NOTES warm bright natural kitchen lighting fast pace with energetic cuts focus on happiness and transformation, BRANDING ELEMENTS logo top-right on CTA shots product color purple clean modern typography consistent brand identity, NEXT SCENE PREVIEW end card brand bumper or scene change to social proof testimonials. Footer states TOTAL SCENE DURATION = 15 SECONDS TOTAL COMMERCIAL = 45 SECONDS 3 SCENES. Photorealistic commercial frames, premium product photography, professional advertising visuals.

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
