# Round 49 falsify — CalibrationRecords (count and pointer mismatches)

VERDICT: FAILS — applies to the round-49 records at c48793d (SCORECARD round-49 rows and move-log rows, the Round 49 completed / Next: round 50 / R3 blocks, LOG round-49 entry, corpus/README rows 68–70 and the round-49 paragraph at lines 119–122, PROVINCE Core bullet at line 17 and the Adjacent table it feeds). Six mismatches. The headline counts reproduce.

Mismatch count: **6** (M1–M6), plus **1 pending forward pointer** (P1) and **1 unverifiable timestamp** (U1), both listed below and not counted in the 6.

## Reproduced (no mismatch)
- Adjacency: 20 PROVINCE rows at HEAD and at f054b8e, 0 at a5adc146; 7 adjacent, 13 none, 0 contested. Guard `rows 20 verified 20`, `province rows 20 matched 20`, exit 0. Guard self-test 39 assertions. All 20 pinned sibling commits exist in their sibling repos. Census recomputed from SKILL.md at the pins: 17 descriptions, 8 name a sibling, 2 name kotoba (kengaku, kotodama). kotoba's description names 5 (kagi, kake, kasegi, kengaku, kumitate), not kotodama. Withdrawn kasegi clause: `git -C kasegi-shokunin grep -qiE 'prompt[- ]injection' 1fafde8f…` exit 1.
- Operability: `--box-proof --map verifiers/checklist-baseline.json` exit 0, `boxes proven 2`. Dispatch self-test exit 0, 32 assertions. Map 41 boxes: 8 executed / 2 delegated / 31 unexecuted at HEAD, 8/0/33 at base. Floors guard exit 0, 10 instruments at HEAD, 9 at base. Live run: dispatch.04 FAIL on the six listed files, dispatch.08 250 PASS / 29 N/A.
- R1: harness self-test 116 (a5adc146), 115 (d1ae458), 116 (48819b9), 123 (f054b8e, HEAD).
- R3 correction: unreadable configured skills root (mode 000, uid 1000) gives exit 2 `SUBSTRATE … Permission denied` at d1ae458 and exit 0 at a5adc146, f054b8e, 48819b9 and HEAD. Commit 48819b9's subject contains the quoted phrase; SCORECARD line 28 (depth row) records the fix.
- Other: SOURCES.md 21 rows at base, 23 at HEAD; S018, S022, S023 present. Corpus integrity at HEAD exit 1, `8/9 checks pass; DRIFT: report_dead` (observed 2); at base 4 DRIFT. Floors registry has no check_sibling row. Wave: 36 seats (scout 23, scribe 4, executor 4, reviewer 2, critic 2, connector 1). Pointer paths: 42 of 43 present at HEAD; `.ufo/reports/round-48/kotoba.md` is absent, as corpus/README row 68 says. Negative probes: base PROVINCE exit 1; kasegi-reclassified copy exit 1 (`matched 19`); one-quote-altered census exit 1; dispatch.04 remapped to an unrelated instrument exit 1 (`boxes proven 1`); HEAD box-proof control exit 0.

## Mismatches
**M1 — operability claim contradicted by the blind instrument (count).** SCORECARD.md:31: "the blind second instrument agrees on the six dispatch.04 failures." Observed: `python3 -B .ufo/waves/round-49/build/c2-independent-indep.py --prompts /home/vgpnk/Projects/shokunin/.ufo/prompts --state /home/vgpnk/Projects/shokunin/.ufo/state` exit 0; its summary `failures_per_box`: dispatch.04 = 7 (aggregator-L1.md, kake, kasegi, kengaku, kotoba, kumitate, protocol), dispatch.08 = 168 (`state-bound-exceeded`). Primary: dispatch.04 = 6 (no aggregator), dispatch.08 = 0 FAIL. The blind instrument still enforces the frozen `<id>.round` authority (its docstring), while SKILL.md:330–332 now says `.report-baseline`. Scope also differs (blind: 291 dispatch in scope of 380 scanned; primary: 287 evaluated + 28 out of scope). The 7-versus-6 count and the 168 dispatch.08 failures appear nowhere in the records. Severity: high for the operability calibration.

