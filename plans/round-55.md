# Plan — round 55 (hyaku campaign, attempt 1)

Base: branch `master` at `f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c` (round 54 admitted; spot-check
`corpus/lessons/round-54-verifier-spotcheck.md`). Shape: default, two v1 waves (build, then falsify). The L1
holds the planner seat; a bounded planning data-walk rides one scout item. Before-values below were run by the
L1 on the lane checkout and a sandbox clone at `f0e5de82`; each run's printed `date -u` line is pasted, not typed
(round-54 M46). Both counters are committed in this plan commit, before any content they score (Q28), together
with the do-nothing and shortcut control receipts (addendum §9): `.ufo/waves/round-55/controls/`.

Axis scores at base (`SCORECARD.md` § axes @ `f0e5de82`): depth 9, consistency 10, coverage 8.5,
operability 8.5, freshness 8, calibration 8.5, adjacency 8.0. Owned axes: depth + consistency; the lowest
owned axis is depth (9), and C1 works it. Session bindings: no freshness claim; nothing on
`verifiers/verify_surfaces.py`; `SKILL.md` is at 599 of 600 lines, so any added table replaces or compresses
existing text, and the change is logged.

## Claims — one frozen predicate each (plan sentence = counter condition = receipt label)

**C1 — depth (lowest owned axis; the learning claim; the sourced claim). Surface: a new `SKILL.md` decision
table `### Explicit invocation by client`, grounded in a new entry
`corpus/knowledge/explicit-invocation-round55.md` and new SOURCES rows.** It works the Frontier row
*Implicit-intent fidelity* (`corpus/README.md` § Frontier): an implicit-trigger measure has to set aside the
turns where the user invoked a skill by name, and that needs each client's documented explicit form.

Predicate (frozen): `python3 -B verifiers/check_explicit_invocation.py --rev <rev> --fetch` exits 0, which it
does iff it prints `explicit invocation forms found on the live page F of K; new ground G` with F ≥ 4 and G ≥ 2.
Receipt label: `C1 predicate: --fetch exit 0 (F>=4, G>=2)`.

Rules (counter docstring): a client (Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, opencode)
is backed when the SKILL.md row's form cell holds a backticked invocation token (`/…`, `$…`, `@…`, `#…`, or a
tool name with `_`), its action cell is non-empty, and the entry row quotes that token verbatim in 3–25 words
from a tier-A `mined` SOURCES row opened 2026-10-22 or 2026-10-23 on a pinned host, which is not a row at
`f0e5de82` and whose quote is recorded in `corpus/lessons/round-55.md` § Gate. `--fetch` then requires the quote
on the live page. New ground counts found clients whose token occurs 0 times in `SKILL.md` and in every
`corpus/knowledge/*.md` at `f0e5de82`.

Before at `f0e5de82` (`date -u` 2026-10-22T23:07:26Z, receipt `.ufo/waves/round-55/controls/C1-base.txt`, on the
committed counter bytes): `explicit invocation forms found on the live page 0 of 0; new ground 0`, exit 1.

What the counter does not measure (Q31): whether a form is explicit invocation rather than a listing or
management command (entry and reviewer reading); whether clients behave as documented; any client outside the
seven.

**C2 — operability. Surface: the could-not-evaluate error paths of thirteen registered gates under
`verifiers/`** (each registered in `SKILL.md` § Gate registry with `2=could-not-evaluate`; round-54 falsify
reports `.ufo/waves/round-54/falsify/W2Row*.md`; SCORECARD `Next: round 55`).

Predicate (frozen): `python3 -B verifiers/check_could_not_evaluate.py --rev <rev>` exits 0, which it does iff it
prints `could-not-evaluate probes honoured 25 of 25; controls held 13 of 13`. Receipt label:
`C2 predicate: exit 0 (25 of 25, 13 of 13)`.

Rules (counter docstring): in a fresh temporary clone at `<rev>`, each gate gets a random 40-hex revision the
counter makes at run time (12 class-R probes) and runs with `git` absent from PATH (13 class-G probes); a probe is
honoured iff it exits exactly 2. A gate's controls hold iff its own `--self-test` exits 0 and a run on the real
revision exits 0 or 1. Trust boundary (Q33): the counter runs the measured revision's own gates; guards outside
it are the wave-2 diff-scope review of each changed gate (judging lines unchanged) and the random revision the
counter makes itself.

