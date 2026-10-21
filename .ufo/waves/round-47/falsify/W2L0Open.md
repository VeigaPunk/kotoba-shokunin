verdict: PARTIAL — the "never queued" premise is false at fleet HEAD: both round-46 questions were appended as kotoba round-47 lines 84–85 at fleet commit `c2e2913` (8m25s after lane landing `7ad7fad`), the append is durable and substantively correct, but the new Q1 line contradicts `SCORECARD.md:287` at the landing tree and does not name the round-13 L0 line it restates.

# W2L0Open — L0 open-line census for kotoba (round-47 falsify wave 2)

## Measurement base

- Lane repo `kotoba-shokunin`, detached at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (2026-10-21T13:46:13-03:00, "round-47: C1 re-derive+re-pin …"). All lane `path:line` citations below are at that commit.
- Fleet root `/home/vgpnk/Projects/shokunin`, HEAD `c2e2913dcfabe58fbb0b678594b7a4ff69604487` (2026-10-21T13:54:38-03:00, "round-47: kotoba L0 questions (two round-46 axis/erratum questions queued)"). The L0 file is outside the lane repo, so its line numbers are stamped at this fleet HEAD, not at 7ad7fad.
- `.ufo/l0-questions.md` at fleet HEAD: **85 lines, 64,754 bytes, sha256 `a5571d95824d88f35c20fb53b13f3fe291e47ea1d2e7c65f656c809987dc919b`**; worktree byte-identical to HEAD (`git status --porcelain -- .ufo/l0-questions.md` empty, exit 0). Terminal byte `0a`.
- The scout's stamp is reproducible but stale by two commits: `f06d3855:.ufo/l0-questions.md` = 82 lines, sha256 `c13d612b01718232b9f5a62ee8ff84675b1da6261659ab81786b5dd51eb125a1` (exactly `ScoutL0Open.md`'s measurement), and `f06d3855` is an ancestor of HEAD (`git merge-base --is-ancestor` exit 0). Between it and HEAD, `c98fa5c` added the mado round-22 line (82→83) and `c2e2913` added the two kotoba round-47 lines (83→85).

## A. The nine fleet-channel lines naming kotoba, and their state

Membership is exhaustive: `grep -in 'kotoba' .ufo/l0-questions.md` (fleet) returns exactly lines 6, 7, 11, 12, 17, 40, 50, 84, 85 (exit 0). No operator answer line exists (`grep -c '^operator'` → `0`, exit 1); the only inline markers in the file are at 52/53 (`L0 ANSWER`, kama/tsukuroi), 75 (`SUPERSEDES`, tsukuroi), and 77 (`RESOLVED-BY-RULING`, tabi) — none kotoba.

