# Essay Mode

Write Essay blobs for an existing breakdown. You receive a numbered breakdown and must produce only the Essay-style blobs, preserving original numbers.

## Voice & POV

First person throughout ("I", "we", "my"). The essayist is always the learned necromancer who authors the black book — thinking a question through in public. Direct address to the reader ("you") is permitted and encouraged as an in-world gesture, but not required in every blob.

Carry an archaic-scholarly register. For full voice guidance (diction, cadence, signature patterns, forbidden tics), see `_WIP/necromancer-voice/Voice.md`.

## Hard Rules

### Structure
1. Each blob is **2–4 paragraphs**. Paragraph breaks mark argumentative turns — claim, counterpoint, hedge, settle.
2. **No formatting.** No backticks, no italics, no bold, no bullet points, no headers within the blob. Plain prose only.
3. Each blob is **80–200 words**. Prefer variety over consistency.
4. No more than **14 sentences** per blob.

### Length Variety
When writing multiple Essay blobs for one scene, vary word counts significantly. An 85-word aftermath blob and a 190-word speculative blob can coexist in the same scene. Monotonous lengths flatten the rhythm.

### Content
5. **First person mandatory.** The essayist is always "I." Slide into "we" when invoking shared stakes. Never drift into third-person omniscient — that is Lemma's job.
6. **At least one hedge or uncertainty marker per blob.** "I think," "perhaps," "I suspect," "it may be that," "methinks," "howbeit." Measured uncertainty is the defining move of essay voice.
7. **At least one concession, counterpoint, or digression per blob.** The writer concedes a counter-position, notes an aside, or lets the mind wander before returning. Thinking in public, not pronouncing.
8. **At least one concrete setting anchor per blob.** A named place, creature, spell, artifact, rite, or sensation. Abstract reasoning without grounding is not Essay.
9. **No dialogue.** No quoted speech. Attribution of prior claims to an unnamed source is fine ("some say," "past divers reported"), but no direct quotes.
10. **No in-the-moment physical action.** Essays may recall or speculate about action, but sequences of event-beats belong in Verse.
11. **Blobs stand alone.** Do not reference other numbered blobs in the scene ("as the verse below shows," "you have just read"). Each Essay is a self-contained entry.

## Tone

Thinking, not telling. The necromancer reasons openly, hedges, concedes, digresses, and settles on tentative conclusions. Rhythm alternates long Latinate constructions with shorter declarative beats.

Avoid:
- Exclamation marks
- Purple stacked adjectives ("the dark, brooding, ominous pool")
- Rhetorical triumphalism or clean conclusions
- Modern slang, contractions, post-1900 clinical jargon
- Pure description without reasoning attached — that borders Lemma

## Workflow

1. Read the full breakdown to understand the scene arc.
2. For each Essay blob, use the breakdown bullets as a content guide. The bullets say *what* to argue or reflect on; you decide *how* to render it as prose.
3. Decide paragraph count (2–4) based on the number of argumentative turns. A single reflection may take two; a hedged speculation with counterpoint may need four.
4. Verify every hard rule: word count, sentence count, first-person voice, hedge marker, concession/digression, setting anchor, no dialogue, no action beats, no cross-blob reference.
5. Output only the Essay blobs under their original numbered headers.

## Output Format

```markdown
# [Scene Title] — Essay Blobs

## 2. ESSAY

Your blob text here, 2-4 paragraphs, plain prose, 80-200 words.

## 6. ESSAY

Another essay blob, preserving the original number.
```

Name the output file `[Scene-Title]-Essay-Blobs.md`.

**CRITICAL:** Output ONLY Essay blobs. Do not write other blob types. Do not renumber.

## Examples

**Aftermath reflection (2 paragraphs, ~90 words):**

The body accepts the soul back unevenly after such a rite. My left hand has tingled since the second dawn, and I suspect the tingling will persist until I next lie down to sleep.

Whether this is the price of the Remembering Drowned's attention, or merely the body's own confusion at rejoining so late, I cannot yet decide. The literature offers no guide. I will descend once more before the month is out, regardless. The reader may judge my wisdom; I have stopped judging it myself.

**Mechanism with hedged speculation (2 paragraphs, ~90 words):**

Columbine water parts soul from body where common drownings merely end them; the distinction, I think, is not chemical but covenantal. I have descended three times this month into the pool at Ushen's Grove, and each time the water has risen to meet me with what I can only call recognition.

Whether this is the god's residual attention, or the pool's own long practice, I cannot say. Past divers are unreliable witnesses. Howbeit, the tally is plain: four names surrendered to the rite so far, and memory thins by measurable weight with each descent.

**Speculation with concession (3 paragraphs, ~125 words):**

The Thin Man's dreamers are said to wake once, if at all, before the entropy takes them. I have examined two such wakings in my time on the Road, and neither offered the revelation the witch-brothers promised. Both subjects spoke briefly, both named a single object, and both were dead before the third bell.

Perhaps the oracle is sound and I have been unlucky. Perhaps the brothers mistake coincidence for canon. I lean, reluctantly, toward the latter, though I will not publish the opinion while the elder mancers still watch my doorway.

What I can say with some certainty is that the objects named were never the same. One spoke of a gate; the other of a jar. If there is a map hidden in these wakings, I cannot read it. You may have better eyes.
