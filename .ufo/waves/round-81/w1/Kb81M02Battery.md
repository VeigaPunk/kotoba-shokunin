# Kb81M02Battery — E6 counter mutation probe

## Snapshot and detector

Used the published `Kb81E05Erratum.patch` snapshot, SHA-256 `c15680f81d2684fc40ef7aeef21143f217ecf4e4fc62b9ea91a7bd5787cfcf4f`. Applied it to a fresh base checkout; `git apply` returned 0. Current post-image: blob `eb00200ee6987a2fd95086915a333fe258aa6c82`, SHA-256 `1753b11c11c6f907be838cb28842e28d01e7935e19d5afb3a6b46afdac51d660`, 751 lines. The pin entries matched blobs obtained by applying the then-current E01/E02 patches to base (`bbee51f2…` and `59602942…`). E05 self-test on those exact counter bytes: exit 0, `self-test: 0 failure(s) over 69 assertions`.

Test worlds were isolated scratch commits: base `b284223105f4d106f7e8f56ed4fd296c643cda0e`; T_repair `ab72e083d3d3e149af9b091e317f58e48fb55926` (current published E01/E02 patches); T_tamper `72a4eeb13a764a3c78cc7cdf58bf5c3124db14db` (one-byte change in integrity verifier); T_stub `ab52e70588f3889c9962db782400dbea94078dda` (integrity verifier replaced by `import sys\nsys.exit(0)\n`). All measured with the same counter and `--fleet /home/vgpnk/Projects/shokunin`; gate outputs are intentionally not treated as the detector for these probes. `--self-test` on every current mutant also returned 0 failures/69 assertions, showing that self-test masks these counter mutations (it replaces `INSTRUMENT_PINS` and derives its size-world constants from `LINE_CAP`).

## Mutants and actual outputs

- **Pristine V0 @ T_repair:** exit 1 because battery is 4/6 in this partial repair world; all five guards PASS. Exact final line: `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 4 of 6`.
- **(a) `LINE_CAP=40` @ T_repair:** exit 1; `FAIL guard instrument-size: instruments gain 402 lines > 40`; guards 4/5. **KILLED** (the size arm fires).
- **(b1) Remove only the r81 integrity SHA from its tuple** @ T_repair: exit 1; `FAIL guard instrument-pin: verifiers/verify_corpus_integrity.py blob bbee51f2bae5b33b123a546150e83352d68eeebc ... is not a pinned blob`; guards 4/5. **KILLED** (pin arm fires).
- **(b2) Remove the entire `verify_corpus_integrity.py` dictionary entry** @ T_tamper: exit 1 from the partial battery, but all five guards PASS, including `instrument-pin`; final line reports guards 5/5. **SURVIVED** as a coverage mutant: deleting a whole row disables pin enforcement for that instrument, and the numstat-neutral byte tamper is then unobserved. This is not a contract change recommendation.
- **(c) Replace the r81 integrity pin with its base SHA** @ T_repair: exit 1; same `instrument-pin` failure on actual blob `bbee51f2…`; guards 4/5. **KILLED**.
- **(d) Two-line stub at the amended cap:** pristine V0 @ T_stub fails both `instrument-size` (`instruments lose 1491 lines > 900`) and `instrument-pin` (stub blob `e15e0b45…`); guards 3/5. To isolate cap independence, **Vd** sets `LINE_CAP=1000000`: at the same T_stub, `instrument-size PASS` while `instrument-pin` fails on `e15e0b45…`; guards 4/5. **KILLED by pin under a nonbinding cap**, confirming the stub fails independently of the cap.

Output format check: exact frozen final-line structure was emitted for both base forms using the current amended counter and real fleet root:

- `--repo .` from the scratch lane root: `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 4 of 6` (exit 1; base battery result).
- `--repo /fast/scratch/hyaku/kotoba-r81/Kb81M02Battery/kotoba-shokunin`: same final line (exit 1).

The 4/6 count is the recorded base result; these checks verify output shape, not the claim after-value.

## Scope discrepancy and restoration

The frozen plan and E05 hunk inventory specify `LINE_CAP=140` and adding exactly two pin members without dropping existing members. The published E05 patch tested above instead says `LINE_CAP=900` and uses tight `(base, r81)` tuples, dropping the earlier integrity/independent alternate blobs. I used the actual published patch bytes for the requested probes; the 900-cap `LINE_CAP=40` mutant still fires at the actual 402-line increase. This divergence should be reconciled by the integration owner; it is not silently treated as a plan change here.

Mutants were separate files; the pristine applied counter remained SHA-256 `1753b11c11c6f907be838cb28842e28d01e7935e19d5afb3a6b46afdac51d660` throughout. Lane counter remained unchanged at SHA-256 `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a`. All world commits, variants, and receipts lived under `/fast/scratch/hyaku/kotoba-r81/Kb81M02Battery/`; scratch is removed before handoff.

VERDICT: Three probes killed; whole-entry removal survives and bypasses instrument-pin; patch differs from frozen E6 cap/tuple instructions.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81M02Battery.md