# ReviewD1D5Facts — round 50 build, D1 + D5 facts (2026-10-22)

CONFIRMED — both routed-defect fact sets verified read-only; D1: four round-49 addenda each rewrote
only line 4 (the lane-head pointer) and appended at EOF, nothing else removed; D5: the round-49
lesson § Gate does say `rejected 0` while at least three reject decisions are visible in the plan
and wave files. Per the spot-check's fix, the round-50 report must leave the filed header alone and
state the current lane head inside each appended addendum.

Seat: KotobaR50.ReviewD1D5Facts (reviewer, leaf — no subagent dispatch). Judged on: calibration.
Fleet repo read-only git only; lane untouched except this report. Tools installed: none.

## D1 — round-49 report addendum mechanics (fleet repo, read-only git)

Commits touching `.ufo/reports/round-49/kotoba.md`
(`git log --format='%h %s' -- .ufo/reports/round-49/kotoba.md`, exit 0, newest first):

- `c688a71` round-49: kotoba report addendum 4 (all seats returned; lane 374ecf9)
- `87de5ea` round-49: kotoba report addendum 3 (lane 9f2f1a7)
- `5d2774f` round-49: kotoba report addendum 2 (lane 2272019)
- `ecb3a52` round-49: kotoba report addendum (late falsify seats; lane b38bc0d)
- `8bf9073` round-49: kotoba report  (base filing; created the file, 116 lines)

Per-addendum `git diff -U0 <c>^ <c> -- .ufo/reports/round-49/kotoba.md` (all exit 0):

| commit | summary | line 4 rewrite (sole deletion) | append hunk (pure insertion) |
|---|---|---|---|
| ecb3a52 | 13 insertions(+), 1 deletion(-) | `pushed lane head bfd5a583…` → `pushed lane head b38bc0d4…` (+ parenthetical "late corrections after the first report filing at lane `bfd5a58`") | `@@ -116,0 +117,12 @@` — 12 lines, `## Addendum (late falsify seats, after the first report filing)` |
| 5d2774f | 8 insertions(+), 1 deletion(-) | `b38bc0d4…` → `22720198…` | `@@ -128,0 +129,7 @@` — 7 lines, "Second late batch (lane `2272019`)" |
| 87de5ea | 9 insertions(+), 1 deletion(-) | `22720198…` → `9f2f1a75…` | `@@ -135,0 +136,8 @@` — 8 lines, "Third late batch (lane `9f2f1a7`)" |
| c688a71 | 5 insertions(+), 1 deletion(-) | `9f2f1a75…` → `374ecf98…` | `@@ -143,0 +144,4 @@` — 4 lines, "Final batch (lane `374ecf9`, evidence only)" |

- Line 4 was rewritten in every addendum, always to the then-current lane head:
  `bfd5a583` → `b38bc0d4` → `22720198` → `9f2f1a75` → `374ecf98`.
- Nothing else was removed: each commit's summary shows exactly 1 deletion, and the only `-` line in
  each diff is line 4. Arithmetic closes it — appended lines + 1 = insertions (12+1=13, 7+1=8,
  8+1=9, 4+1=5); the truncation-elided diff lines all sit inside `@@ -X,0 +Y,N @@` hunks, which are
  insertions by header. This independently reproduces the spot-check row
  `corpus/lessons/round-49-verifier-spotcheck.md:27` (pass, with a defect (D1)).
- Base filing line 4 (`git show 8bf9073:…`, exit 0): `pushed lane head
  bfd5a583a9ba5e7ab702cca301ec2c44c8bf5287 (jj-lane.sh `landed`). Attempt 1. Plan`. Working-tree
  head line 4 today: `pushed lane head 374ecf9820722e34f55ee21f3a27419b61aafc06 (jj-lane.sh
  `landed`; late corrections after the first report filing at lane `bfd5a58`). Attempt 1. Plan`.

### Append-only pattern the round-50 report must follow

