# Verse Mode

Write the Verse blobs for an existing breakdown. You are given a numbered breakdown file and must produce only the Verse-style blobs, preserving their original numbers.

## Voice & POV

First person, past tense throughout. The necromancer is recounting action after-the-fact — never livetexting mid-crisis. The reader eavesdrops on a scholar's post-hoc scrawl, not a play-by-play.

Register is **archaic-scholarly** in the Ashton-Smithian vein: inverted syntax, archaic connectives, Latinate vocabulary, biblical/high-fantasy cadence. For full voice guidance  **read `_WIP/necromancer-voice/Voice.md`** before drafting.

## Hard Rules

These are non-negotiable. Violate none of them.

### Structure (bubbles & groups)
1. **Split at clause-level punctuation.** Semicolons, colons, and commas joining independent clauses or stacking fronted adverbials are bubble boundaries. Parenthetical commas (around appositives, inline qualifiers, mid-clause asides) stay INSIDE their bubble.
2. **Drop terminal punctuation on each bubble.** The line break replaces the comma, semicolon, colon, or period that originally ended the clause. Internal punctuation inside a bubble is retained.
3. **Stack bubbles within a sentence with no blank line between them.** Adjacent lines, back to back.
4. **Separate sentences with blank line / `...` on its own line / blank line.** The ellipsis stands in for the period and signals the drawing of breath before the next barrage.
5. **Per-bubble length: 3–25 words.**
6. **Per-group word count: 40–90 words** (a "group" = the stacked bubbles of one source sentence).
7. **Per-group bubble count: 3–8 bubbles.**

### Blob-level
8. **Per-blob group count: 3–6 sentence-groups.**
9. **Per-blob total word count: 50–200 words.**
10. **Preserve the preamble / development / revelation arc within each sentence.** The key information lands on the LAST bubble of the group, not the first.

### Length Variety
11. When a blob has multiple groups, **vary group lengths.** Do not stack three near-identical-length groups. Mix a long barrage with clipped ones.

### Content
12. **First person mandatory.** Never drift to second or third person.
13. **Past tense.** The narrator is recounting, not livetexting.
14. **Interiority is allowed but must be momentary** — a single reflective clause threaded through action ("I knew then that..."). It may never replace the action beat or dominate a group.
15. **No texting-native tics.** No emoji, no lowercase drift, no contractions introduced by the format, no timestamps, no typing indicators, no greetings, no sign-offs.
16. **No em-dashes, no exclamation marks, no ellipses as filler.** Ellipses are reserved for the sentence-break separator only.

### Consecutive Verse Blobs
17. When 2–3 Verse blobs appear consecutively in the breakdown, treat them as **escalating phases** of a single event (phase 1 → phase 2 → resolution). Each phase raises stakes or changes conditions.

## What Verse Blobs Cover

Verse blobs are for moments where the necromancer is recounting physical action:
- **Combat**: duels, ambushes, monstrous encounters, casting under pressure
- **Traversal**: flight, chase, descent, crossing of hazards
- **Sudden events**: trap-springs, intrusions, eruptions, apparitions
- **Rite-work under duress**: casting, inscribing, banishing mid-crisis

If a breakdown beat is reflection, exposition, or inscribed wisdom, it is NOT a Verse blob.

## Tone

The narrator is a scholar who has survived the event and is scrawling it out in the voice he reads in. There is personality, but it is archaic, ornate, and restrained — never modern, never flippant.

Avoid:
- Modern idioms, casual contractions the base voice would refuse
- Questions directed at the reader
- Meta-commentary ("this was a rough one")
- Padding short bubbles or trimming long ones to even them out

## Quick Test

A Verse blob passes if:

1. Restoring terminal punctuation at the end of each bubble and concatenating produces fluent source-register prose.
2. Each group's FINAL bubble carries the key revelation of that sentence.
3. No bubble has been invented, condensed, or rephrased beyond what the base voice would produce.
4. No bubble contains a texting-native tic (emoji, lowercase, contraction, fragment, sign-off).
5. A reader can count sentences by counting ellipsis-lines plus one.

## Workflow

1. **Read the full breakdown** to understand scene arc and where Verse blobs sit.
2. **Read `_WIP/necromancer-voice/Voice.md`** for full register guidance.
3. **For each Verse blob in the breakdown**, draft the prose from the bullet content, then split into bubbles per the hard rules.
4. **Verify every hard rule** (bubble length, group length, blob length, group count, tense, POV, formatting separators).
5. **Output only the Verse blobs**, each under its original numbered header.

## Output Format

```markdown
# [Scene Title] — Verse Blobs

## 3. VERSE

First bubble of the first group
second bubble
third bubble
final bubble carrying the revelation

...

First bubble of the second group
second bubble
final bubble

## 5. VERSE

[next verse blob, preserving its original number]
```

The output file should be named `[Scene-Title]-Verse-Blobs.md`.

**CRITICAL:** Output ONLY Verse blobs. Do not write blobs for any other style. Do not renumber — preserve the exact numbers from the input breakdown.

## Example

Given breakdown blob:

```
## 3. VERSE
- Third plunge into the columbine pool; water takes him gladly
- Ghost-self rises through the inverted maze; body sinks
- The Remembering Drowned waits, wearing his face
- Strips of memory peel as he navigates the walls
- Finds the final glyph an instant before the entity speaks his name
- Surfaces gasping, one name poorer than before
```

Written output:

## 3. VERSE

Then cast I my body a third time into the columbine pool
and the water took me gladly, as one takes back a long-promised kinsman
and my ghost-self rose through the inverted maze
while the flesh of me sank

...

And the Remembering Drowned was there in the wet dark
wearing my face this time
and strips of memory peeled from me as I navigated the walls
each stripe a year surrendered

...

Howbeit I found the final glyph
an instant, no more
before the entity should speak my name
and therewith I surfaced gasping into the living air
one name the poorer
