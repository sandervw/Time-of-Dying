---
name: prose-producer
description: Orchestrates a full scene draft. Given a scene outline, source style passage, and full story outline, generates four style cards, composes the scene, audits it for story fit and internal quality, and optionally applies chosen fixes. Triggers include "produce a scene", "run the prose pipeline", "prose-producer".
---

# Prose Producer

Multi-stage orchestrator. User provides three file paths:
- `OUTLINE_PATH` — scene outline / idea
- `SOURCE_PATH` — source style passage(s)
- `STORY_PATH` — full story outline

## Setup

1. Verify all three files exist. Halt and report if any is missing.
2. Derive `SCENE_TAG` from the content of `OUTLINE_PATH`.

If at any stage a subagent fails or expected output files are missing, halt immediately and report the failure to the user.

## Stage 1 — Cards (sonnet)

Launch a `general-purpose` subagent with `model: sonnet`. Prompt it with:

> Read ONLY these two files plus files inside the relevant skill folders:
> - Scene outline: `{OUTLINE_PATH}`
> - Source passage: `{SOURCE_PATH}`
>
> Use scene-tag `{SCENE_TAG}` for all card filenames. Derive a short source-tag from the source filename for source-imprint.
>
> Invoke these four skills, each producing one card under `output/`:
> 1. `scene-parameters` (uses scene outline)
> 2. `source-imprint` (uses source passage)
> 3. `speech-rules` — one card per speaking character mentioned in the outline (uses scene outline)
> 4. `forbidden-patterns` in PREDICTIVE mode (uses scene outline)
>
> Do not read any files outside the two listed inputs and the skill folders. Do not write anywhere except `output/`.
>
> Report back the absolute paths of every card file written, clearly labelling which is the blacklist card.

Capture the returned card paths.

## Stage 2 — Compose (opus)

Launch a `general-purpose` subagent with `model: opus`. Prompt it with:

> Read ONLY these files plus files inside the scene-writer skill folder:
> - Scene outline: `{OUTLINE_PATH}`
> - The four cards from Stage 1: `{CARD_PATHS}`
>
> Do NOT read the source style passage or any other file.
>
> Invoke the `scene-writer` skill, following its workflow exactly. Treat the four cards as binding constraints throughout drafting and review.
>
> Write all output files under `output/`.
>
> Report back the absolute paths of the scene draft file and the post-scene summary file.

Capture the returned scene draft path.

## Stage 3 — Audit (sonnet)

Launch a `general-purpose` subagent with `model: sonnet`. Prompt it with:

> Read ONLY these files plus files inside the scene-audit skill folder:
> - Scene draft: `{SCENE_DRAFT_PATH}`
> - Full story outline: `{STORY_PATH}`
>
> Do NOT read any other file.
>
> Invoke the `scene-audit` skill, following its workflow exactly. Use scene-tag `{SCENE_TAG}` for the audit filename. Save under `output/`.
>
> Report back the absolute path of the audit card.

Capture the returned audit card path.

## Review with User

Read the audit card yourself. Present the two lists (Story Fit, Internal Quality) to the user and ask which items, if any, they want applied to the scene draft. Accept their selections in any reasonable form (numbers, ranges, "all", "none", free-form).

If the user picks **none**, skip Stage 4 and go to Final Output.

## Stage 4 — Apply Fixes (sonnet, optional)

Only run if the user picked one or more fixes.

Launch a `general-purpose` subagent with `model: sonnet`. Prompt it with:

> Read ONLY:
> - Scene draft: `{SCENE_DRAFT_PATH}`
>
> Apply the following edits to the scene draft, in place. Preserve all surrounding prose. Do not introduce changes beyond what is listed.
>
> Chosen edits:
> {CHOSEN_EDITS_VERBATIM}
>
> Report back the absolute path of the edited scene file and a brief summary of the changes you made.

## Final Output

Print to the user:
- Scene draft path
- Post-scene summary path
- Audit card path
- (If Stage 4 ran) brief note that fixes were applied
