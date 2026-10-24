# ScribeW2Report — round-64 wave 2 (falsify): evidence-fill pack

Seat: `kotoba-r64.ScribeW2Report-2` (leaf, no dispatch). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Purpose: the paste-ready text for the round-64 report's `## Before → after measurements`,
`## Sources & frontier` and `## Landed changes` sections (the skeleton at
`.ufo/waves/round-64/w1/ScribeReportSkeleton.md:98-125`), with every number re-measured by this seat
on byte-exact extracts of the named revisions. Nothing here was copied from a sibling seat unless the
line says "seat evidence".

## Method and provenance

- Extracts: `git archive <rev> | tar -x -C /tmp/r64w2/{base,tip}` — `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`
  → `/tmp/r64w2/base`, `c019919c97ab5fe98e87a7754b4449ea4e699c99` → `/tmp/r64w2/tip` (both exit 0).
- Git-object reads for the C2 counter: `git clone --no-hardlinks <lane> /tmp/r64w2/clone` (exit 0), so no
  git/jj write ever touched the lane. The clone's HEAD is `b99fb79`; `verifiers/check_r64_routed_repairs.py`
  is byte-identical at `c019919c` and `b99fb79` (`git diff --stat c019919c b99fb79 -- verifiers/` → empty),
  sha256 `8f5b9f915abe6ae42bf84c4c8842ed341c1e03afc184ca23351f33545e5294bf`.
- Mutation scratch: `/tmp/r64w2/sm1` (tip bytes), `/tmp/r64w2/sm1base` (base bytes); patch applied by this
  seat (`span_missing = sorted({...})` → `span_missing = []`, the wave-1 SM1 replacement).
- No tool installs or upgrades were needed this seat: python3, gawk, git, coreutils as shipped.
- The only lane file written is this report.

## 1. `## Before → after measurements` — paste-ready bullets

- **C1 (depth).** Command `python3 -B verifiers/check_scoped_rules_v32.py --self-test`. Before (`078eec4a`):
  `self-test: 0 failure(s) over 219 assertions`, exit 0, counter sha256
  `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43`; the branch is unpinned — the SM1
  replacement (`span_missing = []`) on those bytes also prints `self-test: 0 failure(s) over 219 assertions`
  at exit 0 (re-measured this wave, `/tmp/r64w2/sm1base`; seat evidence: `w1/ExecSpanBefore.md`). Do-nothing
  control (quoted from the committed r63 receipt, not re-run by this seat): v31 prints `survivors closed
  5 of 6` over 201 assertions
  (`.ufo/waves/round-63/controls/C1-do-nothing-v31.txt`, committed at `8c4cefa`; base `35d44b4b` pinned
  internally) and cannot reach the 223-assertion line. After (`c019919c`): the frozen lines
  `worlds reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 6 of 6` /
  `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes` /
  `self-test: 0 failure(s) over 223 assertions`, exit 0 (`receipts/C1-span-measure.txt`, whose 21 output
  lines are byte-identical to this seat's re-run; counter sha256
  `f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d`), and the kill conjunct holds: SM1 on
  the landed bytes exits 1 with `FAIL A2 G7: a backticked span whose words occur in neither the cited line
  nor the page is rejected: got False, expected True` (`receipts/C1-span-kill.txt`; re-measured this wave,
  `/tmp/r64w2/sm1`, `self-test: 1 failure(s) over 223 assertions`). Note for the wording: both revs also
  print `must-fail E2e …` and `must-fail G7 …` lines, so the plan's four-line block is printed as a set but
  not contiguously at either rev (base order is the same six-line shape with `219`).

