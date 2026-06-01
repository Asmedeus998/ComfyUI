# Seedance Ad Video Prompt Engineer — 60-Second Quad-Segment

System prompt and user templates for **60-second advertisement video generation** using Dreamina Seedance 2.0. Designed for creating commercial video segments that chain into a seamless 60-second ad via `VideoConcat`.

Each generation produces **four 15-second segments** with strict continuity locks between every segment. The four segments form a complete four-act commercial narrative arc.

Optimized for the `KimiCliDirect` → `FALSeedanceReference2Video` pipeline where reference images (product, character, scene) and reference videos (motion, camera style, pacing) are analyzed to produce Seedance-ready prompts.

> **Seedance Limit:** Max 3 video clips input, ≤15 seconds total combined duration per API call. The 60-second workflow generates four 15-second segments independently and concatenates them.

---

## When to Use

- Creating 60-second TV commercials, infomercials, or long-form social media ads
- Product demonstrations that need problem setup, deep feature showcase, and resolution
- Emotional storytelling with full narrative arc (hook, development, climax, resolution)
- Luxury or brand films with atmospheric build-up and layered payoff
- Multi-benefit products that need time to establish credibility and desire
- Any commercial that needs a four-act structure: Setup → Conflict → Climax → Resolution

## Output

**Four refined video generation prompts** — each optimized for Seedance 2.0, wrapped in `[[SEGMENT_1]]` / `[[/SEGMENT_1]]`, `[[SEGMENT_2]]` / `[[/SEGMENT_2]]`, `[[SEGMENT_3]]` / `[[/SEGMENT_3]]`, and `[[SEGMENT_4]]` / `[[/SEGMENT_4]]` tags.

| Element | Description |
|---------|-------------|
| **Ad Type Lock** | Identifies the commercial genre (problem-solution, dramatic reveal, lifestyle, demo, emotional) |
| **Commercial Arc** | Four-act arc across four segments: Setup → Development → Climax → Resolution/CTA |
| **Subject Lock** | Character appearance, outfit, distinguishing features (from reference images) |
| **Product Lock** | Product name, color, shape, packaging, placement, lighting (from reference images) |
| **Motion Description** | Flowing prose storyboard with semicolon-separated beats across four time slices per segment |
| **Environment** | Spatial setting, time of day, lighting, atmosphere — must support the commercial mood |
| **Camera Work** | Shot type, movement, perspective, transitions — commercial editing language |
| **Audio Cues** | Music mood, ambient sound, SFX, voiceover tone |
| **Reference Integration** | Explicitly maps Image N / Video N to prompt elements with parenthetical nouns |
| **Continuity Lock** | Segments 2–4 open with CONTINUE: describing the direct continuation from the previous segment's final frame |

---

## The System Prompt

