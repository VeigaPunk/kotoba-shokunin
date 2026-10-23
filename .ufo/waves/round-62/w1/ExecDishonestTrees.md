# ExecDishonestTrees — routed-repairs calibration

Date: 2026-10-23. Scope: construct D1–D6 and H1 as path→blob maps, score them with the assigned `check_repairs`, and score H2 from the measured dispatch-tip tree. No lane/fleet/git/jj mutation was performed; only this report was written in the lane. Scratch scorer: `/fast/scratch/hyaku/kotoba-r62/ExecDishonestTrees/score_trees_final.py` (scratch is not evidence).

## Source and successor availability

- Imported `check_repairs` from `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py`. Its SHA-256 at the assigned dispatch tip and at import time was `95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88`. The imported function is the six R-a–R-f checks in the source lines 71–119; it was not edited.
- Direct read of `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/w1/ExecSuccessorC2.md` returned “not found”; the w1 directory listing also did not contain it. Per assignment, **no successor scores are claimed**; all scores below are frozen-counter scores only.
- Identity caveat: ExecC2Audit §1 records whole-file SHA-256 `9ee77d47…` for its then-current copy; the assigned path at dispatch tip `45a7ecfac9e203297f3146c45d63f5e79367470c` is `95ade9be…`. I imported the requested path (whose hash matches the dispatch-tip blob), without substituting a historical copy. If “frozen” is intended to mean the audit report’s whole-file hash rather than the assigned dispatch-tip file, this hash delta needs L1 reconciliation; the score evidence here is for the requested path.

## Constructed maps

The six checks read exactly the five keys shown below. Common positive-control blobs are literal excerpts of the round-61 committed repairs; each D/H map is a Python dictionary literal with only its named defect overridden. H2 is the actual measured-tip map: each value is the complete decoded blob at the given commit/path, obtained with `git show`, not a synthetic replacement.

