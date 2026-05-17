# CLAUDE.md

A *Time of Dying* fiction project.
- `Stories/` - In progress and completed stories/narratives
- `Output/` - Default destination for generated files (unless the user specifies otherwise)

After creating a new document, ask the user if they want you to run text-trimmer or draft-editor.

When counting words in a file, always use `wc -w <file>`

**`/tod-context` is your most important skill**; use it when creating fiction content.

All skills referenced by name live in this project at `<project>/.claude/skills/<name>/`, never in `~/.claude/skills/`. Pass absolute paths to subagents.

"*subtext*" in an outline indicates material that should not be given directly in a scene - it should be hinted as obliquely as possible

## Naming Guidelines

Where possible, run `python sampling.py names 10` from within the `setting/` subdirectory to generate names. Lean into this inspiration, but create NEW names. Do not fall back to default fantasy templates.
- *locations* Always use the following FORMS: "[Owner]'s [Place]", "[Noun] of [Noun(s)]", "The [Adj] [Noun]", Bare "[Adj/Noun] [Noun]", Welded compound (one word), etc.
- *Character names* Always use the following FORMS: compound descriptive phrases, Germanic/Old English roots, animal-adjacent words, dark irony or oxymoron, Compound neologisms, etc.
- *Spell/magic naming* Also run `python sampling.py spells 7` for example format.