FAILS as the R4 closure: the appended section is a clean append and most re-run values match, but its coverage claim, one count command, one attribution, and the /fast/scratch provenance do not hold. HOLDS for the append-only property (section 1).

Scope: corpus/knowledge/frontmatter-rule-authorities-round48.md. Master = c48793dbe5eb30cd661f42ecad7399ae94e3d7ad; base a5adc146a2995dcc5a95a6d8db6e5674f75191ac. Working-copy sha256 423b8545... equals `git show c48793db:<path> | sha256sum`; `git status --porcelain -- <path>` is empty. All runs 2026-10-22 UTC. Writes: only /fast/scratch/hyaku/kotoba-r49/falsify/ReviewR4Provenance/ and this report.

## 1. Was anything above the appended section edited? No.
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff a5adc146a2995dcc5a95a6d8db6e5674f75191ac c48793dbe5eb30cd661f42ecad7399ae94e3d7ad -- corpus/knowledge/frontmatter-rule-authorities-round48.md` exit 0: 1 file, 43 insertions, 0 deletions, one hunk `@@ -132,3 +132,46 @@`.
- Python over `git show <rev>:<path>` (exit 0): base 15,311 B, 134 lines; new 21,249 B, 177 lines; new bytes start with all base bytes (True); removed lines 0; added lines 43. Section header is at line 136.

## 2. Re-runs (R4 row line in brackets)
- [16] `curl -sSL -o spec.md -w '%{size_download}\n' https://agentskills.io/specification.md` + sha256sum: 7,608 B, 9a67de89...; match, exit 0.
- [23] same form, best-practices.md: 42,169 B, f0a5d61b...; match, exit 0.
- [133] curl errors.md: 541,573 B, 37e9799a...; `grep -n 'over 256 characters' errors.md`: :5388, :5397; match, exit 0 (but see F4).
- [51] `grep -niE -e reserved -e 'third person' -e xml -e angle -e '500 lines' -e 1024 -e '1,024' -e '64 char' -e lowercase -e hyphen -e consecutive build-skills.md`: no lines, exit 1; match. Widened `-e director -e unknown -e unexpected -e 'additional field'`: 5 hits (md:11, 39, 48, 138, 142), exit 0; match, but "director" matches "directory" in all five, so the widened sweep tests little. build-skills.md 11,035 B, ed6e324f...
- [54] `grep -nE -e dirname -e basename -e parent qv.py`: exit 1; `grep -niE -e 'third person' -e reserved -e lines qv.py`: exit 1; match. qv.py 3,972 B, 67cf5703...
- [56] R4-recorded pattern `grep -niE -e max_lines -e 'body length' -e '500 line' -e line_count validator.py parser.py models.py`: exit 1; match. Body footnote (f) pattern `grep -niE 'third person|reserved|max_lines|line_count|500' validator.py parser.py models.py`: `validator.py:12:MAX_COMPATIBILITY_LENGTH = 500`, exit 0. The body's "→ 0" is wrong; R4 says so. validator.py 5,154 B, b5ee3d85...
- [122] R4 printed count command: 5, exit 0. Value matches; command id set is wrong (F1).
- [90] `grep -cP '^\x7c [a-z]' <(sed -n '40,49p' corpus/knowledge/frontmatter-rule-authorities-round48.md)`: 10, exit 0; match.
- [100] `grep -c '^\*\*O[0-9]' .ufo/waves/round-48/falsify/A12OmittedRules.md`: 6, exit 0; match.
- [24] round-47 copy 42,028 B, 727f3fa1...; match. `diff <round-47 copy> bp.md | grep -cE '^[0-9]+(,[0-9]+)?c'`: 62, exit 0; `...d` form: 0, exit 1. "79/79 lines" is not produced (F8). `wc -l`: 1,191 both.
- [22] glob count: 21; `ls` shows 21 entries.
- [32] `python3 -B /fast/scratch/hyaku/kotoba-r49/seats/R4CountProvenance/counts.py`: probe_files 36, probe_dirs 36, probe_distinct 29, exit 0. The 24 is not reproduced (F2).
- [72-74] s_div.py run from a private copy of A07 (its qv.py byte-identical to pinned, `diff` exit 0): 6/10, 7/10, 3/10; values match (F6).
- [40, 44, 48, 102] nine fixtures I built from one-line specs, qv.py at dbd4588f: 64-char name exit 0; 65-char name exit 1 "Name is too long (65 characters). Maximum is 64 characters."; 1024-char description exit 0; 1025 exit 1; padded 1024 exit 0; compatibility 500 exit 0; 501 exit 1; empty compatibility exit 0; extra key `version` exit 1 listing six allowed names. All match. Lane and skills-ref columns not run.
- Not in R4's table, run anyway: Limits rechecks (curl | grep -c): skills-ref 1, packager 1, Anthropic docs 2, Codex docs 1, all exit 0, all match. Spec: `grep -ciE 'third person' spec.md` 0 (exit 1); `grep -ciE reserved spec.md` 0 (exit 1); `grep -niE 'unknown|unrecognized|additional (field|propert)' spec.md` spec.md:161 only (exit 0). Best practices: `grep -ciE consecutive bp.md` 0 (exit 1); `grep -niE 'unknown field|unrecognized|only these fields' bp.md` 0 (exit 1). All match.
- Pins: `git ls-remote https://github.com/anthropics/skills HEAD` = dbd4588f..., exit 0 (pin is still HEAD). `git ls-remote https://github.com/agentskills/agentskills HEAD` = 69ef37e9..., exit 0.
- Tracking: `git ls-files` lists all 8 cited lane files; `git check-ignore -v` on two of them exit 1 (not ignored).
- Skills page `https://code.claude.com/docs/en/skills.md`: 111,557 B, cdfcb0df...; `grep 256` finds no matches.

