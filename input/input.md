Hey claude, I need you to function as a subagent orchestrator for a revision task. I want you to pass the following prompt to three opus-level sub-agents:

```
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
```

Each agent should be given one of three scene files (1-3) from @stories\Dreamreel\Scenes\ .

Any questions?

...