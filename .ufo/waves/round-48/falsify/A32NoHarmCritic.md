# A32NoHarmCritic — round 48 no-harm, axis by axis

Seat `KotobaR48.A32NoHarmCritic` (critic, leaf). Targets: `d1ae458` (C2 depth), `887b6af` (C1 freshness), `84b9c9b` (records); base `75f671b`.

## Verdict

**DEFECT (medium). The round's no-harm claim is refuted on operability and calibration at `84b9c9b`.** In a clean, fleet-shaped clone, the records commit turns the checklist gate from 11/11 exit 0 into 10/11 exit 1. The cause is a dangling governance citation the commit added. The build-wave battery reported "same 2 ids" because it ran in a non-fleet layout, where the same check id was already failing, so the new failing site was hidden.

Depth also has one low-severity harm: `d1ae458` makes an unreadable configured root abort the whole instrument (exit 2) where the base exits 0. I reproduced peer A24's finding.

Consistency, coverage, freshness and adjacency show no round-caused harm at the three target commits. The commits made after my assignment (`d28b16b`, `2788704`) add new reds on consistency/calibration and operability (see "Later tip" below).

| Axis | Verdict | Harm caused by the round? | Pre-existing red, same at base and tip |
|---|---|---|---|
| depth | DEFECT low | yes, edge input: unreadable configured root, exit 0 → 2 | live join exit 2 (`false blocker`, session-carrier race) |
| consistency | CONFIRMED (at the 3 targets) | no; both corpus instruments exit 0 and agree | — |
| coverage | CONFIRMED | no; the gate reads no file the round changed | surfaces exit 1, 5/7 (omp 18.12.6) |
| operability | **REFUTED / DEFECT medium** | yes: checklist gate exit 0 → 1 at `84b9c9b` | — |
| freshness | CONFIRMED (one new warning class) | no failing gate; 3 new W04 census warnings | pins exit 1, DRIFT 2/3 (omp 18.12.6) |
| calibration | **DEFECT medium** | yes: same governance gate (round-47 C3) red; no-harm evidence was blind to it | — |
| adjacency | CONFIRMED | no; replay inputs untouched, pin-bypassed counts identical | replay exit 1 `instrument_drift` |

## Method

- Private clones under `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A32NoHarmCritic/`. `fleet-base/kotoba-shokunin` is at `75f671b`; `fleet-tip/kotoba-shokunin` is at `84b9c9b`. Each sits beside fresh read-only copies of the fleet-root files the checklist gate resolves (AXES/MISSION/PROTOCOL/SCORECARD, `shokunin.conf`, `scripts/sources-census.sh`, 5 reports, 31 wave members, 2 kasegi instruments). That is the same file list the build seat FrCensusAndScorecard used. I did no lane, fleet or sibling VCS writes.
- I ran the same 24-gate battery (`battery.sh`) at both trees under `PYTHONDONTWRITEBYTECODE=1`. Outputs are in `out-{base,tip}/`. I diffed them after normalizing paths and revisions.

## Per-axis evidence

**Depth (`d1ae458`).**
- No harm on the measured surfaces:
  - The committed receipts `before-configured-root.json` (`8bec447a…`) and `after-configured-root.json` (`47e41ea9…`) cover 13 cases × 27 non-target rows. Value changes: 0. Status changes: 0. Exit changes: 0. Only `oc.roots.names_plus_builtin` moves (2→3, 2→3, 2→4, 2→3, 3→4 on the 5 target cases); the 8 controls are unchanged.
  - Live host, `verify_harness_independent.py --json`: exit 0 at both trees. All 28 rows have identical value and status; the configured-roots row is 10 at both, because both configured roots are absent here.
  - `--self-test`: exit 0, 104 → 115.
  - `verify_harness_claims.py`: exit 1, 21/28, same 7 DRIFT ids at both trees.
  - `compare --self-test`: exit 0, 0/330 at both.
- **Harm, low severity (Q18 class, a new false red):**
  - Case: `--oc-config` whose `skills/` directory has mode 000.
  - Base: exit 0. Tip: exit 2, `SUBSTRATE [Errno 13] Permission denied: …/unreadable-case/oc/skills`, no traceback.
  - Cause: the unguarded `iterdir` over configured roots.
  - Independent reproduction of `.ufo/waves/round-48/falsify/A24UnreadableRoot.md`.
- **Not a harm (strongest counterexample tested):** on a host with a populated singular `~/.config/opencode/skill/`, the instrument now exceeds the producer. The producer's root list at `verifiers/verify_harness_claims.py:472` has only the plural `skills`. The shipped opencode 1.19.3 bundle (`~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode`, sha256 `179ca421…` = the committed pin) contains `SA="{skill,skills}/**/SKILL.md"`. So the instrument is the more faithful side, and the divergence is an honest producer gap. It is [INFERENCE] for live, since no singular root exists here; the SCORECARD row discloses that the live row is unchanged on this host.
- Pre-existing: `compare_harness_independent.py --json` exit 2 ×2 at both trees, with identical `false blocker` lines (`candidate_blocks` 5934 vs 5935, then 5935 vs 5936). The race fires identically, so this battery cannot observe the join's values. The build battery's non-race runs show 18/24, 6 disagreements, identical at base and landed.
- Calibration side note: the arm `"round 48: the row's evidence names the configured roots"` can only fail through its `skills` half. Its `skill` half is always true from the fixed words "distinct skill names". A mutant that drops the root list fails only the `skills` half (`got (True, False)`).

