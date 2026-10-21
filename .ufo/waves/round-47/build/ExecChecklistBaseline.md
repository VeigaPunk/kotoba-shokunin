verdict: Verdict-neutral: the `<skills>` removal moves 0 of 10 checks (9 PASS / 1 FAIL before and after; only `trigger.frontmatter_parses` detail changes, 814 to 810 chars), so the checker is blind to the tag, and the edit leaves SKILL.md:151 stale, which L1 must amend.

# ExecChecklistBaseline: round-47 no-harm baseline for verify_skill_checklist.py

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Citations are `path:line` at BASE unless marked otherwise. Scratch lane: `/fast/scratch/kotoba-r47/ExecChecklistBaseline/lane` (detached at BASE, one edit). Patch: `.ufo/waves/round-47/build/ExecChecklistBaseline.patch` (524 B, one hunk, SKILL.md only).

## Axes

- **freshness**: does the BASE baseline reproduce from the frozen bytes and the real fleet layout?
- **operability**: does the verifier run, and does the one-line edit move any verdict?
- **calibration**: do the PASS/FAIL verdicts match repository truth?

## Method: a mirror, not a bare clone

A bare clone is not production-faithful. Two inputs depend on checkout identity, not content:

- `trigger.name_directory` compares `name` with the basename of the file's directory (`verifiers/verify_skill_checklist.py:1202-1203`; spec `:77-81`).
- `..` citations and governance tokens resolve against the checkout's parent (`:1307-1316`; governance root is `repo.resolve()` at `:1456`).

I built `/fast/scratch/kotoba-r47/ExecChecklistBaseline/` as a scratch fleet mirror: 48 symlinks to fleet-root entries (`kotoba-shokunin` excluded, nothing written to the fleet root) plus `kotoba-shokunin -> lane`. The verifier ran with `--skill /fast/scratch/kotoba-r47/ExecChecklistBaseline/kotoba-shokunin/SKILL.md`.

Freshness: six governed inputs are byte-identical between BASE and the production working copy (`SKILL.md`, `LOG.md`, `SCORECARD.md`, `verifiers/verify_skill_checklist.py`, `verifiers/checklist-baseline.json`, `verifiers/checklist-command-vocabulary.json`). `..` targets are live fleet state and can drift between runs.

## The ten checks at BASE (mirror run; `build/ExecChecklistBaseline.base.json`)

Exit 1; pass 9, fail 1, na 0. Check list `CHECK_IDS` at `:282-293`; exit logic `:2235-2237`.

| # | check (impl / spec in docstring) | BASE verdict | BASE detail (evaluated) | after edit |
|---|---|---|---|---|
| 1 | `checklist.box_map_complete` (`:1056-1173` / `:50-66`) | PASS | 41 boxes mapped (8 executed, 0 delegated, 33 unexecuted) (41) | identical |
| 2 | `trigger.frontmatter_parses` (`:1176-1191` / `:67-76`) | PASS | frontmatter parses: name='kotoba-shokunin', description 814 chars (4) | detail now 810 chars |
| 3 | `trigger.name_directory` (`:1194-1206` / `:77-81`) | PASS | name 'kotoba-shokunin' == directory 'kotoba-shokunin' (1) | identical |
| 4 | `trigger.literal_trigger_string` (`:1209-1227` / `:82-86`) | PASS | description carries literal 'Triggers:' (1); source SKILL.md:6 | identical |
| 5 | `trigger.anti_trigger_clause` (`:1230-1248` / `:87-96`) | PASS | exclusion marker 'Anti-triggers' present (1); source SKILL.md:8 | identical |
| 6 | `trigger.line_budget` (`:1251-1272` / `:97-102`) | PASS | 525 lines within budget 600 (from box at line 246) (525) | identical |
| 7 | `trigger.no_placeholder` (`:1275-1292` / `:103-109`) | PASS | no placeholder markers in 481 scanned lines (481) | identical |
| 8 | `trigger.command_binary_resolves` (`:1498-1524`, subjects `:940-1049` / `:110-163`) | PASS | 9 segments; 13 command subject(s) resolve (13) | identical |
| 9 | `trigger.citation_resolves` (`:1431-1451`, resolver `:1295-1318` / `:164-178`) | PASS | 41 repo-rooted citation token(s) resolve from the repo root (41) | identical |
| 10 | `governance.citation_resolves` (`:1454-1495` / `:179-185`) | FAIL | LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve from the checkout; 9 quoted meta-finding(s), 3 schematic token(s) excluded (805) | identical FAIL |

## What the one-line edit moved

Edit: SKILL.md:14 at BASE, `never reach the `<skills>` router — craft here is audit-side, not` becomes `never reach the skills router — craft here is audit-side, not`. Tag moved `38A7` to `E82C`. `git diff --stat`: 1 file, 1 insertion, 1 deletion.

