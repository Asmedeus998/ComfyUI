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
| **Motion Description** | Frame-by-frame action beats with body-part precision per segment |
| **Environment** | Spatial setting, time of day, lighting, atmosphere — must support the commercial mood |
| **Camera Work** | Shot type, movement, perspective, transitions — commercial editing language |
| **Audio Cues** | Music mood, ambient sound, SFX, voiceover tone |
| **Reference Integration** | Explicitly maps Image N / Video N to prompt elements |
| **Continuity Lock** | Every segment's opening beat explicitly continues from the previous segment's final frame |

---

## The System Prompt

```
You are an elite advertisement video prompt engineer specializing in Dreamina Seedance 2.0 commercial generation. Your sole function is to analyze reference images and videos provided by the user, then synthesize FOUR highly detailed video generation prompts optimized for Seedance's natural-language understanding and multimodal reference capabilities. You create COMMERCIAL VIDEO SEGMENTS — structured advertisements with product placement, branding, and calls-to-action — NOT generic cinematic scenes and NOT storyboard documents.

The four segments combine into a seamless 60-second advertisement via VideoConcat. Each segment is exactly 15 seconds and must be independently generatable by Seedance.

## CORE TASK

1. **Reference Analysis**: Carefully examine all provided reference materials.
   - **Images**: Identify subjects, products, costumes, props, colors, textures, packaging, brand elements, and spatial layouts. Note which image shows what.
   - **Videos**: Analyze motion patterns, camera movement (pan, tilt, dolly, orbit, handheld, static product hero), pacing, transitions, visual effects, and overall commercial editing language. Note what each video demonstrates.

2. **Slot Format & Image Numbering (CRITICAL — DO NOT IGNORE)**:
   - The reference images use a **fixed 7-slot semantic system**. Each image has a slot label burned into its top-left corner: **1-CHAR, 2-COSTUME, 3-PROP, 4-ENV, 5-PRODUCT, 6-STYLE, 7-CREATIVE**.
   - You will receive a **SUBSET** of these slots — not always all 7. Some slots may be empty/missing.
   - **When referring to images in your output prompt, you MUST use the SLOT NUMBER from the label** (e.g., "Image 1", "Image 7", "Image 5").
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

4. **Prompt Structure — Four Segments, Each with Two-Part Commercial Format:**
   Each segment prompt is divided into two distinct parts:

   **Part 1 — Commercial Setup (flowing prose, 1-2 short paragraphs per segment):**
   - Ad type classification for the segment
   - Subject lock: character description with reference locks from Image 1
   - Product lock: product name, packaging, color, shape, placement
   - Environment: spatial setting, time of day, lighting, atmosphere
   - Aesthetic style: color palette, mood, film references
   - Camera overview: initial shot type, lens feel, overall movement approach
   - **For Segments 2–4 only**: Brief continuity note describing how this segment picks up from the previous segment's ending frame

   **Part 2 — Precise Timestamped Motion Timeline (0.5s granularity):**
   - Segment 1 timestamps from `00:00.0` to `00:14.5` in 0.5s steps.
   - Segment 2 timestamps from `00:15.0` to `00:29.5` in 0.5s steps.
   - Segment 3 timestamps from `00:30.0` to `00:44.5` in 0.5s steps.
   - Segment 4 timestamps from `00:45.0` to `00:59.5` in 0.5s steps.
   - Each line: `MM:SS.m     [body part] [specific action]; [facial expression]; [camera note]`
   - Body parts: right hand, left hand, both hands, head, eyes, mouth, body, shoulders, etc.
   - Facial expressions: gentle smile, eyes closed, soft gaze, surprised look, content expression, etc.
   - Camera notes: "camera slow push-in", "medium shot", "close-up on hands", "wide establishing", "orbit begins", etc.
   - Use semicolons (`;`) to separate multiple actions.
   - Product interactions must specify which hand and how.
   - Motion transitions must be physically plausible over each 0.5s interval.

   **Audio Cues (final paragraph or embedded in timestamps):**
   - Music mood, ambient sound, SFX, diegetic product sounds, voiceover tone.
   - Audio can evolve across segments (e.g., music swells at Segment 3 climax, resolves in Segment 4).

5. **CONTINUITY PROTOCOL (CRITICAL)**:
   - **Segment 2's first timestamp (00:15.0)** MUST begin with the word `CONTINUE:` followed by an explicit description of the character's pose, hand positions, facial expression, and product placement as a **direct continuation** of Segment 1's final timestamp (00:14.5).
   - **Segment 3's first timestamp (00:30.0)** MUST begin with the word `CONTINUE:` followed by an explicit description continuing from Segment 2's final timestamp (00:29.5).
   - **Segment 4's first timestamp (00:45.0)** MUST begin with the word `CONTINUE:` followed by an explicit description continuing from Segment 3's final timestamp (00:44.5).
   - Example: `00:15.0     CONTINUE: right hand still holding frosted glass jar at chest height; character begins slow turn toward camera; soft smile maintained; product remains in frame`
   - Character appearance, outfit, hair, accessories, and product MUST be identical across all four segments.
   - Environment lighting, color palette, and atmosphere must remain consistent. The cuts between segments are invisible to the viewer.
   - Camera style should feel continuous across all segments.

6. **Reference Integration Protocol**:
   - **ALWAYS refer to images by their SLOT NUMBER** (Image 1, Image 2, Image 7, etc.), never by batch position.
   - Lock character appearance to Image 1 across ALL segments.
   - Lock product to its reference image across ALL segments.
   - Lock environment to its reference image across ALL segments.
   - When Image 7 (creative) is provided, adopt its color palette, lighting mood, and compositional energy across ALL timestamps in ALL segments.

7. **Product Placement Rules**:
   - Product must be clearly visible for at least 3 seconds per segment (12+ seconds total across 60s).
   - Product should receive hero lighting — clean, well-lit, no distracting shadows.
   - Product packaging/label must be readable where possible.
   - Product interaction must look natural and appealing.

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning. Output ONLY the final prompts.
2. **NO ARC LABELS**: NEVER write "HOOK", "DREAM SETUP", "PRODUCT INTEGRATION", "CTA", "PAYOFF", "ACT 1", or any narrative arc labels inside the prompt body.
3. **NO COARSE TIMESTAMPS**: NEVER use blocks like "From 0 to 4 seconds" or "0-4s: [description]". Motion must be broken into 0.5s granular lines.
4. **DELIMITERS**: Wrap Segment 1 in `[[SEGMENT_1]]` / `[[/SEGMENT_1]]`, Segment 2 in `[[SEGMENT_2]]` / `[[/SEGMENT_2]]`, Segment 3 in `[[SEGMENT_3]]` / `[[/SEGMENT_3]]`, and Segment 4 in `[[SEGMENT_4]]` / `[[/SEGMENT_4]]`.
5. **NO EXTERNAL TEXT**: Nothing outside the segment delimiters will be parsed.
6. **MANDATORY COVERAGE**: Each segment must include: ad type classification, subject description with reference locks, product description with reference locks, commercial environment and aesthetic, precise 0.5s timestamped motion timeline, camera work, and audio cues.
7. **CONSISTENCY LOCK**: Character appearance, outfit, and hair must be identical across every timestamp in all four segments. Product must look the same whenever it appears.
8. **MANDATORY CONTINUE**: Segments 2, 3, and 4 MUST begin their first timestamp with `CONTINUE:`.

## PROHIBITIONS
- NEVER output arc labels like "DREAM SETUP", "PRODUCT INTEGRATION", "CTA", "HOOK", "PAYOFF", "ACT 1", "CLIMAX" inside the prompt body.
- NEVER use coarse time blocks like "From 0 to 4 seconds" or "0-4s:".
- NEVER output multiple prompt variants. Output ONE unified four-segment prompt.
- NEVER include aspect ratios, resolution specs, model names, or UI instructions inside the prompt.
- NEVER use vague placeholders like "beautiful scene" or "high quality." Be specific about what the character does at every 0.5s beat.
- NEVER ignore the reference images/video. Every visual detail from references must be locked into the corresponding timestamps.
- NEVER generate storyboard descriptions, shot lists, or production documents.
- NEVER omit the product from the prompt. Every ad prompt must explicitly describe the product and its placement.
- NEVER omit the commercial narrative arc. The arc must guide your internal timing, but the output must be pure motion beats in Part 2.
```

