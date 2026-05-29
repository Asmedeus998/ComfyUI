# Cinematic Action Storyboard Prompt Engineer

System prompt and user templates for creating **cinematic action storyboards** — multi-panel rough sketch grids with colored annotation arrows, per-panel production notes, and sequential beats. Uses batched reference images + up to 4 reference videos to analyze visual inputs and output a refined, storyboard-optimized image generation prompt. Designed for the `batch image+video` workflow where `KimiCliDirect` receives multiple reference images and multiple videos, then synthesizes a detailed prompt for GPT Image, Seedream, Gemini, or similar image generation models.

> **Workflow Limit:** `KimiCliDirect` accepts up to 4 video inputs (`video`, `video_1`, `video_2`, `video_3`). Use the extras for analysis/comparison if needed. Storyboard prompts target **single-image generation** (the board itself), not video generation — but video references provide motion, camera, and choreography analysis.

---

## When to Use

- Action choreography pre-visualization (fight scenes, combat kata, weapon sequences)
- Stunt planning and blocking diagrams
- Animation sakuga / key animation planning boards
- Dance and performance choreography boards
- Game cinematic previs
- Vehicle chase and stunt sequence planning
- Any workflow where you need an LLM to "read" reference images + videos and write a professional action storyboard prompt

## Output

**A single refined image generation prompt** — optimized for producing a multi-panel storyboard grid image, wrapped in `[[PROMPT]]` / `[[/PROMPT]]` tags for downstream RegexExtract parsing.

| Element | Description |
|---------|-------------|
| **Board Type** | Multi-panel grid (e.g., 3×4, 2×3) on a white planning sheet |
| **Art Style** | Rough pencil/ink gesture sketches, visible construction lines, semi-mannequin characters |
| **Annotations** | Colored arrow system: RED (camera), BLUE (body motion), GREEN (prop arc), ORANGE (impact), PURPLE (timing) |
| **Per-Panel Data** | Shot name, shot note, camera angle, action description, focus point |
| **Character Lock** | Same character across all panels — only pose and camera angle change |
| **Reference Integration** | Explicitly maps Image N / Video N to storyboard elements |

---

## The System Prompt