**M2 — stale count, PROVINCE Frontier.** PROVINCE.md:23: "Executed checklist coverage (33 of 41 boxes still lane-attested prose)." Observed: `python3 -B verifiers/verify_skill_checklist.py` exit 0, `box_map … 41 boxes mapped (8 executed, 2 delegated, 31 unexecuted)`. 33 is the base value (8/0/33). Mismatch 33 versus 31.

**M3 — same stale count, corpus/README.md:78, which also contradicts the same file.** corpus/README.md:78: "33 of 41 SKILL.md boxes remain lane-attested prose." corpus/README.md:87: "31 of the 41 SKILL.md checklist boxes are still lane-attested prose." Mismatch 33 versus 31, internal to the README.

**M4 — wording contradicts the executed status (low to medium).** corpus/README.md:78: "the agent-definition, dispatch-prompt and always-on checklists have no executed box." SCORECARD.md:31 says "dispatch-prompt boxes executed"; SCORECARD.md:255 says the capability "runs two dispatch-prompt checklist boxes"; corpus/README.md:91–94 says the instrument "executes them." The map entries are `delegated:verifiers/verify_dispatch_prompts.py` (checklist-baseline.json, dispatch.04 and dispatch.08), so "no executed box" holds only in the map's vocabulary. A reader gets the opposite.

**M5 — "moved from Frontier" is a copy (1 residual entry).** PROVINCE.md:17: "Sibling arbitration (round 49, moved from Frontier)." Observed: PROVINCE.md:23 still lists "sibling arbitration clauses" under Frontier; base PROVINCE.md:22 has the same entry. The Core bullet was added and the Frontier entry was not removed.

**M6 — pointer content does not carry the claim (low).** PROVINCE.md Adjacent, kumitate row: "kotoba owns the prompt wording, not the runtime (kumitate `PROVINCE.md:27`)." `git -C kumitate-shokunin show fac39171…:PROVINCE.md` line 27 reads "- Local model serving and endpoints → kama. Prompt and skill craft → kotoba. Research method → chousa." It supports prompt-craft routing, not the "not the runtime" clause.

**P1 — pending forward pointer (not counted).** LOG.md:2376 (round-49 entry, last section): "Falsification wave and landing pin follow in the next entry." At c48793d no later section exists; the file ends at line 2376. It resolves only once the landing pin is written.

**U1 — unverifiable timestamp (not counted).** SCORECARD.md:31 and LOG.md:2372: "Live run 2026-10-22T11:15Z." `.ufo/waves/round-49/build/c2-live-run-1115Z.json` has keys checks, exit_code, fail, na, pass and no timestamp. The time appears only in the filename. The `.txt` matches the live output.

## Not run or not verified (no verdict given)
- "turning one mutant fixture into a passing file prints boxes proven 1, exit 1" (SCORECARD.md:31): not run; only the dispatch.04 remap was run.
- `scripts/sources-census.sh validate` (LOG.md:2375: exit 0, 21 → 23 rows, three W04 warnings): the script is at the fleet root only and was not run. Row counts were checked directly.
- R1 wording "configured and log-named roots keyed by frontmatter name": only the self-test count (116 → 123) was checked.
- "0 dead seats" and "The L1 held the planner seat": not checked.
- Census finding 5 "17 directed pairs across 8 descriptions": the table's arbitration column lists 19 targets; 17 only if the two kotoba targets (kengaku, kotodama) are excluded, and the census does not say so. Ambiguous; not counted.
- The round-50 candidate "a frontmatter edit, held this round by the drift guard": the SKILL.md frontmatter is unchanged (lines 1–16 identical), but the body changed (15 changed diff lines, dispatch.08 box at SKILL.md:330–332). The LOG and SCORECARD do not list the body change.

## Out-of-bounds write (disclosed)
My blind-instrument run used the script's default `--out`. It wrote `/fast/scratch/hyaku/kotoba-r49/seats/DispatchIndependent/indep.json` (mtime 2026-10-22 08:38:36 -0300). That directory belongs to another seat (its `indep.py` and `run.txt` are there). Any earlier content of indep.json is overwritten and I cannot recover it. The main agent should tell the DispatchIndependent seat. Everything else was read-only: the lane, the fleet root and the sibling repos.

