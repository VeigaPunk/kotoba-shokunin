Result: DONE — Replaced the stale scratch-dump pointer with its regeneration command and verified hashes; both requested checks were unchanged before and after the patch in the sandbox clone.

- Patch: `.ufo/waves/round-54/build/ExecBaselineNote.patch` changes only `verifiers/baseline.json` → `opencode_round53_note`. It cites `strings -n 4 /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe | sha256sum` and the binary SHA-256; the pin key/value and all other keys are untouched. The clone diff reported one file changed, one insertion and one deletion, on the `opencode_round53_note` line.
- Regeneration evidence (from `/fast/scratch/hyaku/kotoba-r54/ExecBaselineNote`):
  - `sha256sum /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` (exit 0): `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7  /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`
  - `strings -n 4 /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe | sha256sum` (exit 0): `2d72d83f8c90b15c4ba12037c305a838fefe03401e0762c90efdfe04f5a4bd98  -`
  - The regenerated digest matches the previously recorded dump digest; the binary digest matches `opencode_binary_sha256`.
- Before the patch, in the clone:
  - `python3 -B verifiers/check_substrate_pins.py` (exit 0):
    ```
    PASS omp_binary_sha256: 85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4
    PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
    PASS opencode_binary_sha256: 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7
    OK 3/3 pins hold
    ```
  - `python3 -B verifiers/verify_harness_claims.py --self-test` (exit 0): `self-test: 0 failure(s) over 10 assertions`
- After applying the final patch in the clone, the outputs and exit codes were unchanged:
  - `python3 -B verifiers/check_substrate_pins.py` (exit 0):
    ```
    PASS omp_binary_sha256: 85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4
    PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
    PASS opencode_binary_sha256: 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7
    OK 3/3 pins hold
    ```
  - `python3 -B verifiers/verify_harness_claims.py --self-test` (exit 0): `self-test: 0 failure(s) over 10 assertions`
- Patch applicability: `git apply --reverse --check .ufo/waves/round-54/build/ExecBaselineNote.patch` exited 0 against the patched clone; reversing and reapplying the patch succeeded before the final checks. An initial zero-context draft did not apply with default `git apply`; the delivered patch includes context and was applied successfully.
- Risks/blockers: none. No tools were installed or updated.