```python
R_A_GOOD = """- R-a erratum: the round-60 report's build wave claimed \"32 reports, 0 dead\"; the committed count is `committed 29` build reports — `ls .ufo/waves/round-60/build | grep -cE '^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\\.md$'` prints 29 at the r60 close commit (claimed 32; 59/65 seat reports overall per the closure) — one line carrying build reports, claimed 32, committed 29, and the counting path `.ufo/waves/round-60/build`."""
R_B_GOOD = """- R-b landed scope (complete list): plans/round-61.md, plans/round-60.md (r60 work, omitted from the r60 report — named here per the closure), considerthese/2026-10-23.md (same), verifiers/check_scoped_rules.py (v3), verifiers/fixtures/scoped-rules/, verifiers/check_routed_repairs.py, corpus/SOURCES.md (S112-S115, S117), corpus/knowledge/scoped-rules-counter-round61.md, corpus/knowledge/writing-revision-calibration-round61.md, corpus/lessons/round-61.md, corpus/QUALITY.md (Q56), corpus/README.md, SKILL.md (registry rows/annotation), .ufo/waves/round-61/ (snapshots, receipts, controls, noharm-battery.sh, wave reports)."""
R_C_GOOD = """- R-c erratum: the r60 base measurement (base `31092dc6`, exit 1) is committed at `.ufo/waves/round-60/receipts/freeze2-selftest.txt`, NOT in `.ufo/waves/round-60/C1-measure.txt` (after-only, both runs at `7b80ae80`) — the r60 report's joint citation conflated them."""

QUALITY_GOOD = """| Q56 | Reserve `byte-exact` for literal byte-for-byte equality between the recorded quote and the cited source bytes; when an HTML-entity escape or whitespace normalization is required, describe the result as `quote-equal after documented shaping`, never `byte-exact`. | report, lesson, and knowledge-entry descriptions of quote/source equality | M91 `report-evidence-overclaim` (`corpus/lessons/round-61.md` § Mistakes); round-60 verifier spot-check §7 defect 5 (`corpus/lessons/round-60-verifier-spotcheck.md:129-132`). | —
"""
LESSON_GOOD = """## Mistakes

- **M91 — class: self-assessment overstatement** · The round-60 report's “32 reports, 0 dead” claim conflicts with the closure's count of 29 committed build reports (59/65 seat reports overall); its joint citation also points at `C1-measure.txt` for a base measurement committed in `receipts/freeze2-selftest.txt` (`corpus/lessons/round-60-verifier-spotcheck.md`, §7 defects 2–3). · captured-by: none — no committed-bytes count guarded report claims before this round · fix: the R-a/R-c patterns in `verifiers/check_routed_repairs.py` correct the committed-report count with its counting path and name the precise base-measurement pointer · shown able to fail: the base control reports `routed repairs verified 0 of 6`, exit 1.
"""
CENSUS_GOOD = """kotoba\tW04\tS018 duplicate url agentskills.io/specification across scopes
kotoba\tW04\tS019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba\tW04\tS021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba\tW04\tS054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba\tW04\tS055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba\tW04\tS056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba\tW04\tS065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba\tW04\tS086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba\tW04\tS103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba\tW04\tS104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba\tW04\tS106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba\tW04\tS110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba\tW04\tS111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba\tW04\tS114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba\tW04\tS115 duplicate url cursor.com/docs/rules across scopes
kotoba\tok\t/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
"""
ANCESTRY_GOOD = """# Round-61 controls-ancestry receipt (R-f)
# date -u: 2026-10-23T20:34:25Z (receipt v2 — the command lines themselves are recorded, not only their output)
# C_CTL (control-receipts commit, carries .ufo/waves/round-61/receipts/C1-worlds.txt + controls/C1-base.txt) = b4a8d2ee79a6190cf5ece5d11395544876e1fc8a
# C_DATA (C1 data commit) = 43fe01804708d65e53965b4be31e9dc7dce793e4
# Claim (DAG chronology ONLY — not wall-clock dispatch order): C_CTL is a STRICT ANCESTOR of C_DATA.
# Both commits: author+committer kotoba-shokunin <kotoba@shokunin.local>.
#
# C_CTL b4a8d2ee79a6190cf5ece5d11395544876e1fc8a round-61: C1-worlds receipt summary ends each world line at exit 1 (counted-set grep now prints 7)
# C_DATA 43fe01804708d65e53965b4be31e9dc7dce793e4 round-61: C1 data commit — S112-S115+S117 SOURCES rows, snapshots, v3 knowledge entry, writing-revision entry, lesson (M91/M92, Gate, status log), Q56, README rows, SKILL v3 annotation, LOG round-61 entry (R-a/R-b/R-c lines)
# distinctness test:
#   $ test \"b4a8d2ee79a6190cf5ece5d11395544876e1fc8a\" != \"43fe01804708d65e53965b4be31e9dc7dce793e4\"
#   exit 0 (hashes differ)
# strict-ancestor test:
#   $ git merge-base --is-ancestor b4a8d2ee79a6190cf5ece5d11395544876e1fc8a 43fe01804708d65e53965b4be31e9dc7dce793e4
exit 0
# merge-base prints C_CTL itself:
#   $ git merge-base b4a8d2ee79a6190cf5ece5d11395544876e1fc8a 43fe01804708d65b4be31e9dc7dce793e4
b4a8d2ee79a6190cf5ece5d11395544876e1fc8a
# controls receipt file present at C_CTL:
#   $ git cat-file -e :.ufo/waves/round-61/receipts/C1-worlds.txt
exit 0
"""
COMMON = {
    "LOG.md": "## Synthetic C2 fixture\\n" + R_A_GOOD + "\\n" + R_B_GOOD + "\\n" + R_C_GOOD + "\\n",
    "corpus/QUALITY.md": QUALITY_GOOD,
    "corpus/lessons/round-61.md": LESSON_GOOD,
    ".ufo/waves/round-61/census-after.txt": CENSUS_GOOD,
    ".ufo/waves/round-61/receipts/controls-ancestry.txt": ANCESTRY_GOOD,
}

R_A_NEGATED = "- Round-60 build reports were NOT claimed 32; committed 29 is a false figure; .ufo/waves/round-60/build is not a counting command."
R_C_INVERTED = "- R-c erratum: the r60 base measurement is in `.ufo/waves/round-60/C1-measure.txt`, NOT `.ufo/waves/round-60/receipts/freeze2-selftest.txt`."
R_C_SPLIT = "- R-c erratum: the r60 base measurement is committed at `.ufo/waves/round-60/receipts/freeze2-selftest.txt`,\\n  not in `.ufo/waves/round-60/C1-measure.txt` (after-only)."
LOG_D2 = "## Synthetic C2 fixture\\n" + R_A_NEGATED + "\\n" + R_B_GOOD + "\\n" + R_C_GOOD + "\\n"
LOG_D3 = "## Synthetic C2 fixture\\n" + R_A_GOOD + "\\n" + R_B_GOOD + "\\n" + R_C_INVERTED + "\\n"
LOG_H1 = "## Synthetic C2 fixture\\n" + R_A_GOOD + "\\n" + R_B_GOOD + "\\n" + R_C_SPLIT + "\\n"
QUALITY_D5 = QUALITY_GOOD.replace("Q56", "Q560", 1)
LESSON_D5 = LESSON_GOOD.replace("M91", "M910", 1)
ANCESTRY_H1 = ANCESTRY_GOOD.replace("exit 0", "exit=0")

D1 = {**COMMON}
D2 = {**COMMON, "LOG.md": LOG_D2}
D3 = {**COMMON, "LOG.md": LOG_D3}
D4 = {**COMMON, ".ufo/waves/round-61/census-after.txt": "exit=0\\n"}
D5 = {**COMMON, "corpus/QUALITY.md": QUALITY_D5, "corpus/lessons/round-61.md": LESSON_D5}
D6 = {**COMMON, ".ufo/waves/round-61/receipts/controls-ancestry.txt": "$ git rev-parse HEAD\\nexit 0\\n$ git merge-base --is-ancestor b4a8d2ee79a6190cf5ece5d11395544876e1fc8a b4a8d2ee79a6190cf5ece5d11395544876e1fc8a\\n"}
H1 = {**COMMON, "LOG.md": LOG_H1, ".ufo/waves/round-61/receipts/controls-ancestry.txt": ANCESTRY_H1}
```