| # | Key (lane \| round \| opening words) | Line | State at fleet HEAD `c2e2913` | Evidence |
|---|---|---|---|---|
| 1 | aggregator \| round-6 \| "Axis vocabulary split (ledger row D-78)…" | 6 | **PARTIALLY-RULED, operator open** | `../.ufo/reports/AGGREGATE.md:1236` "RULED-partially … operator action owed"; `:1811` lists it "open, operator-only". Lane remedy on record `SCORECARD.md:7-15` (consistency declared a calibration sub-axis, satisfying the in-row mapping rule at `../PROTOCOL.md:515-516`). |
| 2 | kengaku \| round-10 \| "Promote the gate convention (exit 0/1/2 + --selftest…)…" | 7 | **ANSWERED-BY-RULING (not operator)** | `AGGREGATE.md:1812`; `git cat-file -t dddb4ec` → `commit`. kotoba residue is D-140 (`AGGREGATE.md:1682-1683, 1899`): `verify_surfaces.py`/`verify_harness_claims.py` stay "probe" until a registry row + frozen run exist. Not an open decision. |
| 3 | kotoba \| round-13 \| "Axis-accounting ratification, two items…" | 11 | **OPEN, operator-only** | `AGGREGATE.md:1815` "open, operator-only; both halves evidenced". Item (1) (may a lane work an advisory axis as its lowest-axis move) is now restated by line 84; item (2) (D-78 fold of `consistency` into `calibration`) remains open. |
| 4 | aggregator \| round-9 \| "CORPUS.md amendment set…" | 12 | **OPEN, operator-side** | `AGGREGATE.md:1817-1819` publishes it as an appended operator-side set. kotoba appears only as an occurrence count; no round-47 claim touches `CORPUS.md` rule text. |
| 5 | kama \| round-1 \| "Fleet hygiene gap … .gitignore lines 1-6 …" | 17 | **MOOT (premise false)** | `../.gitignore:1` is now the glob `*-shokunin/`; `git check-ignore -v kama-shokunin` → `.gitignore:1:*-shokunin/`, exit 0. |
| 6 | kotoba \| round-16 \| "Reconcile the relaunched round namespace and craft-batch contract…" | 40 | **OPEN, non-blocking, operationally moot** | No answer, no inline resolution; but the steered numbering ran 16→47 without collision: `SCORECARD.md:98` round 46 completed, `:106` round 47 completed, `:108` "Next: round 48". |
| 7 | kotoba \| round-22 \| "r16adj owner packets across the five siblings…" | 50 | **OPEN (0 ack), DURABILITY CLOSED** | Ack re-measured 0: `grep -c 'r16adj'` over fleet `LOG.md` → 0, `AGGREGATE.md` → 0, `MANIFEST.json` → 0. Durability: `git merge-base --is-ancestor 31baf5c HEAD` exit 0 (commit `31baf5cb…`, 2026-10-19T17:03:23-03:00), so the earlier "uncommitted" lane records (`LOG.md:1243,1265`) are superseded history. |
| 8 | kotoba \| round-47 \| "(queued from the round-46 report, never appended then) Does AXES.md's…" | 84 | **OPEN, unsurfaced** | Added by `c2e2913`; no answer. `AGGREGATE.md` last touched 2026-10-19T22:21:35-03:00 (2,299 lines) and has **0** rows naming round-47/kotoba round-47, so the aggregator has not surfaced it yet. |
| 9 | kotoba \| round-47 \| "(queued from the round-46 report) Round 47 answered …" | 85 | **OPEN, unsurfaced** | Same commit; same unsurfaced state. |

Nothing else in the file names kotoba; the axis-adjacent non-kotoba lines (31 kama r1, 35 kengaku r13, 47 kotodama r11, 73 kengaku r25) are unchanged from the scout's census and are not kotoba's.

## B. The two round-46 questions: queued, not "never queued"

Both questions lived only in `.ufo/reports/round-46/kotoba.md:141-142` until fleet commit `c2e2913`.

Exact diff (`git show c2e2913 -- .ufo/l0-questions.md`, exit 0): 1 file changed, **2 insertions**, hunk `@@ -81,3 +81,5 @@`, index `5e4cf83..1582833` — pure EOF append, no filed line rewritten. `git log --all -S'range over advisory axes'` and `git log --all -S'confirm or overrule this mechanism'` each return only `c2e2913`, confirming first appearance.

Appended bytes (line 84, 345 bytes; line 85, 334 bytes):

```
kotoba | round-47 | (queued from the round-46 report, never appended then) Does AXES.md's "lowest non-retired axis" range over advisory axes? Under the owned-only reading the lowest is depth (9) and round 47's C1 (freshness 8.0, advisory) meets only the all-axes reading; round 47 worked freshness on the all-axes reading, as its plan declared.
kotoba | round-47 | (queued from the round-46 report) Round 47 answered "can a lane amend an append-only LOG citation that later goes dead (LOG.md:2111)?" with an in-source, line-sha-pinned erratum (verifiers/verify_skill_checklist.py GOVERNANCE_ERRATA, horizon 2315) instead of editing LOG.md — confirm or overrule this mechanism.
```

Fidelity against the sources:

| Facet | Source | Appended line | Verdict |
|---|---|---|---|
| Q1 question sentence | `round-46/kotoba.md:141` verbatim | verbatim | exact |
| Q1 correction | source ends "r47's C1 is freshness, so it meets both readings" (false under owned-only) | "meets only the all-axes reading" | **correction is right** (see F2/F3) |
| Q1 r46 context | source: "C1 met only the owned-only reading the lane declared at SCORECARD § Saturation" | dropped | context loss, minor |
| Q1 tie | source: "freshness and adjacency (8.0) are the lowest" | "freshness 8.0, advisory" (tie omitted) | slight precision loss; `plans/round-47.md:20` itself says "tie with adjacency" |
| Q1 attribution | reading is named at `SCORECARD.md:101` ("lowest non-retired axis under the all-axes reading"); `plans/round-47.md:20` says only "lowest non-retired axis, 8.0; tie with adjacency" | "as its plan declared" | defensible [INFERENCE] but not literal: the plan asserts the conclusion, the scorecard names the reading |
| Q2 mechanism | source options: "a gate erratum ledger, or accepting it as permanent" | "in-source, line-sha-pinned erratum (GOVERNANCE_ERRATA, horizon 2315) … confirm or overrule" | faithful; the mechanism does not amend `LOG.md`, it excuses in the gate, and the line asks the operator to confirm exactly that |
| Q2 static pins | — | `verifiers/verify_skill_checklist.py:377` `GOVERNANCE_ERRATA_HORIZON = 2315`; `:378-383` row `(2111, "7dcbf123…", ".ufo/round-45/drafts/v10/post-r44-hunt.py", "each exited 2 because the referenced runners are absent")`; `:1532` hashes the `splitlines()` line with no trailing newline | **verified**: `LOG.md:2111` without newline → `7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135` (matches); with newline → `d7b4c628…` (does not). `LOG.md` at 7ad7fad is 2,326 lines, so `2111 ≤ min(2315, 2326)` holds |

Timing/ownership: the lane landed at 13:46:13-03:00; the fleet L0 commit is 13:54:38-03:00, so the append is integrator-side and post-landing, consistent with `../PROTOCOL.md:528-530` ("durability owner is the integrator"). `plans/round-47.md` and the lane `LOG.md` round-47 entry predate the append and do not mention it (see F6).

## C. What still needs appending this round, with exact text

**None of the two round-46 questions.** Both are queued (lines 84–85) and committed; no round-46 question remains unqueued, and the round-46 report contains exactly two `## L0 questions` bullets (`round-46/kotoba.md:141-142`).

One append-shaped gap survives, and it is **optional/strict-conformance only**, not a missing decision: line 84 restates item (1) of the round-13 line without naming it. If the L1 wants strict compliance with `../PROTOCOL.md:525-526` ("a lane restating or correcting its own question appends a new line naming the superseded one"), the exact line to append is:

```
kotoba | round-47 | Cross-reference, not a supersede: the "lowest non-retired axis" reading question above restates item (1) of the kotoba round-13 line "Axis-accounting ratification, two items…"; item (2) of that line (the D-78 `consistency`→`calibration` fold) remains standalone and open, and no filed line is withdrawn.
```

No new axis question from round 47 needs the channel: the round's residuals (`verify_harness_claims.py` 21/28 and the three host skills, `LOG.md:2326`; round-46 residuals) are lane debt and `corpus/QUALITY.md` debt, not operator decisions, and `corpus/lessons/round-47.md` contains no `L0`/`operator` question text (`grep` → 0 matches).

## D. Findings and counterexamples

**F1 — the ticket's and the scout's "never queued" is false at fleet HEAD.** `ScoutL0Open.md` §B row 8 is stamped "UNQUEUED / OPEN" and §B row 9 likewise. At `c2e2913` both are filed at lines 84–85. The scout report was correct at its own stamp (`f06d3855`, 82 lines, `c13d612b…`, reproduced exactly); it was overtaken by `c98fa5c` and `c2e2913`. Any round-47 report that repeats "never appended" would be false.

**F2 — committed contradiction at the landing tree (calibration).** `SCORECARD.md:287` (round-46 refresh paragraph) ends:
`The all-axes reading of "lowest non-retired axis" (freshness/adjacency 8.0) is routed to L0 in the round-46 report; round 47's C1 satisfies both readings.`
That is false under the owned-only reading, which the lane's own new line 84 now states ("meets only the all-axes reading"), and it contradicts `SCORECARD.md:101` ("C1 — freshness 8.0 (lowest non-retired axis under the all-axes reading)"). `SCORECARD.md:28` depth = 9 and `:29` consistency = 10 are the owned axes, so the lowest owned is depth 9, which round 47's C1 did not work. C3's claim is "records match repo state"; this sentence does not.

Repro (scratch clone at 7ad7fad):
```
grep -n '^| depth\|^| consistency' SCORECARD.md      # 28 depth 9 · 29 consistency 10
sed -n '125,127p' SCORECARD.md                        # ## retired / None.
awk 'NR==287' SCORECARD.md | grep -o 'The all-axes reading.*'
# → ... round 47's C1 satisfies both readings.
sed -n '84p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md
# → ... meets only the all-axes reading
```

