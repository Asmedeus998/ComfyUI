# 3D CGI Animation Character Bible

System prompt and user templates for creating **3D CGI animation character design bibles** — multi-section pre-production documents used to lock character identity, expressions, poses, props, and materials before modeling and animation. These are the primary visual artifacts for animated films, series, and ad characters.

---

## When to Use

- Animated film / series character design pitches
- 3D CGI ad character development (mascots, brand ambassadors)
- Game character pre-production bibles
- Animation studio internal model sheets
- Character licensing / merchandising style guides
- VTube / virtual influencer character design locks

## Output

**A single image that IS a multi-section character design document.** A polished pre-production bible containing labeled sections arranged in a clear spatial grid — hero line-up, expression sheet, action poses, prop details, color palette & materials, scale reference, and character bios.

| Element | Description |
|---------|-------------|
| **Sections** | Hero line-up, expression sheet, action pose gallery, prop detail callouts, color palette & materials, scale reference, character bios |
| **Text in Image** | Medium-Heavy — character names, section headers, prop labels, personality keywords, material names |
| **Consistency Challenge** | The SAME character must appear identical across ALL sections — same face, proportions, costume, and materials |

---

## The System Prompt

```
You are an elite 3D CGI animation character designer. Your sole function is to generate detailed, professional character design bibles — multi-section pre-production documents that communicate character identity, personality, expressions, action range, props, and materials in a single cohesive document image.

## CORE TASK

1. **Document Structure Analysis**: The output is a SINGLE IMAGE that functions as a multi-section character bible page. It must contain labeled sections arranged in a clear spatial grid. Analyze the user's requested sections and assign them to a logical layout:
   - **Hero Character Line-Up**: The largest or most prominent section. The hero character(s) standing at full scale on a clean neutral background. For dual-character bibles, both characters stand side by side; for single-character bibles, one character occupies the space. Must show complete costumes, proportions, and silhouette readability. Front 3/4 view is ideal for appeal.
   - **Expression Sheet**: Grid of 3–6 facial expressions per character on clean white backgrounds. Common expressions: Happy, Sad, Angry, Surprised, Determined, Playful. Must maintain identical face shape, eye size, and proportions across all expressions.
   - **Action Pose Gallery**: 4–8 dynamic full-body poses showing the character's movement vocabulary — running, jumping, crouching, gesturing, interacting with props. Must maintain identical body proportions and costume details across all poses.
   - **Prop Detail Callouts**: Close-up panels of key props and costume accessories — hats, weapons, tools, jewelry, footwear, fabric texture swatches. Include material descriptions.
   - **Color Palette & Materials**: Row of circular or square swatches representing skin, hair, primary costume, accent color, prop wood/metal, plus material samples (fabric weave, skin subsurface, metal reflectivity, wood grain).
   - **Scale Reference**: The character shown next to a familiar object (or a second character, if applicable) to establish world scale and height reference.
   - **Character Bios**: Small info panels with icons or labels for Age, Role, Personality Traits, Likes, Dislikes. Use short punchy phrases.

   **Character Count Lock**: Generate EXACTLY the number of characters the user specifies. If the user provides one character reference and asks for one character, output a SINGLE-CHARACTER bible. Do NOT invent a second character from prop, costume, or style references. Secondary reference images are for props, materials, or style only unless explicitly labeled as a second character.

2. **Spatial Layout Engineering**: Describe the bible's physical structure explicitly:
   - Define panel positions: left column (hero line-up + bios), top-right grid (expressions), middle-right grid (action poses), bottom strip (props + palette + scale).
   - Specify the presentation surface: clean white art board, subtle warm grey, or very light cream. NEVER dark or textured backgrounds that fight the characters.
   - Specify dividers: thin light grey lines, clean white gutters, or subtle drop shadows. Avoid heavy decorative dividers.
   - Ensure sections do not overlap and have balanced negative space. Characters should "breathe" in their panels.

3. **Typography & Text Integration**: The bible contains real text elements that must be legible and stylistically consistent:
   - Character names: Large friendly rounded sans-serif or playful serif.
   - Section headers: Small caps, clean sans-serif, all caps, minimal.
   - Labels (FRONT / HAPPY / JUMP / PROP 1): Functional, uppercase, small.
   - Bio text: Readable sans-serif at small scale. Short phrases only.
   - Do NOT invent illegible gibberish text. If specific text is provided, use it exactly. If not provided, use plausible, short, readable placeholder text.

4. **Cross-Section Consistency Lock**: All sections must show the EXACT SAME character:
   - Same face shape, eye size, nose shape, ear position across turnaround, expressions, and action poses.
   - Same body proportions — height, limb length, torso shape, hand size.
   - Same costume details — fabric folds, button placement, logo position, scarf knot style.
   - Same material properties — skin subsurface scattering, fabric softness, metal shine, wood grain.
   - Same lighting direction across all panels (typically soft diffused top-left key light).

## MODEL-AWARE OPTIMIZATION
The refined prompt feeds into: OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit.
- For **generation models** (GPT Image, Seedream, Gemini): Emphasize the document-as-image nature. Describe the bible as a physical printed sheet or digital design screen. Use natural language flow. Keep under 800 English words; complex layouts need more room than single-subject prompts.
- For **editing models** (Grok Image Edit, Qwen image edit): If a base bible or character sketch is provided, prepend preservation clauses: "Preserve the existing layout structure, section boundaries, and typography positions. Modify only the character face design to..." or "Keep the bible framework intact. Update the action poses and expression sheet to..."
- **Explicit Purpose / Type**: Always open with the document type: "A professional 3D CGI animation character design bible," "Pixar-quality character model sheet," or "animated film pre-production character guide."

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning or show layout plans. Output ONLY the final prompt.
2. **NO FORMATTING**: No markdown, bullet points, headers, bold text, numbered lists, or line breaks within the prompt body.
3. **STRUCTURE**: Output ONLY a single flowing paragraph (or two short connected paragraphs if complexity demands). Target: **300–600 words**.
4. **DELIMITERS**: Wrap the entire prompt in `[[PROMPT]]` and `[[/PROMPT]]` tags.
5. **NO EXTERNAL TEXT**: Nothing outside the `[[PROMPT]]` tags will be parsed.
6. **MANDATORY COVERAGE**: The prompt must weave together: document type and purpose, presentation surface and dividers, spatial layout description, hero line-up content, expression sheet descriptions, action pose gallery, prop detail callouts, color palette and material swatches, scale reference, character bios, typography style, and cross-section consistency lock.
7. **ANTI-OVERLAP ENFORCEMENT**: Explicitly state that sections are separated by clear gutters or divider lines and must not bleed into each other.

## PROHIBITIONS
- NEVER output a single character portrait or standalone scene. The output must ALWAYS be a multi-section character bible.
- NEVER generate characters in conflicting art styles (e.g., realistic hero next to cartoon expressions).
- NEVER omit requested sections. If the user asks for an expression sheet, action poses, or prop details, they must appear.
- NEVER invent unreadable text or placeholder gibberish. All text must be plausible and stylistically appropriate.
- Do not include aspect ratios, resolution specs, model names, or UI instructions inside the prompt.
- Do not output multiple prompt variants; output one unified optimized prompt.
```

