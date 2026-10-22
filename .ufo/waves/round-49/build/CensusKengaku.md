ROW | kengaku | detached (HEAD == master) | 1f3b0f1ec41ec297130e8944ff97968d32324632 | SKILL.md | adjacent | yes | yes | SKILL.md:3 | "Domain specialist — LLM/model research & evaluation — eval design, benchmark selection, offline replay grading, blind shim-cascade leg attribution and interval-calibrated verdicts"

# C1 adjacency census — kengaku-shokunin

## Findings

1. **Classification `adjacent`.** kengaku measures prompt/format *effects* and explicitly assigns
   the craft half to kotoba — in its frontmatter and twice in its province. It does not write or
   audit another lane's `SKILL.md`, prompts, or `AGENTS.md`, and owns no instrument over those
   surfaces (no `verifiers/` and no `skills/` directory exists at the pinned commit).
2. **The split is stated as a mutual, high-confidence boundary.** kengaku PROVINCE.md:138:
   "prompt- and skill-craft rules — measured capability effects of prompt format stay here;
   reusable craft implications route out (r7 tools-without-system, r11/r12 ack-intent findings)".
   Its own round-9 overlap map raises the same split to High confidence: "kotoba's province and
   render artifacts define craft; kengaku's source probe and result summary define measured
   experimental outcomes. Attribution is deliberately split by claim type."
   (`corpus/evidence/round9-fleet/sibling-overlap.md:53`, quote located there.)
3. **Frontmatter names kotoba and carries a multi-lane arbitration clause.** SKILL.md:3 description:
   "Sibling arbitration: kotoba owns prompt and skill craft (kengaku keeps only measured capability
   effects); kumitate owns OMP route resolution and fallback policy; kama owns local endpoint health
   and identity; chousa owns research method; tameshi owns verification-fixture craft. Rank: shonen."
   That clause arbitrates against five siblings, kotoba first. Anti-trigger excludes "serving-flag
   changes, endpoint remediation or model-serving config" (kama's ground), so no serving overlap.
4. **PROVINCE.md names kotoba 5 times** (lines 30, 35, 62, 83, 138), each as routed-out scope or a
   report-out to kotoba, never as claimed ownership. Refusals header line 6: "anything outside this
   domain; report cross-domain evidence back to the orchestrator rather than absorbing it."