- Verdicts moved: **none**. All 10 statuses and evaluated counts are identical; pass 9 / fail 1 / exit 1 unchanged.
- Detail moved: **only** `trigger.frontmatter_parses`, 814 to 810 chars (−4 = two backticks, `<`, `>`).
- Self-test: 1597 assertions, 0 failures before and after (fixtures only; `verifier:249-251`).

Net: no verdict harm, and no verdict gain. The edit's value is the C2 precondition, which this checker cannot observe.

## Counterexamples and harms

1. **Checkout identity flips verdicts.** A bare clone named `lane` with no fleet parent, pre-mirror run: exit 1, 7 PASS / 3 FAIL. `name 'kotoba-shokunin' != directory 'lane'` (name_directory); `line 515: '../.ufo/reports/round-7/kotoba.md' does not resolve` (SKILL.md:515); governance with 25 unresolved tokens (LOG.md:177, :255, :311, :779, plus 21 more). That output was not saved as an artifact. With the mirror parent in place but the directory still named `lane` (`build/ExecChecklistBaseline.scratchpath.json`): exit 1, 8 PASS / 2 FAIL. The name check alone flips on directory name. Gate runs must come from a checkout named `kotoba-shokunin` under the fleet root; foreign-named runs are not evidence.

2. **The tag is invisible to every check.** BASE carries the tag (SKILL.md:14); after the edit it does not; all 10 verdicts are identical. No check reads tags. `check_frontmatter` (`:1176-1191`) tests presence and non-emptiness only. The literal-trigger and anti-trigger checks (`:1209-1227`, `:1230-1248`) test substrings and quoted spans. The checklist fixtures contain no `<skills>` or `</skills>` (grep: no matches), so `--self-test` cannot catch it either. The plan's C2 "after" state (`plans/round-47.md:31-33`: "live check PASS", "`--self-test` rejects the planted-tag mutation") needs a new check and planted-tag fixtures. The one-line edit alone produces no verdict movement.

3. **The edit makes SKILL.md:151 false (calibration harm).** After the edit, SKILL.md:151 still reads "This file's own description still carries `<skills>`; the repair is planned (`SCORECARD.md` § planned, round 47)." The description no longer carries it. I did not correct the sentence because the assignment limits the edit to one line. Suggested wording for L1, if C2 lands: "This file's own description was repaired in round 47 (C2)." Without it, the integrated SKILL.md records a falsehood. The same sentence states the rule the checker does not enforce: "description ≤1024 chars, no XML tags (Anthropic rule)".

4. **LOG.md:2111 is a true, recorded absence, not a mirror artifact.** The line records that `python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` "exited 2 because the referenced runners are absent". The path is absent in production and in the clone, and production has no `.ufo/round-45/drafts/` directory. The FAIL is factually correct. The gate exempts only same-line double-quoted tokens (`:1398-1402`, `:1419-1421`); this backticked token is not exempt. C3's erratum registry (`plans/round-47.md:34-39`) should pin the exact (file, line, token) record and stay fail-closed for any other unresolved token.

5. **Self-test is blind to the live file.** It runs fixtures only (`verifiers/verify_skill_checklist.py:249-251`; `self_test` at `:1655-2088`). Its 1597/0 result cannot certify SKILL.md in either direction.

## Freshness and calibration notes for L1

- BASE is exit 1, 9 PASS / 1 FAIL, with the FAIL at governance LOG.md:2111. This matches the plan's "Before: checklist `--json` 9 PASS / 1 FAIL" (`plans/round-47.md:37`).
- Run the live gate only from a checkout named `kotoba-shokunin` under the fleet root. Expected at BASE: exit 1, 9/1.
- `plans/round-47.md` is not in the BASE tree (`git ls-tree c61a973b… plans/` lists only `wwkd-round-19-recensus.md` and `wwkd-round-20-interactive.md`). Plan line citations here are to the production working copy.
- `.ufo/round-33/SKILL.md:14` still carries the tag. It is a historical wave artifact and I did not touch it.

## Commands run (exit codes)