---

## User Prompt Templates

### Template A1: Single Character Bible (Recommended for Solo Characters)

```
Design a professional 3D CGI animation character design bible for "[PROJECT NAME]." This is a SINGLE-CHARACTER bible. Do NOT generate a second character.

Reference images attached:
- Image 1: Main character reference — [character description: age, build, costume, key features]
- Image 2: Prop reference — [key prop: weapon, tool, accessory]
- Image 3: Style reference — [target aesthetic: Pixar, anime-CGI, claymation, etc.]
- Image 4: Additional prop / material reference — [optional extra prop or texture reference]

Bible layout:
- LEFT COLUMN (large): Hero line-up showing ONE character standing at full scale on clean white background. [Character name] is [height/build] wearing [costume]. Title "[PROJECT NAME]" at top. "CHARACTER DESIGN BIBLE" label.
- TOP-RIGHT: Expression Sheet — 6 facial expressions for this ONE character: [EXPRESSION 1], [EXPRESSION 2], [EXPRESSION 3], [EXPRESSION 4], [EXPRESSION 5], [EXPRESSION 6]. Clean white backgrounds. Small uppercase labels beneath each.
- MIDDLE-RIGHT: Action Pose Gallery — 6 dynamic full-body poses: [POSE 1], [POSE 2], [POSE 3], [POSE 4], [POSE 5], [POSE 6]. Maintain identical proportions and costume.
- BOTTOM-RIGHT: Key Details — close-up panels of [PROP 1], [PROP 2], [COSTUME DETAIL 1], [COSTUME DETAIL 2], [COSTUME DETAIL 3], [FOOTWEAR]. Include material texture.
- BOTTOM-LEFT: Character Bio — Age, Role, Personality, Likes, Dislikes for this ONE character. Icon-style layout.
- BOTTOM-CENTER: Color Palette & Materials — skin, hair, cloth, accent, wood, metal, special material swatches with material name labels.
- BOTTOM-RIGHT: Scale Reference — character next to [SCALE OBJECT] showing world scale.

Overall: Clean white background, thin light grey divider lines, [AESTHETIC DESCRIPTOR] 3D CGI style, soft appealing lighting, subsurface skin scattering, fabric micro-detail, Pixar-quality appeal.

Task: Synthesize all references into a single cohesive SINGLE-CHARACTER bible image. Maintain absolute character consistency across turnaround, expressions, and action poses. ONLY ONE character appears in this bible. Prop and style references must NOT be interpreted as second characters. All sections share the same 3D CGI art style, lighting, and material quality.
```

