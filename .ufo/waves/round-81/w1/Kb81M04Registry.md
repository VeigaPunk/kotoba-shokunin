# Kb81M04Registry — mutation probe: registry + governance surface

Seat: mutation-tester, round 81 w1. Date: 2026-10-27.
Scope: four assigned mutants against the lane's governance/gate detectors.
Detectors run per mutant (exact commands, run in the scratch clone at
`/fast/scratch/hyaku/kotoba-r81/Kb81M04Registry/clone`, deleted after receipts
were copied):

- `python3 -B verifiers/check_gate_registry.py --rev <rev>` (LANE is derived
  from the script's own path, so the clone's copy measures the clone)
- `python3 -B verifiers/verify_corpus_integrity.py --repo .` (working tree)
- bonus third detector `python3 -B verifiers/verify_corpus_independent.py --repo .`

Receipts: `.ufo/waves/round-81/build/Kb81M04Registry-*.txt` (17 files,
`base-*` = pristine + `mut{ A,B,C1,C2,D }-*` for each detector).

## Pristine baseline (commit b284223105f4d106f7e8f56ed4fd296c643cda0e)

- registry: `gate registry rows conformant 63 of 63 lane verifiers; phantom 0`,
  exit 0. Baseline for mutants: green.
- integrity: `4/9 checks pass; DRIFT: corpus.index.tracked_files (155≠154),
  corpus.index.unindexed (1), corpus.pointers.report_total (111≠109),
  corpus.pointers.report_dead (1), corpus.pointers.commit_unresolvable (2)`,
  exit 1 — the declared r81 base state (plan § Trigger). A mutant is KILLED
  iff it adds a new defect class or defect count vs this base drift set;
  identical output = detector blind to the mutation, not a pass.
- independent: exit 1, same pointers-family drifts.

## Mutant A — C2 counter file, no SKILL.md registry row (Q35 arm)

Commit e1f45174de3f498f97251ed8ed2fbde7e86fd1d7: new
`verifiers/check_sdk_allowed_tools.py` (46-line stub, `--rev` +
`--self-test` handlers; the real reviewed counter was not yet published under
the wave build dir at run time — for the row-absence arm the file's
implementation is immaterial, only its presence in `ls-tree verifiers/`
matters).

- registry: **KILLED** — `verifiers/check_sdk_allowed_tools.py  no registry
  rows naming it: 0 (need 1)`; `conformant 63 of 64`, exit 1. The Q35 arm
  fires exactly as designed.
- integrity: exit 1, byte-identical drift output to base (invisible — correct,
  `verifiers/` is outside `corpus/` scope). independent: identical, exit 1.

## Mutant B — registry row, `gate` kind, self-test `none`

Commit 0ea2640c4717bc573f0e0584d730b995df02c0dc: SKILL.md gains one row for
`check_sdk_allowed_tools.py` — `gate | 0=clean, 1=failed, 2=could-not-evaluate
| none | in-file | none (read-only) | kotoba` (all other cells conformant, so
the defect is singular).

- registry: **KILLED** — `verifiers/check_sdk_allowed_tools.py  no  gate with
  self-test none`; `conformant 63 of 64`, exit 1. `judge_row`'s
  `clean(st)=="none" and kind=="gate"` arm fires.
- integrity: identical-to-base, exit 1 (SKILL.md is outside corpus scope).

## Mutant C — `.ufo/wapee` stray recreated (R80-D2 class)

594-byte copy of the live lane's `.ufo/wapes` probe artifact.

- C1 (untracked file present, rev = base): registry exit 0 `63 of 63`;
  integrity exit 1, output byte-identical to base; independent identical.
- C2 (committed, 5cafbb40c214fb6036baa910e3993f37ea339fc6): registry exit 0;
  integrity exit 1, byte-identical drift to base; independent identical.
- **SURVIVED, both forms** — a coverage finding. `tracked_files` is derived
  from `git ls-files corpus/` only (`tracked_corpus_files()`), so a stray
  under `.ufo/` is invisible to the corpus gates in both tracked and
  untracked form; the registry's universe is `ls-tree verifiers/` `.py|.sh`
  only. `check_correction_sweep.py`'s registry names no untracked-file arm
  (grep: no `ls-files`/`status`/`untracked`). The r80 `.ufo/wapes` was caught
  by seat observation (r80 w1 reports F10/F11), not by any gate — this
  measures the plan's R3 as a manual-only repair: nothing executable stands
  behind "a seat's probe output lands only inside the wave dir". NOT
  permission to change the contract; routed as a candidate mistake class
  (stray-artifact detector gap).

## Mutant D — coverage-map row with a typo'd path

Commit 386cae13183382e7f013d3dde0cd0d7a9a790281: corpus/README.md:157
`lessons/round-79-verifier-spotcheck.md` → `...-spotchek.md` (the file is
covered by exactly one index token).

- integrity: **KILLED** — three NEW DRIFT classes on top of the base five:
  `unindexed 1→2` (+ `corpus/lessons/round-79-verifier-spotcheck.md`),
  `stale_patterns 0→1` (`README.md:157`), `missing_paths 0→1`
  (`... -> lessons/round-79-verifier-spotchek.md`). `2/9 checks pass`, exit 1.
- independent: KILLED — same three observations (`unindexed=2 stale=1
  missing=1`), exit 1. Both corpus gates catch the class.
- registry: exit 0 (SKILL.md untouched) — orthogonal detector, correctly
  blind.

## Verdicts

| mutant | expected detector | registry | integrity | independent | verdict |
|---|---|---|---|---|---|
| A counter w/o row | check_gate_registry (Q35) | exit 1, fired | base-identical | base-identical | KILLED |
| B gate+selftest none | check_gate_registry | exit 1, fired | base-identical | — | KILLED |
| C `.ufo/wapee` stray | none exists | exit 0 (both forms) | base-identical | base-identical | SURVIVED — gap |
| D typo'd index path | integrity unindexed/stale | exit 0 | exit 1, 3 new DRIFTs | exit 1, same | KILLED |

Registry arms (A, B) and the index-family arms (D) fire on the declared
detectors; the stray-artifact class (C) has no executable detector —
consistent with routed defect R80-D2 being a human-found defect and with the
plan's Q76 candidate criterion.

## Restoration evidence

`git -C $S/clone reset --hard b2842231` + `rm -f .ufo/wapee`; final
`git status --porcelain` empty and `git rev-parse HEAD` =
`b284223105f4d106f7e8f56ed4fd296c643cda0e`. Post-restore sha256 of
`verifiers/check_gate_registry.py + verify_corpus_integrity.py +
corpus/README.md + SKILL.md` (combined): `14cdf29ddb44d4…`. Scratch dir
removed after receipts copied to the build dir. No lane files touched; all
mutants committed only inside the scratch clone.

VERDICT: 3 of 4 mutants killed on their declared detectors (A, B, D); mutant C `.ufo/wapee` survived all gates in untracked and committed form — measured coverage gap behind routed defect R80-D2, not a contract change.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81M04Registry.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81M04Registry-{base,mutA,mutB,mutC1,mutC2,mutD}-{registry,integrity,independent}.txt (17 receipts)
