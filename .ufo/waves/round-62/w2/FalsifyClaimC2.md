# FalsifyClaimC2 — attack on the round-62 C2 (calibration) claim

Seat: `L1kotoba62.FalsifyClaimC2` (wave 2, falsify). Lane tip at assignment:
`e6da78bbe420722dd18a13182a7c4b64ce02f005`; lane advanced to `306381d` during the
attack (evidence below). All verdicts run on a clean clone at the pinned bytes
(`/tmp/c2clone`), because the live working tree was transiently dirty mid-run
(see §Environment).

Attack surface (from `plans/round-62.md` §C2):
- frozen predicate: `python3 -B verifiers/check_routed_repairs_v2.py --self-test`
  prints `successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6`, exit 0.
- kill rule: a label-only successor fails its own control arm; D/H arms computed
  from input blobs, never asserted; reject-everything fails H1/H2.
- base control: frozen counter at base `f3246d14…` exits 1 with `0 of 6`.

## Verdict: CLAIM HOLDS at both receipt revisions. One kill-arm gap found in the
`de5e3471` instrument (memorized-label lookup passes its committed self-test);
the fleet's own post-data hardening (`604ae4fb`, landed at `306381d`) closes it.

## 1. Frozen predicate line — same sentence in plan, verifier, receipt

Plan `plans/round-62.md:117-119` (committed `45a7ecf`, still identical at tip —
`git diff 45a7ecf 306381d -- plans/round-62.md` shows zero changes to any C2
sentence; the only post-freeze plan commits `5c924b0`/`9228be4` are pre-data E1
errata touching C1 text only):

    successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6

Verifier print template (`verifiers/check_routed_repairs_v2.py` committed blob
`4e45f660`, lines 602–605; the hardened `604ae4fb` file prints the same template):

    f"successor: dishonest rejected {rejected} of 6; honest passed "
    f"{honest_passed} of 2; base {base_display} of 6; tip {tip_display} of 6"

Committed receipt `.ufo/waves/round-62/C2-successor-measure.txt` (at `e6da78b`)
records stdout:

    successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
    exit=0

My re-run on committed bytes (`sha256 de5e3471`, clean clone at `e6da78b`):

    $ python3 -B verifiers/check_routed_repairs_v2.py --self-test   → exit 0,
      last stdout line byte-identical to the plan/receipt sentence.

One sentence, three places, byte-identical. No C2 sentence changed after data.

## 2. Committed-byte identity

    git show e6da78b:verifiers/check_routed_repairs_v2.py | sha256sum
      → de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7  (receipt pin match)
    git show e6da78b:verifiers/check_routed_repairs.py | sha256sum
      → 95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  (receipt pin match)

Blob `4e45f660` (v2) and `56b86f61` (frozen) are identical at `3e7aed9`,
`f9ab081`, `e6da78b`, `3f911504` — no byte drift between receipt run and tip.

## 3. Base control `0 of 6` — re-run by this seat, real

    $ python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
    R-a … missing × 6 (all six)
    routed repairs verified 0 of 6
    exit=1

    $ python3 -B verifiers/check_routed_repairs_v2.py --rev f3246d14…   → 0 of 6, exit=1
    $ python3 -B verifiers/check_routed_repairs.py --rev e6da78b…       → 6 of 6, exit=0
    $ python3 -B verifiers/check_routed_repairs_v2.py --rev 3e7aed9…    → 6 of 6, exit=0
    $ python3 -B verifiers/check_routed_repairs_v2.py --rev e6da78b…    → 6 of 6, exit=0
    $ python3 -B verifiers/check_routed_repairs_v2.py --rev garbage-rev → could-not-evaluate, exit=2

`tip` in the predicate = the self-test's `TIP_REV` constant `45a7ecfa` (the
plan-freeze commit, not the data rev `3e7aed9` — the plan's wording "the round-62
data revision" is loose; all three revs verified 6 of 6, so no claim hazard).

## 4. D/H arms computed from blobs — per-arm re-derivation

