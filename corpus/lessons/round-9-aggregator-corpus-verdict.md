# Round 9 aggregator corpus verdict — kotoba

> **Path convention.** Bare `CORPUS.md`, `PROTOCOL.md`, `MANIFEST.json`, `SCORECARD.md`, `LOG.md`, `.ufo/…` and `<lane>-shokunin/…` pointers in this file are **main-repo (`shokunin`) relative** — they do not resolve inside this checkout. Paths inside this checkout are written `corpus/…`, `SKILL.md`, `SHONEN.md`, `PROVINCE.md`.

Measured against landed `kotoba-shokunin` commit `63ceba7`. The tree was clean at the L1 stamp; a later concurrent worktree showed two unrelated edits, so this verdict uses committed bytes at `63ceba7`.

## Verdict

**not conformant — rules 7, 8, and 10 fail.** Rule 8 is **FAIL-literal / PASS-intent**: three committed `op://` occurrences are schematic or quoted sweep language, not resolvable vault references, but CORPUS.md's literal rule has no placeholder exception. Rule 7 remains open because the committed coverage index has 40 distinct backticked paths for 43 tracked corpus markdown files (excluding README), with four missing files and one stale brace-pattern row. Rule 10 is not yet satisfied in the landed child commit because no current round-9 aggregator verdict lesson is present there.

## Re-runnable evidence

- `python3 verifiers/verify_surfaces.py` → exit 0, seven PASS checks: 42 loader-kind entries, 8 omp classes, 9/9 opencode classes from 7/7 rules, 42 ids, 8 excluded entries.
- `python3 verifiers/verify_surfaces.py --self-test` → exit 0, `0 failure(s) over 75 assertions`; isolated fixtures assert exit codes and stable finding IDs.
- `python3 verifiers/verify_harness_claims.py --self-test` → exit 0, `0 failure(s) over 10 assertions`; `python3 verifiers/verify_harness_claims.py` → exit 0, `27/27 checks pass`.
- No committed SKILL.md registry row was found that declares either verifier as a §Gate-standard `gate|probe` with verdict map, self-test spelling, pinned-value path, write scope, and owner. No separate committed frozen-snapshot run was found for the mutable live-host measurements. They are gate-shaped read-only verifiers, but registry/two-evidence conformance is absent.
- `git grep -n 'op://' 63ceba7 -- corpus/` → 3 hits: `knowledge/sibling-description-rewrites-round8.md:141,151`; `lessons/round-5-aggregator-audit.md:83`. All are schematic/quoted patterns; no secret value is reproduced.
- D-29: `git show 63ceba7:SHONEN.md` retains stale self-count wording; `corpus/README.md` has 41 data table rows, the parity sweep finds 40 indexed paths vs 43 tracked markdown files, and `SKILL.md` has 40 unchecked boxes. D-72's newline subdefect is closed: committed `SHONEN.md` ends in `\n` (5,377 bytes).

## Box 3 and L0

Round-8 box 3 remains `[~]` absent a fresh committed non-author cold-run artifact. `[x]` requires a named cross-lane/non-author record at the repaired `SKILL.md` revision, with explicit newest-session selection, fault-harness gate classification, exit codes, and finding IDs; a lane-authored rerun cannot provide that promotion evidence.

The r13 L0 question remains unanswered: `/home/vgpnk/projects/shokunin/.ufo/l0-questions.md` (main repo) line filed `kotoba | round-13 | Axis-accounting ratification` records coverage 7→8.0 as an advisory lowest-axis move while mission assigns depth+consistency; `/home/vgpnk/projects/shokunin/.ufo/reports/round-14/kotoba.md:126-129` records that the question was still unanswered and coverage was worked again. This lesson reports both sides without making the operator-side ruling.

---

**Round-15 repair (kotoba lane, appended).** Two `shokunin:`-prefixed pointers above were rewritten to host-absolute form by the kotoba lane in round 15, under the round-13 convention that dead pointer sites in in-repo corpus files are repaired by the repo's owning lane: the corpus verifier resolves pointer bases and has no exception for a documented main-repo-relative convention, so both sites read as dead and kept `corpus.pointers.report_dead` non-zero. The file's header convention note is otherwise preserved; no finding, verdict or routed row was altered.
