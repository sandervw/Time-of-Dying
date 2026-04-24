# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Time of Dying is a collaborative fiction project built for iterative composition with Claude AI. The setting is a necromantic world born from seven necromancers who destroyed all other life, magic, and gods three thousand years ago. Civilization clings to the Road of Graves, an ever-expanding road paved with gravestones of the dead, while the seven necromancer-gods, each bound to a deadly sin and cursed with pseudo-immortality, are still worshipped. Necromancy (called Deadspeech) is the only surviving magic, and the restless dead are varied and common.

## Content Structure

Setting documents are organized hierarchically:

- **Setting/Time-of-Dying.md** - Setting overview for the Time-of-Dying project.
- **Setting/Folklore.md** - Random setting folklore. A good source when asked to generate story ideas.
- **Setting/Ideas.md** - Running scratchpad / todo list for rough ideas and notes. Items here are incorporated or discarded, then deleted from the doc.
- **Setting/Mythology.md** - The main setting summary. Maps setting details to specific myth categories.
- **Setting/Folklore/** - Detailed documents for random pieces of generated folklore that has been confirmed as part of the setting. Only reference this if requested by the user.
- **Setting/Mythology/** - Deep-dive expansions of individual mythology elements (cosmogony, cosmology, theogony, anthropogeny, magic systems, etc.).
- **Setting/Archive/** - Holding pen for old or unused setting and story documents. Never access this folder unless directed by the user.
- **Stories/** - In progress and completed stories/narratives
- **Output/** - Default destination for files generated via skills and agents (unless the user specifies otherwise)

**IMPORTANT:** after creating a new document, ask the user if they want you to run a text-trimmer or draft-editor subagent on the result document.

## Vocabulary Lookups

Before reading full markdown files in `setting/`, check whether the info you need matches one of the array headers in `setting/vocabulary.json`. If it does, run the sampling script from the `setting/` folder. **Never read the full `vocabulary.json` file.** Use the sampling script to pull the full array for the term you need.

- Spells: `python sampling.py spells`
- Ceremonies, Rituals, Rites: `python sampling.py ceremonies_rituals_rites`
- Curses, Afflictions: `python sampling.py curses_affliction`
- Mundane Necromantic Duties: `python sampling.py mundane_necromantic_duties`
- Astrological/Religious Events: `python sampling.py astrological_religious_events`
- Titles, Roles: `python sampling.py titles_roles`
- Necromancy Supplies: `python sampling.py necromancy_supplies`
- Locations: `python sampling.py locations`
- Undead: `python sampling.py undead`
- Cosmologisms: `python sampling.py cosmologisms`
- Epithets: `python sampling.py epithets`

## Writing Conventions

When generating or editing setting/story content:

### Naming

**STOP** - before writing a name in this setting, check if it falls into a category below:
- **location names** Run `python sampling.py names 10`. This your inspiration - create NEW names, in the following FORMS: "[Owner]'s [Place]", "[Noun] of [Noun(s)]", "The [Adj] [Noun]", Bare "[Adj/Noun] [Noun]", Welded compound (one word), etc.
- **Character names** Run `python sampling.py names 10`. This your inspiration - create NEW names, in the following FORMS: compound descriptive phrases, Germanic/Old English roots, animal-adjacent words, dark irony or oxymoron, Compound neologisms, etc.
- **Object/item names** run `python sampling.py necromancy_supplies 7`. This your inspiration - create NEW names from this model.
- **Spell/magic naming** run `python sampling.py spells 7`. This your inspiration - create NEW names from this model.
- **Setting-specific spellings:** "Chrypt" replaces "Crypt" and "Tohmb" replaces "Tomb" in all setting content.

### Tone and Aesthetic

- **Visceral sensory detail across all five senses.** Always ground horror in specific sensations: cartilage crunch, sweet sweat, burned hair, chalky cracked teeth, slimy greens, arrhythmic heart pounding. Never settle for abstract "it was terrifying."
- **Body horror meets domestic familiarity.** Kitchen knives, carpets of rat skins, roaches over moldy meat, a pig giving birth to a cat. The grotesque lives in everyday objects and spaces, not just monsters.
- **Industrial decay fused with organic rot.** Rusty nails alongside fungus through flesh. Wrought-iron gates beside melting trees. Metal and bone occupy the same register.
- **Dark humor threaded through horror.** Speech Cheese, Snot Waffle, Toke Eater. The setting allows absurdity and irony without breaking tone. Comedy and horror coexist; neither cancels the other.
- **No sanitizing, no euphemism.** Call things what they are. Severed heads, ruptured capillaries, organ harvesting. The language is direct, blunt, and unflinching.
- **Never use em-dashes.**

## Agents (.claude/agents/)

- **draft-editor** - Prose editing specialist. Analyzes draft fiction for structural, craft, and surface-level weaknesses (conflict, subtext, movement, metaphor density, sentence/paragraph variety), then produces a revised draft. Three phases: Analyze, Report, Revise.
- **fiction-tagger** - Extracts short feature tags (threats, locations, weapons, character traits) from fictional sources via web search or local file. Outputs JSON tag lists.
- **text-trimmer** - Compresses and restructures text documents to 70% of original token count while optimizing for LLM readability.

## Skills (.claude/skills/)

- **character-analysis** - Analyzes fictional characters into structured profiles. Four mutually exclusive modes: profile, description, actions, quotes.
- **character-abstraction** - Strips setting-specific details from character elements (actions, quotes) to produce reusable templates.
- **fiction-abstraction** - Same idea as character-abstraction but for narrative elements: paragraphs and dialogue. Generalizes source-specific prose into templates.
- **literary-revision** - Rewrites prose in a specific literary style while preserving narrative.
- **folklore-generator** - Generates folklore for any observable object or phenomenon. Multi-step workflow with sequential reference loading.
- **scene-writer** - Writes complete prose scenes from a story background and scene outline. Multi-phase workflow - develops narrative through structured phases.
- **story-idea-generator** - Generates original story premises by colliding two unrelated elements. Multi-step workflow with sequential reference loading.
