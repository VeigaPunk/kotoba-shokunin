# R75Attack48 — independent falsification

## Verdict
**Finding survives in substance, with an important scope limit.** The round-74 *description-threshold* audit does not establish route calibration. Length limits, truncation/budget behavior, and recommended front-loading are not observations of whether descriptions actually select the intended skill. However, the proposed “held-out control” is non-vacuous only if evaluated on actual, labeled route decisions; merely checking for a held-out split or counting description length/lane-name presence cannot support route-calibration claims.

## Evidence

- The exact assigned wave-one report `w1/R75Facet48.md` is absent from the measured worktree (directory listing has no Facet48); I therefore cannot independently inspect its citations or its exact proposed command. The only extant result record says the report finding was: “Round-74 evidence counts description length and lane-name presence, not route calibration; report includes candidate held-out control and caveats” (`.ufo/waves/round-75/w1-results.json:290-293`). This is a dispatch-result summary, not the missing report itself.
- Measured revision is `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`git rev-parse HEAD`). `SKILL.md:164-176` documents per-client thresholds, length caps, truncation/budget behaviors and action advice. No route-choice trial outcomes, intended-vs-actual selection labels, or route accuracy statistic appear in this table. The Gemini row at `SKILL.md:174` is specifically a loader/render-path observation; it does not test selection either.
- Historical plan `plans/round-74.md:101-149` describes C2 as freshness/re-pinning the sibling census, not route-calibration evaluation. C1 at `:49-99` is skill-creation guide assimilation and likewise does not purport to measure routing. Thus the cited round-74 work cannot be treated as route calibration evidence; the dispatch summary’s distinction is materially correct.

## Counterexample / correction

A perfectly passing threshold audit (including descriptions below every documented cap and reports of where clients cut them) is compatible with every tested prompt selecting the wrong skill. Conversely, selection could be accurate despite a threshold warning. Therefore do not infer routing quality from length or lane-name counts. The smallest safe control is a fixed, labeled set of description-routing prompts with intended skill/negative cases, measured on held-out prompts (not used to tune descriptions); report per-class outcomes and the exact routing harness/client. If the proposed check only validates a held-out partition or token presence, it is vacuous for calibration and must be paired with observed selections.

## Axes

- **Calibration:** supported gap; no route outcomes in inspected evidence.
- **Operability:** proposed control remains unverified because the target report and its command are absent; require concrete labeled route trials rather than a structural proxy.

Report path: `.ufo/waves/round-75/w2/R75Attack48.md`
