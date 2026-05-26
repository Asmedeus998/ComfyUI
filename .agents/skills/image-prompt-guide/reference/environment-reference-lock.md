# Environment Reference Lock (I2V Scene Anchor)

Full system prompt, user templates, and anti-patterns for the **Environment Reference Lock** workflow — also called I2V Scene Anchor, Spatial Consistency Board, or Set Lock Reference.

## Overview

The Environment Reference Lock is a single image that acts as a **spatial anchor** for image-to-video (I2V) generation. It tells the video model exactly what the environment looks like, where every prop is positioned, and how light behaves — so when a character moves through the space, the background remains physically consistent.

| Output Type | Single multi-section reference board with environment views + prop callouts + tech specs |
|-------------|-----------------------------------------------------------------------------------------|
| Purpose | Lock spatial relationships for image-to-video or multi-angle image generation |
| Sections | Main camera views, reverse angles, key prop detail callouts, technical spec bar |
| Text in Image | Medium — scene header, camera labels, prop names, technical specs |
| Consistency Challenge | All views must depict the SAME room with identical prop placement and lighting |

## Visual Assets (Reference Video + Frame)

| File | Description |
|------|-------------|
| `assets/environment-reference-lock.mp4` | Full reference video (~28 seconds) showing the Environment Reference Lock in action. **Top half**: a persistent scene reference board for "INT. APARTMENT LIVING ROOM — NIGHT". **Bottom half**: a video of a woman in a golden armored top and red skirt moving through the apartment — sitting on the sofa, touching the lava lamp, turning off the CRT television, and drinking from a coffee mug. The background remains perfectly consistent because the video model is anchored by the reference board. |
| `assets/environment-reference-lock.jpg` | Static frame from the video showing the complete board + a moment from the video sequence. |

### What the Board Looks Like (Visual Specification)

The reference board occupies the **top half** of the frame. It is a **dark, cinematic planning sheet** with:

- **Header bar**: "SCENE REFERENCE — INT. [LOCATION] — [TIME OF DAY]" in clean sans-serif white text on black background
- **Main views** (two large panels side by side):
  - **Camera A — Front View**: Wide shot facing the primary orientation (e.g., facing window / entrance angle)
  - **Camera B — Reverse View**: Wide shot from the opposite side (e.g., from window / facing into room)
  - Both views show the SAME room with identical furniture placement, lighting, and prop positions
- **Key Props — Detail Callouts** (row of 4–6 small panels below the main views):
  - Each panel is a close-up detail shot of one critical prop
  - Props are numbered and labeled beneath each thumbnail
  - Examples: "1. LAVA LAMP", "2. COFFEE TABLE", "3. NIRVANA POSTER", "4. CRT TELEVISION", "5. WINDOW / RAIN", "6. THROW BLANKET + SOFA CORNER"
- **Technical spec bar** (bottom strip):
  - ASPECT, COLOR TEMP, LENS, FORMAT, and other production metadata
  - Example: "ASPECT: 16:9 MAIN PANELS | COLOR TEMP: 2700K PRACTICAL · EXT: 4100K CITY NIGHT | LENS: 24mm EQUIV · FORMAT: 35mm ANALOG GRAIN"
- **Source ref inset** (small thumbnail on the right):
  - "SOURCE REF" and "REF INPUT" labels showing the original reference image used to build the board

The overall aesthetic is **dark, cinematic, and technical** — like a VFX previs sheet or a virtual production planning document. Not a polished film poster; a functional production tool.

---

## The Master System Prompt

Copy-paste this directly into the system prompt field of your environment-lock agent.

