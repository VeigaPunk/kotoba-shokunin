Result: HOLDS — all five targeted v2 mutants were killed by --self-test; only accepting a trailing-slash folder turned the measured miss into a pass.

# C1 v2 targeted guard mutation extension

## Scope and detector

- Axes: depth (which exact guard changes the measured result), detector discrimination, and exact-byte isolation/restoration.
- Read `.ufo/waves/round-57/controls/MutC1Counter.md` first. Its earlier v1 mutation table is not repeated or treated as v2 evidence. This report extends only the assigned guards; it is not an exhaustive v2 audit.
- The two named well-formedness cases have separate smallest-clause mutants, hence five mutants: bare filename, trailing-slash folder, shared-token disqualification, held-ground case handling, and change-note URL rejection. No combined mutant was run.
- Checkout: sandbox `07c33d73ddce769d9cea2846a6313164401b5478` (`/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards`). No sandbox commits were made.
- Subject: `verifiers/check_plugin_manifests.py`, 91,273 pristine bytes, SHA-256 `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` (the declared frozen v2 hash). Only this file in the owned clone was mutated; revision content, fixtures and expected assertions were untouched.
- Clone/checkout command, exit 0, no output:

```sh
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards && timeout 30 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards checkout -q 07c33d73ddce769d9cea2846a6313164401b5478
```

Every detector used the clone as cwd, with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` unset and `TMPDIR=/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/tmp`. Commands were sequential, each bounded to 600 seconds:

```sh
timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
```

Expected pristine/restored behavior: self-test exits 0 with `self-test: 0 failure(s) over 235 assertions`; live measurement prints `plugin manifests found on the live page 4 of 4; new ground 4` and exits 1. That live exit 1 is the declared MISS, not a failed baseline self-test or a killed mutant. A self-test kill requires pristine/restored exit 0 and discriminating mutant assertion failures. Every case met those conditions.

There were 22 detector invocations: initial pristine pair, then mutated/restored pairs for each of five mutants. Each restored pair also supplies the immediately preceding pristine baseline for the next mutant. All 11 live invocations completed; no timeout or detector exception occurred.

## Targeted results

Source lines below refer to the pristine v2 file, not shifted mutant lines.

| Mutant | Counter line(s) | Self-test verdict | Actual live measurement | Turns MISS into PASS? |
|---|---:|---|---|---|
| G1-bare-segment | `558` | killed; exit 1, 4/235 failures | F=4, K=6, G=4; exit 1 | no |
| G2-trailing-folder | `556` | killed; exit 1, 1/235 failures | F=5, K=5, G=5; exit 0 | yes |
| G3-shared-threshold | `747` | killed; exit 1, 4/235 failures | F=4, K=4, G=4; exit 1 | no |
| G4-held-case-sensitive | `967-968` | killed; exit 1, 5/235 failures | F=4, K=4, G=4; exit 1 | no |
| G5-change-note | `510` | killed; exit 1, 4/235 failures | F=4, K=4, G=4; exit 1 | no |

**The only observed pass was G2:** allowing an empty final path segment admitted opencode’s `.opencode/plugins/`; the actual output was `opencode     BACKED token=.opencode/plugins/ norm=.opencode/plugins found=yes held-at-base=no`, raising F and G from 4 to 5. Its self-test failed specifically with `FAIL v2: .opencode/plugins/ is not (a directory, not a manifest): got True, expected False`. Restoration returned the score to 4/4/G4 and the self-test to zero failures.

G1 admitted the two bare `plugin.json` tokens into denominator K (4 → 6), but both rows still failed the independent sharing guard. Conversely, G3 removed their two-client-sharing rejection but both remained not well-formed. Neither one-at-a-time mutation raised F. This is observed rejection redundancy, not evidence that either guard is unnecessary.

G4 left this revision at F=4/G=4; every counted pristine token was already reported `held-at-base=no`. Its five failed assertions, including mixed-case text, mixed-case token and a temporary base-tree scan, killed the regression. G5 also left this revision at F=4/G=4 but failed four change-note assertions. An unchanged live score is not a surviving mutant when the bounded self-test rejects it.

No mutant survived and none was inconclusive. These findings do not establish that every other v2 guard has an adequate test, and do not revise the frozen contract or judge round admission.

## Exact old → new mutant text

These are intentionally defective scratch edits, not proposed lane corrections. Each was restored before the next edit.

### G1-bare-segment — `verifiers/check_plugin_manifests.py:558`

Old:
```python
return len(parts) >= 2 or MARKERS[client] in token.lower()
```
New:
```python
return len(parts) >= 1 or MARKERS[client] in token.lower()
```

### G2-trailing-folder — `verifiers/check_plugin_manifests.py:556`

Old:
```python
if not last.endswith(".json") or not any(w in PLUGIN_WORDS for w in seg_words(last)):
```
New:
```python
if last and (not last.endswith(".json") or not any(w in PLUGIN_WORDS for w in seg_words(last))):
```

### G3-shared-threshold — `verifiers/check_plugin_manifests.py:747`

Old:
```python
if len(sharers) >= 2:
```
New:
```python
if len(sharers) >= 3:
```

### G4-held-case-sensitive — `verifiers/check_plugin_manifests.py:967-968`

Old:
```python
token = token.casefold()
    for line in text.casefold().splitlines():
