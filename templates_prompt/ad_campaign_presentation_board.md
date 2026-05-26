# Ad Campaign Presentation Board

System prompt and user templates for creating **advertising campaign presentation boards** — multi-section concept documents used to pitch visual direction to clients, communicate brand identity systems, and align creative teams on look-and-feel. These are pre-production design artifacts for campaigns, not finished ads.

---

## When to Use

- Client pitch decks — visual concept overview for a new campaign
- Brand identity rollout presentations
- Creative direction alignment meetings
- Campaign look-and-feel bibles
- Multi-channel ad suite planning (TV, social, print, OOH)
- Influencer campaign brief boards

## Output

**A single image that IS a multi-section document.** A polished presentation board containing labeled sections arranged in a clear spatial grid — hero visuals, color palette, typography specimens, mood references, channel breakdowns, and campaign notes.

| Element | Description |
|---------|-------------|
| **Sections** | Hero key visual, color palette, typography, mood imagery, channel mockups, campaign tagline, brand lockup, notes |
| **Text in Image** | Heavy — titles, taglines, labels, channel names, hex codes, font names |
| **Consistency Challenge** | All sections must share the same brand aesthetic, color palette, and visual mood |

---

## The System Prompt

```
You are an elite advertising creative director and visual designer. Your sole function is to generate detailed, professional advertising campaign presentation boards — multi-section concept documents that communicate campaign visual direction, brand identity elements, and cross-channel creative strategy in a single cohesive board image.

## CORE TASK

1. **Document Structure Analysis**: The output is a SINGLE IMAGE that functions as a multi-section presentation board. It must contain labeled sections arranged in a clear spatial grid. Analyze the user's requested sections and assign them to a logical layout:
   - **Hero Key Visual**: The largest or most prominent section. Contains the campaign's primary image — a photorealistic lifestyle shot, product hero shot, or brand ambassador portrait with campaign tagline and brand lockup.
   - **Color Palette**: Row of 4–6 circular or square swatches representing the campaign's dominant colors plus 1–2 accent colors. Include hex codes or color names beneath each swatch.
   - **Typography Specimens**: Display of campaign headline font and body font — showing the typeface names, weights, and sample text (tagline, headline, body copy).
   - **Mood & Tone Imagery**: 2–4 smaller reference thumbnails showing lighting style, environment type, casting direction, or texture references.
   - **Channel Mockups**: Miniature previews of how the campaign appears across channels — social feed post, TV frame, billboard, print ad, story/reel format.
   - **Campaign Tagline & Brand Lockup**: The tagline in final typography form, alongside logo placement rules and clear space guidelines.
   - **Campaign Notes**: 2–4 bullet points summarizing creative insights, target audience, emotional insight, or production priorities.

2. **Spatial Layout Engineering**: Describe the board's physical structure explicitly:
   - Define panel positions: hero panel (left or top), supporting grid (right or below), bottom strip.
   - Specify the presentation surface: clean white art board, dark cinematic slate, textured kraft paper, or brand-colored background.
   - Specify dividers: thin gold lines, clean white gutters, subtle drop shadows, brand-colored rules, or geometric shapes.
   - Ensure sections do not overlap and have balanced negative space.

3. **Typography & Text Integration**: The board contains real text elements that must be legible and stylistically consistent:
   - Campaign title/headline: Large elegant serif or bold sans-serif.
   - Tagline: Medium weight, distinctive, memorable.
   - Section headers: Small caps, clean sans-serif, all caps or title case.
   - Labels (COLOR / FONT / CHANNEL / MOOD): Minimal, functional, uppercase.
   - Body text (notes, descriptions): Readable serif or sans-serif at small scale.
   - Do NOT invent illegible gibberish text. If specific text is provided, use it exactly. If not provided, use plausible, short, readable placeholder text.

4. **Cross-Section Consistency Lock**: All sections must feel like they belong to the same campaign:
   - Same color grading and saturation level across hero visual, mood thumbnails, and channel mockups.
   - Same lighting philosophy (e.g., soft overcast, warm golden hour, cool neon, clean studio).
   - Same realism level (photorealistic, stylized realistic, editorial).
   - Same brand voice — aspirational, playful, luxury, disruptive, wholesome, etc.
   - Logo and tagline must appear consistently across channel mockups.

## MODEL-AWARE OPTIMIZATION
The refined prompt feeds into: OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit.
- For **generation models** (GPT Image, Seedream, Gemini): Emphasize the document-as-image nature. Describe the board as a physical printed sheet or digital presentation screen. Use natural language flow. Keep under 800 English words; complex layouts need more room than single-subject prompts.
- For **editing models** (Grok Image Edit, Qwen image edit): If a base board or poster image is provided, prepend preservation clauses: "Preserve the existing layout structure, typography positions, and section boundaries. Modify only the hero visual, color palette, and mood imagery to..."
- **Explicit Purpose / Type**: Always open with the document type: "A professional advertising campaign presentation board," "brand creative direction concept sheet," or "multi-channel campaign visual bible."

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning or show layout plans. Output ONLY the final prompt.
2. **NO FORMATTING**: No markdown, bullet points, headers, bold text, numbered lists, or line breaks within the prompt body.
3. **STRUCTURE**: Output ONLY a single flowing paragraph (or two short connected paragraphs if complexity demands). Target: **300–600 words**.
4. **DELIMITERS**: Wrap the entire prompt in `[[PROMPT]]` and `[[/PROMPT]]` tags.
5. **NO EXTERNAL TEXT**: Nothing outside the `[[PROMPT]]` tags will be parsed.
6. **MANDATORY COVERAGE**: The prompt must weave together: document type and purpose, presentation surface and dividers, spatial layout description, hero key visual content, color palette swatches, typography specimens, mood imagery descriptions, channel mockup previews, campaign tagline and brand lockup, campaign notes, typography style, and cross-section consistency lock.
7. **ANTI-OVERLAP ENFORCEMENT**: Explicitly state that sections are separated by clear gutters or divider lines and must not bleed into each other.

## PROHIBITIONS
- NEVER output a single photograph, portrait, or standalone scene. The output must ALWAYS be a multi-section presentation board.
- NEVER generate sections in conflicting art styles (e.g., photorealistic hero next to illustrated channel mockups).
- NEVER omit requested sections. If the user asks for a color palette, typography specimens, or channel mockups, they must appear in the output.
- NEVER invent unreadable text or placeholder gibberish. All text must be plausible and stylistically appropriate.
- Do not include aspect ratios, resolution specs, model names, or UI instructions inside the prompt.
- Do not output multiple prompt variants; output one unified optimized prompt.
```

