Result: DONE — All requested C1 guard classes were probed with 18 isolated mutants: the frozen self-test killed 8, missed 10, and every mutation was restored byte-for-byte.

# MutC1Counter — frozen C1 self-test coverage

## Scope and detector

- Seat: `KotobaR56.MutC1Counter`; leaf, no dispatches or other agent runtime.
- Axes for this probe: behavioral discrimination, production-call-site coverage, exact isolation/restoration. This is not a C1 claim judgment or a score change.
- Sandbox only: `/fast/scratch/hyaku/kotoba-r56/MutC1Counter`.
- Checked-out revision: `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`.
- Target: `verifiers/check_agent_definitions.py`; all line references below name its pristine bytes at that revision.
- The bytes at this revision include errata 1–3 and run **99 assertions** (see `plans/round-56.md:124-155`), rather than the earlier 90-assertion v1.1 mentioned in the dispatch summary. The pinned revision, not an older version, was tested.
- Original/restored SHA256, abbreviated **H0** below: `2f672bd155a4c125caa7e1758e06137b72ede4caec75d4e67baeee227bbe6c47`.
- Python: `Python 3.14.8`. No tools installed or upgraded.
- No `--fetch` runs, source downloads, live C1 content scoring, C2 work, fixture edits, self-test edits, or counter fixes. No sandbox commits or pushes. The only lane write is this report.

Sandbox creation command, exit 0, no stdout/stderr:

```sh
timeout 20 mkdir -p /fast/scratch/hyaku/kotoba-r56 && timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r56/MutC1Counter && timeout 30 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r56/MutC1Counter checkout -q e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8
```

Metadata command, sandbox cwd, exit 0:

```sh
timeout 10 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git --no-optional-locks rev-parse HEAD && timeout 10 sha256sum verifiers/check_agent_definitions.py && timeout 10 python3 --version && timeout 10 date -u
```

Observed output:

```text
e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8
2f672bd155a4c125caa7e1758e06137b72ede4caec75d4e67baeee227bbe6c47  verifiers/check_agent_definitions.py
Python 3.14.8
Fri 23 Oct 2026 02:47:30 AM UTC
```

