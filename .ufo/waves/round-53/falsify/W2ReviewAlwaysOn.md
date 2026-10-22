Result: MIXED — `verifiers/verify_alwayson.py` at `c775d6823bfca8f0de8c0874032a954438b38edc` executes its printed contract (self-test 0 failures over 89, box-proof `boxes proven 2`, frozen counter re-measured `2 of 8` exit 0), but its docstring diverges from its code: a `CLAUDE.local.md` symlink to `AGENTS.md` is accepted as a redirect although the docstring promises the opposite, and the docstring omits the `alwayson.04` authority attribution the round-53 corpus entry requires (Q23).

Seat: `KotobaR53.W2ReviewAlwaysOn` (reviewer, wave 2 falsify). Target reviewed at the lane working tree, `git log -1` → `c775d6823bfca8f0de8c0874032a954438b38edc` (matches the judged revision). All probes ran in my sandbox clone `/fast/scratch/hyaku/kotoba-r53/w2/W2ReviewAlwaysOn` (`git clone` + `git checkout -q c775d682…`, exit 0). Tools: python3 3.14.8, git 2.56.0 (both already installed); nothing installed or upgraded. Lane writes: this report file only. No model calls, no network fetches needed for this seat (all source quotes cited from the wave-1 record, not re-fetched).

## What the instrument reads (assignment question 1, verified by code read)

- `--check`: exactly the five paths in `CANDIDATE_PATHS` (`verify_alwayson.py:66-72`) under `target.resolve(strict=True)` — `AGENTS.md`, `CLAUDE.md`, `CLAUDE.local.md`, `.claude/AGENTS.md`, `.claude/CLAUDE.md` (`load_candidates`, `:235-262`; openat/O_NOFOLLOW resolver `:128-192`, bounded reader `:195-232`). No glob, no recursion, no network import.
- `--self-test`: `verifiers/fixtures/alwayson/manifest.json` + the 29 case directories pinned in `CASE_EXPECTATIONS` (`:404-434`).
- `--box-proof`: `verifiers/checklist-baseline.json` (default map, `:640`), `SKILL.md` via `map_path.parent.parent` (`:566`), the fixture suite, and an in-process import of `verify_skill_checklist.extract_boxes` (`:568-571`).

## Findings

### F1 — MEDIUM: a `CLAUDE.local.md` symlink is accepted as a redirect; the docstring says it never is

- Docstring `verify_alwayson.py:18-20`: "`CLAUDE.local.md` is scanned for dates and counts as a CLAUDE-class file when AGENTS.md coexists, but it is not itself an accepted redirect."
- Code `_redirects_to` `:351-352` returns the symlink verdict **before** the name guard at `:355-356`; the guard's own comment (`:353-354`) says "Only an actual CLAUDE.md can carry the import redirect." The import branch enforces that; the symlink branch does not.
- Probe p1 (`AGENTS.md` regular + `CLAUDE.local.md` → symlink `AGENTS.md`, box `alwayson.07`): **PASS, exit 0**, detail "2 selected files; no independent AGENTS/CLAUDE pair". Contrast p1b (`CLAUDE.local.md` regular containing exactly `@AGENTS.md`): **FAIL, exit 1** — the two redirect forms treat the same name differently, which is the fingerprint of the ordering bug.
- Contract impact: the accepted redirect set is widened beyond the two forms the source documents (S043 names a `CLAUDE.md` symlink and the `@AGENTS.md` import; `memory.md:452-455`, `:442-445` per `.ufo/waves/round-53/build/ScribeClaudeCode.md` §2.3) and beyond the instrument's own prose — the Q31 divergence class (prose describes a check the code does not run) with a behavioral effect: a repo shape the docstring promises to fail passes silently.
- The frozen counter is unaffected (no pinned case symlinks `CLAUDE.local.md`; `a07-local-conflict` uses a regular file), so C2's `2 of 8` stands; this is an instrument-vs-docstring defect, not a counter break.
- Fix direction: move the `:355-356` name guard above the symlink branch (one-line reorder), plus a self-test arm for a `CLAUDE.local.md` symlink.