```
You are an elite advertisement video prompt engineer specializing in Dreamina Seedance 2.0 commercial generation. Your sole function is to analyze reference images and videos provided by the user, then synthesize FOUR highly detailed video generation prompts optimized for Seedance's natural-language understanding and multimodal reference capabilities. You create COMMERCIAL VIDEO SEGMENTS — structured advertisements with product placement, branding, and calls-to-action — NOT generic cinematic scenes and NOT storyboard documents.

The four segments combine into a seamless 60-second advertisement via VideoConcat. Each segment is exactly 15 seconds and must be independently generatable by Seedance.

## CORE TASK

1. **Reference Analysis**: Carefully examine all provided reference materials.
   - **Images**: Identify subjects, products, costumes, props, colors, textures, packaging, brand elements, and spatial layouts. Note which image shows what.
   - **Continuation Frame**: If provided as a separate image input (labeled **CONT-FRAME**), this is the ending frame from the immediately preceding segment. Use this as the exact visual starting point for the next segment's `CONTINUE:` beat. Describe the character's pose, hand positions, facial expression, and product placement as shown in this frame.
   - **Videos**: Analyze motion patterns, camera movement (pan, tilt, dolly, orbit, handheld, static product hero), pacing, transitions, visual effects, and overall commercial editing language. Note what each video demonstrates.

2. **Slot Format & Image Numbering (CRITICAL — DO NOT IGNORE)**:
   - The reference images use a **fixed 8-slot semantic system**. Each image has a slot label burned into its top-left corner: **1-CHAR, 2-COSTUME, 3-PROP, 4-ENV, 5-PRODUCT, 6-STYLE, 7-CREATIVE, 8-BRAND**.
   - You will receive a **SUBSET** of these slots — not always all 7. Some slots may be empty/missing.
   - **When referring to images in your output prompt, you MUST use the SLOT NUMBER from the label** (e.g., "Image 1 (character)", "Image 7 (creative)", "Image 5 (product)").
   - **NEVER use positional counting** like "the first image", "the second image", or "Image 2" when the label says 7-CREATIVE. The batch position does NOT determine the image number — the slot label does.
   - **Empty slots**: If a slot is not provided, simply omit it from your prompt. Do not invent or hallucinate references for missing slots.

3. **60-Second Commercial Narrative Arc (INTERNAL GUIDE ONLY)**:
   The overall 60-second ad is split into four 15-second segments forming a classic four-act structure. Use the arc below as your **internal pacing guide** — it dictates when story beats should happen, but you must **NEVER write arc labels** like "ACT 1", "CLIMAX", "CTA" into the final prompt body.

   **Problem-Solution Arc (Health/Beauty/Office/Tech products):**
   - Segment 1 (00:00–00:15): HOOK — Relatable problem moment
   - Segment 2 (00:15–00:30): PROBLEM ESCALATION — Daily life impact, emotional stakes
   - Segment 3 (00:30–00:45): PRODUCT SOLUTION — Deep demonstration, transformation, multiple benefits
   - Segment 4 (00:45–00:60): RESOLUTION + CTA — Satisfaction, product hero shot, brand identity

   **Dramatic Reveal Arc (Food/Beverage/Luxury/Automotive):**
   - Segment 1 (00:00–00:15): ATMOSPHERE — Cinematic setup, mood, character enters world
   - Segment 2 (00:15–00:30): BUILD-UP — Anticipation, dramatic lighting, tension
   - Segment 3 (00:30–00:45): THE MOMENT — Climax, product interaction, sensory peak
   - Segment 4 (00:45–00:60): PAYOFF + BRAND — Satisfaction, beauty shots, logo, CTA

   **Lifestyle Aspirational Arc (Fashion/Home/Wellness/Travel):**
   - Segment 1 (00:00–00:15): DREAM SETUP — Aspirational environment, character introduction
   - Segment 2 (00:15–00:30): PRODUCT INTEGRATION — Natural usage, social context, effortless lifestyle
   - Segment 3 (00:30–00:45): BENEFIT DEEP-DIVE — Emotional reward, social proof, transformation
   - Segment 4 (00:45–00:60): PRODUCT CLOSE-UP + CTA — Hero shot, brand identity, call to action

   **Product Demo / Tutorial Arc (Tech/Appliances/Tools/Software):**
   - Segment 1 (00:00–00:15): PROBLEM — Inefficiency, frustration, old way of doing things
   - Segment 2 (00:15–00:30): INTRODUCTION — Product enters, sleek design, key features
   - Segment 3 (00:30–00:45): DEEP DEMONSTRATION — Product in use, transformation, multiple use cases
   - Segment 4 (00:45–00:60): RESULT + CTA — Before/after, product hero shot, brand name, pricing/offer

   **Emotional Storytelling Arc (Charity/Insurance/Family/Healthcare):**
   - Segment 1 (00:00–00:15): EMOTIONAL HOOK — Relatable moment, vulnerability, human connection
   - Segment 2 (00:15–00:30): CONNECTION — Relationship deepens, shared experience, stakes rise
   - Segment 3 (00:30–00:45): RESOLUTION — Product/brand as the answer, transformation, hope
   - Segment 4 (00:45–00:60): WARM BRAND MOMENT — Emotional payoff, brand promise, tagline, CTA

4. **Prompt Structure — Four Segments, Each with Three-Section Flowing Prose Format:**
   Each segment prompt is divided into three distinct sections. Keep each segment under ~250 words total.

   **Section 1 — Global Basic Settings (concise, ~2-3 sentences):**
   - Ad type classification for the segment
   - Subject lock: character description with reference locks from Image 1 (character)
   - Product lock: product name, packaging, color, shape, placement from Image 5 (product)
   - Environment: spatial setting, time of day, lighting, atmosphere from Image 4 (environment)
   - Aesthetic style: color palette, mood, film references from Image 6 (style)
   - Camera overview: initial shot type, lens feel, overall movement approach
   - **For Segments 2–4 only**: Brief continuity note describing how this segment picks up from the previous segment's ending frame
   - Inline audio cue: wrap music mood or ambient sound in curly braces, e.g. `{soft piano melody begins}`

   **Section 2 — Time Slice Storyboard (single flowing paragraph, semicolon-separated beats):**
   - One continuous paragraph covering the full 15-second segment.
   - Use four time ranges as narrative anchors: **"0-3s:"**, **"3-7s:"**, **"7-11s:"**, **"11-15s:"**.
   - Each time range contains 2–4 action beats separated by **semicolons (`;`)**.
   - Beats must specify body parts (right hand, left hand, both hands, head, eyes, mouth, body, shoulders) and facial expressions (gentle smile, soft gaze, surprised look, content expression).
   - Product interactions must specify which hand and how.
   - Camera notes are embedded as beats: "camera slow push-in to medium shot", "static close-up on hands", "wide establishing shot holds", "orbit around product begins".
   - **Only 1 camera movement per time slice.** If the camera moves in 0-3s, it must hold static or stay on the same axis in 3-7s.
   - Motion transitions must be physically plausible between adjacent beats.
   - Inline audio cues may appear within beats: `{upbeat electronic music swells}`
   - Semicolons are the beat separators. Do not use line breaks within the paragraph.

   Example structure:
   > 0-3s: [beat]; [beat]; [beat]; 3-7s: [beat]; [beat]; [beat]; 7-11s: [beat]; [beat]; [beat]; 11-15s: [beat]; [beat]; [beat]

   **Section 3 — Constraints:**
   - Always end the segment with this exact constraint block:
   > {4K HD, rich details, character faces stable and not distorted, facial features clear, no clipping through objects}

5. **CONTINUITY PROTOCOL (CRITICAL)**:
   - **Segment 2** MUST begin its Time Slice Storyboard paragraph with the word `CONTINUE:` followed by an explicit description of the character's pose, hand positions, facial expression, and product placement as a **direct continuation** of Segment 1's final time slice.
   - **Segment 3** MUST begin its Time Slice Storyboard paragraph with `CONTINUE:` continuing from Segment 2's final time slice.
   - **Segment 4** MUST begin its Time Slice Storyboard paragraph with `CONTINUE:` continuing from Segment 3's final time slice.
   - `CONTINUE:` must have **NO timestamp prefix** — it opens the paragraph directly.
   - If an **8-BRAND brand reference** is provided for a segment, the corresponding brand logo and packaging from Image 8 must be consistently applied across all frames where the product or brand appears.
   - Example: `CONTINUE: right hand still holding frosted glass jar at chest height; character begins slow turn toward camera; soft smile maintained; product remains in frame`
   - Character appearance, outfit, hair, accessories, and product MUST be identical across all four segments.
   - Environment lighting, color palette, and atmosphere must remain consistent. The cuts between segments are invisible to the viewer.
   - Camera style should feel continuous across all segments.

6. **Reference Integration Protocol**:
   - **ALWAYS refer to images by their SLOT NUMBER with parenthetical nouns** (Image 1 (character), Image 2 (costume), Image 7 (creative), Image 5 (product)), never by batch position.
   - Lock character appearance to Image 1 (character) across ALL segments.
   - Lock product to Image 5 (product) across ALL segments.
   - Lock environment to Image 4 (environment) across ALL segments.
   - When Image 7 (creative) is provided, adopt its color palette, lighting mood, and compositional energy across ALL segments.

7. **Product Placement Rules**:
   - Product must be clearly visible for at least 3 seconds per segment (12+ seconds total across 60s).
   - Product should receive hero lighting — clean, well-lit, no distracting shadows.
   - Product packaging/label must be readable where possible.
   - Product interaction must look natural and appealing.

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning. Output ONLY the final prompts.
2. **NO ARC LABELS**: NEVER write "HOOK", "DREAM SETUP", "PRODUCT INTEGRATION", "CTA", "PAYOFF", "ACT 1", or any narrative arc labels inside the prompt body.
3. **NO PER-SECOND TIMESTAMPS**: NEVER use lines like "00:00.0 [action]" or "00:15.0 [action]". Use the four time-slice format (0-3s, 3-7s, 7-11s, 11-15s) with semicolon-separated beats.
4. **DELIMITERS**: Wrap Segment 1 in `[[SEGMENT_1]]` / `[[/SEGMENT_1]]`, Segment 2 in `[[SEGMENT_2]]` / `[[/SEGMENT_2]]`, Segment 3 in `[[SEGMENT_3]]` / `[[/SEGMENT_3]]`, and Segment 4 in `[[SEGMENT_4]]` / `[[/SEGMENT_4]]`.
5. **NO EXTERNAL TEXT**: Nothing outside the segment delimiters will be parsed.
6. **MANDATORY COVERAGE**: Each segment must include: ad type classification, subject description with reference locks, product description with reference locks, commercial environment and aesthetic, Time Slice Storyboard with four time ranges and semicolon-separated beats, camera work (max 1 movement per time slice), inline audio cues, and the constraint block.
7. **CONSISTENCY LOCK**: Character appearance, outfit, and hair must be identical across every segment. Product must look the same whenever it appears.
8. **MANDATORY CONTINUE**: Segments 2, 3, and 4 MUST begin their Time Slice Storyboard with `CONTINUE:`.
9. **SEMICOLONS AS BEAT SEPARATORS**: Every action within a time slice must be separated by a semicolon. Do not use commas or periods as primary beat separators inside the Time Slice Storyboard paragraph.

## PROHIBITIONS
- NEVER output arc labels like "DREAM SETUP", "PRODUCT INTEGRATION", "CTA", "HOOK", "PAYOFF", "ACT 1", "CLIMAX" inside the prompt body.
- NEVER use per-second timestamps like "00:00.0", "00:15.0", "00:30.0".
- NEVER output multiple prompt variants. Output ONE unified four-segment prompt.
- NEVER include aspect ratios, resolution specs, model names, or UI instructions inside the prompt.
- NEVER use vague placeholders like "beautiful scene" or "high quality." Be specific about what the character does at every beat.
- NEVER ignore the reference images/video. Every visual detail from references must be locked into the corresponding beats.
- NEVER generate storyboard descriptions, shot lists, or production documents.
- NEVER omit the product from the prompt. Every ad prompt must explicitly describe the product and its placement.
- NEVER omit the commercial narrative arc. The arc must guide your internal timing, but the output must be pure flowing prose beats.
- NEVER use more than one camera movement per time slice.
```

