# Revision Steps

## Automatic (Make Claude do it)

Revise dialogue

Run prose-pruner

Check for lore consistency

Edit for specificity:
```
Hey claude, I need you to function as a subagent orchestrator for a revision task. I want you to pass the following prompt to three opus-level sub-agents:

PROMPT_START:
Hey claude, read @{FILE} . Do not read any other files. I want you to revise and overwrite this scene file. Your goal is to make the scene more concrete and specific by apply the set of actionable changes below:
1. Convert plural objects/elements into singular ones with a descriptive tag.
2. Replace general descriptive attributes ("wood") with specific ones ("chestnut").
3. Swap abstract nouns ("violence") for the act ("a boot on his wrist").
4. Replace adverbs with the gesture they summarize ("said angrily" becomes a slammed cup).
5. Attach a number where you wrote "many" or "some."
6. Cut "seemed/felt like"; state it.
7. Trade "walked" for how they walked.
8. Replace "things/stuff" with the actual object.

Keep your edits as minimal as possible: you are not rewriting the story, changing the plot, changing the characters, or making other large-scale revisions. You are making minimal adjustments which add specificity to the scene. Your final wordcount must not exceed 105% of the original wordcount. Remember: cutting/replacing is better than adding.
PROMPT_END:

Each agent should be given one of three scene files (scenes 7-9) from @stories\Dreamreel\Scenes\ . Scenes 1-6 are already done.

Any questions?
```

## Manual

Review/Revise Manually
- Compare the scene to your outline
- Compare to the scene to Time of Dying
- Your usual manual changes
- Focus on cutting/trimming

**Look for common LLM patterns** (things to have it avoid next time)

## Automatic

Run final spelling/grammar

Run final sanity check