---

## User Prompt Templates

### Template J: 60s Problem-Solution Ad (Health/Beauty/Office/Tech)

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional)
- Video 1: Motion reference — [describe the consumer action: applying, drinking, using, reacting]
- Video 2 (optional): Camera motion reference — [describe commercial camera work]
- Video 3 (optional): Pacing / mood / creative reference — [describe editing rhythm, transition style]

Task: Generate a Seedance 2.0 video prompt for a 60-second problem-solution advertisement consisting of FOUR 15-second segments.

Segment 1 (00:00–00:15): Hook — Relatable problem moment
Segment 2 (00:15–00:30): Problem Escalation — Daily life impact, emotional stakes
Segment 3 (00:30–00:45): Product Solution — Deep demonstration, transformation, multiple benefits
Segment 4 (00:45–00:60): Resolution + CTA — Satisfaction, product hero shot, brand identity

CRITICAL CONTINUITY INSTRUCTIONS:
- Segment 1's final timestamp (00:14.5) must end with the character experiencing the problem (e.g., looking stressed, rubbing tired eyes).
- Segment 2's first timestamp (00:15.0) MUST begin with "CONTINUE:" and describe the exact same pose continuing into the problem escalation.
- Segment 2's final timestamp (00:29.5) must introduce or reach for the product.
- Segment 3's first timestamp (00:30.0) MUST begin with "CONTINUE:" and show the product interaction beginning.
- Segment 3's final timestamp (00:44.5) must show the transformation or benefit peak.
- Segment 4's first timestamp (00:45.0) MUST begin with "CONTINUE:" and show the satisfied result state.
- Character must match Image 1 exactly across all segments. Product must match Image 2 exactly across all segments.

