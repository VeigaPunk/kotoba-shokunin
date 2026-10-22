Result: MIXED — the three requested naive delegates each stop at 1 of 8, and the C2 statement is bounded to the counter's printed line (Q26 holds), but a delegate only slightly less naive reaches `2 of 8` (exit 0) while being wrong on 13 of 18 held-out cases, and the frozen counter counts a delegate that is not in the revision.

Seat: KotobaR53.CriticC2Sizing (critic, wave 1 build). Judged on: operability, calibration.
Sandbox: `/fast/scratch/hyaku/kotoba-r53/CriticC2Sizing` (clone of the lane at plan commit `3bb0a7a3`). Nothing in the lane was edited except this report.
Frozen counter used: `verifiers/check_alwayson_boxes.py`, sha256 `d07b8fc2ac8c43f760bb0420dca1b2b46f1a5bafee00461c9c4d96a60c28bfc1`, identical to `git show 3bb0a7a:verifiers/check_alwayson_boxes.py | sha256sum`.
Tools: none installed or updated. Python 3.14.8 and git 2.56.0 were already on the host.

## Finding 1: the three requested naive delegates are discriminated

I wrote one shared module (`verifiers/alwayson_common.py`) and five delegates in the clone. The map sends both boxes to one path, `verifiers/alwayson_delegate.py`, and I made one commit per variant by copying that variant onto the path. Each delegate applies one rule to `alwayson.04` and one rule to `alwayson.07`. Where the naive rule is for one box only, the other box gets my reference rule, so each counter line isolates the naive rule.

| Delegate (commit) | alwayson.04 rule | alwayson.07 rule | Counter result |
| :- | :- | :- | :- |
| `naive_n1_isodate` (`76b9619`) | ISO date regex `\d{4}-\d{2}-\d{2}` only | reference | 1 of 8, exit 1 |
| `naive_n2_substring` (`51af5fe`) | reference | PASS if `CLAUDE.md` text contains `AGENTS.md` | 1 of 8, exit 1 |
| `naive_n3_twofiles` (`5725ff2`) | reference | FAIL whenever both files exist | 1 of 8, exit 1 |
| `naive_n4_survivor` (`0be9671`) | ISO date or month-name-plus-day; no transient-word detection | PASS if `CLAUDE.md` is any symlink or has raw `@AGENTS.md` anywhere | **2 of 8, exit 0** |
| `ref_alwayson` (`d9e8851`) | ISO date, month-and-day, or transient words | symlink that resolves to `AGENTS.md`, or an `@AGENTS.md` / `@./AGENTS.md` import outside code spans and fences | 2 of 8, exit 0 |

Command for each commit: `python3 -B verifiers/check_alwayson_boxes.py --rev HEAD --repo /fast/scratch/hyaku/kotoba-r53/CriticC2Sizing`. Observed output:

```
=== naive_n1_isodate @ 76b9619
always-on boxes executed and discriminating 1 of 8
  alwayson.04: not counted (1 of 6 cases wrong: month-day expect FAIL, saw exit 0, PASS)
  alwayson.07: counted (6 of 6 cases as pinned)
exit=1
=== naive_n2_substring @ 51af5fe
always-on boxes executed and discriminating 1 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: not counted (2 of 6 cases wrong: symlink-redirect expect PASS, saw exit 1, FAIL; prose-mention expect FAIL, saw exit 0, PASS)
exit=1
=== naive_n3_twofiles @ 5725ff2
always-on boxes executed and discriminating 1 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: not counted (2 of 6 cases wrong: import-redirect expect PASS, saw exit 1, FAIL; symlink-redirect expect PASS, saw exit 1, FAIL)
exit=1
=== naive_n4_survivor @ 0be9671
always-on boxes executed and discriminating 2 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: counted (6 of 6 cases as pinned)
exit=0
=== ref_alwayson @ d9e8851
always-on boxes executed and discriminating 2 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: counted (6 of 6 cases as pinned)
exit=0
```

So the pinned cases do kill the three naive designs named in the assignment: the `month-day` case kills the ISO-only regex; `prose-mention` and `symlink-redirect` kill the `AGENTS.md` substring; and `import-redirect` and `symlink-redirect` kill the always-flag-two-files rule.

## Finding 2 (counterexample): a weak delegate reaches 2 of 8, and the counter cannot tell it from a better one