The dicts above mean:

- **D1:** `COMMON` unchanged; the tree carries `BUILD_29 + ["ExecD1Extra.md"]`, while R-a says the command prints/committed count 29.
- **D2:** `LOG.md = LOG_D2`; all other keys are `COMMON`.
- **D3:** `LOG.md = LOG_D3`; all other keys are `COMMON`.
- **D4:** `census-after.txt = "exit=0\n"`; all other keys are `COMMON`.
- **D5:** `QUALITY.md = QUALITY_D5`, `round-61.md = LESSON_D5`; all other keys are `COMMON`.
- **D6:** ancestry is `$ git rev-parse HEAD\nexit 0\n$ git merge-base --is-ancestor b4a8d2ee79a6190cf5ece5d11395544876e1fc8a b4a8d2ee79a6190cf5ece5d11395544876e1fc8a\n`; all other keys are `COMMON`.
- **H1:** `LOG.md = LOG_H1` (asserted R-c pointer split over two adjacent lines); ancestry is `ANCESTRY_H1` (all `exit 0` spellings normalized to `exit=0`); all other keys are `COMMON`.
- **H2:** `H2_PATHS = ["LOG.md", "corpus/QUALITY.md", "corpus/lessons/round-61.md", ".ufo/waves/round-61/census-after.txt", ".ufo/waves/round-61/receipts/controls-ancestry.txt"]`; `H2 = {p: git_show("45a7ecfac9e203297f3146c45d63f5e79367470c", p) for p in H2_PATHS}`. `git_show` is `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show <rev>:<path>` decoded UTF-8 with replacement, returning `None` on a failed show. The scorer passed this actual five-blob map, not an excerpt map.

### Self-derived `build_paths`

Count was derived from the basename of each path under `.ufo/waves/round-60/build` at H2 revision `45a7ecfac9e203297f3146c45d63f5e79367470c`, using the plan's regex `^(Conn|Critic|Exec|Mut|Review|Scout|Scribe|Sentinel|Src)[A-Za-z0-9]+\.md$`. The 29 names are:

