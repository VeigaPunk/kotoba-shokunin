# ReviewD1ReportPattern — round 50 falsify, routed defect D1 (report record)

**FAILS** — applies to the D1 disposition's rule wording: `corpus/lessons/round-50.md:115-117` at judged bytes `956ee16`, and byte-identical at lane head `a78fec1` (lines 116-118). The round-49 facts it cites **HOLD** (reproduced below). Round-50 report history: not checked, because `.ufo/reports/round-50/kotoba.md` does not exist (checked at start and at finish).

Seat: KotobaR50.ReviewD1ReportPattern (reviewer, leaf, no subagent). Judged on: calibration. Writes: this report, and scratch files under `/fast/scratch/hyaku/kotoba-r50/falsify/ReviewD1ReportPattern/`. Git read-only (`--no-optional-locks`). No jj command, no git write, no lane file changed. Tools installed: none.

## Findings

1. **F1, moderate: the D1 bullet contradicts itself.** The bullet says the report "keeps its filed header", then cites "one line-4 rewrite per addendum" as the "confirmed round-49 pattern". That rewrite is the defect. The round-49 spot-check says so: "Each of the four addenda rewrote report line 4 … Next time, state the current head inside the addendum and leave the filed header alone" (`corpus/lessons/round-49-verifier-spotcheck.md:216-218`). The round-50 plan agrees: "line 4 is never rewritten" (`plans/round-50.md:43`). The seat report says "Round 50 must not do that" (`.ufo/waves/round-50/build/ReviewD1D5Facts.md:60-62`), and the lesson drops that sentence. A later addendum writer who follows the parenthetical would repeat the defect.
2. **F2, moderate: the plan's rule covers less than it must.** The plan forbids rewriting line 4 only. The spot-check says "leave the filed header alone". Neither forbids a body edit. Fleet protocol says corrections land as new commits, and append-only records never take an in-place rewrite (`PROTOCOL.md:123-124`). The exact rule must cover every filed line. Round 49 edited no body line, but no round-50 text forbids it.
3. **F3, minor: no counter.** Q26 asks that a statement say only what its counter measures. The D1 bullet names no counter. Rule R4 below supplies one.
4. **F4, minor: citation.** The lesson cites `ReviewD1D5Facts.md` with no path. The file is `.ufo/waves/round-50/build/ReviewD1D5Facts.md`.
5. **F5, info: the lane head moved during this run.** Judged bytes are `956ee16`. The lane landed `a78fec1` ("round-50: falsify corrections …"; `git log --format='%h %s' 956ee16..a78fec1` → 1 commit; `git diff --stat 956ee16 a78fec1` → 34 files, +3655 −26). In it, the M32 row that was uncommitted at `956ee16` landed (`git show a78fec1:corpus/lessons/round-50.md | grep -c '^| M32 Misroot'` → 1). The D1 bullet and plan line 43 are unchanged (`cmp` exit 0 for both). The lesson has one removed line since judged: the first line of the D3 bullet, rewritten in place (robust count `git diff -U0 956ee16 a78fec1 -- corpus/lessons/round-50.md plans/round-50.md | awk 'f && /^-/{r++} /^@@/{f=1} END{print r+0}'` → 1). That is outside D1 and I did not judge it, but it is the same in-place class; flag it to the lesson owner.

Round 49 needs no action: its history stays as filed (fleet protocol: history is never rewritten).

## Round-49 evidence (HOLDS, reproduced)

- `git log --format='%h %s' -- .ufo/reports/round-49/kotoba.md` lists five commits: filing `8bf9073` (116 lines), then addenda `ecb3a52`, `5d2774f`, `87de5ea`, `c688a71`.
- Each addendum commit changes one file (`git show --stat --format= <c>`: "1 file changed").
- Each addendum diff (`git diff -U0 <c>^ <c> -- <report>`) has two hunks: `@@ -4 +4 @@` (line 4 replaced) and one pure end-of-file insertion (`@@ -116,0 +117,12 @@`, `@@ -128,0 +129,7 @@`, `@@ -135,0 +136,8 @@`, `@@ -143,0 +144,4 @@`). Line 4 is the only removed line in each.
- Line 4's head moved `bfd5a58` → `b38bc0d` → `2272019` → `9f2f1a7` → `374ecf9`. Final report: 147 lines (`git show c688a71:<report> | wc -l`). Working tree equals HEAD (`git diff --stat HEAD -- <report>` empty, exit 0).
- The seat's D1 facts (`ReviewD1D5Facts.md` §D1) and the spot-check row at `round-49-verifier-spotcheck.md:27` reproduce.

## Exact rule for the round-50 report and any later addendum

