# ReviewLessonQ25 — round 49 falsify (kotoba, judged c48793d)

VERDICT: FAILS — applies to two statements in `corpus/lessons/round-49.md`: M30's claim that the round-46 source "does not carry the clause either" (false: line 22 carries it), and C2's "every per-conjunct mutant fails on its named conjunct" (not enforced: removing a mutant leaves `boxes proven 2`, exit 0). Every "shown able to fail" demonstration the lesson states reproduces with the stated output and exit code. The R1 repair and the Gate's access records reproduce.

## Scope and method
- Judged bytes: master at c48793d. Private clone `/fast/scratch/hyaku/kotoba-r49/falsify/ReviewLessonQ25/kotoba`, HEAD confirmed `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`. Base a5adc146 in `mut/base-clone` for the R1 baseline.
- Mutants, all in scratch `mut/`: kasegi-reclassified PROVINCE copy, one-quote-altered census copy, duplicate-row copies, remapped map, placeholder fixture made literal, d04-stem manifest case removed, `skill_identity` returning the directory name.
- Installs: none. Used git, jq, curl, awk, python3 (stdlib), already present.
- Lane writes: none. `.ufo/waves/round-49/falsify/` already existed; my `mkdir -p` on it was a no-op. Sibling repos were read only (`grep`, `log`, `show`, `cat-file`, `merge-base`).
- No subagent dispatch (leaf seat).

## 1. HIGH — M30 round-46 sentence is false
Lesson M30: "The round-46 source it cites (`.ufo/round-46/scouts/w2-connector.md:22`) does not carry the clause either."
- `sed -n 22p .ufo/round-46/scouts/w2-connector.md` → "- `kasegi` — bounty and security research, prompt injection exploits, and claim packages — `../kasegi-shokunin/PROVINCE.md:3-4`" (exit 0).
- `grep -ciE 'prompt[- ]injection|injection' .ufo/round-46/scouts/w2-connector.md` → 1 (exit 0).
- Tracked at a5adc146: `git ls-tree a5adc146… .ufo/round-46/scouts/w2-connector.md | wc -l` → 1 (exit 0).
- True chain: the round-46 scout wrote the clause and cited kasegi `PROVINCE.md:3-4`, which never held it (§6). M30 should say that.
- The M30 kasegi grep itself is correct (§6).

## 2. HIGH — C2 box proof does not enforce per-conjunct coverage
`box_proof` (`verifiers/verify_dispatch_prompts.py`, lines 772–824) loops over the cases the manifest lists. It never checks that each `CONJUNCTS` entry has a must-fail case.
- c2-nostem mutant: the d04-stem case (manifest lines 19–27) removed with `CUT 19.=27`. `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` → `boxes proven 2`, exit 0. Judged tree: same output, exit 0.
- So "every per-conjunct mutant fails on its named conjunct" holds only for the mutants the manifest lists. Q25 fails for this mutant: the exit code does not change.
- Calibration: `boxes proven 2` tests the instrument against its own pins and fixtures. The pinned hash and the map's `text_sha256` come from the same change. It is not a measure of fleet operability (§3).
- Named-conjunct isolation (python, `evaluate_dispatch_04/08` on each fixture, judged clone):
  - controls PASS (d04-control, d08-control).
  - d04-placeholder: `report_path_literal` FAIL and `report_stem_is_lane_id` FAIL. Not isolated.
  - d04-stem: stem FAIL only. d04-unknown-lane: `lane_identity_known` FAIL, stem N/A.
  - d08-role-round, d08-report-dir-round, d08-above-state: one FAIL each. d08-missing-state: N/A.

## 3. MEDIUM — live dispatch.04 result is omitted from the lesson and SCORECARD
`.ufo/waves/round-49/build/c2-live-run-1115Z.txt`:
- Line 1: "FAIL dispatch.04: evaluated 287 — … 259 PASS, 6 FAIL, 22 N/A; 28 out of scope; failing files: kake-L1.md, kasegi-L1.md, kengaku-L1.md, kotoba-L1.md, kumitate-L1.md, protocol-L1.md".
- Line 2: "PASS dispatch.08: evaluated 279 — 250 PASS, 0 FAIL, 29 N/A; 13 out of scope". The JSON (`jq` over `c2-live-run-1115Z.json`) confirms `round_le_latest_dispatched`: PASS 250, N/A 29. The state clause ran on 250 files and was N/A on 29. "Its live failures are findings" is vacuous: there are none.
- The six dispatch.04 FAILs share one cause. The L2 routing paragraph of each `*-L1.md` prompt holds the template path `.ufo/reports/round-1/<lane>.md` (`kotoba-L1.md` line 12; the same in kake, kasegi, kengaku, kumitate, protocol). `REPORT_PATH_RE` matches every `.ufo/reports/round-N/…` string. The docstring says a template elsewhere in the body does not trip the box. So either these six are false reds from the scope rule, or six prompts carry an unresolved placeholder. The lesson decides neither.
- The lesson's C2 section gives no live result. SCORECARD row 255 cites the live file with no counts. `grep -c "6 FAIL" SCORECARD.md` → 0 (exit 1).

