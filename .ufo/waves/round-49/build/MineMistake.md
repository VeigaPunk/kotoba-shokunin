# MineMistake — frontier step: mine one mistake (M29) from routed defect R2

Seat: `KotobaR49.MineMistake` (build wave, leaf — no subagents dispatched).
Scope: draft (a) the M29 row for `corpus/lessons/round-49.md` § Mistakes, (b) the Q25 row for
`corpus/QUALITY.md`, (c) the demonstration that shows each of round 49's two counters able to fail,
(d) a sweep of earlier rounds for a second instance of the class.
Read-only on the lane; the only file written in the lane is this report. Private clone used for all
mutants: `/fast/scratch/hyaku/kotoba-r49/seats/MineMistake/clone` (`git clone -q` of the lane).
Tools installed or updated: none (no pacman, no uv, no npm).

## Findings

1. **R2 reproduces exactly as routed, and the class is sharper than "the counter is blind".**
   The round-48 C1 counter `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'`
   counts file *names*. In the private clone: base `75f671b` → **34**; committing an **empty**
   `corpus/knowledge/zz-empty.md` (0 B, no `source:`, no citation) → **35**, the declared after-value;
   at `887b6af` renaming the entry's extension to `.markdown` with no knowledge change → **34**.
   So the counter cannot distinguish an empty, uncited file from the real entry, and a rename moves
   it without any knowledge change.

