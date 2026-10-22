# ReviewCounters — round 54 build, review of the two frozen counters

Result: MIXED — both counters are faithful to their docstrings and self-tests pass (22/22 each), but the review found 2 high, 4 medium and 7 low defects, each reproduced in a sandbox clone with a reproducing input and an inflate/deflate direction.

Reviewed blobs: `verifiers/check_description_thresholds.py` and `verifiers/check_gate_registry.py` at plan commit `e33715486a45a4a857b64c30e6b695f7995858b8`. The tip `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39` adds only `verifiers/README.md` (+50 lines, `.md`); `git diff e337154..7ad05d3 -- verifiers/check_description_thresholds.py verifiers/check_gate_registry.py` is empty (0 lines), so the counters are frozen as required (Q28). Line anchors below are against that blob.

Method: sandbox clone `/fast/scratch/hyaku/kotoba-r54/ReviewCounters` at `7ad05d34` (counters byte-identical to `e337154`); all reproducer worlds under `exp/` and all git writes (branches `c2exp`, `v5y`/`v5z`) live in that clone only. No lane files touched; no patches made. No tool installs were needed (python3 + git only).

## What holds (exercised, not assumed)

- `--self-test` both counters: `self-test: 0 failure(s) over 22 assertions`, exit 0.
- Baselines: C1 `--rev 422ffd10|e337154|7ad05d34` → `description thresholds backed 0 of 7 clients`, exit 1; C2 → `gate registry rows conformant 0 of 21 lane verifiers; phantom 0` exit 1 at base, `… 0 of 23 …` at plan commit and tip (the two counters count themselves; the plan's `<M>` is parameterized, but the claim line at the measured rev will read **23 of 23**, not 21 of 21 — the L1 should not misquote the before-value's 21).
- Exit codes: 0/1/2 all as declared. Bad `--rev` → `could-not-evaluate: … invalid object name` exit 2 (both). `--self-test --rev`/`--json` combos rejected, exit 2. Missing `--rev`/`--root` → argparse error exit 2.
- Crash paths: non-UTF-8 `SKILL.md` → exit 2 via `--root` (C1) and via a sandbox commit `3c50e16` (C2), both printing `could-not-evaluate: 'utf-8' codec can't decode byte 0xff`. Missing file at a valid rev takes the `None` branch (`read_file`, C1:114) — the round-54 lesson is absent at tip and C1 prints the honest `backed 0 of 7` exit 1.
- Q32 identity core: sibling host rejected (`code.claude.com.evil.io`, self-tested), `..`/`%2e%2e` path segments rejected, host/path pins need the exact host plus a whole path-segment prefix (`github.com/anthropics/claude-code-docs/...` rejected), Gate quote equality is exact-string set membership with a fragment must-fail arm. Whole-token number matching survives the adversarial cases (`536` inside `1,536` blocked, `1,53` vs `1,536` blocked, `2%` vs `12%`/`20%` blocked, decimals bounded).
- C2 conformant world achievable: a full correct registry over M=2 scores `conformant 2 of 2 lane verifiers; phantom 0` exit 0 (sandbox commit `413de52`), so the counter is not structurally unable to pass (Q25 direction).

## Findings

### F1 — HIGH — C1 — deflate — trailing comma glues into the number token
`NUM_RE = \d[\d,]*(?:\.\d+)?%?` (C1:107) consumes a trailing comma: a threshold cell `1,536, then merged into body` tokenizes as `1,536,`, which no verbatim quote can contain (`has_token`, C1:218, then correctly fails to find it). Any prose cell like `8,000, and …` is likewise dead.
Repro: `exp/w_comma` (`--root`), baseline world 4/7 → `description thresholds backed 3 of 7 clients`, Claude Code `no quote holds none of the threshold numbers ['1,536,']`, exit 1. Deflates: a compliant SKILL.md table row loses backing because of a comma. Self-test gap: no comma-suffix arm.

### F2 — HIGH — C1 — inflate — SOURCES id map is last-wins over the whole file
`sources_table` (C1:171) scans every line of `corpus/SOURCES.md` with no heading scoping and `out[c[1]] = …` silently overwrites duplicates; `judge` then reads the last row for an id. A later appendix, census, or fenced example row with the same `S###` but tier `A`/`mined`/`2026-10-22` overrides the real row.
Repro: `exp/w_sources_queued` (S903 `queued`) → `backed 3 of 7`, Cursor correctly down; `exp/w_sources_dup` appends a valid duplicate S903 row under `## Appendix` → `backed 4 of 7 clients` exit 0. Inflates: unsourced content validates a client. SOURCES.md is append-only, so duplicate ids across rounds are a realistic state, and nothing detects them.

