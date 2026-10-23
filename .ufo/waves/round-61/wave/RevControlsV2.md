# RevControlsV2 — re-score of the r60 control world set against the committed v2 counter
Addendum (19:20 UTC): the seven v1-counter runs were also re-run **without** `--fetch`.
Each prints `<same S>; live not run` and exits 1 with empty stderr, matching the
`live not run` lines quoted in the v1 seat receipts (e.g. `v1-noreaderprobe` →
`1 of 4; live not run`, as recorded in `controls/CtlNoReader.md`). Total runs: 64,
64 reproduced, 0 divergent.


**Seat:** `kotoba-r61-wave-RevControlsV2` (reviewer; L1 `agent://KotobaR61`).
**Scope:** re-run the six v1 control worlds and the CtlRescoreV2 v2 re-score set under the
committed v2 counter; verify every recorded receipt reproduces (same summary line, same exit).
Read-only lane and fleet; all writes confined to `/fast/scratch/hyaku/kotoba-r61/RevControlsV2/`
plus this report.
**Runs taken:** 2026-10-23, 19:15–19:17 UTC (about 7 h after the r60 control runs of ~12:05–12:25Z).

## Verdict

**NO HIGH FINDING.** Every committed receipt in scope reproduces exactly:

- **50 of 50** v2-counter runs whose stdout/stderr are committed as files in the
  CtlRescoreV2 sandbox receipt commit `db75afb07519a185f68d77a6c3a862d7f8770e3f`
  (`receipt/ctl-rescore-v2`, path `.ufo/waves/round-60/controls-v2/receipts/`)
  are **byte-identical** to my re-runs — same summary line, same `counter sha256` line,
  same reject lines, empty stderr, same exit code. This includes all `--fetch` runs:
  the live pages gave identical verdicts 7 h later.
- **All 7** v1-counter delta runs byte-identical to the committed `v1-*.stdout`
  receipt files; v1 self-test passes (302 assertions), v2 self-test passes (318 assertions).
- **All 11** replay-vs-direct pairs identical modulo the `rev` field, matching §5's claim.
- **All 6** world tree ids match the receipt's cross-clone identity table.
- The r61 C2 base control `.ufo/waves/round-61/controls/C2-base.txt` reproduces
  byte-exactly at base `f3246d14` (0 of 6, exit 1).
- `verifiers/check_scoped_rules.py` in the lane is still the frozen v2 file
  (sha256 `ca2585a4…` at v2 freeze `b1cd64bb`, at r61 base `f3246d14`, and at
  current tip `c630c4cb`); the committed counter has not drifted.

## Findings by severity

### HIGH — none

### MEDIUM — none

### LOW

- **L1 (informational, ground fragility): the r60 control worlds are committed only in
  scratch sandboxes, never in the lane.** The 14 measured revisions under
  `/fast/scratch/hyaku/kotoba-r60/<Seat>/` are not objects reachable from any lane ref
  (verified: fetched from sandbox paths, absent from lane refs). The plan already
  requires the seven frozen worlds to be "rebuilt as a committed fixture" this round —
  this is the load-bearing step. If scratch is reaped before integration commits the
  fixtures, the r60 ground cited by C1 becomes unverifiable from lane objects alone.
  This is a property of the r60 design (worlds lived in sandboxes by design), not a
  defect in the receipts; it amplifies the importance of this round's fixture commits.

### Notes (verified, not findings)

- `CtlWrongKey` and `CtlInventedAction` have no world and no receipt — cancelled at the
  r60 settle deadline. Re-verified: their sandboxes still sit at `49c3e87d` (v1 freeze,
  `git rev-parse HEAD` on each) with only untracked files. Nothing to reproduce; the gap
  stays disclosed exactly as recorded.
