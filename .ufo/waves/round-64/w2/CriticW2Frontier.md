# CriticW2Frontier — round 64, wave 2

Seat: `kotoba-r64.CriticW2Frontier-2` (independent leaf critic). Date: 2026-10-24.
Review axes: **coverage and freshness**; source/citation integrity affects **depth and consistency/calibration**, and registry usability affects **operability**. This is adversarial evidence, not admission or a Rust-judge verdict.

## Scope and freshness

- Measured tree: `c019919c97ab5fe98e87a7754b4449ea4e699c99`; base: `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`.
- Measurement began at `2026-10-24T04:20:10.521035+00:00`; mutation receipts completed at `2026-10-24T04:21:26.977697+00:00`. Commands below ran this seat, not copied from wave 1.
- The live HEAD observed during measurement was `b99fb79c27042e0f8a598cbbb4d81479a806b518`, not the measured tip. I therefore extracted a complete `git archive c019919c…` into `/tmp/kotoba-r64-frontier-1kblme_t` and ran all seven frozen manual commands there. Both S120 used-by objects were also tested directly in the measured commit.
- The exact requested live-root validator and a validator over the archived measured tree both exited 0. Live and archived `corpus/SOURCES.md` were byte-identical: SHA256 `975cbce9d2f23291b34389db1419c7b2698825c5dddc8921063e6202824fc847`.
- Fleet validator SHA256: `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30`. Fleet `CORPUS.md` SHA256: `88556402940e7a0f1dbbed3abef9e00c87a90db6f80eaed03269e371f50050b8`. All seven executed command strings were compared with the frozen code block and matched byte-for-byte.
- Read wave-1 `ExecCensusAfter.md`, `ScribeSOURCESRow.md`, `RevSourcesGate.md`, and `ScoutS049.md`; read `plans/round-64.md`, including the declared/errata framing. Findings are grounded again in the measured tree, not in those reports alone.
- The only lane write is this report. Scratch extraction and mutation fixtures are under `/tmp`. No production edits, git/jj writes, index mutations, sibling writes, dispatch, builds, general tests, formatter, or judge/runtime invocation. Census and adversarial probes were explicitly assigned.
- No tools installed or updated. Existing renderer: `markdown-it-py 4.2.0`, invoked through its already-installed uv-tool Python with the table rule explicitly enabled. The prescribed pre-install rules path `/home/vgpnk/Projects/shokunin/.omp/agent/RULES.md` was absent; no install was needed and the host-wide pacman pause was respected.

## Requested checks: measured observations

| Check | Observation |
|---|---|
| Rows | `118`, exit 0 |
| Malformed | `0`, exit 0 |
| Tiers | `A=115 B=2 C=1 `, exit 0 |
| Statuses | `mined=110 queued=7 rejected=1 `, exit 0 |
| Duplicate IDs | No stdout, exit 0 |
| Enum/tier inflation | No stdout, exit 0 |
| Mined used-by missing paths | No stdout, exit 0 |
| Maintained validator | 16 W04 duplicate-URL-across-scopes warnings, no E-code, `ok`, exit 0 |
| S120 used-by exists at measured tip | `corpus/knowledge/g7-span-pinning-round64.md` and `corpus/lessons/round-64.md` are committed blobs, exist in the archive, and cite S120 (8 and 4 textual occurrences, respectively) |
| S120 section/E12 trap | Line 132 is inside `## Registry` (line 10), before `## Paths` (134) and `## Search log` (152); **not** the after-Search-log E12 trap |
| S049 cell preservation | All 11 cells and the complete row are byte-identical between base and measured tip. Row SHA256 (without newline) at both: `b3425f3271d5d5cf8d0148fcaaaad24c604a55bd285b8f1ba6d8b072747867d1` |
| Requested diff | `git diff 078eec4 c019919c -- corpus/SOURCES.md`: 43 added lines, 0 deleted lines. The new S120 row and dated S120/S049 notes are additions only; no S049 row edit |

Empty stdout is shown literally in the command appendix (the next line is `exit=0`). W04 is a warning, not a duplicate-ID finding. These observations do **not** imply complete corpus conformance: the counterexamples below survive the numerical census.

## Findings / smallest safe corrections

### F1 — S120 is section-correct but is not a rendered Registry table row

**Counterexample.** The measured row is preceded by an empty line at `corpus/SOURCES.md:131`. The table starts at 12 and ends at S119 on 130. S120 on 132 is a separate paragraph, despite all seven frozen census commands and the maintained validator being green.

