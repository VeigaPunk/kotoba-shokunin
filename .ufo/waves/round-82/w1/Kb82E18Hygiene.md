# Kb82E18Hygiene — build-tool hygiene audit (round 82, wave 1)

Seat: Kb82E18Hygiene (leaf; no subagent dispatch). Scope: scan proposed build tools for
hardcoded `/tmp`, mutating git outside a sandbox, fixture identity/toplevel checks, and
command exit capture. Read-only scan + bounded runtime proofs; no production writes, no
after-data scored.

Measured revision: lane base `47dbe8781657de563ff867caca6244d28e3db504` (scratch clone,
`git clone --shared`, toplevel asserted before any command). Fleet tools measured at fleet
repo HEAD `825b8a021d6e81c4967666cf27ab1f9bd6d483f9` (read-only). 82 tool files scanned
(`scripts/hyaku/*` + `verifiers/*`).

## Method

Runnable bounded audit script (stdlib only, re-runnable as sibling build proposals land):
`.ufo/waves/round-82/build/Kb82E18Hygiene-audit.py` (sha256
`a839e139a609e828a7082693908b960af96c20a69270359dd0a6a3a23ac25a69`).
Full scan receipt: `Kb82E18Hygiene-audit-receipt.txt` (sha256
`eb9e556a9d64e308fa7c39669c0db0f4a0c5321dbcf15fc636f4cd43f33569f8`); headline
`DEFECTS: 11 INFO: 20`, each finding adjudicated manually below. Two runtime proofs
(P1/P2) with their own receipts. All scan/poll processes were started and killed by this
seat only; `disk-guard.sh status` was green before the work (exit 0).

## Findings

### A. hardcoded `/tmp`

- **A1 CONFIRMED — routed defect.** `scripts/hyaku/jj-lane-selftest.sh:29`
  (`sha256 95b510d7c967ee857fce1efeaeaa8afb0391cda6911d0ef1ad634d3d59d31067`):
  `SB=$(mktemp -d /tmp/jj-hyaku.XXXXXX) || { echo "sandbox failed" >&2; exit 1; }`.
  The whole jj-lane self-test sandbox (bare remote + clones + jj state) is created under
  `/tmp` regardless of `TMPDIR`/`HYAKU_SCRATCH`, and the script exports neither TMPDIR
  nor scratch for children. Violates lane-addendum §7 item 4 verbatim ("a counter, probe
  or gate that writes under `/tmp` regardless of `TMPDIR`/`--work` … is a routed defect
  this round"). **Runtime proof P1** (receipt `Kb82E18Hygiene-p1-jj-lane-tmp.txt`, sha256
  `6b2c422330f5688500fe80489e47bae49623c39c8ca8cb09e99043ac726a0e57`): with
  `TMPDIR=/fast/scratch/hyaku/kotoba-r82/Kb82E18Hygiene/tmp` exported, the exact line
  created `/tmp/jj-hyaku.NkTUII` (removed immediately). Suggested shape:
  `SB=$(mktemp -d "${TMPDIR:-/var/tmp}/jj-hyaku.XXXXXX")` plus `export TMPDIR="$SB/tmp"`.
