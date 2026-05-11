# Post-Scene

This is the assembly step before writing the summary file. The goal is to create compact reference material that can be passed to an LLM when writing the next scene — so everything should be concise and information-dense.

Generate the following from the revised scene:

## Tasks

### 1. Scene Summary

Write a **brief summary (under 150 words)** of the revised scene. Cover what happened, what changed, and where things stand at the end. This is a narrative synopsis, not a craft analysis.

### 2. Ending Text

Copy the concluding paragraph or sentences of the scene **(under 50 words)**. Use ellipses to start the text if necessary. This provides a jumping-off point for the next scene.

### 3. Questions Posed

List **the unresolved threads or tensions that carry forward into future scenes** — under 50 words total. These are the open questions the reader should be holding when they finish the scene.

### 4. Characters Introduced or Referenced

For each character introduced or meaningfully referenced in the scene, write a **brief description (under 50 words each)** covering:

- **Physical**: What they look like — distinctive features, build, dress, mannerisms.
- **Personality**: How they behave — temperament, speech patterns, disposition, any shifts revealed in this scene.

### 5. Review Audit

Assemble the audit findings produced during Step 1 into a structured report:

- **Wordcount**: Target / Actual / Delta (absolute and percentage).
- **Question coverage**: Total Yes count out of 18, and whether the count fell inside, below, or above the 60-80% target zone (11-14 yes).
- **Per-question verdicts**: For each of the 18 questions in `audit-questions.md`, mark **Yes**, **No**, or **N/A**. Append a short rationale phrase (under 12 words) so the reader can see which were answered, which were skipped deliberately, and which were missed.
- **Alignment notes** (optional, under 50 words total): If the scene drifted from its outline or stated priorities, briefly describe where and how, and whether the drift reads as improvement or loss.

This section is the only place where pass-through review analysis is preserved — no scene edits are made.

## Output

Hold this material in working memory. The next step will write it into the post-scene summary file.