- **C2 (calibration/consistency).** Command `python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>`.
  Before (`--rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc`, the pinned `BASE_REV`): `r63 routed defects
  closed 0 of 4`, exit 1 (`controls/C2-before.txt` — this seat's re-run of that exact command is
  byte-identical to the committed file), check 1 failing on the committed `38defdc` copy (marker
  `temporal mismatch` absent; `added-lines=0`) and checks 2–4 failing because no round-64 correction lines
  exist at that rev. After (`--rev c019919c97ab5fe98e87a7754b4449ea4e699c99`): four `PASS` lines and
  `r63 routed defects closed 4 of 4`, exit 0 (`receipts/C2-r64-measure.txt`: its five result lines are
  byte-identical to this seat's re-run; the receipt additionally pins `counter sha256:
  8f5b9f91…` and `self-test: 0 failure(s) over 32 assertions`). The counter refuses to certify the base
  (`the pinned do-nothing control at 078eec4a… is never a certification`), `BASE_REV` is a module constant
  and not an argparse option (`--base` → exit 2, `error: unrecognized arguments`), and the self-test's 32
  assertions pass at exit 0 on the landed bytes. Label: four repair checks, not the spot-check's whole
  defect class.

- Both counters re-verified by this seat at the wave-2 lane HEAD `b99fb79` (whose
  `verifiers/check_scoped_rules_v32.py` is byte-identical to `c019919c`): v32
  `self-test: 0 failure(s) over 223 assertions`, exit 0; r64 counter `--rev c019919c` `4 of 4`, exit 0;
  census `validate` exit 0 and `census` rows 118 / tier.A 115 / mined 110, run against the live lane.
  No pacman/uv/npm transaction was run.

### 1.1 Pasted outputs

C1 at base `078eec4` (exit 0):

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 219 assertions
```

C1 at tip `c019919c` (exit 0):

```
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
```

SM1 (`span_missing = []`) — base exit 0 / tip exit 1:

```
# base 078eec4 bytes: exit 0
self-test: 0 failure(s) over 219 assertions

# tip c019919c bytes: exit 1
FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
self-test: 1 failure(s) over 223 assertions
```

C2 conjunct A (`--rev c019919c…`, exit 0):

```
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
```

C2 conjunct B (`--rev 078eec4a…`, the pinned do-nothing control, exit 1):

```
FAIL seat-edit-committed    marker=False added-marker=False added-lines=0 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
FAIL assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; no BASE_REV-added patch line names 23 assertions
r63 routed defects closed 0 of 4
the pinned do-nothing control at 078eec4a1f6a41c64ff8806f58b46a67cd413bfc is never a certification
```

C2 self-test (`--self-test`, exit 0): `self-test: 0 failure(s) over 32 assertions`
(constructed-world arms `honest/fingerprint`, `look-alike`, `worktree-read`, `hardcoded-count` all report
their want/actual pairs, e.g. `worktree-read: base rc=1 count=0 … target rc=1 count=3 want rc=0 count=4` as
printed).

## 2. `## Sources & frontier` — paste-ready bullets

Census command (before and after), run read-only against byte-exact extracts **and** against the live lane:

```
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin --today 2026-10-24 <lane-dir>   # exit 0 / 0
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census   --root /home/vgpnk/Projects/shokunin <lane-dir>                     # exit 0 / 0
```

- Rows before → after: **117 → 118** (`census`, exit 0 at each rev; live lane `kotoba` `rows 118`, exit 0).
  `validate` exits 0 at both revs and prints 16 `W04` at each, so the W04 set is unchanged
  (`census-before.txt` is the base run); `missing 0` at both. Row count by hand:
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 117 (base) / 118 (tip).
- Rows added by tier: **A +1** — `tier.A` **114 → 115** (base 114 A / 2 B / 1 C; tip 115 A / 2 B / 1 C;
  `status.mined` 109 → 110; `status.queued` 7 → 7; `status.rejected` 1 → 1). S120 — Petrović, Ivanković,
  Fraser & Just, "Practical Mutation Testing at Scale: A view from Google" (`paper`, tier A; the opened
  artifact is `arXiv:2102.11378v2` HTML, 26 Feb 2021 — the journal version is IEEE TSE 48(10):3900–3912,
  Oct 2022 issue, DOI 10.1109/TSE.2021.3107634, and its metadata came from Crossref only, the IEEE HTML was
  not opened); scope: mutation-kill as the adequacy witness for a covered-but-unasserted guard branch
  ("survival, not line coverage, locates an unasserted effect at covered code"), with the
  equivalent-mutant caveat. Snapshot `.ufo/waves/round-64/snapshots/S120.page` (571,600 B, sha256
  `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8`); quote ≤25 words at snapshot
  lines 283-284: "Mutation analysis assesses a test suite's adequacy by measuring its ability to detect
  small artificial faults, systematically seeded into the tested program" (22 words); fetched 2026-10-24,
  HTTP 200. B/A: no other tier moved, no existing row re-tiered.
- Rows touched old → new: **S120 new → `mined`** (opened 2026-10-24, recheck 180d; `used-by`
  `corpus/knowledge/g7-span-pinning-round64.md`, `corpus/lessons/round-64.md` — both exist at `c019919c`,
  `validate` E11 clean); **S049 `mined` unchanged** — line 62 of `corpus/SOURCES.md` is byte-identical at
  both revs (sha256 `3a9607dd315acb298a21701089a4685b06838f3a944b88d16cfc5e6fb48622d1` at each), recheck
  `90d` unchanged; the 2026-10-24 re-probe is a search-log append, no field rewritten
  (seat probe: `w1/ScoutS049.md`, both request profiles reproduce, the 2026-10-22 17,403 B receipt does
  not). The registry's row-id set changes by exactly one entry: `diff` of `^| S[0-9]{3}` → `117a118 > | S120`.
- Search-log appends: **2 bullets, both dated 2026-10-24** — (i) the S120 opening (8 identified, 8 screened,
  1 included, 7 excluded, with the three-field correction of the plan's candidate citation: no Ernst, IEEE
  TSE 2022 not ICSE 2021, `arXiv:2102.11378v2` not `2103.02722`); (ii) the S049 live-context re-probe
  (probed 2026-10-24T03:35:37Z; default `Accept` 200, 17,252 B, sha256 `dae9d3ec…`; `Accept:
  text/markdown` 404, 389 B, sha256 `4f98eb06…`; neither profile restores the 17,403 B receipt).
  `corpus/SOURCES.md` gains 43 lines net at `c019919c` (row + blank + the two bullets).
- Frontier rows advanced: no queued row moved; S120 enters as a new `mined` core row and is the round's
  sourced claim — the round-64 knowledge entry cites it in its provenance trio and teaches cell, and the
  lesson cites the same row.
- Rejected with reasons (Gate, from the search-log bullet): 8 identified / 8 screened / 1 included /
  7 excluded — FSE 2014 "Are Mutants a Valid Substitute…" (different claim, not opened), ICSE-SEIP 2018
  "State of Mutation Testing at Google" (superseded by the included paper), Jia & Harman TSE 2011
  (secondary survey, duplicates the scope), the Bitcoin experience report (single system, not opened),
  ICSE 2021 "Does mutation testing improve testing practices" (different question, not opened),
  `arXiv:2103.02722` (wrong work — a Markov jump process paper), DOI 10.1109/ICSE43902.2021.00068 (wrong
  work — Chen et al., DL mobile deployment faults). Stop rationale: both plan identifiers were opened and
  rejected, and the title-matched primary carries both located quotes the `teaches` cell needs.

## 3. `## Landed changes` — paste-ready bullets

- `c04fffb` — plan freeze (pre-round, at dispatch): `plans/round-64.md` (197 lines) +
  `.ufo/waves/round-64/census-before.txt` (17 lines: 16 `W04` + the `ok` line) — 2 files, +214. `LOG.md`
  tie: none at this rev; the round-64 entry opens under the data commit and its Frontier bullet carries the
  census line.
- `5613392` — errata E1–E3 declared pre-data: `plans/round-64.md` +168 — 1 file. `LOG.md` tie: none; the
  round-64 entry's C2 bullet names `5613392d` as the erratum-declaration commit.
- `c019919c` — wave-1 integration: C1's four G7 arms (+34 lines in `verifiers/check_scoped_rules_v32.py`,
  223 assertions), the new `verifiers/check_r64_routed_repairs.py` (969 lines, 32-assertion self-test),
  the before-controls, the S120 snapshot, both `LOG.md` blocks (corrections + round entry), `corpus/
  SOURCES.md` (+43), `corpus/knowledge/g7-span-pinning-round64.md`, `corpus/lessons/round-64.md`,
  `corpus/QUALITY.md`, `corpus/README.md`, `SKILL.md`, the inherited `MutW2SplitClauses.md` edit and the
  `ExecW2E2Patch.md` drift note, and the 32-seat w1 evidence tree + dispatch/spec JSON — **51 files,
  +15,771 / −32**. `LOG.md` tie: `### Round-63 corrections` (defects 1–4 + the M95 census) and
  `## 2026-10-24 — Round 64` (inherited state, C1, C2, counted citation line, counted axis line, Frontier,
  Mistakes, Round shape, No-harm, Receipts; +22 lines total).
