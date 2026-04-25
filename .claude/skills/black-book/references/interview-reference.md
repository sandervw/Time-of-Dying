# Interview Mode

Write Interview blobs for an existing breakdown. You receive a numbered breakdown and must produce only the Interview-style blobs, preserving original numbers.

## Voice & POV

First person throughout — the named NPC speaks. The main character ("you") **never** answers; the bolded prompts stand in for the unseen interviewer. The reader eavesdrops rather than being addressed directly.

Register is **candid and colloquial** — transcribed speech, not composed prose. This is the key split from Essay: Essay is the scholarly necromancer-author reasoning in public; Interview is any NPC talking in their own voice, tics and all. The register shifts per character (learned, blunt, broken, etc.).

Tense is anchored in the present (the moment of answering), with past-tense excursions for anecdote and occasional future for speculation.

## Hard Rules

### Structure
1. Each blob has **2–4 Q/A exchanges**, matching the `(N)` in the breakdown header exactly.
2. Each exchange is: **bolded prompt** on its own line, then response paragraph below.
3. Prompt is **1–6 words**, typically a fragment: `**Sources?**`, `**And after?**`, `**The fourth dive**`. Statement fragments and single nouns are legal.
4. Response is **1–80 words**, 1–4 sentences.
5. **Total blob word count: 20–200 words.**

### Length Variety
6. If 3+ exchanges, at least two responses must differ by **15+ words**. Mix a long candid turn with clipped ones. Do not write three near-identical-length answers.

### Content
7. **First person mandatory.** Never drift to third-person omniscient.
8. **At least one verbal tic, hesitation, or digression per blob.** "Well," "I mean," "in sooth," trailing off, self-interruption, an aside that wanders before returning. The blob must read as *spoken*.
9. **The NPC must have an agenda.** Confession, complaint, boast, warning, evasion, pitch.
10. **The main character never speaks.** No quoted speech from "you" — the bolded prompts are the only intrusion.
11. **No stage directions or narration.** No "he said," no action beats, no description of the speaker between lines.
12. **No meta-dialogue.** No "as I was saying," "let me explain," "listen carefully." The NPC just speaks.
13. **"I" dominates over "you."** The respondent is revealing themselves or the world, not addressing the interviewer as the subject.

### Consecutive Interview Blobs
14. Interview has an adjacency limit of 2 in the breakdown. If the breakdown places three or more Interview blobs back-to-back, flag it.

## What Interview Blobs Cover

Interview is the most character-driven blob. Use it for:

- **Confessions & revelations**: Something an NPC has been holding back.
- **Backstory & motive**: Personal history conveyed through voice, not exposition.
- **Lore through personality**: World detail filtered through a specific speaker's biases.
- **Aftermath reactions**: An NPC's response to events the reader has just witnessed.
- **Breather beats**: Placed after Verse or heavy Essay to slow the pulse.

Interview is **not** for:
- The narrator-necromancer's reasoning (that is Essay)
- Environmental or canonical description (Lemma)
- In-the-moment action (Verse)
- Inscribed stone-voice (Memorials)

## Tone

The NPC should sound like a *person* — with *excrutiatingly-specific* verbal habits, priorities, and a way of speaking.

Avoid:
- All responses at the same length or emotional register
- Prompts as full polite questions ("Could you tell me about...") — keep them fragmentary
- Generic interviewee-speak ("That's a great question. Well, it all began...")

## Workflow

1. **Read the full breakdown** to understand the scene arc and where Interview blobs sit.
2. **Identify the named NPC and circumstance** from the breakdown header.
3. **Determine the NPC's agenda and voice.** What do they want from this exchange? How do they speak?
4. **For each blob**, use the breakdown bullets as a content guide. The bullets say *what* is conveyed; you decide *how* — vocabulary, cadence, tics, digressions.
5. **Verify every hard rule**: exchange count matches header, word counts per response and total, length variety, first person, verbal tic present, no stage directions, prompt formatting.
6. **Output only the Interview blobs** under their original numbered headers.

## Output Format

```markdown
# [Scene Title] — Interview Blobs

## 4. INTERVIEW (3) — [Character Name], [optional circumstance]

**Prompt fragment**
Response paragraph in candid first-person voice, 15–80 words.

**Next prompt**
Next response.

**Third prompt**
Third response.
```

Name the output file `[Scene-Title]-Interview-Blobs.md`.

**CRITICAL:** Output ONLY Interview blobs. Do not write other blob types. Do not renumber.

## Examples

## 7. INTERVIEW (3) — Brack the Grave-digger, end of shift

**The day's toils**
Aye. Three pits and a reburial, and the reburial were the old trader what they pulled face-down out of the marsh-run. You know the one. I had to use the hook.

**The hook?**
The flensing hook, aye.

**Trouble in the trade**
No trouble from him. His hands were all knit up with bloodroot. From his widow, maybe. She's coming at dawn with the priest, and she'll want to see the face. Good luck to her.

## 11. INTERVIEW (4) — Ollet, who sits in the rear pew

**Name**
My name is Ollet.

**A keepsake?**
Do you want to see what I have in my pocket? I have a thing. A tooth. A big one, not mine. Mine are all still in, see? But this one came out of the wall by the altar, and I keep it and I keep it.

**Sleep**
Sometimes I sleep when the big shadow isn't walking.

**Shadow?**
It walks a lot. It walked last night, and I didn't, and now my head is full of quiet wasps.
