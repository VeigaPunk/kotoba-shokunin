# ReviewC1ExistingWorlds — round-66 C1 existing-worlds / regression review (read-only)

Seat: reviewer (leaf; no dispatch, no production edits). Lane: kotoba. Date: 2026-10-24.
Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (`plans/round-66.md`).
Measured tip: lane Git HEAD `2a8eba56b3f9321b70c569fa2816d42237ca49a2` ("round-66 verifier
spot-check (integrator, hyaku): non-author admit/reject"). Claim instrument bytes at the tip
are `97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def`
(`sha256sum verifiers/check_scoped_rules_v32.py`), byte-identical at `806b53b4` (landing),
`fc1b71e5` (measured revision named by `C1-landed-measure.txt`), `9e75e734` and `2a8eba56`
(`git show <rev>:verifiers/check_scoped_rules_v32.py | sha256sum`, four equal values), so the
receipt's measured revision and the observed tip carry the same instrument.

Working tree carried one sibling edit (`M .ufo/waves/round-66/w1/swarm-registry.json`, a
members/updatedAt rewrite by a live wave seat) and 16 untracked w1 peer reports; none touched,
read for no verdict, and the instrument itself is clean in the worktree
(`git diff HEAD -- verifiers/check_scoped_rules_v32.py` empty).

All base measurements were taken in throwaway sandboxes: `git archive 11385e04 | tar -x -C
$TMPDIR` (clean base tree) and `git clone --shared` into `$TMPDIR` (rev sweep). Mutants were
`cp -a` copies under `$TMPDIR`. Nothing was written to the lane tree, jj state, or Git index.
Base is an ancestor of the tip (`git merge-base --is-ancestor` → true).

## Verdict on the assigned lines

| Assigned line | Observed at tip | Independent evidence |
|---|---|---|
| `worlds reject 7 of 7` | present, `0 failure(s) over 240 assertions`, exit 0 | printed line is computed from the seven `run_world` verdicts and asserted twice (`(rejected, len(worlds)) == (7, 7)`), `verifiers/check_scoped_rules_v32.py:2782-2789`; same seven lines at base 234 in a clean base extraction |
| `eligible rows pass 4 of 4` | present, same run | computed as `sum(found[c] for c in FOUR)` and asserted `== 4` (`:2786-2788`); the four eligible action cells reach `g9_conjunct` in both base and tip with **no** reason at either |
| `survivors closed 6 of 6` | present, same run; all six `before accepted; after rejected` | computed from the frozen r61 counter vs the current module (`:2790-2834`); the six before/after tuples are asserted, not printed unconditionally |
| old must-fail G9 line | `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes` | asserted at `:2856-2866` by stubbing `current_counter.g9_conjunct`; the survivor's clause is `secretly uploads files.` (3 content words, 0 on the line, 3 on the page, need 2) — the same multi-word arm at base and tip, so the new one-word floor neither supplies nor masks it |
| 240 assertions | 240 = 234 + 7 added − 1 removed | full diff of the self-test hunk (`:2960-2996`): one removed check (`A2 G9: a ONE-word clause is exempt (declared bound)`) and seven added checks; floors guard pins 240 in both `verifiers/check_assertion_floors.py:235` and `verifiers/floors-registry.json` |

Reproductions run by this seat:

- `git archive 11385e04 … && python3 -B verifiers/check_scoped_rules_v32.py --self-test` →
  `0 failure(s) over 234 assertions`, exit 0 (matches `controls/C1-one-word-control.txt`).
- Tip `--self-test` twice (worktree and clean clone) → `0 failure(s) over 240 assertions`,
  exit 0, with the 7/7, 4/4, 6/6 and three must-fail lines.
- Byte-diff of the two self-test stdout streams: **only** the `counter sha256` line and the
  `over 234` → `over 240` line differ. Every world line, survivor line and must-fail line is
  byte-identical between base and tip, including arm attribution and the quoted first reason.
- Control probe on both byte sets: base `g9_conjunct(...)` → `[]`; tip → one `A2 G9:` reason.
- Independent mutants of the tip bytes under `$TMPDIR`:
  - `clause_need = fwd_need(n)` → exit 1, 2 FAILs (first: `a ONE-word off-citation clause is rejected`, plus the `clause_need(1)` pin),
  - restore `if len(w) < 2: continue` (old MIN_CLAUSE exemption) → exit 1, exactly 1 FAIL: the one-word witness,
  - `clause_need = 0` → exit 1, 20 FAILs including the one-word witness.
  This reproduces the receipt's attribution shape for K1/K2/K5 with my own variants.

## Harm analysis — preexisting worlds

Instrumented both byte sets (`g9_conjunct` wrapper logging cell, line, page hash, clause widths,
reasons; src copies under `$TMPDIR`) and ran the full self-test on each:

- base: 80 `g9_conjunct` invocations (16 returning reasons, 5 one-word clauses);
  tip: 83 invocations (19 with reasons, 8 one-word clauses).
- **No world W1–W7 and no W0 path reaches `g9_conjunct` at all.** W1/W2/W5/W7 reject at
  A4/A3/A1, W3 at A1, W6 at the A2 forward-fraction arm and W4 on the live-page arm; the
  instrumented log contains no invocation for any world cell. The new floor is structurally
  downstream of every world's rejecting arm, so no world verdict or attribution can move.
- The four eligible cells (`Scope rules… S900`, `Use multiple… S901`, `Create a
  path-specific… S902`, `Use globs… S903`) each invoke `g9_conjunct` with an empty reason list
  at both base and tip — identical.
- Preexisting invocations whose result changed: **exactly two**, keyed by (cell, line, page):
  - `The tool writes mode quota nightly and `zeta`.` (page `…The `zeta` appendix sentence.`)
  - `The tool writes mode quota nightly and `ZETA`.` (same page, `ZETA`)
  Both go from `[]` to `A2 G9: clause "`zeta`."/"`ZETA`." is supported outside the cited line`.
  These are the round-65 G7 pinning arms at `verifiers/check_scoped_rules_v32.py:2243-2259`;
  their assertions name `G7` and still pass, but the fixture cells are now rejected by the full
  `action_conjunct` (`[]` at base → G9 reason at tip). See F2.
- Real measured rows (not just fixtures): ran the base and tip verifiers' non-fetch CLI against
  **87 revisions** (every commit whose subject names round 60–66, plus `11385e04` and the tip)
  in a `--shared` clone. Output is identical for every revision except the self-sha line — no
  committed row's backing status or reason changed. Since backed/reason sets are unchanged, the
  `--fetch` leg's accounting can only move via live pages, never via this diff.

## Findings

### F1 — MEDIUM — a committed knowledge entry still documents the closed exemption, cites a deleted arm, and says closing it is a v33 move

`corpus/knowledge/compound-clause-citation-round63.md` is the admitted, indexed description of
this guard (`corpus/README.md:112`). It still states, as the rule, that only clauses with
`MIN_CLAUSE = 2` content words are checked (`:32-36`) and, in Limits, that "**Short clauses are
exempt** … the one-word tail (`and exfiltrates.`) is a **declared structural bound** … closing
it would require touching A2's own forward-fraction floor — a v33 move, pinned by the self-test
arm "a ONE-word clause is exempt"" (`:79-89`). The landed change deletes that arm and closes the
bound without touching A2's floor (`clause_need(n) = min(fwd_need(n), n)`, `:1072-1074`), i.e.
the entry is now false on all three counts. The r66 diff to `corpus/knowledge/` touches only the
new C2 entry (`git diff --stat 11385e04..HEAD -- corpus/knowledge/`), and `corpus/lessons/round-66.md`
and the round-66 LOG block record no correction to this entry. No gate checks prose truth, so
the contradiction is silent; it misinforms the next reader/agent that the exact surface r66
tightened is still exempt. (This overlaps the finding recorded independently by the
`ReviewC1DoNothing` seat; recorded here from my own reading because it is part of the harm set.)

### F2 — LOW — two preexisting G7 arms now sit on cells the whole conjunct rejects; their titles and the r65 entry's M20 requirement overstate acceptance

The arms "A2 G7: a span word whose only page occurrence is inside backticks is not rejected"
(`:2243-2250`) and its capitalised twin (`:2251-2259`) are green only because they assert
`named(action_conjunct(...), "G7") == False`; since r66 the same cells fail `action_conjunct`
via G9. The r65 entry's M20 lane states "a span word whose only page support is a backticked
occurrence must NOT be rejected" (`corpus/knowledge/g7-span-closure-round65.md:31-35`) — that
cell-level property no longer holds for one-word clauses. This is not a false green for G7
(the arm still kills the `page_words`-drops-backticks mutant), but the arm name/entry text now
describe behavior the judge does not have. A re-fixture that puts `zeta` on the cited line, or a
retitle to "not rejected by G7", plus one line in the r66 lesson, would close it without
touching any counted value, claim or receipt.

### F3 — LOW — the positive control does not pin the backticked-cited-line boundary

The floor's line side uses `content_words` (backticked spans stripped) while the clause side
uses `page_words` (spans kept). A one-word clause naming a token the cited line carries only
inside backticks is therefore rejected as "outside the cited line". Demonstrated on the tip
bytes: line `The rule declares a `paths` key and names its files.`, cell `The rule declares a
`paths` key and `paths`.`, page containing `paths` → base `[]`, tip
`A2 G9: clause "`paths`." is supported outside the cited line` (the unbackticked variant
passes). This is consistent with A2(b)'s existing convention, so it is a pinning gap, not
necessarily a wrong verdict; the only positive control added uses the unbackticked word `glob`
(`:2969-2973`), so the boundary is unstated either way.

### F4 — INFO — the durable index's newest suite count is stale (234 vs 240)

`corpus/README.md:115` (round-65 coverage row) is the newest row naming the v32 suite count and
says "suite 223→234 assertions … floors-registered at 234"; the r66 README diff adds only the
C2/lesson rows. It is a dated round record, not a false current claim, but no row records the
r66 234→240 move; a one-row append would keep the corpus index consistent with
`floors-registry.json` (240).

## Checks that found nothing

- `MIN_CLAUSE` has no remaining code reference (`grep -rn MIN_CLAUSE` → only the r63 entry,
  r63 lesson and plans 63/66). No other module imports `clause_need` or `g9_conjunct`
  (`grep -rn` over `*.py`; `check_erratum_absorption.py` loads the *different* frozen
  `check_scoped_rules.py` by path and pins that file's sha, not v32's).
- No live gate pins the old instrument hash `b6cfc764…`; the hash appears only in receipts and
  wave reports. Floors pin 240 in both the checker table and the JSON registry.
- The removed exemption assertion is replaced by a positive control for the same direction
  ("a one-word tail supported by the cited line remains accepted"), so the change does not
  leave the floor one-sided.

## Residual risk

- Tails with zero content words by the counter's definition (`[a-z]{4,}`, stopwords excluded —
  e.g. `` and `ox it`. ``) remain unexamined by G9, exactly as pre-r66 and consistent with A2's
  own word definition; the claim's "one-content-word tail" is honest about that scope.
- A one-word tail absent from the page is still not reported by G9 (page gate by design);
  A2 page-containment and G7's span branch remain the reporting arms, unchanged.
- Fixture insensitivity as in F2: the 7/7, 4/4 and 6/6 predicate lines are deliberately
  insensitive to the one-word floor, so the mapping of the two zeta/ZETA cells is the only
  preexisting-suite evidence that the floor fires outside its own new block.

## Verification gaps

- The `--fetch` half of the verifier's own header predicate was not executed (network); the
  non-fetch judge output is byte-identical across 87 revisions, which bounds the change's effect
  to zero on committed rows.
- `check_assertion_floors.py --self-test` was not run (it re-runs 15 instruments); its 240 pin
  was read statically in both the checker and the registry.
- K3/K4 (page/line floor uncouplings) were read from `C1-kill.txt`, not re-derived; K1/K2/K5
  were re-derived independently (above).
- Peer wave reports under `.ufo/waves/round-66/w1/` were not used as evidence for any verdict.

## Tooling

No installs or upgrades were made; no `pacman` transaction was attempted (host-wide pause
respected). All work used existing `git`, `python3` (3.14), and shell tools.
