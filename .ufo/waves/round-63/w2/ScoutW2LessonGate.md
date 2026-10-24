# ScoutW2LessonGate

role: UFO-FSD scout (freshness)
item: Audit `corpus/lessons/round-63.md` at `cbbee56e9a3589b0b46736ad36f1b77701def80e` against `/home/vgpnk/Projects/shokunin/CORPUS.md` contract v1 and `plans/round-63.md` § Sources. No production file was edited. No tool was installed.

## Verdict

| Check | Committed bytes | Result |
|---|---|---|
| S119 Gate: URL + access date + ≤25-word located quote | URL and `2026-10-23T23:04Z` are present; both spans are literal substrings and are 16 and 7 words | **holds**, with one false command on the 16-word count |
| Status-change log old → new | S119 `new row → mined`; S049 cells byte-identical base → tip | **holds** |
| M94 class / evidence / captured-by / fix, fix shown able to fail | four fields present; the “able to fail” sentence cites `10 assertions` | **gap** — instrument prints `15`; E1 red-before transcript is not cited |
| Round-end census honestly pending | “see the report's Sources & frontier section” plus a fix claim | **gap** — report and `census-after.txt` do not exist |
| Lane-authored name | `corpus/lessons/round-63.md`, not `round-<N>-aggregator-*` | **holds** |

