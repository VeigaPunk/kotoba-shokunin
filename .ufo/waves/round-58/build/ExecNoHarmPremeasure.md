# ExecNoHarmPremeasure — Q19 before-values and no-harm baseline (round-58 build wave)

Result: DONE — all ten assigned counters were run at base `f56f6e191762c27c1aa2af11a204db9e2ca4edec` and recorded with command, summary line and exit in `.ufo/waves/round-58/build/noharm-base.txt`; nine exit 0, `check_plugin_manifests` exits 1 as a **pre-existing red** (4 rows backed against its frozen `TARGET = 5`), and `verify_skill_checklist`'s three sandbox-only FAILs were shown to be path artifacts by a lane-faithful rerun at the same revision that exits 0 (11 PASS).

## What was run, where, when

- Sandbox clone: `/fast/scratch/hyaku/kotoba-r58/ExecNoHarmPremeasure`, clean tracked checkout of base `f56f6e19` (only untracked scratch dirs `.noharm/`, `mirror/`, `head/`); `git rev-parse HEAD` printed first in the receipt.
- Every command capped with `timeout 900`; three commands used `--fetch` (agent definitions, plugin manifests, explicit invocation), run 2026-10-23T08:09Z–08:11Z (host `date -u` at receipt: `Fri 23 Oct 2026 08:12:03 AM UTC`).
- No lane code was executed and no pre-existing lane file was written; the only lane writes are the two files listed under “Files changed”. No sandbox commit, no push, no tool installed.
- Receipt (assigned): `.ufo/waves/round-58/build/noharm-base.txt`, sha256 `1fa927ab45a7ccb4d176253cce17a25f59127228ca53f6dd1d0ca240f2c75658`.
- Raw logs (base, retained): `/fast/scratch/hyaku/kotoba-r58/ExecNoHarmPremeasure/.noharm/<name>.log`.

## Before-values at base (exit / summary line)

Commands as run (cwd `/fast/scratch/hyaku/kotoba-r58/ExecNoHarmPremeasure`, base `f56f6e191762c27c1aa2af11a204db9e2ca4edec`; each wrapped in `timeout 900`):

```
python3 -B verifiers/check_agent_definitions.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec --fetch
python3 -B verifiers/check_plugin_manifests.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec --fetch
python3 -B verifiers/check_explicit_invocation.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec --fetch
python3 -B verifiers/check_description_thresholds.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
python3 -B verifiers/check_mcp_instructions.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
python3 -B verifiers/check_gate_registry.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
python3 -B verifiers/check_correction_sweep.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
python3 -B verifiers/check_sources_append_only.py --base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec
python3 -B verifiers/verify_skill_checklist.py
python3 -B verifiers/check_assertion_floors.py
```

Exits in that order: `0 1 0 0 0 0 0 0 0 0`.

| exit | command | observed summary |
|---|---|---|
| 0 | `check_agent_definitions.py --rev <base> --fetch` | `agent-definition locations found on the live page 7 of 7; new ground 3` (TARGET 5, NEW_TARGET 2) |
| 1 | `check_plugin_manifests.py --rev <base> --fetch` | `plugin manifests found on the live page 4 of 4; new ground 4`; rejects VS Code, Copilot CLI (`plugin.json` not well-formed, shared by two rows) and opencode (`.opencode/plugins/` not well-formed) |
| 0 | `check_explicit_invocation.py --rev <base> --fetch` | `user-typed invocation forms found on the live page 5 of 5; new ground 4` (TARGET 4, NEW_TARGET 2); VS Code and Gemini CLI unbacked |
| 0 | `check_description_thresholds.py --rev <base>` | `description thresholds backed 7 of 7 clients` (TARGET 4) |
| 0 | `check_mcp_instructions.py --rev <base>` | `mcp instructions backed 7 of 7 clients` (TARGET 3) |
| 0 | `check_gate_registry.py --rev <base>` | `gate registry rows conformant 30 of 30 lane verifiers; phantom 0` |
| 0 | `check_correction_sweep.py --rev <base>` | `correction sweep: 0 stale block(s)` |
| 0 | `check_sources_append_only.py --base 422ffd10… --rev <base>` | `sources append-only rows clean: 5 commits scanned, 0 protected-cell changes` |
| 0 | `verify_skill_checklist.py` (lane-faithful rerun) | 11 PASS, 0 FAIL, 0 N/A; `trigger.line_budget: evaluated 598 — 598 lines within budget 600` |
| 0 | `check_assertion_floors.py` | 13 PASS, observed 10/152/99/175/1852/62/123/330/165/56/68/55/89 (floors 10/152/93/175/1852/62/123/330/150/56/68/51/89) |

