Result: DONE — OC-4/OC-6 now re-derive on opencode 1.19.4 with call/delivery and registration evidence, while the 1.19.3 dump and committed fixtures remain supported.

## Files changed

- `verifiers/verify_surfaces.py`
- `verifiers/baseline.json`
- `corpus/knowledge/instruction-surface-census-round13.md`
- `verifiers/fixtures/surfaces/strings-opencode-1.19.4-anchors.txt`
- `verifiers/fixtures/surfaces/strings-opencode-1.19.4-decoy-oc4.txt`
- `verifiers/fixtures/surfaces/strings-opencode-1.19.4-decoy-oc6.txt`
- `verifiers/fixtures/surfaces/strings-opencode-clean.txt`
- `verifiers/fixtures/surfaces/strings-opencode-drop-oc1.txt`
- `verifiers/fixtures/surfaces/strings-opencode-drop-oc2.txt`
- `verifiers/fixtures/surfaces/strings-opencode-drop-oc3a.txt`
- `verifiers/fixtures/surfaces/strings-opencode-drop-oc3b.txt`
- `verifiers/fixtures/surfaces/strings-opencode-drop-oc5.txt`
- `verifiers/fixtures/surfaces/strings-opencode-drop-oc6.txt`
- `verifiers/fixtures/surfaces/strings-opencode-extra.txt`
- `verifiers/fixtures/surfaces/strings-opencode-planted-name.txt`

`surfaces-baseline.json`, `floors-registry.json`, and `check_assertion_floors.py` were not changed. No opencode class id, kind, or verdict was retired, re-kinded, or re-verdicted.

## Behavior and evidence

