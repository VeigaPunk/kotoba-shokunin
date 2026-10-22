Result: DONE — Added discriminating self-test arms for both routed round-52 surface fixes.

## Changes

- `verifiers/verify_surfaces.py:1314-1327`: added the P4e unresolved-group arm. Its fixture gives `bq` only an unresolved `S$` call for declared `CLAUDE.md`, while separate `Kl` calls register the declared control pairs. The `no_uncovered_class` arm requires exit 1 and the surfaced `omp:<unresolved-var:S$>/CLAUDE.md` diagnosis.
- `verifiers/verify_surfaces.py:1461-1473`: added the empty-baseline fallback arm. It checks the existing clean omp dump against `baseline-empty.json`, requiring `no_uncovered_class` to name both extracted omp classes rather than pass on an empty extraction.
- New fixture: `verifiers/fixtures/surfaces/strings-omp-unresolved-group.txt` (7 lines).
- The exported patch contains only those two implementation paths. No extraction logic, floors, or floor checker changes are in the patch. New assertion total: 133 (from 129).
- Patch: `.ufo/waves/round-53/build/ExecSurfArms.patch`.

## Retained evidence

Commands below ran in `/fast/scratch/hyaku/kotoba-r53/ExecSurfArms`, except where noted. The missing-path `ERROR` diagnostics in self-test output are expected negative fixtures.

1. Sandbox setup: `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r53/ExecSurfArms && git -C /fast/scratch/hyaku/kotoba-r53/ExecSurfArms checkout -q 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` — exit 0, no output.
2. Base self-test: `python3 -B verifiers/verify_surfaces.py --self-test; printf 'exit=%s\n' "$?"` — exit 0; `0 failure(s) over 129 assertions`.
3. With both fixes and new arms: `python3 -B verifiers/verify_surfaces.py --self-test; result=$?; printf 'exit=%s\n' "$result"; exit "$result"` — exit 0; `0 failure(s) over 133 assertions`.
4. Reverted only unresolved-file admission (restored immediately afterward; empty-baseline fix remained): the same self-test command — exit 1; it reported `unresolved-group-admission: exit 1: got 0`, `unresolved-group-admission: names unresolved class` with `PASS surfaces.no_uncovered_class: all 2 extracted loader class(es) declared`, then `2 failure(s) over 133 assertions`.
5. Restored unresolved admission, reverted only the empty-set `bool(declared)` fallback condition (restored immediately afterward): the same self-test command — exit 1; it reported `empty-baseline fallback: exit 1: got 0`, `empty-baseline fallback: names extracted omp classes` with `PASS surfaces.no_uncovered_class: all 0 extracted loader class(es) declared`, then `2 failure(s) over 133 assertions`.
6. After restoring both fixes: `python3 -B verifiers/verify_surfaces.py --self-test; result=$?; printf 'exit=%s\n' "$result"; exit "$result"` — exit 0; `0 failure(s) over 133 assertions`.
7. After removing one extra blank line in the self-test section, the same command — exit 0; `0 failure(s) over 133 assertions`.
8. Patch export (run once before and once after the spacing cleanup; both exit 0): `git -C /fast/scratch/hyaku/kotoba-r53/ExecSurfArms add -A && git -C /fast/scratch/hyaku/kotoba-r53/ExecSurfArms diff --cached --binary 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36 > /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-53/build/ExecSurfArms.patch`.
9. Read-only round-52 inspection commands, all exit 0 and no diff body: `git -C /fast/scratch/hyaku/kotoba-r53/ExecSurfArms log --oneline c2107ecf..c8407a45 -- verifiers/verify_surfaces.py; printf 'exit=%s\n' "$?"`; `git -C /fast/scratch/hyaku/kotoba-r53/ExecSurfArms diff c2107ecf c8407a45 -- verifiers/verify_surfaces.py; result=$?; printf 'exit=%s\n' "$result"; exit "$result"`; and `git -C /fast/scratch/hyaku/kotoba-r53/ExecSurfArms log -p --format='%h %s' c2107ecf..c8407a45 -- verifiers/verify_surfaces.py; result=$?; printf 'exit=%s\n' "$result"; exit "$result"` (the final command was run twice; the first invocation had no explicit status output, so its exit 0 is [INFERENCE] from the successful tool result).

## Risks and blockers

No blocker. The unresolved fixture exercises the CLI diagnostic against the committed 18.12.5 baseline; the empty-baseline arm deliberately uses the existing clean omp fixture. The revert probes show each arm fails independently when only its corresponding fix is removed. Floors were left untouched for L1 integration.