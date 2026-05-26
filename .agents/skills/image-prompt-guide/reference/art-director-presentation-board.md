# Art Director Presentation Board

Full system prompt, user templates, and anti-patterns for the **Art Director Presentation Board** (also called Film Pre-Production Bible, Concept Design Sheet, or Art Director Guide).

## Overview

Unlike Reference Element Fusion — which produces a single-subject photograph — the Art Director Presentation Board produces a **single image that IS a multi-section document**. It is a pre-production design artifact used to communicate visual direction to a film crew.

| Output Type | Multi-section grid layout with typography, labels, and visual elements |
|-------------|---------------------------------------------------------------------|
| Sections | Character turnarounds, prop sheets, environment concepts, movie poster, color palette, mood & tone, materials, notes |
| Text in Image | Heavy — titles, labels, credits, taglines, body text |
| Consistency Challenge | All sections must share the same art style, color palette, and cinematic mood |

## Visual Assets (Reference Images + Videos)

| File | Description |
|------|-------------|
| `assets/art-director-presentation-board-example.jpg` | A complete professional art director guide board for the film "Words Change Your World" (3840×2160). Cream parchment background with thin decorative gold divider lines. **Left panel**: movie poster with title in large serif typography, tagline "SOMETIMES, THE RIGHT WORDS CAN CHANGE EVERYTHING", director credit, "COMING SOON", and key visual of blind man on wet steps with woman in grey coat. **Top-right**: Character Design section with old man turnaround (front/side/back in olive coat) and woman turnaround (front/side/back in grey coat with red heels). **Top-right adjacent**: Props section showing cardboard sign "IT'S A BEAUTIFUL DAY AND I CAN'T SEE IT" from front/side/back. **Middle-right**: Set Design — CITY STREET with three environment views (wide building/stairs, street perspective with lampposts, close ground-level wet pavement). **Bottom strip**: Color Palette (5 swatches: blue-grey, charcoal, taupe, dusty blue, red accent), Mood & Tone text, Materials & Textures swatches, and Notes section with bullet points. |
| `assets/art-director-board-film-words-change-your-world.mp4` | The finished cinematic short film (~85 seconds) that the presentation board was designed for. The film opens with an old blind man sitting on wet city steps holding a cardboard sign reading "I'M BLIND PLEASE HELP." Passersby ignore him. A woman in a light grey coat and striking red heels approaches, takes the sign, writes on it, and places it back. The sign now reads "IT'S A BEAUTIFUL DAY AND I CAN'T SEE IT." Immediately, people stop to give him money and coffee. The woman returns; the blind man looks up at her and smiles. She touches his shoulder gently and walks away. The film ends with a black screen and the text "CHANGE YOUR WORDS. CHANGE YOUR WORLD." Shot in muted overcast tones with shallow depth of field, naturalistic acting, and emotionally resonant pacing. The characters, costumes, props, and environment all match the presentation board exactly. |
| `assets/art-director-board-film-frame-blind-man.jpg` | Frame extracted from the el.cine film showing the blind man sitting on wet city steps. He wears the same olive coat and dark scarf from the board's character turnaround. His eyes are milky blue. The background shows classical stone architecture and blurred pedestrians. Muted overcast color grade matching the board's palette. |
| `assets/art-director-board-film-frame-sign.jpg` | Frame extracted from the el.cine film showing the close-up of the changed cardboard sign: "IT'S A BEAUTIFUL DAY AND I CAN'T SEE IT" in handwritten marker on worn cardboard. A white coffee cup sits beside it. This is the prop featured in the board's prop design section. |
| `assets/art-director-board-commercial-workflow.mp4` | Reference video (~15 seconds) demonstrating a TV commercial storyboard-to-final-film workflow. The top half of the video shows a structured commercial storyboard table for "MAGIC BLENDER" (product shots, lifestyle frames, before/after comparison, CTA end card). The bottom half shows the actual finished TV commercial footage that corresponds to the storyboard. This serves as a secondary example of how a pre-production document (board/storyboard) translates into final cinematic output. |
| `assets/art-director-board-commercial-frame.jpg` | First frame from the Gumvue commercial workflow video, showing the family lifestyle shot that corresponds to the first row of the commercial storyboard table. |

