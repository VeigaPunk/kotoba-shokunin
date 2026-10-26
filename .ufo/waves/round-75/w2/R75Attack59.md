# R75Attack59 — falsification attack on `R75Facet59.md`

Seat: R75Attack59 (wave-2 falsifier, mutation-tester). Target: `.ufo/waves/round-75/w1/R75Facet59.md`.
Measured revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`git rev-parse HEAD`); read-only, no fetch,
no client run, no lane edit. Scratch `/fast/scratch/hyaku/kotoba-r75/R75Attack59/` used and cleaned.

## Central factual claim under attack

`SKILL.md:166` credits the description-threshold table to `verifiers/check_description_thresholds.py`, but
the counter "measures none of its distinguishing clauses" (count "four", the no-cut negative, the omp-99
pointer); only row presence and quote/number-token equality are checked; `TARGET = 4` collides with the
prose "four"; controls: (a) a clause counter with must-fail arms, or (b) bounding the sentence.

## Verification — every measured claim reproduced at `65a5c7a`

| Facet claim | My measurement | Verdict |
|---|---|---|
| Sentence verbatim at `SKILL.md:166`; table `:164-177`; pointer `:153-156` is only a redirect | `git show 65a5c7a:SKILL.md` sed slices: `:166` matches word-for-word; `:155-156` = pointer to `anatomy-and-compression.md` § Moved (round 72) | holds |
| Exactly four threshold cells carry a 1024 token: VS Code `:172`, Copilot CLI `:173`, Cursor `:175`, opencode `:176` | probe parse of `git show` bytes: `['VS Code', 'Copilot CLI', 'Cursor', 'opencode']` | holds |
| Counter prints `description thresholds backed 7 of 7 clients`, exit 0 | ran it: `7 of 7`, rc 0 | holds |
| `--self-test` → `0 failure(s) over 26 assertions`, exit 0 | ran it: same line, rc 0 | holds |
| `TARGET = 4` `:83`; seven `CLIENTS` `:86-87`; floor declared `4 of 7` at `plans/round-54.md:26` | grep-pinned all three lines verbatim (`backed 4 of 7 clients` **or more**) | holds |
| `judge()` reads only threshold tokens (`:281`) and action non-emptiness (`:284`); past-cell `sr[2]` and the sentence never read; disclaimer `:46-48` | pinned `:281` `tokens = NUM_RE.findall(sr[1])`, `:284-285` action check, `:46-48` verbatim | holds |
| Pointer staleness: moved table `anatomy-and-compression.md:211` "hard 99-char cliff"; mechanism `SKILL.md:26-30` (`slice(0, _8n-1)`, `_8n=100`) | pinned `:211` omp row, `:29-30` slice/`_8n=100 (i.e. offset 99)` | holds |
| omp boundary: `CLIFF = 100` `:73`, return-unchanged `:240`, slice `:242`, vectors 99→99 / 100→100 `:591-592` | all four pinned verbatim | holds |
| Entry sourcing: findings 1–4 at `:15-19/:20-27/:32-34`; Codex CLI parser 1024 at `:26-27`; opencode v1/v2 at `:17-19` and `SKILL.md:176` cell; Limits `:60-67` | read all; "Four clients document 1,024 … None of their pages documents a cut" and the v2 no-maximum sentence confirmed | holds |

## Mutation probes (mine, bounded; scratch tree from `git show 65a5c7a` bytes — counter `--root` mode)

Detector = the committed counter at `verifiers/check_description_thresholds.py` (sha256
`15fdf83b30ddb0c68bf694a7d607a59dd80f685ba1d7750487f48d4b602fe186`, worktree == HEAD).

| mutant (scratch `SKILL.md` only) | counter output | verdict |
|---|---|---|
| pristine tree | `description thresholds backed 7 of 7 clients`, rc 0 | baseline green |
| M1 `four clients state 1,024` → `five clients …` | `7 of 7`, rc 0 | SURVIVED — facet's row 1 reproduced |
| M2 VS Code past-cell → `Truncated past 1024 characters` | `7 of 7`, rc 0 | SURVIVED — facet's row 2 reproduced (`sr[2]` unread) |
| M3 `omp cuts at 99` → `omp cuts at 100` | `7 of 7`, rc 0 | SURVIVED — facet's row 3 reproduced |
| M4 Cursor cell `1,024` → `2,048` | `6 of 7`, rc 0 | KILLED only by quote/token equality — facet's row 4 reproduced |

