---
author: hyaku closure (non-author integrator, @m_opus)
round: 54
lane: kotoba
base: 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4
head: c501cd537c75155e0196e217bda013ec164ad770
report: .ufo/reports/round-54/kotoba.md (fleet 77b842026696624cc86013c6cee392361e917ecd)
closed: 2026-10-22
---

author: hyaku closure (non-author integrator, @m_opus)

# Round 54 — non-author verifier spot-check (kotoba)

Driver digest (copied from `.ufo/watchdog.log:767,775`, mutable log):

```
2026-10-22T18:05:24-03:00 launch kotoba round=54 pgid=327882 driver=hyaku-inline attempt=1
2026-10-22T19:44:43-03:00 complete kotoba round=54; hyaku-inline attempt=1
```

Re-checks used seven read-only closure seats (reviewer ×5: `SpotAdmits`, `SpotRejects`, `C2Registry`, `NoHarm`,
`ConformanceEvidence`; critic ×2: `C1Semantics`, `AxisCritic`), dispatched by the closure, not by the lane. The
closure itself ran conformance, the plain counts, the census, one source re-open (S061) and the reject-1 route
check. The two frozen claim counters ran in a sandbox clone (`/tmp/kotoba-r54-close`), never in the lane.
Disclosure: seats `NoHarm`, `C1Semantics` and `ConformanceEvidence` also ran lane gates in their own `/tmp`
clones; those runs are recorded as corroboration only. The no-harm judgment rests on plain diffs and committed
evidence (PROTOCOL § Gate standard, Closure consequence).

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report by lane identity | `git log --format='%an %H' -- .ufo/reports/round-54/kotoba.md` | `kotoba-shokunin 77b842026696624cc86013c6cee392361e917ecd` | pass |
| SHONEN heading | report § SHONEN | 4 lines, one per box, all `[~]` with a pointer | pass |
| cited hashes are ancestors of `master` | `git merge-base --is-ancestor <full> master` for each of the 12 landed commits plus base, `e792607e`, `e5355a62` | all 15 pass | pass |
| `451a02ff` | `git rev-parse --verify 451a02ff^{commit}` | not a lane object. It is the google-gemini/gemini-cli commit pinned in S060's URL. The report cites it as a pointer that was fixed, not as a lane commit, and the entry cites it as `google-gemini/gemini-cli@451a02ff` | not a defect |
| pushed, clean | `scripts/hyaku/jj-lane.sh state …` ; `git status --porcelain` | `local=remote=c501cd53… ahead=0 behind=0 tracked=0 untracked=0`; porcelain empty | pass |
| prompt carries template contract | `diff` of prompt §§1–5 against `templates/round-prompt.md` | only `{{FLEET_ROOT}}`/`{{AXES}}`/`{{LANE}}`/`{{ROUND}}` substitutions; §6 is the hyaku addendum; committed `3a07fbb` | pass |
| marker? | — | real work, 12 landed lane commits | not a marker |

Seat counts were checked against the committed wave registries (`ConformanceEvidence`): build 40 (executor 23,
scribe 10, critic 2, mutation-tester 2, scout 1, connector 1, reviewer 1) and falsify 41 (reviewer 33, critic 4,
mutation-tester 2, scout 2). Both match the report; the round total is 81.

## 2. Claims — re-derived at `c501cd53`

Both counters are frozen: `git diff --stat e3371548 c501cd53 -- verifiers/check_description_thresholds.py
verifiers/check_gate_registry.py` printed nothing.

### C1 — depth (lowest owned axis, 9): description thresholds by client

Re-measured with the frozen counter (`python3 -B verifiers/check_description_thresholds.py --rev <rev>`, sandbox):

| rev | output | exit |
|---|---|---|
| `422ffd10` (base, the do-nothing control) | `description thresholds backed 0 of 7 clients` | 1 |
| `e3371548` (plan) | `… 0 of 7 clients` | 1 |
| `bf65974c` (after C2, before C1) | `… 0 of 7 clients` | 1 |
| `5a097e12` (C1 content) | `… 7 of 7 clients` | 0 |
| `cae8f2ea` / `c501cd53` | `… 7 of 7 clients` | 0 |

