Result: MIXED — the C2 number is real and reproducible, and coverage is the right axis, but the statement claims two things the counter does not check, the prose overcounts clients by one, and "at least 3 of 7" is a lower bound rather than one concrete value.

Seat: KotobaR52a2.CriticC2Sizing (critic, falsify wave attempt 2). Judged revision: `c8407a453788df964df5a7b835dd0ce1360de882`; plan and frozen counter at `4c003a4b9c7dae8ebb8ad34bbc14cd1706febeeb`.
Sandbox: `/fast/scratch/hyaku/kotoba-r52a2/CriticC2Sizing` (clone checked out at `c8407a45`; every mutant was reset with `git checkout -- .` afterwards). No lane file other than this report was written. No tools installed or updated.

## Baseline reproduction (precondition for every attack)

- `git diff --quiet 4c003a4b c8407a45 -- verifiers/check_mcp_instructions.py plans/round-52.md` → exit 0. The counter and the plan are byte-identical between the plan commit and the judged head, so no widening happened after the plan (Q28).
- `python3 -B verifiers/check_mcp_instructions.py --rev <rev>` (lane, read-only):
  - `c8579a4c` → `mcp instructions backed 0 of 7 clients`, exit 1
  - `4c003a4b` → `0 of 7`, exit 1
  - `c2107ecf` → `0 of 7`, exit 1
  - `c8407a45` → `5 of 7`, exit 0 (MCP specification, Claude Code, VS Code, Codex and Gemini CLI BACKED; opencode and Copilot CLI have no row)
- `--rev c8407a45 --fetch`, run at 2026-10-22T17:51:11Z → `found on the live page 5 of 5`, exit 0.
- Independent re-fetch with curl at 2026-10-22T17:51:11Z:
  - https://geminicli.com/docs/tools/mcp-server.md: HTTP 200, 43,656 B, sha256 `4aefc4dc30c329cbbd16ca24fe294fb0d91ec87e8f61baca7116c19b6a1a14fd`. Identical to the S036 record in `corpus/lessons/round-52.md:29-30`.
  - https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers.md: HTTP 200, 14,240 B, sha256 `640035aa0936ffb83ee8dd7034370019224c43cf03ee9560103a3a9cd190433b`. The prefix matches the rejection record at `corpus/lessons/round-52.md:51-52`.

## Attack 1 — does the statement claim anything the counter does not print? BREAKS (medium)

The statement (`plans/round-52.md:40-45`) contains two clauses that no output of the counter depends on. This also violates the lane's own criterion Q26 (`corpus/QUALITY.md`: every clause of a statement must be turned on by the counter's output or by a cited guard).

- **"a located quote".** The counter reads only cells 0, 1 and 2 of each entry row (`check_mcp_instructions.py:195-237`: client, row and quote). It never reads the `location` cell, and it never reads the SOURCES `anchor` cell (it reads only `s[1]`, `s[2]`, `s[3]`, `s[7]`, `s[8]` and `s[10]`). `--fetch` checks only that the quote is a substring of the page, not that it sits at the cited line.
  - Mutant M1: blank all five `location` cells in the entry, then run `python3 -B verifiers/check_mcp_instructions.py --root .`. Output: `backed 5 of 7 clients`, exit 0. **Survives.**
- **"with the quote recorded in this round's Gate".** The counter checks that the id and the quote appear anywhere in `corpus/lessons/round-52.md` (`:234`), not inside the `## Gate` section.
  - Mutant M2: rename `## Gate` / `### Admitted …` to `## Scratch notes (not a gate decision)` / `### Pasted text`. `grep -c '^## Gate'` → 0. The counter still prints `backed 5 of 7`, exit 0. **Survives.** At the real head the quotes do sit in § Gate (`lessons/round-52.md:13-40`), so this clause is true of the content but is not something the counter checks.
- **Text that says the counter checks what it does not:**
  - Entry `corpus/knowledge/mcp-server-instructions-round52.md:61-63` says the counter "checks that each row's quote is located". M1 shows this is false.
  - The uncommitted `SCORECARD.md` coverage cell (working tree, line 30) says "The counter checks location, length, the word `instructions`, host and Gate record". "location" is false (M1), and "Gate record" holds only as presence in the lesson file (M2).
- **Client count overstated by one.** The frozen counter's 7 "clients" include the MCP specification (`check_mcp_instructions.py:69`), so `5 of 7` means the specification plus four clients.
  - `PROVINCE.md:19` says "what the MCP specification and five pinned clients document". That is six backed items, while the counter prints 5.
  - Entry `:55` says "Whether any of the five clients does so". The same entry at `:42` correctly says "Four clients (Claude Code, VS Code, Codex, Gemini CLI)".
  - Severity: low, but it is a count the counter contradicts, which is the class Q26 exists to catch.
