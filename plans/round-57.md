# Plan — round 57 (hyaku campaign, attempt 1)

Base: branch `master` at `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a` (round 56 admitted; spot-check
`corpus/lessons/round-56-verifier-spotcheck.md`). Shape: default, two v1 waves (build, then falsify), preceded by a
counter-writing call (2 executor seats, `w0`) and the pre-freeze control call (critic and mutation-tester seats) that
the phase-4 rule requires before any data seat. The L1 holds the planner seat. Both counters are committed in this
plan commit, before any content they score; the control receipts are committed before the build wave is dispatched.
Every counter version a control scores is committed before that control's receipt is cited (round-56 R3).

Axis scores at base (`SCORECARD.md` § axes @ `47c05558`): depth 9, consistency 10, coverage 8.5, operability 8.5,
freshness 8, calibration 8.5, adjacency 8.0. Lowest-axis duty: this round uses the **owned-axes reading** (the open
L0 question `kotoba | round-55 |` is the operator's); the lowest owned axis is depth (9) and C1 works it. Under the
all-axes reading the lowest are freshness 8 and adjacency 8.0, which neither claim works; the report says so.

Anti-loop (session note): rounds 53–56 worked skill-listing and agent-definition surfaces. This round works two
Frontier rows untouched by them: **MCP/plugin instruction surfaces** (its plugin half: `corpus/README.md:102` and the
round-52 note "still not held: plugin surfaces") for C1, and **Command extraction** (`corpus/README.md:100`,
untouched since round 46) for C2. Base held ground for plugin manifests is empty: `git grep -F -o <t> 47c05558 -- .
':!.ufo' | wc -l` is 0 for `.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, `gemini-extension.json`,
`plugin.json`, `.opencode/plugin`, `.opencode/plugins`, `.github/plugin`, `marketplace.json` (case-sensitive and
case-folded alike, 2026-10-23T03:56Z).

## Claims — one frozen predicate each (plan sentence = counter condition = receipt label)

**C1 — depth (lowest owned axis; the learning claim; the sourced claim). Surface: a new `SKILL.md` decision table
`### Plugin manifests by client`, grounded in a new entry `corpus/knowledge/plugin-manifests-round57.md` and new
SOURCES rows opened 2026-10-23.** Per client it states where the plugin (or extension) manifest lives and which
instruction-bearing parts a plugin can ship (skills, agents, commands, context files, MCP servers), so a reader
auditing a skill or rule file knows when it arrives inside a plugin rather than from the project tree.

Predicate (frozen): `python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch` exits 0, which it does iff it
prints `plugin manifests found on the live page F of K; new ground G` with F ≥ 5 and G ≥ 3.
Receipt label: `C1 predicate: --fetch exit 0 (F>=5, G>=3)`.

Rules: the counter docstring is the rule (adapted from the round-56 v1.3 counter). Differences from v1.3: the token is
the first backticked span of the `Plugin manifest` cell and must carry a `plugin(s)`/`extension(s)` word in a path
segment and no `marketplace` segment; a token naming another client (`claude`, `codex`, `vscode`, `copilot`,
`gemini`, `cursor`, `opencode`) is rejected for that client; the quote must say `plugin(s)`/`extension(s)` outside
the token; **held ground is counted case-sensitively at path-segment boundaries** (round-56 spot-check R4); the
self-test carries a must-fail arm for every guard (R5), shown by the w0 seat's guard-mutation table.

What the counter does not measure (Q31): whether a client loads a plugin as documented; whether the `What a plugin
can ship` cell is complete or right (reviewer reading in the falsify wave); clients outside the seven.

**C2 — operability. Surface: the checklist gate's command extraction over info-less fences —
`verifiers/verify_skill_checklist.py` check `trigger.command_binary_resolves` (box "Every command named resolves").**
Today every line of a fence with no info string is read as shell, so tables, diagrams and `key: value` output in such
a fence FAIL as missing commands (live: kasegi `SKILL.md:39`, tameshi `SKILL.md:255`, tsukuroi `SKILL.md:263`, read
by this round's L1 at 03:57Z). The change must stop those false FAILs while a real missing command in an info-less
fence, in a pipeline, after a table, or with a colon in an argument still FAILs.

Predicate (frozen): `python3 -B verifiers/check_infoless_fences.py --rev <rev>` exits 0, which it does iff it prints
`info-less fence cases correct N of T (…)` with N = T and T ≥ 120 (seeds 11, 22, 33; ten classes × 4 cases per seed;
cases generated at run time with random names and tokens, shuffled, one directory per case; the measured revision's
`verifiers/` tree is extracted and run, never the working tree). Receipt label: `C2 predicate: exit 0 (N=T, T>=120)`.

What the counter does not measure (Q31): commands outside the declared vocabulary used inline (the other half of the
Frontier row); arrow forms other than U+2192; any fence shape outside the ten classes. Trust boundary (Q33): it runs
the measured revision's instrument, on inputs it makes itself; guards outside it are the falsify-wave diff review,
the instrument's own `--self-test` (must stay 0 failures) and the live run on the lane's own `SKILL.md` (output must
stay byte-identical).

Causal separability: C1 changes one new SKILL.md table, one new entry, `corpus/SOURCES.md` and the lesson Gate; C2
changes `verifiers/verify_skill_checklist.py` and its fixtures/floors. C2's counter reads only generated cases, so
C1's content cannot move it; C1's counter reads no verifier output, so C2 cannot move it.

## Pre-freeze controls (committed before the build wave)

Each control runs the counter committed in this plan commit, on a sandbox world, and its receipt is committed under
`.ufo/waves/round-57/controls/`. A claim whose predicate any control meets is redesigned before data (a stricter
erratum, committed before any content) or withdrawn.

- C1: do-nothing (base), junk table (well-formed rows, no sources), fabricated rows/quotes (sources on pinned hosts
  that do not hold the quote), held-variant (re-cited base URLs, case variants of tokens), real-no-form (real plugin
  pages quoting a `marketplace` file or a foreign client's manifest), keyed-labels (rows keyed on the counter's labels
  with no live source).
- C2: do-nothing (base instrument), skip-every-info-less-fence, skip-lines-containing-`|`/`:`/`→`/box chars,
  always-FAIL, always-N/A, a delegate keyed on the generator (fixed seeds read from the counter) — each as a sandbox
  patch to the instrument, scored by the frozen counter.

## Routed defects from the round-56 spot-check (R1–R8)

R1 sandbox hashes are labelled in every wave context and in the report; R2 the S076/S078 quote notes and the
`SKILL.md:109` "singular `agent/`" clause are corrected; R3 every scored counter version is committed; R4 and R5 are
built into the C1 counter; R6 the stale `SKILL.md` § Sources opencode-agents line is marked at the line; R7 the
kill-by-PID and contention-cap bound is in `.ufo/waves/round-57/bounds.md`, included in every wave context, and shown
by a grep that fails on the round-56 build context; R8 (the agent-definition box counter redesign) is not worked:
anti-loop moves this round off the agent-definition surface; it stays carried.

## Before (receipts committed with this plan)

- C1 at `47c05558`: `.ufo/waves/round-57/controls/C1-base.txt` — `plugin manifests found on the live page 0 of 0; new
  ground 0`, exit 1; counter sha256 `2ac51d2a2f50d855…`, `--self-test` 0 failures over 184 assertions; author seat
  guard-mutation table 54 killed, 0 survived (`w0/ExecCounterC1.md`).
- C2 at `47c05558`: `.ufo/waves/round-57/controls/C2-base.txt` — `info-less fence cases correct 48 of 120 (pass-expected
  0 of 60; hard negatives 48 of 60)`, exit 1; counter sha256 `b3dbe72fd9383b6d…`, instrument sha256 `629867d1…`,
  `--self-test` 0 failures over 105 assertions; 34 guard mutants killed, 0 survived (`w0/ExecCounterC2.md`). The 12 H3
  misses at base are the instrument's four-item detail cap hiding the bogus head behind the table cells' failures;
  the rule is kept (stricter), not relaxed.
- Gate registry: both counters get a `SKILL.md` § Gate registry row in this commit (Q35); `SKILL.md` 598 of 600 lines.
