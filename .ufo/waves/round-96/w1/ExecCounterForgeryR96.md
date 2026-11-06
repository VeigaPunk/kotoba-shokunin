# ExecCounterForgeryR96 — v4 counter forgery attack (scratch only)

Round 96, wave r96-w1. Claim under attack: C1 (`selftest-kills.py c1`, v4). Base: freeze commit
`679775abb9277a7b8d17f060b0f5b4ced2b127b6`. The lane repo was never written: every world lives in
`/fast/scratch/hyaku/kotoba-r96/ExecCounterForgeryR96/worlds/<world>.repo`, every receipt and patch
under `.ufo/waves/round-96/w1/ExecCounterForgeryR96/`.

## Method

Each world is a self-test of `verifiers/verify_dispatch_prompts.py` at the freeze commit with one
insertion before the `for f in failures:` report loop (the build-forgeries insertion point). The
insertion tries to reach the C1 target **without a behavioural arm**. Each world was committed in its
own `--shared` scratch clone under the identity `scratch <scratch@invalid>`, its patch saved
(`git diff --binary <freeze> HEAD`), and measured with the frozen counter:

```
HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r96/ExecCounterForgeryR96 \
  python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-96/selftest-kills.py \
  c1 <world-commit> <world-repo>
```

All nine patches pass `git apply --check` on a fresh clone at the freeze commit
(`verify-clone`, toplevel asserted). The counter was never edited; the fix simulation below is a
scratch copy (`counter-fix-sim.py`) and is labelled as such.

## Worlds and readings

| world | shape (no behavioural arm) | commit | patch sha256 | counter tally | reading | caught by |
|---|---|---|---|---|---|---|
| g1-recursive-sniff | recursive `co_consts`/`co_names`/opcode walk over all live code objects (incl. the decoy body) | `f429b87acbe5291fb6debd47beb30744793f4917` | `fdce396b…b84f74` | killed 11/11; honest CLEAN; comment 11/11; **code 6/11** | UNMET | rule 2 (code decoy guard) |
| g2-structural-sniff | non-recursive structural sniffer at the mutated code object (names/consts/opcodes/slices) | `bf73898816855646eb72eb9015edbb26d3132a72` | `7d4fdeed…6348c1` | killed 11/11; honest CLEAN; comment 11/11; **code 6/11** | UNMET | rule 2 (code decoy guard) |
| **g2b-guard-aware-sniff** | same, plus a control-flow filter that drops the `if __name__ == "__decoy__":` body (proves the decoy guard dead) | `c0cb3c5f250944f8230c3e9bb6c501b3e61ea4c4` | `e9f7215b…fd5d4b` | killed 11/11; honest CLEAN; comment 11/11; code 11/11 | **MET** | — (disclosed v3 bound) |
| **g3-recompile-compare** | recompiles the on-disk source and compares `co_code`/`co_consts`/`co_names` with the running functions | `a528758770bce06d11aad756b41c3a9819a27670` | `e1c8cf54…04c231` | killed 11/11; honest CLEAN; comment 11/11; code 11/11 | **MET** | — (disclosed v3 bound) |
| g4-inspect-linecache | `inspect.getsource` / `linecache` source sniffer | `0976fc7a856bcada68735607976e26c9f05f9e13` | `39ee6e2b…a446e3` | **killed 0/11**; honest CLEAN; decoys 11/11 | UNMET | rule 1 (kill rule) |
| g5-harness-sniff | `/proc/self/cmdline` + argv + TMPDIR harness sniffer | `5c015cbb5d97ae78d9fffb9b192916fd33b87d5c` | `9bc21295…4021a5` | killed 11/11; **honest REPORTED-FAILURE**; decoys 0/11 | UNMET | honest conjunct + rule 2 |
| g6-fake-line-exit | fake `self-test FAIL:` line + `SystemExit(1)`, no summary | `28d3a419a2cc991f56ec2ed4fb83e31de0c6f5d6` | `0b016c78…cd3d1cd8` | killed 0/11; run errors 1; honest CLEAN; code 10/11 | UNMET | rule 1 (summary conjunct) |
| **g7-stateful-fake** | writes a marker in the shared `TMPDIR` on the first run, then prints a fake `self-test FAIL:` + `1 failure(s) over 1 assertions` and exits 1 on every later non-decoy run; reads the on-disk decoy text to hold the decoys | `86953dd6fab1f72971914dfa6976b42eb24f2e3c` | `2c66e70a…402f1f` | killed 11/11; honest CLEAN; comment 11/11; code 11/11 | **MET** | — **new finding** |
| **g8-clone-marker** | same, marker written next to the instrument in the shared clone (not TMPDIR) | `473bbc1b802f8203a3e72fa8b41f0b5ca96090fe` | `1fa64f44…e98b96` | killed 11/11; honest CLEAN; comment 11/11; code 11/11 | **MET** | — **new finding** |

