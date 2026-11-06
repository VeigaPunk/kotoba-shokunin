# Round 97 — kotoba (Linux host, omp): lesson

Authors: **ScribeCorpusR97** (curation draft), **KotobaR97** (integration and settlement).
Seat reviews are lane evidence, not the independent non-author admission judgment.

Round: 97, plan `plans/round-97.md` (frozen at `148395bf42af97436b1b832a97a175515f981939`), base
`fa1bebae33e6b0ab4e36b9ba73ff7d4c5d610520`, instrument commit
`94a1021762a888d8a360ba6efa759372cef392fb` (the v5 counter `verifiers/fixtures/round-97/selftest-kills.py`
and the C2 runner `verifiers/fixtures/round-97/forgery-controls.py`).
Pre-data receipts (frozen with the plan, before any scored reading):
`.ufo/waves/round-97/receipts/redbefore-c1-base.txt` (`C1-PREDICATE-UNMET`, `C1 targets killed 0 of
13`), `redbefore-c1-base-rulesv4.txt`, `poscontrol-r96c1-base.txt` and `poscontrol-r95c1-base.txt`
(MET), `c2-before-v4.txt` and `c2-v5-as-v4.txt` (`forgeries refused 0 of 3`), `c2-v5.txt`
(`forgeries refused 3 of 3; honest held 2 of 2`), `base-box-proof.txt`, `census-before.txt` and
`sources-opened.txt` (S273).

## Gate

Candidates considered, with the decision and the reason.

