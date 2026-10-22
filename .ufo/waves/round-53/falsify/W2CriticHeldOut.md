Result: MIXED — the landed `verify_alwayson.py` disagrees with 6 of the 18 held-out cases that have a settled expectation (2 of 8 for `alwayson.04`, 4 of 10 for `alwayson.07`), including three false PASSes. Its verdicts on the live population match the scout's raw evidence. The prose describing the instrument contradicts its code on transient text.

Seat: `KotobaR53.W2CriticHeldOut` (critic, wave 2 falsify). Judged on: operability, calibration.
Target: C2 on held-out cases. This is a second measurement beside the frozen counter and changes nothing in it.
Judged revision: `c775d6823bfca8f0de8c0874032a954438b38edc`.
Sandbox: `/fast/scratch/hyaku/kotoba-r53/w2/W2CriticHeldOut`, a clone checked out at `c775d68`. Nothing in the lane was written except this report.
Tools: none installed or updated. Python 3.14.8 and curl were already on the host.

## Inputs pinned

- Instrument: `verifiers/verify_alwayson.py` at `c775d68`, sha256 `e4a8b3f230bb5c467798b6cb8bf31b420069d972844315dc4a85f243d9adc890`. This equals `git show c775d68:verifiers/verify_alwayson.py | sha256sum`.
- Case definitions: `/fast/scratch/hyaku/kotoba-r53/CriticC2Sizing/heldout/run_heldout.py`, sha256 `8a280d17…4cd68f`. I copied it byte for byte to `heldout-w2/cases_src.py` (same sha) and imported its `CASES` and `plant`, so the 21 fixtures are exactly the wave-1 ones.
- My runner: `heldout-w2/run_landed.py` (sha256 `86081ae3…`). It plants each case under `heldout-w2/targets/<case>/` and runs `python3 -B verifiers/verify_alwayson.py --check <box> --target <dir> --json`. Raw output is in `heldout-w2/results.json` (sha256 `42ce55ba…`).
- Frozen counter, for reference only: `check_alwayson_boxes.py` sha256 `d07b8fc2…bc1`, the same as at `3bb0a7a3`. `python3 -B verifiers/check_alwayson_boxes.py --rev c775d68… --repo <sandbox>` printed `always-on boxes executed and discriminating 2 of 8` (both boxes `6 of 6 cases as pinned`), exit 0.
- Source: https://code.claude.com/docs/en/memory.md, fetched with `curl -sS -L` at 2026-10-22T20:37:51Z. HTTP 200, 51,971 bytes, 638 lines, sha256 `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`. This is byte-identical (`cmp`) to the wave-1 copy. Saved at `<sandbox>/fetch/memory.md`.

## 1. Held-out table (21 cases), run at 2026-10-22T20:37:09Z

Command: `python3 -B heldout-w2/run_landed.py > heldout-w2/results.json`, exit 0. The "Expected" column cites the row in `.ufo/waves/round-53/build/CriticC2Sizing.md`. "Observed" is the instrument's JSON `status` and its exit code.