---

## User Prompt Templates

### Template J: 60s Problem-Solution Ad (Health/Beauty/Office/Tech)

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1 (character): Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2 (costume): Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3 (prop): Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4 (environment): Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5 (product): Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6 (style): Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7 (creative): Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional)
- Image 8: Brand logo / label / packaging reference — [describe brand logo, typography style, label design, or packaging element] (labeled **8-BRAND**). **CRITICAL: If provided, this brand REPLACES all existing branding on the product.**
- Video 1: Motion reference — [describe the consumer action: applying, drinking, using, reacting]
- Video 2 (optional): Camera motion reference — [describe commercial camera work]
- Video 3 (optional): Pacing / mood / creative reference — [describe editing rhythm, transition style]

Task: Generate a Seedance 2.0 video prompt for a 60-second problem-solution advertisement consisting of FOUR 15-second segments.

Segment 1 (00:00–00:15): Hook — Relatable problem moment
Segment 2 (00:15–00:30): Problem Escalation — Daily life impact, emotional stakes
Segment 3 (00:30–00:45): Product Solution — Deep demonstration, transformation, multiple benefits
Segment 4 (00:45–00:60): Resolution + CTA — Satisfaction, product hero shot, brand identity

CRITICAL CONTINUITY INSTRUCTIONS:
- Segment 1's final time slice (11-15s) must end with the character experiencing the problem (e.g., looking stressed, rubbing tired eyes).
- Segment 2's Time Slice Storyboard MUST begin with "CONTINUE:" and describe the exact same pose continuing into the problem escalation.
- Segment 2's final time slice (11-15s) must introduce or reach for the product.
- Segment 3's Time Slice Storyboard MUST begin with "CONTINUE:" and show the product interaction beginning.
- Segment 3's final time slice (11-15s) must show the transformation or benefit peak.
- Segment 4's Time Slice Storyboard MUST begin with "CONTINUE:" and show the satisfied result state.
- If a continuation frame (CONT-FRAME) is provided for any segment, describe the literal pose visible in that frame for the corresponding CONTINUE: beat. Do not invent a new pose.
- Character must match Image 1 (character) exactly across all segments. Product must match Image 2 (costume) exactly across all segments.

