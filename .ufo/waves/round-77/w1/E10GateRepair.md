# E10GateRepair — R76-D4 corpus-gate repair (kotoba round 77, w1)

Seat: `E10GateRepair` (leaf executor). Lane source: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
at `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (freeze). No lane file was edited; no commit, add,
stash or checkout in the lane repo. Both frozen counters are byte-identical to the plan pins:
`verifiers/check_desc_craft.py` = `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`,
`verifiers/check_r75_routed_repairs.py` = `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`.

Axes this seat names (per the round's scoring frame): **depth** and **consistency** are *not* moved by
this seat and no claim is made on them — this is the R76-D4 hygiene item (the gate repair the closure
routed). The axis it does serve is **operability**: a gate that reads red at base cannot certify any
landing, so the repair is what lets C1/C2 evidence be measured at all. **Calibration** is touched only
negatively (two fail-closed refusals added to the refresh path), and **freshness** not at all.

## 1. The defect, reproduced from committed bytes

Base tree, pristine `git clone --shared` of lane HEAD
(`/fast/scratch/hyaku/kotoba-r77/E10GateRepair/ev1`, toplevel verified = clone):

```
$ python3 -B verifiers/verify_corpus_integrity.py --json        exit=1
$ python3 -B verifiers/verify_corpus_independent.py --json      exit=1
```

| check | observed | expected | verdict |
|---|---|---|---|
| `corpus.index.tracked_files` | 146 | 144 | DRIFT |
| `corpus.index.unindexed` | 2 | 0 | DRIFT |
| `corpus.pointers.report_total` | 102 | 99 | DRIFT |
| `corpus.pointers.commit_total` | 44 | 43 | DRIFT |
| stale / missing / report_dead / commit_unresolvable / commit_nonhash | 0 | 0 | PASS |

`unindexed_detail` = `corpus/lessons/round-75-verifier-spotcheck.md`,
`corpus/lessons/round-76-verifier-spotcheck.md`. The independent implementation agrees on all four
drifts and on both unindexed names (receipt `E10GateRepair.gates.txt` stage 1).

### Where every count comes from (measured, not asserted)

Per-file recomputation of the pointer/commit classes over `git show` blobs at `65a5c7a` (the revision
the current baseline was recorded against) versus `HEAD`:

| file | report / commit at `65a5c7a` | at `6523aced` |
|---|---|---|
| `corpus/lessons/round-75-verifier-spotcheck.md` | 0 / 0 (absent) | **2 / 1** |
| `corpus/lessons/round-76-verifier-spotcheck.md` | 0 / 0 (absent) | **1 / 0** |
| every other tracked corpus markdown | unchanged | unchanged |
| totals | 99 / 43 | 102 / 44 |

So the whole drift is the two closure spot-check files: +2 tracked files, +3 report pointers, +1
resolvable commit token. Nothing was "fitted to a denominator"; the repair re-records those bytes.

## 2. How a lane index row is written, and how rounds 53–75 refreshed the baseline

- **Index row.** `file_column_tokens()` harvests backticked tokens in **column 2 (File)** of a
  `## Coverage map` table row in `corpus/README.md`, outside fenced regions. A corpus-relative token
  (`lessons/x.md`) is expanded against `git ls-files corpus/` by exact match or `fnmatch`; the union
  of hits must cover every tracked corpus file except `README.md` itself, or
  `corpus.index.unindexed` rises. The description cell is *not* an index path — but it is scanned
  like the rest of the file for `.ufo/reports/round-<n>/…md` pointers and `commit `<hex>`` citations,
  which is why a row can silently move `report_total`/`commit_total`.
- **Baseline refresh.** `verifiers/corpus-baseline.json` is a property of the checked tree: the gate
  loads `<repo>/verifiers/corpus-baseline.json`, compares `equal` ids to `expect`, and adjudicates
  `zero` ids baseline-free. Rounds 53–75 refreshed it by running
  `verify_corpus_integrity.py --no-baseline --json` on the tree where every round file already
  landed, then re-recording `tracked_files` / `report_total` / `commit_total` and appending a dated
  `notes` key — `git log -S'corpus.index.tracked_files' -- verifiers/corpus-baseline.json` shows the
  practice from `4dd7753` (round 11) through `14ab415` (round 75), and the r74/r75 notes state the
  rule explicitly: re-recorded to observed bytes, zero-mode expectations stay zero. Every one of
  those refreshes happened **after** the round's file had landed, which is the ordering the L1 must
  keep (see §5).

