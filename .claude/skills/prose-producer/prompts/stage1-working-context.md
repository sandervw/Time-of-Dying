Hey claude, read `{STORY_PATH}`. From this full story outline, and the prior scene file at `{PRIOR_SCENE_PATH}`, I want you to extract *just* the context an LLM would need to write the full {SCENE_TAG} of the story, without referencing any other documents. This should include all the text under the scene header, plus any *necessary* information from prior/future scenes. Anything the LLM won't put in the current scene, or affect the writing of the current scene, is *unnecessary*.

- *Necessary* info example: a secret revealed in the previous scene, that affects character relationships in the current one
- *Unnecessary* info example: a statement of belief from a prior scene, which doesn't affect the current scene
- Already-rendered character/location descriptions should be listed under "Already Rendered (DO NOT RE-DESCRIBE)"

The current scene's outline section must be preserved in full. A 20% compression target applies to all other context you extract; your extracted context must not exceed 20% of the full outline wordcount.

If no prior scene exists (scene 1), omit the "Already Rendered" and "Continuing State" sections, and omit "Ending Text (prior scene)".

Write your result to `output/working-context-{SCENE_TAG}.md` in the following form:

```markdown
# Scene {SCENE_TAG} Context

## Premise

[POV / tense / wordcount / brief premise — one paragraph distilled from the story outline]

## Current Scene Outline

[Preserved verbatim from the story outline — the full scene block]

## Prior Scene — Already Rendered (DO NOT RE-DESCRIBE)

Material the reader has already seen depicted in prose. Do not re-use.

- [List character physical descriptions, setting features, sensory details,
  and named props that have already been rendered in the prior scene(s).]

## Prior Scene — Continuing State

Material that persists into this scene and may need to be referenced.

- [Physical positions of characters at the moment this scene picks up,
  emotional states, in-progress conversations, active props or beats that
  carry forward.]

## Necessary Backward/Forward Context

[Secrets revealed in earlier scenes that bear on this one; plot threads
activated upstream; foreshadowing or planted detail required for future
scenes. Only include what genuinely affects the writing of THIS scene.]

## Ending Text (prior scene)

[The final ~50 words from the prior scene. Begin with '...' if necessary.]
```

Report back the absolute path of the working-context file written.