**F3 — the scout's supporting premise is wrong, though its conclusion survives.** `ScoutL0Open.md:59` says "consistency is retired at 10". `SCORECARD.md:125-127` says `## retired` → "**None.** No saturation or wrong-fit evidence". Consistency sits at the saturation line 10 but is not retired. The appended line 84's operative claim ("the lowest owned is depth 9") is still correct because 9 < 10; only the scout's justification is wrong.

**F4 — restatement not named.** Line 84 and line 11 item (1) ask the same operator decision (does the lowest-axis norm range over advisory axes / may a lane work an advisory axis as its lowest-axis move). `../PROTOCOL.md:525-526` requires a restating line to name the superseded one. Line 84 names only the round-46 report, not line 11. Exact remedy text in §C; classification is borderline because line 84 is also grounded in new round-47 evidence and line 11 item (2) stays live, so a full supersede would be wrong — hence "cross-reference, not a supersede".

**F5 — the new lines are unsurfaced.** `AGGREGATE.md` (2,299 lines) was last committed 2026-10-19T22:21:35-03:00, before the append; `grep -c 'kotoba r47\|round-47'` over it → 0 (exit 1). The aggregator's surfacing duty is outstanding for lines 84–85. This is aggregator-side, not a lane defect, but a reader of `AGGREGATE.md` alone would still see kotoba's only open axis question as the round-13 line.

**F6 — the lane record does not mention the filing.** `LOG.md:2317-2326` (round-47 landing entry), `SCORECARD.md:106` (round-47 completion block), and `plans/round-47.md` each contain 0 `L0`/`l0-questions` matches (`awk 'NR>=2317' LOG.md | grep -c …` → 0; `grep -c … plans/round-47.md` → 0, exit 1). Durability is satisfied integrator-side, so this is record completeness, not a conformance failure.

**F7 — precision losses in line 84 (no action required).** The adjacency tie and the round-46 clause were dropped, and "as its plan declared" attributes the reading to `plans/round-47.md:20`, which does not name a reading (only `SCORECARD.md:101` does). I judge the attribution defensible [INFERENCE] because the plan's "lowest non-retired axis" label is false under owned-only, so the plan can only mean the all-axes reading; not worth a correction line.

