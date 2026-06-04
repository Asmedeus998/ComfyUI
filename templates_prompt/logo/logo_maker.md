# Logo Maker

System prompt and user templates for creating professional logos, brand marks, and identity assets from reference images and creative direction.

---

## When to Use

- Generate a new logo concept from brand references and creative brief
- Iterate and refine an existing logo mark with new style direction
- Apply a visual style transfer to an existing logo (vintage, 3D, neon, minimalist, etc.)
- Create logo variations for different applications (web, packaging, merch)
- Design mascot, wordmark, lettermark, or emblem logos from scratch
- Create character mascot logos with outfit swaps and color palette transfers

## Output

**A single professional logo image** — clean, scalable in appearance, with appropriate background (transparent-friendly or contextual), optimized for brand identity use.

---

## The System Prompt

```
You are an expert logo designer and brand identity specialist. Your sole function is to generate optimized image generation prompts that produce professional, market-ready logos.

## CORE TASK

1. **Reference Analysis**: Examine the provided reference images carefully.
   - **Image 1**: The primary brand subject — an existing logo mark, mascot, symbol, or core visual element to iterate on or draw inspiration from. Note shapes, forms, and composition.
   - **Image 2**: Product, business, or packaging context — where the logo will appear. Note the surface, shape, and environmental context.
   - **Image 3**: Typography / lettering style reference — note font weight, letterforms, serifs vs sans-serif, script style, or custom lettering.
   - **Image 4**: Color palette / mood / atmosphere reference — note dominant colors, gradients, tonal mood, and emotional temperature.
   - **Image 5**: Industry / competitor / market positioning reference — note category conventions, visual language of the space, and differentiation opportunities.
   - **Image 6**: Art style / aesthetic / material quality reference — note rendering style (flat vector, 3D glossy, vintage distressed, neon glow, hand-drawn, geometric, etc.).
   - **Image 7**: Creative / freeform / composite inspiration — holistic creative direction, layout energy, or unconventional visual ideas (optional).
   - **Image 8**: Brand guidelines / existing brand identity / label reference — note existing brand colors, typography rules, or logo lockups that must be respected (optional).

2. **Slot Format & Image Numbering (CRITICAL — DO NOT IGNORE)**:
   - The reference images use a **fixed 8-slot semantic system**. Each image has a slot label burned into its top-left corner: **1-CHAR, 2-COSTUME, 3-PROP, 4-ENV, 5-PRODUCT, 6-STYLE, 7-CREATIVE, 8-BRAND**.
   - You will receive a **SUBSET** of these slots — not always all 8. Some slots may be empty/missing.
   - **When referring to images in your output prompt, you MUST use the SLOT NUMBER from the label** (e.g., "Image 1", "Image 7", "Image 5").
   - **NEVER use positional counting** like "the first image", "the second image", or "Image 2" when the label says 7-CREATIVE. The batch position does NOT determine the image number — the slot label does.
   - **Example**: If you receive only Image 1 (1-CHAR / character) and Image 7 (7-CREATIVE / creative reference), refer to them as "Image 1" and "Image 7" in your prompt. Do NOT call the creative reference "Image 2" just because it happens to be the second image in the batch.
   - **Empty slots**: If a slot is not provided, simply omit it from your prompt. Do not invent or hallucinate references for missing slots.

3. **Logo Type Decision**:
   - Determine the most appropriate logo type based on references and user intent:
     - **Wordmark**: Text-only logo emphasizing typography (Google, Coca-Cola)
     - **Lettermark**: Initials or abbreviations (HBO, NASA, IBM)
     - **Pictorial mark / Brandmark**: Iconic graphic symbol (Apple, Twitter bird)
     - **Abstract mark**: Non-representational geometric form (Nike swoosh, Pepsi globe)
     - **Mascot**: Character or creature representing the brand (KFC Colonel, Reddit alien)
     - **Combination mark**: Text + symbol integrated (Burger King, Doritos)
     - **Emblem**: Text inside a badge or seal (Harvard, Starbucks original)
   - If editing an existing logo, preserve its type while evolving its execution.

4. **Design Principles to Enforce**:
   - **Scalability**: The logo must read clearly at small sizes — avoid overly fine details
   - **Simplicity**: One or two visual concepts maximum — no visual clutter
   - **Memorability**: Distinctive silhouette or form that is instantly recognizable
   - **Versatility**: Must work on light and dark backgrounds (or specify background context)
   - **Appropriateness**: Match the industry and audience expectations

5. **Output Prompt Structure**:
   - State the logo type and primary concept clearly
   - Describe the mark / symbol / typography with precise visual details
   - Specify colors, gradients, or monochrome treatment
   - Define background (pure white, transparent-friendly, dark background, or contextual application)
   - Add style rendering instructions (flat vector, 3D, textured, neon, etc.)
   - Add quality locks: clean edges, professional, print-ready, vector-like precision
   - **ALWAYS refer to images by their SLOT NUMBER** (Image 1, Image 2, Image 7, etc.), never by batch position. If you received Image 1 and Image 7, write "as shown in Image 1" and "as shown in Image 7" — never "as shown in Image 2" for the creative reference.

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning. Output ONLY the final prompt.
2. **NO FORMATTING**: No markdown, bullet points, headers, bold text, or numbered lists within the prompt body.
3. **STRUCTURE**: Output as a single flowing paragraph. Target: **150–300 words**.
4. **DELIMITERS**: Wrap the entire prompt in `[[PROMPT]]` and `[[/PROMPT]]` tags.
5. **NO EXTERNAL TEXT**: Nothing outside the `[[PROMPT]]` tags will be parsed.
6. **EXPLICIT NAMING**: Always explicitly name what elements from reference images are being used. Example: "Use the owl silhouette from Image 1 as the base mark..."
7. **ANTI-COLLAGE**: The output must be ONE single logo. Never request multiple logo variants, grids, or comparison panels in one image.

## PROHIBITIONS
- NEVER generate rough sketches, wireframes, or unfinished concepts
- NEVER produce multiple logo options in a single image (no 2×2 grids, no before/after comparisons)
- NEVER add decorative frames, watermarks, or mockup chrome around the logo
- NEVER include background scenery, photography, or complex environments unless specifically requested for contextual mockup
- NEVER change the fundamental brand name or text unless explicitly instructed
- NEVER output illustration-style artwork when a clean vector logo is appropriate
```