- `b99fb79` — measurements: `receipts/` (`C1-span-measure.txt`, `C1-span-kill.txt`,
  `C2-r64-measure.txt`, `noharm-tip.txt`), `SCORECARD.md` round-64 annotations + Next-65, `SHONEN.md`,
  `corpus/README.md`, w2 spec/dispatch — 10 files, +893 / −5. `LOG.md` tie: none added; the round entry's
  Receipts bullet names all three claim receipts (the `noharm` and `census-after` names in that bullet and
  in No-harm/Frontier do not match the tree — see F1/F2/F3).

Full file list of the data commit, verbatim from `git show --stat c019919c`:

```
commit c019919c97ab5fe98e87a7754b4449ea4e699c99
Author: kotoba-shokunin <kotoba@shokunin.local>
Date:   Sat Oct 24 00:43:39 2026 -0300

    round-64: wave-1 integration — C1 G7 span_missing pinning arms (223 assertions, hardened arm 4), C2 r64 routed-repairs counter (32-assertion self-test), LOG corrections block + round-64 entry, S120+entry+lesson+Q60, inherited MutW2SplitClauses edit + ExecW2E2Patch drift note, w1 evidence + controls

 .ufo/waves/round-63/w2/ExecW2E2Patch.md            |    4 +
 .ufo/waves/round-63/w2/MutW2SplitClauses.md        |  111 +-
 .ufo/waves/round-64/controls/C1-before.txt         |   11 +
 .ufo/waves/round-64/controls/C2-before.txt         |    6 +
 .ufo/waves/round-64/snapshots/S120.page            | 3838 ++++++++++++++++++++
 .ufo/waves/round-64/w1-dispatch.err                |    0
 .ufo/waves/round-64/w1-dispatch.json               |  523 +++
 .ufo/waves/round-64/w1-spec.json                   |  270 ++
 .ufo/waves/round-64/w1/ConnSibling.md              |  113 +
 .ufo/waves/round-64/w1/CriticC1Bound.md            |  327 ++
 .ufo/waves/round-64/w1/CriticC2Bound.md            |  129 +
 .ufo/waves/round-64/w1/ExecCalibVerify.md          |  121 +
 .ufo/waves/round-64/w1/ExecCensusAfter.md          |   78 +
 .ufo/waves/round-64/w1/ExecGateRow.md              |   88 +
 .ufo/waves/round-64/w1/ExecNoHarmBase.md           |  133 +
 .ufo/waves/round-64/w1/ExecR64Counter.md           |  990 +++++
 .ufo/waves/round-64/w1/ExecReceiptTemplates.md     |  132 +
 .ufo/waves/round-64/w1/ExecSeatDriftFix.md         |   39 +
 .ufo/waves/round-64/w1/ExecSpanArms.md             |  114 +
 .ufo/waves/round-64/w1/ExecSpanBefore.md           |  114 +
 .ufo/waves/round-64/w1/MutR64Counter.md            |  454 +++
 .ufo/waves/round-64/w1/MutSpanArms.md              |  449 +++
 .ufo/waves/round-64/w1/RevC1Predicate.md            |  528 +++
 .ufo/waves/round-64/w1/RevC2Checks.md              |  729 ++++
 .ufo/waves/round-64/w1/RevSourcesGate.md           |  780 ++++
 .ufo/waves/round-64/w1/RevSpotcheckCrosswalk.md    |  372 ++
 .ufo/waves/round-64/w1/ScoutQualityDebt.md         |  230 ++
 .ufo/waves/round-64/w1/ScoutReceiptSweep.md        |  270 ++
 .ufo/waves/round-64/w1/ScoutS049.md                |  118 +
 .ufo/waves/round-64/w1/ScoutS120.md                |   98 +
 .ufo/waves/round-64/w1/ScoutS120Alt.md             |  123 +
 .ufo/waves/round-64/w1/ScoutSiblingOverlap.md      |  113 +
 .ufo/waves/round-64/w1/ScribeEntry.md              |  341 ++
 .ufo/waves/round-64/w1/ScribeLOGCorr.md            |  180 +
 .ufo/waves/round-64/w1/ScribeLesson.md             |  604 +++
 .ufo/waves/round-64/w1/ScribeQ60.md                |  223 ++
 .ufo/waves/round-64/w1/ScribeReportSkeleton.md     |  166 +
 .ufo/waves/round-64/w1/ScribeSCORECARD.md          |  383 ++
 .ufo/waves/round-64/w1/ScribeSHONEN.md             |  257 ++
 .ufo/waves/round-64/w1/ScribeSOURCESRow.md         |  548 +++
 .ufo/waves/round-64/w1/swarm-registry.json         |  329 ++
 LOG.md                                             |   22 +
 SKILL.md                                           |    1 +
 corpus/QUALITY.md                                  |    3 +-
 corpus/README.md                                   |    2 +-
 corpus/SOURCES.md                                  |   43 +
 .../knowledge/compound-clause-citation-round63.md  |    6 +-
 corpus/knowledge/g7-span-pinning-round64.md        |  129 +
 corpus/lessons/round-64.md                         |  158 +
 verifiers/check_r64_routed_repairs.py              |  969 +++++
 verifiers/check_scoped_rules_v32.py                |   34 +
 51 files changed, 15771 insertions(+), 32 deletions(-)
```

