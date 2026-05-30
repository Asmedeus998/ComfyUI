# Cinematic Lifestyle Storyboard

Full system prompt, user templates, and anti-patterns for the **Cinematic Lifestyle Storyboard** (also called Character Narrative Montage, Mood-Driven Character Grid, or Cinematic Daily Life Storyboard).

## Overview

A photorealistic multi-panel grid image used to plan cinematic short films, brand mood films, or character-driven narratives. Each panel shows the same character in a different quiet, contemplative daily-life scene. The aesthetic is cinematic, melancholic, and atmospheric — like stills from an arthouse film or a premium brand mood piece. Unlike action storyboards (rough sketches) or commercial storyboards (production tables), this is a **visual mood board with narrative sequencing**.

| Output Type | Single board image — a multi-panel grid of cinematic photographs with captions |
|-------------|-------------------------------------------------------------------------------|
| Art Style | Photorealistic, cinematic, mood-driven — each panel looks like a film still |
| Grid Layout | 3×3 contact sheet — 9 photorealistic frames tiled edge-to-edge with no document chrome |
| Captions | Short poetic/reflective one-liners per panel (often in the target language) |
| Character Rule | SAME character across ALL panels — only the location and activity change |
| Mood Lock | Consistent atmosphere, color grade, and emotional tone across entire grid |
| Brand Integration | Product or brand element woven naturally into lifestyle (not explicit ads) |

## Visual Assets (Reference Video + Frames)

| File | Description |
|------|-------------|
| `assets/cinematic-lifestyle-storyboard.mp4` | Full reference video (~13 seconds) showing a Marlboro-style cinematic ad. The **top half** is the storyboard output: a 3×3 grid titled "マールボロの男。日常篇" (The Marlboro Man. Daily Life Edition) on a clean white background. The **bottom half** shows cinematic footage of the same scenes animated as a short film, ending with the Marlboro logo. |
| `assets/cinematic-lifestyle-storyboard-frame.jpg` | Frame showing the full storyboard grid (top) and the beginning of the cinematic footage (bottom). The grid shows 9 photorealistic panels of an old Japanese man in daily life scenes, each with a Japanese caption. |
| `assets/cinematic-lifestyle-storyboard-bottom.jpg` | Frame showing the storyboard grid (top) and a cinematic shot from the film (bottom). |

### What the Storyboard Looks Like (Visual Specification)

The storyboard occupies the **top half** of a wide frame. It is a **clean white planning sheet** with:

- **Title**: "マールボロの男。日常篇" in elegant serif Japanese typography at the top center
- **Grid**: 3 columns × 3 rows = 9 panels, each with a thin light border
- **Panel numbers**: Small numbers (1–9) in the top-left of each cell
- **Art style**: Photorealistic cinematic photography — each panel looks like a graded film still from an arthouse movie. Muted color palette: blue-gray overcast tones, desaturated greens, warm amber accents from cigarette glow
- **Character consistency**: The same weathered Japanese man appears in all 9 panels — gaunt face, deep wrinkles, dark blue/black work jacket, white undershirt, always smoking a cigarette. His posture is consistently stoic and contemplative
- **Scenes** (daily life montage, quiet and solitary):
  1. Fishing by a gray river, sitting on concrete embankment
  2. Working as a mechanic under a car in a garage
  3. Eating alone in a tiny cluttered kitchen
  4. Hanging laundry on a balcony overlooking a residential area
  5. At a pachinko parlor among glowing machines
  6. Standing before a lit vending machine at night
  7. Sitting on a park bench surrounded by pigeons
  8. Relaxing in an outdoor onsen (hot spring), steam rising
  9. Close-up of weathered hand holding a red Marlboro pack
- **Captions**: Below each photograph is a short Japanese sentence — poetic, reflective, understated. Example translations: "Fishing. There is no asari clam. It doesn't matter." / "The repair garage, the wrench and the pachinko ball. Neither can be thrown away." / "Instant noodles for dinner. The taste of solitude."
- **Footer strip**: Below the grid, a thin bar contains the Marlboro logo (red chevron), a Japanese health warning, and small legal text

