# CtlDoNothing — C1 pre-data control (do-nothing base and header-only scaffold)

Result: DONE — CtlDoNothing: S 0 of 0; F 0 of 0; G 0; exit 1; predicate NOT MET

C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) — NOT MET

Claim C1, frozen counter `verifiers/check_hook_files.py` at freeze revision
`67b68e0f9a0c48e5aa5ced63e6117cfca69da491` (`TARGET = 4` at
`verifiers/check_hook_files.py:253`, `NEW_TARGET = 5` at `:254`, read from that committed file).
Control seat: `KotobaR59.CtlDoNothing`. No lane content written; this file and the sandbox commits
are the only products.

## Sandbox

Clone: `/fast/scratch/hyaku/kotoba-r59/CtlDoNothing` (clone of the lane, checked out at the freeze
revision `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`). Four measured revisions:

| # | revision | world |
|---|---|---|
| A | `67b68e0f9a0c48e5aa5ced63e6117cfca69da491` (lane freeze revision, unmodified) | do-nothing — nothing added |
| B | `a975cbbf00534443c49bf02e29c813a3db0bf0f8` (`BASE`, round-58 tip) | do-nothing — base revision |
| C1 | sandbox `2fc6e37ed71a249b6a9dd35c6203635842d3dc3f` (`/fast/scratch/hyaku/kotoba-r59/CtlDoNothing`) | `SKILL.md` gains the empty `### Hook files by client` heading and its empty table header only, no rows |
| C2 | sandbox `c0735a874bc041202be4f996a48db39f705bc090` (`/fast/scratch/hyaku/kotoba-r59/CtlDoNothing`) | C1 plus `corpus/knowledge/hook-files-round59.md` holding only the frozen entry header row and separator, and `corpus/lessons/round-59.md` holding only `# Round 59 — lessons` and an empty `## Gate`; still no table rows, no new SOURCES rows, no snapshots |

Counter identity, read in the clone at the measured revision:

```
$ sha256sum verifiers/check_hook_files.py
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
```

```
$ git rev-parse HEAD            # before the control commits
67b68e0f9a0c48e5aa5ced63e6117cfca69da491
```

The counter at the measured revisions is byte-identical to the frozen counter: the clone was checked
out at the freeze revision and `verifiers/check_hook_files.py` was never edited (its sha256 above is
printed by every run's second output line as well).

Diff of the control world C2 against the freeze revision (the whole of it; 12 insertions, 0
deletions, no `verifiers/` change):

```
 SKILL.md                               | 5 +++++
 corpus/knowledge/hook-files-round59.md | 4 ++++
 corpus/lessons/round-59.md             | 3 +++
 3 files changed, 12 insertions(+), 0 deletions(-)
```

The added bytes, exactly as `git diff 67b68e0f9a0c48e5aa5ced63e6117cfca69da491..c0735a874bc041202be4f996a48db39f705bc090`
prints them:

```diff
diff --git a/SKILL.md b/SKILL.md
index debcb00..b5f467a 100644
--- a/SKILL.md
+++ b/SKILL.md
@@ -118,6 +118,11 @@ A reusable prompt the user invokes by typing `/name` lives in a command (prompt)
 | Cursor | `.cursor/commands` (scope not printed on the cited pages) | Markdown workflow prompt; these pages document no frontmatter or argument schema (S094 `:54`, `customize-cursor.md:31`) | Audit the body; check Cursor's current docs for any newer schema |
 | opencode | `.opencode/commands/` (project; user `~/.config/opencode/commands/`) | `.md` only; nested path → `/`-separated name; optional YAML frontmatter; trimmed body is the template; `$ARGUMENTS`, `$1`–`$n`; legacy singular `command/` still read (S095 `:21,28,34,37,99,109`) | Keep the body a complete prompt template |
 
+### Hook files by client
+
+| Client | Hook config | Events | Action |
+|---|---|---|---|
+
 ## Router model — which harness, which gate
 
 Two harnesses consume skills here, and neither shares the other's catalogue
diff --git a/corpus/knowledge/hook-files-round59.md b/corpus/knowledge/hook-files-round59.md
new file mode 100644
index 0000000..f5ab2ef
--- /dev/null
+++ b/corpus/knowledge/hook-files-round59.md
@@ -0,0 +1,4 @@
+# Hook files by client — round-59 knowledge entry
+
+| Client | Hook config | Source | Quote |
+|---|---|---|---|
diff --git a/corpus/lessons/round-59.md b/corpus/lessons/round-59.md
new file mode 100644
index 0000000..53ec939
--- /dev/null
+++ b/corpus/lessons/round-59.md
@@ -0,0 +1,3 @@
+# Round 59 — lessons
+
+## Gate
```

## The counter, verified at freeze

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 67b68e0f9a0c48e5aa5ced63e6117cfca69da491:verifiers/check_hook_files.py | sha256sum
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  -
```

## Receipts

All runs: cwd `/fast/scratch/hyaku/kotoba-r59/CtlDoNothing`, shell `unset GIT_DIR GIT_WORK_TREE
GIT_INDEX_FILE`. The runs are bracketed by `date -u` readings in the clone: `Fri 23 Oct 2026 09:20:52 AM
UTC` before the A/B runs and `Fri 23 Oct 2026 09:22:46 AM UTC` after the C1/C2 runs. No page
was fetched: with `backed` empty, `main()` never enters the fetch loop
(`verifiers/check_hook_files.py:2386-2396`), so the 3-fetch cap and the bot-challenge rule were not
exercised.

### A — do-nothing at the freeze revision, `--fetch`

```
$ sha256sum verifiers/check_hook_files.py
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
=== A1 freeze --fetch ===
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1
```

### A — do-nothing at the freeze revision, no `--fetch`

```
=== A2 freeze no-fetch ===
hook files backed on committed snapshots 0 of 0; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1
```

### B — do-nothing at base `a975cbbf`, `--fetch`

```
=== B1 base --fetch ===
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev a975cbbf00534443c49bf02e29c813a3db0bf0f8
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1
```

### B — do-nothing at base `a975cbbf`, no `--fetch`

```
=== B2 base no-fetch ===
hook files backed on committed snapshots 0 of 0; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev a975cbbf00534443c49bf02e29c813a3db0bf0f8
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1
```

### C1 — SKILL.md empty section + table header only, `--fetch`

Command: `timeout 900 python3 -B verifiers/check_hook_files.py --rev 2fc6e37ed71a249b6a9dd35c6203635842d3dc3f --fetch`

```
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 2fc6e37ed71a249b6a9dd35c6203635842d3dc3f
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1
```

### C1 — same world, no `--fetch`

```
hook files backed on committed snapshots 0 of 0; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev 2fc6e37ed71a249b6a9dd35c6203635842d3dc3f
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1
```

### C2 — full header scaffold (SKILL header + entry header + empty Gate), `--fetch`

Command: `timeout 900 python3 -B verifiers/check_hook_files.py --rev c0735a874bc041202be4f996a48db39f705bc090 --fetch`

```
hook files backed on committed snapshots 0 of 0; found on the live page 0 of 0; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev c0735a874bc041202be4f996a48db39f705bc090
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1
```

### C2 — same world, no `--fetch`

```
hook files backed on committed snapshots 0 of 0; live not run; new ground 0
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71; rev c0735a874bc041202be4f996a48db39f705bc090
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit=1
```

Predicate label for every `--fetch` run above:

```
C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) — NOT MET
```

Side observation (same frozen counter, no lane effect): `--rev HEAD` is refused before any reading —
`could-not-evaluate: --rev 'HEAD' is not a full 40-hex commit hash`, exit 2, which is the documented
could-not-evaluate code (`main()` before `verify_rev`), not a scoring run.

## Findings

1. Do-nothing scores zero everywhere. At both the freeze revision and `BASE` the counter prints
   `0 of 0; ... new ground 0` and exit 1, with `K = 0`: the round-58 `### Custom command files by
   client` rows are not counted, because the section heading `### Hook files by client` is absent and
   `skill_rows()` returns `[]` for a missing section. The counter has no path that scores structure
   alone.
