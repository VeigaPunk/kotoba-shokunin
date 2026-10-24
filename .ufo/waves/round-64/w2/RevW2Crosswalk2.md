# RevW2Crosswalk2 — final crosswalk: r63 spot-check routed items ↔ C2 counted checks at `c019919c`

Round 64, wave 2 (falsify), hyaku run 5, 2026-10-24. Reviewer seat, independent leaf.
Measured tip `c019919c97ab5fe98e87a7754b4449ea4e699c99`; base `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`.
Read-only: no lane production file edited, no `git`/`jj` write, no ref/index change; scratch
under `/tmp` only. No tool installed or upgraded (nothing was needed: git, python3, sha256sum).

Axes (godspeed, named before data): **mapping exactness** (is 1↔1 real in both directions),
**computation soundness** (does each PASS come from bytes, and only its own item's bytes), and
**bound honesty** (are 5–6 named where the plan says). Cheapest discriminating moves first.

Instrument bytes: `verifiers/check_r64_routed_repairs.py` sha256
`8f5b9f915abe6ae42bf84c4c8842ed341c1e03afc184ca23351f33545e5294bf`, identical at `c019919c`
and at `HEAD` (`b99fb79`), so the runs below are the measured tip's instrument.

## Verdict (3 sentences)

Items 1–4 are closed by exactly one counted check each, measured both ways: all four FAIL at
base with their own evidence line, all four PASS at tip, and four single-evidence-removal worlds
flip exactly one check each (3/4 every time). The check-2 counted line is one physical LOG line
(1-based 2604, 741 characters / 745 bytes) under the round-64 header carrying both basenames,
both committing revs, the pinned base and `committed` — verified by the counter's own matcher and
by simulation. Two declared dispositions are not landed as written: items 5–6 are named in the
lesson's §Routed-input handling, **not** in §Bounds as plan E3.5 requires (F1), and E3.5/D3's
"basename↔rev pairing / distinct lines" matcher discipline is absent from the landed code, so
swapped, negated and inverted statements still score green (F2); the real LOG lines are honest,
so the closure is substantively true but the falsification strength claimed at lesson row (k) is
overstated.

## 1. Base and tip runs (my own, verbatim)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
FAIL seat-edit-committed    marker=False added-marker=False added-lines=0 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
FAIL assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; no BASE_REV-added patch line names 23 assertions
r63 routed defects closed 0 of 4
the pinned do-nothing control at 078eec4a1f6a41c64ff8806f58b46a67cd413bfc is never a certification
EXIT=1
```

```
$ python3 -B verifiers/check_r64_routed_repairs.py --rev c019919c97ab5fe98e87a7754b4449ea4e699c99
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
EXIT=0
```

Fail-closed spot checks: `--rev 5613392` (short hash) → `error: --rev must be a full 40-hex
revision (or use --self-test)`, EXIT=2. Counter self-test: `self-test: 0 failure(s) over 32
assertions`, EXIT=0.

## 2. Items 1–4 ↔ checks 1–4: exactly one, demonstrated two ways

Independence matrix (each world removes exactly one check's evidence; the other three must stay
PASS). Worlds built by monkeypatching the tip module's `show` / `_r64_suffix_lines` /
`_added_lines` in-process against the real lane:

```
baseline                      seat-edit-committed=PASS control-revs-named=PASS lowest-axis-corrected=PASS assertion-count-named=PASS | closed=4/4
world A (seat -marker)        seat-edit-committed=FAIL control-revs-named=PASS lowest-axis-corrected=PASS assertion-count-named=PASS | closed=3/4
world B (-citation line)      seat-edit-committed=PASS control-revs-named=FAIL lowest-axis-corrected=PASS assertion-count-named=PASS | closed=3/4
world C (-axis line)          seat-edit-committed=PASS control-revs-named=PASS lowest-axis-corrected=FAIL assertion-count-named=PASS | closed=3/4
world D (-drift note)         seat-edit-committed=PASS control-revs-named=PASS lowest-axis-corrected=PASS assertion-count-named=FAIL | closed=3/4
```

No check is orphaned, no item is double-counted, and the four checks read disjoint artifacts
(`MutW2SplitClauses.md` / controls+suffix / SCORECARD+suffix / r63 counter+`ExecW2E2Patch.md`).
My own derivations behind each PASS:

| # | Routed item (spot-check §Routed defects) | Check | My derivation at `c019919c` |
|---|---|---|---|
| 1 | uncommitted `MutW2SplitClauses.md` edit (item 1) | `seat-edit-committed` | committed in `c019919c` itself: `git diff --numstat c019919c^ c019919c -- <path>` → `82 29`; `git diff --numstat 38defdc c019919c -- <path>` → `82 29`; marker absent at base (`git show 078eec4:<path> \| grep -c "temporal mismatch"` → `0`, grep exit 1); marker line present at tip (line 728, `was a **temporal mismatch** on my part.`) and is an addition; no later commit touches the file (`git diff --numstat c019919c HEAD -- <path>` empty). |
| 2 | report citation imprecision, controls "@ `35d44b4b`" (item 2) | `control-revs-named` | my own `git log --diff-filter=A --format=%H -1 c019919c -- <control>` → `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8` and `cbbee56e9a3589b0b46736ad36f1b77701def80e`; `git cat-file -e 35d44b4b…:<control>` → fatal, exit 128 for both; both controls internally pin `35d44b4b4dcdda234b5dbff7af37e432fec55f05`. |
| 3 | lowest-axis parenthetical (item 3) | `lowest-axis-corrected` | `SCORECARD.md` at tip: owned header `**depth + consistency**`; `## axes` rows `depth 9`, `consistency (calibration sub-axis) 10`; advisory 8.5/8.5/8/8.5/8.0 are not owned, so owned minimum is depth 9. |
| 4 | `ExecW2E2Patch` "21 assertions" (item 4) | `assertion-count-named` | my own materialization of `verifiers/check_r63_routed_repairs.py` at tip (sha256 `b9e627371cfc5e83a5bbde2b2ab455c819cc9419eafded5c5671bf35d66ed105`, matches the r63 spot-check's pin) in `/tmp/r63x` → `self-test: 0 failure(s) over 23 assertions`, EXIT=0; drift note added vs base (`git diff 078eec4 c019919c -- ExecW2E2Patch.md` → `+` line naming `over 23 assertions`), and the patch file at base contains `23 assertions` 0 times. |

## 3. Check-2 counted line: one physical line, exact text, matcher simulation

Location: `LOG.md` at `c019919c` has exactly **one** round-64 heading, 1-based line 2599
(`## 2026-10-24 — Round 64 (hyaku run 5, attempt 1; …)`, matched by the counter's
exact-or-space rule); the counted line is 1-based **2604**, i.e. 5 lines under the header.
Physical-line proof: `open('/tmp/log_tip.md','rb').read().split(b'\n')[2603]` is a single
element of 745 bytes (741 characters, 2 multi-byte em dashes, no embedded newline); there is
exactly one suffix line containing both basenames (`hits: 1`).

Exact line (verbatim, one line):

```
- **Counted citation line (C2 check 2) — the controls' citation rev (the M95 class, in the report itself).** The round-63 report cites both controls "@ `35d44b4b`" — the rev they were run against, not the rev that contains them: `git log --diff-filter=A --format=%H -1` on master computes `C1-do-nothing-v31.txt` committed at `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8` and `C2-before-r62tip.txt` committed at `cbbee56e9a3589b0b46736ad36f1b77701def80e`, while `git ls-tree -r 35d44b4b4dcdda234b5dbff7af37e432fec55f05 -- .ufo/waves/round-63/controls/` prints nothing (both paths exit 128 under `git cat-file -e`). The correct citation form is committed-at + run-against-base (now QUALITY Q60). C2 check 2 counts this line from committed bytes.
```

Matcher simulation — tip module loaded from a `/tmp` copy of the committed blob,
`_r64_suffix_lines` replaced by a one-line world, real git behind the computations:

| Synthetic line | check 2 |
|---|---|
| the exact line above | **PASS** |
| swapped attribution (`C1-do-nothing-v31.txt` at `cbbee56…`, `C2-before-r62tip.txt` at `8c4cefa…`, base `35d44b4b…`) | **PASS** — F2 |
| negated (`…is false; neither was committed`) | **PASS** — F2 |
| one basename only | FAIL |
| wrong rev | FAIL |
| repinned base (`2ba4547f…`) | FAIL |
| empty line | FAIL |
| 7-hex short forms (`8c4cefa` / `cbbee56` / `35d44b4b`) | PASS (declared) |
| one line carrying both checks' tokens (basenames, revs, base, `committed`, `lowest`, `depth`, `consistency`, 9, 10) | check2 PASS **and** check3 PASS — F2 |

So the required line exists and is a single physical line carrying every required token; the
matcher is *content-presence*, not the basename↔rev-pairing / distinct-line discipline E3.5
declares.

## 4. Items 5–6: bound naming (F1)

Spot-check items 5–6 are the C1 deferred `span_missing` arms and the operator-owned SHONEN
promotion. At `c019919c`:

- **Named, but not in Bounds.** `corpus/lessons/round-64.md` §"Routed-input handling" item 4
  (lines 115–117) says "items 5 (C1's deferred arms) and 6 (operator-owned SHONEN) are outside
  the counted predicate by name." The §"Bounds" section (lines 143–158) says only: C2 "binds the
  r63 spot-check's four routed lane-side defects; the other 13 census instances … not
  headline-counted; a new self-assessment mismatch class is outside the bound" — items 5 and 6
  are not named there. Plan E3.5 (line 351) declares the C2 **Bounds** paragraph "names the
  non-counted items: spot-check items 5 … and 6". Neither the plan's own C2 bound paragraph
  (lines 244–247) nor the lesson's does.
- **Substance is real, not lost.** Item 5 is genuinely closed by C1, not silently dropped: my own
  run of `python3 -B verifiers/check_scoped_rules_v32.py --self-test` at tip prints
  `survivors closed 6 of 6`, the three `must-fail … disabled admits …` lines and
  `self-test: 0 failure(s) over 223 assertions`, EXIT=0. Item 6 is operator-owned and correctly
  uncounted (no `[x]` written).
- Nothing in `LOG.md` at tip or the round-64 SCORECARD annotation names items 5/6 (grep for
  `items? 5|item 6` returns only pre-round-64 rows), so the lesson §Routed-input handling is the
  only placement.

Severity **MEDIUM** for the crosswalk as written: the acceptance item is "named in the lesson
Bounds", and the declared location (E3.5) is unlanded. The repair is a one-sentence append to
§Bounds (M95 discipline: append, do not rewrite the existing bullets) plus an erratum line naming
E3.5's location drift.

## 5. Findings by severity

### F1 — MEDIUM — items 5–6 are outside the counter but not named in the lesson §Bounds

Evidence: §4 above (`corpus/lessons/round-64.md:115–117` vs `:143–158`; `plans/round-64.md:351`
and `:244–247`). The counter's own C2 bound (its docstring and plan text) is correct about the
four counted defects; the promised *naming of the excluded items in Bounds* is absent. No
misclosure — the excluded items are recorded and item 5 is independently closed by C1's 223-arm
predicate — but the round-64 acceptance sentence and E3.5 are unmet as written.

### F2 — MEDIUM — declared matcher discipline (E3.5 / D3) is not in the landed code; lesson row (k) overstates the fix

`plans/round-64.md` E3.5 (lines 343–349 region): "Checks 2 and 3 use **ordered, content-shaped
matchers (a suffix line carrying basename↔rev pairing** …)". `RevSpotcheckCrosswalk` D3 requires
(i) rev token on the same line as its filename in both directions, (ii) `depth` within 80
non-period characters of `lowest`, (iii) distinct appended line indices for checks 2/3, each with
a red arm. Landed `check_control_revs` / `check_lowest_axis` (`verifiers/check_r64_routed_repairs.py`
lines 190–210, 296–315) do independent `search`/`in` presence tests; the 32-assertion self-test
has arm labels for look-alike, one-sided, wrong rev, wrong base, hex boundary, missing basenames —
and **none** for swapped pairing, inversion, negation or line-distinctness (`swap`, `invert`,
`negat` → 0 occurrences in source; `distinct` occurs once, in an unrelated refusal-arm comment).

Measured consequences (my simulation, §3): swapped attribution PASSes; "neither was committed"
PASSes; the inverted axis sentence "`consistency` 10 is the lowest owned axis; `depth` 9 is not"
PASSes check 3; one line satisfies checks 2 and 3 simultaneously. Discriminating parts that do
work: digit boundaries reject `depth 19` / `consistency 100`; missing `lowest` fails; missing
basenames / wrong rev / repinned base / empty line fail.

Lesson falsify-corrections row (k) (`corpus/lessons/round-64.md:99`) reads "**fixed pre-data
(E3.5)** — ordered, content-shaped matchers". Content-shaped is true; ordered/pairing and the
distinct-line rule are not. The real LOG lines (2604, 2605) are honest, so the actual `4 of 4`
certifies true repairs — the defect is that the counter would also certify the exact false prose
items 2/3 exist to correct, which is the class the spot-check's own F5/F6 named. Repair options:
implement D3 (pairing + distinct indices + the four red arms) or carry D3's residual bound
verbatim in the lesson/report and withdraw the "fixed" wording.

### F3 — LOW — checks 1 and 4 accept negated marker/tally lines (residual discrimination risk)

Declared specs (E2.1: marker + addition + ≥60 added lines; E2.4: bounded tally + `assertions` +
addition vs BASE) are implemented literally, so this is not a plan violation. But a world adding
`There is no temporal mismatch in this file.` plus 59 filler lines scores check 1 PASS, and a
world adding `note: the 23 assertions figure in the table above is wrong` scores check 4 PASS
(both measured: 4/4 in each world). For checks 1/4 a requiring-phrase or a pairing of the number
with the self-test command would discriminate. Actual artifacts are affirmative, so no false
certification today; record as a round-65 hardening item, not a re-measurement trigger.

### F4 — LOW (calibration datum) — E1's check-2 leak premise no longer reproduces on base; anchoring is defended by a self-test arm instead

E1 item 1 justified suffix-anchoring because base LOG "already co-locates `8c4cefa`, `cbbee56`
and `35d44b4b`" and a whole-LOG scan "would false-green check 2 at base". Measured at
`078eec4`: base has 0 round-64 headings; the two basenames appear once each on **different**
lines (2581 and 2582); no base line contains both. Simulating an unanchored counter at base
(`_r64_suffix_lines` → all base lines) still scores `0 of 4`, all four FAIL. E1's premise held
for the pre-E2.2 token set (revs + base only); after E2.2 added the basenames it is superseded.
Anchoring remains correct and is exercised by the self-test arm "baseline LOG leak: old control
citations remain outside r64 suffix", so this is a wording datum for the lesson, not a defect in
the landed check. (Also confirmed: the check-2 counted line is a `+` addition; base has no
round-64 header.)

## 6. Residual risk and verification gaps

- I verified the counter's four checks and their witnesses; I did **not** re-run the lane's gate
  battery, no-harm arms, or census (out of this seat's scope; other wave-2 seats hold them). The
  "other 13 census instances" claim in §Bounds is `ScoutReceiptSweep` scope and was not
  re-derived here.
- The `ExecW2E2Patch.md` stale cells ("21 assertions", lines 496/498 etc.) remain unrewritten by
  design (E3.6 drift-note remedy). The added note is the only line naming 23; a future reader
  scanning only the table would still see 21 — by declared choice, not drift.
- `_r64_suffix_lines` returns the suffix after the *first* exact-or-space header; a future
  second round-64 heading is ignored, which is correct today (one heading) but means later
  corrections must sit after the first heading to count. [INFERENCE] No current artifact is
  affected.
- Check 4 depends on running materialized code from a git blob; I reproduced its tally
  independently (23, exit 0) so the number is not merely asserted by the counter under test.
- Base-arm refusal and fail-closed exits verified (`0 of 4`, exit 1, refusal message; `--rev`
  strict 40-hex, exit 2). The base arm for checks 1 and 4 is addition-based and therefore
  trivially empty at base for the diff part; content discrimination at base still holds (marker
  absent, `23 assertions` absent from the base patch file: grep count 0).

## Crosswalk disposition (recommendation, not an admission)

| # | Item | Counted by | Status at `c019919c` | Note |
|---|---|---|---|---|
| 1 | uncommitted seat edit | check 1 | **closed** (commit `c019919c`, 82/29, marker addition) | F3 negation residual |
| 2 | control citation revs | check 2 | **closed** (line 2604, one physical line, all tokens) | F2 pairing residual |
| 3 | lowest-axis parenthetical | check 3 | **closed** (line 2605, depth 9 < consistency 10) | F2 inversion residual |
| 4 | stale "21 assertions" | check 4 | **closed** (drift note, runtime+static 23) | F3 negation residual |
| 5 | C1 deferred arms | none (C1) | outside the counter; C1 predicate green (223, exit 0) | F1: not named in §Bounds |
| 6 | SHONEN operator promotion | none (operator) | outside the counter; correctly uncounted | F1: not named in §Bounds |
