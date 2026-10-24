# RevW2NoHarm — round-63 wave-2 no-harm battery at cbbee56e

role: reviewer (wave-2 falsify, no-harm battery)
item: RevW2NoHarm
attack: re-ran the assigned no-harm arms at lane tip `cbbee56e9a3589b0b46736ad36f1b77701def80e`,
re-ran the frozen round-62 `noharm-battery.sh` (its canonical two-column form) with
`--base 35d44b4b4dcdda234b5dbff7af37e432fec55f05 --tip cbbee56e…` in a `/tmp` sandbox, and
extended the sweep to every registry-listed lane gate, comparing base-column vs tip-column
outputs for each one not already covered by the battery. Lane bytes untouched; all probes
ran read-only or in `/tmp/kotoba-r63-noharm-revw2`.

## Verdict on the committed bytes

**NO-HARM — no defect named.** At `cbbee56e` the canonical battery prints `no-harm OK`
(21 PASS arms, 0 FAIL, including its three vacuity self-checks). Every prior frozen receipt
reproduces verbatim; every still-red gate observed at tip is byte-identical in the
base column, i.e. pre-existing, not wave-1 damage; `check_gate_finding_delta` confirms
`new: none`. The v32/routed-repairs additions and the SKILL/QUALITY/SOURCES/LOG/README/
PROVINCE edits regressed no prior gate.

## Arm 1 — `check_gate_registry.py --rev cbbee56e…`

```
… (all 41 rows print OK) …
gate registry rows conformant 41 of 41 lane verifiers; phantom 0
EXIT=0
```

Both new verifiers (`check_scoped_rules_v32.py`, `check_r63_routed_repairs.py`) carry
registry rows in SKILL.md (added +2 lines). Up from `39 of 39` at base `35d44b4b`
(wave-1 evidence, `ExecNoHarmBaseline.md`) — the two r62 interim reds (`36 of 38`,
no rows for the r62 instruments) were already fixed at base.

## Arm 2 — `check_erratum_absorption.py --self-test`

```
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
EXIT=0
```

Byte-identical to the frozen r62 receipt `.ufo/waves/round-62/C1-absorb-measure.txt`
(`absorbed 2 of 5; surviving 6` — it measures the pinned v3 counter `5a5adc94…`, not v32;
the G9 survivor persisting *here* is correct because the instrument is pinned to the
pre-v32 counter, and its file is unchanged at tip). **Frozen receipt: intact.**

## Arm 3 — `check_scoped_rules_v31.py --self-test`

```
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858
… (W1–W7 world lines, W0 exit=1) …
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2f-compound-purpose-outside-citation: before accepted; after accepted
survivors closed 5 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
self-test: 0 failure(s) over 201 assertions
EXIT=0
```

Matches the plan's expectation verbatim: `survivors closed 5 of 6` plus the
`bound: G9 remains unimplemented…` line, self-reported sha `a07c2269…` == the plan's pin.
The do-nothing control is unweakened at tip (v31 must stay 5-of-6 for C1's control to be
meaningful). **Frozen receipt: intact.**

## Arm 4 — `check_skill_checklist.py` (misnamed; actual: `verify_skill_checklist.py`)

The assigned command fails at ENOENT — no such file exists at *either* revision
(`git ls-tree` on both = 0 rows). Running the real gate:

```
python3 -B verifiers/verify_skill_checklist.py
FAIL governance.citation_resolves: evaluated 1164 — LOG.md:2533: '.ufo/reports/round-60/kotoba.md'
does not resolve from <lane>; SCORECARD.md:158: '.ufo/reports/round-60/kotoba.md' does not resolve
from <lane>; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused
EXIT=1
```

Same check id FAILs in the **base** column (`evaluated 1157`, identical two unresolved
pointers — `check-ptr base=2 tip=2`). LOG.md:2533 sits in the r60/r61 entry block,
which wave-1 did not touch (wave-1 appended lines 2567–2575 only). **Pre-existing red,
not a regression; pointer count unchanged.** The lane red is a structural misroot
(fleet paths unresolvable from the lane), noted not asserted as a defect by this item.

## Arm 5 — `verify_harness_claims.py`

```
python3 -B verifiers/verify_harness_claims.py
INCONCLUSIVE: template anchor occurs 0x in /home/vgpnk/.local/bin/omp (want 1)
EXIT=2
python3 -B verifiers/verify_harness_claims.py --self-test
self-test: 0 failure(s) over 10 assertions
EXIT=0
```