Routed defect D1 (`corpus/lessons/round-49-verifier-spotcheck.md:216-218`): "Each of the four
addenda rewrote report line 4, the 'pushed lane head' pointer. The four addenda were all appended
correctly. **Next time, state the current head inside the addendum and leave the filed header
alone.**"

So for round 50 (`.ufo/reports/round-50/kotoba.md`):

1. On first filing, line 4 records the lane head as pushed at that moment — and is then frozen.
2. Every addendum is a new block appended at the end of the file (`## Addendum (…)`), and **the
   current lane head goes inside that appended block** (e.g. "lane head `<40-hex>` at this
   addendum"), never as a rewrite of line 4 or any other filed line.
3. No filed line is ever removed or rewritten; addenda only grow the file. This matches the
   round-50 plan's D1 line ("report addenda append at the end; line 4 is never rewritten").

(Note the asymmetry with round 49 practice: there line 4 carried the newest head and was rewritten
once per addendum. Round 50 must not do that; the D1 fix moves the live head pointer into the
addendum body.)

## D5 — round-49 Gate says `rejected 0`, reject decisions visible elsewhere

### The Gate line (confirmed)

`corpus/lessons/round-49.md:19` is `## Gate`; `:21-22` reads: "**Knowledge entries:** candidates 1,
admitted 1 (`corpus/knowledge/sibling-overlap-census-round49.md`), **rejected 0**." The round-48
erratum at `:26-27` also says rejected 0 (for round 48). `:24` records one override — "One seat
classification was overridden (kotodama `none` → `adjacent`), with the reason stated in the entry"
— but the Gate line still counts rejected 0. This is exactly what the spot-check's D5 names
(`round-49-verifier-spotcheck.md:230-233`): "The lesson § Gate records 'rejected 0', but the round
did reject: the withdrawn kasegi clause, the overridden seat calls, and the re-sized counters."

### Reject decisions visible in `plans/round-49.md` (path:line)

- `plans/round-49.md:35-38` — C1 re-sizing: the declared name-count after-value was **replaced
  before landing** by the classified-row count ("the name count above is satisfied by a bare list
  of 20 names… The declared after-value is replaced, before anything lands, by a row count…").
- `plans/round-49.md:63-67` — C2 re-sizing: the declared disposition-count after-value was
  **replaced before landing** by the box proof ("the disposition count reads 2 when both boxes are
  mapped to an unrelated instrument or to a ten-byte shell stub… replaced, before anything lands").
- The plan carries no literal `reject` token (case-insensitive grep for `reject` → 0 matches,
  grep exit 1); the two re-sizings are the plan-visible rejections, recorded as replacements.

### Reject decisions visible in `.ufo/waves/round-49/` (path:line)

- Re-sized counter #1: `.ufo/waves/round-49/build/CriticC1Sizing.md:12-15` — "As sized, the
  after-value repeats R2… The plan mines M29 ('content-blind counter') and then declares another
  content-blind counter."
- Re-sized counter #2: `.ufo/waves/round-49/build/CriticC2Sizing.md:16-19` — mapping both boxes to
  an unrelated existing instrument, or to a ten-byte stub, yields counter 2 with map PASS exit 0;
  evidence lines `:92-95`.
- Withdrawn kasegi clause: `.ufo/waves/round-49/build/CensusKasegi.md:26-31` — "Not `adjacent` at
  this pin — and kotoba's existing clause is unsourced"; `prompt[- ]injection` has zero matches in
  the whole kasegi tree. Landed withdrawal confirmed by the falsify wave:
  `.ufo/waves/round-49/falsify/CriticC1Landed.md:32` ("The unsourced kasegi 'prompt-injection'
  clause is withdrawn (M30)") and `.ufo/waves/round-49/falsify/RowKasegi.md:55-59` ("is withdrawn":
  the judged PROVINCE kasegi row carries no such clause. HOLDS).
- Overridden seat call (kotodama): the seat classified `none` —
  `.ufo/waves/round-49/build/CensusKotodama.md:1` (row cell `none`), `:11` ("Classification
  `none`"), `:19` ("Why not `adjacent`") — overridden to `adjacent` per
  `corpus/lessons/round-49.md:24`; the falsify critic flagged the asymmetric reading at
  `.ufo/waves/round-49/falsify/CriticC1Landed.md:24`.
- First-landing kake/kasegi `none` rejected by the falsify wave and reclassified `adjacent`:
  `.ufo/waves/round-49/falsify/CriticC1Landed.md:1` (FAILS — "kake and kasegi are `none` although
  kotoba's own description states the split") and `.ufo/waves/round-49/falsify/RowKake.md:17`
  (hand arithmetic: kake and kasegi together give 9 adjacent / 11 none). The spot-check sample table
  records the decision: `corpus/lessons/round-49-verifier-spotcheck.md:176` ("reject (falsify wave;
  reclassified `adjacent`)").
- Context, not round-49 decisions: `.ufo/waves/round-49/falsify/ReviewLessonQ25.md:46` confirms the
  Gate line "candidates 1, admitted 1, rejected 0" was present; `:49` records SOURCES
  `status … rejected=1` — that is S011, the Agentman tutorial row rejected 2026-10-19
  (`corpus/SOURCES.md:24`), which predates round 49. `.ufo/waves/round-49/build/R4CountProvenance.md:94-97`
  quotes the round-48 erratum "rejected 0" and records the second-candidate sweep (0 hits).

Count: 5 reject-shaped decisions visible across plan + waves — 2 re-sized counters, 1 withdrawn
clause, 1 overridden seat classification, 1 falsify-wave reclassification of two rows — against a
Gate line of `rejected 0` that counts knowledge-entry candidates only.

## Evidence (commands, exit codes)

- `git -C /home/vgpnk/Projects/shokunin log --format='%h %s' -- .ufo/reports/round-49/kotoba.md`
  → exit 0, 5 commits (listed above).
- `git -C /home/vgpnk/Projects/shokunin diff -U0 <c>^ <c> -- .ufo/reports/round-49/kotoba.md` for
  c ∈ {ecb3a52, 5d2774f, 87de5ea, c688a71} → exit 0 each; summaries and hunks as tabulated.
- `git -C /home/vgpnk/Projects/shokunin show 8bf9073:.ufo/reports/round-49/kotoba.md` (first 6
  lines) → exit 0; read of working-tree `.ufo/reports/round-49/kotoba.md:1-10` → line 4 =
  `374ecf98…`.
- grep `reject|Reject|REJECT` on `plans/round-49.md` → no matches (grep exit 1).
- grep sweeps on `plans/round-49.md`, `corpus/lessons/round-49.md`,
  `corpus/lessons/round-49-verifier-spotcheck.md`, `corpus/SOURCES.md` and
  `.ufo/waves/round-49/**` → all exit 0 with the lines cited above.
- All reads via `read`/`grep` tools; no lane file besides this report was created or modified; no
  git write command and no `jj` command was run anywhere.

## Residual risk and verification gaps

- Per-addendum diffs were checked via git's summary line plus the `-U0` hunks shown; content hidden
  by output truncation sits only inside pure-insertion hunks (verified by the insertions/deletions
  arithmetic), so a hidden deletion is excluded arithmetically, not by eyeballing every line.
- The "reject decisions" list is the spot-check's own D5 enumeration plus what a token sweep of
  plan + waves surfaces; a reject decision recorded nowhere in those two locations would not appear
  here (none was claimed by the spot-check beyond the five listed).
- Whether round-50's report contract (.ufo/prompts template) restates the D1 rule was not checked —
  out of scope for this seat; the binding statement cited is
  `corpus/lessons/round-49-verifier-spotcheck.md:216-218`.

Report: `.ufo/waves/round-50/build/ReviewD1D5Facts.md`
