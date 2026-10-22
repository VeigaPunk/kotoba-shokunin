# BaselineGatesB — no-harm baseline, part B (base f3046466, private clone)

Result: **HOLDS for 2 of 6; 4 red at base — 3 red caused by host substrate (omp 18.12.6),
1 red caused by lane bytes already committed at f3046466.** No round-50 edit is responsible for
any red: every command ran in a pristine clone whose `git status --porcelain` is empty.

## Table

| # | command (in `/fast/scratch/hyaku/kotoba-r50/build/baseline-gates-b/lane`) | exit | summary line |
|---|---|---|---|
| 1 | `python3 -B verifiers/verify_harness_independent.py --self-test` | 0 | `0 failure(s) over 123 assertions` |
| 2 | `python3 -B verifiers/compare_harness_independent.py --self-test` | 0 | `self-test: 0 failure(s) over 330 assertions` |
| 3 | `python3 -B verifiers/verify_surfaces.py --json` | 1 | `"exit_code": 1, "pass": 5, "fail": 2` — FAIL `surfaces.literal_present`, `surfaces.no_uncovered_class` |
| 4 | `python3 -B verifiers/verify_harness_claims.py` | 1 | `21/28 checks pass; DRIFT: omp.db.rows, omp.offered.skills, omp.cache.misses, omp.catalogue.total, omp.catalogue.missing_names, omp.cache.verified_skills, oc.roots.names_plus_builtin` |
| 5 | `python3 -B verifiers/check_substrate_pins.py` | 1 | `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` |
| 6 | `bash verifiers/fault_injection_corpus.sh` | 1 | `verdict: FAILURES PRESENT` — `fault-0-control … FAIL-control-dirty`, `fault-f … FAIL`, `fault-g … FALSE-POSITIVE`, `fault-h … FAIL`; faults a/b/c/d1/d2/e all `PASS` |

## Cause per red

**#5 — host state.** `verifiers/baseline.json` `measured_against` pins omp/18.12.5 at
sha256 `fdbc8136…` and mtime `2026-10-21T03:30:38.135013187-03:00`. The installed
`/home/vgpnk/.local/bin/omp` reports `omp/18.12.6`, sha256
`85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`, mtime
`2026-10-21 20:37:24.615549837 -0300` — 61 606 s (17.1 h) after the pin. opencode's pin
(`179ca421…`) still holds, so the guard is discriminating and only omp moved. Re-pin work, not lane bytes.

**#3 — host state, same cause, one layer further in.** The two FAILs are the omp-dump checks; the
opencode half passes (`surfaces.opencode_extract` 9/9 classes, 7/7 rules) and the four
baseline-parity checks pass (42 ids, literals, kinds, 8 reasoned exclusions). The omp failures say
`0 loader class(es) extracted from the omp dump while the baseline declares 8`, and the extractor
`OMP_CALL_RE` (verify_surfaces.py:156-160) gates on a 15-name callee allowlist
`(Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo|lq|Xl|Fo)`. In the 18.12.6 strings dump the registration
callees have rotated again: the only callees carrying the unchanged three-argument shape are
`Kl` and `Ho` (3 hits each), e.g. `Kl(u, "gemini", "GEMINI.md"` and `Ho(u, "gemini", "system.md"`;
2-argument variants: 0. Neither name is on the allowlist, so extraction returns empty by substrate
rename, not by lane drift. The check fires loudly (vacuity guard) rather than passing silently — that
is the designed behaviour, and the fix is a callee-allowlist extension measured on 18.12.6.

**#3 re-pin probe (measured, scratch copy `/tmp/vs-probe.py`, lane untouched).** Feeding the
18.12.6 dump through `--omp-strings` and widening the allowlist: `+Kl|Ho` → 6 of 8 baseline
loader-group classes extract; `+Kl|Ho|bq` → 7 of 8. The last one,
`omp:claude-md/CLAUDE.md`, is registered as `bq(u, S$, "CLAUDE.md")` with `var S$ = "claude-md"`,
but `S$` is rebound elsewhere in the dump so `constant_table` (verify_surfaces.py:300-313) drops it
as a conflicting rebind by design and the class surfaces as `omp:<unresolved-var:S$>/CLAUDE.md`. So
the substrate fix is three callee names plus one conflict decision, not a redesign. The probe still
exits 1 (2 FAIL rows → 1 FAIL + 1 FAIL on the unresolved var), i.e. it is a diagnosis, not a fix.