Driving `v2.check_repairs` + `frozen.check_repairs` directly on the committed
fixture builders:

    D1: successor=5/6 frozen=6/6  lost=[R-a]   (tree-derived 30 vs declared committed 29)
    D2: successor=5/6 frozen=6/6  lost=[R-a]   (negated claim rejected by affirmed_count)
    D3: successor=5/6 frozen=6/6  lost=[R-c]   (inverted pointer direction)
    D4: successor=5/6 frozen=6/6  lost=[R-d]   (bodyless census; frozen accepts exit=0 alone)
    D5: successor=5/6 frozen=6/6  lost=[R-e]   (Q560/M910 substring ids; exact-row regex misses)
    D6: successor=5/6 frozen=6/6  lost=[R-f]   (non-hash merge-base operands; frozen substring-only)
    H1: successor=6/6 frozen=4/6  frozen misses R-c (split-line pointer) and R-f (exit=0 form)

Every dishonest tree loses exactly its targeted repair — the successor counts
per-arm, and each count is a sum over computed regex/parse results, not a table.

G-a self-derivation re-run: `git ls-tree -r --name-only 45a7ecfa --
.ufo/waves/round-60/build` filtered to the seat basename pattern → **29**; LOG
line at that rev declares `claimed 32`/`committed 29` → `32 > 29`, `committed ==
derived` → R-a ok. The paired-population control (29 pass / 30-stale fail /
30-declared pass, frozen scores 6/6/5) reproduces: a frozen-score remap fails.

## 5. Kill rule — empirical, patched `check_repairs` inside committed `self_test()`

| mutant scorer | exit | evidence |
|---|---|---|
| constant-6 label | **1** | all six D arms fail, G-a arm fails, base CLI 6≠0, "constant-6 evaluator unexpectedly passes the base control", `dishonest rejected 0 of 6` |
| constant-0 reject-all | **1** | H1 0≠6, tip CLI exit 1≠0, `honest passed 0 of 2`, both constant-vs-measured arms flag |
| fingerprint-memorized lookup (11 inputs: 6 D + H1 + 3 population + real base/tip blob maps) | **0** — **PASSES** | prints the honest predicate line |

**Finding F-C2-1 (medium, closed at tip):** the `de5e3471` self-test kills
constants and reject-everything but has no arm probing scorer-vs-input
invariance, so a label scorer keyed on `sha256(sorted fixture blobs)` passes
exit 0. The "computed from the input blobs, never asserted" clause was not
enforced against memorized assertions. Harm bounded: the claim/receipt pin the
honest bytes `de5e3471` (verified — it computes), so the C2 claim itself stands;
the gap is kill coverage, not a false measurement. The fleet found the same
class (`FalsifyC2Shortcuts`/`FalsifyC2RejectAll` named in the new receipt) and
landed `invariance_probe` + `score_with`/`fingerprint` + CLI scorer-dependency
arms in `604ae4fb`: my identical memo mutant re-run under the hardened
self-test now exits **1** (`invariance arm failed … fresh 6/0/0`), and the
hardened self-test on real code still prints the identical predicate line,
exit 0.

## 6. Sentences that changed after data

- The frozen predicate sentence: **unchanged** (plan `45a7ecf`→tip, both
  verifier versions, both receipt versions).
- Changed post-data (all disclosed in the new receipt header): `receipt_rev`
  `3e7aed9`→`3f911504`; `successor=` sha `de5e3471`→`604ae4fb` (instrument grew
  650→801 lines); the receipt gains `CLI scorer-dependency:` and
  `invariance controls:` stderr lines. The `f9ab081` receipt pin remains in
  history; the current receipt is a replacement pin, not an appended one.
- Instrument weakness the plan already knew: v2 carries **no sha pin** on the
  frozen file it imports (contrast C1's fail-closed `5a5adc94` pin); drift is
  caught only behaviorally by the `frozen==6` asserts. Receipt pins `95ade9be`,
  verified.

## 7. Environment incident (evidence integrity)

Mid-run the live lane working tree was uncommitted-dirty (sibling activity):
`verifiers/check_routed_repairs_v2.py` mutated to a self-recursive
`honest_fixture_map` → `python3 -B verifiers/check_routed_repairs_v2.py
--self-test` in the lane crashed `RecursionError`, exit 1 (~21:40Z). Committed
bytes were unaffected; all results above come from `/tmp/c2clone` checkouts.
At tip `306381d` the lane tree is clean and the hardened receipt is committed.

## Residual risk

- TIP_REV/`H2` hard-codes `45a7ecfa`; a future regression past that rev would
  not move the self-test's tip arm (CLI `--rev` remains the fresh check —
  verified 6 of 6 at `e6da78b`).
- Frozen counter has no G-a analogue by design; its base `0 of 6` is honest.
- Report written by seat; no subagents, no installs (pacman paused; none needed).
