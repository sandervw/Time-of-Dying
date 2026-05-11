# Review

This is a read-only audit of the scene file. Read the scene file in full, then audit it against the original story context (story background, scene outline, scene priorities) and the guiding questions in `audit-questions.md`. Do NOT edit the scene file at any point.

## Tasks

### 1. Pre-Scene Alignment

Compare the scene against the original inputs:

- Does it reflect the **scene outline's** stated purpose (audience and story)?
- Does it serve the **character goals** implied by the outline?
- Does it honor the **scene priorities** if any were provided?
- Are the **location** and atmosphere consistent with the story background?

If the scene has drifted from its original intent, note where and how (and whether the drift reads as an improvement or a loss). These notes feed into the Review Audit's "Alignment Notes" in the next step.

### 2. Wordcount Comparison

Use `wc -w` on the scene file. Record:

- Target wordcount (from the original inputs)
- Actual wordcount
- Delta (absolute and percentage)

### 3. Question Coverage Audit

Read `audit-questions.md`. For **each of the 18 questions**, decide whether the scene answers it Yes, No, or N/A (not applicable to this scene's role in the story). Hold the per-question verdict and a short rationale phrase.

Count the Yes answers. Note whether the total falls inside, below, or above the **60-80% target zone (11-14 yes)**.

- **60-80% is the target range**. Below 60% is undercooked; above 80% is over-engineered. Lean toward the lower end for short scenes (under 800 words) and continuation scenes, where the right answer is often "this question doesn't apply here."
- For continuation scenes especially, questions already answered by the prior scene should usually be marked N/A.

## Output

Hold the audit findings (alignment notes, wordcount comparison, per-question verdicts, yes count) in working memory. The next step assembles them into the Review Audit section of the post-scene summary file.
