# ScoutW2ReceiptPaths — round-64 evidence-pointer falsification

Measured revision: `c019919c97ab5fe98e87a7754b4449ea4e699c99`. Scout: `kotoba-r64.ScoutW2ReceiptPaths-2`.

Axes: extraction completeness; exact-revision resolvability; separation of committed, worktree-only, external, and non-path tokens. Read-only outside this requested report; no production/index/jj writes, tool installs, builds, tests, linters, census runs, or no-harm runs.

## Findings (observed unless labelled)

**55 distinct normalized objects checked: 45 EXIST, 10 ABSENT at c019919c.** The 10 include an intentional glob, a fleet-relative command, a printed fixture path, and a supplemental later no-harm receipt; they are not 10 distinct missing-evidence defects. Every absent `.ufo` object was additionally checked with `ls -ld`.

1. **F1 — missing after-census evidence (high confidence).** `LOG.md:2606` claims “after 16 W04 exit 0” and points to `census-after.txt`; `corpus/lessons/round-64.md:52` supplies `.ufo/waves/round-64/census-after.txt`. `git cat-file -e` exits **128** and `ls -ld` exits **2**. The lesson still says “round end; appended below when run”. The existing `w1/ExecCensusAfter.md:25-37,63` explicitly records the **117-row round-start**, not the claimed 118-row after-census. [INFERENCE] That runbook is not a substitute for the missing after evidence. This is an actual round-64 M95-class dead evidence pointer.

2. **F2 — missing named no-harm baseline receipt (high confidence).** `LOG.md:2610` names `.ufo/waves/round-64/controls/noharm-base.txt`; cat-file exits **128**, disk ls exits **2**. A real alternate baseline record exists at committed `.ufo/waves/round-64/w1/ExecNoHarmBase.md:29-71`; the LOG does not cite that path in place of the absent receipt. This is another actual round-64 M95-class dead evidence pointer, not proof that no baseline was ever measured.

3. **F3 — receipt storage revision differs from the measured revision (high confidence).** The directory `.ufo/waves/round-64/receipts/` and `C1-span-measure.txt`, `C1-span-kill.txt`, `C2-r64-measure.txt` are **ABSENT at c019919c (128)**. All **EXIST on disk (ls 0)**, satisfying the assignment's worktree-only existence allowance but not a frozen-revision citation. They are evidence pointers in `LOG.md:2602-2603,2610`, `corpus/knowledge/g7-span-pinning-round64.md:5`, and the worktree SCORECARD annotation. Each resolves at later revision **b99fb79c (cat-file 0)**. [INFERENCE] Citing c019919c as the revision containing those receipts repeats the class this round teaches; cite the containing revision separately from the revision measured. This is not an allegation of fabricated receipt bytes.

4. **F4 — the requested SCORECARD round-64 annotation is not in the measured tree (high confidence).** `SCORECARD.md` itself exists at c019919c, but its last line is the round-63 annotation at line 373; the exact round-64 heading has **0 matches** in the successful `git show`. The requested annotation is present at worktree line 375 and explicitly names c019919c. I extracted its pointers as **worktree-only supplemental input**, never as c019919c bytes. Thus the complete requested artifact set is not co-located at the frozen measurement revision.

