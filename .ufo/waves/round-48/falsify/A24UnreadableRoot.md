DEFECT (low severity; verifier availability regression)

C2 causes a new nonzero exit for an unreadable configured `skills/` root. This is a caught substrate error, not an uncaught crash: the verifier emits no traceback. The other three malformed-root cases are clean on both revisions.

Evidence

- Ran only in private clone `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A24UnreadableRoot`, checked out at C2 `d1ae45830235c38320b31032b57a8323cbf90b17` and baseline `75f671b109d8eddd0d64c1429bd6379fe577175a`; clone HEAD was confirmed at each checkout.
- Verifier: `verifiers/verify_harness_independent.py`. C2 Git blob `134f756eb482cae2467218357349f9c1ba256cd6`, SHA-256 `d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937`. Baseline Git blob `06322fc5b0231d9bdc6cb4128c336cc5f1d53597`, SHA-256 `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1`.
- Each invocation was `python3 verifiers/verify_harness_independent.py --json --oc-config <case-path>`. Fixture root: `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A24UnreadableRoot-cases/`. The unreadable `skills/` was mode `000` (`d---------`); the symlink-loop case used `skill/loop -> loop`; the file case used a regular file at `skills`; the broken-child case used `skills/broken` -> missing target.

| Case | C2 exit / stderr | Baseline exit / stderr |
|---|---|---|
| `unreadable` | 2; no traceback. Stdout: `SUBSTRATE [Errno 13] Permission denied: '/fast/scratch/hyaku/kotoba-r48-a2/seats2/A24UnreadableRoot-cases/unreadable/skills'` | 0; no traceback |
| `loop` | 0; no traceback | 0; no traceback |
| `file` | 0; no traceback | 0; no traceback |
| `broken` | 0; no traceback | 0; no traceback |

C2's `derive()` enumerates configured roots at `verifiers/verify_harness_independent.py:599-615`; `path.iterdir()` is unguarded. The surrounding `main()` catches `OSError` and returns 2 (`:1493-1497`), explaining the controlled failure rather than a Python traceback. Baseline enumerates only log-named roots (`verifiers/verify_harness_independent.py:604-610`), so this configured-only unreadable path is not traversed.

Impact and smallest remediation

An unreadable optional configured root prevents `--json` from producing any verifier table, even though the baseline completes. Guard configured-root enumeration against `OSError` and skip an unreadable root (or represent it as unavailable) so this local filesystem condition does not abort unrelated measurements.