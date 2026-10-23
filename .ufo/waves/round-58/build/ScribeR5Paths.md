Result: DONE — the requested path scan and existence checks are recorded; three live SKILL.md lines need case correction.

## Scope and behavior

- Work was read-only against the lane files; this report is the only file written. No product files, lessons, or LOG history were edited.
- Search used the specialized `functions.grep` tool with literal pattern `/home/vgpnk/projects/`, case-sensitive, over `SKILL.md`, `corpus/knowledge/`, `PROVINCE.md`, and `verifiers/README.md` (the requested `grep -n` search; no shell grep was run).
- Search result: 21 matching lines — 3 in `SKILL.md`, 18 in `corpus/knowledge/`; `PROVINCE.md` and `verifiers/README.md` returned “No matches found.” The search tool did not expose an exit code.

## Existence evidence

The executed bounded check tested `/home/vgpnk/projects` and each corrected-case path or each path expanded from a glob. Output began `MISSING /home/vgpnk/projects`; `/home/vgpnk/Projects/shokunin` and all corrected targets tested were `EXISTS`. The exact path groups and matched source lines are:

- `/home/vgpnk/Projects/shokunin/.ufo/prompts/` exists: `SKILL.md:353`; `corpus/knowledge/instruction-surface-census-round13.md:467,476,523,532`; `corpus/knowledge/checklist-execution-round16.md:88`.
- Corrected `*-L1.md` glob exists at all 8 expansions: `SKILL.md:516`; `corpus/knowledge/agents-md-and-dispatch-surfaces.md:11`.
- Corrected `*-round-*.md` glob exists at all 355 expansions: `SKILL.md:518`. The line's “50 files” is an older recount; only the path's existence was in scope.
- Corrected `*/AGENTS.md` glob exists at all 17 expansions: `corpus/knowledge/agents-md-and-dispatch-surfaces.md:10`; `corpus/knowledge/instruction-surface-census-round13.md:485`.
- `/home/vgpnk/Projects/shokunin/MISSION.md` exists: `corpus/knowledge/checklist-execution-round15.md:78`.
- `/home/vgpnk/Projects/shokunin/.ufo/reports/` exists: `corpus/knowledge/checklist-execution-round17.md:263`; `corpus/knowledge/corpus-integrity-round11.md:110`.
- All nine corrected report files for rounds 1, 3–10 exist: `corpus/knowledge/claim-census-round12.md:40`; `corpus/knowledge/corpus-integrity-round11.md:131`.
- The corrected `*-shokunin/SKILL.md` glob exists at all 18 expansions: `corpus/knowledge/claim-census-round12.md:80`.
- Corrected repo root and verifier file exist: `corpus/knowledge/cold-run-round11.md:58,59,200`; `corpus/knowledge/sibling-description-rewrites-round8.md:5`. Line 58 contains four lowercase-root path occurrences (two verifier paths and two repo-root paths); the check covered the corrected root and verifier target.

The bounded `test -e`/glob command run was:

```sh
timeout 30s bash -c 'set -u; check(){ if test -e "$1"; then printf "EXISTS %s\\n" "$1"; else printf "MISSING %s\\n" "$1"; fi; }; globcheck(){ local pattern="$1"; local -a hits; local p; shopt -s nullglob; hits=( $pattern ); if ((${#hits[@]} == 0)); then printf "NO MATCHES %s\\n" "$pattern"; return 1; fi; for p in "${hits[@]}"; do test -e "$p" || { printf "MISSING %s\\n" "$p"; return 1; }; done; printf "EXISTS ALL (%d) %s\\n" "${#hits[@]}" "$pattern"; }; check /home/vgpnk/projects; check /home/vgpnk/Projects/shokunin; check /home/vgpnk/Projects/shokunin/.ufo/prompts; globcheck "/home/vgpnk/Projects/shokunin/.ufo/prompts/*-L1.md"; globcheck "/home/vgpnk/Projects/shokunin/.ufo/prompts/*-round-*.md"; globcheck "/home/vgpnk/Projects/shokunin/*/AGENTS.md"; check /home/vgpnk/Projects/shokunin/MISSION.md; check /home/vgpnk/Projects/shokunin/.ufo/reports; for n in 1 3 4 5 6 7 8 9 10; do check "/home/vgpnk/Projects/shokunin/.ufo/reports/round-$n/kotoba.md"; done; globcheck "/home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md"; check /home/vgpnk/Projects/shokunin/kotoba-shokunin; check /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_corpus_integrity.py'
```

The tool output reported the existence/missing lines above; it did not surface an explicit process exit code.

## Exact current-file replacements

`SKILL.md:353` — old:
```text
form: `/home/vgpnk/projects/shokunin/.ufo/prompts/`). Checkable by reading the file; round-7 application +
```
new:
```text
form: `/home/vgpnk/Projects/shokunin/.ufo/prompts/`). Checkable by reading the file; round-7 application +
```

`SKILL.md:516` — old:
```text
- `/home/vgpnk/projects/shokunin/.ufo/prompts/*-L1.md` (8 files, 9–12 lines) —
```
new:
```text
- `/home/vgpnk/Projects/shokunin/.ufo/prompts/*-L1.md` (8 files, 9–12 lines) —
```

`SKILL.md:518` — old:
```text
- `/home/vgpnk/projects/shokunin/.ufo/prompts/*-round-*.md` (50 files, 3–11
```
new:
```text
- `/home/vgpnk/Projects/shokunin/.ufo/prompts/*-round-*.md` (50 files, 3–11
```

These are all three lowercase hits in the live skill, including the additional hit at line 353 outside the named § Sources bullets. The `corpus/knowledge` hits are in round-numbered audit/census/replay records; they include captured historical commands/results and explicit discussion of the old lowercase path. No replacements are proposed there so those records are not rewritten. The bare `/home/vgpnk/projects` text at `checklist-execution-round17.md:264` is not a match for the requested slash-terminated pattern and already states that it is absent.

## Gates, touched surfaces, limits

- No tests, verifiers, builds, or source fetches were run; none were requested for this scribe assignment. No tools were installed.
- Search scope was limited to the four requested surfaces. Lowercase-root presence was tested at the shared prefix; corrected-case existence was tested for every target class and each glob expansion.
- Suggested change surface: only `SKILL.md` lines 353, 516, 518. No source edits were made; the integrator can apply these exact replacements.
- Artifact: `.ufo/waves/round-58/build/ScribeR5Paths.md`.
