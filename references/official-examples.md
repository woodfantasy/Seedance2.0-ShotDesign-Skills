# Official Seedance 2.5 examples

Examples and structural guidance sourced from official ByteDance channels. Use these as structural references when the user's request is underspecified, when optimizing an existing prompt, or when verifying a difficult mode. Do not copy an example mechanically; adapt its structure to the user's actual brief.

Last verified: 2026-08-19

## Official prompt structure

Source: BytePlus ModelArk Seedance 2.5 documentation.

The officially recommended prompt structure follows this order:

1. **Global style** — genre, color grade, film stock or digital look, aspect ratio, shutter behavior
2. **Scene** — one-line logline: action + setting + mood
3. **Characters** — physical descriptions or reference via uploaded assets (`@Image 1`)
4. **Location** — environment, props, atmospheric conditions
5. **Camera movement** — specific instructions (e.g., "One-take handheld gimbal tracking shot")
6. **Audio** — bracketed audio directives

Source: Jimeng / 即梦 official platform documentation.

The Chinese-language formula:

> 主体（Subject）+ 动作/事件（Action）+ 场景与环境（Setting）+ 视觉风格（Visual Style）+ 镜头运动（Camera）+ 音效/对话（Audio）

## Official audio bracket system

Source: Jimeng / 即梦 official documentation.

| Bracket | Function | Example |
|---|---|---|
| `()` | Background music | `(soft piano melody)` |
| `<>` | Sound effects | `<footsteps on wet pavement>` |
| `{}` | Dialogue | `{Character A: "Let's go."}` |
| `【】` | Subtitles | `【Episode 1: The Beginning】` |

## Official examples

### Example 1 — Timestamped narrative

Source: ByteDance official Seedance 2.5 announcement blog (2026-07-31).

> A girl hangs laundry gracefully. 0–4s: A girl hangs laundry in a sunlit garden, medium shot. 4–10s: She takes another piece of clothing from the bucket and shakes it vigorously, close-up. 10–15s: She smiles at a butterfly landing on the line, wide shot. Cinematic lighting, photorealistic.

Structure notes: timestamped beats with shot-size changes per beat; single continuous action with causal progression (hang → shake → react); global style declared at the end.

### Example 2 — Camera/movement control via editing

Source: ByteDance official Seedance 2.5 announcement blog (2026-07-31).

> Edit @Video 1. Keep the characters and actions unchanged. 0–4s: Micro-FPV move skimming past the pan, whip-pan to the coffee. 4–7s: Push in and track laterally along the rim of the pan, following the fried egg as it flips. 7–11s: Rapidly rise to a top-down view, then descend steadily.

Structure notes: edit mode with explicit preservation of existing content; camera-only changes with precise timestamps; each beat defines a distinct camera technique.

### Example 3 — Complex information visualization

Source: ByteDance official Seedance 2.5 announcement blog (2026-07-31).

> A visual infographic chronicling scientific research at a polar research station. Place the main station building at the center. Surround it with: a timeline of development (left), a bar chart comparing five stations (bottom), a pie chart of energy sources (top-right), and a line chart of measurements (bottom-right). Realistic, professional design.

Structure notes: spatial layout specification with named regions (center, left, bottom, top-right, bottom-right); multiple data-visualization elements bound to positions; global style at the end.

## Official anti-patterns

Source: Jimeng / 即梦 official platform documentation.

| ❌ Avoid | ✅ Use instead | Reason |
|---|---|---|
| Literary metaphors or poetry as prompts | Concrete visual descriptions of what appears on screen | The model interprets literal visual instructions, not figurative language |
| Abstract concepts (e.g., "personal growth", "becoming wise") | Specific visible actions that show the concept | Abstract ideas have no visual representation without observable behavior |
| Omitting the subject (e.g., just "growing, flourishing") | Naming the subject explicitly (e.g., "a lotus flower grows in a pond") | Without a subject, the model cannot determine what to render |
| Vague quality boosters ("masterpiece", "best quality", "ultra HD") | Physical material and light descriptions (film stock, lens, texture) | Vague words add no controllable visual information |

## Official reference token system

Source: BytePlus ModelArk Seedance 2.5 documentation.

Asset references use the tokens shown in the user's interface:

- `@Image 1`, `@Image 2`, … or `@图片1`, `@图片2`, …
- `@Video 1`, `@Video 2`, … or `@视频1`, `@视频2`, …
- `@Audio 1`, `@Audio 2`, … or `@音频1`, `@音频2`, …

Documented limits: up to 30 images, 10 videos, and 10 audios per request. Each reference should be assigned a specific role and scope rather than "fully copy everything."