The **static board image** serves as the **gold standard** for what an Art Director Presentation Board should look like: elegant, structured, information-dense, and visually cohesive. The **el.cine film video** serves as proof-of-concept: it demonstrates how every element designed in the board (character costumes, prop signage, environment location, color grade, and emotional tone) translates faithfully into final cinematic footage. The **Gumvue commercial video** provides a secondary example of the board-to-film pipeline in the advertising domain.

---

## The Master System Prompt

Copy-paste this directly into the system prompt field of your board-generation agent.

```
You are an elite cinematic pre-production visual designer. Your sole function is to generate detailed, professional art director presentation boards (film concept bibles) that communicate character design, props, environments, and visual mood in a single cohesive document image.

## CORE TASK

1. **Document Structure Analysis**: The output is a SINGLE IMAGE that functions as a multi-section presentation board. It must contain labeled sections arranged in a clear spatial grid. Analyze the user's requested sections and assign them to a logical layout:
   - **Movie Poster / Key Visual**: Typically the largest or most prominent section. Contains title typography, tagline, director credit, release status, and a cinematic key visual.
   - **Character Design**: Turnaround sheets showing FRONT, SIDE, and BACK views of each character on clean neutral backgrounds. Must maintain identical proportions, costume details, and facial features across all three views.
   - **Prop Design**: Multi-angle presentation of key props (front, side, back, detail close-up). Include material texture callouts and weathering/aging notes.
   - **Set Design / Environment**: 2–4 cinematic environment shots without people. Wide establishing shot, medium perspective, close detail. Atmospheric lighting, realistic textures, production-level environmental storytelling.
   - **Color Palette**: Row of 4–6 circular or square swatches representing the film's dominant colors plus 1 accent color.
   - **Mood & Tone**: Short paragraph describing the emotional and atmospheric direction.
   - **Materials & Textures**: Small swatch samples of key surface materials (fabric, stone, metal, wood, etc.).
   - **Notes**: 2–4 bullet points with production design insights or world-building rules.

2. **Spatial Layout Engineering**: Describe the board's physical structure explicitly:
   - Define panel positions: left column, top-right grid, middle-right row, bottom strip.
   - Specify the presentation surface: elegant cream parchment, clean white art board, textured kraft paper, or dark cinematic slate.
   - Specify dividers: thin gold lines, clean white gutters, subtle drop shadows, or decorative rules.
   - Ensure sections do not overlap and have balanced negative space.

3. **Typography & Text Integration**: The board contains real text elements that must be legible and stylistically consistent:
   - Film title: Large elegant serif or cinematic sans-serif.
   - Section headers: Small caps, clean sans-serif, all caps or title case.
   - Labels (FRONT / SIDE / BACK / VIEW 1 / VIEW 2): Minimal, functional, uppercase.
   - Body text (mood description, notes): Readable serif or sans-serif at small scale.
   - Do NOT invent illegible gibberish text. If specific text is provided, use it exactly. If not provided, use plausible, short, readable placeholder text.

4. **Cross-Section Consistency Lock**: All sections must feel like they belong to the same film:
   - Same color grading and desaturation level across poster, characters, props, and environments.
   - Same lighting philosophy (e.g., soft overcast, warm golden hour, cool neon).
   - Same realism level (photorealistic, stylized realistic, painterly).
   - Character turnarounds must depict the SAME character in all three views — no drift in face, height, or costume.

## MODEL-AWARE OPTIMIZATION
The refined prompt feeds into: OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit.
- For **generation models** (GPT Image, Seedream, Gemini): Emphasize the document-as-image nature. Describe the board as a physical printed sheet or digital presentation screen. Use natural language flow. Keep under 800 English words; complex layouts need more room than single-subject prompts.
- For **editing models** (Grok Image Edit, Qwen image edit): If a base board or poster image is provided, prepend preservation clauses: "Preserve the existing layout structure, typography positions, and section boundaries. Modify only the character designs to..." or "Keep the board framework intact. Update the color palette and mood text to..."
- **Explicit Purpose / Type**: Always open with the document type: "A professional film pre-production art director guide board," "Hollywood concept design presentation sheet," or "Cinematic visual development bible."

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning or show layout plans. Output ONLY the final prompt.
2. **NO FORMATTING**: No markdown, bullet points, headers, bold text, numbered lists, or line breaks within the prompt body.
3. **STRUCTURE**: Output ONLY a single flowing paragraph (or two short connected paragraphs if complexity demands). Target: **300–600 words**.
4. **DELIMITERS**: Wrap the entire prompt in `[[PROMPT]]` and `[[/PROMPT]]` tags.
5. **NO EXTERNAL TEXT**: Nothing outside the `[[PROMPT]]` tags will be parsed.
6. **MANDATORY COVERAGE**: The prompt must weave together: document type and purpose, presentation surface and dividers, spatial layout description, movie poster content, character turnaround descriptions, prop sheet details, environment views, color palette, mood text, material swatches, notes, typography style, and cross-section consistency lock.
7. **ANTI-OVERLAP ENFORCEMENT**: Explicitly state that sections are separated by clear gutters or divider lines and must not bleed into each other.

## PROHIBITIONS
- NEVER output a single photograph, portrait, or standalone scene. The output must ALWAYS be a multi-section presentation board.
- NEVER generate characters or environments in conflicting art styles (e.g., photorealistic poster next to cartoon turnarounds).
- NEVER omit requested sections. If the user asks for a color palette, material swatches, or notes, they must appear in the output.
- NEVER invent unreadable text or placeholder gibberish. All text must be plausible and stylistically appropriate.
- Do not include aspect ratios, resolution specs, model names, or UI instructions inside the prompt.
- Do not output multiple prompt variants; output one unified optimized prompt.
```

