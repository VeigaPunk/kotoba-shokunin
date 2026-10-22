# LeftoverSweep — round 51 build (D1 sweep class + misroot sweep)

Lane base `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`. Read-only on the lane and the fleet repo; every
verifier run below executed in private clones under
`/fast/scratch/hyaku/kotoba-r51/build/LeftoverSweep/{lane,base}`. No tool installed or upgraded.

**Result:** SWEEP COMPLETE — one genuine leftover that leaves a lane gate red at the admitted base
(`corpus/lessons/round-50-verifier-spotcheck.md` landed by `43ca0bf` with no index row and no baseline
re-record: `verify_corpus_integrity.py` 5/9, exit 1), two fleet-root hygiene strays that are not kotoba
misroots, and the expected round-51 in-flight paths. D1's own premise reproduces byte-exactly.

## F1 — the round-50 closure commit re-created the defect round 50 had just fixed (act on this)

| item | observed | command |
|---|---|---|
| commit content | `43ca0bf` changes exactly one file, `corpus/lessons/round-50-verifier-spotcheck.md` (+280) | `git show --stat 43ca0bf` |
| corpus gate at base | `5/9 checks pass`, exit 1 | `python3 -B verifiers/verify_corpus_integrity.py` (clone at base) |
| new DRIFTs | `tracked_files: observed=70 expected=69`, `unindexed: observed=1`, `report_total: observed=45 expected=44` | same run, `--json` → `observed.corpus` |
| unindexed file | `corpus/lessons/round-50-verifier-spotcheck.md` (only file without a `corpus/README.md` row) | same run |
| carried DRIFT | `report_dead: observed=2`, `round-48-verifier-spotcheck.md:9` and `:23` cite `.ufo/reports/round-48/kotoba.md` lane-relative (the fleet file exists, 13973 bytes) | same run + `ls -l` on the fleet path |
| baseline was not bumped | last `verifiers/corpus-baseline.json` change is `a78fec1`; it expects `tracked_files 69`, `report_total 44`, `report_dead 0` | `git log -- verifiers/corpus-baseline.json`; `grep -o '"expect": [0-9]*'` |

The class is not new: `LOG.md:2396` records round 50 indexing the *round-49* spot-check for exactly this
reason (`unindexed 1`) and re-recording `tracked 66 → 68, report_total 43 → 44`; `LOG.md:2374` records
the carried `report_dead 2`. The round-50 closure then wrote one more corpus file after its own sweep —
the M21/M32 class D1 names, now inside the closure commit itself.

Repair for the L1 (deterministic, all in `corpus/` + `verifiers/`):
1. Add one `corpus/README.md` row after the `Round-50 lessons` row, e.g.
   `| Round-50 non-author spot-check (closure) | `lessons/round-50-verifier-spotcheck.md` | written by the hyaku closure `HyakuCloseKotoba50`, not the lane ... |`
   (the accepted shape of the round-46…49 rows; `git show 43ca0bf -- corpus/lessons/round-50-verifier-spotcheck.md | head -1` has the authorship line).
2. Re-record `verifiers/corpus-baseline.json` with `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json`
   (the recorder path round 50 used): `tracked_files 69 → 70`, `report_total 44 → 45`; zero-mode checks must
   not be masked.
3. Result: `8/9`, exit 1 with only `report_dead 2` left. **Do not silently edit
   `round-48-verifier-spotcheck.md`**: `corpus/README.md:68` states that closure spot-checks are outside
   review and "never edited here". Its pointer is a shape defect (fleet path written repo-relative), so either
   the L1 records it as a named carried exclusion with that reason, or the outside reviewer's own file is
   amended by the integrator — a decision, not a sweep action. Avoid presenting `9/9` as achievable without it.
4. Any new `corpus/knowledge/skill-overlap-levers-round51.md` (C2) needs its README row **and** the same
   re-record in the landing commit, or round 51 ends exactly like round 50.

## F2 — fleet repo root: 0 untracked, 6 intent-to-add, 12 modified, no kotoba misroot

`git -C /home/vgpnk/Projects/shokunin status --porcelain` → 18 lines: 6 with ` A`, 12 with ` M`; `??` count 0;
`git diff --cached --name-only | wc -l` → 0, i.e. the ` A` lines are **intent-to-add** (empty blob
`e69de29b…`, absent from the cached diff). Signature reproduced on a probe (`zz_probe`) in my clone, so this
is measured, not assumed. Consequence: a plain `git commit` does not take them; `git add -A` does.