2. Commentary/scaffold does not score. World C1 adds the exact heading and the exact header
   `| Client | Hook config | Events | Action |` — the only two structural strings the counter matches
   outside the row cells — and the result is unchanged: `0 of 0`, exit 1, because row count is what
   `K` counts and `skill_rows()` yields no rows under the header.
3. The full scaffold does not score either. World C2 additionally adds the entry table header the
   counter looks for and an empty `## Gate`; `entry_rows()` and `gate_section()` find them, but with no
   entry rows and no SOURCES rows there is nothing to pair, and the summary is still
   `0 of 0; found 0 of 0; new ground 0`, exit 1.
4. `G` without `--fetch` is 0 by construction (the spec sentence and `main()`'s
   `counted = ... if args.fetch else []`), and without `--fetch` the exit is always 1 — both observed
   on every measured revision and consistent with `predicate()` at `verifiers/check_hook_files.py:1245-1251`.
5. The predicate is therefore not met by anything a do-nothing or header-only seat can produce; a
   redesign is not forced by this control, and the C1 targets remain measured against real data.

[INFERENCE] Because `backed` is empty in all six runs, no HTTP request was made; this follows from
the fetch loop iterating `backed` only (`verifiers/check_hook_files.py:2386-2396`) and is consistent
with the absence of any `live fetch failed:` line in the output.

## Limits

- This control exercises structure and the zero-row path only. It says nothing about the row rules
  (token grammar, E5, foreign markers, quote/event/snapshot pins); those are the sibling controls'
  subjects.
- The freeze addendum's Events-conjunct limit is untouched here: no row exists in any of these worlds,
  so no event name is asserted or proven.
- No lane file, no fleet file, no jj state, no Git index was written. Sandbox commits exist only in
  `/fast/scratch/hyaku/kotoba-r59/CtlDoNothing`.

## Bounds

- Report path check (after writing):

```
$ ls -l /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/controls/CtlDoNothing.md
-rw-r--r-- 1 vgpnk vgpnk 14662 Oct 23 06:23 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/controls/CtlDoNothing.md
```
- Tool installs: none.
- Processes: only the six scoring runs, two refused `--rev HEAD` invocations and read-only git, each
  under `timeout 900`; no background jobs, no pattern kills.
