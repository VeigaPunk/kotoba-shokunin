# ExecGovCorrections — round 70 wave 1 (executor)

**Verdict: CONFIRMED.** Both round-70 `GOVERNANCE_CORRECTIONS` rows re-derive byte-exactly from the
LOG.md bytes, and `governance.citation_resolves` fails closed on all three requested arms (one-byte
edit, restored stale path, deleted corrected target) for row 2723. The same three arms on row 2724
also fail closed. The reverted copy returns to PASS.

Lane read at `HEAD` = `16b212a` (the measured tip). `git diff --quiet HEAD -- LOG.md
verifiers/verify_skill_checklist.py` returned 0, so the working tree matches HEAD for both files.
No lane file was modified. All mutations ran in `cp -r` copies under
`/tmp/k70w1-ExecGovCorrections.AgsZ/`, which was deleted afterwards.

## 1. Re-derivation of the rows

The rows are at `verifiers/verify_skill_checklist.py:429-437`, and the horizon is set at
`GOVERNANCE_CORRECTIONS_HORIZON = 2724` on `:415`.

Command (run in the lane, read-only):
`for n in 2723 2724; do sed -n "${n}p" LOG.md | tr -d '\n' | sha256sum; done`, and the same over
`git show HEAD:LOG.md`.

| row | LOG.md line | pinned sha256 | re-derived (worktree and HEAD) | subject | stale → corrected |
|---|---|---|---|---|---|
| 1 | 2723 | `a2b5c003…71535be` | `a2b5c003bd6c4b87ff6cf524924731e1816f1f231c4e64cb3a621bd2e71535be` (match) | LOG.md:2676 | `.ufo/waves/round-67/w1/controls/census-validate-append.txt` → `.ufo/waves/round-67/controls/census-validate-append.txt` |
| 2 | 2724 | `13a858af…236c7589d` | `13a858af8a3740826a1ab47cf4d7e172ec9b046a037009ac7dbf7fd236c7589d` (match) | LOG.md:2678 | `.ufo/waves/round-67/w1/controls/junk-world/` → `corpus/lessons/round-68.md` |

Supporting observations:
- `wc -l LOG.md` returns `2724`, so lines 2723 and 2724 are the last two lines and sit at the horizon.
  The file ends in `0a`, which means the hashed lines are complete lines with the trailing newline
  stripped.
- Each subject line carries its stale token. `grep -c` gave `1` for each of 2676 and 2678.
- In the lane, both stale paths are `absent` and both corrected paths `exist`. Both corrected paths
  are tracked (`git ls-files --error-unmatch` listed both).

## 2. Harness (needed for a /tmp copy to be valid)

- **Control without a parent mirror.** This ran in the bare copy at
  `/tmp/k70w1-ExecGovCorrections.AgsZ/kotoba-shokunin`, using
  `python3 -B verifiers/verify_skill_checklist.py --check governance.citation_resolves --json`.
  - Result: `status FAIL`, `evaluated 1256`, `exit=1`.
  - Detail: the corrected tokens for rows 2619/2620/2621 (`../.ufo/...`) and
    `LOG.md:177 '../.ufo/reports/round-9/kotoba.md'` do not resolve, `… (+30 more)`. The detail also
    shows `2 recorded correction(s) excused`, which are the two round-70 rows.
  - Cause: `citation_resolve` (`:1523-1546`) resolves `../` tokens against the repo's ancestors.
  - This is the sandbox effect recorded as M116 (`corpus/lessons/round-70.md:136`).
- **Fleet mirror.** I symlinked every top-level entry of `/home/vgpnk/Projects/shokunin` except
  `kotoba-shokunin` into the scratch parent (37 entries). The gate only calls `.exists()` on them.
  An intermediate run that symlinked only `.ufo` still FAILed on `../PROTOCOL.md`,
  `../kasegi-shokunin/...` and `../AXES.md` (`+9 more`).