### Template A2: Dual Character Bible (For Pairs / Duos)

```
Design a professional 3D CGI animation character design bible for "[PROJECT NAME]." This is a DUAL-CHARACTER bible.

Reference images attached:
- Image 1: Main character reference — [character A description: age, build, costume, key features]
- Image 2: Secondary character reference — [character B description: age, build, costume, key features]
- Image 3: Prop reference — [key prop: weapon, tool, accessory]
- Image 4: Style reference — [target aesthetic: Pixar, anime-CGI, claymation, etc.]

Bible layout:
- LEFT COLUMN (large): Hero line-up showing BOTH characters standing side by side at full scale on clean white background. Character A is [height/build] wearing [costume]. Character B is [height/build] wearing [costume]. Title "[PROJECT NAME]" at top. "CHARACTER DESIGN BIBLE" label.
- TOP-RIGHT: Expression Sheet — 3 expressions per character. Character A: [EXPRESSION 1], [EXPRESSION 2], [EXPRESSION 3]. Character B: [EXPRESSION 1], [EXPRESSION 2], [EXPRESSION 3]. Clean white backgrounds. Small uppercase labels beneath each.
- MIDDLE-RIGHT: Action Pose Gallery — 6 dynamic full-body poses: [POSE 1], [POSE 2], [POSE 3], [POSE 4], [POSE 5], [POSE 6]. Maintain identical proportions and costume.
- BOTTOM-RIGHT: Key Details — close-up panels of [PROP 1], [PROP 2], [COSTUME DETAIL 1], [COSTUME DETAIL 2], [COSTUME DETAIL 3], [FOOTWEAR]. Include material texture.
- BOTTOM-LEFT: Character Bios — Age, Role, Personality, Likes, Dislikes for both characters. Icon-style layout.
- BOTTOM-CENTER: Color Palette & Materials — skin, hair, cloth, accent, wood, metal, special material swatches with material name labels.
- BOTTOM-RIGHT: Scale Reference — both characters next to [SCALE OBJECT] showing height difference.

Overall: Clean white background, thin light grey divider lines, [AESTHETIC DESCRIPTOR] 3D CGI style, soft appealing lighting, subsurface skin scattering, fabric micro-detail, Pixar-quality appeal.

Task: Synthesize all references into a single cohesive character bible image. Maintain absolute character consistency across turnaround, expressions, and action poses. All sections share the same 3D CGI art style, lighting, and material quality.
```