Before at `f0e5de82` (`date -u` 2026-10-22T23:07:53Z–23:10:42Z, receipt `.ufo/waves/round-55/controls/C2-base.txt`):
`could-not-evaluate probes honoured 13 of 25; controls held 13 of 13`, exit 1. The twelve misses: R and G on
`box_proof_case_deletion.py` and `check_mcp_instructions.py`; R (both arguments) and G on
`check_gate_finding_delta.py`; R on `check_overlap_levers.py` and `check_description_thresholds.py`; G on
`check_correction_sweep.py`, `check_assertion_floors.py` and `verify_corpus_independent.py`.

Causal separability: C1 changes `SKILL.md` (one new table), one new entry, `corpus/SOURCES.md` and the lesson
Gate; its counter reads only those files. C2 changes the error paths of gate scripts under `verifiers/`; its
counter reads only the exit codes those scripts produce. Neither counter reads the other's surface.

## Controls (addendum §9; committed with this plan, before data)

- C1 do-nothing: the base `f0e5de82` → exit 1 (above; receipt `controls/C1-base.txt`).
- C1 shortcut keyed on labels: a sandbox commit on `f0e5de82` that adds the table, entry, SOURCES rows and Gate
  quotes with fabricated quotes holding each client's token (receipt `controls/C1-shortcut.txt`). Without
  `--fetch` it reaches `backed 7 of 7`, which is why the predicate is the `--fetch` form; with `--fetch` it must
  exit 1.
- C2 do-nothing: the base `f0e5de82` → exit 1 (receipt `controls/C2-base.txt`).
- C2 shortcut keyed on labels: a sandbox commit on `f0e5de82` where each of the thirteen gates exits 2 unless
  `--self-test` is in its arguments (receipt `controls/C2-shortcut.txt`): all 25 probes are honoured, and the
  real-verdict control must drop `controls held` below 13, exit 1.

A miss under either predicate is reported as a miss; no predicate, target or table in the counters changes after
this commit.

## Frontier step and routed defects (not claims)

- Sources: rows opened this round for the C1 clients; census before/after.
- Mistake: mined into `corpus/lessons/round-55.md` § Mistakes (candidate: round-54 routed defect 1, receipts
  attributed to a revision they did not measure).
- Round-54 spot-check routed defects: (1) tip runs committed with the revision measured; (2) QUALITY criteria
  for M45 and M47; (3) the four over-wide C1 cells narrowed; (4) the reject-1 route move recorded; (5) the
  registry counter's probe route and substring flag test closed, with a control receipt; (6)
  `fault_injection_corpus.sh` repaired or its row annotated; (7) minor quote notes; (8) carried items named.
  The 12 earlier SOURCES protected-cell changes go to one L0 line.

## Erratum 1 (append-only; on wave-1 critic `CriticC1Sizing`, before any C1 content is committed or scored)

- The v1 C1 counter frozen at `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0` is met by a shortcut the plan's control
  did not try: the critic's world W1 (sandbox commit `04869b82`) quotes real text on pinned hosts that holds no
  invocation form (`/compact`, `@layer` from CSS, `#file:`, `/skills list`, link paths) and prints `found on the
  live page 7 of 7; new ground 7`, exit 0; world W3 (`09053321`) re-scores held `$skill` as new ground by a case
  flip (`.ufo/waves/round-55/build/CriticC1Sizing.md`). Under addendum §9 the counter is wrong and is fixed before
  data: no C1 content exists in any commit, and no seat has scored C1 content on any counter (the source seats
  ran only `--self-test`; the L1 had read their draft rows, which is why every v2 rule only adds a failure).
- v2 (this commit; rules in the counter's docstring § ERRATUM v2) is strictly stricter than v1: user-typed tokens
  only (one segment after `/`, `$` or `@`; no tool names, `#`, spaces, dots or paths), client built-in and
  listing commands excluded, the quote must contain the word `skill`, style/script/comment blocks dropped from the
  live page, and new ground counted per distinct case-folded token whose row URL is not a base row.
- The C1 predicate is now: `python3 -B verifiers/check_explicit_invocation.py --rev <rev> --fetch` exits 0, which
  it does iff it prints `user-typed invocation forms found on the live page F of K; new ground G` with F ≥ 4 and
  G ≥ 2. Receipt label: `C1 predicate (v2): --fetch exit 0 (F>=4, G>=2)`. The v1 line is reported beside it,
  never in its place.
- Receipts, committed here: `controls/C1-shortcut-W1W3.txt` (W1 and W3 under v1 → met, under v2 → `0 of 0`,
  exit 1 and `3 of 3; new ground 1`, exit 1); `controls/C1-v2-controls.txt` (base → `0 of 0`, exit 1; the
  fabricated-quote control → `0 of 6`, exit 1).
- Consequence for the C1 rows: Gemini CLI's documented form is the model's `activate_skill` tool call, which v2
  does not count; it stays in the table as a non-counted row.
