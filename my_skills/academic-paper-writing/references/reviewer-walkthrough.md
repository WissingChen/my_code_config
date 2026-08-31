# Reviewer Walkthrough — academic-paper-writing §8 Companion

Reference-only: the four reviewer tests applied to one fictional paragraph. Use as the shape of a self-review before submission.

Draft paragraph under review:

> "Spatial reasoning remains challenging for MLLMs. Our novel framework significantly improves performance, achieving 67.8% on VSI-Bench, clearly surpassing previous methods. Extensive experiments demonstrate the effectiveness of our approach."

## Test 1: 5-minute test

Problem / insight / main result must be visible from title, abstract, first figure.
Verdict: **fail**. "Remains challenging" is a generic gap; the insight (what re-framing?) is absent; 67.8% appears with no baseline next to it, so the main result is not scannable.
Fix: name the precise gap ("protocol bias, not model capability, dominates X% of measured error"), state the insight in one sentence, put baseline and delta in the abstract.

## Test 2: Surprise test

Figures and tables must tell the story without the text.
Verdict: **fail**. "Extensive experiments" is asserted, not shown. If the ablation table needs the prose to argue the mechanism, the figure set is not carrying its weight.
Fix: the main table alone should show baseline / expected mechanism / ablation isolating the claimed cause.

## Test 3: Objection test

List every objection; preempt or acknowledge each.

| Objection a reviewer will raise | Current text | Required action |
|---|---|---|
| "67.8% vs. what baseline, with what variance?" | no baseline, no uncertainty | add 参照文献 baseline, effect size, interval |
| "surpassing *which* previous methods?" | vague | name the strongest credible method compared |
| "is the gain the mechanism or the protocol?" | unaddressed | control-subset result + limitation sentence |
| "novel?" | claimed | delete the word; the framing earns novelty or nothing does |

## Test 4: Title test

Accessible to a non-specialist, under 100 characters, no jargon, no abbreviations.
Verdict of the implied title ("A Novel Framework for Spatial Reasoning Enhancement in MLLMs"): **fail** — "novel", "framework", "MLLMs" all break the rules.
Fix shape: "Measuring and Correcting Evaluation Bias in Video Spatial Reasoning" — states the problem and the act, no acronym.

## Rewritten paragraph (post-walkthrough)

> "On VSI-Bench, 34% of the errors of a strong video MLLM trace to evaluation-protocol bias rather than reasoning failure (E03, control subset). Correcting for this bias raises measured accuracy from 61.2% to 67.8% (3 runs, observed range ±0.9), moving the model past Spatial-MLLM (63.1%) without any model change. The correction over-fires on bias-free questions (−2.6pp), which bounds the claim to bias-affected subsets."

Note what changed: every number carries a source (experiment ID) or a named comparator; every hedge states its boundary; no hype word survives.
