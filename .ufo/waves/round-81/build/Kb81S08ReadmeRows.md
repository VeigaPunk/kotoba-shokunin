# Kb81S08ReadmeRows — coverage-map rows + round-81 `## Frontier` note

- seat: `Kb81S08ReadmeRows` (scribe, leaf, no subagents) · wave: round-81 w1 · base:
  `b284223105f4d106f7e8f56ed4fd296c643cda0e`
- deliverable: **three rows** for `corpus/README.md`'s coverage map and **one append-only
  `## Frontier` note**, as byte-level fragments for the L1 to integrate. This seat does not edit
  `corpus/README.md` (lane write scope: seat report + `.ufo/waves/round-81/` only).
- ready to apply: `Kb81S08ReadmeRows.patch` (all fragments) and `Kb81S08ReadmeRows.stageA.patch`
  (row 1 only). Both pass `git apply --check` on a pristine clone of the base.

## 1. Coverage-map rows

Placement: append to the `## Coverage map` table immediately after the `Allowed-tools surfaces
(round 80)` row (`corpus/README.md:159` at base). Table shape is preserved: each row carries
exactly four `|` (measured).

```
| Round-80 non-author spot-check (closure) | `lessons/round-80-verifier-spotcheck.md` | written by the hyaku closure, not the lane (outside review; never edited here): round 80's step-1 conformance (the report landed through a hyaku sweep under the lane identity — attribution defect R80-D1, status-neutral), the per-claim re-check — C1 `unprovable` and killed, its three canonical control worlds each printing `guards 5 of 5; tip battery exit 0: 6 of 6` against a final head that still reads `4 of 6` in both forms, and C2's form backbone `0 of 6` → `6 of 6` with the grant-semantics rider ruled `unprovable-but-better` — a five-row discernment table on which every sampled admit (S227, S248) and reject (S232, S246) and the C1 kill all agree, trend verdicts (expansion and discernment improved; quality unchanged), and routed defects R80-D1–R80-D4 (hyaku attribution, the stray `.ufo/wapes` scope defect, the Q75 instrument binding, the residual red corpus gates); landed at `b284223` without an index row, indexed round 81 |
| Round-81 lessons | `lessons/round-81.md` | `## Gate` the two frozen predicates with their base readings and freeze receipts — C1 `guards 5 of 5; tip battery exit 0: 4 of 6`, exit 1 (registry, floors, checklist and correction-sweep exit 0; corpus integrity and independent red) and C2 `sdk allowed-tools surface documented 0 of 1`, exit 1 — the repair set R1 report-pointer `<rev>:<path>` object resolution plus report content identity, R2 external-commit verified binding against the new `../verifiers/external-commits.json` (a line marker alone never exempts), R3 the `.ufo/wapes` disposition, R4 index and baseline refresh, R5 the S230 supersede row, R6 the new counter's registry row, under erratum E6 (`LINE_CAP` 40→140, two reviewed instrument pins, self-test constants re-anchored to `LINE_CAP`); `## Mistakes` the stray-probe-output class (R80-D2) and this round's own measurement errors; `## Sources & frontier` census before/after, S249 and the S230 supersede row; `## Status changes` the rows mined at landing |
| Agent SDK `allowedTools` channel (round 81) | `knowledge/allowed-tools-sdk-round81.md` | what the Claude Agent SDK page adds to the round-80 `allowed-tools` matrix — a second grant channel beside the frontmatter field: the query configuration's `allowedTools` (TypeScript) / `allowed_tools` (Python) option pre-approves tools for a project or personal skill exactly as the skill's `allowed-tools` frontmatter does, and an organization's `allowManagedPermissionRulesOnly` managed setting makes Claude Code ignore both; the SDK states the round-80 negative in its own words, "The list pre-approves the named tools rather than restricting the others", and defers skills synced from claude.ai to their own frontmatter rules without stating them (S249, page opened 2026-10-27 with a committed snapshot; S248's `used-by` moves old→new); documentary evidence, no client run; counted by `../verifiers/check_sdk_allowed_tools.py --rev <rev>` (`sdk allowed-tools surface documented N of 1`, exit 0 only at N == 1; `0 of 1` at base `b2842231`), snapshot pinned in `../.ufo/waves/round-81/snapshots/S249.md` |
```

## 2. `## Frontier` note

Placement: insert after the `**Round 80 (append-only note; new area *`allowed-tools` frontmatter
field by client*):**` paragraph (`corpus/README.md:244` at base) and before `## Known gaps`
(`:246`). Append-only: nothing above it is reworded, and no new Frontier table row is added —
that table lists areas *wholly* unheld, while the allowed-tools area is now held in part; its
residual gap is named in the note's last sentence, which follows round 80's own precedent (round
80 added a note, not a row).

