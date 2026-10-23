Result: PARTIAL — The harness and self-test now isolate injected faults against control, but the entry correctly remains red on the plan-commit corpus defects.

Files changed:
- `.ufo/waves/round-55/build/ExecFaultInjection.patch` — unified patch for `verifiers/fault_injection_corpus.sh` only.
- `.ufo/waves/round-55/build/ExecFaultInjection.md` — this report.

Behavior in the patch:
- `fault_h_context` compares its quoted-pointer count with the control count plus one, and checks that the other observed findings and checked population remain unchanged. This replaces the stale hardcoded `quoted = 1` expectation (`verifiers/fault_injection_corpus.sh`, patched function around lines 334–354).
- `fault_must_not_fire` compares both instruments with an unmutated control, avoiding a false positive when the corpus is already dirty (`fault_injection_corpus.sh`, patched function around lines 357–379).
- `fault_known_blind_f` now requires a clean control in both no-baseline and baseline modes, and requires baseline-mode exit 1 for the planted case. It no longer treats any nonzero baseline-mode result as evidence that this injected fault was detected (`fault_injection_corpus.sh`, patched function around lines 298–328).
- Self-test T2 compares a no-op world with control; T3 now plants harmless fault-g and verifies no new finding. T1/T4 remain in place (`fault_injection_corpus.sh`, patched `self_test` around lines 399–436).

Retained evidence (sandbox clone at `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`; `TMPDIR=/fast/scratch/hyaku/kotoba-r55/KotobaR55.ExecFaultInjection/tmp`):

Before patch:
- `timeout 900 env TMPDIR=/fast/scratch/hyaku/kotoba-r55/KotobaR55.ExecFaultInjection/tmp bash verifiers/fault_injection_corpus.sh` — exit 1; `fault-0-control ... corpus.index.unindexed,corpus.pointers.commit_unresolvable | FAIL-control-dirty`; `fault-f ... FAIL`; `fault-g ... FALSE-POSITIVE`; `fault-h ... FAIL`; `verdict: FAILURES PRESENT`.
- `timeout 900 env TMPDIR=/fast/scratch/hyaku/kotoba-r55/KotobaR55.ExecFaultInjection/tmp bash verifiers/fault_injection_corpus.sh --self-test` — exit 1; `self-test T2: FAIL (exit=1)`, `self-test T3: FAIL`, `self-test: BROKEN`.

After patch:
- `timeout 900 env TMPDIR=/fast/scratch/hyaku/kotoba-r55/KotobaR55.ExecFaultInjection/tmp bash verifiers/fault_injection_corpus.sh` — exit 1; `fault-0-control | integrity | 1 | corpus.index.unindexed,corpus.pointers.commit_unresolvable | FAIL-control-dirty`; `fault-f | integrity | 1 | corpus.index.unindexed,corpus.pointers.commit_unresolvable | FAIL`; `fault-g | integrity | 1 | corpus.index.unindexed,corpus.pointers.commit_unresolvable | PASS(no new drift vs control)`; `fault-h | integrity | 1 | corpus.index.unindexed,corpus.pointers.commit_unresolvable | PASS(context: quoted=2, control=1, checked=53 unchanged)`; `verdict: FAILURES PRESENT`.
- `timeout 900 env TMPDIR=/fast/scratch/hyaku/kotoba-r55/KotobaR55.ExecFaultInjection/tmp bash verifiers/fault_injection_corpus.sh --self-test` — exit 0; `self-test T2 no-op world preserves control result (exit=1, fired=corpus.index.unindexed,corpus.pointers.commit_unresolvable): PASS`; `self-test T3 must-not-fire assertion preserves control result: PASS`; `self-test: OK`.
- `timeout 900 python3 -B verifiers/verify_corpus_integrity.py --repo . --no-baseline --json` — exit 1; observed `unindexed=1` at `corpus/lessons/round-54-verifier-spotcheck.md` and `commit_unresolvable=1` at that file's line 147 (`451a02ff`).
- `timeout 900 python3 -B verifiers/verify_corpus_integrity.py --repo . --json` — exit 1; observed `tracked_files=82` vs expected 81, `report_total=53` vs 51, `commit_total=33` vs 32, plus the same two zero-mode drifts. The pinned expectations are `verifiers/corpus-baseline.json:13-45`. The exact residual corpus causes are `corpus/lessons/round-54-verifier-spotcheck.md:147` and the unindexed file itself.

Blocker/risk: I did not alter the corpus or the instrument it injects into. The `fault-0-control` finding is genuine on the frozen plan-commit tree; suppressing it would make this gate report green over real corpus defects. `fault-f` also remains unprovable there: its control is already red, so the baseline-mode signal cannot distinguish the planted blind-spot case from the stale counts. It is deliberately left failing until the corpus/index and baseline are repaired. The entry is therefore not green; the self-test is green.

Exact proposed one-cell annotation for `SKILL.md:470` (Pinned values cell; no newline):
`in-file; on the plan-commit tree control reports corpus.index.unindexed=1 and corpus.pointers.commit_unresolvable=1, so entry remains exit 1 pending corpus/index and baseline repair`

No tools were installed or updated. No build, lint, formatter, or unrelated tests were run.