Output format: Four segments, each with Part 1 (flowing prose) and Part 2 (0.5s timestamped motion timeline). Timestamps: Seg1 00:00.0–00:14.5, Seg2 00:15.0–00:29.5, Seg3 00:30.0–00:44.5, Seg4 00:45.0–00:59.5. NO arc labels anywhere. Wrap segments in [[SEGMENT_1]] / [[/SEGMENT_1]], [[SEGMENT_2]] / [[/SEGMENT_2]], [[SEGMENT_3]] / [[/SEGMENT_3]], and [[SEGMENT_4]] / [[/SEGMENT_4]] tags.
```

### Template K: 60s Lifestyle Aspirational Ad (Fashion/Home/Wellness/Travel)

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional)
- Video 1: Motion reference — [describe the lifestyle action: walking, lounging, applying, enjoying]
- Video 2 (optional): Camera motion reference — [describe smooth, elegant camera movement]
- Video 3 (optional): Pacing / mood / creative reference — [describe relaxed, aspirational editing rhythm]

Task: Generate a Seedance 2.0 video prompt for a 60-second lifestyle aspirational advertisement consisting of FOUR 15-second segments.

Segment 1 (00:00–00:15): Dream Setup — Aspirational environment, character introduction
Segment 2 (00:15–00:30): Product Integration — Natural usage, social context, effortless lifestyle
Segment 3 (00:30–00:45): Benefit Deep-Dive — Emotional reward, social proof, transformation
Segment 4 (00:45–00:60): Product Close-up + CTA — Hero shot, brand identity, call to action

CRITICAL CONTINUITY INSTRUCTIONS:
- Segment 1's final timestamp (00:14.5) must end with the character naturally engaging with the environment.
- Segment 2's first timestamp (00:15.0) MUST begin with "CONTINUE:" and show the product entering the scene naturally.
- Segment 2's final timestamp (00:29.5) must show the character fully integrated with the product.
- Segment 3's first timestamp (00:30.0) MUST begin with "CONTINUE:" and show the benefit experience beginning.
- Segment 3's final timestamp (00:44.5) must show the peak emotional reward moment.
- Segment 4's first timestamp (00:45.0) MUST begin with "CONTINUE:" and transition toward the product hero shot.
- Character must match Image 1 exactly across all segments. Product must match Image 2 exactly across all segments. Environment must match Image 4 if provided.
- Style: [Warm/Natural/Aspirational/Clean/Minimalist]. The ad should feel like a lifestyle magazine come to life.

Output format: Four segments, each with Part 1 (flowing prose) and Part 2 (0.5s timestamped motion timeline). Timestamps: Seg1 00:00.0–00:14.5, Seg2 00:15.0–00:29.5, Seg3 00:30.0–00:44.5, Seg4 00:45.0–00:59.5. NO arc labels anywhere. Wrap segments in [[SEGMENT_1]] / [[/SEGMENT_1]], [[SEGMENT_2]] / [[/SEGMENT_2]], [[SEGMENT_3]] / [[/SEGMENT_3]], and [[SEGMENT_4]] / [[/SEGMENT_4]] tags.
```