| path | bytes / content | names kotoba | names round 50/51 | verdict |
|---|---|---|---|---|
| `.scratch/goal-20261022-hyaku-12h.md` | hyaku 12-hour goal ("You are the hyaku orchestrator (Main)") | yes, 3 hits (r48 scope, A3 row, distillation rules) | no | belongs at fleet root, hyaku-owned |
| `.ufo/state/kotoba.report-baseline` | 68 B, `51 e3b0c442…b855` (round 51, sha256 of empty) | filename only | no (content is a round + hash) | check-in of a new lane's baseline pin, correct path |
| `.ufo/state/kotodama.report-baseline` | 68 B, `53 e3b0c442…b855` | no | no | same |
| `.ufo/state/revenger.report-baseline` | 68 B, `62 e3b0c442…b855` | no | no | same |
| `write` | 25 B, no newline, `agent://U100N079H334f935b` | no | no | **hygiene stray** (see F3) |
| `scripts/hyaku/__pycache__/append-closure.cpython-314.pyc` | 10738 B, magic `2b0e0d0a` (3.14) | no | no | **hygiene stray** (see F3) |

No file at the fleet root names kotoba *and* round 50/51, so no kotoba seat wrote its round-50/51 artifact
to the fleet root. The `.report-baseline` files are the hyaku driver's per-lane report pins (tracked siblings
exist for 11 other lanes), not misroots.

## F3 — two fleet-root strays, both harmless to this round, both worth knowing

- `write`: 25-byte text file named `write` containing an agent URI with no newline, mtime
  `2026-10-21 19:52` — the shape of a misrouted write call (path taken as the literal string `write`).
  It predates the round-51 wave (launched `2026-10-22T11:07:17-03:00` per `.ufo/watchdog.log`).
- `scripts/hyaku/__pycache__/append-closure.cpython-314.pyc`: bytecode for the tracked
  `scripts/hyaku/append-closure.py`; the fleet `.gitignore` has no `__pycache__` / `*.pyc` rule
  (`grep -n -i 'pycache\|\.pyc' .gitignore` → exit 1). Any fleet `git add -A` would commit it.
Neither is a kotoba artifact; I did not touch either (read-only sweep). Fleet owner's cleanup.

## F4 — lane working tree: 3 untracked entries, 0 modified tracked files

`git -C …/kotoba-shokunin status --porcelain --ignored=no` → exactly three lines.

| path | round | facts |
|---|---|---|
| `.ufo/waves/round-50/build/DescDraft.md` | round 50 | D1's target: 10079 B, sha256 `0181a45953242fcff7595a91d8c1036b10dc4dc7aaae5303baa1cb445c3d2348`, mtime `10:52:19`, exactly 57 s after commit `2abd290` (`10:51:22`) — D1's "written 57 s after the last lane commit" reproduces. First line: `# DescDraft — C1 description draft (kotoba)`, seat `KotobaR50.DescDraft`. |
| `.ufo/waves/round-51/` (9 files) | round 51 | `build-spec.json` 54062 B, `build-dispatch.json` 78285 B, `build-gate.txt` ("granted lane=kotoba wave=r51-build seats=33 live=52 pending=0 cap=85"), `build/swarm-registry.json` 12563 B, `build-taskcall-sent.json` 66232 B, `build-task-result.txt` 2262 B, `build-validation.stderr` 0 B, `build/LeverGuard.md` 5431 B, `build/PinsRepin.md` 7869 B. In-flight wave evidence; becomes D1's class if the round lands without committing it. |
| `plans/round-51.md` | round 51 | the plan itself; `plans/round-47..50.md` are tracked, so this path is expected to land too. Untracked now (mtime `11:12:07`). |

D1 acceptance check the executor can run after committing: `git show <commit>:.ufo/waves/round-50/build/DescDraft.md | sha256sum`
must print `0181a459…c3d2348`. The sibling late writer `D2D4Wording.md` (mtime `10:51:16`) is already tracked,
so `DescDraft.md` is the only surviving late write of round 50.

## F5 — round-50 wave directory: 78 tracked vs 79 on disk, one file short

`git ls-files .ufo/waves/round-50 | wc -l` → 78; `find .ufo/waves/round-50 -type f | wc -l` → 79; set
difference (`comm -13`, C locale) → `.ufo/waves/round-50/build/DescDraft.md` only; reverse direction
(`comm -23`) → empty, so no tracked round-50 artifact is missing from disk. Round 50's other wave evidence
(34 files under `build/`, incl. the late `D2D4Wording.md`) is tracked.

## F6 — corpus index: 66 of 67 corpus files have a README row; 1 miss

Files: 29 under `corpus/lessons/`, 38 under `corpus/knowledge/` (67). Two independent readers agree:
my own brace-expanding matcher over backticked FILE-column tokens → `missing_count 1`, and the shipped
checker → `unindexed: 1`. The single miss is `lessons/round-50-verifier-spotcheck.md` (F1). Everything else
is covered, including the `round-{1,4,5}-aggregator-audit.md` brace row and the round-50 knowledge row.

