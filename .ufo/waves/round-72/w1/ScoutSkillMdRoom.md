# ScoutSkillMdRoom — wave 1 round 72 (C1 depth line-budget scout)

## Verdict

Best candidate: **SKILL.md lines 150–204 (the `## Router model — which harness, which gate` body, 55 lines) move VERBATIM to `corpus/knowledge/anatomy-and-compression.md` § Moved from SKILL.md § Router model (round 72)**, with the heading `## Router model — which harness, which gate` kept at SKILL.md:148 and a pointer line at SKILL.md:150. Net freed ≈ 54 lines (55 moved − 1 pointer). That covers the round's ≈ 22-line addition (four checklist boxes + five registry rows) with margin, with **zero breakage**: no verifier parses or hashes any line of 150–204, and the destination file is already tracked and indexed (no new corpus file, no index row needed).

Secondary candidate (NOT zero-breakage as one block): `## Sources` body 526–600 (75 lines) — it contains one bullet (line 590) carrying `` `../.ufo/reports/round-7/kotoba.md` ``, which becomes a dead report pointer if moved verbatim into `corpus/knowledge/` (breaks `verify_corpus_integrity.py`).

## Method

Read the frozen plan (`plans/round-72.md`), full SKILL.md (600 lines), and inspected parse/hash behavior of the four named instruments. All commands ran from the lane root `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. No files written outside this report; no tools installed; no git/jj mutations; single process, well under the 4/120s cap.

## Candidate A — Router model body (SKILL.md 150–204)

Block: intro paragraph (150–152), two-harness table (154–157), "Check before predicting" recipe (159–168), `### Run the verifier instead of re-typing the recipe` (170) plus the two verifier-recipe paragraphs (172–204). Contains **0** `- [ ]` box markers and **0** fenced blocks (SKILL.md has no fences at all).

### Observables

- `sed -n '150,204p' SKILL.md | sha256sum` → `7aa505aadb970057cf7cbcfd0c9ca0414fbbbda701b50060043e61f41df738bb  -`
- `sed -n '148,204p' SKILL.md | sha256sum` → `76051db31df5e0d42b8eafdcffdc2f3f3312bb1b4001a554879c0306e68eb4be  -` (heading+body; the moved-block receipt should pin the 150–204 body hash)
- `sed -n '148,204p;524,600p' SKILL.md | grep -cE '^\s*- \[ \]'` → `0`
- `grep -c '^```' SKILL.md` → `0` (exit 1; no fenced blocks in the file)

### Do any of the four instruments parse/hash lines of 150–204?

- `verify_skill_checklist.py`: parses only `- [ ]` boxes (keyed by section + text sha256) plus whole-file scans for citation/command subjects and line counts. No box lives in 148–204; the block's lines are scanned generically (counted toward `line_budget`, scanned by `no_placeholder`/`citation_resolves`/`command_binary_resolves` subjects) but never hashed by identity. Removing them only lowers evaluated counts; `citation_resolves` keeps ≫0 subjects from the rest of the file (e.g. the trigger-fidelity checklist and instruction-surfaces tables), so no `N == 0 → N/A → not PASS` failure is reachable.
- `check_province_core.py`: reads only `PROVINCE.md` and `corpus/README.md` (index row); no SKILL.md access. Does not touch 148–204.
- `check_gate_registry.py`: parses only the first table under the pinned `## Gate registry` heading (SKILL.md 470–522). Does not touch 148–204.
- `verify_corpus_integrity.py`: docstring states "SKILL.md is outside corpus/ and is never scanned"; it reads only corpus/README.md index + tracked corpus `*.md` pointers. Does not touch 148–204.
- `verify_harness_claims.py` references `SKILL.md` § Router model **only in its docstring** (line 4: "Recomputes, from live host state, the facts that `SKILL.md` § Router model and" — 15 words); runtime reads host paths, never the lane's SKILL.md.
- `verify_surfaces.py`, `verify_harness_independent.py`, `check_assertion_floors.py`: no lane-SKILL.md access (surfaces reads the census entry; independent reads host skill roots; floors reads the floors registry).