**C1 (counterexample to ticket/ScoutL0Open §B):** "the two round-46 questions were never queued" — false; `git show c2e2913` adds both, and `-S` proves first appearance there.
**C2 (counterexample to the round-46 report sentence and `SCORECARD.md:287`):** "r47's C1 meets both readings" — false under owned-only; see F2 repro.
**C3 (counterexample to the scout's justification):** "consistency is retired at 10" — false; `SCORECARD.md:125-127`.
**C4 (stale premise, line 17):** "`.gitignore` omits kama-shokunin" — false; glob at `../.gitignore:1`, `git check-ignore` exit 0.
**C5 (stale premise, line 50):** "the round-22 L0 line is uncommitted" — false; `31baf5c` is an ancestor of fleet HEAD (exit 0).

## E. Commands run (cwd; exit codes)

| Command | Exit | Key output |
|---|---|---|
| `wc -l -c .ufo/l0-questions.md; sha256sum .ufo/l0-questions.md` (fleet) | 0 | `85 64754`; `a5571d95…` |
| `git rev-parse HEAD` (fleet) | 0 | `c2e2913dcfabe58fbb0b678594b7a4ff69604487` |
| `git status --porcelain -- .ufo/l0-questions.md` (fleet) | 0 | empty (worktree == HEAD) |
| `grep -in 'kotoba' .ufo/l0-questions.md` (fleet) | 0 | lines 6, 7, 11, 12, 17, 40, 50, 84, 85 |
| `grep -c '^operator' .ufo/l0-questions.md` (fleet) | 1 | `0` |
| `grep -n 'L0 ANSWER\|RESOLVED-BY-RULING\|SUPERSEDES' .ufo/l0-questions.md` | 0 | 52, 53, 75, 77 — none kotoba |
| `git show c2e2913 -- .ufo/l0-questions.md` (fleet) | 0 | 1 file, `+2` at EOF, `@@ -81,3 +81,5 @@`, index `5e4cf83..1582833` |
| `git show HEAD~1:.ufo/l0-questions.md \| wc -l` / `\| grep -c kotoba` | 0 / 0 | `83` / `7` |
| `git show f06d3855:.ufo/l0-questions.md \| wc -l; sha256sum` | 0 | `82`; `c13d612b…` (scout stamp reproduced) |
| `git merge-base --is-ancestor f06d3855 HEAD` | 0 | ancestor |
| `git log --all -S'range over advisory axes' -- .ufo/l0-questions.md` | 0 | only `c2e2913` |
| `git log --all -S'confirm or overrule this mechanism' -- .ufo/l0-questions.md` | 0 | only `c2e2913` |
| `git merge-base --is-ancestor 31baf5c HEAD` | 0 | ancestor (line 50 durable) |
| `grep -c 'r16adj'` fleet `LOG.md` / `AGGREGATE.md` / `MANIFEST.json` | 1 / 1 / 1 | `0` / `0` / `0` |
| `git check-ignore -v kama-shokunin` (fleet) | 0 | `.gitignore:1:*-shokunin/` |
| `git cat-file -t dddb4ec` (fleet) | 0 | `commit` |
| `sed -n '2111p' LOG.md \| perl -pe 's/\n\z//' \| sha256sum` (lane) | 0 | `7dcbf123…` = erratum row |
| `sed -n '2111p' LOG.md \| sha256sum` (lane) | 0 | `d7b4c628…` (newline included — does not match) |
| `wc -l LOG.md` (lane) | 0 | `2326` |
| `grep -n '^| depth\|^| consistency' SCORECARD.md` (lane) | 0 | 28 (9), 29 (10) |
| `sed -n '125,127p' SCORECARD.md` (lane) | 0 | `## retired` / `None. …` |
| `awk 'NR==287' SCORECARD.md \| grep -o 'The all-axes reading.*'` (lane) | 0 | "…round 47's C1 satisfies both readings." |
| `grep -n 'D-140' .ufo/reports/AGGREGATE.md` (fleet) | 0 | 1682, 1683, 1899 |
| `grep -n 'CORPUS.md amendment set' .ufo/reports/AGGREGATE.md` | 1 | no table row; published in the `:1817-1819` "New this refresh" paragraph |
| `git log -1 --format='%cI' -- .ufo/reports/AGGREGATE.md` (fleet) | 0 | `2026-10-19T22:21:35-03:00` |
| `grep -c 'kotoba r47\|round-47' .ufo/reports/AGGREGATE.md` | 1 | `0` |
| `awk 'NR>=2317' LOG.md \| grep -c 'L0\|l0-questions'` (lane) | 1 | `0` |
| `grep -c 'L0\|l0-questions' plans/round-47.md` (lane) | 1 | `0` |

No tools were installed or upgraded for this report.

## F. What I did NOT check

- No lane gate was run: `verify_skill_checklist.py` (live or `--self-test`), `verify_surfaces.py`, `check_substrate_pins.py`, corpus integrity/independent, fault harness, floors. The erratum mechanism was verified **statically only** (row bytes, hash convention, horizon, `LOG.md` length); its runtime acceptance/rejection arms are the C3 seats' attack surface, not mine.
- No operator chat, console, session transcript, or untracked prompt was read. "No answer" is measured only on tracked fleet/lane surfaces (L0 file, fleet `LOG.md`/`AGGREGATE.md`/`MANIFEST.json`, lane `LOG.md`/`SCORECARD.md`/reports).
- r16adj acknowledgment was re-measured only on tracked fleet surfaces; sibling working trees were not re-swept (they are outside a leaf's read scope in this wave).
- Non-kotoba L0 lines were not semantically adjudicated beyond the marker scan; D-137..D-139 were not verified, and D-140 was read only through `AGGREGATE.md` rows.
- The round-47 C1/C2/C3 claims and the round-46 report's other sections were not tested; other falsify seats own them.
- I did not verify that `AGGREGATE.md`'s line numbers (1811-1819, 1236) survive the next aggregator refresh; they are stamps at fleet HEAD `c2e2913`.
- The missing cross-reference (F4) is classified against `../PROTOCOL.md:525-526`; the rule's application to a *partial* restatement is a judgement call, and I mark it as such rather than as a proven violation.

Confidence: high on all file identities, line states, commit relationships, and the erratum pin (each reproduced above); medium on F4's protocol classification and on F7's "no action required" judgement.
