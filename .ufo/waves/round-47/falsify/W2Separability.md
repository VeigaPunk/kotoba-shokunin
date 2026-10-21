verdict: PARTIAL — C1 and C3 verify alone at their declared counting commands; C2 verifies alone only at check granularity (its file-level `--json` is red without C3), and the landed floor pair (surfaces 99 / checklist 1845) is a union-only attestation that no single claim satisfies.

# W2Separability — C1/C2/C3 causal separability at 7ad7fad

Method: three canonical-layout clones of `c61a973`, one claim each, from `git diff c61a973 7ad7fad` split by path and (for the two shared files) by hunk. No production file was touched; all work in `/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2Separability-2/{A,B,C}/kotoba-shokunin`.

| clone | commit | applied |
|---|---|---|
| A (C1) | `b1b48d1` | 33 files: `verifiers/verify_surfaces.py`, `verifiers/surfaces-baseline.json`, `corpus/knowledge/instruction-surface-census-round13.md`, `verifiers/baseline.json`, `verifiers/check_substrate_pins.py`, `verifiers/verify_harness_claims.py`, `verifiers/fixtures/surfaces/*`; floors **surfaces 87→99 only** (`check_assertion_floors.py` EXPECTED + INSTRUMENTS rows + two self-test anchors; `floors-registry.json` surfaces floor) |
| B (C2) | `5d50621` | `verify_skill_checklist.py` hunks 0,2,4,6,7,11,12,13,17 of 18; `SKILL.md`; `fixtures/checklist/xml-tag-{codespan,control,dq-escape,split}`; floors left at BASE |
| C (C3) | `371e901` | `verify_skill_checklist.py` hunks 1,3,5,8,9,10,14,15,16 of 18; `corpus/README.md`; `corpus/lessons/round-47.md`; `corpus-baseline.json`; `fault_injection_corpus.sh`; floors left at BASE |

Hunk split, mechanically checked: the C2 subset contains no `GOVERNANCE_ERRATA` / `errata_problems` / `excused` identifier and the C3 subset contains no `no_xml_tag` / `XML_TAG_RE` / `YAML_ANGLE` identifier; both subsets `py_compile` and run. Split patches are attached as `W2Separability.checklist-c2.patch` and `W2Separability.checklist-c3.patch`. Machine-readable matrix: `W2Separability.matrix.json`.

## Findings

### F1 — the matrix (each row is a command, exit, key output)

| clone | command | exit | output |
|---|---|---|---|
| A | `python3 -B verifiers/verify_surfaces.py --json` | **0** | 7 PASS / 0 FAIL |
| A | `python3 -B verifiers/check_substrate_pins.py` | **0** | 3/3 pins hold |
| A | `verify_surfaces.py --self-test` | 0 | `0 failure(s) over 99 assertions` |
| A | `check_assertion_floors.py` (C1-only floors) | **0** | 9/9; surfaces 99/99, checklist 1597/1597 |
| A | `check_assertion_floors.py` (landed floors, worktree) | **1** | surfaces 99/99 PASS; **checklist 1597 < 1845 FAIL** |
| A | `verify_skill_checklist.py --json` (BASE file) | 1 | 9 PASS / 1 FAIL `governance.citation_resolves`, evaluated 805 |
| A | `verify_corpus_integrity.py --json` | 1 | DRIFT `tracked_files 59!=58`; `unindexed 1` |
| A | `verify_corpus_independent.py --json` | 1 | DRIFT `corpus.index.unindexed` |
| A | `fault_injection_corpus.sh` (BASE) | 1 | control dirty; d1/d2 WRONG-CLASS |
| B | `verify_skill_checklist.py --check trigger.no_xml_tag` | **0** | PASS, evaluated 2 |
| B | `verify_skill_checklist.py --json` | **1** | 10 PASS / **1 FAIL `governance.citation_resolves`**, evaluated 805 |
| B | frontmatter `<skills>` count | 0 matches (grep exit 1) | `0` |
| B | `verify_skill_checklist.py --self-test` | 0 | `0 failure(s) over **1837** assertions` |
| B | `verify_surfaces.py --json` (BASE file) | 2 | `opencode binary not found: /home/vgpnk/.opencode/bin/opencode` |
| B | `check_assertion_floors.py` (BASE floors) | **0** | 9/9; checklist 1837/1597 |
| B | `check_assertion_floors.py` (landed floors, worktree) | **1** | **surfaces 87 < 99 FAIL; checklist 1837 < 1845 FAIL** |
| C | `verify_skill_checklist.py --json` | **0** | 10 PASS / 0 FAIL; governance evaluated **804**, `1 recorded absence(s) excused` |
| C | `verify_skill_checklist.py --self-test` | 0 | `0 failure(s) over **1605** assertions` |
| C | `verify_corpus_integrity.py --json` | **0** | 9/9; tracked 60; unindexed 0; report_total 40; commit_total 29 |
| C | `verify_corpus_independent.py --json` | **0** | 0 DRIFT |
| C | `fault_injection_corpus.sh` (sequential ×3) | **0** | `ALL PASS` ×3 |
| C | `verify_surfaces.py --json` (BASE file) | 2 | opencode binary not found |
| C | `check_substrate_pins.py` (BASE) | 2 | `DRIFT 3/3` (omp sha, omp mtime, opencode unreadable) |
| C | `verify_skill_checklist.py --check trigger.no_xml_tag` | 2 | argparse invalid choice |