`naive_n4_survivor` passes all 12 pinned cases. On the held-out cases in Finding 6 it is wrong on 13 of 18 cases that have a settled expectation. That is more than `naive_n3_twofiles` (8), which the counter rejects, and more than `ref_alwayson` (7). Passing the counter therefore does not order instruments by quality on cases it does not pin. [INFERENCE] The 12 cases are public in the counter file, so an instrument written after the plan commit can be fitted to them, and the counter cannot detect that.

Two specific gaps:

- **No transient-only case for `alwayson.04`.** `plans/round-53.md:46` says "4 dated/transient FAIL cases". All four FAIL cases contain a date (`check_alwayson_boxes.py:69-74`), and transient wording ("Until", "As of", "is down") appears only next to a date. A delegate with no transient detection at all (`naive_n4_survivor`) counts. The box text is "No dated or transient text" (`SKILL.md:371`). Any prose saying the instrument checks transient text or live state goes beyond what the counter measures (Q31) and must be labelled reviewer judgment. The statement itself (`plans/round-53.md:39-40`) does not make that claim.
- **`alwayson.07` has no case that separates a real import from the raw `@AGENTS.md` string, or a symlink to `AGENTS.md` from a symlink to anything else.** The source says import parsing skips code spans and fenced blocks (`memory.md:112`), but no pinned case puts `@AGENTS.md` inside a code span or fence, and no case symlinks `CLAUDE.md` to a different file.

Impacted axes: calibration (the claim `2 of 8` is weaker evidence of discrimination than its wording suggests), and operability (a passing instrument can still misjudge real repositories).

## Finding 3 (counter defect): the counter counts a delegate that is not in the revision

The counter's docstring says a box counts only if the disposition is `delegated:<repo-relative path>` and "that file exists in the revision" (`check_alwayson_boxes.py:30`). The code builds `script = tree / d.split(":", 1)[1]` (`check_alwayson_boxes.py:144`). In Python, joining a path with an absolute path discards the left side, so an absolute disposition escapes the extracted tree.

Probe (commit `626abcf`): I deleted every delegate file from the revision and pointed both dispositions at `/fast/scratch/hyaku/kotoba-r53/CriticC2Sizing-ext/ref_alwayson.py`. Before that I confirmed that `git ls-tree -r --name-only HEAD verifiers` lists only `check_alwayson_boxes.py` among names matching `alwayson_`.

```
always-on boxes executed and discriminating 2 of 8
  alwayson.04: counted (6 of 6 cases as pinned)
  alwayson.07: counted (6 of 6 cases as pinned)
exit=0
```

The no-harm guard does not catch it either: `python3 -B verifiers/verify_skill_checklist.py --repo <clone> --check checklist.box_map_complete --json` exits 0 with `PASS … delegated /fast/scratch/hyaku/kotoba-r53/CriticC2Sizing-ext/ref_alwayson.py: no --box-proof support …, not run`. Its escape check rejects only `..` segments (`verify_skill_checklist.py:1244`), not absolute paths.

So on this point the docstring describes a check the code does not run (the Q31 class). The defect is fixable without widening the frozen counter (Q28); see the corrections below.

## Finding 4: the denominator is read from the revision, so `2 of 7` also exits 0

Probe (branch `drop-box`, commit `d4fdb88`, from the `ref_alwayson` commit): I removed the `alwayson.08` entry from the map.

```
always-on boxes executed and discriminating 2 of 7
  ...
exit=0
```

The guard catches this: `checklist.box_map_complete FAIL unmapped box at line 377 …`, guard exit 1. The statement's "of 8" is supported only by the printed text, not by the exit code (`check_alwayson_boxes.py:166`: `0 if n == len(CASES)`). Under Q26 this is acceptable only if the judge compares the printed line word for word and also runs the no-harm guard. Exit 0 alone does not establish the claim.

Related: for both the real map and the sandbox maps, the guard reports the C2 delegate as `no --box-proof support …, not run`. The no-harm guard never executes the C2 instrument, so the guard is no evidence of how the instrument behaves.

## Finding 5: the redirect rule matches the source, with qualifiers the counter does not encode

I opened the page myself:

- URL: https://code.claude.com/docs/en/memory.md
- Accessed: 2026-10-22T20:04:26Z (UTC), with `curl -sS -L`
- Result: HTTP 200, 51,971 bytes, 638 lines
- sha256: `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`
- Saved copy: `/fast/scratch/hyaku/kotoba-r53/CriticC2Sizing-fetch/memory.md`

No `corpus/SOURCES.md` row cites this page yet: `rg 'memory\.md|code\.claude\.com' corpus/SOURCES.md` finds only S022, S026 and S033. The fetch record above can be used for the scribe's row.

What the source supports, with verbatim quotes and line numbers in the fetched bytes:

