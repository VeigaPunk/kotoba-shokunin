# kotoba round 62 — plan (attempt 1, hyaku run 5)

Date: 2026-10-23. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base tip:
`a745411c66d4765e9ac0ce48f1d96c34f425dab4` (branch `master`, pushed; r61 close tip).
Axes: **depth + consistency (calibration sub-axis)**. Lowest owned axis: depth (9);
consistency/calibration is 10 (saturation line). The all-axes reading of "lowest
non-retired axis" (freshness/adjacency 8.0, advisory) remains the open round-47 L0
question; C1 works depth, the lowest owned axis, and satisfies the owned-only reading.

Shapes: two v1 waves — wave 1 build (32–64 seats), wave 2 falsify (32–64 seats), plus one
residual ≤8-seat reviewer/critic call if wave 2 leaves leftovers. Round total ≤128. The
§3 planner seat is held by the L1; a bounded planning data-walk rides `ScoutPriorReceipts`
and `RevPlanScope` (recorded in the report).

## Round claims (2)

### C1 — depth: the erratum absorption matrix (E2, E2b, E2c, E2e, E2f)

**Motivating evidence (r61 close).** The r61 report credits "five pre-data arm amendments
each forced by a measured attack (MutA3, MutFixtures, MutA4 ×3 seams, MutA1, MutA2)"
(`.ufo/reports/round-61/kotoba.md`) — but every one of those attacks was measured against
the *draft predicate text*, and no committed receipt measures the **landed** v3 counter's
arms against the seat's attack classes. The r61 closure is expected to ask: is each erratum
absorbed by the bytes that landed? Round 62 answers it with a frozen instrument.

**Frozen predicate (one sentence, same in plan, counter label, receipt):**

```
python3 -B verifiers/check_erratum_absorption.py --self-test
```

prints

```
errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2
```

and exits 0, where:

- **errata measured 5 of 5** — for each erratum class (E2/A3 url_key, E2b/A3(b) rendering
  alias, E2c/A4(iv) full-sha alias, E2e/A1 guarded key form, E2f/A2 guarded action) the
  instrument runs **two fresh attack instances** through the committed counter's own
  arm-level functions (`url_key`/`reopen_why`, `render_form`/`alias_why`,
  `alias_sha_why`, `a1_conjunct`+`scope_conjunct`/`path_site`, `action_conjunct`), and
  scores each instance **rejected** (a non-empty reason list naming the arm) under the
  committed counter.
- **absorbed k of 5** — an erratum is *absorbed* only when **both** its instances are
  rejected **and** disabling that erratum's guard in-process (the guard function replaced
  by an admitting stub) makes **both** instances accepted. An erratum whose instances
  survive the committed counter is **not absorbed** regardless of the guard mutation.
- **surviving N** — the number of frozen instances the committed counter accepts. Each
  survivor is printed as `survivor <erratum> <instance-id>: <reason list>`.
- **controls 2 of 2** — the instrument's own seeded controls: one instance pair the
  committed counter rejects (must score absorbed) and one pair it accepts (must score
  surviving). A hollow instrument that prints the line without running both directions
  fails the second control (recorded as the pre-data control receipt).

The instrument pins the audited counter's sha256 (`5a5adc94…`, r61 freeze) and **fails
closed** (`exit 2`) if the working-tree counter bytes differ, so it can never silently
audit a different counter. It is an arm-level audit; it does not re-run the seven worlds —
the world-level predicate stays C1's r61 measurement and is re-run unchanged (`--self-test`
and `--fetch`) as a no-harm arm.