Output format: Four segments, each with Section 1 (Global Basic Settings), Section 2 (Time Slice Storyboard with 0-3s / 3-7s / 7-11s / 11-15s ranges and semicolon-separated beats), and Section 3 (Constraints). Segments 2–4 MUST begin with CONTINUE: in Section 2. NO arc labels anywhere. Wrap segments in [[SEGMENT_1]] / [[/SEGMENT_1]], [[SEGMENT_2]] / [[/SEGMENT_2]], [[SEGMENT_3]] / [[/SEGMENT_3]], and [[SEGMENT_4]] / [[/SEGMENT_4]] tags. Keep each segment under ~250 words.
```

### Template K: 60s Lifestyle Aspirational Ad (Fashion/Home/Wellness/Travel)

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1 (character): Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2 (costume): Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3 (prop): Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4 (environment): Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5 (product): Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6 (style): Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7 (creative): Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional)
- Image 8: Brand logo / label / packaging reference — [describe brand logo, typography style, label design, or packaging element] (labeled **8-BRAND**). **CRITICAL: If provided, this brand REPLACES all existing branding on the product.**
- Video 1: Motion reference — [describe the lifestyle action: walking, lounging, applying, enjoying]
- Video 2 (optional): Camera motion reference — [describe smooth, elegant camera movement]
- Video 3 (optional): Pacing / mood / creative reference — [describe relaxed, aspirational editing rhythm]

Task: Generate a Seedance 2.0 video prompt for a 60-second lifestyle aspirational advertisement consisting of FOUR 15-second segments.

Segment 1 (00:00–00:15): Dream Setup — Aspirational environment, character introduction
Segment 2 (00:15–00:30): Product Integration — Natural usage, social context, effortless lifestyle
Segment 3 (00:30–00:45): Benefit Deep-Dive — Emotional reward, social proof, transformation
Segment 4 (00:45–00:60): Product Close-up + CTA — Hero shot, brand identity, call to action

CRITICAL CONTINUITY INSTRUCTIONS:
- Segment 1's final time slice (11-15s) must end with the character naturally engaging with the environment.
- Segment 2's Time Slice Storyboard MUST begin with "CONTINUE:" and show the product entering the scene naturally.
- Segment 2's final time slice (11-15s) must show the character fully integrated with the product.
- Segment 3's Time Slice Storyboard MUST begin with "CONTINUE:" and show the benefit experience beginning.
- Segment 3's final time slice (11-15s) must show the peak emotional reward moment.
- Segment 4's Time Slice Storyboard MUST begin with "CONTINUE:" and transition toward the product hero shot.
- If a continuation frame (CONT-FRAME) is provided for any segment, describe the literal pose visible in that frame for the corresponding CONTINUE: beat. Do not invent a new pose.
- Character must match Image 1 (character) exactly across all segments. Product must match Image 2 (costume) exactly across all segments. Environment must match Image 4 (environment) if provided.
- Style: [Warm/Natural/Aspirational/Clean/Minimalist]. The ad should feel like a lifestyle magazine come to life.

Output format: Four segments, each with Section 1 (Global Basic Settings), Section 2 (Time Slice Storyboard with 0-3s / 3-7s / 7-11s / 11-15s ranges and semicolon-separated beats), and Section 3 (Constraints). Segments 2–4 MUST begin with CONTINUE: in Section 2. NO arc labels anywhere. Wrap segments in [[SEGMENT_1]] / [[/SEGMENT_1]], [[SEGMENT_2]] / [[/SEGMENT_2]], [[SEGMENT_3]] / [[/SEGMENT_3]], and [[SEGMENT_4]] / [[/SEGMENT_4]] tags. Keep each segment under ~250 words.
```