The declared target was "4 of 7 or more, exit 0". It is met, and these values match the report.

Plain checks:
- `git show c501cd53:SKILL.md | grep -n 'Description thresholds by client'` → `179`. The table has 7 client rows,
  each with threshold, past-threshold and action cells.
- Guards (erratum 3, declared before content), from `C1Semantics`:
  - (a) S053–S064: `grep -c` gives 0 each at `e3371548`.
  - (b) `1,536`, `1%`, `0.01`, `2%`, `8,000` and `10,000` each count 0 in `e3371548:SKILL.md`. That makes two
    clients with new numbers (Claude Code, Codex), the declared minimum.
  - (c) `--fetch --rev c501cd53` prints `found on the live page 7 of 7`, exit 0. This was re-run after
    `cae8f2ea` changed the cells; W2RerunC1 recorded the same at `5a097e12`.
- The SKILL.md table cells were compared with the live pages: Claude Code `skills.md:389,1207-1213` and
  changelog 2.1.105, Codex `build-skills.md:38-44`, Cursor `release-notes.md:122`. The wording matches.

**Verdict: verifies (re-measured).** It is a learning claim under the session quality bar: a `SKILL.md` decision
table grounded in an admitted entry. New ground: the Codex 2%/8,000/10,000 numbers, which were only in SOURCES
rows before, and the Copilot CLI, Cursor, Gemini CLI and opencode-v2 rows. The Claude Code row confirms numbers
already held in `sibling-overlap-census-round49.md:155` and `skill-selection-rules-round50.md:48`.

### C2 — consistency (declared calibration sub-axis): gate registry rows

Re-measured with the frozen counter (`python3 -B verifiers/check_gate_registry.py --rev <rev>`, sandbox):

| rev | output | exit |
|---|---|---|
| `422ffd10` (base, the do-nothing control) | `gate registry rows conformant 0 of 21 lane verifiers; phantom 0` | 1 |
| `b55550b9` | `… 0 of 23 …; phantom 0` | 1 |
| `bf65974c` (C2 content) | `… 24 of 24 lane verifiers; phantom 0` | 0 |
| `5a097e12` / `c501cd53` | `… 24 of 24 …; phantom 0` | 0 |

Plain count: `git ls-tree --name-only <rev> verifiers/ | grep -cE '\.(py|sh)$'` gives 21 at base and 24 at
`bf65974c` and the tip. `## Gate registry` headings: 0 at base, 1 at tip. Registry rows at the tip: 24. The
sorted row names diff empty against the blob list (`C2Registry`).

`C2Registry` also checked:
- All 24 self-test flags are real argparse/case handlers wired to an in-file self-test. None passes only by the
  disclosed substring test.
- All 24 rows map `0=clean, 1=failed` and declare the other codes they use.
- In `b55550b9`, the four scripts' judging and counting lines are unchanged.
- The erratum-2 guard is evidence-verified from `.ufo/waves/round-54/falsify/W2RerunC2.md`, not executed by the
  closure: the four gates' own self-tests exit 0 at `bf65974c`, and the negative control exits 2 at `7ad05d34`.

**Verdict: verifies.** The counter results are re-measured. The erratum-2 guard is evidence-verified.

### Rulings on C2's axis and the §9 standard

- **Fleet-2 mapping (PROTOCOL.md:525-527): holds.** At both revisions the row label in the same row is
  `consistency (calibration sub-axis)`, and the SCORECARD preamble (lines 8-16) carries the derivation.
- **Calibration bullet carried in this prompt (§6.9): met in substance.** The bullet says a calibration claim
  "must count mismatches between the lane's self-assessment (SCORECARD/SHONEN) and observed repo state".
  - C2's counter does count mismatches: a verifier with no row, a phantom row, a flag absent from the file, a
    pinned path that does not exist. What it compares is the lane's own description of its gates against
    `verifiers/`. That description sits at the PROTOCOL § Gate standard registry home, which is a
    self-description surface but neither SCORECARD nor SHONEN.
  - The ruling: it is a count, not an assertion, so the bullet's operative requirement holds. The surface
    difference is recorded rather than graded as a misfit.
  - Critic `AxisCritic` dissents: it reads the work as operability-shaped. That dissent is on record.