**Evidence.** The installed Markdown parser, with its table rule enabled, reports:

```text
file=/tmp/kotoba-r64-frontier-1kblme_t/corpus/SOURCES.md
table lines=12-130
S120 parent=paragraph_open; in_table=False
registry ids rendered in table=117; S120_in_table=False
```

A scratch-only copy that removes only the blank separator (no row-cell changes) reports:

```text
file=/tmp/kotoba-r64-frontier-1kblme_t/corpus/SOURCES-contiguous.md
table lines=12-131
S120 parent=td_open; in_table=True
registry ids rendered in table=118; S120_in_table=True
```

The parser command exited 0. This independently reproduces wave-1 `ScribeSOURCESRow.md` R1 at the measured tip. The maintained validator checks section membership, not Markdown table contiguity (`scripts/sources-census.sh:608-624`). Frozen contract shape says `## Registry` is “the one table below” (`CORPUS.md:79-83`).

**Impacted axes.** Coverage (118 line-counted rows vs 117 actual table rows); operability (S120 is not a usable table row); calibration/consistency if a clean census is reported as full shape conformance.

**Smallest safe correction.** L1 removes only the blank separator before S120; preserve every existing row cell and the blank before `## Paths`. No source identity change or predicate relaxation is necessary. This is a fixable artifact defect, not an unavoidable axis trade. I did not apply it.

### F2 — S120's immutable teaches cell points the productive-equivalent-mutant caveat at the wrong section

**Counterexample.** `corpus/SOURCES.md:132` ends its teaches cell with `(equivalent mutants can be productive, §III-B2)`. The committed snapshot's §III-B2 says equivalent mutants are a plague and cannot generally be automatically detected. The productive-equivalent-mutant sentence is in **§VI Related Work**, paragraph `#S6.p3.1`, lines 1911–1916 (phrase wraps across 1913–1914).

**Evidence.** Snapshot `.ufo/waves/round-64/snapshots/S120.page:776-783` identifies `#S3.SS2.SSS2` / “III-B2 Heuristics to Prevent Equivalent Mutants”; `:1883-1884` identifies `#S6` / “VI Related Work”; `:1913-1914` says `mutants might be unproductive or that equivalent mutants can be` / `productive`. Snapshot is 571,600 B, SHA256 `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8`, matching S120's recorded artifact. The registry still contains the wrong §III-B2 parenthetical. This independently reproduces wave-1 `ScribeSOURCESRow.md` R2 / `RevSourcesGate.md` §13.2; it was not repaired by the measured integration.

**Impacted axes.** Depth (a citation resolves to a section that does not say the attributed thing); consistency/calibration and freshness (an already-detected citation defect remains at the measured tip). The adequacy definition and the equivalent-mutant warning elsewhere in the row/lesson are not refuted by this finding.

**Smallest safe correction.** Do not silently change the already-committed teaches/anchor cells: contract v1 permits only status/recheck/used-by changes in place (`CORPUS.md:116-118`). The contract-safe correction is the next unused source ID with teaches opening `supersedes S120 —`, locating the caveat at `§VI Related Work #S6.p3.1` (or replacing it with the actual §III-B2 caveat), with citing entries and allowed used-by changes logged accordingly. The old row remains historical. A one-cell swap was cheap before landing, but is no longer the append-only correction path. This is fixable reference drift, not a reason to conflate or silently weaken either frozen claim predicate.

### F3 — the new S120/S049 “Search log” notes are actually under Leads (unopened)

**Counterexample/evidence.** At the measured tip `## Search log` is line 152 and is closed by `## Leads (unopened)` at 204. No later level-2 heading occurs. Both round-64 notes (S120 opening at 246 and S049 re-probe at 286) therefore belong to **Leads**, not Search log. The lesson nevertheless says “Appended to `corpus/SOURCES.md` § Search log” (`corpus/lessons/round-64.md:49`). Wave-1 `ScoutS049.md:42` explicitly noticed the original EOF was under Leads, so this is a preserved landing-placement defect rather than missing evidence.

**Impacted axes.** Coverage/operability of the search record; consistency/calibration of its declared location. The search evidence and dated receipts exist; this finding does not say the searches never happened. The same layout debt existed for the round-63 note, so it is not attributed as wholly introduced this round.

