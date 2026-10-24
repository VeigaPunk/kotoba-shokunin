# ScoutQualityDebt

role: scout (leaf; no subagent dispatch)
item: carry-forward quality debt on SCORECARD.md `Next: round 64`, plus r63 spot-check routed items 1–4, at the current tip
revision judged: `c04fffbeafcaf810897258d56f99cca736ed3a91` (plan freeze; parent `078eec4` is the r63 spot-check). Committed bytes, plus the working tree for routed item 1.
installs: none
confidence: high on the searches and the quoted sentences. Not claimed: a line-by-line re-score of every r62 wave-2 report beyond the four remainder sentences.

Axes used: exact Next-line bytes; open vs closed against committed bytes; recommended handling limited to claim / lesson note / defer. Frozen plan (`plans/round-64.md`) already binds routed items 1–4 as C2 and says the SCORECARD Next-line debt stays outside that counter. No production edit.

## Pinned Next line

`SCORECARD.md:371` at HEAD (one line):

```
**Next: round 64** — survivor debt: the W8 escape class and A2's F6 compound-purpose bound; C2 remains bounded to the five r62 spot-check repair checks, so a new self-assessment mismatch class remains outside its counter; v33 candidates recorded by E3 (the one-word tail needs `MIN_SHARED` coupling; the `-and-`/quote/relatedness lanes need a deliberate contract change). Carry-forward quality debt until evidenced closed (verified open at the r63 close by `ScoutW2QualityDebt`): SentBounds' pre-wave baseline receipt; helper-invocation receipts; the r62 wave-2 dispositions remainder (M93 hollow diagnostic wording, the `LOG.md:2549` clock, SCORECARD's r62 no-harm sentence vs the receipt's two interim reds, the r61 R-b corpus-idx omission).
```

Prior verdict `.ufo/waves/round-63/w2/ScoutW2QualityDebt.md` was at `cbbee56e`. Re-checked here at HEAD. `corpus/lessons/round-62.md` has no commit in `cbbee56e..HEAD`. SCORECARD commits in that range (`849a546`, `2ba4547`) added round-63 annotations and did not retract the debt clause. `078eec4` and `c04fffbe` do not touch `LOG.md` or `SCORECARD.md`.

Owned-axis scores still `SCORECARD.md:28` depth **9**, `:29` consistency **10**. Round-63 annotation `:373` repeats depth held 9, consistency held 10.

## Disposition table

| debt item | open/closed | evidence pointer | recommended round-64 handling |
|---|---|---|---|
| SentBounds' pre-wave baseline receipt | **open** | no `bounds.md` at rounds 61–64 (`git cat-file -e` exit 128 ×4); `fleet_status` / `jj_op_head` hits are the unrun proposal in `.ufo/waves/round-61/wave/SentBounds.md:177,181` plus later mentions of the debt name | **defer** — wave 1 is already dispatched; a snapshot now is not pre-dispatch. Outside frozen C1/C2 |
| helper-invocation receipts | **open** | phrase hits are the debt name, `SentBounds.md:80` (the remediation sentence), and later mentions. `LOG.md` has zero hits. `rg` of `jj-lane.sh` for `op log` / `argv` / `invocation receipt` exits 1 | **defer** — L1 process change, not a paperwork fix. Outside frozen C1/C2 |
| M93 hollow diagnostic wording | **open** | `corpus/lessons/round-62.md:25` still says the hollow diagnostic is a missing `` `check_scoped_rules.py` `` path. Receipt `.ufo/waves/round-62/controls/absorption-hollow.txt:8` says `guard-mutation direction is missing for one or more errata`, `exit=1` | **lesson note** (append-only). Do not fold into C2 |
| `LOG.md:2549` clock | **open** | line still dates `absorption-before.txt` at `2026-10-23T20:53:36Z`. Receipt line 2 is `date_utc=2026-10-23T20:57:43Z`. `20:53:36` is absent from the receipt | **lesson note** (append-only LOG/lesson correction). Not a claim |
| SCORECARD r62 no-harm sentence vs two interim reds | **open** | `SCORECARD.md:36` still ends "No axis harmed: the frozen counter is byte-identical (`5a5adc94…`) and the successor self-test imports the frozen six unchanged." `noharm-tip.txt:12` `FAIL reg_gate`, `:17` `FAIL corpus-idx`, `:23` `Battery exit code: 124`. `LOG.md:2573` corrected the fleet-report bullet only | **lesson note** (append-only SCORECARD annotation). The report-side fix is already counted by r63 C2; do not re-claim it |
| r61 R-b corpus-idx omission | **open** (list sentence only) | `LOG.md:2557` says "complete list to date" and does not contain `round-61-verifier-spotcheck` or the substring `spot-check`. The index gap itself is **closed**: `corpus/README.md:108` names `lessons/round-61-verifier-spotcheck.md`; `LOG.md:2573` records the interim `corpus-idx` red as fixed | **lesson note** naming the omitted path. Do not re-open the corpus-idx gate |
| r63 routed 1 — uncommitted `MutW2SplitClauses.md` | **open** | porcelain below; committed blob lacks `temporal mismatch` (`git grep` exit 1); worktree line 728 has it | **claim** — frozen C2 check `seat-edit-committed` |
| r63 routed 2 — controls cited `@ 35d44b4b` | **open** | fleet report `.ufo/reports/round-63/kotoba.md:31-32`. True add revs `8c4cefa8` and `cbbee56e`. Both paths absent at `35d44b4b` (`cat-file` exit 128) | **claim** — C2 check `control-revs-named`. See false-green hazard |
| r63 routed 3 — lowest-axis parenthetical | **open** | fleet report `:8` says "lowest owned axis — calibration/consistency". No LOG line contains both `lowest` and `depth`. SCORECARD owns depth 9 < consistency 10 | **claim** — C2 check `lowest-axis-corrected` |
| r63 routed 4 — `ExecW2E2Patch` "21 assertions" | **open** | seat file still says 21 at `:496` (also `:146,:413,:427,:430,:519,:589`). Spot-check count of the committed counter is 23. `verifiers/check_r64_routed_repairs.py` absent at HEAD (`cat-file` exit 128) | **claim** — C2 check `assertion-count-named`. See count-method hazard |

