source: S260 (Stryker Mutator documentation — "Mutant states and metrics", https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/ — § Mutant states: Killed (HTML line 12), Survived (HTML line 14); § Metrics: Mutation score (HTML line 51, `detected / valid * 100`); sibling page "Equivalent mutants" (HTML line 16); fetched 2026-11-05, HTTP 200) and S261 (own-work — the round-89 mutant matrix `git show 0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5:.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv`, sha256 bba3a5c0506274df8099beed7950af92805e80ac3459d5cd4ac1341de362e1cc)
verified-at: 2026-11-05 — the battery and manifest are committed in the round-90 landing commit; the landing measurement is `.ufo/waves/round-90/receipts/landing-battery.txt` and names the measured revision in its first line (Q36)
recheck: python3 -B verifiers/check_mutation_battery.py --rev <rev> --self-test (expect `0 failure(s) over 19 assertions`, exit 0), then python3 -B verifiers/check_mutation_battery.py --rev <rev> --work <scratch-dir> (expect `mutation battery killed 14 of 14 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`, exit 0, at a revision that carries the battery, its manifest and its registry row)

# Mutation battery (round 90 C1): a committed, revision-pinned kill/equivalence measure over the lane's two round-89 gates

## What it measures

`verifiers/check_mutation_battery.py` reads three committed inputs at `--rev`: the two gates it probes
(`verifiers/check_freeze_gate.py`, `verifiers/check_r86_routed_repairs_v3.py`), its manifest
`verifiers/fixtures/mutation-battery/manifest.tsv`, and its own registry row in `SKILL.md`. It prints

    mutation battery killed K of M kill-set; equivalents survived E of E; disclosed survivors S of S

and exits 0 iff K == M, M >= 8, E == E, E >= 4, S == S_declared, and guards G1–G3 pass. The manifest's
classes (`plans/round-90-addendum-1.md` A1) are:

- **kill** — 14 rows (8 freeze-gate, 6 D5 v3). Each recipe is anchored regex edits applied to the target's
  revision bytes; the row is killed when a probe's exit code or result-bearing output differs from the
  observed baseline.
- **equivalent** — 6 rows, generated at measurement time: a comment line before each top-level statement, a
  marker in each docstring, and trailing spaces on code lines outside strings (AST and tokenize, per target).
  Each must leave every probe identical.
- **survivor** — 0 rows. The r89 survivor `d5-m1a-d5iii-leg-only` was reclassified to `kill` at the round-90
  amendment: at the final bytes it flips both frozen D5 probes.

## The kill rule is a baseline flip, not a verdict

Each target's probes run unmodified first; that observation is the baseline. A mutant is killed only when some
probe's exit code or result-bearing output differs from that baseline. Output lines carrying 12+ hex runs or
scratch paths are excluded (run-specific tokens); exit codes are always compared. A probe timeout counts as a flip.

## Two-sided (Q47)

The measure is not a kill rate. Every declared kill-class mutant must be killed **and** every generated
equivalent must survive. The equivalent class is generated per run, not published as a fixed list, so a
fixed-list self-test cannot key on it.

## Bounds (what the measure does not prove)

1. **The equivalence leg is over the three declared rewrite classes only.** `E == E` verifies that those
   rewrites are semantics-preserving for the frozen probe set. It is not a general equivalence oracle.
2. **The minimum pins are floors, not coverage.** M >= 8 and E >= 4 stop an empty or trivial manifest from
   satisfying the equalities (critic F6); they do not establish that the 14 kill rows cover the targets.
3. **Three of the thirteen ported kills are self-test-only**, and the battery's own guard self-test has three
   surviving mutants (G1 commit-check skip, G1 clean-tree guard off, revision-copy restore not re-read). Both
   are disclosed in the round-90 landing receipts, not counted in the predicate.
4. **The d5 baseline is path-dependent (Q79).** The base-receipt probe reads `closed 4 of 5, instance drift 4`
   at the round base and the battery observes that baseline, so a kill there is a flip from the observed value.
5. **Anchors are revision-bound.** A recipe whose anchor is absent from the measured bytes is
   could-not-evaluate (exit 2), never skipped: the r89 anchor `if not grew:` no longer occurs at the final
   bytes, and the port uses `if not grew and not added:`.

## Reviewer-judged parts

Named non-author seats judged: the manifest's class assignment per row (ReviewerBattery, round-90 wave), the
survivor disposition, and the sufficiency of the probe set (not measured here; see the round-90 lesson § Gate).