5. **F5 — external-command location, not missing lane evidence (high confidence).** Lesson line 51 spells `scripts/sources-census.sh`; the literal lane-relative object is absent at c019919c. The script exists at `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (ls 0), and `w1/ExecCensusAfter.md:12` uses that absolute path. [INFERENCE] The lesson's bare command is fleet-cwd-dependent; this is an operability ambiguity, not a missing measured receipt.

**Other ABSENT tokens, disclosed without false-positive M95 attribution:** `corpus/lessons/round-6*` is deliberately a pattern (all 11 matches below exist); `.ufo/waves/round-60/snapshots/S900.page` appears only inside the W6 self-test stdout diagnostic, not as a standalone evidence link; `.ufo/waves/round-64/receipts/noharm-tip.txt` is supplemental worktree input and explicitly names later tip `b99fb79c27042e0f8a598cbbb4d81479a806b518`. [INFERENCE] The W6 token is a synthetic-fixture pathname; I did not investigate its lifecycle or treat it as a source snapshot citation.

## Scope, extraction and command contract

Frozen inputs were materialized with `git show c019919c97ab5fe98e87a7754b4449ea4e699c99:<path>` (each successful): LOG lines 2590–2610 (round-64 corrections block plus entry), the full lesson, and the full knowledge entry. SCORECARD was fetched successfully but has no r64 annotation, so its observed worktree annotation was separately captured. No receipt directory exists in the frozen tree; all four observed worktree receipt bodies were scanned, with origin explicitly retained. The two committed before-controls and census-before receipt were also scanned to close the local evidence graph. Read required wave-1 `ScoutReceiptSweep.md` and relevant `ExecReceiptTemplates.md` sections; consulted `ExecNoHarmBase.md` / `ExecCensusAfter.md` to disambiguate two missing pointers.

Extraction retains tokens containing a slash or apparent file extension, excludes URLs/DOIs/MIME types/numeric ratios/labels/absolute paths from the repo-relative set, strips only line/fragment suffixes and terminal punctuation, and expands basenames with their stated round/directory context. The four `C1-measure.txt` uses at LOG:2596 are resolved separately to rounds 56–59, not opportunistically to any existing basename. `noharm-battery.sh` is resolved to the r62 path specifically named by the committed baseline seat. Directories are tested without the terminal slash. The deliberate lesson glob is tested literally **and** expanded against the frozen tree. A second conservative lexical pass retaining numeric starts and leading slashes found only excluded boundary cases listed below.

Every row is the observed exit status of the exact command:

```sh
git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:<normalized-path>
```

`EXIST (0)` has empty stdout/stderr. `ABSENT (128)` stderr is pasted below. Disk status is the actual `ls -ld -- <path>` result for each absent `.ufo` object, not an inferred `stat` result. `—` means disk checking was unnecessary, not absent. Source artifacts, pattern expansions, and three provenance reports are included so the table is a superset of requested pointers. No code definitions/callers or exported contracts were changed or semantically audited; LSP tracing was not applicable to this document/object-existence question.

### Source key

- `L` = frozen LOG.md; `T` = frozen corpus/lessons/round-64.md; `K` = frozen corpus/knowledge/g7-span-pinning-round64.md.
- `S-WT` = worktree SCORECARD.md r64 annotation (absent from frozen file).
- `R1-WT`, `RK-WT`, `R2-WT`, `RN-WT` = worktree receipts C1-span-measure, C1-span-kill, C2-r64-measure, noharm-tip respectively.
- `B1`, `B2`, `CB` = frozen C1-before control, C2-before control, census-before receipt.

## Full object table

| normalized repo-relative object | original token(s) | citation locations | at c019919c | disk fallback | note |
|---|---|---|---|---|---|
| `.ufo/round-46/evidence/w2/gates/before-78ee57e/summary.txt` | `before-78ee57e/summary.txt` | L:2596 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-55/C2-measure-e966cd59.txt` | `C2-measure-e966cd59.txt` | L:2596 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-56/C1-measure.txt` | `C1-measure.txt` | L:2596 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-57/C1-measure.txt` | `C1-measure.txt` | L:2596 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-58/C1-measure.txt` | `C1-measure.txt` | L:2596 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-58/noharm-tip.txt` | `noharm-tip.txt` | L:2596 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-59/C1-measure.txt` | `C1-measure.txt` | L:2596 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-60/snapshots/S900.page` | `.ufo/waves/round-60/snapshots/S900.page` | R1-WT:9 | ABSENT (128) | ABSENT (2) | printed W6 fixture diagnostic; not a standalone evidence citation |
| `.ufo/waves/round-62/C1-absorb-measure.txt` | `C1-absorb-measure.txt` | L:2596 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-62/noharm-battery.sh` | `noharm-battery.sh` | L:2609 | EXIST (0) | — | noharm-battery.sh expanded via committed ExecNoHarmBase.md:11-26 |
| `.ufo/waves/round-63/controls` | `.ufo/waves/round-63/controls/` | L:2604 | EXIST (0) | — |  |
| `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` | `C1-do-nothing-v31.txt` | L:2604; T:59 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-63/controls/C2-before-r62tip.txt` | `C2-before-r62tip.txt` | L:2604; T:60 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-63/receipts/C1-g9-measure.txt` | `.ufo/waves/round-63/receipts/C1-g9-measure.txt`, `C1-g9-measure.txt` | L:2597; S-WT:375; T:98 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-63/w2/ExecW2E2Patch.md` | `ExecW2E2Patch.md` | L:2595 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-63/w2/MutW2SplitClauses.md` | `.ufo/waves/round-63/w2/MutW2SplitClauses.md` | L:2592; L:2601 | EXIST (0) | — |  |
| `.ufo/waves/round-63/w2/MutW2V32.md` | `.ufo/waves/round-63/w2/MutW2V32.md`, `MutW2V32.md` | K:1; K:37 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-64/census-after.txt` | `.ufo/waves/round-64/census-after.txt`, `census-after.txt` | L:2606; T:52 | ABSENT (128) | ABSENT (2) | F1: cited completed after-census record, missing everywhere checked |
| `.ufo/waves/round-64/census-before.txt` | `.ufo/waves/round-64/census-before.txt`, `census-before.txt` | L:2606; T:50 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-64/controls` | `.ufo/waves/round-64/controls/` | L:2610 | EXIST (0) | — |  |
| `.ufo/waves/round-64/controls/C1-before.txt` | `.ufo/waves/round-64/controls/C1-before.txt`, `C1-before.txt` | L:2602; L:2610; S-WT:375 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-64/controls/C2-before.txt` | `.ufo/waves/round-64/controls/C2-before.txt`, `C2-before.txt` | L:2603; L:2610 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-64/controls/noharm-base.txt` | `noharm-base.txt` | L:2610 | ABSENT (128) | ABSENT (2) | F2: named baseline record, missing everywhere checked |
| `.ufo/waves/round-64/receipts` | `.ufo/waves/round-64/receipts/` | L:2610 | ABSENT (128) | EXIST (0) | F3: directory only committed later (exists in b99fb79c) |
| `.ufo/waves/round-64/receipts/C1-span-kill.txt` | `.ufo/waves/round-64/receipts/C1-span-kill.txt`, `C1-span-kill.txt` | L:2602; L:2610; S-WT:375; source artifact | ABSENT (128) | EXIST (0) | F3: cited at measured tip; exists in b99fb79c |
| `.ufo/waves/round-64/receipts/C1-span-measure.txt` | `.ufo/waves/round-64/receipts/C1-span-measure.txt`, `C1-span-measure.txt` | L:2602; L:2610; S-WT:375; K:5; source artifact | ABSENT (128) | EXIST (0) | F3: cited at measured tip; exists in b99fb79c |
| `.ufo/waves/round-64/receipts/C2-r64-measure.txt` | `.ufo/waves/round-64/receipts/C2-r64-measure.txt`, `C2-r64-measure.txt` | L:2603; L:2610; S-WT:375; source artifact | ABSENT (128) | EXIST (0) | F3: cited at measured tip; exists in b99fb79c |
| `.ufo/waves/round-64/receipts/noharm-tip.txt` | `.ufo/waves/round-64/receipts/noharm-tip.txt` | source artifact | ABSENT (128) | EXIST (0) | supplemental disk-only receipt itself names tip b99fb79c |
| `.ufo/waves/round-64/snapshots/S120.page` | `.ufo/waves/round-64/snapshots/S120.page`, `S120.page` | K:1; T:22 | EXIST (0) | — | context/suffix expansion |
| `.ufo/waves/round-64/w1/ExecCensusAfter.md` | `.ufo/waves/round-64/w1/ExecCensusAfter.md` | after-census provenance | EXIST (0) | — | supplemental runbook; reports 117-row round-start, not after-census |
| `.ufo/waves/round-64/w1/ExecNoHarmBase.md` | `.ufo/waves/round-64/w1/ExecNoHarmBase.md` | noharm-base provenance | EXIST (0) | — | supplemental existing baseline provenance |
| `.ufo/waves/round-64/w1/ScoutReceiptSweep.md` | `.ufo/waves/round-64/w1/ScoutReceiptSweep.md` | prior sweep read | EXIST (0) | — | required prior-seat context |
| `LOG.md` | `LOG.md` | L:2596; T:157; T:67; T:89; source artifact | EXIST (0) | — |  |
| `SCORECARD.md` | `SCORECARD.md` | L:2596; K:116; source artifact | EXIST (0) | — | file exists; F4: round-64 annotation absent from this version |
| `corpus/SOURCES.md` | `corpus/SOURCES.md` | T:49 | EXIST (0) | — |  |
| `corpus/knowledge/g7-span-pinning-round64.md` | `corpus/knowledge/g7-span-pinning-round64.md` | source artifact | EXIST (0) | — |  |
| `corpus/lessons/round-6*` | `corpus/lessons/round-6*` | L:2596 | ABSENT (128) | — | intentional glob, not a literal object; its 11 matches are individually checked |
| `corpus/lessons/round-6-aggregator-audit.md` | `corpus/lessons/round-6*` | L:2596 [pattern expansion] | EXIST (0) | — | intentional pattern expansion |
| `corpus/lessons/round-6.md` | `corpus/lessons/round-6*` | L:2596 [pattern expansion] | EXIST (0) | — | intentional pattern expansion |
| `corpus/lessons/round-60-verifier-spotcheck.md` | `corpus/lessons/round-6*` | L:2596 [pattern expansion] | EXIST (0) | — | intentional pattern expansion |
| `corpus/lessons/round-60.md` | `corpus/lessons/round-6*` | L:2596 [pattern expansion] | EXIST (0) | — | intentional pattern expansion |
| `corpus/lessons/round-61-verifier-spotcheck.md` | `corpus/lessons/round-6*` | L:2596 [pattern expansion] | EXIST (0) | — | intentional pattern expansion |
| `corpus/lessons/round-61.md` | `corpus/lessons/round-6*` | L:2596 [pattern expansion] | EXIST (0) | — | intentional pattern expansion |
| `corpus/lessons/round-62-verifier-spotcheck.md` | `corpus/lessons/round-6*`, `corpus/lessons/round-62-verifier-spotcheck.md` | RN-WT:11; L:2596 [pattern expansion] | EXIST (0) | — | intentional pattern expansion |
| `corpus/lessons/round-62.md` | `corpus/lessons/round-6*` | L:2596 [pattern expansion] | EXIST (0) | — | intentional pattern expansion |
| `corpus/lessons/round-63-verifier-spotcheck.md` | `corpus/lessons/round-6*`, `corpus/lessons/round-63-verifier-spotcheck.md` | RN-WT:11; L:2596 [pattern expansion]; T:58 | EXIST (0) | — | intentional pattern expansion |
| `corpus/lessons/round-63.md` | `corpus/lessons/round-6*` | L:2596 [pattern expansion] | EXIST (0) | — | intentional pattern expansion |
| `corpus/lessons/round-64.md` | `corpus/lessons/round-6*`, `corpus/lessons/round-64.md` | L:2592; L:2596 [pattern expansion]; source artifact | EXIST (0) | — | intentional pattern expansion |
| `plans/round-64.md` | `plans/round-64.md` | K:127; T:13; T:69 | EXIST (0) | — |  |
| `scripts/sources-census.sh` | `scripts/sources-census.sh` | T:51 | ABSENT (128) | — | F5: fleet-relative command, not a lane object; external absolute script exists |
| `verifiers/check_r63_routed_repairs.py` | `verifiers/check_r63_routed_repairs.py` | T:134 | EXIST (0) | — |  |
| `verifiers/check_r64_routed_repairs.py` | `verifiers/check_r64_routed_repairs.py` | L:2603; S-WT:375 | EXIST (0) | — |  |
| `verifiers/check_scoped_rules_v31.py` | `verifiers/check_scoped_rules_v31.py` | B1:10 | EXIST (0) | — |  |
| `verifiers/check_scoped_rules_v32.py` | `check_scoped_rules_v32.py`, `verifiers/check_scoped_rules_v32.py` | B1:2; R1-WT:2; L:2602; S-WT:375; K:1; K:11; K:121; K:122; K:2; K:3; K:70; T:153 | EXIST (0) | — | context/suffix expansion |
| `verifiers/floors-registry.json` | `floors-registry.json` | T:153 | EXIST (0) | — | context/suffix expansion |

## Exact failed-command and fallback output

```text
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-60/snapshots/S900.page
fatal: path '.ufo/waves/round-60/snapshots/S900.page' does not exist in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
[exit 128]
$ ls -ld -- .ufo/waves/round-60/snapshots/S900.page
ls: cannot access '.ufo/waves/round-60/snapshots/S900.page': No such file or directory
[exit 2]
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/census-after.txt
fatal: path '.ufo/waves/round-64/census-after.txt' does not exist in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
[exit 128]
$ ls -ld -- .ufo/waves/round-64/census-after.txt
ls: cannot access '.ufo/waves/round-64/census-after.txt': No such file or directory
[exit 2]
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/controls/noharm-base.txt
fatal: path '.ufo/waves/round-64/controls/noharm-base.txt' does not exist in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
[exit 128]
$ ls -ld -- .ufo/waves/round-64/controls/noharm-base.txt
ls: cannot access '.ufo/waves/round-64/controls/noharm-base.txt': No such file or directory
[exit 2]
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/receipts
fatal: path '.ufo/waves/round-64/receipts' exists on disk, but not in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
[exit 128]
$ ls -ld -- .ufo/waves/round-64/receipts
drwxr-xr-x 1 vgpnk vgpnk 134 Oct 24 01:05 .ufo/waves/round-64/receipts
[exit 0]
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/receipts/C1-span-kill.txt
fatal: path '.ufo/waves/round-64/receipts/C1-span-kill.txt' exists on disk, but not in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
[exit 128]
$ ls -ld -- .ufo/waves/round-64/receipts/C1-span-kill.txt
-rw-r--r-- 1 vgpnk vgpnk 1539 Oct 24 01:05 .ufo/waves/round-64/receipts/C1-span-kill.txt
[exit 0]
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/receipts/C1-span-measure.txt
fatal: path '.ufo/waves/round-64/receipts/C1-span-measure.txt' exists on disk, but not in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
[exit 128]
$ ls -ld -- .ufo/waves/round-64/receipts/C1-span-measure.txt
-rw-r--r-- 1 vgpnk vgpnk 2088 Oct 24 01:04 .ufo/waves/round-64/receipts/C1-span-measure.txt
[exit 0]
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/receipts/C2-r64-measure.txt
fatal: path '.ufo/waves/round-64/receipts/C2-r64-measure.txt' exists on disk, but not in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
[exit 128]
$ ls -ld -- .ufo/waves/round-64/receipts/C2-r64-measure.txt
-rw-r--r-- 1 vgpnk vgpnk 570 Oct 24 01:04 .ufo/waves/round-64/receipts/C2-r64-measure.txt
[exit 0]
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/receipts/noharm-tip.txt
fatal: path '.ufo/waves/round-64/receipts/noharm-tip.txt' exists on disk, but not in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
[exit 128]
$ ls -ld -- .ufo/waves/round-64/receipts/noharm-tip.txt
-rw-r--r-- 1 vgpnk vgpnk 1144 Oct 24 01:18 .ufo/waves/round-64/receipts/noharm-tip.txt
[exit 0]
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:corpus/lessons/round-6*
fatal: path 'corpus/lessons/round-6*' does not exist in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
[exit 128]
$ git cat-file -e c019919c97ab5fe98e87a7754b4449ea4e699c99:scripts/sources-census.sh
fatal: path 'scripts/sources-census.sh' does not exist in 'c019919c97ab5fe98e87a7754b4449ea4e699c99'
[exit 128]
```

### Later-revision / external-location controls

```text
$ git cat-file -e b99fb79c:.ufo/waves/round-64/receipts/C1-span-measure.txt
[stdout empty; exit 0]
$ git cat-file -e b99fb79c:.ufo/waves/round-64/receipts/C1-span-kill.txt
[stdout empty; exit 0]
$ git cat-file -e b99fb79c:.ufo/waves/round-64/receipts/C2-r64-measure.txt
[stdout empty; exit 0]
$ git cat-file -e b99fb79c:.ufo/waves/round-64/receipts
[stdout empty; exit 0]
$ ls -ld -- /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
-rwxr-xr-x 1 vgpnk vgpnk 35466 Oct 19 21:22 /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
[exit 0]
```

## Excluded lexical tokens (not repo-relative evidence paths)

| token | reason | locations |
|---|---|---|
| `.md` | extension mentioned in an external URL control, not a file | T:46 |
| `ADMIT/REJECT` | verdict pair | T:92 |
| `B1/B2` | checkbox labels | T:100 |
| `E1.1/E2` | errata labels | T:89 |
| `E1.2/E2.4` | errata labels | T:90 |
| `E1/E2` | errata labels | L:2603; S-WT:375 |
| `F5/F6` | finding labels | T:99 |
| `LOG/SCORECARD` | document labels; LOG.md and SCORECARD.md are separately checked | T:12 |
| `M8/M12` | mutant labels | T:94 |
| `SM4/SM6` | mutant labels | L:2602; S-WT:375; T:147; K:5 |
| `True/False` | boolean pair | K:63 |
| `agentskills.io/specification` | external URL without scheme in diagnostic stdout | CB:1 |
| `calibration/consistency` | axis names | L:2605 |
| `code.claude.com/docs/en/hooks.md` | external URL without scheme in diagnostic stdout | CB:12 |
| `code.claude.com/docs/en/memory.md` | external URL without scheme in diagnostic stdout | CB:9; CB:16 |
| `code.claude.com/docs/en/skills.md` | external URL without scheme in diagnostic stdout | CB:7 |
| `code.visualstudio.com/docs/agent-customization/agent-skills` | external URL without scheme in diagnostic stdout | CB:5 |
| `corpus.index.unindexed` | diagnostic identifier | RN-WT:10 |
| `cursor.com/docs/rules` | external URL without scheme in diagnostic stdout | CB:15 |
| `developers.openai.com/plugins/build/plugins.md` | external URL without scheme in diagnostic stdout | CB:8 |
| `docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` | external URL without scheme in diagnostic stdout | CB:11; CB:14 |
| `docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference` | external URL without scheme in diagnostic stdout | CB:6 |
| `home/vgpnk/Projects/shokunin` | absolute filesystem path, not repo-relative (leading / was lexical delimiter) | T:51 |
| `home/vgpnk/Projects/shokunin/kotoba-shokunin` | absolute filesystem path, not repo-relative (leading / was lexical delimiter) | RN-WT:1 |
| `home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md` | absolute filesystem path, not repo-relative (leading / was lexical delimiter) | CB:17 |
| `learn.chatgpt.com/docs/agent-configuration/agents-md.md` | external URL without scheme in diagnostic stdout | CB:10 |
| `learn.chatgpt.com/docs/build-skills` | external URL without scheme in diagnostic stdout | CB:3; CB:4 |
| `learn.chatgpt.com/docs/hooks.md` | external URL without scheme in diagnostic stdout | CB:13 |
| `lowest/depth/consistency` | counter match labels | B2:3 |
| `over/under-flag` | ordinary prose | T:101 |
| `platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices` | external URL without scheme in diagnostic stdout | CB:2 |
| `sib_M1..M8` | mutant range | K:90 |
| `text/html` | MIME type | T:20 |
| `text/markdown` | MIME type | T:44 |
| `tmp/kotoba-r62-noharm.F4Ix1g` | absolute filesystem path, not repo-relative (leading / was lexical delimiter) | RN-WT:4 |

Additional conservative-pass boundary cases: `/` is a prose separator; `/rules` is an elided external URL control; `10.1109/ICSE43902.2021.00068` and `10.1109/TSE.2021.3107634` are DOI identifiers; `20/19`, `229/230`, `32/32`, `41+/13-`, `82+/29-` are ratios/numstats. The four leading-`/` filesystem paths are the already-excluded absolute paths above, not extra lane-relative paths.

## Confidence, remaining gaps, and tooling

- **Confidence:** high for all object-existence and disk statuses, because every table row was exercised with the requested binary command; high for the missing frozen SCORECARD section from the materialized file. Temporal provenance of later receipts is not assumed from worktree presence: b99fb79c containment was checked explicitly.
- **Unresolved:** source receipt authenticity, assertion/kill semantics, future/other-revision after-census results, and the lifecycle of the W6 synthetic fixture are outside this path-only seat. No inference that a command was never run follows merely from its named receipt being absent. Later lane changes cannot retroactively add objects to c019919c.
- **Installs/updates:** none. The requested `/home/vgpnk/Projects/shokunin/.omp/agent/RULES.md` read returned “Path … not found”; no installation was attempted and the host-wide pacman pause was respected.
- **Verification exercised:** only read-only Git object listing/materialization/existence checks, document token extraction, and requested ls fallbacks. No counts, self-tests, mutation runs, no-harm battery or census was re-run by this path seat.