Facet 59's four-row mutant table is **exactly right**. Its conclusion — no clause-level falsifier for
"four", "none documents a cut", or "omp … 99" — is true of the committed counter.

Its two untested must-fail arms, now run:

| arm | my run | verdict |
|---|---|---|
| omp constant 100→101 → "the harness vectors red" | `verify_harness_claims.py --self-test` on scratch copy with `CLIFF = 101`: rc 1, FAIL on `preview[no-sentence-last-space]` (`g`×120 → 99+`…` vs 98+`…`) and `preview[cjk-no-ascii-period]`; pristine and restored copies rc 0 (`0 failure(s) over 10 assertions`) | arm kills — but via the `:598-599` vectors; the facet's cited `:591-592` vectors (99/100) stay green at CLIFF=101. Cited lines are not the killing ones; the control still works. |
| round-54 base do-nothing control → "`0 of 4`, exit 1" | `--rev 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`: `description thresholds backed 0 of 7 clients`, rc 1 | arm kills — printed denominator is **7**, not 4 (`len(CLIENTS)`, `:509`); the facet's own floor-vs-count distinction, correct everywhere else, slips in this one expected-output string |

Lexical over-flag probe (facet's non-vacuity argument for reviewer-assigned past-cell judgment): the four
committed denial cells each contain affirmative-cut vocabulary (VS Code `truncation, drop, warning,
refusal`; Copilot `truncation, refusal`; Cursor `cut, warning, warned`; opencode `cut, truncation,
warning, refusal`) — 4/4 over-flag confirmed; a naive `cut|truncat|refus` counter would flag every honest
row, so that control bullet is correctly assigned to reviewers rather than a regex.

## Where the attack lands

1. **Duplicate (material).** The facet's Risks section claims: "No sibling round-75 facet reported on
   `SKILL.md:164-177` … `grep -l` … returned nothing", concluding "the facet is distinct". False at wave
   settlement: `R75Facet53.md` (title: ":166 credits the whole table to a counter that reads one column";
   its O2/O5 = the same unread-cell and TARGET-floor facts; W1/W2 = same-world mutants; successor-counter
   sketch = same control space), `R75Facet56.md` (O1-O8: same sentence verbatim, same sr[1]/sr[3] finding,
   same `TARGET = 4`/7-clients/printed-`of-7` collision, same pointer-staleness observation, control =
   scratch-rewrite of `:166`), `R75Facet58.md` (same four 1024 rows with cell text, same past-cells-all-
   denials reading, measured probes four→seven / past-cell flipped / 1024-removed / tokenless — the same
   mutant classes as M1/M2/M4 — and controls (g) count-of-1024-cells-pinned-to-"four" and (h) no-cut form
   matching, which **are** facet 59's option-(a) bullets 1–2, plus the explicit TARGET-4/"four clients"
   coincidence at its `:104-106`), and `R75Facet64.md` (O2 same four-row count, O4 counter never reads
   1024, O5 same disclaimer, O6 same plan floor, O7 mutant M1 four→seven green). `R75Facet60.md` already
   cross-references facet 59 beside 53/64 and folds option (b) into its G2 "land one, not two" with facet
   53. The stale grep is explainable (directory was still filling) but the distinctness conclusion it
   licenses is wrong: the facet's core finding and control (a) are at least four-fold covered; its control
   (b) is the consolidated surface-disclosure control owned elsewhere.
2. **Genuinely marginal content survives** (verified absent from the sibling set): the 99/100 framing —
   "trigger >100, retained ≤99", i.e. exactly-100 is not cut and "cuts at 99" is the retained length —
   appears in no other w1 report; likewise the opencode v1-superseded-page scoping of the "four" count,
   the Codex-CLI fifth-1024 corpus note as an audit-misprediction risk, the omp-vector-read control
   bullet, and the round-54-base do-nothing arm. A round-75 audit reusing this gate should keep these
   three sentences and drop the rest to the siblings.
3. **Calibration nit (control bullet 3).** "print `omp: trigger >100, retained <=99` read from the
   committed guard's vectors" overstates the vectors: `:591-592` pin non-cut at 99/100 and `:598-599` pin
   cut at 120 with 98 retained; no committed vector pins input 101, so the strict ">100" trigger is a
   read of the guard source (`:240` `len(t) <= CLIFF`), not of the vectors alone.
4. **Worktree drift at judgment time (restoration evidence, not a defect of the facet).** The lane
   worktree no longer matches the facet's measured revision: `git status --porcelain` shows ` M` on
   `LOG.md`, `SCORECARD.md`, `SKILL.md`, `corpus/README.md`,
   `corpus/knowledge/skill-eval-artefacts-round70.md` (plus untracked round-75 outputs). The `SKILL.md`
   drift is one line at ~`:193` (round-70 eval wording) — nowhere near `:164-177`, so every worktree
   line-read I made matches the revision bytes; the facet's "worktree clean except untracked" premise was
   true when written and is stale now. All my evidence above is pinned to `git show 65a5c7a` bytes.

## Verdict

**SURVIVED, materially duplicated.** The central claim is true at the measured revision: every citation
reopened matches byte-for-byte, both stated commands reproduce (`7 of 7` rc 0; `0 failure(s) over 26
assertions` rc 0), all four mutant verdicts reproduce, and both proposed must-fail arms kill when
actually run. The attack does not overturn the finding; it narrows its action: the facet's distinctness
claim is false (four siblings own the same sentence/counter), its option (a) bullets 1–2 duplicate
facet 58's (g)/(h), its option (b) duplicates the consolidated surface-disclosure control, and two
must-fail-arm details are misstated (`0 of 7` not `0 of 4`; killing vectors `:598-599` not `:591-592`).
In scope; read-only honored.

## Restoration evidence

- Lane files never written by this seat; hashes constant across session:
  `SKILL.md` worktree `7b1263b5ccbe2ba8b6ffd5d0f4c87ffc5ab3292c9ce792aeee96de283a06464a`,
  counter `15fdf83b30ddb0c68bf694a7d607a59dd80f685ba1d7750487f48d4b602fe186`,
  harness `d7b767d61798d2ede4ab6ec98c7f4b2792a77f2c179c1b93b71591139b394114` (worktree == HEAD for both
  verifiers; neither in the modified list).
- Pristine bytes for the probe: `git show 65a5c7a:SKILL.md | sha256sum` =
  `1b2804fbab784b2c523681259f37d783238f65b2ca21c69b01a5a041bd13155f`; post-restore assertion "scratch
  tree bytes == git show 65a5c7a bytes for all four inputs: OK" passed; harness mutant differed from
  pristine by exactly 1 byte (`0`→`1` in `CLIFF = 100`) and the restored copy re-hash-verified True.
- Counter mutants ran in `/fast/scratch/hyaku/kotoba-r75/R75Attack59/tree` via `--root`; lane untouched;
  probe.py and tree removed after the run (scratch cleaned).

## Report trailer

- `SKILL.md:26-30,153-156,164-177,172-176,193` (sentence, table, four 1024 cells, pointer, mechanism; `:193` = the concurrent worktree drift line)
- `corpus/knowledge/skill-listing-thresholds-round54.md:15-34,60-67` (findings 1-4, Limits)
- `corpus/knowledge/anatomy-and-compression.md:211` (moved Router model row, hard 99-char cliff)
- `verifiers/check_description_thresholds.py:46-48,83,86-87,151-152,281,284-285,459,509` (disclaimer, target, clients, --root reads, judge cells, self-test line, backed line)
- `verifiers/verify_harness_claims.py:73,240,242,591-592,598-599` (CLIFF, guard, vectors; `:598-599` are the killing vectors)
- `plans/round-54.md:26` (historical `4 of 7` floor); base `422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`
- Siblings owning the same ground: `.ufo/waves/round-75/w1/R75Facet53.md`, `R75Facet56.md`, `R75Facet58.md`, `R75Facet64.md`; cross-reference: `R75Facet60.md` (Facet59 row; G2 "land one, not two")
- Commands: `python3 -B verifiers/check_description_thresholds.py --rev 65a5c7a…` → `description thresholds backed 7 of 7 clients` rc 0; `--self-test` → `self-test: 0 failure(s) over 26 assertions` rc 0; `--rev 422ffd10…` → `description thresholds backed 0 of 7 clients` rc 1; `python3 -B verifiers/verify_harness_claims.py --self-test` → rc 0 pristine/restored, rc 1 at `CLIFF = 101`; scratch probe outputs quoted above.
