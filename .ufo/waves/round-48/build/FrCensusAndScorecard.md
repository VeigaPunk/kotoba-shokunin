# Round 48 build · FrCensusAndScorecard — census and scorecard calibration read

Lane: kotoba-shokunin. Measured at HEAD `75f671b109d8eddd0d64c1429bd6379fe577175a` (master, committed 2026-10-21 22:18 -0300). Read-only; no lane file edited.

## Findings (most consequential first)

**F1 (high). The pins guard and the surfaces gate are red at HEAD; SCORECARD records them as green.**
- Observed: `omp --version` = `omp/18.12.6`. `/home/vgpnk/.local/bin/omp` has sha256 `85d9daf3…` and mtime `2026-10-21 20:37:24 -0300`. The pin in `verifiers/baseline.json` is `fdbc8136…` (omp 18.12.5), mtime `03:30:38 -0300`.
- SCORECARD: freshness row (round 47) says `verify_surfaces.py --json` "exit 0, 7/7" and `check_substrate_pins.py` "exit 0, 3/3". Capability row (substrate-pin guard) says "`exit 0`, `OK 3/3 pins hold`".
- Observed: `check_substrate_pins.py` exit 1. `verify_surfaces.py --json` exit 1 (pass 5, fail 2).
- Read: both guards work as built; they name the moved pins. The substrate moved after the round-48 base: base `197b5a4` 18:36 -0300, omp binary replaced 20:37 -0300, HEAD 22:18 -0300. No re-pin has landed. No repo regression found.

**F2 (high). The adjacency axis's only counting command fails at HEAD and at its documented before-revision.**
- SCORECARD adjacency row (round 26): "published replay exits 0 at HEAD (`226/14/14/0/4/3`) AND at the before-revision `581e293`".
- Observed: `HEAD frozen` exit 1 `instrument_drift`. `581e2932… frozen` exit 1 `instrument_drift`.
- Cause (verified): the replay compares a whole-file sha256 of `verifiers/verify_skill_checklist.py` with `instrument.sha256` (`214ae44d…`) in `corpus/knowledge/sibling-citation-routing-round16.json`. That pin equals the file at `321647c` (round 38). The only later commit touching the file is `7ad7fad` (round 47, C2). It changed the file with no re-pin; the file now hashes `4ea2100d…`. Adjacency score 8.0 rests on this replay.

**F3 (high for depth). The "live 24/24" join is red. The snapshot-carrier leg is recorded but not re-run here.**
- Observed: `compare_harness_independent.py --json` exit 2: `false blocker: scoped row omp.catalogue.found declares observable {"candidate_blocks": 5769 …} but recomputation gives {"candidate_blocks": 5770 …}`. Same for `.matched` and `.missing_names`. An earlier run in a misnamed clone gave 5695 vs 5698.
- Mechanism [INFERENCE from code]: the observable walks the live `~/.omp/agent/sessions` tree (`verifiers/compare_harness_independent.py:973-1017` and `:1133-1157`). A session file written between the two reads moves the count.
- Stale present-tense claims: `corpus/README.md:38` "**live 24/24 over the landed scope, exit 0**"; `corpus/README.md:59` "a fresh live producer/join remains protocol 24/24 (strict 20/24 …)".
- Depth row's "snapshot-carrier honest join exit 0, 24/24 protocol, 20/24 strict" cites `.ufo/round-46/evidence/w2/c1/summary.json` (`honest_join_pass: true`). Its runner `.ufo/round-46/evidence/w2/c1/runner.py` is committed. The recorded invocation uses placeholders (`<x3 frozen 055d3b9 copy>`) and `/tmp/kotoba-r46-c1b/…`, which no longer exists. Not re-run here.

**F4 (medium). Q19 on the `planned` block "Next: round 48".** Re-measured at HEAD:

| Before-value in block | Measured at HEAD | Verdict |
|---|---|---|
| `verify_harness_claims.py` 21/28 | exit 1, `21/28 checks pass` | Value matches. Block prints no command or commit; Q19 requires both. |
| Allowlist "goes vacuous on the next minifier rename" | `surfaces.no_uncovered_class` FAIL, "0 loader class(es) extracted" | Premise already true: the allowlist goes vacuous on the current omp 18.12.6. Stale premise (M20 class). |
| "three new host skills" | `missing_names` = create-toolset, unreal-mcp, unreal-skill | Matches. |
| Stale "Next: round 47" block: "surfaces 5/7, pins 1/3" | Live: surfaces 5/7, pins 1/3 | Same numbers, on omp 18.12.6. Coincidence; does not confirm the struck provenance. |

