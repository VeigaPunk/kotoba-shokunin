Result: DONE — the declared C1 miss reproduces exactly under the frozen counter in a clean sandbox clone at all three revisions; the only deviation from the assignment's premise is that `verifiers/check_plugin_manifests.py` does not exist in the base tree `47c05558` (it was committed later at `ee50d8fa`/`01312a77`), which is consistent with the freeze history and changes nothing.

Seat: KotobaR57A3.A3RerunC1Counter (leaf). Sandbox: `/fast/scratch/hyaku/kotoba-r57a3/A3RerunC1Counter`, cloned 2026-10-23T06:47:15Z from the lane, `rev-parse HEAD` = `07c33d73ddce769d9cea2846a6313164401b5478`. Nothing written in the lane except this report.

## 1. Counter identity (`git show <rev>:verifiers/check_plugin_manifests.py | sha256sum`)

Command run in the sandbox clone, 2026-10-23T06:48:02Z:

- `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a` (base): **file not in tree** — `fatal: path 'verifiers/check_plugin_manifests.py' exists on disk, but not in '47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a'`. The pipe therefore does NOT print `bf11a4ef…` at base.
- `ac22ca8791980314a37eb1daa69b846f80a1b9e2` (C1 content): `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` ✓
- `07c33d73ddce769d9cea2846a6313164401b5478` (lane tip): `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` ✓

Cross-checks (same command family, 06:48:27Z):
- Freeze commit `01312a77e36317feb6e961aba77841ddab1225ca` (v2, erratum 1): `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` ✓
- v1 at plan commit `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`: `2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b` — matches the plan's recorded v1 prefix `2ac51d2a2f50d855…` (`plans/round-57.md:93`).
- `git log 01312a77..07c33d73 -- verifiers/check_plugin_manifests.py` → empty: **zero commits touched the counter between freeze and lane tip**. The counter is byte-frozen where it matters.

F1 (wording, not a defect): the assignment asks to confirm `bf11a4ef…` *at* the base revision; the counter cannot hash to anything at base because it did not exist in that tree. The declared result's own wording is the correct one — "Counter v2 sha256 `bf11a4ef…`, frozen at `01312a77` before any content" — and that claim verifies. The `counter sha256` line in receipts is `self_sha()` of the executed file's own bytes (`verifiers/check_plugin_manifests.py:305-308`), not of the measured tree, so no contradiction.

## 2. Counter runs (sandbox, working tree at tip; the score depends only on `--rev` — `git_show(lane, args.rev, …)` at `verifiers/check_plugin_manifests.py:331-338,1807-1811`)

Base, `--fetch` (06:48:27Z):

```
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a --fetch
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a
plugin manifests found on the live page 0 of 0; new ground 0
reject Claude Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Codex: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject VS Code: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Copilot CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Gemini CLI: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject Cursor: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
reject opencode: SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
exit 1
```

C1 content rev, `--fetch` (06:48:36Z):

```
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --rev ac22ca8791980314a37eb1daa69b846f80a1b9e2 --fetch
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
counter rev ac22ca8791980314a37eb1daa69b846f80a1b9e2
plugin manifests found on the live page 4 of 4; new ground 4
Claude Code  BACKED token=.claude-plugin/plugin.json norm=.claude-plugin/plugin.json found=yes held-at-base=no
Codex        BACKED token=.codex-plugin/plugin.json norm=.codex-plugin/plugin.json found=yes held-at-base=no
reject VS Code: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
reject Copilot CLI: SKILL.md manifest token 'plugin.json' is not well-formed; SKILL.md manifest token 'plugin.json' is shared by rows Copilot CLI, VS Code
Gemini CLI   BACKED token=gemini-extension.json norm=gemini-extension.json found=yes held-at-base=no
Cursor       BACKED token=.cursor-plugin/plugin.json norm=.cursor-plugin/plugin.json found=yes held-at-base=no
reject opencode: SKILL.md manifest token '.opencode/plugins/' is not well-formed
exit 1
```