### Template B1: Minimal Single-Character Bible

```
Design a 3D CGI animation character model sheet for "[PROJECT NAME]." SINGLE CHARACTER ONLY.

Reference images attached for character design, costume, prop, and target style.

Required sections: Hero character line-up (ONE character only), expression sheet (6 expressions for this one character), action pose gallery (6 poses), prop detail callouts (4–6 items), color palette & material swatches, scale reference, character bio panel.

Style: Clean white art board, thin light grey gutters, [AESTHETIC] 3D CGI character design, soft diffused lighting, appealing rounded shapes, production-ready quality.

Task: Generate a single character bible image containing exactly ONE character. Do NOT create a second character from prop or style references. All sections must share consistent 3D art style, lighting, and proportions. No section overlap. Professional animation studio presentation quality.
```

### Template B2: Minimal Dual-Character Bible

```
Design a 3D CGI animation character model sheet for "[PROJECT NAME]." DUAL CHARACTER.

Reference images attached for character design, costume, prop, and target style.

Required sections: Hero character line-up (both characters), expression sheet (3 per character), action pose gallery (6 poses), prop detail callouts (4–6 items), color palette & material swatches, scale reference, character bio panels.

Style: Clean white art board, thin light grey gutters, [AESTHETIC] 3D CGI character design, soft diffused lighting, appealing rounded shapes, production-ready quality.

Task: Generate a single character bible image. All sections must share consistent 3D art style, lighting, and proportions. No section overlap. Professional animation studio presentation quality.
```

### Template C: Editing an Existing Bible (for Grok / Qwen)

```
Base character bible image attached. Preserve the existing layout structure, section boundaries, typography positions, and presentation surface.

Reference images for content updates:
- Image 1: Revised character face design
- Image 2: New costume reference
- Image 3: Updated prop reference

Task: Update the bible content while keeping the framework intact. Replace hero line-up with new character design. Refresh expression sheet and action poses. Update prop details. Maintain the same [AESTHETIC] 3D CGI style and professional typography. Output a prompt describing the updated single bible image.
```

### Template D: Character Bible with Environment / Atmospheric Background

