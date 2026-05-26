# Cinematic Action Storyboard

Full system prompt, user templates, and anti-patterns for the **Cinematic Action Storyboard** (also called Animation Previs Board, Sakuga Planning Sheet, or Action Timing Board).

## Overview

A multi-panel grid image used to plan action sequences for film, animation, or game cinematics. Each panel is a rough gestural sketch representing one beat in a choreographed sequence. Heavy production annotations (colored arrows, camera notes, action notes) overlay the sketches.

| Output Type | Multi-panel grid (e.g., 3×4, 2×3) of rough thumbnail sketches with annotations |
|-------------|--------------------------------------------------------------------------------|
| Art Style | Loose, gestural, sketchy, unfinished — like animation planning thumbnails |
| Annotations | Colored arrow system for camera, body motion, prop arcs, impact, timing |
| Per-Panel Data | Shot name, shot note, camera angle, action description, focus point |
| Character Rule | SAME character across all panels — only pose and camera angle change |

## Visual Assets (Reference Video + Frame)

| File | Description |
|------|-------------|
| `assets/storyboard-whisperbloom-fan-kata.mp4` | Full reference video (~5 seconds, 21:9 aspect ratio) showing a female war fan master performing a combat kata in an ancient stone courtyard. The **bottom half of the video** contains the actual storyboard output — a 12-panel grid (3 columns × 4 rows) titled "WHISPERBLOOM FAN KATA" on white paper. Each panel shows rough pencil gesture sketches of the same character in sequential action beats, overlaid with colored annotation arrows and per-panel production notes. |
| `assets/storyboard-whisperbloom-fan-kata.jpg` | Static frame extracted from the video showing both the cinematic action (top) and the complete 12-panel storyboard grid (bottom). Use this for quick visual reference without playing the video. |

### What the Storyboard Looks Like (Visual Specification)

The storyboard occupies the **bottom half** of a wide cinematic frame. It is a **white planning sheet** with:

- **Grid**: 3 columns × 4 rows = 12 panels, each with thin black borders
- **Panel numbers**: Large readable numbers (01–12) in the top-left of each cell
- **Title bar**: "WHISPERBLOOM FAN KATA" in bold sans-serif, "ASPECT RATIO: 21:9" on the right
- **Art style**: Rough grayscale pencil/ink gesture sketches with visible construction lines. Characters are semi-mannequin with minimal faces. Environments are suggested by minimum architectural shapes (pillars, stairs, banners)
- **Character consistency**: The same female warrior appears in all 12 panels — dark robes, high bun with pins, large folding war fan
- **Annotation arrows** (hand-drawn, thin, overlaid on sketches):
  - **RED** arrows = camera movement (push-ins, tracking, orbit)
  - **BLUE** arrows = body motion paths (spins, leaps, slides)
  - **GREEN** arcs = fan/weapon trajectory paths
  - **ORANGE** marks = impact zones and debris
  - **PURPLE** marks = timing pauses and acceleration bursts
- **Per-panel metadata** (small readable text in each cell):
  - Shot name: e.g., "01 FAN SNAP HOOK", "06 AERIAL TURN"
  - Shot note: one-line purpose, e.g., "Immediate silhouette reveal", "Sakuga showcase beat"
  - Camera: angle + movement, e.g., "low front close shot", "high angle follow"
  - Action: what happens, e.g., "closed fan instantly opens across frame"
  - Focus: eye-tracking target, e.g., "fan shape and eye line", "body line and fan trail"
- **Sequence flow**: The panels read left-to-right, top-to-bottom, escalating from a still pose (panel 02) through explosive motion (panels 03–09) to a heroic silhouette (panel 10) and an active ending (panel 12)

This serves as the **gold standard** for what a Cinematic Action Storyboard should look like: rough, readable, motion-focused, and production-ready.

---

## The Master System Prompt

Copy-paste this directly into the system prompt field of your storyboard-generation agent.

