# kotoba: reasoning demonstrations, decomposition and context selection

Date: 2026-11-03 · Batch 5

**Unassimilated post-hyaku reading proposal; assimilation awaits the user’s explicit instruction.** No prompt execution, model calls, optimizer runs, training or skill edits were performed. The comparison concerns instruction design, not a claim that historical prompting recipes beat current reasoning models.

## What decomposition added to intermediate-step demonstrations

**Historical timeline.** Wei et al.'s [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903v6) first appeared 2022-01-28; selected v6 is 2023-01-10. It studies demonstrations containing intermediate reasoning steps across arithmetic, commonsense and symbolic tasks. Zhou et al.'s [Least-to-Most Prompting](https://arxiv.org/abs/2205.10625v3) first appeared 2022-05-21; selected v3 is 2023-04-16, associated with ICLR 2023. It separates decomposition from sequential subproblem solving, conditioning later answers on earlier results. Read method and compositional-generalization experiments rather than exporting its headline SCAN result to unrelated tasks.

The dates matter: both ideas first appeared in 2022. Later arXiv revisions or the ICLR publication year do not establish a 2023 invention or a universal succession. The experiments concern particular models, exemplars and task distributions.

**Contemporary continuity, disclosed baseline.** Anthropic's [Effective context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), dated 2025-09-29 and re-read 2026-11-03, is already in batch 1. It broadens the design object to the information available at each generation, including instructions, examples and retrieved material. This supplies current practitioner context, not new comparative evidence or proof of an installed client's loading behavior. The new contribution here is the two-paper history and the choice between single-pass demonstration and staged decomposition.

**What changed and stayed.** Decomposition exposes dependencies that a single answer prompt can leave implicit; it also introduces more handoffs where a bad intermediate answer can contaminate the remainder. The underlying need for relevant examples, clear task boundaries and a correct final result persists. Older single-pass demonstrations remain useful as a cheaper, simpler baseline when tasks resemble examples and do not benefit from staged work. This is a hypothesis for evaluation, not an instruction to demand private internal reasoning or equate verbose explanations with correctness.

**Original future question.** After hyaku, can a skill preserve dependency-critical facts with staged subproblem answers while spending fewer context tokens on repeated instructions? Design a paper comparison of direct answer, demonstration and decomposition variants, including one wrong intermediate result and one ambiguous decomposition. Score final correctness, error propagation and context budget separately.

**Rights and novelty.** CoT's selected record is CC-BY-4.0; least-to-most uses arXiv's non-exclusive distribution license. No open article-reuse grant was established for Anthropic. Link and original summary only, with no exemplars reproduced. The historical paper families were absent from supplied context; the contemporary baseline is explicitly reused.
