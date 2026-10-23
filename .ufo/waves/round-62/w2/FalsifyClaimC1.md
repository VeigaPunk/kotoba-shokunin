# FalsifyClaimC1 — attack on C1's claim sentence vs the landed instrument (round-62 wave 2)

Seat: `L1kotoba62.FalsifyClaimC1`. Lane tip measured: `3f911504ce76d9ca186f297d6d4a9cd8ed77508a`
(`git rev-parse HEAD`), one commit past assigned tip `e6da78b` (`git merge-base --is-ancestor
e6da78b… HEAD` → ancestor; the delta commit adds only wave-2 evidence; instrument, counter,
successor sha256s all unchanged and verified below).

Claim attacked (E1-corrected, `plans/round-62.md:252-261`): `python3 -B
verifiers/check_erratum_absorption.py --self-test` prints `errata measured 5 of 5; absorbed K
of 5; surviving N; controls 2 of 2`, "K and N computed from the runs and printed; exit 0 iff
all five errata were measured in both directions and the two seeded controls classified
correctly."

## Verdict

The sentence **literally matches the landed exit rule** — no post-data target change,
after-state quoted exactly — but its two fixed fields are weaker than the plan's kill-rule
prose: `measured` is a hard-coded schema constant (can only ever print 5), `K`/`N` never gate
exit, and a do-nothing attack catalogue reaches `5 of 5 … controls 2 of 2`, exit 0. The claim
as amended is honest; the evidentiary weight of "measured 5 of 5" is nil on its own.

## Verified clean (commands run, outputs verbatim)

- **Re-run at tip** — `cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B
  verifiers/check_erratum_absorption.py --self-test; echo EXIT=$?` → prints the receipt's six
  lines byte-identical (`errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of
  2`, six `survivor …` rows), `EXIT=0`. Matches `.ufo/waves/round-62/C1-absorb-measure.txt:7-18`.
- **Pin** — `sha256sum verifiers/check_scoped_rules.py` → `5a5adc945e58…` = `COUNTER_SHA256`
  (`check_erratum_absorption.py:15`); imported-module `self_sha()` double-checked at :92-96.
- **No post-data target change** — `git log --follow plans/round-62.md`: freeze `45a7ecf`
  17:45 → E1 `5c924b0` 17:54 → E1-add2 `9228be4` 17:58; instrument `git log` last touched
  `3e7aed9` 18:21; first data receipt `f9ab081` 18:22. All amendments precede data.
- **Controls before data** — instrument and `controls/absorption-hollow.txt` land in the same
  commit `3e7aed9` (`git show --stat 3e7aed9b`); the matrix receipt lands in the next commit
  `f9ab081`. Hollow → exit 1 `guard-mutation direction is missing…`; label → exit 1 `seeded
  controls did not classify…` (receipt lines 8/13); both failure strings reproduced
  independently by Probes B/G/I below (same `require` sites fire).
- **After-state quote** — `LOG.md:2548` quotes the exact printed line + exit 0 + all six
  survivor ids; `SCORECARD.md:36` quotes the same line; knowledge entry
  `corpus/knowledge/erratum-absorption-round62.md:21` same quote.
- **Universal clauses** — none found over-reaching. Entry :31 bounds itself: "These are
  results for the frozen matrix, not universal guarantees about other instances"; declared
  bounds F6/G9, E2 canonicalization, A4(iii) at :39-41; Q57 (`corpus/QUALITY.md:68`) is a
  per-class conditional. The claim's arm list checks out: `scope_conjunct` calls `path_site`
  (`check_scoped_rules.py:1109`), so `a1_conjunct + scope_conjunct/path_site` is accurate.

## Findings

### F1 (Medium) — `measured 5 of 5` is a schema tautology; the do-nothing catalogue reaches the claimed line

`main` exits 0 iff `summary.measured == 5 and summary.controls == 2`
(`check_erratum_absorption.py:494`). `measured` is `len(run.baseline)` (:397) over the
hard-coded 5-entry `ERRATA` tuple, and `validate_run` requires `set(run.baseline) == names`
(:330) — so after validation `measured` is 5 by construction, and `"of 5"` is a literal. `K`
and `N` are printed but never enter the exit code. `score_one` (:248-253) enforces only
"list of strings", so the claim's parenthetical "(a non-empty reason list naming the arm)"
is unenforced — any non-empty list counts, no arm named.

**Do-nothing probe (A), in-process, lane untouched** — all 10 `attack.score` callables
replaced with `lambda c: ["trivial rejection"]` (module loaded via `importlib`, `ERRATA`
replaced in memory, `m.main(["--self-test"])` called):

```
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 0; E2b 0; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 0 of 5; surviving 0; controls 2 of 2
A => rc=0
```