Closed subset, do not re-open: r62 lesson `## Falsify corrections` F1–F17; r62 spot-check `:147-152`; the corpus-idx **index** row at `README.md:108`; `LOG.md:2573` (report no-harm bullet). Those pointers do not cover the four sentences above.

## (1) SentBounds pre-wave baseline — open

Closure would be a committed pre-dispatch snapshot of fleet status, lane status, runtime-file bytes, sibling HEADs/statuses, and the jj op id (`SentBounds.md:68`; keys `fleet_status` `:177`, `jj_op_head` `:181`).

```
git grep -n -I -e 'fleet_status' -e 'jj_op_head' -e 'pre-wave baseline' HEAD -- '*.md' '*.json' '*.txt'
```

Exit 0. Every hit is `SentBounds.md` (the unrun proposal), `ScoutR62Candidates.md:36` ("do not claim the debt closed"), `FalsifyReportClaims.md` Next-line diffs, `ExecScorecardRow.md:20`, `ScoutW2QualityDebt.md`, `RevW2ScorecardWording.md`, the r63 w2 spec/dispatch prompts, or `SCORECARD.md:371`. No captured receipt.

```
git cat-file -e HEAD:.ufo/waves/round-61/bounds.md   # fatal, exit 128
git cat-file -e HEAD:.ufo/waves/round-62/bounds.md   # fatal, exit 128
git cat-file -e HEAD:.ufo/waves/round-63/bounds.md   # fatal, exit 128
git cat-file -e HEAD:.ufo/waves/round-64/bounds.md   # fatal, exit 128
```

## (2) helper-invocation receipts — open

Closure would be a precommitted receipt of each helper invocation: before/after jj op ids, helper path, hash, and argv (`SentBounds.md:80`).

```
git grep -n -I -e 'helper-invocation' -e 'helper invocation' HEAD -- SCORECARD.md LOG.md plans corpus/lessons .ufo/waves/round-61 .ufo/waves/round-62 .ufo/waves/round-63 .ufo/waves/round-64
```

Exit 0. Hits are `SentBounds.md:80`, `ScoutR62Candidates.md:5,53`, `FalsifyReportClaims.md:614,617`, `FalsifyScorecard.md:145`, `ExecScorecardRow.md:20`, the r63 scout/reviewer/spec files, and `SCORECARD.md:371`. `LOG.md`: zero hits. `plans/round-64.md`: zero hits.

```
rg -n -e 'op log' -e 'argv' -e 'invocation receipt' /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh
```

Exit 1. The helper still does not write the ledger `SentBounds.md:76` said was absent.

## (3) r62 wave-2 remainder — four sentences still false

### M93

`corpus/lessons/round-62.md:25`, tail of the "shown able to fail" clause (unchanged since `cbbee56e`):

```
shown able to fail: `.ufo/waves/round-62/controls/absorption-hollow.txt:5-8` records the hollow variant exiting 1, but its diagnostic is a missing `check_scoped_rules.py` path, not the intended guard-direction rejection
```