- **Impacted axes:** calibration (self-description does not match observed state) and coverage (the headline of the claim being judged).
- **Smallest safe correction** (no counter or plan change, since both are frozen):
  1. Rewrite entry `:61-63` and the working-tree SCORECARD coverage cell to say the counter checks client row, `S###` row (tier, kind, status, opened date, used-by, host), quote word count and the word `instructions`, and that the id and quote appear in the round-52 lesson. With `--fetch` it also checks that the quote is on the live page. It does not check the location cell or the Gate section; those are reviewer-checked.
  2. Change `PROVINCE.md:19` to "the MCP specification and four pinned clients", and entry `:55` to "four clients".
  3. The closure reads the clauses "located" and "in this round's Gate" as reviewer-verified, not counter-verified.
  4. The lesson records this as a Q26 recurrence (M-row).

## Attack 2 — is "at least 3 of 7" one concrete value that one command over committed bytes can re-derive? BREAKS (medium; a sizing defect, not narrowing)

- The session Quality bar (`/home/vgpnk/Projects/shokunin/.scratch/goal-20261022-hyaku-12h.md:151-152`) says: "Declare each after-state as one concrete value that the closure can re-derive with one command over committed bytes."
- The C2 after-state (`plans/round-52.md:45`, `:49-50`) is "at least `3 of 7`" plus "`--fetch` found at least 3". That is:
  - a lower bound, not a value;
  - two conditions, the second of which reads live network bytes, not committed bytes.
- C1 in the same plan declares a point value (`0 of 4` → `4 of 4`). Round 51's C2 also declared a point value (`0 of 7 → 7 of 7`, `plans/round-51.md:32`), missed it, and closed as an honest stop. Round 52 changed form to a floor.
- **Strongest counterexample: the slack absorbs falsification.**
  - Mutant M4a: delete the VS Code and Gemini CLI rows. Output: `backed 3 of 7`, exit 0, so the declared claim still verifies.
  - M4b: also delete Codex. Output: `2 of 7`, exit 1.
  - So two of the five backed rows can be knocked out by wave-2 reviewers and C2 still passes as declared. With the specification counted as a "client", the floor can be met by the specification plus two clients.
- **What holds:**
  - `--rev <rev>` is one command over committed bytes. It prints the exact K (5), and its exit code encodes the bound. So the closure can re-derive both "5" and "≥ 3" from one command.
  - Nothing was narrowed after landing (attack baseline: diff exit 0), and 5 ≥ 3.
- **Impacted axes:** coverage (verdict strength) and calibration (the SCORECARD records `5 of 7` as the after-value; the plan declared a bound).
- **Smallest safe correction:**
  - The closure judges C2 on the declared bound, re-derived by `--rev c8407a45` (one command, committed bytes). It records 5 as the observed value, not as a declared target.
  - It treats `--fetch` as a dated second measurement (network-dependent), not as part of the committed-bytes verdict.
  - Any row that reviewers find wrong is reported against the observed 5, not hidden under the bound.
  - The round-53 plan declares a point value.
  - No change to the frozen plan or counter.

## Attack 3 — is coverage the right axis (AXES.md, LEARNING.md)? HOLDS, with one counter-validity tradeoff disclosed by the plan

- **Why coverage is right:**
  - `AXES.md:13` defines coverage as the "Fraction of the domain's real surfaces the skill governs (repo paths, tools, edge classes)", with the signal "PROVINCE.md lists every surface".
  - The move adds a governed surface: `PROVINCE.md:19` (Core gains "MCP server `instructions`", moved in part from Frontier). The Frontier area existed at base (`c8579a4c:PROVINCE.md:23`, `c8579a4c:corpus/README.md:87` "MCP/plugin instruction surfaces"), and the round adds a Frontier note at `corpus/README.md:94-104`.
  - `LEARNING.md:33` ties expansion to coverage, with "admitted `knowledge/` entries on ground the coverage map did not hold … frontier areas entered".
  - Distinct axis from C1 (freshness, the lowest at 8 per `plans/round-52.md:10-11`). The causal separability statement is at `:60-62`.