```
You are an elite cinematic pre-visualization storyboard artist specializing in action choreography and motion planning. Your sole function is to generate multi-panel storyboard grids for action sequences, fight scenes, dance choreography, or kinetic showcases.

## CORE TASK

1. **Grid Structure Engineering**: The output is a SINGLE IMAGE containing a multi-panel storyboard grid.
   - Define the grid dimensions explicitly: 3×4, 2×3, 4×3, etc.
   - Each panel must have a clear border or gutter separating it from neighbors.
   - Panel numbers must be large and readable in the top-left corner of each cell.
   - The overall sheet should feel like a physical printed planning document or digital previs board.

2. **Art Style Lock — Rough & Gestural**: The drawings must NOT be polished illustrations.
   - Use loose hand-drawn pencil and ink strokes, quick construction lines, gesture drawing, and simplified masses.
   - Characters are semi-abstract with minimal facial detail — built from basic forms, mannequin-like, gesture-driven.
   - Environments are indicated, not illustrated — minimum shapes for orientation and spatial context.
   - Allow rough unfinished strokes, broken lines, visible construction, and sketch overlap.
   - Avoid texture rendering, materials, lighting, clothing folds, decorative linework, and production illustration quality.
   - The board should feel like rough sakuga planning thumbnails, key animation boards, or first-pass animation previs.

3. **Character Consistency Across Panels**: The SAME character appears in every panel.
   - Core identity (costume silhouette, hair shape, body proportions, weapon/prop) must remain IDENTICAL across all panels.
   - Only the pose, camera angle, and moment in the sequence change.
   - Do not let the character's design drift between panels.

4. **Annotation System**: Every panel contains colored production annotations overlaid on the sketches:
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

5. **Per-Panel Metadata**: Each panel includes readable text:
   - Panel number and shot name (e.g., "01 — FAN SNAP HOOK")
   - Shot note: one short sentence explaining purpose or transition value
   - Camera: angle and movement (e.g., "low front close shot")
   - Action: what happens in the beat (e.g., "closed fan instantly opens across frame")
   - Focus: what the viewer's eye should track (e.g., "fan shape and eye line")
   - Text must be concise, readable, and styled like production notes.

6. **Sequence Logic**: The panels must tell a coherent kinetic story:
   - **Opening**: Immediate visual hook — explosive or mysterious first beat.
   - **Escalation**: Each subsequent panel increases intensity, speed, or complexity.
   - **Peaks & Valleys**: Alternate between explosive motion beats and controlled held poses.
   - **Ending**: Unresolved forward momentum or a definitive finishing pose — never a dead stop.
   - Preserve spatial continuity: if the character moves left in panel 3, panel 4 must respect that position.

7. **Spatial Continuity Enforcement**: The environment and character position must flow logically from panel to panel.
   - If panel 4 shows the character on a stone platform, panel 5 must show them leaping FROM that platform.
   - Avoid jarring location changes unless intentionally a cut.
   - Maintain left/right orientation consistency for readable choreography.

## MODEL-AWARE OPTIMIZATION
The refined prompt feeds into: OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit.
- For **generation models** (GPT Image, Seedream, Gemini): Emphasize the document-as-object nature. Describe the board as a physical planning sheet. Because storyboards need MORE words than single-subject prompts (layout + 12 panels + annotations), target **400–800 words**. Use explicit panel-by-panel structure in the prompt body.
- For **editing models** (Grok Image Edit, Qwen image edit): If modifying an existing board, prepend: "Preserve the grid structure, panel borders, and annotation color system. Modify only the character poses and action descriptions within each panel."
- **Explicit Purpose / Type**: Always open with: "A cinematic action storyboard grid," "animation previs planning sheet," or "sakuga motion planning board."

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning. Output ONLY the final prompt.
2. **NO FORMATTING**: No markdown, bullet points, headers, bold text, numbered lists, or line breaks within the prompt body.
3. **STRUCTURE**: Output as a single flowing paragraph (or two connected paragraphs if complexity demands). Target: **400–800 words**.
4. **DELIMITERS**: Wrap the entire prompt in `[[PROMPT]]` and `[[/PROMPT]]` tags.
5. **NO EXTERNAL TEXT**: Nothing outside the `[[PROMPT]]` tags will be parsed.
6. **MANDATORY COVERAGE**: The prompt must include: grid dimensions, panel count, art style lock (rough/gestural), annotation color key, per-panel metadata structure, character consistency rule, sequence logic (hook/escalation/ending), spatial continuity, and environment context.
7. **ANTI-POLISH ENFORCEMENT**: Explicitly state that the drawings are rough sketches, not finished art. If the model drifts toward illustration quality, anchor with "rough pencil thumbnails," "gesture sketches," "construction lines visible," and "unfinished strokes."

## PROHIBITIONS
- NEVER generate polished concept art, finished illustrations, or painted renders. The output must always be rough planning sketches.
- NEVER let the character design drift between panels. The same figure must be recognizably identical in all cells.
- NEVER omit the annotation arrows or color-coded motion paths.
- NEVER use clean vector-style arrows or digital UI graphics for annotations. They must look hand-drawn.
- NEVER break spatial continuity without an explicit cut rationale.
- Do not include aspect ratios, resolution specs, model names, or UI instructions inside the prompt.
- Do not output multiple prompt variants; output one unified optimized prompt.
```

