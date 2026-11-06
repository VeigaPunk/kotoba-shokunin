# ScoutSourcesR97 — re-open of C2's source, and two candidate judgments (round 97, wave 1)

Seat: `ScoutSourcesR97`. Date of access: **2026-11-06** (fetch window 01:08:15–01:08:22 -03:00).
Lane: `kotoba-shokunin`. Scope: re-open the source claim C2 rests on (S273, Bazel Test
Encyclopedia) and judge candidates that could ground C1 or C2.

Bounds honoured: no HTML page is stored under `.ufo/waves/round-97/w1/` — only digests, line
numbers and short excerpts (round-96 routed defect 6; QUALITY Q11). The four fetched pages
(749 617 B total) live only in `/fast/scratch/hyaku/kotoba-r97/ScoutSourcesR97/`, removed at exit.
No repo writes: this file is the only artifact. No subagent dispatch (leaf member).

## 1. Re-open — Bazel Test Encyclopedia (the plan's S273)

- URL: `https://bazel.build/reference/test-encyclopedia`
- cmd: `curl -sS -L -o bazel-test.html -w 'http %{http_code} bytes %{size_download}\n' https://bazel.build/reference/test-encyclopedia`
  then `sha256sum bazel-test.html`
- observed: `http 200 bytes 223640`
  `6b07e08f0f4bae537544eac1afc64d98f0b19a9ae7408b8e6482f56e134d5346  bazel-test.html`
- **Equals the L1's receipt** (`.ufo/waves/round-97/receipts/sources-opened.txt:3-4`: `url …`, then
  `http 200 bytes 223640 sha256 6b07e08f…5346`): **yes, byte-identical** — same size, same digest. The page did not move
  between the L1's open and mine, so the L1's HTML line numbers are valid in my bytes and no
  re-location is needed.
- heading: HTML line **656**, `<h2 class="…" id="test-interaction-filesystem" …>` (§ Test interaction
  with the filesystem).
- quote, HTML lines **659–661**:
  "Tests should create files only within the directories specified by $TEST_TMPDIR and
  $TEST_UNDECLARED_OUTPUTS_DIR (if set). These directories will be initially empty."
  - words: **21** —
    `printf '%s\n' "Tests should create files only within the directories specified by \$TEST_TMPDIR and \$TEST_UNDECLARED_OUTPUTS_DIR (if set). These directories will be initially empty." | wc -w`
    → `21` (matches the L1's `words: 21`).
  - shaping (Q56): the quote is the text of two `<span data-as="p">` bodies (lines 659–660 and line
    661) joined, with the `<code>` element tags around `$TEST_TMPDIR` and
    `$TEST_UNDECLARED_OUTPUTS_DIR` removed. It is **quote-equal after documented shaping**, never
    `byte-exact`. The unshaped bytes are the excerpt in `receipts/sources-opened.txt`.
- second locators (verified present in my bytes): line **559** env table `HOME` = `$TEST_TMPDIR`
  (recommended); line **574** `TEST_TMPDIR` = private writable directory (required); line **622**
  "Tests must not assume that any constant path is available for their exclusive use."
- registry: `grep -cF 'bazel.build/reference/test-encyclopedia' corpus/SOURCES.md` → `0`.
  S273 is a new row, not a duplicate of a held URL (Q84).
- **Verdict: re-open confirmed; no correction to the plan's C2 sourcing.** The S273 row as the plan
  states it (kind `docs`, tier A, grounds rule 4 and the disclosed bound) is supported by my bytes.

## 2. Candidate A — GoogleTest "Advanced GoogleTest Topics" § Shuffling the Tests → **ADMIT as S274**

- URL: `https://google.github.io/googletest/advanced.html`
- observed: `http 200 bytes 214623`;
  `7317f5e7d59afb22c2bd9550122f55b38c60d28865d7522664972769b2fd16c5  gtest-advanced.html`
- page: title line 9 `Advanced GoogleTest Topics | GoogleTest`; first `<h1>` line 39; § heading line
  **2110** `<h3 id="shuffling-the-tests">Shuffling the Tests</h3>`.
- quote, HTML lines **2112–2113**:
  "You can specify the --gtest_shuffle flag (or set the GTEST_SHUFFLE environment variable to 1) to
  run the tests in a program in a random order."
  - words: **25** —
    `printf '%s\n' "You can specify the --gtest_shuffle flag (or set the GTEST_SHUFFLE environment variable to 1) to run the tests in a program in a random order." | wc -w`
    → `25`.
  - shaping (Q56): `<code class="language-plaintext highlighter-rouge">` tags removed and the line
    break between 2112 and 2113 joined; **quote-equal after documented shaping**.
  - token spread (Q70): `grep -c 'gtest_shuffle' gtest-advanced.html` → `1` (line 2112 only), so the
    token is body text, not site banner or navigation.
- second locator (the seed half), HTML lines **2117–2118**: "The console output includes the random
  seed value, such that you can reproduce an order-related test failure later." — words **18** —
  `printf '%s\n' "The console output includes the random seed value, such that you can reproduce an order-related test failure later." | wc -w` → `18`.
- registry: `grep -cF 'google.github.io/googletest/advanced.html' corpus/SOURCES.md` → `0`.
- **Verdict: ADMIT** — kind `docs`, tier **A** for the scope "randomizing test order with a printed,
  replayable seed to expose order-dependent state".
  - reason: C2's v5 rule 6 (honest bracket, shuffled order, seed printed and replayable via
    `KOTOBA_R97_SEED`) is the one rule of rules 4–6 with no cited authority: the plan cites S273 for
    rule 4 and discloses the state-outside-per-run bound, while rule 6's mechanism — randomize the
    order, print the seed, replay it to reproduce an order-related failure — is stated by the
    framework's own docs here. Admitting it gives the round lesson a located quote for a rule it
    already implements, which is the Q23 shape (a rule attributed to an authority carries a located
    quote), and it is a **distinct document** from S273 (filesystem isolation), so Q84 holds.
  - flip: if rule 6 is dropped from the counter, or if no C2 arm's verdict turns on run order any
    more, the row degrades to a lead, not a row; and if the section is reworded so the 25-word quote
    no longer resolves at line 2112, the row is re-opened before it is re-cited (`recheck: on-release`).
  - anchor caveat: the page carries **no version marker** — the footer (lines 2601–2606) links only
    the GitHub repository and the licence, and the URL has no `release-` path. The row's `anchor`
    must therefore pin the fetch date + digest (the lane's S260/S253 precedent), e.g.
    "§ Shuffling the Tests (HTML line 2110; quote lines 2112–2113, 25 words; seed locator lines
    2117–2118), fetched 2026-11-06, HTTP 200, 214623 B, sha256 7317f5e7…16c5".