---

## User Prompt Templates

### Template A: Full Board with All Sections (Recommended)

```
Design a professional art director presentation board for the film "Words Change Your World."

Reference images attached:
- Image 1: Old blind main character reference (elderly man, white beard, weathered coat)
- Image 2: Woman character reference (blonde, grey coat, sunglasses, red heels)
- Image 3: Cardboard sign prop reference with text "IT'S A BEAUTIFUL DAY AND I CAN'T SEE IT"
- Image 4: City street environment reference (wet stone, classical architecture, overcast)

Board layout:
- LEFT PANEL: Movie poster showing the two characters on a rainy city street. Title "WORDS CHANGE YOUR WORLD" in large elegant serif. Tagline: "SOMETIMES, THE RIGHT WORDS CAN CHANGE EVERYTHING." "A FILM BY [DIRECTOR NAME]" and "COMING SOON." "ART DIRECTOR GUIDE" label.
- TOP-RIGHT: Character Design section. Old Man turnaround (FRONT, SIDE, BACK) in olive coat and scarf. Woman turnaround (FRONT, SIDE, BACK) in grey coat and red heels. Clean white backgrounds.
- TOP-RIGHT (adjacent): Props section. Cardboard sign — FRONT with text, SIDE showing folded structure, BACK plain. Weathered texture.
- MIDDLE-RIGHT: Set Design — CITY STREET. Three views without people: wide establishing shot of building and stairs, street perspective with lampposts, close ground-level detail of wet pavement.
- BOTTOM STRIP: Color Palette (5 swatches: blue-grey, charcoal, taupe, dusty blue, red accent). Mood & Tone text. Materials & Textures swatches (wet stone, cardboard, wool, glass). Notes section with 3 bullet points.

Overall: Cream parchment background, thin gold divider lines, muted desaturated palette, sophisticated typography, premium cinematic pre-production quality.

Task: Synthesize all references into a single cohesive presentation board image. Maintain character consistency across turnaround views. Ensure all sections share the same muted, realistic cinematic style.
```

### Template B: Minimal Board with Auto-Layout

```
Design a cinematic film pre-production art director guide board for "Words Change Your World."

Reference images attached for characters, props, and environment.

Required sections: Movie poster with title and tagline, character turnarounds (front/side/back), prop multi-angle sheet, three environment views, color palette, mood description, material swatches, production notes.

Style: Elegant cream background, thin decorative dividers, muted desaturated cinematic color grading, sophisticated film industry typography, realistic textures.

Task: Generate a single presentation board image. All sections must share consistent art style and color palette. No section overlap. Clean, professional, award-worthy pre-production quality.
```

### Template C: Editing an Existing Board (for Grok / Qwen)

```
Base board image attached. Preserve the existing layout structure, section boundaries, typography positions, and presentation surface.

Reference images for content updates:
- Image 1: New character design reference
- Image 2: New prop reference
- Image 3: New environment reference

Task: Update the board content while keeping the framework intact. Replace character turnarounds with the new reference. Update prop sheet. Refresh environment views. Maintain the same muted cinematic color grading and professional typography style. Output a prompt describing the updated single board image.
```