The instrument prints `measured 5 of 5` and exits 0 when all instances are trivially
"rejected" by a constant. Only the single content-variant pair carries an asserted expected
verdict — `expected_rejected` is read at :418/:420 for `e2-url-unrelated-path` and its
variant; the other nine attacks' `expected_rejected` fields are dead data (grep: declared
:31, set :122, asserted nowhere else). So `measured 5 of 5` means "the dict was shaped
right", not "the errata's classes were exercised". E1's own defect rule ("if it prints 5 of
5 [absorbed] … the frozen instances were not the erratum's class", plan :263-264) therefore
depends entirely on catalogue honesty, not on the gate.

### F2 (Medium) — kill-rule (iii) overclaims: an erratum's own mutation is never required to do anything; only E2's is

Plan `round-62.md:95-98` claims: "(iii) each guard mutation must be shown to change exactly
its erratum's verdicts and no other class's (isolation arm)". The instrument enforces only
the negative half: `summarize` requires off-diagonal verdicts unchanged (:367-369); the
diagonal is never `require`d. For rejected classes the flip is implicitly credited into
`absorbed` (:383) — but nothing gates it, so a broken mutation silently demotes its class
out of BOTH buckets (absorbed-and-surviving do not partition the five):

**Probe G2** — delete E2b's `patches` (mutation becomes a no-op):

```
guard flips: E2 2; E2b 0; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 1 of 5; surviving 6; controls 2 of 2
G2 => rc=0
```

E2b vanishes from `absorbed` without appearing in `surviving`, exit still 0. **Probe K** —
re-point all three surviving classes' patches at inert `self_sha` (a real attribute,
inert for every attack): prints the identical real-data line (`absorbed 2 of 5; surviving 6`)
and exits 0 — surviving classes' mutations are presence-only (`validate_run` :336-345 checks
the sweep exists and is shaped, not that it touched a live guard). The only mutation the
gate truly requires to admit is **E2's**, and only because `run_matrix` reuses
`ERRATA[0].patches` for the absorbed-control's after-direction (:315) — an incidental
coupling, not an independent control. `LOG.md:2549` honestly lists only the three arms
actually armed (hollow, label, real); the overclaim lives in the plan's kill-rule text.

### F3 (Medium) — "computed" is not "verified": a forged run-record set passes `summarize` at `absorbed 5 of 5`, exit 0

`validate_run` checks run-records' shape and instance ids, never re-scores. Feeding
`summarize` a hand-shaped `MatrixRun` (baseline all-rejected, mutations accepting only the
diagonal — off-diagonals must stay rejected or isolation :368 correctly kills it, verified),
controls shaped correctly:

```
fabricated summarize: measured=5 absorbed=5 survivors=0 controls=2
forged line: errata measured 5 of 5; absorbed 5 of 5; surviving 0; controls 2 of 2
main() exit for that summary: 0
```

So even a *computed* line carries no proof that scoring happened; the only live re-scoring
in `self_test` is the one content-variant pair and the three negative auditor probes (all of
which DO fire — Probes B/G/I/J below). This is the semantic-layer version of the sibling
finding already recorded in the entry (`:51`, `FalsifyMatrixMutants` m3: a hardcoded line
above computed rows exits 0). Bounded: in the landed bytes `run_matrix` is the only producer,
so this attacks the claim's evidence strength, not the recorded verdict.

### F4 (Low) — plan file retains self-contradicting pre-E1 definitions

`plans/round-62.md:34-36` still prints the superseded literal line `absorbed 4 of 5;
surviving 2`, and bullets :40-56 still define "measured" as "scores each instance **rejected**"
and "an erratum whose instances survive the committed counter is **not absorbed**" —
directly contradicted by the landed data (3 errata, 6 instances, survive and print
`measured 5 of 5`). E1 (:252-273) corrected the counted line but the where-bullets and the
stale literal were never amended; LOG/SCORECARD quote only the corrected line, so this is a
plan-internal readability defect, not a ledger defect.

## Tripwires confirmed armed (probes that correctly failed)

| Probe | Mutation | Result |
|---|---|---|
| B | A + `variant_score` constant-reject | exit 1 `content variant differs from its frozen expected verdict` |
| I | all 10 attacks trivially accepted | exit 1 `content-variant original differs from its frozen expected verdict` |
| G | E2 `patches` deleted | exit 1 `seeded controls did not classify in both directions` (control reuse of `ERRATA[0].patches`) |
| J | surviving classes' patch names typo'd | exit 1 `…has no attribute 'alias_sha_why_typo'` (getattr fails closed) |
| F1 | forged run with off-diagonal flips | `MatrixFailure: E2 guard mutation changed E2b verdicts` (isolation armed) |

## Residual risk / gaps

- Nothing verifies the 10 frozen instances actually exercise their named counter functions
  (they do today — `key_attack`→`a1_conjunct`/`scope_conjunct`, `sha_attack`→`alias_sha_why`,
  `action_attack`→`action_conjunct`, `alias_attack`→`render_form`/`alias_why`,
  `_reopen_score`→`url_key`/`reopen_why` — confirmed by reading the scorer closures), but a
  catalogue drift would print `5 of 5` regardless (F1).
- `absorbed + surviving` need not equal 5 (F2): a rejected-but-unflipped erratum is
  unclassified and invisible in both printed counts; the report layer should name it
  (receipt does name per-instance survivors, so a gap is detectable only by counting rows).
- The C1 counted predicate as landed is honest per the E1 text; the strongest statement it
  supports is "the five errata were exercised in both directions and the controls
  classified" — exactly E1's wording. Any future wording that re-reads `measured` or
  `absorbed` as gated quantities would overclaim.

## Tooling

No installs; python3 3.14 system binary and git only. No lane writes: all probes loaded the
module via `importlib` and mutated in-memory state; `git` calls were read-only
(`rev-parse`, `log`, `show --stat`, `merge-base`).
