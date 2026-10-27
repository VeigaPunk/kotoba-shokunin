# Kb79A04LogScoreDraft — seat report (round 79, w1)

Seat: Kb79A04LogScoreDraft (scribe). Leaf seat, no subagents, no background jobs, no scratch clone
(no item here needs a working tree: nothing was committed, patched or measured on a counter).

Task: draft the round's records — the `LOG.md` `## Round 79` entry, the `SCORECARD.md` round-79 axis
annotations plus a Capabilities-table row candidate, the four `SHONEN.md` evidence lines, and one
`corpus/QUALITY.md` candidate row for the mined mistake — with markers wherever this seat could not
observe a value, and with every path-like token either resolving from the lane root or explicitly
quoted/schematic in the form the governance citation gate excludes.

**Deliverable:** `.ufo/waves/round-79/build/Kb79A04LogScoreDraft.md` (343 lines; insertion-ready text
in four fenced blocks, a marker table, a measured token audit, and five findings for the L1). Nothing
in the lane tree was edited: no `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `corpus/QUALITY.md`,
`corpus/SOURCES.md`, `SKILL.md` or `PROVINCE.md` write; no git mutation anywhere.

## 1. What the draft contains, and what it refuses to invent

1. **`LOG.md` `## Round 79` entry** in the r73–r78 bullet style (Trigger / Action / Outcome / Limits /
   Pointer). Claim shape: C1 consistency = the lane's own tip battery at `6 of 6` in both invocation
   forms with the counter frozen; C2 depth = per-client `allowed-tools` semantics, sourced. Every
   commit id is `{{HASH_C1}}` / `{{HASH_C2}}` / `{{HASH_F2}}`; every measured value is a marker
   (`{{REV_FINAL}}`, `{{C2_N}}`, `{{C2_SCRIPT}}`, `{{C1_RECEIPT}}`, …). There is **no honest-stop
   framing for round 79** anywhere in the entry: rounds 77/78 appear only as the trigger, and the
   Limits bullet states what the battery does *not* prove rather than presenting a stop.
2. **`SCORECARD.md`**: one appended paragraph with two clauses — *Consistency (C1 calibration
   sub-axis, score held 10)* and *Depth (C2, sourced, score held 9)* — each carrying its counter, its
   frozen bytes, the base value pasted from a receipt that exists today, and a marker for the
   after-value; plus the Capabilities row, first cell `allowed-tools surfaces counter`, first-working
   round 79, explicitly headed **enter only after the L1's measurement** (SCORECARD.md:320: rows enter
   only through a round that demonstrates the capability running).
3. **`SHONEN.md`**: all four boxes stay `[~]` (no non-author verifier exists before closure). Boxes 2
   and 3 are drafted **unchanged** — round 79 ran no cold end-to-end task, so boxes 2 and 3 have no
   round-79 evidence, and box 3's round-8 `B1`/`B2` gap must not be upgraded. Boxes 1 and 4 get one
   appended clause each, conditional on C2 landing and on the sibling-census guard actually being
   re-run at the tip.
4. **`corpus/QUALITY.md` `Q74`**: criterion, applies-to, grounded-in, supersedes. Duplicate test
   written out against Q50, Q65 and Q36 — it **extends Q50 and Q65, supersedes neither**, and the new
   thing it requires is stated in one sentence: the battery run is a *landing step* and a closure
   without it is defective, which is exactly what Q50 cannot say (Q50 only bites when a report
   *states* a result; r76–r78 closed in silence). `grounded in` names M140, which is free today
   (`grep -rn 'M14[0-9]' corpus/` → no output, rc=1; highest existing id M139). The draft says
   explicitly: if the L1 reads that as already covered by Q50, write `no new criterion` and drop the
   row.

## 2. Evidence actually run (each line: command → output, exit status)

