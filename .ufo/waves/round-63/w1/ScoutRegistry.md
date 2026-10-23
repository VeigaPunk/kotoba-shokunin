# ScoutRegistry

role: scout
item: ScoutRegistry

## Findings

1. Gate conformance is per blob, not per family. v32 does not inherit v31. Universe is every blob directly under `verifiers/` at `--rev` whose name ends in `.py` or `.sh` (`verifiers/check_gate_registry.py:16-18`, `118-129`). A file is conformant iff exactly one `## Gate registry` row has a name cell equal to that path (`clean()` strips backticks and lower-cases; `check_gate_registry.py:227-234`). v31's row names `verifiers/check_scoped_rules_v31.py` only (`SKILL.md:490`). The frozen v3 row already says the successor "is separate evidence, not this gate" (`SKILL.md:486`). A shared or rewritten name cell makes one file `registry rows naming it: 0 (need 1)` or a duplicate. A probe is impossible while `add_argument("--self-test")` exists (`check_gate_registry.py:193-197`).

2. Baseline is 39 of 39, exit 0, at both the plan base and HEAD.

```
git rev-parse HEAD
8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
git log --oneline 35d44b4b4dcdda234b5dbff7af37e432fec55f05..HEAD
8c4cefa round-63: plan freeze and C1 do-nothing control (v31 5 of 6), census-before
python3 -B verifiers/check_gate_registry.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
gate registry rows conformant 39 of 39 lane verifiers; phantom 0
python3 -B verifiers/check_gate_registry.py --rev HEAD
gate registry rows conformant 39 of 39 lane verifiers; phantom 0
```

HEAD `8c4cefa` is a child of plan base `35d44b4b` (`merge-base --is-ancestor` rc 0). `git ls-tree` counts 39 `*.py`/`*.sh` blobs at both revs. Neither new instrument is in either commit (`git cat-file -e` rc 128).

3. On-disk v32 is untracked and invisible to `--rev`. `git status --porcelain -- verifiers/check_scoped_rules_v32.py` is `?? verifiers/check_scoped_rules_v32.py` (2789 lines). `verifiers/check_r63_routed_repairs.py` is absent. Untracked v32 already has the v31 handlers (`check_scoped_rules_v32.py:2710-2713`): `--rev`, `--fetch`, `--json`, `--self-test`, and prints `self-test: %d failure(s) over %d assertions` (`:2699`). Committing that blob without a new SKILL row drops the headline to 39 of 40. Adding the row before the blob is a phantom (`check_gate_registry.py:45-46, 240-241`). Both must be in the same revision. This seat did not write that file.

4. Conformant row shape is eight cells, header at `SKILL.md:470`. From `check_gate_registry.py:20-43` and `judge_row` `:178-224`:

| cell | rule |
|---|---|
| Name | exactly one backticked `verifiers/FILE` |
| Kind | `gate` |
| Entry command | raw cell contains `verifiers/FILE` as a substring. Flags in this cell are not checked |
| Verdict map | at least one code=class pair (`=`, `->`, or arrow); class in {clean, failed, could-not-evaluate}; no code twice; a gate must declare `0=clean` and `1=failed`. Trailing prose is ignored. The checker does not run the script |
| Self-test | one or more backticked `--flags`; each must be an exact `add_argument` string. `none` is illegal for a gate. Landed predecessors put only backticked `--self-test` here |
| Pinned values | `in-file` (landed choice for v31 and v2) or backticked repo-relative paths that `git cat-file -e REV:PATH` accepts. A gate may not say `none` |
| Write scope | non-empty, not `-` or an em dash |
| Owner | `kotoba` |

Landed templates copied (not the unlanded r62 candidate that pinned the frozen counter as a path; that did not ship). Live cells use an angle-bracket rev placeholder; this report spells it REV so the quote stays plain text.

```
SKILL.md:489
| `verifiers/check_routed_repairs_v2.py` | gate | `python3 -B verifiers/check_routed_repairs_v2.py --rev REV` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only) | kotoba |

SKILL.md:490
| `verifiers/check_scoped_rules_v31.py` | gate | `python3 -B verifiers/check_scoped_rules_v31.py --rev REV --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — round-62 successor to the frozen v3 counter: closes five of the six measured survivor instances (E2c x2, E2e x2, E2f G7) with the r61 worlds/eligible line unchanged; G9 compound-purpose stays a declared bound; the frozen counter's bytes are unchanged | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
```

Insert inside the first table under `## Gate registry` (`SKILL.md:464`). A blank line ends the table (`check_gate_registry.py:164-166`); the table's blank line is `SKILL.md:511`, before `## Sources`. Order is not checked. Do not edit frozen `check_gate_registry.py` (pinned at the r54 plan commit, `:11-14`).