---

## User Prompt Templates

### Template A: Full Action Sequence with All Panels Defined

```
Generate a cinematic action storyboard grid for a 12-beat combat kata sequence.

Grid: 3 columns × 4 rows. 12 numbered panels with clear borders.

Art style: Rough hand-drawn pencil and ink sketches, loose gestural strokes, visible construction lines, semi-mannequin characters with minimal facial detail, environments indicated by minimum shapes only. Unfinished, sketchy, previs quality — NOT polished illustration.

Character: A female war fan master in dark flowing robes with a red sash, hair in a high bun with ornamental pins. She wields a large black folding fan that conceals a blade. Same costume and silhouette in every panel.

Environment: Ancient stone courtyard with terraces, hanging bells, banners, and shallow reflecting pools. Indicated only — not fully rendered.

Annotation color key:
- RED arrows = camera movement and framing
- BLUE arrows = body motion path (spins, leaps, slides)
- GREEN arrows = fan arc and blade path
- ORANGE marks = impact zones and debris
- PURPLE marks = timing pauses and acceleration bursts

Sequence panels:
01 FAN SNAP HOOK — low front close shot, fan opens across frame, focus on fan shape
02 STILLNESS BEFORE MOTION — medium side shot, body lowers, weight transfer
03 FIRST BLOOM CUT — tracking wide, horizontal fan slash with torso rotation
04 SPIN ENTRY — orbit shot, 360 spin with cloak trailing
05 HIDDEN BLADE DRAW — low angle push-in, fan separates revealing blade
06 AERIAL TURN — high angle follow, twisting leap over platform
07 DOUBLE ARC STRIKE — wide side view, intersecting fan and blade paths
08 WATER STEP — ground tracking, slide across shallow water
09 BELL IMPACT PASS — rear three-quarter, fan wave swings hanging bells
10 MID-AIR SILHOUETTE — extreme low angle, leap with fan overhead
11 DESCENT CUT — front tracking, descending slash to kneeling finish
12 WHISPERBLOOM END — wide hero shot, rises and advances forward

Each panel includes: shot name, one-line shot note, camera angle, action description, focus point. All text readable and concise.

Overall: Grayscale base with limited annotation colors. Production planning sheet aesthetic. Spatial continuity between panels. Readable at a glance.
```

### Template B: Minimal Template with Auto-Sequence

```
Generate a cinematic action storyboard grid for a choreographed weapon sequence.

Grid: 3×4. 12 panels. Rough gestural sketch style — loose pencil strokes, construction lines visible, semi-mannequin characters, minimal facial detail, environments suggested not rendered.

Character: [describe your character briefly]. Same figure in all panels.

Annotations: RED for camera, BLUE for body motion, GREEN for weapon arc, ORANGE for impact, PURPLE for timing. Hand-drawn thin arrows. Never cover the silhouette.

Sequence logic: Open with a visual hook. Escalate from controlled to explosive. End on unresolved forward motion. Preserve spatial continuity between panels.

Each panel needs: number, shot name, short note, camera angle, action, focus. Readable production text.

Reference images attached for character design, weapon, and environment.

Task: Create the full 12-panel storyboard with annotations and metadata. Rough sketch quality only — no polished rendering.
```

### Template C: Editing an Existing Board (for Grok / Qwen)

```
Base storyboard image attached. Preserve the grid structure, panel borders, annotation color system, and text layout.

Reference images for character/action updates attached.

Task: Modify the poses and actions within each panel to match the new sequence. Keep the same rough sketch style, annotation colors, and per-panel metadata format. Maintain character consistency across all panels. Output a prompt describing the updated storyboard.
```

---

## Common Anti-Patterns

### Polish Drift

**Symptom:** Panels look like finished concept art or painted illustrations instead of rough planning sketches.

**Cause:** Prompt lacks explicit anti-polish language. Model defaults to "high quality" rendering.

**Fix:** Add explicit style anchors: "rough pencil thumbnails," "gesture sketches," "visible construction lines," "unfinished strokes," "do not clean the drawing," "avoid texture rendering and lighting." Add: "The storyboard should feel like first-pass animation previs rather than concept art."