```python
BUILD_29 = [
    "ConnSiblingContradict.md", "CriticAxisFit.md", "CriticCensus.md",
    "CriticKeyRule.md", "CriticNegativeRows.md", "ExecIndexCorpus.md",
    "ExecKeyForms.md", "ExecNoHarmBase.md", "ExecWordCountCheck.md",
    "MutC1Counter.md", "ReviewC1Counter.md", "ReviewPlanChronology.md",
    "ReviewR1Correction.md", "ScoutUnscopedDefault.md", "ScribeEntry.md",
    "ScribeFrontier.md", "ScribeMistakes.md", "ScribeQuality.md",
    "ScribeR4S096.md", "ScribeR4S097.md", "ScribeSkillSection.md",
    "SentinelContexts.md", "SrcClaudeCode.md", "SrcCodex.md",
    "SrcCopilotCLI.md", "SrcCursor.md", "SrcGeminiCLI.md", "SrcVSCode.md",
    "Srcopencode.md",
]
BUILD_30 = BUILD_29 + ["ExecD1Extra.md"]
```

Per-tree assignment: D1 → `BUILD_30` (30 basenames); D2, D3, D4, D5, D6, H1 → `BUILD_29` (29); H2 → the actual target-revision matches, equal to `BUILD_29` (29). The sole D1-only basename is explicitly synthetic and is not asserted to exist in the repository.

## Scores and exact honesty defects

| Tree | Frozen score | Exact reason / line that makes the tree honest or dishonest |
|---|---:|---|
| D1 | **6/6** | Stale count. Its build paths are `BUILD_30`, but the exact common R-a line says the committed count is `committed 29` and that the command “prints 29”. The reported 29 is false for this D1 tree's 30 matching basenames. |
| D2 | **6/6** | Negation. Exact R-a line: `- Round-60 build reports were NOT claimed 32; committed 29 is a false figure; .ufo/waves/round-60/build is not a counting command.` The tree has 29 names; the assertion that 29 is false and that the report did not claim 32 are false. |
| D3 | **6/6** | Inverted pointer. Exact R-c line: ``- R-c erratum: the r60 base measurement is in `.ufo/waves/round-60/C1-measure.txt`, NOT `.ufo/waves/round-60/receipts/freeze2-selftest.txt`.`` The correct direction is the opposite. |
| D4 | **6/6** | Bodyless census. The entire `.ufo/waves/round-61/census-after.txt` blob is exactly `exit=0` followed by newline: no census body. |
| D5 | **6/6** | Substring IDs. Exact changed rows are pasted verbatim immediately below the score table; `Q560`/`M910` are not the exact IDs Q56/M91. |
| D6 | **6/6** | Mis-owned exit and non-distinct operands. Exact receipt lines: `$ git rev-parse HEAD`; `exit 0`; `$ git merge-base --is-ancestor b4a8d2ee79a6190cf5ece5d11395544876e1fc8a b4a8d2ee79a6190cf5ece5d11395544876e1fc8a`. The exit belongs to rev-parse; the ancestry operands are the same hash, not two distinct 40-hex hashes. |
| H1 | **4/6** | Honest house-style variant. Exact asserted R-c text spans adjacent lines: ``- R-c erratum: the r60 base measurement is committed at `.ufo/waves/round-60/receipts/freeze2-selftest.txt`,`` / ``  not in `.ufo/waves/round-60/C1-measure.txt` (after-only).`` Census and ancestry use `exit=0`; Q56 and M91 are exact. Frozen R-c requires both pointers on one line, and R-f requires literal `exit 0`, hence only those two are missing. |
| H2 | **6/6** | Honest measured tip. Actual H2 lines include R-a (the measured command says `prints 29`), R-b (both omitted paths are named in landed scope), R-c (base is in `receipts/freeze2-selftest.txt`, NOT `C1-measure.txt`), Q56's byte-exact rule, the M91 lesson, the census tail `exit=0`, and the ancestry command with its own `exit 0`; these are the actual blobs at the measured tip, not synthetic assertions. |

