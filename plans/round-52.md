# Plan — round 52 (hyaku campaign, attempt 1)

Base: branch `master` at `c8579a4c5b48789e56fb9060ddd48f33569e1215` (round 51 closed
`rejected-honest-stop`; spot-check `corpus/lessons/round-51-verifier-spotcheck.md`). Shape: default,
two v1 waves (build, then falsify). The L1 holds the planner seat; no swarm planner item. Every
before-value below was measured by the L1 at round start, 2026-10-22T15:56Z, on the lane checkout at
`c8579a4c` (Q19). Both counters are committed in the plan commit, before any content they score
(Q28); their judgment tables are frozen there and are never widened this round.

Axis scores at base (`SCORECARD.md` § axes @ `c8579a4c`): depth 9, consistency 10, coverage 8.5,
operability 8.5, freshness 8, calibration 8.5, adjacency 8.0. Lowest non-retired: freshness and
adjacency, tied at 8. Adjacency was claimed in rounds 49 and 50, so C1 works freshness.

The round-51 C2 claim (overlap levers by client) is not re-declared: its surface (sibling and
overlap arbitration) has carried a claim in rounds 49, 50 and 51, and the drift sentinel asks for a
different frontier area. C2 below works a different frontier item.

## Claims (each statement is exactly what its counter prints)

**C1 — freshness (lowest non-retired axis, 8).**
Statement: the omp loader-registration extraction in `verifiers/verify_surfaces.py` survives a pure
callee rename on the 4 pinned omp fixtures: `callee-rename robust 0 of 4 fixtures` → `4 of 4`.

Counter: `python3 -B verifiers/check_callee_rename.py --rev <rev>` (frozen here; fixtures read from
`c8579a4c`, never from the revision measured). Per fixture it runs the gate three times: the fixture
as committed must pass; the fixture with every historical registration callee renamed to a fresh
seeded name must still pass both `surfaces.literal_present` and `surfaces.no_uncovered_class` (so the
alias decoy `q(u, "evil", "EVIL.md")` must stay unextracted); and the renamed fixture plus one planted
call by a renamed real callee registering `("rnplant", "RNPLANT.md")` must FAIL
`surfaces.no_uncovered_class` naming `omp:rnplant/RNPLANT.md` (so a rule that keeps only declared
pairs cannot pass). `--seed N` changes the fresh names.
Before at `c8579a4c`: `callee-rename robust 0 of 4 fixtures`, exit 1 (each fixture: control exit 0,
renamed exit 1, planted exit 1). After: `4 of 4`, exit 0, also with `--seed 7` and `--seed 1234`.
No-harm guards (not part of the statement): `python3 -B verifiers/verify_surfaces.py --json` on the
installed omp 18.12.6 stays `pass 7`, exit 0; `--self-test` green with its tally not below the floor
in `verifiers/floors-registry.json` (`surfaces` 119); `python3 -B verifiers/check_substrate_pins.py`
stays `OK 3/3`.

**C2 — coverage (advisory, 8.5; the learning claim; the sourced claim).**
Statement: the new entry `corpus/knowledge/mcp-server-instructions-round52.md` records, for K of 7
pinned clients (MCP specification, Claude Code, VS Code, Codex, Gemini CLI, opencode, Copilot CLI), a
located quote of at most 25 words containing the word `instructions` from that client's own
documentation or source on a pinned host, citing a tier-A `mined` `corpus/SOURCES.md` row opened
2026-10-22 whose `used-by` names the entry, with the quote recorded in this round's Gate:
`mcp instructions backed 0 of 7 clients` → at least `3 of 7`.

Counter: `python3 -B verifiers/check_mcp_instructions.py --rev <rev>` (frozen here; clients, hosts,
required word, word limit and target pinned in the script). `--fetch` additionally re-opens each cited
page and requires the quote on the live bytes. Before at `c8579a4c`: `backed 0 of 7`, exit 1 (no
entry). After: at least 3, exit 0, and `--fetch` found at least 3.
What the counter does not measure: whether the quote says what the entry's `reading` cell says. That
is checked by wave-2 reviewers re-opening each page and by the closure; the statement claims only what
the counter prints. Clients whose documentation is silent are recorded in the entry with the sweep
that found nothing (Q14) and do not count.
Learning content: the frontier item "MCP/plugin instruction surfaces" (`corpus/README.md` § Frontier,
`PROVINCE.md` § Frontier) gains held ground: where an MCP server's server-wide text goes in each
client, and the authoring rule that follows; `SKILL.md` gains a decision-table row grounded in the
entry.

Causal separability: C1 changes only `verifiers/verify_surfaces.py` (and its fixtures, self-test,
floor); C1's counter reads no C2 file. C2 changes the entry, `corpus/SOURCES.md`, the round-52 lesson,
`SKILL.md`; C2's counter reads no C1 file. Each verifies without the other.

## Routed defects from the round-51 spot-check (repairs, not claims)

1. `corpus/README.md:133-141` (Core note) still lists the pre-falsify lever set and an unqualified
   "7 of 7"; the index row (`:75`) omits `removed in a scope`. Append corrections in place of record.
2. `SCORECARD.md:28` depth cell opens with the widened-counter `7 of 7 @ 34cfffbb` and "six rows are
   new": rewrite the lead to the declared result (4 of 7 on the plan-commit counter, four new rows).
3. C2 of round 51 is not credited and not re-declared this round (above).
4. Carried items: superseding rows for S031 (`teaches` names `disabledSkills`, absent from the page)
   and S024 (narrow cell), each re-opened this round; labels for fixture lines 9, 15 and 33 of
   `verifiers/fixtures/surfaces/strings-omp-18.12.6.txt`; D2 F1–F5, D7, R1, R5 surveyed and carried
   with reasons unless a seat closes one.

## Frontier step

- SOURCES: new rows for every C2 source opened this round, plus the S031/S024 superseding rows.
  Census before at `c8579a4c`: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin
  kotoba` → exit 0 (W04 S018, S019, S021; `kotoba ok`).
- Mistake to mine (round 51): the corrections sweep missed `corpus/README.md:133-141` and the
  `SCORECARD.md:28` headline (routed defects 1–2). Fix shown able to fail: a committed sweep check
  that is red at `c8579a4c` on both places and green after the repairs.
- Sourced claim: C2.

## Waves

- Wave 1 build (v1, 32–40 seats): C1 implementation in a sandbox clone; fixture labels; C1 counter
  attacks with naive implementations; C2 source opening per client; C2 counter attacks; repairs;
  mistake fix; sibling-overlap scan.
- Wave 2 falsify (v1, 32–40 seats) only if wave 1 yields at least 32 distinct attack items;
  otherwise one residual call of at most 8 reviewer and critic seats.