```
You are an elite spatial consistency designer for image-to-video workflows. Your sole function is to generate Environment Reference Lock boards — single images that anchor a 3D space for video generation by showing multiple camera angles, prop positions, and technical specs.

## CORE TASK

1. **Spatial Lock Architecture**: The output is a SINGLE IMAGE that functions as a scene anchor. It must contain:
   - **Header**: Scene location and time of day — "SCENE REFERENCE — INT. [LOCATION] — [TIME OF DAY]"
   - **Primary Camera View**: A wide establishing shot showing the full environment from the main orientation.
   - **Reverse Camera View**: A wide shot from the opposite angle showing the same space from behind or across.
   - **Prop Detail Callouts**: 4–8 close-up panels of critical props, furniture, or environmental features that must maintain consistency across video frames.
   - **Technical Spec Bar**: Production metadata — aspect ratio, color temperature, lens, film format, grain, and lighting setup.
   - **Source Reference Inset**: A small thumbnail showing the original input reference (if applicable) labeled "SOURCE REF" and "REF INPUT."

2. **Cross-View Consistency Lock**: Every view must depict the EXACT SAME space:
   - Identical furniture placement in both wide shots.
   - Identical prop positions — if a lamp is on the left in Camera A, it must be on the right in Camera B (reverse perspective) but in the same physical location.
   - Identical lighting quality, color temperature, and mood across all panels.
   - Identical wall decorations, window views, and floor surfaces.

3. **Prop Detail Extraction**: Identify the props that matter most for spatial consistency:
   - Light sources (lamps, screens, windows) — because their position affects shadows and reflections on the character.
   - Furniture the character will interact with (sofa, table, chair, shelf).
   - Interactive objects (TV, remote, mug, book, switch).
   - Background features (posters, plants, curtains, rain on windows).
   - Each prop gets a clear close-up with a number and label.

4. **Technical Specification Bar**: Include realistic production metadata:
   - ASPECT: The output aspect ratio (e.g., 16:9, 21:9, 9:16).
   - COLOR TEMP: Interior practical lights vs. exterior/environmental light sources.
   - LENS: Equivalent focal length (e.g., 24mm, 35mm, 50mm).
   - FORMAT: Film or digital format with grain characteristics (e.g., 35mm analog grain, digital clean).
   - Any additional notes on depth of field, motion blur, or frame rate if relevant.

## MODEL-AWARE OPTIMIZATION
The refined prompt feeds into: OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit.
- For **generation models** (GPT Image, Seedream, Gemini): Emphasize the functional production-document nature. Describe the board as a "VFX previs sheet," "virtual production planning document," or "I2V scene anchor." Target **300–600 words**.
- For **editing models** (Grok Image Edit, Qwen image edit): If modifying an existing board, prepend: "Preserve the existing room layout, prop positions, and lighting setup. Add the new prop detail callout and update the technical spec bar."
- **Explicit Purpose / Type**: Always open with the document type: "An Environment Reference Lock board for image-to-video spatial consistency," "I2V scene anchor document," or "Cinematic spatial planning sheet."

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning. Output ONLY the final prompt.
2. **NO FORMATTING**: No markdown, bullet points, headers, bold text, numbered lists, or line breaks within the prompt body.
3. **STRUCTURE**: Output as a single flowing paragraph (or two connected paragraphs if complexity demands). Target: **300–600 words**.
4. **DELIMITERS**: Wrap the entire prompt in `[[PROMPT]]` and `[[/PROMPT]]` tags.
5. **NO EXTERNAL TEXT**: Nothing outside the `[[PROMPT]]` tags will be parsed.
6. **MANDATORY COVERAGE**: The prompt must include: scene header, primary camera view description, reverse camera view description, prop detail callout list with numbers and labels, technical spec bar content, and cross-view consistency lock language.
7. **ANTI-DRIFT ENFORCEMENT**: Explicitly state that both wide shots show the same room from opposite angles, that prop positions are physically identical, and that lighting/color temperature must match across all panels.

## PROHIBITIONS
- NEVER generate conflicting room layouts between the primary and reverse views.
- NEVER omit the technical spec bar — it is critical for model alignment on lighting and lens characteristics.
- NEVER place props in different locations in different views.
- NEVER change the time of day or lighting mood between views.
- Do not include aspect ratios, resolution specs, model names, or UI instructions inside the prompt.
- Do not output multiple prompt variants; output one unified optimized prompt.
```

---

## User Prompt Templates

### Template A: Full Environment Lock with All Props Defined

```
Generate an Environment Reference Lock board for an interior apartment living room at night.

Scene: INT. APARTMENT LIVING ROOM — NIGHT

Main views:
- Camera A — Front View: Wide shot facing the large rain-streaked window with city lights visible outside. Beige L-shaped sofa facing the window. Wooden coffee table with remote, black mug, and stacked magazines. Floor lamp with warm glow. Bookshelves on the right wall with a CRT television showing static. Nirvana-style smiley face poster on the left wall. Potted plant in the corner.
- Camera B — Reverse View: Wide shot from the window side facing back into the room. Shows the entrance area, the back of the sofa, the bookshelf wall, and the lamp from the opposite angle.

Key Props — Detail Callouts (6 panels):
1. LAVA LAMP: Classic lava lamp on a small side table, green and blue blobs glowing
2. COFFEE TABLE: Dark wood, remote control, black ceramic mug, ashtray, magazines
3. NIRVANA POSTER: Black poster with yellow smiley face and "MDON" text
4. CRT TELEVISION: Old box TV on bookshelf, static screen, wood-grain casing
5. WINDOW / RAIN: Large window with rain streaks, out-of-focus city bokeh lights at night
6. THROW BLANKET + SOFA CORNER: Rumpled grey knit blanket draped over sofa arm

Technical Spec Bar:
- ASPECT: 16:9 MAIN PANELS
- COLOR TEMP: 2700K practical interior · EXT: 4100K city night
- LENS: 24mm equivalent
- FORMAT: 35mm analog grain

Style: Dark cinematic VFX previs sheet, clean white text on black background, thin panel borders, photorealistic room rendering, functional production-document aesthetic.

Task: Create a single board image where both wide views show the same room from opposite angles with identical prop placement and lighting. The prop callouts must be clear close-ups. The technical bar must be readable and realistic.
```

### Template B: Minimal Environment Lock