**#4 — host state.** Every drifted observation is read from host surfaces
(`~/.local/bin/omp`, `~/.omp/agent/skill-descriptions.db`, the newest session catalogue, the
opencode log): offered skills 11 (pinned 7), db rows 17 (14 well-formed), cache misses 4 (pinned 0),
catalogue 10 lines with 7 matched and `catalogue_missing_names = ['create-toolset','unreal-mcp','unreal-skill']`,
verified skills 11, opencode roots 11 live names + 1 builtin = 12 (pinned 7). The 4 extra offered
skills are host installs (`create-toolset`, `unreal-mcp`, `unreal-skill`, …) that the round-47 pin
predates. `--no-baseline --json` exits 0 and prints the same numbers, i.e. the instrument is healthy and
only the pin lags. Lane bytes are not implicated: no kotoba file feeds these observations.

**#6 — lane bytes, pre-existing at f3046466.** The corpus instruments read the tree only (no host
input), and the driver's own pristine control world is already dirty. `verify_corpus_integrity.py
--json` in the clean clone exits 1 with four DRIFT rows: `corpus.index.tracked_files` 67 vs 66,
`corpus.index.unindexed` 1 (`corpus/lessons/round-49-verifier-spotcheck.md`),
`corpus.pointers.report_total` 44 vs 43, `corpus.pointers.report_dead` 2. The independent instrument
agrees (exit 1: md_files 66, tracked 67, unindexed 1, report_dead 2), and it names the dead pointers:
`corpus/lessons/round-48-verifier-spotcheck.md:9` and `:23`, both `.ufo/reports/round-48/kotoba.md`.
Two of the four are documented and deliberate: `corpus/README.md:68` states the round-48 pointers are
written repo-relative so they "read as `report_dead=2` … at base and after this round" (the report sits
in the fleet repository), and it records that the round-48 spot-check landed "without an index row,
indexed round 49" — the round-49 spot-check (landed at f3046466) repeats exactly that one-round
latency and is likewise unindexed. The two count drifts follow from the same landing:
`verifiers/corpus-baseline.json` was last recorded at `c48793d` (`tracked 63->66, report_total 41->43`)
and f3046466 added one corpus file and its pointers afterwards.

Timeline, same instrument, private clones of the lane at each commit: at `a5adc14^` (before the
round-48 spot-check landed) no row drifts; at `a5adc14` (the round-48 spot-check lands)
`corpus.pointers.report_dead` = 2, and it is still the only drift at `c48793d` (the round-49 landing,
which re-recorded the counts); f304646 adds `tracked_files` 67/66 (equal), `unindexed` 1 (zero) and
`report_total` 44/43 (equal). So this harness has been red for two rounds on the round-48 pointers
alone, and the round-49 spot-check landing added two more rows at base — round 50 inherits all four.

Consequence of #6 for the driver's own verdicts: `fault_must_fire` (fault_injection_corpus.sh:276)
gates on class membership only, so because the control already fires
`corpus.index.unindexed,corpus.pointers.report_dead`, rows **a** and **e** "PASS" are
non-discriminating: their fired sets are exactly the control's two classes, so the intended class was
already present before the plant. Rows b, c, d1, d2 are discriminating — each adds a class the
control lacks (`commit_nonhash`, `commit_unresolvable`, `missing_paths`, `stale_patterns`
respectively). Until the round-48 pointers are rewritten (or the documented drift is encoded
in `control_clean`) and the round-49 spot-check is indexed with `corpus-baseline.json` re-recorded,
this harness cannot exit 0 in this tree regardless of round-50 content.

## Scoped implication for round 50

- C1/C2 claims and the D1–D6 work are unaffected by #1, #2, #6-lane: none of them reads the omp
  binary. Any claim or guard that cites `verify_surfaces.py` or `verify_harness_claims.py` is
  currently unmeasurable against the shipped omp and must be re-pinned (callee allowlist + claims
  baseline) or explicitly scoped out in the round-50 lesson.
- The corpus baseline (`tracked 66→67`, `report_total 43→44`) plus the round-49 index row are
  round-50 housekeeping that the harness makes visible; the two round-48 dead pointers are the only
  item that needs a decision rather than a count bump.

## Evidence

```
$ git -C lane rev-parse HEAD                    # f30464660c675d1c1e2851a3bf0366a3aaffe5a8  exit 0
$ git -C lane status --porcelain                # empty  exit 0
$ omp --version                                 # omp/18.12.6  exit 0
$ sha256sum ~/.local/bin/omp                    # 85d9daf3…ccfa4  exit 0
$ stat -c '%y %s' ~/.local/bin/omp              # 2026-10-21 20:37:24.615549837 -0300 256702432  exit 0
$ python3 -B verifiers/verify_harness_independent.py --self-test   # exit 0
$ python3 -B verifiers/compare_harness_independent.py --self-test  # exit 0
$ python3 -B verifiers/verify_surfaces.py --json                   # exit 1
$ python3 -B verifiers/verify_harness_claims.py                    # exit 1
$ python3 -B verifiers/check_substrate_pins.py                     # exit 1
$ TMPDIR=<scratch>/faults-tmp bash verifiers/fault_injection_corpus.sh   # exit 1 (13.14 s)
$ python3 -B verifiers/verify_corpus_integrity.py --json           # exit 1
$ python3 -B verifiers/verify_corpus_independent.py --json         # exit 1
$ git clone --no-hardlinks lane hist-<rev> && cd hist-<rev> && python3 -B verifiers/verify_corpus_integrity.py --json
    # a5adc14^: exit 0, no DRIFT rows · a5adc14: exit 1, report_dead 2 ·
    # c48793d: exit 1, report_dead 2 · f304646: exit 1, +tracked_files/unindexed/report_total
