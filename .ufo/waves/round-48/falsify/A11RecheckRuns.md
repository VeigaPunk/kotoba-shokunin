# A11RecheckRuns: round-48 falsify, Q04/Q12 recheck runs

Seat: KotobaR48.A11RecheckRuns (leaf). Judged on: freshness. Times UTC, 2026-10-22, runs 08:54Z to 09:01Z.
Targets: the entry's `recheck:` line (line 3) and the five commands in `.ufo/waves/round-48/build/C2RecheckCommand.md`. Lane master moved during the run (I1).

## Verdict

- Entry `recheck:` line, run verbatim: **CONFIRMED.** Count 1, exit 0. Fails closed: altered fixed string, rule line removed, and dead URL each give 0 and exit 1.
- C2 five commands: **CONFIRMED** on counts and exits (R1 1/0, R2 1/0, R3 1/0, R4 1/0, R5 2/0; negative control 0/1). **REFUTED** on one detail: pipefail on a dead URL exits 1, not 22 (L3).
- Source freshness (sha256, size, line cites): **CONFIRMED** for S018, S019, S017, S012, S021 and the PyPI wheel validator. S020 matches only in the worktree (M3).
- Gate coverage: **DEFECT, MEDIUM.** One recheck covers one of six sources, S021 has none, and nothing executes `recheck:` lines (M1, M2).
- Committed HEAD: **DEFECT, MEDIUM.** The lane checker `--json` exits 1 at 27887041 (M3).

## Findings, severity order

**M1 (MEDIUM) No runner.** Nothing executes `recheck:` lines or checks the `source:`, `verified-at:` and `recheck:` admission fields.
- Grep tool: `recheck` over `verifiers/` gives No matches; over lane `**/*.py` and `**/*.sh` gives No matches; `(?i)verified-at|verified_at|recheck` over `verifiers/` gives No matches.
- Lesson round-46 M4 (`corpus/lessons/round-46.md` line 22) recorded the same gap; round 48 adds no runner. A dead line cannot turn a gate red because no gate reads it.

**M2 (MEDIUM) Coverage gap; Limits overstates it.** Entry line 3 holds one command, for S018 only. Entry lines 99-101 say "Five of the six sources are read live; the recheck line and the commands in `C2RecheckCommand.md` fail closed." The five C2 commands cover S018 (R1), S017 (R2), S012 (R3, R4) and S019 (R5). S021 has no command in any file; C2 risk 5 says the five do not cover the Codex source (it names S013, superseded by S021). The "not stated (a)" cells rest on S021, so a Codex rule change would pass silently. The S017, S012 and S019 commands sit in a `.ufo` build report that nothing runs.

**M3 (MEDIUM, records) Committed HEAD fails the lane's own checker.** In a clean clone at 27887041, laid out like the fleet so `../` citations resolve: `python3 -B verifiers/verify_skill_checklist.py --repo <clone> --skill <clone>/SKILL.md --json` exits 1, 10 PASS / 1 FAIL. The FAIL is `governance.citation_resolves`: "SCORECARD.md:112: '.ufo/waves/round-48/falsify/A24UnreadableRoot.md' does not resolve". `git ls-files .ufo/waves/round-48/falsify/` at 27887041 prints nothing; the file exists only in the lane worktree. The same command on the worktree (`python3 -B`; grep found no file writes in the `--json` path) exits 0 with 11 PASS / 0 FAIL. So S020's "exit 0" holds only for the worktree state. For the integrator: commit the falsify report or fix the citation before calling the records green. I did not touch the lane.

**L1 (LOW) Inline comment misstates the cause.** Entry line 3 says "0 means the spec's rule text moved". A 404 also gives count 0 and exit 1 (`curl: (22) ... 404`). Limits (lines 99-100) states both cases. Suggested: "0 means the fetch failed or the rule text moved."

**L2 (LOW) The expected "1" is not enforced.** The gate is red only on 0; a duplicated rule line gives 2 and exit 0 (see commands below). That may be intended, but the comment reads as an assertion. Say "at least 1", or assert equality.

**L3 (REFUTED detail in C2RecheckCommand.md).** C2 says pipefail turns the exit into curl's 22. Observed: `bash -o pipefail -c "<entry command, dead URL>"` exits 1, because the rightmost non-zero status is grep's. Still red.

**L4 (residual) Substring, not section.** The grep matches anywhere on the page. If the sentence moved elsewhere on the page, the count stays 1 and the gate stays green.

**I1 (INFO) Moving target.** Lane master: 84b9c9b (records), then d28b16b (falsify corrections 1), then 27887041 (falsify corrections 2, committed 2026-10-22 05:58:57 -0300). Line 3 is byte-identical in all three and in the worktree (`IDENTICAL_TO_08_54Z_EXTRACT True`). Entry sha256 `e456be3f95dd0b763b0a1e8b5f4142ca8bcf845a28f9f6723d7de5bdc3d755a1` at 27887041 equals the worktree file. 27887041 fixed the spec cite spec.md:27 to spec.md:30 (live line 30 is the `name` row), added source-line URLs and the PyPI byte disclosure.

## Commands and exits (exact)

Entry line 3, verbatim (extracted 08:54:17Z; re-extracted from the 27887041 blob at ~09:00Z, identical):

    curl -fsSL https://agentskills.io/specification.md | grep -c 'Must match the parent directory name'  # 1 on 2026-10-22; 0 means the spec's rule text moved

