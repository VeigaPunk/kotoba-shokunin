Result: HOLDS — all six cells of the C2 registry row for `verifiers/verify_skill_checklist.py` (bf65974c, unchanged at tip 58db81c) hold; no cell breaks, no row repair proposed.

Scope: row attacked as landed at bf65974c7845a06d7ef621ad998c6378ff735cd5 and re-checked at tip 58db81c4465b0e9b07ef2485b87d8970683afac6 (identical text). All execution in sandbox clones under /fast/scratch/hyaku/kotoba-r54/ (seats: W2RowVerifySkillChecklist, fleethome). No installs performed (tooling directive: nothing needed). No network use.

Row under attack:
`| `verifiers/verify_skill_checklist.py` | gate | `python3 -B verifiers/verify_skill_checklist.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=failed | `--self-test` | `verifiers/checklist-baseline.json`, `verifiers/checklist-command-vocabulary.json` | self-test trees under `$TMPDIR` | kotoba |`
(Source: SKILL.md, `## Gate registry` section, row line 31 of the table excerpt; identical at bf65974c and 58db81c via `git show bf65974c:SKILL.md` vs working tree.)

Findings by cell:

1) Entry command — HOLDS.
   Ran in sandbox clone at 58db81c (flat):
   `python3 -B verifiers/verify_skill_checklist.py` → exit 1; last stdout lines:
   - `PASS trigger.command_binary_resolves: evaluated 39 — 20 segments; 39 command subject(s) resolve`
   - `FAIL trigger.citation_resolves: evaluated 113 — line 589: '../.ufo/reports/round-7/kotoba.md' does not resolve from /fast/scratch/hyaku/kotoba-r54/W2RowVerifySkillChecklist`
   - `FAIL governance.citation_resolves: evaluated 1018 — LOG.md:177: '../.ufo/reports/round-9/kotoba.md' does not resolve ... (+20 more); ...`
   Exit 1 is the declared meaning (any FAIL). The FAILs are an artifact of the clone's location: every failing token is a `../` sibling citation (`../.ufo/...`, `../PROTOCOL.md`, `../kasegi-shokunin/...`, `../AXES.md`, `../MISSION.md`) that resolves only in the canonical fleet root; my clone has no siblings. Re-run in a nested fleet-layout clone (`/fast/scratch/hyaku/kotoba-r54/fleethome/kotoba-shokunin` with `../.ufo`, `../PROTOCOL.md` symlinks) still failed only on further sibling `../` citations (e.g. `LOG.md:824 '../kasegi-shokunin/...'`, `SCORECARD.md:3 '../MISSION.md'`) exit 1. No network, no writes (git status clean before/after, no `__pycache__`). Command shape matches the row text. The gate's verdict in the canonical lane environment is [INFERENCE] not observable from sandbox bounds.

2) Self-test flag — HOLDS.
   `python3 -B verifiers/verify_skill_checklist.py --self-test` → exit 0; last line `0 failure(s) over 1852 assertions`. The flag is this script's own argparse flag (`--self-test`, source :2502-2504), dispatches to its own `self_test()` (:1881-2474), which drives the script's own CLI in-process (`run_capture` → `main`, :1757-1762, :1893-1900) over committed fixtures only (`verifiers/fixtures/checklist/`, 153 committed files), asserting exit codes and expected findings per case (CASES table :1903-2060; fence pins :1774-1878). Not a nested external call, not usage text.

3) Verdict map — HOLDS.
   Source produces exactly {0,1,2,3} with the declared meanings, nothing else:
   - 0: no FAIL and >=1 subject evaluated — `main` :2624-2626.
   - 1: any FAIL, or no subject evaluated — :2624-2626; also `self_test` returns 1 on failures (:2474; rc documented as not comparable to live runs, :281-283).
   - 2: environment error (target file/vocabulary unreadable or unparseable) — EnvError :431-433, handled :2561-2581; argparse usage errors also exit 2 (documented :274-283).
   - 3: box map missing/unparseable/schema-invalid for a required map — MapError :435, :453-504, handled :2539-2559.
   Produced-code completeness: the only exit mechanism is `sys.exit(main())` (:2637); no `os._exit`/`raise SystemExit` elsewhere; the `sys.exit(1)` strings at :2430/:2432/:2437 are literals written into temp stub scripts for the self-test, not executed by this script. Empirical probes (sandbox): `--map /tmp/does-not-exist-map.json --check checklist.box_map_complete` → exit 3, `ERROR box map unreadable: ...`; `--vocabulary /tmp/does-not-exist-vocab.json --check trigger.command_binary_resolves` → exit 2, `ERROR command vocabulary unreadable: ...`; `--skill verifiers/fixtures/checklist/clean/SKILL.md --map .../clean/map.json --check checklist.box_map_complete` → exit 0, `PASS checklist.box_map_complete: evaluated 2 ...`.
   Note (not a break): 3=failed is a deliberate, documented classification ("a gate failure class, not merely environment unreadable", :274-283); a missing committed baseline means the graded tree is defective. One prose inconsistency exists at SKILL.md:139 ("3 = box map missing, unparseable, or bound elsewhere") — the code returns 1 (FAIL) for a bound-elsewhere map via `check_box_map` (:1208-1210); this is a documentation wording issue outside the registry row, already flagged by RegVerifySkillChecklist.md:21.