```
Generate an Environment Reference Lock board for an interior space.

Reference image attached showing the room from one angle.

Required sections:
- Header: "SCENE REFERENCE — INT. [location] — [time]"
- Camera A: Front view wide shot
- Camera B: Reverse view wide shot from the opposite angle
- 4–6 Key Prop detail callouts with numbers and labels
- Technical spec bar: aspect, color temp, lens, format

Task: Both wide views must show the SAME room with identical furniture and prop placement. Add detail callouts for the most spatially important props. Include production metadata. Dark cinematic previs aesthetic.
```

### Template C: Editing an Existing Lock (for Grok / Qwen)

```
Base environment board image attached. Preserve the existing room layout, camera angles, and lighting.

Reference images for new prop details attached.

Task: Add new prop detail callouts to the existing board. Update the technical spec bar if needed. Maintain cross-view consistency — the new props must appear in correct positions in both wide shots. Output a prompt describing the updated board.
```

---

## Common Anti-Patterns

### Spatial Drift Between Views

**Symptom:** Camera A shows a sofa on the left; Camera B shows the same sofa also on the left (should be on the right in reverse view). Or a lamp moves from one side of the room to the other.

**Cause:** Model doesn't understand that reverse view means mirror-flipped spatial relationships.

**Fix:** Add explicit spatial lock language: "Camera B is the reverse angle — if a lamp appears on the left in Camera A, it must appear on the right in Camera B while remaining in the same physical location." Describe the room layout from both perspectives explicitly.

### Missing Prop Callouts

**Symptom:** The wide shots look good but the detail callouts are missing or show wrong props.

**Cause:** Prop list not specified clearly enough.

**Fix:** Number each prop explicitly (1–6). Provide a brief visual description for each callout panel. Prioritize props that emit light or that the character will interact with.

### Inconsistent Lighting

**Symptom:** Camera A is warm golden hour; Camera B is cool fluorescent. Or one view has rain on the window and the other doesn't.

**Cause:** No lighting lock across views.

**Fix:** Add: "Identical lighting quality, color temperature, and weather conditions across all panels." Specify exact color temps in the technical bar.

### Missing Technical Spec Bar

**Symptom:** Board looks like a concept art sheet with no production metadata.

**Cause:** Technical specs not requested.

**Fix:** Always include the spec bar in the prompt. It grounds the model in realistic cinematography parameters and prevents wild lens/lighting hallucinations when the video is generated.

---

## Good vs Bad Examples

### Good — Full Environment Lock Prompt

> An Environment Reference Lock board for I2V spatial consistency, scene reference INT apartment living room night, header bar in white sans-serif on black background. Camera A front view wide shot facing the rain-streaked window shows a beige L-shaped sofa with a rumpled grey throw blanket, wooden coffee table with remote black mug and magazines, green-blue lava lamp on side table, floor lamp with warm 2700K glow, bookshelf with CRT television showing static, and Nirvana-style smiley poster on the wall. Camera B reverse view from the window facing into the room shows the same space from behind with the sofa back visible, the bookshelf wall on the left, and the entrance area on the right, maintaining identical prop placement and warm interior lighting with 4100K city bokeh visible through rain-streaked glass. Below the wide shots, six detail callout panels numbered one through six show close-ups of the lava lamp glowing blobs, the coffee table surface with objects, the black and yellow poster, the old wood-grain CRT with static, the rain-covered window with city lights, and the sofa corner with the knit blanket. A bottom technical spec bar reads aspect sixteen-nine main panels, color temp twenty-seven-hundred-k practical interior ext forty-one-hundred-k city night, lens twenty-four-millimeter equivalent, format thirty-five-millimeter analog grain. Small source ref inset in the upper right. Dark cinematic VFX previs aesthetic, clean panel borders, photorealistic rendering, functional production document style.

### Bad — Vague Concept Art

> A beautiful painting of a cozy apartment at night with a sofa and some lights and a TV. Warm colors, rainy window, city view.

### Bad — No Reverse View

> A detailed interior scene of a living room with a sofa, coffee table, lamp, and TV. Multiple detail shots of props.

---

## Model-Specific Notes

| Model | Environment Lock Generation Tip |
|-------|--------------------------------|
| **GPT Image** | Excellent at following multi-panel layouts with technical text. Be explicit about spatial relationships (left/right in each view). |
| **Seedream** | Good at cinematic interiors. Emphasize "VFX previs," "virtual production," or "set reference" framing. |
| **Gemini** | Handles long prompts well. Can manage detailed prop lists and technical specs in one flow. |
| **Grok / Qwen** | Best for editing existing boards. Always preserve room geometry first, then add/modify prop callouts. |

---

## Connection to Image-to-Video

This pattern is designed as a **pre-generation anchor** for I2V workflows:

1. **Generate** the Environment Reference Lock board first (this pattern).
2. **Feed** the board to the video model (Seedance, Kling, Sora, etc.) as a spatial reference.
3. **Generate** the character movement video with the board as context.
4. **Result**: The background stays locked — furniture doesn't shift, lighting doesn't change, props remain in the same positions as the character moves through the space.

Without this lock, video models freely hallucinate background changes between frames.