- **R1 Filing.** The first commit creates `.ufo/reports/round-50/kotoba.md`. Line 4 names the lane head pushed at filing, and that line is then frozen. (Prompt §6 item 4: "The report lands last and cites the pushed lane hash", `.ufo/prompts/kotoba-round-50.md:317`.)
- **R2 Addendum.** One new block at the end of the file: a blank line, then `## Addendum (<what it records>)`. The block names the lane head it describes, citing only the helper's `landed <hash>` line (prompt line 273). The lane head lives in the lane repo, so the block cannot name its own fleet commit.
- **R3 Nothing filed changes.** No filed line, line 4 included, is edited, reflowed, reordered or removed. A correction is a new sentence in the block that names the filed line and the corrected value (`PROTOCOL.md:123-124`).
- **R4 Landing and check.** Each addendum is its own fleet commit, limited to the report path (`git commit -- .ufo/reports/round-50/kotoba.md`; `PROTOCOL.md:490-492`). For each addendum commit `c`, with `n` = line count of `c^`'s copy of the report, this must print `removed 0 non_EOF 0`:

```
git -C /home/vgpnk/Projects/shokunin diff -U0 c^ c -- .ufo/reports/round-50/kotoba.md | awk -v n=<n> 'f && /^-/{r++} /^@@/{f=1; h++; if ($0 ~ "^@@ -" n ",0 [+]") e++} END{print "removed", r+0, "non_EOF", h-e+0}'
```

Do not use `grep -cE '^-[^-]'`. A removed markdown bullet `- item` shows in the diff as `-- item`, and that pattern misses it (scratch M2 below).

Suggested replacement for lesson lines 115-117 (116-118 at `a78fec1`): "**D1 (report record):** the round-50 report is append-only. No filed line, line 4 included, is edited, reflowed or removed. Each addendum appends one `## Addendum` block at the end of the file and states the current lane head inside it. The four round-49 addenda each rewrote line 4 (`bfd5a58`→`b38bc0d`→`2272019`→`9f2f1a7`→`374ecf9`); that rewrite is the defect. Check: the R4 one-liner in `.ufo/waves/round-50/falsify/ReviewD1ReportPattern.md` prints `removed 0 non_EOF 0` for each addendum."

R1-R4 match the seat's rule (`ReviewD1D5Facts.md:44-58`) and add body-line coverage, a counter and the landing rule. With F1-F3 corrected, the D1 rule text would HOLD.

## Evidence (commands, exit codes)

- Judged bytes: `git rev-parse HEAD` and `git rev-parse --verify master` both give `956ee1676e4c18480bce8ac3993541462be76e11`; `merge-base --is-ancestor` exit 0. `git show 956ee16:corpus/lessons/round-50.md` lines 115-117 and `git show 956ee16:plans/round-50.md` line 43 read, exit 0.
- Lane head at finish: `a78fec1` (`git rev-parse --short HEAD`), descends from `956ee16` (`merge-base --is-ancestor`, exit 0). D1 bullet at `a78fec1` vs judged: `cmp` exit 0. Plan line 43: `cmp` exit 0.
- Real addenda, R4 one-liner, with n = 116, 128, 135, 143 (`git show <c>^:<report> | wc -l`, exit 0 each): `removed 1 non_EOF 1` for all four (awk exit 0). Filing commit `8bf9073` (`git diff -U0 8bf9073^ 8bf9073 | grep -cE '^-[^-]'`): 0, exit 0.
- Scratch mutants (`/fast/scratch/hyaku/kotoba-r50/falsify/ReviewD1ReportPattern/t2`; base = `c688a71` bytes; n = 147; R4 one-liner, awk exit 0 each):
  - M0 append block only → `removed 0 non_EOF 0` (PASS)
  - M1 line-4 head rewrite → `removed 1 non_EOF 1` (FAIL)
  - M2 body bullet rewritten → `removed 1 non_EOF 1` (FAIL); naive `^-[^-]` count → 0
  - M3 insertion mid-file → `removed 0 non_EOF 1` (FAIL)
  - M4 `Attempt 1` → `Attempt 2`, same line count → `removed 1 non_EOF 1` (FAIL)
- Prompt `.ufo/prompts/kotoba-round-50.md` §4 (lines 99-129) has no addendum or header rule. Case-sensitive grep for `pushed lane head|filed header|line 4|addendum block|append-only|never rewritten|Addend` in that file → no match.
- Round-50 report: `test -e .ufo/reports/round-50/kotoba.md` → absent. `git log --format='%h %s' -- .ufo/reports/round-50/kotoba.md` → 0 commits (exit 0). Checked at start and again at finish; fleet HEAD moved `54ffccb` → `584c4a6` → `8d56eb1` in between, and the round-49 history was unchanged. `.ufo/reports/round-50/` holds only `kotodama.md` (tracked, `ba557b1`).

## Residual risk and gaps

- No real round-50 addendum exists. R1-R4 are tested on round-49 history and five scratch mutants only.
- The append-only reading of reports rests on `PROTOCOL.md:123-124`, which names `LOG.md` as its append-only file and does not name reports, plus the aggregator's reading at `.ufo/reports/AGGREGATE.md:1196` (D-93).
- The verdict covers the judged bytes and the `a78fec1` head. Later lane commits can change the lesson again; re-run the `cmp` on lesson lines 115-117 (judged) or 116-118 (`a78fec1`) before filing.
- Not checked here: the C1/C2 counters, the D2-D6 repairs, S024-S029, Q26, the D3 line rewritten in `a78fec1`, and the D5 facts beyond the seat's report.