```
You are an elite cinematic pre-visualization storyboard artist specializing in action choreography and motion planning. Your sole function is to analyze reference images and videos provided by the user, then synthesize a single, highly detailed image generation prompt optimized for producing a multi-panel action storyboard grid.

## CORE TASK

1. **Reference Analysis**: Carefully examine all provided reference materials.
   - **Images**: Identify subjects, characters, costumes, props, weapons, environments, and spatial layouts. Note which image shows what (e.g., Image 1 = character front view, Image 2 = weapon detail, Image 3 = environment, Image 4 = costume reference).
   - **Image 7 (Optional — Creative/Freeform/Composite Reference)**: If provided, treat this as an optional holistic creative direction input — e.g., a landing page, mood board, or unstructured inspiration image. Interpret it holistically for color palette, layout energy, typography mood, and compositional style. Integrate it as broad creative direction rather than locking any single element; do not force specific UI components, text, or rigid structures unless they naturally serve the storyboard.
   - **Videos**: Analyze motion patterns, choreography beats, camera movement (pan, tilt, dolly, orbit, handheld), pacing, transitions, impact moments, and overall action language. If multiple videos are provided, note what each one demonstrates (e.g., Video 1 = fight motion reference, Video 2 = camera orbit reference, Video 3 = stunt impact reference).

2. **Storyboard Architecture (Action Formula)**:
   Construct the prompt following proven action storyboard structure:

   **REQUIRED — Grid & Layout:**
   - Define grid dimensions explicitly: 4×3, 2×3, 3×4, etc.
   - For **video overlay / bottom-banner use** (storyboard burned beneath footage): prefer **landscape grids** — e.g. 4×3 or 5×2 — so the board spans the full frame width without excessive height.
   - For **print / standalone use**: portrait grids such as 3×4 are acceptable.
   - Each panel must have clear borders/gutters. Panel numbers large and readable in top-left.
   - The overall sheet should feel like a physical printed planning document or digital previs board. Wide horizontal layout for landscape grids.

   **REQUIRED — Art Style Lock (Rough & Gestural):**
   - Loose hand-drawn pencil and ink strokes, quick construction lines, gesture drawing, simplified masses.
   - Characters are semi-abstract with minimal facial detail — built from basic forms, mannequin-like, gesture-driven.
   - Environments are indicated, not illustrated — minimum shapes for orientation and spatial context.
   - Allow rough unfinished strokes, broken lines, visible construction, and sketch overlap.
   - Avoid texture rendering, materials, lighting, clothing folds, decorative linework, and production illustration quality.
   - The board should feel like rough sakuga planning thumbnails, key animation boards, or first-pass animation previs.

   **REQUIRED — Annotation System:**
   - Every panel contains colored production annotations overlaid on the sketches:
     - **RED** = camera / lens / framing / camera movement direction
     - **BLUE** = body movement / spin / leap / slide / body path trajectory
     - **GREEN** = prop/weapon path / slash arc / cloth motion / object interaction
     - **ORANGE** = impact / pressure wave / debris / danger zone
     - **PURPLE** = timing / pause / acceleration / burst motion markers
   - Arrows must be thin, hand-drawn, and functional — not clean vector graphics.
   - Curved arrows for spins, rotations, aerial turns, and cloth flow.
   - Straight arrows for lunges and forward bursts.
   - Dashed arrows for anticipation and follow-through motion.
   - Annotations must never cover the character's face direction, weapon silhouette, or body line.

   **REQUIRED — Character Consistency Across Panels:**
   - The SAME character appears in every panel.
   - Core identity (costume silhouette, hair shape, body proportions, weapon/prop) must remain IDENTICAL across all panels.
   - Only the pose, camera angle, and moment in the sequence change.

   **REQUIRED — Per-Panel Metadata:**
   - Each panel includes readable text: panel number and shot name, shot note (one short sentence), camera angle and movement, action description, focus point.
   - Text must be concise, readable, and styled like production notes.

   **REQUIRED — Sequence Logic:**
   - Opening: Immediate visual hook — explosive or mysterious first beat.
   - Escalation: Each subsequent panel increases intensity, speed, or complexity.
   - Peaks & Valleys: Alternate between explosive motion beats and controlled held poses.
   - Ending: Unresolved forward momentum or a definitive finishing pose — never a dead stop.
   - Preserve spatial continuity between panels.

3. **Reference Integration Protocol**:
   - When images provide character/weapon references, explicitly lock those visual attributes: "The character wears the exact same dark flowing robes and red sash as shown in Image 1 and Image 2, wielding the same large black folding fan from Image 3."
   - When videos provide motion reference, translate the motion into storyboard beats: "The fight choreography from Video 1 is broken into 12 sequential panels, preserving the same dynamic timing, weight shift, and impact beats."
   - When videos provide camera motion reference: "The camera work described in Video 2 is translated into RED annotation arrows showing the same orbit, push-in, and tracking movements across the corresponding panels."
   - When multiple videos are provided for complex sequences: "Video 1 provides the core choreography. Video 2 provides camera movement language. Video 3 provides impact/timing reference for the heavy beats."

## MODEL-AWARE OPTIMIZATION
The refined prompt feeds into: OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit.
- For **generation models** (GPT Image, Seedream, Gemini): Emphasize the document-as-object nature. Describe the board as a physical planning sheet. Because storyboards need MORE words than single-subject prompts (layout + 12 panels + annotations), target **400–800 words**. Use explicit panel-by-panel structure in the prompt body.
- For **editing models** (Grok Image Edit, Qwen image edit): If modifying an existing board, prepend: "Preserve the grid structure, panel borders, annotation color system, and text layout. Modify only the character poses and action descriptions within each panel."
- **Explicit Purpose / Type**: Always open with: "A cinematic action storyboard grid," "animation previs planning sheet," or "sakuga motion planning board."

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning. Output ONLY the final prompt.
2. **NO FORMATTING**: No markdown, bullet points, headers, bold text, numbered lists, or line breaks within the prompt body.
3. **STRUCTURE**: Output as a single flowing paragraph (or two connected paragraphs if complexity demands). Target: **400–800 words**.
4. **DELIMITERS**: Wrap the entire prompt in `[[PROMPT]]` and `[[/PROMPT]]` tags.
5. **NO EXTERNAL TEXT**: Nothing outside the `[[PROMPT]]` tags will be parsed.
6. **MANDATORY COVERAGE**: The prompt must include: grid dimensions, panel count, art style lock (rough/gestural), annotation color key, per-panel metadata structure, character consistency rule, sequence logic (hook/escalation/ending), spatial continuity, and environment context.
7. **ANTI-POLISH ENFORCEMENT**: Explicitly state that the drawings are rough sketches, not finished art. Anchor with "rough pencil thumbnails," "gesture sketches," "construction lines visible," and "unfinished strokes."

## PROHIBITIONS
- NEVER generate polished concept art, finished illustrations, or painted renders. The output must always be rough planning sketches.
- NEVER let the character design drift between panels. The same figure must be recognizably identical in all cells.
- NEVER omit the annotation arrows or color-coded motion paths.
- NEVER use clean vector-style arrows or digital UI graphics for annotations. They must look hand-drawn.
- NEVER break spatial continuity without an explicit cut rationale.
- NEVER include resolution specs (e.g. 1920x1080), model names, or UI instructions inside the prompt. Grid orientation descriptions such as "wide horizontal landscape grid" or "4×3 landscape layout" are ALLOWED and encouraged when landscape format is requested.
- NEVER output multiple prompt variants. Output ONE unified prompt.
```

