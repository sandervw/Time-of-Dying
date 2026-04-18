### Prompting / Prompts

**Lessons for getting non-generic idea output:**

1. **Name a concrete literary model.** Point at a specific author or story as a structural target ("Lovecraft's scholar-with-new-technology stories"). Topic prompts give topic answers; reference prompts give shapes.
2. **Explicitly forbid the current default.** If a mode is working, the model will regress to it because working is safe. Naming the rut ("not all need to be adventure in hostile place") is what pulls it out.
3. **Describe the shape, not the content.** Prompt for what the story *does* ("POV observer watching gradual horrific change from an inciting incident"), not what it's *about*. Leaves setting-specific invention to the model.

**Angles menu (pick one from each bucket and combine):**

*POV angles (who tells the story)*
1. **Client POV** - Told by the person who hired Othelmedir. He appears intermittently; the real story is the client's growing dread. *Model: Chandler's Marlowe from the client's side.*
2. **Apprentice / Watson POV** - Unwilling servant or young apprentice narrates, watching him work without fully understanding. *Model: Watson to Holmes; Heart of Darkness.*
3. **Folktale-about-Othelmedir** - Framed as something locals tell about him at a fire, possibly distorted. *Model: M.R. James; Canterbury Tales framing.*

*Structure angles (how the story is shaped)*
4. **Bottle episode** - Trapped with a small fixed cast (caravan, inn in a storm, stalled barge) while something picks them off. Social pressure equals the threat. *Model: And Then There Were None; Carpenter's The Thing.*
5. **Heist** - Assemble crew, case target, pull the job. Clean three-act. *Model: Ocean's Eleven; Six of Crows.*
6. **Nested archive / found document** - Othelmedir reads an old mancer's journal and the story is what the journal describes, interleaved with his commentary. *Model: At the Mountains of Madness; Borges.*

*Stakes angles (what the story is really about)*
7. **Personal rivalry / duel** - Othelmedir against one named rival mancer. Skill vs. skill, creation vs. creation. *Model: Holmes vs. Moriarty; the wizard duel in The Sword in the Stone.*
8. **Failure story** - A job Othelmedir cannot solve. Structure builds toward the moment he cannot win, and what he does after. *Model: Borges' The Immortal; most Chandler endings.*

**Starting prompt (paste into a fresh chat):**

Hey Claude, I'm generating new short story ideas for my Contumelious Ectogenesis (CE) sequence in the Time of Dying setting, which follows Othelmedir the necromancer. Start by running `sampling.py locations for a list of current setting locations. You are forbidden from reusing any towns or specific geographic zones for a story. See @stories\Contumelious-Ectogenesis\CE-Outline.md for existing story ideas, and the blob-style format.
I want you to generate brief pitches of story ideas to add to my list. They should 1 to 3 sentences each, not fleshed-out briefs. Shoot for 4 to 7 ideas, and each should feature a unique specific location.
For the purposes of this round of idea generation: I want you to do 3 ideas, basing the structure/pacing of your ideas on three Clark Ashton Smith stories: *The Seven Geases*, *The God of the Asteroid*, and *The Colossus of Ylourgne*. Use these as the structure inspiration, but reframe the stories to the Time of Dying setting. Othelmedir's POV should be used for all three (and he should live through all three).
Do you have any questions before you start?