Do not rewrite the Gate or M94 in place. Append the three blocks under `## Falsify corrections` (the round's own correction practice, S119).

## Attack

Pinned tip: `git rev-parse HEAD` → `cbbee56e9a3589b0b46736ad36f1b77701def80e`. Lesson blob: `git ls-tree HEAD -- corpus/lessons/round-63.md` → `100644 blob dcf8ecc64d79fca4e04d2e6b31a5a8d7fcbf9041`.

### 1. S119 quote (contract v1 rule 1; plan lines 124–127)

`corpus/lessons/round-63.md:21-23` records

- URL `https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html`
- accessed `2026-10-23T23:04Z`
- `:170` span “publish a correction notice  as soon as possible detailing changes from and citing the original publication” — claimed 16 words, “`wc -w` on the extracted line prints 16”
- `:172` span “archive all prior versions of the article” — claimed 7 words, no `wc -w`

Commands and output:

```text
$ sed -n '170p' .ufo/waves/round-63/snapshots/S119.page | wc -w
49
$ sed -n '172p' .ufo/waves/round-63/snapshots/S119.page | wc -w
31
$ printf '%s' 'publish a correction notice  as soon as possible detailing changes from and citing the original publication' | wc -w
16
$ printf '%s' 'archive all prior versions of the article' | wc -w
7
```

Python membership against the same snapshot: `LINE170_HAS_Q1 True`, `LINE172_HAS_Q2 True`. Snapshot sha256 `d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2` (matches the lesson and `corpus/SOURCES.md` S119). The double space in “notice  as” is in both the lesson and line 170.

The ≤25-word records are the spans, not the HTML lines. The parenthetical on `:170` is false: `wc -w` of the extracted line prints 49, not 16. The 7-word line states a count and does not carry `wc -w` (QUALITY.md Q54; the count itself is true of the span). `teaches` on the S119 row quotes the same two spans, so the location still grounds the teach.

### 2. Status log (contract v1 rule 2)

`corpus/lessons/round-63.md:47-50`:

- S119 — new row → `mined`; `used-by` names the entry and this lesson.
- S049 — `mined` unchanged; `recheck` `90d`; no field rewritten.

Cell diff, base `35d44b4b4dcdda234b5dbff7af37e432fec55f05` → `HEAD` (columns status / opened / recheck / used-by, plus kind):

```text
base_rows 116  head_rows 117
added ['S119']
removed []
S049 identical True
S119 status mined  recheck 365d
S119 used-by corpus/knowledge/compound-clause-citation-round63.md, corpus/lessons/round-63.md
```

S049 at both revs: `kind docs`, `status mined`, `recheck 90d`, `used-by corpus/knowledge/alwayson-rule-files-round53.md`. No other row's status, recheck, used-by, or kind changed. S119 is a new row, so `new row → mined` is the old→new log; its `used-by` is the initial cell, not an in-place edit. The search-log S049 errata is an append (`corpus/SOURCES.md:221-235`), not a protected-cell rewrite.

### 3. M94 and the E1 red-before (CORPUS.md “a fix is shown able to fail”, lines 179–184)

`corpus/lessons/round-63.md:45` has all four fields:

- class: the frozen plan's expected headline contradicted the check it described
- evidence: `plans/round-63.md` § C2, `1 of 5` vs declared `0 of 5`, seats `ExecCalibBefore.md` and `ScribeReportSkeleton.md`
- captured-by: none (Q48 named as nearest, not a hit)
- fix: erratum E1, prefix and growth

The able-to-fail clause cites the self-test summary `0 failure(s) over 10 assertions`. It does not name `.ufo/waves/round-63/controls/C2-before-r62tip.txt`.

Re-run at the lane root:

```text
$ python3 -B verifiers/check_r63_routed_repairs.py --self-test
self-test: 0 failure(s) over 15 assertions
SELF_EXIT=0

$ python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5
BEFORE_EXIT=1
```

Stdout lines 1–6 match `controls/C2-before-r62tip.txt:1-6`; that file's line 7 is `EXIT=1`. Check 4 fails because growth is zero while the prefix holds. That is the E1 red-before. The green self-test line is not it, and `10` is not the printed assertion count (`verifiers/check_r63_routed_repairs.py:246-338` is 15 `check()` calls).

The prose class is not a `mistakes.md` §5 token. Same shape as M93 in `corpus/lessons/round-62.md:25`. Not a gap: Q58 already cites this sentence. Do not relabel.

### 4. Round-end census

`corpus/lessons/round-63.md:24` says the round-end census is in “the report's Sources & frontier section”, and that interim `E05` was fixed immediately and the two `E11`s by this commit.

```text
census-after.txt exists: False
/home/vgpnk/Projects/shokunin/.ufo/reports/round-63/kotoba.md exists: False
census-before.txt line count: 18
```

`census-before.txt` is 16 `W04` (lines 1–16), `ok` on line 17, `exit=0` on line 18. The lesson's locator `:2-20` is not that file. The count 16 is right; the range is not.

Live re-run (not a round-end receipt; do not paste it into the lesson as one):

```text
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
CENSUS_EXIT=0
```

No `E05`, no `E11`, no S119 `W04`. S119's URL is new, so the warning count stays 16. The plan's “After: expected exit 0, 17 W04” (`plans/round-63.md:137-138`) does not follow from a new URL. The interim file `.ufo/waves/round-63/census-interim.txt` still shows `E05` kind `guidance`, two `E11`, `exit=1`. The lesson's “fixed” clause has no after-sweep in the lesson (CORPUS.md: a negative claim carries its sweep). The slot is not the word pending.

### 5. Lane-authored name (CORPUS.md lines 53–60)

```text
$ git log -1 --format='commit=%H%nauthor=%an <%ae>%nsubject=%s' -- corpus/lessons/round-63.md
commit=cbbee56e9a3589b0b46736ad36f1b77701def80e
author=kotoba-shokunin <kotoba@shokunin.local>
subject=round-63: wave-1 build — …
$ git diff --name-status 35d44b4b4dcdda234b5dbff7af37e432fec55f05 HEAD -- corpus/lessons/round-63.md
A	corpus/lessons/round-63.md
```

Frontmatter: `author: kotoba L1 round 63`, `lane: kotoba`. Path is `corpus/lessons/round-63.md`. No `corpus/lessons/round-63-aggregator-*`. The only `round-63*` lesson is this file. Aggregator-owned names are `lessons/round-<N>-aggregator-*.md`. This one is the lane's.

Spot-check result (CORPUS.md lines 19–20; LEARNING.md): the Gate does not say pending. The non-author result cannot exist yet. Same append block as the census.

## Smallest safe correction

Append under `## Falsify corrections`, after the existing “Filled after wave 2” line. Do not edit line 24 or line 45 in place.

```markdown
- **F-gate-wc (ScoutW2LessonGate):** the `:170` parenthetical “`wc -w` on the extracted line prints 16” is false. `sed -n '170p' .ufo/waves/round-63/snapshots/S119.page | wc -w` prints `49`; `sed -n '172p' .ufo/waves/round-63/snapshots/S119.page | wc -w` prints `31`. The ≤25-word records are the quoted spans, both literal substrings: `printf '%s' 'publish a correction notice  as soon as possible detailing changes from and citing the original publication' | wc -w` prints `16`, and `printf '%s' 'archive all prior versions of the article' | wc -w` prints `7`.
- **F-census (ScoutW2LessonGate):** round-end census is **pending**. No `.ufo/waves/round-63/census-after.txt` is committed, and `/home/vgpnk/Projects/shokunin/.ufo/reports/round-63/kotoba.md` does not exist, so “see the report's Sources & frontier section” names an unwritten slot. The only after-row receipt on disk is the interim file `.ufo/waves/round-63/census-interim.txt` (`E05` kind `guidance`, two `E11`, `exit=1`). The before locator `.ufo/waves/round-63/census-before.txt:2-20` overshoots a file of 18 lines; the 16 `W04` are lines 1–16 and `exit=0` is line 18. The report pastes the after command when the round ends. Do not record `17 W04`: a new URL adds no duplicate-URL warning. Spot-check result is **pending** (non-author, after the round).
- **F-M94 (ScoutW2LessonGate):** `0 failure(s) over 10 assertions` is not the committed instrument. `python3 -B verifiers/check_r63_routed_repairs.py --self-test` prints `self-test: 0 failure(s) over 15 assertions` and exits 0. The E1 red-before is the r62 tip under the landed check, committed at `.ufo/waves/round-63/controls/C2-before-r62tip.txt` and re-run as `python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05`, which prints `FAIL append-only          prefix=True grew_by=0 line(s)` and `r62 routed defects closed 0 of 5` and exits 1. That failure text, not the green self-test summary, is what shows the fix able to fail.
```

## Bounds

- Status log and lane filename: no correction.
- M94's prose class: leave it; it is the string Q58 cites. Do not relabel.
- This seat's live census (exit 0, 16 `W04`, no `E05`/`E11`) is a wave-2 probe, not the round-end receipt. The lesson stays pending until the report pastes the command.