C1's two declared commands are green in clone A and red where C1 is absent (surfaces exit 2 in B and C; pins `DRIFT 3/3` in C); C3's four declared commands are green in clone C and red in clone A (checklist 9/1, integrity 1, independent 1, fault 1). The axis is separable in both directions: `verifiers/verify_surfaces.py:130` (`DEFAULT_BINARIES`), `:157` (`OMP_CALL_RE` with `lq|Xl|Fo`), `:370` (`OC_PRIORITY_RE`), `:426` (`OC_V2_KEY`); `verifiers/baseline.json:5,9`; `verifiers/check_substrate_pins.py:66`.

C2's own observables are green alone: `verifiers/verify_skill_checklist.py:310` (CHECK_IDS), `:404` (`XML_TAG_RE`), `:409` (YAML escape), `:1294` (`check_no_xml_tag`), `:2391` (dispatch); `SKILL.md:14` (`omp skills router`) and `:151` (portability floor citing `trigger.no_xml_tag` + S012).

### F2 — C2's *file-level* counting command is not separable; C3's is (one-directional coupling)

`verify_skill_checklist.py --json` on the C2-only tree is **exit 1, 10 PASS / 1 FAIL**, and the only failure is `governance.citation_resolves` — C3's class (`LOG.md:2111` unresolved, evaluated 805). On the C3-only tree the same command is **exit 0, 10/10** with `SKILL.md` still carrying `<skills>` (C2 absent). So the aggregate gate is C2+C3 → union: 11/11 only with both. The plan's C2 after-target ("live check PASS") is check-scoped and does hold; the file-level gate does not. The two claims' hunks are disjoint in the file, so this is aggregation, not code coupling.

Repro:
```
git clone --no-hardlinks <lane> C && cd C && git checkout --detach c61a973
git apply W2Separability.checklist-c2.patch
git checkout 7ad7fad -- SKILL.md verifiers/fixtures/checklist/xml-tag-codespan \
    verifiers/fixtures/checklist/xml-tag-control verifiers/fixtures/checklist/xml-tag-dq-escape \
    verifiers/fixtures/checklist/xml-tag-split
python3 -B verifiers/verify_skill_checklist.py --json   # exit 1, 10/1, governance only
```

Provenance nuance: C2's S003 basis is at BASE (`corpus/SOURCES.md`, row S003 states "The description cannot contain XML tags"), but the "S012 stricter" half of the claim is carried by the frontier row `corpus/SOURCES.md:25`, which exists only after the SOURCES step (0 occurrences of `S012` at BASE) — outside all three claim file sets. So a C2-only tree can verify the rule but not its declared S012 support; no gate reads SOURCES.md, so this is provenance, not counting-command, coupling.

### F3 — the landed floors are a union-only attestation

`verifiers/floors-registry.json:6` (`checklist 1845`), `:38` (`surfaces 99`); `verifiers/check_assertion_floors.py:123,144`. Measured self-test counts: BASE 1597, C2-only **1837** (+240), C3-only **1605** (+8), landed 1845. Both sums close (`1837+8=1845`, `1605+240=1845`), which proves the assertion sets are additive and disjoint — but no single claim reaches the landed pair: C1-only attests 99/1597, C2-only 87/1837, C3-only 87/1605. Each subset passes floors only at BASE/its-own floors because the floor is a lower bound (`assertions >= floor`); with the landed floors file, the C1-only tree exits 1 and the C2-only tree exits 1. The floors gate therefore cannot discriminate *which* claim produced the ratchet; it only fails the union's absence.

Repro:
```
git worktree add /tmp/w HEAD && cd /tmp/w
git checkout 7ad7fad -- verifiers/check_assertion_floors.py verifiers/floors-registry.json
python3 -B verifiers/check_assertion_floors.py    # exit 1: surfaces 87<99, checklist 1837<1845
```

### F4 — record over-attribution (calibration)