### Template L: 60s Dramatic Reveal Ad (Food/Beverage/Luxury/Automotive)

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional)
- Video 1: Motion reference — [describe the dramatic product interaction: eating, drinking, unboxing, driving]
- Video 2 (optional): Camera motion reference — [describe dramatic camera: orbit, push-in, dolly]
- Video 3 (optional): Pacing / mood / creative reference — [describe dramatic lighting style]

Task: Generate a Seedance 2.0 video prompt for a 60-second dramatic cinematic product reveal advertisement consisting of FOUR 15-second segments.

Segment 1 (00:00–00:15): Atmosphere — Cinematic setup, mood, character enters world
Segment 2 (00:15–00:30): Build-Up — Anticipation, dramatic lighting, tension
Segment 3 (00:30–00:45): The Moment — Climax, product interaction, sensory peak
Segment 4 (00:45–00:60): Payoff + Brand — Satisfaction, beauty shots, logo, CTA

CRITICAL CONTINUITY INSTRUCTIONS:
- Segment 1's final timestamp (00:14.5) must end with the character approaching or discovering the product moment.
- Segment 2's first timestamp (00:15.0) MUST begin with "CONTINUE:" and escalate the anticipation.
- Segment 2's final timestamp (00:29.5) must reach the peak of tension just before the product interaction.
- Segment 3's first timestamp (00:30.0) MUST begin with "CONTINUE:" and launch into the climax moment.
- Segment 3's final timestamp (00:44.5) must show the peak sensory reaction.
- Segment 4's first timestamp (00:45.0) MUST begin with "CONTINUE:" and transition from reaction to appreciation.
- Character must match Image 1 exactly across all segments. Product must match Image 2 exactly across all segments. Environment must match Image 4 exactly.
- Style: [Dramatic/Cinematic/High Contrast]. The product reveal must feel like a cinematic climax.

Output format: Four segments, each with Part 1 (flowing prose) and Part 2 (0.5s timestamped motion timeline). Timestamps: Seg1 00:00.0–00:14.5, Seg2 00:15.0–00:29.5, Seg3 00:30.0–00:44.5, Seg4 00:45.0–00:59.5. NO arc labels anywhere. Wrap segments in [[SEGMENT_1]] / [[/SEGMENT_1]], [[SEGMENT_2]] / [[/SEGMENT_2]], [[SEGMENT_3]] / [[/SEGMENT_3]], and [[SEGMENT_4]] / [[/SEGMENT_4]] tags.
```

### Template M: 60s Product Demo / Tutorial Ad (Tech/Appliances/Tools/Software)

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional)
- Video 1: Motion reference — [describe product demonstration motion]
- Video 2 (optional): Camera motion reference — [describe product showcase camera work]
- Video 3 (optional): Transformation reference — [describe before/after transition]

Task: Generate a Seedance 2.0 video prompt for a 60-second product demonstration advertisement consisting of FOUR 15-second segments.

Segment 1 (00:00–00:15): Problem — Inefficiency, frustration, old way of doing things
Segment 2 (00:15–00:30): Introduction — Product enters, sleek design, key features
Segment 3 (00:30–00:45): Deep Demonstration — Product in use, transformation, multiple use cases
Segment 4 (00:45–00:60): Result + CTA — Before/after, product hero shot, brand name, pricing/offer

CRITICAL CONTINUITY INSTRUCTIONS:
- Segment 1's final timestamp (00:14.5) must end with the character looking frustrated or inconvenienced.
- Segment 2's first timestamp (00:15.0) MUST begin with "CONTINUE:" and show the product entering the frame.
- Segment 2's final timestamp (00:29.5) must show the product ready to use.
- Segment 3's first timestamp (00:30.0) MUST begin with "CONTINUE:" and start the demonstration.
- Segment 3's final timestamp (00:44.5) must show the successful result of using the product.
- Segment 4's first timestamp (00:45.0) MUST begin with "CONTINUE:" and show appreciation of the result.
- Character must match Image 1 exactly across all segments. Product must match Image 5 exactly across all segments.
- Style: [Clean/Modern/Tech-forward/Premium]. Product must be the visual hero.

Output format: Four segments, each with Part 1 (flowing prose) and Part 2 (0.5s timestamped motion timeline). Timestamps: Seg1 00:00.0–00:14.5, Seg2 00:15.0–00:29.5, Seg3 00:30.0–00:44.5, Seg4 00:45.0–00:59.5. NO arc labels anywhere. Wrap segments in [[SEGMENT_1]] / [[/SEGMENT_1]], [[SEGMENT_2]] / [[/SEGMENT_2]], [[SEGMENT_3]] / [[/SEGMENT_3]], and [[SEGMENT_4]] / [[/SEGMENT_4]] tags.
```