Receipt, committed:

```
     6	## variant H (hollow: never runs the guard-mutation direction)
     7	$ python3 -B /tmp/r62hollow/hollow.py --self-test
     8	absorption self-test failed: guard-mutation direction is missing for one or more errata
     9	exit=1
```

The missing-path sentence was never true of that receipt.

### LOG clock

`LOG.md:2549` still contains `2026-10-23T20:53:36Z` next to `absorption-before.txt`.

```
     1	# Round-62 pre-data control: absorption-before (C1)
     2	date_utc=2026-10-23T20:57:43Z
```

Python: `BEFORE_HAS_20:53:36 False`, `BEFORE_HAS_20:57:43 True`.

### SCORECARD no-harm sentence

`SCORECARD.md:36` tail (length 1857), still:

```
No axis harmed: the frozen counter is byte-identical (`5a5adc94…`) and the successor self-test imports the frozen six unchanged.
```

```
HEAD:.ufo/waves/round-62/noharm-tip.txt:12:FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1
HEAD:.ufo/waves/round-62/noharm-tip.txt:17:FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/lessons/round-61-verifier-spotcheck.md
HEAD:.ufo/waves/round-62/noharm-tip.txt:23:Battery exit code: 124
```

`LOG.md:2573` names those two interim reds and records them fixed by `e6da78bb`/`e424f2a4`. That does not make line 36 true. Hash identity of `check_scoped_rules.py` is not a no-harm pass.

### R-b list

`LOG.md:2557` (614 bytes). Python: `HAS_round-61-verifier-spotcheck False`, `HAS_spot-check False`, `HAS_complete list True`. The line ends:

```
`corpus/lessons/round-62.md`, `corpus/QUALITY.md` (Q57), `corpus/README.md`, `SCORECARD.md`, `LOG.md`.
```

`corpus/lessons/round-61-verifier-spotcheck.md` is in the tree and indexed at `corpus/README.md:108`. The omission is the "complete list" sentence, not the index.

## Routed items 1–4 — all open; C2 not built yet

`git cat-file -e HEAD:verifiers/check_r64_routed_repairs.py` → fatal, exit 128.

### Item 1 — working tree (required paste)

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain
 M .ufo/waves/round-63/w2/MutW2SplitClauses.md
?? .ufo/waves/round-64/w1-dispatch.err
?? .ufo/waves/round-64/w1-dispatch.json
?? .ufo/waves/round-64/w1-spec.json
?? .ufo/waves/round-64/w1/
```

Exit 0. The `??` paths are this wave's dispatch artifacts, not defect 1.

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --stat
 .ufo/waves/round-63/w2/MutW2SplitClauses.md | 111 ++++++++++++++++++++--------
 1 file changed, 82 insertions(+), 29 deletions(-)
```

Exit 0. HEAD at the command: `c04fffbeafcaf810897258d56f99cca736ed3a91`. Matches the plan's inherited `82+/29-` against `38defdc` (the spot-check's earlier `41+/13-` is stale; the worktree grew after that closure).

```
git grep -n -e 'temporal mismatch' HEAD -- .ufo/waves/round-63/w2/MutW2SplitClauses.md
```

Exit 1 (marker absent from the committed blob).

```
rg -n -e 'temporal mismatch' .ufo/waves/round-63/w2/MutW2SplitClauses.md
```

Exit 0: line 728 `was a **temporal mismatch** on my part.`

### Item 2 — citation

Fleet report (not in the lane tree) `/home/vgpnk/Projects/shokunin/.ufo/reports/round-63/kotoba.md:31-32` still cites both controls `@ 35d44b4b`:

- `:31` `controls/C1-do-nothing-v31.txt` @ `35d44b4b`
- `:32` `controls/C2-before-r62tip.txt` @ `35d44b4b`

True committing revisions (`git log --diff-filter=A --format=%H -1`):

```
8c4cefa8e1b751d5f93dbcc65349b8e985b102d8  .ufo/waves/round-63/controls/C1-do-nothing-v31.txt
cbbee56e9a3589b0b46736ad36f1b77701def80e  .ufo/waves/round-63/controls/C2-before-r62tip.txt
```

```
git cat-file -e 35d44b4b:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt   # exit 128, not in that rev
git cat-file -e 35d44b4b:.ufo/waves/round-63/controls/C2-before-r62tip.txt   # exit 128, not in that rev
```

No LOG line states those two hashes as the control files' committing revs.