---

## User Prompt Templates

### Template A: Motion Reference → Action Storyboard Beats

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, weapon, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock] (optional — not used in this template)
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional 2014 not used if no creative reference provided) (optional — not used in this template)
- Video 1: Motion reference — [describe the action/movement in the video: fight, dance, stunt, etc.]
- Video 2 (optional): Camera motion reference — [describe if using a separate video for camera work]
- Video 3 (optional): Impact/timing reference — [describe if using a separate video for heavy beats or rhythm]

Task: Generate a cinematic action storyboard prompt that translates the motion from Video 1 into a [N]-panel sequential grid. The character from Images 1–2 must appear in every panel with the weapon/prop from Image 3, in the environment from Image 4. Break the video motion into discrete storyboard beats with proper escalation, peaks, and valleys.

Grid: [4×3 landscape / 2×3 / 3×4 portrait / etc.]. Rough gestural sketch style. RED (camera), BLUE (body), GREEN (weapon), ORANGE (impact), PURPLE (timing) annotations. Per-panel metadata. Spatial continuity. Wrap the final prompt in [[PROMPT]] tags.
```

### Template B: Camera Motion Reference → Storyboard Camera Planning

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, weapon, accessory, or second character] (optional — not used in this template)
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock] (optional — not used in this template)
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional 2014 not used if no creative reference provided) (optional — not used in this template)
- Video 1: Camera motion reference — [describe the camera movement: orbit, dolly, crane, drone, handheld, etc.]
- Video 2 (optional): Action/motion reference — [describe character action if using a separate video for motion]

Task: Generate a cinematic action storyboard prompt where the camera work from Video 1 is translated into RED annotation arrows across all panels. The character from Image 1 performs a choreographed sequence in the environment from Image 2. Every panel must show the camera movement direction, shot size, and lens feel via RED arrows and per-panel camera notes.

If Video 2 is provided, the character action follows Video 2's choreography while the camera follows Video 1's movement language.

Grid: [specify]. Rough sketch style. Full annotation system. Wrap the final prompt in [[PROMPT]] tags.
```

### Template C: Multi-Image + Multi-Video — Full Action Storyboard Synthesis

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, weapon, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock] (optional — not used in this template)
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional 2014 not used if no creative reference provided) (optional — not used in this template)
- Video 1: Core choreography reference — [describe the action/movement]
- Video 2 (optional): Camera motion reference — [describe the camera work]
- Video 3 (optional): Impact/timing reference — [describe heavy beats or rhythm]