```
tail -60 LOG.md                                       → r73–r78 entries (style + the r78 "Round-end census and no-harm battery were not run" line)
python3 -B verifiers/verify_skill_checklist.py --json → exit 1
  FAIL governance.citation_resolves 1312 | LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not
  resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin; 10 quoted meta-finding(s), 3 schematic
  token(s) excluded, 2 recorded absence(s) excused, 4 recorded correction(s) excused
  (every other check PASS or N/A in that run)
cat .ufo/waves/round-79/receipts/tipbattery-base-dot.txt → last lines:
  fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 1 of 6 ; exit=1
  gate lines: check_gate_registry 1, check_assertion_floors 1, verify_skill_checklist 1,
  verify_corpus_integrity 1, verify_corpus_independent 1, check_correction_sweep 0
grep -rlE 'allowed-tools|allowed_tools' corpus/knowledge SKILL.md
  → corpus/knowledge/frontmatter-rule-authorities-round48.md,
    corpus/knowledge/chinese-vendor-skill-surfaces-round73.md ; rc=0
grep -c 'allowed-tools' SKILL.md                      → 0 ; rc=1
grep -rn 'M14[0-9]' corpus/                           → (no output) ; rc=1   [M140 free]
grep -n 'Q74' corpus/QUALITY.md                       → (no output) ; rc=1   [Q74 free]
ls verifiers/check_allowed_tools.py                   → No such file or directory ; rc=2
wc -l SKILL.md                                        → 590
git rev-parse b10bcbc6b00f8f56b202ccbadca311007b5b463c:verifiers/verify_skill_checklist.py
  → 6aab16849bd6d71ded8f3bcb3f95668f14f6a78f  (one of the two blobs pinned in check_tip_battery.py:131-133)
git cat-file -s/-p 8d44c063… / 6aab1684…              → 136,350 B / 2,804 lines (7 GOVERNANCE_CORRECTIONS
  mentions) vs 137,349 B / 2,821 lines (9 mentions)
test -e ../.ufo/reports/round-76/kotoba.md            → true     (the `../` root resolves into the fleet root)
test -e ../.ufo/reports/round-79/kotoba.md            → absent
python3 (citation_subjects + citation_resolve over the draft's fenced blocks) → §4 below
```

The three-shape quoting test (§4) and the per-block token audit were run in-process against
`verifiers/verify_skill_checklist.py` imported as a module — the gate's own predicate, not a
re-implementation. No counter was run: the C2 counter does not exist yet, and a C1 after-value needs a
commit that does not exist yet. So no claim data, no hashes beyond the frozen ones the receipts state,
and no verdicts appear in the draft.

## 3. Token discipline (the constraint that broke the base gate)

The base gate is red on exactly one subject, a fleet-report pointer written unquoted in the r76 entry
(`LOG.md:2818`). The draft therefore does not write a fleet pointer the lane cannot resolve. Measured
mechanism (three shapes run through `citation_subjects(..., exclude_quoted=True)`):

| line shape | subjects | quoted |
|---|---:|---:|
| `` `../.ufo/reports/round-79/kotoba.md` `` | 1 (dead) | 0 |
| `` "../.ufo/reports/round-79/kotoba.md" `` (no backticks) | 0 | 0 |
| `` "`../.ufo/reports/round-79/kotoba.md`" `` (quote outside the span, one line) | 0 | 1 |

So: a token is a subject only inside a backticked span, and the exclusion needs the double quote
**outside** the span, closed on the same line. The draft uses the third shape, which the gate counts
(`10 quoted meta-finding(s)` → 11), and records that an unbackticked path is invisible rather than
excused. The corrected live form `../.ufo/reports/round-79/kotoba.md` was considered and rejected with
a measured reason: `../` from the lane root is the fleet root (`.ufo/reports/round-76/kotoba.md` exists
there today), but the plan writes the fleet report last, so that token is dead at the lane tip C1 is
scored on.

## 4. Token audit result (per fenced block, so the draft's own commentary cannot pollute it)

| block | subjects | quoted exclusions | dead today |
|---|---:|---|---|
| LOG entry | 16 | `../.ufo/reports/round-79/kotoba.md` | C2 entry, C2 counter ×2, round lesson ×2 |
| SCORECARD annotations | 8 | — | C2 counter, C2 entry |
| Capabilities row | 2 | — | C2 counter |
| QUALITY row | 2 | — | round lesson |

Every dead token is **prospective**: it is created by F2 (counter), the C2 data commit (entry) or the
commit that carries the LOG entry (lesson) — all before the record that cites it. Nothing else in the
drafted text is dead, and the live-now tokens that carry the base evidence resolve. The draft also
warns that §2.1/§7 — this file's rationale prose — must never be pasted into a governance file: they
quote dead examples inside backticks.

## 5. Findings for the L1 (also in the draft §7; none of them is a repair and none is measured)

