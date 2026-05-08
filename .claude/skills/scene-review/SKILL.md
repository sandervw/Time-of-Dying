---
name: scene-review
description: Review and finalize a draft scene against its original story context, then produce a post-scene summary file with reference material for downstream scenes. Use when asked to "review the scene", "finalize the scene", "produce the scene summary", or any request to revise a finished scene draft and generate its summary.
---

# Scene Review

Review a finished scene draft against its original story context, revise the prose in place, and produce a post-scene summary file.

## Inputs

The user provides:

- **Scene file path**: The finished scene draft (typically the output of `scene-writer`).
- **Story background**: The broader narrative context (world, characters, prior events).
- **Scene outline/idea**: What this specific scene was meant to accomplish — its purpose, characters involved, tone.
- **Scene priorities (optional)**: Stylistic or content priorities the scene was meant to honor.
- **Wordcount**: The original target length for the scene (informational — wordcount is relaxed during review).
- **Scene type (optional)**: Establishing or continuation. If not provided, infer from the scene outline and wordcount.

## Workflow

_Each step's reference file must only be read AFTER the previous step's output has been completed. Do NOT batch-read reference files. Reading a step's reference file counts as beginning that step._

---

### Step 1: Review and Revise

Read `references/review.md` and `references/audit-questions.md`.

Follow the review reference's instructions to audit the scene against the original story context and the guiding questions. Edit the scene prose directly in the scene file.

### Step 2: Generate Post-Scene Material

Read `references/post-scene.md`.

Follow the reference's instructions to generate the post-scene material from the revised scene: Scene Summary, Ending Text, Questions Posed, Characters Introduced or Referenced, and Reflection.

### Step 3: Write Post-Scene Summary

Copy the `assets/post-scene-summary.md` template to a new file named `[Storyname]-Scene-[X]-Summary.md` (matching the scene file's naming).

Write the post-scene material into this file.

### Step 4: Present

Present both finished files to the user:
- `[Storyname]-Scene-[X].md` — the revised scene prose
- `[Storyname]-Scene-[X]-Summary.md` — the post-scene summary

## File Structure

```
scene-review/
├── SKILL.md
├── references/
│   ├── review.md
│   ├── audit-questions.md
│   └── post-scene.md
└── assets/
    └── post-scene-summary.md
```
