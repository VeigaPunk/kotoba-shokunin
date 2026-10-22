Result: HOLDS — the declared C1 threshold and all three erratum-3 guards hold, and the counter is byte-identical between plan and C1.

# W2RerunC1 — re-run of the C1 counter and the three erratum-3 guards

Seat: KotobaR54.W2RerunC1. Scope: re-run `verifiers/check_description_thresholds.py`
(the frozen C1 counter) at `422ffd10`, `e3371548`, `bf65974c`, `5a097e12`, plus
`--fetch` at `5a097e12`; re-check erratum-3 guards (a) backed-S### absence at plan,
(b) zero-count threshold numbers in plan SKILL.md, (c) live fetch; check the counter
file is byte-identical `e3371548`→`5a097e12`. Everything ran in a sandbox clone at
`58db81c4465b0e9b07ef2485b87d8970683afac6`. No tools installed (python3 + git suffice).
The only lane file written was this authorized report; no source files, lane Git index,
or jj state were changed.

## 1. Frozen-counter byte identity — HOLDS

```
git show <rev>:verifiers/check_description_thresholds.py | sha256sum / wc -c
422ffd10 : absent — "fatal: path 'verifiers/check_description_thresholds.py' exists
           on disk, but not in '422ffd10…'" (counter committed in the plan commit)
e3371548 : sha256 4edad582973786a8b46c7a948edc5ec8f7df7e6911d6ea7e982e7834a8e32aa0, 20712 B
bf65974c : sha256 4edad582…a0, 20712 B
5a097e12 : sha256 4edad582…a0, 20712 B
58db81c4 : sha256 4edad582…a0, 20712 B
git diff e3371548 5a097e12 -- verifiers/check_description_thresholds.py → empty (exit 0)
git diff e3371548 58db81c4 -- verifiers/check_description_thresholds.py → empty (exit 0)
```

The counter file does not exist at base `422ffd10` (it was introduced by the plan
commit itself). The base "before" run therefore uses the frozen copy from the plan
commit (`--rev 422ffd10` makes the counter read repo content at that revision via
`git show`), which is the only way the declared before-value can be produced.

## 2. Counter re-runs — declared statement HOLDS

| Rev | Command (cwd = worktree of that rev) | Last output line | Exit |
|-----|--------------------------------------|------------------|------|
| 422ffd10 | `python3 -B …/.wt-plan/verifiers/check_description_thresholds.py --rev 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4` | `description thresholds backed 0 of 7 clients` | 1 |
| e3371548 | `python3 -B verifiers/check_description_thresholds.py --rev e33715486a45a4a857b64c30e6b695f7995858b8` | `description thresholds backed 0 of 7 clients` | 1 |
| bf65974c | `python3 -B verifiers/check_description_thresholds.py --rev bf65974c7845a06d7ef621ad998c6378ff735cd5` | `description thresholds backed 0 of 7 clients` | 1 |
| 5a097e12 | `python3 -B verifiers/check_description_thresholds.py --rev 5a097e12b9409a1f425fbc76334f36f1402eb4cc` | `description thresholds backed 7 of 7 clients` | 0 |
| 5a097e12 | `python3 -B verifiers/check_description_thresholds.py --rev 5a097e12b9409a1f425fbc76334f36f1402eb4cc --fetch` | `description thresholds backed 7 of 7 clients` / `description thresholds found on the live page 7 of 7` | 0 |

