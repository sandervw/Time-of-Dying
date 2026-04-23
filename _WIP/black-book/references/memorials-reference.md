# Memorials Mode

Write Memorials blobs for an existing breakdown. You receive a numbered breakdown and must produce only the Memorials-style blobs, preserving original numbers.

## Voice & POV

A Memorials blob is a **sequence of 2-4 discrete epitaphs** that feel semi-randomly adjacent, as if the reader has paused at a stretch of the Road of Graves and the stones happen to be ordered this way. Each epitaph stands alone. No narrative thread links them. The main character is not named, addressed, or referenced.

Register is **formal, elevated, compressed** — carved in stone, or written to feel that way. The mason charges by the letter; every syllable earns its place. Always declarative, never chatty.

Each epitaph is written in ONE of three POV modes:

1. **Eulogy** (3rd-person about the deceased) — biography + verdict. The communal tribute.
2. **Wayfarer Address** (2nd-person to the passing reader) — oracular admonition, compressed wisdom.
3. **Dead's Own Voice** (1st-person from the deceased) — rare, aphoristic. "As I am, so shall ye be."

**Living-writer 1st person ("I carved this for my brother...") is banned.** Memorials are not confessions.

Tense rules:
- **Past** for the biography of the dead.
- **Present** for the verdict, the toast, or the wisdom aimed at the reader.
- Both tenses often sit side by side in a single epitaph.

## Hard Rules

### Structure
1. Epitaph count matches the `(N)` in the breakdown header exactly (2, 3, or 4).
2. Epitaphs are separated by `---` horizontal rules. Nothing else between them.
3. Each epitaph is **5-60 words**.
4. **Total blob word count: up to 150 words.**
5. Format per epitaph is free: line-broken verse OR a single prose paragraph. Mix within a blob.

### POV Diversity
6. If the blob has **3 epitaphs**, at least **2 different POV modes** must appear.
7. If the blob has **4 epitaphs**, at least **3 different POV modes** must appear.
8. **No two adjacent epitaphs share the same POV mode.**

### Length Variety
9. If 3+ epitaphs, at least two must differ by **15+ words**. Do not write near-identical-length stones in a row.

### Content
10. **No dialogue. No quotation marks. No character speech.**
11. **No reference to the main character, the narrator, or current scene events.** These are strangers' graves.
12. **No connective tissue between epitaphs.** No "meanwhile," "nearby," "the next stone reads." Each stone is its own object.
13. **No stage directions, no italics framing, no bullet points.**
14. **No meta-commentary.** No "here lies a lesson," no "read this well." The epitaph itself is the lesson.
15. **No em-dashes** (per project rule). Use commas, semicolons, colons, or periods.

### Tone
16. Rhyme and meter are **allowed but never required**. If rhyme is used, it should feel like an actual stonecutter's choice, not a poem.
17. Avoid generic memorial clichés ("rest in peace," "gone but not forgotten"). The setting demands specificity: names, places, offices, deeds, curses, sins.

## What Memorials Blobs Cover

Memorials is the ambient-texture blob. Use it for:

- **Foreshadowing** — prefiguring the main character's potential fate through another's death.
- **Region lore** — dropping place-names, institutions, past events, regional customs, sins honored or reviled here.
- **Tone-setting** — establishing the mood of a location through the quality of its dead.
- **Threshold marking** — at the edge of a chrypt, tohmb, village, or region, the stones tell you what sort of place you are entering.
- **Cultural values expressed obliquely** — what this community mourned, celebrated, warned against.
- **Historical echo** — a distant past event half-remembered through its casualties.
- **Memento mori / death-philosophy** — compressed meditations on mortality, decay, the Wheel, the Road.
- **Unresolved mystery** — a strange death whose details hint at something larger.

Memorials is **not** for:
- The necromancer-narrator's reasoning (Essay).
- Canonical encyclopedia description of an entity (Lemma).
- A named NPC speaking in their own voice (Interview).
- In-the-moment action (Verse).

## Tone Targets

Think of three registers the examples in the source move between:

- **Eulogistic warmth** — a toast to the fallen, group or individual, affectionate specificity.
- **Lapidary stoicism** — biography stripped to its essentials, verdict delivered flat.
- **Oracular admonition** — wisdom aimed at the passing reader, weight of inherited knowing.

A single blob can traverse all three. That is the point of the sequence.

Avoid:
- Three eulogies in a row (monotone).
- All three stones at identical length (mason never does this).
- Modern euphemism ("passed away," "lost us"). Say died, fell, rotted, was taken, surrendered.
- Overt fantasy diction when plainness cuts deeper.

## Workflow

1. **Read the full breakdown** to understand the scene arc and where the Memorials blob sits.
2. **Read the blob's bullets.** Each bullet previews one epitaph. The bullet count equals the `(N)` in the header.
3. **Assign a POV mode to each bullet.** Check the diversity rules (3+: two modes; 4: three modes; never adjacent repeats).
4. **Draft each epitaph.** Vary length deliberately. Choose verse or prose per stone.
5. **Verify every hard rule.** Word counts, POV diversity, adjacency, no em-dashes, no dialogue, no main-character references, no connective tissue.
6. **Output only the Memorials blobs** under their original numbered headers.

## Output Format

```markdown
# [Scene Title] — Memorials Blobs

## 3. MEMORIALS (3)

[Epitaph 1, verse or prose, 5-60 words.]

---

[Epitaph 2.]

---

[Epitaph 3.]
```

Name the output file `[Scene-Title]-Memorials-Blobs.md`.

**CRITICAL:** Output ONLY Memorials blobs. Do not write other blob types. Do not renumber.

## Examples

### Example A — 3 epitaphs, mixed POV (Eulogy / Wayfarer / Dead's Voice)

## 2. MEMORIALS (3)

Here lies Osred Tallowhand, keeper of the ninth lantern on the Bone Mile. He trimmed the wick for forty years and never once let the road go dark. The road is dark now.

---

Wayfarer, the stones grow closer together past this marker. Do not mistake a quiet stretch for an empty one. The thickest silences belong to the loudest graves.

---

I was Mera, I was a cooper, I was owed three coin by the man who buried me. Ask him.

### Example B — 2 epitaphs, Eulogy + Wayfarer, length contrast

## 5. MEMORIALS (2)

Brethel, fell of the marsh-rot, aged nineteen. Buried by her sister. Buried well.

---

You who pause here: the ground beneath your feet is softer than the ground five paces on, and softer still five paces after that. The Road sinks where the dead are thickest. Read the sinking and you will read the ledger of this place. Move on before dusk.

### Example C — 4 epitaphs, rhymed eulogy + three others (demonstrating variety)

## 1. MEMORIALS (4)

Here drink to the dead of the Eighth Gate Watch:
Thom of the hook, who could patch any patch,
Red Una the brawler, whose fist was a latch,
Quiet Sib, who alone could hear the grave hatch.
None of them lived to see the batch.

---

Gromal the Flenser served two necromancers and neither remember his name. He is buried under the work he did for them.

---

As I am, so shall ye be. I was a tax collector.

---

Wayfarer, read no further. The next stone is a lie.