- **OC-4:** `verify_surfaces.py:650-708,805-810` accepts minifier-renamed wrapper callees by their quoted registration labels, then requires the `Instruction.resolve` function to be exported as `resolve`, a `ReadTool.execute` call to `.resolve(messages,path,id)`, and the same result's content inside the `<system-reminder>` tool-result block. The 1.19.4 dump showed `l("Instruction.resolve")` / `resolve:k` at 598311-598312, `l("ReadTool.execute")` at 598484, `r.resolve(F.messages,I,F.messageID)` at 598489, and result delivery at 598496-598499.
- **OC-6:** `verify_surfaces.py:622-648,711-755,821-825` recognizes the aliased `.make("core/instructions")` form, links the key to the `InstructionContext.observe` `targets:["AGENTS.md"]` walk, and requires the `instruction-context` registration to be a dependency of `system-context-builtins`. The 1.19.4 dump showed these at 597823 and 597828. The prior 1.19.3 fixture generation remains supported.
- The 1.19.4 positive fixture has selected anchor excerpts only. Each decoy preserves all seven bare literals (`Instruction.resolve`, `ReadTool.execute`, `<system-reminder>`, `core/instructions`, `targets:["AGENTS.md"]`, `InstructionContext.observe`, and `system-context-builtins`) while breaking one edge. `verify_surfaces.py:1581-1604` asserts literal retention and the isolated OC-4/OC-6 failure.
- The append-only census note is at `corpus/knowledge/instruction-surface-census-round13.md:547-569`; the dated re-pin is at `verifiers/baseline.json:10-11`. Installed binary SHA-256: `538fcb1b6408c8d460882acee19f7ff5b3a3eb3383c0633c4f06170857312a7`. Dump SHA-256: `2d72d83f8c90b15c4ba12037c305a838fefe03401e0762c90efdfe04f5a4bd98`; `strings -n 4` output size: 74,137,746 bytes.
- The verifier's `surfaces.opencode_extract` detail line was: `opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)`.
- Self-test assertions rose from **129 before** to **151 after** (+22); the floor registry was left for L1. The pre-fix predicate mutation produced `4 failure(s) over 151 assertions`; replacing both rules with bare-literal checks produced `6 failure(s) over 151 assertions` because the literal-preserving decoys incorrectly passed. The fixed self-test is green.
- The installed 1.19.3 dump at `/fast/scratch/hyaku/kotoba-r53/RevOcLoader/oc-1.19.3.strings` also passes the final `surfaces` check 7/7. This caught and corrected the historical output accumulator spelling (`R+=` versus 1.19.4's `_+=`).

## Commands and observed results

Shell commands run in the sandbox clone unless a lane path is shown; all listed commands exited with the stated status.

1. `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r53/ExecOcRederive && git -C /fast/scratch/hyaku/kotoba-r53/ExecOcRederive checkout -q 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` — **0**, no output.
2. `sha256sum /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe && strings -n 4 /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe > /fast/scratch/hyaku/kotoba-r53/ExecOcRederive/oc-1.19.4.strings && wc -c /fast/scratch/hyaku/kotoba-r53/ExecOcRederive/oc-1.19.4.strings` — **0**; printed binary SHA-256 `538fcb1b6408c8d460882acee19f7ff5b3a3eb3383c0633c4f06170857312a7` and `74137746` bytes.
3. `python3 -B verifiers/verify_surfaces.py --self-test` (base) — **0**; `0 failure(s) over 129 assertions`.
4. `python3 -B verifiers/verify_surfaces.py --opencode-strings /fast/scratch/hyaku/kotoba-r53/ExecOcRederive/oc-1.19.4.strings --json` (base rules) — **1**; `surfaces pass 6 of 7`, with OC-4 missing its `fn(...)` strings and OC-6 missing `Key.make("core/instructions")`.
5. `sha256sum /fast/scratch/hyaku/kotoba-r53/ExecOcRederive/oc-1.19.4.strings` — **0**; `2d72d83f8c90b15c4ba12037c305a838fefe03401e0762c90efdfe04f5a4bd98`.
6. First structural implementation: the same direct 1.19.4 `verify_surfaces.py --json` command — **1**, OC-4 unmatched because the initial call shape did not accept the `F.messageID` property argument. The accompanying `python3 -B verifiers/verify_surfaces.py --self-test` — **1**, `3 failure(s) over 151 assertions`; the positive 1.19.4 fixture and OC-6 decoy exposed it.
7. After widening that argument shape, the direct 1.19.4 `verify_surfaces.py --json` command — **0**, `pass: 7`, `fail: 0`, `opencode extraction 9/9 declared class(es) from 7/7 rules`. `python3 -B verifiers/verify_surfaces.py --self-test` — **0**, `0 failure(s) over 151 assertions`.
8. Temporarily restored the pre-fix OC-4/OC-6 predicates and ran `python3 -B verifiers/verify_surfaces.py --self-test` — **1**, `4 failure(s) over 151 assertions`; the 1.19.4 positive arm no longer passed.
9. Temporarily changed both predicates to bare-literal checks and ran the same self-test — **1**, `6 failure(s) over 151 assertions`; both decoy fixtures incorrectly returned opencode extraction 9/9, so their expected OC-specific failures failed.
10. `python3 -B verifiers/verify_surfaces.py --opencode-strings /fast/scratch/hyaku/kotoba-r53/RevOcLoader/oc-1.19.3.strings --json` (before generalizing the output accumulator) — **1**, OC-4 unmatched. The observed 1.19.3 shape uses `d.length>0)R+=`.
11. After the alias-agnostic registration and accumulator-pattern refinements, the same 1.19.3 command — **0**, `opencode extraction 9/9 declared class(es) from 7/7 rules`.
12. `python3 -B verifiers/verify_surfaces.py --self-test` (final tree) — **0**, `0 failure(s) over 151 assertions`.
13. `rm -- oc-1.19.4.strings && printf 'removed generated oc-1.19.4.strings\n'` — **0**; removed the scratch dump before staging.
14. `git add -A && git commit -m "Re-derive opencode 1.19.4 instruction surfaces"` — **0**, interim commit `7760b96`. `git rev-parse HEAD` — **0**, `7760b96c8a584d9612faf7b65144d97f43487e2c`.
15. `python3 -B verifiers/check_opencode_repin.py --rev 7760b96c8a584d9612faf7b65144d97f43487e2c` — **0**; initial acceptance output passed 7/7 surfaces, 3/3 pins, 9/9 classes, and 151 self-test assertions.
16. `git -C /fast/scratch/hyaku/kotoba-r53/ExecOcRederive add -A && git -C /fast/scratch/hyaku/kotoba-r53/ExecOcRederive diff --cached --binary 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36 > /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-53/build/ExecOcRederive.patch` — **0** after the interim commit; final patch was regenerated after the final commit below.
17. `git add -A && git commit -m "Keep opencode 1.19.3 surface matching"` — **0**, final commit `9ed5b93`. `git rev-parse HEAD` — **0**, `9ed5b938dcb89e397f47f0a1e7c2075136ef9936`.
18. `python3 -B verifiers/check_opencode_repin.py --rev 9ed5b938dcb89e397f47f0a1e7c2075136ef9936` — **0**, exact final output:

   ```text
   opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 151 assertions
   substrate opencode: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe sha256 538fcb1b6408c8d460882acee19f7ff5b3a3eb3383c0633c4f06170857312a7 bytes 214522032
   ```

19. Re-ran the exact patch-generation command in item 16 after the final commit — **0**; final artifact is `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-53/build/ExecOcRederive.patch` (15 files).

## Risks and blockers

- No outstanding implementation blocker. The census remains a strings-dump shape check, not proof of runtime prompt delivery.
- LSP was unavailable in this seat (no LSP tool exposed); this is recorded rather than interpreted as symbol absence.
- No tool was installed or updated. No files outside this C1 patch and the exclusive report were changed.