# RevSentNovelty — novelty/economy re-cover of the round-62 C1 entry (SentNovelty class)

Seat: `KotobaR62.RevSentNovelty` (reviewer, leaf; no dispatch, no subagent, no ask tool).
Wave: `kotoba-r62-w1` (build). Date: 2026-10-23. Lane tip at dispatch: `45a7ecfac9e203297f3146c45d63f5e79367470c`.

## 0. Status and method (honesty first)

- The r61 wave has **no `SentNovelty.md`** (`.ufo/waves/round-61/wave/` listing; 66 files, none named SentNovelty). Per the assignment fallback, the r61 novelty expectations are taken from the **r61 spec's prompt** for the SentNovelty seat (`.ufo/waves/round-61/wave-spec.json` item `SentNovelty`):
  > "Overclaim scan of the planned texts (plan + ScribeEntryV3 draft shape): flag any wording that claims novelty the r60 entry already disclosed (the round-13 omp applyTo class; S048/S049 filename rows), any 'first' without a sweep, any 'byte-exact' outside Q56's reservation, any 'exhaustive' without enumeration. Deliver the flagged lines with corrections."
- The new entry draft `corpus/knowledge/erratum-absorption-round62.md` **does not exist yet** at review time, and neither does ScribeEntry62's report (`.ufo/waves/round-62/w1/ScribeEntry62.md`). Evidence: `find` over `.ufo/waves/round-62/` shows only `census-before.txt`, `w1-dispatch.json`, `w1-plan.json`, `w1-spec.json`; a workspace-wide `grep` for `erratum[-_]absorption` matches nothing under `/home/vgpnk/Projects/shokunin`; no ScribeEntry62 scratch dir exists under `/fast/scratch/hyaku/kotoba-r62/`; the w1 report dir (created at report time) contains 13 seat reports, none from ScribeEntry62.
- I therefore applied the r61 novelty expectations to the **mandated content of the entry** as frozen by the r62 plan §C1 and the r62 spec's ScribeEntry62 prompt (`.ufo/waves/round-62/w1-spec.json` item `ScribeEntry62`), and cross-checked every mandated fact against the prior homes. Several w1 data seats have already landed measured facts that the entry is obliged to report (`ExecInstancesA1.md`, `ExecInstancesA4.md`, `ScoutPriorReceipts.md`, `ScribeSourcesS118.md`, `SrcRulesFrontmatter.md`, `ExecGateArms.md`, `ExecInstancesA3.md`); those measured facts are used below as the data the entry will carry. When ScribeEntry62 lands, this table applies verbatim to the actual draft; the check is mechanical.

## 1. Prior homes used

| Home | Path |
|---|---|
| r61 entry | `corpus/knowledge/scoped-rules-counter-round61.md` (committed r61) |
| r61 plan errata E2–E2f + E2c binding conditions | `plans/round-61.md` lines 123–254 |
| r61 seat reports (attack tables) | `.ufo/waves/round-61/wave/{MutA1,MutA2,MutA3,MutA4,MutFixtures,MutFixtureEscape,RevE2Boundary,RevEntryGround}.md` |
| r61 receipts | `.ufo/waves/round-61/receipts/C1-worlds.txt`, `controls/C1-base.txt`, `C1-v3-measure.txt` |
| r62 plan (§C1 frozen predicate, expected result, successor, S118) | `plans/round-62.md` lines 17–98, 170–182 |
| r62 w1 data seats | `.ufo/waves/round-62/w1/` reports listed above |
| Existing criteria | `corpus/QUALITY.md` Q31 (reviewer judgment), Q56 (byte-exact reservation) |
| SOURCES rows | `corpus/SOURCES.md` S043/S103 (memory.md chain), S112–S115 (canonical keys), S110 (byte-identity precedent) |

## 2. Verdict table: fact → prior home → new here? → keep/cut

"New here?" = not already held by the r61 entry + plan + seat reports (i.e. genuinely novel for the corpus). KEEP = the fact may appear in the new entry (it is either measured-new or a required binding sentence); CUT = it is a restatement that must not be re-written as if new — cite the prior home instead (one authoritative home per fact).

