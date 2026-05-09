---
name: prose-producer
description: Orchestrates a full scene draft. Given a full story outline, prior scene prose, source style passage, and a scene tag, generates a working context, produces a scene frame document with style cards, composes the scene, audits it for story fit and internal quality, and optionally applies chosen fixes. Triggers include "produce a scene", "run the prose pipeline", "prose-producer".
---

# Prose Producer

Multi-stage orchestrator. User provides:
- `STORY_PATH` — full story outline
- `PRIOR_SCENE_PATH` — prior scene's prose file (omit / leave empty if this is scene 1)
- `SOURCE_PATH` — source style passage(s)
- `SCENE_TAG` — identifier for the scene to produce (e.g., scene number or label, like "Scene 2" or "dreamreel-s2")

## Setup

1. Verify `STORY_PATH` and `SOURCE_PATH` exist. Halt and report if missing.
2. If `PRIOR_SCENE_PATH` was provided, verify it exists. If not provided, treat as scene 1.
3. Confirm `SCENE_TAG` with the user if it isn't unambiguous from the inputs.

If at any stage a subagent fails or expected output files are missing, halt immediately and report the failure to the user.

## Prompt files

Each stage's agent prompt lives in its own file under `references/`. For each stage: read the prompt file, substitute the placeholders (e.g. `{STORY_PATH}`, `{SCENE_TAG}`, `{SCENE_FRAME_PATH}`) with the actual values captured so far, and pass the resulting text to the subagent.

## Stage 1 — Working Context (opus)

Launch a `general-purpose` subagent with `model: opus`. Prompt: `references/stage1-working-context.md`.

Substitute `{STORY_PATH}`, `{PRIOR_SCENE_PATH}`, `{SCENE_TAG}`.

Capture the returned path as `WORKING_CONTEXT_PATH`.

## Stage 2 — Scene Frame (sonnet)

Launch a `general-purpose` subagent with `model: sonnet`. Prompt: `references/stage2-cards.md`.

Substitute `{WORKING_CONTEXT_PATH}`, `{SOURCE_PATH}`, `{SCENE_TAG}`.

Capture the returned scene-frame path as `SCENE_FRAME_PATH`.

## Stage 3 — Compose (opus)

Launch a `general-purpose` subagent with `model: opus`. Prompt: `references/stage3-compose.md`.

Substitute `{WORKING_CONTEXT_PATH}`, `{SCENE_FRAME_PATH}`.

Capture the returned scene draft path as `SCENE_DRAFT_PATH`.

## Stage 4 — Review (opus)

Launch a `general-purpose` subagent with `model: opus`. Prompt: `references/stage4-review.md`.

Substitute `{SCENE_DRAFT_PATH}`, `{WORKING_CONTEXT_PATH}`, `{SCENE_FRAME_PATH}`.

Capture the returned post-scene summary path as `POST_SCENE_SUMMARY_PATH`. The scene draft path is unchanged (revised in place).

## Stage 5 — Audit (sonnet)

Launch a `general-purpose` subagent with `model: sonnet`. Prompt: `references/stage5-audit.md`.

Substitute `{SCENE_DRAFT_PATH}`, `{STORY_PATH}`, `{PRIOR_SCENE_PATH}`, `{SCENE_TAG}`.

Capture the returned audit card path.

## Review with User

Read the audit card yourself. Present the two lists (Story Fit, Internal Quality) to the user and ask which items, if any, they want applied to the scene draft. Accept their selections in any reasonable form (numbers, ranges, "all", "none", free-form).

If the user picks **none**, skip Stage 6 and go to Final Output.

## Stage 6 — Apply Fixes (sonnet, optional)

Only run if the user picked one or more fixes.

Launch a `general-purpose` subagent with `model: sonnet`. Prompt: `references/stage6-apply-fixes.md`.

Substitute `{SCENE_DRAFT_PATH}` and `{CHOSEN_EDITS_VERBATIM}` (the verbatim text of the edits the user picked).

## Final Output

Print to the user:
- Working context path
- Scene frame path
- Scene draft path
- Post-scene summary path
- Audit card path
- (If Stage 6 ran) brief note that fixes were applied
