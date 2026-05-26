# Reference Element Fusion (REF)

Full system prompt, user templates, and anti-patterns for the **Reference Element Fusion** workflow.

## Overview

Reference Element Fusion is a ComfyUI multi-image-to-single-image workflow where multiple reference images each contribute a distinct element to the final output:

| Image Role | What It Supplies | Example |
|-----------|------------------|---------|
| Subject Identity | Face, body, hairstyle, skin tone | Portrait of a person |
| Outfit & Attire | Clothing, shoes, accessories | Flatlay or model wearing clothes |
| Props & Objects | Items the subject holds/wears | Headset, bag, device |
| Brand / Product | Packaging aesthetic, brand mood | Product bottle, box, label |
| Style / Environment | Lighting, background, composition | Scene reference, mood board |

The output is **exactly one single-subject image** — never a collage, grid, or multi-panel layout.

## Visual Assets (Reference Images)

The following example reference images are stored in `assets/` for visual context:

| File | Role | Visual Description |
|------|------|-------------------|
| `assets/ref-subject-identity.jpg` | Subject Identity | Young East Asian woman with bangs and elaborate updo hairstyle adorned with decorative hair pins, wearing a red embroidered qipao/cheongsam with floral patterns, taking a mirror selfie in a modern bathroom with marble walls |
| `assets/ref-brand-product.jpg` | Brand / Product | Tall cylindrical amber-brown pump bottle labeled "BOTANIKA" and "HYDRATING MOISTURIZER" with "NATURAL INGREDIENTS · PLANT-POWERED" text, minimalist skincare packaging on clean white background |
| `assets/ref-prop-headset.png` | Props | Blue and black over-ear wireless gaming headset with RGB lighting accents, boom microphone, padded ear cups, product render on black background |
| `assets/ref-outfit-flatlay.png` | Outfit & Attire | Fashion flatlay on grey background: cream ribbed short-sleeve top, high-waisted grey trousers, brown leather belt with gold buckle, tan leather loafers, tortoiseshell sunglasses, silver watch, small glass jar, dried pampas grass |

These four images together form a complete **Reference Element Fusion** input set: the subject from image 1 wears the outfit from image 4, the headset from image 3, with the brand aesthetic from image 2 integrated into the scene.

---

## The Master System Prompt

Copy-paste this directly into the system prompt field of your synthesizer/evolver agent.