### F3 — MEDIUM — C1 and C2 — both directions — fenced code blocks are graded as content
Neither `table_rows` (C1:139) nor `registry_rows` (C2:113) tracks ``` fences, so an inert example table inside a fence is parsed.
- Inflate: `exp/w_fence_only2` — the decision table exists only inside a ```` ```markdown ```` fence, full entry/SOURCES/Gate chain for opencode → `backed 1 of 7 clients`, `opencode BACKED`. Content that renders as documentation scores toward the claim.
- Deflate: `exp/w_fence_before` — fenced example before the real table → `backed 1 of 7` instead of 4; C2 sandbox commit `f07be23` — fenced registry with a ghost row first → `conformant 0 of 2 lane verifiers; phantom 1` exit 1, displacing the real registry. Once any rows are seen, the `done` flag (C1:139ff / C2:113ff) never resets, so nothing later in the section is ever read again.

### F4 — MEDIUM — C1 and C2 — deflate — `\|` (escaped pipe) inside cells splits them
`cells()` (C1:128, C2 same) splits on every `|` with no `\|` unescaping, though `\|` is the correct markdown way to write a literal pipe in a table cell.
- C1 entry quote cell `"…characters \| are used"` → cell splits, `exp/w_pipe_entry` → `backed 3 of 7`, `Cursor no quote cell not wrapped in double quotes`.
- C1 SOURCES row: the stray pipe makes `split("|")` ≠ 13 fields → row dropped, `exp/w_pipe_sources` → `backed 3 of 7`, `Gemini CLI no S902 absent or malformed in SOURCES.md`.
- C2: a `\|` in any cell shifts all later columns; with 9 cells there is no truncation to 8, so `r[7]` reads the wrong text — sandbox commit `97d7842` (write scope `read-only \| no writes`) → `conformant 1 of 2 lane verifiers; phantom 0` exit 1.
All deflate in the reproduced cases.

### F5 — MEDIUM — C2 — inflate — self-test flag check is literal-substring over file bytes
`FLAG_RE` flags (C2:67) are checked with `f.encode() not in src` (C2 `judge_row`, :141). Any backticked `--x` that appears anywhere in the file — usage prose, docstring, comments — satisfies the cell, so a gate can declare a non-self-test flag as its self-test.
Repro: sandbox commit `8d4168c`, self-test cell `` `--rev` `` (present only in usage text, not a self-test mode) → `conformant 2 of 2 lane verifiers; phantom 0` exit 0. Inflates: PROTOCOL § Gate standard asks for "self-test command and spelling"; the counter cannot tell a runnable mode from a mentioned string. Same weakness family: the entry-command check is substring containment (`path not in r[2]`), and `PAIR_RE` scans the whole verdict-map cell. Docstring declares "occurs as a literal", so this is the declared semantics — reported because it is the loosest link in C2.

### F6 — MEDIUM — C2 — inflate (vacuous verdict) — empty universe passes vacuously
A rev whose tree has no `verifiers/*.py|sh` and a header-only registry prints `gate registry rows conformant 0 of 0 lane verifiers; phantom 0` and exits 0 (sandbox commit `51d8a2e`, orphan tree with only SKILL.md). A mis-pointed `--rev` yields a green C2 line. The K==M and phantom==0 rule is honest per-revision, but the pass is vacuous when M=0; C1 has the mirror image (`backed 0 of 7` exit 1, honest). Low exploitability (needs a wrong rev) — medium because the printed line is indistinguishable from a real pass.

### F7 — LOW — C1 — inflate — same-heading re-entry after an empty section scores a second section
`table_rows` resets `in_sec`/`header_ok` on a repeated exact heading but never resets `rows` (only `done` suppresses it, and `done` only arms after a data row). With a first section that has header+separator but zero data rows, a later `### Description thresholds by client` section's rows are scored. Repro: `exp/w_reentry_scaffold` → `backed 1 of 7`, opencode BACKED from the re-opened section. Narrow trigger (first table must be empty), inflate direction.

### F8 — LOW — C2 — inflate — a pinned value may be a directory tree
`exists()` (C2:98) is `git cat-file -e rev:path`, which succeeds for trees. A gate pinning `` `corpus` `` (a directory, no file) stays conformant: sandbox commit `aebcb35` → `conformant 2 of 2 … phantom 0` exit 0. Docstring says "paths each of which exists at the revision" — a tree exists, but PROTOCOL's row field is "pinned-value path"; the pin validates nothing.

### F9 — LOW — C1 — inflate — leading-dot decimals mis-tokenize
`NUM_RE` requires a leading digit, so `.5% of context` tokenizes as `5%` (executed micro-repro: `tokens('.5% of context') == ['5%']`, and `has_token("the cap is 5% here", ["5%"]) == True`). A sloppy cell meaning 0.5% is backed by a quote saying 5%.

