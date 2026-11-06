# MutTesterCounterV4 — mutate the v4 counter itself (scratch copy only)

Seat: MutTesterCounterV4 (mutation-tester, r96-w1, leaf — no subagent dispatch).
Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin (read-only for this seat except this report and
`.ufo/waves/round-96/w1/MutTesterCounterV4/`).
Scratch: `/fast/scratch/hyaku/kotoba-r96/MutTesterCounterV4` (TMPDIR + HYAKU_SCRATCH; removed before yield).
Tools installed: none (Python 3.14 stdlib, `python3 -B`, git read-only + scratch-clone commits only).

## Assignment

Mutate the v4 counter `verifiers/fixtures/round-96/selftest-kills.py` (scratch copy only; lane file
byte-frozen). Port the round-95 counter mutants M1–M8 (MutTesterCounter95) and add v4-specific ones
M9 (failure prefix ignored / set to the r95 `FAIL `), M10 (the elif climb removed), M11 (the claim's
instrument path swapped). Run each mutated counter against the base `679775abb9…` (c1), the r95c1
positive control (only where relevant) and the five forgery worlds (built with the frozen
`build-forgeries.py` into scratch). Report the matrix: which committed control receipt or world
exposes each counter mutant (verdict flip or tally deviation vs the committed receipt). A counter
mutant no control exposes is a gap — report it with the minimal new control world that would.

## Setup evidence

```
sha256 counter-pristine.py == lane verifiers/fixtures/round-96/selftest-kills.py
  1711b68fd9f443b53aa6878fdd367c8dc1cc6c38f4ec750d6725f0a0ab13b2b2
git -C $S/repo rev-parse --show-toplevel  -> /fast/scratch/hyaku/kotoba-r96/MutTesterCounterV4/repo
git -C $S/repo rev-parse HEAD             -> 679775abb9277a7b8d17f060b0f5b4ced2b127b6
pristine c1 at base, diff vs receipts/redbefore-c1-base.txt (minus the `claim` header and `rc=`):
  "BASE READING IDENTICAL TO COMMITTED RECEIPT"
pristine r95c1 at base: R95C1-PREDICATE-MET, `R95C1 targets killed 3 of 3 (run errors 0); positive
  killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` — identical to
  receipts/poscontrol-r95c1-base.txt.
```

Five forgery worlds rebuilt with the frozen `build-forgeries.py 679775ab…` into `$S/forgeries`
(identity `forgery`, scratch repos only). Every pristine reading of every rebuilt world reproduces
its committed receipt's verdict **and** summary line exactly (see `receipts/analysis.md`,
"committed receipt match: YES" on all six c1 worlds and on r95c1).

## Counter mutants under test