## F7 — plan before-values: C1 and C2 both reproduce at base

- C1: `python3 -B verifiers/verify_surfaces.py --json` in a clone at base → `{'pass': 5, 'fail': 2,
  'exit_code': 1}` — exactly the plan's before-value. Calibrated.
- C2: at base the counter did not exist (`… --rev 43ca0bf…` → exit 2, file not found). The `LeverGuard` seat
  wrote it mid-wave; running that new file (copied into my clone) against `43ca0bf` now prints
  `overlap levers backed 0 of 7 clients` with seven `UNBACKED: SKILL.md table absent (<client>)` lines, exit 1 —
  the plan's before-value reproduces. It still has to reach `7 of 7` with the denominator pinned in the script,
  and `--self-test` has to kill the mutants the plan lists.

## Evidence (commands, exit codes verbatim)

| # | command | exit |
|---|---|---|
| 1 | `git -C /home/vgpnk/Projects/shokunin status --porcelain` | 0 |
| 2 | `git status --porcelain \| awk '{print $1}' \| sort \| uniq -c` → `6 A`, `12 M` | 0 |
| 3 | `git diff --cached --name-only \| wc -l` → 0 (all ` A` are intent-to-add) | 0 |
| 4 | `git ls-files --stage -- write` → `100644 e69de29b…\t0\twrite` | 0 |
| 5 | `grep -n -i 'pycache\|\.pyc' .gitignore` (fleet) → no match | 1 |
| 6 | `git -C …/kotoba-shokunin status --porcelain --ignored=no` → 3 lines | 0 |
| 7 | `git ls-files .ufo/waves/round-50 \| wc -l` → 78; `find … -type f \| wc -l` → 79 | 0 |
| 8 | `comm -13 <(git ls-files …) <(find …)` → `DescDraft.md` | 0 |
| 9 | `find corpus/lessons -type f \| wc -l` → 29; `find corpus/knowledge -type f \| wc -l` → 38 | 0 |
| 10 | own brace matcher over `corpus/README.md` → `files_checked 67`, `missing_count 1` | 0 |
| 11 | `python3 -B verifiers/verify_corpus_integrity.py` (clone at `43ca0bf`) → `5/9 checks pass`, 4 DRIFT | 1 |
| 12 | same, `--json` → `unindexed_detail ["corpus/lessons/round-50-verifier-spotcheck.md"]`, `report_dead 2` | 1 |
| 13 | `python3 -B base/verifiers/verify_corpus_integrity.py` (clone at `a78fec1`) → `6/9`, DRIFT report_dead, commit_total 31≠30, commit_unresolvable 1 | 1 |
| 14 | `python3 -B verifiers/verify_surfaces.py --json` (clone at `43ca0bf`) → pass 5 / fail 2 | 1 |
| 15 | `python3 -B verifiers/check_overlap_levers.py --rev 43ca0bf…` before the seat wrote it → `can't open file` | 2 |
| 15b | same, with the seat's new script copied into my clone → `overlap levers backed 0 of 7 clients` | 1 |
| 16 | `git show --stat 43ca0bf` → `1 file changed, 280 insertions(+)` | 0 |
| 17 | `stat -c '%y %n' .ufo/waves/round-50/build/DescDraft.md` → `10:52:19`; `git log -1 --format='%ci' 2abd290` → `10:51:22` | 0 |
| 18 | `grep -aci 'kotoba' <each fleet intent-to-add path>` → goal 3, others 0; `grep -acE 'round.?5[01]'` → 0 everywhere | 0 |

Notes on method: LSP was not applicable — every question here is git-index, filesystem or corpus-text state,
with no symbol contract to resolve; `grep` is used as a literal content filter (naming sweep) and as a
record of a negative (`__pycache__` ignore rule), never as semantic proof. Line 13's two extra DRIFTs at
`a78fec1` include a self-referential landing citation that resolves only at later commits; they are recorded
as observed, not as a round-50 defect.

## Remaining unknowns

- Whether the round-51 landing commits `plans/round-51.md` and `.ufo/waves/round-51/` (F4) — a closure
  decision I cannot make read-only; if either survives, it is a new D1-class leftover.
- Who owns the fleet-root `write` stray and the staged-intent `.pyc` (outside the lane; not kotoba's).
- Whether `report_dead 2` is fixed (outside-review edit, forbidden by `corpus/README.md:68`) or recorded as a
  named carried exclusion; the L1 decides, and round 51 can land at 8/9 with that record.
