---
name: prose-producer
description: Orchestrates a full scene draft. Given a full story outline, prior scene prose, source style passage, and a scene tag, generates a working context, produces four style cards, composes the scene, audits it for story fit and internal quality, and optionally applies chosen fixes. Triggers include "produce a scene", "run the prose pipeline", "prose-producer".
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

## Stage 1 — Working Context (sonnet)

Launch a `general-purpose` subagent with `model: sonnet`. Prompt it with:

> Hey claude, read `{STORY_PATH}`. From this full story outline, and the prior scene file at `{PRIOR_SCENE_PATH}`, I want you to extract *just* the context an LLM would need to write the full {SCENE_TAG} of the story, without referencing any other documents. This should include all the text under the scene header, plus any *necessary* information from prior/future scenes. Anything the LLM won't put in the current scene, or affect the writing of the current scene, is *unnecessary*.
>
> - *Necessary* info example: a secret revealed in the previous scene, that affects character relationships in the current one
> - *Unnecessary* info example: a statement of belief from a prior scene, which doesn't affect the current scene
> - Already-rendered character/location descriptions are NOT unnecessary — list them under "Already Rendered (DO NOT RE-DESCRIBE)" so the composer knows to avoid them. Omitting them lets the composer re-render from instinct.
>
> The current scene's outline section is preserved in full; the 20% compression target applies only to the cross-scene context you extract (Already Rendered + Continuing State + necessary backward/forward facts), not to the current scene's own outline block.
>
> If no prior scene exists (this is scene 1), omit the "Already Rendered" and "Continuing State" sections, and omit "Ending Text (prior scene)".
>
> Write your result to `output/working-context-{SCENE_TAG}.md` in the following form:
>
> ```markdown
> # Scene {SCENE_TAG} Context
>
> ## Premise
>
> [POV / tense / wordcount / brief premise — one paragraph distilled from the
> story outline's premise section]
>
> ## Current Scene Outline
>
> [Preserved verbatim from the story outline — the full scene block, including
> all beats, details, character bullets, lore notes, and (withheld) markers]
>
> ## Prior Scene — Already Rendered (DO NOT RE-DESCRIBE)
>
> Material the reader has already seen depicted in prose. Reference obliquely
> if it must come up again (a phrase, a callback) but do not paint it fresh.
> Treat as established fact, not as texture inventory.
>
> - [List character physical descriptions, setting features, sensory details,
>   and named props that have already been rendered in the prior scene(s).]
>
> ## Prior Scene — Continuing State
>
> Material that persists into this scene and may need fresh prose handling.
>
> - [Physical positions of characters at the moment this scene picks up,
>   emotional states, in-progress conversations, active props or beats that
>   carry forward.]
>
> ## Necessary Backward/Forward Context
>
> [Secrets revealed in earlier scenes that bear on this one; plot threads
> activated upstream; foreshadowing or planted detail required for future
> scenes. Only include what genuinely affects the writing of THIS scene.]
>
> ## Ending Text (prior scene)
>
> [The final paragraph or two of the prior scene, verbatim, so the composer
> can pick up cleanly without re-establishing.]
> ```
>
> Report back the absolute path of the working-context file written.

Capture the returned path as `WORKING_CONTEXT_PATH`.

## Stage 2 — Cards (sonnet)

Launch a `general-purpose` subagent with `model: sonnet`. Prompt it with:

> Read ONLY these two files plus files inside the relevant skill folders:
> - Scene working context: `{WORKING_CONTEXT_PATH}`
> - Source passage: `{SOURCE_PATH}`
>
> Use scene-tag `{SCENE_TAG}` for all card filenames. Derive a short source-tag from the source filename for source-imprint.
>
> Invoke these four skills, each producing one card under `output/`:
> 1. `scene-parameters` (uses the scene working context)
> 2. `source-imprint` (uses the source passage)
> 3. `speech-rules` — one card per speaking character mentioned in the working context's "Current Scene Outline"
> 4. `forbidden-patterns` in PREDICTIVE mode (uses the scene working context)
>
> Do not read any files outside the two listed inputs and the skill folders. Do not write anywhere except `output/`.
>
> Report back the absolute paths of every card file written, clearly labelling which is the blacklist card.

Capture the returned card paths.

## Stage 3 — Compose (opus)

Launch a `general-purpose` subagent with `model: opus`. Prompt it with:

> Read ONLY these files plus files inside the scene-writer skill folder:
> - Scene working context: `{WORKING_CONTEXT_PATH}`
> - The four cards from Stage 2: `{CARD_PATHS}`
>
> Do NOT read the source style passage, the full story outline, the prior scene file, or any other file.
>
> Material listed under "Already Rendered (DO NOT RE-DESCRIBE)" in the working context has been depicted in prior scenes. Treat it as established fact. You may reference it obliquely (a phrase, a callback) but do not re-describe character appearances, setting features, or sensory details that have already been rendered. New material this scene introduces is fair game for full prose treatment.
>
> Invoke the `scene-writer` skill, following its workflow exactly. Treat the four cards as binding constraints throughout drafting and review.
>
> Write all output files under `output/`.
>
> Report back the absolute paths of the scene draft file and the post-scene summary file.

Capture the returned scene draft path.

## Stage 4 — Audit (sonnet)

Launch a `general-purpose` subagent with `model: sonnet`. Prompt it with:

> Read ONLY these files plus files inside the scene-audit skill folder:
> - Scene draft: `{SCENE_DRAFT_PATH}`
> - Full story outline: `{STORY_PATH}`
> - Prior scene prose (if any — omit if this is scene 1): `{PRIOR_SCENE_PATH}`
>
> Do NOT read any other file.
>
> Invoke the `scene-audit` skill, following its workflow exactly. Use scene-tag `{SCENE_TAG}` for the audit filename. Save under `output/`.
>
> Report back the absolute path of the audit card.

Capture the returned audit card path.

## Review with User

Read the audit card yourself. Present the two lists (Story Fit, Internal Quality) to the user and ask which items, if any, they want applied to the scene draft. Accept their selections in any reasonable form (numbers, ranges, "all", "none", free-form).

If the user picks **none**, skip Stage 5 and go to Final Output.

## Stage 5 — Apply Fixes (sonnet, optional)

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
- Working context path
- Card paths
- Scene draft path
- Post-scene summary path
- Audit card path
- (If Stage 5 ran) brief note that fixes were applied