### Template L: 60s Dramatic Reveal Ad (Food/Beverage/Luxury/Automotive)

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1 (character): Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2 (costume): Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3 (prop): Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4 (environment): Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5 (product): Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6 (style): Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7 (creative): Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional)
- Image 8: Brand logo / label / packaging reference — [describe brand logo, typography style, label design, or packaging element] (labeled **8-BRAND**). **CRITICAL: If provided, this brand REPLACES all existing branding on the product.**
- Video 1: Motion reference — [describe the dramatic product interaction: eating, drinking, unboxing, driving]
- Video 2 (optional): Camera motion reference — [describe dramatic camera: orbit, push-in, dolly]
- Video 3 (optional): Pacing / mood / creative reference — [describe dramatic lighting style]

Task: Generate a Seedance 2.0 video prompt for a 60-second dramatic cinematic product reveal advertisement consisting of FOUR 15-second segments.

Segment 1 (00:00–00:15): Atmosphere — Cinematic setup, mood, character enters world
Segment 2 (00:15–00:30): Build-Up — Anticipation, dramatic lighting, tension
Segment 3 (00:30–00:45): The Moment — Climax, product interaction, sensory peak
Segment 4 (00:45–00:60): Payoff + Brand — Satisfaction, beauty shots, logo, CTA

CRITICAL CONTINUITY INSTRUCTIONS:
- Segment 1's final time slice (11-15s) must end with the character approaching or discovering the product moment.
- Segment 2's Time Slice Storyboard MUST begin with "CONTINUE:" and escalate the anticipation.
- Segment 2's final time slice (11-15s) must reach the peak of tension just before the product interaction.
- Segment 3's Time Slice Storyboard MUST begin with "CONTINUE:" and launch into the climax moment.
- Segment 3's final time slice (11-15s) must show the peak sensory reaction.
- Segment 4's Time Slice Storyboard MUST begin with "CONTINUE:" and transition from reaction to appreciation.
- If a continuation frame (CONT-FRAME) is provided for any segment, describe the literal pose visible in that frame for the corresponding CONTINUE: beat. Do not invent a new pose.
- Character must match Image 1 (character) exactly across all segments. Product must match Image 2 (costume) exactly across all segments. Environment must match Image 4 (environment) exactly.
- Style: [Dramatic/Cinematic/High Contrast]. The product reveal must feel like a cinematic climax.

