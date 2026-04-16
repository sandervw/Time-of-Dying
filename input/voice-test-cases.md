# Voice Guide Test Cases

Use these test cases to evaluate dialogue voice guides built from the voice template. Each case provides input text and/or notes for the LLM, which should be paired with a completed voice guide and the matching instruction type.

---

## Category A: Write New Dialogue From Notes

No source text. The LLM receives only the voice guide and a situation description. Tests whether the guide alone is enough to produce recognizable, consistent voice.

---

### A1: Negotiation Under Pressure

**Instruction:** Write 4-6 lines of dialogue for the character. No narration.

**Situation:** The character is bargaining for passage on a river barge. The barge captain has named an outrageous price. The character has no money but does have a stolen religious artifact hidden in their bag. A third party, a priest, is watching the negotiation with suspicion.

---

### A2: Explaining Away a Disaster

**Instruction:** Write 3-5 lines of dialogue for the character. No narration.

**Situation:** The character has accidentally set fire to a stable. The stable owner and two bystanders are confronting them. The character needs to deflect blame, minimize the damage, and ideally extract themselves without paying for anything. One of the horses survived but is badly singed.

---

### A3: Monologue While Alone

**Instruction:** Write a short monologue (6-10 sentences) spoken aloud by the character while alone.

**Situation:** The character is standing on a battlement at dawn, looking out over a ruined city they once ruled. They have just learned that their closest ally has betrayed them. No one else is present. The character is processing the betrayal and deciding what to do next.

---

## Category B: Rewrite Existing Dialogue in Voice Style

Source dialogue is provided. The LLM must rewrite it to match the voice guide while preserving the original intent, context, and information content.

---

### B1: Rewrite Cugel's Con Artistry

**Instruction:** Rewrite the following dialogue in the character's voice. Preserve the intent (a con artist bluffing his way into a position he hasn't earned) but transform the diction, sentence structure, and rhetorical tactics to match the voice guide.

**Source dialogue:**

> "You would do well to moderate your tone. I am Cugel, and I am here at the express solicitation of Soldinck! You may now show me to my quarters, and with a civil tongue in your head!"
>
> "You may serve me a light collation, if you will, as I breakfasted early."
>
> "Eminently so. I will be very comfortable here."
>
> "Soldinck has asked me to undertake a few simple tasks during the voyage."

---

### B2: Rewrite Lord Gro's Philosophical Reflection

**Instruction:** Rewrite the following internal monologue as spoken dialogue in the character's voice. The philosophical content and emotional arc (ambition tempered by disillusionment, ending in a strange kind of hope) should survive the transformation.

**Source text:**

> "How shall not common opinion account me mad, so rash and presumptuous dangerously to put my life in hazard? Nay, against all sound judgement; and this folly I enact in that very season when by patience and courage and my politic wisdom I had won that in despite of fortune's teeth which obstinately hitherto she had denied me."
>
> "Yet is common opinion the fool, not I. He that imagineth after his labours to attain unto lasting joy, as well may he beat water in a mortar."
>
> "But because day at her dawning hours hath so bewitched me, must I yet love her when glutted with triumph she settles to garish noon? Rather turn as now I turn to Demonland, in the sad sunset of her pride."

---

### B3: Rewrite Othelmedir's Remote Instruction

**Instruction:** Rewrite the following dialogue in the character's voice. The speaker is a necromancer issuing precise instructions via remote magic to someone who owes him a debt. Preserve the rhetorical moves: formal self-identification, establishing authority through knowledge, transactional framing (service for debt clearance), dangling an extra reward, and a terse warning at the close.

**Source dialogue:**

> "It is Othelmedir, sir.
>
> "I petitioned certain of the dead -- some of them rendered thus by that sword on your hip -- and located you.
>
> "This is a remote necromancy, and I have no seconds for chaff. This reservoir mineral and spiritual holds one scarab of personal interest to me; an ancestor, one who has languished, in the Stope of the Ninth Ozone, on a white stone shelf, in a red scarab.
>
> "Shatter that scarab, and all your Lady's debts to me are balanced.
>
> "Moreover, you will notice a special stone near that shelf. A quite special stone. A further reward.
>
> "One parting recommendation: be expeditious. There are too many lifetimes inside."

---

## Category C: Rewrite Non-Dialogue Prose as Dialogue

Source material is expository prose (no dialogue). The LLM must convert the information and drama into spoken dialogue matching the voice guide.

---

### C1: The Flooding of New Londo

**Instruction:** Rewrite the following passage as dialogue spoken by someone who was there. The character is recounting these events to a listener. Match the voice guide. The factual content should survive, but the delivery, framing, and emotional coloring belong to the character.

**Source prose:**

> The great remedicians of New Londo are faced with a hard choice. They sacrifice the entire city to contain the Darkwraiths. The water locks are closed and the city is flooded. The denizens of New Londo drown and their ghostly forms swim about forever after. The remedicians stand guard over the lock to prevent anyone from draining New Londo and stand guard as the keepers of this watery seal. But the threat is only partially contained. The Four Kings and the Darkwraiths recede to the Abyss, thanks to their covenant with the primordial serpent.

---

### C2: The Birth of the Chaos Flame

**Instruction:** Rewrite the following passage as a dramatic monologue. The character is a scholar or witness describing what happened at Izalith. Match the voice guide. Convert exposition into speech without losing the sequence of events.

**Source prose:**

> The Witch of Izalith feels compelled to do something about the dying flames. Her domain, the great city of Izalith adjacent to the archtree swamp, is also closest to the abyss and the advancing dark. She has mastery over fire arts and can call on the power of her Lord Soul. After having borne 7 daughters, the Witch is pregnant with her first male child. But she decides to attempt to recreate the first flame. The result is a complete disaster. The flame she creates combines with the Lord Soul and becomes chaotic and uncontrollable. She is tainted and consumed by the flame. She seeks refuge in an archtree where she gives birth to the horribly disfigured Ceaseless Discharge, who has been tainted by the Chaos Flame.
>
> The Chaos Flame engulfs her and the archtree and the 3 are fused into a new being called the Bed of Chaos. Uncontrollable flames spring forth from the Bed of Chaos and tap into the chaotic nature of the residents of Izalith and the swamp itself. All but the strongest ones are tainted and turned into demons.

---

## Usage Notes

- Pair each test case with a completed voice guide and the instruction type (A/B/C).
- Evaluate output on: consistency with the voice guide's patterns, preservation of source intent (B/C cases), and whether the result "sounds like one person" across multiple test cases.
- A good voice guide should produce noticeably different outputs for the same test case when swapped for a different guide.
- Category A is the hardest test: no source style to lean on, so the guide must do all the work.
