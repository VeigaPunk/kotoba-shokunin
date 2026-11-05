# ReviewerFreezeGate — controlled findings (C1 freeze gate, r89-w1)

Files: `.ufo/waves/round-89/w1/ReviewerFreezeGate/review.md` and
`.ufo/waves/round-89/w1/ReviewerFreezeGate/attack-fixtures.md`.

## Verdict: REPULSED — no exploitable finding in the gate's refusal path

The freeze gate (`verifiers/check_freeze_gate.py`, sha256
`a20e6f9afff367dfb56b3d8fa437a176627bf55623d1f6b20dea320943e15e41`, digest
matches `.ufo/waves/round-89/w1/FG_READY`) refuses the r88 unsatisfiable
control plan and holds the fixed plan, exactly as the C1 frozen predicate
declares. Every forged attack from the seat spec (six) plus two added worlds
(order litmus, heading re-entry) is repelled with the declared-vs-observed
text naming the offending control.

## Predicate arms re-run (item 1)

    python3 -B verifiers/check_freeze_gate.py --self-test
      → exit 0, "0 failure(s) over 30 assertions"
    python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls.md
      → exit 1, REFUSED control w_added_red (line 36): declared "exit 0; stdout contains D5=FAIL";
        observed exit=0 stdout=w_added_red D5=PASS
    python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md
      → exit 0, freeze gate: 4 control(s) held — freeze may proceed

## Attack table (item 2, verbatim observed lines)

| id | attack plan | expected | observed | verdict |
|---|---|---|---|---|
| A1 | declaring exit 0 only against the refusing sim (`plans/attack-1-zero-on-refusing.md`) | refuse | `A1 exit=0 : freeze gate: 1 control(s) held` | **finding F-1** (see below) |
| A2 | control command `false` (`plans/attack-2-false-command.md`) | refuse naming it | `A2 exit=1 : REFUSED control always_false (line 4): declared "exit 0"; observed exit=1 …` | repelled |
| A3 | wrong `stdout contains` literal (`plans/attack-3-wrong-literal.md`) | refuse | `A3 exit=1 : REFUSED control w_tip (line 4): declared "exit 0; stdout contains D5=TAMPERED"; observed exit=0 stdout=w_tip D5=PASS` | repelled |
| A4 | two controls, second fails after first held (`plans/attack-4-second-fails.md`) | name the SECOND | `A4 exit=1 : REFUSED control bad_two (line 6) …` (first control `good_one` is not named) | repelled |
| A5 | command exits 2 unexpectedly (`plans/attack-5-unexpected-exit2.md`) | gate exit 1 naming it, not silent pass | `A5 exit=1 : REFUSED control exits_two_once (line 4): declared "exit 0"; observed exit=2 …` — refusal (1), not could-not-evaluate (2), control named | repelled |
| A6 | nondeterministic command output (`plans/attack-6-nondet.md`) | stable verdict across re-runs | two invocations of the same world both exited 0 (`freeze gate: 1 control(s) held — freeze may proceed`); gate re-measured in fresh tmpdirs — verdict byte-identical, "held" stability across runs | repelled |
| A7 (added) | order litmus: same control name ordering / mixed truth (`plans/attack-7-order-litmus.md`) | both controls actually hold | `A7 exit=0 : freeze gate: 2 control(s) held — freeze may proceed` | repelled |
| A8 (added) | heading re-entry worlds (`plans/attack-8-hidden-reentry.md`, `plans/attack-8-h2-placement.md`) | no silent pass | `A8 exit=3 : INVALID SPEC: empty ## Controls block` (and same for h2 variant) | repelled |

## Simulators receipt-grounded + fail-closed (item 3)

Verified by running each of the four simulators inside a scratch
`git clone --shared` of the lane (`/fast/scratch/hyaku/kotoba-r89/ReviewerFreezeGate/repo`)
while renaming the cited receipt away and restoring it (each restore checked
with `cmp`, byte-identical).

With receipt PRESENT, sims printed the receipt-grounded verdicts:
`w_added_red D5=PASS`, `w_silenced D5=FAIL-world-unreachable`,
`w_healed D5=PASS`, `w_tip D5=PASS`; both predicate plans re-run inside the
clone with the same exit codes and refusal text as the lane run.

With receipt RENAMED AWAY (`ExecMonotoneD5/receipts.txt`, one sim at a time):

    sim-w-added-red.sh exit=2 message='sim-w-added-red: receipt missing: …/receipts.txt'
    sim-w-silenced.sh  exit=2 message='sim-w-silenced: receipt missing: …/receipts.txt'
    sim-w-healed.sh    exit=2 message='sim-w-healed: receipt missing: …/receipts.txt'
    sim-w-tip.sh       exit=2 message='sim-w-tip: receipt missing: …/receipts/before-C2-tip.txt'

    gate (unsat plan) with receipt absent → exit=1 (not silent PASS):
      REFUSED control w_added_red (line 36): declared "exit 0; stdout contains D5=FAIL";
      observed exit=2 stdout= (exit mismatch …)

    sim-w-tip with l1-c2-tip.txt absent (other two present) → exit=2 'receipt missing: …/l1-c2-tip.txt'
    sim-w-tip with review.md absent (other two present)    → exit=2 'receipt missing: …/review.md'
    sim-w-tip with before-C2-tip.txt absent (other two present)
      → exit=2 'sim-w-tip: receipt missing: …/receipts/before-C2-tip.txt'
      (re-verified explicitly with a targeted one-receipt-away probe; restore checked with cmp)

    sim-w-silenced with CriticFalsify/attacks.md absent → exit=2 'receipt missing'