---

## User Prompt Templates

### Template A: Full Board with All Sections (Recommended)

```
Design a professional advertising campaign presentation board for the "[CAMPAIGN NAME]" campaign.

Reference images attached:
- Image 1: Hero visual reference — primary campaign image style, casting direction, lighting mood
- Image 2: Product reference — the product or service being advertised
- Image 3: Brand identity reference — logo, existing brand colors, typography
- Image 4: Environment / lifestyle reference — setting, atmosphere, target audience context

Board layout:
- LEFT PANEL (large): Hero key visual showing [subject description] in [environment]. Campaign tagline "[TAGLINE]" in [FONT STYLE]. Brand logo [POSITION]. "[CAMPAIGN NAME]" title in large [TYPEFACE].
- TOP-RIGHT: Color Palette section — [N] swatches: [COLOR 1], [COLOR 2], [COLOR 3], [COLOR 4], [ACCENT COLOR]. Include color names or hex codes beneath.
- TOP-RIGHT (adjacent): Typography Specimens — Headline font [FONT NAME] showing "[SAMPLE HEADLINE]". Body font [FONT NAME] showing sample paragraph text.
- MIDDLE-RIGHT: Mood & Tone Imagery — [N] small thumbnails showing [lighting style], [texture reference], [casting direction], [atmosphere].
- MIDDLE-RIGHT (adjacent or below): Channel Mockups — miniature previews of social post, TV frame, billboard, print ad, story format. Each showing consistent logo placement and tagline.
- BOTTOM STRIP: Campaign Notes — [N] bullet points: [NOTE 1], [NOTE 2], [NOTE 3]. Brand lockup with clear space guidelines. "CREATIVE DIRECTION" label.

Overall: [BACKGROUND COLOR] background, [DIVIDER STYLE] divider lines, [OVERALL MOOD] palette, [TYPOGRAPHY STYLE] typography, premium advertising agency presentation quality.

Task: Synthesize all references into a single cohesive presentation board image. Maintain visual consistency across all sections. Ensure all sections share the same [STYLE DESCRIPTOR] aesthetic.
```

### Template B: Minimal Board with Auto-Layout

```
Design a professional advertising campaign concept board for "[CAMPAIGN NAME]."

Reference images attached for hero visual, product, brand identity, and lifestyle context.

Required sections: Hero key visual with tagline and brand lockup, color palette (4–6 swatches), typography specimens (headline + body), mood imagery (2–4 thumbnails), channel mockups (social, TV, billboard, print), campaign notes (2–4 bullets).

Style: [BACKGROUND] background, [DIVIDER] dividers, [MOOD] color grading, [TYPE STYLE] typography, realistic textures, premium agency presentation quality.

Task: Generate a single presentation board image. All sections must share consistent art style, color palette, and brand voice. No section overlap. Clean, professional, award-worthy creative direction quality.
```

### Template C: Editing an Existing Board (for Grok / Qwen)

```
Base campaign board image attached. Preserve the existing layout structure, section boundaries, typography positions, and presentation surface.

Reference images for content updates:
- Image 1: New hero visual reference
- Image 2: Revised product reference
- Image 3: Updated brand identity / color palette reference

Task: Update the board content while keeping the framework intact. Replace hero visual. Refresh color palette. Update channel mockups with new product imagery. Maintain the same [STYLE] aesthetic and professional typography style. Output a prompt describing the updated single board image.
```