## 4. MEDIUM — Q25 hole: the C1 guard accepts duplicate rows
- `mut/PROVINCE.dup.md` (audio row duplicated): `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province ../mut/PROVINCE.dup.md` → "rows 20 verified 20", "province rows 21 matched 21", exit 0. Row counter on the same file → 21 (exit 0).
- `mut/census.dup.md` (census audio row duplicated) with the current PROVINCE → "rows 21 verified 21", "province rows 20 matched 20", exit 0.
- Cause (code read): `_check_province` tests `len(rows) < len(expected)`, so more rows pass. The census keeps lanes in a set, and `census_meta[lane]` is overwritten by the last duplicate. [INFERENCE, not run] A contradictory duplicate would be checked only if it came last.
- Effect: the "20" after-value is guarded from below only. A 21-row table passes with exit 0.

## 5. MEDIUM — Gate against CORPUS.md (judged bytes)
Passes:
- Candidates/admitted/rejected line present (candidates 1, admitted 1, rejected 0).
- Access records for S022 and S023 present (URL, UTC time, quote, location). Re-fetched today (§7): sha256 matches the rows, quotes sit at the stated lines, word counts 19 and 13 (limit 25).
- Status changes: SOURCES diff `git diff a5adc146 c48793d -- corpus/SOURCES.md` changes one S018 cell (`used-by`, census entry appended), adds S022 and S023, moves nothing else. `grep -c '^| S0'` → 21 at base, 23 judged (exit 0).
- CORPUS.md census commands on judged SOURCES: malformed 0; duplicate ids none; enum violations none; mined `used-by` paths missing none; tiers A=22 C=1; status mined=14 queued=8 rejected=1 (all exit 0).
Gaps:
- (a) No `spot-check result` line in `## Gate`. CORPUS.md lines 19–20 require it. Expected before falsify, but absent.
- (b) S016 re-open is not in the Gate. The R1 repair cites "S016: … index.ts:134, re-opened by seat R1Premise.md". S016's row carries `:24` and `:205-207`, not `:134`. Rule 2 forbids in-place anchor edits, so the citation needs a correction row or should be dropped. The premise holds (§7).
- (c) Q13: "Rows 21 → 23" has a command but no date. "(20 of 20 found)" has neither.
- (d) The S022 and S023 rows say "byte-identical to the round-48 fetch of the same route": these URLs were opened in round 48, which the Gate does not mention.

## 6. M30 kasegi evidence — HOLDS
- `git -C /home/vgpnk/Projects/shokunin/kasegi-shokunin grep -qiE 'prompt[- ]injection' 1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a` → exit 1.
- Wider: `git grep -niE 'prompt.{0,3}injection|injection.{0,3}prompt' 1fafde8f…` → no lines, exit 1. "injection" appears in 11 files at the pin, all command- or argument-injection contexts (e.g. `SKILL.md:739`).
- History: `git log --all --oneline -G'[Pp]rompt|[Ii]njection' -- PROVINCE.md | wc -l` → 0 (exit 0); `-S'prompt'` → 0; `-S'injection'` → 0.
- Pin exists and is an ancestor of kasegi HEAD: `git merge-base --is-ancestor 1fafde8f… HEAD` → exit 0.
- Base PROVINCE.md line 33 at a5adc146: "- kasegi — security research incl. prompt-injection exploits." (`grep -n kasegi`, exit 0).