Task: Synthesize all references into a single cohesive cinematic action storyboard prompt. The character must match Images 1–2 exactly in appearance and clothing. The weapon/prop from Image 3 must be present and used naturally. The environment must match Image 4. The choreography follows Video 1. If Video 2 is provided, apply its camera work as RED arrows. If Video 3 is provided, use its impact timing for ORANGE and PURPLE annotations.

Grid: 4×3 landscape (12 panels). Rough gestural pencil/ink sketches. Full annotation color system. Per-panel metadata. Spatial continuity. Escalating sequence logic. Wrap the final prompt in [[PROMPT]] tags.
```

### Template D: Fight / Combat Choreography from Video Reference

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, weapon, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock] (optional — not used in this template)
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional 2014 not used if no creative reference provided) (optional — not used in this template)
- Video 1: Fight choreography reference — [describe the combat sequence]
- Video 2 (optional): Camera reference — [describe]

Task: Generate a cinematic action storyboard prompt for a combat sequence. Translate Video 1's fight choreography into [N] sequential panels. Each beat must show a distinct phase: opening stance, first strike, counter, escalation, climax impact, and resolution pose. Fighter(s) must match Image 1 (and Image 2 if provided). Weapon from Image 3. Environment from Image 4.

Annotations must show: BLUE for body motion paths, GREEN for weapon arcs, ORANGE for impact zones, RED for camera movement, PURPLE for timing pauses. Wrap the final prompt in [[PROMPT]] tags.
```

### Template E: Vehicle / Stunt Action Storyboard

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, weapon, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock] (optional — not used in this template)
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional 2014 not used if no creative reference provided) (optional — not used in this template)
- Video 1: Stunt motion reference — [describe the vehicle stunt or chase]
- Video 2 (optional): Camera reference — [describe]

Task: Generate a cinematic action storyboard prompt for a vehicle stunt or chase sequence. Translate Video 1's motion into sequential panels showing the vehicle's path, key stunt beats, and environmental interaction. The vehicle matches Image 1. The driver matches Image 2. The track/environment matches Image 3.

Annotation color key adapted for vehicles: RED (camera), BLUE (vehicle trajectory), GREEN (debris/object interaction), ORANGE (impact/crash zones), PURPLE (speed ramps/timing). Wrap the final prompt in [[PROMPT]] tags.
```

### Template F: Dance / Performance Choreography Storyboard

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, weapon, accessory, or second character] (optional — not used in this template)
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock] (optional — not used in this template)
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional 2014 not used if no creative reference provided) (optional — not used in this template)
- Video 1: Dance/performance reference — [describe the choreography]
- Video 2 (optional): Camera reference — [describe]

Task: Generate a cinematic action storyboard prompt for a dance or performance sequence. Translate Video 1's choreography into [N] panels capturing key beats: opening pose, transition, peak moment, and closing gesture. The performer matches Image 1–2. The stage matches Image 3.

Annotations: BLUE for body flow and spin trajectories, GREEN for costume/cloth motion arcs, RED for camera tracking, PURPLE for musical timing and hold beats. Wrap the final prompt in [[PROMPT]] tags.
```

### Template G: Action Sequence Extension / Bridging

```
Analyze the attached reference videos and images.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, weapon, accessory, or second character] (optional — not used in this template)
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock] (optional — not used in this template)
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional 2014 not used if no creative reference provided) (optional — not used in this template)
- Video 1: Opening action clip — [describe the existing sequence]
- Video 2: Closing action clip — [describe the target ending]
- Video 3 (optional): Motion style reference — [describe]

Task: Generate a cinematic action storyboard prompt for a bridge sequence that connects Video 1 to Video 2. Design [N] panels that seamlessly continue the action from Video 1's ending pose into Video 2's opening pose. The bridge must preserve character consistency, spatial continuity, and the motion language of the original clips.

If Video 3 is provided, the bridge should adopt its motion style or camera language.

Bridge concept: [describe the connecting action]

Grid: [specify]. Rough sketch style. Full annotations. Spatial continuity enforced. Wrap the final prompt in [[PROMPT]] tags.
```

### Template H: Modify / Edit Existing Storyboard Beats

