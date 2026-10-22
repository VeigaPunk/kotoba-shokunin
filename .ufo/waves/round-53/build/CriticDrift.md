Result: BREAKS — the plan's disposition of the drift sentinel is contradicted by the lane's own records: C2 sits in the same frontier area ("executed checklist coverage") that rounds 49 and 50 worked. C1 is the third freshness claim running on `verify_surfaces.py` loader extraction, and it meets the lowest-axis duty only under the all-axes reading. The no-harm guards leave out six lane gates that read files this round writes.

Seat: `KotobaR53.CriticDrift` (critic, wave 1 build). Judged on: calibration. The sandbox is `/fast/scratch/hyaku/kotoba-r53/CriticDrift`, a clone at plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`. Nothing in the lane was written except this report. No tools were installed or updated.

## Severity summary

| # | Finding | Severity | Kind |
|---|---|---|---|
| F1 | Routed defect 5 (drift sentinel) has a disposition that rests on a false premise: C2 is not a different frontier area | HIGH | the plan text is fixable; whether the sentinel action is met is the judge's ruling |
| F2 | C1 repeats the freshness axis on the `verify_surfaces.py` extraction surface a third round running, and the lane's own tie-break is silently reversed | MEDIUM | tradeoff for the judge plus a disclosure defect |
| F3 | Lowest-axis duty: met under the all-axes reading (freshness 8); unmet under the owned reading (depth 9), and no waiver applies | MEDIUM | tradeoff for the judge plus a disclosure defect |
| F4 | No-harm guards are incomplete: six gates that read round-written files are not named, including the instrument behind consistency 10 | MEDIUM | fixable |
| F5 | The named guard `verify_skill_checklist.py` does not run C2's new delegate (the carried D2 fail-open) | MEDIUM | fixable |
| F6 | Routed defect 4 is applied to the archived round-52 counter in place, so the path the round-52 record names stops being the frozen counter | LOW (MEDIUM if the round-52 SCORECARD row is left unqualified) | fixable |
| F7 | The C1 statement carries an omp clause the counter does not print, although the plan says each statement is "the counter's printed line and nothing more" | LOW | fixable |
| F8 | C1 and C2 are separable at the counter level, but C2's knowledge content about opencode depends on C1's re-derivation | LOW | fixable |
| F9 | C2's live-population run reads a file shared with kagi; the plan has no routing rule for findings on it | LOW | fixable |

## F1 — HIGH: C2 is in the same frontier area as rounds 49 and 50

**Counterexample.** `plans/round-53.md:16-18` says "C2 works a different frontier area: executed checklist coverage of the always-on (AGENTS.md-class) constraint-file checklist … (`corpus/README.md` § Frontier, first row)". The lane's own round-49 plan uses the same area name for its C2: `plans/round-49.md:48`: "### C2 — operability (8.5): dispatch-prompt checklist boxes executed (frontier area: executed checklist coverage)". Round 50's C2 (`plans/round-50.md:32`, box proof deletion-enforced) hardened that same delegate and box-proof path. Rounds 49, 50 and 53 are also the same claim template: operability, 2 boxes moved from `unexecuted:` to `delegated:` in `verifiers/checklist-baseline.json`, and an instrument proven on pinned cases (round 49: `boxes proven 0 → 2`; round 53: `0 of 8 → 2 of 8`).

**Evidence.**
- `corpus/README.md:87` is the row the plan cites. It is one row, and it explicitly bundles the dispatch boxes worked in round 49 with "the agent-definition and always-on checklists". `PROVINCE.md:26` lists "Executed checklist coverage" as one Frontier item. The lane's own taxonomy treats always-on and dispatch box execution as one area.
- Frontier areas worked in rounds 50–52: sibling arbitration (r50 C1, r51 C2), executed checklist coverage (r50 C2), loader-rule freshness (r51 C1, r52 C1), MCP/plugin instruction surfaces (r52 C2). Round 53 works loader-rule freshness (C1) and executed checklist coverage (C2), so both claims fall inside that set. Three rows are untouched in rounds 49–52: command extraction (`corpus/README.md:88`), implicit-intent fidelity (`:89`) and per-render consumption (`:92`).
- The sentinel's defect class has a history in this area. Of the three routed instances that tripped it (`.ufo/waves/round-52/falsify-a2/CriticLearning.md:71-78`), two concern this area: round 50 D2 (the box-proof docstring "discriminate every conjunct") and round 51 D2 (`SCORECARD.md:31`, "the checklist gate runs `--box-proof` with no fail-open bound").
- The binding sentinel row is `.scratch/goal-20261022-hyaku-12h.md:173`: "Same axis+surface claim or same routed defect class in a lane 3 rounds running | The lane's next round must work a different frontier area." The closure routed it as `corpus/lessons/round-52-verifier-spotcheck.md:127`.
- The plan sentence "C2 works a different frontier area" is unverified, and the lane's own records falsify it. That makes it an instance of the sentinel's own class: a record wider than what was verified.
- `ReviewSpotcheckRouting.md:15,25` marks item 5 as "dispositioned", which is true at the level of having a line. This finding contests what that line asserts, not whether it exists.

**Impacted axes:** calibration (the plan record), and admission of the round shape against the sentinel. C2's own counter result is not affected.

**Smallest safe correction.** In the plan erratum and the report, restate the routed-defect-5 disposition as: "C2 is in the frontier area of rounds 49–50 (executed checklist coverage, always-on sub-checklist); the sentinel's 'different frontier area' action is not met by area. The record-width class is mitigated only by Q26 and Q31 statements." Then let the judge rule. Moving C2 onto an untouched Frontier row would need a new plan commit and a new frozen counter (Q28), so it cannot be done inside this attempt's freeze.

## F2 — MEDIUM: C1 is the third freshness claim running on the same surface, and the tie-break is reversed

**Counterexample.**
- Freshness claims: r51 C1 (omp re-pin, `verify_surfaces.py`), r52 C1 (omp callee rename, `verify_surfaces.py`), r53 C1 (opencode OC-4/OC-6 re-derivation, `verify_surfaces.py` plus pins). All three sit in the Frontier row "Loader-rule freshness" (`corpus/README.md:91`, `PROVINCE.md:27`).
- The round-52 critic left a watch item: `CriticLearning.md:35-39`, "round 53 must not claim freshness on omp extraction in `verify_surfaces.py` again".
- Two readings:
  - Harness-level surface (omp versus opencode): no trip.
  - Gate-level or Frontier-row surface: the axis+surface trigger trips at its third occurrence.
- The plan names neither reading.

**The tie-break is reversed.** Rounds 51 and 52 broke the freshness/adjacency tie by recency: `plans/round-52.md:11-12`, "Adjacency was claimed in rounds 49 and 50, so C1 works freshness" (same at `plans/round-51.md:10-11`). The same rule at round 53 picks adjacency: freshness was claimed in r51 and r52, and adjacency was last claimed in r50. `plans/round-53.md:10-12` states the tie and picks freshness without giving a tie-break.

**The duty is discharged by a forced repair.** C1 is routed defect 1 (`plans/round-53.md:66`, "this is C1"). The closure ruled the 1.19.4 drift "not harm … a red gate routed to its owner" (`round-52-verifier-spotcheck.md:73-79`). The lowest-axis duty is therefore met by a repair the round owed anyway. That is a tradeoff the judge rules on, not a defect the lane can fix in place.

**Impacted axes:** freshness (the claim's standing as an axis-move) and calibration (disclosure).

**Smallest safe correction.** The plan erratum and the report should state three things: the surface granularity the lane reads the sentinel at, that the r51/r52 tie-break rule would have picked adjacency, and that C1 is routed defect 1 promoted to a claim. The judge then rules.

## F3 — MEDIUM: the lowest-axis duty holds under one reading only

- **All axes.** Axis scores at base (`SCORECARD.md:28-34`): depth 9, consistency 10, coverage 8.5, operability 8.5, freshness 8, calibration 8.5, adjacency 8.0. The lowest is 8, a tie between freshness and adjacency. C1 works freshness, so the duty is **met**, subject to F2's tie-break point.
- **Owned axes.** `SCORECARD.md:3` reads "Axes owned by this lane: **depth + consistency**", and the round prompt §1 reads "Your lane axes: depth + consistency". The lowest owned axis is depth 9. If the consistency sub-axis is read as owning its parent (`SCORECARD.md` § Saturation: "depth and the consistency/calibration sub-axis"), the lowest is calibration 8.5. Either way, neither C1 (freshness) nor C2 (operability, advisory) works an owned axis, so the duty is **unmet**.
- **No waiver.** `AXES.md:66-73` waives the duty only when every owned axis is at or above the saturation line. The lane's own § Saturation says "depth sits below the line, so **the nudge is dormant**".
- **Two readings in one file.** The lane reads "owns" as the owned-proxy for the nudge (§ Saturation) but as all axes for the duty. These are two authorities for one word in the same file.
- **Round 51 met both readings.** `plans/round-51.md:10` says "under the all-axes reading" for C1, and `:26` gives C2 "depth (owned axis, lowest owned at 9)". Round 53 meets only the all-axes reading, and unlike round 51 it does not name the reading it uses.

**Impacted axes:** depth (no claim) and calibration (the reading is unstated).

**Smallest safe correction.** State in the plan erratum and the report: "lowest under the all-axes reading: freshness and adjacency at 8; under the owned reading, depth 9 carries no claim this round, and the nudge is dormant." The judge rules on which reading binds.

## F4 — MEDIUM: the no-harm guards leave out gates that read round-written files

The plan names these guards (`plans/round-53.md:61-63`): `verify_skill_checklist.py --json`, `check_assertion_floors.py`, `check_sibling_census.py`, `check_correction_sweep.py`, and "the frozen round-52 counters". I mapped which gates read which shared files with `grep -o -E 'checklist-baseline\.json|baseline\.json|corpus-baseline\.json|…' verifiers/*` in the sandbox. The gates below are not named, yet each reads a file this round writes:

| Unnamed gate | Reads | Written this round by | State at base |
|---|---|---|---|
| `verify_corpus_independent.py` (the second instrument behind **consistency 10**, an owned axis: "agrees check-for-check", `SCORECARD.md` move log, round 12) | `corpus/` index and pointers | routed defect 2 (index the spot-check, classify 5 pointers); C2's knowledge entry | `exit 1`; `unindexed=1 DRIFT`, `report_dead observed=5 DRIFT` (run below). It agrees with integrity today |
| `fault_injection_corpus.sh` (gates both corpus instruments across 10 fault classes) | `corpus-baseline.json`, `corpus/knowledge` | routed defect 2 re-records `corpus-baseline.json` | red at the r52 base and head: `FAILURES PRESENT`; self-test `BROKEN (T2,T3 FAIL)` (`.ufo/waves/round-52/falsify-a2/ExecGateMatrix.md:48-49`) |
| `verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | the box map | C2 (dispositions of `alwayson.04`/`.07`) | `boxes proven 2`, exit 0 (`ExecGateMatrix.md:29`) |
| `box_proof_case_deletion.py --rev` (round-50 frozen counter) | the box map (`box_proof_case_deletion.py:63`) | C2 | `killed 6 of 6`, exit 0 (`ExecGateMatrix.md:47`) |
| `verify_harness_claims.py` | `verifiers/baseline.json` (`verify_harness_claims.py:58`) | C1 (re-pin of `measured_against`) | 21/28, exit 1, 7 named DRIFT ids (`ExecGateMatrix.md:30`) |
| `check_overlap_levers.py --rev` (round-51 frozen counter) | `SKILL.md`, `corpus/SOURCES.md`, `corpus/knowledge` | C2 (SOURCES rows, entry, any SKILL.md rule) | `7 of 7`, exit 0 (`ExecGateMatrix.md:38`) |

Two more gaps:
- **Routed defect 2 has no after-value.** `plans/round-53.md:68-72` gives no target ("N of 9", exit code). It also says "in the instrument", singular. `ExecCorpusIntegrity.patch` in fact touches both `verify_corpus_integrity.py` and `verify_corpus_independent.py`, so execution covers what the plan text does not. Even so, no guard checks that the two instruments still agree. That agreement is the evidence for the lane's only score-10 owned axis.
- **Red-at-base gates need a different guard form.** For a gate that is already red, "unchanged exit code" can hide a new red id. The guard should be "no new failing id or class versus base".

**Smallest safe correction.** Add to the guard list:
- `verify_corpus_independent.py` agrees with `verify_corpus_integrity.py` on every shared check id.
- `fault_injection_corpus.sh` shows no new failing class versus `e78dff66`.
- `verify_dispatch_prompts.py --box-proof` prints `boxes proven 2`, exit 0.
- `box_proof_case_deletion.py` prints `killed 6 of 6`.
- `verify_harness_claims.py` keeps the same 21/28 and the same DRIFT id set.
- `check_overlap_levers.py` prints `7 of 7`, exit 0.
- Routed defect 2 states a concrete after-value for `verify_corpus_integrity.py`.

## F5 — MEDIUM: the named checklist guard does not run C2's new delegate

**Evidence.**
- `verifiers/verify_skill_checklist.py:66-71`: "An instrument that does not support ``--box-proof`` keeps today's behaviour — it is not run".
- This fail-open is carried debt: `SCORECARD.md:126`, "the checklist gate's fail-open on unprobeable delegates (D2, carried)".
- C2 adds a new `delegated:` target. Neither the counter contract (`check_alwayson_boxes.py:27-38`, which needs only `--check/--target/--json`) nor the plan requires `--box-proof`.

**Counterexample.** A delegate that passes the 6 pinned cases and lacks `--box-proof` leaves `verify_skill_checklist.py --json` at exit 0 with `box_map_complete` PASS, and the gate never executes it. The guard the plan names for C2 is vacuous for the change C2 makes. The plan also does not list D2 as carried.

**Smallest safe correction.** Either require the new delegate to support `--box-proof --map <map>`, so the gate runs it, or state in the plan erratum and report that D2 is carried and that the checklist guard does not exercise the new delegate.

## F6 — LOW: routed defect 4 changes which bytes the round-52 counter path names

**Evidence.**
- The spot-check wording is "the loose host pins and the substring Gate rule … apply to the next counter written" (`round-52-verifier-spotcheck.md:126`).
- The plan instead tightens `verifiers/check_mcp_instructions.py` itself (`plans/round-53.md:74-77`). `ExecMcpTighten.patch` touches only that file.
- The round-52 record names this path as frozen. The SCORECARD coverage row reads "(frozen at the plan commit `4c003a4b`)", and the closure's conformance check was `git diff 4c003a4b 0c9180a6 -- verifiers/check_mcp_instructions.py` → empty (`round-52-verifier-spotcheck.md:29`).
- After the patch, replaying the round-52 counting command at HEAD runs a different program.
- Round 53's own counters read no URL or quote cells (`check_alwayson_boxes.py`, `check_opencode_repin.py`), so the "next counter written" reading is vacuous this round. That explains the plan's choice. The cost is that a recorded identity changes.
- The guard "frozen round-52 counters unchanged in exit code" does not say which bytes it means: HEAD or `4c003a4b`.

**Severity condition.** LOW if the round-52 SCORECARD row gains a qualifier. MEDIUM if it is left unqualified, because the row would then state more than is true (the sentinel class again), and Q29 applies.

**Smallest safe correction.** Land the tightened checks under a new path and keep `check_mcp_instructions.py` byte-identical to `4c003a4b`. Otherwise, append a qualifier to the coverage row (the round-52 result reads on `git show 4c003a4b:verifiers/check_mcp_instructions.py`), register it in `check_correction_sweep.py` (Q29), and run the guard on both copies.

## F7 — LOW: the C1 statement includes a clause its counter does not print

**Evidence.**
- `plans/round-53.md:18-19`: "Each statement below is the counter's printed line and nothing more (Q26)".
- The C1 statement (`:23-26`) adds "and omp 18.12.6 (sha256 `85d9daf3…`)".
- `check_opencode_repin.py:127-130` prints only the opencode substrate line. Its exit (`:131-132`) does not depend on any sha value.
- The omp clause is turned on only indirectly, through `pins OK 3/3`, and only if the omp pin in the revision's `baseline.json` is left untouched. The counter does not check that.
- The statement also drops the printed `opencode re-pin: ` prefix and the ` over <A> assertions` suffix, so its after-value is not one concrete value: A is only bounded below (at least 129).
- The clause is true today: `sha256sum /home/vgpnk/.local/bin/omp` gives `85d9daf3a05fc76e…`, which equals the `baseline.json` `omp_binary_sha256`. The opencode binary hashes to `538fcb1b6408c8d4…`.

**Smallest safe correction.** Drop the omp clause, or bound it to "pins row `omp_binary_sha256` unchanged from `e78dff66`". Quote the full printed line, including A.

## F8 — LOW: separable counters, coupled knowledge

**Counter level: holds.**
- C1's counter archives `verifiers/` and `corpus/`, but its result reads only `verify_surfaces.py --json`, `check_substrate_pins.py --json`, `surfaces-baseline.json` and the surfaces self-test (`check_opencode_repin.py:88-121`).
- C2's counter reads only `checklist-baseline.json` and the delegate (`check_alwayson_boxes.py:128-160`).
- Neither counter reads the other claim's files. The axes are distinct: freshness and operability, both advisory (see F3).

**Knowledge level: coupled.**
- C2's both-files rationale ("two independent rule files are read by different clients", `check_alwayson_boxes.py:19-21`) includes a wave-1 opening of opencode's AGENTS.md/CLAUDE.md resolution (`plans/round-53.md:50-51`).
- In the binary, that resolution is exactly what C1 re-derives: OC-1's name-priority array `["AGENTS.md" … "CONTEXT.md"]` (`corpus/knowledge/opencode-extraction-round14.md:50`) and OC-6, "second instruction subsystem (own load condition for AGENTS.md)" (`verify_surfaces.py:707`). OC-6 is one of the two rules that match nothing on 1.19.4.
- If C2's entry states opencode 1.19.4 behaviour, it either depends on C1's result or risks contradicting it. It could also contradict `instruction-surface-census-round13.md:478`, giving two authorities for one fact.

**Shared write.** C1 raises the `surfaces` floor, routed defect 3 adds arms (`ExecSurfArms.patch`), and C2's instrument, if floored, also lands in `verifiers/floors-registry.json`.

**Smallest safe correction.** For opencode's binary behaviour, C2's entry either cites C1's re-derived classes or is bounded to the docs with their access date. Add this dependency to the plan's separability paragraph. Have the L1 serialize the `floors-registry.json` edits.

## F9 — LOW: the live always-on run touches a kagi-shared file

- `PROVINCE.md:46`: kagi "shared read of `$HOME/.agents/AGENTS.md` — kagi pins the bytes, kotoba owns the checklist".
- The round-7 entry records that this host file fails dates (`SKILL.md:362-364`).
- The plan's live-population item (`plans/round-53.md:94-95`) has no routing rule. An `alwayson.04` FAIL on that file is cross-domain evidence to report, not to edit.

**Correction.** Name the kagi row in the live-run item: report the finding, do not edit the file.

## Checked and holds

- **Source basis of C2.** I opened https://code.claude.com/docs/en/memory.md at 2026-10-22T20:09:13Z: HTTP 200, 51,971 bytes, sha256 `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`, 638 lines.
  - `:357` "An `AGENTS.md` and a `CLAUDE.md` or `CLAUDE.local.md` … | Your `CLAUDE.md` files only"
  - `:436` "A `CLAUDE.md` that tells Claude in words to read `AGENTS.md`**: Claude sees `AGENTS.md` only if it decides to open the file."
  - `:442` "putting an `@AGENTS.md` import in a `CLAUDE.md` next to it"
  - `:455` `ln -s AGENTS.md CLAUDE.md`

  These support the counter's import, symlink, two-file and prose-mention cases. One bound: the two-file FAIL is the **default** (`claude-md-or-agents-md`). Under `claude-md-and-agents-md` both files load (the § Choose which instruction files load table, around `:391`). The entry should say "default".
- **Routed defects.** Each of spot-check §6 items 1–6 has a line in `plans/round-53.md:64-80`, which agrees with `ReviewSpotcheckRouting.md`. The substance is contested for item 5 (F1), item 4 (F6) and item 2 (F4: no after-value, one instrument named).
- **Concrete after-values.** C2's after-value is concrete: exit 0 iff N = 2 (`check_alwayson_boxes.py:166`). C1's is concrete except for the assertion count (F7).

## Commands run (sandbox clone at `3bb0a7a3`)

```
git clone -q <lane> /fast/scratch/hyaku/kotoba-r53/CriticDrift && git -C … checkout -q 3bb0a7a3…  → exit 0
python3 -B verifiers/verify_corpus_integrity.py | tail -12
  → "4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total,
     corpus.pointers.report_dead, corpus.pointers.commit_total"   (exit code not captured: piped through tail)
python3 -B verifiers/verify_corpus_independent.py
  → "unindexed=1 … dead=5 …", "corpus.index.unindexed zero observed=1 DRIFT",
    "corpus.pointers.report_dead zero observed=5 DRIFT", "exit 1"; PIPESTATUS rc=1
grep -o -E '<shared-file names>' verifiers/*.py verifiers/*.sh   → reader map used in F4
sha256sum ~/.local/bin/omp <npx opencode.exe>   → 85d9daf3…, 538fcb1b…   (exit 0)
curl -sS -L https://code.claude.com/docs/en/memory.md   → http=200 bytes=51971   (exit 0)
```

I did not run any C1 or C2 counter, any self-test, or any gate besides the two corpus instruments. Those runs are other seats' work. Statements above about other gates' states at base are cited from `.ufo/waves/round-52/falsify-a2/ExecGateMatrix.md` and were not re-run here.