- **S273** — Bazel, "Test encyclopedia" (`https://bazel.build/reference/test-encyclopedia`).
  **Admitted** as tier A, kind `docs`, status `mined`, opened 2026-11-06, recheck `180d`, used-by
  `corpus/lessons/round-97.md,plans/round-97.md`.
  - Access record (rule 1): access date 2026-11-06; HTTP 200; 223640 B; sha256
    `6b07e08f0f4bae537544eac1afc64d98f0b19a9ae7408b8e6482f56e134d5346`. Fetched independently by
    this seat (`curl -sS -L -o bazel-test.html -w '%{http_code} %{size_download}'` then `sha256sum`)
    and recorded by the L1 in `receipts/sources-opened.txt`; both readings agree byte for byte.
  - Located quote (≤25 words): "Tests should create files only within the directories specified by
    $TEST_TMPDIR and $TEST_UNDECLARED_OUTPUTS_DIR (if set). These directories will be initially
    empty." — **21 words** (`printf '%s\n' "<quote>" | wc -w` → 21), at **HTML lines 659-661** of the
    fetched bytes: line 659 ends `…directories specified by`, line 660 carries the two rendered code
    spans and `(if set).`, line 661 is `These directories will be initially empty.` — quote-equal
    after joining the two `<span data-as="p">` bodies (the first spans HTML lines 659-660), with
    the code tags removed (documented shaping; not byte-exact). The section heading is at
    **HTML line 656** (`<h2 … id="test-interaction-filesystem" …>Test interaction with the
    filesystem</h2>`), so the anchor is re-locatable, not a bare homepage.
  - Secondary locators: **HTML line 559** (the environment table's `HOME` row: value of
    `$TEST_TMPDIR`; can be overridden via `--test_env=HOME=…` or unset), **HTML line 574**
    (`TEST_TMPDIR`: absolute path to a private writable directory; required), and **HTML lines
    622-623** ("Tests must not assume that any constant path is available for their exclusive
    use.") — the page's own bound on the claim.
  - **What this row adds** to the registry: the registry holds no `bazel.build` row
    (`grep -c 'bazel.build' corpus/SOURCES.md` → 0 before this round), so this is a new document and
    no new `W04`.
  - Scope: the isolation contract a test runner gives each test — a private, initially empty
    temporary directory and HOME. It grounds v5 rule 4 (every counter run gets a fresh clone,
    `TMPDIR`, `HOME`, `XDG_CACHE_HOME`) and the disclosed bound (state outside the per-run
    directories survives isolation, and the page itself says no constant path is exclusive). It is
    not a statement about this lane's counter mechanics and not a kill rule.
- **S274** — GoogleTest, "Advanced GoogleTest Topics" § Shuffling the Tests
  (`https://google.github.io/googletest/advanced.html`). **Admitted** as tier A, kind `docs`, status
  `mined`, opened 2026-11-06, recheck `on-release` (the page carries no version marker, so a release
  that rewords the section re-opens the anchor), used-by `corpus/lessons/round-97.md`.
  - Access record (rule 1): access date 2026-11-06; HTTP 200; 214623 B; sha256
    `7317f5e7d59afb22c2bd9550122f55b38c60d28865d7522664972769b2fd16c5`. Fetched independently by
    this seat (`curl -sS -L -o gtest-advanced.html -w '%{http_code} %{size_download}'` then
    `sha256sum`) and screened by the scout (§ 2 of `w1/ScoutSourcesR97.md`); both readings agree byte
    for byte.
  - Located quote (≤25 words): "You can specify the --gtest_shuffle flag (or set the GTEST_SHUFFLE
    environment variable to 1) to run the tests in a program in a random order." — **25 words**
    (`printf '%s\n' "<quote>" | wc -w` → 25), at **HTML lines 2112-2113**: line 2112 carries the
    `--gtest_shuffle` and `GTEST_SHUFFLE` code spans and ends `…set the`, line 2113 continues
    `environment variable to 1) to run the tests in a program in a random order.` — quote-equal after
    joining the two lines and taking the rendered code-span text (documented shaping). The section
    heading is at **HTML line 2110** (`<h3 id="shuffling-the-tests">Shuffling the Tests</h3>`), and
    `--gtest_shuffle` occurs exactly once in the fetched bytes (`grep -c` → 1), so the quote is body
    text, not site furniture.
  - Seed locator: **HTML lines 2117-2119** — "The console output includes the random seed value,
    such that you can reproduce an order-related test failure later." (**18 words**) — the second
    half of the mechanism: the order is replayable, not merely random.
  - **What this row adds**: the registry holds no `google.github.io` row at all
    (`grep -cF 'google.github.io/googletest/advanced.html' corpus/SOURCES.md` → 0 before this
    round), so this is a new document and no new `W04`. It is a different document from S273
    (filesystem isolation), so the two rows do not overlap.
  - Scope: randomizing test order with a printed, replayable seed to expose order-dependent state.
    It grounds **v5 rule 6** (the honest bracket: three honest runs, first, last and a random
    interior position, every other run in a random order, the seed printed and `KOTOBA_R97_SEED`
    replaying an order — `verifiers/fixtures/round-97/selftest-kills.py` header rule 6, lines 31-33,
    and the seed at lines 341-345). Of rules 4-6 it is the one the plan left without a cited
    authority: rule 4 is S273's, rule 5 (the mirror run) is a lane construction with no external
    authority claimed, and the state-outside-per-run bound is disclosed. It is not a kill rule.
- **S275 — REJECTED this round — pytest, "How to use temporary directories and files in tests" § The
  `tmp_path` fixture** (`https://docs.pytest.org/en/stable/how-to/tmp_path.html`).
  Opened by scout/scribe and re-opened by L1 on 2026-11-06; HTTP 200; 40121 B;
  sha256 `dbc7d4b7e96ff939428f8bd3b0ce09e20fee4be5912427833fb9170d675c8df2`.
  Located quote, HTML lines 314-315 under § The tmp_path fixture: "a temporary directory unique to
  each test function." — 8 words (`printf '%s\n' "<quote>" | wc -w` → 8).
  Rejected as redundant corroboration for the chosen S273 authority, not as an unsound source.
  A counter run is itself a test, so the different fixture granularity does not invalidate this
  source. Flip: a per-test-function isolation claim specifically needs pytest's fixture contract.