```
Design a professional 3D CGI animation character design bible for "[PROJECT NAME]." This is a SINGLE-CHARACTER bible set within an atmospheric environment. Do NOT generate a second character.

Reference images attached:
- Image 1: Main character reference — [character description: age, build, costume, key features]
- Image 2: Environment / background reference — [atmosphere: bamboo forest, ink-wash mountains, moonlit temple, cherry blossom garden, etc.]
- Image 3: Prop reference — [key prop: weapon, tool, accessory]
- Image 4: Style reference — [target aesthetic: Pixar, anime-CGI, claymation, etc.]

Bible layout:
- LEFT COLUMN (large): Hero line-up showing ONE character standing at full scale against the environment background. The character is [height/build] wearing [costume]. The background incorporates the atmosphere from the environment reference — [describe: misty bamboo, moonlit peaks, falling petals, etc.]. Title "[PROJECT NAME]" at top. "CHARACTER DESIGN BIBLE" label.
- TOP-RIGHT: Expression Sheet — 6 facial expressions for this ONE character: [EXPRESSION 1], [EXPRESSION 2], [EXPRESSION 3], [EXPRESSION 4], [EXPRESSION 5], [EXPRESSION 6]. Each expression is shown as a portrait inset against a subtle vignette of the environment background. Small uppercase labels beneath each.
- MIDDLE-RIGHT: Action Pose Gallery — 6 dynamic full-body poses: [POSE 1], [POSE 2], [POSE 3], [POSE 4], [POSE 5], [POSE 6]. The character interacts with the environment — standing on rocks, beneath bamboo, near waterfalls, etc. Maintain identical proportions and costume.
- BOTTOM-RIGHT: Key Details — close-up panels of [PROP 1], [PROP 2], [COSTUME DETAIL 1], [COSTUME DETAIL 2], [COSTUME DETAIL 3], [FOOTWEAR]. Include material texture.
- BOTTOM-LEFT: Character Bio — Age, Role, Personality, Likes, Dislikes for this ONE character. Icon-style layout on a subtle background texture.
- BOTTOM-CENTER: Color Palette & Materials — skin, hair, cloth, accent, wood, metal, environment tone swatches with material name labels.
- BOTTOM-RIGHT: Scale Reference — character next to [SCALE OBJECT] within the environment showing world scale.

Overall: [ENVIRONMENT DESCRIPTOR] background inspired by the attached environment reference — atmospheric depth, mist layers, ink-wash gradients, or cinematic lighting. Thin light grey divider lines, [AESTHETIC DESCRIPTOR] 3D CGI style, soft appealing lighting with environmental color bounce, subsurface skin scattering, fabric micro-detail, Pixar-quality appeal.

Task: Synthesize all references into a single cohesive SINGLE-CHARACTER bible image. The environment background must be visible in the hero line-up and expression portraits, creating an immersive pre-production document. Maintain absolute character consistency across turnaround, expressions, and action poses. ONLY ONE character appears in this bible. Prop and style references must NOT be interpreted as second characters. All sections share the same 3D CGI art style, lighting, and material quality.
```

---

## Common Anti-Patterns

### Unwanted Second Character Invention
**Symptom:** The user provided one character reference plus prop/costume/style references, but the bible generates two distinct characters — often treating a clothing flatlay or product photo as a "second character."  
**Cause:** The prompt template defaults to dual-character language ("both characters," "Character A / Character B") or the model invents a second figure from accessory/prop images.  
**Fix:** Use the **Single-Character templates (A1 / B1)**. Explicitly state "SINGLE-CHARACTER bible" and "Do NOT generate a second character." Label every reference image clearly: "Image 1: Main character reference," "Image 2: Prop reference," "Image 3: Style reference." Add a character count lock: "ONLY ONE character appears in this bible. Prop and style references must NOT be interpreted as second characters."

### Character Drift Between Sections
**Symptom:** The hero line-up shows a round-faced character with large eyes, but the expression sheet shows a longer face with smaller eyes. Action poses have different body proportions.  
**Cause:** No strong consistency lock tying all sections to the same character identity.  
**Fix:** Add explicit consistency language: "The SAME character appears in EVERY section — identical face shape, eye size, nose shape, body height, and costume. Only expression and pose change."

### Expression Sheet Looks Like Different People
**Symptom:** Each expression looks like a different character. Happy face has round eyes; angry face has narrow eyes AND a different nose.  
**Cause:** Model treats each expression as an independent generation.  
**Fix:** Lock facial structure: "All expressions share the EXACT same base face — same eye shape, same nose, same mouth width, same ear position. Only eyebrows, eyelids, and mouth corners move to express emotion."

### Action Poses Break Proportions
**Symptom:** Jump pose has longer legs. Crouching pose has a different torso length. Hands change size between poses.  
**Cause:** Dynamic poses trigger proportion drift.  
**Fix:** Add: "All action poses maintain identical body proportions — same limb length, same torso height, same head size. Poses are dynamic but anatomically consistent."

### Missing Prop or Material Sections
**Symptom:** The bible generates with characters and expressions, but prop details, material swatches, or scale reference are completely absent.  
**Cause:** Prompt lists too many sections; model drops the less visually prominent ones.  
**Fix:** Group related minor sections into a unified bottom strip: "a full-width bottom strip containing prop detail callouts, color palette and material swatches, scale reference, and character bios."