- **Addendum §9 do-nothing and surface clauses: not in this prompt.** They were amended at `dc05427` (21:55Z) and
  `4248e92` (22:37Z), after this round's 21:05Z dispatch. `grep -c do-nothing .ufo/prompts/kotoba-round-54.md`
  gives 0. Applied informationally:
  - **Do-nothing control:** the base prints 0/7 and 0/21 with exit 1, so neither target is reachable by doing
    nothing.
  - **Cheaper control (`AxisCritic`, `/tmp` clone):** a mechanical all-`probe` table at `422ffd10` makes the
    counter alone print `21 of 21 … phantom 0`, exit 0. It fails the claim's pre-data predicate, because erratum
    2 (`3b2535d2`, before content) says "A `probe` label or a borrowed flag on any of the four fails the claim
    even if the counter prints `M of M`". So the declared claim is not reachable by that control. No control
    receipt was committed before freezing, which is a future-round duty (routed 5).
  - **Axis by surface:** the surface changed is the `SKILL.md` § Gate registry, the lane's description of its own
    gates. That fits the lane's mapped consistency axis. The four self-tests are enabling operability work and
    are not credited as a separate move.

## 3. No-harm

| check | command | observed |
|---|---|---|
| SCORECARD scores | `git diff 422ffd10 c501cd53 -- SCORECARD.md` plus score extraction at both revisions | identical at both: depth 9, consistency 10, coverage 8.5, operability 8.5, freshness 8, calibration 8.5, adjacency 8.0; diff adds round-54 row text and history rows only |
| SKILL.md budget | `git show <rev>:SKILL.md \| wc -l` | 593 → 599 (≤ 600) |
| SKILL.md removals | removed lines compared with the `7ad05d34` additions to `verifiers/README.md` | exactly 43 removed lines, identical to the 43 moved lines; no other removal (`NoHarm`) |
| SOURCES append-only | cell-by-cell diff of changed rows | only S046 `used-by` changed (allowed by CORPUS.md rule 2, logged in the lesson); everything else is appended rows S053–S064 |
| LOG append-only | `git diff … -- LOG.md \| grep -c '^-[^-]'` | 0 |
| deleted files | `git diff --name-status --diff-filter=D 422ffd10 c501cd53` | none |
| corpus integrity at tip | committed baseline 81/51 re-recorded; `ConformanceEvidence` sandbox `verify_corpus_integrity.py` | tip 81 tracked / 51 report pointers, 0 defects |

No axis is harmed. The `commit_unresolvable` 0→1 that `W2CriticNoHarm` found at `58db81c4` (the
`` commit `451a02ff` `` grammar in the new entry) was fixed in `cae8f2ea`. At the tip the entry reads
`google-gemini/gemini-cli@451a02ff`.

## 4. Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| depth | improved | C1 re-measured 0/7 → 7/7, guards a–c hold; score held 9 (band move left to the operator) |
| consistency (calibration sub-axis) | improved | C2 re-measured 0/21 → 24/24, phantom 0; erratum-2 guard evidence-verified; score held 10 |
| calibration | unchanged | 8.5 at both revisions |
| coverage | unchanged | 8.5 at both revisions |
| operability | unchanged | 8.5 at both revisions; the four self-tests are C2's enabling work, not a declared move |
| freshness | unchanged | 8 at both revisions; no freshness claim (drift-sentinel binding) |
| adjacency | unchanged | 8.0 at both revisions |

Neither claim is exploratory, so no `unprovable-but-better` ruling is needed.

### Dispatch-note bindings (drift-sentinel trip, round-53 routed defect 1)

| binding | evidence | holds |
|---|---|---|
| no freshness claim | plan claims are C1 depth and C2 consistency only (`plans/round-54.md:24,38`) | yes |
| nothing on `verify_surfaces.py` | `git diff --stat 422ffd10 c501cd53 -- verifiers/verify_surfaces.py` → empty; only its registry row names it | yes |
| nothing on the executed-checklist / always-on row | `corpus/README.md` diff: 9 insertions, 0 deletions, all on the Per-render row note (:120). `check_alwayson_boxes.py` gained only its own `--self-test` (C2 guard) | yes |
| different frontier area | `git log -S'Per-render' -- corpus/README.md` → only `f2f9ee1` (round 46) and `5a097e1` (round 54) | yes |
| depth learning claim | C1, verified above | yes |
| lowest-axis duty | owned-only reading: depth 9 is lowest and C1 works it | yes (the round-47 L0 question stays open) |

