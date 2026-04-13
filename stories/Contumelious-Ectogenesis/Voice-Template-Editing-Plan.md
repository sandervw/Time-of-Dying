# Editing Plan: Necromancer-Voice.md

Goal: Revise the Othelmedir voice template so that it (1) preserves the archaic-scholarly style identity, (2) maximizes dialogue variety across sessions, and (3) cuts token count by 30-50% from the current ~3,800 tokens.

This plan is a prompt. Feed it to an LLM alongside the current Necromancer-Voice.md and it will produce the revised template.

---

## Editing Instructions

### 1. Eliminate Redundancy Across Sections

The same principles (delay information to end of sentence, use archaic diction, avoid emotional directness) are restated in Core Prose Posture, Sentence Structure, Rhetorical Tactics, and Rhythm and Flow. State each principle once, in the section where it fits most naturally, and cut all restatements.

Specifically:
- **Core Prose Posture** and **Rhythm and Flow** overlap heavily. Merge them into a single short section called "Prose Posture." Keep: ledger frame, biblical rhythm, no exclamation marks, information-at-the-end principle. Cut everything that Sentence Structure already covers.
- **Rhetorical Tactics** items 3 and 5 restate what Sentence Structure Patterns 1 and 4 already demonstrate. Cut them. Keep tactics 1, 2, 4, 6, and 7 as a compact list.

### 2. Keep Sentence Structure Patterns As-Is

This is the strongest section. The five named patterns with bracketed formulas are generative and structural. Do not cut, compress, or merge them. They are the core engine of the template.

### 3. Keep "What This Voice Is NOT" As-Is

High-value negative constraints that counteract the most likely LLM failure modes (Lovecraft drift, thou/hast archaism, horror-genre directness, decorative floweriness). Do not cut.

### 4. Keep the Quick Test As-Is

Four binary self-checks. Compact and effective. Do not cut.

### 5. Restructure All Vocabulary Guidance

This is the biggest change. Replace the current flat vocabulary lists and example-substitution tables with the three-layer system described below.

#### Layer 1: Fixed Canon (keep in template)
Reduce to only proper nouns and mandatory setting spellings. These are not style choices; they are names. Cap at 10 terms max. Example: Deadspeech, Chrypt, Tohmb, the Road of Graves, the Slate Sun, Pilgrim Tohmb.

#### Layer 2: Generative Patterns (keep in template, replaces word lists)
Replace the preferred vocabulary list (line 71-72) and setting-specific vocabulary list (line 73) with word-formation rules. Describe the construction grammar, not the inventory. Format as:

> [pattern formula]: [2-3 examples to demonstrate, not to reuse]

Cover these categories:
- Compound adjective coinage (already good, keep as-is)
- Setting-term coinage (body/craft compounds, decay/container compounds, color/substance compounds)
- Epithet construction for recurring entities (gods, the Road, necromantic concepts)
- Circumlocution construction for mundane actions (the understatement-through-elevation principle, without fixed mappings)

#### Layer 3: Per-Session Rotation (do NOT put in template)
This layer lives outside the template. Add a short note at the top of the template that says: "This template is designed to be paired with a per-session vocabulary rotation prompt. See Voice-Vocabulary-Guide.md." Do not embed rotation content in the template itself.

### 6. Cut the Recurring Phrase Patterns Table

This nine-row table is a repetition engine. The sentence structure patterns already provide the same guidance in a more generative form. Delete the entire table.

### 7. Cut Specific Example Substitutions

The Necromantic and Infernal Reference examples (fear = X, bad omen = Y, evil place = Z) and the Understatement Through Elevation examples (being eaten = X, dying = Y) will calcify into reused phrases. In both sections:
- Keep the principle (one sentence describing what to do)
- Cut all specific mappings
- Replace with the generative pattern from Layer 2

### 8. Trim Figurative Language Section

- Keep the "Off-limits" list (negative constraints, high value)
- Keep the density note ("moderate to heavy")
- Cut the "Source domains" list (redundant with vocabulary guidance)
- Cut the "Preferred simile frame" (will be reused verbatim)

### 9. Trim the Avoid List in Word Choice

Keep: no contractions, no modern slang, no casual intensifiers, no emotional directness. Cut the specific replacement examples ("find out" becomes "discover") as these are obvious from context and add tokens without value.

### 10. Cut All Markdown Horizontal Rules and Excessive Formatting

The template is consumed by LLMs, not rendered for human reading. Strip horizontal rules, reduce header depth where possible, and prefer compact formatting.

---

## Validation

After editing, the revised template should:
- Be 1,900-2,700 tokens (down from ~3,800)
- Contain zero flat vocabulary lists
- Contain zero fixed phrase-substitution mappings
- Retain all five sentence structure patterns with bracketed formulas
- Retain all five "What This Voice Is NOT" items
- Retain the four-point Quick Test
- Reference the external vocabulary guide for per-session rotation
