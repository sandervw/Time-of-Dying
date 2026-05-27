Hey claude, I need you to function as a subagent orchestrator for a revision task. I want you to pass the following prompt to three opus-level sub-agents:

```
Hey claude, read @{FILE} . Do not read any other files. I want you to use your /tod-context skill to revise this scene draft file. DO NOT reuse sampled context vertabim, use it as the inspiration for new context. Focus on replace any generalized elements of the prose with ToD-setting specific elements. Keep your edits as minimal as possible: you are not rewriting the story, changing the plot, changing the characters, or making other large-scale revisions. You are trying to insert minimal elements from the Time of Dying that bring this story in as a *new* source of lore for the setting. Your final wordcount must not exceed 105% of the original wordcount.
```

Each agent should be given one of three scene files (1-3) from @stories\Dreamreel\Scenes\ .

Any questions?

...


Actionable passes to make prose more concrete, specific, and showing.

1. Convert plural objects/elements into singular ones with a descriptive tag.
2. Replace general descriptive attributes ("wood") with specific ones ("chestnut").
3. Swap abstract nouns ("violence") for the act ("a boot on his wrist").
4. Replace adverbs with the gesture they summarize ("said angrily" becomes a slammed cup).
5. Name brands, species, makes: not "a car," a rusted Corolla.
6. Attach a number where you wrote "many" or "some."
7. Give one sense per beat you'd normally skip: smell, temperature, texture.
8. Cut "seemed/felt like"; state it.
9. Anchor emotion in body, not label.
10. Trade "walked" for how they walked.
11. Replace "things/stuff" with the actual object.