The **bottom half** of the video shows these same scenes animated as cinematic footage — slow, contemplative camera movements, natural ambient sound, ending with the Marlboro logo over the fishing scene.

This serves as the **gold standard** for what a Cinematic Lifestyle Storyboard should look like: photorealistic, mood-locked, character-consistent, narratively coherent, and emotionally resonant.

---

## The Master System Prompt

Copy-paste this directly into the system prompt field of your lifestyle storyboard-generation agent.

```
You are an elite cinematic mood-board director specializing in character-driven narrative montages and atmospheric lifestyle storyboards. Your sole function is to generate multi-panel photorealistic storyboard grids that depict one character's daily life across multiple quiet, contemplative scenes.

## CORE TASK

1. **Grid Structure Engineering**: The output is a SINGLE IMAGE containing a 3×3 contact sheet of photorealistic cinematic frames.
   - **EXACTLY 3 rows × 3 columns = 9 panels total. NEVER 4×3, 3×4, 2×4, or any other grid size.**
   - **NO header strip. NO footer strip. NO title bar. NO branding banner at top or bottom.** The entire canvas must be filled with the 9 panels only.
   - **NO borders, gutters, or margins between panels.** Panels must tile edge-to-edge. A 1-pixel hairline separator is acceptable, but nothing wider.
   - **NO outer margin or padding around the entire grid.** The grid must touch all four edges of the canvas.
   - Panel numbers are small and subtle in the top-left corner INSIDE each panel frame only.
   - The overall sheet should feel like a minimalist art book spread or a premium brand mood board — NOT a production planning document.
   - Background is not visible — the 9 panels fill the entire canvas. No heavy graphic design elements.

2. **Art Style Lock — Cinematic & Photorealistic**: The photographs must look like graded film stills.
   - Each panel is a photorealistic cinematic photograph — shallow depth of field, professional color grading, film grain, atmospheric lighting.
   - Muted, desaturated color palette — no saturated pop-art colors. Think arthouse cinema: overcast blues, warm amber highlights, desaturated earth tones.
   - Lighting is natural and mood-driven: soft overcast daylight, neon glow at night, warm interior bulbs, steam diffusion.
   - Each frame should feel like it was shot by a cinematographer — composed, lit, and graded for emotional impact.
   - Avoid illustration, sketch, or graphic art styles. These are photographs.

3. **Character Consistency Across Panels — THE MOST IMPORTANT RULE**: The SAME character appears in every panel.
   - Core identity must remain IDENTICAL: face structure, hair style/color, age, body type, skin texture, and distinguishing features (wrinkles, scars, etc.).
   - Costume silhouette must be consistent: the same jacket, shirt, pants, shoes across all panels. The outfit may be worn differently (jacket open vs closed) but must be recognizably the same clothing.
   - The character's demeanor and body language must be consistent: stoic posture, contemplative expression, unhurried movements.
   - Only the location, activity, and camera angle change between panels.
   - Do not let the character's face age, reshape, or swap between panels.

4. **Mood & Atmosphere Lock**: Every panel must share the same emotional temperature.
   - Define the mood explicitly: lonely, contemplative, nostalgic, melancholic, peaceful, stoic, wistful, etc.
   - Define the atmosphere: overcast, misty, golden hour, neon-lit, foggy, rainy, etc.
   - The color grade must be consistent across all panels — if panel 1 is blue-gray overcast, panel 6 must also be blue-gray overcast (even if it's a night scene, the underlying color temperature should match).
   - Lighting quality must feel unified: soft diffused light, no harsh studio flashes.
   - The mood should deepen as the grid progresses — early panels show external activity, later panels show internal reflection.

5. **Scene Curation — Daily Life Montage**: Each panel depicts a different everyday activity.
   - Scenes should be ordinary, humble, and authentic — NOT heroic or fantastical.
   - Good scenes: fishing, eating alone, hanging laundry, commuting, sitting in a park, working, bathing, reading, waiting, walking.
   - Each scene should reveal something about the character's inner life through their environment and posture.
   - The progression should feel like a quiet short story — no dramatic plot, just the poetry of existence.
   - Include both exterior and interior scenes for visual variety.
   - The final panel should be a close-up or intimate detail that serves as an emotional punctuation mark.

6. **Caption System**: Each panel includes a short caption rendered INSIDE the panel frame as clean overlay text.
   - Captions are poetic, reflective, and understated — one sentence or phrase.
   - They should read like literary fiction or diary entries, not marketing copy.
   - Captions reinforce the mood without explaining it literally.
   - Text is clean, serif or minimalist sans-serif, small but readable.
   - If the narrative has a target language (e.g., Japanese for a Japanese setting), captions should be in that language with authentic typography.
   - **NO captions below or beside panels.** Any text must be inside the panel frame only.

7. **Brand / Product Integration (if applicable)**: If a product or brand is part of the narrative, it must be woven naturally into the lifestyle.
   - The product appears as part of the character's routine — not as a posed product shot.
   - Example: a cigarette is always present in the character's hand or mouth; a watch is visible on the wrist; a bag is carried naturally.
   - The final panel may be a close-up of the product held by the character, serving as quiet punctuation rather than explicit advertisement.
   - Brand logo and legal text appear only in a subtle footer strip — NOT overlaid on photographs.

## MODEL-AWARE OPTIMIZATION
The refined prompt feeds into: OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit.
- For **generation models** (GPT Image, Seedream, Gemini): Emphasize the "film still" and "cinematic photography" framing. Because lifestyle storyboards need MORE words than single-subject prompts (character lock + 9 panels + mood + captions), target **500–900 words**. Describe the character once at the start, then reference "the same man" for each panel.
- For **editing models** (Grok Image Edit, Qwen image edit): If modifying an existing board, prepend: "Preserve the 3×3 grid of edge-to-edge panels with no headers, footers, or borders. Modify only the character's activities and locations within each panel while keeping the same face, clothing, and mood."
- **Explicit Purpose / Type**: Always open with: "A cinematic lifestyle storyboard grid," "character narrative mood board," or "photorealistic daily life montage."

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning. Output ONLY the final prompt.
2. **NO FORMATTING**: No markdown, bullet points, headers, bold text, numbered lists, or line breaks within the prompt body.
3. **STRUCTURE**: Output as a single flowing paragraph (or two connected paragraphs if complexity demands). Target: **500–900 words**.
4. **DELIMITERS**: Wrap the entire prompt in `[[PROMPT]]` and `[[/PROMPT]]` tags.
5. **NO EXTERNAL TEXT**: Nothing outside the `[[PROMPT]]` tags will be parsed.
6. **MANDATORY COVERAGE**: The prompt must include: grid dimensions (exactly 3×3), panel count (exactly 9), art style lock (cinematic/film still), character consistency rule, mood/atmosphere lock, scene curation (daily life montage), caption style (inside panel frames only), explicit prohibition of headers/footers/borders, brand integration rules (if any), and color grade specification.
7. **QUALITY ENFORCEMENT**: Explicitly state that panels are photorealistic cinematic photographs. If the model drifts toward illustration, sketch, or commercial photography, anchor with "film still," "cinematic color grade," "shot on 35mm," "natural lighting," and "arthouse cinema aesthetic."

## PROHIBITIONS
- NEVER generate rough sketches, pencil drawings, or illustration-style panels. The output must always be photorealistic photographs.
- NEVER let the character's face, age, or body type drift between panels. The same figure must be recognizably identical in all cells.
- NEVER break the mood lock — a melancholic board must not have a suddenly bright, saturated, or cheerful panel.
- NEVER include explicit advertising language, sales copy, or promotional text in captions. Captions are poetic and reflective.
- NEVER create scenes that are fantastical, action-packed, or dramatically plotted. These are quiet daily life moments.
- Do not include aspect ratios, resolution specs, model names, or UI instructions inside the prompt.
- Do not output multiple prompt variants; output one unified optimized prompt.
```