**F5 (medium). SHONEN box 1 cites a stale Sources count.**
- Claim (`.ufo/round-46/scouts/B2.md`, cited by SHONEN): "38 Sources entries".
- HEAD `SKILL.md` (sha256 `975e13f6…`, 528 lines) has 39 bullets under `## Sources`.
- B2's `SKILL.md` sha256 `0404fdc0…` equals blob `e8a81ac` (round 28): 521 lines, 38 bullets. Round-46 landing `f2f9ee1` added the 39th bullet (`+- \`corpus/SOURCES.md\` — where this lane learns…`). B2 counted a pre-round-46 blob.
- Other box-1 counts match HEAD: 41 checklist boxes; 15/9/9/8 by section; 7 anatomy rows; 5 decision rows.

**F6 (low). Record hygiene.**
- Axis-row "Last change" cells vs the last move-log row per axis: depth 15 vs 46; operability 16 vs 46; freshness 21 vs 43; calibration 17 vs 46; adjacency 21 vs 26.
- The move log has no round-47 rows. Round 46 has its own landing table; round-47 moves live only in row prose.
- The substrate-pin capability row has no dated annotation for the post-round-47 omp move. The floors row got one at round 41.

## Confirmed, no mismatch (HEAD)
- SOURCES census: validate exit 0 (`ok`); census exit 0 with rows 15, tier A 14, tier C 1, mined 6, queued 8, rejected 1. SCORECARD cites S003 (×3), S012 (×2), S015 (×1); all are `mined`.
- `verify_skill_checklist.py --json` exit 0, 11/11. `--self-test` exit 0, 0 failures over 1845 assertions (the round-47 operability and calibration figures).
- `verify_corpus_integrity.py` exit 0, "9/9 checks pass". `verify_corpus_independent.py` exit 0.
- `verify_harness_independent.py --json` exit 0 (28 checks); self-test 0/104. `compare_harness_independent.py --self-test` 0/330.
- `check_assertion_floors.py` exit 0, 9 of 9 PASS.
- `<skills>` in the frontmatter: 0 matches (exit 1).
- C1 before-value (plan): ruler exit 1, verdict `failed`, 5 target failures, 0 behavioral mismatches, 13 settled cases. Matches the plan.
- Knowledge entries: 34 `.md` files at HEAD (plan "before: 34"). `agentskills|skills-ref` sweep of `corpus/knowledge`: no hits.
- SHONEN boxes 2–4: evidence paths exist. LOG.md cites the round-11 cold run (lines 287, 294, 342).

## Commands and outputs

Fleet-shaped clone used for items 4–19: `S=/fast/scratch/hyaku/kotoba-r48-a2/seats/FrCensusAndScorecard/fleet`. `$S/kotoba-shokunin` is a clone at `75f671b` with empty `git status`, plus a copy of `shokunin.conf`.

1. `scripts/sources-census.sh validate --root $S kotoba; echo EXIT=$?` → `kotoba	ok	…/fleet/kotoba-shokunin/corpus/SOURCES.md` · `EXIT=0`
2. `scripts/sources-census.sh census --root $S kotoba; echo EXIT=$?` → `kotoba rows 15`, `tier.A 14`, `tier.C 1`, `status.mined 6`, `status.queued 8`, `status.rejected 1`; FLEET lines identical, plus `tier.B 0`, `missing 0` · `EXIT=0`
3. Lane root, working tree (other seats editing; NOT HEAD): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → 21 rows, `E11 S016 missing used-by corpus/lessons/round-48.md`, W04 warnings · `EXIT=1`
4. `python3 -B verifiers/verify_skill_checklist.py --json` → exit 0, `pass 11 fail 0`. `--self-test` → exit 0, `0 failure(s) over 1845 assertions`.
5. `python3 -B verifiers/verify_corpus_integrity.py` → exit 0, `9/9 checks pass`. `verify_corpus_independent.py` → exit 0.
6. `python3 -B verifiers/verify_harness_independent.py --json` → exit 0. `--self-test` → `0 failure(s) over 104 assertions`. `compare_harness_independent.py --self-test` → `0 failure(s) over 330 assertions`.
7. `python3 -B verifiers/check_assertion_floors.py` → exit 0, nine PASS lines (e.g. `PASS floors_guard observed=150 floor=150`).
8. `python3 -B verifiers/check_substrate_pins.py` → exit 1: `FAIL omp_binary_sha256: sha256 drift: expect=fdbc8136… got=85d9daf3…`; `FAIL omp_binary_mtime: … delta_ns=61606480536650`; `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime`.
9. `python3 -B verifiers/verify_surfaces.py --json` → exit 1, `pass 5 fail 2`: `surfaces.literal_present` (8 loader literals unverifiable); `surfaces.no_uncovered_class` (vacuity: 0 loader classes extracted).
10. `python3 -B verifiers/verify_harness_claims.py` → exit 1: `21/28 checks pass; DRIFT: omp.db.rows, omp.offered.skills, omp.cache.misses, omp.catalogue.total, omp.catalogue.missing_names, omp.cache.verified_skills, oc.roots.names_plus_builtin`.
11. `python3 -B verifiers/compare_harness_independent.py --json` → exit 2 (message quoted in F3).
12. Replay: `PYTHONDONTWRITEBYTECODE=1 python3 -c '<count-code block of corpus/knowledge/sibling-citation-routing-round16.md>' HEAD frozen` → exit 1 `instrument_drift`. Same with `581e2932850db9cb917844662651f533bfd98519 frozen` → exit 1 `instrument_drift`.
13. C1 before (plan), at base: `python3 -B .ufo/round-48/tools/config-root-ruler.py --repo . --revision 197b5a4087bad49a465df7d13d7e821fe4cf227b --consumer-sha256 872993f875338f4f… --oracle .ufo/round-48/oracle/config-root-cases.json --oracle-sha256 1d09a38ce04d6c0a… --scratch <fresh dir> --baseline-receipt .ufo/round-48/verification/before-configured-root.json --baseline-sha256 8bec447aa538446e…` → exit 1. Output: `"verdict": "failed"`, `"target_failures": ["singular-unlogged","plural-unlogged","both-distinct-unlogged","same-name-both-config-roots","configured-plus-other-log-root"]`, `"behavioral_mismatches": []`, `"settled_cases": 13`. Hashes: ruler `01af33a6…`; before receipt `8bec447a…` (accepted by `--baseline-sha256`).
14. `git ls-tree -r --name-only HEAD corpus/knowledge | grep -c '\.md$'` → `34`.
15. `git log --format=%h -- verifiers/verify_skill_checklist.py` → 11 commits; newest `7ad7fad`, then `321647c`. The replay pin equals the blob at `321647c`.
16. `git log -6 --format='%h %aI %s'` → `3f43454` 16:59 -0300 (round-47 landing); `197b5a4` 18:36 -0300 (base); `75f671b` 22:18 -0300 (HEAD). Omp binary mtime `2026-10-21 20:37:24 -0300`.
17. `git show e8a81ac:SKILL.md | wc -l` → 521; bullets after `## Sources` → 38. HEAD: 528 lines, 39 bullets.
18. `git ls-files | grep -i runner` → `.ufo/round-46/evidence/w2/c1/runner.py` (plus a round-46 console file). `ls /tmp/kotoba-r46-c1b` → `No such file or directory`.
19. `git grep -n -i horizon -- README.md corpus/README.md` → no hits. The plan's "erratum horizon" wording is not located there.

