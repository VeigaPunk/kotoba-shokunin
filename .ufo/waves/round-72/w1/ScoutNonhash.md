# ScoutNonhash — corpus-integrity red at base `c69711ee` (round-72 w1)

**Verdict:** the red is exactly three disjoint classes, all caused by the r71 closure's spot-check file (`corpus/lessons/round-71-verifier-spotcheck.md`, landed as the round tip at `c69711e`): (1) tracked but unindexed → `corpus.index.unindexed=1`; (2) two `.ufo/reports/round-71/kotoba.md` pointers → `report_total 91→93`; (3) two abbreviated junk-commit citations → `commit_nonhash=2`. Minimal honest fixes, each verified in a fleet-shaped sandbox at the base, each keeping both gates able to fail: **A** index row (README), **B** baseline re-record of the three equal-mode expectations, **C** instrument rule in both verifiers classifying a trailing‑U+2026-ellipsis hex-prefix commit token as context (abbreviated meta-finding). After A+B+C both gates exit 0 (integrity 9/9; independent exit 0) and both self-tests pass. No `zero` check loosened to N; no non-author file touched; net +8 lines across the two instrument scripts.

Revision note: lane master HEAD reads `e61fd29` (wave-1 spec commit); the plan base `c69711ee` is its ancestor and the receipts were measured there; every run below is at `c69711ee` in a fresh fleet-shaped sandbox (symlinked fleet root + `git clone --shared`).

## Red-before (base `c69711ee`)

- `python3 -B verifiers/verify_corpus_integrity.py` → `exit=1`, `4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_nonhash`
- `python3 -B verifiers/verify_corpus_independent.py` → `exit=1`, `corpus.index.unindexed … observed=1 DRIFT`, `corpus.pointers.commit_nonhash … observed=2 DRIFT`
- `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` observed: `tracked_files=133`, `report_total=93`, `commit_total=41`, `unindexed=1` (`corpus/lessons/round-71-verifier-spotcheck.md`), `commit_nonhash=2`
- Matches the committed receipts (`.ufo/waves/round-72/receipts/base-outputs/verify_corpus_integrity.out`, `verify_corpus_independent.out`, both `HEAD c69711e`).

## Finding 1 — the exact two `commit_nonhash` tokens

- `corpus/lessons/round-71-verifier-spotcheck.md:90` → `commit `955ffd5d…``
- `corpus/lessons/round-71-verifier-spotcheck.md:120` → `commit `fb6a28ee…``

Byte-exact: `sed -n '90p;120p' … | grep -o 'commit `[0-9a-f]*…`' | od -c` shows `342 200 246` = UTF-8 U+2026 “…” in both. Context (quotes ≤25 words, copied from the fetched bytes):
- line 90: “the scratch junk commit `955ffd5d…`” (7 words; dropped bytes: preceding “committed bundle, ” … the rest of the receipt-name sentence);
- line 120: “scratch junk commit `fb6a28ee…`” (5 words; dropped bytes: preceding “`receipts/c2-junk-world.txt` (W12 bundle, ” and tail “, `0 of 10`, `exit 1`);”).

Neither prefix resolves anywhere: `git log --all` (lane and fleet) has no commit starting `fb6a28ee`/`955ffd5d` — they are round-71 scratch junk commits from /tmp control worlds, never committed to any repo. The file is non-author (r71 hyaku closure) and was not edited in this work.

## Finding 2 — why `unindexed`, and where the row belongs

- `corpus.index.unindexed` counts tracked corpus files not covered by any FILE-column token of the `## Coverage map` table. `tracked_corpus_files` = `git ls-files corpus/` (133 total = 132 md + `knowledge/sibling-citation-routing-round16.json`); `index_findings` harvests backticked column-2 tokens and marks uncovered tracked files (README.md exempt).
- Lessons are indexed as coverage-map rows with column-2 tokens like `lessons/round-71.md`; closure spot-checks follow the convention “Round-N verifier spot-check (closure)” placed directly after that round's lessons row (precedents: rounds 46–50, 58–62, 66–70; many landed unindexed and were indexed the next round — the M21/M98 class).
- `lessons/round-71-verifier-spotcheck.md` landed as the round tip (`c69711e`) after the r71 baseline re-record (`eb394f5`) and after the Round-71 lessons row (README line 137) existed, so no row covers it. The row belongs immediately after line 137, before `## Frontier` (line 139).

## Finding 3 — the nonhash classification rule

