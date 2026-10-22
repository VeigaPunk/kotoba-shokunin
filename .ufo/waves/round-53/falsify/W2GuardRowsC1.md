Result: HOLDS — the landed gate at tip c775d68 exits 0 with all 7 check ids appearing exactly once and `surfaces.opencode_extract` named 9/9 declared classes from 7/7 rules; the emit path has a single row-emission site with no duplication or injection avenue in the canonical run.

## Command, lane tip, exit code

Command (run read-only in the lane, no writes; stdout captured to /tmp/w2guard_c1_run.json):

```
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_surfaces.py --json
```

- Lane tip (`git rev-parse HEAD`): `c775d6823bfca8f0de8c0874032a954438b38edc` (round-53 floors commit).
- `git status --porcelain=v1 -v`: only untracked `.ufo/waves/round-53/` and `corpus/lessons/round-53.md` (fleet/falsify reports); no tracked modification. Run was read-only.
- **Exit code 0**, stderr empty, wall 15.66 s. Payload `"exit_code": 0`, `"pass": 7`, `"fail": 0`.

## Guard (c) sub-checks

**1. Each of the 7 check ids exactly once — HOLDS.** JSON `checks` has 7 rows; parsed: `n_checks=7`, `unique=7`, `dup_ids=[]`, and the id set equals `CHECK_IDS` exactly (`surfaces.literal_present`, `surfaces.no_uncovered_class`, `surfaces.opencode_extract`, `surfaces.table_parity`, `surfaces.literal_parity`, `surfaces.kind_parity`, `surfaces.excluded_reason`). All 7 statuses PASS.

**2. opencode_extract detail names 9/9 classes from 7/7 rules — HOLDS.** Detail: `opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)`. Cross-checked against the landed baseline (`verifiers/surfaces-baseline.json`): 42 classes total, 9 opencode entries, 9 unique `class_id`s — so 9/9 is the true declared count, and the detail enumerates all seven rule ids.

**3. Emit path duplication/injection review — no avenue in the canonical run.**

- Single row-emission site: `verify_surfaces.py` `main()` loop, `results.append({"id": cid, "status": ..., "detail": ...})` at line 1837. A grep for `checks|results).append|emit_json|CHECK_IDS|results\s*=` finds no other append to `results` anywhere; the only other `emit_json` calls are the two error paths that emit `checks: []` with exit 2/3 (lines 1788-1789, 1815-1816). `emit_json` (1760-1772) prints the payload verbatim with no transformation, dedup, or row synthesis.
- Default `wanted = list(args.check) if args.check else list(CHECK_IDS)` (line 1783); `CHECK_IDS` is a 7-element tuple of unique ids (254-262), so the default run emits exactly one row per id — duplicates are structurally impossible.
- Injection of foreign ids: `--check` is `choices=CHECK_IDS` (line 1719), so a row's `id` can only be one of the seven frozen ids; the row shape is constant `{"id","status","detail"}`. `load_baseline` rejects duplicate class ids (`BaselineError`, → exit 3 with empty checks; ReviewCounterC1 L1), so baseline-level injection is loud.
- The canonical C1 counter invokes the gate as `verify_surfaces.py --json --repo <tree>` with no `--check` (`verifiers/check_opencode_repin.py` lines 97-103), i.e. exactly the default path verified above.

## Findings (severity)

- **Low (observation) — `--check` is repeatable (`action="append"`) and not deduplicated.** A caller passing the same id twice (e.g. `--check surfaces.literal_present --check surfaces.literal_present`) gets two rows with the same id; `pass` (line 1764) counts them twice and `emit_json` outputs the duplicate. This is unreachable from any in-repo caller (the counter never passes `--check`) and is a manual CLI misuse, not a landed-behavior defect. No action required; noted because it is the only literal "row can be duplicated" mechanism in the file.
- **Low (note) — PASS detail names counts + rule ids, not the 9 class ids.** The detail string is computed (line 1084-1087: `len(declared)`, matched-rule sum, `len(report)`, joined rule ids), not hardcoded, and the numbers match the baseline (9/42, 9 unique opencode ids). It does not enumerate the class ids (e.g. `opencode:read-hook/instructions`); the erratum guard (c) phrasing "names all declared opencode classes from all rules" is satisfied to the count+rules level used in this assignment. A stricter class-id-enumeration reading is not met by the emitted text on PASS (FAIL details do name the exact classes, lines 1067-1081). Flagging for the L1's awareness, not a defect of the landed gate.
- No other defects found in the emit path.

## Residual risk and verification gaps

- Honesty of the numbers rests on the checker computing them from real extraction (`extract_opencode_classes(dump)`) and the revision's own baseline; a revision that rewrites `check_opencode_extract` to return a canned True detail would print the same PASS row. That is precisely the counter trust gap documented by ReviewCounterC1 (M1 family); it is covered by erratum guards (a) (scope diff) and (b) (independent strings dump), not by guard (c) alone.
- I did not run `--self-test` or the pins script; this seat is scoped to guard (c) rows. Floor claims (surfaces 155) are not exercised here.
- Dup vector via repeated `--check` untested end-to-end (code-cited only); harmless to the canonical runtime.
