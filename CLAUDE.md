# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Time of Dying is a collaborative fiction project built for iterative composition with Claude AI. TODO - 2-3 sentence setting summary

## Content Structure

Setting documents are organized hierarchically:

- **Setting/Time-of-Dying.md** - Setting overview for the Time-of-Dying project.
- **Setting/Folklore.md** - Random setting folklore. A good source when asked to generate story ideas.
- **Setting/Ideas.md** - Running scratchpad / todo list for rough ideas and notes. Items here are incorporated or discarded, then deleted from the doc.
- **Setting/Mythology.md** - The main setting summary. Maps setting details to specific myth categories.
- **Setting/Folklore/** - Detailed documents for random pieces of generated folklore that has been confirmed as part of the setting. Only reference this is requested by the user.
- **Setting/Mythology/** - Deep-dive expansions of individual mythology elements (cosmogony, cosmology, theogony, anthropogeny, magic systems, etc.).
- **Setting/Potential-Folklore/** - Holding pen for generated folklore pieces the user hasn't decided how to use yet. Not yet incorporated into the setting framework.
- **Stories/** - In progress and completed stories/narratives
- **Output/** - Default destination for files generated via skills and agents (unless the user specifies otherwise)

**IMPORTANT:** after creating a new document, ask the user if they want you to run a text-trimmer or draft-editor subagent on the result document.

## Writing Conventions

When generating or editing setting/story content:

- TODO - setting writing conventions

## Agents (.claude/agents/)

- **draft-editor** - Prose editing specialist. Analyzes draft fiction for structural, craft, and surface-level weaknesses (conflict, subtext, movement, metaphor density, sentence/paragraph variety), then produces a revised draft. Three phases: Analyze, Report, Revise.
- **fiction-tagger** - Extracts short feature tags (threats, locations, weapons, character traits) from fictional sources via web search or local file. Outputs JSON tag lists.
- **text-trimmer** - Compresses and restructures text documents to 70% of original token count while optimizing for LLM readability.

## Skills (.claude/skills/)

- **character-analysis** - Analyzes fictional characters into structured profiles. Four modes: profile (default), description, actions, quotes.
- **character-abstraction** - Strips setting-specific details from character elements (actions, quotes) to produce reusable templates.
- **fiction-abstraction** - Same idea as character-abstraction but for narrative elements: paragraphs and dialogue. Generalizes source-specific prose into templates.
- **literary-revision** - Rewrites prose in a specific literary style while preserving narrative.
- **folklore-generator** - Generates folklore for any observable object or phenomenon. Multi-step workflow with sequential reference loading.
- **scene-writer** - Writes complete prose scenes from a story background and scene outline. Multi-phase workflow - develops narrative through structured phases.
- **story-idea-generator** - Generates original story premises by colliding two unrelated elements. Multi-step workflow with sequential reference loading.