- **Import redirect.** Line 442: "putting an `@AGENTS.md` import in a `CLAUDE.md` next to it". Line 445 is the bare line `@AGENTS.md`. This matches the `import-redirect` case.
- **Symlink redirect.** Line 452: "If you don't need Claude-specific content, a symlink also works". Line 455 is `ln -s AGENTS.md CLAUDE.md`. This matches `symlink-redirect`.
- **Both files present.** Line 357 (table row): "An `AGENTS.md` and a `CLAUDE.md` or `CLAUDE.local.md` … | Your `CLAUDE.md` files only". This matches `two-rule-files` = FAIL.
- **Prose mention is not an import.** Line 436: "A `CLAUDE.md` that tells Claude in words to read `AGENTS.md`: Claude sees `AGENTS.md` only if it decides to open the file." The counter states this without citing it (`check_alwayson_boxes.py:21-22`). Line 436 is the source sentence the knowledge entry should cite.
- **Direct `AGENTS.md` reading.** Line 368: "By default, Claude reads `AGENTS.md` only when you have no `CLAUDE.md` in your working directory or above it." Line 364: "Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later." This supports `agents-only` = PASS.

Qualifiers the counter does not encode:

1. **The both-files rule is the default only.** The `claude-md-and-agents-md` value reads both files (line 391). That value is honoured only from user, `--settings` or managed settings and is ignored in project settings (line 395), so a repository cannot declare it. FAIL on two independent files therefore stays correct per repository.
2. **The import is now a compatibility redirect, not a requirement.** Line 435 says a `CLAUDE.md` holding only `@AGENTS.md` can be removed. The source presents the import for sessions that do not read `AGENTS.md` directly (line 442), so any prose calling the import "required" over-reads the source.
3. **More files count than the two the pinned cases use.** `.claude/CLAUDE.md` and `CLAUDE.local.md` also block `AGENTS.md` (line 370: "a `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` in your working directory or any directory above it"). No pinned case uses either file.
4. **Imports inside code are skipped.** Line 112: "Import parsing skips Markdown code spans and fenced code blocks." No pinned case tests this.
5. **A symlink can arrive as text.** Line 461: "Git checks a committed symlink out as a plain text file unless `core.symlinks` is enabled". That leaves a one-line `CLAUDE.md` whose text is `AGENTS.md`, which is a prose mention and not a redirect.

Verdict on the source question: the redirect rule the counter pins (import or symlink passes; two independent files fail; a prose mention fails) is what the source says for default settings. Items 3–5 are documented behaviour the pinned cases never exercise.

## Finding 6: held-out cases proposed for wave 2

These are not to be added to the frozen counter (Q28). Run them in wave 2 against the delivered instrument and report the result as a second measurement beside the declared one.

The harness is `/fast/scratch/hyaku/kotoba-r53/CriticC2Sizing/heldout/run_heldout.py`, run with `python3 -B heldout/run_heldout.py` (exit 0). In the table, "ok" means the delegate matched the expected status and "WRONG" means it did not.

