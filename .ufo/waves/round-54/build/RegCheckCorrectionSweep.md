Result: DONE — Inspected the pinned source and ran help and self-test; the verifier is a gate with in-file expected patterns.

| `verifiers/check_correction_sweep.py` | gate | `python3 -B verifiers/check_correction_sweep.py --root .` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none; self-test temporary fixtures under `$TMPDIR` | kotoba |

Evidence for the row:

- **Name / entry command:** `verifiers/check_correction_sweep.py:16-17` gives the invocation modes; `:125-133` confirms `--root .` reads the current repository tree. `:196-202` makes one of `--rev`, `--root`, or `--self-test` required.
- **Kind / verdict map:** `:10-17` defines stale-block detection and documents 0/1/2. `:108-122` identifies violating blocks and missing files; `:205-213` returns 2 for a missing comparison file, 1 for violations, and 0 when clean. Self-test mismatch/success returns 1/0 at `:190-193`. Invalid CLI input also uses argparse's exit 2 (`:196-202`). Thus gate is appropriate: 1 denotes a failed check.
- **Self-test:** exact flag is `--self-test` (`:199-204`). In the clone at `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`, `python3 -B verifiers/check_correction_sweep.py --help` exited 0; last output line: `--self-test`. `mkdir -p .tmp-check-correction-sweep && TMPDIR="$PWD/.tmp-check-correction-sweep" python3 -B verifiers/check_correction_sweep.py --self-test` exited 0; last output line: `0 failure(s) over 11 assertions`.
- **Pinned values / compared files:** Expected stale/declared regexes are literals in `REGISTRY` (`:30-72`), so `in-file` is accurate; no committed expected-value file is read. It sweeps these eight unique files: `corpus/README.md`, `SCORECARD.md`, `PROVINCE.md`, `SKILL.md`, `corpus/knowledge/claude-md-surface.md`, `corpus/knowledge/instruction-surface-census-round13.md`, `corpus/knowledge/agents-md-and-dispatch-surfaces.md`, and `verifiers/checklist-baseline.json` (`:30-72`, read at `:108-113`). `SEEDED` at `:75-82` only supplies self-test fixtures.
- **Write scope:** Normal `--root` / `--rev` sweep paths only read (`:125-133`); self-test writes fixture files in `TemporaryDirectory` (`:136-153`) and cleans the temp directory on exit. The test command constrained `TMPDIR` to `.tmp-check-correction-sweep` inside the clone; no host access or network call was needed.
- **Owner:** `verifiers/check_gate_registry.py:20-36` defines the allowed row fields and pins owner to `kotoba`.

Documentation comparison / mismatch:

- Snapshot search for `check_correction_sweep` / `Correction sweep` found no target-specific mention in `SKILL.md`, `verifiers/README.md`, or `verifiers/floors-registry.json`. `SKILL.md:533` points to “§ Gate registry,” and `verifiers/README.md:4-5` says the rows live there, but the snapshot has no `## Gate registry` heading/table; the frozen counter also records that absence (`verifiers/check_gate_registry.py:5-9`). This is the missing registry C2 is meant to fill, not a conflicting claim about this script.
- `verifiers/floors-registry.json:2-3` scopes itself to `check_assertion_floors.py` and its 13 instruments (`:4-56`); it is not the gate-row registry and makes no claim about this verifier.

Files changed: this report only; no implementation files changed.
Risks / blockers: none observed; self-test writes are contained within the clone.