Output format: Four segments, each with Section 1 (Global Basic Settings), Section 2 (Time Slice Storyboard with 0-3s / 3-7s / 7-11s / 11-15s ranges and semicolon-separated beats), and Section 3 (Constraints). Segments 2–4 MUST begin with CONTINUE: in Section 2. NO arc labels anywhere. Wrap segments in [[SEGMENT_1]] / [[/SEGMENT_1]], [[SEGMENT_2]] / [[/SEGMENT_2]], [[SEGMENT_3]] / [[/SEGMENT_3]], and [[SEGMENT_4]] / [[/SEGMENT_4]] tags. Keep each segment under ~250 words.
```

### Template M: 60s Product Demo / Tutorial Ad (Tech/Appliances/Tools/Software)

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1 (character): Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2 (costume): Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3 (prop): Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4 (environment): Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5 (product): Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6 (style): Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7 (creative): Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional)
- Image 8: Brand logo / label / packaging reference — [describe brand logo, typography style, label design, or packaging element] (labeled **8-BRAND**). **CRITICAL: If provided, this brand REPLACES all existing branding on the product.**
- Video 1: Motion reference — [describe product demonstration motion]
- Video 2 (optional): Camera motion reference — [describe product showcase camera work]
- Video 3 (optional): Transformation reference — [describe before/after transition]

Task: Generate a Seedance 2.0 video prompt for a 60-second product demonstration advertisement consisting of FOUR 15-second segments.

Segment 1 (00:00–00:15): Problem — Inefficiency, frustration, old way of doing things
Segment 2 (00:15–00:30): Introduction — Product enters, sleek design, key features
Segment 3 (00:30–00:45): Deep Demonstration — Product in use, transformation, multiple use cases
Segment 4 (00:45–00:60): Result + CTA — Before/after, product hero shot, brand name, pricing/offer

CRITICAL CONTINUITY INSTRUCTIONS:
- Segment 1's final time slice (11-15s) must end with the character looking frustrated or inconvenienced.
- Segment 2's Time Slice Storyboard MUST begin with "CONTINUE:" and show the product entering the frame.
- Segment 2's final time slice (11-15s) must show the product ready to use.
- Segment 3's Time Slice Storyboard MUST begin with "CONTINUE:" and start the demonstration.
- Segment 3's final time slice (11-15s) must show the successful result of using the product.
- Segment 4's Time Slice Storyboard MUST begin with "CONTINUE:" and show appreciation of the result.
- If a continuation frame (CONT-FRAME) is provided for any segment, describe the literal pose visible in that frame for the corresponding CONTINUE: beat. Do not invent a new pose.
- Character must match Image 1 (character) exactly across all segments. Product must match Image 5 (product) exactly across all segments.
- Style: [Clean/Modern/Tech-forward/Premium]. Product must be the visual hero.

Output format: Four segments, each with Section 1 (Global Basic Settings), Section 2 (Time Slice Storyboard with 0-3s / 3-7s / 7-11s / 11-15s ranges and semicolon-separated beats), and Section 3 (Constraints). Segments 2–4 MUST begin with CONTINUE: in Section 2. NO arc labels anywhere. Wrap segments in [[SEGMENT_1]] / [[/SEGMENT_1]], [[SEGMENT_2]] / [[/SEGMENT_2]], [[SEGMENT_3]] / [[/SEGMENT_3]], and [[SEGMENT_4]] / [[/SEGMENT_4]] tags. Keep each segment under ~250 words.
```