### F10 — LOW — C1 — deflate of diagnosis — `--root` at a nonexistent path reads as a measured zero
`read_file` returns `None` for missing files and `main` substitutes `""`, so `--root /nonexistent-xyz-Reviewer` prints `description thresholds backed 0 of 7 clients` exit 1 — an operator typo is indistinguishable from a measured zero (could-not-evaluate/2 never fires for C1's root mode; C2 has no root mode and does raise 2 for a missing SKILL.md).

### F11 — LOW — C1 — inflate (match set) — h1 does not close the lesson Gate section
`gate_quotes_by_id` (C1:197) flips sections only on lines starting `"## "`; an `# Appendix` h1 after `## Gate` leaves the section open, so quotes under later headings are still collected as recorded quotes (executed micro-repro: S901 after an h1 still collected). Over-collection weakens the Gate-equality check marginally; every entry quote must still equal one collected string exactly.

### F12 — LOW — C2 — both directions — universe is case-sensitive to `.py`
`universe()` (C2:81) keeps blobs whose name `endswith(".py")`/`(".sh")`. A committed `verifiers/LIB.PY` escapes M (undercount — registry-exempt), while a row honestly naming it can never be satisfied and counts as an eternal phantom: sandbox commit `0620be3` → `conformant 2 of 2 lane verifiers; phantom 1` exit 1. Docstring's literal reading; realistic only with odd filenames.

### F13 — LOW — [INFERENCE] — C1 — localized git messages break missing-file detection
`read_file` (C1:114) classifies a missing path by matching the English phrases `"does not exist"` / `"exists on disk, but not in"` in git's stderr; under a localized git (e.g. `LC_ALL=fr_FR.UTF-8`), a missing file would raise → exit 2 instead of the honest exit 1. Not reproducible on this host (`locale -a` shows only C/C.utf8/en_US.utf8/POSIX); the English path itself is verified working (tip run above).

## Checked and sound (no defect found)

- Whole-token number matching boundaries: `536` inside `1,536` rejected (lookbehind), `1,53` vs `1,536` rejected (lookahead), `2%` vs `12%`/`20%` rejected, `8,000.`/`1,536)` sentence punctuation not consumed, decimals bounded both sides (self-test arms + executed micro-repros).
- Rows after a blank line: once data rows exist, a blank line permanently ends the scored table — matches GFM (a blank line ends the table) and the docstring's "first table with header"; header+separator+blank+rows still collects (no premature `done` before the first data row).
- Header match: first-N-cells equality, case/backtick/bold-insensitive; C1 accepts extra columns ≥4 and C2 ≥8 as declared, with the column-shift risk covered under F4.
- Heading level: C1 sections close at the anchor's own level or higher; C2's `## Gate registry` closes at level ≤2; a `###` subheading inside either section does not close it (executed micro-repro) — consistent with the docstrings.
- C2 row rules: duplicate-code rejection, arrow/→ forms, gate requires `0=clean` and `1=failed`, gate may not say `none` for self-test/pinned values, `..`/absolute pinned paths rejected, owner exact `kotoba`, phantom rows inside the table counted and outside ignored (all self-tested; phantom-in-table re-verified at sandbox commits `c37e5e0`/`0620be3`).
- Q32 must-fail arms present and holding: sibling host arm and fragment-quote arm both in C1's self-test.

## By-design loosenesses (declared in the frozen docstrings; listed for calibration, not defects)

- Any-of-numbers: a threshold cell listing several numbers (`1,536 characters or 2% of context`) is backed by a quote containing any one of them — `exp/w_multinumber` scores Claude Code via a 2%-only quote. The docstring says "one of the number tokens"; the plan's "that same number" is looser than the code only when a cell lists several numbers.
- A wrong-header table under the exact heading is skipped, and a compliant table later in the same section is used (`exp/w_wrong_header`) — docstring says "first table with `header`", not "first table must have header".
- Bare-host pins accept subdomains (`host.endswith("."+h)`, self-test asserts `www.cursor.com` passes) — Q32 says "host equality"; the docstring declares "host equality or subdomain" and the sibling-host arm still holds. Host/path pins are exact.
- C2's declared non-measurements (exit codes really produced, gate-vs-probe fit) and C1's (render-cut vs budget vs maximum reading) are correctly out of scope per Q31.

## Verification gaps

- `--fetch`/`norm()`/`fetch()` (C1:225–238) untested here — it needs live fetches of pinned hosts; it has no self-test coverage and is a second measurement beside the declared one anyway.
- F13 not executed (no non-English locale installed) — code-path inference, marked above.
- C1's SOURCES column indices were checked against the real `corpus/SOURCES.md` header (`id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by` at `corpus/SOURCES.md:11`) — they line up; the fleet census regex at `/home/vgpnk/Projects/shokunin/CORPUS.md:135` matches the counter's row shape.
- Round-54 content (entry, Gate quotes, SOURCES rows) did not exist at tip when reviewed; all verdicts above are about counter code on synthetic worlds plus real-rev baselines, not about the incoming claim values.