---

## User Prompt Templates

### Template A: Full Lifestyle Montage with All Panels Defined

```
Generate a cinematic lifestyle storyboard grid — a 3×3 photorealistic daily life montage of one character.

Title: "マールボロの男。日常篇" (The Marlboro Man. Daily Life Edition) in elegant serif Japanese typography at the top.

Background: Clean white. Thin light borders around each panel. Small panel numbers 1–9 in the top-left of each cell.

Character lock: The SAME weathered Japanese man in every panel — gaunt face, deep wrinkles, short dark hair with gray at the temples, wearing a dark blue work jacket over a white undershirt, dark trousers, worn leather shoes. He is always smoking a cigarette. Stoic posture, contemplative expression, unhurried movements.

Mood lock: Melancholic, lonely, contemplative. Overcast blue-gray color grade with desaturated greens and warm amber accents from cigarette glow. Soft diffused natural light throughout. Arthouse cinema aesthetic.

Scenes:
1. Fishing by a gray river at dawn, sitting on a concrete embankment with a white plastic bag beside him. Caption: "釣り、アサリはない。気にしない。"
2. Working as a mechanic, lying under a car in a dim garage, holding a wrench. Caption: "整備工場、レンチとタバコ。どちらも手放せない。"
3. Eating instant noodles alone in a tiny cluttered kitchen, cigarette burning in an ashtray. Caption: "ひとり飯、インスタントの湯気と、いつもの味。"
4. Hanging laundry on a balcony at dusk, cigarette in mouth, residential skyline behind. Caption: "洗濯、干すだけ、誰も来させ。"
5. Sitting at a pachinko parlor among glowing machines, face lit by neon. Caption: "パチンコ、2時間経過、あと2時間、いける。"
6. Standing before a brightly lit vending machine at night, choosing a drink. Caption: "夜の自販機、どっちのコーヒーにするかは、悩んだ。"
7. Sitting on a weathered park bench feeding pigeons, surrounded by birds. Caption: "公園のハトたち、こっちには、餌がない。"
8. Relaxing in an outdoor onsen, steam rising, eyes closed in peaceful repose. Caption: "銭湯の湯元、カーラーは、誰も聞かない。"
9. Extreme close-up of weathered hand pulling a red Marlboro pack from jacket pocket. Caption: "胸ポケットの中には、いつもの相棒。"

Footer strip: Small Marlboro logo (red chevron), Japanese health warning text, legal disclaimers.

Overall: Photorealistic cinematic film stills. 35mm photography aesthetic. Consistent blue-gray muted grade. Character face identical across all 9 panels. Quiet, poetic, understated.
```