- **F1 — the r76 dead token cannot be repaired through `GOVERNANCE_CORRECTIONS`.** The horizon is
  2723 and the subject sits at line 2818, so a new row means editing `verifiers/verify_skill_checklist.py`
  (blob `6aab1684…`, pinned) → instrument-pin red. Pin-compatible repairs are data-only (make the
  cited path exist at the measured revision, or an in-tree resolution). Any repair that needs an
  instrument edit is the plan's kill rule.
- **F2 — "both forms" needs two receipts.** The counter prints the fleet root, the guard tally and the
  gate count, not the invocation form (`check_tip_battery.py:392-399`); `Kb79CR01C1Target` reached the
  same conclusion. One run cannot evidence the both-form clause.
- **F3 — `trigger.name_directory` fails inside a clone whose directory name differs** (`Kb79MT01BatteryGates`
  measured it). The battery's sandbox path is `<parent>/kotoba-shokunin`, so a differently-named
  sandbox is a measurement artifact, not a red gate.
- **F4 — budget:** `trigger.line_budget` = 600 lines, base 590, planned C2 addition +7 lines = 597
  (`Kb79S07BudgetCensus`). This draft adds nothing to `SKILL.md`.
- **F5 — a control the plan's C1 list does not have:** the instrument-pin guard accepts *any* of a
  script's pinned blobs, and the other pinned blob of `verify_skill_checklist.py` is 2,804 lines vs the
  base 2,821 — a 17-line delta, inside the ±40 instrument-size cap. Reverting an instrument to its
  other pinned blob is therefore permissible under both guards and is not in the W0–W7 control list.
  Unmeasured by this seat; the w2 attack wave should run it before the C1 after-value is trusted (if it
  reads `6 of 6`, that is a guard gap to report, not a repair).

## 6. Out of scope / not done

- No counter run, no control world, no scratch clone, no patch: the seat produces drafts, and the
  counters are frozen by the L1 after the wave.
- No claim data, no source row, no snapshot, no hash, no verdict, no score movement.
- No edit to `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `corpus/QUALITY.md`, or any other lane file; the
  only writes are this report and the build draft under `.ufo/waves/round-79/`. `corpus/QUALITY.md`'s
  Q74 row must be applied by the L1 together with the lesson row M140 it cites.
- The C2 annotations deliberately do not touch the `## axes` table rows' `Last change` cells (§3.2 of
  the draft): that text is the L1's judgement and the round-54/round-60 evidence must be appended to,
  not replaced.
- Tool installs: none. No pacman, no host service, no PATH writes. One 4 KB `/tmp` file
  (`/tmp/kb79-chk.json`, the checklist gate's JSON) was written and removed; nothing else left `/tmp`,
  and no scratch dir was created under `/fast/scratch`.

## 7. Discipline notes

- Read-only git only (`git log`, `git rev-parse`, `git cat-file`, `git show`); no `jj`, no commit, no
  add, no stash, no checkout anywhere.
- Registry `[:unordered]` principles held: the draft quotes only receipts it read, marks everything
  else, and attributes plan-derived repair items to the plan in a "before you commit" note.
- `git status --porcelain` at the start showed the round-79 build directory, the wave-1 report
  directory, the `w1.ready` markers and the dispatch-output json untracked — sibling seats' in-flight
  artifacts; untouched by this seat.

## 8. The report is opened by its own command (Q68), measured

Run from the lane root against the lane HEAD (`daa3a09`) with `$REPORT` set to this file's path and
`$REPORT` deliberately left as a variable so the command is not itself a pointer:

```
python3 -B verifiers/check_report_pointers.py --report "$REPORT" --repo . --rev HEAD --round 79
```

Result: exit 1, `report pointers resolved 27 of 28; unresolved 1` — the one unresolved pointer is this
seat's own untracked build draft (`report line 12`). It resolves at the commit that carries the wave
directory; at the time of this measurement the round-79 receipts are already tracked at HEAD and every
other pointer (26 blobs, 1 directory) resolved. Re-run with the carrying commit id before filing, and
expect `unresolved 0`.

VERDICT: four record drafts delivered with markers only, no invented data, and every drafted token audited by the gate's own predicate (dead-today set is exactly the three prospective paths the round creates).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79A04LogScoreDraft.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79A04LogScoreDraft.md
