# Kb81E06Controls — C1 control worlds W0–W9 (round 81, w1)

Seat: leaf executor. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base: `b284223105f4d106f7e8f56ed4fd296c643cda0e`. Frozen plan: `e6d48e6a9b11da4660df8145bd2f28c3238c5b83`
(`plans/round-81.md`, which declares erratum E6 with `LINE_CAP 40 → 900` and TIGHT pin tuples; the
`140` in the dispatch ticket was the pre-freeze draft and is superseded — see §"Erratum facts").
Nothing in `verifiers/`, `corpus/`, `SKILL.md`, `PROVINCE.md`, `plans/` or `MANIFEST.json` was edited.
All writes are under `.ufo/waves/round-81/`; scratch removed before this report was written.

## What was measured

Final receipt: `.ufo/waves/round-81/build/c1_controls.txt` — **one run, ten worlds, 10 PASS /
0 FAIL / 0 ERROR / 0 SKIPPED**, generated `2026-10-28T00:06:15`, harness
`.ufo/waves/round-81/build/c1_controls.py`.

Counter bytes under test (frozen triple reproduced from the published patch, byte-for-byte with
`.ufo/waves/round-81/receipts/freeze-shas.txt`):

| item | value |
|---|---|
| counter patch | `Kb81E05Erratum.patch` sha256 `c15680f81d2684fc40ef7aeef21143f217ecf4e4fc62b9ea91a7bd5787cfcf4f` |
| counter post-image | blob `eb00200ee6987a2fd95086915a333fe258aa6c82`, sha256 `1753b11c11c6f907be838cb28842e28d01e7935e19d5afb3a6b46afdac51d660`, 751 lines |
| constants | `BASE = 072048fa8e8a52c707d25f7079772fa317244eb7`, `LINE_CAP = 900`, `TOTAL = 6` |
| pins | integrity `("e470eaae…", "bbee51f2…")`, independent `("edac0df7…", "59602942…")` (exactly the two r81 post-images) |
| counter copy used | `.ufo/waves/round-81/build/Kb81E06Controls.counter-amended.py` (identical sha256; the patch was applied in a scratch clone at `b2842231`, never in the lane) |

Repair artifacts fed to the worlds (all as published at run time):

| role | artifact | sha256 |
|---|---|---|
| R1 + manifest | `Kb81E01Integrity.patch` | `6bbb304bea83968ced6c2ba3f33afa26b7d4256334303ea99a32279079495fe7` |
| R2 | `Kb81E02Independent.patch` | `d8bf88c8ef5daf99ddf861ab2a5aeaa1193a57a90200e1d314134750e2e7f9d1` |
| index + baseline (repairs 3/4) | `Kb81E04Baseline.patch` | `7b5781caa6fb533a0f2601f97b65f6ffa46e020acda9abe934d137d0b76bf733` |
| baseline refresh | `refresh-corpus-baseline.py` | `8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a` |

Measured instrument arithmetic of the stack (scratch clone, `git diff --numstat
072048fa… HEAD -- <the six BATTERY scripts>`): `22/3` floors, `210/10` integrity, `170/16`
independent = **+402 / −29 added/deleted ≤ 900**. The frozen plan narrates `+203/-10` and
`+247/-18` (measured on pre-final patch bytes); the final published blobs are `210/10` and
`170/16`. Both readings are under the frozen 900, so the size-bound kill condition does not fire.

## Method (and why the worlds are built this way)

`c1_controls.py` ports the r80 `c2_controls.py` construction: each world is its own
`git init -q` repository at `<work>/<world>/fleet/kotoba-shokunin`, identity `scratch-r81`, every
git call `-C`'d, `git -C <repo> rev-parse --show-toplevel` asserted equal to the repo before any
mutation. `.git/objects/info/alternates` points at a read-only base clone at `b2842231`, so the
counter's pinned `BASE` resolves without copying the object store. The base tree is materialised with
`read-tree` + `checkout-index -a`; published patches are applied with `git -C <repo> apply`; the
world's fixture is written; one or two commits are created with `commit-tree -p <base-rev>` and
`update-ref`. The measured command is

    python3 -B <counter> --repo <world-repo> --rev <commit> --fleet <world>/fleet

