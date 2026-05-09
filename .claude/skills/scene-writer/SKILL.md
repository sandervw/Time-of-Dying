---
name: scene-writer
description: Write a complete prose scene from a given scene outline. Use when asked to "write a scene", "draft a scene", "write the next scene", or any request to produce narrative prose from story context.
---

# Scene Writer

## Inputs

The user provides:

- **Story background**: The broader narrative context (world, characters, prior events).
- **Scene outline/idea**: What this specific scene should accomplish — its purpose, characters involved, tone.
- **Scene priorities (optional)**: What different aspects of style or parts of of prose should weigh most in the scene - action, dialogue, humor, etc.
- **Wordcount**: Target length for the finished scene.

## Workflow

_Each step's reference file must only be read AFTER the previous step's output has been completed. Do NOT batch-read reference files. Reading a step's reference file counts as beginning that step._

---

### Step 1: Pre-Setup

Read `references/pre-setup.md`.

Using the story background and scene outline, follow the reference file's instructions to generate the raw material for this scene.

### Step 2: Condense to Working Document

Condense the output of Step 1 to **under 300 words**. This is your scene's working inventory — a compact reference of elements available to draw from as you write.

Write this condensed material to a new file using the `assets/working-doc.md` template.

### Step 3: Setup

Read `references/setup.md`.

Follow the reference file's instructions to write the setup phase of the scene, drawing from your working document.

### Step 4: Append Setup & Spend Details

Append the prose you wrote in Step 3 to your `working-doc.md` file.

Then, in the working document's inventory section, **remove any textural details you used** in the setup.

### Step 5: Conflict

Read `references/conflict.md`.

Follow the reference file's instructions to write the conflict phase of the scene, drawing from the remaining details in your working document.

### Step 6: Append Conflict & Spend Details

Append the prose you wrote in Step 5 to your `working-doc.md` file.

Again, **remove any textural details you used** from the working document's inventory.

### Step 7: Resolution

Read `references/resolution.md`.

Follow the reference file's instructions to write the resolution phase of the scene, drawing from the remaining details in your working document.

### Step 8: Append Resolution

Append the prose you wrote in Step 7 to your `working-doc.md` file. **Remove any remaining textural details** from the working document's inventory. The inventory should now be empty.

### Step 9: Write to Scene Template

Copy the `assets/scene-template.md` template to a new file named `[Storyname]-Scene-[X].md` (where `[Storyname]` is derived from the story background and `[X]` is the scene number, provided by the user or inferred).

Write the scene prose into the **Full Scene** section. Combine the setup, conflict, and resolution into continuous text — **remove the phase subheaders** (Setup / Conflict / Resolution) so the prose reads as a single unbroken scene.

### Step 10: Clean Up & Present

Delete the working document created in Step 2.

Present the finished scene file to the user:
- `[Storyname]-Scene-[X].md` — the scene prose

Suggest running `scene-review` next if the user wants to revise the scene and produce a post-scene summary.

## File Structure

```
scene-writer/
├── SKILL.md
├── references/
│   ├── pre-setup.md
│   ├── setup.md
│   ├── conflict.md
│   └── resolution.md
└── assets/
    ├── working-doc.md
    └── scene-template.md
```
