# Recommended Pipeline Edits

Concrete patches to address the issues identified in `Pipeline-Diagnostic.md`. Ordered by leverage. The first three edits would absorb most of the redundancy work you've been doing by hand.

## Edit 1 — Split "Prior Scene Notes" into "Already Rendered" and "Continuing State" (HIGHEST LEVERAGE)

**Where:** Your separate-Claude prep instructions for `WorkingContext.md`.

**Problem:** Today's "Prior Scene Notes" mixes "things the reader already saw rendered as prose" with "things still in play this scene." The composer cannot tell them apart and re-renders both.

**Fix:** Split into two named subsections with explicit instructions:

```markdown
## Prior Scene — Already Rendered (DO NOT RE-DESCRIBE)

Material the reader has already seen depicted in prose. Reference obliquely
if it must come up again ("the dead arm," "the velvet"), but do not paint
it fresh. Treat as established fact, not as texture inventory.

- Othelmedir's physical appearance (height, face, eyes, hair, beard, cloak,
  prosthetic left arm hanging lifeless beneath the cloak)
- The Hooded Pillow's interior: low ceiling, hearth of orange coals,
  bench-sleepers, smell of stale millet and unwashed wool, the warped door
- The bedmeister's plank counter, attercop-silk ledger, bead-tally on a
  nailed cord
- The barefoot child reciting *The Little Mass of Failing Lamps* (the rite
  itself, in full)

## Prior Scene — Continuing State (still active this scene)

Material that persists into this scene and may need fresh prose handling.

- Othelmedir is at the counter, having just spoken his last line.
- The bedmeister's thumb is on the bead-cord.
- Weirmoth is at the bench-end nearest the door, mid-bargain.
- The barefoot child is asleep against a bench-leg.
```

**Why this works:** It encodes the distinction the composer currently can't infer. The label *"DO NOT RE-DESCRIBE"* is a hard signal even a fresh-context model will obey. This is the single highest-leverage fix.

## Edit 2 — Add a "no re-render" clause to the composer's stage prompt

**Where:** `prose-producer/SKILL.md`, Stage 2 prompt (around lines 44-58).

**Patch:**

```diff
 Read ONLY these files plus files inside the scene-writer skill folder:
 - Scene outline: `{OUTLINE_PATH}`
 - The four cards from Stage 1: `{CARD_PATHS}`

 Do NOT read the source style passage or any other file.

+Material listed under "Already Rendered" in the scene outline has been
+depicted in prior scenes. Treat it as established fact. You may reference
+it obliquely (a phrase, a callback) but do not re-describe character
+appearances, setting features, or sensory details that have already been
+rendered. New material this scene introduces is fair game for full prose
+treatment.
+
 Invoke the `scene-writer` skill, following its workflow exactly. Treat the
 four cards as binding constraints throughout drafting and review.
```

**Why this works:** Belt-and-suspenders with Edit 1. Even if the working context author forgets to split the section, the composer is now primed to treat redundant rendering as a violation.

## Edit 3 — Add a "Continuation Scene" branch to the scene-writer pre-setup

**Where:** `scene-writer/references/pre-setup.md`.

**Patch (insert as Task 0, before Task 1):**

```markdown
### 0. Scene Type

Decide whether this is an **establishing scene** or a **continuation scene**:
- **Establishing**: new location, new time-jump, new POV, or first appearance
  of a major character. Setup may run a full 25-30% of wordcount.
- **Continuation**: same location and time as the prior scene, no major new
  characters, picking up mid-stride. Setup should run 5-15% of wordcount —
  a single establishing line or paragraph at most. Do not re-orient the
  reader to a setting they were just in.

State which type this scene is and proceed accordingly.
```

**Patch to Task 2 (Textures):**

```diff
 ### 2. Textures

-List **8–12 textures** — these are magnified sensory details, minute
-specifics, and concrete physical particulars that you will weave into the
-prose as you write.
+List **5-8 textures** for short scenes (under 800 words) or continuation
+scenes; **8-12 textures** for establishing scenes 800+ words.
+
+Textures must be **fresh** — material not already rendered in prior scenes.
+Do not list a texture if its sensory content has been depicted before.
```

**Patch to `setup.md`** Wordcount Constraint:

```diff
 ## Wordcount Constraint

 The total finished scene should be approximately **[WORDCOUNT]** words.
-The setup should account for **25–30%** of that total.
+For establishing scenes, the setup should account for **25–30%**.
+For continuation scenes, **5-15%** is the target — a single beat of
+orientation, no more.
```

**Why this works:** The current setup phase is structurally a fresh-opener. Continuation scenes need a different rule. This formalizes the distinction without breaking the phase model.