The **same detector command** was executed separately on pristine, mutant and restored bytes for each mutant, always from the sandbox cwd with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` removed from the environment:

```sh
timeout -k 2s 30s python3 -B verifiers/check_agent_definitions.py --self-test
```

Each invocation was captured with `subprocess.run(..., capture_output=True, text=True, timeout=35)`. SHA256 was computed immediately before and after each invocation; restored bytes were also compared directly with the original byte sequence. Every process returned synchronously; none timed out. Observed detector durations were 0.047–0.184 seconds. No background jobs or services were started.

**Expected detector for every mutant:** this unchanged command should exit 1 with at least one `FAIL` assertion if the self-test covers the affected behavior. Actual 1 = killed; actual 0 = survived. Any pristine/restored failure or unstable source hash would be inconclusive. No such case occurred.

## Mutants and outcomes

Each mutant below was applied alone and reverted before the next pristine run. Guard deletion means deleting the indicated conditional and its rejection statement, not altering its helper or a self-test expectation.

| ID | Guard / pristine location | Exact mutation | Actual self-test exit / failures | Verdict |
|---|---|---|---|---|
| M01 | Left boundary, `:727` | `if boundary_ok(text, i) and right_ok:` → `if right_ok:` | 1 / 8 | KILLED |
| M02 | Right path-segment boundary, `:727` | `if boundary_ok(text, i) and right_ok:` → `if boundary_ok(text, i):` | 1 / 1 | KILLED |
| M03 | Base-URL exclusion, `:599-600` | Delete `if url_key(url) in base_urls:` and its rejection | 1 / 1 | KILLED |
| M04 | Base-row-id exclusion, `:578-579` | Delete `if sid in at_base:` and its rejection | 1 / 1 | KILLED |
| M05 | Entry host pin, `:601-602` | Delete `if not host_ok(url, HOSTS[client]):` and its rejection | 1 / 1 | KILLED |
| M06 | Agent word outside token, production caller, `:571-572` | Delete `elif not agent_word_outside(q_plain, hit[1], hit[2]):` and its rejection | 0 / 0 | SURVIVED |
| M07 | Agent word outside token, helper, `:507` | `m.end() <= start` → `m.end() <= end`, retaining the rest of the condition | 1 / 1 | KILLED |
| M08 | Quote lower bound, production caller, `:565` | `if not MIN_WORDS <= n <= MAX_WORDS:` → `if not MIN_WORDS - 1 <= n <= MAX_WORDS:` | 0 / 0 | SURVIVED |
| M09 | Quote upper bound, production caller, `:565` | `if not MIN_WORDS <= n <= MAX_WORDS:` → `if not MIN_WORDS <= n <= MAX_WORDS + 1:` | 0 / 0 | SURVIVED |
| M10 | Quote-in-Gate enforcement, `:575-576` | Delete `if not quote_in_gate(quote, gate_raw, gate_plain):` and its rejection | 1 / 1 | KILLED |
| M11 | Distinct-form new ground, `:1136` | `ground = len({n for n, c in counts.items() if c == 0})` → `ground = sum(r["base_count"] == 0 for r in counted)` | 0 / 0 | SURVIVED |
| M12 | Base-count exclusion of `.ufo/`, `:227` | Remove the final `":!.ufo"` argument from the git-grep argument list | 0 / 0 | SURVIVED |
| M13 | F threshold, `:125` | `TARGET = 5` → `TARGET = 4` | 0 / 0 | SURVIVED |
| M14 | G threshold, `:126` | `NEW_TARGET = 2` → `NEW_TARGET = 1` | 0 / 0 | SURVIVED |
| M15 | Host pin after redirect, `:769-770` | Delete `if pins is not None and not host_ok(final, pins):` and its exception | 0 / 0 | SURVIVED |
| M16 | Base-URL exclusion after redirect, `:771-772` | Delete `if base_keys is not None and url_key(final) in base_keys:` and its exception | 0 / 0 | SURVIVED |
| M17 | Form normalization / example-name exclusion, `:476` | Change `break` to `continue` in `normalise()` after the first agent segment | 1 / 4 | KILLED |
| M18 | Gate section scoping, production caller, `:616` | `gate = gate_section(lesson)` → `gate = lesson` | 0 / 0 | SURVIVED |

Aggregate command over the captured mutant records:

```python
mutants = runs[1::3]
print('killed', sum(r['exit']==1 for r in mutants),
      'survived', sum(r['exit']==0 for r in mutants),
      'inconclusive', sum(r['exit'] not in (0,1) for r in mutants))