4) Pinned values — HOLDS.
   Both paths exist at the rev and are read as expected values:
   - `verifiers/checklist-baseline.json` — read via `load_map` when the target is the repo SKILL.md (default `--map` path, :2543-2544); expected box map (schema kotoba-checklist-v1, file=SKILL.md, box_total floor, per-box text_sha256 + disposition) consumed by `check_box_map` (:1200-1337). 41 entries at the rev; both `--box-proof` delegates proven (below).
   - `verifiers/checklist-command-vocabulary.json` — read via `load_vocabulary` whenever `trigger.command_binary_resolves` runs (default, :2563-2564); declared command vocabulary (schema kotoba-command-vocab-v1) used as the ceiling for inline-command classification (:1084-1193).
   Both committed (`git ls-files` lists both; 153 fixture files committed under `verifiers/fixtures/checklist/`).

5) Write scope — HOLDS.
   Normal (live) run writes nothing: checks only read and print; delegated instruments are launched with `sys.executable -B` (:946-958), `capture_output=True`, `cwd=base` (:1008-1009); their live `--box-proof` paths (`verify_alwayson.box_proof` :558-614; `verify_dispatch_prompts.box_proof` :985-1147) are read-only (all `write_text` sites in verify_dispatch_prompts.py are inside its self-test temp trees, `tempfile.TemporaryDirectory` :689, :857-894). Post-entry-run `git status --porcelain` empty; no `__pycache__` anywhere in the clone. Self-test writes only inside `tempfile.TemporaryDirectory` trees (`$TMPDIR`) at :2276, :2363, :2392, :2439, auto-cleaned; observed `TMPDIR` behavior confirmed by wave-1 run (RegVerifySkillChecklist.md:16). Cell text "self-test trees under `$TMPDIR`" is accurate; it does not claim the delegated instruments' temp proof trees (which are also under `$TMPDIR` per their own rows) — acceptable.

6) Gate vs probe — HOLDS.
   It fails (nonzero) on defects (exit 1 on any FAIL/no-subject, 2 on env unreadable, 3 on required map failure) and is read-only over surfaces it does not own; registered as gate, correct per PROTOCOL.md § Gate standard (a tool that cannot fail is a probe — this one fails).

Counter reconciliation (C2 consistency):
- `python3 -B verifiers/check_gate_registry.py --rev 58db81c...` → `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0 (this row listed `OK`).
- Counter self-test: `--self-test` → `self-test: 0 failure(s) over 22 assertions`, exit 0.
- Counter frozen: `git diff e3371548 58db81c -- verifiers/check_gate_registry.py` empty (unchanged since plan commit; frozen respected).
- Row text identical at bf65974c and tip.

Residual risk / verification gaps:
- The live verdict of the gate inside the canonical fleet root (where `../` sibling citations resolve) was not observable under leaf sandbox bounds; the two wave-1 exit-1 records in ExecTipRuns.md (rev 7ad05d34, b38c32a0) carry the same sandbox-fleet artifact. A reviewer with lane-run latitude should confirm exit 0 there (i.e., the 11 checks pass on the real tree) — that is a gate-health check, not a row-consistency check; the row itself is accurate.
- Pinned-values cell names the two live-run expected files but not the committed self-test fixture tree (`verifiers/fixtures/checklist/`). The counter rule requires only that named paths exist, so no break; if the lane wants maximal symmetry with `verify_dispatch_prompts`' row (which lists its fixtures manifest), appending `verifiers/fixtures/checklist` to the cell would be an optional tightening, not a correction.
- `SKILL.md:139` prose "or bound elsewhere" for exit 3 is inaccurate (source returns 1 for that case) — pre-existing doc mismatch, outside this row; proposed fix: change "bound elsewhere" to "unparseable, or schema-invalid".