**Smallest safe correction.** Add a correctly placed, dated correction/cross-reference in the actual Search log pointing to the preserved round-64 evidence and amend the lesson by an appended location correction. If L1 instead relocates the newly introduced notes, preserve their content and make the location correction explicit; do not rewrite the S049 row or old dated errata. Do not count the current Leads placement as a new unopened-source lead or as a correctly located Search-log addition.

## Adversarial controls (scratch only)

1. **E12 relocation control:** removed only the S120 row from its original location and appended the identical row at EOF under Leads. All seven frozen commands produced the same results as the measured source, including 118 rows and no missing paths. Maintained validator emitted `file	E12	S120 row outside Registry section`, exit 1. This shows why the numerical census cannot establish section placement and confirms the maintained E12 guard is live. The measured tree itself does not have this E12 defect.
2. **Missing-used-by control:** substituted only S120's knowledge-entry path with `corpus/knowledge/ABSENT-r64-frontier.md`. Frozen command printed `missing: corpus/knowledge/ABSENT-r64-frontier.md` but still exited **0**; maintained validator emitted E11 and exited **1**. Therefore the frozen manual existence check must be read for stdout as the contract says, not interpreted as an exit-code gate. The real two S120 paths exist and cite S120.
3. **Formatting-only correction control:** removing the one blank separator restored S120 to the actual parsed table while leaving its cells unchanged (F1). No production correction was applied.

These are bounded frontier controls, not SM1–SM6/C2 mutation-battery results. This seat did not run, judge, or claim to refute the C1/C2 verifier predicates. All three findings are fixable frontier/citation defects; whether they affect the round's no-harm/admission outcome belongs to the canonical judge, not this report. The clean census must not be promoted to a saturation/conformance claim that it does not measure.

## Command evidence (full captured stdout/stderr and exits)

Commands ran through `bash -o pipefail -c`; the seven manual invocations themselves are byte-for-byte the frozen commands. Working directory is given for each command. Scratch extraction preserves committed used-by files; no live-root path substitution was used for the pinned manual existence check.

### Measured commit

Working directory: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`

```text
$ git rev-parse HEAD && git cat-file -t c019919c97ab5fe98e87a7754b4449ea4e699c99
b99fb79c27042e0f8a598cbbb4d81479a806b518
commit
exit=0
```

### Pinned archive

Working directory: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`

```text
$ git archive c019919c97ab5fe98e87a7754b4449ea4e699c99 | tar -x -C /tmp/kotoba-r64-frontier-1kblme_t
exit=0
```

### Frozen rows

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
118
exit=0
```

### Frozen malformed

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
0
exit=0
```

### Frozen tiers

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
A=115 B=2 C=1 
exit=0
```

### Frozen statuses

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
mined=110 queued=7 rejected=1 
exit=0
```

### Frozen duplicates

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
exit=0
```

### Frozen enums

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
exit=0
```

### Frozen mined used-by existence

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
exit=0
```

### Exact requested validator

Working directory: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

### Pinned archive validator

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /tmp/kotoba-r64-frontier-1kblme_t /tmp/kotoba-r64-frontier-1kblme_t
kotoba-r64-frontier-1kblme_t	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba-r64-frontier-1kblme_t	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba-r64-frontier-1kblme_t	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba-r64-frontier-1kblme_t	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba-r64-frontier-1kblme_t	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba-r64-frontier-1kblme_t	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba-r64-frontier-1kblme_t	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba-r64-frontier-1kblme_t	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba-r64-frontier-1kblme_t	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba-r64-frontier-1kblme_t	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba-r64-frontier-1kblme_t	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba-r64-frontier-1kblme_t	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba-r64-frontier-1kblme_t	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba-r64-frontier-1kblme_t	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba-r64-frontier-1kblme_t	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba-r64-frontier-1kblme_t	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba-r64-frontier-1kblme_t	ok	/tmp/kotoba-r64-frontier-1kblme_t/corpus/SOURCES.md
exit=0
```

### Exact required registry diff