## 3. Candidate B — pytest "How to use temporary directories and files in tests" § The tmp_path fixture → **REJECT**

- URL: `https://docs.pytest.org/en/stable/how-to/tmp_path.html`
- observed: `http 200 bytes 40121`;
  `dbc7d4b7e96ff939428f8bd3b0ce09e20fee4be5912427833fb9170d675c8df2  pytest-tmp.html`
- page: first `<h1>` line 311 (`How to use temporary directories and files in tests`); § heading line
  **313** `<h2>The tmp_path fixture</h2>`.
- quote, HTML lines **314–315**: "a temporary directory unique to each test function." — words **8** —
  `printf '%s\n' "a temporary directory unique to each test function." | wc -w` → `8`.
  Shaping: `<code>` tags around `tmp_path` removed; the sentence continues across the line break.
- registry: `grep -cF 'docs.pytest.org/en/stable/how-to/tmp_path.html' corpus/SOURCES.md` → `0`.
- **Verdict: REJECT** (scope overlap with S273, not a defect in the page).
  - reason (observed, Q62): S273 already grounds the counter's rule 4 with the stronger sentence for
    that rule — "These directories will be initially empty" (Bazel HTML line 661) — and rule 4's unit
    is a **run**: "Every run gets a fresh clone of REV, a fresh TMPDIR, HOME and XDG_CACHE_HOME"
    (`verifiers/fixtures/round-97/selftest-kills.py` header, rule 4). pytest's distinct property on
    this page is a directory "unique to each test function" (lines 314–315) — a per-test unit the
    counter does not have. A row would teach a unit the instrument does not implement, and SOURCES
    rule 4 says a short registry of honestly tiered rows beats a long one.
  - flip: if a counter's isolation unit becomes per-test or per-assertion inside one run (a self-test
    that must give each assertion its own temp dir), admit with the quote at HTML lines 314–315 and
    `teaches` "a temporary directory unique to each test function".

## 4. Candidate C — Python docs `pathlib.Path.is_dir` (with `is_file` / `exists`) → **REJECT (deferred to a lead)**

- URL: `https://docs.python.org/3/library/pathlib.html`
- observed: `http 200 bytes 271233`;
  `b55e4f2852c8fc1a2ef215fb1383fd184a73dc0003a211e9b0c94008fcc2dc14  pathlib.html`
- definitions: `#pathlib.Path.exists` line 1326, `#pathlib.Path.is_file` line 1351,
  `#pathlib.Path.is_dir` line 1365; first `<h1>` line 242.
- quote, HTML lines **1367–1369**: "False will be returned if the path is invalid, inaccessible or
  missing, or if it points to something other than a directory." — words **22** —
  `printf '%s\n' "False will be returned if the path is invalid, inaccessible or missing, or if it points to something other than a directory." | wc -w` → `22`.
  Shaping: `<code>` tags around `True` / `False` removed; the sentence is unbroken across lines
  1367–1369.