### Template N: 60s Emotional Storytelling Ad (Charity/Insurance/Family/Healthcare)

```
Analyze the attached reference images and videos.

Reference mapping (SLOT FORMAT — swap any images into these slots):
- Image 1: Character / subject reference — [describe face, hair, body type, skin tone, distinguishing features]
- Image 2: Costume / outfit / product reference — [describe garments, packaging, colors, fabrics, materials]
- Image 3: Prop / accessory / secondary subject reference — [describe key prop, accessory, or second character]
- Image 4: Environment / scene / background reference — [describe setting, lighting, atmosphere, architecture]
- Image 5: Product / brand / commercial element reference — [describe product, logo, brand element, or additional visual lock]
- Image 6: Style / aesthetic / mood / material reference — [describe target aesthetic, color palette, material quality, or mood tone]
- Image 7: Creative / freeform / composite reference — [describe landing page, mood board, or unstructured visual inspiration for holistic creative direction] (optional)
- Video 1: Motion reference — [describe emotional interaction: hugging, helping, sharing, reacting]
- Video 2 (optional): Camera motion reference — [describe intimate, emotional camera work]
- Video 3 (optional): Mood reference — [describe emotional tone, color grade]

Task: Generate a Seedance 2.0 video prompt for a 60-second emotional storytelling advertisement consisting of FOUR 15-second segments.

Segment 1 (00:00–00:15): Emotional Hook — Relatable moment, vulnerability, human connection
Segment 2 (00:15–00:30): Connection — Relationship deepens, shared experience, stakes rise
Segment 3 (00:30–00:45): Resolution — Product/brand as the answer, transformation, hope
Segment 4 (00:45–00:60): Warm Brand Moment — Emotional payoff, brand promise, tagline, CTA

CRITICAL CONTINUITY INSTRUCTIONS:
- Segment 1's final timestamp (00:14.5) must end with the emotional hook landing — a vulnerable or tender moment.
- Segment 2's first timestamp (00:15.0) MUST begin with "CONTINUE:" and deepen the relationship or shared experience.
- Segment 2's final timestamp (00:29.5) must show the stakes or need at their highest.
- Segment 3's first timestamp (00:30.0) MUST begin with "CONTINUE:" and introduce the product/brand as the solution.
- Segment 3's final timestamp (00:44.5) must show hope or transformation taking hold.
- Segment 4's first timestamp (00:45.0) MUST begin with "CONTINUE:" and show the warm resolution.
- Character A must match Image 1 exactly across all segments. Character B must match Image 2 if provided. Environment must match Image 4 exactly.
- Style: [Heartfelt/Genuine/Cinematic/Documentary-feel]. Emotion first, product second.

Output format: Four segments, each with Part 1 (flowing prose) and Part 2 (0.5s timestamped motion timeline). Timestamps: Seg1 00:00.0–00:14.5, Seg2 00:15.0–00:29.5, Seg3 00:30.0–00:44.5, Seg4 00:45.0–00:59.5. NO arc labels anywhere. Wrap segments in [[SEGMENT_1]] / [[/SEGMENT_1]], [[SEGMENT_2]] / [[/SEGMENT_2]], [[SEGMENT_3]] / [[/SEGMENT_3]], and [[SEGMENT_4]] / [[/SEGMENT_4]] tags.
```

---

## Common Anti-Patterns

### Missing CONTINUE Lock

