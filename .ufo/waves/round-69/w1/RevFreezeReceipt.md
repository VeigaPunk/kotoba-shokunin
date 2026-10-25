# RevFreezeReceipt — the freeze-time `--self-test` exit 2

Seat: reviewer (leaf, no dispatch). Observation window 2026-10-25T10:17:01Z – 10:21Z.
Lane HEAD `a238989a96cb0d2b939679126b832d75b861ca6e` (round-69 plan commit); base
`a5f7459f99bb27bf697e9438362e75ac5833eca8`. All counter runs in `git clone --shared` sandboxes at
`/tmp`; the lane working tree, index and jj state were not written.

## Verdict (the question asked)

The lesson gained the explanation **during this review**, so the answer changed between my two reads:

- **10:17:01Z — absent.** `corpus/lessons/round-69.md` (md5 `3406bfef1d284779da25faf2a1a462`) named
  the receipt only as inherited inventory (line 12); `plans/round-69.md` (committed, byte-identical
  to the working tree, md5 `14f521b6e39ba834332fbb9afa319815`) never mentioned it. The only artifact
  carrying the causal account was the wave-1 seat prompt (`.ufo/waves/round-69/w1-spec.json:278`) —
  the instruction under verification, which cannot serve as the round's own explanation.
- **10:17:50Z — the paragraph landed** (lesson mtime `2026-10-25 07:17:50.679 -0300`, 9,234 B, md5
  `dbd377427e74f55394f2d8a92bf959d3`), 49 s after this seat's first read, and was **observed on the
  10:21Z re-read**. The file was re-edited at 10:25:38Z (md5 `1194709a6dbe10fa668da0abcb0cdc50`) with
  this paragraph unchanged at lines 17-24. It reads:

  > **Freeze receipt explanation (checks the entry-absent exit 2).** The freeze receipt
  > (`.ufo/waves/round-69/controls/freeze-receipt.txt`) records `check_skill_precedence --self-test`
  > exit 2 (`selftest setup failed: the entry is not present in the working tree`) at freeze time.
  > That is a setup artifact, not a defect verdict: the counter's `--self-test` builds its honest world
  > from the working-tree entry (QUALITY Q48), which only exists after C1's content lands. The content
  > verdict for a missing entry is the measurement path (`--rev` → `0 of 5`, exit 1), which the base
  > control exercises. At the committed round-69 tip, with the entry present, `--self-test` exits 0
  > (18 assertions).

So: **the round now explains the freeze-time exit 2**, and the explanation's core is correct —
setup artifact, not a defect verdict; the measurement path is where a missing entry becomes a content
verdict. Its **closing clause is false**, and the round's answer to the second half of the ticket
("at the branch tip the self-test now exits 0") is **no for the committed tip, yes for the working
tree**. F1-F8 below are the calibrated defects; the exonerations section records what the receipt does
not corrupt. One rebuttal was accepted: ScoutStaleLane's point that the `--self-test` exit 2 is
implemented and intentional narrows my first framing — the counter is not routed as a defect, only its
docstring carve-out (F2b) and its missing receipt (F2).

