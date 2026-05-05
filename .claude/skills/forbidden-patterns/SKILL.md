---
name: forbidden-patterns
description: Per-scene blacklist of LLM prose tells. Rolls a sampled blacklist before drafting. Triggers include "forbidden patterns", "ban patterns", "scene blacklist".
---

Roll bans using `assets/sampling.py`:

```
python assets/sampling.py simile_bans 2
python assets/sampling.py cadence_bans 2
python assets/sampling.py syntactic_bans 1
python assets/sampling.py imagery_bans 2
python assets/sampling.py register_bans 1
```

Use the rolled rules verbatim. If the user supplies additional bans, append them.

Compose a markdown card with categorized bans.

Do not add extra categories to your card.

Keep your card under 100 words.

Save to `output/blacklist-[scene-tag].md`.