Evidence bundle (scratch copies of raw output; sha256 prefixes): `/fast/scratch/hyaku/kotoba-r48-a2/seats/FrCensusAndScorecard/evidence/`. Checklist JSON `62444ab3…`; surfaces JSON `a9852b01…`; harness claims `25c90410…`; compare join `d525515b…`; ruler rerun `87aba4b4…`; corpus integrity `bc2c2bfa…`; corpus independent `641f0e4c…`; floors `cb7e5d08…`.

## Setup, bounds, tools
- Fleet-shaped clone needed. The first clone was named `kotoba`; the checklist gate then reported a name mismatch and unresolved `../` citations (exit 1, 8/11). That run is discarded. The final layout has 43 read-only copies of fleet-root files (`AXES.md`, `MISSION.md`, `PROTOCOL.md`, `SCORECARD.md`, `.ufo/` reports and wave members, two `kasegi-shokunin` instrument files) plus `shokunin.conf`. Copies were added until the gate's own unresolved list was empty. No fleet file was written.
- Writes: scratch paths and this report only. `git status` ran in the lane (read only; git may refresh the index stat cache, disclosed here).
- Tools installed: none. Used system python 3.14, git, sha256sum, awk.
- Lane working tree at read time (other seats, not measured here): `M SKILL.md`, `M corpus/SOURCES.md` (21 rows), `M verifiers/verify_harness_independent.py`, `?? corpus/knowledge/frontmatter-rule-authorities-round48.md`, `?? .ufo/waves/round-48/`, `?? plans/round-48.md`.
- Not run: the after-ruler on a landed commit; the snapshot-carrier join (F3); anything inside the working-tree diff.

## Checks for Main after integration
- `python3 -B verifiers/check_substrate_pins.py` (expect exit 1 until re-pinned).
- `python3 -B verifiers/verify_surfaces.py --json` (expect exit 1).
- Adjacency replay `HEAD frozen` (expect exit 1 `instrument_drift`).
- `python3 -B verifiers/compare_harness_independent.py --json` (expect exit 2).
- `python3 -B verifiers/verify_skill_checklist.py --json`, run in a checkout named `kotoba-shokunin` beside fleet siblings (expect exit 0, 11/11).

## Routed (not fixed here)
- Replay pin: pin a function slice, not the whole file; re-issue on each instrument edit.
- Live join: freeze the omp-session observable at measure time, or tolerate a bounded difference; commit the snapshot runner's inputs.
- Re-stamp freshness, adjacency, and capability pointers to omp 18.12.6; add round-47 move-log rows; reconcile the Last-change cells.
- SHONEN box 1: change 38 to 39, citing `f2f9ee1`.
- Round-48 candidate "rename-robust omp call-shape rule": its before-value is already red at HEAD (F1, F4).
