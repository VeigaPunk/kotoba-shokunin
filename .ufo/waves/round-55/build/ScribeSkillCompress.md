Result: DONE — found 18 duplicate prose lines that compress to three pointer lines, freeing 15 lines for the planned additions.

## Finding

At base `f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c`, `SKILL.md` lines 408–416 and 418–426 are two explanations whose evidence and operating guidance already live in the referenced round-50 and round-51 knowledge entries. Compress those 18 lines to the following three lines; keep the source/correction label at line 407, the `Overlap levers by client` anchor at line 417, and the table at lines 428–436. Net: 18 lines become 3, saving 15 lines.

Suggested replacement for `SKILL.md:408–416`:

> The eight-page/five-client finding, Claude Code exception, and `trigger.05` remedy (1,024 characters) are in `corpus/knowledge/skill-selection-rules-round50.md` §§ Findings and What this changes for craft; `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` returns “skill description names 9 of 9 non-none lanes,” exit 0 at `542f515`.
> The keep-both versus remove-one decision and its cost are in `corpus/knowledge/skill-overlap-levers-round51.md` § What this changes for craft.

Suggested replacement for `SKILL.md:418–426`:

> The seven-client lever evidence (including uncounted location levers), no-tie-break result, removal trade-offs, and reviewer-judgment limits are in `corpus/knowledge/skill-overlap-levers-round51.md` §§ Levers by client, Findings, What this changes for craft, and Limits; `python3 -B verifiers/check_overlap_levers.py` checks the table.

The destination material is already present: `corpus/knowledge/skill-selection-rules-round50.md:29–48,52–61` records the scoped finding, Claude Code exception, `trigger.05` remedy, 1,024-character limit, check command, and result. `corpus/knowledge/skill-overlap-levers-round51.md:16–37,41–60,69–75,91–97` records the seven-client evidence, uncounted alternatives, no-tie-break limit, authoring branch/cost, and reviewer-judgment caveat. Both destination files are already referenced from `SKILL.md` lines 407 and 417.

## Gate and pin review

- `verifiers/check_overlap_levers.py:102,211–240,258–280` defines the `Overlap levers by client` marker and reads the first table after that marker within `## Anti-patterns`. Keep line 417's marker and the table at 428–436 unchanged. The proposed replacement leaves the marker/table ordering intact.
- A verifier search for distinctive prose from the proposed moved lines returned `No matches found`: `two sibling descriptions|nothing in either text|name the neighbour and the split|When both skills should stay automatic|the cost is that the removed skill|whether each label matches its page|reviewed list in the checker|Round 50.*Error pattern|round 51.*description is still the only`, plus `two sibling descriptions|both match|fit-based default|component types or configuration sources|session or settings scope|both remain candidates|both automatic everywhere|never fire unasked|location rather than intent|do not own the other skill|only stops firing automatically|whether each label matches its page`. The overlap marker/path and the table are intentionally not moved.
- `verify_skill_checklist.py` checks generic SKILL properties, including the line budget and file citations/commands; the replacement keeps the paths and both check commands. The candidate prose is outside every checklist box. `verifiers/checklist-baseline.json:31–34` pins the separate `trigger.05` checklist box; do not change that box or its hash. No verifier run was performed.
- The round-55 registry rows at `SKILL.md:453–478` are outside these ranges and are not part of this recommendation.

## Identity, commands, and limits

Command: `timeout 15s bash -c 'git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD; git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --quiet f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c a10240c0940f770a5f2a5f32a7e3c363dd5d40c0 -- SKILL.md; rc=$?; printf "SKILL.md base-to-plan diff exit=%s\\n" "$rc"; exit "$rc"'` → exit 0; output: `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0` and `SKILL.md base-to-plan diff exit=0`. Thus the read `SKILL.md` line numbers (599 lines) match the requested base.

Text-only investigation. No product file, gate, baseline, or lane state was edited; no tests, self-tests, or counters were run; no external sources were fetched. The report is the only written artifact.