# ScribeLOGCorr

role: Leaf scribe; appends-only LOG.md drafting for round 64 (C2 checks 2 and 3, C1/C2 entry skeleton).
item: Draft (1) the round-63 corrections block and (2) the `## 2026-10-24 — Round 64` entry skeleton,
delivered as exact text inside this report; nothing outside this report was written.

## Findings

1. **Check 2 is measurably true, and the cited rev is measurably empty.** I re-derived the two
   committing revisions read-only at the lane tip `c04fffbeafcaf810897258d56f99cca736ed3a91`:
   `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` → `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8`;
   `.ufo/waves/round-63/controls/C2-before-r62tip.txt` → `cbbee56e9a3589b0b46736ad36f1b77701def80e`.
   `git ls-tree -r --name-only 35d44b4b -- .ufo/waves/round-63/controls/` prints **nothing**, and the
   same command at `8c4cefa` prints only the C1 control — so the round-63 report's `@ 35d44b4b`
   citation names a rev that does not contain either file (the M95 class, in the report itself).
   Each control pins base `35d44b4b4dcdda234b5dbff7af37e432fec55f05` internally
   (`C1-do-nothing-v31.txt:2` `at: 35d44b4b…`; `C2-before-r62tip.txt:1` `… not a tracked blob at 35d44b4b…`).
   Supports **C2 check 2**; falsifies nothing. `[INFERENCE]` the counter's own computation will print
   the same two revs — its command is the same `git log --diff-filter=A --format=%H -1`.
2. **Check 3's numbers are the SCORECARD table's numbers.** `SCORECARD.md`'s axes table reads
   `| depth | 9 |` (owned) and `| consistency (calibration sub-axis) | 10 |` (owned); the five
   non-owned rows are coverage 8.5, operability 8.5, freshness 8, calibration 8.5 and adjacency 8.0,
   each marked advisory / non-owned. The owned minimum is therefore depth 9, and "depth is the lowest
   owned axis, 9 below consistency 10" is literal-true at this tip.
   Supports **C2 check 3**.
3. **The append point is clean.** `git diff --stat 078eec4 -- LOG.md` is empty and `LOG.md` is 2,588
   lines, ending `…receipt refresh.\n` (the round-63 entry's last line). There is no
   `^## 2026-10-24` heading yet. Appending at EOF therefore (a) keeps `LOG.md` at base a byte-prefix
   of `LOG.md` at the measured rev (the append-only arm of the r63 E2 shape) and (b) puts both
   correction lines inside any suffix scan based on `BASE_REV = 078eec4…`.
4. **Token-shape hazard for check 2 (the only real risk in this draft).** The counter does not exist
   yet (`verifiers/check_r64_routed_repairs.py` absent at `c04fffbe`), so its matcher is unmeasured.
   A `(?<![0-9a-fA-F])<rev[:7]>(?![0-9a-fA-F])` scan will **not** match a bare 40-hex token (the
   character after the 7th hex is hex). The drafted line therefore carries, for each rev, the full
   40-hex token **and** standalone 7-hex and 8-hex tokens (plus the full 40-hex and literal
   `35d44b4b` for the base), which satisfies a 7-prefix, an 8-prefix and a full-rev matcher alike —
   verified by simulation over the substituted line (all three true). Recommended contract for the
   counter, stated once: scan per line, `_tok_re(rev[:7])` or a `≥7 hex, startswith(rev)` token match,
   suffix-scoped by the `LOG@BASE_REV` byte prefix.
5. **Two closure paths are outside this block by design.** The r63 spot-check's defect 1 (the
   uncommitted seat edit) is closed by the round-64 commit of
   `.ufo/waves/round-63/w2/MutW2SplitClauses.md` (inherited-state bullet, below), and defect 4 (the
   `21` vs `23` assertion drift) is closed by amending `.ufo/waves/round-63/w2/ExecW2E2Patch.md` — the
   counter's check 4 reads the tally by materialising the r63 counter and running its `--self-test`
   (spec: `over N assertions`, expect 23), so **no LOG line is required for check 4**. The block below
   still records both closures in one bullet so the round-63 record is not left half-corrected.
