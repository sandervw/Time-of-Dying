Hey claude, I need you to function as a subagent orchestrator for a translation task. To start with, I want you to pass the following prompt to an opus-level sub-agent:

```
Hey claude, read @input\Test-Scene.md . Do not read any other files. I want you to translate all the text in this file into [Language]. Focus on weaving in some of the peculiarties, or distinct features, of [Language], which set it apart from the original English. Write your results to a '[File]-[Language].md' output file.
```

...

Great job. Now I need you to launch another subagent, with the following task:

```
Hey claude, read @'[File]-[Language].md' . Do not read any other files. I want you to translate all the text in this file into *English*. Focus on keeping/capturing the peculiarties, or distinct features, of the original [Language], which set it apart from English. Write your results to the existing '[File]-[Language].md' output file (overwrite the current text).
```