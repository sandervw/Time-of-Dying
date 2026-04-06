# Editing Stages

*Note: For all edits, use version control to cherry pick changes*

## (DONE) Manual Revision (No Claude)

Focus on:
- Pruning
- Tone
- Character Personality
- Movement/Action

## Breakdown Into Scenes

TODO

## Prose-pruner

(reduce to 80% - cut clauses, sentences, andparagraphs, not words)

## Draft-editor

(basic analysis+cleanup)

## (Optional) Voice Revision

TODO - whose voice?

## General Prose Review

Hey claude, do a general prose review of the text below. Your job is to find logical inconsistencies, use of common fiction tropes, repeated beats - anything that seems 'rough' or 'unpolished' in the prose. Your output should be a a brief list of any identified issues, along with suggested fixes. Your output must be less than 200 words.\n\nThe Prose:\n\n

## Lore Inconsistences

*Note: how to stop it giving same recs?*

Look for missed opportunities to weave in lore

```
RAN VIA 10 OPUS-LEVEL SUB-AGENTS
Read @Stories/RafeScigley/Scene-Docs/RafeScigley-scene-[#].md . I want you to review this scene for possible lore inconsistencies, and for any places where the existing world lore might play in. Reference any files in @Setting/ which might guide your understanding, except the Potential-Folklore folder. Do not reference any folders, skills, sub-agents, or files outside of the scene file and Settings. Your output should be a list of suggested fixes/additions, no mroe than 200 words in total length. Outpot only the list of suggested changes.
```

## Word Choice

(uncommon verbs/adverbs/adjectives, specific instances of nouns, certain % replacement for each)

Possible future idea - have it do 'Archaic word replacement' too

```
VERBS/ADVERBS/ADJECTIVES
Hey claude, do a 'vocabulary' edit of the story scene below. Your job is to find the most common verbs, adverbs, and adjectives, and replace them with uncommon synonyms. Only replace those three parts of speech; do not do any noun-replacements. Also no hyphenated, compound, or made-up replacements, and no word insertions/deletions (only *replacements*). Your goal is to replace only the 15% most-common verbs/adverbs/adjectives as they appear in fiction; if a word is the first one that appears in your large-language-model word completion, it is probably a common one. Your output should be just the edited text, no comments, summaries, etc.\n\nThe Scene:\n\n

NOUNS
Hey claude, do a 'vocabulary' edit of the story scene below. Your job is to replace roughly 15% of the *nouns* in the scene with obscure, archaic, or excrutiatingly-specific synonyms. Only replace the nouns - do not replace verbs, adjectives, etc. Also, do not replace any proper-nouns or pronouns. Your replacements must not be hyphenated, compound, or made-up words, and no word insertions/deletions (only *replacements*). Focus on the most-common nouns as they appear in fantasy; if a word is the first one that appears in your large-language-model word completion, it is probably a common one. Your output should be just the edited text, no comments, summaries, etc.\n\nThe Scene:\n\n
```

## Dialogue

TODO - need distinct othelmedir, birdsey, fogg voices

## Prose-pruner 2

(reduce to 80% again)

## Spelling/grammar

Simple