Exact tally lines (`.counter.txt` receipts):

```
g1: C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 6 of 11
g2: C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 6 of 11
g2b: C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
g3: C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
g4: C1 targets killed 0 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
g5: C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest REPORTED-FAILURE; comment decoys held 0 of 11; code decoys held 0 of 11
g6: C1 targets killed 0 of 11 (run errors 1); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 10 of 11
g7: C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
g8: C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
```

## Findings

### F1 (new, high) — the counter shares run state and runs the honest self-test first; a fake reported failure reads MET

g7 and g8 have **no behavioural arm at all** and never inspect the instrument's code. They exploit
two properties of `selftest-kills.py`:

1. all runs of one counter invocation share `work/tmp` (`TMPDIR`) and the clone `work/world/kotoba-shokunin`;
2. the honest self-test runs **first**, so the first run is the only run without a marker.

g7 writes `$TMPDIR/.g7_seen` on the first (honest) run, then on every later run that is not a decoy
prints `self-test FAIL: …` and `1 failure(s) over 1 assertions` and exits 1 — rule 1's
REPORTED-FAILURE shape, with no assertion and no observation of t01..t11. It holds both decoys by
reading the on-disk text (`# r96-decoy` for the comment decoy, `if __name__ == "__decoy__":` for the
code decoy). g8 is the same with the marker next to the instrument in the shared clone, so a fresh
`TMPDIR` alone would not close the class. Both read `C1-PREDICATE-MET`, rc 0.

This is **not** the disclosed v3 code-object bound: the header's rule 3 bound is about a sniffer of
its own compiled code objects; g7/g8 are a cross-run state + fake-summary forgery, undisclosed.

Severity: high for the counter (the predicate is satisfiable with zero behavioural arms); mitigated
in the overall process only by the reviewers' source check, which the plan already requires.

Minimal fix recommendation (measured, see below): run the honest self-test **once more at the very
end** and require both honest runs CLEAN. The double honest run alone closes g7 and g8 (the last
honest run sees the marker and fakes a failure). A fresh `TMPDIR` per run is complementary hardening
(g8 shows a fresh `TMPDIR` alone is insufficient, because the clone is shared too). Residual risk: a
world that reads `verifiers/fixtures/round-96/selftest-kills.py` from the clone (it is in the
checkout) can learn the exact run schedule and fake failures on exactly the mutant runs; closing that
needs isolation (a sandbox dir holding only the instrument + `SKILL.md`) and/or a randomized run
order, not just the double honest run.

### F2 (disclosed bound, medium) — recompile-compare reads MET; the mirror run closes it

g3 recompiles `Path(__file__).read_text()` and compares the running functions' `co_code`/`co_consts`
with the recompiled ones. Source-blind mutant runs hold the honest bytes on disk, so g3 detects every
mutant; the decoy runs hold the decoy text on disk and in memory, so g3 is CLEAN and both decoys
hold. It reads MET with no behavioural arm. This is the v3 disclosed bound (`plans/round-96.md`
§Disclosed bounds: "the v3 code-object-sniffer bound is unchanged in v4"; routed defect 4).

Minimal fix recommendation (measured): a **mirror run** per target and for the positive — execute the
mutant text with the mutant text on disk too, and require REPORTED-FAILURE there as well. A
behavioural arm kills in both runs; g3 is CLEAN in the mirror run. The mirror run also does not
weaken source-blindness (f1 stays CLEAN in the source-blind run and therefore still fails the
"killed in both" requirement).

### F3 (disclosed bound, informational) — guard-aware code-object sniffer reads MET and survives the proposed fix