**Expected result, declared before data.** Reading the committed counter before writing
any instance: `action_conjunct` implements the forward/reverse support fractions but **no
raw-tokenizer event-claim conjunct (E2f's G7) and no compound-purpose conjunct (G9)**
(`verifiers/check_scoped_rules.py` `content_words` strips backticked spans; no claim-verb
code exists). The matrix is therefore expected to report **E2f unabsorbed** with its
event-claim instance surviving: `absorbed 4 of 5; surviving 1` (the count printed is
computed; if it prints 5 of 5 the frozen E2f instances were not the erratum's class and
the round records a counter defect). The other four errata are expected absorbed.

**Successor (same claim, causally part of C1).** The E2f gap is closed in a copy of the
counter, `verifiers/check_scoped_rules_v31.py`, carrying the frozen E2f form
(G5 key-on-line **and** G7 raw-tokenizer event-claim conjunct, with the F6 compound-purpose
bound still declared as surviving), measured by:

```
python3 -B verifiers/check_scoped_rules_v31.py --self-test
```

which must print the unchanged r61 line `worlds reject 7 of 7; eligible rows pass 4 of 4`
**and** the added line `E2f fresh instances reject 2 of 2`, and exit 0. If the successor
cannot keep both sides, it does not land; the gap stays reported as a named bound and the
round records the miss honestly. The successor never edits `check_scoped_rules.py` (the
r61 frozen instrument, sha `5a5adc94…`, stays byte-identical — Q28).

**Before → after.** Before: no committed receipt measures any erratum against the landed
counter; the five amendments are evidenced against plan text only (`grep` over
`.ufo/waves/round-61/` receipts for per-erratum arm-level results prints 0 of 5). After:
`errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2` (the matrix), and
the successor's `E2f fresh instances reject 2 of 2` with worlds/eligible unchanged.

**Kill rule (Q25/Q37/Q47).** The instrument's self-test carries: (i) a *hollow* auditor
that prints the predicate without running the guard-mutation direction must fail; (ii) a
*label* auditor that returns constants must fail the controls; (iii) each guard mutation
must be shown to change exactly its erratum's verdicts and no other class's (isolation
arm). The control receipts are committed **before** the matrix data run (M90).

### C2 — calibration: the routed-repairs successor (honest-pass + self-derived count)

**Motivating evidence.** `ExecC2Audit` (`.ufo/waves/round-61/wave/ExecC2Audit.md`)
measured that the r61 frozen counter scores **6 of 6 on 15 dishonest variants** and also
**rejects honest repairs** written in the lane's house style (`exit=0`; pointers split
across two lines). R61's SCORECARD names the successor measurement as the next step
("G-a registry-roster re-derivation … as a separately identified successor measurement,
NOT a rewrite of the frozen six").

**Frozen predicate:**

```
python3 -B verifiers/check_routed_repairs_v2.py --self-test
```

prints

```
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
```

and exits 0. Universe:

- **dishonest rejected 6 of 6** — six frozen synthetic trees, each of which the r61 frozen
  counter scores 6 of 6 (`check_routed_repairs.check_repairs` imported and re-run
  in-process by the successor's self-test; the frozen file is not modified): (D1) a stale
  count (tree-derived 30, line says 29), (D2) a negated correction ("did not claim 32…"),
  (D3) the inverted R-c pointer (C1-measure first, freeze2 named as the wrong one),
  (D4) a bodyless census (`exit=0` only), (D5) substring ids (`Q560`, `M910`), (D6) an
  ancestry receipt whose `exit 0` does not belong to the merge-base command and whose
  operands are not two distinct 40-hex hashes. Each must score **< 6** under the
  successor (rejected).
- **honest passed 2 of 2** — (H1) the same six repairs written in house style (`exit=0`
  in census/ancestry, R-c pointers split across two adjacent lines, asserted rather than
  negated), which the frozen counter scores **4 of 6**; (H2) the measured tip tree, which
  must score 6 of 6 via the CLI.
- **base 0 of 6; tip 6 of 6** — the CLI at base `f3246d1493b60ea1c0d947a19c39f9e08e92f326`
  exits 1 with `0 of 6`, and at the round-62 data revision exits 0 with `6 of 6`.

G-a is the self-derived count: R-a's declared `committed <n>` must equal the number of
`^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$` names under
`.ufo/waves/round-60/build` **at the measured revision** (`git ls-tree -r --name-only
<rev> -- .ufo/waves/round-60/build`), and the claimed count must exceed it. The other
hardened forms are ExecC2Audit's G-b/G-c/G-d/G-e/G-f, each in its smallest form (assertion
direction, bounded window, census body, exact ids, owned exit).

**Before → after.** Before (re-measured, committed receipt): frozen counter
`dishonest accepted 6 of 6; honest passed 1 of 2`; base 0 of 6. After: successor
`dishonest rejected 6 of 6; honest passed 2 of 2`; tip 6 of 6.

**Kill rule.** A label-only successor (returns constants) fails its own control arm (the
self-test's base-world arm must print 0 of 6 and its D/H arms must be computed from the
input blobs, never asserted); a successor that rejects everything fails H1/H2.

## Controls committed before any data (M90)

1. `verifiers/check_erratum_absorption.py` (draft) + its **hollow-auditor control**
   (`.ufo/waves/round-62/controls/absorption-hollow.txt`): the constant-printing variant
   run under `--self-test` exits 1, naming the controls arm.
2. The **before** receipts:
   `.ufo/waves/round-62/controls/absorption-before.txt` (grep over `.ufo/waves/round-61/`
   receipts showing 0 of 5 erratum-level measurements),
   `.ufo/waves/round-62/controls/frozen-repairs-dishonest.txt` (frozen counter scores the
   six dishonest trees 6 of 6 and H1 4 of 6).
3. `verifiers/check_scoped_rules.py` sha256 pin (`5a5adc94…`) recorded in the absorption
   instrument and its control receipt.

The data commits (the matrix run, the successor runs, the SOURCES row, the entry, the
lesson, LOG/SCORECARD) come after these controls land.

## Frontier step

- New source row **S118** — `https://code.claude.com/docs/en/memory.md` (the rules
  frontmatter reference S112's table links to), opened this round with a committed
  snapshot; its `paths` frontmatter text grounds C1's E2e instances (the key takes glob
  patterns, listed or inline). Fetched once by `SrcRulesFrontmatter` and re-verified by a
  second seat; sha256 recorded in the row and snapshot.
- Census before → after with `scripts/sources-census.sh validate … kotoba` (before exit 0
  is recorded at round start; after at round end).
- Lesson `corpus/lessons/round-62.md` § Mistakes: mined class = **"erratum recorded as
  absorbed without an arm-level receipt"** (the E2f G7/G9 gap), captured-by = C1's
  absorption matrix, fix = the successor + QUALITY row.
- Sourced claim: C1's E2e instances cite S118's `paths` text (row opened this round).

## Wave shape

Wave 1 (`kotoba-r62-w1`, policy v1, 32–64 seats): build the absorption instrument drafts,
the ten fresh instances (2/class), the five benign controls, the guard-mutation table, the
successor counter v3.1 draft, the routed-repairs successor draft, the six dishonest + two
honest trees, the S118 open, the before receipts, the recon/attack seats (connector,
scout, reviewer, critic, sentinel, revenger), and the scribe drafts (entry, Q57, registry
rows, lesson, LOG/SCORECARD).

Wave 2 (`kotoba-r62-w2`, policy v1, 32–64 seats): fresh seats attack the landed bytes —
re-run every counting command, re-derive each of the ten instances, re-run each of the
five guard mutations, re-open S118, attack the two new gates, mutation-test both new
gates, attack the C1/C2 claims against the frozen sentences, check the registry rows, the
lesson/no-harm/census, and the report claims.

Residual: one ≤8-seat reviewer/critic `task` call if wave 2 leaves leftovers; counted in
the round total.

Routing: the host route table decides; no model aliases in the spec. Planner = L1
(validator rejects the seat); the planning data-walk rides `ScoutPriorReceipts` +
`RevPlanScope`. Executors only for code; prose drafts to scribes; attacks to
reviewers/critics/mutation-testers/scouts.

## Commit order

1. this plan + `.ufo/waves/round-62/census-before.txt` (freeze commit);
2. wave 1 evidence (spec, registry, seat reports);
3. the two instruments + their control receipts (controls before data);
4. the ten instances / five mutations / six dishonest trees frozen in the instrument's
   self-test (same commit as 3);
5. data: matrix run, successor runs, C1 successor self-test, before receipts;
6. SOURCES S118 + snapshot + knowledge entry + QUALITY Q57 + lesson + README index + SKILL
   registry rows + LOG § Round 62 + SCORECARD;
7. wave 2 evidence;
8. report (fleet helper) citing the pushed lane tip.

All lane commits go through `scripts/hyaku/jj-lane.sh commit <lane> --as kotoba`. The fleet
report goes through `scripts/hyaku/fleet-commit.sh`.

## Routed r61 items (report-only unless stated)

- The r60 fleet-report erratum authorization is an **operator decision** (L0, fleet commit
  `c6746bc`); this round names it and does not decide it.
- The v3 scoped-rules counter stays a **gate**; no capability row. Its SKILL.md registry
  row is checked for honesty (the `gate` kind, the self-test flag, the frozen sha) and
  annotated with the r62 absorption finding.
- SentNovelty/SimplEntry classes (r61 outstanding) are re-covered by wave seats on the new
  entry and lesson (novelty + economy pass), not assumed covered.
- The E1 hollow-counterexample class (M92) is re-attacked against C1's matrix: the matrix
  must show both directions and a benign side; a presence counter cannot pass it.

## Erratum E1 — C1's frozen line corrected, and the successor moved out of the counted predicate (pre-data, 2026-10-23)

Two wave-1 seats (`ScribeLog62`, `ExecGateArms`) independently flagged that §C1's frozen
predicate (`absorbed 4 of 5; surviving 2`) contradicts §C1's expected-result paragraph
(`absorbed 4 of 5; surviving 1`). `ScoutCounterApi` then executed the arm-level probe and
measured two more absences than §C1 assumed:

- **E2f** — no G7/G9 code exists: `action_conjunct` implements the forward/reverse
  fractions only, `content_words` strips backticked spans, and no claim-verb conjunct is
  present; a backticked `InstructionsLoaded` cell returns `[]`.
- **E2e** — the guarded form's colon-only and commented-key clauses are absent:
  `KEY_SUFFIX_RE` is `["'`]?[ \t]*[:=]` (accepts `=`), and `key_site` does not reject a
  commented key. The probe measured both accepting.

**No C1 matrix data has run** (the instrument is still a draft; no survivor has been
scored against a committed instrument). Amendment, before any data:

1. The frozen predicate line is corrected to:

   ```
   errata measured 5 of 5; absorbed K of 5; surviving N; controls 2 of 2
   ```

   where K and N are **computed from the runs** and printed; exit 0 iff all five errata
   were measured in both directions and the two seeded controls classified correctly.
   The after-value C1 counts is `errata measured 5 of 5; controls 2 of 2` (fixed), with
   K/N and every survivor name printed in the same receipt and quoted in the report.
2. The expected result is corrected: at least **two** survivors are expected (E2f and
   E2e); if the matrix prints 5 of 5 or fewer than two survivors, the frozen instances
   were not the errata's classes and the round records a counter defect, not a pass.
3. The successor (`verifiers/check_scoped_rules_v31.py`) moves **out of the counted
   predicate**: it is landed fix evidence reported under Landed changes with its own
   measured line `worlds reject 7 of 7; eligible rows pass 4 of 4; survivors closed S of S`
   (S = the matrix's survivor count), and it lands only if both r61 sides stay green. C1's
   counted predicate is item 1. This keeps the claim's after-state re-derivable with one
   command while the successor remains honest frontier repair.
4. C1's before-state is `0 of 5` committed erratum-level measurements against the landed
   counter (`ScoutPriorReceipts` census: the five seat attack tables measured the draft
   text/v2 oracle; 0 receipts name the landed counter sha for any erratum class).

The wave-1 seats' drafts are unaffected except that `ExecAbsorbInstrument` and
`ExecSuccessor31` must implement this corrected line; the L1 relays it.

### E1 addendum — E2c's conditions 5 and 6 are also measured absent (pre-data, same window)

`ExecInstancesA4` (wave 1) measured, before any matrix data, that the landed
`alias_sha_why` enforces only the anchored `supersedes S###` prefix: it returns `[]` for
(i) a wrong-target declaration (`supersedes S048 —` where S048 records only the
`00e45ea5` prefix and not the counted row's full sha — E2c binding condition 5) and
(ii) a declared byte-identity row whose anchor cell still carries a `fetched <ISO>`
assertion (condition 6). `ExecInstancesA1` measured the E2e negated-key case accepted
(`Do not use paths: src/legacy/**/*.ts` → `path_site=True`, `scope_conjunct=[]`), alongside
the equals-form and commented-key accepts from `ScoutCounterApi`. The corrected expected
result is therefore **at least three survivors** (E2c, E2e, E2f); E2 and E2b are expected
absorbed. The matrix's `absorbed K of 5; surviving N` stays computed; the receipt names
every survivor with its instance id and reason. The successor's scope grows to close the
survivors it can (E2c conditions 5/6, E2e colon/negation/commented keys, E2f G7) while the
r61 sides stay green; anything it cannot close stays a named bound. `ExecAbsorbInstrument`
and `ExecSuccessor31` are relayed this addendum.

### E1 addendum 2 — commit order corrected (pre-data, F10)

"Controls before data" means every pre-data control receipt lands before the **first**
matrix/successor data receipt, in this measured order: plan freeze `45a7ecfa` → erratum E1
`5c924b02` → the before receipts (`absorption-before.txt`, `frozen-repairs-dishonest.txt`,
`seat-counts-r61.txt`) and the seat-count gate `9f03dcd7` → wave evidence → the instrument
and its hollow/label/presence controls (same commit) → the matrix and successor data
receipts. The critic's F10 ambiguity is resolved in favour of the stricter reading; no
data run precedes its controls. F3/F5's stronger controls are implemented inside the
instruments' self-tests: a content-variant arm (a renamed/re-valued instance whose verdict
flips — a label table fails), a constants arm, and the paired tree-population arm
(`build_paths` 29 vs 30 with identical repair blobs — a frozen-score remap fails).