$ strings -n 4 ~/.local/bin/omp | grep -oE '<callee>\("<group>", "<file>.md"'  # Kl 3, Ho 3, bq 2
$ python3 -B /tmp/vs-probe.py --json --omp-strings out/omp-strings-18126.txt \
    --baseline verifiers/surfaces-baseline.json \
    --inventory corpus/knowledge/instruction-surface-census-round13.md
    # +Kl|Ho exit 1 pass 6 fail 1 · +Kl|Ho|bq exit 1 pass 5 fail 2 (S$ unresolved)
```

Raw outputs: `/fast/scratch/hyaku/kotoba-r50/build/baseline-gates-b/out/` (`*.out`, `*.err`,
`omp-strings-18126.txt`). Reads were taken from the private clone at
`/fast/scratch/hyaku/kotoba-r50/build/baseline-gates-b/lane`; the fault driver builds its worlds by
`git clone` under `$TMPDIR` (fault_injection_corpus.sh:76-77, worlds at `$WORLDS`, line 75) and never
writes into the repo.

Tooling: nothing installed or upgraded (all six commands ran with host python3 3.14.8, bash, git).
Bounds: read-only on the lane; the only lane write is this file. No subagents, no jj, no git writes.

Remaining unknowns: (i) whether the round-49 spot-check's missing index row is intended to be closed
in round 50 or is a repeat defect of the round-48 pattern — the round-49 lesson's own coverage row
(line 160) claims an index row only for the census entry, not for itself; (ii) whether the
`report_dead=2` accepted drift should be encoded in `control_clean` rather than left to keep this
harness red permanently; (iii) how the `S$` conflicting rebind should be resolved for the re-pin
(per-callee group guard versus a scoped constant table) — measured, not decided.
