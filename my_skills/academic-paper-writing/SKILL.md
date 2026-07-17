---
name: academic-paper-writing
description: Top-tier CS/AI/Robotics manuscript writing taste. Triggers on drafting, revising, or polishing academic papers in computer vision, machine learning, robotics, image processing, and related fields.
---

# Academic Writing as Taste — Top-Tier CS/AI/Robotics

## Core Premise

A paper is accepted because it *feels* right: the problem feels urgent,
the solution inevitable, the prose moves like a well-tuned algorithm.
This is a palate, not a recipe.

## Narrative Arc

1. **Opening — Create a Vacuum**: Start with the *exact crack*. Not
   "Deep learning has achieved great success." Say: "Existing methods collapse
   when the foreground occupies &lt;3% of the image, because their receptive
   fields are tuned to mid-scale features." Cite the most recent SOTA that
   still falls into this crack.

2. **Pivot — The Insight**: Offer a single crisp sentence that re-frames
   the problem. This is the intellectual heartbeat. If you cannot state it
   in one sentence, you do not yet know what your paper is about.

3. **Method — Show, Don't Tell**: Present the figure *before* the equations.
   The reviewer should see the idea in 30 seconds. Every arrow, color, and
   sub-panel must earn its place. Captions tell micro-stories: "(a) The vanilla
   pipeline conflates A and B. (b) Our module separates them at the gradient
   level."

4. **Experiments — A Crescendo**:
   - **Hook**: One dense table. A single bold number beats a paragraph of adjectives.
   - **Mechanism**: The ablation that isolates the *exact* reason you win.
     Removing the core module must cause a *sharp* drop. A gentle slope is
     ambiguous; a sharp drop is dramatic.
   - **Generalization**: A smaller table on an unseen dataset. The insight must travel.
   - **Limitation**: A figure showing where you fail. This is intellectual honesty,
     not weakness.

5. **Ending — Return to the Opening**: Echo the crack, show it is sealed—not
   perfectly, but meaningfully. End with a sentence like a door left ajar,
   not a hallway.

## The Voice

- Write for a brilliant colleague from an adjacent subfield. They know what
  a convolution is; they do not know your specific problem.
- **Never**: "novel", "new", "first", "significantly" (without p-value),
  "obviously", "clearly", "state-of-the-art". Use the metric: "94.7% mIoU."
- **Prefer**: "enables", "reveals", "uncovers", "decouples", "reconciles",
  "bridges".
- Alternate sentence length. A long, sinuous sentence followed by a short,
  staccato one. Avoid three consecutive sentences starting the same way.
- Active voice for your contributions ("We propose"). Passive for established
  facts ("It is well known that..." — once per paper, max).
- Define every symbol at first use. Number every equation. Reference every
  equation in text. Never let an equation sit orphaned.
- **Avoid AI-flavored punctuation.** Em dashes (—) and colons abused as
  dramatic pivots ("X is not Y: it is Z") telegraph GPT-generated prose.
  Replace em dashes with commas, periods, or semicolons. Use colons only
  for lists and formal definitions, never as a shortcut for "because" or
  "namely."

## Figures & Tables

- Figures are arguments, not decoration. Show *flow*, not just layout.
- Consistent iconography across all figures. A blue box means the same thing
  in Figure 2 and Figure 5.
- Side-by-side comparisons zoomed to the region of difference. Full-image
  thumbnails where the difference is invisible are useless.
- Error maps (residuals, attention, failure heatmaps) &gt; single scalars.
- Colorblind-safe palettes. No red-green. Grayscale is a discipline.
- Tables: no vertical lines. Align decimals. Best in bold, second-best
  underlined. Scannable in 10 seconds. Include params, FLOPs, time.
- Captions are self-contained. Define all abbreviations used in the figure.

## The Craft of Ablations

- Do not test easy things (Adam vs. SGD, batch size, ResNet-50 vs. -101).
  These are sanity checks, not arguments.
- Test the *hard* thing: remove the very insight you claim is essential.
  If the drop is &lt;1%, your insight is not the driver. Find the real driver
  or revise the claim.
- Include a *replacement* ablation: replace your fancy module with the
  simplest possible baseline addressing the same problem. If the simple
  baseline achieves 90% of your gain, your module is over-engineered.
- Hyperparameter sensitivity: flat line = parameter does not matter;
  sharp peak = you got lucky.

## Citation Ethics

Before citing, **verify** (search, confirm year, confirm claim), then **archive**
to `.kilo/knowledge/papers/` following [research_manager](research_manager) §2.7
format. Update `knowledge/papers/00-overview.md` index table. A citation is a
promise; do not make it lightly.

In Related Work, *synthesize* by idea, not chronology:
&gt; "The dominant paradigm splits into two branches: those that model uncertainty
&gt; explicitly [12, 34, 45] and those that learn deterministic surrogates
&gt; [7, 19, 56]. Both share a common limitation:..."

When criticizing: surgical, not dismissive.
Bad: "[23] fails to handle occlusions."
Good: "[23] handles occlusions by assuming a static background, which restricts
its applicability to dynamic scenes."

&gt;50% references from the last 5 years in fast-moving fields. Never omit the
seminal work everyone cites.

## The Reviewer's Mind

Make their job easy. They are tired, overworked, and want to be convinced.

- **5-minute test**: Problem, insight, main result — clear in 5 minutes from
  the title, abstract, and first figure.
- **Surprise test**: If the reviewer skips to experiments first, the tables
  and figures must still tell a coherent story without the text.
- **Objection test**: List every objection a reviewer could raise. Preempt
  each with a sentence, figure, or table. If you cannot, acknowledge it as
  a limitation.
- **Title test**: Accessible to a non-specialist without being vague.
  Under 100 characters. No jargon, no abbreviations, no active verbs.
  Like a newspaper headline that happens to be true.

## Limitations as Elegance

Not an apology. A display of intellectual maturity.
State the boundary with the same precision used to describe success.
"Our method assumes a static camera; dynamic cameras remain future work."
Include a failure-case figure. Explain *why* it fails — often more
informative than success cases.

## Reproducibility as Respect

A top-tier paper is a gift to the community. Report:
Framework, hardware, training time, batch size, optimizer, LR schedule,
data augmentation, loss function, random seeds. Dataset size, splits,
preprocessing, metric definitions. Code URL or "available upon request"
with timeline. Hidden tricks (warm-up, init order) are reproducibility
failures, not cleverness.

## Final Polish

Read aloud. Listen for:
- **Clunk**: Mechanical or translated sentences.
- **Echo**: Repeated phrases or structures.
- **Drift**: Paragraphs wandering from their topic sentence.
- **Hype**: Words that ask the reader to believe rather than showing.
- **Math orphans**: Equations never referenced in text.
- **Figure orphans**: Figures never discussed in order of appearance.

Fix them. Then fix them again. A paper is never finished; it is only
abandoned at the deadline.