| # | Case | Box | Expected (source line) | Observed | Agree? |
| :- | :- | :- | :- | :- | :- |
| 1 | H04-transient-only | 04 | FAIL (`CriticC2Sizing.md:132`; `SKILL.md:371` live-state) | FAIL, exit 1 (`date-free transient cue 'currently'`) | yes |
| 2 | H04-us-numeric-date | 04 | FAIL (`:133`) | **PASS**, exit 0 | **no (false PASS)** |
| 3 | H04-quarter-year | 04 | FAIL (`:134`) | **PASS**, exit 0 | **no (false PASS)** |
| 4 | H04-day-month | 04 | FAIL (`:135`) | FAIL, exit 1 (`month-day date '1 Nov'`) | yes |
| 5 | H04-dated-dot-claude | 04 | FAIL (`:136`; `memory.md:370`) | FAIL, exit 1 (`.claude/CLAUDE.md:4`) | yes |
| 6 | H04-dated-local | 04 | FAIL (`:137`; `memory.md:122`) | FAIL, exit 1 (`CLAUDE.local.md:1`) | yes |
| 7 | H04-format-rule | 04 | PASS (`:138`, control) | PASS, exit 0 | yes |
| 8 | H04-versions | 04 | PASS (`:139`, control) | PASS, exit 0 | yes |
| 9 | H04-example-timestamp | 04 | undecided (`:150`; the harness leans PASS) | FAIL, exit 1 (`'2026-01-31T00:00Z'`) | undecided; differs from the lean |
| 10 | H07-code-span | 07 | FAIL (`:140`; `memory.md:112`) | FAIL, exit 1 | yes |
| 11 | H07-fenced | 07 | FAIL (`:141`; `memory.md:112`) | FAIL, exit 1 | yes |
| 12 | H07-relative-import (`@./AGENTS.md`) | 07 | PASS (`:142`; `memory.md:104`) | **FAIL**, exit 1 | **no (false FAIL)** |
| 13 | H07-suffix-not-import | 07 | FAIL (`:143`) | FAIL, exit 1 | yes |
| 14 | H07-symlink-elsewhere | 07 | FAIL (`:144`; `memory.md:357`) | FAIL, exit 1 | yes |
| 15 | H07-windows-symlink-text | 07 | FAIL (`:145`; `memory.md:461`) | FAIL, exit 1 | yes |
| 16 | H07-dot-claude | 07 | FAIL (`:146`; `memory.md:370`) | FAIL, exit 1 | yes |
| 17 | H07-dot-claude-import (`.claude/CLAUDE.md` = `@../AGENTS.md`) | 07 | PASS (`:147`; `memory.md:104,370`) | **FAIL**, exit 1 | **no (false FAIL)** |
| 18 | H07-nested-pair (`pkg/AGENTS.md` + `pkg/CLAUDE.md`) | 07 | FAIL (`:148`; box text "per repo") | **PASS**, exit 0 (`1 selected files; no independent AGENTS/CLAUDE pair`) | **no (false PASS)** |
| 19 | H07-dangling-symlink | 07 | FAIL (`:149`) | **ERROR**, exit 2 (`dangling symlink in CLAUDE.md`) | **no (ERROR instead of FAIL; not a false PASS)** |
| 20 | H07-local-only (`AGENTS.md` + `CLAUDE.local.md`) | 07 | undecided (`:151`; leans FAIL) | FAIL, exit 1 | undecided; matches the lean |
| 21 | H07-reverse-symlink (`AGENTS.md` links to `CLAUDE.md`) | 07 | undecided (`:152`; leans PASS) | FAIL, exit 1 | undecided; differs from the lean |

Disagreements per box, over the cases with a settled expectation:

