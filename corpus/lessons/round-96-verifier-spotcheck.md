author: hyaku closure (non-author integrator, @m_zfl)

# Round 96 verifier spot-check (non-author closure of kotoba round 96)

Closure of lane-round kotoba r96. Base `0f66016a3b35cf1e25c67caf8cf371996805cbb8`, lane tip
`74fa240b5fb3ef4a7b0507f36f12127db264a33d`. Report `.ufo/reports/round-96/kotoba.md` (fleet repo).
The reviewer did not author the round, and none of these checks changes any lane-authored file.

Driver digest (copied from `.ufo/watchdog.log`, which can change):

```
2026-11-05T23:53:50-03:00 launch kotoba round=96 pgid=2297041 driver=hyaku-inline attempt=1
2026-11-06T00:40:50-03:00 complete kotoba round=96; hyaku-inline attempt=1
```

## Step-1 conformance

- Report attribution: `git log --format='%an %H' -- .ufo/reports/round-96/kotoba.md` →
  `kotoba-shokunin 3e3ea88a178cc34bf0895d8d48a844d745a84cb0` (00:40:26-03:00). The report landed
  after the last lane commit (00:39:25), so it was not filed before its commits.
- `## SHONEN` heading present, with one `[~]` line for each of the four boxes and an evidence pointer on each.
- Cited commits: for each hash, `git cat-file -e <h>^{commit}` and
  `git merge-base --is-ancestor <h> master` both pass for `0f66016a`, `679775ab` (freeze), `801dd9bc`
  (landing), `762859df` (record), and `74fa240b` (wave evidence). Authors are kotoba-shokunin, apart from
  the protocol-authored base.
- `scripts/hyaku/jj-lane.sh state` → `branch=master local=remote=74fa240b… ahead=0 behind=0
  head=detached tracked=0 untracked=0`. `git status --porcelain` in the lane printed nothing, so no
  round work is left uncommitted. `git ls-remote origin refs/heads/master` → `74fa240b…`.
- Prompt contract: the first 140 lines of `.ufo/prompts/kotoba-round-96.md` (§1–§5) differ from
  `templates/round-prompt.md` only in substituted placeholders (`{{LANE}}`, `{{ROUND}}`,
  `{{FLEET_ROOT}}`, `{{AXES}}`). §6 is the hyaku addendum. The contract is carried verbatim.
- Status: **ok**. The round has real committed work, so it is not a marker report.
- Red-gate carry (Gate standard, Closure consequence; status-neutral): the tip battery at landing
  reports `guards 5 of 5; tip battery exit 0: 3 of 6`. `verify_skill_checklist.py`,
  `verify_corpus_integrity.py`, and `verify_corpus_independent.py` exit 1. The round-95 landing
  receipt shows the same three reds, so this round added none.

## Claim re-checks

