## Round 80 — C1 consistency (calibration sub-axis: tip battery 1 of 6 → 6 of 6) and C2 depth (allowed-tools form matrix 0 of 6 → 6 of 6; grant semantics exploratory)

- **Plan/base:** `plans/round-80.md` (frozen with the validated 64-seat wave and the base receipts at `c2f69d4`; Addendum 1,
  the pre-data freeze clarification of erratum E5's exact amended line set, at `308bff9`); lane base
  `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Two fresh claims on distinct axes — nothing from the r77–r79 frozen predicates
  is reused unchanged. **C1 (consistency, calibration sub-axis), frozen predicate:** `python3 -B verifiers/check_tip_battery.py
  --rev <rev>` (round-80 bytes: the round-72 frozen counter amended by erratum E5 as clarified pre-data in Addendum 1 —
  `LINE_CAP` 40→60; exactly two `INSTRUMENT_PINS` entries gained, the composed E04∘E05 blob for
  `verifiers/verify_corpus_integrity.py` and the E05 blob for `verifiers/verify_corpus_independent.py`; the self-test fixture
  constants that hard-assert the old bound re-anchored to derive from `LINE_CAP` with arm semantics unchanged and the
  assertion count unchanged at 69; docstring cap mentions updated — and nothing else; the amended counter's sha256 and the
  hunk inventory are recorded in the round-80 freeze receipt `freeze-shas.txt` under `.ufo/waves/round-80/receipts/` before
  any after-value is measured) prints `guards 5 of 5`
  and `tip battery exit 0: 6 of 6` and exits 0 at `<rev>`, both in the `--repo .` form run from the lane root and in the
  absolute `--repo <lane>` form; at the r80 base it prints `tip battery exit 0: 1 of 6` and exits 1. **C2 (depth,
  sourced), frozen predicate:** `python3 -B verifiers/check_allowed_tools.py --rev <rev>` prints `allowed-tools surfaces
  documented N of 6` and `generator world: M of 6` and exits 0 iff N == 6 and the tree conjuncts hold; at the r80 base it
  prints `allowed-tools surfaces documented 0 of 6` and exits 1. The headline asserts **form-level documentation only**
  (Q71/Q74): the grant-semantics matrix is the exploratory rider, and its verdict and reviewer pointer sit on the SCORECARD
  row instead of a number.
- **C1 before-value (measured at `398cbe1b`, direct exit capture):** `python3 -B verifiers/check_tip_battery.py --rev
  398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93 --repo .` → `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery
  exit 0: 1 of 6`, exit 1 (`.ufo/waves/round-80/receipts/tipbattery-base-dot.txt`). The five red gates, each read from its own
  exit status: `check_gate_registry.py` exit 1 (`60 of 62` lane-verifier rows conformant; `check_desc_craft.py` and
  `check_r75_routed_repairs.py` unrouted); `check_assertion_floors.py` exit 1 (the checklist self-test's live governance
  arm re-reds on the same LOG.md:2818 token; the plan's base pass records the line `FAIL checklist observed=1863
  floor=1863 self_test_failures=1`); `verify_skill_checklist.py` exit 1 (`FAIL governance.citation_resolves` at
  LOG.md:2818); `verify_corpus_integrity.py` exit 1 and `verify_corpus_independent.py` exit 1 — the plan's base pass
  records six DRIFTs (`tracked_files` 152≠144, `unindexed` 1, `report_total` 109≠99, `report_dead` 1, `commit_total`
  46≠43, `commit_unresolvable` 2) and the independent gate's `unindexed` 1 with `commit_unresolvable` 2.
  `check_correction_sweep.py` exit 0 is the one green gate. The same gates read rc 0 through `cmd | tail; echo $?` — the
  round's mined mistake M80-1 (`.ufo/waves/round-80/receipts/m80-1-pipe-vs-direct.txt`: pipe-rc 0 vs direct-rc 1).
- **C1 repair set (five pieces, each reviewed in the round-79 wave and ported to `398cbe1b` against the current bytes):**
  1. **Registry rows.** `SKILL.md` § Gate registry gains the two withdrawal rows for `check_desc_craft.py` and
     `check_r75_routed_repairs.py` (r79 `Kb79E01Registry.patch`, sha256 `c411106e…`, +2 lines) plus a third row for the new
     `verifiers/check_allowed_tools.py` — C2's counter; a new lane verifier without a row would re-red the registry gate.
  2. **The dead LOG citation.** A relative symlink at `.ufo/reports/round-76/kotoba.md` targeting the fleet report: one
     artefact, one byte-stream (sha256 `a025051d…` = the fleet file), fails closed when the fleet tree is absent, and edits
     no record (r79 `Kb79E02LogCitation.patch`). The target string is never written backticked in tracked prose — the
     governance gate caps parent-directory hops at 3, and the r79 seat's landmine note stands.
  3. **Index + baseline.** Coverage-map rows for `corpus/lessons/round-79-verifier-spotcheck.md`, `corpus/lessons/round-80.md`
     and `corpus/knowledge/allowed-tools-surfaces-round80.md`, then
     `.ufo/waves/round-79/build/refresh-corpus-baseline.py --repo .` re-records the baseline at the final pre-report commit
     (clean-tree precondition; `--carry` none — every zero class must read 0 after repairs 4 and 5).
  4. **The dead report pointer.** `verifiers/verify_corpus_integrity.py` resolves `<rev>:<path>` report pointers as git
     object expressions, citing the repo first and the fleet second, with a red-before regression arm
     (r79 `Kb79E04DeadPointer/Kb79E04DeadPointer.patch`, sha256 `d7169dd8…`, +17 lines).
  5. **The external-commit grammar class (new this round, both corpus gates).** A commit citation is classified external — and
     counted in its own INFO class instead of `commit_unresolvable` — when the hex token sits in the `owner/repo@<hex>`
     grammar **or** its line names an explicit third repository (the plan's "or otherwise an explicit third-repository
     citation" clause, evaluated at line scope). Rationale (Q61): a gate states its resolution set, and a third-repository
     object is absent from lane and fleet *by construction*. Lane and fleet hex tokens keep the exact current resolution
     behavior; the change is classification-only, with red-before arms in both gates' self-tests. The two counted tokens at
     base are the same third-repository commit `7bb48f213ac6…`: `corpus/SOURCES.md:171` (row S230, the pi-mono page) and
     `corpus/SOURCES.md:172` (row S231, the Mistral Vibe page). The fetch records settle which row is wrong:
     `.ufo/waves/round-79/snapshots/S230.fetch.json` records pi-mono main at fetch time as `bb65e3e4…` (blob sha1
     `19d2bf28…`), and `S231.fetch.json` records Mistral Vibe main as `7bb48f21…` — so the S230 anchor cell cites another
     repository's commit. That is a row defect the INFO class keeps visible instead of excusing; the anchor cell is out of
     scope to rewrite (CORPUS rule 2), and the object is absent from lane and fleet (`git cat-file -t` rc 128 in both). The
     r54 lesson tokens are quoted context the integrity gate already excludes (`quoted-excluded=6`); the fix must leave them
     classified as quoted. Consequence for C2's own bytes: any full-hex commit citation the new entry carries must sit on a
     line with an explicit third-repository marker (an `owner/repo` token or URL); a bare repo name is not a marker, and a
     class whose red-before arm keeps an unmarked absent token on the red path would otherwise turn landing the entry into a
     third `commit_unresolvable`. The C2 entry seat's remedy is stronger: carry no commit-shaped citation at all and cite the
     pinned snapshot / fetch record instead.
- **Erratum E5 (declared in the plan before any data, its exact amended line set frozen pre-data in Addendum 1):** (1)
  `LINE_CAP` 40→60; (2) exactly two `INSTRUMENT_PINS` entries gained — the composed E04∘E05 blob for
  `verifiers/verify_corpus_integrity.py` and the E05 blob for `verifiers/verify_corpus_independent.py` (the E04-only blob
  `051b8c5f…` is a cross-check, never the pin); (3) the self-test fixture constants that hard-assert the old bound re-anchored
  to derive from `LINE_CAP`, arm semantics unchanged, assertion count unchanged at 69, no arm added or dropped (a 41-line gain
  under cap 60 passes the size guard alone and still FAILS `instrument-pin`); (4) docstring/comment cap mentions updated. The
  size arithmetic is 22 lines already spent at base (measured: "instruments added 22 / deleted 3 lines (cap 40)" in the base
  battery receipt) + 17 (repair 4) = 39, leaving repair 5 at most 21 added lines across both corpus gates to stay ≤ 60. The
  pin guard carries the anti-laundering load — every instrument byte at the measured rev must equal the round-72 base blob or
  a reviewed pin — and the size bound is secondary: a 2-line stub still fails under any cap (+2 / −~1000).
- **C1 kill rule:** any control world reaching `6 of 6`, a repair that needs a guard's *logic* edited (the five guards' checks
  stay semantically identical), or a repair set whose instrument growth exceeds the declared cap arithmetic
  (22 + 17 + ≤21 ≤ 60) stops C1 as an honest stop — no narrowing after data.
- **C1 control worlds (declared before any after-value, run on the round-80 counter bytes):** W0 the base tree with an empty
  commit (expect `guards 5 of 5; tip battery exit 0: 1 of 6`); W1 registry rows only (≤3 of 6); W2 the symlink only (≤3 of 6,
  per the r79 receipt); W3 coverage rows + baseline refresh only, no instrument repair (integrity still red on `report_dead`
  and `commit_unresolvable` — proves repairs 4 and 5 load-bearing); W4 the E04 instrument only (≤3); W5 the grammar class only
  (≤3); W6 the failing checks deleted or stubbed inside any battery instrument (expect `instrument-pin` and/or
  `instrument-size` failure, never 6 of 6); W7 a spot-check file edited (`spotcheck-identity` failure). Receipts:
  {{LANDED:c1-control-receipts}}.
- **C1 outcome:** {{LANDED:c1-tip}} — both invocation forms print `guards 5 of 5` and `tip battery exit 0: 6 of 6`, exit 0
  (receipts {{LANDED:c1-tip-dot-receipt}}, {{LANDED:c1-tip-abs-receipt}}). Until both receipts exist at the landed tip, no
  after-value or score move is claimed.
- **C2 before-value:** `allowed-tools surfaces documented 0 of 6`, exit 1 at the r80 base — the entry, the `SKILL.md` rule
  line, the `PROVINCE.md` § Core bullet and the registry row are all absent there (the plan declares the figure; the r79
  draft counter's base receipts print `allowed-tools surfaces backed 0 of 6` at the r79 base,
  `.ufo/waves/round-79/build/base-c2-dot.txt`). The r80 counter's own base receipt at `398cbe1b` is
  {{LANDED:c2-base-receipt}}.
- **C2 data:** the r79 draft counter (`.ufo/waves/round-79/build/check_allowed_tools.py`, sha256 `74e067cc…`) ported to
  `398cbe1b` as `verifiers/check_allowed_tools.py`; the entry `corpus/knowledge/allowed-tools-surfaces-round80.md`; rows
  S226–S231 (the open specification, Claude Code, Factory, Microsoft Agent Framework, pi and Mistral Vibe) keep their
  snapshots at `.ufo/waves/round-79/snapshots/` (18 tracked files, per-source `.manifest` pins), and all six pages are
  re-opened live this round with access receipts; `used-by` moves to the round-80 entry, old→new logged in the lesson.
- **C2 conjuncts:** the r79 shape (entry with `source:`/`verified-at:`/`recheck:`; 11-cell `mined` tier-A/B rows with
  `used-by` naming the entry and host-exact URLs; snapshot pins equal in the snapshots' manifests, each row's fetch record and
  the counter; located quotes of 5–25 words containing `allowed-tools`, after the first heading per Q70; `opened` =
  `verified-at:` = 2026-10-27) plus the tree conjuncts — (g) one `SKILL.md` rule line naming ≥3 surfaces and a conformant
  registry row for the counter; (h) `PROVINCE.md` § Core names the entry; (i) the counter prints the generator world's score
  (Q71/Q74).
- **C2 controls (declared before any after-value):** C0 base; C1 token dump without snapshots; C2 wrong-page quotes; C3
  shared-banner quotes (Q70); C4 the independent mechanical generator, whose score is printed beside the headline (Q74 — the
  claim does not rest on beating it); C5 label-only; C6 sibling-host; C7 stale snapshot / wrong pin; C8 first-answer baseline
  (N=6 asserted from the census alone, no files — must print 0). Any world the headline would misread as falsifying the form
  claim, or any world making the exit predicate lie, is a counter defect and stops C2. Receipts {{LANDED:c2-control-receipts}}.
- **C2 outcome:** {{LANDED:c2-tip}} — `allowed-tools surfaces documented 6 of 6` with `generator world: {{LANDED:c2-generator-world}} of 6`,
  exit 0; receipt {{LANDED:c2-tip-receipt}}. The grant-semantics rider stays exploratory: verdict and reviewer pointer on the
  SCORECARD row ({{LANDED:scorecard-reader}}), reviewers of record the round-80 non-author closure spot-check — a dispatched
  seat does not count, and the closure is not the author.
- **Frontier:** census before — `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kotoba` → exit 0, 157 rows, 24 existing W04 duplicate-URL warnings
  (`.ufo/waves/round-80/receipts/census-before.txt`); row count `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
  corpus/SOURCES.md` → 157 at the r79 tip and at the r80 base. This round: S226–S231 re-opened live (receipt
  {{LANDED:reopen-six-receipt}}), and NEW rejection rows from the negative sweep starting at S232
  ({{LANDED:rejection-ids}}), each opened this round with URL, access date and a ≤25-word located quote in the lesson
  `## Gate`. Assimilation: the kotoba quarantine-register slice hand-checked ({{LANDED:slice-verdicts}}), adoption stays
  closed — the r79 disposition stands until a slice verdict flips; `merge/kotoba/` is read-only input and nothing is
  appended; `considerthese/2026-10-26.md` proposals 2–5 are dispositioned in the lesson and none is implemented.
- **Mistake mined (M80-1, class `measurement`, captured-by `none`):** the round's own measurement error — gate verdicts read
  through a shell pipeline (`cmd | tail; echo $?` reports the pipeline's last element), which read every gate green at the
  base pass while the true exits were 1. Fix: receipts capture the command's own status (`cmd > f 2>&1; rc=$?`), shown able
  to fail by the same commands run both ways at base (`.ufo/waves/round-80/receipts/m80-1-pipe-vs-direct.txt`).
- **R79-D2 correction notice (append-only; the r79 lesson is not edited):** the round-79 lesson's round-end census line reads
  `151 rows` with `census-after.txt`; the tracked `corpus/SOURCES.md` carries 157 rows at the round-79 tip `6ef6753` and at
  the r80 base, and the r79 round-end receipt is `.ufo/waves/round-79/receipts/census-final.txt`. The `151` figure was not
  re-measured after the six S226–S231 rows landed; corrected by an append-only notice in `corpus/lessons/round-80.md`.
- **Wave shape:** one v2 wave (`ufo-wave-policy-v2.json`, band 64–128), w1 = 64 seats, build and attack together (dispatch
  `.ufo/waves/round-80/w1-dispatch.json`, registry `.ufo/waves/round-80/w1/swarm-registry.json`): 16 executors, 17 scribes,
  9 scouts, 3 connectors, 6 critics, 6 reviewers, 4 mutation-testers, 1 sentinel, 1 simplifier, 1 revenger. Attack share —
  6 critics + 6 reviewers + 4 mutation-testers + 1 sentinel = 17/64 = 26.6 % ≥ 25 % (plan § Round shape, recomputed from the
  registry); the 3 connector seats satisfy the few-connector rule. Settled seat reports {{LANDED:settled-seats}}, dead seats
  {{LANDED:dead-seats}}, all under `.ufo/waves/round-80/w1/`; build outputs under `.ufo/waves/round-80/build/`.
- **No-harm battery (Q72):** at the final pre-report tip {{LANDED:no-harm-tip}} in a sandbox holding the claim's own files —
  the tip battery in both forms, `check_gate_registry.py`, `check_assertion_floors.py`, `verify_skill_checklist.py`,
  `verify_corpus_integrity.py`, `verify_corpus_independent.py`, `check_correction_sweep.py`, the sources census, the sibling
  census and `check_report_pointers.py` at the report commit. Receipts {{LANDED:no-harm-receipts}}.
- **Pointer:** `plans/round-80.md`, `corpus/lessons/round-80.md`, `corpus/knowledge/allowed-tools-surfaces-round80.md`,
  `.ufo/waves/round-80/receipts/`, `.ufo/waves/round-80/build/`, `.ufo/waves/round-80/w1/`.
