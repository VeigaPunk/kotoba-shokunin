# R75Attack04 — Survey evidence paragraph

## Axes
Factual accuracy; material actionability; control non-vacuity.

## Verdict
**Partially falsified; residual operational gap survives.** The facet correctly observes that `SKILL.md:50-56` itself gives no dated membership manifest/recheck command. But its broader assessment that the 16-file population has no contemporaneous inventory elsewhere is contradicted by the relocated corpus record. The report's own caveat that another artifact might preserve the membership is borne out.

## Independent evidence at `65a5c7a`
- `SKILL.md:50-56` matches the quoted paragraph: it dates the 16-file survey to 2026-09-28, names both glob roots, points to “Instruction surfaces,” and warns that citations are points-in-time. The roots are `~/.agents/skills/*/SKILL.md` and `~/.config/opencode/skills/ufo/SKILL.md`.
- `corpus/knowledge/anatomy-and-compression.md:3,7-24,150-179` preserves the dated observation, an enumerated production-skill inventory, and the exact `wc -l ~/.agents/skills/*/SKILL.md ~/.config/opencode/skills/ufo/SKILL.md` measurement command. This is evidence against treating the surveyed population as wholly unrecoverable. The list is grouped in places (e.g. `bailian-finetune, bailian-sandbox`), and is not a per-file hash manifest; it does not prove each historical file's exact bytes.
- The report's safe host check reproduces: the `~/.agents` glob currently counts 74; the opencode `ufo/SKILL.md` path is absent; the opencode skill glob currently counts 0. This does not contradict the dated historical count. It is a current-state observation, not a rerun against 2026-09-28.
- `SKILL.md:517-526` (the source section; actual read around lines 516+) does record the round-59/60 moves, including the production skill files to `anatomy-and-compression.md` and host surfaces. The move record supplies a route to the relocated evidence, though the survey paragraph does not link directly to the inventory.
- The cited `git log -1 --format='%H %ci %s' -- SKILL.md` output matches the report: `559ee76a9bcf3bccd374776a3ae5f0f1dcba47dd`, dated 2026-10-25 23:29:02 -0300. That commit is an ancestor of HEAD `65a5c7a663249e0522cc49e4a148424200d9ddfe`; the current lane HEAD is dated 2026-10-26 09:05:54 -0300.

## Attack and scope
The asserted missing artifact is not wholly missing: a corpus document contains the dated membership list and command. Thus “falsifiable only if contemporaneous membership evidence exists elsewhere” should not be left as unresolved uncertainty, and the recommended future exact enumeration is partly redundant for the historic survey. However, the evidence is a text inventory, not a hashed snapshot, and `SKILL.md:50-56` does not point readers directly to it. The narrower reproducibility concern (membership and bytes are not independently reconstructed from the paragraph alone) remains actionable, but is less severe than the facet's formulation suggests.

The current 74-vs-16 comparison is correctly bounded and does not establish historical error. I found no defect in the dated-count claim from this comparison. The report's “distinct facet” declaration is not enough to establish non-duplication; I did not independently compare sibling facet findings, so no duplicate finding is made.

## Verification limits
Read-only. No lane edits, live fetches, or tests. Host glob counts and git ancestry/date commands were exercised. The assigned report's cited file content and relocated inventory were re-opened at lane HEAD. No installation performed.