## 5. Discernment spot-check (`corpus/lessons/round-54.md` `## Gate`)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S053 Claude Code skills | admit | https://code.claude.com/docs/en/skills.md → 200, 111,928 B, sha256 `d1359f0c…` | agree | quote verbatim at `:389`; a description listing cut, not a name cap; 15 words |
| S054 Codex build-skills | admit | https://learn.chatgpt.com/docs/build-skills.md → 200, 11,035 B, sha256 `ed6e324f…` (full match) | agree | quote at `:38-39` (line wrap); a listing budget, and SKILL.md frames it so; 20 words |
| S057 Gemini CLI best practices | admit | https://geminicli.com/docs/cli/skills-best-practices.md → 200, 3,257 B, sha256 `612c3b83…` | agree | content identical at `:24`, but the lesson strips the markdown `**`, so it is not byte-verbatim (routed 7); ~100 words is a size estimate, and the action cell says so |
| S058 Cursor release notes | admit | https://cursor.com/docs/release-notes.md → 200, 301,193 B, sha256 `fd4d830a…` | agree | verbatim at `:122`; 64 = name, 1,024 = description, kept distinct; 25 words |
| S061 Zed instructions (correction row) | admit | https://zed.dev/docs/ai/instructions.md → 200, 3,169 B, sha256 `7c63efe035bf0638…` (closure fetch) | agree | the lesson quote "Project instruction files apply to the current project. Zed uses the first matching file in this list:" is verbatim at `:25` (17 words) |
| docs.github.com `concepts/agents/about-agent-skills.md` | reject | `.md` → 404, 502 B; without `.md` → 200, redirected to `concepts/customizations/agent-skills` (`.md` 200, 2,622 B) | agree (decision) | the route really is 404. The flip condition ("a live route for the concept page") is now met, but `grep -n -i -E "1024\|1,024\|character\|descript\|limit"` on the moved page gives 0 hits, so there is still nothing to quote for C1 (routed 4) |
| cursor.com/changelog.md | reject | 200, 186,742 B; `grep -ci skill` → 0 | agree | HTML shell; admitting it would record a false silence |
| Copilot CLI plugin reference `Max 1024 chars` | reject | `cli-plugin-reference.md` → 200, 47,200 B; `:195` plugin manifest, `:349` marketplace entry | agree | the caps are on plugin metadata, not a skill `description` |
| `RegCheckOpencodeRepin` draft row (borrowed nested `--self-test`) | reject | `build/RegCheckOpencodeRepin.md`; `git show c501cd53:verifiers/check_opencode_repin.py` (own handler `:43,199-203`, `def self_test()` `:87`) | agree | the borrowed literal would have passed the substring test; the script got its own self-test instead |