6. **Check 4's tally is runtime, not static — a counter that follows the plan's literal parenthetical false-fails.** Measured at `c04fffbe` on `verifiers/check_r63_routed_repairs.py`: 20 lines match `check(`, 19 call sites outside a definition line, while `python3 -B verifiers/check_r63_routed_repairs.py --self-test` prints `self-test: 0 failure(s) over 23 assertions` (17 outside the three-arm loops + 2 sites × 3 arms, per `ScribeSCORECARD`, whose two `--diff-filter=A` lookups also reproduced my finding 1). An r64 counter that implements plan C2 check 4's phrase "counting `check(` invocations … (expected 23)" statically computes 19 or 20 and can never certify — it must materialise the counter and parse `over N assertions` from its run, as the seat spec (`ExecR64Counter`) states. This is a plan-wording/implementation gap, not a LOG defect: **no LOG line can fix it**, and the block below deliberately does not try.
7. **Landing order is load-bearing for C2 (append this block before the SCORECARD annotation commit).** Checks 2 and 3 scan the appended LOG suffix at the measured `<REV>` that the round-64 SCORECARD annotation cites; if the SCORECARD axis annotation lands naming a rev that predates this block, both checks read `0 of 4` at that rev and the annotation's cited measurement is falsified. The r63 pattern is the model (corrections block landed in `2ba4547`, annotation citing measured tip `849a546`); here the LOG suffix and the amended seat file must both be in the tree at `<C2_MEASURED_REV>` before the annotation names it.
8. **No gate ran.** Everything here is read-only `git log`/`git ls-tree`/`git rev-parse`/`grep`/`wc`
   over committed bytes and the worktree; no counter, battery or checklist was executed, so no line
   below may be cited as a measured gate result. No tool was installed or upgraded. I did not run any
   `git`/`jj` write and did not touch the lane index, jj state, the fleet repo or sibling lanes.

## Artifacts

### A. Exact text to append to `LOG.md` (nothing else)