Lane tip, `--fetch` (06:48:36Z): output **byte-identical** to the `ac22ca87` run above except the `counter rev` line reads `07c33d73ddce769d9cea2846a6313164401b5478`; `4 of 4; new ground 4`, exit 1. Consistent with `git diff --stat ac22ca87..07c33d73 -- SKILL.md corpus/SOURCES.md corpus/knowledge/plugin-manifests-round57.md corpus/lessons/round-57.md`: only `corpus/lessons/round-57.md` changed (+50 lines, the Mistakes/Q45 tail sections — the `## Gate` section the counter reads is unchanged, hence identical scoring).

Self-test, once (06:48:36Z):

```
$ timeout 600 python3 -B verifiers/check_plugin_manifests.py --self-test
counter sha256 bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e
self-test: 0 failure(s) over 235 assertions
exit 0
```

Bonus no-`--fetch` run at `ac22ca87` (06:49:12Z), for the receipt's second block: `plugin manifests backed 4 of 4; new ground not computed (needs --fetch)`, same four BACKED lines and three reject lines as above minus the fetch fields, exit 1.

## 3. Line-by-line comparison with `.ufo/waves/round-57/C1-measure.txt`

- Receipt block 1 (`--fetch` at `ac22ca87`, lines 3–13 of the file): **identical line for line** to my run — same `counter sha256`, `counter rev`, summary `plugin manifests found on the live page 4 of 4; new ground 4`, all four BACKED lines, all three reject lines, `exit 1`. Zero differences.
- Receipt block 2 (no `--fetch` at `ac22ca87`): **identical line for line** to my bonus run — `plugin manifests backed 4 of 4; new ground not computed (needs --fetch)`, exit 1. Zero differences.
- The declared base result (`0 of 0; new ground 0`, exit 1) is not itself printed in `C1-measure.txt`; it matches verbatim the committed base control `.ufo/waves/round-57/controls/C1-base-v2.txt:14-25` (`--fetch` block) — my base run reproduces both. Zero differences.
- `--self-test` line matches `controls/C1-base-v2.txt:27-28` (`0 failure(s) over 235 assertions`, exit 0) and the plan's recorded `bf11a4ef…` / 235-assertion figures (`plans/round-57.md:113`).

## 4. Findings

- **Declared result HOLDS.** The frozen predicate (`--fetch` exit 0 iff `F ≥ 5` and `G ≥ 3`) scores `ac22ca87` and `07c33d73` at F=4, G=4 → exit 1: a MISS as declared. The miss is driven solely by F; new-ground G=4 exceeds its target.
- **Counter integrity verified:** v2 bytes `bf11a4ef…` at `01312a77` (freeze), `ac22ca87`, `07c33d73`; untouched between freeze and tip; self-test green (235 assertions).
- **F1 (cosmetic, assignment wording):** `verifiers/check_plugin_manifests.py` is absent from the base tree `47c05558` — `git show` fails there. The correct, verified statement is "v2 `bf11a4ef…` frozen at `01312a77` before any content"; the receipt's `counter sha256` line is `self_sha()` of the executed file. No defect in the declared result; noted so the round record does not overclaim a base-tree hash.
- **No counter artifact found in the miss:** the three rejects are the frozen v2 grammar applied as specified (`token_well_formed`, `verifiers/check_plugin_manifests.py:535-558`): VS Code/Copilot CLI rows carry bare `plugin.json` (not well-formed, and shared → both disqualified) and opencode carries the directory `.opencode/plugins/` (no `.json` file segment). That is precisely the `target-above-reachable-population` outcome recorded as M62 in `corpus/lessons/round-57.md`; the counter behaved per its frozen rule, not per a bug.

## 5. Hygiene / tooling

No installs needed (system `git`, `python3` sufficed). Every run capped with `timeout` ≤ 600 s; four live-page fetches were performed by the counter itself (the four BACKED rows report `found=yes` — S079/S080/S083/S084 URLs per `corpus/lessons/round-57.md` Gate table); observed via output, none errored. No git writes in the lane; all git objects read inside the sandbox clone with `GIT_DIR`/`GIT_WORK_TREE`/`GIT_INDEX_FILE` unset.