- what it would ground: t06 — `if (fleet / ("%s-shokunin" % lane)).is_dir():`
  (`verifiers/verify_dispatch_prompts.py:217`), a plain FILE named `<lane>-shokunin` must not count as
  a lane repository — and t02/t10 — `base.is_file()` (line 234), `legacy.is_file()` (line 246), an
  absent or unreadable baseline is never a bound.
- registry: `grep -cF 'docs.python.org/3/library/pathlib.html' corpus/SOURCES.md` → `0`; the registry
  already holds six `docs.python.org` rows (S007, S253, S263, S265, S266, S270 —
  `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|[^|]*https://docs\.python\.org' corpus/SOURCES.md`
  → `6`).
- **Verdict: REJECT for S274; keep as a lead.**
  - reason: the row would teach a language primitive, and the lane's t06/t02/t10 kills are observed
    by the self-test's own behavioural arms (the frozen counter requires a REPORTED failure in both
    the blind and the mirror run), so no claim's verdict turns on an authority for `is_dir()`; the six
    held Python-doc rows are already the lane's runtime-primitive shelf. A seventh row for a primitive
    the self-test itself observes adds no curation (SOURCES rule 4).
  - flip: if a claim's verdict turns on a pathlib semantic the lane must **attribute as a rule** (a
    gate that approximates "a directory, not a file, is a repository" and must name the parsed rule
    per Q23), admit with the quote at HTML lines 1367–1369 and `teaches` "is_dir is False for a plain
    file, a missing path or an inaccessible path — the distinction a lane-repository test needs".

## 5. Registry check (all four URLs, one command each, run from the lane root)

| URL | rows today | command |
|---|---|---|
| `bazel.build/reference/test-encyclopedia` | 0 | `grep -cF 'bazel.build/reference/test-encyclopedia' corpus/SOURCES.md` |
| `google.github.io/googletest/advanced.html` | 0 | `grep -cF 'google.github.io/googletest/advanced.html' corpus/SOURCES.md` |
| `docs.pytest.org/en/stable/how-to/tmp_path.html` | 0 | `grep -cF 'docs.pytest.org/en/stable/how-to/tmp_path.html' corpus/SOURCES.md` |
| `docs.python.org/3/library/pathlib.html` | 0 | `grep -cF 'docs.python.org/3/library/pathlib.html' corpus/SOURCES.md` |

Registry size at this read: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
→ `198` rows (2026-11-06). `grep -nF '<url>' corpus/SOURCES.md` prints nothing and exits 1 for each
of the four URLs (run for all four, 2026-11-06). No held row names any of the four URLs, so no
candidate is a duplicate and Q84's "second row on a held URL" question does not arise.

## 6. Handoff to ScribeCorpusR97

- **S273** — unchanged from the plan's line; my re-open is byte-identical (digest above) and the
  quote is 21 words at HTML lines 659–661 under heading line 656.
- **S274** — one row admitted: GoogleTest, `Advanced GoogleTest Topics` § Shuffling the Tests, cells
  as in § 2 above (`docs` / A / scope "randomizing test order with a printed, replayable seed to
  expose order-dependent state" / anchor with fetch date + sha256 / `recheck: on-release` /
  `used-by` the round-97 lesson § Gate). This is the only admission from this seat; pytest and
  pathlib are rejected with their flip conditions recorded above.

## 7. Findings and risks

- **F1 (re-open clean).** The Bazel page is byte-identical to the L1's open — same 223640 B and same
  sha256 — so the L1's HTML line numbers hold in my bytes and the plan's C2 sourcing needs no
  correction. This is the one dynamic-page risk the item named, and it did not materialise.
- **F2 (anchor without a version).** The GoogleTest page is unversioned: no `release-` path, and the
  footer (lines 2601–2606) links only the repository and the licence. The S274 anchor must pin the
  fetch date + sha256, and the quote must be described as quote-equal after documented shaping
  (Q56), never byte-exact.
- **F3 (token is body text).** `--gtest_shuffle` occurs exactly once on the page (line 2112), so the
  quote is not site furniture (Q70).
- **F4 (evidence size).** No HTML saved under the wave dir; the four pages (749 617 B) stayed in
  scratch and are deleted at exit (Q11; round-96 routed defect 6).
- **F5 (rejections are taste, not defects).** The pytest and pathlib pages are sound, A-tier sources;
  their rejection is scope and curation, and each carries the flip condition that would admit it.
- Remaining unknowns: whether the scribe lands S274 (out of this seat's hands — the plan's C2 does
  not depend on it), and whether the GoogleTest section is reworded at the next release
  (`recheck: on-release`).