`~/.local/bin/omp` is now a **bash wrapper script** ("# omp crash-restart wrapper"),
not the ELF the gate was written against — host drift, not lane damage: the gate is
tree-independent (it probes host binaries/logs), and `verify_harness_independent.py` /
`compare_harness_independent.py` / `check_substrate_pins.py` hit the identical INCONCLUSIVE
/`omp_binary_sha256, omp_binary_mtime` DRIFT on **both** sandbox columns. **Gate verdict:
could-not-evaluate (exit 2), environment-limited, identical at base and tip.** Not a
lane regression; flagged as a substrate finding.

## Canonical two-column battery — `.ufo/waves/round-62/noharm-battery.sh`

```
bash .ufo/waves/round-62/noharm-battery.sh \
  --base 35d44b4b4dcdda234b5dbff7af37e432fec55f05 \
  --tip  cbbee56e9a3589b0b46736ad36f1b77701def80e \
  --sandbox /tmp/kotoba-r63-noharm-revw2 --keep
noharm: column base ready (35d44b4b4dcdda234b5dbff7af37e432fec55f05)
noharm: column tip ready (cbbee56e9a3589b0b46736ad36f1b77701def80e)
--- arms ---
PASS  reg_gate    exit 0 in both columns (base=0 tip=0)
PASS  corpus      tip introduces no new DRIFT kind (base set: corpus.index.tracked_files: corpus.index.unindexed: corpus.pointers.commit_total: corpus.pointers.commit_unresolvable: corpus.pointers.report_total: )
PASS  corpus-idx  no new unindexed corpus file at tip (base set: corpus/lessons/round-62-verifier-spotcheck.md )
PASS  sources     exit 0 in both columns (base=0 tip=0)
PASS  checklist   tip introduces no new failing check id (base set: governance.citation_resolves: )
PASS  check-ptr   unresolved citation pointers did not grow (base=2 tip=2)
PASS  boxproof    exit 0 in both columns (base=0 tip=0)
PASS  floors      exit 0 in both columns (base=0 tip=0)
PASS  agentdefs   exit 0 and normalized output identical in both columns
PASS  explicit    exit 0 and normalized output identical in both columns
PASS  desc        exit 0 and normalized output identical in both columns
PASS  mcp         exit 0 and normalized output identical in both columns
PASS  plugin      exit 1 and normalized output identical in both columns
PASS  hooks       exit 0 and normalized output identical in both columns
PASS  scoped      exit 0 in both columns (base=0 tip=0)
PASS  absorption  check_erratum_absorption.py self-test exited 0 at tip
PASS  repairs-v2  check_routed_repairs_v2.py self-test exited 0 at tip
PASS  scoped-v31  check_scoped_rules_v31.py self-test exited 0 at tip
PASS  battery-self a mutated verdict line was detected by the comparison (battery is not vacuous)
PASS  battery-self2 an injected new corpus DRIFT kind was detected by the comparison
PASS  battery-self3 an exit-2 (could-not-evaluate) column is caught by the comparison guard
no-harm OK
BATTERY_EXIT=0
```

Notes on `corpus-idx`: at **both** columns the single unindexed file is
`corpus/lessons/round-62-verifier-spotcheck.md` — the r62 spot-check commit `35d44b4b`
itself introduced it unindexed (the older `round-61-verifier-spotcheck.md` routed defect
is repaired). Same file, same count at base and tip → the PASS is honest; the residual
unindexed lesson is pre-existing damage the round may optionally sweep, not a wave-1
regression. `plugin` exits 1 in **both** columns (pre-existing opencode
`.opencode/plugins/` token reject). `--fetch` arms all normalized-identical — live
fetches stable this run.

## Extended gate sweep (outside the battery's 13 arms)