5. Floors registration is not required, and a half-row fails closed. `verifiers/floors-registry.json` has `instrument_total: 14` and 14 entries. Neither v31, v2, nor the two new names is among them. Keys: alwayson, checklist, compare_harness_independent, corpus_independent, corpus_integrity, correction_sweep, dispatch_prompts, floors_guard, harness, harness_independent, overlap_levers, pins, sibling_census, surfaces. `check_assertion_floors.py` walks only `INSTRUMENTS` (`:588-599`). r62 left the successor gates unfloored on purpose: fleet `.ufo/reports/round-62/kotoba.md:108` (F17) says the guard passes 14 of 14 while executing neither gate, and the smallest fix is an assertion-count line plus registry rows (v31 already prints 201 assertions). `plans/round-63.md` does not require a floors bump. Do not invent one.

If the L1 floors them anyway, the JSON shape the anchor accepts (`check_assertion_floors.py:385-390`) is an object with `path` a non-empty str and `floor` a plain int (not bool), and `instrument_total` must equal `len(instruments)` (`:377-381`). The same change must also add the name to `EXPECTED_INSTRUMENTS` (`:151`) and a 5-tuple to `INSTRUMENTS` (`:191-220`): path str, floor int, regex, assertion_group, failure_group, with path and floor identical across JSON and both tables (`:415-420`); update the docstring floor list (`:7-11`, the file's own bump-in-step rule); and change the F6 literal `"instrument_total": 14` (`:802`) to the new total. A JSON-only row is `row vanish` (`:391-393`). A tables-only row is `extra row` (`:425-427`). A stale total is `size drift` (`:379-381`). A stale F6 literal fails `mutation anchor lands exactly once (F6/total)`. v32's on-disk print matches `self-test: N failure(s) over M assertions` with groups `(2, 1)`, the correction_sweep tuple (`:218-219`). The floor integer is the observed count. This seat did not run `--self-test`, so it is unknown. Do not copy v31's 201. `check_routed_repairs_v2.py` has no `failure(s) over` line. A C2 counter that only prints `r62 routed defects closed 5 of 5` is `summary=missing` under that regex until it also prints the assertion line (F17's fix) or the tuple's regex is written to a line it actually prints.

6. Proof commands after the landing commit (both blobs and both rows in that revision; no other `verifiers/*.{py,sh}` add or remove):

```
python3 -B verifiers/check_gate_registry.py --rev LANDING
```

prints `gate registry rows conformant 41 of 41 lane verifiers; phantom 0` and exits 0. The two new paths print `OK` with an empty why. Optional: `--json`, and require `"conformant": true` for both and `"phantom": []`.

```
python3 -B verifiers/check_gate_registry.py --self-test
```

is the checker's own battery. It does not see the new rows. Not a substitute for `--rev`.

Floors, if left unregistered (this seat's recommendation): do not add a row; `instrument_total` stays 14. This seat did not re-run `check_assertion_floors.py`. If the L1 does the full bump, that command must exit 0 and name `PASS` for each new instrument at the observed floor, and the guard self-test must still pass after the F6 literal moves.

## Artifacts

Candidate rows. Verdict-map prose is the plan's predicate (`plans/round-63.md`), not a measurement. In `SKILL.md` spell the rev placeholder the way every existing row does; it is written REV here only as plain text. v32's entry command matches the untracked file's `--rev` and `--fetch` handlers. Drop `--fetch` from the entry cell if the landed file drops that flag (conformance does not check it). C2's backticked `--self-test` cell is conformant only if the landed file has `add_argument("--self-test")` exactly.

```markdown
| `verifiers/check_scoped_rules_v32.py` | gate | `python3 -B verifiers/check_scoped_rules_v32.py --rev REV --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — round-63 successor to frozen v31: closes G9 `e2f-compound-purpose-outside-citation`; the self-test prints `worlds reject 7 of 7; eligible rows pass 4 of 4`, `survivors closed 6 of 6`, and `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`, and exits 0; v31 bytes unchanged | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
| `verifiers/check_r63_routed_repairs.py` | gate | `python3 -B verifiers/check_r63_routed_repairs.py --rev REV` | 0=clean, 1=failed, 2=could-not-evaluate — round-63 counter: `--rev REV` prints `r62 routed defects closed 5 of 5` and exits 0 | `--self-test` | in-file | none (read-only) | kotoba |
```

No floors-registry diff. No installs.

## Verdict

PROPOSES. Each new `verifiers/*.py` needs its own `SKILL.md` Gate-registry row in the same commit as the blob; v32 does not inherit v31. Floors stays at 14 unless the L1 does the four-surface bump (JSON + both tables + docstring + F6 literal 14) with a measured floor. Change this if the landed C2 script has no exact `--self-test` handler, or if v32 drops `--rev`/`--fetch` and the entry cell should name only `--self-test` (still conformant either way, as long as the path is in the entry cell).
