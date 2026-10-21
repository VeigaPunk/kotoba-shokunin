verdict: PARTIAL — planter fails closed for absent/rowless sections, but accepts non-coverage and fenced decoys as successful d1/d2 plants

## Scope and axes

Reviewed `verifiers/fault_injection_corpus.sh` at **7ad7fadfc09354b74fb66605dfb0c1182c115a2f**, specifically the round-47 index-row planter change. Axes: **operability** (reliable fault placement), **calibration** (a successful plant must actually enter the checked population), **freshness** (no substrate-freshness claim tested or contradicted here). This is a lane-authored review, not admission or closure.

## Finding: successful plant can be invisible to both corpus instruments

**Fixable defect; operability and calibration.** `verifiers/fault_injection_corpus.sh:117` selects the *first prefix match* for `## Coverage map`, without checking exact heading identity or fenced context. Lines 118–121 then insert after the last pipe-starting line in that selected region. The d1 guard at **:205–206** and d2 guard at **:212–215** verify marker presence anywhere in README, not membership in the live coverage map.

Strongest fixture: place a fenced example coverage map before a real live coverage map:

```markdown
# Fixture

```markdown
## Coverage map

| Area | File | Basis |
|---|---|---|
| Existing | `knowledge/real.md` | fixture |
```

## Coverage map

| Area | File | Basis |
|---|---|---|
| Existing | `knowledge/real.md` | fixture |
```

(The inner fence is literal README content; the executable fixture is defined without formatting ambiguity in the attached probe.) Both exact shipped shell functions return **0**, planting into the fenced example at fixture README line 9. Author `index_findings` reports **missing_paths=0, stale_patterns=0, unindexed=0** and classifies the injected token as fenced. Independent `coverage_cells` does not include the injected token. Thus the planted fault is not a live index promise.

A second, simpler counterexample has `## Coverage map example` plus a table before the exact `## Coverage map`. Both d1/d2 return **0**, place their marker at fixture README line 6 in the wrong section, and both instruments exclude it from coverage. Author results remain **missing_paths=0, stale_patterns=0, unindexed=0**; independent records the marker outside coverage.

This is not evidence that the *whole harness* silently passes. `fault_must_fire` at **:265–272** proceeds to instrument evaluation after these false-success plant guards; its exit-zero handling at **:275–276** would report MISS rather than INVALID-PLANT [INFERENCE from code, not a full-harness execution]. The defect is silent wrong placement at the planter boundary and resulting misattribution to the detector, not an observed false ALL PASS.

Parser authorities differ from the planter: `verifiers/verify_corpus_integrity.py:366–383` requires the coverage heading predicate and `:400–402` removes fenced tokens from live checks; `verifiers/verify_corpus_independent.py:265–282` skips fences and requires exact heading equality at :272. A raw `startswith` plus marker grep does not establish the semantic postcondition those parsers require.

## Requested edge cases that held / conditional behavior

Each row was executed for **both** `plant_d1` and `plant_d2` using their exact shipped function definitions:

| Fixture | d1 exit | d2 exit | Observed result |
|---|---:|---:|---|
| Normal coverage map followed by Frontier table | 0 | 0 | Marker enters live coverage; d1 missing_paths=1, stale_patterns=1; d2 missing_paths=0, stale_patterns=1. |
| Coverage heading absent, unrelated table remains | 1 | 1 | `StopIteration`; README unchanged; no marker. Fails closed. |
| Coverage heading present but no pipe rows before next heading | 1 | 1 | `ValueError: max() iterable argument is empty`; README unchanged. Fails closed. |
| Empty table meaning header + separator, no data rows | 0 | 0 | Marker becomes first data row and is live to both parsers. Not a wrong-place defect. |
| Two exact, non-fenced coverage maps with data rows | 0 | 0 | First map selected. Both parsers recognize the injected token; duplicate heading alone is not a demonstrated defect. |
| Two exact coverage headings, first has no table rows | 1 | 1 | First section wins; `max()` fails despite a usable later section. Fails closed, availability tradeoff. |
| Prefix decoy before exact coverage map | 0 | 0 | Wrong-section plant, ignored by live coverage parsers. |
| Fenced example coverage map before live coverage map | 0 | 0 | Fenced plant, ignored by live coverage parsers. |

For failure cases d2 creates its untracked payload file before attempting insertion (`fault_injection_corpus.sh:210–212`), so “fails closed” means no accepted/indexed plant, not an entirely unchanged world. The caller turns failed planter status into INVALID-PLANT at :265–267; `row` sets FAIL for that verdict at :253–258 [code-read].

## Smallest safe correction

Keep the section-local insertion, but select an **exact live coverage heading outside fenced regions**, with the same section/fence semantics as the instruments. Make ambiguity policy explicit: fail closed if more than one eligible live heading remains, or deliberately support the shared parsers' multi-section semantics. Exact duplicate live sections are not inherently wrong today, so rejecting them is a conservative policy choice rather than a proven correctness requirement.

Before returning successful plant status, establish that the inserted row belongs to the selected live coverage table, not merely that its path string exists somewhere in README. Add absent-heading, rowless-section, header-only, duplicate-first-empty, prefix-decoy, and fenced-decoy fixtures. The absence/empty guards already reject mutation; they need clearer diagnostics, not fallback insertion into unrelated tables. No production correction was applied.

## Commands, evidence, and reproduction

1. In `/fast/scratch/kotoba-r47/w2/W2FaultPlanterEdge/kotoba-shokunin`, `git rev-parse HEAD` — **exit 0**, output `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.
2. Executed:

   ```sh
   python3 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/falsify/W2FaultPlanterEdge.probe.txt /fast/scratch/kotoba-r47/w2/W2FaultPlanterEdge/kotoba-shokunin
   ```

   **Exit 0**. Probe extracts exact `insert_index_row`, `plant_d1`, and `plant_d2` shell functions from the checked-out target, invokes each with `bash -c` against 16 newly created fixture worlds, and runs the shipped author's `index_findings` plus independent `coverage_cells` over the resulting README. Each fixture's `git init -q <world>` exited **0**; the per-planter exit codes and full author findings are in `W2FaultPlanterEdge.results.json`. Probe exit 0 means observation collection succeeded, not that every fixture had a successful plant. Fixture git repositories are uncommitted: these probes deliberately exercise the helpers and parser functions directly, not the harness's committed-state cloning path.
3. Repro source: `.ufo/waves/round-47/falsify/W2FaultPlanterEdge.probe.txt`; raw observations: `.ufo/waves/round-47/falsify/W2FaultPlanterEdge.results.json`. Scratch fixture world paths are included in that JSON. All fixture writes were under the unique scratch directory; only this report and named small artifacts were written in the production lane.

## Not checked

Did not rerun the complete fault harness or its self-test, corpus verifier CLI/baseline modes, counting commands outside the assigned planter scope, C1 binaries/strings/pins, C2 XML behavior, governance errata, source rows, or the canonical Rust judge. No full-harness exit code is claimed for these mutations. No tools were installed or updated. No production code, Git index/refs, historical receipts, or sibling lanes were changed.