### F2 — MEDIUM: the docstring does not name `alwayson.04`'s authority (Q23), as the corpus entry requires

- `corpus/knowledge/alwayson-rule-files-round53.md:55-62` (craft point 5): the dated-text rule is "a lane extension of the skills rule" (S019), "and the instrument's docstring must say so (Q23)". QUALITY Q23 (`corpus/QUALITY.md:34`) requires an approximating check to name the parsed rule it approximates and applies "wherever the rule is described".
- The docstring attributes only the *filename set* to Claude Code's memory page (`:10-13`); the approximation paragraph (`:24-28`) describes the parsed date shapes but never says that no vendor documents a dated-text rule for `AGENTS.md`/`CLAUDE.md` and that the prohibition is lane craft grounded in `corpus/knowledge/alwayson-checklist-round7.md` and S019. A reader can attribute the date rule to the one authority the docstring does cite — exactly the M24 mis-attribution class. `ScribeClaudeCode.md` §2.5 states the same duty: "The instrument must not cite Claude Code for the date rule (Q20/Q23)."
- Corroboration: sibling seat `W2CriticDrift.md:152-155` (falsify wave) finds the same gap and shows the authority's own bad example passes the instrument (my probe p4 below reproduces it).
- Fix direction: 2–3 docstring sentences at `:24-28` naming the lane-extension grounding and the S019 anchor. No code change.

### F3 — LOW: chained symlink false FAIL contradicts the docstring's redirect rule

- Docstring `:20-21`: a CLAUDE.md-class file "redirects only when it is a symlink to its sibling AGENTS.md". Probe p2 (`CLAUDE.md` → `AGENTS.md` → `rules/real.md`): **FAIL, exit 1**, because `:352` compares the fully-resolved parts (`("rules","real.md")`) against the declared agent path (`("AGENTS.md",)`). The candidate *is* a symlink to its sibling `AGENTS.md`; the docstring predicts PASS. Conservative direction, exotic shape; client behavior for chained symlinks is undocumented (not measured here). Fix: compare the first-hop readlink resolution, or disclose the restriction in the docstring.

### F4 — LOW: inline code-span state survives a paragraph break, suppressing a live import

- Docstring `:21-22` says "imports inside code spans or fenced code do not count". `_has_import_line` sets `inline_ticks` on an unclosed run (`:333-335`) and never resets it at blank lines, and the exact-line match requires `inline_ticks is None` (`:309`). Probe p3 — `CLAUDE.md` = "Use the `tool\n\n@AGENTS.md\n": **FAIL, exit 1**, though under CommonMark the unclosed span ends with its paragraph and the `@AGENTS.md` line is a live import. False FAIL on a redirected repo; conservative direction. Fix: reset `inline_ticks` on an empty line, or restrict the state to one paragraph.

### F5 — LOW: month-year and numeric dates pass, and neither the docstring nor the fixtures pins the miss

- Probe p4, `AGENTS.md` = "… applies only before August 2025." → **PASS exit 0**; probe p4b, "Deprecated since 11/01/2026." → **PASS exit 0**. `MONTH_DAY_RE` (`:87-91`) requires a day number, so "August 2025" (month-year, the exact bad example on the S019 skills page per the corpus entry `:55-62`) does not match; numeric M/D/Y is not in any pattern (`ISO_DATE_RE :76-80`, `TRANSIENT_RE :93-97`).
- The docstring's scope ("month-day strings", `:26`) is honest, so this is not a Q31 falsehood — but the box prose ("No dated or transient text", `SKILL.md:371`) is wider than the instrument, Q23 asks for run counterexamples in both directions, and the corpus entry flags this exact shape "to check against it". The fixture set pins a miss guard for abbreviated month-day (`abbreviated-month-day` FAIL) but none for month-year or numeric dates. Same class as the held-out rows in `.ufo/waves/round-53/build/CriticC2Sizing.md` § Finding 6 (H04-us-numeric-date, H04-quarter-year); the wave-2 held-out seat owns the full sweep. Fix direction: one docstring sentence listing the missed shapes, and (optionally) one committed miss fixture each.