run with the world's own `TMPDIR`. The fleet directory holds the repo plus read-only symlinks to the
real fleet's other entries, so report-pointer paths resolve as in the lane. For the baseline-bearing
worlds `refresh-corpus-baseline.py --repo <repo>` runs at the committed HEAD and, when it writes,
a second commit is the measured rev (a refused refresh is recorded in the receipt).

Harness defects found and fixed **before** the verdict run (each is visible in the two retained smoke
receipts, which are base-counter *harness validation only* and are superseded):

1. `Kb81E06Controls-smoke.txt` (base counter): W5 failed because the fixture edited
   `corpus/lessons/round-76-verifier-spotcheck.md`, which is *added after* the counter's pinned r73
   base and therefore INFO by design; the fixture now edits `round-72` (a base file).
2. `Kb81E06Controls-smoke2.txt` (base counter): the probe reader kept only count scalars, so detail
   lists were lost; `TMPDIR` was not created before the refresh (refresh exit 1).
3. Marker mirror walked `.ufo`'s contents with the `.ufo` component still in the path, so no marker
   was ever written.
4. W9 assumed the manifest was a list; the published manifest is `{"note":…, "commits":[…]}`.
5. W8's first construction cited a bare `.ufo/reports/…` token. The corpus gates resolve a bare
   report path against their hard-coded `FLEET_ROOT` (`/home/vgpnk/Projects/shokunin`), so a
   counter `--fleet` override cannot redirect it: no marker was reachable and that world read
   `6 of 6` (a synthetic stack, not a claim measurement — this seat does not score after-values).
   The world now cites the marked report through the lane's own relative symlink
   (`../../.ufo/reports/round-76/kotoba.md` from `corpus/lessons/round-79.md`), which is the r80 W10
   shape and the only route into the measured tree.

The published `build/c1_controls.py` is the verdict harness plus two post-verdict additions — the
supplementary `W6b` world and a case-insensitive `--only` lookup — neither of which touches a
`W0–W9` fixture, check or runner path. The verdict receipt was produced by the same file minus those
additions; its header names the counter and patch shas, so the run is reproducible from the published
artifacts (pass `--only W0,W1,W2,W3,W4,W5,W6,W7,W8,W9` to select exactly the plan's set, or omit it to
run `W6b` as an eleventh, supplementary world).

## Results — every world against the frozen counter