```

Observed: `killed 8 survived 10 inconclusive 0`.

## Exact observed detector output

All 18 pristine runs and all 18 restored runs exited **0**, with empty stderr and exactly this stdout:

```text
self-test: 0 failure(s) over 99 assertions
```

All surviving mutant runs (**M06, M08, M09, M11, M12, M13, M14, M15, M16, M18**) also exited **0**, with empty stderr and exactly that same stdout. Their individual executions, source hashes, and timestamps are recorded below; none is an unrun or inferred pass.

Killed mutant stdout follows verbatim. Each exited **1** with empty stderr.

### M01 — left boundary

```text
FAIL boundary: .ai/docs/agents inside opencode.ai/docs/agents/ is rejected: got True, expected False
FAIL boundary: after a letter is rejected: got True, expected False
FAIL boundary: after a digit is rejected: got True, expected False
FAIL boundary: after a dot is rejected: got True, expected False
FAIL boundary: after a slash is rejected: got True, expected False
FAIL boundary: after a hyphen is rejected: got True, expected False
FAIL boundary: after a comma is rejected: got True, expected False
FAIL found: token only inside a URL is rejected: got True, expected False
self-test: 8 failure(s) over 99 assertions
```

### M02 — right boundary

```text
FAIL erratum 1: a singular token inside the plural is not found: got True, expected False
self-test: 1 failure(s) over 99 assertions
```

### M03 — base URL

```text
FAIL a base URL is not backed: got ['Claude Code', 'Codex'], expected ['Codex']
self-test: 1 failure(s) over 99 assertions
```

### M04 — base row id

```text
FAIL an S### already at base is not backed: got ['Claude Code', 'Codex'], expected ['Codex']
self-test: 1 failure(s) over 99 assertions
```

### M05 — entry host pin

```text
FAIL an off-host URL is not backed: got ['Claude Code', 'Codex'], expected ['Codex']
self-test: 1 failure(s) over 99 assertions
```

### M07 — agent-word helper span

```text
FAIL no agent word outside the token span: got True, expected False
self-test: 1 failure(s) over 99 assertions
```

### M10 — Gate enforcement

```text
FAIL a quote missing from the Gate is not backed: got ['Claude Code', 'Codex'], expected ['Codex']
self-test: 1 failure(s) over 99 assertions
```

### M17 — normalized form suffix

```text
FAIL normalise ~/.cursor/agents/*.md: got '.cursor/agents/*.md', expected '.cursor/agents'
FAIL normalise .github/agents/*.agent.md: got '.github/agents/*.agent.md', expected '.github/agents'
FAIL normalise ~/.claude/AGENTS/foo: got '.claude/agents/foo', expected '.claude/agents'
FAIL normalise keeps the first agent segment only: got '.config/opencode/agents/other.md', expected '.config/opencode/agents'
self-test: 4 failure(s) over 99 assertions
```

## Coverage findings, not counter repairs

1. **Agent-word helper coverage does not protect the production call.** M07 is killed while M06 survives. The whole-judge negative at `:993-997` changes the entry quote but leaves the lesson quote unchanged; Gate enforcement independently rejects it. [INFERENCE] This masking explains why that fixture cannot expose deletion of the agent-word call. The direct helper checks at `:919-930` remain green under caller deletion.
2. **Quote bounds are tested as repeated arithmetic, not through the production verdict.** The self-test at `:906-914` compares lengths with `MIN_WORDS`/`MAX_WORDS` directly. It does not execute the changed comparison at `:565` with otherwise-valid two-word or 26-word rows and matching Gate quotes. Both production off-by-one mutants survive. No change to the frozen 3–25-word contract is warranted.
3. **New-ground normalization and distinct aggregation are different coverage surfaces.** The helper's suffix truncation is covered (M17 killed), but per-client rather than per-form aggregation survives (M11). [INFERENCE] An otherwise valid VS Code/Copilot CLI pair sharing `.github/agents` is a differentiating input shape; it was not separately scored in this probe.
4. **Base scan scope is not exercised by this self-test.** `:1074-1077` checks only `sum_grep_counts()` on strings. The self-test never calls `git_grep_count()`; removing the `.ufo/` exclusion survives (M12). This is a self-test gap, not evidence that the pristine exclusion is wrong.
5. **The actual F/G exit predicate is outside the self-test path.** `main()` returns from `--self-test` at `:1092-1095`, before counting and the final predicate at `:1157-1158`. Both weakened target constants survive (M13/M14). No end-to-end threshold world was executed here.
6. **Initial source identity is covered; redirected source identity is not.** M03/M05 die on whole-judge negatives, but M15/M16 survive. The self-test does not call `fetch()` (`:750-778`), so its post-redirect host/base-URL checks are unexercised by this detector. No HTTP redirects were fetched during this probe.
7. **Gate presence is covered; Gate-only placement is not.** M10 dies, but replacing section extraction with the whole lesson survives (M18). The existing synthetic lesson at `:948-952` has only a Gate section; it does not distinguish a quote recorded solely in another section.

These are bounded coverage findings for these exact mutants. They do not establish that the pristine counter accepts invalid C1 content, that C1 is met or missed, or that every possible mutation in a killed class is detected. The counter, its rules and its tests remain frozen and unchanged.

## Per-mutant run and hash receipt

P/M/R means pristine, mutant, restored. All timestamps are UTC on 2026-10-23. For **every row**, the complete source-hash sequence is **H0 → listed mutant SHA256 → H0**. Each of those hashes was checked both before and after its detector invocation and was unchanged during the invocation. Every restored byte sequence also equaled the saved original bytes, not merely its hash.

| ID | P UTC | M UTC | R UTC | Exits P/M/R | Mutant SHA256, before = after detector |
|---|---|---|---|---|---|
| M01 | 02:48:05.130537 | 02:48:19.595913 | 02:48:33.911222 | 0/1/0 | `e710d645ff58a0a8f84e7c68897b43deb3d1dd862e1b4cbb3dc53d65ea4b47ea` |
| M02 | 02:48:33.960653 | 02:48:48.730710 | 02:49:04.568298 | 0/1/0 | `38f540e3ae7184893fd3d85cf632c79ce0bd10e0687b0182152aa5bf8705f204` |
| M03 | 02:49:04.628901 | 02:49:18.514844 | 02:49:31.879204 | 0/1/0 | `ff4888f666f5ccc1fd3ac19c6880a368d3902df9791c7ac6d717df56370cb99f` |
| M04 | 02:49:31.941284 | 02:49:44.737428 | 02:50:02.670856 | 0/1/0 | `1d57d9d2712daabf2f7095760901d5995df80f37287f1eb1707e8caa3129f5cc` |
| M05 | 02:50:02.741523 | 02:50:14.193018 | 02:50:26.436060 | 0/1/0 | `840a33bd3cb5af1536cb527a18e37c60aa1884dd1fb8e2ddd09cad355ea8e45d` |
| M06 | 02:50:26.493191 | 02:50:37.989634 | 02:50:49.889689 | 0/0/0 | `6bdb63f7c687c3c867d7a3516110d78285ed79cd7ae5566a0c6ee82170bbc428` |
| M07 | 02:50:50.073940 | 02:50:59.969895 | 02:51:16.779679 | 0/1/0 | `c60a56b89f5ae8d26dfcc9c26116343a2ca54cc6d143c993b4e723cf4dea442a` |
| M08 | 02:51:16.837236 | 02:51:30.958282 | 02:51:46.437821 | 0/0/0 | `8515198e7b733530932be4c2bbe0c4dcd085362cf4fd52b53d8fdcef1587e560` |
| M09 | 02:51:46.485720 | 02:52:03.278991 | 02:52:15.669702 | 0/0/0 | `e9b63479e26b4e57f04ab3a97589b8d5e089ba4f6c01b369f7ad68b5013b1ef4` |
| M10 | 02:52:15.721222 | 02:52:31.444953 | 02:52:44.926572 | 0/1/0 | `fb40ce59db9a73849ddf98a4127a5634604e02fe49dc27de29460be6b8d005e3` |
| M11 | 02:52:44.976773 | 02:52:59.558066 | 02:53:14.074092 | 0/0/0 | `df1413e91ec44a4179f83ffb6cb93c2b6bf37913019008ef7b37afc5c1953fb1` |
| M12 | 02:53:14.133979 | 02:53:28.339429 | 02:53:45.438588 | 0/0/0 | `1b816632cdc0d5ad0818a15e7edbbd98dbe5f726372d2d1d37576428406ffdab` |
| M13 | 02:53:45.493403 | 02:53:57.131240 | 02:54:11.521501 | 0/0/0 | `f491457dd85534f32f7fd17bedf0ce0abdf9acba00a69d2463d45f2e60f96a48` |
| M14 | 02:54:11.571662 | 02:54:26.185358 | 02:54:39.332074 | 0/0/0 | `5d28616df9703fa821dcb5dd361064b5bab6feef4a0464ab55b1ebe121154b37` |
| M15 | 02:54:39.379681 | 02:54:54.121386 | 02:55:07.511795 | 0/0/0 | `3470fc9a5f618a5c8a59a691b35df02d8518085ddc8f3537ba3f5dccdb13207e` |
| M16 | 02:55:07.566728 | 02:55:22.264047 | 02:55:42.501682 | 0/0/0 | `36fd933c4dd5714a5e546966dedd6bbf70bc156d2b668e15ac176cafa505b19f` |
| M17 | 02:55:42.553504 | 02:55:55.784691 | 02:56:09.054383 | 0/1/0 | `5cfa7b4ef1ea901410ad970eb50a7644e709c59cff78e68b09262430f091a217` |
| M18 | 02:56:09.102779 | 02:56:22.667686 | 02:56:36.380585 | 0/0/0 | `dff6b51bed4e5b07f95e1a884ee985d177cee87befe19dc7d872beaf72ac936f` |

Captured-record summary:

```text
triplets 18 runs 54
all unchanged during detector: True
all pristine/restored exact: True
all mutants differ: True
all stderr empty True
```

Final restored run was M18/R at `2026-10-23T02:56:36.380585+00:00`: exit 0, `self-test: 0 failure(s) over 99 assertions`, SHA256 before/after both H0, direct byte comparison with the original `True`. All assigned probes are complete; no counter change is proposed or delivered.