| # | Fact (entry sentence class) | Prior home | New here? | Keep/Cut |
|---|---|---|---|---|
| 1 | The five erratum classes E2/E2b/E2c/E2e/E2f and the arm each forced (A3 url_key, A3(b) rendering alias, A4(iv) full-sha alias, A1 guarded form, A2 guarded action) | r61 plan E2–E2f addenda; r61 entry lines 13–47; r61 seat reports (MutA3/MutFixtures/MutA4/MutA1/MutA2) | no — restatement | CUT → cite `scoped-rules-counter-round61.md` |
| 2 | Canonical per-client key set (Claude `paths`, VS Code/Copilot `applyTo`, Cursor `globs`) | r61 plan E2d addendum; r61 entry lines 15–22; SOURCES S112–S115; verified again by `ExecInstancesA1.md` | no — restatement | CUT → cite S112–S115 |
| 3 | A1's guarded form: one key per cell, exact-case, path-like value on cited line or block, no commented/negated/equals/example keys | r61 plan E2e; MutA1 §5; r61 entry lines 15–22 | no — restatement | CUT → cite MutA1/r61 entry |
| 4 | A2's guarded claim form: G5 (key on cited line + half-overlap) ∧ G7 (raw-tokenizer event-claim conjunct), G9 for compound-purpose; F6 compound-purpose declared bound | r61 plan E2f; MutA2; r61 entry lines 23–27 | no — restatement | CUT → cite MutA2/r61 entry |
| 5 | A3 `url_key` identity (host lowercased, scheme/default-port/www normalized, one trailing `.md` dropped); E1 sub-rules kept; 11 canonical-equivalence spellings admitted | r61 plan E2; MutA3; r61 entry lines 28–35 | no — restatement | CUT → cite MutA3/r61 entry |
| 6 | A3(b): fresh-row rendering alias (locale segment / `@version`/`enterprise` suffix) rejects | r61 plan E2b; MutFixtures S1; r61 entry lines 32–34 | no — restatement | CUT → cite MutFixtures/r61 entry |
| 7 | A4(iv) full-64-hex alias conjunct + the seven binding conditions (BASE scan, header-only base, anchored `supersedes`, measured-table scan, named-row full-sha binding, 11-cell fetch-claim scan, prefix-never-alias) | r61 plan E2c + binding conditions 1–7; MutA4; r61 entry lines 36–47; re-frozen in `ExecInstancesA4.md` | no — restatement | CUT → cite MutA4/r61 entry |
| 8 | A4(iii) is consistency-only, not acquisition authentication | r61 plan E2c; r61 entry lines 39–40; MutA4 §5.1; CriticA4Limit | no — restatement | CUT → cite r61 entry |
| 9 | The counter does not prove row truth / same-mechanism applicability; reviewers re-read cells (Q31) | r61 entry "Entry bound" + "Not held" (lines 65–71, 79–85); MutFixtureEscape W8; QUALITY Q31 | no — restatement | CUT → cite r61 entry + Q31 |
| 10 | Counter sha pin `5a5adc94…` (r61 freeze), fails-closed sha check in the instrument | r61 entry verified-at; r62 plan §C1; `ScoutPriorReceipts.md` | no — restatement | CUT → cite r61 entry verified-at |
| 11 | Before-state: no committed receipt measures any erratum against the landed v3 arms (0 of 5) | r62 plan motivating evidence (grep 0 of 5); measured by `ScoutPriorReceipts.md` (0 of 5, exact counts) | plan-predicted; measurement now landed | KEEP as the before-sentence (cite `ScoutPriorReceipts.md`) |
| 12 | The instrument runs two fresh attack instances per class through the committed counter's own arm-level functions and scores reject | r62 plan §C1 (instrument definition) | no — plan text | CUT → cite plan (or instrument source once landed) |
| 13 | Absorption definition: absorbed iff both instances reject AND stub-replacing that guard admits both; an unabsorbed class's survivors printed | r62 plan §C1 | no — plan text | CUT → cite plan |
| 14 | The ten fresh instance literals (2/class) with their exact ids, append lines, expected reasons, and the four benign controls | r61 attack tables are the class ground (MutA1 15 mutants, MutA2 10 cells, MutA3 19 rows, MutA4 12+3, MutFixtures S1); the concrete r62 instance IDs/bytes are drafted in `ExecInstancesA1/A3/A4` (and A2 pending) | **yes — new artifacts (new inputs, not previously existing anywhere)** | KEEP (new data) |
| 15 | Measured verdicts per class: e.g. E2e `bold-only-value` REJECT, E2e `negated-within-60` **ACCEPT** (survives); E2c F-A4-7 REJECT, F-A4-11 condition-(5) and condition-(6) **ACCEPT** (survive) | not in any r61 artifact; r62 plan expected "other four errata absorbed" — the measured survivors contradict the plan's expectation | **yes — new measurements (and they revise the plan's expectation)** | KEEP — must be reported exactly as measured, NOT as "absorbed" |
| 16 | E2f G7/G9 gap: landed counter implements forward/reverse support fractions but no raw-tokenizer event-claim conjunct / no compound-purpose conjunct | r62 plan §C1 "Expected result, declared before data"; MutA2's four implementation pins (F2a raw-tokenizer blindness, `apply` exclusion) | prediction/design in plan; **measurement confirmation = new** | KEEP with explicit "predicted in plan, confirmed by matrix" wording |
| 17 | E2f survivor instance(s) printed by the matrix | r61 W6 word-support line is a different, synthetic world; no committed E2f instance exists | **yes — new measurement** | KEEP |
| 18 | Successor counter `verifiers/check_scoped_rules_v31.py` (copy carrying G5+G7, G9/F6 still declared surviving) and its self-test line `E2f fresh instances reject 2 of 2` with unchanged `worlds reject 7 of 7; eligible rows pass 4 of 4` | r62 plan §C1 successor paragraph (planned; no file exists yet); fix-shape restates MutA2's recommendation | **yes — new artifact + measurement (when run)** | KEEP (new) |
| 19 | S118 row: `https://code.claude.com/docs/en/memory.md` opened this round with committed snapshot; its `paths` frontmatter text grounds E2e instances | The FACT "`paths` takes glob patterns, listed or inline; memory.md:198/199" is already held by r61 entry lines 19–20 + SOURCES S103 (S103 **is** memory.md, re-opening S043, same URL). S118 is a fresh fetch of the same URL | fact: no (restatement); fresh bytes/sha/line numbers: **yes (narrowly)** | KEEP only the fresh-byte evidence (sha, lines, drift); the proposition itself must cite S103/S112, not be presented as new |
| 20 | Matrix result line `errata measured 5 of 5; absorbed 4 of 5; surviving N; controls 2 of 2` (frozen sentence) and the computed counts | r62 plan §C1 frozen predicate (the sentence itself is plan text; the numbers are data) | counts: **yes — new measurement** | KEEP — print the computed values, never hard-code; note the plan's internal `surviving 2` (frozen line) vs `surviving 1` (expected-result paragraph) inconsistency — the entry must print what the instrument computes |
| 21 | Controls 2 of 2 (one pair must reject/score absorbed; one pair must accept/score surviving) and isolation arm | r62 plan §C1 kill rule + `ExecGateArms.md` | measurement: **yes** | KEEP (new measurement) |
| 22 | Limits list: instrument does not measure world-level semantics, reviewer judgment (Q31), or the counter sha pin | r61 entry "Not held"; QUALITY Q31; r62 plan | no — restatement | CUT → cite r61 entry/Q31 |
| 23 | "The five pre-data amendments were each forced by a measured attack" (r61 report line) | fleet `.ufo/reports/round-61/kotoba.md`; refined by `ScoutPriorReceipts.md` (draft-text attacks, 0 of 5 landed receipts) | no — restatement (and must be phrased as *draft-text* attacks) | CUT → cite `ScoutPriorReceipts.md` |

