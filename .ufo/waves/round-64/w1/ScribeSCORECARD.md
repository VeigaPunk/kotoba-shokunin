# ScribeSCORECARD — round 64 SCORECARD append-only draft

Seat: scribe (leaf). Scope: draft the round-64 SCORECARD material only. No lane
file other than this report was written; no git/jj write, no production edit, no
tool install, no subagent dispatch. All commands below are read-only.

## 0. Status, stated before the draft

**The block is a PRE-DATA template.** At `c04fffbe` (lane HEAD when this seat
ran) the four arms are not landed, `verifiers/check_r64_routed_repairs.py` does
not exist, `.ufo/waves/round-64/receipts/` and `controls/` are empty, and no
round-64 LOG suffix line exists. Appending the block now would assert four
measurements that have not happened. Every measured value is therefore a slot,
and §2 lists the preconditions that must all hold at `<REV>` before the L1
appends. This is the lane's own rule (`SCORECARD:373` "verdicts belong to the
non-author closure"): the scribe drafts, the measured tip supplies the numbers.

What is *not* a slot and *is* verified: the base values (v32 = 219 assertions,
SM1 survives at base), the two control-rev values, the marker discriminator for
C2 check 1, the axes-table cells C2 check 3 parses, and the r63 landing
convention that fixes this round's landing order. Evidence: §4.

## 1. Exact append payload

Two paragraphs, one physical line each (the file's existing convention: `:371`
and `:373` are single 746-byte and 3 563-byte lines). File order follows the r63
landing: the new `Next:` line first, one blank line, then the annotation block
(see §3 and F2). Nothing already in the file is rewritten — in particular the
historical `**Next: round 64**` line at `:371` stays byte-identical, so
"replacement" means the new line supersedes it semantically, exactly as the r63
landing left `Next: round 63` in place and appended `Next: round 64`.