- As written (`bash <file>`): stdout `1`, exit 0. Under `bash -o pipefail`: `1`, exit 0.
- Fixed string altered to `'Must match the parent folder name'`: stdout `0`, exit 1.
- Dead URL `.../specification-NOPE.md`: `curl: (22) ... 404`, stdout `0`, exit 1 (also 1 under pipefail).
- Rule line removed (`grep -v` into a scratch copy, read via `curl file://`): `0`, exit 1. Unmodified copy, same pipeline: `1`, exit 0. Line duplicated: `2`, exit 0.

C2RecheckCommand.md five commands, verbatim (run 08:55-08:57Z):

| id | source and fixed string | count | exit | C2 run |
|---|---|---|---|---|
| R1 | spec .md, `Must be 1-1024 characters` | 1 | 0 | 1 / 0 |
| R2 | validator.py @547831f3, `MAX_DESCRIPTION_LENGTH = 1024` | 1 | 0 | 1 / 0 |
| R3 | quick_validate.py @dbd4588, `Description cannot contain angle brackets (< or >)` | 1 | 0 | 1 / 0 |
| R4 | same file @main | 1 | 0 | 1 / 0 |
| R5 | best-practices .md, `Cannot contain XML tags` (lines 155, 162) | 2 | 0 | 2 / 0 |
| NEG-A | quick_validate.py @dbd4588, `Description must not contain angle brackets` | 0 | 1 | 0 / 1 |

## C. Freshness cross-checks (today's bytes)

sha256 and size. Fetched 08:56:14Z (S018, S019, S017, S012) and 08:56:54Z (S021); re-hashed 08:58-09:00Z.
- S018 spec .md: `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`, 7608 B. Matches.
- S019 best-practices .md: `f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960`, 42169 B. Matches.
- S017 validator.py @547831f3 and @69ef37e9: both `b5ee3d8537c83c959c31c2cb080a5227646ede5aea545f1ac835ed3c4645f6c5`, 5154 B. Matches.
- S012 quick_validate.py @dbd4588 and @main: both `67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365`, 3972 B. Main equals the pin today.
- S021 build-skills.md: `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5`, 11035 B, 232 lines. Matches.
- PyPI skills_ref-0.1.1 wheel: sha256 `d35db5bb...` equals the PyPI digest. Member `skills_ref/validator.py`: sha256 `7b5cb3dc...`, 5347 B, 177 CRLF line endings, contains `read_text(encoding='utf-8')`. Matches the new disclosure.
- Line cites all match: spec.md 30, 63, 64, 66, 67, 101, 161, 237; best-practices.md 153-156, 160-162, 206, 257; validator.py 10, 11, 37, 51-52, 54, 60-64, 110-113; quick_validate.py 42-49, 65, 67, 70-71, 78, 79-81, 83-84; build-skills.md 39.
- Negative sweeps: spec.md `(?i)angle|xml|third person|reserved word|unknown field|unrecognized` and case-sensitive `MUST|SHOULD` give no matches. best-practices.md `(?i)consecutive|unknown field|unrecognized` gives no matches; `third person` is at line 206 only. quick_validate.py `dirname|basename|parent|(?i)third person|(?i)reserved` gives no matches. build-skills.md footnote (a) pattern gives no matches.
- URLs: the four that the 27887041 source line names, plus the S012 tree, all return HTTP 200 (agentskills.io/specification; github .../tree/69ef37e9.../skills-ref; platform.claude.com best-practices; learn.chatgpt.com/docs/build-skills; github .../tree/dbd4588.../skill-creator). The HTML spec page gives count 2 for the description rule; the .md gives 1 (reproduces C2 F6).
- S020: `--self-test` in the 27887041 clone prints `0 failure(s) over 1845 assertions`, exit 0. `--json` on the worktree: exit 0, 11 PASS / 0 FAIL.

## Located quotes (each at most 25 words; UTC)

- spec.md:67, 08:56:14Z: "Must match the parent directory name". spec.md:101: "Must be 1-1024 characters".
- best-practices.md:155, 08:56:14Z: "Cannot contain XML tags". Line 206: "Always write in third person".
- quick_validate.py:81 @dbd4588, 08:56:14Z: "Description cannot contain angle brackets (< or >)".
- validator.py:11 @547831f3, 08:56:14Z: "MAX_DESCRIPTION_LENGTH = 1024".
- build-skills.md:39, 08:56:54Z: "context window, or 8,000 characters when the context window is unknown".
- PyPI wheel `skills_ref/validator.py`, about 09:00Z: "read_text(encoding='utf-8')".
- Not quoted (HTTP status only): the GitHub tree pages and the agentskills.io HTML page.

## Actions, installs, bounds

- Installed or upgraded: nothing (no pacman, npm, cargo or uv action).
- Lane: read-only. Git reads only (`ls-remote`, `rev-parse`, `show`, `log`, `diff`, `cat-file`, `merge-base`, `ls-files`) and a `git clone` into scratch. The checker ran with `--json` once in the worktree (`python3 -B`). The only lane file written is this report.
- Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A11RecheckRuns/`.

## Not run, residual gaps

- The C2 mutation battery for R2-R5 is not reproduced; only the entry line's mutations were run.
- PyPI sdist and `prompt.py:46` (S017) not checked.
- Results are for 27887041; re-run the recheck line and M3 after the final commit.

## Out-of-scope observations (not touched)

- The fleet root holds an entry literally named `bash: ` and near-duplicate directories `mori-shokukin`/`mori-shokunin` and `tameshi-shokukin`/`tameshi-shokunin`. These look like typing or shell mishaps.
