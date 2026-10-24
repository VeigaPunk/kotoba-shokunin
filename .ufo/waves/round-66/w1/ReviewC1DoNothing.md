# ReviewC1DoNothing — round-66 C1 do-nothing control (read-only re-run)

Seat: reviewer (leaf; no dispatch, no production edits). Lane: kotoba. Date: 2026-10-24.
Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (`plans/round-66.md`).
Measured tip: lane Git HEAD `2a8eba56b3f9321b70c569fa2816d42237ca49a2` ("round-66 verifier
spot-check (integrator, hyaku): non-author admit/reject"). Instrument bytes at the tip are
clean in the worktree (`git diff HEAD -- verifiers/check_scoped_rules_v32.py` empty; committed
blob sha256 `97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def`, equal to the
`C1-measure.txt` / `C1-landed-measure.txt` value). Only peer-owned artifacts are uncommitted:
`M .ufo/waves/round-66/w1/swarm-registry.json` and untracked peer reports under
`.ufo/waves/round-66/w1/` — none touched by this seat.

Base bytes were measured in throwaway `git archive 11385e04 | tar -x -C $TMPDIR` sandboxes;
mutants in `cp -a` copies under `$TMPDIR`. Nothing was written to the lane tree, the jj
working copy, or the lane Git index. The base is an ancestor of the measured tip
(`git merge-base --is-ancestor` → true).

## Verdict

The committed do-nothing control reproduces exactly and **cannot meet the frozen 240 target**:
on the pinned base bytes the one-word off-citation tail is admitted (`one-word-tail reasons:
[]`, exit 0) and the suite prints `0 failure(s) over 234 assertions`, exit 0. The witness is
genuinely **page-present and cited-line-absent**, and the rejection at the tip is attributable
to the landed G9 coupling alone. **No control shortcut found.** Two non-blocking findings are
recorded below: one stale committed knowledge entry that still documents the closed exemption,
and one receipt-wording nuance.

## 1. Control replay — exact committed command, base bytes

The committed command in `.ufo/waves/round-66/controls/C1-one-word-control.txt` was extracted
and replayed verbatim from a base-byte archive:

```
one-word-tail reasons: []
exact_control_exit=0
self-test: 0 failure(s) over 234 assertions
exact_selftest_exit=0
```

The control file's bytes are unchanged since the freeze commit: `sha256` at `e7d1d8c`
("round-66: freeze claims and controls") equals the `HEAD` blob,
`12d2469acefb35b63824e452b377c527c17d623cc046097d3009bee59cf27f12`; and
`git merge-base --is-ancestor e7d1d8c 806b53b` is true, so the control was committed **before**
"round-66: land G9 coupling and integrity fixes". No post-hoc editing of the control.

The same command at the measured tip returns:

```
one-word-tail reasons: ['A2 G9: clause "exfiltrates." is supported outside the cited line']
```

The base and tip behaviours are therefore the exact before/after pair the plan freezes.

## 2. Witness genuineness — present on page, absent from line

Fixture (as committed): `line = "The index stores project rules."`, page =
`line + "\n\n## Schedule\nThe agent secretly exfiltrates telemetry."`,
`cell = line[:-1] + " and exfiltrates."`.

Computed on the tip instrument (`page_words`, `content_words`, `split_clauses`):

- `split_clauses(cell)` → `['The index stores project rules', 'exfiltrates.']` — the tail is a
  genuine single-content-word clause, not a whole-cell artefact.
- `'exfiltrates' in page_words(page)` → **True**; raw occurrences on the page → **1**
  (line 3 of the page, the appended `## Schedule` section).
- `'exfiltrates' in content_words(line)` → **False**; raw occurrences on the cited line → **0**.
- `page_words(page) - content_words(line)` → `['agent', 'exfiltrates', 'schedule', 'secretly',
  'telemetry']`.
- `clause_need(1)` → **1**; `covered({'exfiltrates'}, line_w)` → 0.

So the witness is supported **only** outside the cited line. The support is also literal: the
page carries the same word, not merely a 4-character prefix sibling. (The fixture design would
still reject if the page carried only `exfiltrated`, because `supported()` matches on a
4-character prefix — verified separately.)

The page argument is passed as the 4th positional parameter of
`g9_conjunct(lines, cell, L, page_text)`, so the arm reads the committed page, not the
line list; a variant that supplies the same page as `lines` and cites line 1 also rejects
(verified).

## 3. Frozen 240 target

| Revision | self-test | one-word witness | G9 must-fail line | worlds / eligible |
|---|---:|---|---|---|
| base `11385e04` (archive) | `0 failure(s) over 234 assertions` | `[]` (admitted) | present | `7 of 7` / `4 of 4` |
| measured tip `2a8eba5` | `0 failure(s) over 240 assertions` | rejection reason | present | `7 of 7` / `4 of 4` |

Tip also retains `survivors closed 6 of 6`. The +6 delta is arithmetic, not label inflation:
the diff replaces **one** assertion (`"A2 G9: a ONE-word clause is exempt (declared bound)"`,
now absent from the instrument — `grep` returns nothing) with **seven**:
`:2966` one-word off-citation rejected, `:2969` one-word supported-by-line passes, `:2974`
`clause_need(1) == 1`, `:2976` and `:2978` coupling no-ops at 2 and 3 words, `:2987` uncoupled
mutant admits, `:2995` zero-floor mutant admits. The count itself is computed by
`assertions += 1` inside `check()` (`:1764-1766`), not printed as a constant.

Coupling is minimal and confined to length 1: `clause_need(n) = min(fwd_need(n), n)`
(`:1072-1074`) gives `[1, 2, 2, 4]` for `n = 1,2,3,5`; for every `n >= 2` it equals
`fwd_need(n)`, and `fwd_need` keeps its own absolute pins at `:2082-2085`. `MIN_CLAUSE` is
deleted with no remaining Python reference anywhere in the lane (`grep -rn MIN_CLAUSE
--include=*.py` → none outside historical Markdown).

**Do-nothing cannot reach 240**: with no instrument change the suite stays at 234 by
construction, and no other assertion was added elsewhere in the same landing (the base..tip
diff touches only the G9 clause floor, its docstring, and the self-test arms).

## 4. Control shortcut audit

Checked, none of these is a shortcut:

- **Unit helper vs full verifier.** The control calls `g9_conjunct` directly. On base bytes the
  *full* `action_conjunct([line], cell, 1, page)` also returns `[]`, i.e. the entire A2/G7/G9
  citation machinery admitted the fabrication at base. The control understates, it does not
  overstate. At the tip the only reason `action_conjunct` returns is the G9 one — attribution
  is clean.
- **Non-vacuity.** The one-word cell is 5 content words against `fwd_need(5) = 4`, and the cited
  line supplies exactly 4 — the fabrication clears A2's forward floor **at the minimum**. Reverse
  coverage: line 4 words, covered 4, need 3. Page containment: all 5 present. So the before-state
  is a genuinely admitted fabrication, not one a stricter quote-check would have rejected.
- **Prefix-only page support.** Not used: the page contains the literal token (raw count 1). A
  prefix-only variant (`exfiltrated` on the page, `exfiltrates` in the cell) also rejects, so the
  result is not an artefact of prefix matching.
- **Page/line aliasing.** The page is the line plus an unrelated section; the cited line itself
  contains zero occurrences of the witness.
- **Evidence completeness.** Base `234` and base `[]` both reproduced from archived base bytes,
  not from the tip or a receipt; the receipt values `C1-measure.txt` (240) and
  `C1-landed-measure.txt` (240, core rev `806b53b`, final pre-report `fc1b71e`) match my tip run
  and the committed blob hash.

## 5. Independent mutation re-verification (kill receipt)

Five temporary mutants were rebuilt independently in `$TMPDIR` copies (the lane file was never
mutated) and run through `--self-test`:

| Mutant | exit | first FAIL line(s) |
|---|---:|---|
| K1 `clause_need → fwd_need` (uncoupled) | 1 | `A2 G9: a ONE-word off-citation clause is rejected: got False, expected True`, then `clause need couples the one-word floor: got 2, expected 1` |
| K2 reinsert `if len(w) < 2: continue` (old exemption) | 1 | `A2 G9: a ONE-word off-citation clause is rejected: got False, expected True` — **only** failure |
| K3 page floor uses `fwd_need(len(w))` | 1 | same one-word rejection — **only** failure |
| K4 line floor uses `fwd_need(len(w))` | 1 | `A2 G9: a ONE-word clause supported by the cited line passes: got True, expected False`, then a zero-floor meta-arm |
| K5 `clause_need → 0` | 1 | 20 failures; the first lines are pre-existing r63 A2 G9 arms; `A2 G9: a ONE-word off-citation clause is rejected` is present in the output |

K2 and K3 each fail through the **single** new witness, which is the strongest available
evidence that the old exemption was load-bearing and that the coupling (not some other arm) is
what the control measures. The mutation patch is effective because the self-test declares
`global ... clause_need` (`:1759`); without it the meta-arms would fail closed, not pass
vacuously.

## 6. No-harm on committed rows

`python3 -B verifiers/check_scoped_rules_v32.py --rev <rev>` at the pinned base and at the
measured tip is byte-identical except the revision line: `scoped rule files backed on committed
snapshots 4 of 4; live not run`, the same canonical-key line, the same three client rejects
(Codex, Gemini CLI, opencode), exit 1 at both. The landing therefore changes no committed entry
row's verdict; C1's gain is a latent-class closure, not a corpus-visible repair. That is
consistent with the frozen claim (which measures the instrument, not the corpus) and should be
read that way when the depth axis is scored.

## Findings

### Medium — a committed knowledge entry still states the closed exemption as the current rule
`corpus/knowledge/compound-clause-citation-round63.md` describes the instrument in the present
tense and was not reconciled:

- `:33-36` "For each resulting clause with at least `MIN_CLAUSE` = 2 content words … require the
  same forward-support fraction" — `MIN_CLAUSE` no longer exists in the instrument
  (`verifiers/check_scoped_rules_v32.py:1143-1145`).
- `:79-89` "**Short clauses are exempt.** … the one-word tail (`and exfiltrates.`) is a
  **declared structural bound** … closing it would require touching A2's own forward-fraction
  floor — a v33 move, pinned by the self-test arm \"a ONE-word clause is exempt\"." The named
  arm is absent from the instrument (`grep "ONE-word clause is exempt"` → nothing), the bound is
  closed at the tip, and the landed `clause_need(n) = min(fwd_need(n), n)` closes it **inside**
  G9 without touching `fwd_need`, i.e. not by the route the entry declares as the only one.
- The file has its own correction practice: a dated freshness note at `:128` for the earlier
  219 → 223 move. No analogous note was appended for 234 → 240.

This does not touch C1's frozen predicate or the 240 counter; it is an observable-contract
inconsistency in the corpus and belongs to the L1 / C2 consistency work (erratum or a dated
freshness note). Note that the same staleness pattern already exists for the r64 entry
(`g7-span-pinning-round64.md` still pins 223 with no note for 234), so this is a practice gap,
not a round-66-only violation.

### Low — `C1-kill.txt` attribution wording for K5
The table names `FAIL A2 G9: a ONE-word off-citation clause is rejected …` as the attributed
failure for K5. That string does appear in K5's output, but K5's output has 20 failures and its
**first** lines are pre-existing r63 arms. The receipt's parenthetical ("attribution above names
the first load-bearing C1 witness/control in each output") is accurate only under the
C1-specific reading. Recommend wording that distinguishes "first C1-specific failure" from
"first failure line"; no counter or claim value changes. K1–K4 reproduce as stated.

### Low — new G7 + G9 co-report for a single-word backticked clause
For a cell whose one-word tail is a single backticked token that is prefix-supported on the page
but absent as a raw substring (`exfiltrated` on the page, `` `exfiltrates` `` in the cell), the
tip returns **two** reasons where base returned one:

```
tip  action: ['A2 G7: backticked identifier(s) exfiltrates occur in neither the cited line nor
              the committed snapshot',
             'A2 G9: clause "`exfiltrates`." is supported outside the cited line']
base action: ['A2 G7: backticked identifier(s) exfiltrates occur in neither the cited line nor
              the committed snapshot']
```

The verdict is unchanged and the documented invariant (G9 does not double-report **A2's page
arm**, `:1128-1129`) still holds; this is diagnostic duplication with G7's stricter
raw-substring test. Worth a sentence in the entry if the reason list is treated as stable.

### Info — characterization notes
- `clause_need(1) = 1` keeps A2's 4-character-prefix support (`supported()`), so a one-word tail
  can ride a line word sharing four leading characters. This is A2's existing contract
  inherited unchanged, not a new loophole, but it is the residual weakness of the new floor.
- One-word clauses with no `[a-z]{4,}` content words (numeric or stopword-only tails) stay
  skipped; a bare word absent from the page is still caught by A2 page containment (verified:
  `and zzzz.` → `A2: action word(s) zzzz do not occur on the committed snapshot`, no G9 reason).
- One-word tail supported by the cited line passes (verified `and glob.` → `[]`), so the
  landing is symmetric, not a blanket rejection.

## Residual risk

- The C1 claim is an instrument-depth claim; no committed entry row changes verdict at this
  revision (§6). If the depth score is justified on guard surface alone, that is a rubric ruling,
  not something this control can settle.
- `supported()` prefix matching bounds the new floor in both directions (line and page).
- The `MIN_CLAUSE`-era knowledge entry (Medium finding) is the only committed text that now
  contradicts the instrument; any future reader following it would test the wrong contract.

## Verification gaps

- No `--fetch` run: live-page arms and network-dependent worlds were not exercised (both base
  and tip report `live not run`).
- C2 (consistency/calibration, routed D1/D2) was not scored or re-measured — out of this seat's
  assignment.
- `verify_corpus_integrity.py`, `check_r66_routed_repairs.py`, the floors registry, and
  `check_erratum_absorption.py` were only exercised indirectly through the v32 self-test's
  sibling load; no standalone run.
- jj working-copy state (`98c994b0…` per peer report) was not inspected; measurements are on
  committed Git bytes plus `$TMPDIR` archives, and the worktree instrument file is clean.
- No statement is made about seats' reports in this wave; only the committed controls,
  receipts, plan, verifier, and corpus text were read.

## Commands (reproducible)

```
# base bytes
D=$(mktemp -d); git archive 11385e04e368c1e94ab1a5a89d7439033eb1f855 | tar -x -C $D
cd $D && <exact command from controls/C1-one-word-control.txt>
#   one-word-tail reasons: []                      exit 0
#   self-test: 0 failure(s) over 234 assertions    exit 0

# tip bytes
python3 -B verifiers/check_scoped_rules_v32.py --self-test
#   counter sha256 97d89716…; self-test: 0 failure(s) over 240 assertions; exit 0
python3 -B verifiers/check_scoped_rules_v32.py --rev 11385e04…   # vs --rev 2a8eba56…: only rev line differs

# frozen hashes
git show e7d1d8c:.ufo/waves/round-66/controls/C1-one-word-control.txt | sha256sum   # 12d2469a…
git show HEAD:verifiers/check_scoped_rules_v32.py | sha256sum                       # 97d89716…
```