Then two commits landed. `a02ba7e` (10:27:15Z, "round 69: skill name-collision precedence; close
R68-1..R68-8") shipped entry, lesson and strengthened counters — and **at that commit C1 measured 0 of
5** (`--self-test` 1 failure/22, exit 1; `--rev a02ba7e` 0 of 5; F8). `54f4b6c` (the current tip,
"baseline re-record (127/0/87/39), honest receipts, hardened counters") repaired the entry: a clean
clone now gives `--self-test` **0 failure(s) over 22 assertions, exit 0** and `--rev 54f4b6c` **5 of
5, exit 0**. So the ticket's second half is answered **yes at the current tip** — with the caveat that
the committed lesson still writes "(18 assertions)" where the shipped counter reports 22, and that the
first content commit failed its own claim (F1, F8). The freeze receipt's hashes still describe
`a238989` while the shipped counters are `dc9f1507…` / `53ea6956…`, and `54f4b6c` changed neither the
receipt nor added a C1 self-test receipt (F5).

## What I measured (sandbox, reset to `a238989`)

| state | command | result |
|---|---|---|
| committed tip `a238989` (`git ls-tree HEAD corpus/knowledge/` carries no round-69 entry) | `--self-test` | `selftest setup failed…`, **exit 2** |
| committed tip `a238989` | `--rev a238989` | `skill precedence backed 0 of 5` / `entry missing`, **exit 1** |
| working tree, C1 draft overlaid (`corpus/knowledge/skill-name-precedence-round69.md`, `corpus/SOURCES.md`, `corpus/README.md`) | `--self-test` | `PASS honest world: backed 5 of 5` + 16 `PASS broken world rejected` + `PASS missing-entry classification`, `self-test: 0 failure(s) over 18 assertions`, **exit 0** |
| 10:19Z re-run, **frozen** counter bytes (`9c796574…`) + then-current draft (`md5 6a69525e…` / `6f8648d0…` / `ba03b829…`) | `--self-test` | 18 PASS lines, `0 failure(s) over 18 assertions`, **exit 0** |
| **live** counter bytes (`dc9f1507…`, edited 10:21:28Z) + live draft | `--self-test` | 20 PASS lines + `PASS missing-entry classification`, `self-test: 0 failure(s) over 22 assertions`, **exit 0** |
| live counter bytes, committed tip `a238989`, entry absent | `--self-test` | `selftest setup failed…`, **exit 2** |
| live counter bytes, base `a5f7459` | `--rev a5f7459` | `skill precedence backed 0 of 5` / `entry missing`, **exit 1** |
| live counter bytes, sandbox commit carrying the entry (`8ca2828`) | `--rev HEAD` | `skill precedence backed 5 of 5`, **exit 0** |
| live C2 counter bytes (`9cf97497…`, edited 10:22:44Z) | `--self-test` | `0 failure(s) over 25 assertions`, **exit 0** — intermediate copies inside the edit window: `fdafd542…` → `NameError: R68_INS`, traceback exit 1; `5be7f1e1…` → 1 failure over 23. Those two blobs are gone from disk, so only this cell's final state is reproducible |
| C3 counter, unchanged bytes (`c85f9d7…`) | `--self-test` | `0 failure(s) over 10 assertions`, **exit 0** |
| **committed content tip `a02ba7e`** (10:27:15Z), entry committed | `--self-test` | `FAIL honest world: backed 0 of 5; ["S207: the row's source cell is not in the entry's source line"]`, `1 failure(s) over 22 assertions`, **exit 1** |
| committed content tip `a02ba7e` | `--rev a02ba7e` | `skill precedence backed 0 of 5` / `S207: the row's source cell is not in the entry's source line`, **exit 1** |
| working tree after the uncommitted S207 fix (entry gains "V1") | `--self-test` | `0 failure(s) over 22 assertions`, **exit 0** |
| **current tip `54f4b6c`** ("baseline re-record … hardened counters"), entry repaired | `--self-test` | `0 failure(s) over 22 assertions`, **exit 0** |
| current tip `54f4b6c` | `--rev 54f4b6c` | `skill precedence backed 5 of 5`, **exit 0** |

The round then committed entry, lesson and counters at `a02ba7e` (10:27:15Z) and repaired the entry at
`54f4b6c`, so they are no longer working-tree drafts. **Counter bytes matched the receipt at 10:17Z and
no longer do**: at 10:21:28Z the C1 counter became `dc9f1507…` (receipt: `9c796574…`), at 10:22:44Z the
C2 counter became `9cf97497…` (receipt: `3202549…`), and at 10:28:40Z it became `53ea6956…`; only
`check_province_core.py` still matches (`c85f9d7…`). `54f4b6c` changed neither the freeze receipt nor
added a C1 self-test receipt — F5.

## Findings

### F1 — MEDIUM: the committed lesson still states a count the shipped counter does not produce (`18` vs `22`); its state clause was false at the first content commit and is true only at `54f4b6c`

> "At the committed round-69 tip, with the entry present, `--self-test` exits 0 (18 assertions)."

At the current tip `54f4b6c` the state clause is **true** — `--self-test` gives `0 failure(s)`, exit 0
— and at the first content commit `a02ba7e` it was **false** (`FAIL honest world: backed 0 of 5`,
`1 failure(s)`, exit 1; F8). The count is false at both: the committed counter reports
`self-test: 0 failure(s) over 22 assertions`, because the sentence was written against the frozen
counter's 18 arms and the round then committed the strengthened counter. The lesson was committed
unchanged at `a02ba7e` and not corrected in `54f4b6c`, so the shipped lesson carries a number its
shipped instrument contradicts — pin the sentence to a hash or write 22.

Re-checked at the current tip `54f4b6c`: the lesson still reads `(18 assertions)` (line 24) while the
committed counter prints 22, and its § Mistakes discloses neither the drift nor a re-freeze.

### F2 — MEDIUM (evidence substitution): the round's only receipt named `C1-selftest` is the r68 counter's, it is green, and no receipt covers `check_skill_precedence`

`recapture/` holds ten files and **none** runs `check_skill_precedence.py`: `C1-{base,after,fetch,
selftest}.txt` are `check_client_trust_gates.py` at `e94ae32`/`2cf0d99` (r68, C2/D1),
`C2-routed-*.txt` are the r67 routed counter, `r67-repairs-base.txt` is D3. The one named
`C1-selftest.txt` prints:

```
command: python3 -B verifiers/check_client_trust_gates.py --self-test
measured-rev: 2cf0d99a…
PASS honest world: backed 5 of 5
…
self-test: 0 failure(s) over 12 assertions
exit=0
```

A reader grepping the round-69 recapture set for "C1-selftest" finds a green `backed 5 of 5` line that
belongs to a different counter, one round earlier. The set is **committed at `a02ba7e`**, and `git grep
check_skill_precedence a02ba7e -- .ufo/waves/round-69/{recapture,controls}` returns only `C1-base.txt`
and `freeze-receipt.txt`, so the shipped tree carries no receipt of the C1 self-test at all. That is a live false-green trap for the closure
spot-check (the Q50/M80 class: a result stated without a receipt for the instrument it names), and it
is what makes the lesson's "`--self-test` exits 0 (18 assertions)" unbacked — only seat runs observe
that, never a committed receipt. Correction: re-capture `check_skill_precedence.py --self-test` under
a filename that names the instrument (e.g. `C1prec-selftest.txt`) with `measured-rev:` and `exit=`, or
rename the r68 files to `C2r68-*`.

### F2b — LOW (doc clarity, not a counter defect): the docstring classification lacks a `--self-test` carve-out

Corrected from my first framing after ScoutStaleLane's rebuttal, which I accept on this point: the
self-test's exit 2 at `:292-300` is implemented and intentional, and "2 usage/environment error"
(:42-43) can be read as covering a self-test invoked where it cannot run. So this is **not** a counter
defect to route, and I do not route it as one. What remains is a contract-text gap: the classification
paragraph (`:15-17`, sha256 `9c796574…da48`) and `plans/round-69.md:48-49` state the missing-entry →
exit-1 rule without saying it binds the measurement path only, so a reader of the counter alone has to
infer the carve-out the lesson now supplies. Cure, doc-only and hash-safe at C1's landing commit or in
an erratum: add "`--self-test` in a tree with no entry is a setup exit (2)" to that paragraph.

One sub-claim of the rebuttal does not hold: the self-test does **not** assert the exit-1 rule. Its
`missing-entry classification` arm (`:361-366`) asserts `n == 0` only — the count from `check()`,
never an exit code, on either path; the exit-1 measurement is evidenced by `controls/C1-base.txt`, not
by the self-test. That is F3 below, and it is exactly why the docstring gap could persist.

Still true of the **live** bytes (`dc9f1507…`): the classification paragraph at `:15-18` is unchanged
and still lacks the carve-out, while the new setup exits at `:330-338` are the behaviour the carve-out
should name. Those exits also close ScoutStaleLane's entry-only `KeyError` finding — so that
robustness item is *fixed inside round 69* and remains true only of the committed/frozen bytes.

### F3 — LOW: the `(QUALITY Q48)` citation does not support its clause, and Q48's requirement is not met

The lesson attaches Q48 to "builds its honest world from the working-tree entry". Q48
(`corpus/QUALITY.md:59`) says something else: "A counter's self-test drives its public `main()` on a
satisfying fixture and asserts exit 0 with the exact printed line, beside one broken-conjunct world
asserting exit 1". The C1 self-test does neither — it calls `check()` directly, asserts counts, and
its `missing-entry classification` arm (`:361-366`) checks only `n == 0`, never an exit code. That
unexercised exit code is exactly why the docstring gap (F2b) survived the self-test. The citation
should be dropped or replaced by the sentence's actual basis (the `selftest()` guard at `:292-300`).

True of the **live** bytes as well: `def main` (`:404`) and `sys.exit(main())` (`:443`) remain the only
exit points, and the self-test's 22 arms still assert counts. Q48 is unmet by both the frozen and the
live counter, so the citation is wrong either way and the exit-1 rule remains on the control receipt
(`controls/C1-base.txt`), not in the self-test.

### F4 — LOW: `_world()` lost the r68 `is_file()` guard

`check_skill_precedence.py:275-279` copies `ENTRY`, `SOURCES` and `README` unconditionally; the r68
counter guards the same loop with `if src.is_file()` (`check_client_trust_gates.py:290-293`). An absent
`SOURCES.md`/`README.md` raises an uncaught `FileNotFoundError` (traceback, exit 1) instead of a
classified setup exit — the same unclassified-environment seam as F2b, one file over.

### F5 — HIGH: the shipped counters are no longer the frozen instruments, and no re-freeze artifact exists

The receipt's first three lines are the freeze pin (`sha256 of the frozen counters as committed with
plans/round-69.md`). As of this review:

| counter | receipt (`a238989`) | shipped tip (`54f4b6c`) | working tree |
|---|---|---|---|
| `check_skill_precedence.py` | `9c796574…da48` | `dc9f150764431ec6…c246` (edited 10:21:28Z, committed at `a02ba7e`) | `dc9f1507…c246` |
| `check_r68_routed_repairs.py` | `3202549…dcf2` | `53ea6956cf92050f…cc09` (edited 10:22:44Z then 10:28:40Z, committed at `54f4b6c`) | `53ea6956…cc09` |
| `check_province_core.py` | `c85f9d7…6c5a` | `c85f9d7533fbc4b9…6c5a` | `c85f9d75…6c5a` |

Two independent states exist for two of the three counters, and `plans/round-69.md:42` describes only
the first. `git show 54f4b6c:verifiers/… | sha256sum` confirms the shipped tip carries `dc9f1507…` /
`53ea6956…`, i.e. the strengthened instruments, not the receipted ones. `git diff a02ba7e 54f4b6c --
.ufo/waves/round-69/controls .ufo/waves/round-69/recapture` touches only
`recapture/C2-integrity-after.txt` and `recapture/noharm-at-tip.txt`: **no re-freeze and no C1 receipt**
were added by either commit.

`git status --porcelain` corroborates this from the other side: at 10:17Z the only modified verifier was
`check_r67_routed_repairs.py`; the 10:27Z listing also carries `M verifiers/check_skill_precedence.py`
and `M verifiers/check_r68_routed_repairs.py` against `a238989`.

Both edits are substantive and *good engineering* — the C1 diff tightens the quote span to 5-25 words,
confines the located quote to the quote cell, requires a rule cell of ≥6 words and a client cell that
is not the id, scopes the index row to `## Coverage map`, de-duplicates registry rows, and turns the
scout's entry-only `KeyError` into a setup exit 2 (:330-338); the C2 diff adds a D7 `--numstat`
truncation arm and tightens D5/D6. But they are **post-freeze and undisclosed**: no artifact under
`.ufo/waves/round-69/` or in the lesson records either new hash, and the freeze receipt still prints
the old ones. Consequences under the lane's own bar:

- **The receipt remains true of `a238989` but no longer describes the instrument that will measure the
  claim.** `git show a238989:verifiers/check_skill_precedence.py | sha256sum` still gives
  `9c796574…da48` and the C2 file still gives `3202549…dcf2`, so Q24 — a receipt's hash checked against
  the *committed* instrument bytes — passes for the revision the receipt names. The break is against
  `plans/round-69.md:42` ("Counter semantics (frozen with this plan; sha256 recorded in the plan
  commit's receipt)") and against the tree that will measure the claim. A reviewer can rebut "the hash
  matches the committed bytes"; they cannot rebut "the shipped bytes are no longer the frozen
  instrument".
- **Seat evidence is pinned to a superseded instrument**: `MutC1Counter.md:34,167-168`,
  `RevC1Counter.md:5`, `ScribeFactsAudit.md:87` and `ExecFetchArm.md:5` all cite `9c796574…` as the
  working-tree bytes; that was true when they ran and is no longer true.
- **The edit window was observed non-green**, as expected mid-edit but worth recording: a copy at
  10:26Z crashed `NameError: name 'R68_INS' is not defined` (C2), a copy at 10:27Z returned
  `FAIL honest world: closed 6 of 8` / `1 failure(s) over 23 assertions` (C2), and the settled bytes
  (`9cf97497…`) return `0 failure(s) over 25 assertions`, exit 0.

Cure: a **re-freeze** — new sha256 lines with a superseding note naming the seat findings that drove
each change (MutC1Counter for the C1 arms; the D5/D6/D7 findings for C2), re-captured controls against
the new hashes, and the lesson's `18` updated to the measured arm count — or commit the counters at the
frozen bytes and carry the strengthening to round 70. Either way the receipt as committed cannot be the
round's instrument pin.

### F6 — MEDIUM: the three cheapest controls cite revisions that do not exist in the lane object database

Each control receipt names a sandbox commit as `measured-rev:`. Verified in the lane:

```
95651d4d6a465d7986f993cfe9c47b394fd53ea0  (C1 junk control)   ABSENT
bf69a719846436a0a08ff4235fa9c676df09cbbd  (C2 cheap control)  ABSENT
00b5ddeab26d94f3a07860ed5a3bfba74034a20a  (C3 cheap control)  ABSENT
e94ae32a5cd8dc3ee8e2d247816784bec2750cc0  (r68 base)          PRESENT
2cf0d99a6d5a3e1cb0b73e3b71cb495fd1eadc6f  (r68 tip)           PRESENT
```

(`git cat-file -e <rev>`; reps in `controls/C1-junk-control.txt`, `C2-cheap-control.txt`,
`C3-cheap-control.txt`.) The base controls at `a5f7459` are reproducible — I re-ran the C1 base myself
(`0 of 5`, exit 1) — but the three shortcut controls cannot be re-measured by any reader, now or at
closure, because the objects were never pushed into the lane. That undercuts the plan's own control
requirement (each shortcut control runs under the frozen predicate *before* data): the receipts exist,
the evidence does not. Cure, folded into the F5 re-freeze: re-capture the three controls on
lane-present revisions (commit the control worlds through `jj-lane.sh`, or rebuild each world from a
lane-visible commit) and name the revision in the receipt.

### F7 — MEDIUM: the C2 counter's D7 arm diverges from the spec the round accepted (equality instead of a floor), and the constant has no receipt

`verifiers/check_r68_routed_repairs.py:100` fixes `R68_INS, R68_DEL = 4081, 251`, and `d7_wave_paths`
(:312-317) compares `git diff --numstat R69_BASE..measured -- <24 paths>` to that pair by **exact
equality** (`!=`). The round's own C2 critic specified a floor
(`.ufo/waves/round-69/w1/CritC2Repairs.md:180-183`): "sum `git diff --numstat R69_BASE..rev` over the
ten `MODIFIED` paths and require `insertions ≥ 4081` and `deletions ≥ 251` (growth from later seat
appends passes; a trimmed commit fails)". So this is a **spec divergence**, not merely an unreceipted
constant: D7 now fails as a non-defect whenever any of the 24 paths legitimately grows — and those
paths include the r68 seat logs and reports this round itself appended to. The constant's only
provenance is CritC2Repairs prose (`:175-176`, "verified at the lane's working tree today"), with no
receipt naming the `--numstat` command and revision. Cure: the floor the critic asked for (`≥`), plus a
receipt carrying the measured command and revision (or derive the value from a named revision at
measure time).

Corollary: D7 receipts captured before the counter edit are not comparable with the shipped arm — the
body changed, so a `2cf0d99`-era D7 result describes a different check and cannot be cited for the
current one.

### F8 — HIGH at `a02ba7e`, **repaired at `54f4b6c`**: the first content commit failed its own C1 claim

Commit `a02ba7e` (10:27:15Z) carries the entry, the lesson and the strengthened counter, together with
the r68 wave paths. Measured on a clean clone at that commit, with no overlay:

```
$ python3 -B verifiers/check_skill_precedence.py --self-test
FAIL honest world: backed 0 of 5; ["S207: the row's source cell is not in the entry's source line"]
…
self-test: 1 failure(s) over 22 assertions
exit=1
$ python3 -B verifiers/check_skill_precedence.py --rev a02ba7e
skill precedence backed 0 of 5
  - S207: the row's source cell is not in the entry's source line
exit=1
```

Cause: that commit's `SOURCES.md` S207 row carries the `source` cell
`opencode — Agent skills (served V1 docs page) — https://opencode.ai/docs/skills/`, while its entry's
line 5 reads `source: S207 — opencode — Agent skills (served docs page) — …`; conjunct 4 requires the
row's `source` cell verbatim in the entry's `source:` line, so the honest world scored 0.

Repair: at the current tip `54f4b6c`, the same two commands give `0 failure(s) over 22 assertions`,
exit 0 and `skill precedence backed 5 of 5`, exit 0. The finding is closed, but the episode is the
round's clearest reproducibility fact: its first shipped revision measured 0 of 5 against its own
counter, so any closure check pinned to `a02ba7e` reproduces 0 of 5 and no working-tree run can stand
in for a `--rev` tip measurement. A tip receipt at `54f4b6c` (or later) is the evidence to cite.

## What is exonerated (calibration in the other direction)

- **The receipt is faithful to its own moment.** Freeze receipt mtime 06:57:18 -0300; the entry was
  created 07:08:07 (and re-edited since). A clean clone at `a238989` still reproduces exit 2 exactly,
  under both the frozen bytes and the live bytes. The instrument-pin staleness that begins at
  10:21:28Z (F5) does not change what the receipt measured; it changes what the receipt can be cited
  for now.
- **The exit-2 setup idiom is inherited, not invented.** Identical `selftest setup failed … return 2`
  at `check_client_trust_gates.py:306-310` (r68) and `check_instruction_authority.py:227-229` (r67).
- **No claim measurement is corrupted.** Both C1 before-state receipts use the measurement path and
  correctly read exit 1 (`controls/C1-base.txt`: `0 of 5`, `entry missing`;
  `controls/C1-junk-control.txt`: `0 of 5`, provenance-trio failure). With the entry present the
  self-test's remaining arms are green — 17 under the frozen bytes (18 total), 21 under the live bytes
  (22 total) — including `PASS broken world rejected: entry missing`; the honest worlds are intact and
  the exit code was never the thing that failed.

## Cross-check with ScoutStaleLane (corroborated, then sharpened)

Independent agreement on the measurement and the freshness point (receipt 06:57 < entry 07:08; clean
clone exit 2; entry overlaid exit 0). Four sharpenings after two exchanges:

1. The gap is deeper than "a post-entry re-capture is needed": `grep -rn check_skill_precedence
   .ufo/waves/round-69/recapture/` returns nothing, so no committed receipt of the C1 self-test exists
   at any state, before or after the entry — including the one the lesson now asserts. ScoutStaleLane
   sharpened this into the trap I now carry as F2: the receipt *named* `C1-selftest.txt` is the r68
   counter's and prints a green `PASS honest world: backed 5 of 5` (12 assertions, `exit=0`), so a
   filename grep yields false green for the round-69 counter.
2. `plans/round-69.md:17` ("The watchdog log shows no `lane-dead-no-report kotoba round=69` line: no
   earlier attempt") is **superseded, not false at freeze**: the plan was authored 03:31:26 and
   committed 06:57:22; **kotoba attempt-1 launch is 06:46:36** (`../.ufo/watchdog.log:1304` — not the
   06:56:04 line 1306, which is `launch revenger round=69` as ScoutStaleLane corrected me), and the
   death line `lane-dead-no-report kotoba round=69` is 06:59:59 (line 1309). So the plan was committed
   10 m 46 s into attempt 1 and the sentence went stale 2 m 37 s after the commit; the "died 13m in"
   label reconciles with 06:46:36 → 06:59:59 = 13 m 23 s. The sentence was true when frozen; the
   lesson's opening paragraph already supersedes it, and because the plan is frozen the correction
   belongs in the lesson or an erratum, never a plan edit.
3. He corrected my observation timing: the lesson's paragraph landed at **10:17:50Z** (mtime), not
   10:21Z — 10:21Z is when I re-read; we agree it is present now. He independently measured the live
   counter at `0 failure(s) over 22 assertions`, exit 0 (matching my table), and independently
   confirmed Q48 is unmet on live bytes (F3).
4. He reports the entry-only `KeyError` robustness item as fixed by the live setup exits; I verified
   that (:330-338) and route it as *closed inside round 69, still true of the frozen/committed bytes*
   (F2b note), not as an open defect.
5. His Q24 refinement is adopted verbatim in F5: the receipt still hashes `a238989`'s bytes exactly, so
   the defect is "true of a revision the lane no longer ships", not "a bad receipt". F6 and F7 are his
   findings, verified here: the three shortcut-control revisions are `git cat-file -e` ABSENT from the
   lane while `e94ae32`/`2cf0d99` are present, and the C2 counter's `4081`/`251` has no receipt naming
   its measurement (only `CritC2Repairs.md:175-176` prose) while `d7_wave_paths` compares by equality
   rather than the floor the critic recommended.

## Residual risk

Entry, lesson and counters were committed at `a02ba7e`, the entry repaired at `54f4b6c`, and the
counters edited again after the freeze (F5), so every line below is pinned to the tip present at
10:33Z. **F1 is now a one-number fix** (write 22, or pin to the shipped hash). F2 closes with a
re-capture of `check_skill_precedence --self-test` under an instrument-naming filename (or a rename of
the r68 `C1-*` receipts); F2b with a docstring carve-out or an erratum; F3/F4 persist unless the
counter is amended. F5 needs a re-freeze receipt (new sha256 lines, a note naming the seat findings
that drove each change, re-captured controls) before any claim cites the shipped instrument — the
current receipt is true of `a238989` and describes nothing the lane ships. F6's three shortcut controls
must be re-captured on lane-present revisions inside that same re-freeze; F7 needs a receipt naming the
`--numstat` command and revision behind `4081`/`251`, with the floor the critic asked for instead of
equality. **F8 is closed** — `54f4b6c` measures `5 of 5`, exit 0 — but its episode stands: the round's
first shipped revision measured 0 of 5 against its own counter, so a closure check pinned to
`a02ba7e` reproduces the failure, and only a `--rev` measurement at `54f4b6c` or later is tip evidence.

## Verification gaps

- No `lsp` device is mounted in this session (`xd://lsp` → "No such tool"), so caller/definition checks
  were executed runs plus end-to-end reads of `selftest()`, `_world()` and the r68 counterpart — not
  presented as semantic resolution.
- No jj state was read (`jj` commands snapshot the working copy, which the seat bounds forbid); "branch
  tip" is `git rev-parse HEAD` only.
- `--fetch` was not run (network, out of ticket scope); no claim is made about the five live pages.
- No corpus gate was run; scope is the freeze receipt and the artifacts that could explain it.
- The three shortcut-control revisions are absent from the lane (F6), so I verified those controls only
  from their receipts, not by re-running them; the two C2 counter blobs I caught mid-edit are gone
  (table note), so those two non-green observations cannot be re-derived by a reader.

## Commands run (sandboxes `/tmp/rfr69`, `/tmp/rfr69b`, `/tmp/rfr69c`; `git clone --shared`, reset to `a238989`)

```
# frozen counter bytes (receipt hash 9c796574…)
python3 -B verifiers/check_skill_precedence.py --self-test              # entry absent -> exit 2
python3 -B verifiers/check_skill_precedence.py --rev a238989            # 0 of 5, entry missing -> exit 1
cp <lane>/{corpus/knowledge/skill-name-precedence-round69.md,corpus/SOURCES.md,corpus/README.md}
python3 -B verifiers/check_skill_precedence.py --self-test              # 0 failure(s) over 18 assertions -> exit 0
git show a238989:verifiers/check_skill_precedence.py | sha256sum        # 9c796574…da48 == receipt

# live counter bytes (sha dc9f1507…, edited 10:21:28Z)
cp <lane>/verifiers/check_skill_precedence.py verifiers/
python3 -B verifiers/check_skill_precedence.py --self-test              # 0 failure(s) over 22 assertions -> exit 0
python3 -B verifiers/check_skill_precedence.py --rev a5f7459            # 0 of 5, exit 1
git add -A && git commit -m sandbox \\
  && python3 -B verifiers/check_skill_precedence.py --rev HEAD          # 5 of 5, exit 0

# live C2 counter bytes (sha 9cf97497…, edited 10:22:44Z)
cp <lane>/verifiers/check_r68_routed_repairs.py verifiers/
python3 -B verifiers/check_r68_routed_repairs.py --self-test            # 0 failure(s) over 25 assertions -> exit 0
```
