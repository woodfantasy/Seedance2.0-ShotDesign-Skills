# First-use onboarding

This file is displayed automatically on first install or first invocation in a conversation. It teaches the user how to interact with the skill efficiently.

## Quick-start guide

### Minimum input

You only need **one sentence** to get a production-ready Seedance 2.5 prompt:

```text
Use $seedance-shot-design.
A 15-second cinematic product reveal for a pair of sneakers.
```

The skill will infer duration, aspect ratio, mode, style, and camera work from your description. You can override any parameter explicitly.

### What you can add

| Parameter | Example |
|---|---|
| Duration | `20 seconds`, `30s`, `2 minutes` |
| Aspect ratio | `16:9`, `9:16`, `1:1` |
| Assets | `@Image 1 is the character reference`, `@Video 1 is the motion guide` |
| Style | `cinematic`, `anime`, `documentary`, `Wes Anderson color palette` |
| Dialogue | `Character A says "Let's go" in English` |
| Mode hint | `extend this video`, `edit the scene`, `ultra-long story` |
| Deliverable | `only the prompt`, `shot list + prompt`, `diagnosis only` |

If something is missing, the skill will use sensible defaults (15 seconds, 16:9, standard generation) and label them.

---

## Examples

### Example 1 — Standard video (product / commercial)

```text
Use $seedance-shot-design.
A 15-second 16:9 luxury watch commercial.
The watch rests on a dark marble surface. Camera slowly pushes in.
Golden hour light refracts through the crystal.
End with the watch face filling the frame.
```

**What happens**: The skill selects `standard` mode, designs a timestamped beat sheet with causal camera moves, applies quality anchors (material texture, light behavior), and outputs a copy-ready prompt.

### Example 2 — Timestamped narrative (30 seconds)

```text
Use $seedance-shot-design.
30s, 16:9 cinematic. @Image 1 is the character (full appearance, keep original outfit).
0–10s: Character walks through a rain-soaked city street at night, medium tracking shot.
10–20s: Stops under a streetlight, looks up, rain drips from an umbrella, close-up.
20–30s: Turns and walks away into the fog, wide shot, camera holds static.
Mood: melancholy. Sound: rain, distant traffic, soft piano.
```

**What happens**: The skill selects `standard` mode with precise timeline, binds the image reference to character identity and wardrobe for the full duration, designs continuity across the three beats, and validates timestamp coverage.

### Example 3 — Video extension

```text
Use $seedance-shot-design.
Extend @Video 1 forward by 15 seconds.
Continue the character's walk. She reaches a door, hesitates, then pushes it open.
Keep the same lighting, camera style, and outfit from the original.
```

**What happens**: The skill selects `extension` mode, describes only the added 15-second interval, preserves the source video's terminal state (position, lighting, wardrobe, camera), and adds boundary-crossing instructions.

### Example 4 — Video editing (remove + audio)

```text
Use $seedance-shot-design.
Edit @Video 1. Remove the logo in the top-right corner from 0–20s.
Reconstruct the sky behind it. Also remove background music but keep all dialogue and ambient sound.
```

**What happens**: The skill selects `smart_edit`, specifies the edit target with exact location and time window, lists what must remain untouched, then chains a BGM-removal pass that explicitly preserves speech and environment audio.

---

## Supported modes at a glance

| Mode | Duration | Use when |
|---|---|---|
| Standard generation | 4–30s | Create a new video from text, images, or audio |
| Ultra-long | 30–180s | Create a continuous long-form story |
| Extension | +4–30s | Continue an existing video forward or backward |
| Smart / Advanced edit | any | Modify, replace, or remove content in a video |
| Viewpoint | any | Rebuild camera angle or POV |
| BGM separation | any | Remove music while preserving speech and visuals |
| Creative transfer | any | Transfer camera, emotion, or rhythm from a reference |
| Green screen | any | Composite keyed foreground and background |
| White model (rough/fine) | any | Render a 3D blockout or previs into realistic footage |
| Seamless transition | any | Generate a bridge between two finished clips |
| Storyboard | any | Animate a multi-panel storyboard |

---

## FAQ

**Q: Does this skill generate videos or spend credits?**
A: No. It designs and validates prompts only. You paste the result into the Jimeng / Dreamina UI yourself.

**Q: What language should I write in?**
A: Use your natural working language. The skill will direct in your language and handle dialogue binding separately.

**Q: Can I use multiple modes together?**
A: Each request uses one primary mode. Some capabilities (voice reference, character locking, BGM removal) can be combined as specialist additions to any mode. The skill will handle the combination.