Tally: I re-ran 22 of 23 R4 rows (not row 49). 21 of 22 values match; row 32's 24 is the one that does not. R4's "21 of 23 reproduce" is a value tally. It does not test whether each command tests the claim it sits beside (F1, F2, F6).

## 3. Findings, by severity

High
- F1 [122, lane tree; high confidence]. The printed command counts S016-S021. The body's six sources (body line 1, `source:`) are S012, S017, S018, S019, S020, S021. S016 (opencode, https) is counted and S012 (packager, https) is not. The 5 matches by coincidence: the body's six give five https rows (S012, S017, S018, S019, S021), and S020 has no https (python, exit 0). The "five of six read live" claim is true; the command cannot show it. Fix: use the body's six ids.
- F2 [32; high]. "24 probe fixtures, the table's source" (body line 32) is not reproduced. The cited tree holds 36 SKILL.md files in 36 directories with 29 distinct contents. The row's "33 distinct names" is not printed by counts.py. Distinct basenames of those 36 directories is 33 (python, exit 0): right value, command does not print it. R4's disposition says "the cells those counts support are unaffected". R4 did not test that; it is an inference, not a finding. Until a run list is committed, the body's "table's source" claim is unverified.
- F3 [coverage; high]. Intro says "Every count and size above is re-measured here with its command." The table omits the four Limits rechecks (1, 1, 2, 1), the spec and best-practices sweeps in body footnotes (c) and (e), and the hashes ed6e324f..., 67cf5703..., b5ee3d85.... I re-ran the omitted counts and they match, so the values hold. The coverage sentence does not.
- F4 [body lines 132-133 vs R4 row 133; high]. The body attributes the 256-character refusal to "Claude Code's skills page". The skills page I fetched has no "256" and no numeric name cap. "over 256 characters" is at errors.md:5388 and :5397, and the seat's own note C2ClaudeDocs.md:39 cites errors.md:5388. R4's command uses the right URL, but the body sentence still names the wrong page and R4 does not flag it.

Medium
- F5 [56; high]. R4 correctly flags that footnote (f)'s printed pattern gives a hit. Its replacement drops `third person` and `reserved`, two of the five original terms, without saying so. I ran both: exit 1, 0 hits. The "not stated (f)" cells hold, but R4's executed command does not cover them.
- F6 [72-74; medium]. Row 72 is labelled a re-run of the packager's angle rule ("re-runs the ten pairs"). The 6-of-10 and 3-of-10 counts come from s_div.py's own re-implementations (lines 31-33; docstring lines 5-6), not from a packager or docs run. The angle test matches qv.py:79-80 by reading, so the number is faithful. The note "(f02b and f04 emulated)" is not reproduced: the script has no emulation branch, and the packager column (row 73, 7/10) is a real run of a byte-identical qv.py.

Low
- F7 [22]. "(seat F3: 21 skill directories plus the lane copy)": the directory holds 21 entries and none is a lane copy.
- F8 [24]. "79/79 lines" is not produced by the row's command. It is copied from C2ClaudeDocs.md:131. `wc -l` gives 1,191 for both files.
- F9 [90]. Observed cell says "A07's set equals the build seat's, diff -r exit 0". That belongs to rows 33/72; row 90's command never touches A07. The value 10 is right.

## 4. Are /fast/scratch commands acceptable as provenance?
No, not on their own. A path under /fast/scratch is not in the repo and carries no hash manifest, so a reader cannot check it.
- Rows 40, 44, 48, 102: acceptable only with the fixture generator committed. I rebuilt these nine fixtures from one-line specs and got the same verdicts, so this is cheap.
- Rows 33, 72-74: A07 fixtures are 10 SKILL.md files; all files under fixtures/ total 751 bytes. Commit them with a sha256 manifest.
- Row 22: commit the 21 directory names and SKILL.md hashes.
- Row 32: commit the run list, or replace "24" with the measured 36 files / 29 contents (F2).
- Network rows (16, 23, 51, 54, 56, 133): acceptable as dated provenance because each names a URL and sha256. Pinned-commit URLs (skills-ref, packager) are durable. Live docs pages (best-practices, errors, build-skills, skills) are not; rows should say their hashes are a 2026-10-22 snapshot.
- Lane-tree rows (24, 90, 100, 122): acceptable. All cited files are tracked and none is ignored.

## 5. Residual risk and verification gaps
- Not run: row 49 (lane line budget); lane columns of rows 40 and 44; skills-ref `agentskills validate` for rows 40, 44, 48, 102; the A07 `diff -r` against the build seat (build-seat path not located); overview.md sweep (body footnote b); PyPI validator hash 7b5cb3dc...
- Row 32's 24: I found no run list, so I cannot say whether 24 was ever right.
- Live pages can change after 2026-10-22; my values come from one fetch each.
- Confidence: F1, F2, F4 high (direct reproduction). F6 medium (rests on reading the script).

## 6. Tools
None installed or upgraded. Used /usr/bin/curl, sha256sum, python3, diff, git (read-only). No jj commands, no git write commands, no subagents.