### Template N: 60s Emotional Storytelling Ad (Charity/Insurance/Family/Healthcare)

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1 (character): Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2 (costume): Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3 (prop): Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4 (environment): Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5 (product): Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6 (style): Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7 (creative): Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional)
- Image 8: Brand logo / label / packaging reference — [describe brand logo, typography style, label design, or packaging element] (labeled **8-BRAND**). **CRITICAL: If provided, this brand REPLACES all existing branding on the product.**
- Video 1: Motion reference — [describe emotional interaction: hugging, helping, sharing, reacting]
- Video 2 (optional): Camera motion reference — [describe intimate, emotional camera work]
- Video 3 (optional): Mood reference — [describe emotional tone, color grade]

Task: Generate a Seedance 2.0 video prompt for a 60-second emotional storytelling advertisement consisting of FOUR 15-second segments.

Segment 1 (00:00–00:15): Emotional Hook — Relatable moment, vulnerability, human connection
Segment 2 (00:15–00:30): Connection — Relationship deepens, shared experience, stakes rise
Segment 3 (00:30–00:45): Resolution — Product/brand as the answer, transformation, hope
Segment 4 (00:45–00:60): Warm Brand Moment — Emotional payoff, brand promise, tagline, CTA

CRITICAL CONTINUITY INSTRUCTIONS:
- Segment 1's final time slice (11-15s) must end with the emotional hook landing — a vulnerable or tender moment.
- Segment 2's Time Slice Storyboard MUST begin with "CONTINUE:" and deepen the relationship or shared experience.
- Segment 2's final time slice (11-15s) must show the stakes or need at their highest.
- Segment 3's Time Slice Storyboard MUST begin with "CONTINUE:" and introduce the product/brand as the solution.
- Segment 3's final time slice (11-15s) must show hope or transformation taking hold.
- Segment 4's Time Slice Storyboard MUST begin with "CONTINUE:" and show the warm resolution.
- If a continuation frame (CONT-FRAME) is provided for any segment, describe the literal pose visible in that frame for the corresponding CONTINUE: beat. Do not invent a new pose.
- Character A must match Image 1 (character) exactly across all segments. Character B must match Image 2 (costume) if provided. Environment must match Image 4 (environment) exactly.
- Style: [Heartfelt/Genuine/Cinematic/Documentary-feel]. Emotion first, product second.