## 3. Deliverables

| file | sha256 | what it is |
|---|---|---|
| `.ufo/waves/round-77/build/E10GateRepair.readme-index-rows.patch` | `3b3b7dbbef59fce2b5da82682aa790b6f5bbb0870288bce85473e93ef6b3da26` | the two missing index rows as a `git apply`-able diff (a/ b/ prefixes; the lane's `diff.mnemonicPrefix=true` would otherwise emit `i/` `w/`) |
| `.ufo/waves/round-77/build/E10GateRepair.readme-index-rows.md` | `a14142c05d6f78bcd00e262080bf2ffa7e7d9da9374ca91f43b2bd32186e2d45` | the rows verbatim, the pattern they satisfy, the insertion anchor, the measured effect, and the SC06 conflict |
| `.ufo/waves/round-77/build/E10GateRepair.refresh_baseline.sh` | `862689e0972259a74bab9f780fd8c69e8b8453e4cbcba45dd2441909bd851f25` | the recipe: recomputes every `equal` expectation from the integrity gate's own `--no-baseline --json`, asserts every `zero` expectation is 0, prints `old -> new`, writes the baseline in its existing shape, then re-runs both gates and fails if either is non-zero |
| `.ufo/waves/round-77/build/E10GateRepair.notes.md` | `774c074079040704b9a0e45ec8b5f0216d75dd6d5ba17a38ac480cbb801e7485` | which new files must be indexed, how the counts move, the landing order (baseline LAST), residual risks |

Receipts (`.ufo/waves/round-77/receipts/`): `E10GateRepair.gates.txt`,
`E10GateRepair.recipe.txt`, `E10GateRepair.sibling-rows-ordering.txt`,
`E10GateRepair.patch-conflict.txt`. Every command in them was captured as `cmd > out 2>&1; echo
"exit=$?"` on that command alone — no `| tail`, no pipeline status anywhere.

## 4. The proof (scratch clones of lane HEAD; each gate's own exit status)

`ev1` pristine · `ev2` + index-rows patch · `ev3` + patch and recipe. Each clone's
`git rev-parse --show-toplevel` was asserted equal to the clone path before the first write.

| stage | integrity exit | independent exit | observations |
|---|---|---|---|
| 1. base | **1** | **1** | unindexed 2; 146/102/44 vs 144/99/43 |
| 2. + index rows, old baseline | **1** | **0** | unindexed 0, stale 0, missing 0, report_dead 0, commit_unresolvable 0, commit_nonhash 0; the three `equal` drifts remain |
| 3. + recipe | **0** (9 PASS) | **0** | `tracked_files 144 -> 146`, `report_total 99 -> 102`, `commit_total 43 -> 44` |

Recipe behaviour (`E10GateRepair.recipe.txt`, clone `sim5`):

- run on the final tree: prints the three `old -> new` lines, writes the baseline, and re-verifies
  both gates green (`verified: both corpus gates exit 0 against the re-recorded baseline`) → exit 0;
- second run: `no expectation moved` → exit 0 (idempotent);
- untracked `corpus/` file present: refuses, exit 2, baseline sha256 unchanged
  (`d00783aee7367ccbfe5d6ef8b82ff2451ab0c89a08839c67036a0da3d1d78d2d` before and after);
- staged but unindexed `corpus/` file: refuses, exit 2, same unchanged digest;
- a path that is not the work-tree toplevel: refuses, exit 2;
- three new corpus files each carrying one report pointer and one `commit` token, with their rows:
  observed `149 / 0 / 105 / 47` (from `146 / 0 / 102 / 44`), recipe records exactly that and both
  gates exit 0. This is the "how the counts move" evidence: **+1 tracked per file, plus whatever that
  file cites** — so the L1 must let the recipe produce the numbers, never type them.

## 5. Operability: what the L1 must do, in order

1. Land the two spot-check rows **now** (this patch) — they index files that already exist, so this
   patch is green on the base tree and depends on nothing unlanded. Result of stage 2 above.
2. Land the three r77 data files (`corpus/lessons/round-76.md`, `corpus/lessons/round-77.md`,
   `corpus/knowledge/description-craft-round76.md`) **with** their index rows in the same commit. A
   row without its file costs two zero-mode failures: measured on the sibling patch
   `build/SC06ReadmeCorpus.patch` at the base tree, `stale_patterns` 0 → 3 and `missing_paths` 0 → 3
   (`E10GateRepair.sibling-rows-ordering.txt` §1); with the files present and committed both return to
   0 and the recipe closes the `equal` ids (§2 of the same receipt).
3. **Baseline refresh last**, after the final `corpus/` change: clone the final tree to scratch
   (commit anything untracked there — the recipe refuses otherwise, because the gate's universe is
   `git ls-files`), run
   `E10GateRepair.refresh_baseline.sh <clone> round77_rerecord`, commit the resulting
   `verifiers/corpus-baseline.json` as its own commit, then run the no-harm battery at that tip.
   Re-run the recipe after any later `corpus/` change; it is idempotent and preserves the baseline's
   `repo` identity instead of recording the scratch directory's name.

### Conflict the L1 must resolve before applying anything

`build/SC06ReadmeCorpus.patch` (sibling seat) contains the same two spot-check rows **plus** rows for
the three r77 data files and a Round 77 Core/known-gap note. The two patches are mutually exclusive in
both orders — `git apply --check` exits 1 each way (`E10GateRepair.patch-conflict.txt`), because both
insert at the `## Frontier` anchor. Apply **exactly one**: SC06's is the superset and is correct only
if it lands in the same commit as its three files; this seat's patch is the fallback that is green at
base today. Applying both would produce duplicate rows for the two spot-checks (and is blocked anyway).

## 6. Risks, limits, and what this seat did not do

- **Not a claim.** No axis score moves on this report; C1 and C2 remain unmeasured by this seat and
  their counters were not touched.
- **The gate cannot see untracked files.** A corpus file the integrator forgets to `git add` leaves
  `unindexed` at 0. That is structural; the recipe guards only its own run.
- **Rows are prose with counts attached.** A later edit that adds a pointer or a `commit` token to a
  description cell moves `equal` expectations; only a baseline refresh catches it (as a red drift).
- **No installs.** No tool was installed or upgraded (pacman untouched, per the host pause); no
  package manager, no `uv`, no `npx` was needed.
- **Scratch removed.** `/fast/scratch/hyaku/kotoba-r77/E10GateRepair` and `…/E10GateRepair3` (the
  overlay sandboxes used for §7) were deleted after the last receipt was written; nothing in `/tmp` is
  cited as evidence. Lane tree unchanged: `git -C <lane>
  status --porcelain` shows only the pre-existing untracked `.ufo/waves/round-77/` artifacts, `HEAD`
  still `6523aced`.

## 7. Addendum — the standing battery red reported by `E12BatteryScript` (verified, not owned)

Peer report: `verify_skill_checklist.py` and `check_assertion_floors.py` are red at `6523ace` because
`LOG.md:2818` (round-76 entry, committed at `ec7f853`) carries the bare token
`.ufo/reports/round-76/kotoba.md`, which resolves inside the lane and misses the fleet report. This
seat re-measured it independently rather than taking the report:

- **Harness first.** The governance check resolves leading `..` hops against the **parent of the
  repo**, so a scratch clone under `/fast/scratch/...` is not a faithful harness: it reports ~30
  spurious failures (`../PROTOCOL.md`, `../kasegi-shokunin/...`). All numbers below come from clones
  placed beside a symlink overlay of the fleet root (`$S/fleet`, `$S/fleetA`, `$S/fleetB`, each with
  the fleet's sibling entries and `.ufo` symlinked). Any seat quoting this gate from a bare clone
  should re-run with that overlay or against the lane path.
- `verify_skill_checklist.py --json` at `6523aced` (overlay clone): **exit 1, 10 pass / 1 fail**; the
  single failure is `LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not resolve`, with "2
  recorded absence(s) excused, 4 recorded correction(s) excused". At `b7f13f4` the same gate is
  **exit 0, 11 pass / 0 fail**.
- `verify_skill_checklist.py --self-test` at the **lane path**: exit 1, `1 failure(s) over 1863
  assertions`, failing on the live-data fixture ("governance: live round-65 corrections land,
  errata-excused"), i.e. the self-test red is downstream of the same data defect, not a second one.
  `check_assertion_floors.py`'s checklist arm therefore fails for the same reason.
- Provenance and the fix target: `git log -S'.ufo/reports/round-76/kotoba.md' -- LOG.md` → `ec7f853`;
  `lane/.ufo/reports/round-76/` does not exist, `fleet/.ufo/reports/round-76/kotoba.md` does, and
  `citation_resolve("../.ufo/reports/round-76/kotoba.md", lane)` → `True`.
- Two routes, both measured in the overlay sandboxes (receipt
  `E10GateRepair.battery-log-pointer.txt`):
  - **A — rewrite the token in place** (`../.ufo/reports/round-76/kotoba.md`): checklist **exit 0,
    11/0**, self-test **exit 0, 0 failures**, `check_assertion_floors.py` **exit 0** (`PASS checklist
    observed=1863 floor=1863`). One line, no gate edit — but it contradicts the lane's own append-only
    rule for `LOG.md` (`LOG.md:2619`, round-65 notice: "corrections land as new entries, never
    in-place edits").
  - **B — appended notice + pinned row** (notice as a new `LOG.md` line with both tokens
    double-quoted, `GOVERNANCE_CORRECTIONS_HORIZON` bumped to that line, one
    `(notice line, line sha256, "LOG.md", 2818, stale, corrected)` row): checklist **exit 0, 11/0**,
    but the self-test then **fails 1** because its live fixture pins the literal "4 recorded
    correction(s) excused"; adding that fifth row's expectation update
    (`verify_skill_checklist.py:2526`, 4 → 5) makes it **B2**: self-test **exit 0, 0 failures**,
    `check_assertion_floors.py` **exit 0** (`PASS checklist observed=1863 floor=1863`) — fully inside
    the r65 correction mechanism, at four coupled edits instead of one line.
  - Net: `check_assertion_floors.py`'s only base red was this checklist arm (both routes take the
    whole gate to exit 0), so the L1's choice is purely A's one line vs B2's convention compliance.
- This seat did not apply either route: the file is `LOG.md` (lane data) and, for B, a verifier. It is
  the L1's call, and `E12BatteryScript` holds that battery item; the measurements and both exact
  change sets are handed over in the receipt.
- **Independent agreement.** `E12BatteryScript` re-measured with the same clone-overlay shape and
  reports the identical `10 pass / 1 fail`, exit 1, sole failure `LOG.md:2818` at `6523ace` (and
  `11/0` at `b7f13f4`), and agrees that the checklist self-test/assertion-floor reds are downstream
  of that line. Two independent readings, two harnesses, same numbers.

VERDICT: R76-D4 repaired and proved in scratch clones — the two closure spot-check index rows are patched, the baseline is re-recorded by a guarded no-hand-numbers recipe (144/99/43 -> 146/102/44), both corpus gates exit 0 after the repair while the base exits 1 on both, and the row-must-land-with-its-file ordering plus the SC06 patch conflict are measured and documented for the L1.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E10GateRepair.readme-index-rows.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E10GateRepair.readme-index-rows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E10GateRepair.refresh_baseline.sh, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E10GateRepair.notes.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E10GateRepair.gates.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E10GateRepair.recipe.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E10GateRepair.sibling-rows-ordering.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E10GateRepair.patch-conflict.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E10GateRepair.battery-log-pointer.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E10GateRepair.md