---

## Common Anti-Patterns

### Section Collapse / Overlap

**Symptom:** Sections bleed into each other. The movie poster overlaps character turnarounds. Text from the mood description covers environment shots.

**Cause:** Layout not described with explicit spatial boundaries and gutters.

**Fix:** Add explicit anti-overlap language: "separated by clean white gutters," "thin gold divider lines between sections," "sections do not overlap." Describe panel proportions: "left panel occupies 30% width," "bottom strip spans full width."

### Missing Sections

**Symptom:** The board generates with poster, characters, and environments, but the color palette, mood text, or notes section is completely absent.

**Cause:** Prompt lists too many sections; model drops the less visually prominent ones.

**Fix:** Group related minor sections into a single "bottom strip" or "footer bar." Prioritize them by describing them as a unified visual element: "a full-width bottom strip containing color swatches, mood text, material samples, and notes."

### Inconsistent Art Style Across Sections

**Symptom:** Movie poster is photorealistic, character turnarounds look illustrated, environment looks like a 3D render.

**Cause:** No cross-section consistency lock in the prompt.

**Fix:** Add: "All sections share the same photorealistic cinematic style, muted desaturated color grading, and soft overcast lighting. No section may deviate in art style or realism level."

### Character Turnaround Drift

**Symptom:** Front view shows a tall man with a long beard; back view shows a shorter man with different hair.

**Cause:** Model treats each view as an independent generation.

**Fix:** Add strong consistency lock: "The old man is the EXACT SAME person in all three views — identical height, identical facial structure, identical coat and scarf. Only the viewing angle changes."

### Gibberish Typography

**Symptom:** Title text is wavy, illegible, or random characters. Labels are unreadable squiggles.

**Cause:** Model invents text without explicit content.

**Fix:** Provide exact text strings for all major typography: title, tagline, director credit, section headers. For minor labels, specify style: "clean uppercase sans-serif labels reading FRONT, SIDE, BACK."

---

## Good vs Bad Examples

### Good — Complete Board Prompt

> A professional film pre-production art director guide board for "Words Change Your World" on an elegant cream parchment background with thin gold decorative divider lines. The left panel features a cinematic movie poster of a rainy city street with an elderly blind man sitting on wet stone steps and a woman in a light grey coat standing nearby holding a white cane, muted desaturated tones with subtle red accents, large elegant serif title at top, tagline "SOMETIMES, THE RIGHT WORDS CAN CHANGE EVERYTHING," director credit, and "COMING SOON" at bottom. The top-right grid contains character design turnarounds: the old man in an olive winter coat with front side and back views on clean white backgrounds, and the woman in a grey coat with red heels with front side and back views, both maintaining identical proportions and costume details across all angles. Adjacent prop section shows a weathered cardboard sign reading "IT'S A BEAUTIFUL DAY AND I CAN'T SEE IT" from front side and back angles. Below, the set design section presents three cinematic city street environment views without people: a wide establishing shot of classical architecture and stairs, a street perspective with lampposts and wet cobblestones, and a close ground-level detail of wet stone tiles. A full-width bottom strip contains five circular color swatches in blue-grey charcoal taupe dusty blue and red, mood text describing a realistic grounded story of empathy and connection, small material texture samples of wet pavement stone cardboard wool and glass, and three production notes. All sections share consistent muted cinematic color grading, realistic textures, and sophisticated typography. No section overlap, balanced negative space, premium film industry presentation quality.

### Bad — Vague and Under-Structured

> A movie poster with some character designs and props and environments. Make it look professional with good typography and a color palette. Cinematic style.

### Bad — Missing Document Structure

> Generate a beautiful image of an old blind man and a woman on a rainy street, plus some character drawings and a sign and city views. Award-winning drama film aesthetic.

---

## Model-Specific Notes

| Model | Board Generation Tip |
|-------|---------------------|
| **GPT Image** | Handles complex multi-section layouts well if spatial structure is explicit. Provide exact text strings to avoid gibberish typography. |
| **Seedream** | Responds well to "presentation board," "art bible," and "concept sheet" framing. Emphasize document-as-object. |
| **Gemini** | Good at following detailed section lists. May need stronger anti-overlap language. |
| **Grok / Qwen** | Best for editing existing boards. Always prepend layout preservation clauses. |
