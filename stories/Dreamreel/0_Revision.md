# Revision Steps

## Dialogue

Revise Wiermoth Dialogue

**TRANSLATING DIALOGUE:**
- Ask claude to translate one dialogue-heavy scene to japanese (sonnet? Opus?)
  - "Hey claude, read @REPLACE . Do not read any other files. I want you to translate all the dialogue (DIALOGUE ONLY) in this scene into Romanji. Focus on capturing the mystery or peculiarity of the original English language. Write your results to a '-temp.md' output file."
- Ask it to launch subagents for other scenes, with 'meta-notes' from its own translations, following your prompt
- THEN, in a new session, have a *different model* translate back to english (with meta-notes)
- Do the same subagent run

## Manual

Review/Revise Manually
- Compare the scene to your outline
- Compare to the scene to Time of Dying
- Your usual manual changes
- Focus on cutting/trimming

**Look for common LLM patterns** (things to have it avoid next time)

## Automatic (Make Claude do it)

Compare each manually-edited scene file to claude's output
- Break down differences for each file
- Ask claude to create editing guide for each file
- Ask claude to merge editing guides

Check for lore consistency
- possibly look for missed opportunities to weave in lore