Exact frozen line per world (the counter's own last line), exit status, and the pre-registered
expectation. `guards 5 of 5` means every guard held; the fleet-root prefix is the world's own fleet.

| W | world | frozen line | exit | expected | verdict |
|---|---|---|---|---|---|
| W0 | empty commit on the base tree | `guards 5 of 5; tip battery exit 0: 4 of 6` | 1 | 4 of 6, exit 1 | **PASS** |
| W1 | index+baseline repairs only | `guards 5 of 5; tip battery exit 0: 4 of 6` | 1 | still red on report_dead / commit_unresolvable | **PASS** |
| W2 | R1 artifact only | `guards 5 of 5; tip battery exit 0: 4 of 6` | 1 | ≤5 of 6 | **PASS** |
| W3 | R2 artifact only | `guards 5 of 5; tip battery exit 0: 4 of 6` | 1 | ≤5 of 6 | **PASS** |
| W4 | both failing instruments stubbed `sys.exit(0)` | `guards 3 of 5; tip battery exit 0: 4 of 6` | 1 | instrument-pin / instrument-size FAIL | **PASS** |
| W5 | base spot-check edited (round-72) | `guards 4 of 5; tip battery exit 0: 4 of 6` | 1 | spotcheck-identity FAIL | **PASS** |
| W6 | isolated-clone commit masked `owner/repo@<sha>`, no manifest row | `guards 5 of 5; tip battery exit 0: 4 of 6` | 1 | red in a zero class | **PASS** |
| W7 | absent lane commit as bare hex in a lane-URL row | `guards 5 of 5; tip battery exit 0: 4 of 6` | 1 | commit_unresolvable red | **PASS** |
| W8 | seven-byte `marker` at the fleet report the lane symlink resolves to | `guards 5 of 5; tip battery exit 0: 4 of 6` | 1 | report_dead red | **PASS** |
| W9 | manifest row whose evidence receipt does not exist | `guards 5 of 5; tip battery exit 0: 4 of 6` | 1 | commit_unresolvable red | **PASS** |

No world reached the claim target; no world went green; therefore no counter defect was found by
these controls. Supporting detail (from each gate's own `--json --no-baseline` observation at the
world repo, recorded in the receipt):

- **W1** — integrity `report_dead=1` (the base rev-object token), `commit_unresolvable=2`,
  `commit_nonhash=0`; independent `commit_unresolvable=2`, `report_dead=0`. Both corpus gates exit 1.
  The world's baseline refresh **refused** (`zero-mode corpus.pointers.report_dead observed 1, not 0
  … a baseline never records a zero-mode value`, exit 2): an index/baseline repair provably cannot
  launder a zero class. This is the load-bearing property W1 was built to test.
- **W2** — the published E01 artifact contains **both** repairs for the integrity gate (pointer
  identity *and* the committed-manifest binding; the patch adds `verifiers/external-commits.json`).
  Measured: integrity `report_dead=0, commit_unresolvable=0, commit_external=2` (green), independent
  unpatched `commit_unresolvable=2` (red) → still 4 of 6. The plan's `commit_unresolvable` class
  assertion for W2 was withdrawn before the verdict run in favour of the plan's own `≤5 of 6`
  criterion, because a gate-pure R1 world cannot be built from the reviewed artifact; the gate split
  is reported, not hidden.
- **W3** — independent patched, no manifest file in the tree: `commit_unresolvable=2` stays red;
  integrity unpatched `report_dead=1` red → 4 of 6.
- **W4** — `instruments lose 2626 lines > 900` and both patched instruments carry the stub blob
  `e15e0b45…`, not a pin; the battery itself reads 4 of 6 and the counter exits 1. The anti-laundering
  load sits on the pin/size guards exactly as E6 claims.
- **W5** — `corpus/lessons/round-72-verifier-spotcheck.md differs from the base blob 8c49e01f8234`.
- **W6** — both gates: `commit_nonhash=1`, detail `corpus/SOURCES.md:431:
  kotoba-shokunin/kotoba-shokunin@<sha>`, `commit_unresolvable=0`, `commit_external=2` (only the two
  manifest-bound S230/S231 sites). **Class note:** the plan's W6 letter expects
  `commit_unresolvable`; the r80-literal shape (marker *inside* the backticked token) is not a
  hex token, so both r81 gates place it in `commit_nonhash`, also a zero class (`CHECKS` in both
  gates). The token is therefore not silently exempted, but it is also not resolved as a commit.
- **W7** — `commit_unresolvable=1` in **both** gates with the lane GitHub URL in the same row; the
  r80 W9 bypass (URL reads as external) is closed.
- **W8** — marker verified as 7 bytes at `<world>/fleet/.ufo/reports/round-76/kotoba.md`, and the
  cited path `../../.ufo/reports/round-76/kotoba.md` resolves exactly there; both gates report
  `report_dead=1` with detail `corpus/lessons/round-79.md:27: ../../.ufo/reports/round-76/kotoba.md`
  (the r80 W10 bypass is closed; the neighbouring `HEAD:.ufo/reports/round-77/kotoba.md` object still
  resolves and is not flagged).
- **W9** — manifest row `{hash, repo: example/example, evidence:
  .ufo/waves/round-81/snapshots/DOES-NOT-EXIST.json}` is dropped (`_committed_blob` → None) and the
  cited bare hash stays `commit_unresolvable=1` in both gates: a manifest row alone never exempts.

Supplementary world (not part of the plan's W0–W9 list), `.ufo/waves/round-81/build/c1_controls.W6b.txt`,
pre-registered before it ran: `guards 5 of 5; tip battery exit 0: 4 of 6`, exit 1,
`commit_unresolvable=1` in both gates for the Q75 canonical shape — the same isolated-clone commit
cited as a **bare hex token** with `kotoba-shokunin/kotoba-shokunin@` elsewhere in the row
(detail `corpus/SOURCES.md:431: c5a67e0b…`). This is the shape the E02 self-test pre-registers, and it
stays red, so the r80 W8 threat is closed for commit candidates as well as for marker-in-token rows.

## Erratum facts this seat measured

- The committed plan's E6 (`plans/round-81.md:15,26`, rev `e6d48e6`) declares `LINE_CAP = 900` and
  TIGHT tuples `(base blob, reviewed r81 blob)`. The dispatch ticket's `140` is the superseded
  pre-freeze text; my first blocker message to the L1 used that draft and is withdrawn — with 900 the
  measured `+402/−29` is inside the bound.
- Both gates' base blobs are identical at `072048fa` and `b2842231`
  (`e470eaae…` integrity, `edac0df7…` independent), so the frozen tuple wording is satisfied.
- Pin freshness: E02 was revised during the wave (post-image `7b37461a…` → `59602942…`). The counter
  I measured pins `59602942…` and was reproduced from the patch whose sha is in
  `receipts/freeze-shas.txt`; a stale-pin reading does not affect any world above.

## Residual risks / observations (no counter defect claimed)

1. **`--fleet` is not a resolution boundary.** `verify_corpus_integrity.py` and
   `verify_corpus_independent.py` hard-code `FLEET_ROOT = /home/vgpnk/Projects/shokunin`; the counter's
   `--fleet` only shapes the sandbox's sibling links. Report/commit resolution therefore ignores the
   counter's fleet argument. The claim's predicate runs in the lane, where that constant is correct;
   but any future "run the battery against a fake fleet" control must route through an in-tree relative
   token (as W8 does).
2. **W6's class mapping.** A non-hex token with a `owner/repo@` prefix is `commit_nonhash` (zero), not
   `commit_unresolvable`; the frozen plan's W6 wording names the latter. Both are zero classes and the
   world stays red, but a reader of the raw gate JSON will see a different class.
3. **Spot-check guard reach.** `spotcheck-identity` is anchored at `072048fa`, so the round-73…80
   spot-check lessons at the r81 base are INFO (added after the base), not pinned: they can be edited
   at the tip without the guard noticing. W5 only trips on rounds ≤72. This is the frozen counter's
   documented design, not a repair scope, but it is a real calibration gap for recent closures.
4. Worlds are synthetic stacks built from patches + a baseline refresh; they are not the landed tip.
   The repaired stack's own reach of the target is **not** scored here.

## Reproduction

```
S=/fast/scratch/hyaku/kotoba-r81/Kb81E06Controls; mkdir -p "$S/tmp"; export TMPDIR=$S/tmp
git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin "$S/base"
git -C "$S/base" checkout -q b284223105f4d106f7e8f56ed4fd296c643cda0e
# materialise the frozen counter (never in the lane):
git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin "$S/cbase"
git -C "$S/cbase" checkout -q b284223105f4d106f7e8f56ed4fd296c643cda0e
git -C "$S/cbase" apply .ufo/waves/round-81/build/Kb81E05Erratum.patch
cp "$S/cbase/verifiers/check_tip_battery.py" .ufo/waves/round-81/build/Kb81E06Controls.counter-amended.py
python3 -B .ufo/waves/round-81/build/c1_controls.py \
    --counter .ufo/waves/round-81/build/Kb81E06Controls.counter-amended.py \
    --base-tree "$S/base" --base-rev b284223105f4d106f7e8f56ed4fd296c643cda0e \
    --r1 .ufo/waves/round-81/build/Kb81E01Integrity.patch \
    --r2 .ufo/waves/round-81/build/Kb81E02Independent.patch \
    --baseline .ufo/waves/round-81/build/Kb81E04Baseline.patch \
    --refresh .ufo/waves/round-81/build/refresh-corpus-baseline.py \
    --work "$S/full" --jobs 3 --only W0,W1,W2,W3,W4,W5,W6,W7,W8,W9 \
    --out .ufo/waves/round-81/build/c1_controls.txt
# exit 0 = every world matched its pre-registration; 1 = divergence (a green control is a COUNTER DEFECT)
```

Operability: `--list` prints the pre-registration table; `--only W0,W4`; `--json` emits the machine
summary; `--keep` retains the world repos; a patch that does not apply is exit 2, never a silent skip.
Tooling: nothing installed or upgraded this seat (pacman paused host-wide; no other channel needed).
Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81E06Controls/` removed after the receipts were copied into
the build dir.

VERDICT: C1 controls hold on the frozen counter (10/10 worlds match their pre-registration, no world reaches 6 of 6, no counter defect); residual calibration risks are the hard-coded fleet root, W6's nonhash class mapping, and spot-check pins anchored at the r73 base.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E06Controls.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/c1_controls.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/c1_controls.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/c1_controls.W6b.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E06Controls.counter-amended.py; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E06Controls-smoke.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E06Controls-smoke2.txt
