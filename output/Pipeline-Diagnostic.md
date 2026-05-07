# Prose-Producer Pipeline Diagnostic

A process-level diagnosis of the redundancy and over-description issues observed in scenes 1-3 of *Dreamreel*, working from the rough drafts vs your hand-revised versions.

## Headline Finding

The composer agent's redundancy problem is **not** a context leak. It is the opposite: the composer is so isolated from prior prose that it cannot tell which material has already been rendered. `WorkingContext.md` is the only window into prior scenes, and it presents already-spent material **as if it were available raw inventory**. The composer faithfully renders it again.

The verbosity / over-description problem is a separate, additive issue: the source-imprint, scene-parameters, and scene-writer phase guides all push toward expansion, with no compression counter-pressure anywhere in the chain.

## Root Cause: How "Already Rendered" is Lost

Trace through the pipeline for scene 2:

1. **A separate Claude instance** writes `WorkingContext.md` with a "Prior Scene Notes" section. That section faithfully recaps scene 1's setting and character details: the inn's smell, Othelmedir's full physical description (tall as redwood, iron eyes, oxblood velvet, prosthetic arm), the ledger of attercop silk, the bench-sleepers, the boy with strong neck and clean teeth, the barefoot child reciting the rite.
2. The composer reads `WorkingContext.md` plus 4 cards. **It cannot tell what's already been depicted in prose** versus what's "still to come" inventory. Both look the same.
3. Scene-writer Step 1 (`pre-setup.md`) asks the composer to "List 8-12 textures" and to "Describe the scene's setting. Be specific." With Prior Scene Notes sitting there full of vivid detail, the composer rationally picks them up as textures. They feel like the richest material on the page.
4. Setup phase pulls 1-2 textures + asks "Active setting? Environmental subtext?" → Inn re-rendered. Conflict pulls 6+ more textures + asks "Re-blocking? Traded objects?" → physical inventory of bodies + arm + cloak gets re-rendered. By the time review runs, the redundancy is baked in.
5. Scene-audit Stage 3 cannot catch it; it sees only the draft + full outline, never scene 1's prose.

**Specific traceback to observed redundancies:**

| Observed                                                                                   | Source in pipeline                                                                                                                           |
| ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| S2 opens with long inn-survey paragraph                                                    | `WorkingContext.md` Prior Scene Notes recap of inn + setup phase's "Active setting" guiding question + texture inventory                     |
| S3 re-describes prosthetic arm in opening                                                  | Othelmedir character bullets re-injected in working context for S3; pre-setup pulls character physical traits as textures                    |
| S3 carries the "valley took a long breath" simile, "spider on thread", seminary-town aside | Imprint card calls for periodic sentences with "as if" + scene-params calls for run-on/cumulative + 8-12 textures = pressure to layer images |

## Secondary Issue: Setup Phase Bias Toward Establishment

You agreed this is real. Your S2 cuts confirm it: you removed the entire opening paragraph and started cold on dialogue. The setup-phase guiding questions (`setup.md:13-18`) are written for **first-of-its-kind scenes** — they ask if the setting is intimidating, if environmental subtext is in play, if false expectations are being seeded. For a continuation scene picking up *minutes* after the prior scene in the same room, those questions are largely answered already. But the composer answers them again, because the phase is structured as a fresh-start opener.

This produces a recognizable **scene shape**: every scene opens with several lines of orientation (where we are, who is here, what the room feels like), regardless of whether the reader needs it. Your revision pass repeatedly killed those opening orientations.

## Secondary Issue: Verbosity Reinforcement

The cards stack in one direction:

- **Imprint card** (S2): "Long periodic sentences (25-60 words) dominate... Pile right-branching subordinates... use semicolons to chain action-consequence."
- **Scene-params card** (S2): "Run-on / Cumulative... clause on clause... Othelmedir's formal accretion."
- **Speech card (Othelmedir)**: "Sentence-length cap: Minimum 15 words; no cap maximum."

Three signals all push toward longer, more accumulating sentences. None of the cards push the other way. The result is the long periodic prose you spent your revision passes trimming. Your edits routinely break run-on sentences into shorter declaratives, the exact opposite of what every card requests.

## Secondary Issue: Texture Inventory Sizing

`pre-setup.md` requests 8-12 textures for any scene. Scene 2 is 700 words; scene 3 is 800. That's roughly one texture per 60-100 words, which is heavy when 30-40% of the scene is dialogue and a chunk of the rest is interior thought. The conflict phase (`conflict.md:8-9`) explicitly says "Draw on most of the remaining textures... This is where the bulk of your sensory material should land." A scene that spends 8-12 distinct sensory details in 700 words will read overwritten — and that's exactly what you trimmed.

For continuation scenes the available *new* texture pool is smaller still, since prior-scene textures are off-limits if you don't want redundancy.

## Tertiary Issue: Cardinal Detail Re-Injection

The author of `WorkingContext.md` is a separate Claude. With the brief "write up the context needed for scene X," it sensibly re-states cardinal character traits each time (Othelmedir's height, eyes, prosthetic, cloak; Weirmoth's body, hands, cloak, spear). These are framed in `WorkingContext.md` as available material, not as "previously established do-not-re-render." So they get re-rendered. The arm in particular shows up in scene 1 (introduced), scene 2 (Working Context restates it as Prior Scene Note), scene 3 (probably restated again as character profile) → composer paints it again each time.

## Summary of Mechanism

```
[separate Claude]                  [composer Claude]
prior scene + outline      ───►    WorkingContext.md (no "rendered" flag)
                                            │
                                            ▼
                                   pre-setup: "List 8-12 textures + describe setting"
                                            │
                                            ▼
                                   setup: "Active setting? Environmental subtext?"
                                            │
                                            ▼
                                   conflict: "Spend most textures here"
                                            │
                                            ▼
                                   draft = re-rendered prior + new (no compression card to push back)
                                            │
                                            ▼
                                   audit: cannot see prior scene → cannot flag redundancy
```

Two leakage points + one missing counter-pressure = the scene shape you've been hand-fixing.

## What's Working

To be clear: a lot of the pipeline is sound.
- Four-card structure is a strong skeleton.
- Speech cards are doing real work; voice in dialogue is character-specific.
- Source-imprint is a one-way extraction (no prose pollution).
- Outline-fidelity is high; beats land.
- The audit catches some quality issues even with limited scope.

The fix is targeted, not a rewrite.

## Recommended Edits

See `Recommended-Edits.md` for a concrete patch list against the WorkingContext template, the composer's stage prompt, and the scene-writer skill files.
