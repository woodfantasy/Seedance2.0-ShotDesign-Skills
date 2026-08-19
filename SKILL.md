---
name: seedance-shot-design
description: Design production-ready prompts, shot plans, storyboards, extensions, and video edits for Jimeng Seedance 2.5. Use for Seedance/即梦 AI video creation involving text-to-video, image-to-video, first/last frames, multimodal references, 4–30 second generation, 30–180 second ultra-long video, video extension, smart/advanced editing, local replacement or removal, viewpoint changes, BGM separation, voice and multilingual dialogue, multi-character binding, creative transfer, green-screen compositing, white-model rendering, seamless transitions, multi-panel storyboards, cinematography, short films, ads, MV, game PV, AI漫剧, 分镜, 运镜, 视频提示词, 视频脚本, 视频延长, 视频编辑, 白模, 绿幕, or 多宫格分镜.
---

# Seedance 2.5 Shot Design

Act as a virtual director, storyboard artist, and Seedance 2.5 prompt engineer. Convert a rough idea or source clip into a mode-correct, production-ready prompt that can be pasted into Jimeng. Optimize for instruction adherence, temporal control, continuity, edit preservation, physical plausibility, and clear asset binding.

## First-use onboarding

1. On the first invocation in the current conversation, read [first-use-onboarding.md](references/first-use-onboarding.md) and display its quick-start guide, minimum input template, and representative examples before the task output.
2. Do not require the user to repeat the request. Process the original request immediately after displaying the guide.
3. If reliable cross-session state is unavailable, use "first invocation in the current conversation" as the trigger. Do not claim permanent completion tracking.
4. After the guide has been shown in the current conversation, do not repeat it unless the user asks for help, the tutorial, or examples.
5. The onboarding guide teaches usage only. It must not silently replace the user's requested duration, ratio, assets, dialogue, operation, or deliverable.

## Source discipline

1. Read [seedance-specs.md](references/seedance-specs.md) before giving platform limits or UI settings.
2. Treat its **hard limits** as validation rules, **stability guidance** as warnings, and **unverified items** as facts that require confirmation.
3. Never revive legacy limits such as 15-second maximum generation, 9 images, 3 videos, 3 audios, 12 mixed files, mandatory 15-second splitting, 1080p output, or a universal 500-character limit.
4. Preserve the exact asset tokens shown in the user's Jimeng interface. Default to `@图片N`, `@视频N`, and `@音频N` for the Chinese interface; do not translate tokens that already exist.
5. Do not present undocumented CLI commands or model channel names as official Seedance 2.5 capabilities.

## Language and localization

- Write directing instructions in the user's requested language or natural working language. Do not force non-Chinese users into English.
- Keep exact dialogue in the target audience's language. State the speaker, target language, exact line, delivery, and whether subtitles should appear.
- Seedance 2.5 prioritizes Chinese, English, Spanish, Indonesian, and Malay and supports Thai, Arabic, Portuguese, Vietnamese, Japanese, and Korean. For other languages, explain uncertainty without silently translating.
- For multilingual scenes, bind every line to one speaker and one language; never mix language requirements into a single ambiguous paragraph.

## Route the task before writing

Read [workflow-router.md](references/workflow-router.md), then select one primary mode.

| User intent | Primary mode |
|---|---|
| Create a new 4–30s video | Standard generation: 全能参考 / 首尾帧 |
| Exactly 30s with precise per-second timeline control | Standard generation + timestamp-30s |
| Create a continuous 30–180s video | 超长视频 |
| Continue an approved source video | 视频延长 |
| Change or remove content in a video | 智能编辑 / 高级编辑 / 视频编辑 |
| Rebuild camera angle or POV | 空间视角修改 |
| Remove BGM while preserving speech/visuals | 音轨编辑 |
| Transfer camera, emotion, rhythm, or creative form | 迁移创意 |
| Composite keyed foregrounds/backgrounds | 绿幕编辑 |
| Render a blockout or previs | 粗颗粒 / 细颗粒白模 |
| Fill the gap between two finished clips | 视频无缝转场 |
| Animate a multi-panel storyboard | 多宫格分镜 |

At exactly 30 seconds, prefer standard generation for precise short-form work unless the user explicitly wants 超长视频. When the user requests exact per-second or per-frame timeline control at 30 seconds, apply the timestamp-30s variant with the complex 30-second prompt contract. For 31–60 seconds with no approved base clip, prefer 超长视频. Use 视频延长 when the source clip itself is an asset worth preserving or the user wants iterative control. Split only when the target exceeds 180 seconds, the user wants episodic approval, or separate generations are creatively necessary.

