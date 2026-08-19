# Seedance 2.5 Workflow Router

## Contents

- Routing questions
- Primary decision table
- Duration strategy
- Edit-mode routing
- Compound requests
- Fallback rules

## Routing questions

Resolve these in order:

1. Is the user creating a new video or changing an existing video?
2. Is an existing source clip meant to remain intact, be extended, or be edited?
3. What is the target duration?
4. Are there specialized sources: green screen, white model, two finished clips, storyboard panels, or audio only?
5. Does the user want a final prompt, a shot plan, or a full production package?

Infer answers already present in the request. Ask only when two plausible modes would produce materially different work.

## Primary decision table

| Condition | Route | Why |
|---|---|---|
| New video, 4–30s | Standard generation | Native single-generation range |
| New video, exactly 30s | Standard by default | Greater short-form precision; use ultra-long only when requested |
| New video, exactly 30s with precise per-second or per-frame timeline | Standard + timestamp-30s | Apply the complex 30-second prompt contract with full timestamp beats |
| New continuous video, 31–180s | Ultra-long video | Native long-form path, no mandatory splitting |
| Existing approved clip, user wants what happens next/before | Video extension | Preserves original and generates only the added interval |
| Existing clip, target/object/style/time should change | Smart/video edit | Modification rather than continuation |
| User supplies annotations or needs precise region control | Advanced/video edit | Locator-aware editing |
| Only camera position or POV should change | Spatial viewpoint modification | Reconstructs space while preserving scene content |
| Remove music but preserve speech/subtitles/visuals | Audio-track edit | Explicit source-preservation task |
| Reuse reference camera/emotion/viral concept | Creative transfer | Transfers selected creative dimensions |
| Keyed/green source footage | Green-screen edit | Foreground/background compositing workflow |
| Rough previs/blockout video | Rough white model | Motion, blocking, camera, and spatial skeleton |
| Detailed 3D model needing finish/render | Fine white model | Material, light, and style rendering |
| Two finished clips need a generated bridge | Seamless transition | Protect source A and B; generate the gap |
| One multi-panel storyboard image | Multi-panel storyboard | Map panels, then interpolate story and motion |
| Only audio is supplied | Audio-only multimodal | Seedance 2.5 supports pure-audio driving |

## Duration strategy

### 4–30 seconds

Use standard generation. Do not split solely because the duration exceeds 15 seconds.

### 31–60 seconds

- No approved source clip: prefer ultra-long video.
- Approved source clip that must remain untouched: use extension if the source is ≤30s and the requested added duration is 4–30s.
- User wants iterative approval of every stage: extension or deliberate multi-generation may be appropriate.

### 61–180 seconds

Use ultra-long video unless the user explicitly wants episodes or shot-by-shot approval. Build acts and continuity rather than 15-second fragments.

### More than 180 seconds

Split at story acts, locations, format changes, or approval gates. Each segment may itself use ultra-long generation. Define handoff state and post-production assembly. Never default to equal 15-second slices.

## Extension eligibility

Require all of the following:

- source/current video ≤30s;
- added duration 4–30s;
- final result ≤60s;
- the user values preservation of the source segment.

If any condition fails, recommend ultra-long generation, intentional multi-part production, or post-production assembly.

## Edit-mode routing

| Request wording | Route |
|---|---|
| “去掉、删除、增加、替换、改成” | Smart edit |
| “红框内、箭头指向、地标点、某条线左侧” | Advanced edit |
| “把平视改成俯拍/第一人称/固定正面” | Spatial viewpoint modification |
| “去掉 BGM，只留人声/环境音” | Audio-track edit |
| “参考这个视频的网感、情绪、镜头节奏” | Creative transfer |
| “保持动作和镜头，只改画风” | Style edit or creative transfer; choose edit when preservation is strict |

## Compound requests

Select one primary mode, then attach compatible secondary operations.

Examples:

- BGM removal + sunlight relighting: primary smart edit, secondary audio preservation.
- Green-screen composite + weather change: primary green-screen edit, secondary environment edit.
- White-model render + multi-character identity binding: primary white model, secondary multimodal binding.
- Ultra-long story + multilingual dialogue: primary ultra-long, secondary multilingual audio.

Do not combine incompatible operations into one prompt when preservation matters. Recommend two passes when one task changes geometry/camera and another requires pixel-level preservation.

## Fallback rules

- If a hard platform limit fails, do not hide it; propose the closest valid route.
- If a stability recommendation is exceeded but still within a hard limit, warn and offer asset reduction or staged generation.
- If source duration or annotation details are unknown, use a clearly labeled placeholder instead of inventing a number.
- If the platform behavior is not documented, say it requires a live test; do not promote a legacy 2.0 rule to a 2.5 fact.

