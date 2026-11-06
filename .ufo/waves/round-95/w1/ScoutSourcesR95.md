# ScoutSourcesR95 — C1 source re-open + two candidates (round 95, w1)

Seat: ScoutSourcesR95 (scout 1 of r95-w1). Access date for every fetch below: **2026-11-05**.
Saved fetch bytes: `.ufo/waves/round-95/w1/ScoutSourcesR95/` (this seat's receipt dir). No repo
writes outside this report and that dir. No patch, no READY file (not a builder).

## 1. Re-opened frozen sources — byte-identity vs L1's 2026-11-05 record

| # | URL | HTTP | bytes | sha256 | vs L1 record |
|---|---|---|---|---|---|
| 1 | https://docs.python.org/3/library/unittest.html | 200 | 336978 | f9510cd7d7a67a32fb891016cbb42bf1dfcb80a370c689ed222058acbff3506d | **MATCH** (byte-identical) |
| 2 | https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/ | 200 | 27068 | 8641c38959222238f34aba0e20d3c51919cf183bf19a53f436257614cab656da | **MATCH** (byte-identical) |

Fetch command: `curl -sS -L -o <receipt> -w "%{http_code}" <url>`; `stat -c %s`; `sha256sum`.

### 1a. unittest.html — Python docs (grounds counter rule 1, S270)

- Documents **Python 3.15.2**: `<title>unittest — Unit testing framework — Python 3.15.2 documentation</title>` at HTML line 20 (also line 34).
- `TestResult.errors` definition: dt anchor `id="unittest.TestResult.errors"` at **HTML line 2410**; body lines 2412–2414. Located quote (10 words):
  > "Each tuple represents a test which raised an unexpected exception."
  — lines **2413–2414**; shaping: the sentence is folded across the two HTML source lines after
  "an" (line 2413 ends `…raised an`, line 2414 is `unexpected exception.</p>`); quote-equal after
  joining the fold, no bytes dropped (Q42/Q56).
- `TestResult.failures` definition: dt anchor at **HTML line 2418**; body lines 2420–2422. Located quote (15 words):
  > "Each tuple represents a test where a failure was explicitly signalled using the assert* methods."
  — lines **2421–2422**; shaping: folded after "failure" (line 2421 ends `…where a failure`); the
  trailing "assert* methods" is the rendered text of a link (`<span class="std std-ref">assert* methods</span>`,
  line 2422); quote-equal after joining the fold and taking the rendered link text, no bytes dropped.
- Q70 shape: both quotes lie far below the page's first heading, outside any subtitle block.
- **Verdict: ADMIT** — tier **A** (`docs`, official Python docs), scope: what distinguishes an
  *error* (unexpected exception) from a *failure* (explicitly signalled via assert*) in the runner
  whose tally line `<N> failure(s) over <M> assertions` the v3 counter classifies. This is the
  semantic ground of selftest-kills.py rule 1 (REPORTED-FAILURE vs RUN-ERROR). Registry grep:
  **no existing row** on this URL (only docs.python.org rows S007 json, S253 tempfile, S263/S265
  subprocess, S266 exceptions) — clean for ScribeCorpusR95's S270 append.
- **Flip condition:** the documented classes reverse or either sentence moves/vanishes on a future
  fetch (recheck: on-release / at any landing that re-cites S270).

### 1b. Stryker mutant states (S260, corroboration)

- Located quotes: **Killed** — line 12 (16 words, prefix of the line):
  > "When at least one test failed while this mutant was active, the mutant is killed."
  **Runtime error** — line 24 (14 words):
  > "The running of the tests resulted in an error (rather than a failed test)."
  (line 23 is the `<strong>Runtime error</strong>` label; line 26 adds "It is not represented in
  your mutation score.")
- Anchor cross-check vs registry S260 (SOURCES.md line 201): row records Killed at HTML line 12 ✓,
  Survived at line 14 ✓ ("When all tests passed while this mutant was active, the mutant survived."),
  Mutation score at line 51 ✓ (`detected / valid * 100`). **S260's anchor still holds against the
  current bytes; corroboration PASSED.**
- **Verdict: NO NEW ROW** — S260 already holds this URL; the round adds no row on a URL the
  registry already holds (per plan). Re-open outcome: byte-identical, quotes verified in place.
- **Flip condition:** a future fetch whose Runtime-error/Killed wording changes re-opens the S260
  anchor (recheck: on-release).

## 2. Candidate A — pytest exit codes (process-level run-error vs failure) — ADMIT

- URL: **https://docs.pytest.org/en/stable/reference/exit-codes.html** — HTTP 200, 25787 B,
  sha256 `a403306a1d763fc8123749544905dd64e8e0cfa5ed46a416679001c3142e3977` (receipt
  `w1/ScoutSourcesR95/pytest-exit-codes.html`).
- Search log: first guess `https://docs.pytest.org/en/stable/explanation/exit-codes.html` →
  **HTTP 404** (2531 B error body; stats only, body not kept). Real path found from the reference
  toctree (`reference.html` HTML line 232 links `exit-codes.html`); the 1.1 MB `reference.html`
  dump was exploratory and is not kept (Q11).
- Located quotes: "Tests were collected and run but some of the tests failed" (11 words, HTML
  line 318, exit code 1); **"Internal error happened while executing tests, or a plugin raised
  while importing"** (12 words, HTML line 324, exit code 3). The § Exit codes h1 is at line 311;
  the page states "seven different exit codes" (line 312): 0 (315), 1 (318), 2 interrupted (321),
  3 (324), 4 usage (327), 5 no tests (330), 6 max-warnings exceeded (333). Quotes are plain `<dd><p>`
  text, no tags, no shaping.
- **Verdict: ADMIT** — tier **A** (`docs`, official pytest docs), scope: **process-level outcome
  classes only** — that a test runner carries a distinct non-zero exit class for internal/usage
  errors apart from "tests failed". Corroborates the lane's exit ladder (0 pass / 1 content fail /
  2 could-not-evaluate) as standard runner convention. Q20/Q31 scope honesty: this page does NOT
  define the within-run error-vs-failure split (rule 1's ground stays S270+S260); do not cite it
  for that. Registry grep: **no docs.pytest.org row anywhere** — no duplicate (no S270/S271 clash;
  this would be a *new* id).
- **Flip condition:** pytest changes a code's meaning or moves the section; recheck on-release.

## 3. Candidate B — TAP 13 specification (failure line vs bail-out) — ADMIT

- URL: **https://testanything.org/tap-specification.html** — HTTP 200, 22741 B,
  sha256 `d4d82502f11cae2bad4960586cb2a7bbead03bd55eabe1d85c76c86266d9b09a` (receipt
  `w1/ScoutSourcesR95/tap-specification.html`).
- Located quotes: **"As an emergency measure a test script can decide that further tests are
  useless (e.g. missing dependencies) and testing should stop immediately."** (22 words, HTML
  line 175, under the `Bail out!` heading, h3 anchor `id="bail-out"` at line 173); complement:
  "`/^not ok/` indicates a failed test point." (HTML line 97, plain prefix of the line, no shaping).
  Line 175 is plain `<p>` text, no tags, no shaping.
- **Verdict: ADMIT** — tier **A** (`spec`, the TAP specification's canonical home), scope: harness
  output grammar — a per-test failure line (`not ok`) vs a suite-level unrecoverable stop
  (`Bail out!`) as two separate output classes. It is the protocol-side ancestor of the counter's
  REPORTED-FAILURE (`FAIL ` line + summary) vs RUN-ERROR classes. Sweep (Q23): the same split is
  stated tool-side by S260 (Stryker Runtime error) and S262 (PIT Run error), state-side by S270
  (unittest errors/failures); TAP states it protocol-side — consistent, no contradiction found.
  Registry grep: **no testanything/TAP row** — no duplicate.
- **Flip condition:** a spec revision changes bail-out semantics or the section moves; recheck
  on-release.

## 4. Examined and rejected — Ant junit task page

- URL: **https://ant.apache.org/manual/Tasks/junit.html** — HTTP 200, 33365 B,
  sha256 `3f1ee369f541938791d02b8a09506e48ef33472bccb6c237c4280730c7bcc4a1` (receipt kept as
  rejection evidence: `w1/ScoutSourcesR95/ant-junit.html`).
- Observed: the modern Ant manual page defines only halt/property behavior — HTML line 104 (14
  words): "Stop the build process if a test fails (errors are considered failures as well)." —
  which **conflates** errors into failures; the page carries no outcome-class definition of error
  vs failure (grep `unexpected exception` → 0 hits; no `<error>`/`<failure>` XML element
  semantics on the page).
- **Verdict: REJECT** — it does not define error-vs-failure, and its only statement conflates the
  two; admitting it would teach the gate the wrong lesson (Q62 spirit: a refusal grounded in an
  observed fact).
- **Flip condition:** admit if the Ant manual (or its JUnit-XML successor page) again defines
  `<error>` as an unexpected exception vs `<failure>` as an assertion failure.
- Side note: `raw.githubusercontent.com/boxed/mutmut/main/README.md` → HTTP 404 (14 B); mutmut not
  pursued further (two candidates already admitted) — recorded here for the search log (rule 5).

## 5. Registry checks (grep -n in corpus/SOURCES.md, case-insensitive)

- `docs\.python\.org/3/library/unittest` → **no row** (clean for S270; ScribeCorpusR95 owns the append).
- `stryker` → **S260 at SOURCES.md:201** (exists; no new row).
- `docs\.pytest\.org` → **no row**.
- `testanything|tap-specification` → **no row**.
- `ant\.apache\.org` → **no row**.
- Pitfalls already held by the registry: S262/S269 (PIT, same URL row pair from the round-88
  forced duplicate) and S263/S265 (subprocess duplicate) — a reminder that a new row must be a new
  document, not a new fetch of a held URL.

## 6. Recommendation summary (for Scribe/L1; row-writing is not this seat's write)

Admit-worthy evidence rows, in ground order: S270 = §1a (planned this round, grounds rule 1);
next unused ids for §2/§3 if the L1 wants the corroborations held (both tier A, both clean
duplicates-wise). §4 stays a rejection note in the lesson Gate if recorded at all.

## 7. Bounds compliance

One scratch dir `/fast/scratch/hyaku/kotoba-r95/ScoutSourcesR95` created (mkdir -p), TMPDIR +
HYAKU_SCRATCH exported for the session's commands, no `--work` instrument run by this seat, and
the dir is deleted before yield. No git/jj write anywhere; no fleet-root writes; no pacman; no
PIDs left running (curl processes finished; nothing backgrounded). No kernel/host setting touched.
No tool installs were needed (curl/stat/sha256sum/awk/grep were sufficient) — nothing to record
per the operator tooling rule.