**Symptom:** A segment starts with a completely new pose unrelated to the previous segment's ending. The cut feels jarring and Seedance drifts the character.  
**Fix:** Every segment after the first MUST begin its first timestamp with `CONTINUE:` and explicitly describe the continuation pose, hand positions, and product placement from the previous segment's final timestamp.

### Segment Drift (Reference Amnesia)

**Symptom:** Later segments' character face, hair, or outfit slowly morph because the prompt stops referencing Image 1.  
**Fix:** Re-lock character to Image 1 in every segment's Part 1 prose. Mention the same outfit details, hair style, and distinguishing features in Segments 2, 3, and 4.

### Pacing Collapse in Later Segments

**Symptom:** Segments 3 and 4 rush through beats or repeat earlier actions because the prompt runs out of ideas.  
**Fix:** Treat each 15-second segment as its own mini-movie with a clear micro-arc. Segment 3 should have its own build and climax. Segment 4 should have its own resolution.

### Coarse Timestamp Blocks

**Symptom:** The prompt uses narrative blocks like "From 0 to 4 seconds, the DREAM SETUP: ..." or "0-4s: HOOK — [description]". This gives Seedance no precise motion control.  
**Fix:** Demand frame-by-frame 0.5s timestamped beats in Part 2 of each segment. Every line must be `00:00.0     [body part] [action]; [expression]; [camera]`.

### Missing Body Part Precision

**Symptom:** "She touches the product." Which hand? How?  
**Fix:** Demand specificity: "right hand unscrews jar lid; left hand steadies jar base; soft smile".

### Arc Label Bleed

**Symptom:** Timestamped lines still include arc labels like "00:04.0     DREAM SETUP: character turns..."  
**Fix:** Prohibit arc labels entirely. The internal arc guides timing only — the output must be pure motion beats.

### Generic Product Description

**Symptom:** "A woman holds a bottle." The product is vague and unbranded.  
**Fix:** Demand explicit product lock at specific timestamps: "00:07.5     Right hand lifts amber glass bottle with blue label toward camera; label faces lens; hero lighting catches glass".

### Missing Camera Direction

**Symptom:** No camera notes; Seedance defaults to static medium shots.  
**Fix:** Embed camera notes into timestamps: "camera slow push-in from wide to close-up", "orbit around product begins", "handheld shake intensifies".

### Storyboard Drift

**Symptom:** The prompt describes shot lists or production documents instead of continuous motion.  
**Fix:** Remind that this is a single continuous 60-second video split into four segments, NOT a storyboard.

---

## Model-Specific Notes

| Model | Ad Video Prompt Engineering Tip |
|-------|--------------------------------|
| **Kimi / GPT-4** | Excellent at analyzing video + image references and synthesizing detailed timestamped motion timelines. Provide explicit reference mapping and continuity instructions for best results. With four segments, explicitly remind the model to maintain energy and ideas through Segments 3 and 4. |
| **Seedance (R2V)** | When using generated prompts with multiple image inputs, ensure the prompt explicitly references the image content at specific timestamps so Seedance knows which visual elements to lock. Continuation frames (last frame of previous segment as image_1 for next segment) dramatically improve temporal consistency. |
| **Seedance (I2V)** | Not recommended for multi-segment workflows — use Reference2Video with the last frame as image_1 plus original references to prevent drift. |

---

## Quick Reference: 60s Seedance Ad Prompt Formula

```
[Ad Type: Problem-Solution / Dramatic Reveal / Lifestyle / Demo / Emotional] +
[Segment 1 — Part 1: Setup prose with subject/product/environment locks] +
[Segment 1 — Part 2: 00:00.0–00:14.5 motion timeline] +
[Segment 2 — Part 1: Development prose with CONTINUE note] +
[Segment 2 — Part 2: 00:15.0–00:29.5 motion timeline beginning with CONTINUE:] +
[Segment 3 — Part 1: Climax prose with CONTINUE note] +
[Segment 3 — Part 2: 00:30.0–00:44.5 motion timeline beginning with CONTINUE:] +
[Segment 4 — Part 1: Resolution prose with CONTINUE note] +
[Segment 4 — Part 2: 00:45.0–00:59.5 motion timeline beginning with CONTINUE:] +
[Audio: evolving music mood, ambient sound, product sounds, voiceover tone]
```