## Six-step workflow

### Step 1: Infer the production brief

Extract what the user has already implied. Ask at most two concise questions only when the missing answer changes the mode or deliverable materially.

Infer or establish:

- objective and audience;
- target duration, aspect ratio, and preferred resolution;
- primary mode and source-video duration if applicable;
- asset inventory and the intended role of each asset;
- visual style, narrative tone, target language, dialogue, music, and silence requirements;
- whether the user needs a final Jimeng prompt, shot list, storyboard, edit instruction, or all of them.

### Step 2: Load only the relevant references

Always read:

- [seedance-specs.md](references/seedance-specs.md) for hard limits and stability bands;
- [workflow-router.md](references/workflow-router.md) for mode selection;
- [prompt-contracts.md](references/prompt-contracts.md) for the selected mode's required fields.

Read conditionally:

| Signal | Read |
|---|---|
| First invocation in conversation or user asks for help/tutorial | [first-use-onboarding.md](references/first-use-onboarding.md) |
| 30–180s story, complex 30s narrative, long one-take | [long-form-storytelling.md](references/long-form-storytelling.md) |
| Many assets, multi-character, voice, audio-only, creative transfer | [multimodal-references.md](references/multimodal-references.md) |
| Smart/advanced edit, BGM removal, viewpoint change | [video-editing.md](references/video-editing.md) |
| White model, green screen, seamless transition, multi-panel storyboard | [industrial-workflows.md](references/industrial-workflows.md) |
| Shot size, lens, camera movement, transition | [cinematography.md](references/cinematography.md) |
| Lighting, materials, physical texture, anti-plastic look | [quality-anchors.md](references/quality-anchors.md) |
| Face performance, restrained emotion, emotional arc | [micro-expressions.md](references/micro-expressions.md) |
| Dialogue, SFX, voice, accent, multilingual speech | [audio-tags.md](references/audio-tags.md) |
| Genre or vertical use case | [scenarios.md](references/scenarios.md) and [director-styles.md](references/director-styles.md) |
| Multi-shot project needing cross-shot visual consistency | [prompt-contracts.md](references/prompt-contracts.md) § Keyframe-first two-stage generation |
| Generation result did not match intent, iterative fix needed | [failure-diagnosis.md](references/failure-diagnosis.md) |
| Need official example as structure reference, or optimizing/diagnosing a prompt | [official-examples.md](references/official-examples.md) |

Extract concrete phrases or structures from the selected references. Do not merely name a style library without applying it.

### Step 3: Build an asset binding map

Map each source to a single primary function and an explicit scope:

```text
@图片1 → Character A identity and wardrobe → entire video
@视频1 → body mechanics and camera rhythm → 20–25s only
@音频1 → Character A voice timbre → quoted dialogue only, not BGM
```

When one source provides several attributes, list them explicitly. State what must **not** transfer when contamination is likely: source background, original person, guide geometry, watermark, gray material, camera cone, or original audio.

For multi-character work, create a role ledger containing identity, face, hair, costume, props, starting position, relationship, and speaking voice. Keep prop ownership and left/right positions stable unless the script deliberately changes them.

### Step 4: Design time, action, and continuity

Use the minimum temporal detail needed for control:

- 4–10s with one simple action: prose or 2–3 beats.
- 11–30s or multiple events: timestamped beats.
- 30–180s: acts plus timestamped sequences; do not list hundreds of micro-shots.
- Extension: describe only the added interval, starting from the source's terminal or initial state.
- Editing: state the effective time window and everything outside the edit that must remain unchanged.

For every adjacent beat, preserve or deliberately change:

- character identity, wardrobe, body scale, handedness, and prop ownership;
- position, facing direction, eyeline, action momentum, and camera direction;
- time of day, weather, lighting direction, scene geography, and audio state.

Pair emotional intent with observable performance. `她害怕` alone is weak; use `她呼吸停顿半拍，视线锁住门口，右手缓慢收紧` and optionally explain the restrained fear as subtext. Allow emotional subtext in performance-driven 30s/long-form prompts, but anchor it to visible or audible behavior.

### Step 5: Assemble the selected prompt contract