**Consistency (calibration sub-axis).**
- `verify_corpus_integrity.py --json`: exit 0, all PASS at both trees.
- `verify_corpus_independent.py --json`: exit 0 at both.
- `tracked_files` 61 → 63 equals the 2 new indexed files (baseline re-recorded in-step). `report_total` 40/40, `commit_total` 30/30, and `unindexed`, `missing_paths` and `report_dead` are 0 at both trees. The two instruments agree.
- `fault_injection_corpus.sh`: `verdict: ALL PASS` at both trees, byte-identical after normalization. `--self-test` exit 0 at both.

**Coverage.**
- `verify_surfaces.py --json`: exit 1, pass 5 / fail 2 (`literal_present`, `no_uncovered_class`). Byte-identical at both trees.
- `--self-test`: 0/99 at both.
- The gate reads only `corpus/knowledge/instruction-surface-census-round13.md`, which no round-48 commit touched. `surfaces-baseline.json` is also unchanged (`git diff --stat 75f671b 84b9c9b`).

**Operability (`84b9c9b`).**
- `verify_skill_checklist.py --json`:
  - Base: exit 0, pass 11, 872 governance tokens.
  - Tip: exit 1, pass 10 / fail 1, 901 tokens. Failing site: `governance.citation_resolves`, `SCORECARD.md:110: '.ufo/reports/round-48/kotoba.md' does not resolve`. No such file exists in the lane, and the fleet tree has only `round-48/kotodama.md`.
- `--self-test`: 0/1845 at both.
- `check_assertion_floors.py`: exit 0, 9/9 PASS at both (`harness_independent` 104/104 → 115/115).
- Why the build wave missed it: `.ufo/waves/round-48/build/C1NoHarmBattery.md` ran in non-fleet clones, where `governance.citation_resolves` was already FAIL on `../` targets. Its landed column, "pass 9 / fail 2 (same 2 ids)", compared ids, not sites, so the new site was invisible.

**Freshness.**
- `check_substrate_pins.py`: exit 1, DRIFT 2/3 (omp sha `85d9daf3…` ≠ pin `fdbc8136…`, plus mtime). Byte-identical at both trees. `--self-test`: 0/62 at both.
- `sources-census.sh validate`: exit 0 at both. The tip adds 3 W04 warnings: S018, S019 and S021 have duplicate URLs across scopes, from the superseding rows. LOG discloses them. They are non-failing noise, not harm.
- `census`: rows 15 → 21, tier A 14 → 20, mined 6 → 12.

**Calibration.**
- The operability red is also the round-47 C3 calibration gate. That gate's governance check is what fails.
- The round's records list "Observed, not caused by this round" reds (LOG round-48 entry). That list omits the one red the round did cause, so the no-harm provenance is overstated.

**Adjacency.**
- `HEAD frozen` and `HEAD live` replays: exit 1 `instrument_drift` at both trees.
- `verify_skill_checklist.py` has sha256 `4ea2100d…` at both trees; none of the three commits touch it or the routing JSON.
- I ran the same count code with only the instrument pin replaced by the current digest (scratch copy). Frozen mode gives exit 0 and the same counts at both trees: subjects 226, unresolved 14, classified 14, unclassified 0, actionable 4, routes 3.
- Live mode is unrunnable in scratch (sibling `SKILL.md` absent).

## Later tip (outside the three targets, measured because it is the lane's live state)

The lane advanced to `d28b16b`, then `2788704`, while I ran. `d28b16b` rewords the `SCORECARD.md:110` pointer to prose, which repairs that site. It also introduces two new reds, both still present at `2788704` in clean fleet-shaped clones:

1. `governance.citation_resolves` FAIL: `SCORECARD.md:112` cites `.ufo/waves/round-48/falsify/A24UnreadableRoot.md`, which is untracked (`git ls-files --error-unmatch` fails). The real lane checkout reads 11/11 only because that file is on disk, so the gate is green on the working tree and red on the committed tree.
2. Both corpus instruments exit 1, 7/9: `report_total` 41 ≠ 40 and `report_dead` 1. The site is `corpus/lessons/round-48.md:21`, citing `.ufo/reports/round-47/kotoba.md`, which exists only in the fleet repo. This reproduces in the real lane checkout too (`LANE_CI_EXIT=1`, `LANE_CIND_EXIT=1`).

## Smallest safe corrections

1. Before landing, every pointer the round adds to `SCORECARD.md`, `LOG.md` or `corpus/` must resolve at the committed tree:
   - Commit the cited falsify reports, or reword the pointer as prose (the `d28b16b` idiom).
   - Write the round-47 report pointer host-absolute (the round-46 idiom), or use prose.
   - Then re-run `verify_skill_checklist.py --json` and both corpus instruments in a clean fleet-shaped clone, not in the working tree.
2. Guard configured-root enumeration against `OSError`: skip the root, or mark it unavailable, with a regression arm (A24's remedy).
3. No-harm batteries compare failing sites, not check ids, and run in a fleet-shaped clone.

## Bounds and tools

- Writes: scratch paths above and this report only. Reading the lane ran `git status` (it may refresh the index stat cache). Lane gate runs were read-only (`-B`, no bytecode).
- I ran `opencode --version` once by mistake. `~/.local/share/opencode/log/opencode.log` mtime stayed 2026-10-20 07:52, so the log was not perturbed.
- No web sources opened. No tools installed or upgraded (system `python3`, `git`, `sha256sum`).
- Not run: the ruler at `84b9c9b` (its receipt was checked instead); the live join's values (race); live adjacency mode.