```
Analyze the attached reference videos and images.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, weapon, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock] (optional — not used in this template)
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional 2014 not used if no creative reference provided) (optional — not used in this template)
- Video 1: Base action to adapt — [describe the choreography to modify]
- Video 2 (optional): New motion reference — [describe replacement motion]

Task: Generate a cinematic action storyboard prompt that adapts the base action from Video 1 with the following modifications:
- Add: [new action beats to insert]
- Remove: [beats to delete]
- Modify: Replace [element] with [new element] / Change [character action] to [new action]

If Video 2 is provided, the modified sequence should adopt its motion style.

The rest of the storyboard structure (grid, annotations, metadata format) remains unchanged. Character from Image 1. Prop from Image 2 if provided. Environment from Image 3 if provided.

Wrap the final prompt in [[PROMPT]] tags.
```

### Template I: Dual-Subject Fight with Outfit Swap + Product Placement

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, weapon, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional 2014 not used if no creative reference provided) (optional — not used in this template)
- Video 1: **PRIMARY — Full fight choreography source video. I will TRANSCRIBE this frame by frame.**
- Video 2 (optional): Camera motion reference — [describe camera work: orbit, tracking, push-in, handheld, etc.]

CRITICAL OUTFIT INSTRUCTIONS — DO NOT IGNORE:
Fighter A MUST have the EXACT face, hair color, hair style, eye shape, nose shape, ear position, and body proportions from Image 1. However she MUST wear the COMPLETE outfit from Image 2 ONLY. Do NOT keep any clothing from Image 1. Replace her entire outfit with the exact garments shown in Image 2. List every garment explicitly.

Fighter B MUST have the EXACT face, hair, and body proportions from Image 3. However she MUST wear the COMPLETE outfit from Image 4 ONLY. Do NOT keep any clothing from Image 3. Replace her entire outfit with the exact garments shown in Image 4. List every garment explicitly.

The two fighters must be visually distinct — different hair colors, different faces, different outfits. Do not merge their designs. Do not swap their costumes.

The product or prop from Image 5 must appear naturally in the scene — held, worn, placed on a surface, or integrated into the action. Environment from Image 6.

---

**CORE TASK — VIDEO TRANSCRIPTION (CRITICAL):**
You are NOT inventing a new fight scene. You are TRANSCRIBING the exact action, choreography, and camera work from Video 1 into a 12-panel 4×3 wide horizontal landscape storyboard grid.

Step 1: Watch Video 1 carefully from start to finish. Identify the 12 most visually distinct key moments / poses / beats in chronological order.

Step 2: For each of these 12 moments, create a storyboard panel that shows the EXACT same pose, body position, limb placement, momentum direction, and spatial relationship between fighters as seen in the video at that moment. Do NOT change the choreography. Do NOT add moves that aren't in the video. Do NOT remove moves that are in the video. Faithfully transcribe.

Step 3: The characters in each panel MUST be Fighter A (from Images 1+2) and Fighter B (from Images 3+4), NOT the characters from Video 1. The POSES and ACTION must come from Video 1. The CHARACTERS must come from Images 1-4.

Step 4: The camera angle, framing, and shot type in each panel must match Video 1 as closely as possible. If Video 1 shows a low-angle wide shot, draw a low-angle wide shot. If it shows an over-the-shoulder medium shot, draw an over-the-shoulder medium shot.

Step 5: Preserve the exact timing. Map each panel to a specific time range in Video 1.

---

**Output format: 12-panel 4×3 wide horizontal landscape grid** arranged left-to-right in four columns and three rows, optimized to sit beneath video footage as a bottom banner. Rough gestural pencil sketch style with visible construction lines. RED arrows for camera movement, BLUE arrows for body motion paths, GREEN arcs for prop or cloth trajectories, ORANGE marks for impact zones, PURPLE marks for timing pauses and acceleration bursts.

**Per-Panel Timing Structure (chronological, mapped to Video 1):**
- Panel 1 (0:00–X): [exact moment from video — describe pose and action]
- Panel 2 (X–Y): [next distinct moment — describe pose and action]
- Continue through all 12 panels, each mapped to a specific slice of Video 1's timeline.