Application: append the block below verbatim at EOF of
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/LOG.md`. Its **first byte is a newline** (producing one
blank line after `…receipt refresh.`), and its last line ends with a newline. Substitution is the only
permitted edit: every `<UPPER_SNAKE>` token is a placeholder; `<rev>` inside the frozen predicates is
the **plan's own metavariable**, copied verbatim from `plans/round-64.md`, not a substitution token —
leave it.

````markdown

### Round-63 corrections (appended in round 64; the r63 verifier spot-check's routed defects 2 and 3)

- **Defect 2 — the controls' citation rev (the M95 class, in the report itself).** The round-63 entry cites both controls "@ `35d44b4b`" (`controls/C1-do-nothing-v31.txt` @ `35d44b4b`; `controls/C2-before-r62tip.txt` at `r62 routed defects closed 0 of 5`, exit 1 @ `35d44b4b`), but that is the rev the controls were run *against*, not the rev that contains them: at `<C2_MEASURED_REV>` the counter's own command, `git log --diff-filter=A --format=%H -1` on each control path, computes `C1-do-nothing-v31.txt` committed at `<C1_CTRL_COMMIT_FULL>` (7-hex `<C1_CTRL_COMMIT_7>`, 8-hex `<C1_CTRL_COMMIT_8>`) and `C2-before-r62tip.txt` at `<C2_CTRL_COMMIT_FULL>` (7-hex `<C2_CTRL_COMMIT_7>`, 8-hex `<C2_CTRL_COMMIT_8>`), while `git ls-tree -r 35d44b4b4dcdda234b5dbff7af37e432fec55f05 -- .ufo/waves/round-63/controls/` prints no entry — the report's `@ 35d44b4b` citation named a rev that does not contain the files. Each control pins base `35d44b4b`/`35d44b4b4dcdda234b5dbff7af37e432fec55f05` internally, so the repaired citation is committing rev plus pinned base. The committed report text is preserved as committed; this line is the correction.
- **Defect 3 — the lowest-axis parenthetical.** The round-63 report's claim line `at least one on the lowest owned axis — calibration/consistency` names the wrong axis. `SCORECARD.md`'s axes table scores depth `9` and consistency (calibration sub-axis) `10`, both owned, so depth is the lowest owned axis, 9 below consistency 10; the lowest-axis rule is satisfied because C1 targets depth, not because consistency is lowest. The committed report text is preserved; this line is the correction.
- **Defects 1 and 4 — closed outside this block (recorded, not re-argued).** Defect 1, the uncommitted seat edit `.ufo/waves/round-63/w2/MutW2SplitClauses.md` (`<INHERITED_DIFFSTAT>` vs its `38defdc` copy), is committed under this round as `<INHERITED_COMMIT>` with the seat correction intact (the committed blob carries the marker `temporal mismatch`, absent from `38defdc`; `<C2_CHECK1_VERDICT>`). Defect 4, the `21`-vs-`23` assertion drift in `ExecW2E2Patch`'s table, is closed by amending that seat file to the counter's computed tally `<R63_COUNTER_ASSERTIONS>` (`<C2_CHECK4_VERDICT>`); the r63 C2 counter's self-test is the authority, not the seat's count.

## 2026-10-24 — Round 64 (hyaku run 5, attempt 1): C1 depth G7 `span_missing` pinning arms (219→223); C2 calibration r63 routed repairs (4 of 4)

- **Inherited state.** Base tip `<BASE_TIP>` (`<BASE_SUBJECT>`); the plan freeze is `<PLAN_FREEZE>`. One lane file was modified at base: `.ufo/waves/round-63/w2/MutW2SplitClauses.md` (`<INHERITED_DIFFSTAT>` vs its committed copy at `<SPLIT_COMMITTED_REV>`), which is the r63 verifier spot-check's routed defect 1 (a dirty evidence file at closure). It is committed under this round as `<INHERITED_COMMIT>` with the seat correction intact — the committed blob carries the marker phrase `temporal mismatch` that the `38defdc` copy lacks, so C2's check 1 reads it from committed bytes at `<C2_MEASURED_REV>` rather than from the worktree (`<C2_CHECK1_VERDICT>`). Nothing reverted, nothing discarded, nothing silently dropped.
- **C1 — depth (the G7 `span_missing` branch pinned; four arms land; score `<C1_SCORE>`).** Frozen predicate (declared before data in `plans/round-64.md` § C1 at `<PLAN_FREEZE>`; `<rev>` is the plan's metavariable, not a substitution token): `python3 -B verifiers/check_scoped_rules_v32.py --self-test` prints all four lines —

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
```

— and exits 0. Before: at `<C1_BEFORE_REV>` the same command prints `self-test: 0 failure(s) over 219 assertions` with the four arms absent (`<C1_BEFORE_RECEIPT>`); control (a), the v31 do-nothing counter, prints `survivors closed 5 of 6` over 201 assertions and cannot reach the predicate's 223-assertion line (`<C1_V31_RECEIPT>`). After: `<C1_LANDED_REV>`, exit 0, committed v32 sha256 `<V32_SHA256>`, measured line `<C1_MEASURED_TAIL>` (`<C1_RECEIPT>`) — a tally other than the frozen 223 is a declared miss, recorded here and never rewritten into the predicate. The four arms are byte-exact as measured in `MutW2V32` §11 at `<C1_METHOD_REV>` (arm 1 fabricated backticked span, kills SM1; arm 2 stopword-only span, kills SM3; arm 3 sub-four-character span word, kills SM2; arm 4 cited-line-present span calling `g7_conjunct` directly, kills SM5), the SM1–SM6 battery prints all six red (`<SM_KILL_RECEIPT>`) with SM1's receipt printing `A2 G7: a backticked span whose words occur in neither the cited line nor the page`, and `judge()` verdicts on the committed rows stay `4 of 4` backed (`<JUDGE_RECEIPT>`). Bound (declared before data): the claim pins the four measured lanes of the `span_missing` branch; the W8 escape class and A2's F6 compound-purpose bound remain SCORECARD's round-64 Next-line debt.
- **C2 — calibration (consistency sub-axis): the r63 spot-check's four routed defects closed and machine-counted; score `<C2_SCORE>` (delta `<C2_DELTA>`).** Frozen predicate (two conjuncts; both must hold, declared before data at `<PLAN_FREEZE>`; `<rev>` is the plan's metavariable):

