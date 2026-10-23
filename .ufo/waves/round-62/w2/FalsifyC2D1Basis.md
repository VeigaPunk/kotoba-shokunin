# FalsifyC2D1Basis — attack on D1/G-a count basis (wave 2)

Seat: `L1kotoba62.FalsifyC2D1Basis` (falsify). Date: 2026-10-23.
Pinned landed bytes: lane tip `e6da78bbe420722dd18a13182a7c4b64ce02f005`;
`verifiers/check_routed_repairs_v2.py` sha256 `de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7` (verified on committed bytes in a `/tmp` clone — see "Mid-run lane mutation" below).

## Verdict

**NO DEFECT in the D1/G-a count basis.** The frozen census command prints **29**
at base, r60 close, and tip; the committed LOG line claims `committed 29` —
honest. The D1 fixture tree adds a real regex-matching report name to reach 30
while its LOG line still claims 29, and the successor rejects it for exactly the
right arm (R-a). The paired population control's numbers are computed from input
blobs, not printed constants — verified by independent re-computation and by
perturbations outside the self-test's own inputs.

## 1. Frozen census command, re-run on committed bytes

Frozen basis (v2 lines 33–35, 84–102, 128–135): `git ls-tree -r --name-only
<rev> -- .ufo/waves/round-60/build`, then `COUNT_PATTERN =
^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$`
fullmatched against the **basename** (`PurePosixPath(path).name`).

| rev | role | `ls-tree -r` total | regex-matching names |
|---|---|---|---|
| `f3246d1493b60ea1c0d947a19c39f9e08e92f326` | BASE_REV (r60 spot-check) | 33 | **29** |
| `79cf263800552812ce6a45f4bb0313668b576749` | r60 close (attempt 2) | 33 | **29** |
| `45a7ecfac9e203297f3146c45d63f5e79367470c` | pinned TIP_REV (r62 plan freeze) | 33 | **29** |
| `e6da78bbe420722dd18a13182a7c4b64ce02f005` | assigned lane tip | 33 | **29** |

Commands (run in lane, read-only):
`git ls-tree -r --name-only <rev> -- .ufo/waves/round-60/build | wc -l` → 33;
`... | sed 's|.*/||' | grep -cE '^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$'` → 29 at every rev above.
`diff` of the base-vs-tip name sets: **IDENTICAL**.

Non-matching entries (all four revs): `ExecIndexCorpus.patch`,
`check_word_counts.fixture.md`, `check_word_counts.py` (mode 100755, the only
non-100644 entry — still a regular blob), `swarm-registry.json`. No trees, no
gitlinks, no nested dirs, no symlinks in the subtree.

**The line claims 29:** `git show e6da78b:LOG.md` line 2540 —
`claimed "32 reports, 0 dead" ... committed count is \`committed 29\` ...
(claimed 32; ...)` — sits inside the Round-61 section. R-a at tip: `claimed
32 > derived 29`, `committed 29 == derived 29` → `ok`. Claimed count exceeds
derived (32 > 29), satisfying the frozen predicate's "must exceed" clause.

## 2. D1 fixture tree adds an actual matching name to reach 30

`verifiers/check_routed_repairs_v2.py:379-380` (pinned bytes):
`d1 = make_fixture_blob_map(30)` then `d1["LOG.md"] = common["LOG.md"]`.
`make_fixture_blob_map(30)` emits `.ufo/waves/round-60/build/ExecSynthetic01.md`
…`ExecSynthetic30.md` — every basename `ExecSyntheticNN.md` fullmatches
`Exec[A-Za-z0-9]+\.md`. The added 30th name is `ExecSynthetic30.md`, a real
regex match (independently confirmed: `COUNT_PATTERN.fullmatch("ExecSynthetic30.md")` → True).

Measured in-process (pinned bytes, `/tmp/r62d1lane` clone):
- `len(fixture_tree_names(d1))` = 35; `committed_report_count` = **30**.
- `d1["LOG.md"]` contains `committed 29` → declared ≠ derived.
- `check_repairs(d1, names)` → **5** with `R-a count correction: missing`,
  other five arms `ok`. `frozen.check_repairs(d1)` → **6** (the frozen R-a is
  three literal substrings, `claimed 32`/`committed 29`/path — it never derives;
  that is the calibration gap the successor exists to close, not a defect here).