- **A2 CONFIRMED.** `verifiers/check_mcp_instructions.py:274` (base blob
  `2127fedd00a5e295eba61821beab45a73e7a7c1c`, sha256
  `8e04e8fc3eae12789ee1db42b0ef593f583f107e61dc54fe465ea52238838cae`):
  `with tempfile.TemporaryDirectory(prefix="mcp-self-test-", dir=LANE) as td:` — the
  `--self-test` PATH shim (a directory containing a `python3` symlink that is put on the
  child gate's PATH, child run with `cwd=LANE`) is created **inside the live lane working
  tree**, not in TMPDIR. Removed on normal exit, but a SIGKILL/reaper window leaves an
  untracked `mcp-self-test-*` dir in the production lane. **Runtime proof P2** (receipt
  `Kb82E18Hygiene-p2-mcp-lane-temp.txt`, sha256
  `2db646a34e1c9249907dc44305e6f04e24dd8b81ff180bf85941c33d5a0de4f6`): strace of the
  real `--self-test` in the scratch clone shows
  `mkdir("/fast/scratch/hyaku/kotoba-r82/Kb82E18Hygiene/clone/mcp-self-test-gznq60s3", 0700) = 0`
  while the sibling git128 shim correctly landed in TMPDIR
  (`.../tmp/mcp-self-test-git128-s6foqb01`). Fix: drop `dir=LANE` (honour TMPDIR).
- **A3 INFO (accepted by design, no change requested).** `scripts/hyaku/disk-guard.sh:291-293`
  honours `${TMPDIR:-/var/tmp}` first; the `/var/tmp` mktemp is a deliberate last-resort
  fallback when TMPDIR is unusable — consistent with the reaper policy.
  `verifiers/fault_injection_corpus.sh:53` uses `${TMPDIR:-/tmp}` — honours TMPDIR, contract-clean.

### B. mutating git/jj outside a sandbox

**None confirmed at base.** Every verifier fixture write lives in a
`tempfile.TemporaryDirectory`/`mkdtemp` world pinned with `-C`/`cwd=`; fleet writers
(`fleet-commit.sh`, `jj-lane.sh`, `append-closure.py`) are the sanctioned integrator
tools and are excluded by name in the audit. `jj-lane-selftest.sh` keeps all mutations
inside its own sandbox — its only escape is the sandbox *location* (A1).
Corroboration note (not a new defect): `verifiers/verify_skill_checklist.py:2521-2527`
(base blob `6aab16849bd6d71ded8f3bcb3f95668f14f6a78f`) — the self-test arm
`governance: live round-65 corrections land, errata-excused` reads
`live_repo = Path(__file__).resolve().parent.parent`; this is exactly the live-reach that
produces the committed before-value `1 failure(s) over 1863 assertions` for C2.

### C. fixture identity/toplevel posture

Reference pattern (both present): `verifiers/check_substrate_repin_v2.py:414-419`
(asserts `rev-parse --show-toplevel` == the fixture repo and sets fixture identity before
the first commit), `verifiers/check_r75_routed_repairs.py:144,702`,
`verifiers/check_report_pointers.py:592`.

- **8 files — identity pinned, no `--show-toplevel` assert** (all fixtures are in
  TMPDIR-honouring temp worlds, so practical risk is low; the assert is the fleet
  contract's named guard): `box_proof_case_deletion.py`, `check_agentdef_boxes.py`,
  `check_alwayson_boxes.py`, `check_overlap_levers.py`, `check_r63_routed_repairs.py`,
  `check_r66_routed_repairs.py`, `check_r69_routed_repairs_v2.py`,
  `verify_corpus_integrity.py` (identity spot-verified: `-c user.name=t` at base lines
  1177/1240).
- **8 files — both present** (clean): `check_allowed_tools.py`, `check_author_rules.py`,
  `check_cn_vendor_surfaces.py`, `check_desc_craft.py`, `check_r64_routed_repairs.py`,
  `check_sdk_allowed_tools.py`, `check_spec_craft.py`, `check_tip_battery.py`.

### D. command exit capture

- **D1 CONFIRMED (minor robustness).** `verifiers/check_r69_routed_repairs_v2.py:714-717`
  (base blob `0b9ca25973b14cf432d1967b0fdbc7f364fc96b1`): the real-git fixture loop
  `for cmd in (["git", "init", "-q"], ["git", "add", "-A"], ["git", "-c", user…, "commit", "-qm", "fixture"]): subprocess.run(cmd, cwd=fx, capture_output=True)`
  checks neither `check=True` nor `returncode`; a fixture git failure degrades to an empty
  rev and a confusing downstream env-error. The neighbouring sandbox block at 587-592 in
  the same file shows the correct pattern (`if … .returncode != 0: return None`).
  (The unchecked `add -A` at line 585 is transitively covered: its commit is returncode-checked.)
- **D2 INFO.** 11 fleet shell tools + `fault_injection_corpus.sh` use pipelines without
  `set -o pipefail`; every claim-bearing capture was reviewed and takes the command's own
  exit (`rc=$?` after command substitution or a direct command — disk-guard.sh:60-78,
  515-519, 963-1173; inline.sh:60-75; jj-lane-selftest.sh:662-789), never a pipeline's
  last stage. No `local x=$(cmd)` maskers, no `| tee` claim receipts, no `os.system` in
  any scanned tool.

## Round-82 counter hygiene status (context for C1/C2 seats)

`verifiers/check_substrate_repin_v2.py` (C1 counter): TMPDIR-honouring temp worlds,
toplevel assert + fixture identity in its self-test (414-419), `strings` and instrument
runs returncode-checked (226-227, 253-258) — clean on A/B/D.
`verifiers/verify_skill_checklist.py` (C2 counter): TMPDIR-honouring fixture worlds —
clean on A/B/D; its one live-reach arm is the known C2 failure (B corroboration above),
a data-dependence repair, not a hygiene escape.

Sibling build proposals under `.ufo/waves/round-82/build/` currently hold 5 markdown/text
docs only (no executable tool code); nothing executable to audit there yet. The audit
script accepts no arguments by design (bounded) and can be re-run as proposals land.

## No-harm

No production file, lane git index, jj state, or sibling path was written. All work in the
asserted scratch clone at `/fast/scratch/hyaku/kotoba-r82/Kb82E18Hygiene` (deleted after
receipts were copied). No installs/upgrades (none needed). No pacman activity. Bounded
runtime: P1+P2 ≈ 45 s wall, 2 concurrent processes max.

## VERDICT: 2 confirmed hygiene defects with runtime proof (jj-lane-selftest.sh:29 hardcoded /tmp — routed per lane-addendum §7.4; check_mcp_instructions.py:274 temp shim in live lane tree) + 1 minor unchecked-fixture-commit (check_r69_routed_repairs_v2.py:714) + 8 verifiers missing the contract's fixture toplevel assert (identity present, temp-world sandboxed); no confirmed git-mutation-outside-sandbox; both round-82 counters hygiene-clean on A/B/D.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E18Hygiene.md
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E18Hygiene-audit.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E18Hygiene-audit-receipt.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E18Hygiene-p1-jj-lane-tmp.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E18Hygiene-p2-mcp-lane-temp.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E18Hygiene-evidence-shas.txt