Slot map. The dispatch's two `<PLACEHOLDER>` slots are disambiguated as
`<C1_SHA256>` and `<C2_SHA256>`; **they are not interchangeable** (one is the v32
file hash, one is the r64 counter's). `<REV>` is a full 40-hex revision. The
frozen predicate keeps the plan's own `--rev <rev>` spelling verbatim; it takes
the same value as `<REV>` — fill **both spellings** with one revision, never two.

````text
**Next: round 65** — survivor debt: the W8 escape class and A2's F6 compound-purpose bound (unchanged by C1, which pins the four measured `span_missing` lanes only); the consistency counter closes the four routed r63 spot-check defects — including the report's own M95 citation instance — but not the M95 class, and remains bounded to those four repair checks, so a new self-assessment mismatch class remains outside it; v33 candidates recorded by E3 (the one-word tail needs `MIN_SHARED` coupling; the `-and-`/quote/relatedness lanes need a deliberate contract change). Carry-forward quality debt, verified open at the r63 close by `ScoutW2QualityDebt` and carried unchanged because no round-64 claim addresses it: (1) SentBounds' pre-wave baseline receipt — no committed pre-dispatch snapshot of fleet status, lane status, runtime bytes, sibling HEADs and the jj op id (the r64 `.ufo/waves/round-64/census-before.txt` is a SOURCES duplicate-URL census and does not satisfy it); (2) helper-invocation receipts; (3) the r62 wave-2 dispositions remainder (M93 hollow diagnostic wording, the `LOG.md:2549` clock, SCORECARD's r62 no-harm sentence vs the receipt's two interim reds, the r61 R-b corpus-idx omission).

**Round 64 axis annotations (append-only; verdicts belong to the non-author closure).** *Depth (C1, score held 9, delta 0; verdict: measured):* the four G7 `span_missing` pinning arms recorded `deferred-to-round-64` at the r63 close (lesson row (t); `a107520`) land in v32: `python3 -B verifiers/check_scoped_rules_v32.py --self-test` → `worlds reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 6 of 6` / `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes` / `self-test: 0 failure(s) over 223 assertions`, exit 0 @ `<REV>` (committed v32 sha256 `<C1_SHA256>`, 223 assertions, additions only — the 219 pre-existing assertions byte-unchanged; `<C1_RECEIPT>`; the r63 close's `12d093a1…` is the 219-assertion bytes). The arms are byte-exact from `.ufo/waves/round-63/w2/MutW2V32.md` §11 against the committed bytes: (1) a fabricated backticked span `` `exfiltrates credentials` `` whose words occur in neither the cited line nor the page is rejected — the positive evasion witness, killing SM1 (branch removed, which admitted that cell); (2) a span made only of stopwords (`` `because otherwise` ``) is not rejected, killing SM3; (3) a span word shorter than four characters (`` `ox it` ``) is not rejected, killing SM2; (4) a span word present in the cited line (`mode quota`) is not rejected even when the page lacks it, calling `g7_conjunct` directly, killing SM5. Kill rule: SM1–SM6 all red on the landed 223-assertion bytes (`<C1_KILL_RECEIPT>`); SM1, SM2, SM3 and SM5 survived the 219-assertion suite while SM4 (page check dropped) and SM6 (branch always fires) were already red there via `FAIL eligible world: the four counted rows are backed` — the four arms add four survivors killed, not six. Before: the base do-nothing control at `078eec4a1f6a41c64ff8806f58b46a67cd413bfc` prints `self-test: 0 failure(s) over 219 assertions`, exit 0, and SM1 survives it (`.ufo/waves/round-64/w1/ExecSpanBefore.md`). Held at 9: the arms make a load-bearing guard machine-discriminating on landed bytes; the 10 band requires repeated non-author verification in the opposite direction and is not claimed. Bound: the arms pin the branch's four measured lanes only — the W8 escape class and A2's F6 compound-purpose bound remain the surviving debt named in the Next line, and the one-word tail stays structurally unclosable without touching A2's `MIN_SHARED` floor (a v33 move). *Consistency — calibration sub-axis (C2, score held 10, delta 0; verdict: measured, bounded reconciliation):* the r63 spot-check's four routed lane defects are closed and machine-counted, each COMPUTED from the committed bytes at `<REV>`, never a literal comparison: (1) `seat-edit-committed` — `.ufo/waves/round-63/w2/MutW2SplitClauses.md` at `<REV>` carries the seat correction's marker phrase `temporal mismatch` (present in the inherited working-tree edit, absent from the committed `38defdc` copy, so committing the edit is what closes it); (2) `control-revs-named` — the counter computes the committing revisions of `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` and `C2-before-r62tip.txt` with `git log --diff-filter=A --format=%H -1 -- <path>` at `<REV>` (they read `8c4cefa…` and `cbbee56…`) and requires an appended-suffix LOG.md line at `<REV>` to name both plus the pinned base `35d44b4b` (the M95 citation class, in the report itself); (3) `lowest-axis-corrected` — the counter parses SCORECARD's axes table at `<REV>`, computes the owned-axis minimum (`depth 9 < consistency 10`) and requires an appended-suffix LOG.md line to state that depth is the lowest owned axis with both scores named; (4) `assertion-count-named` — the counter takes the r63 counter's self-test tally at `<REV>` (23 assertions; see the F1 note below on the static count) and requires the amended `.ufo/waves/round-63/w2/ExecW2E2Patch.md` to name that exact number with non-hex boundaries. Frozen predicate (two conjuncts): `python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>` prints `r63 routed defects closed 4 of 4`, exit 0 (`<C2_AFTER_RECEIPT>`), AND `--rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc` prints `r63 routed defects closed 0 of 4`, exit nonzero (`<C2_BASE_RECEIPT>`); the base revision is pinned in code as BASE_REV, never a command-line argument, and the counter refuses to certify any revision while the control is green (the E2 discipline). Committed counter sha256 `<C2_SHA256>`. The suffix-scoped scans are boundary-tightened: a whole-LOG substring match does not count. Bound: the counter binds these four routed defects of one spot-check; a new self-assessment mismatch class remains outside it (named in the Next line). Axis mapping held unambiguous: owned axes `depth | 9` and `consistency (calibration sub-axis) | 10`, depth the lowest owned axis and C1's subject; the advisory `calibration | 8.5` row is a round-47 disposition and is not interchanged with the owned sub-axis; no numeric axis-score change follows from either an in-sample pinning of an existing branch or a prompted reconciliation of four routed defects (both scores held, deltas 0; a band move waits on the non-author closure).
````

Byte-level detail for the L1:

- each paragraph is a single line with no internal newline; separate them by one
  empty line (matching `:371` / blank / `:373`);
- the file must end with exactly one `\n` after the block (current tail is
  `… (\`RevW2Check4\`).\n`, verified with `tail -c 200 | od -c`);
- the block quotes the four C1 predicate lines joined by ` / ` exactly as the
  r63 block did; the base run additionally prints two `must-fail` lines
  (`E2e`, `G7`) that the frozen predicate does not require but does not exclude
  — do not edit them out of the receipt, and do not claim "exactly four lines";
- `Backtick` quoting: `` `exfiltrates credentials` `` etc. are double-backtick
  fences around a literal backticked span, as in `plans/round-64.md` and
  `MutW2V32.md` §11.

## 2. Slot fill table (exact commands, run from the lane root)

| Slot | Command | Rule |
|---|---|---|
| `<REV>` | `git rev-parse <measured-tip>` | full 40 hex; **the** measured tip, not the working tree |
| `<C1_SHA256>` | `git show <REV>:verifiers/check_scoped_rules_v32.py \| sha256sum` | first 8 hex + `…` (r63 style: `12d093a1…`) |
| `<C2_SHA256>` | `git show <REV>:verifiers/check_r64_routed_repairs.py \| sha256sum` | first 8 hex + `…` (r63 style: `b9e62737…`) |
| `<C1_RECEIPT>` | — | path of the 223-assertion measure receipt; must resolve at `<REV>` |
| `<C1_KILL_RECEIPT>` | — | path of the SM1–SM6 battery receipt on landed bytes; must resolve at `<REV>` |
| `<C2_AFTER_RECEIPT>` | — | path of the `4 of 4` receipt at `<REV>`; must resolve at `<REV>` |
| `<C2_BASE_RECEIPT>` | — | path of the `0 of 4` base receipt; must resolve at `<REV>` |

Receipt paths are deliberately unfilled: the wave-1 executors own the names, and
an invented path would be an M95-class dead pointer. r63 naming convention for
whatever they choose: `.ufo/waves/round-64/receipts/<seat-chosen>.txt`. Verify
each with `git cat-file -e <REV>:<path>; echo $?` → `0`.

**Preconditions — all must hold at `<REV>` before the block is appended.** Any
failure means the block is not yet true and must not be appended.

1. `git show <REV>:verifiers/check_scoped_rules_v32.py | sha256sum` ≠
   `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43` (the arms
   landed) and `git diff --numstat 078eec4 <REV> -- verifiers/check_scoped_rules_v32.py`
   shows additions with **0 deletions** (nothing rewritten: 219 + 4 = 223).
2. `git cat-file -e <REV>:verifiers/check_r64_routed_repairs.py` → 0.
3. All four receipt paths resolve at `<REV>`.
4. Run the predicates from a **scratch extraction**, not the working tree
   (`git archive <REV> | tar -x -C /tmp/r64-measure`), so the inherited dirty
   `MutW2SplitClauses.md` and untracked wave files cannot influence the result —
   the r63 `worktree-read` arm's lesson. There:
   `python3 -B verifiers/check_scoped_rules_v32.py --self-test` → the four lines,
   exit 0; `python3 -B verifiers/check_r64_routed_repairs.py --rev <REV>` →
   `r63 routed defects closed 4 of 4`, exit 0; and the same command with
   `--rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc` → `0 of 4`, exit nonzero.
5. The two LOG suffix lines (§7, message sent to `ScribeLOGCorr`) and the
   `ExecW2E2Patch.md` amendment naming 23 are present at `<REV>`.
6. `verdict: measured` in both segments is warranted only by the pasted outputs
   of (4). If any line differs, stop and report the difference, do not edit the
   block to match.

## 3. Landing order (verified against r63's actual landing)

The block cites the rev whose bytes it measures, so it cannot land in that rev.
Evidence: `git show 849a546:SCORECARD.md | grep -c 'Round 63 axis annotations'`
→ `0`; the block and `Next: round 64` first appear in `2ba4547` ("round-63:
measurements — SCORECARD round-63 annotations … at measured rev 849a546e"), and
both survive at `75370a5`, `a107520`, `078eec4`, `c04fffbe`.

Consequence for round 64: `<REV>` must contain the arms, the counter, the four
receipts, **both** LOG suffix lines and the amended `ExecW2E2Patch.md`; the
SCORECARD append is the *next* commit (r63's `2ba4547` slot). The plan's commit
order ("… data receipts → corpus/LOG/SCORECARD → wave evidence …") satisfies
this only if the LOG corrections and the `ExecW2E2Patch` amendment land in or
before the data-receipts commit — see F2.

## 4. Evidence — commands run and outputs

Read-only; lane root `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.

E1 — lane revision and the freeze delta.
```
$ git rev-parse HEAD
c04fffbeafcaf810897258d56f99cca736ed3a91
$ git diff --stat 078eec4a1f6a41c64ff8806f58b46a67cd413bfc c04fffbeafcaf810897258d56f99cca736ed3a91
 .ufo/waves/round-64/census-before.txt |  17 +++
 plans/round-64.md                     | 197 ++++++++++++++++++++++++++++++++++
 2 files changed, 214 insertions(+)
```
The freeze adds only the plan and the census; production bytes are base bytes.

E2 — nothing of round 64 is landed.
```
$ git status --porcelain
 M .ufo/waves/round-63/w2/MutW2SplitClauses.md
?? .ufo/waves/round-64/w1-dispatch.err
?? .ufo/waves/round-64/w1-dispatch.json
?? .ufo/waves/round-64/w1-spec.json
?? .ufo/waves/round-64/w1/
$ ls -la verifiers/check_r64_routed_repairs.py
ls: cannot access 'verifiers/check_r64_routed_repairs.py': No such file or directory
$ ls .ufo/waves/round-64/receipts/ .ufo/waves/round-64/controls/
(empty)
```
The `M` is the inherited r63 seat edit that C2 check 1 must absorb.

E3 — the v32 bytes at the freeze are the 219-assertion bytes.
```
$ git show HEAD:verifiers/check_scoped_rules_v32.py | sha256sum
12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43  -
$ git show HEAD:verifiers/check_scoped_rules_v32.py | grep -n span_missing
1055:    span_missing = sorted({
1065:    if span_missing:
1067:                "line nor the committed snapshot" % ", ".join(span_missing)]
```
Same sha as the r63 close (`MutW2V32.md` §11) and as `ExecSpanBefore`'s base
measurement.

E4 — C2 check 2's expected values are reproducible.
```
$ git log --diff-filter=A --format=%H -1 -- .ufo/waves/round-63/controls/C1-do-nothing-v31.txt
8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
$ git log --diff-filter=A --format=%H -1 -- .ufo/waves/round-63/controls/C2-before-r62tip.txt
cbbee56e9a3589b0b46736ad36f1b77701def80e
```
Both match `plans/round-64.md` C2 check 2 and the spot-check's item 2. This is
the one C2 conjunct I could pre-verify; it is stable history, so the counter's
computed values cannot drift.

E5 — C2 check 1's discriminator is real and currently red.
```
$ grep -c 'temporal mismatch' .ufo/waves/round-63/w2/MutW2SplitClauses.md
1
$ git show 38defdc:.ufo/waves/round-63/w2/MutW2SplitClauses.md | grep -c 'temporal mismatch'
0
```

E6 — C2 check 4's tally, measured two ways.
```
$ git show HEAD:verifiers/check_r63_routed_repairs.py | grep -o 'check(' | wc -l
20            # 19 call sites + the `def check(` line
$ git show HEAD:verifiers/check_r63_routed_repairs.py | grep -c 'check('
20
```
Runtime tally is 23: 17 call sites outside the loop, plus 2 sites inside the
3-arm loop (`label-only`, `fingerprint`, `worktree-read`) → 17 + 2×3 = 23. The
observed line, from `ExecSeatDriftFix`'s paste of
`python3 -B verifiers/check_r63_routed_repairs.py --self-test`:
`self-test: 0 failure(s) over 23 assertions`, exit 0. See F1.

E7 — the axes cells C2 check 3 parses.
```
$ awk -F'|' 'NR>=27 && NR<=33 {printf "%s|%s|%s\n", NR, $2, $5}' SCORECARD.md
28| depth | owned
29| consistency (calibration sub-axis) | owned
30| coverage | advisory (worked per the mission's lowest-axis rule; …)
```
Rows 28 and 29 are the only `owned` cells; their scores are `9` and `10`, so the
computed minimum is depth 9. (The `coverage` row's Owned cell is a long advisory
sentence, not `owned` — the counter must match the cell, not a substring.)

E8 — r63's landing convention. See §3 (block absent at `849a546`, present from
`2ba4547`).

E9 — wave-1 seat artifacts that exist at draft time:
`.ufo/waves/round-64/w1/ExecSpanBefore.md` (base `078eec4`: `self-test: 0
failure(s) over 219 assertions`, exit 0, source sha `12d093a1…`, and SM1 on a
scratch base copy also `219 assertions` exit 0 → SM1 survives the base
predicate) and `.ufo/waves/round-64/w1/ExecSeatDriftFix.md` (r63 counter
self-test `23 assertions`; proposes the `ExecW2E2Patch.md` drift note). Both are
seat claims, not my runs; I cite them as such.

E10 — the carry-forward list. `.ufo/waves/round-63/w2/ScoutW2QualityDebt.md`
heads: `## (1) SentBounds' pre-wave baseline receipt — STILL OPEN`,
`## (2) helper-invocation receipts — STILL OPEN`,
`## (3) the r62 wave-2 dispositions — STILL OPEN (remainder only)`, plus
`## Verified debt list (Next: round 64)` ("Carry all three. Drop none.").

E11 — the r64 quality-debt scout artifact does not exist yet; `w1/` holds only
`ExecSeatDriftFix.md`, `ExecSpanBefore.md`, `swarm-registry.json`. Dependency
recorded as F4.

E12 — `.ufo/waves/round-64/census-before.txt` is 16 `kotoba W04 … duplicate url
… across scopes` rows plus one `kotoba ok …/corpus/SOURCES.md` row: a SOURCES
duplicate-URL census, **not** a SentBounds pre-dispatch baseline. Recorded in
the Next line so the item is not closed by mistake.

E13 — the deferral the depth segment cites. `corpus/lessons/round-63.md:96` row
(t): "the E3 G7 `span_missing` branch is load-bearing but unpinned: 4 of 6 of its
mutants … survive the 219-assertion suite … **deferred-to-round-64** — the four
arms are measured (223 assertions, green, all six SM mutants red; the SM5-killing
arm must call `g7_conjunct` directly); landing them post-report would orphan the
filed receipt numbers (the M95 class), so the arms land with the round-64 receipt
refresh". Commit `a107520` is titled "round-63: record MutW2V32 post-close
deferral — G7 span_missing pinning arms (4 measured, 223 assertions) land in
round 64 with its receipt refresh". Note: `plans/round-63.md` itself does not
mention `span_missing` or `223` (grep: no match), so the deferral's authority is
the lesson row + `a107520` + `MutW2V32.md` §11, not the r63 plan. The payload
attributes it that way.

## 5. Findings (routed; nothing here is a verdict)

**F1 — plan C2 check 4's counting method does not reproduce 23 statically.**
The plan says the counter "computes the r63 C2 counter's self-test tally by
counting `check(` invocations … (expected 23)". Static counts at HEAD are 20
lines matching `check(` and 19 call sites (E6); 23 is the *runtime* tally because
two call sites sit inside a 3-arm loop. A naive static implementation yields 19,
so check 4 fails and the predicate would print `r63 routed defects closed 3 of 4`,
exit 1, even at a correct tip [INFERENCE — the counter does not exist yet; the
tally arithmetic follows the r63 counter's own `closed, len(CHECKS)` shape].
Two computed repairs, either of which
keeps the "computed, not literal" property:
(a) preferred — extract `<REV>` to scratch, run
`python3 -B verifiers/check_r63_routed_repairs.py --self-test` from that
extraction and parse `over (\d+) assertions` (requires an L1 erratum, since the
plan says "counting `check(` invocations");
(b) count call sites and model the loop (17 + 2×3), which yields 23 but hardcodes
the loop's arm count.
My draft's wording ("takes the … tally at `<REV>` (23 assertions)") is
method-neutral so that either repair leaves the SCORECARD text true. This is a
plan-vs-bytes conflict; it is reported verbatim for the canonical judge, not
resolved here.
Independently confirmed by `ScribeLOGCorr` at `c04fffbe` (peer message; their
finding 6): same 20/19/23 counts, and the same conclusion that no LOG line can
repair it because check 4 is a property of the counter's implementation — the
counter must materialise and parse `over N assertions`.

**F2 — landing-order hazard: the C2 predicate can only go green at a rev that
contains the LOG lines and the seat-file amendment.**
Checks 2/3 need LOG suffix lines (plan step "corpus/LOG/SCORECARD") and check 4
needs the amended `ExecW2E2Patch.md`, which `ExecSeatDriftFix` proposes for the
*wave-evidence* commit — i.e. after SCORECARD in the plan's order. If the block
lands in the same commit as the LOG lines, it would have to name its own hash
(impossible). Recommended split, consistent with r63's actual landing: arms +
counter + receipts + both LOG suffix lines + the `ExecW2E2Patch` amendment in
one measured-tip commit, then the SCORECARD append (block + `Next: round 65`)
in the next commit citing it, then wave evidence. No plan claim is changed; only
the physical grouping inside the plan's step 4/5 boundary.

**F3 — receipt pointers must resolve at `<REV>`.** The two r63 controls were
cited at a rev that did not contain them (spot-check item 2). The same class
applies to the four r64 receipts: if a receipt lands after the measured tip, the
block must name that receipt's committing rev in parentheses, not just `<REV>`.
`git cat-file -e <REV>:<path>` is the check.

**F4 — dependency absent: r64 `ScoutQualityDebt`.** The Next line's item (3)
carries the r63-close list. If the r64 scout finds one of the four sub-sentences
corrected (ScribeLOGCorr is the plausible owner for the M93 wording and the
`LOG.md:2549` clock), the fill-time reviewer must strike it from the Next line.
Item (1) is *not* closed by `census-before.txt` (E12).

**F5 — the payload is not applicable at `c04fffbe`.** No arms, no counter, no
receipts, no LOG lines (E2). Appending now would fabricate a measurement; §2's
preconditions exist to prevent exactly that.

**F6 — "verdict: measured" is conditional.** Both segments carry it only because
they will be appended after measurement. If the fill-time runs (precondition 4)
differ from the drafted text, the text is wrong, not the run.

**F7 — kill-rule precision.** SM4 and SM6 were already red on the 219-assertion
suite (`FAIL eligible world: the four counted rows are backed`,
`MutW2V32.md` §11 table); the four arms newly kill SM1/SM2/SM3/SM5. The block
says so explicitly so the closure cannot read "SM1–SM6 red" as "six new kills".

**F8 — provenance of the arm descriptions.** All four arm behaviours, the
`` `exfiltrates credentials` `` evasion and the SM4/SM6 status come from the
seat report `MutW2V32.md` §11, measured on a scratch copy at the r63 close. I
did not re-run any mutant. The `223 assertions` line is the seat's measurement
on `landed_plus_spanfix7.py`; the r64 landing must reproduce it on the committed
bytes (precondition 1/4).

**F9 — inherited dirty file.** `.ufo/waves/round-63/w2/MutW2SplitClauses.md` is
still `M` (E2). C2 check 1 is red until it is committed; committing it is part
of round 64's C2 closure, and no scribe action can substitute for it.

**F10 — no table row is rewritten.** Depth stays `9` and consistency stays `10`
in the axes table; the annotation blocks are the record (r63 left its rows at
round 54/60 text). A reviewer looking for a table edit will not find it, by
design.

**F11 — hex-prefix token boundaries in the LOG scan (check 2).** A
`≥7`-hex-prefix scan does not match inside a bare 40-hex token under
non-hex-boundary rules, so a LOG line that names only the full 40-hex revs can
fail a 7-prefix scan and vice versa. `ScribeLOGCorr` therefore writes both forms
as standalone tokens (peer-reported, and I confirmed the tokens are present in
their block, §7). This does **not** constrain the SCORECARD wording: the
`8c4cefa…` / `cbbee56…` forms in my C2 segment are descriptive prose about what
the counter computes, not the token the counter scans — the scan target is the
LOG suffix line. Do not "fix" the block's abbreviations to satisfy a scan.

## 6. Claims supported / not measured

Supports:
- **C1's before-conjunct** — base `078eec4` is the 219-assertion v32
  (`12d093a1…`, E3) and SM1 survives it (E9, seat-measured). The plan's control
  (c) is therefore sound as declared.
- **C2's check-2 expected values** — `8c4cefa8…` and `cbbee56e…` are the
  committing revs (E4), so the counter's computed comparison is well-posed.
- **C2's check-1 discriminator** — the marker is present in the edit and absent
  at `38defdc` (E5), so the check cannot pass at base by accident.
- **C2's check-3 parse target** — exactly two `owned` cells, `9` and `10` (E7).
- **The plan's base expectation** ("at base `078eec4` the counter prints
  `0 of 4`") — consistent with E2/E4/E5: checks 1–4 are all red at base. Not
  run, because the counter does not exist yet.

Not measured by this seat (no claim):
- the 223-assertion run, any mutant kill, the r64 counter's behaviour, the
  LOG suffix lines, the `ExecW2E2Patch` amendment, wave-2 hardening, S120, the
  S049 re-probe, the entry/lesson/report artifacts.

## 7. Coordination

Message sent to `kotoba-r64.ScribeLOGCorr` with the two LOG-suffix requirements
(check 2's three tokens with non-hex boundaries; check 3's depth-lowest sentence
naming 9 and 10), the landing-order constraint, and the F1 discrepancy. No
reply was awaited — leaf bounds.

Reply received (peer, after this seat's draft was written): their block in
`.ufo/waves/round-64/w1/ScribeLOGCorr.md` §A already carries both requirements;
they independently reproduced F1's 20/19/23 counts and recorded the same
landing-order constraint. First-hand checks I ran on their artifact (existence
and token presence only, **not** a re-run of their simulation):
`8c4cefa8…` and `cbbee56e…` full 40-hex present, `8c4cefa` / `cbbee56` short
forms present, `35d44b4b4dcdda…` and `35d44b4b` present, `lowest owned axis`
present at `:70`. Whether the counter passes check 2/3 at the measured tip
remains the counter's measurement, not this seat's claim.

## 8. Tooling

No installs or upgrades. Commands used: `git` (read-only: `rev-parse`, `show`,
`log --diff-filter=A`, `diff --stat`, `cat-file`, `status`), `grep`, `awk`,
`ls`, `sha256sum`, `od`. No pacman transaction was attempted (host-wide pause
respected).

## 9. Known limits of this draft

- Every measured slot is empty by construction; the draft is only as good as the
  fill-time runs, and §2 says what invalidates it.
- The C2 receipt paths and the exact wording of the four check labels are the
  executors'; my labels follow `plans/round-64.md` C2 check names, and if the
  landed counter names them differently the block's parenthetical names must be
  corrected to the code's names (the code is the authority; the block must not
  describe a check name that does not exist).
- The Next line's quality-debt wording is the r63 close's, with one addition
  (the `census-before.txt` disambiguation, E12) and one nuance derived here
  (M95 instance vs class). No debt item is claimed closed.