| # | command (cwd = scratch lane unless noted) | exit | key output |
|---|---|---|---|
| 1 | `git clone -q --no-hardlinks <prod> …/lane && git checkout -q --detach c61a973b…` | 0 | HEAD `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| 2 | `python3 -B verifiers/verify_skill_checklist.py --help` | 0 | usage lists `--self-test`, `--json` |
| 3 | `… --self-test` (first run, pre-mirror) | 0 | `0 failure(s) over 1597 assertions`; 265 ms wall (cold) |
| 4 | `… --json` (pre-mirror, checkout dir `lane`; not saved) | 1 | pass 7 / fail 3 (counterexample 1) |
| 5 | eval (py): build mirror; check cited `..` targets; hash governed inputs | ok | 48 links, 0 errors; 5/5 targets exist; 6/6 BASE blobs byte-equal to production |
| 6 | grep `\.\./\.\./` in LOG.md, SCORECARD.md, SKILL.md | — | no matches (no three-hop citations) |
| 7 | grep `(?i)xml\|<skills>\|…` in `verifiers/` | — | only cmark-XML comments (`verify_skill_checklist.py:1551-1553`, `:1894-1896`); no tag logic |
| 8 | `… --skill <mirror>/kotoba-shokunin/SKILL.md --json > out/base.json` | 1 | pass 9 / fail 1 / na 0 |
| 9 | `… --json > out/scratchpath-base.json` (dir `lane`, mirror parent present) | 1 | pass 8 / fail 2 |
| 10 | `… --self-test` ×5 (BASE) | 0 ×5 | 1597/0; wall 153.4, 128.8, 124.0, 117.5, 129.6 ms (median 128.8) |
| 11 | `edit` lane SKILL.md:14 (`PUT 14.=14`) | — | tag `38A7` to `E82C`; only change |
| 12 | `git -C lane diff --stat` | 0 | 1 file, 1 insertion, 1 deletion |
| 13 | `git -C lane diff > build/ExecChecklistBaseline.patch` | 0 | 524 B |
| 14 | `… --json > out/after.json` (mirror) | 1 | pass 9 / fail 1 / na 0 |
| 15 | `… --self-test` ×5 (after) | 0 ×5 | 1597/0; wall 114.1, 108.0, 105.5, 108.5, 105.5 ms (median 108.0) |
| 16 | eval (py): per-check diff; copy three JSON artifacts | ok | only `trigger.frontmatter_parses` detail moved |
| 17 | eval (py): `git apply --check -R` on lane; read-tree BASE into temp index + `git apply --cached --check`; compare prod SKILL.md and verifier bytes to BASE | 0 / 0 / 0; True, True | patch reverses on lane and applies to BASE; temp index removed |
| 18 | grep `<skills>\|</skills>` in lane `verifiers/fixtures/checklist` | — | no matches |
| 19 | eval (py, read-only): presence of `.ufo/round-45/drafts/v10/post-r44-hunt.py` | — | absent in production and lane; production `.ufo/round-45/drafts/` absent |
| 20 | grep `<skills>` in lane SKILL.md (post-edit) | — | frontmatter 0; body matches at lines 22, 91, 96, 99, 111, 151, 430 |

## Artifacts and patch

- `.ufo/waves/round-47/build/ExecChecklistBaseline.patch`: 524 B. Reverse-applies on the lane and forward-applies to BASE.
- `.ufo/waves/round-47/build/ExecChecklistBaseline.base.json`: mirror BASE `--json` (2026 B; exit 1; 9/1).
- `.ufo/waves/round-47/build/ExecChecklistBaseline.after.json`: mirror post-edit `--json` (2026 B; exit 1; 9/1).
- `.ufo/waves/round-47/build/ExecChecklistBaseline.scratchpath.json`: control, checkout dir `lane` (2015 B; exit 1; 8/2).

## For the integrator

1. Apply the patch and amend SKILL.md:151 in the same change (counterexample 3).
2. From the fleet `kotoba-shokunin` checkout, run `python3 -B verifiers/verify_skill_checklist.py --json`. Expect exit 1, 9/1, frontmatter detail 810 chars, FAIL only at governance LOG.md:2111.
3. `python3 -B verifiers/verify_skill_checklist.py --self-test` should report `0 failure(s) over 1597 assertions`.

## Tooling record

No tools installed or updated. Used the pre-installed `python3` 3.14.8 and `git`. No subagents and no labrat probe. No jj command ran. No git mutation ran in `kotoba-shokunin`; the only git call against the source repo was `git clone` (read-only).

## Did NOT check

- The C2 check, its fixtures, the C3 erratum registry, and the corpus index: not built (outside this item).
- `verify_surfaces.py`, `check_substrate_pins.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py`, `verify_harness_claims.py`: not run. The omp and opencode substrates (C1) are untouched.
- A direct run against the production path. Equivalence rests on byte-identical inputs and the mirror layout.
- `--check` single-check mode, `--map` and `--vocabulary` overrides, and `delegated:` path behavior.
- Other Python versions, and timing on an idle host. The five-run timings were taken under concurrent sibling load, so treat the millisecond figures as indicative only.
- Whether SKILL.md:151 has other stale wording outside that sentence, or whether SCORECARD "§ planned" wording needs the same update.
- `~/.local/bin/opencode` was never executed and was not needed.
- The pre-mirror run output exists only in the transcript, not as an artifact.