```
python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>
```

prints `r63 routed defects closed 4 of 4` and exits 0, AND

```
python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
```

prints `r63 routed defects closed 0 of 4` and exits nonzero. The second conjunct is the do-nothing control: its revision is pinned in code as `BASE_REV` and is never a command-line argument, and the counter refuses to certify any revision while the control is green (the E2 discipline of `check_r63_routed_repairs.py`). Before: `<C2_BEFORE_VERDICT>` at `078eec4`, exit `<C2_BEFORE_EXIT>` (`<C2_BEFORE_RECEIPT>`) — check 1 fails (the committed copy lacks the marker) and checks 2–4 fail (no round-64 correction lines or amended seat file exist at base). After: `<C2_MEASURED_REV>` → `r63 routed defects closed 4 of 4`, exit 0 (`<C2_RECEIPT>`); counter sha256 `<R64_COUNTER_SHA256>`, `--self-test` `<R64_SELFTEST_LINE>`. The four checks, each computed from the file's committed blob at `<C2_MEASURED_REV>` and never a literal comparison: `seat-edit-committed` (the `temporal mismatch` marker at `<C2_MEASURED_REV>`); `control-revs-named` (the two controls' committing revs `<C1_CTRL_COMMIT_7>`/`<C2_CTRL_COMMIT_7>` plus pinned base `35d44b4b` named on the appended correction line above, suffix-scoped and boundary-tightened); `lowest-axis-corrected` (SCORECARD's owned minimum computed as depth `9` below consistency `10`, named on its own appended correction line); `assertion-count-named` (the r63 counter's tally materialised at `<C2_MEASURED_REV>` — `<R63_COUNTER_ASSERTIONS>` assertions — named with non-hex boundaries in the amended `.ufo/waves/round-63/w2/ExecW2E2Patch.md`, `<C2_CHECK4_VERDICT>`). Bound: the counter binds these four routed defects of one spot-check; a new self-assessment mismatch class stays outside it.
- **Frontier.** SOURCES `<SOURCES_BEFORE>` → `<SOURCES_AFTER>` rows: S120 `<S120_CITATION>` (tier `<S120_TIER>` for `<S120_TIER_BASIS>`, status `<S120_STATUS>`; fetched `<S120_FETCH_STAMP>`, HTTP `<S120_HTTP>`, `<S120_BYTES>` B, sha256 `<S120_SHA256>`, snapshot `<S120_SNAPSHOT>`), opened by `<S120_SEAT>` and cited by the C1 knowledge entry `<C1_ENTRY_PATH>`. S049 live re-probe appended to the SOURCES search log: `Accept: text/markdown` → `<S049_MD_VERDICT>`; default request → `<S049_DEFAULT_VERDICT>`; measured `<S049_PROBE_STAMP>` (`<S049_RECEIPT>`); the errata stands and no row is rewritten. Census: before `<CENSUS_BEFORE_COUNTS>` exit `<CENSUS_BEFORE_EXIT>` (`<CENSUS_BEFORE_FILE>`) → after `<CENSUS_AFTER_COUNTS>` exit `<CENSUS_AFTER_EXIT>` (`<CENSUS_AFTER_FILE>`).
- **Receipts.** `.ufo/waves/round-64/receipts/`: `<C1_RECEIPT>` (the run printing `<C1_MEASURED_TAIL>` at `<C1_LANDED_REV>`), `<C1_BEFORE_RECEIPT>`, `<C1_V31_RECEIPT>`, `<SM_KILL_RECEIPT>`, `<C2_RECEIPT>`, `<C2_BEFORE_RECEIPT>`, `<CENSUS_AFTER_FILE>`; `.ufo/waves/round-64/controls/` carries `<C2_BEFORE_RECEIPT>` and the pre-data controls, committed before the data receipts (`<COMMIT_ORDER>`). The round-63 post-close deferral (`MutW2V32` §11 at `75370a5`) is closed here: the four measured arms land with the receipt refresh, so the refreshed numbers describe the committed bytes at the rev they name (the M95 class), never a revision that does not contain them.
- **Round shape.** Wave 1 `kotoba-r64-w1` (policy v1, `<W1_SPAWN>` spawn, band 32–64): `<W1_ROLE_COUNTS>`; §3 floor met inside (`<S3_FLOOR_LINE>`; planner seat held by the L1, planning data-walk `<PLANNING_WALK>`); seat reports committed `<W1_SEAT_COUNTS>` exit `<W1_SEAT_EXIT>`. Wave 2 `kotoba-r64-w2` (policy v1, `<W2_SPAWN>` spawn): `<W2_STATUS>`, `<W2_ROLE_COUNTS>`, attack roles `<W2_ATTACK_FRACTION>`; dead seats `<W2_DEAD>`; residual call `<RESIDUAL_CALL>`. Round total `<ROUND_SEATS>` seats.
- **No-harm.** `noharm-battery.sh --base <NOHARM_BASE_REV> --tip <R64_TIP>`: `<NOHARM_ARMS>` arms PASS (`<NOHARM_RECEIPT>`); gate registry `<GATE_REGISTRY_COUNT>` at the build tip (`<GATE_REGISTRY_RECEIPT>`); every still-red gate column-identical base→tip; the v31 control, the r63 routed-repairs counter and the skill checklist baseline unchanged (`<NOHARM_UNCHANGED_LINE>`).
````

