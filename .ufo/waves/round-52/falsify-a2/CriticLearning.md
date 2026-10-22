Result: MIXED — the round shape passes the lowest-axis test, C1's after-state and both re-derivations, but the learning claim's content records two clients as silent when both document MCP server instructions on hosts the frozen counter pins, the routed-defect drift sentinel trips (third round running), and C2's after-state is declared as a floor ("at least 3"), not one value.

Seat: `KotobaR52a2.CriticLearning` (critic, falsify wave attempt 2). Judged revision: `master` at
`c8407a453788df964df5a7b835dd0ce1360de882`, plus the uncommitted `SCORECARD.md` working-tree diff.
Sandbox: `/fast/scratch/hyaku/kotoba-r52a2/CriticLearning` (clone at `c8407a45`). Nothing was
written in the lane except this file. Installs: none. Tools used: `git`, `python3`, `curl`, `gh api`
(already installed, read-only calls).

Targets: `.scratch/goal-20261022-hyaku-12h.md` § Quality bar (lines 144-161) and § Drift sentinels
(lines 163-178); `.ufo/prompts/kotoba-round-52.md` § 6.9 (lines 342-350); `plans/round-52.md`,
`plans/round-50.md`, `plans/round-51.md`; `SCORECARD.md` § axes.

## Verdict per test

| Test | Verdict | Severity of defect |
|---|---|---|
| T1. At least one learning claim | HOLDS-BOUNDED as a claim; its content BREAKS (finding F1) | HIGH (content, not the count) |
| T2a. Same axis and surface as rounds 50-51 (claims) | HOLDS | none (watch item for round 53) |
| T2b. Same routed defect class three rounds running (sentinel) | BREAKS: the sentinel trips (F2) | MEDIUM |
| T3. C1 on the lowest non-retired axis | HOLDS | none |
| T4. After-states concrete and re-derivable by one command | C1 HOLDS; C2 re-derives but is declared as a floor (F3) | LOW-MEDIUM |
| T5. Universal clauses | Claim statements HOLD; landed text has one unbounded craft row (part of F1) and one wide headline (F5) | LOW (F5) |
| Extra: uncommitted `SCORECARD.md` diff | BREAKS on one unsupported sentence (F4) | MEDIUM |
| Extra: round shape (waves, attack share) | HOLDS-BOUNDED (F6) | LOW |

## T3 — C1 on the lowest non-retired axis: HOLDS

- `SCORECARD.md` § axes at the plan commit (`git show 4c003a4b…:SCORECARD.md`, axes table): depth 9,
  consistency 10, coverage 8.5, operability 8.5, freshness 8, calibration 8.5, adjacency 8.0. Same
  values at base `c8579a4c`. Lowest is 8, a tie between freshness and adjacency.
- `SCORECARD.md:147-149` § retired: "None." So no axis is excluded.
- C1 works freshness (`plans/round-52.md:20`). The tie-break given (`plans/round-52.md:10-12`:
  adjacency claimed in rounds 49 and 50) is consistent with the sentinel. HOLDS.

## T2a — same axis and surface as rounds 50-51: HOLDS (with a watch item)

| Round | C1 | C2 |
|---|---|---|
| 50 | adjacency — `SKILL.md` description names census lanes (`plans/round-50.md:9-11`) | operability — box-proof case deletion (`plans/round-50.md:32-33`) |
| 51 | freshness — `verify_surfaces.py` omp extraction re-pin (`plans/round-51.md:10-14`) | depth — overlap levers table (`plans/round-51.md:26-32`) |
| 52 | freshness — `verify_surfaces.py` omp extraction, callee rename (`plans/round-52.md:20-22`) | coverage — MCP server `instructions` entry (`plans/round-52.md:39-45`) |

- C1 repeats round 51's axis and surface (freshness, omp extraction in `verify_surfaces.py`): two
  rounds running, not three. Round 49 was adjacency and an unnamed C2 (`plans/round-49.md:11-17`), so
  no trip.
- C2 is a new axis and surface. The plan correctly drops the sibling and overlap arbitration surface,
  which did run three rounds (49, 50, 51) (`plans/round-52.md:14-16`).
- Watch item: round 53 must not claim freshness on omp extraction in `verify_surfaces.py` again. The
  uncommitted round-53 note lists the omp fixture labels as a candidate; that is fine as a carried
  item, not as a claim.