- `lane_dir()` resolution held for every run: the counter copy placed at the clone root
  resolves to the clone (probe: `--rev 000…0` →
  `could-not-evaluate: revision … is not a commit in /fast/scratch/hyaku/kotoba-r61/RevControlsV2/lane`,
  exit 2 — matching the r60 seat's mechanism).
- Replay parents and probe ancestry verified: `4d0463de`'s parent is the v2 freeze
  `b1cd64bb`; probe `43513eea`'s parent is the world `eabe93f6`; world `f4dcfd99`'s
  parent is the v1 freeze `49c3e87d`.
- The §5 "byte-identical mod rev" claim verified independently: each of the 11
  direct/replay stdout pairs hashes the same after `sed 's/rev [0-9a-f]\{40\}/rev R/'`.
- **Zero divergence in live-fetch verdicts.** `fabsnap-pristine`, `fabsnap-restored`,
  `noreader-probe` still found the one live row (VS Code); `allfalse-world` still got
  HTTP 404 on all 7 fabricated URLs; `fabsnap-fabricated` still failed the live quote
  check. The receipt's own live-drift disclaimer (§11) stands but did not materialize.
- `CtlReopenForged`/`CtlReopenHeldKey` worlds (W1–W4, incl. the two MET receipts) are
  **not in my scope** — my item was "the six v1 worlds and the v2 re-scores"
  (= CtlRescoreV2's table). Their reproduction is the neighbouring reviewer seats' item;
  listed here so the gap is owned somewhere.
- The lane tip moved past base (`c630c4cb` > `f3246d14` at 19:13 UTC); the counter file
  and `check_routed_repairs.py` at tip are byte-identical to the freeze
  (sha256 `ca2585a4…` / `61d8c583…`).

## Exact commands and outputs

Environment: `git clone --no-local` of the lane into scratch, then
`git fetch` of every ref from the r60 seat sandboxes
(`/fast/scratch/hyaku/kotoba-r60/{CtlRescoreV2,CtlNoReader/probe,CtlJunk,CtlFabSnapshot,CtlLabelShortcut,CtlAllFalse,CtlDoNothing}`)
plus five unreferenced replay commits and the detached-HEAD probe commit fetched by SHA
(`git fetch <path> <sha>` — `uploadpack.allowAnySHA1InWant` accepted SHA wants on local
path fetches). All 14 measured revisions + 11 replays present as commits in my clone
(`git cat-file -t` → `commit`, each).

Counter files extracted, sha-verified:

```
$ git show 49c3e87d4fb5677783c55f8225c9e4f892273879:verifiers/check_scoped_rules.py > v1.py
$ git show b1cd64bb45eee744c4ec93be8631f1eddb28fddd:verifiers/check_scoped_rules.py > v2.py
$ sha256sum v1.py v2.py
6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440  v1.py   (matches v1 receipt)
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  v2.py   (matches v2 receipt)
$ git show f3246d1493b60ea1c0d947a19c39f9e08e92f326:verifiers/check_scoped_rules.py | sha256sum
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  (r61 base still v2)
```

Run shape (per the receipt's own command form; script at clone root so `lane_dir()`
resolves to the clone):

```
cd /fast/scratch/hyaku/kotoba-r61/RevControlsV2/lane
timeout 900 python3 -B ./v2.py --rev <world> --fetch   # or without --fetch
```

### Direct worlds under v2 — results (2026-10-23 19:15 UTC; every run exit 1, stderr 0 bytes)

| world | rev | summary line (first line, fetch run) | exit | receipt match |
|---|---|---|---|---|
| donothing-world | `f4dcfd99` | `backed 0 of 0; found on the live page 0 of 0` | 1 | byte-identical |
| donothing-freeze | `49c3e87d` | `0 of 0; … 0 of 0` | 1 | byte-identical |
| donothing-base | `31092dc6` | `0 of 0; … 0 of 0` | 1 | byte-identical |
| junk-world | `de808c7b` | `0 of 7; … 0 of 7` | 1 | byte-identical |
| junk-restored | `127c6043` | `0 of 0; … 0 of 0` | 1 | byte-identical |
| allfalse-world | `101c2140` | `7 of 7; … 0 of 7` | 1 | byte-identical (all 7 rows still live 404) |
| noreader-world | `eabe93f6` | `0 of 4; … 0 of 4` | 1 | byte-identical |
| noreader-probe | `43513eea` | `1 of 4; … 1 of 4` | 1 | byte-identical |
| fabsnap-pristine | `a2893fa2` | `1 of 4; … 1 of 4` | 1 | byte-identical |
| fabsnap-fabricated | `8933ce9e` | `1 of 4; … 0 of 4` | 1 | byte-identical |
| fabsnap-restored | `b713e5b1` | `1 of 4; … 1 of 4` | 1 | byte-identical |
| labelshort-world | `415c7672` | `0 of 2; … 0 of 2` | 1 | byte-identical |
| labelshort-restored | `18afea67` | `0 of 0; … 0 of 0` | 1 | byte-identical |
| v2freeze | `b1cd64bb` | `0 of 0; … 0 of 0` | 1 | byte-identical |

Every `nofetch` twin: `… ; live not run`, exit 1, byte-identical to receipt.
Full stdout of each run reproduced the committed files under `receipts/` —
verified by `cmp` per file: `byte-same=50, differ=0` (the 7 `v1-*` files needed a name
map; after mapping they too are byte-same).

### Replays under v2 — all exit 1, masked stdout identical to direct

`replay-{donothing,junk,allfalse,noreader,fabsnap,labelshort}-{world,restored/probe/pristine/fabricated}`
(11 commits listed in §5 of the receipt): every `.fetch`/`.nofetch` stdout
byte-identical to its committed `replay-*.stdout`; and each pair identical to the direct
run after masking `rev ` (recorded claim §5, re-derived):

```
IDENTICAL(masked) donothing-world <-> replay-donothing-world
IDENTICAL(masked) junk-world <-> replay-junk-world        … (all 11 pairs identical)
```

### v1 counter delta runs — byte-identical to `v1-*.stdout` receipts

```
v1-donothing     backed 0 of 0; found 0 of 0   exit 1   BYTE-SAME
v1-junk          0 of 7; 0 of 7                exit 1   BYTE-SAME
v1-allfalse      7 of 7; 0 of 7                exit 1   BYTE-SAME
v1-noreader      0 of 4; 0 of 4                exit 1   BYTE-SAME
v1-noreaderprobe 1 of 4; 1 of 4                exit 1   BYTE-SAME
v1-fabsnap       1 of 4; 0 of 4                exit 1   BYTE-SAME
v1-labelshort    0 of 2; 0 of 2                exit 1   BYTE-SAME
```

Headline S/F of the v1 `controls/SUMMARY.md` table (0/0, 0/7, 7/7, 0/4, 1/4, 0/2 — all
exit 1) reproduced; the same summary strings appear quoted in each v1 seat receipt.

### Self-tests

```
$ timeout 300 python3 -B ./v2.py --self-test        # 19:16 UTC
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
self-test: 0 failure(s) over 318 assertions            exit=0
$ timeout 300 python3 -B ./v1.py --self-test
counter sha256 6aea3be07b769bc83724fe814493e6b2ab8baa4482f8ff58c776ab7e0d0ef440
self-test: 0 failure(s) over 302 assertions            exit=0
```

### C2 base control (round-61 committed receipt)

```
$ date -u → Fri 23 Oct 2026 07:16:35 PM UTC
$ python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
```

`diff` against `.ufo/waves/round-61/controls/C2-base.txt` (whose trailer line is
`base-exit=1`): **empty** — reproduced exactly. (`git show HEAD:verifiers/check_routed_repairs.py`
sha256 `61d8c583…` equals the working-copy file.)

## Isolation

- Lane and fleet read-only throughout. My clone was built with `git clone --no-local`
  and `git fetch` (read ops on lane `.git`); no `git status`/`git checkout`/`jj` was run
  against the lane. All object writes landed in
  `/fast/scratch/hyaku/kotoba-r61/RevControlsV2/lane/.git`. The only lane file this seat
  wrote is this report.
- Seat-sandbox commits are content-addressed evidence: every world/replay sha
  hash-verifies as a commit object whose tree matches the receipt's recorded tree ids
  (`a15846da…`, `4f5c3555…`, `fc716ed2…`, `5e42d8fc…`, `468f4336…`, `008a97cb…`).

## Residual risk / verification gaps

- Live-page drift remains possible tomorrow; zero drift observed today (7 h delta).
- The two MET provenance-forgery worlds (W1 forged-d, W2 held-key-b) and their siblings
  were not re-run here (out of scope; sibling seats cover).
- The v1 seat receipts' *prose claims beyond the summary/stdout* (e.g., sandbox-command
  transcripts) were checked only where quoted lines coincide with my outputs — full
  prose audit was not my item.

## Installs

No installs (pacman paused host-wide per operator ruling; git/python3/curl all present).

## Blockers

None.

## One line

Re-scored all 14 r60 control revisions + 11 replays under frozen v2 (50/50 committed
receipt files byte-identical, all exits 1, all summary lines reproduced), v1 delta runs
byte-identical, C2 base control byte-exact — zero divergence, no HIGH finding.