### B. Substitution table (placeholder → value the L1 must take from measured receipts)

Defaults in the right column are **my read-only measurements at `c04fffbe`**, offered so the L1 can
sanity-check; every one of them must be replaced by ExecCalibVerify's / the relevant seat's measured
value, or by the run's own printed number. No placeholder may survive into `LOG.md`.

| Placeholder | Substitute | My read-only default |
|---|---|---|
| `<C1_CTRL_COMMIT_FULL>` | full 40-hex of the A-commit of `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` | `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8` |
| `<C1_CTRL_COMMIT_7>` / `<C1_CTRL_COMMIT_8>` | its 7-hex and 8-hex prefixes (both present so a 7-prefix or an 8-prefix matcher matches) | `8c4cefa` / `8c4cefa8` |
| `<C2_CTRL_COMMIT_FULL>` | full 40-hex of the A-commit of `.ufo/waves/round-63/controls/C2-before-r62tip.txt` | `cbbee56e9a3589b0b46736ad36f1b77701def80e` |
| `<C2_CTRL_COMMIT_7>` / `<C2_CTRL_COMMIT_8>` | its 7-hex and 8-hex prefixes | `cbbee56` / `cbbee56e` |
| `<C2_MEASURED_REV>` | the data rev the r64 counter is certified at (C2 after conjunct) | — (receipt) |
| `<C2_BEFORE_VERDICT>` | the base-arm headline as printed | `r63 routed defects closed 0 of 4` |
| `<C2_BEFORE_EXIT>` / `<C2_AFTER_EXIT>` | measured exit codes | `1` / `0` |
| `<C2_BEFORE_RECEIPT>` | `.ufo/waves/round-64/controls/C2-before-<BASE_REV7>.txt` as committed | — |
| `<C2_RECEIPT>` | `.ufo/waves/round-64/receipts/C2-routed-repairs-<REV7>.txt` as committed | — |
| `<C1_MEASURED_TAIL>` / `<C2_MEASURED_TAIL>` | the run's own last line as printed (`self-test: 0 failure(s) over N assertions`), never a predicted number | `223` expected; anything else is a declared miss |
| `<C2_SCORE>` / `<C2_DELTA>` | axis score after the verdict; delta | `10` / `0` (held — verdict belongs to the closure) |
| `<C2_CHECK1_VERDICT>` / `<C2_CHECK4_VERDICT>` | per-check verdict text at `<C2_MEASURED_REV>` | — |
| `<R64_COUNTER_SHA256>` / `<R64_SELFTEST_LINE>` | `sha256sum verifiers/check_r64_routed_repairs.py`; its `--self-test` summary line | — |
| `<R63_COUNTER_ASSERTIONS>` | the r63 counter's `--self-test` tally (`over N assertions`) | `23` (runtime; static `check(` sites are 19 call sites / 20 matching lines — never count them) |
| `<INHERITED_COMMIT>` | the round-64 commit that lands the `MutW2SplitClauses` edit | — |
| `<INHERITED_DIFFSTAT>` / `<SPLIT_COMMITTED_REV>` | worktree-vs-commit stat; the committed copy compared against | `111 ++/--, 82 insertions(+), 29 deletions(-)` / `38defdc58acc970810bc677da41f714f211713ac` |
| `<BASE_TIP>` / `<BASE_SUBJECT>` / `<PLAN_FREEZE>` | base rev + its subject; the plan-freeze commit | `078eec4a1f6a41c64ff8806f58b46a67cd413bfc` / `round-63 verifier spot-check …` / `c04fffbeafcaf810897258d56f99cca736ed3a91` |
| `<C1_BEFORE_REV>` / `<C1_LANDED_REV>` / `<C1_METHOD_REV>` | rev of the before-run, the landed bytes, the §11 measurement (`219`/`223` are literal in the frozen predicate and in the heading; a different printed tally is recorded via `<C1_MEASURED_TAIL>`) | `078eec4` (base) / — / `75370a52b6fbc34d39dcd9d93b784b47716d96bc` (`[INFERENCE]` from the plan's "at `75370a5`") |
| `<C1_RECEIPT>` / `<C1_BEFORE_RECEIPT>` / `<C1_V31_RECEIPT>` / `<SM_KILL_RECEIPT>` / `<JUDGE_RECEIPT>` | committed receipt paths | — |
| `<C1_SCORE>` / `<V32_SHA256>` | axis score (verdict-owned); `sha256sum` of the landed v32 | `9` (held) / — |
| `<C1_ENTRY_PATH>` | the round-64 knowledge entry that cites S120 | `corpus/knowledge/<ENTRY_NAME>.md` |
| `<SOURCES_BEFORE>` / `<SOURCES_AFTER>` | SOURCES row counts (`^| S[0-9]`) | `117` / `118` |
| `<S120_CITATION>`, `<S120_TIER>`, `<S120_TIER_BASIS>`, `<S120_STATUS>`, `<S120_FETCH_STAMP>`, `<S120_HTTP>`, `<S120_BYTES>`, `<S120_SHA256>`, `<S120_SNAPSHOT>`, `<S120_SEAT>` | the S120 row's and snapshot's measured cells | — |
| `<S049_MD_VERDICT>` / `<S049_DEFAULT_VERDICT>` / `<S049_PROBE_STAMP>` / `<S049_RECEIPT>` | the re-probe's per-profile results and receipt | — |
| `<CENSUS_BEFORE_COUNTS>` / `<CENSUS_BEFORE_EXIT>` / `<CENSUS_BEFORE_FILE>` / `<CENSUS_AFTER_COUNTS>` / `<CENSUS_AFTER_EXIT>` / `<CENSUS_AFTER_FILE>` | census before/after counts, exits, receipt paths | files exist (`census-before.txt`); counts unmeasured here |
| `<COMMIT_ORDER>` | the round's commit chain, controls before data | — |
| `<W1_SPAWN>`, `<W1_ROLE_COUNTS>`, `<W1_SEAT_COUNTS>`, `<W1_SEAT_EXIT>`, `<W2_SPAWN>`, `<W2_STATUS>`, `<W2_ROLE_COUNTS>`, `<W2_ATTACK_FRACTION>`, `<W2_DEAD>`, `<RESIDUAL_CALL>`, `<ROUND_SEATS>`, `<S3_FLOOR_LINE>`, `<PLANNING_WALK>` | wave spec / dispatch json counts and the registry's own census | spec: 32 (w1) |
| `<NOHARM_BASE_REV>` / `<R64_TIP>` / `<NOHARM_ARMS>` / `<NOHARM_RECEIPT>` / `<GATE_REGISTRY_COUNT>` / `<GATE_REGISTRY_RECEIPT>` / `<NOHARM_UNCHANGED_LINE>` | the battery's base, tip, PASS-arm count, receipt; registry count + receipt | r63 used `--base 35d44b4b`; r64's base is the round base `078eec4…` — L1 decides and states it |

### C. Check → line mapping (what each line must keep)

- **C2 check 2** is satisfied by the **Defect 2** bullet alone. It must keep, on that one physical
  line: both committing revs (full 40-hex **and** a standalone 7-hex token each), the pinned base
  `35d44b4b` (literal) and its full 40-hex, and the statement that the cited rev does not contain the
  files. Do not wrap the bullet across lines: the counter's scans are per-line.
- **C2 check 3** is satisfied by the **Defect 3** bullet alone. It must keep `depth is the lowest owned
  axis` verbatim plus the two standalone score tokens `9` and `10` with `consistency` on the same line.
- **C1's frozen predicate** in the entry must remain byte-identical to `plans/round-64.md` § C1 —
  four printed lines including `self-test: 0 failure(s) over 223 assertions`, exit 0. The plan's
  metavariable `<rev>` in C2's command is verbatim plan text; leave it.
- **C2's frozen predicate** must remain byte-identical to `plans/round-64.md` § C2, including the
  literal base rev in the control conjunct.
- **Landing order:** this block and the amended `ExecW2E2Patch.md` must both be in the tree at the
  rev the round-64 SCORECARD annotation cites; appending the block after that annotation is filed
  makes checks 2–4 read `0 of 4` at the cited rev (finding 7).

## Gates

None run. This seat's scope was drafting; the gate results that would make the placeholders true are
other seats' receipts (`ExecCalibVerify`, `ExecR64Counter`, `ExecC1Arms`, `ExecC2Receipts`,
`ExecGateRow`, `ExecNoHarmBase`) and the L1's own runs. No counter, battery, checklist, self-test or
`--stream` probe was executed; no `git`/`jj` write was made; no tool was installed or upgraded. The
only write is this file.

## Out of scope / dependencies recorded as findings

- `verifiers/check_r64_routed_repairs.py` did not exist at `c04fffbe` (`ls` → no such file), so
  finding 4's matcher question is a real dependency, not a style preference. The drafted correction
  line already carries the 7-hex and 8-hex prefixes as separate tokens, so no matcher shape below a
  full 40-hex comparison needs a rewording; if the counter demands an exact 40-hex token, the full
  tokens are present too.
- `.ufo/waves/round-64/receipts/` and `.ufo/waves/round-64/controls/` are present but empty; every
  receipt placeholder is therefore unmeasured by this seat.
- The round-63 report (fleet repo `.ufo/reports/round-63/kotoba.md`, lines 8, 31, 32) is outside the
  lane; I quoted it read-only and did not modify it. Its committed text stands under every correction
  above.
- SCORECARD's round-64 axis annotation, the SOURCES S120 row, the knowledge entry, the lesson (M96)
  and QUALITY Q60 are other seats' artifacts; this report asserts nothing about their content.