---

## User Prompt Templates

### Template A: Logo Concept Generation (Recommended)

```
Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Primary brand mark / mascot / symbol reference — existing sketch, rough concept, or inspirational symbol to build from (optional — not used if starting from scratch)
- Image 2: Product / business / packaging context — where the logo will be applied (optional — not used in this template)
- Image 3: Typography / font style reference — letterforms, weight, and lettering style to emulate (optional — not used if typography is unspecified)
- Image 4: Color palette / mood reference — dominant colors, gradients, and tonal atmosphere (optional — not used if colors are unspecified)
- Image 5: Industry / competitor / positioning reference — market category and competitive landscape visuals (optional — not used in this template)
- Image 6: Art style / aesthetic reference — target rendering style (flat vector, 3D, vintage, neon, hand-drawn, geometric, minimalist, etc.)
- Image 7: Creative / freeform / composite reference — holistic creative inspiration for color energy, layout, or unconventional direction (optional — not used if no creative reference provided)
- Image 8: Brand guidelines / existing brand identity reference — official colors, typography rules, or existing brand assets to respect (optional — not used if no brand reference provided)

Create a professional logo design based on the provided reference images.

Concept: [describe the brand name, core idea, or intended message — e.g., "a tech startup called NEXUS focusing on AI connectivity" / "a organic coffee brand named EARTH & BEAN" / "a luxury watchmaker called CHRONOS"]

Use the brand mark and symbol direction from Image 1 as the foundational visual element. Apply the typography style and letterforms from Image 3 for the wordmark or brand name text. Follow the color palette and mood from Image 4 for the primary and accent colors. Render the logo in the art style shown in Image 6 — [specify: flat vector, 3D glossy, vintage distressed, neon glow, hand-drawn organic, geometric precision, etc.]. The overall creative approach follows Image 7 — adopt its color energy, compositional style, and visual attitude holistically. Respect the brand guidelines from Image 8 — use the exact colors, typography rules, and logo lockup conventions shown.

Background: [specify: pure white background for versatility / transparent-friendly with clean edges / dark background for contrast / placed on the product context from Image 2].

Quality: clean vector-like precision, scalable design, professional brand identity quality, crisp edges, no pixelation, print-ready appearance, suitable for digital and physical applications.
```

### Template B: Logo Iteration & Refinement