g2b walks the live function's own instructions and drops the body of any
`if __name__ == "__decoy__":` guard (a small control-flow filter). It kills all 11 and holds all
decoys, so it is exactly the header's "sniffer of its own compiled code objects that also proves the
decoy guard dead". It is disclosed in the counter header (rule 3 bound) and in the plan. Under the
F1+F2 fix simulation it still reads MET (the mirror run kills, the second honest run is CLEAN).

No cheap counter-side fix: the decoy guard is statically recognizable, and any static guard can be
modelled. Options: keep the bound disclosed (current), or randomize the decoy guard's shape per
target (raises the bar, remains analyzable). The honest recommendation is to keep the disclosure and
treat the reviewer source check as the guard for this class.

### F4 (negative results — the counter's guards work as designed)

- g1/g2 (naive recursive / non-recursive code-object sniffers) are UNMET: the code decoy's inline
  mutated statement is visible to a function-level sniffer, so 5 of 11 code decoys fail (t04, t07,
  t08, t09, t10). The decoy guard does its job against non-guard-aware sniffers.
- g4 (disk/`inspect`/`linecache` source sniffer) is UNMET: killed 0 of 11; the source-blind run
  leaves the honest bytes on disk, so the sniffer cannot see any mutant.
- g5 (harness/argv/`/proc/self/cmdline` sniffer) is UNMET: the harness is symmetric, so the honest
  run is REPORTED-FAILURE too and all decoys fail.
- g6 (fake `self-test FAIL:` line + `SystemExit(1)`, no summary) is UNMET: rule 1 classifies it
  RUN-ERROR (no summary line), so it is not a kill; its t04 code decoy also reads RUN-ERROR.

## Fix simulation (scratch copy, not a counter edit)

`counter-fix-sim.py` is a copy of the frozen counter with two proposed v5 rules: `R-honest-final`
(a second honest run at the end, both CLEAN) and `R-mirror` (each target and the positive also run
with the mutant text on disk, both runs must be REPORTED-FAILURE). Readings:

| target | frozen v4 | fix simulation | effect |
|---|---|---|---|
| base `679775a…` | UNMET (0/11) | UNMET (0/11), honest-final CLEAN, mirror 0/11 | no regression |
| g3-recompile-compare | MET | **UNMET** (mirror 0/11) | R-mirror closes it |
| g2b-guard-aware-sniff | MET | **MET** (mirror 11/11, honest-final CLEAN) | disclosed bound remains |
| g7-stateful-fake | MET | **UNMET** (honest-final REPORTED-FAILURE) | R-honest-final closes it |
| g8-clone-marker | MET | **UNMET** (honest-final REPORTED-FAILURE) | R-honest-final closes it |
| r95c1 positive control | MET (pre-data) | **MET** (mirror 3/3, honest-final CLEAN) | the fix does not refuse honest behavioural arms |

## Risks / blockers

- The g7/g8 class is an **undisclosed** counter gap. The counter's predicate alone is necessary but
  not sufficient for "behavioural arms"; the reviewers' source check is the only guard for it and for
  g2b. A landing reading of `C1-PREDICATE-MET` should not be reported as "the arms are behavioural"
  without that review.
- The fix simulation is a scratch copy; it is evidence for a recommendation, not a proposed patch to
  the frozen counter (the counter is frozen; an amendment is an L1 act via
  `plans/round-96-addendum-*.md` before any scored reading).
- No tool installs were needed (`python3` 3.14.8, `git`; stdlib only). No network was used by any
  world or by the counter.
- Scratch is removed at the end of the seat; the patches, counter receipts, fix-sim receipts and this
  report are the retained evidence.

## Receipts in this directory

`<world>.patch` (9), `<world>.counter.txt` (9), `<world>.honest-local.txt` (9),
`base.fixsim.txt`, `g3.fixsim.txt`, `g2b.fixsim.txt`, `g7-stateful-fake.fixsim.txt`,
`g8.fixsim.txt`, `r95c1.fixsim.txt`, `build.log`, and the three scripts used
(`build-g.py`, `make-fix-sim.py`, `counter-fix-sim.py`) for reproducibility.

The world repos under `/fast/scratch/hyaku/kotoba-r96/ExecCounterForgeryR96/worlds/` are scratch and
are removed before this seat yields; each patch is a `git diff --binary` against the freeze commit and
reproduces its world commit with `git apply` on a fresh clone at `679775a…` (checked for all nine).