```
New:
```python
for line in text.splitlines():
```

### G5-change-note — `verifiers/check_plugin_manifests.py:510`

Old:
```python
return any(w in path for w in CHANGE_NOTE_WORDS)
```
New:
```python
return False
```

## Hashes and restoration

Common before and restored hash B: `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e`.

| Mutant | Before | Mutant SHA-256 | After restoration | Exact bytes equal original? |
|---|---|---|---|---|
| G1-bare-segment | B | `f7840f610b3bd3ce648d8ad0a203dae631d1c7f1d9180e8f13436b0fbba68b6e` | B | true |
| G2-trailing-folder | B | `8e4427bf529fec054341f75f5daaaf83393d9788c30e9c1d10367ba14e4cec8e` | B | true |
| G3-shared-threshold | B | `1d90d1945640433ca71af8cc64268f68996fe2ce0a62af7da73f6c8b9f7461ba` | B | true |
| G4-held-case-sensitive | B | `a2f433f23cc155f3656c5be0386c2670e8ba7534e67f30a267d2ff6856af595e` | B | true |
| G5-change-note | B | `5a03e885801906953bae738bf7701d0a8ed0e408a01194de0947d757f4e86f59` | B | true |

The saved pristine text was written back in a `finally` block after every mutated pair; each restoration was compared byte-for-byte with the saved original and then exercised with the same two commands. All five restored self-tests exited 0; all five restored live runs printed 4 of 4, new ground 4, exit 1.

Final independent hash command, exit 0:

```text
timeout 5 sha256sum verifiers/check_plugin_manifests.py
bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e  verifiers/check_plugin_manifests.py
```

## Actual detector receipts

Machine-readable receipts remain under the owned clone: `guard-probe/runs.json` (all 22 invocations) and `guard-probe/mutants.json` (exact changes, before/mutant/restored hashes and per-mutant outputs). Full outputs are also embedded below so this report is not dependent on scratch durability. Empty stderr is explicitly recorded. Each date line was produced by `timeout 5 date -u`, exit 0.

### pristine/self-test

```text
Fri Oct 23 06:47:23 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 0; elapsed 0.069 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
self-test: 0 failure(s) over 235 assertions
stderr: (empty)
```

### pristine/fetch

```text
Fri Oct 23 06:47:23 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 1; elapsed 0.742 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
stderr: (empty)
```

### G1-bare-segment/mutated/self-test

```text
Fri Oct 23 06:48:03 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 1; elapsed 0.082 s
counter sha256 f7840f610b3bd3ce648d8ad0a203dae631d1c7f1d9180e8f13436b0fbba68b6e
FAIL v2: bare plugin.json is not (one segment, no own marker): got True, expected False
FAIL v2: gemini-extension.json is not well-formed for Cursor (no own marker): got True, expected False
FAIL v2: a leading ~/ is not a path segment: got True, expected False
FAIL v2: a leading ./ is not a path segment: got True, expected False
self-test: 4 failure(s) over 235 assertions
stderr: (empty)
```

### G1-bare-segment/mutated/fetch

```text
Fri Oct 23 06:48:03 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 1; elapsed 0.757 s
counter sha256 f7840f610b3bd3ce648d8ad0a203dae631d1c7f1d9180e8f13436b0fbba68b6e
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 4 of 6; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
stderr: (empty)
```

### G1-bare-segment/restored/self-test

```text
Fri Oct 23 06:48:04 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 0; elapsed 0.075 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
self-test: 0 failure(s) over 235 assertions
stderr: (empty)
```

### G1-bare-segment/restored/fetch

```text
Fri Oct 23 06:48:04 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 1; elapsed 0.931 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
stderr: (empty)
```

### G2-trailing-folder/mutated/self-test

```text
Fri Oct 23 06:48:12 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 1; elapsed 0.076 s
counter sha256 8e4427bf529fec054341f75f5daaaf83393d9788c30e9c1d10367ba14e4cec8e
FAIL v2: .opencode/plugins/ is not (a directory, not a manifest): got True, expected False
self-test: 1 failure(s) over 235 assertions
stderr: (empty)
```

### G2-trailing-folder/mutated/fetch

```text
Fri Oct 23 06:48:12 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 0; elapsed 0.766 s
counter sha256 8e4427bf529fec054341f75f5daaaf83393d9788c30e9c1d10367ba14e4cec8e
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 5 of 5; new ground 5
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
opencode     BACKED token=.opencode/plugins/ norm=.opencode/plugins found=yes held-at-base=no
stderr: (empty)
```

### G2-trailing-folder/restored/self-test

```text
Fri Oct 23 06:48:13 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 0; elapsed 0.081 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
self-test: 0 failure(s) over 235 assertions
stderr: (empty)
```

### G2-trailing-folder/restored/fetch

```text
Fri Oct 23 06:48:13 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 1; elapsed 0.704 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
stderr: (empty)
```

### G3-shared-threshold/mutated/self-test

```text
Fri Oct 23 06:48:24 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 1; elapsed 0.085 s
counter sha256 1d90d1945640433ca71af8cc64268f68996fe2ce0a62af7da73f6c8b9f7461ba
FAIL v2 E5: a token shared with another client disqualifies both rows: got [], expected ['Gemini CLI', 'Cursor']
FAIL v2 E5: the sharing disqualifies the otherwise-backed row: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code']
FAIL v2 E5: sharing is judged on casefold(normalise()): got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
FAIL v2 E5: a row of an unlisted client name also counts as a user: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code']
self-test: 4 failure(s) over 235 assertions
stderr: (empty)
```

### G3-shared-threshold/mutated/fetch

```text
Fri Oct 23 06:48:24 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 1; elapsed 0.714 s
counter sha256 1d90d1945640433ca71af8cc64268f68996fe2ce0a62af7da73f6c8b9f7461ba
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
stderr: (empty)
```

### G3-shared-threshold/restored/self-test

```text
Fri Oct 23 06:48:25 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 0; elapsed 0.076 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
self-test: 0 failure(s) over 235 assertions
stderr: (empty)
```

### G3-shared-threshold/restored/fetch

```text
Fri Oct 23 06:48:25 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 1; elapsed 0.709 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
stderr: (empty)
```

### G4-held-case-sensitive/mutated/self-test

```text
Fri Oct 23 06:48:33 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 1; elapsed 0.181 s
counter sha256 a2f433f23cc155f3656c5be0386c2670e8ba7534e67f30a267d2ff6856af595e
FAIL v2: a CASE difference holds it (.Claude-Plugin vs held lowercase): got False, expected True
FAIL v2: an upper-case token is held by lowercase base text: got False, expected True
FAIL v2: Extensions is held by base text extensions: got False, expected True
FAIL held occurrences over a temp base tree: got {'.claude-plugin/plugin.json': False, '.cursor/plugins': False, '.opencode/plugins': False, 'gemini-extension.json': True, '.copilot-plugin/plugin.json': False}, expected {'.claude-plugin/plugin.json': False, 'gemini-extension.json': True, '.cursor/plugins': True, '.copilot-plugin/plugin.json': False, '.opencode/plugins': False}
FAIL v2: the control's ground world (Extensions held as extensions) is 3, not 4: got 4, expected 3
self-test: 5 failure(s) over 235 assertions
stderr: (empty)
```

### G4-held-case-sensitive/mutated/fetch

```text
Fri Oct 23 06:48:33 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 1; elapsed 0.916 s
counter sha256 a2f433f23cc155f3656c5be0386c2670e8ba7534e67f30a267d2ff6856af595e
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
stderr: (empty)
```

### G4-held-case-sensitive/restored/self-test

```text
Fri Oct 23 06:48:34 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 0; elapsed 0.177 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
self-test: 0 failure(s) over 235 assertions
stderr: (empty)
```

### G4-held-case-sensitive/restored/fetch

```text
Fri Oct 23 06:48:34 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 1; elapsed 0.829 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
stderr: (empty)
```

### G5-change-note/mutated/self-test

```text
Fri Oct 23 06:48:44 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 1; elapsed 0.092 s
counter sha256 5a03e885801906953bae738bf7701d0a8ed0e408a01194de0947d757f4e86f59
FAIL v2: a changelog URL is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
FAIL v2: a change-note URL is reported as such: got False, expected True
FAIL v2: url_is_change_note on each word: got [False, False, False, False, False], expected [True, True, True, True, True]
FAIL v2: url_is_change_note is case-insensitive and percent-decoded: got (False, False), expected (True, True)
self-test: 4 failure(s) over 235 assertions
stderr: (empty)
```

### G5-change-note/mutated/fetch

```text
Fri Oct 23 06:48:44 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 1; elapsed 0.888 s
counter sha256 5a03e885801906953bae738bf7701d0a8ed0e408a01194de0947d757f4e86f59
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
stderr: (empty)
```

### G5-change-note/restored/self-test

```text
Fri Oct 23 06:48:45 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
exit 0; elapsed 0.086 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
self-test: 0 failure(s) over 235 assertions
stderr: (empty)
```

### G5-change-note/restored/fetch

```text
Fri Oct 23 06:48:45 AM UTC 2026
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 07c33d73ddce769d9cea2846a6313164401b5478 --fetch
exit 1; elapsed 0.902 s
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev 07c33d73ddce769d9cea2846a6313164401b5478
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
stderr: (empty)
```

## Supplemental ordinary-fetch provenance

The counter CLI does not expose HTTP status, raw body length or raw body hash. The following separate, bounded curl requests record those fields for the five URLs that the tested counter fetched (four pristine rows plus opencode under G2); they are not represented as the exact response bytes of each earlier counter invocation. Each curl exited 0, returned HTTP 200, and reported the requested URL as its final URL. No challenge, browser, access-control workaround or alternate runtime was used.

Bodies, response headers and `guard-probe/source-fetches.json` are inside the owned clone. Exact commands and observed metadata:

### S079

[https://code.claude.com/docs/en/plugins-reference.md](https://code.claude.com/docs/en/plugins-reference.md)

```text
Fri Oct 23 06:49:34 AM UTC 2026
$ timeout 60 curl --max-time 45 --location --silent --show-error --fail-with-body --user-agent kotoba-shokunin-counter/57 --dump-header /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/S079-headers.txt --output /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/plugins-reference.md --write-out '%{http_code}	%{size_download}	%{url_effective}
' https://code.claude.com/docs/en/plugins-reference.md
exit 0
200	42124	https://code.claude.com/docs/en/plugins-reference.md
body bytes 42124
sha256 f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e
stderr: (empty)
```

Fetched body: `/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/plugins-reference.md`; headers: `/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/S079-headers.txt`.

### S080

[https://developers.openai.com/plugins/build/plugins.md](https://developers.openai.com/plugins/build/plugins.md)

```text
Fri Oct 23 06:49:34 AM UTC 2026
$ timeout 60 curl --max-time 45 --location --silent --show-error --fail-with-body --user-agent kotoba-shokunin-counter/57 --dump-header /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/S080-headers.txt --output /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/build-plugins.md --write-out '%{http_code}	%{size_download}	%{url_effective}
' https://developers.openai.com/plugins/build/plugins.md
exit 0
200	38036	https://developers.openai.com/plugins/build/plugins.md
body bytes 38036
sha256 c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1
stderr: (empty)
```

Fetched body: `/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/build-plugins.md`; headers: `/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/S080-headers.txt`.

### S083

[https://geminicli.com/docs/extensions/reference.md](https://geminicli.com/docs/extensions/reference.md)

```text
Fri Oct 23 06:49:34 AM UTC 2026
$ timeout 60 curl --max-time 45 --location --silent --show-error --fail-with-body --user-agent kotoba-shokunin-counter/57 --dump-header /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/S083-headers.txt --output /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/extensions-reference.md --write-out '%{http_code}	%{size_download}	%{url_effective}
' https://geminicli.com/docs/extensions/reference.md
exit 0
200	12022	https://geminicli.com/docs/extensions/reference.md
body bytes 12022
sha256 8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72
stderr: (empty)
```

Fetched body: `/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/extensions-reference.md`; headers: `/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/S083-headers.txt`.

### S084

[https://cursor.com/docs/plugins.md](https://cursor.com/docs/plugins.md)

```text
Fri Oct 23 06:49:34 AM UTC 2026
$ timeout 60 curl --max-time 45 --location --silent --show-error --fail-with-body --user-agent kotoba-shokunin-counter/57 --dump-header /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/S084-headers.txt --output /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/cursor-plugins.md --write-out '%{http_code}	%{size_download}	%{url_effective}
' https://cursor.com/docs/plugins.md
exit 0
200	20323	https://cursor.com/docs/plugins.md
body bytes 20323
sha256 74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62
stderr: (empty)
```

Fetched body: `/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/cursor-plugins.md`; headers: `/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/S084-headers.txt`.

### S085

[https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx](https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx)

```text
Fri Oct 23 06:49:34 AM UTC 2026
$ timeout 60 curl --max-time 45 --location --silent --show-error --fail-with-body --user-agent kotoba-shokunin-counter/57 --dump-header /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/S085-headers.txt --output /fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/opencode-plugins.mdx --write-out '%{http_code}	%{size_download}	%{url_effective}
' https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx
exit 0
200	60780	https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx
body bytes 60780
sha256 e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5
stderr: (empty)
```

Fetched body: `/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/opencode-plugins.mdx`; headers: `/fast/scratch/hyaku/kotoba-r57a3/A3MutC1Guards/guard-probe/sources/S085-headers.txt`.

S085 corroborating quote, fetched body `guard-probe/sources/opencode-plugins.mdx:21`, byte-exact contiguous substring, no Markdown stripped (11 words):

> Plugins under `.opencode/plugins/` are loaded automatically, like the local example above.

The rest of line 21 continues after the quoted sentence; no line folding or reshaping was used.

## Bounds

- Lane write: this scoped report only. No lane counter, content, Git index, jj state, sibling checkout, fleet file or untrusted earlier-attempt artifact was written or used as evidence.
- Clone writes: owned scratch counter mutations, exact restorations, bounded temporary self-test repositories and the named receipts/source snapshots only. No push, integration or contract change.
- No subagents, paid model calls, other runtime, package install/update, service change or contention test. Tool installs/updates: none.
- Final result is the assigned guard probe only: five killed mutants, one observed miss-to-pass regression, exact restoration evidenced above.