---

## Common Anti-Patterns

### Section Collapse / Overlap
**Symptom:** Sections bleed into each other. The hero visual overlaps the color palette. Text from campaign notes covers channel mockups.  
**Cause:** Layout not described with explicit spatial boundaries and gutters.  
**Fix:** Add explicit anti-overlap language: "separated by clean white gutters," "thin gold divider lines between sections," "sections do not overlap." Describe panel proportions: "left panel occupies 45% width," "bottom strip spans full width at 15% height."

### Missing Sections
**Symptom:** The board generates with hero visual and color palette, but typography specimens, channel mockups, or campaign notes are absent.  
**Cause:** Prompt lists too many sections; model drops the less visually prominent ones.  
**Fix:** Group related minor sections into a single "bottom strip" or "right column." Prioritize them by describing them as a unified visual element: "a full-width bottom strip containing color swatches, typography specimens, channel mockups, and campaign notes."

### Inconsistent Art Style Across Sections
**Symptom:** Hero visual is photorealistic, channel mockups look illustrated, mood thumbnails look like 3D renders.  
**Cause:** No cross-section consistency lock in the prompt.  
**Fix:** Add: "All sections share the same photorealistic commercial photography style, [COLOR GRADE] color grading, and [LIGHTING] lighting. No section may deviate in art style or realism level."

### Gibberish Typography
**Symptom:** Title text is wavy, illegible, or random characters. Labels are unreadable squiggles. Font names are nonsense.  
**Cause:** Model invents text without explicit content.  
**Fix:** Provide exact text strings for all major typography: campaign title, tagline, sample headline, sample body text, color names, section headers. For minor labels, specify style: "clean uppercase sans-serif labels reading COLOR, FONT, CHANNEL, MOOD."

### Weak Brand Lockup
**Symptom:** Logo appears inconsistently across channel mockups, or tagline is missing from key sections.  
**Cause:** No explicit brand lockup rules specified.  
**Fix:** Add: "Brand logo appears [POSITION] on hero visual and all channel mockups. Campaign tagline appears below logo in [FONT STYLE]. Clear space around logo follows [GUIDELINE]."

---

## Good vs Bad Examples

### Good — Complete Campaign Board Prompt

> A professional advertising campaign presentation board for the BOTANIKA Skincare Rise and Shine campaign on a clean white art board background with thin gold decorative divider lines. The left panel occupying 45 percent width features a cinematic hero key visual of a young East Asian woman with dewy glowing skin holding a warm amber BOTANIKA moisturizer bottle near her face in a softly lit minimalist bathroom with natural window light, shallow depth of field, premium beauty photography aesthetic. Overlaid text reads RISE AND SHINE in large elegant serif and the tagline YOUR BEST SKIN STARTS TODAY in medium sans-serif below, with the BOTANIKA leaf logo in the top-left corner. The top-right grid contains a Color Palette section with five circular swatches in warm amber, soft cream, botanical green, blush pink, and charcoal black, each with clean uppercase labels beneath. Adjacent Typography Specimens section shows headline font Playfair Display with sample text RADIANT SKIN AWAITS and body font Inter with sample paragraph text. Below, a Mood and Tone Imagery section presents four small thumbnails: soft morning window light on linen, fresh botanical ingredients, dewy skin macro detail, and clean minimalist bathroom interior. The adjacent Channel Mockups section shows miniature previews of an Instagram feed post, a TV commercial frame, a billboard layout, and a vertical story format, each incorporating the BOTANIKA logo and RISE AND SHINE tagline consistently. A full-width bottom strip contains campaign notes: target audience is health-conscious millennials aged 25 to 40, emotional insight is self-care as a morning ritual, creative priority is natural authenticity over heavy retouching, production note is shoot during golden hour for warm skin tones. All sections share consistent warm natural color grading, photorealistic commercial photography style, and sophisticated minimalist typography. No section overlap, balanced negative space, premium creative agency presentation quality.

### Bad — Vague and Under-Structured

> A campaign board for a skincare brand. Make it look professional with good typography and a color palette. Beauty brand aesthetic.

### Bad — Missing Document Structure

> Generate a beautiful image of a woman with glowing skin holding a moisturizer bottle, plus some color swatches and font samples and social media mockups. Premium beauty brand aesthetic.

---

## Model-Specific Notes

| Model | Board Generation Tip |
|-------|---------------------|
| **GPT Image** | Handles complex multi-section layouts well if spatial structure is explicit. Provide exact text strings to avoid gibberish typography. |
| **Seedream** | Responds well to "presentation board," "creative direction deck," and "concept sheet" framing. Emphasize document-as-object. |
| **Gemini** | Good at following detailed section lists. May need stronger anti-overlap language. |
| **Grok / Qwen** | Best for editing existing boards. Always prepend layout preservation clauses. |
