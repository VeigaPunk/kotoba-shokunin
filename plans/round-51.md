# Plan — round 51 (hyaku campaign, attempt 1)

Base: branch `master` at `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10` (round 50 admitted; spot-check
`corpus/lessons/round-50-verifier-spotcheck.md`). Shape: default, two v1 waves (build, then falsify).
The L1 holds the planner seat; no swarm planner item. Every before-value below was measured by the L1
at round start, 2026-10-22T14:09Z, on the lane checkout at `43ca0bfb` (Q19).

## Claims (each statement is exactly what its counter prints)

**C1 — freshness (lowest-scoring non-retired axis under the all-axes reading, 8.0, tied with
adjacency; adjacency was claimed in rounds 49 and 50, so this round works freshness).**
Statement: run against the installed omp 18.12.6 (`/home/vgpnk/.local/bin/omp`, sha256
`85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`), the instruction-surface gate
passes 5 of 7 checks → 7 of 7.

Counter: `python3 -B verifiers/verify_surfaces.py --json` → the `pass` field (and `exit_code`).
Before at `43ca0bfb`: `{'exit_code': 1, 'fail': 2, 'pass': 5}`; the two FAILs are
`surfaces.literal_present` (8 loader literals not verifiable) and `surfaces.no_uncovered_class`
(0 loader classes extracted from the omp dump; the baseline declares 8). After: `pass 7`, exit 0.
Companion measurement on the same axis (not a second claim): `python3 -B verifiers/check_substrate_pins.py`
→ `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime`, exit 1 → `OK 3/3`, exit 0.
Shown able to fail (Q25): the base run above is red on the same binary; the new 18.12.6 fixture arm
must fail with the round-50 callee allowlist and pass with the new one. Q09: the re-derivation
records version, sha256, mtime and the extraction rule change.

**C2 — depth (owned axis, lowest owned at 9; the learning claim; sourced claim).**
Statement: `SKILL.md` § Anti-patterns carries an "Overlap levers by client" table that names, for
K of 7 pinned clients (GitHub Copilot SDK, GitHub Copilot CLI, VS Code, Claude Code, opencode,
Gemini CLI, Codex), a documented lever other than description wording for stopping one of two
overlapping skills from being chosen; a client counts only when its row's key term appears verbatim
in the quote that the new entry `corpus/knowledge/skill-overlap-levers-round51.md` gives for that
client, citing a `mined` `corpus/SOURCES.md` row whose `used-by` names the entry: 0 of 7 → 7 of 7.

Counter: `python3 -B verifiers/check_overlap_levers.py --rev <rev>` → `overlap levers backed K of 7
clients` (the denominator is pinned in the script, never read from the revision measured). Before:
0 of 7 at `43ca0bfb` (no table; the round-50 error pattern names only "a more specific
description"). After: 7 of 7. `--fetch` additionally re-opens each cited page and checks each quote
on the live bytes. Shown able to fail: `--self-test` mutants (row removed, row unmined, `used-by`
missing, key term absent from the quote, key term about the description, duplicate client, table
absent).

This supersedes finding 4 of `corpus/knowledge/skill-selection-rules-round50.md` ("the documented
remedy for overlap is specificity in the description") with the wider documented set, and fixes the
`SKILL.md:375-377` sentence routed as D3.

## Routed defects from the round-50 spot-check (fixed or explained; not claims)

- D1: commit `.ufo/waves/round-50/build/DescDraft.md` byte-exact as wave evidence; disposition and the
  seat-accounting correction (both `DescDraft` and `D2D4Wording` wrote after being called cancelled)
  in this round's lesson and LOG; the leftover sweep runs after the last seat write.
- D2: bound the checklist-gate sentence (`SCORECARD.md:31`, `SKILL.md:135`): the gate reports PASS
  "not run" for a delegate whose `--help` probe times out, cannot exec or hides the flag.
- D3: `corpus/README.md:72` index row corrected; `SKILL.md:375-377` rewritten under C2.
- D4: appended correction of the round-50 reject reason for the Copilot SDK page; the page becomes a
  row because C2 cites it.
- D5: `PROVINCE.md:44` kama quote and citation; census line 273 kengaku `README.md:192`.
- D6: the precedence rule is marked provisional until the L0 answer, with the note that it was
  written after the three rows were known; it is not extended or relied on this round.
- D7: carried with reasons.

## Frontier step

Census before (exit 0, three W04 warnings) and after; new SOURCES rows for C2; one mined mistake into
`corpus/lessons/round-51.md`.

## Waves

- build (32–40 seats): `.ufo/waves/round-51/build-spec.json`.
- falsify (32–40 seats), only if build yields at least 32 distinct attack items.

## Re-sizing before landing (build-wave critics, 2026-10-22, before any landing)

No target value moved. Both statements were narrowed to what the counters turn on.

- **C1** (`.ufo/waves/round-51/build/CriticC1Sizing.md`, HOLDS-BOUNDED): five of the seven checks
  already pass at base and do not read the omp binary, so the real freshness move is the two omp
  checks, `surfaces.literal_present` and `surfaces.no_uncovered_class`, 0 of 2 → 2 of 2. Re-sized
  statement: `python3 -B verifiers/verify_surfaces.py --json`, run with no override flags
  (`--omp-strings`, `--omp-binary`, `--baseline`, `--inventory`, `--repo`), reads
  `/home/vgpnk/.local/bin/omp` with sha256 `85d9daf3…` (now printed in the output's `substrate`
  block) and passes 5 of 7 → 7 of 7, the two omp checks 0 of 2 → 2 of 2; the baseline's check rows
  and the surfaces inventory are byte-unchanged from `43ca0bfb`, and the omp callee allowlist grows
  by exactly `Kl|Ho|bq`. The `S$` group identifier is resolved by a stated module-scope rule
  (`.ufo/waves/round-51/build/SurfacesRepin.md`); an ambiguous rebind inside one module stays
  `<unresolved-var:NAME>`. The 18.12.6 fixture carries the earlier `var S$ = "title"` binding, so a
  callee-names-only fix fails the self-test. Not measured: whether omp actually loads these files at
  run time (the gate reads strings, it does not run omp).
- **C2** (`.ufo/waves/round-51/build/CriticC2Sizing.md`, FAILS as first designed: four 7-of-7 false
  worlds). The script was hardened before landing (table only inside `## Anti-patterns`; six
  columns with pinned `held by` and `effect` values; pinned vendor URL prefix per client; tier-A
  `docs`/`code`/`spec` row; a reviewed per-client list of lever key terms; the key term must be an
  exact backtick span in a quote of at most 25 words; exact entry path in `used-by`; a round-51
  `## Gate` record naming the row; duplicate row ids refused); self-test 10 → 22 assertions, the four
  false worlds among the mutants. Re-sized statement: `SKILL.md` § Anti-patterns names, for K of 7
  pinned clients, a key term from the script's reviewed per-client list of skill-removal levers;
  each term is an exact backtick span in a quote of at most 25 words in
  `corpus/knowledge/skill-overlap-levers-round51.md`, which cites a tier-A row under that client's
  vendor docs prefix, `mined`, `used-by` naming the entry, with a round-51 Gate record: 0 of 7 → 7
  of 7. The `--fetch` run (time, count, exit) is reported beside it. Bound (`CriticLearning.md`):
  every listed lever removes one named skill from the candidates (everywhere, from automatic choice,
  or outside a scope); none is a documented tie-break between two skills that both remain
  candidates. The reviewed list is a reviewer's judgment frozen in code, not a measurement.