| Case | Box | Expected | n1 | n2 | n3 | n4 (passes counter) | ref | Basis |
| :- | :- | :- | :- | :- | :- | :- | :- | :- |
| H04-transient-only ("currently down", no date) | 04 | FAIL | WRONG | ok | ok | WRONG | ok | `SKILL.md:371` live-state |
| H04-us-numeric-date (`11/01/2026`) | 04 | FAIL | WRONG | WRONG | WRONG | WRONG | WRONG | box text |
| H04-quarter-year (`Q4 2026`) | 04 | FAIL | WRONG | WRONG | WRONG | WRONG | WRONG | box text |
| H04-day-month (`1 Nov`) | 04 | FAIL | WRONG | ok | ok | ok | ok | box text |
| H04-dated-dot-claude (date in `.claude/CLAUDE.md`) | 04 | FAIL | WRONG | WRONG | WRONG | WRONG | WRONG | `memory.md:370` |
| H04-dated-local (date in `CLAUDE.local.md`) | 04 | FAIL | WRONG | WRONG | WRONG | WRONG | WRONG | `memory.md:122` |
| H04-format-rule (`YYYY-MM-DD`) | 04 | PASS | ok | ok | ok | ok | ok | control |
| H04-versions (`Python 3.10 … Node 22`) | 04 | PASS | ok | ok | ok | ok | ok | control |
| H07-code-span (`` `@AGENTS.md` ``) | 07 | FAIL | ok | WRONG | ok | WRONG | ok | `memory.md:112` |
| H07-fenced (`@AGENTS.md` in a fence) | 07 | FAIL | ok | WRONG | ok | WRONG | ok | `memory.md:112` |
| H07-relative-import (`@./AGENTS.md`) | 07 | PASS | ok | ok | WRONG | WRONG | ok | `memory.md:104` |
| H07-suffix-not-import (`@AGENTS.md.bak`) | 07 | FAIL | ok | WRONG | ok | WRONG | ok | imports another file |
| H07-symlink-elsewhere (`CLAUDE.md` links to `docs/claude-rules.md`) | 07 | FAIL | ok | ok | ok | WRONG | ok | `memory.md:357` |
| H07-windows-symlink-text (`CLAUDE.md` text is `AGENTS.md`) | 07 | FAIL | ok | WRONG | ok | ok | ok | `memory.md:461` |
| H07-dot-claude (`AGENTS.md` and `.claude/CLAUDE.md`, no import) | 07 | FAIL | WRONG | WRONG | WRONG | WRONG | WRONG | `memory.md:370` |
| H07-dot-claude-import (`.claude/CLAUDE.md` = `@../AGENTS.md`) | 07 | PASS | ok | ok | ok | ok | ok | `memory.md:104,370` |
| H07-nested-pair (`pkg/AGENTS.md` and `pkg/CLAUDE.md`) | 07 | FAIL | WRONG | WRONG | WRONG | WRONG | WRONG | box says "per repo"; `memory.md:376` |
| H07-dangling-symlink (`CLAUDE.md` links to a missing `AGENTS.md`) | 07 | FAIL | WRONG | WRONG | WRONG | WRONG | WRONG | no readable rule file |
| H04-example-timestamp (example date in a format rule) | 04 | needs L1 decision | FAIL | FAIL | FAIL | FAIL | FAIL | is an example date "dated text"? |
| H07-local-only (`AGENTS.md` and `CLAUDE.local.md`) | 07 | needs L1 decision (FAIL?) | PASS | PASS | PASS | PASS | PASS | `memory.md:357,382` blocks `AGENTS.md`, but the file is gitignored per `:122` |
| H07-reverse-symlink (`AGENTS.md` links to `CLAUDE.md`) | 07 | needs L1 decision (PASS?) | FAIL | FAIL | FAIL | FAIL | FAIL | one file; the source does not name this form |

Totals over the 18 cases with a settled expectation: n1 wrong on 9, n2 on 11, n3 on 8, n4 on 13, ref on 7. Even my reference delegate misses the root-only scope and the numeric-date forms, so every row marked WRONG for ref is real work for the delivered instrument, not a strawman.

## Smallest safe corrections (none of them touches the frozen counter)

1. **Finding 3.** At judgment, the L1 records beside the counter line that both `alwayson.04` and `alwayson.07` dispositions are relative paths listed by `git ls-tree -r --name-only <rev> -- verifiers/`. As a routed repair to the no-harm guard, `verify_skill_checklist.py:1244` should also reject absolute targets (`Path(target).is_absolute()`), with a self-test arm beside `delegated-escape` (`verify_skill_checklist.py:2054`). This does not change the guard's exit code on the real map.
2. **Finding 4.** The verdict reads the printed line word for word (`2 of 8`), not the exit code, and requires `box_map_complete` PASS.
3. **Finding 2 (Q26/Q31).** The knowledge entry's Limits and the SCORECARD cell say that `alwayson.04` is shown to discriminate dated text on the pinned cases, and that transient or live-state detection without a date is reviewer judgment. The plan's "4 dated/transient FAIL cases" (`plans/round-53.md:46`) should be read as "4 dated FAIL cases". The `alwayson.07` entry names the source qualifiers from Finding 5 (default setting only; `.claude/CLAUDE.md` and `CLAUDE.local.md` not covered; code-span imports not covered).
4. **Finding 6.** Wave 2 runs the held-out table against the delivered instrument as a second measurement, after the L1 decides the three undecided rows.

## Sandbox record

- Clone: `/fast/scratch/hyaku/kotoba-r53/CriticC2Sizing`. Commits on a detached head from `3bb0a7a3`: `76b9619`, `51af5fe`, `5725ff2`, `0be9671`, `d9e8851`, `626abcf` (escape probe). Branch `drop-box`: `d4fdb88`. Nothing was pushed.
- Out-of-revision delegate copy: `/fast/scratch/hyaku/kotoba-r53/CriticC2Sizing-ext/`.
- Fetched source: `/fast/scratch/hyaku/kotoba-r53/CriticC2Sizing-fetch/memory.md`.