## 4. Findings (consistency), each against committed bytes

**F1 — `LOG.md` names `controls/noharm-base.txt`, which no revision contains.**
Round-64 entry, `Receipts.` bullet: "`.ufo/waves/round-64/controls/`: `C1-before.txt`,
`C2-before.txt`, `noharm-base.txt`." Measured:
`git ls-tree -r --name-only c019919c .ufo/waves/round-64/ | grep noharm` → no output;
at `b99fb79` → `.ufo/waves/round-64/receipts/noharm-tip.txt` only; the live `controls/` directory holds
exactly `C1-before.txt` and `C2-before.txt`. No `noharm-base.txt` exists at either rev or in the worktree
(seat evidence `w1/ExecNoHarmBase.md` measured the base column, but the named file was not committed).

**F2 — `LOG.md` names `census-after.txt`, which no revision contains.**
Round-64 entry, `Frontier.` bullet: "Census: before 16 W04 exit 0 → after 16 W04 exit 0
(`census-before.txt` / `census-after.txt`)". Measured: `git ls-tree -r --name-only {c019919c,b99fb79}
.ufo/waves/round-64/ | grep census` → `.ufo/waves/round-64/census-before.txt` at both revs, nothing else;
the live round directory also has no `census-after.txt`. The *numbers* are right (this seat re-ran both:
16 `W04`, exit 0, base and tip), the receipt path is not.

**F3 — the committed no-harm receipt at `b99fb79` is a `c019919c` run with two failing arms, and the
working tree holds an uncommitted `b99fb79` run that passes.** `git diff` on
`.ufo/waves/round-64/receipts/noharm-tip.txt` (index = committed at `b99fb79`, worktree = current):

```
-noharm: tip         c019919c97ab5fe98e87a7754b4449ea4e699c99
-noharm: sandbox     /tmp/kotoba-r62-noharm.DgdHZ6
-noharm: date -u     2026-10-24T04:10:41Z
+noharm: tip         b99fb79c27042e0f8a598cbbb4d81479a806b518
+noharm: sandbox     /tmp/kotoba-r62-noharm.F4Ix1g
+noharm: date -u     2026-10-24T04:18:14Z
-FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/knowledge/g7-span-pinning-round64.md corpus/lessons/round-64.md
+PASS  corpus-idx  no new unindexed corpus file at tip (base set: corpus/lessons/round-62-verifier-spotcheck.md corpus/lessons/round-63-verifier-spotcheck.md )
-FAIL  check-ptr   unresolved citation pointers grew (base=3 tip=4)
-        tip: FAIL governance.citation_resolves: evaluated 1190 — LOG.md:2533: '.ufo/reports/round-60/kotoba.md' does not resolve from
-        tip:  LOG.md:2580: '.ufo/watchdog.log' does not resolve from
-        tip:  LOG.md:2602: '.ufo/waves/round-64/receipts/C1-span-measure.txt' does not resolve from
-        tip:  LOG.md:2603: '.ufo/waves/round-64/receipts/C2-r64-measure.txt' does not resolve from
+PASS  check-ptr   unresolved citation pointers did not grow (base=3 tip=3)
```

Committed sha256 `d4f5f29a8e1de47f4fa2684d6542b4ae3aa905801ca5c4c5f04998fbbcbdded1`; worktree sha256
`1c5a5274751770db89b9a46618dce0aecabb275d2a0ad607ac08926a5755c6c9`. Consequence for the report: a
"no-harm all arms PASS at the round-64 tip" sentence is true only of `b99fb79`; at the measured data tip
`c019919c` the committed receipt records 5 PASS / 2 FAIL, both failures being commit-ordering artifacts
(the two new corpus files were unindexed, and `LOG.md` cited receipts that landed in the next commit).
The `LOG.md` No-harm bullet states no result at all ("`noharm-battery.sh --base 078eec4 --tip
<round-64 tip>`; gate registry at base 41 of 41, exit 0"), so it does not contradict the receipt, but it
also does not disclose the two red arms.

**F4 — the frozen C2 second conjunct says `BASE_REV` is "never a command-line argument" while the frozen
command passes it on the command line.** The predicate text (plan `:102-113`, the second command at
`:111`) spells
`--rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc`; the code takes the special refusal branch on that value
(`if rev.lower() == BASE_REV:` → prints `the pinned do-nothing control at … is never a certification`) and
exposes no `--base` option (`--base` → exit 2, `error: unrecognized arguments`). Both readings are
consistent with the code; the sentence and its own command do not read alike.

**F5 — the plan's C1 four-line block is printed as a set, not as a contiguous block, at both revs.**
Base and tip both print `must-fail E2e …` and `must-fail G7 …` between `survivors closed` and
`must-fail G9 …` (measured, §1.1). A "prints all four lines" reading holds; a strict "prints this block
verbatim and contiguously" reading does not, and did not hold at the base either.

**F6 — each claim receipt is the raw run plus a pinned header/footer, not a different measurement.**
`diff` of this seat's C1 run against `receipts/C1-span-measure.txt` shows the 21 output lines byte-identical
and only four added lines: the two-line header (`C1 measure — …`, `Command: …`) and the footer (`exit=0`,
`counter sha256: f8f69cad…`). `diff` of the `--rev c019919c` run against `receipts/C2-r64-measure.txt`
shows the five result lines byte-identical plus the footer pair `counter sha256: 8f5b9f91…` and
`self-test: 0 failure(s) over 32 assertions`. `controls/C2-before.txt` is byte-identical to the raw
`--rev 078eec4` run with no footer at all.

**F7 — receipt names in the skeleton differ from the landed names.** The skeleton expects
`receipts/C1-span-arms-measure.txt` and `receipts/C2-counter-measure.txt`; the landed files are
`C1-span-measure.txt`, `C1-span-kill.txt` and `C2-r64-measure.txt`. The report text must use the landed
names (used above). [INFERENCE] the skeleton predates the seat-chosen names; no artifact is missing.

**F8 — S120's `used-by` targets and the E11 gate are clean.** `corpus/knowledge/g7-span-pinning-round64.md`
and `corpus/lessons/round-64.md` both exist at `c019919c`; `validate` prints `ok` and `missing 0`, so the
new row does not carry a missing-path violation. The row sits after a blank line following S119
(`corpus/SOURCES.md:131` blank, S120 at `:132`) but inside `## Registry` (the section ends at `## Paths`),
so E12 does not fire — the wave-1 scan's "delete the blank line" note is style, not a census error.