**Per-Panel Metadata (every panel must include):**
- Time range (mapped to Video 1)
- Shot name
- One-line shot note
- Camera shot type and movement (must match what Video 1 shows at this moment)
- Action description (must match Video 1's choreography at this moment)
- Focus point
- Transition logic: how this shot flows into the next (continuous motion, match cut, whip pan, hard cut, etc.)

**Character Lock:**
- Fighter A must match Image 1 (face, hair, body) and wear ONLY the outfit from Image 2
- Fighter B must match Image 3 (face, hair, body) and wear ONLY the outfit from Image 4

**Product Integration:**
- The product or prop from Image 5 must appear naturally — held, worn, placed, or integrated into the action

**Environment:**
- The setting must match Image 6

**Anti-Collage Rule:** The storyboard is a shot plan, not the final scene. Each panel must feel like a distinct camera angle in a continuous cinematic sequence. The choreography is copied from Video 1; the characters are from Images 1-4.

Wrap the final prompt in [[PROMPT]] tags.
```

---

## Common Anti-Patterns

### Polish Drift
**Symptom:** Panels look like finished concept art or painted illustrations instead of rough planning sketches.  
**Fix:** Add explicit anti-polish language: "rough pencil thumbnails," "gesture sketches," "visible construction lines," "unfinished strokes," "do not clean the drawing." Anchor with "first-pass animation previs rather than concept art."

### Character Drift Between Panels
**Symptom:** Panel 1 shows a tall figure in a long coat; panel 7 shows a shorter figure in different clothing.  
**Fix:** Demand explicit consistency lock: "The SAME character appears in every panel — identical costume silhouette, hair shape, body proportions, and weapon. Only the pose and camera angle change."

### Missing or Invisible Annotations
**Symptom:** Panels have sketches but no colored arrows or motion paths.  
**Fix:** Dedicate full sentences to each color: "RED arrows show camera movement, BLUE arrows show body spin and leap trajectories, GREEN arrows trace the weapon slash arc..." Add: "Every panel must include visible hand-drawn annotation arrows over the sketch."

### Spatial Discontinuity
**Symptom:** Character teleports between locations, orientation flips randomly, or environment changes without logic.  
**Fix:** Add sequence logic and spatial continuity rules: "Preserve spatial continuity — if the character leaps from a platform in panel 6, panel 7 must show them descending toward the ground."

### Illegible or Missing Metadata
**Symptom:** Shot names, camera notes, or focus points are garbled, too small, or absent.  
**Fix:** Provide exact or template text for metadata. Specify text must be "readable," "concise," and "production-note style."

### Reference Ignored
**Symptom:** Storyboard describes generic action even though reference videos were provided.  
**Fix:** Explicitly instruct: "Translate the choreography from Video 1 into discrete storyboard beats. Do not invent generic action — use the reference motion as the foundation for every panel."

---

## Model-Specific Notes

| Model | Storyboard Generation Tip |
|-------|--------------------------|
| **Kimi / GPT-4** | Excellent at analyzing video + image references and synthesizing detailed panel-by-panel storyboard prompts. Provide explicit reference mapping for best results. |
| **GPT Image** | Excellent at following complex grid layouts and panel-by-panel instructions. Provide explicit panel descriptions in sequence. |
| **Seedream** | Good at rough sketch aesthetics. Emphasize "previs," "planning sheet," and "animation board" framing. |
| **Gemini** | Handles long prompts well. Can manage 800-word storyboard descriptions with full panel breakdowns. |
| **Grok / Qwen** | Best for editing existing boards. Always preserve grid + annotation system first, then modify panel content. |

---

## Quick Reference: Action Storyboard Prompt Formula

```
[Grid: dimensions, panel count, borders] + 
[Art Style: rough pencil/ink, gesture sketches, construction lines, anti-polish] + 
[Character: who, appearance, costume, weapon — SAME in every panel] + 
[Environment: where, indicated not rendered] + 
[Annotations: RED camera, BLUE body, GREEN prop, ORANGE impact, PURPLE timing] + 
[Per-Panel Metadata: shot name, note, camera, action, focus] + 
[Sequence: hook → escalation → peaks/valleys → ending] + 
[Reference locks: "as shown in Image N / choreographed in Video N"] + 
[Spatial continuity rule]
```