Working directory: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`

```text
$ git diff 078eec4 c019919c -- corpus/SOURCES.md
diff --git a/corpus/SOURCES.md b/corpus/SOURCES.md
index 2ace7b3..5829494 100644
--- a/corpus/SOURCES.md
+++ b/corpus/SOURCES.md
@@ -129,6 +129,8 @@ for a source the row's author opened this round; access evidence lives in
 | S118 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Current Claude Code `.claude/rules/` `paths` frontmatter matching syntax (vendor documentation; not a runtime test) | § Rule frontmatter reference (`memory.md:244-250`), especially `paths` (`:250`); § Path-specific rules (`:194-200`); fetched 2026-10-23T20:49:56Z (HTTP 200, 55,354 B, sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`); snapshot `.ufo/waves/round-62/snapshots/S118.page` | re-opens S103 — opened this round because the round-62 C1 E2e instances need the vendor's own statement of how the `paths` key takes glob patterns; S103's scope covered the directory overview, and this row records the current-round access to the rule-frontmatter reference | mined | 2026-10-23 | 90d | corpus/lessons/round-62.md, corpus/knowledge/erratum-absorption-round62.md |
 | S119 | ICMJE — Corrections and Version Control — https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html | docs | A | Correction practice for a published record: a transparent correction notice that cites the original, and preservation of prior versions | § Corrections (snapshot `.page:170-174`); fetched 2026-10-23T23:04Z (HTTP 200, 22,722 B, sha256 `d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2`; the page carries a dynamic element — a re-fetch of the same size hashed `e2c3db05…` in a seat probe, so byte-identity across fetches is not claimed, only the located quotes); snapshot `.ufo/waves/round-63/snapshots/S119.page` | A journal publishes a correction notice "as soon as possible detailing changes from and citing the original publication" and "archive all prior versions of the article" — transparent correction with preserved history, not a silent rewrite of the record; the page does not mandate literal append-only files | mined | 2026-10-23 | 365d | corpus/knowledge/compound-clause-citation-round63.md, corpus/lessons/round-63.md |
 
+| S120 | Practical Mutation Testing at Scale: A view from Google (Petrović, Ivanković, Fraser & Just) — https://arxiv.org/html/2102.11378 | paper | A | Primary peer-reviewed study for the claim this row scopes: mutation analysis measures a test suite's adequacy by whether it detects seeded faults — so survival, not line coverage, locates an unasserted effect at covered code. Scoped to the paper's own statement; the lane's load-bearing-branch application is the lane's inference, not the paper's study object. Not a survey | arXiv:2102.11378v2 HTML (26 Feb 2021), the artifact opened and quoted: abstract `#abstract1.1` snapshot lines 283-284, §1 Introduction `#S1.p1.1` line 324, §III-B2 Heuristics to Prevent Equivalent Mutants `#S3.SS2.SSS2.p1.1` lines 780-782; journal version IEEE TSE 48(10):3900-3912 issue Oct 2022 (online Aug 2021), DOI 10.1109/TSE.2021.3107634, metadata from `curl -sS https://api.crossref.org/works/10.1109/TSE.2021.3107634` only — the IEEE HTML was not opened; fetched 2026-10-24 (HTTP 200, 571,600 B, sha256 `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8`); snapshot `.ufo/waves/round-64/snapshots/S120.page` | "Mutation analysis assesses a test suite’s adequacy by measuring its ability to detect small artificial faults, systematically seeded into the tested program" — mutant-kill is the adequacy witness, so a survivor on a covered branch is a lead that its assertion is missing, not proof of a gap (equivalent mutants can be productive, §III-B2) | mined | 2026-10-24 | 180d | corpus/knowledge/g7-span-pinning-round64.md, corpus/lessons/round-64.md |
+
 ## Paths
 
 - **Authoring a SKILL.md that loads everywhere — S018 → S017 → S008 → S019 → S012 → S002 → S011.**
@@ -241,3 +243,44 @@ for a source the row's author opened this round; access evidence lives in
   serves the same content at the same path modulo the request profile, so a second row
   would duplicate the scope S088/S115 already govern. The row's recorded receipt stays as
   the dated original.
+- **2026-10-24 — round-64 S120 opening (C1's method source).** Question: which primary source teaches
+  mutation-kill as witnessed coverage — a surviving mutant as the signal that a load-bearing guard
+  branch is exercised but never witnessed — and states the equivalent-mutant caveat. Where: two web
+  searches (the plan's named candidate; then the mutant-versus-real-fault validity line), the arXiv
+  record and PDF for `2102.11378` (fetched twice byte-identical), the arXiv HTML the snapshot pins,
+  Crossref for both DOIs the plan named and for the journal version, and the included paper's own
+  bibliography. Identified 8 distinct candidate works; screened 8; included 1 (S120); excluded 7 —
+  (a) Just, Jalali, Inozemtseva, Ernst, Holmes and Fraser, "Are Mutants a Valid Substitute for Real
+  Faults in Software Testing?", FSE 2014, DOI 10.1145/2635868.2635929: grounds a different claim
+  (mutant detection correlates with real-fault detection beyond coverage), so carrying it would widen
+  S120's scope against rule 2, and it was not opened this round, so rule 1 forbids a row; (b)
+  Petrović and Ivanković, "State of Mutation Testing at Google", ICSE-SEIP 2018, pp. 163–171, DOI
+  10.1145/3183519.3183521: the same authors' earlier, smaller report (6,000 engineers against the
+  included paper's 24,000 developers on 1,000+ projects), superseded for this scope; (c) Jia and
+  Harman, "An Analysis and Survey of the Development of Mutation Testing", IEEE TSE 37(5):649–678,
+  2011: secondary survey, tier B at best, and it is the included paper's own reference [28] for the
+  equivalent-mutant problem, so it duplicates S120's scope; (d) "Mutation Testing in the Wild:
+  Challenges and Lessons from Bitcoin" (SBC/SAST, surfaced 2026): single-system experience report in
+  another domain, no scale claim for this scope, not opened; (e) "Does mutation testing improve
+  testing practices" (ICSE 2021, pp. 910–921, the same four authors, identified by RevSourcesGate's
+  independent record check and surfaced by my search only as a secondary index page): a different
+  question — whether mutation testing changes developer testing behaviour — and a different venue
+  class from the included journal article, not opened; (f) `arXiv:2103.02722`, the plan's identifier:
+  opened, and it is Peralta, "A Markov jump process associated with the matrix-exponential
+  distribution" — wrong work, rejected; (g) DOI 10.1109/ICSE43902.2021.00068, the plan's DOI:
+  resolved through Crossref, and it is Chen et al., "An Empirical Study on Deployment Faults of Deep
+  Learning Based Mobile Applications", ICSE 2021, pp. 674–685 — wrong work, rejected. The plan's
+  candidate citation is therefore corrected by the opened record in three places: the authors are
+  Petrović, Ivanković, Fraser and Just (no Ernst), the venue is IEEE Transactions on Software
+  Engineering 48(10):3900–3912, published in issue Oct 2022 (Crossref published-print 2022-10-01,
+  created 2021-08-27), not ICSE 2021, and the preprint is `arXiv:2102.11378v2` (26 Feb 2021), not
+  `2103.02722`. Stop rationale (rule 5): the plan's two identifiers were opened and rejected rather
+  than silently skipped, and the title-matched primary then opened and carries both located quotes
+  the `teaches` cell needs — the adequacy definition at `abstract1.1` and "are a plague in mutation
+  testing and cannot generally be detected automatically" at `S3.SS2.SSS2.p1.1` — so the sweep stops
+  at full inclusion of the one qualifying source; every other screened work grounds a different
+  claim, is secondary, or was not opened, and ScoutS120Alt's three fallbacks (a Google engineering
+  blog post, a university mutation-testing chapter, PIT's equivalent-mutant docs) stay unscreened
+  because the title match succeeded — recorded there, not counted here.
+
+- **2026-10-24 — round-64 S049 live-context re-probe (appended; the S049 row and the 2026-10-23 errata are not rewritten).** Question: does the request-profile split on `https://cursor.com/docs/rules.md` still hold, and does either profile reproduce a held receipt? Where: that URL under curl 8.23.0 default `Accept` (sent `Accept: */*`, no `-H`) and under `Accept: text/markdown`, plus one control fetch of `https://cursor.com/docs/rules` (no `.md`, default Accept). Probed 2026-10-24T03:35:37Z. Default `Accept`: HTTP 200, `content-length` absent, body 17,252 B, sha256 `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0` (`text/markdown; charset=utf-8`; `vary: Accept`; Vercel cache HIT, age 1254, `Date: Sat, 24 Oct 2026 03:14:43 GMT`). `Accept: text/markdown`: HTTP 404, `content-length` absent, body 389 B, sha256 `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1` (body headed `# Page not found`; Vercel cache MISS, age 0, `Date: Sat, 24 Oct 2026 03:35:37 GMT`). The 2026-10-22 receipt (17,403 B, sha256 `884c67ca…`, fetched 2026-10-22T20:09:33Z) does not reproduce under either profile. The 2026-10-23 default-Accept receipt (17,252 B, sha256 `dae9d3ec…`) reproduces byte-for-byte, and the request-profile-dependent 404 still reproduces. Control `https://cursor.com/docs/rules`: HTTP 200, `content-length: 540892`, body 540,892 B, `text/html; charset=utf-8`, sha256 `35ff98b0fca637195a670ca8907d32b52642cb311d5455717aedfbc2d91e6ee2` (0 redirects; same byte count as the 2026-10-23 extensionless HTML fetch, which recorded no digest). No S049 field is rewritten.
exit=0
```

### Measured S120 used-by object existence

Working directory: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`

```text
$ git cat-file -t c019919c97ab5fe98e87a7754b4449ea4e699c99:corpus/knowledge/g7-span-pinning-round64.md && git cat-file -t c019919c97ab5fe98e87a7754b4449ea4e699c99:corpus/lessons/round-64.md
blob
blob
exit=0
```

### Measured and formatting-only corrected table rendering

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ /home/vgpnk/.local/share/uv/tools/markdown-it-py/bin/python -c 'from markdown_it import MarkdownIt
from pathlib import Path
import re, sys
print("markdown-it-py table rule enabled")
for name in sys.argv[1:]:
    text=Path(name).read_text()
    tokens=MarkdownIt("commonmark").enable("table").parse(text)
    in_table=False
    source_ids=[]
    print("file="+name)
    for i,t in enumerate(tokens):
        if t.type=="table_open":
            in_table=True
            print("table lines="+str(t.map[0]+1)+"-"+str(t.map[1]))
        elif t.type=="table_close": in_table=False
        elif in_table and t.type=="inline" and re.fullmatch(r"S\d{3,}", t.content): source_ids.append(t.content)
        if t.type=="inline" and "Practical Mutation Testing at Scale" in t.content:
            print("S120 parent="+tokens[i-1].type+"; in_table="+str(in_table))
    print("registry ids rendered in table="+str(len(source_ids))+"; S120_in_table="+str("S120" in source_ids))
' /tmp/kotoba-r64-frontier-1kblme_t/corpus/SOURCES.md /tmp/kotoba-r64-frontier-1kblme_t/corpus/SOURCES-contiguous.md
markdown-it-py table rule enabled
file=/tmp/kotoba-r64-frontier-1kblme_t/corpus/SOURCES.md
table lines=12-130
S120 parent=paragraph_open; in_table=False
registry ids rendered in table=117; S120_in_table=False
file=/tmp/kotoba-r64-frontier-1kblme_t/corpus/SOURCES-contiguous.md
table lines=12-131
S120 parent=td_open; in_table=True
registry ids rendered in table=118; S120_in_table=True
exit=0
```

### E12 mutant frozen rows

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES-E12.md
118
exit=0
```

### E12 mutant frozen malformed

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES-E12.md
0
exit=0
```

### E12 mutant frozen tiers

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES-E12.md
A=115 B=2 C=1 
exit=0
```

### E12 mutant frozen statuses

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES-E12.md
mined=110 queued=7 rejected=1 
exit=0
```

### E12 mutant frozen duplicates

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES-E12.md | sort | uniq -d
exit=0
```

### E12 mutant frozen enums

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES-E12.md
exit=0
```

### E12 mutant frozen mined used-by existence

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES-E12.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
exit=0
```

### E12 mutant maintained validator

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file /tmp/kotoba-r64-frontier-1kblme_t/corpus/SOURCES-E12.md
file	W04	S018 duplicate url agentskills.io/specification across scopes
file	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
file	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
file	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
file	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
file	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
file	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
file	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
file	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
file	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
file	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
file	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
file	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
file	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
file	W04	S115 duplicate url cursor.com/docs/rules across scopes
file	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
file	E12	S120 row outside Registry section
exit=1
```

### Missing-usedby mutant frozen command

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES-missing-usedby.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
missing: corpus/knowledge/ABSENT-r64-frontier.md
exit=0
```

### Missing-usedby mutant maintained validator

Working directory: `/tmp/kotoba-r64-frontier-1kblme_t`

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file /tmp/kotoba-r64-frontier-1kblme_t/corpus/SOURCES-missing-usedby.md
file	W04	S018 duplicate url agentskills.io/specification across scopes
file	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
file	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
file	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
file	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
file	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
file	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
file	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
file	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
file	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
file	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
file	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
file	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
file	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
file	W04	S115 duplicate url cursor.com/docs/rules across scopes
file	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
file	E11	S120 missing used-by corpus/knowledge/ABSENT-r64-frontier.md
exit=1
```

Report: .ufo/waves/round-64/w2/CriticW2Frontier.md