Note: `d1["LOG.md"] = common["LOG.md"]` is redundant — `make_fixture_blob_map`
already installs `HONEST_LOG` — but harmless; D1's staleness lives entirely in
the tree, exactly the shape the plan's `(D1) a stale count (tree-derived 30,
line says 29)` describes.

## 3. Paired population control re-run — computed, not printed

`python3 -B verifiers/check_routed_repairs_v2.py --self-test` on the pinned
bytes (sha `de5e3471…`, in `/tmp/r62d1lane` at `e6da78b`), exit 0, stderr:

```
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=5; 30 names/committed 30=6; frozen=6/6/5
```

Independent re-computation (not the self-test's own assertions):

| input | derived | successor | frozen |
|---|---|---|---|
| pop29 (29 names, `committed 29`) | 29 | **6** | 6 |
| pop30 stale (30 names, `committed 29`, repair blobs byte-identical to pop29) | 30 | **5** (R-a missing) | 6 |
| pop30 declared (30 names, `committed 30`) | 30 | **6** | **5** |

Frozen tuple explained: the frozen counter accepts 30/29 (substring match) and
rejects 30/30 (no `committed 29` substring) — `(6,6,5)`, opposite polarity to
the successor's `(6,5,6)`. A frozen-score remap cannot produce these numbers;
the successor's count is a function of the input tree.

### Input-dependence probes beyond the self-test's inputs

All four numbers move when inputs move — no constant survives:

| perturbation | derived | successor R-a |
|---|---|---|
| 28 names, `committed 29` | 28 | missing → 5 |
| 29 names, `claimed 29` (claim not exceeding count) | 29 | missing → 5 |
| 30 names via `build/nested/ExecDeep.md`, `committed 29` | 30 | missing → 5 |
| same nested tree, `committed 30` | 30 | ok → 6 |

## 4. CLI re-measurement (pinned bytes)

- `--rev e6da78b` → 6 of 6, exit 0; `--rev 3f91150` (post-dispatch tip) → 6 of 6,
  exit 0; `--rev f3246d14` → 0 of 6, exit 1. The self-test's tip arm measures
  pinned `TIP_REV=45a7ecfa` (plan-freeze commit — already carries all six
  repairs), not the live tip; the direct runs above cover the live tip.

## Residual risk / latent divergences (not defects against the frozen predicate)

1. **Count basis is "matching ls-tree entries", not "matching regular files":**
   `committed_report_count` counts any entry type (a gitlink/submodule or a tree
   named `ExecX.md` would count), and `ls-tree -r` recurses — a nested
   `build/subdir/ExecX.md` counts while the LOG's quoted census
   (`ls .ufo/waves/round-60/build | grep -cE …`) is non-recursive. Latent only:
   the real subtree is flat blobs at every measured rev (verified modes:
   32×100644 + 1×100755).
2. **Underclaim is also rejected** (`committed ≠ derived` fails both ways) —
   consistent with the predicate; noted since the plan text stresses
   overstatement.
3. `HONEST_LOG`'s line carries a trailing `` `.` `` (`build`.` — a stray
   backtick-period). `exact_path`'s boundary class `[\w./-]` still matches;
   cosmetic only.

## Mid-run lane mutation (recorded, adapted to)

At report time the lane tip is `3f91150` (wave-2 dispatch) and the working tree
carries **uncommitted** hardening of `check_routed_repairs_v2.py` (sha
`604ae4fb…`, +151 lines: `invariance_probe`, transcript/lookup negative
controls, CLI scorer-dependency arms) plus a rewritten
`C2-successor-measure.txt` (receipt_rev `3f91150`, dated 21:38Z vs committed
21:21Z). All findings above were produced against the **committed** `de5e3471…`
bytes in a sandbox clone (`/tmp/r62d1lane`, `git checkout e6da78b`; clone reads
the lane `.git` but writes nothing to it). Spot-verified: D1 construction,
`COUNT_PATTERN`, `committed_report_count`, and the paired block are byte-for-byte
identical in the hardened file; the hardened self-test prints the same paired
line. The in-flight hardening belongs to the L1 integrator; this seat wrote no
lane file other than this report.

## Commands (evidence trail)

- `sha256sum verifiers/check_routed_repairs_v2.py` → `de5e3471…` (committed),
  `604ae4fb…` (in-flight WT); frozen `95ade9be…` unchanged.
- `git ls-tree -r --name-only <rev> -- .ufo/waves/round-60/build` ×4 revs → 33
  names, 29 matching (§1).
- `python3 -B verifiers/check_routed_repairs_v2.py --self-test` (pinned bytes,
  clone) → exit 0, frozen `6 of 6` ×6 dishonest, `H1 4 of 6`, `H2 tip 6 of 6`.
- In-process probe: `check_repairs`/`committed_report_count` tables §2–§3.
- `python3 -B verifiers/check_routed_repairs_v2.py --rev <rev>` ×3 → §4.

## Tooling record

No installs (pacman paused; nothing needed beyond git/python3).

Report: `.ufo/waves/round-62/w2/FalsifyC2D1Basis.md`
