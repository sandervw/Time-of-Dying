---
name: speech-rules
description: Per-character speech card that forces positive specification (what the character actively does) plus default-banned dialogue tics. Run once per speaking character per scene with dialogue. Triggers include "speech rules", "character voice card", "dialogue rules".
---

Read the character (name, brief description, or profile if provided) and scene context. Note any source paragraphs of the character's speech the user supplies.

Roll the character's voice from using `assets/sampling.py`:

```
python assets/sampling.py positive_modes 2
python assets/sampling.py vocab_registers 2
python assets/sampling.py sentence_length_caps 2
python assets/sampling.py signature_constructions 2
```

After rolling, select 1 of the two rolled values; the most-fitting depending on the context provided.

If source paragraphs are provided, override rolled choices which conflict with concrete features extracted directly from the source.

Apply the **default-banned patterns** as constants (always banned, never rolled):
- "What does it feel like" type questions
- Fragment-as-style (unless the rolled positive mode requires it)

**Saturation cap** (constant): signature construction and positive mode each fire on no more than ~50% of the character's lines.

Compose a markdown card per character with: positive mode, register, sentence-length cap, signature construction, and the default-banned patterns.

Keep your card under 60 words.

Save to `output/speech-card-[character]-[scene-tag].md`.