## T2b — same routed defect class three rounds running: BREAKS (F2, MEDIUM)

The class is "a record sentence or headline states more than was verified, and the corrections sweep
missed it". It was routed into three consecutive rounds:

- Into round 50, from `corpus/lessons/round-49-verifier-spotcheck.md:219-230`: D2 ("docstring … still
  says the fixtures 'discriminate every conjunct' … SCORECARD … without the six-conjunct bound") and D4
  ("The SCORECARD adjacency row says … Append a qualifier").
- Into round 51, from `corpus/lessons/round-50-verifier-spotcheck.md:254-261`: D2 ("`SCORECARD.md:31`
  … say the checklist gate runs `--box-proof` with no fail-open bound") and D3, labelled "(corrections
  sweep)": "`corpus/README.md:72` still says … which the entry's own correction withdrew".
- Into round 52, from `corpus/lessons/round-51-verifier-spotcheck.md:160-167`: item 1 ("The corrections
  sweep missed both", `corpus/README.md:133-141` and the index row) and item 2 (`SCORECARD.md:28` "The
  headline must lead with the declared result").

The goal file's sentinel row (`.scratch/goal-20261022-hyaku-12h.md:173`): "Same axis+surface claim or
same routed defect class in a lane 3 rounds running | The lane's next round must work a different
frontier area." That row trips at this round's closure.

Evidence that the class will recur:
- The M36 fix, `verifiers/check_correction_sweep.py:30-37`, is a registry of three literal strings
  (`overlap levers backed 7 of 7 clients` twice, and `` `7 of 7`, exit 0 @ `34cfffbb` ``). Its
  docstring says (`:18`) "A new superseded claim is added as a new registry row". It catches only the
  instances already found by hand, so it cannot catch a new instance until someone else spots it and
  adds a row.
- The uncommitted `SCORECARD.md` diff already carries two new instances (F4, F5).

Smallest safe correction: the round-53 note in `SCORECARD.md` (and the round report) states that the
sentinel tripped and that round 53 works a different frontier area. The closure records the trip.
Whether the sweep check should generalize is the M36 seats' call (`MutSweepCheck`, `CriticQ29`); this
seat only records that, as written, it does not stop the class.

## T4 — after-states concrete and re-derivable by one command

All runs were in the sandbox clone. Both counters are byte-identical to the plan commit:

```
$ git show 4c003a4b…:verifiers/check_mcp_instructions.py > …/CriticLearning-plan-mcp.py; cmp … verifiers/check_mcp_instructions.py && echo identical-to-plan
identical-to-plan
$ git show 4c003a4b…:verifiers/check_callee_rename.py | cmp - verifiers/check_callee_rename.py && echo c1-identical-to-plan
c1-identical-to-plan
```

**C1: HOLDS.** One value (`4 of 4`), one command, over committed bytes (fixtures pinned to
`FIXTURE_REV = "c8579a4c…"`, `verifiers/check_callee_rename.py:61`). Run at 2026-10-22T17:51:18Z:

```
python3 -B verifiers/check_callee_rename.py --rev c8579a4c…  → callee-rename robust 0 of 4 fixtures  exit=1
python3 -B verifiers/check_callee_rename.py --rev 4c003a4b…  → callee-rename robust 0 of 4 fixtures  exit=1
python3 -B verifiers/check_callee_rename.py --rev c2107ecf…  → callee-rename robust 4 of 4 fixtures  exit=0
python3 -B verifiers/check_callee_rename.py --rev c8407a45…  → callee-rename robust 4 of 4 fixtures  exit=0
  … --rev c2107ecf… --seed 7     → 4 of 4  exit=0
  … --rev c2107ecf… --seed 1234  → 4 of 4  exit=0
```

**C2: re-derives as reported; the declared after-state BREAKS the sizing rule's letter (F3,
LOW-MEDIUM).** Run at 2026-10-22T17:51:09Z:

```
python3 -B verifiers/check_mcp_instructions.py --rev c8579a4c…  → mcp instructions backed 0 of 7 clients  exit=1
python3 -B verifiers/check_mcp_instructions.py --rev 4c003a4b…  → backed 0 of 7  exit=1
python3 -B verifiers/check_mcp_instructions.py --rev c2107ecf…  → backed 0 of 7  exit=1
python3 -B verifiers/check_mcp_instructions.py --rev c8407a45…  → backed 5 of 7  exit=0
```

`plans/round-52.md:45` declares the after-state as "at least `3 of 7`" and `:50` as "At least 3, exit
0". The counter's `TARGET = 3` (`verifiers/check_mcp_instructions.py:65`) makes exit 0 mean "3 or
more". § 6.9 (`.ufo/prompts/kotoba-round-52.md:343`) and the goal file (`:151`) ask for "one concrete
value". The closure can still re-derive the count, so this is a sizing defect, not a broken
measurement. The cost: the falsify wave could knock out two of the five rows and the claim would
still read verified, so the declared target says less than what landed. `--fetch` (live pages) is
correctly kept outside the statement. I did not run `--fetch`; other seats own it.

Smallest safe correction: none to the landed claim; the target must not be moved after landing. The
report states C2 as "declared floor 3; measured 5 of 7 @ `c8407a45`", and the lesson records the
floor-shaped after-state as a sizing slip.

## T1 — learning claim: HOLDS-BOUNDED as a claim; its content BREAKS (F1, HIGH)

C2 meets the quality bar's form: it adds a new knowledge entry
(`corpus/knowledge/mcp-server-instructions-round52.md`), a `SKILL.md` decision table
(`SKILL.md:86-95`), and moves a Frontier item to Core (`PROVINCE.md:19`). The counted statement
(5 of 7 at least 3) holds. The defects are in what the entry and the table teach.

### F1a — both "silent" clients document server instructions on hosts the counter pins

The entry (`:29-37`) and the lesson (`corpus/lessons/round-52.md:47-54`) record opencode and Copilot
CLI as not counted because their pages contain no statement about server instructions. The lesson
gives the flip condition (`:49-50`): "Flip: a docs statement, or a read of opencode's MCP client
source showing where the text goes." Both clients have such a statement on a host listed in the
counter's `HOSTS` (`verifiers/check_mcp_instructions.py:84-89`), and both were published before the
sweep (17:05:56Z and 17:05:54Z on 2026-10-22).

**opencode.** The sweep opened a docs path that has been dead since July. The live docs source in
the same repository says the opposite.

- Swept file, re-fetched: `https://raw.githubusercontent.com/anomalyco/opencode/cdf1c200a671378458b50f9e3167405f1f326b24/packages/web/src/content/docs/mcp-servers.mdx`,
  2026-10-22T17:52:13Z, HTTP 200, 14,015 B, sha256
  `ad6e6687ab4c8b535471ff176957fc7623b5f06230efc848b854c5c96acd70f5`. This matches the lesson's
  `ad6e6687ab4c`. Last commit touching that path: `58201a32c119` on 2026-07-13T02:23:59Z
  (`gh api 'repos/anomalyco/opencode/commits?path=packages/web/src/content/docs/mcp-servers.mdx&sha=dev'`).
- `https://opencode.ai/docs/mcp-servers.md`, 2026-10-22T17:52:13Z, 200, 13,941 B, sha256
  `12ed2af6c5f48701160ab6e1abe79fedbe293e55c5889c447be57ff79cd14de0` (matches the lesson's
  `12ed2af6c5f4`; 0 hits for `instructions`, confirmed).
- Live docs source: `https://raw.githubusercontent.com/anomalyco/opencode/cdf1c200a671378458b50f9e3167405f1f326b24/services/www/src/docs/content/mcp-servers.mdx`,
  2026-10-22T17:52:12Z, 200, 15,476 B, sha256
  `fd3b05ead1ecfde68181f90507cbb616f5cd3d5fa360494b4e261e4b9f3627a2`. The same sha256 is served at
  `d0732eadf883bdc64c0b0ea91e9c4ee0fe51d8c3` (fetched 17:52:40Z), the last commit touching the path
  (2026-10-15T18:54:15Z). So these bytes were live a week before the sweep. Verbatim:
  - line 427: `## Server instructions`
  - line 429: `When a server returns instructions during initialization, OpenCode adds them to the system prompt:`
    (14 words, contains `instructions`)
  - lines 432-436: a `<mcp_instructions>` / `<server name="sentry">` example block
  - line 441: `A server's instructions are omitted when the agent's permissions deny every one of its tools, or when they deny `execute` for a server that uses Code Mode.`
- Source, same commit: `https://raw.githubusercontent.com/anomalyco/opencode/cdf1c200a671378458b50f9e3167405f1f326b24/packages/core/src/mcp/instructions.ts`,
  17:52:12Z, 200, 4,803 B, sha256 `13a166ca02c13aa6b14e6545676400efe542804ce76b81f26ec4d4e6788c7070`.
  Lines 28-29: `const render = (servers: ReadonlyArray<Summary>) =>` /
  `  ["<mcp_instructions>", ...entries(servers), "</mcp_instructions>"].join("\n")`.
- The repository moved: `gh api repos/sst/opencode --jq .full_name` → `anomalyco/opencode`. The
  round-8 raw path `https://raw.githubusercontent.com/sst/opencode/dev/packages/opencode/src/session/prompt.ts`
  returned 404 (14 B) at 17:51:50Z.

**Copilot CLI.** Its own changelog documents support and an opt-in flag.

- `https://raw.githubusercontent.com/github/copilot-cli/7ea98dfc33c68aaf6443ea8fc054e20ff7fcd120/changelog.md`,
  2026-10-22T17:54:37Z, 200, 289,859 B, sha256
  `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb`. Verbatim:
  - line 2893 `## 0.0.400 - 2026-01-30`, line 2895 `- Add MCP server instructions support`
  - line 1063 `## 1.0.66 - 2026-06-30`, line 1157 `- Add --allow-all-mcp-server-instructions to optionally include instructions from all MCP servers in system prompts`
  - line 195 `## 1.0.92 - 2026-10-05`, line 219 `- MCP tools recover within the same turn when server instructions change`
- [INFERENCE] Line 1157 suggests that by default Copilot CLI puts instructions from only some servers
  into the system prompt. That would be a stronger, located basis for "do not rely on it everywhere"
  than page silence. I did not verify the default set.

### F1b — the `SKILL.md` decision row rests on that false negative

`SKILL.md:94`: `| needed on every client | a skill or always-on file too | the opencode and Copilot CLI
pages opened on 2026-10-22 say nothing about server instructions (entry § sweep) |`. The advice may
still be right, since the spec makes the field optional (S032), but the "why" given is contradicted
by both clients' own documents. The entry's craft point 3 (`:47-48`) says "two of the seven clients
checked here document nothing about it". It is literally bounded to the pages opened (`:36-37`), but
it is wrong as a statement about the clients. The uncommitted `SCORECARD.md` coverage row repeats it:
"opencode and Copilot CLI pages opened and silent (sweep)".

### F1c — the entry misstates the lane's own prior knowledge

The entry, lines 8-10: "Round 13 … found the MCP configuration keys absent … it did not record what
text an MCP server puts in front of the model." But:

- `corpus/knowledge/instruction-surface-census-round13.md:283`: "opencode non-file prompt surfaces:
  MCP server instructions (`<mcp_instructions>`), … | doc | they reach the prompt but are **not file
  classes**".
- `corpus/knowledge/opencode-offer-trace-round8.md:162-163` (committed `8c300ad`, 2026-09-28),
  upstream read: "`const system = [...env, ...instructions, ...(mcpInstructions?[mcpInstructions]:[]),
  ...(skills?[skills]:[])]`".

So the lane already held, as admitted knowledge, that opencode puts MCP server instructions into the
system prompt. The round-52 entry's novelty sentence and its opencode record both contradict that.
These are hidden-regression and false-provenance defects in the learning content.

Impacted axes: coverage (C2's content), depth (the `SKILL.md` row), calibration (the Q14 silence
record and the novelty sentence).

What F1 does not break: the declared count. The frozen counter prints 5 of 7 at `c8407a45`, which is
at least 3. [INFERENCE] Rows for opencode (`mcp-servers.mdx:429`, 14 words) and Copilot CLI
(`changelog.md:2895`, 5 words) appear to meet the counter's quote, length and host rules, which
would raise the count at a later head. That would be in-round content under a frozen counter, not a
widening. The report should still state the `c8407a45` value and any later-head value separately.

Smallest safe correction (the L1 makes it; this seat edits nothing):
1. In the entry § Not counted and in the lesson § Gate, append a correction (appended, not rewritten)
   giving the two located statements above, with their URLs, commits, byte counts and sha256. Either
   open them as `corpus/SOURCES.md` rows or record why not.
2. Rewrite the "why" cell of `SKILL.md:94` so it no longer rests on silence. For example: the spec
   makes the field optional (S032), and Copilot CLI includes all servers' instructions only with
   `--allow-all-mcp-server-instructions` (once that row is opened and the default is checked).
3. Correct entry lines 8-10 to cite census round 13 `:283` and the round-8 trace `:162-163`.
4. Fix the uncommitted `SCORECARD.md` coverage-row phrase "opened and silent" to match.

## T5 — universal clauses

- Claim statements HOLD. C1's "every historical registration callee" (`plans/round-52.md:28`) is
  enumerated: "the 19 historical registration callees (BASE_CALLEES)"
  (`verifiers/check_callee_rename.py:21-22, :74`). C2's statement has no universal clause. The plan's
  no-harm guards name specific commands and values (`plans/round-52.md:34-37`), not "no harm
  anywhere".
- Landed text: `SKILL.md:94` "needed on every client" is a universal craft row resting on a
  two-client silence that is false (counted under F1).
- **F5 (LOW)**: the uncommitted `SCORECARD.md` freshness row leads with "C1 — omp extraction survives
  a callee rename". It drops the statement's "pure" and "on the 4 pinned omp fixtures" bounds; the
  body bounds only "a change of call shape". The round-53 block repeats "omp extraction callee-rename
  robust". This is the T2b class again. `PROVINCE.md:20` carries "4 of 4 fixtures" and is fine.
  Correction: lead with "on the 4 pinned fixtures, a pure rename of the 19 historical callees".

## F4 — uncommitted `SCORECARD.md`: one sentence not supported by any evidence (MEDIUM)

Source: `git -C … diff --no-ext-diff -- SCORECARD.md`, hunk `@@ -125,6 +125,10 @@`: "**Round 52
completed (hyaku campaign, attempt 1):** … The build wave never ran … the L1 did the build work; the
falsify wave ran on live roles only."

- `.ufo/waves/round-52/falsify/` contains only `swarm-registry.json` (36 members, `createdAt`
  `2026-10-22T17:12:35.908Z`, never updated). `.ufo/waves/round-52/falsify-gate.txt` is 0 B, with no
  grant line. `.ufo/watchdog.log:724` records the omp process restart at 17:26Z with "no landed
  report". No attempt-1 falsify seat report exists in the lane. So "the falsify wave ran" is
  unsupported. [INFERENCE] The empty gate file suggests the wave was never granted.
- The heading "Round 52 completed (hyaku campaign, attempt 1)" is stale. Attempt 2 is running, and
  its carried build items (fixture labels, S024 row) have not landed.

Correction: before committing, rewrite the block for attempt 2. Say that the attempt-1 falsify wave
left no seat reports, and name the attempt-2 waves and their counts.

## F6 — round shape (LOW, recorded honestly by the lane)

- Build wave: 34 seats validated (`build-taskcall-sent.json`, 34 tasks) but never granted
  (`build-gate.txt` 0 B; lesson M37 `corpus/lessons/round-52.md:11`). C1 and C2 therefore landed
  without the pre-landing sizing critics that re-sized both claims in rounds 50 and 51
  (`plans/round-50.md:66-86`, `plans/round-51.md:71-102`). F3 (the floor-shaped target) is the kind of
  defect those critics caught before.
- Attempt-2 wave: `falsify-a2-spec.json` has 34 items (scout 10, reviewer 9, critic 7,
  mutation-tester 3, executor 3, connector 1, scribe 1), granted at
  `seats=34 live=50 pending=0 cap=85` (`falsify-a2-gate.txt`). Attack roles (reviewer, critic,
  mutation-tester) are 19 of 34 (56%), at least the 25% the quality bar asks for (goal `:160-161`).
  It sits inside the v1 band (32-64). Executors carry code items and the scribe carries the S024 prose
  row, as the routing rule asks.
- The total stays within 100 even if the 36 attempt-1 falsify tasks count as dispatched (36 + 34 = 70).

## Commands run (all exit codes observed)

- `git -C <lane> rev-parse master` → `c8407a45…` (exit 0)
- `git -C <lane> diff --no-ext-diff -- SCORECARD.md > /fast/scratch/hyaku/kotoba-r52a2/CriticLearning-scorecard.diff` (exit 0)
- `git clone -q <lane> /fast/scratch/hyaku/kotoba-r52a2/CriticLearning && git -C … checkout -q c8407a45…` (exit 0)
- the C1 and C2 counter runs above (exits as shown)
- `gh api` commit-history and code-search calls for `anomalyco/opencode` and `github/copilot-cli` (exit 0)
- `curl` fetches listed in F1a (each HTTP status, byte count and sha256 recorded)
