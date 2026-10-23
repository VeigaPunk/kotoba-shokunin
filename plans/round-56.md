# Plan — round 56 (hyaku campaign, attempt 1)

Base: branch `master` at `b0b7140b5a7cf8a50f13989ee6285fc8ee245c41` (round 55 rejected as an honest stop; spot-check
`corpus/lessons/round-55-verifier-spotcheck.md`). Shape: default, two v1 waves (build, then falsify), preceded by a
counter-writing call (2 executor seats) and the pre-freeze control call (critic and mutation-tester seats) that the
phase-4 rule requires before any data seat. The L1 holds the planner seat. Both counters are committed in this plan
commit, before any content they score; the control receipts are committed before the build wave is dispatched.

Axis scores at base (`SCORECARD.md` § axes @ `b0b7140b`): depth 9, consistency 10, coverage 8.5, operability 8.5,
freshness 8, calibration 8.5, adjacency 8.0. The lowest owned axis is depth (9); C1 works it. Anti-loop (session note):
rounds 53–55 worked skill-listing surfaces (always-on files, description thresholds, explicit invocation); this round
moves to a different frontier surface, **agent-definition files** — the subagent and custom-agent definition files
that clients load, whose checklist (`SKILL.md` § Agent-definition fidelity checklist) is opencode-only and has no
executed box (`verifiers/checklist-baseline.json`: agentdef.01–.09 all `unexecuted:`; Frontier row *Executed checklist
coverage*, "the agent-definition … checklists have no executed or delegated box").

## Claims — one frozen predicate each (plan sentence = counter condition = receipt label)

**C1 — depth (lowest owned axis; the learning claim; the sourced claim). Surface: a new `SKILL.md` decision table
`### Agent-definition files by client`, grounded in a new entry `corpus/knowledge/agent-definition-files-round56.md`
and new SOURCES rows.** It states, per client, where its agent-definition files live and what such a file sets, so the
opencode-only checklist below it can be applied to the right file on the other six clients.

Predicate (frozen): `python3 -B verifiers/check_agent_definitions.py --rev <rev> --fetch` exits 0, which it does iff it
prints `agent-definition locations found on the live page F of K; new ground G` with F ≥ 5 and G ≥ 2.
Receipt label: `C1 predicate: --fetch exit 0 (F>=5, G>=2)`.

Rules (counter docstring, summarised): a client (Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor,
opencode) is backed when its one SKILL.md row's location cell holds a backticked dot-directory path with an `agent` or
`agents` segment and its action cell holds at least 3 words, and the entry row quotes that path verbatim in 3–25 words
that also say `agent`/`subagent` outside the path, from a tier-A `mined` SOURCES row opened 2026-10-22 or 2026-10-23 on
the client's pinned host, which is neither a row at `b0b7140b` nor a re-citation of a base row's URL (`.md` suffix,
slash, query and fragment ignored), and whose quote is recorded in `corpus/lessons/round-56.md` § Gate. `--fetch` then
requires the quote on the live page and the path at a word boundary there (never inside a URL). **New ground** counts
DISTINCT normalised paths (lowercase, no `~/`, cut after the first `agent(s)` segment) among found clients whose
case-insensitive count in the whole base tree outside `.ufo/` is 0 — forms, not example names, against all base text,
which is the fix round-55 routed defect 2 asks for. At base, `.claude/agents`, `.codex/agents` and `.opencode/agent(s)`
are held; S026 already cites Claude Code's sub-agents page, so a Claude Code row can stay in the table but cannot count.

Before at `b0b7140b`: receipt `.ufo/waves/round-56/controls/C1-base.txt` (committed with this plan): `agent-definition
locations found on the live page 0 of 0; new ground 0`, exit 1; counter sha256 `1b0aadba…`, `--self-test` 0 failures
over 86 assertions.

What the counter does not measure (Q31): whether the client loads the file as documented; whether the "What the file
sets" cell is complete or right (reviewer reading in the falsify wave); clients outside the seven.

**C2 — operability. Surface: the agent-definition checklist's execution — a new delegate instrument
`verifiers/verify_agentdef.py` and the map dispositions of agentdef boxes in `verifiers/checklist-baseline.json`.**

Predicate (frozen): `python3 -B verifiers/check_agentdef_boxes.py --rev <rev>` exits 0, which it does iff it prints
`agent-definition boxes executed and discriminating N of T` with N ≥ 3. Receipt label: `C2 predicate: exit 0 (N>=3)`.