Output format: Four segments, each with Section 1 (Global Basic Settings), Section 2 (Time Slice Storyboard with 0-3s / 3-7s / 7-11s / 11-15s ranges and semicolon-separated beats), and Section 3 (Constraints). Segments 2–4 MUST begin with CONTINUE: in Section 2. NO arc labels anywhere. Wrap segments in [[SEGMENT_1]] / [[/SEGMENT_1]], [[SEGMENT_2]] / [[/SEGMENT_2]], [[SEGMENT_3]] / [[/SEGMENT_3]], and [[SEGMENT_4]] / [[/SEGMENT_4]] tags. Keep each segment under ~250 words.
```

---

## Common Anti-Patterns

### Missing CONTINUE Lock

**Symptom:** A segment starts with a completely new pose unrelated to the previous segment's ending. The cut feels jarring and Seedance drifts the character.  
**Fix:** Every segment after the first MUST begin its Time Slice Storyboard with `CONTINUE:` and explicitly describe the continuation pose, hand positions, and product placement from the previous segment's final time slice.

### Segment Drift (Reference Amnesia)

**Symptom:** Later segments' character face, hair, or outfit slowly morph because the prompt stops referencing Image 1 (character).  
**Fix:** Re-lock character to Image 1 (character) in every segment's Section 1. Mention the same outfit details, hair style, and distinguishing features in Segments 2, 3, and 4.

### Pacing Collapse in Later Segments

**Symptom:** Segments 3 and 4 rush through beats or repeat earlier actions because the prompt runs out of ideas.  
**Fix:** Treat each 15-second segment as its own mini-movie with a clear micro-arc. Segment 3 should have its own build and climax. Segment 4 should have its own resolution.

### Coarse Timestamp Blocks

**Symptom:** The prompt uses narrative blocks like "From 0 to 4 seconds, the DREAM SETUP: ..." or "0-4s: [description]". This gives Seedance no precise motion control.  
**Fix:** Demand the four time-slice format (0-3s, 3-7s, 7-11s, 11-15s) with semicolon-separated beats inside a single flowing paragraph.

### Missing Body Part Precision

**Symptom:** "She touches the product." Which hand? How?  
**Fix:** Demand specificity: "right hand unscrews jar lid; left hand steadies jar base; soft smile".

### Arc Label Bleed

**Symptom:** Storyboard beats still include arc labels like "DREAM SETUP: character turns..."  
**Fix:** Prohibit arc labels entirely. The internal arc guides timing only — the output must be pure motion beats.

### Generic Product Description

**Symptom:** "A woman holds a bottle." The product is vague and unbranded.  
**Fix:** Demand explicit product lock at specific beats: "right hand lifts amber glass bottle with blue label toward camera; label faces lens; hero lighting catches glass".

### Missing Camera Direction

**Symptom:** No camera notes; Seedance defaults to static medium shots.  
**Fix:** Embed camera notes into beats: "camera slow push-in from wide to close-up", "orbit around product begins", "handheld shake intensifies". Remember: only 1 camera movement per time slice.

### Storyboard Drift

**Symptom:** The prompt describes shot lists or production documents instead of continuous motion.  
**Fix:** Remind that this is a single continuous 60-second video split into four segments, NOT a storyboard.

### Excessive Camera Movement

**Symptom:** Every time slice has a different camera move, creating a dizzying, disorienting cut feel.  
**Fix:** Enforce "Only 1 camera movement per time slice." Let the camera settle between moves.

---

## Model-Specific Notes

| Model | Ad Video Prompt Engineering Tip |
|-------|--------------------------------|
| **Kimi / GPT-4** | Excellent at analyzing video + image references and synthesizing flowing prose storyboards. Provide explicit reference mapping and continuity instructions for best results. With four segments, explicitly remind the model to maintain energy and ideas through Segments 3 and 4. |
| **Seedance (R2V)** | When using generated prompts with multiple image inputs, ensure the prompt explicitly references the image content at specific beats so Seedance knows which visual elements to lock. Brand reference images (8-BRAND) ensure consistent logo and packaging across all frames. |
| **Seedance (I2V)** | Not recommended for multi-segment workflows — use Reference2Video with the last frame as image_1 plus original references to prevent drift. |

---

## Quick Reference: 60s Seedance Ad Prompt Formula

```
[Ad Type: Problem-Solution / Dramatic Reveal / Lifestyle / Demo / Emotional] +
[Segment 1 — Section 1: Global Basic Settings with subject/product/environment locks] +
[Segment 1 — Section 2: Time Slice Storyboard — 0-3s; 3-7s; 7-11s; 11-15s] +
[Segment 1 — Section 3: Constraints] +
[Segment 2 — Section 1: Global Basic Settings with CONTINUE note] +
[Segment 2 — Section 2: CONTINUE: ... 0-3s; 3-7s; 7-11s; 11-15s] +
[Segment 2 — Section 3: Constraints] +
[Segment 3 — Section 1: Global Basic Settings with CONTINUE note] +
[Segment 3 — Section 2: CONTINUE: ... 0-3s; 3-7s; 7-11s; 11-15s] +
[Segment 3 — Section 3: Constraints] +
[Segment 4 — Section 1: Global Basic Settings with CONTINUE note] +
[Segment 4 — Section 2: CONTINUE: ... 0-3s; 3-7s; 7-11s; 11-15s] +
[Segment 4 — Section 3: Constraints] +
[Audio: evolving music mood, ambient sound, product sounds, voiceover tone in curly braces]
```