- **S276 — REJECTED this round — Python docs `pathlib.Path.is_dir`**
  (`https://docs.python.org/3/library/pathlib.html`). Opened by scout/scribe and re-opened by L1 on
  2026-11-06; HTTP 200; 271233 B; sha256
  `b55e4f2852c8fc1a2ef215fb1383fd184a73dc0003a211e9b0c94008fcc2dc14`.
  Located quote, HTML lines 1367-1369 under § pathlib.Path.is_dir: "False will be returned if the
  path is invalid, inaccessible or missing, or if it points to something other than a directory."
  — 22 words (`printf '%s\n' "<quote>" | wc -w` → 22).
  Deferred as an additional primitive-authority row while C1 observes t06 directly. This is a
  curation choice, not a rejection of the documented semantics. Flip: a sourced pathlib-semantic
  rule becomes the claim. Both rejections remain registry rows under CORPUS v1.

**Census.** The scribe's candidate contains 200 rows (198 + S273/S274), validates exit 0 with
34 W04 warnings (`.ufo/waves/round-97/w1/ScribeCorpusR97/census-after.txt`).
The integrated registry adds rejected S275/S276 too: 198 → 202 rows, counted with
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`.
The end census receipt is under `.ufo/waves/round-97/receipts/landing/census.txt`.

## Corrections

Named, append-only correction entries. A frozen receipt is never edited; a correction is a new entry
that points at it.

- **C97-1 — the S272 word count in the round-96 receipt (round-96 closure routed defect 1).**
  `.ufo/waves/round-96/receipts/sources-opened.txt` **line 12** records the S272 quote as
  `lines 790-791 (located quote, 19 words): "The parameter name or symbol can be enclosed in braces,
  which are optional except for positional parameters with more than one digit"`. The same quote
  string measures **22** words (`printf '%s\n' "<quote>" | wc -w` → 22). The receipt stays frozen as
  written; `corpus/lessons/round-96.md` § Gate already discloses the drift and keeps the true count
  at 22, and registry row S272 carries `(22 words)`. This entry is the named correction the round-96
  closure asked for: it changes no admission (22 ≤ 25 words) and no registry row.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `shared-state-between-scored-runs`: a kill counter that runs every mutant in one clone with one `TMPDIR`/`HOME`, honest run first, cannot tell a run's order from its behaviour — a stateful fake writes a marker on its first run and prints a fake reported failure on every later run, reading MET with no behavioural arm | `plans/round-96-addendum-1.md` § A3 (g7 stateful fake and g8 clone marker read MET with no arm; g3 recompile-compare reads MET source-blind) and `.ufo/waves/round-96/w1/ExecCounterForgeryR96.md` F1 (the counter shares run state and runs the honest self-test first) | none — no committed stateful control world existed, so no registry criterion or protocol rule could have caught it; the round-96 control worlds were scratch patches under `.ufo/waves/round-96/w1/ExecCounterForgeryR96/` | **v5 rules 4-6** in `verifiers/fixtures/round-97/selftest-kills.py`: a fresh clone, `TMPDIR`, `HOME` and `XDG_CACHE_HOME` per run (rule 4), a mirror run with the mutant bytes on disk (rule 5) and a three-run honest bracket (rule 6); shown able to fail by `.ufo/waves/round-97/receipts/c2-v5-as-v4.txt`, where the same file with the rules switched off (`--rules v4`) reads `forgeries refused 0 of 3` |

## Status changes

- **None.** The registry is append-only and this seat's ownership of `corpus/SOURCES.md` is
  append-rows-only: **S273 and S274 are new rows** (`mined` at opening, 2026-11-06, tier A, kind
  `docs`, recheck `180d` and `on-release`, used-by `corpus/lessons/round-97.md,plans/round-97.md` and
  `corpus/lessons/round-97.md`), and **no existing row's `status`, `recheck` or `used-by` cell was
  changed** — so there is no old→new pair to log here.
