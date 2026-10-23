# Round 62 no-harm battery run

- Script: `.ufo/waves/round-62/noharm-battery.sh` (written executable from the draft).
- Measured revision: `3e7aed9b61bbfd83e0c800213b6dfc6da6191f85`, read with `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse master`.
- Receipt: `.ufo/waves/round-62/noharm-tip.txt`; its first line names the measured revision. Run command: `bash .ufo/waves/round-62/noharm-battery.sh --base a745411c66d4765e9ac0ce48f1d96c34f425dab4 --tip 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85`.

The battery did **not** print `no-harm OK`. It emitted these failures verbatim before its 110-second timeout (the run command used `timeout 110s`; the receipt records `Battery exit code: 124`):

```text
FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1
        tip: verifiers/check_erratum_absorption.py        no registry rows naming it: 0 (need 1)
        tip: verifiers/check_routed_repairs_v2.py         no registry rows naming it: 0 (need 1)
        tip: gate registry rows conformant 36 of 38 lane verifiers; phantom 0
FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/lessons/round-61-verifier-spotcheck.md 
```

The receipt shows execution stopped after the `boxproof` arm; later arms and the final verdict were not reached. No failing gate or verifier was edited. At the measured revision, `git cat-file -e <revision>:<file>` found `check_erratum_absorption.py` and `check_routed_repairs_v2.py` present, and `check_scoped_rules_v31.py` missing. Thus no optional `SKIP <name> (not landed)` line was reached or printed; the required `scoped-v31` arm was not run and would be blocked by its missing file.

Contention cap: one serial battery invocation (no more than one concurrent job, within the four-process cap), bounded at 110 seconds (below the 120-second per-command limit); no agents or parallel jobs were started. Installs: none. Blocker: the captured gate failures and timeout prevent the requested exit-0 acceptance; report only, no gate remediation.