## Edit 4 — Add a compression counter-pressure card

**Where:** Stage 1 of `prose-producer/SKILL.md`, OR a new sub-skill.

**Problem:** Imprint, scene-params, and speech cards all push toward longer accumulation. No card pushes back. Result: prose that needs trimming on every revision pass.

**Option A (lighter):** Add a single line to `setup.md`, `conflict.md`, and `resolution.md`:

```markdown
## Drafting Discipline

If two adjacent sentences carry similar sensory or descriptive load, cut
one. If a simile rephrases the noun it modifies, cut the simile. The
imprint and scene-parameter cards favor accumulation; this rule is the
counter-weight. Apply throughout — not just in review.
```

**Option B (more structured):** Add a fifth card to Stage 1 — a "Drafting Discipline" card that explicitly lists "compression triggers" specific to this scene's length and type. This is heavier-weight but produces a card that lives alongside the others as a binding constraint.

I'd start with Option A; only escalate to B if redundancy persists.

## Edit 5 — Loosen the review-phase "75-90% question coverage" rule

**Where:** `scene-writer/references/review.md`, Task 2.

**Problem:** The review phase audits how many guiding questions the scene answers and aims for 75-90%. For a 700-word scene with ~18 guiding questions across setup/conflict/resolution, that's 13-16 questions answered — which forces additions. You then spend revision time cutting what the review phase added.

**Patch:**

```diff
 ### 2. Question Coverage Audit

 Review all guiding questions from the setup, conflict, and resolution
 phases. Count how many the scene currently answers "yes" to.

-- **75–90% is the target range.** This is the sweet spot — enough craft to
-  feel intentional, enough gaps to feel unpredictable.
-- **Over 90%**: The scene is too tidy. Look for a question or two that could
-  be *removed* by editing — strip out an element that makes the scene feel
-  overly constructed. Introduce a rough edge.
-- **Below 75%**: The scene is undercooked. Look for questions you could
-  answer by *adding* to the current prose — a line of dialogue, a shifted
-  detail, a beat of action.
+- **60-80% is the target range.** Below 60% is undercooked; above 80% is
+  over-engineered. Lean toward the lower end for short scenes (under 800
+  words) and continuation scenes, where the right answer is often "this
+  question doesn't apply here."
+- **Above 80%**: Cut. Remove an element rather than add one. Continuation
+  scenes especially should NOT try to re-answer questions already answered
+  by the prior scene.
+- **Below 60%**: Add only if the missing question genuinely serves the
+  scene; otherwise let the gap stand.
```

**Why this works:** Re-anchors the review phase as a *cutting* tool rather than a *checklist-completing* tool. Your hand-edits show you consistently cut, never add — the review phase should bias the same way.

## Edit 6 — Give the audit agent partial cross-scene visibility

**Where:** `prose-producer/SKILL.md`, Stage 3 prompt.

**Patch:**

```diff
 Read ONLY these files plus files inside the scene-audit skill folder:
 - Scene draft: `{SCENE_DRAFT_PATH}`
 - Full story outline: `{STORY_PATH}`
+- Prior scene "Already Rendered" sections (if any): `{PRIOR_RENDERED_LIST}`

 Do NOT read any other file.
```

And in `scene-audit/SKILL.md`, add to the Internal Quality criteria:

```markdown
3. **Redundancy with prior scenes** — Flag any sentence or paragraph that
   re-describes material listed in prior "Already Rendered" sections.
```

**Why this works:** Even with the upstream fixes, the audit becomes a final safety net for redundancy.

## Suggested Application Order

1. **Edit 1** (Working context split) — biggest single win, zero code changes, just prep-instruction tweak.
2. **Edit 2** (Composer prompt no-re-render clause) — one-line patch, reinforces Edit 1.
3. **Edit 3** (Continuation-scene branch in pre-setup) — addresses the structural setup bias you confirmed.
4. **Edit 5** (Review-phase rebalance) — stops the review from re-inflating what setup just trimmed.
5. **Edit 4** (Compression counter-pressure) — only if redundancy persists after 1-3.
6. **Edit 6** (Audit cross-scene visibility) — backstop; lowest priority.

## What I'd Skip

- **Don't pass prior scene prose to the composer.** Your original instinct is right; the trade-off favors fresh generation. Edit 1 gets you the benefit without the prose-pollution cost.
- **Don't add more cards.** Adding cards has diminishing returns and increases composer cognitive load. Modifying existing prompts is cheaper.
- **Don't shorten the source-imprint.** The imprint card is doing useful work; the issue is that nothing balances it, not that it's wrong.
