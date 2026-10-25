source: S218 — Vercel — AGENTS.md outperforms skills in our agent evals — https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals — "Skills weren't being triggered reliably" and the four-configuration results table; quote "In 56% of eval cases, the skill was never invoked."; also "A compressed 8KB docs index embedded directly in `AGENTS.md` achieved a 100% pass rate, while skills maxed out at 79%"; post by Jude Gao (Vercel), retrieved 2026-10-23 — opened 2026-10-23 (carried from the staged campaign row S248; this seat did not re-open the page)
source: S219 — Chroma — Context Rot: How Increasing Input Tokens Impacts LLM Performance — https://research.trychroma.com/context-rot — the report's own summary of its findings; quote "model performance degrades as input length increases, often in surprising and non-uniform ways"; also the LongMemEval and repeated-word tasks; report by Hong, Troynikov and Huber (Chroma), year 2025, retrieved 2026-10-23 — opened 2026-10-23 (carried from the staged campaign row S254; this seat did not re-open the page)
verified-at: 2026-10-23
recheck: 90d — re-fetch the post and confirm the 56%, 53/53/79/100% figures and the 40KB→8KB compression result are unchanged (ran 2026-10-23) (row S218; every row's own stripped prose is in the round-72 Gate notes)
ground: normalization candidate, round 72 wave 1; rows S218, S219 from staged S248, S254

# Context rot and always-on context — the cost side of passive injection (round 72, candidate)

**Candidate entry.** Rows normalized by seat ExecIdNormalize in round-72 wave 1 from the read-only campaign package `merge/kotoba/`; admission is the source-opening seats' and the L1's decision, and the rule prose for `SKILL.md` § Trigger-fidelity checklist is the C1 seat's. Every claim below is the staged row's own `teaches` cell; the quotes are carried from the row's `anchor` cell and were not re-fetched here.

## What the rows teach

- **S218** — the first quantified **non-invocation** rate the lane holds: a skill was never called in 56% of cases, so adding it moved the pass rate not at all (baseline 53%, skill 53%, +0pp), while telling the agent to use it reached 79% and an always-on `AGENTS.md` index reached 100% — with the diagnosis that the failure is the *decision point*, not the content
- **S219** — that longer input is not merely more expensive but **worse**, non-uniformly, even on deliberately simple controlled tasks — which is the cost side of the always-on strategy S218 measures: passive context buys availability with degradation, and the degradation is not a smooth function of length

## Located quotes (carried from the anchor cells)

| row | quotes |
|---|---|
| S218 | "In 56% of eval cases, the skill was never invoked." / "A compressed 8KB docs index embedded directly in `AGENTS.md` achieved a 100% pass rate, while skills maxed out at 79%" |
| S219 | "model performance degrades as input length increases, often in surprising and non-uniform ways" |