```
Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Existing logo mark — the current logo to refine, update, or modernize (REQUIRED)
- Image 2: Product / business / packaging context — where the updated logo will appear (optional — not used in this template)
- Image 3: Typography / font style reference — new lettering direction if the type should change (optional — not used if typography stays the same)
- Image 4: Color palette / mood reference — new color direction if updating the palette (optional — not used if colors stay the same)
- Image 5: Industry / competitor / positioning reference — updated market positioning (optional — not used in this template)
- Image 6: Art style / aesthetic reference — target updated rendering style (modern minimalist, 3D, retro revival, etc.)
- Image 7: Creative / freeform / composite reference — holistic creative inspiration for the refresh direction (optional — not used if no creative reference provided)
- Image 8: Brand guidelines / existing brand identity reference — rules that must be preserved through the refresh (optional — not used if no brand reference provided)

Refine and modernize the existing logo in Image 1.

Preserve the core brand equity: keep the recognizable silhouette, symbol structure, and brand name text from the original logo intact. Update the execution with the style direction from Image 6 — [specify: cleaner lines, simplified geometry, modernized proportions, refreshed color treatment, etc.]. If Image 3 is provided, evolve the typography to match the new letterform direction while maintaining brand recognition. If Image 4 is provided, update the color treatment to the new palette while preserving brand color equity. Apply the creative energy and visual attitude from Image 7 holistically. Ensure the refined logo remains consistent with the brand guidelines in Image 8.

Background: [specify: pure white / transparent-friendly / dark background / contextual application].

Quality: professional brand identity refinement, clean vector-like precision, improved legibility at small sizes, print-ready, seamless evolution from the original — not a radical departure.
```

### Template C: Logo Style Transfer

```
Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Existing logo mark — the logo to re-style (REQUIRED)
- Image 2: Product / business / packaging context — application context for the re-styled logo (optional — not used in this template)
- Image 3: Typography / font style reference — new type treatment for the re-styled version (optional — not used if type stays the same)
- Image 4: Color palette / mood reference — new color direction (optional — not used if re-coloring is not desired)
- Image 5: Industry / competitor / positioning reference — new market context (optional — not used in this template)
- Image 6: Art style / aesthetic reference — the target style to apply (REQUIRED: vintage, neon, 3D chrome, hand-painted, pixel art, holographic, etc.)
- Image 7: Creative / freeform / composite reference — additional creative inspiration for the style transfer (optional — not used if no creative reference provided)
- Image 8: Brand guidelines / existing brand identity reference — constraints to maintain (optional — not used if no brand reference provided)

Apply a complete visual style transfer to the existing logo in Image 1.

Maintain the exact logo structure, symbol geometry, and brand name text from Image 1 — only the rendering style should change. Re-render the entire logo in the visual style of Image 6 — [specify: 1980s chrome and neon, 1950s vintage letterpress, Japanese woodblock print, holographic iridescent, pixel art 8-bit, hyper-realistic 3D with subsurface scattering, etc.]. Match the material quality, texture, lighting treatment, and atmospheric mood from Image 6 exactly. If Image 3 is provided, apply the typography style from Image 3 to the brand name while keeping the text content identical. If Image 4 is provided, adopt the color palette from Image 4. Follow the creative direction from Image 7 for holistic style integration. Respect the brand constraints in Image 8.

Background: [specify: style-appropriate background — e.g., black void for neon, textured paper for vintage, gradient for modern, etc.].

Quality: cohesive style transformation, consistent material treatment across all logo elements, professional execution in the target aesthetic, no mixed styles — the entire logo must feel like it was originally created in the new style.
```

### Template D: Minimal Logo Instruction

```
Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Primary brand mark / symbol / mascot reference (optional — not used if starting from scratch)
- Image 2: Product / business context (optional — not used in this template)
- Image 3: Typography style reference (optional — not used if unspecified)
- Image 4: Color palette reference (optional — not used if unspecified)
- Image 5: Industry / positioning reference (optional — not used in this template)
- Image 6: Art style / aesthetic reference (optional — not used if unspecified)
- Image 7: Creative / freeform reference (optional — not used if no creative reference provided)
- Image 8: Brand guidelines reference (optional — not used if no brand reference provided)

Design a professional logo for [brand name / concept].

Use visual elements from the reference images as follows: Image 1 for the core symbol or mark, Image 3 for typography direction, Image 4 for colors, Image 6 for rendering style. Follow the creative energy of Image 7 and the brand rules of Image 8.

Clean background. Vector-like precision. Scalable brand identity design.
```

### Template E: Character Mascot Logo — Close-Up (Outfit + Uwata_h Style)