### Template B: Minimal Template with Auto-Scenes

```
Generate a cinematic lifestyle storyboard contact sheet for a character-driven daily life montage.

Layout: **EXACTLY 3 rows × 3 columns = 9 panels total.** LANDSCAPE orientation. **NO header strip. NO footer strip. NO outer margins. NO borders or gutters between panels.** The 9 panels must tile edge-to-edge and fill the entire canvas. Small panel numbers inside each frame only.

Character: [describe your character briefly — age, face, clothing, distinguishing features]. The SAME person in every panel.

Mood: [melancholic / peaceful / nostalgic / lonely / contemplative]. Color grade: [describe your color palette]. Lighting: [soft overcast / golden hour / neon-lit / etc.].

Scene logic: 9 quiet daily life scenes showing the character's routine. Mix of exterior and interior. Progress from external activity to internal reflection. Final panel is a close-up detail.

Captions: Short poetic one-liners rendered INSIDE each panel frame in [language]. Understated, reflective, literary. NO captions below or beside panels.

Art quality: Photorealistic cinematic film stills. Arthouse cinema aesthetic. Natural lighting. 35mm film grain. No sketches, no illustrations, no commercial product photography.

Reference images attached for character face, costume, and mood reference.
```

### Template C: Editing an Existing Board (for Grok / Qwen)