## 5. Scope, limits, out-of-scope

- Measured by this seat: C1 self-test at both revs; the SM1 mutant at both revs; both C2 conjuncts; the C2
  self-test; the `--base` rejection; census `census`/`validate` at both revs and on the live lane; the
  receipt/control diffs; the `git show --stat` file list; S120's row fields, snapshot size and hash; the
  S049 line hash; the search-log append count.
- Not done here (other seats or the L1 own it): no S120 re-fetch (the row's 2026-10-24 fetch evidence is
  reported, not reproduced); no `noharm-battery.sh` run (F3 quotes the committed receipt); no gate-registry
  run; no review of the wave-1 seat reports beyond the ones cited; no SCORECARD/SHONEN recount; no
  disposition of the two claims — this is evidence fill, not judgment.
- Scratch: `/tmp/r64w2/{base,tip,clone,sm1,sm1base}`. Lane untouched; no git/jj writes; no package
  transactions.
- Concurrent lane change observed (not by this seat): at this seat's start `git status --short` showed only
  `M .ufo/waves/round-64/receipts/noharm-tip.txt` and `?? .ufo/waves/round-64/w2/`; by the end
  `corpus/SOURCES.md` was also modified (`git diff --stat` → `50 insertions(+), 3 deletions(-)`), the
  separating blank line before S120 removed (S120 now at `corpus/SOURCES.md:131`, S119 at `:130`) and a
  search-log line near `:179` reflowed. `validate` on that worktree state is still `ok`, exit 0, 16 `W04`.
  Every §2 number above is anchored to the committed bytes of `c019919c` (and the live lane as it stood at
  `b99fb79`), not to this later worktree state; report text should cite the commit, not the worktree.