Rules (counter docstring): a box counts iff its map disposition is `delegated:<repo-relative path>` that exists in the
revision, its `text_sha256` equals the base map's (the box was not reworded), no `verifiers/*.py` in the revision
shadows a standard-library module, and on every case the counter generates at run time (random stems, names, words and
dates; at least 4 PASS and 4 FAIL per box, each box with a hard negative) the delegate, run with `python3 -B -P` from an
empty directory under `PYTHONSAFEPATH=1`, exits 0 with status PASS or 1 with status FAIL as the case expects. Case
generators exist for agentdef.01, .02, .05, .06 and .07; the other four boxes cannot count. The counter's docstring
states the operational reading of each box; that reading is the rule the instrument is judged by.

Before at `b0b7140b`: receipt `.ufo/waves/round-56/controls/C2-base.txt` (committed with this plan): `agent-definition
boxes executed and discriminating 0 of 9`, exit 1; counter sha256 `8aeb9bcf…`, `--self-test` 0 failures over 109 assertions.

Disclosure: the counter's author seat (`w0/KotobaR56.ExecCounterC2AgentdefBoxes.md`) proved the generators satisfiable with a
reference delegate inside the self-test and an independent instrument in its scratch dir (5 of 9). Neither is lane
content; the build-wave executor writes `verifiers/verify_agentdef.py` without reading that scratch dir, and the C2
after-value is measured only on the lane's own delegate.

Trust boundary (Q33): the counter runs the measured revision's delegate, but on cases it makes itself at run time and
under an isolated interpreter; guards outside it are the falsify-wave diff review of the delegate and an independent
run of the delegate on the live `~/.config/opencode/agents/` files.

Causal separability: C1 changes one new SKILL.md table, one new entry, `corpus/SOURCES.md` and the lesson Gate; its
counter reads only those. C2 changes `verifiers/verify_agentdef.py` and map dispositions; its counter reads the map,
the agentdef box texts' hashes and the delegate's exit codes. The SKILL.md line-budget move that makes room for C1's
table must not touch the nine agentdef box texts (C2's sha guard would see it).

## Controls (addendum §9 and the phase-4 pre-freeze control wave; before data)

- C1 do-nothing: base `b0b7140b` (receipt `controls/C1-base.txt`).
- C2 do-nothing: base `b0b7140b` (receipt `controls/C2-base.txt`).
- The control call after this commit: fresh critic and mutation-tester seats build, in sandbox clones, the
  do-nothing, junk, all-false, no-reader and id/label-keyed shortcut controls for each claim (C1: fabricated quotes,
  real text with no agent-definition path, held paths in case/prefix/glob variants, URL-embedded paths, off-host rows,
  re-cited base URLs; C2: constant PASS/FAIL, no-reader, exit remap, stdlib shadow, a delegate keyed on file names or
  sizes or on the generators' word pools, a reworded box) and score them with these frozen counters. Their receipts are
  committed under `.ufo/waves/round-56/controls/` before the build wave. A claim whose counter any control meets is
  redesigned before data or declared exploratory.

A miss under either predicate is reported as a miss; no predicate, target or rule in the counters changes after this
commit except by an erratum committed before any seat scores claim content.

## Frontier step and routed defects (not claims)

- Sources: rows opened this round for the C1 clients; census before (`census-start.txt`, 01:18:56Z, exit 0, 71 rows,
  7 × W04) and after.
- Mistake: mined into `corpus/lessons/round-56.md` § Mistakes (candidate: round-55 C1 counter counted example names
  as new ground, routed defect 2; the fix is this round's new-ground rule, shown able to fail by a held-variant
  control).
- Round-55 spot-check routed defects: (1) commit `.ufo/waves/round-55/falsify/ReviewLessonMistakes.md` under a
  correction entry and record its two calibration findings; (2) `check_explicit_invocation.py` new ground counts
  distinct forms against all base text (correction receipt at `b0b7140b`, never a re-claim); (3) close the round-55 C2
  counter's three shortcuts (remap, entry preflight, argparse shadow) with a control receipt; no C2 re-claim this
  round; (4) `check_assertion_floors.py` nested-timeout exit 2 under load; (5) the two diagnostic defects (refusing-git
  revision message; floors preflight returncode); (6) the S065 census W04 reported and its scope reasoned; (7) the
  report's cross-domain evidence item.