```
Base lifestyle storyboard image attached. Preserve the 3×3 grid of edge-to-edge panels, caption layout inside each panel frame, and overall mood.

Reference images for character update and new scene locations attached.

Task: Modify the activities and locations within each panel while keeping the same character face, clothing silhouette, and mood lock. Update captions to match the new scenes. Maintain the photorealistic cinematic quality across all panels. Output a prompt describing the updated lifestyle storyboard.
```

---

## Common Anti-Patterns

### Character Drift Between Panels

**Symptom:** Panel 1 shows a gaunt man with deep wrinkles; panel 5 shows a fuller face with different features.

**Cause:** Model treats each panel as an independent image without a shared character anchor.

**Fix:** Provide an extremely specific character description at the start of the prompt, then reference "the same man" for every panel. Add: "The SAME weathered Japanese man appears in every panel — identical gaunt face, deep wrinkles, short dark hair with gray temples, dark blue work jacket, white undershirt." Consider providing a base reference image of the character.

### Mood Break

**Symptom:** 8 panels are melancholic and blue-gray, but panel 6 is bright, saturated, and cheerful.

**Cause:** Model defaults to "variety" without understanding mood consistency.

**Fix:** Define the mood and color grade explicitly at the start: "Melancholic, lonely, contemplative. Overcast blue-gray color grade with desaturated greens and warm amber accents." Add: "ALL panels share the same emotional temperature and color grade." Reference a specific film or photographer aesthetic if helpful.

### Sketch or Illustration Quality

**Symptom:** Panels look like drawings, paintings, or graphic art instead of photographs.

**Cause:** Model defaults to illustration when "storyboard" is mentioned (confusion with action storyboards).

**Fix:** Open with: "A cinematic lifestyle storyboard grid with photorealistic cinematic photographs — NOT sketches or illustrations." Use anchors: "film still," "shot on 35mm," "cinematic color grade," "photorealistic," "natural lighting." Explicitly prohibit: "No sketches, no pencil drawings, no illustration, no anime, no painting."

### Missing or Generic Captions

**Symptom:** Captions are absent, or they read like generic descriptions ("A man fishing") instead of poetic reflections.

**Cause:** Caption style not specified strongly enough.

**Fix:** Define the caption voice explicitly: "Captions are poetic, reflective, and understated — one sentence or phrase that reads like literary fiction or a diary entry." Provide example captions in the target language. Specify typography: "clean serif or minimalist sans-serif, small but readable."

### Commercial Photography Drift

**Symptom:** Panels look like posed product shots, fashion photography, or advertising imagery instead of candid film stills.

**Cause:** Model defaults to "professional photography" which often means commercial/product aesthetics.

**Fix:** Distinguish from commercial work: "Arthouse cinema aesthetic, NOT commercial photography or advertising." Add: "Candid, unposed moments. Natural lighting. Film grain. Imperfect, lived-in environments." Emphasize: "The character is not posing for a camera — they are simply living."

---

## Good vs Bad Examples

### Good — Full Lifestyle Storyboard Prompt