| Box | Settled cases | Disagree | False PASS | False FAIL | ERROR instead of FAIL |
| :- | :- | :- | :- | :- | :- |
| `alwayson.04` | 8 | **2** | 2 (#2, #3) | 0 | 0 |
| `alwayson.07` | 10 | **4** | 1 (#18) | 2 (#12, #17) | 1 (#19) |
| total | 18 | **6** | 3 | 2 | 1 |

On the three undecided rows, the instrument matches one lean (#20) and differs from two (#9, #21). I found no L1 decision on these rows anywhere in the lane (`rg --hidden` for the case names and "L1 decision" finds only `CriticC2Sizing.md`), so they are not scored. The instrument's own fixtures take a position on two of them without an L1 ruling. `a04-fenced-date` (a fenced example date, expected FAIL) implies #9 = FAIL, and `a07-local-conflict` (expected FAIL) implies #20 = FAIL. One inconsistency in the wave-1 record: `CriticC2Sizing.md:150` says #9 "needs L1 decision", while its harness encodes `PASS?`.

How this compares with wave 1: the wave-1 reference delegate was wrong on 7 of these 18 cases. The landed instrument is wrong on 6. It fixes three of the reference's misses (#5, #6, #16, by reading `.claude/CLAUDE.md` and `CLAUDE.local.md`). It adds two misses the reference did not have (#12, #17), because it accepts only an exact `@AGENTS.md` line between sibling files.

## 2. Findings

**F1 — `alwayson.04` misses dates that are neither ISO nor month-day, including the authority's own example (BREAKS on held-out; severity medium for calibration).**
Counterexamples: #2 `11/01/2026` gives PASS, and #3 `Q4 2026` gives PASS. My extra probe `- If you are doing this before August 2025, use the old API.` (`heldout-w2/extra/month-year/AGENTS.md`) gives PASS, exit 0. That sentence is S019's bad example. The knowledge entry names it as "a shape to check against it" (`corpus/knowledge/alwayson-rule-files-round53.md:62-63`), and the instrument passes it. The cause is `MONTH_DAY_RE` (`verify_alwayson.py:87-91`): it requires a day, and `\d{1,2}…\b` cannot match the `20` in `2025`. The docstring is honest about this ("ISO calendar dates/timestamps, month-day strings", `:25-26`).
Impacted axes: calibration and operability.
Smallest safe correction: add a month-and-year form (`MONTH_NAME\.?\s+\d{4}`) and a numeric `d/m/yyyy` form to the instrument, with own-origin fixtures. This is the instrument's self-test, not the frozen counter, and the assertion floor only rises. Alternatively, state in the entry's line 62-63 that the named example passes the instrument.

**F2 — `alwayson.07` rejects import forms the source documents (BREAKS on held-out; severity low-medium, because the errors are conservative false FAILs).**
- #12 `@./AGENTS.md` gives FAIL. Source, `memory.md:104`: "Both relative and absolute paths are allowed. Relative paths resolve relative to the file containing the import".
- #17 `.claude/CLAUDE.md` containing `@../AGENTS.md` gives FAIL. The same line 104 applies, and line 370 says `.claude/CLAUDE.md` counts.
- Extra probe: `See @AGENTS.md for the shared rules.` in `CLAUDE.md` gives FAIL, exit 1. Source, `memory.md:112`: "writing `` `@README` `` keeps the text literal, while `@README` outside backticks imports the file." So the source treats inline `@AGENTS.md` outside backticks as an import.
- Extra probe: a trailing space (`@AGENTS.md ␠`) gives FAIL, and a two-space indent gives FAIL. [INFERENCE] Both are imports under `memory.md:106` ("the path ends at the first space"). A CRLF file gives PASS (correct).

The cause is `_has_import_line` (`verify_alwayson.py:309`, `line == "@AGENTS.md"`) plus `_redirects_to`, which requires the same parent directory (`:347-350`). The docstring states both limits (`:17-22`). The knowledge entry does not: its Claude Code row reads "a `CLAUDE.md` with an `@AGENTS.md` import", and its Limits (`:83-84`) list "other names, nested directories, transient text without a date" but not the exact-line, sibling-only import rule.
Impacted axes: calibration (an undisclosed narrowing in the entry) and operability (correct repositories are told to change).
Smallest safe correction: add one Limits clause to the entry ("the import redirect is accepted only as a line exactly `@AGENTS.md` in a sibling `CLAUDE.md`; `@./AGENTS.md`, inline imports and `.claude/CLAUDE.md` imports are reported FAIL"). Or widen the matcher to an `@`-token outside code that resolves to the sibling `AGENTS.md`, with fixtures.

**F3 — a nested independent pair passes (#18; severity low, because it is disclosed).**
`pkg/AGENTS.md` and `pkg/CLAUDE.md` with root `AGENTS.md` gives PASS with detail `1 selected files; no independent AGENTS/CLAUDE pair`. The box says "per repo" (`SKILL.md:375`). The docstring (`:28-30`, "does not … recurse beyond these fixed paths") and the entry's Limits ("nested directories") both disclose this. It has no live impact today: the depth-6 scan in §3 finds no nested `CLAUDE.md`. However, the PASS detail reads as a repository verdict. Note that the instrument's own `nested-pair` fixture is `.claude/AGENTS.md` + `.claude/CLAUDE.md`, not a subdirectory pair, so the name does not mean what #18 tests.
Smallest correction: make the PASS detail say "root and `.claude/` only".

**F4 — a dangling `CLAUDE.md` symlink is ERROR, exit 2, not FAIL (#19; severity low).**
This is consistent with the contract ("2 means usage or unreadable input", `:6-7`), and it is not a PASS. A box checker that reports a usage-class error for a repository defect is a calibration choice the L1 should state.

**F5 — the prose and the code disagree on transient text (BREAKS for calibration; severity low-medium; duplicate authorities).**
- Entry `alwayson-rule-files-round53.md:62`: "Its date detector misses undated transient text". Entry `:84` lists "transient text without a date" as not checked. The uncommitted lane `corpus/README.md:112` lists it as "still not held".
- Code: `TRANSIENT_RE` (`verify_alwayson.py:93-97`), the docstring (`:26-28`, "a small set of date-free transient cues"), and the own fixture `date-free-transient` (FAIL, `:415`). Held-out #1 gives FAIL on `currently` with no date.

The counter does not pin transient text (erratum item 3), so "not held" is the correct claim-scope reading. However, "misses undated transient text" is false about the code.
Smallest correction: reword the entry's line 62 to "flags six cue phrases only; other undated transient wording is missed, and the cues also fire on durable wording (F6)".

**F6 — the transient cues fire on durable rules (severity low-medium for operability).**
- Live false positive: `kimi-code/apps/kimi-code/AGENTS.md:25` "…settings popups that temporarily replace the editor." gives FAIL. This describes UI behaviour, not live state.
- Probes: `- Never store secrets in the repo, even temporarily.` gives FAIL, and `- Run tests on the currently checked-out branch before pushing.` gives FAIL.
- Live true positives, by my reading: `kimi-code/docs/AGENTS.md:18` "The changelog is currently generated manually…" and `xbrd-gdsp-fknpft/AGENTS.md:40` "no teammate currently uses this prefix".

So 1 of the 3 cue-only or cue-bearing live hits I read is a false FAIL.

**F7 — a directory with no rule files is FAIL on both boxes (severity low).**
An empty directory, `~/.omp/agent` and `~/.omp` each give `FAIL … no selected always-on rule files found`, exit 1. For `alwayson.07` ("one canonical name"), zero files is not a second name. The verdict is not wrong for "is there a rule file to judge", but it is a FAIL with no violation. [INFERENCE] A wrapper that walks directories would report every directory without a rule file as failing.

**F8 — the lane's uncommitted `SKILL.md` gives a command that exits 2 (severity medium for operability if committed; it is not in the judged revision).**
The lane working copy `SKILL.md:366` (an uncommitted edit; `git status` shows ` M SKILL.md`; absent at `c775d68`) says "Boxes 4 and 7 run as `python3 -B verifiers/verify_alwayson.py --target <dir>`". Run as written, it prints `verify_alwayson.py: error: --check and --target are required`, exit 2, with or without `--json`.
Smallest correction: `python3 -B verifiers/verify_alwayson.py --check alwayson.04|alwayson.07 --target <dir>`.

## 3. Live population (read-only), run at 2026-10-22T20:37:40Z

Command, per directory and box: `python3 -B <sandbox>/verifiers/verify_alwayson.py --check <box> --target <dir> --json`. The population is `ScoutAlwaysOnPop.md` §1–2 (host plus depth ≤2). The rule-file sha256 values I re-measured all equal the scout's: host `7b06a503…`, kimi-code `a6319863…`, opencodeufo `92b17a0d…`, shokunin `382f28ab…`, ufo-fsd-alpha `4896d671…`. `readlink kimi-code/CLAUDE.md` gives `AGENTS.md`.

| Target | alwayson.04 | alwayson.07 | Agrees with the scout's raw evidence? |
| :- | :- | :- | :- |
| `~/.agents` | FAIL, exit 1: `AGENTS.md:1` ISO `2026-10-19` ("# Operator tooling directive — 2026-10-19") | PASS, exit 0 (1 file) | yes (`ScoutAlwaysOnPop.md:177`) |
| `Projects/kimi-code` | PASS, exit 0 (2 files) | PASS, exit 0 (symlink redirect) | yes (`:80-82`, the PASS form) |
| `Projects/opencodeufo` | PASS, exit 0 | PASS, exit 0 | yes (no dates, `:178`) |
| `Projects/shokunin` | PASS, exit 0 (root file only; the 17 lane files are not walked) | PASS, exit 0 | yes |
| `Projects/ufo-fsd-alpha` | FAIL, exit 1: `AGENTS.md:87`, `:139`, `:268` (dated section headings, e.g. "## NC2 fleet dispatch protocol (standard, 2026-09-20)") | PASS, exit 0 | yes (`:177-178`) |
| `~/.omp/agent` (what omp loads; `RULES.md` is outside the class) | FAIL, exit 1: no selected files | FAIL, exit 1: no selected files | n/a (F7) |

By my reading, every box-04 FAIL in this table is a true positive: each is a date in a heading. Box 07's FAIL branch is unreachable on this population, which matches the scout's conclusion (`:92-96`).

Supplement: the scout's depth ≤6 list (`:65-70`). The same `find` gives 35 `AGENTS.md` files, which I ran per directory. Box 07 gives PASS on all 35. Box 04 gives FAIL on 9 and PASS on 26:

- `ds4cc-marketplace/…/xbrd-gdsp-fknpft` (ISO dates at `:5`, `:13`, `:15`, `:39` and `currently` at `:40`)
- `kimi-code/apps/kimi-code` (`temporarily` at `:25`, the false positive in F6)
- `kimi-code/docs` (`currently` at `:18`)
- `shokunin/game-dev-3d-shokunin` (`2026-10-18` at `:4`, `:27`)
- `shokunin/kama-shokunin` (`2026-10-20` at `:6`)
- `ufo-fsd-alpha`
- `xsnapshot/snapshots/2026-10-19/applied/{agents,devin}` (dates at `:1`; these are snapshot copies)

The two `.tower/jj-probe` worktree copies give PASS, so they are counted twice, as the scout predicted (`:73`).

## 4. Attacks: verdict summary

| Attack | Verdict | Severity |
| :- | :- | :- |
| The frozen counter line on the judged revision | HOLDS (`2 of 8`, exit 0) | — |
| Held-out agreement, `alwayson.04` | BREAKS on 2 of 8 (F1) | medium |
| Held-out agreement, `alwayson.07` | BREAKS on 4 of 10 (F2, F3, F4) | low-medium |
| The instrument agrees with the live population's raw evidence | HOLDS | — |
| The instrument's prose matches its code | BREAKS (F5; F2 is undisclosed in the entry) | low-medium |
| The documented invocation runs | BREAKS in the uncommitted lane `SKILL.md` (F8); not in `c775d68` | medium if committed |

None of these break the C2 statement, which is only the counter's printed line (Q26). They bound what the round may say about the instrument beyond the 12 pinned cases.

## 5. Sandbox record

- Clone: `/fast/scratch/hyaku/kotoba-r53/w2/W2CriticHeldOut` at `c775d68`, with no commits and nothing pushed.
- Scratch: `heldout-w2/cases_src.py`, `run_landed.py`, `results.json`, `targets/`, `extra/` (nine probe directories: inline, trailing-space, CRLF, indented and BOM-prefixed imports, two durable-cue rules, an empty directory, and `month-year`; the BOM-prefixed `@AGENTS.md` also gives FAIL) and `depth6.txt`; `fetch/memory.md`.
