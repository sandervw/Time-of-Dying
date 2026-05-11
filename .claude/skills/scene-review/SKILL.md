---
name: scene-review
description: Audit a finished scene draft against its original story context and produce a post-scene summary file with reference material and a review audit. Use when asked to "review the scene", "produce the scene summary", or any request to analyze a finished scene draft and generate its summary.
---

# Scene Review

Audit a finished scene draft against its original story context and produce a post-scene summary file. The scene file itself is not modified.

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

### Step 1: Audit Against Original

Read `references/review.md` and `references/audit-questions.md`.

Follow the review reference's instructions to audit the scene against the original story context and the guiding questions. Hold the audit findings (wordcount comparison, per-question yes/no/N/A coverage, any alignment notes) in working memory. Do NOT edit the scene file.

### Step 2: Generate Post-Scene Material

Read `references/post-scene.md`.

Follow the reference's instructions to generate the post-scene material from the scene: Scene Summary, Ending Text, Questions Posed, Characters Introduced or Referenced, and the Review Audit (assembled from Step 1's findings).

### Step 3: Write Post-Scene Summary

Copy the `assets/post-scene-summary.md` template to a new file named `[Storyname]-Scene-[X]-Summary.md` (matching the scene file's naming).

Write the post-scene material into this file.

### Step 4: Present

Present the finished file to the user:
- `[Storyname]-Scene-[X]-Summary.md` — the post-scene summary

The scene file is left untouched.

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