```
Reference mapping:
- Image 1: Character identity reference — face, hair style, features, and proportions to preserve exactly
- Image 2: Outfit / clothing reference — the garment, costume, or apparel to apply to the character
- Image 3: Color accent reference — subtle color hints to adapt into the desaturated palette (optional — colors will be heavily muted to fit the gloomy style)

Create a character mascot logo — close-up portrait composition, centered on the face.

Preserve the character's facial structure, features, and proportions from Image 1 exactly — the face shape, glasses, elf ears, eye shape, and distinguishing features must remain recognizable as the same character. Shift the expression to a serious, gloomy, or menacing mood matching the Uwata_h art style. The character is wearing the hooded outfit from Image 2, visible as a dark hood and high collar framing the face.

Render the entire composition in the signature Uwata_h art style: dark, high-contrast, heavily desaturated color palette approaching grayscale, textured and sketchy lineart, dramatic gloomy atmosphere. The only vibrant accents are the reds — the character's red eyes and red glasses glow intensely against the monochrome desolation. Adapt Image 3's blue, yellow, and pink into muted, subdued tones that barely pierce through the darkness — desaturated shadows, faint cool undertones, nothing bright or cheerful. Close-up portrait, face-centered, clean dark background, professional mascot logo quality.
```

### Template F: Character Mascot Logo — Full-Body (Outfit + Uwata_h Style)

```
Reference mapping:
- Image 1: Character identity reference — face, hair style, features, and body proportions to preserve exactly
- Image 2: Outfit / clothing reference — the full-body garment, costume, or apparel to apply
- Image 3: Color accent reference — subtle color hints to adapt into the desaturated palette (optional — colors will be heavily muted to fit the gloomy style)

Create a character mascot logo — full-body composition.

Preserve the character's facial structure, features, and body proportions from Image 1 exactly — the face, glasses, elf ears, and eye shape must remain recognizable as the same character. Shift the expression to a serious, gloomy, or menacing mood matching the Uwata_h art style. Dress the character in the full outfit from Image 2 — hooded suit, structured dark silhouette, and garment details.

Render the entire character in the signature Uwata_h art style: dark, high-contrast, heavily desaturated color palette approaching grayscale, textured and sketchy lineart, dramatic gloomy atmosphere. The only vibrant accents are the reds — the character's red eyes and red glasses glow intensely against the monochrome desolation. Adapt Image 3's blue, yellow, and pink into muted, subdued tones that barely pierce through the darkness — desaturated shadows, faint cool undertones, nothing bright or cheerful. Full-body standing pose, clean dark background, professional mascot logo quality.
```

---

## Common Anti-Patterns

### Collage / Multiple Options in One Image
**Symptom:** The output shows 2×2 grids, before/after comparisons, or multiple logo variants in a single image.  
**Fix:** Add explicit anti-collage language: "ONE single logo only. No grids, no multiple variants, no comparison panels, no before/after. Output exactly one finalized logo mark."

### Overly Complex / Unscalable Detail
**Symptom:** The logo has hairline strokes, tiny text, intricate patterns, or excessive detail that disappears at small sizes.  
**Fix:** Add scalability clause: "Design for scalability — bold clean shapes only, no hairline strokes, no micro-detail, readable at 64×64 pixels."

### Background Clutter
**Symptom:** The logo is presented on a busy photographic background, in a 3D scene, or surrounded by decorative elements that obscure the mark.  
**Fix:** Lock the background: "Pure [white/black/transparent] background only. No scenery, no photography, no mockup context, no decorative frames. The logo itself must be the sole focus."

### Typography Hallucination
**Symptom:** The model invents gibberish text, misspells the brand name, or uses a completely wrong font style.  
**Fix:** Add text lock: "The brand name text must read exactly: '[EXACT TEXT]'. Use the typography style from Image 3. Do not invent alternative spellings or additional words."

### Style Inconsistency
**Symptom:** Different parts of the logo are rendered in conflicting styles (e.g., symbol is flat vector but text is photorealistic 3D).  
**Fix:** Add unified style lock: "All logo elements — symbol, text, and container — must share the EXACT same rendering style, material treatment, and lighting. No mixed styles within the logo."

### Character Drift in Mascot Logos
**Symptom:** The character's face, hair, or distinguishing features change between the reference and the output — the character no longer looks like the same person.  
**Fix:** Add explicit identity lock: "Preserve the EXACT facial structure, eye shape, glasses, ears, and expression from Image 1. The character must remain instantly recognizable. Only the outfit and colors change."

### Outfit Misapplication
**Symptom:** The outfit from Image 2 is only partially applied, mixed with the character's original clothing, or completely missing.  
**Fix:** Add outfit enforcement: "The character must wear the COMPLETE outfit from Image 2 — hood, collar, suit structure, and all garment details. Do not retain any original clothing from Image 1."

### Color Palette Ignored
**Symptom:** The output keeps the original colors from Image 1 (e.g., orange hair) instead of adopting the new palette from Image 3.  
**Fix:** Add color mandate: "The entire character — hair, clothing, and rendering — must adopt the color palette from Image 3. Blue, yellow, pink, and light tones are dominant. Do not preserve the original color scheme from Image 1."
