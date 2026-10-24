# ScoutLessonBacklog — round-65 W1 (lesson evidence recheck)

Seat: scout, lane: kotoba. Scope: verify every M-row in
`corpus/lessons/round-65.md` cites evidence that resolves; verify the Gate
quotes are ≤25 words (measured with wc -w / str.split). Read-only outside this
file; all checks re-run on the landed bytes @ tip 0e104f49.

## Verdict: all three M-rows' cited evidence resolves; both Gate quotes pass ≤25w. No falsification found in scope.

## M-row evidence resolution

**M99 — fixture-hermeticity leak.** Receipt
`.ufo/waves/round-65/receipts/M99-fixture-leak.txt` EXISTS (286 B) and records
the two named FAIL classes verbatim:
```
bug A (errata default leaks into fixture): status=FAIL
   ["erratum LOG.md:2111 '.ufo/round-45/drafts/v10/post-r44-hunt.py' is past horizon 2315 or absent"]
bug B (subject line mismatch): status=FAIL
   ["correction LOG.md:2 SCORECARD.md:8 'corpus/gone.md': names no live red subject"]
```
Fix claims verified in source: `check_governance_citations(repo, errata=…, corrections=(), …)` — the
`corrections=()` default is at `verifiers/verify_skill_checklist.py:1739`;
fixture-world calls pin `errata=()` explicitly (lines 2373, 2383, 2394, 2414);
`main()` is the only callsite passing the live table
(`corrections=GOVERNANCE_CORRECTIONS`, line 2763). The "landed self-test green
at 1862 assertions" claim re-run: `python3 -B verifiers/verify_skill_checklist.py --self-test`
→ `0 failure(s) over 1862 assertions`, exit=0 (1.40 s). SUPPORTS C2.

**M100 — self-referential citation.** Receipt
`.ufo/waves/round-65/receipts/C2-selfreference-redbefore.txt` EXISTS (286 B):
```
BACKTICKED notice: status=FAIL
detail: LOG.md:2: 'corpus/gone.md' does not resolve from /tmp/kotoba-redbefore-nkodw7fe; … 1 recorded correction(s) excused
QUOTED notice:     status=PASS (evaluated=1)
```
The landed LOG.md:2619-2621 notices quote tokens in double quotes (not
backticks) — confirmed at the cited lines. The "live run FAILed on
LOG.md:2619-2621" claim is [INFERENCE]-consistent: the checker's live run at
base was fail=1 over 3 named cells (controls/C2-before.txt, 2951 B, exists);
my re-run `… --check governance.citation_resolves` → `PASS … 3 recorded
correction(s) excused`, exit=0. SUPPORTS C2.

**M101 — stale-premise candidate (M97 recurrence).** Resolvement:
`corpus/lessons/round-64.md:68` defines M97 ("frozen plan citing identifiers
no seat had opened") — the rule M101 claims caught it exists. The plan's
frozen record at `plans/round-65.md:123` states: "The plan's first candidate
(arXiv:1309.4818) was opened and REJECTED — it is a mathematics paper
(Carlson's ε-numbers); the row cites the artifact actually opened (M97
discipline, recorded in the search log)." The replacement artifact is real:
`snapshots/S121.pdf` = 1,126,684 B, sha256
`bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3` (recomputed,
matches the Gate's claim); `S121.txt` line 90 carries "Digital Object
Identifier no. 10.1109/TSE.2013.44" and lines 88-89 name Torkar/Józala.
Registry row: `corpus/SOURCES.md:132` = S121 tier A, used-by the knowledge
entry `corpus/knowledge/g7-span-closure-round65.md` (exists, header line 1
cites the same identity/sha). SUPPORTS C1's S121 row + the lesson's claim the
row cites the opened artifact.

## Gate quotes — word counts (measured)

| quote | wc -w | source line | whitespace-normalized substring count in S121.txt |
|---|---|---|---|
| "The experiment indicated that SOM in general and JudyDiffOp strategy in particular provide the best results" | **16** | S121.txt:64-65 (wraps two lines as recorded) | 1 |
| "Empirical results suggest that applying SOMs reduced the number of mutants by approximately 50%, without much decrease in the quality of the test suite." | **24** | S121.txt:1174-1176 | 1 |

Both ≤25. The lesson's parenthetical "(16 words ≤ 25)" and "(24 words)" are
correct to the word.

## Cross-checked peripheral claims in the lesson

- Census before: `census-before.txt` exists, 16 W04 rows + 1 ok line = 17
  lines, matches "16 W04" (the "118 rows" figure is the SOURCES registry row
  count, not the census file's line count — consistent, the row-level census
  reports W04-classed rows only). After: `census-after.txt` exists at tip,
  16 W04 + ok — the lesson's "appended below when run" deferred to the report;
  the file is committed and consistent.
- LOG.md line-sha pins in `GOVERNANCE_CORRECTIONS` recomputed from the live
  file: 2619→`b11e4e8b…`, 2620→`1dcb9d9e…`, 2621→`6836c34a…` — all MATCH the
  table at `verify_skill_checklist.py:417-428`; stale tokens confirmed present
  at LOG.md:2533 (`.ufo/reports/round-60/kotoba.md`), LOG.md:2580
  (`.ufo/watchdog.log`), SCORECARD.md:158 (`.ufo/reports/round-60/kotoba.md`).
- `corpus/knowledge/g7-span-closure-round65.md` and `corpus/lessons/round-65.md`
  both exist at tip (same-commit claim not independently re-verified via VCS —
  jj/git reads allowed but commit-parent proof left to RevReceiptRevs).

## Claims supported / falsified

- C1 (depth closing package): supported indirectly — S121 evidence chain
  resolves end-to-end (PDF sha + txt quotes + registry row + knowledge entry).
- C2 (governance corrections): supported — M99/M100 red-before receipts exist,
  fix mechanism verified in source, live check PASS with 3 corrections excused.
- Falsifications: none found in scope. Minor [INFERENCE] note: M100's claim
  "the live run FAILed on LOG.md:2619-2621 — the notices' own tokens" is a
  pre-fix historical observation; only the red-before receipt is directly
  re-checkable (it holds).

## Tooling / installs

None. Used system python3, sha256sum, wc, awk only. Pacman guard respected
(no pacman transaction).

## Remaining unknowns (out of scope)

- Whether S121.pdf's bytes equal the live URL's bytes at fetch time (HTTP 200
  claim) — network fetch not performed; the committed snapshot self-consists
  (sha in lesson = sha on disk = sha in knowledge entry).
- Commit-level ordering (same-commit landing of S121 row + consumers, the E11
  gate claim) — left to the VCS-literate reviewers.