Complete plain-run stdout (all stdout lines, including the counter's per-client rows);
each `exit=` is the shell-observed Python exit status:

```
422ffd10:
Claude Code  no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Codex        no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
VS Code      no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Copilot CLI  no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Gemini CLI   no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Cursor       no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
opencode     no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
description thresholds backed 0 of 7 clients
exit=1

e3371548: [same complete stdout as 422ffd10]
Claude Code  no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Codex        no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
VS Code      no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Copilot CLI  no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Gemini CLI   no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Cursor       no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
opencode     no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
description thresholds backed 0 of 7 clients
exit=1

bf65974c: [same complete stdout as 422ffd10]
Claude Code  no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Codex        no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
VS Code      no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Copilot CLI  no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Gemini CLI   no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Cursor       no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
opencode     no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
description thresholds backed 0 of 7 clients
exit=1

5a097e12:
Claude Code  BACKED
Codex        BACKED
VS Code      BACKED
Copilot CLI  BACKED
Gemini CLI   BACKED
Cursor       BACKED
opencode     BACKED
description thresholds backed 7 of 7 clients
exit=0
```

At `422ffd10`/`e3371548`/`bf65974c` each of the 7 clients reports
`SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)` —
the `### Description thresholds by client` table and the entry
`corpus/knowledge/skill-listing-thresholds-round54.md` do not exist at those revs
(`git cat-file -e` on the entry exits 128 at both `e3371548` and `bf65974c`;
`git show e3371548:SKILL.md | grep -c 'Description thresholds by client'` → 0).
Matches the declared before-values (`backed 0 of 7`, exit 1). The claimed value at
`5a097e12` is 7, well above the declared floor of 4 → statement HOLDS.

Backed mapping at `5a097e12` (`--json`, all `backed: true`, `why: []`):
Claude Code→S053, Codex→S054, VS Code→S055, Copilot CLI→S056, Gemini CLI→S057,
Cursor→S058, opencode→S059.

## 3. Erratum-3 guard (a): each backed S### absent at e3371548 — HOLDS

```
git show e3371548:corpus/SOURCES.md | grep -c -E '^\|[[:space:]]*S05[3-9][[:space:]]*\|' → 0 each
  (S053 0, S054 0, S055 0, S056 0, S057 0, S058 0, S059 0)
git show e3371548:corpus/SOURCES.md | grep -c 'S05[3-9]'  → 0   (no mention at all)
git show bf65974c:corpus/SOURCES.md | grep -c 'S05[3-9]'  → 0
highest row id at e3371548: S052 (rows end S050/S051/S052)
git show 5a097e12:corpus/SOURCES.md | grep -c -E '^\|[[:space:]]*S05[3-9][[:space:]]*\|' → 1 each
```

All seven backing rows were opened this round (S053–S059, lines 66–72 of SOURCES.md
at `5a097e12`), not pre-existing rows re-dated `2026-10-22`.

## 4. Erratum-3 guard (b): ≥2 backed clients carry a number counting 0 in plan SKILL.md — HOLDS

`git show e3371548:SKILL.md | grep -c -F -- '<token>'` over every token the counter
extracted from the new table's threshold cells:

| Client (row) | Tokens in threshold cell | Plan-count per token | Zero-count token? |
|---|---|---|---|
| Claude Code (S053) | `1,536`, `1%`, `0.01` | 0, 0, 0 | yes |
| Codex (S054) | `2%`, `8,000`, `10,000` | 0, 0, 0 | yes |
| VS Code (S055) | `1024`, `64` | 1, 1 | no |
| Copilot CLI (S056) | `1024` | 1 | no |
| Gemini CLI (S057) | `100` | 4 | no |
| Cursor (S058) | `1,024` | 1 | no |
| opencode (S059) | `1`, `1024`, `1`, `2` | 93, 1, 93, 66 | no |

Clients carrying at least one token absent from plan SKILL.md: **2** (Claude Code,
Codex) → the required `≥2` is met exactly. Note the guard's number is literal-substring
`grep -c -F` per the plan: `1024` counts 1 at plan (the portability floor), so VS Code,
Copilot CLI and opencode contribute nothing; `1` and `2` count 93/66. Matches the
plan's own prediction (`1,536`, `2%`, `8,000`, `1%` count 0; `1024`/`1,024` count 1).

## 5. Erratum-3 guard (c): each backed quote found by --fetch — HOLDS

```
$ python3 -B verifiers/check_description_thresholds.py --rev 5a097e12… --fetch
Claude Code  BACKED found=True     Codex  BACKED found=True
VS Code      BACKED found=True     Copilot CLI  BACKED found=True
Gemini CLI   BACKED found=True     Cursor  BACKED found=True
opencode     BACKED found=True
description thresholds backed 7 of 7 clients
description thresholds found on the live page 7 of 7
exit=0
```

URLs fetched (as read from each SOURCES row): code.claude.com/docs/en/skills.md,
learn.chatgpt.com/docs/build-skills, code.visualstudio.com/docs/agent-customization/agent-skills,
docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference,
geminicli.com/docs/cli/skills-best-practices.md, cursor.com/docs/release-notes.md,
opencode.ai/docs/skills.md. All returned pages containing the normalized quote.

## 6. Residual observations (not counter-measured; reported, not counted)

- The re-run verifies the counter's structural source/quote rules, not whether a
  documented number is an authoring cap, listing cut, or render budget; this report
  does not independently adjudicate that semantic reading (counter docstring lines 46–48).
- S054's SOURCES URL (`learn.chatgpt.com/docs/build-skills`) differs by suffix from
  the lesson Gate URL (`build-skills.md`). The counter's `--fetch` uses the SOURCES URL;
  I did not separately fetch the Gate URL.
- `--json` output is followed by the `description thresholds backed …` summary line
  (not one JSON document) — re-observed; already named in erratum 3.
- Counter file absent at `422ffd10` is expected (frozen counters committed in the
  plan commit), not a defect; it means the declared before-value is only runnable
  via the frozen copy, which is what the plan describes.

## 7. Not in this seat's scope / not run here

`--self-test` (assigned to the self-test seats), per-row content/quote/location
review, append-only ordering of SOURCES rows, and the `--root` mode were not in this
seat's scope. No patch was verified; no lane source file was touched.