## 3. Minimum set of genuinely new facts (everything else cites prior homes)

1. The matrix measurement (when committed): `errata measured 5 of 5; absorbed 4 of 5; surviving N; controls 2 of 2` with the per-class instance verdicts — the first committed arm-level score of the landed v3 counter (sha `5a5adc94…`).
2. The ten fresh instances (2/class) + four benign controls — new test artifacts.
3. The guard-mutation (stub-replacement, both directions, isolation) evidence per class — new measurement.
4. The measured survivors among the plan's "expected absorbed" classes: E2e `negated-within-60` ACCEPT; E2c F-A4-11 (condition 5) and condition-6 ACCEPT (verified in `ExecInstancesA1.md` / `ExecInstancesA4.md`) — these revise the plan's expectation and must appear as survivors.
5. E2f's unabsorbed verdict and its survivor instance(s) — confirmed measurement of the plan's declared prediction.
6. The successor `check_scoped_rules_v31.py` + its self-test output lines — new artifact + measurement.
7. S118: fresh snapshot sha + exact cited lines (the `paths`-takes-globs proposition itself is restatement of S103/S112).

## 4. Overclaim / unearned-claim flags (the class's core mandate)

- **F1 (must not).** Do not write "E2e absorbed" or "E2c absorbed" as if both instances rejected: `ExecInstancesA1.md` measured the negated-key E2e instance ACCEPT, and `ExecInstancesA4.md` measured F-A4-11 (condition 5) and condition (6) ACCEPT against the landed primitive. Any entry sentence claiming absorption for these classes without the matrix data is unearned.
- **F2 (must not).** Do not print the matrix numbers before the control receipts (absorption-hollow, absorption-before, frozen-repairs-dishonest) and the data run are committed (M90 order). Plan §C1: controls commit before matrix data; the entry's `verified-at` must postdate the data commit. An unrun check has not passed.
- **F3 (must not).** Do not claim S118 was "opened this round" nor cite its lines before `SrcRulesFrontmatter.md`'s fetched bytes and the S118 row/snapshot are committed — `ScribeSourcesS118.md` correctly refused to draft the row for exactly this reason. Also: S118's URL is already held by S043/S103; the row needs an explicit re-open (or byte-identity) disposition, and if the fetched bytes are byte-identical to S103's snapshot, A4(iv) applies to the S118 row itself (full-sha alias against S043/S103) unless it declares lineage honestly — the entry must not assert S118 as a fresh, unencumbered source.
- **F4 (flag).** The plan's frozen predicate prints `surviving 2` while its expected-result paragraph says `surviving 1`; the entry must print the instrument's computed count and should not silently reproduce either number as a fact.
- **F5 (flag).** Any "first-ever measurement / first time the five amendments are verified" phrasing must be scoped: it is the first *arm-level committed receipt*; the world-level and fetch measurements (C1-worlds, C1-v3-measure) already exist and are not superseded by the matrix.
- **F6 (must not).** Do not describe the successor as "closing E2f" without the G9/F6-bound qualification: G9 remains a declared surviving bound; the successor only adds G5+G7.

## 5. Residual risk and verification gaps

- The actual entry text was not reviewable (draft absent at review time). The table above is grounded in the mandated content (r62 plan §C1 + ScribeEntry62 prompt + landed w1 data); when ScribeEntry62's draft lands, re-run this table mechanically — it is formulated as sentence-class checks.
- `ExecInstancesA2.md` (E2f instances) was not yet landed at review time; the E2f instance literals are thus not cited in detail here, but their class home (MutA2) and the plan's prediction are stable.
- `ExecAbsorbInstrument`'s run output (final numbers, controls receipts) is future data; rows 15/16/17/20/21 are marked new-as-measurement and will only become corpus facts once committed (F2).

## 6. End matter

- Installs: no installs (no tool installed or upgraded; pacman untouched).
- Blockers: none. (The absent ScribeEntry62 draft is a timing artifact, not a blocker: the verdict table is complete against the frozen content.)
- Produced: the SentNovelty re-cover for the round-62 C1 entry — verdict table (23 rows), the minimum genuinely-new set (7 items), and six overclaim flags, written to `.ufo/waves/round-62/w1/RevSentNovelty.md`.