- `verifiers/verify_corpus_integrity.py`: `COMMIT_RE` line 149 (backticked token after literal `commit`); inside double quotes or a code span → quoted meta-finding (lines 522–525); else `not is_hex_object_id(token)` → nonhash (lines 526–527); `is_hex_object_id` (lines 303–305) requires `HEX_RE` `\A[0-9a-fA-F]{7,40}\Z` (line 150). The ellipsis character breaks hex → nonhash.
- `verifiers/verify_corpus_independent.py`: `COMMIT_RE` line 125; `analyse_commits`: inside quote/code-span → quoted (lines 480–482); else `not (7 <= len(token) <= 40 and HEX_RE.match(token))` → nonhash (lines 484–485); `HEX_RE` line 136. Same net rule.

## Proposal A — index row (lane-side, README)

Insert after line 137:
`| Round-71 verifier spot-check (closure) | `lessons/round-71-verifier-spotcheck.md` | written by the hyaku closure, not the lane (outside review; never edited here): round 71 admitted; per-claim re-checks, verdicts and routed defects R1-R7; landed at `c69711e` without an index row (round-72 indexed), which turned `verify_corpus_integrity.py` red at that base (`unindexed 1`) |`

Verify (sandbox, A only):
- integrity: `5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.pointers.report_total, corpus.pointers.commit_total, corpus.pointers.commit_nonhash`, `exit=1` (unindexed 1→0);
- independent: `exit=1` (unindexed 0; nonhash red).

## Proposal B — baseline re-record (equal-mode expectations only)

In `verifiers/corpus-baseline.json`: `corpus.index.tracked_files.expect` 132→133, `corpus.pointers.report_total.expect` 91→93, `corpus.pointers.commit_total.expect` 40→41; append `round72_rerecord` note (value source: `--no-baseline --json` at the base; mirrors the established note style). All zero-mode expectations untouched.

Verify (sandbox, A+B):
- integrity: `8/9 checks pass; DRIFT: corpus.pointers.commit_nonhash`, `exit=1`;
- independent: `exit=1` (only nonhash red).

## Proposal C — instrument rule for abbreviated commit citations

The tokens live only in the non-author file (MUST NOT be edited), so a lane-side change is impossible; the fix is an instrument rule, identical in both verifiers: a commit-token ending in U+2026 “…” whose stem is 7–40 hex is an abbreviation — context, like the existing quoted meta-findings — and is collected into the quoted/context detail bucket, not nonhash.

- integrity (`verify_corpus_integrity.py`), inserted after the quoted/code-span branch, before the nonhash branch: `if token.endswith("\u2026") and is_hex_object_id(token[:-1]): quoted.append(…) "(abbreviated meta-finding)"); continue` (+4 lines);
- independent (`verify_corpus_independent.py`), same position: `if token.endswith("\u2026") and 7 <= len(token)-1 <= 40 and HEX_RE.match(token[:-1]): quoted.append(…) "(abbreviated meta-finding)"); continue` (+4 lines).

Red-before (C only, base sandbox): integrity `5/9 checks pass` `exit=1` (nonhash 0; equal/unindexed stay red), independent `exit=1` — the rule alone cannot green the gates.

After A+B+C:
- integrity: `9/9 checks pass`, `exit=0`; both tokens report as `commit_quoted: …: fb6a28ee… (abbreviated meta-finding)` / `955ffd5d… (abbreviated meta-finding)`;
- independent: `exit=0`; same two tokens listed `(abbreviated meta-finding)`;
- `verify_corpus_integrity.py --self-test` → `self-test: 0 failure(s) over 161 assertions`, `exit=0`;
- `verify_corpus_independent.py --self-test` → `self-test: 103 assertions, 0 failures`, `exit=0`.

No `zero` check changed to `equal N`; `commit_nonhash` remains a zero check (a malformed non-hex token without ellipsis still lands there). No tracked file deleted; the spot-check file is byte-identical to the base. Net +8 lines across the two instrument scripts (within the C3 40-line cap).

## Addendum — named-class variant of Proposal C (calibration note)

Peer `ExecIndexBaseline` drafted the same repair with a dedicated `commit_truncated`
context class in both instruments (regex + branch + count + detail + docstring +
self-test arms; self-tests 164/105 assertions, 0 failures; gates 9/9 exit 0 /
exit 0). Difference versus my 4-line C variant: mine lands the two tokens in the
existing quoted bucket, moving `commit_quoted` 6 → 8; theirs keeps `commit_quoted`
at 6 (matching the base receipt's `quoted-excluded=6`) and prints the sites under
their own label. Verified impact of my variant: no gate verdict changes (neither
check list includes `commit_quoted`); `fault_injection_corpus.sh` arm h asserts
`report_pointers_quoted` (+1 on a planted dead pointer), which neither variant
touches. Both variants are functional; the named class is semantically cleaner and
receipt-consistent. Implementation choice is the L1's; the frozen predicates and
controls are satisfied by either.