**C1 — depth (the dispatch-prompt checker's self-test kills the frozen survivors t01..t11).**
I re-measured the claim myself where plain measurement allows. Where it rests on the lane's counter and
self-test, I verified the committed evidence instead. I did not execute any lane gate or self-test.

| check | command (run by this reviewer) | observed | reported | match |
|---|---|---|---|---|
| production code untouched | `git diff -U0 0f66016a 74fa240b -- verifiers/verify_dispatch_prompts.py \| grep -E '^(@@\|-[^-])'` | one hunk `@@ -799,0 +800,128 @@ def self_test()`, zero deleted lines; `self_test` spans 679–1112 at tip | +128 lines inside `self_test()` | yes |
| arms added | `git show <rev>:verifiers/verify_dispatch_prompts.py \| grep -c 'rec('` | 45 → 63 textual calls; with the 2-iteration loop and `CONJUNCTS["dispatch.04"]` (3 ids, line 122) this expands to 22 assertions | 56 → 78 assertions (+22) | yes |
| arms are behavioural | inserted lines grepped for `__file__\|compile(\|open(\|environ\|TMPDIR\|getsource\|inspect\|marker\|read_text\|read_bytes\|sys.` | 0 matches. Each arm calls `evaluate_dispatch_04/08` on a `_write_case` fixture | behavioural arms | yes |
| counter frozen | `git show <rev>:verifiers/fixtures/round-96/selftest-kills.py \| sha256sum` at `679775ab` and `74fa240b` | `1711b68fd9f443b5…0a0ab13b2b2` both | `1711b68f…13b2b2` | yes |
| before (evidence) | read `.ufo/waves/round-96/receipts/redbefore-c1-base.txt` (committed at the freeze `679775a`) | `rev 0f66016a…`; `C1 targets killed 0 of 11 (run errors 0) … code decoys held 11 of 11` `C1-PREDICATE-UNMET` `rc=1`; all 11 mutants `SURVIVED … over 56 assertions` | same | yes |
| after (evidence) | read `.ufo/waves/round-96/receipts/landing/c1-counter.txt` | `rev 801dd9bc…`; `C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; …` `C1-PREDICATE-MET` `rc=0`; 12 `KILLED` lines (11 targets + positive) | same | yes |
| per-mutant failure counts | `grep -E '^mutant t' …/c1-counter.txt \| grep -oE '[0-9]+ failure'` | 2,1,1,2,3,2,1,1,1,3,5 | CriticClaimR96 hand-applied: 2,1,1,2,3,2,1,1,1,3,5 | yes |
| controls | `grep PREDICATE receipts/forgery-f*.txt` | f1–f5 all `C1-PREDICATE-UNMET` (pre-data) | same | yes |
| mutant ↔ arm semantics (t04, t07, t11) | counter lines 90/96/104 compared with the arms in the landing diff | t04 `<=`→`<` is caught by the equal-round PASS arm. t07 `dirs != [n]`→`n not in dirs` is caught by the round-6 + round-7 FAIL arm. t11 N/A→PASS is caught by the per-conjunct N/A arms | — | sound |

The A3 bound (the v4 counter reads MET on the g3/g7/g8 no-arm forgery classes) is disclosed. It does not
affect this landing: by the zero-match scan above, the landed arms contain no stateful, recompile, or
source-reading constructs. The kill is therefore real behaviour, confirmed by the counter reading together
with arm semantics read statically by a non-author.

No-harm (evidence-verified from committed landing receipts):

- `r95-c1.txt` and `r95-r94c1.txt` are MET (rc 0). `r93-c1-killpin.txt` is MET. `r92-controls.txt` reads
  `shortcuts refused 2 of 2; honest held 2 of 2`.
- `dp-boxproof.txt` reads `boxes proven 2`. `gate-registry.txt` reads `74 of 74 … phantom 0`.
  `floors-selftest.txt` reads `0 failure(s) over 176 assertions`.
- `dp-live.txt`: dispatch.04 reads `1191 PASS, 6 FAIL, 22 N/A` and dispatch.08 reads `1172 PASS, 10 FAIL,
  29 N/A`. SentinelScopeR96 found these byte-identical to the base run, with the prefix and suffix bytes
  equal.
- `git diff --stat 0f66016a 74fa240b -- SKILL.md PROVINCE.md SHONEN.md AXES.md` prints nothing.
  SKILL.md is 600 lines.
- The SCORECARD diff appends only (the round-96 annotation and the round-97 intentions). No score was
  changed.

## Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| depth | improved | C1 verified. The self-test kills 0 → 11 of 11 frozen survivors, re-measured as above |
| consistency | unchanged | SKILL.md, PROVINCE.md, and SHONEN.md are byte-identical. Live verdicts are identical |
| coverage | unchanged | no change |
| operability | unchanged | no change |
| freshness | unchanged | no change |
| calibration | unchanged | no change |
| adjacency | unchanged | no change |

No axis was harmed.

## Discernment spot-check (lesson `round-96.md` § Gate)

I re-opened every source from this host on 2026-11-06 with
`curl -sS -L -o <f> -w '%{http_code} %{size_download}'` and `sha256sum`.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S272 POSIX.1-2024 XCU 2.6.2 | admit (A, spec) | `pubs.opengroup.org/…/V3_chap02.html` → 200, 357953 B, sha256 `0889867a53fe1250…` (equal to the lesson's digest) | agree | Line 777 is the `2.6.2 Parameter Expansion` heading (`tag_19_06_02`). Lines 790–791 carry the quote verbatim, folded after "with". `wc -w` gives 22 words (≤25). The quote directly grounds t01–t03 (braces optional ⇒ both `${X}` and `$X` are unsubstituted) |
| S271 PIT "Mutation operators" | admit (A, docs) | `pitest.org/quickstart/mutators/` → 200, 67033 B, sha256 `a31331daf89f246f…` (equal) | agree | Line 313 is the heading. Lines 317–319 hold the 16-word quote, joined across the code span. The table row at lines 334–335 is `&lt;=` → `&lt;`, which is the t04 direction |
| mutmut docs | reject | `mutmut.readthedocs.io/en/latest/` → 200, 51074 B, sha256 `07453b3fdb3b962a…` (equal) | agree | Line 523 is the only relational example (`&lt;` → `&lt;=`), and line 527 defers to `node_mutation.py`. The `<=`→`<` direction is not stated, so the source is weaker than S271 for t04 |

SOURCES row re-opened: **S272**. The `corpus/SOURCES.md` row quote ("The parameter name or symbol can be
enclosed in braces, which are optional except for positional parameters with more than one digit") is
22 words and matches the fetched bytes at lines 790–791. That is ≤25, so it passes.

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` returns rc 0. Its
last line is `kotoba ok …/corpus/SOURCES.md`, with 34 `W04` and no `E` codes. No W04 names S271 or S272.
Row count from `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` goes 196 (at
`0f66016a`) → 198, matching the report.

## Trend verdicts

- **expansion: unchanged.** No `knowledge/` entry was admitted. S271/S272 are registry rows (+2, 196 → 198).
- **quality: improved.** The province instrument's self-test now kills 11 behaviours it previously missed
  (0 → 11 of 11). Production bytes are unchanged and every no-harm receipt held.
- **discernment: improved.** The outside spot-check agrees with both admits and the reject. The round-95
  routed defect 1 (Ant reject reason) is amended append-only in § Gate. The counter bounds (A3) are
  disclosed rather than absorbed. The mined mistake `decoy-builder-cuts-elif-chain` was captured into Q86.

## Routed defects (lane fixes next round)

1. Frozen receipt `.ufo/waves/round-96/receipts/sources-opened.txt` line 12 records the S272 quote as
   "19 words", but it measures 22. The lesson discloses this. Land a named correction entry (append-only)
   that points at the receipt.
2. The v4 counter reads MET on the no-arm forgery classes g3/g7/g8 (addendum A3). Close this with a v5
   counter shown on committed g3/g7/g8 control worlds. This is already in the round-97 intentions.
3. Surviving mutants of `verify_dispatch_prompts.py`: MutTesterDispatchR96 left 15, and the pre-freeze
   sweep left 7 non-target survivors. Route them to a frozen kill set.
4. Counter exit ladder (addendum A4, carried from ReviewerCounterV3 F1/F3) and round-95 defect 3 (m08 /
   N4) are carried.
5. Three long-standing red gates (`verify_skill_checklist`, `verify_corpus_integrity`,
   `verify_corpus_independent`, exit 1) and the tip battery's flat 280 s floors cap (the floors gate took
   264.9 s this round, close to the cap) are carried from round 95, defect 5.
6. Wave-evidence growth: `du -sb .ufo/waves/round-96` is 1941368 B, against 719539 B in round 95 (Q82),
   mostly from saved source HTML. Consider storing digests and line excerpts instead of full HTML copies.
7. Attribution: the dispatch prompt `.ufo/prompts/kotoba-round-96.md` was committed under the lane
   identity (608f2a60). This is orchestrator-side and noted for the operator.

SHONEN: all four boxes cite evidence a non-author can check (`SHONEN.md:5`, LOG § Round 96, the
round-8 cold-run lesson, PROVINCE § Adjacent). Promotion is operator-owned; this is noted only.