## Method
- Private clone `/fast/scratch/hyaku/kotoba-r49/falsify/CalibrationRecords/clone`, checked out at c48793d. Revisions a5adc146, f054b8e, d1ae458 and 48819b9 were checked out in mirror trees.
- Gates ran in mirrors: a kotoba clone at each revision, with every fleet entry symlinked in, because citations resolve `../.ufo/...` against the fleet root. A bare-clone run failed `citation_resolves` for that reason, so those results are not used.
- Tools: none installed or updated. Used python3, git, and the installed omp (`omp --version` → omp/18.12.6).

## Evidence (command → exit code, key output)
- `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → 0; `rows 20 verified 20`; `province rows 20 matched 20`.
- `python3 -B verifiers/check_sibling_census.py --self-test` → 0; `0 failure(s) over 39 assertions`.
- `awk '/^## Adjacent/{f=1;next} /^## /{f=0} f' PROVINCE.md | grep -cE '^\| (<20 names>) \| (contested|adjacent|none) \| [0-9a-f]{40} \|'` → 20 (HEAD), 20 (f054b8e), 0 (a5adc146). Class counts 7 adjacent, 13 none.
- `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` → 0; `boxes proven 2`. `python3 -B verifiers/verify_dispatch_prompts.py --self-test` → 0; `0 failure(s) over 32 assertions`.
- `python3 -B verifiers/verify_dispatch_prompts.py` (fleet defaults) → 1; dispatch.04 `287 evaluated: 259 PASS, 6 FAIL, 22 N/A; 28 out of scope`; dispatch.08 `279 evaluated: 250 PASS, 0 FAIL, 29 N/A; 13 out of scope`.
- `python3 -B verifiers/verify_skill_checklist.py` → 0 at HEAD (11 check lines, no FAIL) and 0 at base; box_map 8/2/31 (HEAD), 8/0/33 (base).
- `python3 verifiers/check_assertion_floors.py` → 0 at HEAD (10 PASS lines, `dispatch_prompts observed=32 floor=32`) and 0 at base (9 lines).
- `python3 -B verifiers/verify_corpus_integrity.py` → 1 at HEAD (`8/9 checks pass; DRIFT: corpus.pointers.report_dead`, observed=2); 1 at base (4 DRIFT, 5/9 pass); 1 at f054b8e (tracked 66 vs 63 expected).
- `python3 -B verifiers/verify_harness_independent.py --self-test` → 0 at a5adc146 (116), d1ae458 (115), 48819b9 (116), f054b8e (123) and HEAD (123).
- R3 probe `python3 -B verifiers/verify_harness_independent.py --json --oc-config <case>` with skills mode 000 → 0 at a5adc146, 0 at f054b8e, 2 at d1ae458 (`SUBSTRATE [Errno 13]`), 0 at 48819b9, 0 at HEAD.
- Negative probes: base PROVINCE → 1; kasegi reclassified → 1; one-quote-altered census → 1; dispatch.04 remapped → 1 (`boxes proven 1`); HEAD box-proof control → 0.
- `git -C <sibling> cat-file -t <pin>` → `commit` for all 20 (mori via mori-shokunin; tameshi via tameshi-shokunin). mori-shokukin and tameshi-shokukin are not git repositories (exit 128).
- Description census: SKILL.md at the pins, hyphen-bounded whole-token match → 17 descriptions, 8 name a sibling, 2 name kotoba.
- `grep -cE '^\| S[0-9]{3}' corpus/SOURCES.md` → 21 (a5adc146), 23 (HEAD).
- `python3 -B .ufo/waves/round-49/build/c2-independent-indep.py --prompts … --state …` (see out-of-bounds note) → 0; summary.failures_per_box dispatch.04 = 7, dispatch.08 = 168.
- `git -C kasegi-shokunin grep -qiE 'prompt[- ]injection' 1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a` → 1.
- Wave: build-spec.json items by role (scout 23, connector 1, scribe 4, executor 4, reviewer 2, critic 2) = 36; build-dispatch.json counts spawn 36.
- `git diff --stat a5adc146 c48793d` → 87 files changed, 20573 insertions, 47 deletions.

## Residual risk
- M1 means the round-49 operability claim rests on one instrument at HEAD. The blind check disagrees on dispatch.08 and on scope, and its authority was not updated with SKILL.md.
- The mirror trees symlink fleet-root entries, so instrument writes to the fleet are not ruled out beyond the reads I observed.