SOURCES row quote check:
- S061: the lesson's ≤25-word quote is verbatim on the closure's fetch.
- S053, S054, S057 and S058: SOURCES `teaches` cells are 23, 22, 16 and 16 words, each ≤25 (`SpotAdmits`).

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` printed `kotoba ok`,
exit 0. W04 duplicate-url warnings: S018, S019, S021, S054, S055, S056 (six, as the report says). Rows went
52 → 64 (`grep -c '^| S[0-9]'`).

## 6. Trend verdicts

| trend | verdict | evidence |
|---|---|---|
| expansion | improved | knowledge entries 40 → 41 (`git ls-tree -r --name-only <rev> corpus/knowledge \| grep -c '\.md$'`); the new entry sits on Frontier row *Per-render consumption* (offer-render half) and cites mined rows S053–S064 |
| quality | improved | S046 `teaches` was superseded by S060, and S050's in-place edit was recorded by S061, both append-only. The baseline that was red at base (79 tracked, 1 unindexed) is 81/51 with 0 defects at tip. Over-wide C1 cells were corrected in `cae8f2ea`. No admitted entry fails its re-check; the leftover cells (routed 3) are precision gaps, and the Codex one is marked "from source, not documented" in the entry |
| discernment | improved | the outside spot-check agrees on 5 of 5 admits and 4 of 4 rejects |

## 7. Routed defects (lane fixes next round; all status-neutral)

1. **No-harm receipts are not attributed to the revisions the report names.**
   - Report line 56 says `--base 422ffd10 --head cae8f2ea → new 0, resolved 3`, but the committed receipt is
     `ExecTipRuns.md:214-221` at head `b38c32a0`. `git grep cae8f2e c501cd53 -- .ufo/waves/round-54/` → 0 hits.
   - "checklist 11/11 PASS" has no committed receipt. `W2CriticNoHarm` records 3 environment FAILs in its
     sandbox at both revisions.
   - The numbers hold at the tip in the closure seat's sandbox. This is a repeat of the round-53 routed defect 5
     class: commit the runs with the revision measured.
2. **Mined mistakes without QUALITY criteria.** M45 and M47 have `captured-by: none`, but `corpus/QUALITY.md` is
   unchanged in the range (`git diff --stat` empty). LEARNING.md step 3 asks for a criterion citing the lesson,
   or the report should say why not.
3. **Over-wide C1 cells at the tip** (`C1Semantics`). None of them drops the count below 4 of 7.
   - Gemini threshold "~100 words" is a size estimate that the counter still counts. Mark it as no threshold.
   - The Codex "shipped parser cuts at 1,024" cell cites `frontmatter-rule-authorities-round48.md:51`, which
     says it is "not tabled here because no source row pins that code". Label it unpinned or drop it.
   - The Cursor action "move detail into `references/`" is not in S058. Cite `cursor.com/docs/skills.md` or drop
     it.
   - Gemini "nothing is cut" lacks its source pointer (`skillLoader.ts`, `snippets.ts` @ `451a02ff`).
4. **Reject-1 flip met.** Record the route move (`concepts/customizations/agent-skills.md`, 200, 2,622 B, no
   description threshold) in the next lesson. The reject decision stands.
5. **C2 counter hollow shape.** A mechanical all-`probe`/`none` table reaches `M of M` (21 of 21 at `422ffd10`,
   `AxisCritic`), and the flag check is a substring test (disclosed in erratum 2). Before C2's counter is used
   again, close the probe route (check kind against the script), match the exact flag handler, and commit a
   cheapest-control receipt before freezing. Addendum §9 as amended (`dc05427`, `4248e92`) binds rounds rendered
   after it.
6. **Registry row vs a red gate.** `verifiers/fault_injection_corpus.sh` is registered `gate` with `--self-test`,
   while the report carries it as red since round 49 with its self-test red. Under § Gate standard Closure
   consequence it stays a routed red gate; annotate the row or repair the gate.
7. **Minor.**
   - The S057 lesson quote drops the markdown `**`. Quote bytes or state the normalisation.
   - The S060 Gate cell holds three quotes (14 + 4 + 22 words). Each is ≤25, but the row has no single grounding
     quote.
   - SKILL.md is at 599/600 lines.
8. **Carried from the report:** environment failures exit 1 instead of 2 in several gates; weak self-tests
   (callee rename, opencode repin 1/4 mutants); the 12 earlier SOURCES protected-cell changes found by M45's
   gate await an operator decision; the round-53 items under its routed 7.

## 8. SHONEN (operator note)

`git diff 422ffd10 c501cd53 -- SHONEN.md` is empty: 4 boxes, all `[~]`, no `[x]`.
- Box 1 (real decision tables, error patterns, checklists, cited sources) now looks checkable by a non-author:
  the § Description thresholds table is source-quoted and was re-verified here, and § Gate registry is
  re-derivable.
- The other boxes still rest on lane-run evidence.

Promotion is operator-owned; nothing was marked.

## Verdict

Status `ok`; **admitted**. Both claims verify (C1 re-measured; C2 re-measured, guard evidence-verified), and no
axis is harmed. The drift-sentinel bindings hold. The calibration bullet is met in substance by a mismatch
count, with the `AxisCritic` dissent on record. Routed defects 1–8 above are status-neutral.