### Dependents found (heading/phrase/`SKILL.md:<line>` grep over verifiers/*.py, verifiers/*.json, corpus/knowledge/*.md, corpus/README.md, LOG.md, SCORECARD.md, SHONEN.md)

All prose/§-level citations; none is a runtime parse. Keeping the heading at 148 keeps every one of them truthful:

- `corpus/knowledge/skill-listing-thresholds-round54.md:33` — "description (`../../SKILL.md` § Router model; `render-mechanism-round7.md`). So the tightest documented" (12 words; sed output).
- `corpus/knowledge/frontmatter-trigger-surface.md:104-105` — "activation — the catalogue is built from frontmatter only (see `SKILL.md`" (12 words).
- `verifiers/verify_harness_claims.py:4` — docstring, quoted above.
- `corpus/knowledge/claim-scope-audit-round9.md:57` — "| `grep -c '^## Router model'` | 0 | 1 |" (historical record of the section's addition; 9 words).
- `corpus/README.md:48` — "before-state on `SKILL.md` @ md5 `143fe473…` … the landed `## Router model` table" (historical; 12 words).
- `LOG.md:153` — "`SKILL.md` gained `## Router model — which harness," (round-9 record; 7 words).
- `LOG.md:212`, `LOG.md:295` — `SKILL.md` § Sources references (not § Router; listed under candidate B).
- No `SKILL.md:<line>` citation landing inside 148–204 exists in any committed lane doc; all hits in `.ufo/` archives (e.g. `SKILL.md:151`, `:135` in round-48/50 reports) are point-in-time references at their own commits, not live checks.

### Hazards scan inside the block

`sed -n '150,204p' SKILL.md | grep -nE '\.ufo/|verifiers/|corpus/'` shows only: `verifiers/verify_harness_claims.py`, `verifiers/baseline.json`, `verifiers/checklist-baseline.json`, `verifiers/verify_dispatch_prompts.py`, `.ufo/waves/round-50/falsify/ReviewBoxProofGate.md`, `corpus/knowledge/harness-verifier-round10.md`, `corpus/knowledge/checklist-execution-round17.md`. None is a `.ufo/reports/round-N/*.md` report-pointer or `commit <hex>` citation, so none becomes a corpus-integrity subject when the block moves into a corpus file.

## Candidate B — Sources body (SKILL.md 526–600)

Block: 75 bullets/pointer lines under `## Sources` (524). Contains 0 boxes, 0 fences. `sed -n '526,600p' SKILL.md | sha256sum` → `ff419b06b78a6dfe1f8616f9e427b05462f9312178d6cc1b53c60ef166135cce  -`.

### The breakage

`sed -n '525,600p' SKILL.md | grep -nE '\.ufo/reports/|commit `|`[0-9a-f]{7,}`'` → one hit, relative 66 = absolute 590: `../.ufo/reports/round-7/kotoba.md` inside the `render-mechanism-round7.md` bullet ("`../.ufo/reports/round-7/kotoba.md`, not in the artifact. Loss figures" — 11 words; byte-exact from sed output). In SKILL.md (lane root) this resolves at the fleet root; inside `corpus/knowledge/` it resolves to `corpus/.ufo/reports/round-7/kotoba.md`, which does not exist → `report_dead` +1 → `verify_corpus_integrity.py` DRIFT. A verbatim whole-block move is therefore **not** zero-breakage. (Mitigations would violate verbatim: split around the bullet or change one hop to `../..`.)

### Dependents found

- `LOG.md:212` — "`corpus/knowledge/harness-router-models-round9.md`, `SKILL.md` § Sources and" (11 words).
- `LOG.md:295` — "`corpus/README.md` rows, `SKILL.md` § Sources + the citation rule made" (12 words).
- `LOG.md:2453` (round 54 record of the earlier verifier-bullets move), `LOG.md:2520` (round 59 record of the 28-line Sources move into anatomy-and-compression.md).
- `corpus/knowledge/agent-definition-files-round56.md:91` — "`../../SKILL.md` § Sources still lists 18 files there, marked" (10 words; notes a historical marker — content already handled at that line).
- `corpus/knowledge/claim-census-round12.md:100,161` — historical awk/records over `## Sources`.
- `verifiers/check_correction_sweep.py` rows `r53-c2-skill-75-line` / `r53-c2-skill-six-files` carry their DECLARED patterns (`14 lines / 949 B`, `17 files`) physically on Sources line 531. The sweep rule fires only when a block contains the STALE pattern without DECLARED; both stale patterns are absent from SKILL.md, so moving line 531 does not fire the sweep (verified by reading the registry: stale regexes `75-line host`, `AGENTS\.md` \(6 files\)` occur nowhere in the current file).
- `verifiers/verify_corpus_integrity.py:73` — docstring notes "deliberately recorded dead paths (SKILL.md:588's `~/wikillm`, `~/.xbgst`" (10 words); that line is now 597 in Sources. Moving it makes this docstring's line number stale (cosmetic, not a gate). The `~/wikillm`/`~/.xbgst` tokens themselves are tilde-anchored non-report tokens — per that same docstring they are not citation subjects inside corpus either, so no new corpus finding.
- No `SKILL.md:<line>` citation landing inside 526–600 exists in committed lane docs (all hits archived in `.ufo/`).

## Rejected blocks (not ≥24 contiguous or parsed)

- `## Trigger-fidelity checklist` 253–326, `## Agent-definition fidelity checklist` 328–372, `## Dispatch-prompt fidelity checklist` 374–406, `## Always-on constraint-file checklist` 408–430: contain the 41 hash-pinned boxes → `box_map_complete` would fail.
- `## Gate registry` 464–522: first table parsed by `check_gate_registry.py` (pinned heading/header).
- Per-client decision tables 82–90, 96–104, 110–118, 124–132, 138–146, 216–224, 230–238: parsed by `check_agent_definitions.py`, `check_plugin_manifests.py`, `check_command_files.py`, `check_hook_files.py`, `check_scoped_rules*.py`, `check_description_thresholds.py`, `check_explicit_invocation.py` (each requires the exact section heading + first table + one row per client).
- `## Anti-patterns` 432–453 (22 lines): `check_overlap_levers.py` reads the "Overlap levers by client" table inside that section.
- Intro/loader-contract paragraph 23–47: excluded per assignment (separate considerthese proposal).
- All other runs are <24 lines.

## Destination and pointer

- Destination: `corpus/knowledge/anatomy-and-compression.md` (already tracked, indexed at `corpus/README.md:10`; 199 lines; ends with the round-60 host-surfaces `## Moved from SKILL.md § Sources` section). Append `## Moved from SKILL.md § Router model (round 72)` with the receipt hash `7aa505aadb970057cf7cbcfd0c9ca0414fbbbda701b50060043e61f41df738bb` computed before and after the move (round 59/60 precedent).
- Pointer in SKILL.md: keep `## Router model — which harness, which gate` at 148; blank 149; pointer at **SKILL.md:150** (1–3 lines, e.g.): `The full router-model facts, check-before-predict recipe, and verifier recipes moved verbatim to \corpus/knowledge/anatomy-and-compression.md` § Moved from SKILL.md § Router model (round 72).`
- Net freed ≈ 54 lines; round addition ≈ 22 lines (four boxes with continuations + five registry rows) fits without touching any parsed section.

## Bounds/tooling

No installs, no scratch dirs, no git/jj writes, single process. All findings observed via the commands above; nothing unobserved is asserted.