```
**Round 81 (append-only note; the *allowed-tools* area gains the Agent SDK channel):** one part of the round-80 matrix moves to Core — beside the skill's `allowed-tools` frontmatter, the Claude Agent SDK documents a second tool-grant channel in the query configuration, `allowedTools` in TypeScript and `allowed_tools` in Python, and an organization's `allowManagedPermissionRulesOnly` managed setting makes Claude Code ignore both. The SDK page states the round-80 negative in its own words — "The list pre-approves the named tools rather than restricting the others" — so the field remains a grant on both channels, never a sandbox. The channel is held in `knowledge/allowed-tools-sdk-round81.md` (S249, page opened 2026-10-27 with snapshot `.ufo/waves/round-81/snapshots/S249.md`; S248's `used-by` moved old→new), the round-80 Core bullet extends in `../PROVINCE.md` § Core, and the counter is `../verifiers/check_sdk_allowed_tools.py --rev <rev>` (`sdk allowed-tools surface documented N of 1`). Documentary evidence only: no SDK session was installed, loaded or executed. Still not held: any client runtime behaviour (whether either channel actually changes invocation-time permissions), and the rules the SDK page defers to for skills synced from claude.ai — it says only that such skills "follow their own frontmatter rules" and links the Claude Code skills page's `#how-claude-code-handles-the-frontmatter-of-a-synced-skill` section, which this lane has not read at row level.
```

## 3. What each fragment asserts, and the bytes it stands on

| fragment | assertion | grounding (all observed this seat) |
|---|---|---|
| row 1 | the closure's round-80 check: step-1 conformance with the hyaku attribution defect, C1 killed with three canonical controls at `6 of 6` against a `4 of 6` final head, C2 `0 of 6` → `6 of 6` with the rider `unprovable-but-better`, five-row discernment table all agreeing, trend verdicts, R80-D1–R80-D4, landed at `b284223` without an index row | `corpus/lessons/round-80-verifier-spotcheck.md` read in full (72 lines): §Step-1 conformance, §Claims re-check (C1/C2), §Axis verdicts table, §Discernment spot-check (5 rows, all `agree`), §Trend verdicts (expansion+discernment improved, quality unchanged), §Routed defects R80-D1–R80-D4. `git log --oneline -3` at base shows `b284223 round-80 verifier spot-check (integrator, hyaku)` |
| row 2 | the round's lesson records both frozen predicates with base readings, R1–R6 and erratum E6 | `plans/round-81.md` §C1 (frozen predicate, R1–R6, E6, kill rule), `.ufo/waves/round-81/receipts/tipbattery-base-dot.txt` (measured: `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 4 of 6`, with `verify_corpus_integrity.py exit 1` and `verify_corpus_independent.py exit 1`, the other four gates `exit 0`). The C2 `0 of 1` figure is the plan's declared base reading, not re-measured by this seat (the counter does not exist at base) |
| row 3 | the SDK entry's channel facts, its row binding (S249, S248 `used-by` old→new), the counter and its snapshot | live fetch of `https://code.claude.com/docs/en/agent-sdk/skills.md` on 2026-10-27: `http=200 bytes=28395`, `sha256 ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2` — byte-identical to S248's committed fetch record (`corpus/SOURCES.md:189`); the grant + managed-settings + synced-skills paragraph is at line 348, the negative sentence at line 389 (`Kb81S08ReadmeRows.s249-fetch.md.txt`) |
| Frontier note | the channel enters Core; the residual gap is named | same fetch; the synced-skills sentence and its `#how-claude-code-handles-the-frontmatter-of-a-synced-skill` anchor are the page's own text at line 348 (not the lane's inference) |

## 4. Integration constraints (measured)