Raw log sha256 (base): `agent_definitions` `ccd808e2…`, `plugin_manifests` `3d8ecfeb…`, `explicit_invocation` `d90ad0bf…`, `description_thresholds` `afe3006e…`, `mcp_instructions` `561cf4b4…`, `gate_registry` `3ea84b55…`, `correction_sweep` `a740e0c7…`, `sources_append_only` `08d711af…`, `skill_checklist` `a4d75a6a…`, `assertion_floors` `524cd46e…` (full digests printed by `sha256sum` in the session; truncated here only for width).

## Calibration findings

1. **`verify_skill_checklist.py` is working-directory dependent; its raw sandbox exit 1 is not lane state.** In the plain clone the run exits 1 with exactly three FAILs: `trigger.name_directory` (frontmatter name `kotoba-shokunin` vs clone directory `ExecNoHarmPremeasure`) and the two citation checks, whose subjects are `../` hops into the **fleet root** (`../PROTOCOL.md`, `../.ufo/reports/round-7/kotoba.md`, `../AXES.md`, `../MISSION.md`, `../kasegi-shokunin/...`). All of those exist in the lane's real parent (`test -e /home/vgpnk/Projects/shokunin/<p>` → EXISTS for each). A clean clone at the same base rev, placed in a directory named `kotoba-shokunin` with every fleet-root top-level entry symlinked read-only into its parent (ancestor resolution then identical to the lane), exits 0 with `--json`: `pass 11, fail 0, na 0, exit 0`. **The base before-value for this check is exit 0**; a failure after integration is therefore real, and the checker must be run in the lane or an equivalent checkout, never in a seat-named sandbox.
2. **The same directory rule applies to `check_assertion_floors.py`** (no `--rev`; it shells out to the other verifiers in the same tree). Base value comes from the lane-faithful mirror, not from the seat-named clone.
3. **`check_plugin_manifests` is red at base for content, not for code.** `TARGET = 5` (`verifiers/check_plugin_manifests.py:216`) and the predicate `return 0 if found >= TARGET and ground >= NEW_TARGET else 1` (`:1037`); base backs 4 rows. Three SKILL.md rows are rejected (`VS Code`, `Copilot CLI` share the bare token `plugin.json`; `opencode` carries `.opencode/plugins/`). This is a known pre-existing state, not a wave effect; the no-harm criterion is that the backed count and new-ground count do not drop (4 and 4) and that the reject set does not grow.
4. **Three before-values depend on live vendor pages.** `--fetch` values can drift with the vendors' sites; if a post-integration run differs, re-run the same command at base before attributing the delta to the wave.
5. **The gate-registry universe grew between base and lane HEAD, by design.** Base has 39 blobs under `verifiers/` (30 counted `.py`/`.sh`); HEAD `a39942c` adds `verifiers/check_command_files.py` and `verifiers/check_sweep_mutants.py` → 32 counted. Both revisions are 100 % conformant. A count comparison against base alone would misread `30 → 32` as change; conformance is the invariant.
6. **Coverage of this item.** Ten of the lane's 32 registered verifiers at lane HEAD (30 at base) are measured here, exactly the assigned set. The remaining registered rows are not measured by this item; a full-gate no-harm sweep would need their registry entry commands.