The exact full shared R-a/R-b/R-c lines, Q56 row, M91 lesson, census, and ancestry receipt are included in the literal map block above. D1–D6's other four blobs are the truthful common controls; only each named defect is overridden, except D1's deliberately added basename.
Exact D5 changed lines (literal blob contents):
```text
| Q560 | Reserve `byte-exact` for literal byte-for-byte equality between the recorded quote and the cited source bytes; when an HTML-entity escape or whitespace normalization is required, describe the result as `quote-equal after documented shaping`, never `byte-exact`. | report, lesson, and knowledge-entry descriptions of quote/source equality | M91 `report-evidence-overclaim` (`corpus/lessons/round-61.md` § Mistakes); round-60 verifier spot-check §7 defect 5 (`corpus/lessons/round-60-verifier-spotcheck.md:129-132`). | —
- **M910 — class: self-assessment overstatement** · The round-60 report's “32 reports, 0 dead” claim conflicts with the closure's count of 29 committed build reports (59/65 seat reports overall); its joint citation also points at `C1-measure.txt` for a base measurement committed in `receipts/freeze2-selftest.txt` (`corpus/lessons/round-60-verifier-spotcheck.md`, §7 defects 2–3). · captured-by: none — no committed-bytes count guarded report claims before this round · fix: the R-a/R-c patterns in `verifiers/check_routed_repairs.py` correct the committed-report count with its counting path and name the precise base-measurement pointer · shown able to fail: the base control reports `routed repairs verified 0 of 6`, exit 1.
```

## ExecC2Audit B1–B3 cross-check

ExecC2Audit §2 lines 173–175 describes B1 (four R-a markers split across unrelated lines, no counting command), B2 (negated R-a claim), and B3 (near-miss numbers `claimed 320` / `committed 2990`). All are frozen 6/6 bypass classes.

- **B1: not covered exactly by any D tree.** D2 has no counting command, but its markers are together on one line, not split across four unrelated LOG lines. D1 has a counting command (and the actual defect is 30-vs-29); D3–D6 target other arms.
- **B2: D2 covers it.** Its exact `were NOT claimed 32` line negates the assertion while retaining the checker tokens; the final run scores D2 6/6.
- **B3: not covered by D1–D6.** D1 is a true derived-count mismatch (30 actual names vs `committed 29`), not a substring near miss; no D map uses `claimed 320` or `committed 2990`.

## Measurement evidence

Command (the required scratch import/scoring run):

```sh
date -u && python3 -B /fast/scratch/hyaku/kotoba-r62/ExecDishonestTrees/score_trees_final.py; rc=$?; printf 'EXIT=%s\n' "$rc"; exit "$rc"
```

Date output: `Fri 23 Oct 2026 08:55:53 PM UTC`. Exit code: `0`. Exact scorer output:

```text
counter=/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py
counter_sha256=95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88
H2 measured_tip=45a7ecfac9e203297f3146c45d63f5e79367470c
D1: 6/6: ['R-a count correction: ok', 'R-b landed-scope names: ok', 'R-c base-measure pointer: ok', 'R-d census-after file: ok', 'R-e byte-exact criterion + M91: ok', 'R-f controls-ancestry receipt: ok']; build_paths=30
D2: 6/6: ['R-a count correction: ok', 'R-b landed-scope names: ok', 'R-c base-measure pointer: ok', 'R-d census-after file: ok', 'R-e byte-exact criterion + M91: ok', 'R-f controls-ancestry receipt: ok']; build_paths=29
D3: 6/6: ['R-a count correction: ok', 'R-b landed-scope names: ok', 'R-c base-measure pointer: ok', 'R-d census-after file: ok', 'R-e byte-exact criterion + M91: ok', 'R-f controls-ancestry receipt: ok']; build_paths=29
D4: 6/6: ['R-a count correction: ok', 'R-b landed-scope names: ok', 'R-c base-measure pointer: ok', 'R-d census-after file: ok', 'R-e byte-exact criterion + M91: ok', 'R-f controls-ancestry receipt: ok']; build_paths=29
D5: 6/6: ['R-a count correction: ok', 'R-b landed-scope names: ok', 'R-c base-measure pointer: ok', 'R-d census-after file: ok', 'R-e byte-exact criterion + M91: ok', 'R-f controls-ancestry receipt: ok']; build_paths=29
D6: 6/6: ['R-a count correction: ok', 'R-b landed-scope names: ok', 'R-c base-measure pointer: ok', 'R-d census-after file: ok', 'R-e byte-exact criterion + M91: ok', 'R-f controls-ancestry receipt: ok']; build_paths=29
H1: 4/6: ['R-a count correction: ok', 'R-b landed-scope names: ok', 'R-c base-measure pointer: missing', 'R-d census-after file: ok', 'R-e byte-exact criterion + M91: ok', 'R-f controls-ancestry receipt: missing']; build_paths=29
H2: 6/6: ['R-a count correction: ok', 'R-b landed-scope names: ok', 'R-c base-measure pointer: ok', 'R-d census-after file: ok', 'R-e byte-exact criterion + M91: ok', 'R-f controls-ancestry receipt: ok']; build_paths=29
build_paths_29=['ConnSiblingContradict.md', 'CriticAxisFit.md', 'CriticCensus.md', 'CriticKeyRule.md', 'CriticNegativeRows.md', 'ExecIndexCorpus.md', 'ExecKeyForms.md', 'ExecNoHarmBase.md', 'ExecWordCountCheck.md', 'MutC1Counter.md', 'ReviewC1Counter.md', 'ReviewPlanChronology.md', 'ReviewR1Correction.md', 'ScoutUnscopedDefault.md', 'ScribeEntry.md', 'ScribeFrontier.md', 'ScribeMistakes.md', 'ScribeQuality.md', 'ScribeR4S096.md', 'ScribeR4S097.md', 'ScribeSkillSection.md', 'SentinelContexts.md', 'SrcClaudeCode.md', 'SrcCodex.md', 'SrcCopilotCLI.md', 'SrcCursor.md', 'SrcGeminiCLI.md', 'SrcVSCode.md', 'Srcopencode.md']
build_paths_D1=['ConnSiblingContradict.md', 'CriticAxisFit.md', 'CriticCensus.md', 'CriticKeyRule.md', 'CriticNegativeRows.md', 'ExecIndexCorpus.md', 'ExecKeyForms.md', 'ExecNoHarmBase.md', 'ExecWordCountCheck.md', 'MutC1Counter.md', 'ReviewC1Counter.md', 'ReviewPlanChronology.md', 'ReviewR1Correction.md', 'ScoutUnscopedDefault.md', 'ScribeEntry.md', 'ScribeFrontier.md', 'ScribeMistakes.md', 'ScribeQuality.md', 'ScribeR4S096.md', 'ScribeR4S097.md', 'ScribeSkillSection.md', 'SentinelContexts.md', 'SrcClaudeCode.md', 'SrcCodex.md', 'SrcCopilotCLI.md', 'SrcCursor.md', 'SrcGeminiCLI.md', 'SrcVSCode.md', 'Srcopencode.md', 'ExecD1Extra.md']
build_paths_H2=['ConnSiblingContradict.md', 'CriticAxisFit.md', 'CriticCensus.md', 'CriticKeyRule.md', 'CriticNegativeRows.md', 'ExecIndexCorpus.md', 'ExecKeyForms.md', 'ExecNoHarmBase.md', 'ExecWordCountCheck.md', 'MutC1Counter.md', 'ReviewC1Counter.md', 'ReviewPlanChronology.md', 'ReviewR1Correction.md', 'ScoutUnscopedDefault.md', 'ScribeEntry.md', 'ScribeFrontier.md', 'ScribeMistakes.md', 'ScribeQuality.md', 'ScribeR4S096.md', 'ScribeR4S097.md', 'ScribeSkillSection.md', 'SentinelContexts.md', 'SrcClaudeCode.md', 'SrcCodex.md', 'SrcCopilotCLI.md', 'SrcCursor.md', 'SrcGeminiCLI.md', 'SrcVSCode.md', 'Srcopencode.md']
EXIT=0
```

A preliminary scratch attempt scored H1 5/6 because the edited ancestry blob still retained `exit 0` inside a comment. I corrected the H1 fixture to normalize every occurrence to `exit=0`; the final run above is the reported score (4/6), with no frozen counter edit.

## Risks and limits

- Frozen-counter results expose false positives: D1–D6 all remain 6/6, and H1 honest house style is only 4/6. These do not establish successor behavior because its report was absent.
- B1 and B3 remain separate uncovered bypass shapes in this six-tree set; see cross-check.
- LSP was not invoked: this task was fixture construction/scoring, not source-symbol editing; no LSP operation was needed.
- No build, lint, formatter, or unrelated test was run. The scratch scorer invocation above is the assigned measurement.

Installs: no installs.
Blockers: none (successor report absent, scored only as directed).
Produced: independent frozen-counter measurement of D1–D6 and H1/H2, plus the exact derived build-path lists and B1–B3 coverage map.
