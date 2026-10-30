# Kb82E19PinGuard — independent predata guard

Axes: freshness; operability. No production after-value measured, no axis score or 6/6 battery claim.

## Deliverable and freeze

Stdlib-only `build/Kb82E19PinGuard_guard.py`, SHA256 `61ace2b9e586f34f9344e0147a5f586b94c9680e17f900494f76b36ecbfd77e3`.
Frozen before any production after scoring by this seat. L1 owns committing the predata freeze and any subsequent integration gate.

The guard never executes candidate verifier code or consumes its claimed PASS counts. It reads committed blobs using `git -C`, parses defaults via AST, measures file-descriptor bytes with SHA256 and ns mtime, and checks stat identity before/after reading. Live identities are embedded in the frozen guard, so subsequent host replacement cannot be laundered by updating candidate pins.

Independent measurements:

| Substrate | ELF magic | bytes | mtime ns | SHA256 |
|---|---|---:|---:|---|
| `/home/vgpnk/.local/bin/omp` | yes | 276244656 | 1793326786168359786 | e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f |
| `/home/vgpnk/.opencode/bin/opencode` | yes | 240416944 | 499162500000000000 | ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7 |

## Exact retained evidence

- `build/Kb82E19PinGuard_before.json`: command-owned exit **1**, elapsed 0.492 s, revision `47dbe8781657de563ff867caca6244d28e3db504`. Expected predata reds: omp SHA pin, omp ns-mtime pin, and both instruments' omp defaults (missing `omp.real`). Opencode identity/pin/defaults hold. Census preserves **42/42** identities, no additions/deletions/changes, and removal ledger unchanged.
- `build/Kb82E19PinGuard_selftest.json`: command-owned exit **0**, elapsed 0.063 s; **0 failure(s) over 9 assertions**. Matching fixture green; wrong binary despite self-pin, wrong SHA pin, one-ns wrong mtime, deleted class, either stdout-stub instrument with otherwise correct pins/defaults, changed ledger, and changed live identity all red. No host binary used in fixture selftest.
- `build/Kb82E19PinGuard_scope.json`: exit **0**, retained historical extractor-scope stat from counter base `c69711ee08279609374d895bb0f3c8c18ccf15c9` to round82 base: baseline +6/-, removal ledger +39, pins +7/-, surfaces +980/-; 4 files, 901 insertions/131 deletions. `surfaces-baseline.json` unchanged over that range. These historical changes are already within the frozen round82 base, not newly approved semantic edits.
- `build/Kb82E19PinGuard_SHA256.json`: full SHA256 manifest for script and receipts. Both execution receipts carry the script SHA and exact command/stdout/stderr/exit; load-at-start retained.

## Allowed syntax changes and risks

Executable instrument AST is compared against immutable round82 base. Allowed deltas only: the value of the one top-level `BINARIES` or `DEFAULT_BINARIES` dictionary; explanatory module/function/class docstrings; comments/formatting ignored by AST. Default dictionaries must remain literal dictionaries with exactly `omp` and `opencode` string values. Candidate default files must match live measured ELF magic, SHA, byte count and ns mtime. Baseline omp mtime requires a timezone and exactly nine fractional digits, without widening tolerance. All base census class identities (including omp), literals, kinds and verdicts must remain exactly equal; the removal ledger must remain unchanged.

A legitimate extractor semantic change will be honestly **red** under this base-semantic guard. L1 has explicitly reserved a separate narrow full-postimage review/freeze rather than widening this guard blindly. The historical 980-line extractor diff is scope-accounted, not re-certified line-by-line here. ELF identification checks magic, not ELF structural validity; frozen SHA binding supplies actual host-byte identity. This guard does not prove exhaustive runtime discovery or prompt effectiveness and does not replace independent loader-pair derivation seats.

LSP tools were not exposed; no symbol-refactor claims. No tools installed, no production files/index/configuration changed, no commits/pushes, no counted scripts run. Disk guard reported scratch 428.7G free before work. Scratch clone asserted at the named toplevel/base before use; scratch deleted after copying receipts.

## Main-agent invocation

`python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E19PinGuard_guard.py --repo <integration-clone> --rev <full-candidate-commit>`

Set TMPDIR to an existing owned scratch directory for `--self-test`. Main owns all post-integration production scoring. No missing implementation prerequisite; semantic extractor changes require the separately owned review described above.

VERDICT: Frozen independent guard delivered; authorized fixtures 9/9; predata base honestly red on stale omp pins/defaults.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E19PinGuard.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E19PinGuard_guard.py ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E19PinGuard_before.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E19PinGuard_selftest.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E19PinGuard_scope.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E19PinGuard_SHA256.json