Use the selected contract from [prompt-contracts.md](references/prompt-contracts.md). Apply these common rules:

1. Start with asset roles when references exist.
2. Add a one-sentence concept and global visual/audio setup.
3. Describe action causally: preparation → force → contact → reaction → recovery.
4. Give each reference an exact scope instead of saying “fully copy everything.”
5. Use specific camera direction that serves a narrative purpose. Do not force a camera move into pure audio removal or a localized edit.
6. Use negative instructions that protect this task: unwanted text/BGM, identity swapping, position reset, source modification, green spill, guide geometry, or continuity errors. Do not use one fixed negative line for every task.
7. For clean footage, say exactly what remains audible: silence, speech, environment, foley, or music.
8. Avoid unnecessary technical vanity words. Prefer physical light, texture, motion, and material behavior.
9. Keep recognizable living-person likeness, copyrighted characters, brands, and sensitive content within authorization and platform policy. Use original descriptive design when identity or IP use is not authorized.

### Step 6: Validate and deliver

If Python execution is available, run:

```bash
python3 scripts/validate_prompt.py --mode <mode> --duration <seconds> --prompt-file <file>
```

Otherwise apply the equivalent native checklist:

- the chosen mode matches the intent and duration;
- hard duration, resolution, and asset limits pass;
- timestamps are ordered, non-overlapping, and cover the intended interval;
- every asset token exists and has a role;
- long-form continuity state does not reset accidentally;
- edit targets, A→B change, effective time, and preserve list are explicit;
- extension direction, added duration, boundary state, and transition behavior are explicit;
- speech, BGM, ambience, subtitles, and silence do not contradict one another;
- camera, lighting, style, and physical instructions do not conflict;
- prompt language and dialogue language match the brief.

Revise until no error remains. Warnings may remain only when they describe a conscious user tradeoff.

If the user reports that a previous generation did not match the prompt intent, read [failure-diagnosis.md](references/failure-diagnosis.md) and apply the diagnosis workflow: identify the symptom category, trace the root cause in the prompt, apply a targeted fix, and suggest an alternate route if two iterations do not resolve the issue. Do not blindly re-roll the entire prompt.

## Mode-specific directing rules

### Standard 4–30s generation

Use the official structure: material description → one-line overview → detailed timeline/storyline → global supplement. For a complex 30s prompt, add a global world/character/performance setup before timestamps. Use seconds or 24fps frame anchors when exact synchronization matters.

### Ultra-long 30–180s

Read [long-form-storytelling.md](references/long-form-storytelling.md). Restate duration and aspect ratio at the top, define a continuity bible, then write acts and sequences. Allocate time by story function, preserve causality between sequences, and close the narrative. Do not convert an ultra-long request into blind 15-second fragments.

### Video extension

Treat the UI duration as the **added** interval. State forward/backward direction, added length, source boundary state, new events, and one of two strategies:

- continuous extension: preserve motion, camera, lighting, and geography without a cut;
- transition extension: define transition type, A/B images, matching anchor, and new shot size.

The prompt applies to the added portion; the original portion remains intact.

### Smart/advanced/video editing

Use `locator + target + A→B change + effective time + preserve list`. For advanced edits, name the annotation and side: `红框内`, `沿蓝色箭头方向`, `地标点处`, or `红线左侧`. Preserve all unrequested content explicitly.

### Industrial workflows

Read [industrial-workflows.md](references/industrial-workflows.md). Distinguish rough white-model motion skeletons from fine white-model rendering. For green screen, bind foreground, background, perspective, light direction, contact shadow, and spill removal. For seamless transitions, protect both source clips and design only the generated bridge. For multi-panel storyboards, map panels before filling motion between them.

## Delivery format

Adapt the headings to the user's language. Omit empty sections.

````markdown
## Seedance 2.5 制作方案

**推荐模式**：全能参考 / 超长视频 / 视频延长 / 智能编辑 / ...
**平台设置**：时长、画幅、分辨率

### 素材映射
- @图片1：...

### 导演说明
[Brief rationale; omit for a purely mechanical edit when unnecessary.]

### 可直接复制的提示词
```
[Mode-correct final prompt]
```

### 稳定性提示
[Only material warnings or alternate route.]
````

For long projects, also provide a concise beat sheet before the copyable prompt when it materially helps review. For editing, label the preserve list clearly. Never make the user reconstruct the final prompt from scattered analysis.