## 7. Demonstrations re-run (judged clone; exit codes verbatim)
| # | run | output | exit |
|---|---|---|---|
| a | C2 `--box-proof --map verifiers/checklist-baseline.json` | `boxes proven 2` | 0 |
| b | C2 map: dispatch.04 → `verify_harness_independent.py` | `boxes proven 1`; stderr disposition line | 1 |
| c | C2 placeholder fixture made literal | `boxes proven 1`; stderr "verdict 'PASS', expected 'FAIL'" | 1 |
| d | C1 guard, current PROVINCE | `rows 20 verified 20`, `province rows 20 matched 20` | 0 |
| e | C1 guard, census only | `rows 20 verified 20` | 0 |
| f | C1 guard, base PROVINCE (`git show a5adc146:PROVINCE.md`) | FAIL "…holds no lane table … a bare-name list is not a table"; `province rows 0 matched 0` | 1 |
| g | C1 row counter, base | `0` (grep, no match) | 1 |
| h | C1 row counter, current | `20` | 0 |
| i | C1 kasegi `none`→`adjacent` copy | FAIL "province row 9 (line 19) … 'adjacent' does not match the census 'none'"; `province rows 20 matched 19` | 1 |
| j | row counter on copy i | `20` | 0 |
| k | census copy, kagi quote "evidence"→"proof" | FAIL "row 5 (census line 67) (lane kagi): quote not found"; `rows 20 verified 19` | 1 |
| l | R1 self-test, judged | `0 failure(s) over 123 assertions` | 0 |
| m | R1 self-test, a5adc146 | `0 failure(s) over 116 assertions` | 0 |
| n | R1 copy, `skill_identity` returns directory name | "got 4 want 3" twice; `2 failure(s) over 123 assertions` | 1 |

Rows a–n match the lesson's stated outputs.

Access records (ordinary curl; no bot challenge met):
- https://code.claude.com/docs/en/skills.md — 2026-10-22T11:36:35Z — 111,557 B — sha256 cdfcb0df93… — Gate quote at line 389.
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md — 11:36:36Z — 21,840 B — 7913d455… — line 59.
- https://agentskills.io/specification.md — 11:36:36Z — 7,608 B — 9a67de89… — line 102.
- https://raw.githubusercontent.com/anomalyco/opencode/v1.19.3/packages/opencode/src/skill/index.ts — 11:38:09Z — 11,843 B — 91dce57f… — line 134 is `state.skills[md.data.name] = {`.
- kotodama override reason: "NOT prompt/skill craft (kotoba-shokunin)" is in `SKILL.md` line 3 at 35f0d49f (`git show … | grep -o`, exit 0).

## 8. Other counts (with commands)
- Plan name count (`awk '/^## Adjacent/,0' PROVINCE.md | grep -oE … | sort -u | wc -l`): base 10, current 20 (exit 0 each).
- Dispatch boxes with `executed:`/`delegated:` (jq over `checklist-baseline.json`): a5adc146 → 0; c48793d → 2 (exit 0 each). Dispatch boxes total at a5adc146: 9.
- Sibling dirs (`ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l`): 21, including kotoba. 20 siblings, matching the census.
- Knowledge `.md` files (`git ls-tree -r --name-only <c> corpus/knowledge | grep -c '\.md$'`): 75f671b → 34; a5adc146 → 35; c48793d → 36 (exit 0 each). The M29 "35" is arithmetic from 34 plus one file; not committed.
- Floors: `verify_harness_independent` 116 → 123; `instrument_total` 9 → 10 (`git diff` of `floors-registry.json`). `dispatch_prompts` floor 32 added, not checked.

## 9. Not verified (unrun)
- R4 "21 of 23 reproduce" and the two named lines. R5 "13 of 13 stay green". R1 "`oc.roots.names_plus_builtin` is 10 before and after".
- SCORECARD and LOG round-49 text; corpus baseline re-record (63→66, 41→43 per commit message).
- Census count lines (7 adjacent / 13 none; 8 of 17 name a sibling; 2 of 17 name kotoba). These are knowledge-entry counters and are not shown able to fail under Q25.
- Contradictory duplicate census row (§4 INFERENCE).

## 10. Recommendations (for the integrator; nothing edited)
1. Correct M30: the round-46 source carries the clause and cites kasegi `PROVINCE.md:3-4`, which never held it.
2. `box_proof`: require at least one must-fail case per `CONJUNCTS` entry and fail on any uncovered conjunct. Or drop "every per-conjunct" from the claim.
3. Decide the six dispatch.04 live FAILs: narrow `REPORT_PATH_RE` to the report line, or fix the six `*-L1.md` templates. State the live counts in SCORECARD.
4. `check_sibling_census`: exact row count and duplicate-lane refusal; add a duplicate arm to the self-test.
5. Gate: add the spot-check line; add an S016 correction row or drop `index.ts:134` from R1; add dates to the Q13 counts.

Residual risk: the C1 quote check is sound for the pinned quotes (20 of 20 re-verified). The main C1 risks are the duplicate-row and classification-overwrite gaps. The C2 fixture semantics are sound. The main C2 risk is reading `boxes proven 2` as operability.