**False-green hazard for C2 check 2.** `LOG.md:2576` (1201 bytes) already contains `8c4cefa`, `cbbee56`, and `35d44b4b` on one line. That line is the round-63 defect-2c descendant correction ("nothing else descends from `e53b6e5c` is false"), not a control-rev citation. It is inside the LOG prefix at `078eec4` / HEAD (neither commit touches `LOG.md`). A suffix anchored at the r62 tip `35d44b4b`, or any whole-LOG co-occurrence scan, credits this line and check 2 goes green before round 64 writes anything. The scan baseline has to be the LOG bytes at `078eec4` (same bytes at HEAD), and the new line has to say these hashes are the committing revs of the two control paths. [INFERENCE] from the plan's "appended-suffix" wording plus this line; the r64 counter does not exist yet, so this is a construction constraint, not a measured counter failure.

### Item 3 — lowest axis

Fleet report `:8`:

```
Declared claims (2, both measured; at least one on the lowest owned axis — calibration/consistency):
```

SCORECARD owns depth 9 (`:28`) below consistency 10 (`:29`). Python over `LOG.md`: no line contains both `lowest` and `depth`. `SCORECARD.md:365` says "lowest owned axis is depth 9" in a round-47 disposition; that is not an appended correction of the r63 report parenthetical.

### Item 4 — assertion count

`ExecW2E2Patch.md:496` (committed):

```
| patched counter `--self-test` | `self-test: 0 failure(s) over 21 assertions`, exit 0 |
```

Same "21 assertions" also at lines 146, 413, 427, 430, 498, 519, 589, 595. Not amended.

Spot-check method (`round-63-verifier-spotcheck.md:96-98`): 17 fixed `check()` calls + the counter-arms loop (3 arms × 2 checks) = **23**. Re-derived on HEAD source: 19 lines matching a call-site `check(` (17 outside the loop at 444, 450, 452, 454, 456, 458, 460, 476, 478, 485, 497, 510, 517, 523, 533, 543, 550; loop body at 595 and 601, executed for `label-only` / `fingerprint` / `worktree-read`). `def check(` is one extra `check(` token, so a raw `check(` count is 20, not 23.

**Count-method hazard for C2 check 4.** `plans/round-64.md` says the counter counts `` `check(` `` invocations and expects 23. A raw count of the token or of source lines yields 20 or 19. The number that matches the spot-check, the report (`kotoba.md:17,32`), and `LOG.md:2582` ("23 assertions") is the runtime expansion 17 + 3×2. A counter that requires the seat file to name its own raw count would amend `ExecW2E2Patch` to the wrong integer and miss the defect.

## What this supports

- Supports the Next line's "verified open" clause: all six named debts are still open at `c04fffbe`. None gained a closing receipt after `ScoutW2QualityDebt`.
- Supports C2's "0 of 4 at `078eec4`" expectation: items 1–4 are all still red, and the r64 counter is absent. Holds only if check 2's suffix baseline is the LOG at `078eec4`, not `35d44b4b` (hazard above), and check 4 expands the loop to 23 (hazard above).
- Does not support closing any of these inside C1. C1 is the G7 `span_missing` arms; these sentences are paperwork.
- Does not support adding a third claim. `plans/round-64.md:161` already leaves the Next-line debt outside the counter.

## Recommended handling (frozen-plan compatible)

- Routed 1–4: land under C2 as written. Commit the worktree `MutW2SplitClauses.md` (do not revert; the marker is only in the worktree). Append one LOG suffix line past the `078eec4` LOG that names `8c4cefa8` and `cbbee56e` as the committing revs of the two control paths and also names base `35d44b4b`. Append one LOG suffix line that depth (9) is the lowest owned axis and consistency is 10. Amend `ExecW2E2Patch.md` so the patched-counter cell names 23, not 21.
- The four false r62 sentences: one append-only lesson/LOG/SCORECARD note this round, not a counter check. Suggested sentences (not applied):
  - M93: `absorption-hollow.txt:8` records `guard-mutation direction is missing for one or more errata`, exit 1. The missing-path clause in `round-62.md:25` was never true of that receipt.
  - Clock: the receipt's `date_utc` is `2026-10-23T20:57:43Z`; `20:53:36Z` does not appear in the file.
  - No-harm: `noharm-tip.txt` records `FAIL reg_gate`, `FAIL corpus-idx`, and `Battery exit code: 124`. The SCORECARD `:36` sentence is not a no-harm pass. (`LOG.md:2573` already covers the report.)
  - R-b: `LOG.md:2557`'s "complete list" omits `corpus/lessons/round-61-verifier-spotcheck.md`. The file is indexed at `corpus/README.md:108`.
- SentBounds baseline and helper-invocation receipts: defer. Say so on the next Next line; do not drop them.