| Gate | base col | tip col | verdict |
|---|---|---|---|
| `check_gate_finding_delta.py --base 35d44b4b --head cbbee56e` | — | — | `base drift 5, head drift 5; new: none; resolved: none`, exit 0 — **zero new findings** |
| `check_seat_counts.py --spec w1-spec.json --dir w1 --rev cbbee56e` | — | — | `seat reports committed 32 of 32; missing 0; unmatched 0`, exit 0 |
| `check_infoless_fences.py --rev <col>` | exit 0 | exit 0 | PASS both (seeded `wrong 33 … status=FAIL` cases identical; claim-withdrawn instrument) |
| `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md` | `rows 20 verified 20` exit 0 | same | PASS both — the PROVINCE.md +1 bullet broke nothing |
| `check_command_files.py --rev <col> --fetch` | exit 0 | exit 0 | PASS both (live fetch identical) |
| `check_could_not_evaluate.py --rev <col>` | `probes 29/29; controls 13/13; red anchors 12/13` | identical | identical red (12/13 anchors) in both columns — pre-existing |
| `check_agentdef_boxes.py --rev <col>` | exit 1 | exit 1 | identical red: 9 `not counted` lines (withdrawn claim, non-gating) |
| `check_opencode_repin.py --rev <col>` | exit 1 | exit 1 | identical: `surfaces pass 5 of 7; pins OK 1/3` |
| `check_substrate_pins.py` | exit 1 | exit 1 | identical host DRIFT (omp wrapper) — not tree-dependent |
| `verify_surfaces.py` | exit 1 | exit 1 | identical FAIL ids (`surfaces.literal_present`, `surfaces.no_uncovered_class`) — same host-substrate cause |
| `verify_corpus_independent.py` | exit 1 | exit 1 | `!` violation sets diff-clean identical (18 lines) |
| `verify_dispatch_prompts.py` | exit 1 | exit 1 | identical: same 6 failing files (sibling-lane prompts, outside this lane's diff) |
| `verify_harness_independent.py` | exit 2 | exit 2 | identical could-not-evaluate (host omp wrapper) |
| `compare_harness_independent.py` | exit 2 | exit 2 | identical could-not-evaluate |
| `fault_injection_corpus.sh` | exit 1 | exit 1 | identical: `fault-f | integrity | FAIL`; logs differ only in sandbox paths (2 lines) |
| `verify_alwayson.py --check alwayson.04/.07 --target .` | — | exit 0/0 | PASS at tip (no AGENTS/CLAUDE pairs added) |
| `check_correction_sweep.py`, `check_sweep_mutants.py`, `check_assertion_floors.py`, `check_overlap_levers.py` | — | exit 0 | PASS at tip (floors `alwayson 89/89`, `correction_sweep 25/25`) |
| `check_scoped_rules_v32.py --self-test` | — | exit 0 | C1 receipt verbatim: `worlds reject 7 of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`, `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`, sha `42460691…` |
| `check_r63_routed_repairs.py --rev cbbee56e` | — | exit 0 | `r62 routed defects closed 5 of 5` (all 5 PASS lines incl. `prefix=True grew_by=9`) |

`git diff 8c4cefa..cbbee56e -- verifiers/` touches exactly two paths, both **new files**
(v32, routed counter); no pre-existing verifier was modified. Doc edits are one-line
appends/replacements only; `check_sources_append_only.py` exits 0 in both columns.

## Advisory observations (not defects against the wave-1 claims)

1. **Assignment typo:** `check_skill_checklist.py` does not exist at any landed revision;
   the gate is `verify_skill_checklist.py`. Worth a dispatch-template fix if the w2
   prompts are regenerated.
2. **Pre-existing red set (column-identical, host/substrate or fleet-scoped):**
   `governance.citation_resolves` (2 misroot fleet pointers), `surfaces.literal_present`
   + `no_uncovered_class` (omp wrapper), `dispatch.04` (6 sibling-lane prompt files),
   `check_substrate_pins`/`check_opencode_repin`/`verify_harness_*`/`compare_*`
   (omp now a bash wrapper — `verify_harness_independent.py --freeze` is the
   environment fix, out of scope), `verify_corpus_independent` (18 `!` lines,
   identical), `agentdef_boxes` (withdrawn-claim gate), `fault_injection_corpus`
   `fault-f` integrity FAIL (identical at both revs — a pre-existing detection gap,
   not introduced by wave-1).
3. **Working-tree hygiene:** `receipts.new-C1.txt` and `receipts.new-C2-interim.txt`
   sit untracked at the lane root — the same class as r62 routed defect 1. Not a
   committed-bytes defect; flagging so the L1 commits or removes them before the
   r63 close receipt.

## Smallest safe correction

None required — no regression found. The only text-level suggestion is the dispatch
template's `check_skill_checklist.py` → `verify_skill_checklist.py` rename if wave-2
item text is ever regenerated (one-word correction).

## Residual risk / verification gaps

- Live `--fetch` arms passed normalized-identical *this run*; a mid-run page flip would
  show as a false FAIL, not a false PASS (battery design).
- `check_could_not_evaluate.py --rev` printed `probes honoured 29 of 29; controls held
  13 of 13; red anchors held 12 of 13` in **both** columns — the one held-anchor miss
  (12/13) is identical at base and tip, so it predates this round.
- Host `omp` drift prevents evaluating the harness-claims family on any revision;
  its lane-relevant inputs (baseline.json, scope JSON) are unchanged, but the family
  cannot certify bytes it cannot execute against.
