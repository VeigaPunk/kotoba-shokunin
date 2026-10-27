# Kb79E01Registry — round 79 w1, C1 repair 1 of 4: gate registry (Q35/Q46)

sandbox commit c3ee93d23faaee0b21a2f1c99cb314f706f459ec (clone `/fast/scratch/hyaku/kotoba-r79/Kb79E01Registry/clone`, checked out from F1 `2c56622375641193a03bb97c0624e6536f3dffba`)
lane head at measurement `daa3a09aa7980dbaa99d532cc2e9ad391f829bc6`; its `SKILL.md` is byte-identical to the r79 base `b10bcbc6b00f8f56b202ccbadca311007b5b463c`

## What changed

One file, two inserted lines, zero deletions: `SKILL.md`, appended at the end of the `## Gate registry` table (after the `verifiers/check_sibling_reread.py` row, which is the table's last row at the r79 base, `SKILL.md:512`). No other `SKILL.md` byte moves; `wc -l SKILL.md` goes 590 -> 592 (budget 600).

```
| `verifiers/check_desc_craft.py` | gate | `python3 -B verifiers/check_desc_craft.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — claim withdrawn r79 before data (declared r76, never landed); not a claim gate until redesigned and re-controlled | `--self-test` | in-file | none when measuring (reads committed bytes); `--self-test` isolated fixture repos under `$TMPDIR` (removed) | kotoba |
| `verifiers/check_r75_routed_repairs.py` | gate | `python3 -B verifiers/check_r75_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — claim withdrawn r79 before data (declared r76, never landed); not a claim gate until redesigned and re-controlled | `--self-test` | in-file | none when measuring (reads committed bytes); `--self-test` sandbox and fixture clones under `$TMPDIR` (removed) | kotoba |
```

## Why each cell is what it is (no cell guessed)

- **Position.** Both counters were created by `ec7f853` ("round-76: honest stop — frozen counters, wave evidence, base-red receipts", 2026-10-27), a descendant of `d919179` (the round-74 rows `check_spec_craft`/`check_sibling_reread`). The registry is appended in creation chronology; `check_sibling_reread` is its last row at base (`git merge-base --is-ancestor d919179 ec7f853` passes). C1 row before C2 row, matching the round-74 pair's order.
- **kind `gate`.** `check_gate_registry.py` rejects a `probe` whose source has an exact `--self-test` handler, and both scripts do: `check_desc_craft.py:1002` `ap.add_argument("--self-test", action="store_true")`; `check_r75_routed_repairs.py:1007` the same. Read from the AST-visible `add_argument` calls, not from help text.
- **verdict map.** Both `main()`s return `2` on environment errors (`check_desc_craft.py:1018,1025,1031,1037`; `check_r75_routed_repairs.py:1035`), `1` on an unmet target (`check_desc_craft.py:1049` `return 0 if held == TOTAL else 1`; `check_r75_routed_repairs.py:1042` `return 0 if closed == TOTAL else 1`) and `0` otherwise. `0=clean, 1=failed, 2=could-not-evaluate` is the declared map, and no code repeats.
- **withdrawal annotation (Q46).** Their claims were declared at r76 and never landed (r76–r78 all closed as honest stops). The in-cell text is `claim withdrawn r79 before data (declared r76, never landed); not a claim gate until redesigned and re-controlled`, i.e. the wording Q46 requires, with the round it is withdrawn in, at the same place the existing withdrawn rows carry it (`SKILL.md:455,480,488`).
- **self-test.** `` `--self-test` `` — exact `add_argument("--self-test")` handler in both files, so `has_flag_handler` finds it; a `gate` may not say `none`.
- **pinned values `in-file`.** `check_desc_craft.py` pins `SELF_SHA` (`:149`), the three page digests and the snapshot manifest name in the file; `check_r75_routed_repairs.py` pins `BASE`, `RENDER_CLIP`, `RENDER_STRIPPED`, `GATE_TOKENS`, the receipt path and `REPAIRS` in the file (`:72-98,549`). I did **not** cite `.ufo/waves/round-76/w2-registry-note.md`, because that path does not exist at the base revision (`git cat-file -e b10bcbc:…` -> 128), and a backticked pinned path must exist.
- **write scope.** `check_desc_craft.py`'s measurement path only reads (`git show`); its `--self-test` builds isolated git fixture repos under `WORK_DIR` (`:1252-1298`, removed at `:1437`). `check_r75_routed_repairs.py` re-runs the corpus gates in `git clone --shared` sandboxes under `$TMPDIR` (`:132-162`) and builds fixture repos (`:697-809`).

## Evidence (commands and their own exit codes)

1. `cd <sandbox>/clone && python3 -B verifiers/check_gate_registry.py --rev c3ee93d23faaee0b21a2f1c99cb314f706f459ec` -> `gate registry rows conformant 62 of 62 lane verifiers; phantom 0`, **rc=0**; `--json` run rc=0 with `conformant 62, of 62, phantom []`. Receipts `Kb79E01Registry-registry-tip.txt`, `-registry-tip.json`.
2. Same counter at the base `b10bcbc6…` -> `check_desc_craft.py  no registry rows naming it: 0 (need 1)`, `check_r75_routed_repairs.py  no registry rows naming it: 0 (need 1)`, `gate registry rows conformant 60 of 62 lane verifiers; phantom 0`, **rc=1**. Receipt `Kb79E01Registry-registry-base.txt`.
3. `wc -l SKILL.md` at the sandbox commit -> `592 SKILL.md`.
4. Checklist at the authentic lane root (read-only run in `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, whose `SKILL.md` is the base bytes): `python3 -B verifiers/verify_skill_checklist.py --json` -> **rc=1**, `{"exit_code": 1, "fail": 1, "na": 0, "pass": 10}`, and the only FAIL is `governance.citation_resolves | LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not resolve` — the dead pointer another seat repairs, exactly as the item states. Receipt `Kb79E01Registry-checklist-base-lane.json`.
5. Checklist compared in two identically shaped clones (directory named `kotoba-shokunin`, `../.ufo` linked to the real fleet `.ufo`): base at `b10bcbc6…` and tip at `c3ee93d2…` both print `10 pass, 1 fail, exit 1`; per-check status diffs: **none**; the tip's own details are `line_budget PASS "592 lines within budget 600"`, `box_map_complete PASS "45 boxes mapped"`, `trigger.citation_resolves PASS "209 repo-rooted citation token(s) resolve"`. Both worlds fail only `governance.citation_resolves`, on `../<sibling lane>/…` tokens absent under the scratch parent — clone shape, identical on both sides, so this change adds no FAIL. Receipts `Kb79E01Registry-checklist-cmp-base.json`, `-checklist-cmp-tip.json`.
6. `check_assertion_floors.py` (no `--rev`; it measures the worktree) in the same two clones: base **rc=1**, tip **rc=1**, stdout byte-identical (`diff` -> `FLOORS-IDENTICAL`); the single FAIL arm is the pre-existing `FAIL checklist observed=1863 floor=1863 self_test_failures=2`. My two lines change nothing in that measurement. Receipts `Kb79E01Registry-floors-base.txt`, `-floors-tip.txt`.
7. Patch portability: `git -C <clone at daa3a09> apply --check -v …/Kb79E01Registry.patch` -> `Checking patch SKILL.md...` clean, then applied -> `592` lines, `git diff --stat` -> `SKILL.md | 2 ++`.
8. Patch: `Kb79E01Registry.patch`, 3712 bytes, sha256 `c411106e1ce60f14a87840b42906642d3bfe1dee1f37d8f60042143d2c95c611`; `git diff --stat 2c56622 c3ee93d` -> `SKILL.md | 2 ++`, `1 file changed, 2 insertions(+)`.

Full transcript with the Q41 sandbox label (commit `c3ee93d23faaee0b21a2f1c99cb314f706f459ec`, clone path `/fast/scratch/hyaku/kotoba-r79/Kb79E01Registry/clone`) is `Kb79E01Registry-receipt.txt`.

## What this does and does not do for C1

- It clears the gate-registry arm of the C1 battery: 60 of 62 -> 62 of 62, phantom 0, exit 0, so `check_tip_battery.py`'s `check_gate_registry` gate step now leaves the battery's six-gate count one step closer to 6 of 6.
- It does **not** claim C1. The battery's other red gates (`check_assertion_floors`, `verify_skill_checklist`, `verify_corpus_integrity`) are other repair seats' items, and the frozen counter `check_tip_battery.py` was neither edited nor re-run here.
- Nothing was scored on a frozen C2 counter; no control world was run or re-interpreted by this seat.

## Risks

- **Integration collision (medium).** The C2 seat's registry row for `check_allowed_tools.py` will also be appended at the same table end. Both are pure additions at the same anchor; the L1 must stack them (my two rows after `check_sibling_reread`, the C2 row after mine or before — the counter does not care about row order), not pick one hunk. `git apply` of both patches independently against base will conflict at `SKILL.md:512`.
- **Withdrawal wording is a judgement call (low).** I chose `claim withdrawn r79 before data (declared r76, never landed)`. The counter does not inspect this text (it reads only kind, entry command, verdict pairs, self-test flags, pinned values, write scope, owner); Q46 is a reviewer-read requirement. If a reviewer prefers the bare round-78 wording, the change is text-only inside the same cell.
- **`in-file` over backticked paths (low).** Both counters also cross-check committed manifests/snapshots, but I recorded `in-file` because `check_desc_craft`'s digest table and `check_r75_routed_repairs`'s constants are the frozen pins. If the L1 wants the manifest path named too, `.ufo/waves/round-76/snapshots/MANIFEST.sha256` exists at base and can be appended to that cell — nothing else would move.

## Blockers

None. Scratch (`/fast/scratch/hyaku/kotoba-r79/Kb79E01Registry`) is removed before yield; no tool was installed, no pacman run, no lane or fleet mutation, no network fetch.

VERDICT: gate registry repaired in draft — 62 of 62 conformant, phantom 0, exit 0 at sandbox `c3ee93d`; SKILL.md 590 -> 592; checklist and assertion-floors measurements unchanged except for the pre-existing `governance.citation_resolves` FAIL; patch ready for L1 integration.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E01Registry.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E01Registry-receipt.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E01Registry-registry-tip.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E01Registry-registry-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E01Registry-registry-tip.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E01Registry-checklist-base-lane.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E01Registry-checklist-cmp-base.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E01Registry-checklist-cmp-tip.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E01Registry-floors-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E01Registry-floors-tip.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79E01Registry.md