### Section Overlap / Crowding
**Symptom:** The hero line-up overlaps the expression sheet. Action poses bleed into prop details. Text covers character faces.  
**Cause:** Layout not described with explicit spatial boundaries.  
**Fix:** Add explicit anti-overlap language: "separated by clean white gutters," "thin light grey divider lines between sections," "sections do not overlap."

### Inconsistent Rendering Quality
**Symptom:** Hero line-up is beautifully rendered 3D CGI, but expressions look flat or action poses look like sketches.  
**Cause:** No cross-section quality lock.  
**Fix:** Add: "All sections share the SAME 3D CGI rendering quality — subsurface skin scattering, fabric micro-detail, soft ambient occlusion, and appealing warm lighting. No section may deviate in render quality or art style."

---

## Good vs Bad Examples

### Good — Complete Character Bible Prompt

> A professional 3D CGI animation character design bible for "Baobao & Master" on a clean white art board background with thin light grey divider lines. The left column occupying 35 percent width features a hero character line-up showing two characters standing side by side at full scale on a clean white background — Baobao, a small optimistic 10-year-old apprentice chef boy with big expressive eyes, wearing a cream-colored traditional Chinese chef uniform with a red scarf and a woven bamboo steamer hat, holding a bamboo steamer basket filled with dumplings; and Master, a large kind heavyset kung fu chef master in his 40s with a warm smile, small goatee, and hair tied in a topknot, wearing the same cream uniform with a broader red sash, arms crossed confidently. Above them the title "BAOBAO & MASTER" in large friendly rounded sans-serif with Chinese characters beside it, and the subtitle "THE APPRENTICE & THE KUNGFU MASTER CHEFS." The top-right grid contains an Expression Sheet with three expressions per character on clean white backgrounds — Baobao showing Hopeful, Focused, and Embarrassed; Master showing Kind, Proud, and Playful — all maintaining identical face shapes and proportions with only eyebrows and mouth changing. Below that, an Action Pose Gallery presents six dynamic full-body poses on clean white backgrounds: Steamer Balance, Dance Step, Dumpling Twirl, Kungfu Stance, Teaching, and Approving — both characters in identical costumes with consistent proportions. The bottom-right section shows Key Details — close-up panels of Baobao's woven bamboo steamer hat texture, the red scarf knot, Baobao's black cloth shoes, a bamboo steamer basket filled with white dumplings, Master's topknot with red band, Master's apron with a circular dumpling logo, and Master's sturdy black shoes. The bottom-left contains Character Bio panels with small icons for Age, Role, Personality, Likes, and Dislikes for both characters. The bottom-center shows a Color Palette & Materials row with circular swatches for skin tone, black hair, cream cloth, red scarf, bamboo yellow, wood brown, flour dust white, steam grey, and metal accent grey, each with small material name labels. The bottom-right shows a Scale Reference with both characters standing next to a tall stack of bamboo steamers to emphasize their height difference. All sections share consistent Pixar-quality 3D CGI rendering with soft rounded appealing shapes, warm subsurface skin scattering, fabric micro-detail, soft diffused top-left lighting, and clean professional animation studio presentation quality. No section overlap, balanced negative space, white background throughout.

### Bad — Vague and Under-Structured

> A character design sheet for an animated film about chefs. Make it look cute and 3D with good expressions and poses. Pixar style.

### Bad — Missing Document Structure

> Generate a beautiful image of a boy chef and his master standing together, plus some face expressions and action poses and props. Cute 3D animation style.

---

## Model-Specific Notes

| Model | Bible Generation Tip |
|-------|---------------------|
| **GPT Image** | Handles complex multi-section layouts well if spatial structure is explicit. Provide exact text strings for character names and section headers to avoid gibberish typography. |
| **Seedream** | Responds well to "character bible," "model sheet," and "design sheet" framing. Emphasize document-as-object and 3D CGI quality. |
| **Gemini** | Good at following detailed section lists. May need stronger anti-overlap and consistency-lock language. |
| **Grok / Qwen** | Best for editing existing bibles. Always prepend layout and proportion preservation clauses. |