`SCORECARD.md:31` (C2 row) says ```verify_skill_checklist.py --self-test` 1597 → 1845 assertions, 0 failures``. C2 alone is **1837**; the missing 8 are C3's erratum arms. `LOG.md:2322` discloses this correctly ("1597 → 1845 assertions **with C3's arms**"); the SCORECARD row dropped the qualifier. Measured: C2-only `--self-test` → `0 failure(s) over 1837 assertions` (exit 0); C3-only → 1605; arithmetic above. This is a record defect in the C2 row only; the C1 row's "87 → 99" and the C3 row's "11/11 (C2's check included)" are accurate as measured.

### F5 — the fault-harness sub-claim is a within-C3 bundle, and it is environment-sensitive

`verifiers/fault_injection_corpus.sh:117-119` (planter now inserts inside `## Coverage map`). Applying only that file to a BASE corpus exits **1**: `fault-0-control | integrity | 1 | corpus.index.unindexed | FAIL-control-dirty` — the control world is dirty because `corpus/lessons/round-46-verifier-spotcheck.md` is tracked-but-unindexed at BASE, and d1/d2 only reach PASS once the planter is fixed. So "fault harness exit 1→0" is caused by the index rows + `corpus-baseline.json` + the planter fix jointly, not by the planter fix alone.

Repro:
```
git worktree add /tmp/p HEAD && cd /tmp/p
git checkout 7ad7fad -- verifiers/fault_injection_corpus.sh
bash verifiers/fault_injection_corpus.sh --repo "$PWD"    # exit 1, control dirty
```

Environment note (not a landed defect): two harness runs started in parallel both failed from the 6th world onward with `env unreadable: clone failed for fault-<id>` (new_world suppresses git's stderr) while `/tmp` was at 98% used (3.5 GiB free); the same two clones were green 3/3 when run sequentially, and 12 concurrent `git clone file://` of the same repo succeeded once space was available. `[INFERENCE]` capacity pressure, not harness logic — but a parallel gate battery can read this harness red for reasons unrelated to the tree.

### F6 — doc-level cross-claim pointer (non-gating)

`corpus/README.md:76` (a C3-owned file) points at `knowledge/instruction-surface-census-round13.md § B′`, and `§ B′` exists only after C1's census edit: 0 occurrences at BASE, 2 at 7ad7fad (`corpus/knowledge/instruction-surface-census-round13.md:167,212`). No gate resolves section anchors (`verify_corpus_independent.py` resolves paths only), so a C3-only tree carries a correct path with a dangling section pointer. Not a gate coupling; a reader of the C3 subset alone cannot follow the pointer.

### F7 — erratum pin re-derives (negative result, recorded)

`LOG.md:2111` at 7ad7fad hashes (UTF-8, no trailing newline) to `7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135`, matching `verifiers/verify_skill_checklist.py:380`; the absence wording at `:382` is on the line; horizon 2315 (`:377`) equals the BASE `LOG.md` line count (2315; LAND 2326) and the round-47 append starts at 2316, so the pinned line is byte-unchanged. The gate reports `governance ... evaluated 804 ... 1 recorded absence(s) excused` (measured in clone C), one fewer than BASE's 805.

### F8 — no cross-claim harm observed on the named commands

C1's presence leaves the corpus DRIFT set exactly at the before values (`tracked_files 59!=58`, `unindexed 1`; clone A), C3's presence leaves surfaces/pins at their BASE errors (exit 2; `DRIFT 3/3`; clone C), and C2's presence leaves surfaces at exit 2 (clone B). Nothing in one claim's file set rescues or breaks another's named count except the aggregations named in F2/F3.

## Proposed move (one, bounded)

Correct the C2 attribution and make the check-scoped command the canonical C2 count in the landed records: change `SCORECARD.md:31` to `self-test 1597 → 1837 for C2's arms (1845 with C3's 8 erratum arms)` and, because `LOG.md` is append-only, record the same one-line decomposition in the next LOG entry (the landing-pin entry) rather than editing `LOG.md:2322`/`:2324`. Optionally add the per-claim floor decomposition (`1845 = 1597 + 240 + 8`) to the same line. This is a record-only change: no verifier behavior moves, no floor moves.

- Affected axes: calibration (primary — a record currently over-attributes 8 assertions to C2), operability (makes the standalone C2 command explicit: `--check trigger.no_xml_tag`). Freshness untouched.
- Risks: record churn must be dated and must not imply the landed 1845 is wrong (it is correct for the union); a future re-measure on a different host still inherits the host-anchored C1/C2 paths. Do not "fix" the floors registry — the union floor is correct as a ratchet; the defect is the record's causal claim.
- Verification: rebuild the two subset clones, re-run `--self-test` in each (1837 / 1605), and confirm `1837+8 == 1605+240 == 1845`; re-run the C2-only `--json` to confirm the single expected FAIL is `governance.citation_resolves`.

## What I did NOT check

- Did not re-derive the C1 extraction or fixture fidelity (other seats), nor mutation-test the XML check or the erratum arms (`W2XmlMutants`, `W2Errata*`), nor the post-landing full after-battery on the union tree.
- Did not re-run `floors` alone on the C3-only clone (only B was re-run alone at BASE floors; C's floor run was observed only under load, where `harness_independent` hit its 120 s timeout — an environment effect also seen in B before its solo rerun).
- Did not test `npx` cache invalidation of the pinned opencode path (`verifiers/verify_surfaces.py:130` embeds the npx hash `e2094862b59aac7b`); it is a hardlink of `opencode-linux-x64/bin/opencode` (same inode 43795736, sha `179ca421…`), so the `.exe` name is cosmetic today.
- Did not measure `verify_harness_claims.py` 21/28 (declared not claimed) or the fault harness `--self-test` mode.
- No production file, Git ref, or jj state in the lane was touched; clones A/B/C and the two worktrees are throwaway.
