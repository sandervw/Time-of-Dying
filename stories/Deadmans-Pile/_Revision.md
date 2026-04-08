# Editing Stages

*Note: For all edits, use version control to cherry pick changes*

## (DONE) Manual Revision (No Claude)

Focus on:
- Pruning
- Tone
- Character Personality
- Movement/Action

## (DONE) Breakdown Into Scenes

Hey claude, I need you to help me break down @stories\Deadmans-Pile\Deadmans-Pile-Draft1.md . I want to split it into 4-5 distinct "scenes" or "sections" for automatic/llm-based editing purposes. The seperate sections should dropped into a subfolder in the current directory, called 'scenes'. Your job is to:
1. Help me identify the natural breakpoints in the story that lend themselves to splitting it into 4-5 (roughly even) pieces
2. split the story into its seperate files (IE. Deadman's-Pile-S1.md), and put them in the subfolder

## (DONE) Ruthless-pruner

*Mixed success: agent kept falling back to small cuts, or cuts that made it confusing; **may work better w. LLM prose***

Need to create this agent: combination of text-trimmer and draft-editor
- Reduce to 80% - cut clauses, sentences, and paragraphs, not words

## (DONE) Draft-editor

*Very mixed... had to undo over half of claude's recommandations; agent needs improvement*

(basic analysis+cleanup)

TODO Draft-editing enhancements:
- Text transplant (take metaphors/similes, 1 character dialogue, etc; extract to seperate file; look at it in isolation)
- Sensory scan (how much was each of the five senses used in the chapter?)
- Middle-scene start (pick one scene/section from middle of story, start with that instead; non-chronological storytelling)
- Take out beginnings/ends of every chapter, isolate them (text transplant) - how do they look in isolation

## (Optional) Voice Revision

TODO - whose voice?

## (DONE) General Prose Review

*Highly effective: 5-10 targeted edits works great*

Hey claude, do a general prose review of the text below. Your job is to find logical inconsistencies, use of common fiction tropes, repeated beats - anything that seems 'rough' or 'unpolished' in the prose. Your output should be a brief list of any identified issues, along with suggested fixes. Your output must be less than 200 words.\n\nThe Prose:\n\n

## (SKIPPED) Lore Inconsistences

*Note: how to stop it giving same recs?*

Look for missed opportunities to weave in lore

```
RAN VIA 10 OPUS-LEVEL SUB-AGENTS
Read @Stories/RafeScigley/Scene-Docs/RafeScigley-scene-[#].md . I want you to review this scene for possible lore inconsistencies, and for any places where the existing world lore might play in. Reference any files in @Setting/ which might guide your understanding, except the Potential-Folklore folder. Do not reference any folders, skills, sub-agents, or files outside of the scene file and Settings. Your output should be a list of suggested fixes/additions, no mroe than 200 words in total length. Outpot only the list of suggested changes.
```

## (DONE) Word Choice

(uncommon verbs/adverbs/adjectives, specific instances of nouns, certain % replacement for each)

Possible future idea - have it do 'Archaic word replacement' too

```
VERBS/ADVERBS/ADJECTIVES
Hey claude, do a 'vocabulary' edit of the story scene below. Your job is to find the most common verbs, adverbs, and adjectives, and replace them with obscure, archaic, or excrutiatingly-specific synonyms. Only replace those three parts of speech; do not do any noun-replacements. Also no hyphenated, compound, or made-up replacements, and no word insertions/deletions (only *replacements*). Your goal is to replace only the 15% most-common verbs/adverbs/adjectives as they appear in fiction; if a word is the first one that appears in your large-language-model word completion, it is probably a common one. Your output should be just the edited text, no comments, summaries, etc.\n\nThe Scene:\n\n

NOUNS
Hey claude, do a 'vocabulary' edit of the story scene below. Your job is to replace roughly 15% of the *nouns* in the scene with obscure, archaic, or excrutiatingly-specific synonyms. Only replace the nouns - do not replace verbs, adjectives, etc. Also, do not replace any proper-nouns or pronouns. Your replacements must not be hyphenated, compound, or made-up words, and no word insertions/deletions (only *replacements*). Focus on the most-common nouns as they appear in fantasy; if a word is the first one that appears in your large-language-model word completion, it is probably a common one. Your output should be just the edited text, no comments, summaries, etc.\n\nThe Scene:\n\n
```

## Dialogue

TODO - need distinct othelmedir, birdsey, fogg voices

## (SKIPPED) Prose-pruner 2

(reduce to 80% again)

## Spelling/grammar

Simple