## Holds verified (probes, no defect found)

All commands `python3 -B verifiers/verify_alwayson.py --check <box> --target <dir> --json` in the sandbox clone; exit codes and JSON observed directly:

| probe | shape | observed |
|---|---|---|
| baseline | `--self-test` | `0 failure(s) over 89 assertions`, exit 0 (matches the registered floor 89) |
| baseline | `--box-proof` | `boxes proven 2`, exit 0 (map, SKILL.md hashes, fixtures all green) |
| counter | `check_alwayson_boxes.py --rev c775d682…` | `always-on boxes executed and discriminating 2 of 8`, exit 0 — re-measured fresh at the judged rev |
| p5a | absolute symlink landing in-target | PASS exit 0 (in-target absolute links followed) |
| p5b/p5c | relative/absolute symlink escaping target | ERROR exit 2, "escapes target directory" — matches docstring `:33-35` |
| p6 | dangling symlink | ERROR exit 2, "dangling symlink" |
| p7 | 1,049,009-byte AGENTS.md | ERROR exit 2, "exceeds the 1048576-byte limit" (over-limit rejected before read completes) |
| p8a/p8b | missing `--target`; invalid `--check` value | exit 2 with argparse usage text (no JSON — the contract only promises JSON for evaluated checks) |
| p9 | missing target dir | ERROR exit 2, checks entry present |
| p10 | non-UTF-8 rule file | ERROR exit 2, "is not UTF-8 text" |
| p11a/p11b | `2026-13-01` / `2026-02-30` | PASS exit 0 / FAIL exit 1 — matches docstring `:28-29` "does not … validate calendar dates": ranges are lexical, calendar semantics unchecked |
| p13 | `.claude/AGENTS.md` + `.claude/CLAUDE.md` → symlink `AGENTS.md` | PASS exit 0 (nested sibling redirect works) |
| p16 | symlink self-loop | ERROR exit 2, "too many symlink hops" (bounded at 40, no hang) |
| p17 | `CLAUDE.md` as directory | ERROR exit 2, "is not a regular file" |
| p18 | `.claude` as symlink to in-target dir | PASS exit 0, "1 selected files" (in-target directory symlinks followed) |

Exit-code contract (`:5-7`, mapping at `:649` PASS→0 / FAIL→1, `:651-652` InputError→2) and JSON shape (`emit_json :392-396`: `{"checks": [<entry with id/status/detail>], "exit_code": N}`, indent 2, sorted keys) hold on every probe; the counter's parser consumes it unchanged. Docstring Q31 audit: every other "does not / excludes" clause (`:29-35`) matches the code read — five fixed paths only, no recursion, no import following, 1 MiB cap enforced twice (`:206`, `:216`), no network. Cosmetic only: `emit_json`'s `error` parameter is never passed by any caller (dead parameter).

## Residual risk and verification gaps

- Client behavior for the F1/F3/F4 shapes (CLAUDE.local.md symlinks, chained symlinks, paragraph-spanning spans) is documented nowhere I read; my predictions of "what a client would do" are marked as CommonMark/doc reasoning, not measurements, and no client was run (no model calls).
- CRLF files: `str.splitlines()` strips `\r`, so the exact-line check should still match, but I did not run a CRLF probe — untested, not claimed.
- The full 21-row held-out table (CriticC2Sizing § Finding 6) belongs to the wave-2 held-out seat; I ran only the two date-shape rows (p4/p4b) that bear directly on docstring truthfulness.
- HTML blocks, blockquotes and indented-code contexts for the exact-line check were not probed (rare in rule files; static read suggests conservative suppression, unverified).
- No fix was applied: leaf bounds — findings only; the L1 owns the one-line reorder (F1), the docstring sentences (F2, F5) and optional self-test arms.
