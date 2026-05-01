# CLAUDE.md

A fiction project for iterative composition with Claude AI.
- **Stories/** - In progress and completed stories/narratives
- **Output/** - Default destination for generated files (unless the user specifies otherwise)

**After creating a new document**, ask the user if they want you to run text-trimmer or draft-editor.

Never combine cd with output redirection in a single bash command - split into separate tool calls to avoid manual approval prompts in VS Code

## Naming Guidelines

Where possible, run `sampling.py` as below. Lean into this inspiration, but create NEW names. Mirror the register and form of the samples; do not fall back to default fantasy templates.

Run commands from within the `setting/` subdirectory.
- **locations** Run `python sampling.py names 10`.  Always use the following FORMS: "[Owner]'s [Place]", "[Noun] of [Noun(s)]", "The [Adj] [Noun]", Bare "[Adj/Noun] [Noun]", Welded compound (one word), etc.
- **Character names** Run `python sampling.py names 10`. Always use the following FORMS: compound descriptive phrases, Germanic/Old English roots, animal-adjacent words, dark irony or oxymoron, Compound neologisms, etc.
- **Object/item names** run `python sampling.py necromancy_supplies 7`.
- **Spell/magic naming** run `python sampling.py spells 7`.