- **Clean control (fleet mirror, unmodified copy).**
  - Result: `status=PASS`, `evaluated=1253`, `exit=0`.
  - Detail: `1253 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s),
    3 schematic token(s) excluded, 1 recorded absence(s) excused, 5 recorded correction(s) excused`.

## 3. Fail-closed arms

Every arm was run from the copy root using
`python3 -B verifiers/verify_skill_checklist.py --check governance.citation_resolves --json`. Each
mutation was reverted before the next arm, and each revert was checked: the LOG.md sha256 matched
the original, `cmp` showed restored targets byte-identical, and the stale path was confirmed absent
again.

| arm | mutation | status / exit | detail (head) |
|---|---|---|---|
| (a) row 2723 | LOG.md:2723 last byte `.`→`;` (length stays 239; line sha becomes `8a5e85d4…bef3b`) | FAIL / 1 | `correction LOG.md:2723 LOG.md:2676 '.ufo/waves/round-67/w1/controls/census-validate-append.txt': line text drifted; LOG.md:2676: '…/w1/controls/census-validate-append.txt' does not resolve …; 4 recorded correction(s) excused` |
| (b) row 2723 | created `.ufo/waves/round-67/w1/controls/census-validate-append.txt` (a copy of the corrected file) | FAIL / 1 | `correction LOG.md:2723 LOG.md:2676 '…/w1/controls/census-validate-append.txt': stale, the old token now resolves; … 4 recorded correction(s) excused` |
| (c) row 2723 | moved away `.ufo/waves/round-67/controls/census-validate-append.txt` | FAIL / 1 | `correction LOG.md:2723 …: corrected token '.ufo/waves/round-67/controls/census-validate-append.txt' does not resolve; LOG.md:2641: … does not resolve; LOG.md:2676: … does not resolve; LOG.md:2677: … does not resolve … (+1 more)` |
| (a) row 2724 | LOG.md:2724 last byte `.`→`;` (length stays 235) | FAIL / 1 | `correction LOG.md:2724 LOG.md:2678 '.ufo/waves/round-67/w1/controls/junk-world/': line text drifted; LOG.md:2678: '…/junk-world/' does not resolve …` |
| (b) row 2724 | `mkdir -p .ufo/waves/round-67/w1/controls/junk-world` | FAIL / 1 | `correction LOG.md:2724 …: stale, the old token now resolves; …` |
| (c) row 2724 | moved away `corpus/lessons/round-68.md` | FAIL / 1 | `correction LOG.md:2724 …: corrected token 'corpus/lessons/round-68.md' does not resolve; LOG.md:2660/2666/2674: … does not resolve … (+1 more)` |
| control-after | all arms reverted | PASS / 0 | `1253 … resolve …; 5 recorded correction(s) excused` |

Reading the results:
- In each arm the row stops excusing its subject: the excused count drops from 5 to 4.
- In arms (a) and (c), the stale subject also re-surfaces as an independent `does not resolve`
  problem. So a broken row never silently keeps its subject excused.
- In arm (b), the row problem is the only FAIL cause, because the stale token now resolves.
- The arm detail strings match the branch order in `correction_problems`
  (`verify_skill_checklist.py:1708-1743`): horizon → sha drift → wording → live subject →
  stale-resolves → corrected-resolves.

## Risks / notes

- **Sandbox validity depends on the fleet mirror.** A bare `/tmp` copy FAILs this check for reasons
  unrelated to these rows. This is consistent with M116. Any seat repeating this proof needs the
  same sibling-entry mirror. The symlinks are read-only in use, since the gate only calls `exists()`.
- **Unobserved.**
  - I did not exercise a past-horizon arm, for example appending a line that shifts the rows' line
    numbers, or editing a line above 2723.
  - I did not exercise a wording-not-on-line arm separately from a sha change. A wording edit also
    changes the sha, so the drift branch fires first and the wording branch cannot be reached
    without a forged digest.
- **No tools were installed or updated.**