- S275 and S276 are new `rejected` rows, opened 2026-11-06; no existing cell changes.
- **S271 and S272 — deliberately not edited.** Both hold the round-96 sources; this round's lesson
  cites neither for a claim, so neither `used-by` cell gains this lesson and neither `recheck`
  changes. The L1 may add `corpus/lessons/round-97.md` at settlement if the round cites them (the
  old → new pair would be logged there); this seat did not make it.

## Considerthese

`considerthese/2026-10-26.md` was re-read (proposals only; nothing implemented).

- **Assimilation: none.** No proposal is newly implemented; this round addresses the already-planned
  dispatch-checker survivors and counter forgeries. Proposal 1 remains a concrete next-round
  candidate, not silently implemented as adjacent work.
- **Proposal 1** (a byte ceiling and a 200-character max-line check in the floors guard) stays
  carried and is **still unimplemented**: measured at this round's freeze, `SKILL.md` is 600 lines /
  92672 B with **165** lines over 120 characters, **94** over 300, and the longest line **1491**
  characters at line 518 — the ratchet Q78 asks for, but the instrument that would hold it is not
  this round's claim.
- **Proposal 2** (move `## Gate registry` out of `SKILL.md`) stays an **L0 question** rather than a
  claim (`corpus/QUALITY.md` Q67: a move that takes a protocol-named home elsewhere is an L0
  question). The skill file remains byte-identical to the round base; no comparative registry-size
  growth is claimed this round.
- **Proposal 3** (land the page round 74 rejected and use it on the skill's own description) stays
  carried and is **still unimplemented**: the round-74 rejection was a W04 duplicate (the URL is
  held twice, at S210 and S213), and the skill's own description is unchanged at **1021**
  characters with a **151**-character first sentence. `SKILL.md` is at the 600-line box (600 of
  600), so a rewrite of the frontmatter description has to be paid for by lines saved elsewhere —
  and this wave's context gives the 600-line skill budget to no seat, so the claim-adjacent edit is
  not available.
- **Proposals 4 and 5** are carried unchanged from the previous rounds; proposal 5 is already mined
  as criterion Q82 and is not re-mined here.

## Settlement

L1 settlement (KotobaR97, after the landing reading; the verdicts are the non-author closure's).

Landing `693be9c321c26078a2adbf32c220dfcd371cbe35`; receipts `.ufo/waves/round-97/receipts/landing/`
(runner `.ufo/waves/round-97/landing-run.sh`, unseeded, uid 1000).

- **C1** `selftest-kills.py c1 693be9c3` → `C1 targets killed 13 of 13 (run errors 0); positive killed 1
  of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13` `C1-PREDICATE-MET` rc 0
  (`c1-v5.txt`); same tally under `--rules v4` (`c1-rulesv4.txt`). Before (base `fa1bebae`): `killed 0
  of 13`, UNMET rc 1. Self-test 78 → 105 assertions. Kill-rule conjuncts: `r96c1`/`r95c1` MET, box
  proof `boxes proven 2`, production code outside `self_test()` byte-identical (`prod-identity.txt`:
  one insertion hunk `1102a1103,1333`).
- **C2** `forgery-controls.py v5 693be9c3` → `C2 v5: forgeries refused 3 of 3; honest held 2 of 2;
  bound g2b MET` `C2-PREDICATE-MET` rc 0 (`c2-v5.txt`). Before: v4 refused 0 of 3 (`c2-before-v4.txt`);
  cause control v5-as-v4 refused 0 of 3. Counter and runner bytes equal to the instrument commit.
- **Disclosed after data** (`plans/round-97-addendum-1.md`): g10 committed-reference forgery and g11
  seeded-replay forgery read MET under v5 (A1, A2) — named bounds, not rescues; counter-rule mutants
  V4–V9 survive C2's committed worlds (A3); 11 new dispatch-checker survivors (A4). Q87 names the
  committed-reference bound.
- **Census** round start rc 0, 198 rows, 34 `W04`; round end rc 0, 202 rows, 34 `W04` (`census.txt`).