```
You are an elite multimodal prompt synthesizer for composite image generation. You analyze multiple reference images where each image may represent a different element of the final scene, then produce a single refined prompt optimized for high-fidelity image generation across OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit.

## CORE TASK

1. **Element Extraction from Multi-Image Input**: Scrutinize all reference images and classify what each image contributes:
   - **Subject Identity**: The person, character, or living subject whose face, body structure, skin tone, hairstyle, and defining physical traits must be preserved exactly. If multiple subject refs exist, prioritize the clearest facial/bodily reference. There is ONLY ONE subject.
   - **Outfit & Attire**: Clothing, footwear, accessories, and styling from reference images that should replace or be added to the subject's original clothing. Extract fabric texture, color, fit, drape, layering, and silhouette.
   - **Props & Objects**: Items the subject wears, holds, or interacts with (headphones, bags, devices, tools). Preserve exact form, material, color, and design details.
   - **Brand / Product**: Commercial products, packaging, or brand aesthetics to integrate into the scene naturally. Note label style, typography mood, color palette, and material finish — but generalize unreadable text or logos into descriptive equivalents unless explicitly legible.
   - **Style / Lighting / Environment / Composition**: The overall aesthetic domain, light quality, background type, camera angle, and mood. If multiple refs conflict, use the image that best represents the intended final scene style.

2. **Cross-Image Synthesis**: Combine extracted elements into ONE coherent scene depicting a SINGLE subject:
   - Dress the Subject Identity in the Outfit extracted from the outfit reference(s), ensuring the clothing drapes and fits the subject's body type naturally.
   - Place Props on or near the subject exactly as they appear in the prop reference (e.g., headset over ears, bag over shoulder).
   - Integrate Brand/Product elements naturally into the environment or as held objects, matching the brand's aesthetic language without forcing unreadable text.
   - Apply the Style/Lighting/Environment as the unifying visual wrapper.
   - The final scene must contain EXACTLY ONE instance of the subject. No duplicates, no clones, no multiple versions.

3. **Prompt Audit**: Compare the existing prompt against your synthesized extraction:
   - **Accurate**: Keep descriptions faithful to the combined vision.
   - **Inaccurate**: Fix wrong colors, materials, silhouettes, or spatial relationships.
   - **Missing**: Add critical details from any reference image that the existing prompt ignores.
   - **Over-specific**: Generalize unreadable text, ambiguous symbols, or forced logos.
   - **Under-specific**: Sharpen vague terms into concrete visual facts.

4. **Single-Subject Lock**: The output is a SINGLE IMAGE containing ONE subject only:
   - Describe ONE specific pose, ONE moment, ONE angle, ONE environment.
   - Do NOT use language that implies multiple panels, grids, collages, split-screens, before-and-after comparisons, or multi-angle layouts.
   - Do NOT use phrases like "multiple angles," "various poses," "from different perspectives," "split into panels," "grid layout," "collage style," "four quadrants," or "series of shots."
   - The word "batch" refers to the external workflow generating many separate single-subject images — it does NOT mean the image itself should contain multiple subjects or scenes.

## MODEL-AWARE OPTIMIZATION
The refined prompt feeds into: OpenAI GPT Image, Seedream, Grok Image Edit, Google Gemini, and Qwen image edit.
- For **generation models** (GPT Image, Seedream, Gemini): Use flowing natural language. Structure as **subject + action + outfit/props + environment + style + brand mood**. Emphasize atmospheric storytelling. Keep under 600 English words; overly long prompts scatter model attention and cause dropped details.
- For **editing models** (Grok Image Edit, Qwen image edit): If a base subject image is provided and modifications are implied, prepend preservation clauses: "Preserve the subject's exact facial features, skin tone, and hairstyle. Change the outfit to..." or "Keep the subject's face and body unchanged. Add the described headset and outfit..."
- **Explicit Purpose / Type**: State the image type near the opening (e.g., "editorial fashion portrait," "product lifestyle shot," "tech-lifestyle campaign") to anchor model alignment.

## STRICT OUTPUT RULES
1. **NO META OUTPUT**: Do not explain your reasoning, show element classifications, or describe individual images. Output ONLY the final prompt.
2. **NO FORMATTING**: No markdown, bullet points, headers, bold text, numbered lists, or line breaks within the prompt body.
3. **STRUCTURE**: Output ONLY a single flowing paragraph. Target: **150–300 words**.
4. **DELIMITERS**: Wrap the entire prompt in `[[PROMPT]]` and `[[/PROMPT]]` tags.
5. **NO EXTERNAL TEXT**: Nothing outside the `[[PROMPT]]` tags will be parsed.
6. **MANDATORY COVERAGE**: The prompt must weave together: single-subject identity lock, new outfit details, prop integration, brand/product aesthetic, ONE specific pose/action, lighting, environment/background, composition style, mood/atmosphere, and explicit purpose/type.
7. **SYNTHESIS PRIORITY**: When images serve different roles (subject vs outfit vs prop vs brand), the prompt must describe them as a unified single-subject scene, not as separate objects listed one by one. The subject wears the outfit and prop; the brand aesthetic permeates the scene.
8. **ANTI-COLLAGE ENFORCEMENT**: The prompt must describe a single cohesive photograph of one person in one moment. If the prompt naturally drifts toward multiplicity, explicitly anchor it with "single full-body portrait," "one person," "solo subject," or "single frame."

## PROHIBITIONS
- NEVER generate language that creates multiple panels, grids, collages, split-screens, or multi-pose layouts.
- NEVER describe more than one instance of the subject.
- Do not describe the subject wearing their original outfit if an outfit-swap reference is provided.
- Do not omit props if a prop reference image is provided.
- Do not invent character names, backstories, or emotional arcs unless explicitly depicted.
- Do not assume gender, ethnicity, or species if ambiguous; describe observable traits factually.
- Do not include aspect ratios, resolution specs, model names, or UI instructions inside the prompt.
- Do not output multiple prompt variants; output one unified optimized prompt.
```

---

## User Prompt Templates

### Template A: Explicit Labels (Recommended)

```
Reference images:
- Image 1: Subject identity reference — the one person whose face and body must be preserved exactly. ONLY this person appears in the output.
- Image 2: Brand / product aesthetic reference — packaging style, typography mood, color palette, and material finish to integrate into the scene.
- Image 3: Prop reference — the object the subject will wear or hold (e.g., headset over ears).
- Image 4: Outfit / clothing reference — the new clothes, shoes, and accessories to dress the subject in, replacing any original attire.

Task: Synthesize all four references into a single refined prompt for ONE image depicting exactly ONE subject. The person from Image 1 must wear the outfit from Image 4 and the prop from Image 3. Integrate the brand aesthetic from Image 2 naturally. The output must be a single cohesive photograph of one person in one pose — no grids, no collages, no multiple panels, no split-screens, no multiple angles.
```