## Informational pre-integration HEAD sweep (not the assigned receipt)

Base is 3 commits behind lane HEAD `a39942c94027cd3875144284112422d1aa642260` (plan draft, freeze, erratum; 32 files, 9392 insertions, no deletions). Because integration will sit on HEAD, the same ten commands were run there (clean clone in `.../ExecNoHarmPremeasure/head/kotoba-shokunin`, fleet-root siblings symlinked; logs in `.../head/.noharm-logs/`):

| exit | command | observed at HEAD |
|---|---|---|
| 0 | `check_agent_definitions --fetch` | 7 of 7 live, new ground 3 |
| 1 | `check_plugin_manifests --fetch` | 4 of 4 live, new ground 4, same three rejects |
| 0 | `check_explicit_invocation --fetch` | 5 of 5 live, new ground 4 |
| 0 | `check_description_thresholds` | 7 of 7 |
| 0 | `check_mcp_instructions` | 7 of 7 |
| 0 | `check_gate_registry` | **32 of 32** conformant, phantom 0 |
| 0 | `check_correction_sweep` | 0 stale blocks |
| 0 | `check_sources_append_only` | 5 commits, 0 protected-cell changes |
| 0 | `verify_skill_checklist` | 11 PASS (`--json`: pass 11, fail 0, na 0); citation tokens 135, placeholders scanned 539 |
| 0 | `check_assertion_floors` | 13 PASS, identical observed/floor pairs to base |

Exit codes are identical at base and HEAD for all ten. Differences are counts only: gate registry 30→32, citation tokens 131→135, placeholder scan 537→539, **SKILL.md 598→600 lines**.

## Highest no-harm risk for the wave

`SKILL.md` at HEAD is **exactly 600 lines against the budget of 600** (`trigger.line_budget: evaluated 600 — 600 lines within budget 600`). The C1 section therefore cannot add a net line: the paired move-out (`ExecBudgetMove`) must land verbatim and in the same integration, or the checklist flips to exit 1 and this baseline's only green on that file is lost. Two integration orderings keep the gate green: apply the move first, or apply section and move together.

## Post-integration comparison protocol (what "no harm" means here)

Run the same ten commands at the integrated rev with the same flags (`--fetch` on the first three; `--base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4` on the append-only check). Run the two worktree commands in the lane itself (or a checkout named `kotoba-shokunin` whose parent carries the fleet root). No harm iff:

- the nine green exits stay 0;
- `check_plugin_manifests` stays exit 1 with `found >= 4` and `new ground >= 4`, and its reject list does not grow (an exit 0 there would require a fifth backed row and must be explained, not merely celebrated);
- `check_gate_registry` stays fully conformant and phantom-free, with its universe equal to the number of `.py`/`.sh` blobs under `verifiers/` at that rev;
- `check_assertion_floors`: no observed value falls below its recorded floor (values may rise);
- `verify_skill_checklist`: 11 PASS, and `trigger.line_budget` still within 600.

The round-58 C1 counter `verifiers/check_command_files.py` does not exist at base (confirmed absent; present at HEAD) and is not part of this baseline — these ten values must not be mixed with the C1 predicate `F >= 4 and G >= 3`.

## Files changed

- `.ufo/waves/round-58/build/noharm-base.txt` (new; the assigned receipt).
- `.ufo/waves/round-58/build/ExecNoHarmPremeasure.md` (this report).

No lane source, verifier, corpus, plan or config file was touched; no sandbox commit was made.

## Risks and blockers

- Live-page drift is the only source of nondeterminism in the three `--fetch` values; re-measure at base before attributing a delta.
- The lane-faithful mirror reproduces ancestor resolution by symlinking the fleet root read-only; it does not snapshot fleet-root content. A change to `PROTOCOL.md`, `AXES.md`, `MISSION.md` or sibling lanes between now and integration would move the citation count (the 131→135 delta shows such counts are content-sensitive).
- No blocker; nothing in this item contends for a lane write or a counter the build wave edits.