### Character Drift Between Panels

**Symptom:** Panel 1 shows a tall figure in a long coat; panel 7 shows a shorter figure in different clothing.

**Cause:** Model treats each panel as an independent image.

**Fix:** Add strong consistency lock: "The SAME character appears in every panel — identical costume silhouette, hair shape, body proportions, and weapon. Only the pose and camera angle change." Provide a brief but specific character description near the start of the prompt.

### Missing or Invisible Annotations

**Symptom:** Panels have sketches but no colored arrows or motion paths.

**Cause:** Annotation system not emphasized strongly enough.

**Fix:** Dedicate a full sentence to each color: "RED arrows show camera movement, BLUE arrows show body spin and leap trajectories, GREEN arrows trace the fan slash arc..." Add: "Every panel must include visible hand-drawn annotation arrows over the sketch."

### Spatial Discontinuity

**Symptom:** Character teleports between locations, orientation flips randomly, or environment changes without logic.

**Cause:** Each panel described in isolation without flow logic.

**Fix:** Add sequence logic and spatial continuity rules: "Preserve spatial continuity — if the character leaps from a platform in panel 6, panel 7 must show them descending toward the ground." Add: "Maintain left/right orientation for readable choreography."

### Illegible or Missing Metadata

**Symptom:** Shot names, camera notes, or focus points are garbled, too small, or absent.

**Cause:** Text content not specified explicitly enough.

**Fix:** Provide exact or template text for metadata. Specify text must be "readable," "concise," and "production-note style." For critical panels, provide the exact shot name and note text.

---

## Good vs Bad Examples

### Good — Full Action Storyboard Prompt

> A cinematic action storyboard grid for a 12-beat war fan combat kata, arranged in a 3-column by 4-row grid on a clean white planning sheet with thin gray panel borders. The art style is rough hand-drawn pencil and ink gesture sketches with visible construction lines, semi-mannequin characters, minimal facial detail, and environments suggested by only the minimum architectural shapes. The same female warrior appears in every panel wearing dark flowing robes with a red sash and wielding a large black folding fan. Panel 01 low front close shot shows the fan snapping open with a RED arrow indicating camera push-in and GREEN arc tracing the fan bloom. Panel 02 medium side shot shows her lowering into a still stance with BLUE arrows for weight transfer. Panel 03 tracking wide shows a horizontal fan slash with GREEN arc and RED tracking arrow. Panel 04 orbit shot shows a 360 spin with BLUE circular arrow and GREEN fan trail. Panel 05 low angle push-in reveals a concealed blade as the fan separates with PURPLE timing marks. Panel 06 high angle follow shows a twisting leap with BLUE aerial arc. Panel 07 wide side view shows intersecting fan and blade paths with crossed GREEN arcs. Panel 08 ground tracking shows a water slide with BLUE motion line and ORANGE splash marks. Panel 09 rear three-quarter shows a fan wave striking hanging bells with ORANGE impact ripples. Panel 10 extreme low angle shows a mid-air silhouette with the fan overhead against sky. Panel 11 front tracking shows a descending slash to kneeling with BLUE descent arc. Panel 12 wide hero shot shows rising forward advance with RED camera pull-back and GREEN extended fan line. Each panel has a large top-left number, shot name, short shot note, camera angle, action description, and focus point in readable small production text. The base is grayscale with only RED BLUE GREEN ORANGE and PURPLE annotation colors. Rough unfinished sketch quality throughout. No polished rendering. No lighting or texture. Spatial continuity maintained across all panels.

### Bad — Too Vague

> A storyboard of a woman fighting with a fan. 12 panels. Action poses. Some arrows showing movement. Rough sketch style.

### Bad — Too Polished

> A beautifully illustrated comic page showing a female warrior performing an elegant fan dance across 12 highly detailed painted panels with rich colors, dramatic lighting, and finished backgrounds.

---

## Model-Specific Notes

| Model | Storyboard Generation Tip |
|-------|--------------------------|
| **GPT Image** | Excellent at following complex grid layouts and panel-by-panel instructions. Provide explicit panel descriptions in sequence. |
| **Seedream** | Good at rough sketch aesthetics. Emphasize "previs," "planning sheet," and "animation board" framing. |
| **Gemini** | Handles long prompts well. Can manage 800-word storyboard descriptions with full panel breakdowns. |
| **Grok / Qwen** | Best for editing existing boards. Always preserve grid + annotation system first, then modify panel content. |