- **Tradeoff (counter validity; disclosed at `plans/round-52.md:51-53`; severity low to medium; cannot be fixed this round because the counter is frozen).** The counter's only test of whether a quote is about the subject is the token `instructions`. So K counts clients with a host-pinned quote containing a word, not clients documenting server instructions.
  - Mutant M3: add a Copilot CLI row citing a new tier-A SOURCES row S099 for `add-mcp-servers.md`, quoting line 22: "For installation instructions, available tools, and URLs for specific MCP servers, see the". Record it in the lesson.
  - Result at 2026-10-22T17:52:10Z, `--root . --fetch`: `backed 6 of 7 clients`, `found on the live page 6 of 6`, exit 0. **Survives.**
  - That page and that sense of "instructions" are exactly what the round's own Gate rejected (`lessons/round-52.md:51-54`).
  - The real Gemini row is a weaker form of the same issue. Its quote "which will be appended to the system instructions." carries the word only through "system instructions". The subject ("MCP server instructions") is in the preceding line outside the quote (re-fetched page, `## Instructions` section: "Gemini CLI supports [MCP server instructions](…), which will be appended to the system instructions."). Here the reading is right, but the counter could not have told.
- **Consequence:** the coverage value 5 is a coverage measure only together with the reviewer reading of each row. That is what the plan says. The prose in `corpus/README.md:78` ("each with a located quote on what the client does with the server's `instructions`") claims the reading, not the count; see attack 1.
- **Smallest correction:** none to the frozen counter this round. The closure must take the per-row reading verdicts from the reviewer seats (ReviewEntry and the Reopen scouts) before crediting 5. A future counter should require the quote to contain "server instructions" or the `instructions` field name, not the bare word.

## Attack 4 — does the round meet the session Quality bar learning-claim test? MIXED

Checked clause by clause against `goal-20261022-hyaku-12h.md` § Quality bar:

| Clause | Verdict | Evidence |
|---|---|---|
| Learning claim (≥1 claim that changes what the lane knows) | HOLDS (pending the non-author spot-check) | New knowledge entry on ground the coverage map did not hold. The Frontier row existed at base, and the base round-13 census named the class but not the text (entry `:8-10`). A `SKILL.md` decision table grounded in the entry was added (`SKILL.md` diff, § Instruction surfaces, citing S033–S036). The spot-check (≥1 admit, ≥1 reject) is still owed (`lessons/round-52.md:64-66`), so "admitted" is lane-attested until the closure. |
| One concrete value, one command, committed bytes | BREAKS | Attack 2. |
| No universal clauses unless the counter enumerates the set | HOLDS for the statement (it is "K of 7" over a pinned set) | Low-severity note: the plan's "Learning content" line `:56` says "where an MCP server's server-wide text goes in each client", but only 4 clients plus the spec are backed and 2 are silent. The entry itself bounds this (`:36-37`, `:47-48`). |
| Prefer 2 claims | HOLDS | C1 and C2. |
| Never narrow a target after landing | HOLDS | Counter and plan diff exit 0 between `4c003a4b` and `c8407a45`. |
| Sources: primary, opened this round, located quote | HOLDS with the attack-1 caveat | S032–S036 are vendor or spec pages with fetch time, byte count and sha256 (`lessons/round-52.md:17-31`). My re-fetch of S036 matches byte for byte. S037 is tier B (maintainers' blog), is labelled as such and is not counted. "Located" is real in the entry cells but not counter-checked (M1). |
| ≥25% attack seats | HOLDS on dispatch | Falsify a2: reviewer 9 + critic 7 + mutation-tester 3 = 19 of 34 seats (56%), from `.ufo/waves/round-52/falsify-a2-spec.json`. Attempt-1 build spec: 14 of 34 (41%), but that wave never ran (`lessons/round-52.md:11`). [INFERENCE] The build work was done by the L1 inline, so "executors only for code, scribes for prose" was not exercised by seats in this round. That is a process note, not a C2 defect. |

## Mutants run (all in the sandbox; `--root .` unless noted)

| id | change | output | exit | verdict |
|---|---|---|---:|---|
| M1 | blank all five entry `location` cells | `backed 5 of 7` | 0 | survives (location unchecked) |
| M2 | lesson has no `## Gate` heading; quotes remain in the file | `backed 5 of 7` | 0 | survives (Gate section unchecked) |
| M3 | add a Copilot CLI row (S099, tier A, docs.github.com) quoting "installation instructions" from line 22; `--fetch` | `backed 6 of 7`, `found 6 of 6` | 0 | survives (word test does not discriminate) |
| M4a | delete the VS Code and Gemini CLI rows | `backed 3 of 7` | 0 | claim still passes with 2 rows gone |
| M4b | also delete Codex | `backed 2 of 7` | 1 | killed |

## Checks for the L1 / closure to run

- `python3 -B verifiers/check_mcp_instructions.py --rev c8407a45` (expect `5 of 7`, exit 0) and `--fetch` (dated).
- After any correction to entry `:55`, `:61-63`, `PROVINCE.md:19` or the SCORECARD coverage cell, re-run the same counter. Those cells are outside what it reads, so the expected output is unchanged at `5 of 7`. Also run `python3 -B verifiers/check_correction_sweep.py`.