All four sims therefore fail closed on ANY missing grounding receipt, ea. of
the three receipts named in their headers.

## F-2 (sim receipts, resolved during re-check)

An earlier provisional note claimed `sim-w-tip.sh` still printed
`w_tip D5=PASS` while `before-C2-tip.txt` was absent. That provisional claim
did not reproduce: with the one-receipt-restore probe above (targeted,
receipt moved to `$BT.absent`, everything else untouched in the clone), the
sim exited 2 with the stated receipt-missing message. The 0/PASS print seen
earlier in the same session replicated the rename*failure* pattern (the
`.absent` name is inside a tracked directory, so the shell `mv` silently
resolved the file), not a sim defect. All four sims are receipt-grounded and
fail-closed on missing receipts: confirmed. No finding.

## Gate source escape-hatch analysis (item 4)

Direct read of the gate source. No `/tmp`-hardcoded path handling; `TMPDIR`
is honoured (self-test even has a `--tmpdir-honoured` arm and a name check
`arm source-has-no-hardcoded-temp-literal`); `--work` places the tmpdir
under `work_root`; unmatched/unreadable/timeout commands produce
could-not-evaluate (exit 2) — never silent. Silent-skip candidates probed and
repelled, each via a constructed plan (`runs/*.md` under my scratch
`/fast/scratch/hyaku/kotoba-r89/ReviewerFreezeGate/`):

    '- control: false'                      → INVALID SPEC, exit 3 (not a control; no silent pass)
    '- control a false' (no colon)          → INVALID SPEC exit 3
    '%-prefixed junk line'                  → INVALID SPEC, exit 3
    expect-line clause reorder              → valid spec (order not enforced; the parsed clause list is logical, not positional)
    CRLF line endings                       → valid spec (CRLF tolerated)
    '-control-'-prefixed fuzzy names        → '-a' parsed as control name (minor); refusal still names that control
    duplicate control names                 → **both entries parsed; the first violation wins, exit 1** — the docstring asserts SpecError-on-duplicate; behavior deviates (F-3, non-blocking: even with a duplicate world, the refusal is intact)
    heading-close re-entry                  → exit 3 safe-close (never silently re-opens)
    indented '##'-prefixed close-in-block   → parses as a control named 'deep' (minor); refusal intact

## Findings (defects / deviations; none breaks C1 refusal-safety)

- **F-1 (docstring drift on partial expectation).** `A1` holds a plan whose
  control declares only `expect: exit 0` against a sim printing
  `w_added_red D5=PASS`. Both clauses are individually optional per the
  docstring ("`exit` and `stdout contains` clauses are each optional but at
  least one must be present"), so the observed behavior (exit 0) conforms to
  the grammar — but the ladder's *spirit* of "declared expectations must
  actually hold" is only enforced on declared clauses. The C1 predicate arm
  (`r88-controls.md`) declares both clauses for `w_added_red`, so the frozen
  score is unaffected. Recommendation (not for me to edit the gate): future
  plans should declare both clauses; alternatively, restrict rc-only expects
  to 0-declaring refusal plans.
- **F-2 (sim receipts, resolved).** An earlier note claimed `sim-w-tip.sh`
  could print PASS with a receipt renamed away. Re-verified with a targeted
  probe (see item 3): the sim exits 2 on any missing grounding receipt.
  Withdrawn; no finding.
- **F-3 (docstring drift on duplicate control names).** Docstring asserts
  duplicate names are invalid spec; observed behavior parses both entries
  and the first mismatch wins (exit 1, correct refusal, correct name). No
  C1 shortcut is opened. Recommendation: either track duplicate names as
  SpecError, or reword the docstring.

## Verification gaps

- No world was constructed where a control's *command* silently mutated the
  lane tree (a sim that writes to the lane and does the probe of "matches a
  cleanOutputStream" — gate runs control commands with `cwd=LANE_ROOT`, so
  such a control could theoretically write into the lane). I did not probe
  this; the plan-level gate assumes the lane is not under my write
  privileges as reviewer; not exploitable within this seat's privilege set.
- Duplicate-names, CRLF, junk-line, sim-rename probes were all executed but
  were spot-checks, not an exhaustive grammar sweep; the docstring/behavior
  mismatch claims above are grounded in these runs, not solely in source
  reading.
