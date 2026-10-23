# ExecR4PluginMain — routed defect R4: `check_plugin_manifests.py --self-test` never reaches a successful `main()`

Result: DONE — `verifiers/check_plugin_manifests.py` now has a self-test arm that drives a successful `main()` over a throw-away v2-satisfying git repo (exit 0, exact found line) and a broken-conjunct arm (exit 1, exact one-of-two line), with no rule, constant or non-self-test code touched; patch and sha256s delivered below.

## Deliverable

- Patch: `.ufo/waves/round-58/build/ExecR4PluginMain.patch` (lane root, `git apply -p1`, conventional `a/` `b/` prefixes)
  - sha256 `d453bc12588dfa2adfafb9778184f0df95349536f9d9f9b9153d8233e765e530`
  - `index 0100282..28ccab6 100755`; 86 insertions, 0 deletions, one file.
- Old file sha256 (lane at `3de87aad29e960c95ed35840442f424c48c29729`, and the sandbox checkout before editing):
  `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`
  (`sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_plugin_manifests.py` prints exactly this; `git rev-parse 3de87aa:verifiers/check_plugin_manifests.py` = `010028202f282098cf1e15c5f2b72d02cde41a30`, matching the patch's `0100282`.)
- New file sha256: `7cefb99751b948c2d7f24e68b245f28ecaf5e8a9a116b55a1c5ab191ed47cdd6`
  (`git hash-object` of the patched file = `28ccab679e9b4076aef0f74600f715f6121a31f3`, matching the patch's `28ccab6`.)

No file in the lane was modified by me other than this report and that patch. All execution happened in the sandbox clone
`/fast/scratch/hyaku/kotoba-r58/ExecR4PluginMain` checked out at the freeze commit (HEAD = `3de87aad29e960c95ed35840442f424c48c29729`).

## What the patch adds (all inside `self_test()`)

- `verifiers/check_plugin_manifests.py:1106` — `global BASE, TARGET, NEW_TARGET, lane_dir, fetch`
  (added only so the arm can point the counter at a temp repo and restore afterwards; the
  model is `verifiers/check_command_files.py:1144`).
- `verifiers/check_plugin_manifests.py:1771-1854` — the R4 arm, modelled on the R4 arms in
  `verifiers/check_command_files.py:1805-1863` (search `successful`):
  - Builds a temp git repo whose **base** commit holds only the 11-column `corpus/SOURCES.md`
    header; the **measured** commit adds `SKILL.md` (section `### Plugin manifests by client`,
    frozen header, two rows), `corpus/knowledge/plugin-manifests-round57.md` (header
    `| Client | Manifest | Source | Quote |`, two rows), `corpus/SOURCES.md` (rows `S089`
    Claude Code, `S093` Gemini CLI: `docs`/`A`/`mined`/`2026-10-23`, pinned hosts) and
    `corpus/lessons/round-57.md` (`## Gate` carrying both quotes verbatim).
  - The satisfying world: tokens `.claude-plugin/plugin.json` (Claude Code) and
    `gemini-extension.json` (Gemini CLI) are well-formed v2 E1/E7 tokens, quotes are 7 and 6
    words with a plugin/extension word outside the token span, entry `Manifest` cells equal the
    tokens (E4), the two tokens are not shared (E5), the URLs are docs, not change notes (E3),
    and the base tree holds neither token (G = 2). `fetch` is stubbed to a local page string,
    so the arm is hermetic (no network).
  - Asserts `main(["--rev", measured, "--fetch"])` exits **0** and its stdout contains the exact
    line `plugin manifests found on the live page 2 of 2; new ground 2` with `TARGET,
    NEW_TARGET = 2, 2`.
  - Broken-conjunct arm: rewrites the Gate so the Claude quote is no longer recorded, commits,
    and asserts `main(["--rev", broken, "--fetch"])` exits **1** and prints the exact line
    `plugin manifests found on the live page 1 of 2; new ground 1`.
  - `finally:` restores `BASE, TARGET, NEW_TARGET, lane_dir, fetch`.

The four new assertions are `verifiers/check_plugin_manifests.py:1833,1834,1849,1850`. No rule,
constant, docstring rule text or non-self-test function changed: the diff has **0** deletion
lines (`git diff ... | grep -E '^-[^-]' | wc -l` → `0`), and both hunks land inside
`self_test()` (`@@ -1103,6 +1103,7 @@` and `@@ -1767,6 +1768,91 @@ def self_test() -> int:`).

## Evidence (commands, exit codes, observed output)

1. Before — pristine freeze tree extracted from the sandbox (`before/`):
   `python3 -B before/verifiers/check_plugin_manifests.py --self-test`
   → `counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`
   → `self-test: 0 failure(s) over 235 assertions`, **exit 0**.
2. After — patched sandbox file:
   `python3 -B verifiers/check_plugin_manifests.py --self-test`
   → `counter sha256 7cefb99751b948c2d7f24e68b245f28ecaf5e8a9a116b55a1c5ab191ed47cdd6`
   → `self-test: 0 failure(s) over 239 assertions`, **exit 0** (235 + the 4 new arms).
3. Patch applied to a pristine extraction of `3de87aa` inside the sandbox (`applycheck/`):
   `git apply <patch>` → exit 0; the applied file is `7cefb997...`; its `--self-test` →
   `self-test: 0 failure(s) over 239 assertions`, **exit 0**. So the delivered patch, not just
   my working copy, produces the measured result.
4. Live fetch after the change (sandbox clone, network on):
   `timeout 300 python3 -B verifiers/check_plugin_manifests.py --rev 118d3ac4c6ca9db51d4b05a7dc2ce82d35cc4711 --fetch`
   → `counter sha256 7cefb99751b948c2d7f24e68b245f28ecaf5e8a9a116b55a1c5ab191ed47cdd6`
   → `counter rev 118d3ac4c6ca9db51d4b05a7dc2ce82d35cc4711`
   → `plugin manifests found on the live page 4 of 4; new ground 4`
   → four `BACKED` rows (Claude Code, Codex, Gemini CLI, Cursor), three `reject` rows
   (VS Code, Copilot CLI, opencode), **exit 1**. Unchanged from the pre-patch run of the same
   command (identical line, identical rows, exit 1).
5. The new arms are operative, not vacuous — two mutants in `.probe/` (scratch only, not in the
   patch):
   - `mutant_target.py` (arm target `2` → `3`): `--self-test` → `FAIL R4: the satisfying world
     exits 0: got 1, expected 0`, `self-test: 1 failure(s) over 239 assertions`, exit 1.
   - `mutant_page.py` (drops the Gemini token from the stubbed page): → `FAIL R4: the satisfying
     world exits 0: got 1, expected 0`, `FAIL R4: the exact found line is printed: got False,
     expected True`, `FAIL R4: the broken world prints the one-of-two line: got False, expected
     True`, `self-test: 3 failure(s) over 239 assertions`, exit 1.
6. Global hygiene: two `self_test()` calls in one process both return 0, and after the first run
   the module globals are back to `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`, `5`, `3`,
   `lane_dir`, `fetch` (printed before and after the call).

## Behavior

- `--self-test` now exits 0 only if a full `main()` evaluation reaches `predicate(...) == 0` on a
  v2-satisfying world **and** its summary line is byte-exact, plus a second `main()` where one
  backing conjunct (the Gate recording) is broken exits 1 with its own byte-exact line. Before
  this patch no self-test arm ever entered `main()` past the argument guards, so the whole
  judge/lines/predicate path could regress silently while `--self-test` stayed green.
- The measured live behavior is unchanged: same counter line, same four backed clients, exit 1
  (the C1 counter is frozen; this patch adds observation, not a claim).

## Risks

- The arm adds four git commits across two temp repos per self-test run (~1-2 s on this host);
  the repo already makes commits in `held_world()`, so no new dependency. It inherits
  `held_world()`'s assumption that `git` is runnable and that `git init`/`commit` work under the
  current user (no gpg signing configured; the baseline 235-assertion run passed under the same
  assumption). [INFERENCE] On a host with `commit.gpgsign=true` the arm would surface as a
  self-test error exactly like `held_world` does today — not a new failure mode.
- The dummy SOURCES/entry/lesson fixtures are local strings inside `self_test()`; they do not
  read the lane's round-57 files, so the arm is independent of later C1 edits.
- The printed counter sha256 changes (`bf11a4…` → `7cefb9…`) as expected for any edit; receipts
  that cite the old hash must be re-pointed at integration.

## Blockers

None. No lane writes other than the patch and this report; no tool installs or upgrades were
needed; no paid model calls; no network beyond the counter's own pinned-host `--fetch` run.