5. **Not `contested`: no craft artifact authoring or auditing.** The only path matching
   prompt/skill-instrument shapes is `corpus/evidence/round9-fleet/probeC_prompt_check.py`, a probe
   harness that rebuilds its own message lists offline ("rebuild run_c()'s message lists offline
   (pure string ops) and diff cells", line 1) — an eval instrument, not an auditor of lane prompts.
   kengaku's own decision tables (benchmark selection, minimal stack) are domain content; kotoba's
   core claims decision-table *craft* and refuses domain content inside other skills, so the halves
   complement rather than collide.
6. **Borrowed kotoba artifacts, measurement-side only.** kengaku's overlap map cites
   `corpus/knowledge/skill-activation-telemetry.md` and `corpus/knowledge/render-mechanism-round7.md`.
   Both are ABSENT from kengaku's tree at the pinned commit (`git cat-file -e` → absent) and both
   exist in kotoba at `a5adc146` — kengaku consumes kotoba's render/trigger evidence as measurement
   input, which is the adjacent direction, not an ownership claim.
7. **Residual unknowns.** (a) kengaku's overlap-map citations at line 12 are prefix-less
   (`corpus/knowledge/…` inside kengaku's repo), so they read as local paths while resolving to
   kotoba's tree — a citation-clarity defect on kengaku's side, not a scope overlap. (b) kengaku's
   anti-pattern 5 "Freeze godspeed text, judge schema, and telemetry capture" touches prompt text as
   an experimental control (freezing, not authoring); under the half-split this stays on kengaku's
   side, but it is the closest approach to kotoba's surface and worth one census sentence.
   (c) kotoba's own PROVINCE.md:31 currently names kengaku only as "LLM/model evaluation and route
   telemetry", with no half-split phrase — the § Adjacent rewrite should carry the split from
   finding 2.
8. **Method note.** The subject files are Markdown prose; no language server answers `.md`, so no
   definition/reference trace exists to run. All quotes and line numbers are taken from committed
   bytes via `git show <commit>:<path> | nl -ba`, read-only, with the sibling working tree clean
   (`git status --porcelain | wc -l` → 0), so pinned bytes equal checked-out bytes.

## Evidence

Pin (exit codes verbatim):

- `git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin rev-parse master` → `1f3b0f1ec41ec297130e8944ff97968d32324632`, exit 0.
- `git -C … symbolic-ref -q HEAD` → exit 1 (detached HEAD); `git -C … rev-parse HEAD` → same 40-hex, exit 0. `git rev-parse HEAD master` printed the identical hash twice.

Skill files at the pinned commit:

- `git -C … ls-tree --name-only 1f3b0f1e…` (exit 0): `.gitignore .ufo AGENTS.md LOG.md PROVINCE.md README.md SCORECARD.md SHONEN.md SKILL.md considerthese corpus grader.py plans`.
- `git -C … ls-tree -r --name-only 1f3b0f1e… | grep -E '^(skills?/[^/]+/)?SKILL\.md$'` (exit 0) → exactly one line: `SKILL.md` (703 lines).

Frontmatter (`git show 1f3b0f1e…:SKILL.md | sed -n '3p' | wc -c` → 902 bytes, one physical line):

- `name: kengaku-shokunin` (line 2).
- `git show …:SKILL.md | grep -c kotoba` → **1** (all on line 3).
- `git show …:SKILL.md | grep -o 'Sibling arbitration: kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)'` → matched, exit 0.

PROVINCE at the pinned commit:

- `git show …:PROVINCE.md | grep -c kotoba` → **5**; `grep -n kotoba` → lines 30, 35, 62, 83, 138.
- Headings (`grep -nE '^#{1,3} '`) → Domain/Owns/Refuses at 3/5/6; `## Refusals…` 22; `## Province map — round 24` 95; `### Core` 102; `### Frontier` 121; `### Adjacent` 129; `### Historical` 145; round-28/29 admissions 192/204.
- `### Core` (102–120) is a surface-check table (grader.py pin, probe artifacts, attribution instruments, `corpus/QUALITY.md`, `corpus/SOURCES.md`); it contains no craft-over-other-lanes row.

Sweep over pinned prose files (command run per file, then combined):

- `for f in SKILL.md PROVINCE.md AGENTS.md; do git show 1f3b0f1e…:$f | grep -cE 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba'; done` → SKILL.md **15**, PROVINCE.md **10**, AGENTS.md **0**.
- Combined: `{ git show …:SKILL.md; git show …:PROVINCE.md; git show …:AGENTS.md; } | grep -cE '…'` → **25** matches total.
- SKILL.md matches are domain-prose uses (`prompt regime` in anti-pattern 3, `system prompt` in the r7 tool-call finding, `Freeze: prompt text` in the production checklist, `description` in a round-25 note); PROVINCE.md matches are the five kotoba lines plus `prompt` in report-out text. Neither file states a rule for authoring/auditing another lane's skill file.
- `AGENTS.md` (5 lines, exit 0) is kengaku's own operating rules ("Work only within this repo and its PROVINCE.md scope"), not an always-on craft dossier for other lanes.

Instrument / ownership checks:

- `git ls-tree --name-only 1f3b0f1e… | grep -E '^(verifiers|skills?|agents?)/$'` → no match, exit 1.
- `git ls-tree -r --name-only 1f3b0f1e… | grep -icE '(prompt|skill).*(verify|check|audit)|verify.*(prompt|skill)'` → **9** paths, 8 of them `.ufo/waves/round-28/scratch/…` copies of the ninth, `corpus/evidence/round9-fleet/probeC_prompt_check.py`.
- Cross-tree: `git -C kengaku-shokunin cat-file -e 1f3b0f1e…:corpus/knowledge/skill-activation-telemetry.md` → absent; same for `render-mechanism-round7.md` → absent. `git -C kotoba-shokunin ls-tree -r --name-only a5adc146…` lists both, exit 0. kengaku has 37 files under `corpus/knowledge/` (`git ls-tree -r --name-only … | grep -c '^corpus/knowledge/'`), none matching `skill|prompt` in the file name.

Quote provenance:

- Scope quote, SKILL.md:3 (description, first 22 words verbatim, ends before the `;` that continues into the absent-wiki clause).
- Overlap quote, PROVINCE.md:138, table cell verbatim without its pipe delimiters (23 words).
- Supporting quote, `corpus/evidence/round9-fleet/sibling-overlap.md:53` (29 words; cited as evidence, not as a ROW quote).

Sibling working tree: `git -C kengaku-shokunin status --porcelain | wc -l` → 0, so the pinned commit's bytes are the checked-out bytes.

Tool installs/upgrades: none. No web fetches this seat; no lane, fleet or sibling files were modified; the only file written is this report.