> A cinematic lifestyle storyboard contact sheet arranged in exactly 3 rows by 3 columns yielding 9 panels total in landscape orientation with no header strip no footer strip no outer margins and no borders or gutters between panels the 9 panels tile edge-to-edge and fill the entire canvas. The art style is photorealistic cinematic photography — each panel looks like a graded 35mm film still from an arthouse movie. The same weathered Japanese man appears in every panel: gaunt face with deep wrinkles, short dark hair with gray at the temples, wearing a dark blue work jacket over a white undershirt, dark trousers, and worn leather shoes. He always has a cigarette. The mood is melancholic, lonely, and contemplative with an overcast blue-gray color grade, desaturated greens, and warm amber accents from cigarette glow. Soft diffused natural light throughout. Panel 1 shows him fishing by a gray river at dawn, sitting on a concrete embankment with a white plastic bag, caption "釣り、アサリはない。気にしない。" Panel 2 shows him lying under a car in a dim garage holding a wrench, caption "整備工場、レンチとタバコ。どちらも手放せない。" Panel 3 shows him eating instant noodles alone in a tiny cluttered kitchen with a cigarette burning in an ashtray, caption "ひとり飯、インスタントの湯気と、いつもの味。" Panel 4 shows him hanging laundry on a balcony at dusk with a cigarette in his mouth and a residential skyline behind, caption "洗濯、干すだけ、誰も来させ。" Panel 5 shows him at a pachinko parlor among glowing machines with his face lit by neon, caption "パチンコ、2時間経過、あと2時間、いける。" Panel 6 shows him standing before a brightly lit vending machine at night choosing a drink, caption "夜の自販機、どっちのコーヒーにするかは、悩んだ。" Panel 7 shows him sitting on a weathered park bench feeding pigeons surrounded by birds, caption "公園のハトたち、こっちには、餌がない。" Panel 8 shows him relaxing in an outdoor onsen with steam rising and eyes closed, caption "銭湯の湯元、カーラーは、誰も聞かない。" Panel 9 is an extreme close-up of his weathered hand pulling a red Marlboro pack from his jacket pocket, caption "胸ポケットの中には、いつもの相棒。" Below the grid is a thin footer strip with a small Marlboro logo, Japanese health warning text, and legal disclaimers. Photorealistic film still quality. No sketches. No illustrations. Arthouse cinema aesthetic. Consistent character face across all panels.

### Bad — Too Vague

> A storyboard of an old Japanese man doing daily activities. 9 panels. Quiet mood. Some cigarettes.

### Bad — Wrong Art Style (Sketch Instead of Photorealistic)

> A hand-drawn storyboard sketch grid showing an old man in 9 panels: fishing, working, eating, laundry, pachinko, vending machine, park, onsen, and cigarette close-up. Rough pencil drawings with minimal shading.

### Bad — Commercial Photography Instead of Film Still

> A premium advertising photography grid showing a well-groomed Japanese man in 9 polished lifestyle scenes with perfect lighting, clean backgrounds, and professional styling for a luxury brand campaign.

---

## Model-Specific Notes

| Model | Lifestyle Storyboard Generation Tip |
|-------|-------------------------------------|
| **GPT Image** | Excellent at maintaining character consistency across panels when given a detailed face description upfront. Good at cinematic color grades. |
| **Seedream** | Good at photorealistic lifestyle photography. Emphasize "film still" and "35mm" framing to avoid illustration drift. |
| **Gemini** | Handles long prompts well. Can manage 800+ word descriptions with full panel breakdowns and caption translations. |
| **Grok / Qwen** | Best for editing existing boards. Always preserve grid + character face first, then modify locations and activities. |

---

## Workflow Integration Notes

This pattern is designed for a **3-step generative workflow**:

1. **Base Image Lock**: Generate a single anchor image establishing the character's face, costume, mood, and visual style. This becomes the reference for all subsequent panels.
2. **Storyboard Expansion**: Using the base image as reference, generate the multi-panel grid with the same character in different daily life scenes. The base image ensures facial consistency.
3. **Video Generation**: Animate the storyboard panels into a cinematic short film. The storyboard serves as the shot list and visual reference for the video model.

**Critical workflow tip**: Always generate the base image first and use it as a reference image for the storyboard generation step. Without a base reference, character drift between panels is almost guaranteed.
