# ReviewSourcesCensus — round-50 falsify (S024-S029 rows, Gate log, census validate)

HOLDS — scope: SOURCES.md rows S024-S029 (shape, `mined` justification, used-by existence and
citation), the lesson Gate's status/used-by old→new log, the re-opened S019/S022 rows, and the
`grep -c '^| S0'` counts at f304646 and 956ee16. No actionable defect found in scope.

## Findings

1. [INFO, not a round-50 defect] The fleet census emits three W04 warnings (same URL across
   scopes) at the working tree: S018, S019, S021. All three reproduce byte-identically at base
   f304646 (run below), so they pre-date round 50; the pairs are S001/S018, S003/S019,
   S013/S021. The validator's own contract says W-codes never change status and W04 does not
   affect a clean lane (exit 0 is correct).
2. [INFO] Rows S024-S029 are already present at the claims commit 542f515 (count 29), i.e. the
   SOURCES change rode the claims landing, not only the records commit 956ee16. The requested
   counts (base 23, records 29) are unaffected.

## Verification detail

- Shape: all 29 `^| S0` rows at 956ee16 have exactly 13 pipe-split fields (11 registry columns,
  matching the SOURCES-CONTRACT-v1 note in sources-census.sh "11 columns => NF=13"). Zero
  BADSHAPE lines; S024-S029 conform.
- Status/used-by: S024-S029 all `status=[ mined ] opened=[ 2026-10-22 ] recheck=[ 90d ]`, each
  used-by = `corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md`.
- `mined` justification — both used-by files exist and cite every id (word-boundary grep,
  occurrence counts, clone at 956ee16):
  S024 census=2 lesson=4; S025 census=1 lesson=1; S026 census=1 lesson=1; S027 census=1
  lesson=2; S028 census=1 lesson=1; S029 census=2 lesson=5. S019: census=1 lesson=5 SKILL.md=1
  fm-round48=5; S022: census=8 lesson=7. The census file's appended "Round 50" sections cite
  S024-S029 individually with located quotes and seat reports; no id relies on a bare range
  mention alone.
- Independent check: the validator's E11 (used-by path missing on disk) and W03 (mined with
  used-by —) fired zero times on the same file.
- Gate log vs actual (diff f304646 → 956ee16, SOURCES.md): changed/added rows are exactly
  `-/+ S019`, `-/+ S022`, `+ S024` … `+ S029` — "No other row moved" is true.
  - S019 used-by OLD: `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md`;
    NEW: `…, corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md` —
    matches Gate verbatim. Status `mined` at both revs (Gate's "`mined` → `mined`" honest).
  - S022 used-by OLD: `corpus/knowledge/sibling-overlap-census-round49.md`; NEW: `…,
    corpus/lessons/round-50.md` — matches Gate verbatim. Status `mined` at both revs.
  - Gate claim "S024-S029 created as `mined` (used-by: the census entry and this lesson)" matches
    the rows exactly.
- Counts (every count with its command):
  - `git -C <clone> show f30464660c675d1c1e2851a3bf0366a3aaffe5a8:corpus/SOURCES.md | grep -c '^| S0'`
    → 23
  - `git -C <clone> show 956ee1676e4c18480bce8ac3993541462be76e11:corpus/SOURCES.md | grep -c '^| S0'`
    → 29
  - `git -C <clone> show 542f515672306e1baefcb69ba79f1d4c18b6450e:corpus/SOURCES.md | grep -c '^| S0'`
    → 29
  - Matches the Gate's "Rows 23 → 29 (`grep -c '^| S0' corpus/SOURCES.md`)".
- Seat reports the Gate cites all exist under `.ufo/waves/round-50/build/`: SrcOpencodeDocs.md,
  SrcVSCodeSkills.md, SrcClaudeSubagents.md, SrcCopilotSkills.md, SrcGeminiCliSkills.md,
  SrcReopenS019.md, SrcReopenS022.md.

## Assignment command output (pasted verbatim)

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`

```
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
EXIT_CODE=0
```

Base-revision control run:
`sources-census.sh validate --file <scratch-clone-at-f304646>/corpus/SOURCES.md` → same three W04
lines, `file ok`, EXIT_CODE=0.

## Evidence: commands and exit codes

- validate lane working tree: exit 0 (above).
- `git -C <lane> rev-parse HEAD` → 956ee1676e4c18480bce8ac3993541462be76e11 (judged records rev).
- Shape: `git -C <clone> show 956ee16…:corpus/SOURCES.md | awk -F'|' '/^\| S0/ {nf[NF]++; if
  (NF!=13) print "BADSHAPE"} END {for (k in nf) print "NF="k" rows="nf[k]}'` → `NF=13 rows=29`,
  exit 0.
- Citation counts: `grep -o "\b<id>\b" <file> | wc -l` per id/file (clone at 956ee16), all ≥1 as
  listed; `test -f` on all four used-by paths → all exist, exit 0.
- Row diff: `git -C <clone> diff f304646… 956ee16… -- corpus/SOURCES.md | grep -E '^[+-]\| S0'`
  → exactly the eight expected lines (2 changed pairs, 6 additions).
- Status fields: awk extraction of `$9/$10/$11` for S019/S022 at both revs and S024-S029 at HEAD
  → `mined` / 2026-10-22 / 90d throughout.

## Residual risk and verification gaps

- I did not re-fetch any live URL; the sha256/byte-identical re-open claims for S019/S022 and the
  S024-S029 fetch records rest on the seat reports (existence verified above, content out of my
  scope — covered by ReopenS019S022 and the per-source seats).
- Checks are text/data-level on a Markdown registry; no language server applies to these files,
  so literal grep/awk is the appropriate (and only) instrument here, cross-checked against the
  validator's own E11/W03 machinery.
- Bounds: lane untouched except this report file; rev comparisons ran in scratch clones at
  `/fast/scratch/hyaku/kotoba-r50/falsify/ReviewSourcesCensus/`; no tools installed.