2. **Both of round 49's counters are name-blind in the same way — the plan's "content guard" is the
   only thing that can fail.** Measured in the clone:
   - C1: `PROVINCE.md` § Adjacent rewritten to 20 bare lane names with every classification, pinned
     commit, quote and sweep deleted → the plan's counter still prints **20** (exit 0); the section
     emptied → **0**.
   - C2: `verifiers/checklist-baseline.json` with `dispatch.04`/`dispatch.08` set to
     `delegated:verifiers/verify_dispatch_prompts.py` while that file is absent → the counter prints
     **2** (exit 0) while `verify_skill_checklist.py --json` exits **1** with
     `checklist.box_map_complete` FAIL "delegates to a target that does not exist".
   Consequence for the draft: the before→after *number* stays the census observable, and the
   claim's evidence must be the content guard's exit code (C1: the entry's `recheck:` script on a
   mutated quote; C2: the new instrument's `--self-test` must-fail arms). A stub instrument that
   exists and does nothing still passes `checklist.box_map_complete` (measured PASS), so for C2 the
   decisive mutant lives in the new instrument's own self-test, not in the map.

3. **Second instance of the class, in earlier rounds: the seat denominator counted committed file
   names.** `SCORECARD.md:80` (round-41 calibration annotation) and `LOG.md:1409` (seat N06): the
   round-40 "41/41 seats" is a count of committed scout *fragments* — `git ls-tree -r --name-only
   <rev> -- .ufo/round-40/scouts/ | wc -l` → **41** while the frozen `claims.json` declares
   **40**; the same shape at round 37 (26 files vs 24 declared seats, verified). An empty fragment
   counts the same as a finished one. The lane annotated this rather than leaving it silent, so it is
   a recorded instance of the class, not a live defect.

4. **A third, sharper instance of the same class survives in the round-10/11 record:** a counting
   regex that cannot match the class it names prints **0 with the defect present**
   (`LOG.md:261`, `SCORECARD.md:143`). Verified at the round-10 landing `abef8aa`:
   `git show abef8aa:corpus/README.md | grep -cE "commit \`round-[0-9]\`"` → **0** (exit 1) while the
   same file contains `commit \`round-10\`` and the `+` variant prints **1**. The round-10 move-log
   row (`SCORECARD.md:142`) also carries a name-only count with no command that the round-12
   reconstruction could not reproduce: "**4** unindexed files" vs a reconstruction yielding 7 (my
   naive basename `comm` at `e997d45` yields 7 entries, of which 6 exclude the index `README.md`).

5. Nothing in `corpus/QUALITY.md` Q01–Q24 required a counter to be *able* to fail. Q13 requires the
   count to carry its command and date — the round-48 counter did, and it was still unfalsifiable.
   Hence `none → Q25`.

## Drafted rows (verbatim, for the L1 to land)

### (a) `corpus/lessons/round-49.md` § Mistakes — M29

```markdown
| M29 A claim's counter counted file names, so it could not fail on an empty or uncited file | `git ls-tree -r --name-only 75f671b corpus/knowledge \| grep -c '\.md$'` → 34, and the same command over the round-48 tree → 35, but committing an empty `corpus/knowledge/zz-empty.md` (0 B, no `source:`, no citation) at `75f671b` also prints **35** — the declared after-value — while renaming `frontmatter-rule-authorities-round48.md` to `.markdown` at `887b6af` prints **34** with no knowledge change (`.ufo/waves/round-48/falsify/A09ClaimSizingC1.md` § Counterexample 1; reproduced in the private clone at `/fast/scratch/hyaku/kotoba-r49/seats/MineMistake/clone`, 2026-10-22) | none → Q25 (Q13 was satisfied in form — the count carried its command and date — but no criterion required the counter to be able to fail; the same class is visible at `SCORECARD.md:80` / `LOG.md:1409`, where a seat denominator is a count of committed file names) | Both of this round's counters keep the name-only count as the census observable only, and each claim's evidence is the content guard's exit code. C1: the entry's committed `recheck:` script re-reads every census quote at its pinned commit and exits non-zero when a quote is missing or altered; the plan's lane-name count is reported as the census observable, not as the freshness evidence. C2: `verifiers/verify_dispatch_prompts.py` ships `--self-test` must-fail arms for `dispatch.04` and `dispatch.08`, and the two boxes move to `delegated:verifiers/verify_dispatch_prompts.py` in `verifiers/checklist-baseline.json`. Q25 states the rule: a claim's counter is shown able to fail — it is run on a mutant with the claimed content removed or falsified and the changed output recorded. Shown able to fail: C1's guard exits non-zero naming the altered quote (unmutated census: exit 0); C2's self-test exits non-zero on a mutated dispatch prompt (unmutated prompts: exit 0) — and the two name-only counters are shown *not* to be the evidence: C1's counter prints 20 on 20 bare lane names with every classification, quote and sweep deleted, and C2's counter prints 2 while the delegated instrument is absent. |
```

### (b) `corpus/QUALITY.md` — Q25

```markdown
| Q25 | A claim's counter is shown able to fail: it is run on a mutant with the claimed content removed or falsified and the changed output recorded; a counter that counts names, extensions or empty files and reads no content of the claimed thing is a census observable, never the evidence of a claim, and the claim's evidence is the content guard's exit code. | claim counters and before/after numbers (plans, SCORECARD, LOG, lessons, knowledge entries) | M29 A claim's counter counted file names, so it could not fail on an empty or uncited file (`corpus/lessons/round-49.md` § Mistakes) | — |
```

### (c) Demonstration that the fix can fail — round 49's two counters

**C1 — adjacency, sibling-overlap census.**
Counter (plan): `awk '/^## Adjacent/,0' PROVINCE.md | grep -oE '\b(audio|chousa|game-dev-2d|game-dev-3d|kagi|kaidoku|kake|kama|kasegi|kengaku|kotodama|kumitate|lore|mado|mori|revenger|souji|tabi|tameshi|tsukuroi)\b' | sort -u | wc -l` — before **10** at `a5adc146` (measured), after declared **20**.

| mutant | expected changed output |
|---|---|
| `PROVINCE.md` § Adjacent with the new sibling lines deleted | counter → **10** (the before-value); the section emptied → **0** (measured) |
| `PROVINCE.md` § Adjacent listing the same 20 lane names with every classification, pinned commit, located quote and sweep deleted | counter → **20** (unchanged, measured) — the count is name-only and must not be cited as the evidence |
| the census table in `corpus/knowledge/sibling-overlap-census-round49.md` with one located quote altered (one character changed) fed to the entry's committed `recheck:` script | script exits **non-zero**, naming the sibling and the mismatching quote; unmutated census → exit 0 |
| the census table with one sibling's row deleted | script exits **non-zero**, naming the missing sibling and its pinned commit |

**C2 — operability, dispatch-prompt checklist boxes.**
Counter (plan): `jq '[.boxes[]|select((.box_id|startswith("dispatch.")) and (.disposition|test("^(executed|delegated):")))]|length' verifiers/checklist-baseline.json` — before **0** of **9** at `a5adc146` (measured), after declared **2**.

| mutant | expected changed output |
|---|---|
| `dispatch.04`/`dispatch.08` dispositions reverted to `unexecuted:` | counter → **0** (measured) |
| dispositions set to `delegated:verifiers/verify_dispatch_prompts.py` with the instrument file absent | counter → **2** (unchanged, measured) while `python3 -B verifiers/verify_skill_checklist.py --json` exits **1**, `checklist.box_map_complete` FAIL "delegates to a target that does not exist" (measured) |
| disposition pointed at an existing non-instrument (`delegated:SKILL.md`) | counter → **1** (measured) and the same check FAILs "is not an instrument" (measured) |
| the delegated target replaced by a stub script that exists, is executable and does nothing | `checklist.box_map_complete` still **PASS** ("41 boxes mapped (8 executed, 1 delegated, 32 unexecuted)", measured) — so the decisive arm is the new instrument's own `--self-test`: a `dispatch.04` prompt whose report path is not literal or whose file name is not the lane id, and a `dispatch.08` prompt whose round token differs across file name, role line and report path, must each make `--self-test` exit **non-zero** naming the box |

### (d) Earlier-round sweep — claims counted by `ls`/`grep -c` over file names only

| site | line | the count | status |
|---|---|---|---|
| SCORECARD.md | 80 | `git ls-tree -r --name-only <rev> -- .ufo/round-40/scouts/ \| wc -l` → 41 files vs `claims.json` `seats: 40` | annotated by the round-41 closure; instance of the class |
| LOG.md | 1409 | round-37: 26 committed scout files vs 24 declared seats; round-40: 41 files vs 40 declared | recorded; instance of the class |
| SCORECARD.md | 142 | round-10: "8 dead commit pointers" (`git grep -h -o -E "commit \`round-[0-9]+\`" e997d45 -- 'corpus/*.md' \| wc -l` → 8) and "**4** unindexed files" with no recorded command (round-12 reconstruction yields 7) | recorded; the pointer count is shape-blind, the unindexed count is unreproducible |
| SCORECARD.md | 32, 203 / LOG.md | 2360 | round-48's own C1 count, restated in the axes row and the move log (the R2 origin) | open until Q25 |
| LOG.md | 261 / SCORECARD.md | 143 | round-10/11: `grep -cE "commit \`round-[0-9]\`"` → 0 with the defect present; the regex cannot match `round-10` | recorded as the round-11 class; the sharpest "counter that cannot fail" instance |

## Evidence (commands, exit codes, paths)

Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, HEAD `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`,
read-only. Private clone `/fast/scratch/hyaku/kotoba-r49/seats/MineMistake/clone`.

| command | output | exit |
|---|---|---|
| `git ls-tree -r --name-only HEAD corpus/knowledge \| grep -c '\.md$'` | 35 | 0 |
| `git ls-tree -r --name-only 75f671b corpus/knowledge \| grep -c '\.md$'` (clone) | 34 | 0 |
| clone: commit empty `corpus/knowledge/zz-empty.md` at `75f671b`, same counter | 35 (0-byte file, `wc -c` → 0) | 0 |
| clone: rename `frontmatter-rule-authorities-round48.md` → `.markdown` at `887b6af`, same counter | 34 | 0 |
| clone: `awk '/^## Adjacent/,0' PROVINCE.md \| grep -oE '<20 lane names>' \| sort -u \| wc -l` — base | 10 | 0 |
| clone: same counter, § Adjacent = 20 bare names, no classification/quote/sweep | 20 | 0 |
| clone: same counter, § Adjacent emptied | 0 | 0 |
| `jq '[.boxes[]\|select((.box_id\|startswith("dispatch.")) and (.disposition\|test("^(executed\|delegated):")))]\|length' verifiers/checklist-baseline.json` | 0 (of 9 dispatch boxes) | 0 |
| clone: same jq after setting `dispatch.04`/`dispatch.08` to `delegated:verifiers/verify_dispatch_prompts.py`, instrument absent | 2 | 0 |
| clone: `python3 -B verifiers/verify_skill_checklist.py --json` with that map | `checklist.box_map_complete` FAIL "delegates to a target that does not exist" (dispatch.04, dispatch.08); `exit_code` 1 | 0 (script) |
| clone: disposition `delegated:SKILL.md` | jq → 1; `box_map_complete` FAIL "is not an instrument" | 0 |
| clone: stub `verifiers/verify_dispatch_prompts.py` (executable, does nothing) | `box_map_complete` PASS "41 boxes mapped (8 executed, 1 delegated, 32 unexecuted)" | 0 |
| `git show abef8aa:corpus/README.md \| grep -cE "commit \`round-[0-9]\`"` | 0 (file contains `commit \`round-10\``) | 1 |
| `git show abef8aa:corpus/README.md \| grep -cE "commit \`round-[0-9]+\`"` | 1 | 0 |
| `git grep -h -o -E "commit \`round-[0-9]+\`" e997d45 -- 'corpus/*.md' \| wc -l` | 8 (tokens: round-1, round-4, round-5 ×2, round-6 ×2, round-7 ×2) | 0 |
| `git ls-tree -r --name-only b1be35f9522f21c0c5b39879358a011806ab9200 -- .ufo/round-40/scouts/ \| wc -l` | 41 | 0 |
| `git show b1be35f…:.ufo/round-40/claims.json \| jq '.seats'` | 40 | 0 |
| `git ls-tree -r --name-only b1be35f… -- .ufo/round-37/scouts/ \| wc -l` / `claims.json .seats` | 26 / 24 | 0 |
| clone: naive basename `comm` of corpus `.md` names vs README tokens at `e997d45` | 7 entries (README.md, round-1-aggregator-audit.md, round-1.md, round-3.md, round-4-aggregator-audit.md, round-4.md, round-5-aggregator-audit.md) — 6 excluding the index | 0 (comm warns "not in sorted order" without `LC_ALL=C`) |
| `ls -d /home/vgpnk/Projects/shokunin/*-shokunin \| wc -l` | 21 (20 siblings + kotoba itself) | 0 |

Sources read for the drafts: `corpus/lessons/round-48.md` § Mistakes (row shape M24–M28),
`corpus/QUALITY.md` (table shape, five columns, `grounded in` + `supersedes`),
`corpus/lessons/round-48-verifier-spotcheck.md` (routed defect R2),
`.ufo/waves/round-48/falsify/A09ClaimSizingC1.md` (the counterexample),
`plans/round-49.md` (both counters and their declared before/after).

## Out of scope

Landing the lesson row, the QUALITY.md row, the knowledge entry and the instrument (L1's write
scope); the `recheck:` script and `verifiers/verify_dispatch_prompts.py` do not exist yet at
`a5adc146`, so the guard arms above are specified against the plan's text and the map's current
semantics, not against landed bytes. No lane file was edited; the only write in the lane is this
report. No sibling lane repo was written; no `jj` command was run.
