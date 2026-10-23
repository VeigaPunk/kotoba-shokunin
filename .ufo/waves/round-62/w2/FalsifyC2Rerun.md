# FalsifyC2Rerun — C2 routed-repairs successor re-run at committed bytes

Seat: `L1kotoba62.FalsifyC2Rerun` (wave 2, falsify). Scope: re-run every C2
counting command on committed bytes, verify the receipt's `successor sha256`
names the bytes executed, report every divergence. Lane tip at run time:
`e6da78bbe420722dd18a13182a7c4b64ce02f005`. Run timestamp: `date -u` →
`2026-10-23T21:35:11Z`. All commands run `cwd=/home/vgpnk/Projects/shokunin/kotoba-shokunin`.

## Verdict: no divergence — every receipt line reproduced byte-exact

## Identity of the bytes run

`sha256sum` (working tree, committed, and at the receipt/data revs — all identical):

| path | expected (receipt) | observed | where |
|---|---|---|---|
| `verifiers/check_routed_repairs_v2.py` | `de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7` | `de5e3471…7b7` | worktree; `git show e6da78bb:…`; `git show 3e7aed9b:…`; `git show f9ab081:…` |
| `verifiers/check_routed_repairs.py` (frozen) | `95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88` | `95ade9be…88` | worktree; `git show e6da78bb:…` |

The file at lane tip is byte-identical to the file at the receipt rev and at the
wave-1 data rev, so every re-run below executes the receipted successor.

## Command re-runs vs `.ufo/waves/round-62/C2-successor-measure.txt`

| command | receipt block (lines) | my output | diff | exit |
|---|---|---|---|---|
| `python3 -B verifiers/check_routed_repairs_v2.py --self-test` | 8–28 | identical (`diff -u` empty) | none | `exit=0` |
| `python3 -B verifiers/check_routed_repairs_v2.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326` | 32–38 | identical | none | `exit=1` |
| `python3 -B verifiers/check_routed_repairs_v2.py --rev 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85` | 42–48 | identical | none | `exit=0` |
| `python3 -B verifiers/check_routed_repairs_v2.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005` | (lane tip; receipt measured `3e7aed9b`) | identical to the `3e7aed9b` block: 6 × `ok`, `routed repairs verified 6 of 6` | none | `exit=0` |
| `python3 -B verifiers/check_routed_repairs.py --rev f3246d14…` (frozen, receipt lines 52–58) | 52–58 | identical incl. label `R-d census-after file: missing` | none | `exit=1` |
| `python3 -B verifiers/check_routed_repairs_v2.py --rev routed-repairs-v2-no-such-revision` | self-test claims `exit 2` | `routed repairs verified could-not-evaluate: unreadable rev` | none | `exit=2` |

## Independent spot-checks of the measured quantities

- `git merge-base --is-ancestor` confirms `f3246d14`, `45a7ecfa`, `3e7aed9b`
  are all ancestors of lane tip `e6da78bb`.
- `git ls-tree -r --name-only e6da78bb -- .ufo/waves/round-60/build | grep -cE
  '^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$'`
  → **29**; LOG.md at tip carries the R-a line "claimed 32 … committed 29"
  (`git show e6da78bb:LOG.md`, round-61 §R-a erratum). 32 > 29: R-a legitimately ok.
- `check_repairs` reads only committed bytes: `git rev-parse --verify <rev>^{commit}`,
  `git ls-tree`, `git show <rev>:<path>` per `INPUT_PATHS` (LOG.md, QUALITY.md,
  lessons/round-61.md, census-after.txt, controls-ancestry.txt). No working-tree
  reads on the `--rev` path; the dirty worktree (`M` on two w1 scribe reports,
  sibling `FalsifyS118.md`) cannot affect the measurement.
- Frozen counter not modified: tip bytes `95ade9be…` equal receipt; self-test
  line `frozen counter before: D1..D6 6 of 6; H1 4 of 6; H2 tip 6 of 6` reproduced.
- `-B` honored: pre-existing ignored `verifiers/__pycache__/` (mtime 17:09) lacks
  a `check_routed_repairs_v2` entry; no new bytecode written by my runs.

## Observations (not divergences)

1. Receipt's `receipt_rev=3e7aed9b` is not lane tip — two commits landed after it
   (`f9ab081` receipts, `e6da78bb` corpus/registry/v3.1). Re-run at tip
   reproduces `6 of 6` exit 0, so the claim survives the intervening commits.
2. The self-test's internal tip arm is `TIP_REV=45a7ecfa` — the round-62 **plan**
   commit, not the data commit. Plan §C2 calls it "the round-62 data revision";
   it is strictly an ancestor of the data commits (and the measured INPUT_PATHS
   blobs are round-61 artifacts unchanged since), so the arm still measures real
   committed bytes and both ancestor and current tip score `6 of 6`. Loose
   naming, not a measurement error.
3. Receipt's `$ date -u` line (`2026-10-23T21:21:15Z`) is 14 min before my run;
   expected.

## Verdict

C2's calibration claim — `successor: dishonest rejected 6 of 6; honest passed
2 of 2; base 0 of 6; tip 6 of 6` plus the frozen-predicate CLI outputs and exits
— reproduces byte-exact at committed bytes at base, receipt rev, and lane tip.
`successor sha256` names exactly the bytes executed. Falsification attempt:
**failed to falsify**; claim stands.

No tools installed this run (python3/git/sha256sum/diff all present; pacman paused).
