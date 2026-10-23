# Round 61 — Gate registry draft (ScribeSkillReg)

## Scope and disposition

Drafted the complete `SKILL.md` § Gate registry row for `verifiers/check_routed_repairs.py` and a replacement row for `verifiers/check_scoped_rules.py` that marks the r60 v2 predicate superseded while the r61 v3 redesign is pending. These are report-only drafts; no lane file was edited. The only write from this seat is this report.

Target surface for integration: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/SKILL.md`, § Gate registry. Proposed exact rows:

```markdown
| `verifiers/check_routed_repairs.py` | gate | `python3 -B verifiers/check_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; reads committed blobs only | kotoba |
| `verifiers/check_scoped_rules.py` | gate | `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — claim withdrawn r61 before v3 data (the r60 v2 predicate is superseded); not a claim gate until redesigned and re-controlled | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
```

The withdrawal annotation applies to using the r60 v2 counter as the r61 claim gate; it does **not** withdraw the plan's r61 C1 v3 claim. Once v3 has actually been redesigned and re-controlled, the integration owner should remove/update the temporary annotation in the same integration that lands the counter and its receipts. The v3 row's CLI, pinned-values, self-test, and write-scope cells follow the plan/current registry pending a check against the landed v3 bytes; this seat did not inspect an integrated v3 implementation.

## Provenance and findings

Read-only sources consulted:

- `plans/round-61.md` (base `f3246d1493b60ea1c0d947a19c39f9e08e92f326`): C1 specifies the v3 counter and `--rev <tip> --fetch`; C2 specifies six repairs and the exact `--rev <rev>` base/tip count contract. The plan says the frozen checker and base receipt are committed before repairs/data.
- `SKILL.md` § Gate registry: table columns are Name, Kind, Entry command, Verdict map, Self-test, Pinned values, Write scope, Owner; the registry's own check command is `python3 -B verifiers/check_gate_registry.py --rev <rev>`. Existing row for `check_scoped_rules.py` has `in-file` pinned values and `self-test repos under $TMPDIR (removed); --fetch reads the network` write-scope wording.
- `corpus/lessons/round-58.md` § Mistakes, M70, plus `SKILL.md` existing rows for `check_sweep_mutants.py`, `check_infoless_fences.py`, and `check_agentdef_boxes.py`: precedent is an in-cell `claim withdrawn … not a claim gate until redesigned and re-controlled` annotation, not a `probe` relabel or an edit to history. Q46 in `corpus/QUALITY.md` states the same registry rule.
- `verifiers/check_routed_repairs.py`: its header says it is the round-61 C2 counter; frozen repair patterns are in-file; its measured-revision inputs are read using `git show <rev>:<path>`; `--self-test` exercises an all-repairs world and a base world; exit 0 iff all six are present, exit 1 otherwise, and 2 for could-not-evaluate. The checker explicitly limits itself: it does not judge substantive honesty of repair text. This supports the proposed new row's `in-file` and `none; reads committed blobs only` cells.
- `verifiers/check_scoped_rules.py`: the currently readable source labels itself the round-60 counter and specifies the v2 predicate; this confirms the need to mark that version as superseded rather than imply it already implements r61 v3.

### Existing C2 base receipt (copied, not rerun)

Artifact: `.ufo/waves/round-61/controls/C2-base.txt`. The plan specifies the base invocation as `python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326`, with expected base score 0 of 6 and exit 1. The receipt's visible contents are:

```text
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
base-exit=1
```

This is a read of the supplied receipt, not a command executed by this seat. The receipt text itself does not print its invocation or a UTC timestamp; I do not present it as a fresh measurement. No `date -u` or gate command was run here, and no check pass/fail is claimed for this seat.

## Gates, touched surfaces, and limits

- **Behavior drafted:** one gate row for the committed-blob-only C2 checker; one updated C1 row carrying the r58-style temporary withdrawn/redesigned warning.
- **Gate execution:** none. `check_gate_registry.py`, either counter's `--self-test`, C2 base/tip measurements, C1 v3 fixtures/controls, and live `--fetch` were not run by this seat. The L1 must validate the integrated row against landed v3 and run the applicable gates; no report-only draft is registry verification.
- **Files read:** `plans/round-61.md`, `SKILL.md`, `corpus/lessons/round-58.md`, `corpus/QUALITY.md`, `verifiers/check_routed_repairs.py`, `verifiers/check_scoped_rules.py`, and `.ufo/waves/round-61/controls/C2-base.txt`.
- **File written:** `.ufo/waves/round-61/wave/ScribeSkillReg.md` only.
- **Out of scope / not established:** no source or registry edit; no C1 v3 implementation review, fixture/control attack, re-score of r60 evidence, C2 rerun, C3 review, or integration. No claims are made about tip behavior or the eventual v3 write scope.
- **Installs:** no installs.
- **Blockers:** none.
- **Produced:** report-only drafts for the routed-repairs gate row and the scoped-rules v3 transition annotation.