All are 1:1 line-count replacements in the scratch copy; the generator asserts each anchor matches
exactly once (`mutants.diff`, `mutants.sha256`, line numbers below are the pristine file's).

| id | line | mutation (anchor -> replacement) |
|---|---|---|
| M1-classify-rc-only | 138 | `if rc == 1 and n >= 1 and fails >= 1:` -> `if rc != 0:` |
| M2-classify-drop-fail-line | 138 | same anchor -> `if rc == 1 and n >= 1:` |
| M3-code-decoys-skipped | 302 | `held_code += cls == "CLEAN"` -> `held_code += 1` |
| M4-comment-decoys-skipped | 298 | `held_comment += cls == "CLEAN"` -> `held_comment += 1` |
| M5-runner-writes-mutant-to-disk | 266 | `path.write_text(on_disk, …)` -> `path.write_text(text, …)` (rule 3 broken) |
| M6-honest-clean-conjunct-dropped | 310 | `met = cls_h == "CLEAN" and killed == n …` -> `met = killed == n …` |
| M7-decoy-held-rc0-no-summary | 298,302 | both decoy tallies -> `cls == "CLEAN" or rc == 0` |
| M8-positive-forced-killed | 291 | `pos = 1 if cls == "REPORTED-FAILURE" else 0` -> `pos = 1` |
| M9a-prefix-ignored | 137 | `if ln.startswith(fail_prefix)` -> `if ln.strip()` |
| M9b-prefix-r95-FAIL | 81 | c1 `"fail_prefix": "self-test FAIL: "` -> `"FAIL "` |
| M10-elif-climb-removed | 203 | `while isinstance(best, ast.If) and …` -> `while False and …` (v3 behaviour) |
| M11-instrument-swapped | 80 | c1 `"instrument": DP,` -> `"instrument": MB,` |
| M12-anchor-count-weakened | 278 | `if found != count:` -> `if found < count:` |
| M13-restore-guard-removed | 304 | `if path.read_text(…) != original:` -> `if False and …` |
| M14-summary-first-not-last | 136 | `n = int(found[-1][0])` -> `n = int(found[0][0])` |
| M15-decoy-guard-always-true | 214 | `'if __name__ == "__decoy__":\n'` -> `'if True:\n'` |
| M16-killed-counts-run-errors | 286 | `killed += cls == "REPORTED-FAILURE"` -> `killed += cls != "CLEAN"` |

## Matrix (18 counters x 7 contexts; full text in `receipts/matrix.tsv`, `receipts/analysis.md`)

`FLIP` = the verdict line changes; `TALLY` = same verdict, summary line differs; `—` = identical
reading (inert). Contexts are the committed receipts; the pristine reading of each is the baseline.

| mutant | base c1 | f1-sniff | f2-crash | f3-summary | f4-honest | f5-label | r95c1 |
|---|---|---|---|---|---|---|---|
| M1 | — | — | — | TALLY | — | — | — |
| M2 | — | — | — | TALLY | — | — | — |
| M3 | — | TALLY | — | — | TALLY | — | — |
| M4 | — | TALLY | — | — | TALLY | — | — |
| M5 | — | TALLY | — | — | — | — | — |
| M6 | — | — | — | — | **—** | — | — |
| M7 | — | — | — | — | — | — | — |
| M8 | — | — | — | — | — | — | — |
| M9a | — | — | — | TALLY | — | — | — |
| M9b | TALLY | TALLY | TALLY | TALLY | TALLY | TALLY | — |
| M10 | **FLIP** | **FLIP** | **FLIP** | **FLIP** | **FLIP** | **FLIP** | — |
| M11 | **FLIP** | **FLIP** | **FLIP** | **FLIP** | **FLIP** | **FLIP** | — |
| M12 | — | — | — | — | — | — | — |
| M13 | — | — | — | — | — | — | — |
| M14 | — | — | — | — | — | — | — |
| M15 | — | — | — | — | — | — | **FLIP** |
| M16 | — | — | TALLY | TALLY | — | — | — |

### Observed exposure lines (verbatim)

- **M1 / M2 / M9a — f3-summary-no-line** (the world prints a summary and exits 1 with no
  `self-test FAIL: ` line). Pristine: `mutant t04-le-to-lt rc 1 RUN-ERROR (not a kill): 1 failure(s)
  over 57 assertions` and `C1 targets killed 0 of 11 (run errors 1)`. Mutant: `mutant t04-le-to-lt
  rc 1 KILLED` and `C1 targets killed 1 of 11 (run errors 0)`. Tally deviation only (verdict UNMET
  both ways, because the other ten targets still survive).
- **M3 / M4 — f1 and f4**: `code decoys held 0 of 11` -> `11 of 11` (M3), `comment decoys held 0 of
  11` -> `11 of 11` (M4). Tally only.
- **M5 — f1**: pristine `killed 0 of 11 … comment 0/11; code 0/11`; mutant `killed 11 of 11 … comment
  0/11; code 0/11`. The sniffer starts killing (source on disk is the mutant) but still trips on both
  decoys, so the verdict stays UNMET. **Tally only — the committed battery never flips M5.**
- **M9b — every c1 world**: `positive killed 1 of 1` -> `0 of 1` (the c1 `self-test FAIL: ` lines do
  not start with `FAIL `, so the positive run is reclassified RUN-ERROR). On f4 it is louder:
  `honest RUN-ERROR`, `killed 0 of 11 (run errors 11)`, `positive killed 0 of 1`.
- **M10 — every c1 world**: `C1-PREDICATE-UNMET` (rc 1) -> `C1-NOT-EVALUATED: code decoy
  t05-finish-allna-pass does not compile: invalid syntax (verify_dispatch_prompts.py, line 499)`
  (rc 2). This is exactly the committed `receipts/predraft-elif-decoy.txt` shape, which is direct
  evidence that the v4 climb is load-bearing. r95c1 is unaffected (no `elif`-arm mutant there).
- **M11 — every c1 world**: `C1-NOT-EVALUATED: anchor miss: t01-var-dropped matches 0 time(s),
  expected 1` (rc 2). r95c1 unaffected (the swap is inside `CLAIMS["c1"]`).
- **M15 — r95c1 only**: `R95C1-PREDICATE-MET` (rc 0) -> `R95C1-PREDICATE-UNMET` (rc 1) with
  `code decoys held 1 of 3` (n5's `raise` and n11's `return` decoys fire; n1's assignment decoy is
  overwritten by the original statement that follows it). **No c1 world exposes M15**: at base the
  11 target behaviours are unobserved, so executing the mutated statements under `if True:` changes
  nothing observable (`code decoys held 11 of 11`).
- **M16 — f2 and f3**: `killed 0 of 11 (run errors 1)` -> `killed 1 of 11 (run errors 1)`.

## Gaps: counter mutants no committed control exposes

| mutant | committed exposure | minimal new control world (built in scratch, measured) | pristine reading | mutant reading |
|---|---|---|---|---|
| M6-honest-clean-conjunct-dropped | **none — f4 does not expose it** | `g2-honest-trip-decoy-aware`: one arm fails when the decoy marker is ABSENT (so honest/mutant runs trip, decoy runs pass) | UNMET, `killed 11 of 11; honest REPORTED-FAILURE; comment 11/11; code 11/11` | **`C1-PREDICATE-MET` (false, rc 0)** |
| M7-decoy-held-rc0-no-summary | none | `g5-decoy-silent-zero`: `os._exit(0)` when a decoy marker is present (decoy runs exit 0 with no summary) | UNMET, `comment decoys held 0 of 11; code decoys held 0 of 11` | UNMET, `comment 11 of 11; code 11 of 11` (tally) |
| M8-positive-forced-killed | none | `g6-positive-survives`: filters the five p00-observing failures (`control: dispatch.04 verdict PASS`, `report_paths keeps an absolute report path`, `box proof: a complete corpus proves both boxes`, `box proof: a note-only manifest edit is still a proof`, `box proof: a twin of a must-fail case replaces it`) | UNMET, `positive killed 0 of 1` | UNMET, `positive killed 1 of 1` (tally; at the landing candidate this becomes a false MET) |
| M12-anchor-count-weakened | none | `g3-duplicate-anchor`: a dead duplicate of `if round_n <= value:` inside `if False:` | `C1-NOT-EVALUATED: anchor miss: t04-le-to-lt matches 2 time(s), expected 1` (rc 2) | `C1-PREDICATE-UNMET` (rc 1) — **FLIP** |
| M13-restore-guard-removed | none — **equivalent mutant** | none possible; see finding 4 | — | — |
| M14-summary-first-not-last | none | `g4-two-summaries`: an early `0 failure(s) over 0 assertions` before the real summary | UNMET, `positive killed 1 of 1` | UNMET, `positive killed 0 of 1` (tally) |
| M5 (verdict level) | f1 exposes only the tally | `g1-decoy-aware-sniffer`: source sniffer that drops `#` lines and `__decoy__` blocks | UNMET, `killed 0 of 11; comment 11/11; code 11/11` | **`C1-PREDICATE-MET` (false, rc 0)** — rule 3 is what stops it |

The six new worlds are scratch-only (`$S/extra/*.repo`, identity `forgery`), built by
`receipts/build-extra.py` (world names and commits in `receipts/extra-built.txt`). They are
proposals for the control battery, not landed artifacts.

## Findings

1. **The committed battery has six real gaps (M6, M7, M8, M12, M14, and M5 at verdict level).**
   Of these, **M6 is the sharpest: `f4-honest-trip` does not expose M6 at all** — not even at tally
   level — although plans/round-96.md names f4 as "the M6 shape". f4's always-failing arm also fires
   on every decoy run, so its decoys read `0 of 11`; the honest-conjunct mutant therefore still reads
   UNMET (`met` needs `held_comment == n and held_code == n`). The M6 shape needs a world that trips
   only when the decoy marker is *absent* (`g2`), which flips M6 to a **false MET**.
2. **Rule 3 (source-blind) is load-bearing and the battery only checks it at tally level.** f1 shows
   M5 as `killed 11 of 11` but keeps it UNMET through the decoys. A decoy-aware source sniffer (`g1`)
   is scored UNMET by the honest counter and **MET** by M5 — the only world in this matrix that
   converts a rule-3 break into a false acceptance. If the battery is extended, g1 is the world to add.
3. **M10 and M11 are strongly exposed** (verdict flip to `C1-NOT-EVALUATED`, rc 2) by the base
   do-nothing control and by all five forgery worlds. `predraft-elif-decoy.txt` is a committed,
   independent receipt of the M10 shape. M9b is exposed by the base control at tally level
   (`positive killed 1 of 1` -> `0 of 1`).
4. **M13 is an equivalent mutant, not a gap.** The only writer between the last `run_text` and the
   restore guard is the `finally: path.write_text(original)` itself; if that write fails it raises
   before the guard is reached, and if it succeeds the guard is trivially true. Demonstrated with
   `g7-self-immutable` (the instrument `os.chmod(__file__, 0o444)`s itself): pristine and M13 both
   exit **rc 1 with an uncaught `PermissionError` traceback and no verdict line**, byte-for-byte the
   same failure mode. No control can distinguish them, and removing the guard cannot change a
   reading.
5. **Counter robustness defect (new, not a mutant exposure):** in that same `g7` run the counter
   violates its own exit ladder — a could-not-evaluate (the world cannot be measured because the
   instrument makes its own file unwritable) surfaces as an **uncaught `PermissionError` with rc 1**
   (the content-fail code) instead of `C1-NOT-EVALUATED`, rc 2. The `finally` restore and the
   `read_text` guard are both outside the `NotEvaluated` contract. A driver that keys on the verdict
   line sees `<no verdict>`; a driver that keys on rc reads "content fail". Fix (L1 decision, not
   this seat's): wrap the restore/guard in `try/except OSError -> NotEvaluated`.
6. **The code decoy is weak for non-terminal statements.** Under M15 the r95c1 decoys trip only
   2 of 3: n1's `committed = git_show(...)` decoy is immediately overwritten by the original
   statement that follows it, so the decoy stays held even though it executes the mutant. Decoy
   power depends on statement shape (terminal `raise`/`return` yes, assignment no). Not a defect of
   the counter's bookkeeping, but it bounds what a "code decoy held" line proves.
7. **M1 is exposed only by f3, not by f2.** The crash world produces no summary at all, so
   `classify` returns RUN-ERROR at the `if not found` line before the rc test; only a world with a
   summary and no failure line exercises the rc conjunct. The battery needs f3 (it has it) and would
   not notice M1 from f2 alone.

## Bounds / risks

- Every reading here is against the **base** instrument (`verify_dispatch_prompts.py` at
  `679775ab…`), because the C1 arms are not landed yet. The landing candidate changes which c1
  behaviours are observed; mutant exposure at the candidate is expected to grow (M15 in particular:
  once the 11 behaviours are observed, `if True:` decoys should stop holding), but that is
  **[INFERENCE]**, not measured — the candidate did not exist during this seat.
- Forgery-world commit hashes differ from the committed receipts (timestamps); only the reading
  lines are compared, and all six pristine readings match their receipts exactly.
- The six `g*` worlds are proposals built in scratch; they are not committed and not claimed as
  landed controls.
- The counter was never edited in the lane; the lane file's sha256 was re-checked after the matrix
  (`receipts/counter-pristine.sha256`).

## Receipts (`receipts/`)

`counter-pristine.py`, `counter-pristine.sha256`, `mutants.sha256`, `mutants.diff`, `matrix.tsv`,
`matrix.json`, `analysis.md`, `base-pristine.txt`, `forgeries-built.txt`, `extra-built.txt`,
`runs/` (50 full counter outputs: every counter on the base world and on r95c1, the six g-world
pairs, and both g7 runs).