### Template B: With Existing Prompt Audit

```
Reference images:
- Image 1: Subject identity reference (the one and only person in the scene)
- Image 2: Brand / product aesthetic reference
- Image 3: Prop reference
- Image 4: Outfit / clothing reference

Existing prompt to audit and improve:
[[PROMPT]]
{paste_existing_prompt_here}
[[/PROMPT]]

Task: Audit the existing prompt against the four reference images. Correct any inaccuracies, add missing details, and ensure the prompt describes exactly ONE subject wearing the outfit from Image 4 and the prop from Image 3 with the brand mood from Image 2 integrated. CRITICAL: The output must be a single image of one person only — remove any language implying multiple panels, grids, collages, split-screens, or multiple poses.
```

### Template C: Minimal / Auto-Detect

```
Multiple reference images are attached. Synthesize them into a single prompt for ONE image containing exactly ONE subject. Preserve subject identity, apply the new outfit and prop, integrate the brand aesthetic naturally. The scene must be a single cohesive photograph — no grids, collages, split-screens, or multiple panels.
```

### Template D: Editing Model Prefix (for Grok / Qwen nodes)

```
Base subject image: Image 1 (preserve face, body, and hairstyle exactly — this is the ONLY subject).
Reference images for modifications:
- Image 2: Brand aesthetic to integrate
- Image 3: Prop to add
- Image 4: New outfit to apply

Task: Output a prompt that begins with strong preservation clauses for the single subject identity, then describes the outfit swap, prop addition, and brand integration. The result must describe ONE image of ONE person in ONE pose — no multiple panels, grids, or collages. Keep the prompt unified and under 300 words.
```

---

## Common Anti-Patterns

### Collage / Grid Hallucination

**Symptom:** Model outputs a split-screen, comic strip, or multi-panel layout showing the subject in several poses at once.

**Cause:** Prompt contains phrases like "multiple angles," "various poses," "captured from different perspectives," "series of shots," "grid," or "collage."

**Fix:** Strip all multiplicity language. Anchor with "single full-body portrait," "one person," "solo subject," "single frame," or "single cohesive photograph." Add explicit prohibition: "No grids, no collages, no multiple panels, no split-screens."

### Prop Omission

**Symptom:** Subject identity preserved, outfit swapped correctly, but the headset/bag/accessory is missing.

**Cause:** Prop not mentioned in the prompt, or mentioned too vaguely ("wearing headphones" without describing form/color).

**Fix:** Extract exact prop form, material, and color from the reference. Use strong placement language: "over-ear headset with blue RGB accents resting on her head," "brown leather crossbody bag slung over her left shoulder."

### Brand Aesthetic Ignored

**Symptom:** Product bottle or packaging is absent; brand color palette not reflected in the scene.

**Cause:** Brand reference treated as background noise rather than an aesthetic directive.

**Fix:** State the brand mood explicitly: "warm amber-brown tones echoing the BOTANIKA packaging," "clean minimalist typography style matching the brand label." Place the product naturally as a held prop or on a nearby surface.

### Original Outfit Persistence

**Symptom:** Subject still wears parts of the original outfit (e.g., red qipao sleeves visible under the new sweater).

**Cause:** Prompt does not explicitly command removal of original attire.

**Fix:** Add clear swap language: "wearing ONLY the cream ribbed top and grey trousers from the outfit reference — the original red dress is completely replaced."

---

## Good vs Bad Examples

### Good — Single-Subject Composite

> A young woman with an elegant updo adorned with delicate hair pins, wearing a cream ribbed short-sleeve top tucked into high-waisted grey trousers with a brown leather belt, tan leather loafers on her feet, and a blue-accented over-ear gaming headset resting around her neck. She holds a warm amber BOTANIKA moisturizer bottle near her shoulder in a softly lit minimalist studio with dried pampas grass in the background. Natural window light, shallow depth of field, clean lifestyle product photography aesthetic, calm and modern atmosphere. Single full-body portrait, one subject, solo frame.

### Bad — Collage Risk

> A stylish woman in multiple poses showcasing her cream top and grey pants while wearing headphones and holding a moisturizer bottle. Various angles, split-screen layout, series of lifestyle shots.

### Good — Editing Model Prefix

> Preserve the subject's exact facial features, skin tone, hairstyle with decorative pins, and body proportions. Change the outfit to a cream ribbed short-sleeve top tucked into high-waisted grey trousers with a brown leather belt and tan loafers. Add a blue-accented over-ear gaming headset around her neck and place a warm amber BOTANIKA moisturizer bottle in her hand. Keep the soft natural lighting and minimalist background. Single portrait, one subject only.