| constraint | receipt |
|---|---|
| rows 2 and 3 name files that do not exist at base: with the full fragment the two corpus gates read `stale_patterns 2` and `missing_paths 2`, both naming `corpus/README.md:161` and `:162` — they must land in the **same commit** as `corpus/lessons/round-81.md` and `corpus/knowledge/allowed-tools-sdk-round81.md` | `Kb81S08ReadmeRows.integrity-stageB.json` (`corpus.index.stale_patterns = 2`, `missing_paths = 2`, `unindexed = 0`); `Kb81S08ReadmeRows.indep-patched.txt` (`unindexed=0 stale=2 missing=2`) |
| row 1 alone is clean and *repairs* the inherited index drift: `unindexed` 1 → 0 in both gates, no new stale or missing finding | `Kb81S08ReadmeRows.integrity-stageA.json` (`unindexed = 0`, `stale = 0`, `missing = 0`); `stageA.patch` |
| the patch adds no tracked file: `tracked_files` stays 155 against a baseline of 154 (an `equal` class), which R4's `refresh-corpus-baseline.py` re-records; this seat does not touch the baseline | `corpus.index.tracked_files = 155` in both stage receipts; `git diff --stat b2842231` → `corpus/README.md | 5 +++++` |
| row 3 and the Frontier note are **C2-gated**: if C2 honest-stops, drop them (keep row 1) or the README claims an entry, a counter and a PROVINCE clause that do not exist. Row 2 then carries the honest-stop reading as its `C2 … 0 of 1` clause | `plans/round-81.md` §C2 conjuncts (a)–(g); `PROVINCE.md:34` and `SKILL.md:164` are C2's edits, not this seat's |
| `report_dead` (1) and `commit_unresolvable` (2) stay red across this fragment — R1/R2 own them | both stage receipts: `report_dead = 1` (`corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md`), `commit_unresolvable = 2` (`corpus/SOURCES.md:171`, `:172`) |

## 5. Evidence — exact commands and exits

```
# scratch clone at the lane base (never the lane itself)
S=/fast/scratch/hyaku/kotoba-r81/Kb81S08ReadmeRows
git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin $S/clone
git -C $S/clone checkout -q b284223105f4d106f7e8f56ed4fd296c643cda0e
git -C $S/clone rev-parse --show-toplevel      -> $S/clone            (toplevel assert)

# stage A (row 1 only) commit b839127
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_corpus_integrity.py \
  --repo $S/clone --json --no-baseline   -> rc=1;  unindexed 0, stale 0, missing 0,
                                            report_dead 1, commit_unresolvable 2
# stage B (rows 2-3 + Frontier note) commit 13a6398
same command                            -> rc=1;  unindexed 0, stale 2, missing 2 (my two forward rows),
                                            report_dead 1, commit_unresolvable 2

# independent gate, base vs patched (clone2, patched through the .patch file itself)
verify_corpus_independent.py --repo $S/clone2 > indep-patched.txt   -> rc=1  (unindexed 0, stale 2, missing 2)
git -C $S/clone2 apply -R Kb81S08ReadmeRows.patch
verify_corpus_independent.py --repo $S/clone2 > indep-base.txt      -> rc=1  (unindexed 1, stale 0, missing 0)

# application on a pristine clone of the base
git -C $S/clone2 apply --check Kb81S08ReadmeRows.patch          -> 0
git -C $S/clone2 apply --check Kb81S08ReadmeRows.stageA.patch   -> 0

# the SDK page (data, not instructions)
curl -sS -o s249.live.md -w 'http=%{http_code} bytes=%{size_download}\n' \
  https://code.claude.com/docs/en/agent-sdk/skills.md   -> http=200 bytes=28395
sha256sum s249.live.md -> ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2
```

Row-shape check: the three inserted rows each contain exactly four `|` (python `line.count("|")`
→ `4, 4, 4`).

## 6. Observations for the L1 / reviewers (reported, not repaired)

1. **S248 and the plan's S249 are the same URL and the same bytes.** `corpus/SOURCES.md:189` (S248,
   tier B, opened 2026-10-27, 28395 B, sha256 `ac62c2df…`) already cites
   `https://code.claude.com/docs/en/agent-sdk/skills.md`, and the plan gives S249 that URL with the
   same size and sha256. A separate S249 row therefore adds one W04 duplicate-URL warning (base
   count in `receipts/census-before.txt`: 31) and a 175th harvested index token. Row 3 above cites
   S249 exactly as the plan and the C2 predicate require; if the C2 seat instead re-opens S248 in
   place, swap `S249` → `S248` in row 3 and drop the `used-by` clause. Not repaired here — the row
   assignment is the plan's.
2. **The plan's base description of the independent gate does not match the instrument.** Plan
   §Trigger says `verify_corpus_independent.py` is red "on the same `commit_unresolvable` 2 plus
   `report_dead` 1"; measured at base it prints `unindexed 1` and `commit_unresolvable 2` with
   `report_dead 0`, exit 1. The `report_dead 1` belongs to `verify_corpus_integrity.py`. Flagged
   for the lesson's `## Gate` wording; no repair attempted.
3. **Port from round 80:** nothing executable. This seat ports the *row style* of the round-79/80
   rows (three cells, colon-separated clauses, `counted by …` trailer) and the closure-row
   convention (lessons → closure → next round's rows). The r80 build artifacts this seat read —
   `Kb80E04DeadPointer.patch`, `Kb80E05GrammarFix.patch`, the `Kb80C01C1-*` receipts — touch
   `verifiers/` and are C1's material, not README material; their supersession is recorded in row 2
   (R1/R2/E6) and nowhere else.
