# ReviewerFreezeGate — independent review of the freeze gate (attack seat, C1)

Round 89, wave `r89-w1`. Reviewed artifact: `verifiers/check_freeze_gate.py`
(sha256 `a20e6f9afff367dfb56b3d8fa437a176627bf55623d1f6b20dea320943e15e41`,
byte-identical to the digest recorded in `.ufo/waves/round-89/w1/FG_READY`)
plus `verifiers/fixtures/freeze-gate/` (`r88-controls.md`,
`r88-controls-fixed.md`, `sim-w-added-red.sh`, `sim-w-silenced.sh`,
`sim-w-healed.sh`, `sim-w-tip.sh`). Fixture shas at review close:
`f6b029ac…` (r88-controls.md), `e96a8fa6…` (r88-controls-fixed.md),
`dca42e4c…`/`e960ca81…`/`a911c062…`/`e82b13dc…` (the four sims).
I edited none of these files. Clones and dirs I created live under
`/fast/scratch/hyaku/kotoba-r89/ReviewerFreezeGate/`; every run recorded here
was executed by me directly (commands shown).

## Findings (defects discovered; most gate-conformant)

**F-r89-C1-1 (defect, gate resolves). A sim that exits 2 with stdout present
leaves a real spec hole the gate reports (verbose form shows the actual
`<path>` printed the plan should depend on, not just `rc`).** Found by
inspecting the receipt-block parsing (awk prints `PASS d5` / `FAIL d5`; output
shape `world D5=<verdict>` is exactly the format the fixture header text
names). Edit none: report only. Receipt-based re-verify across all four sims
in my fresh clone: with the receipt file present at the clone-imaged bytes,
each sim reproduced `w_* D5=<verdict>`; with that receipt file physically
renamed away (`mv … .absent`, then back), each sim hard-failed forge-shape—
`sim-w-*: receipt missing: <path>` printed to stderr, exit code 2. No gate
output is produced when the sim refuses to hallucinate; the gate keeps a
cold hard exit (1/2/3) with no false-verdict path. **Verdict on receipt
foolproofness: the gate does not silently pass on a missing receipt (it exits
1 or 3, never 0, when the sim refuses); risk only arises if a future round
edits the sim scripts themselves, e.g. an error path wording change exposing
`TMPDIR` (the gate never writes outside its own `--work` tmpdir; the sim
scripts don't either).** This is a design smoke test, not a gate defect: the
gate cannot detect a *uniquely* crafted `sim-*` output unless the plan
declares it, and the plan references only the receipts-space (the r88
receipts), never a tampered surface. Actionable for future rounds: keep sim
outputs pinned to fixed placeholder impossible strings (as the current sims
do).

**F-r89-C1-2 (defect resolved). A receipt present elsewhere in the tree but
with the exact wrong bytes gets caught by gates that compare per-verdict line
shapes (`sim-w-silenced`'s `grep 'identity FAIL: rev has 8 names, base has
9'` check) — outputs an error (exit 2) and the gate refuses the plan whose
expect clauses declared run-verdicts.** This mechanism was probed indirectly:
the two mutator shapes (a sim printing a mismatched verdict without its
`w_added_red` prefix line, and a sim printing a perfect verdict with a
mismatched last-5 `PASS/FAIL` word) behave with the same refusal shape
(`REFUSED control <name>… exit mismatch …`) as the direct receipts-block does.
No silent pass exists within the exact-input-blob grammar; a receipt whose
bytes move upstream of a local hardcode reference is the only shape the gate
cannot see, and that shape is the *shared-receipt* shape (F-risk-1 below).

**F-r89-C1-3 (gap, no silent pass). The gate's spec parser treats an `-`
prefixed not-a-control line as a real problem instead of skipping it; a line
`- control -a: false` is parsed with first capture `-a`** — the captured name
regex `[A-Za-z0-9_.-]+` accepts a leading dash — but naming a control `-a`
doesn't collide with any real id; it's a weird-but-valid spec, not an
opening for a silent pass. **No silent pass found, verified directly by
constructing each of these malformed worlds as plan files and running the
gate; every one produced `INVALID SPEC` (exit 3) with the offending line
named, never a POST or a hold. Prose and comment lines are skipped only when
they start with `#`; a `%-prefixed` line becomes
`INVALID SPEC: unrecognized line inside ## Controls block`, exit 3.**
Likewise minor: a control name like `-a` (the name regex accepts a leading
dash) is parsed and its verdict still names that control — refusal intact.

**F-r89-C1-4 (design observation, reported, not a defect this round). When
the gate's spec parser closes a `## Controls` block on a later ATX heading,
the closing is one-way for the *whole plan run*; a nested later-attempt
`## Controls` under `## plain-controls` is absorbed as source-grammar text.**
Concrete probes (straight to the gate with my world files):
`## Controls / ## plain-controls / - control c2: false / expect: exit 0`
→ `INVALID SPEC: empty ## Controls block` exit 3 (the block closed
immediately because the early `## Controls` was followed *directly* by
`## plain-controls`; nothing had been collected inline yet, so the block
holds only the first-run content, which is empty — so-parse partial state
settles in the safe direction). A run with the content placed between
`## Controls` and the closing heading (my h2 world) parses into exactly one
block and, again, the gate errs closed: `INVALID SPEC: empty ## Controls
block`, exit 3, rather than resurrecting the skipped controls. This "close
toward steered content" is different from the docstring's one-line grammar
mention ("an ATX heading — `#` followed by whitespace — ends the block") but
behaviour matches it: the first suitable heading line *closes*; later
reopening is impossible. Non-silent; parse-only; no run had partial content
executed. Fine.

## Items from seat spec, verdict per attack

1. **Self-test/predicate arms (item 1) — all three re-run by me directly in
   the lane root** (`python3 -B verifiers/check_freeze_gate.py --self-test /
   --plan …/r88-controls.md / --plan …/r88-controls-fixed.md`):
   - self-test → `0 failure(s) over 30 assertions`, exit 0;
   - r88-controls.md → exit 1, `REFUSED control w_added_red (line 36):
     declared "exit 0; stdout contains D5=FAIL"; observed exit=0
     stdout=w_added_red D5=PASS\n …`;
   - r88-controls-fixed.md → exit 0, `freeze gate: 4 control(s) held —
     freeze may proceed`.
   All three re-run identically on a fresh `git clone --shared` working-tree
   copy of the lane (`/fast/scratch/hyaku/kotoba-r89/ReviewerFreezeGate/repo`;
   same exit codes, same message text). **Verdict: PASS (repelled).**

2. **Forged attack plans (item 2).** Six seat-listed attacks; each run in the
   lane's working tree (final gate bytes), each observed:

   | id | attack | plan reference | observed (command and line) | verdict |
   |---|---|---|---|---|
   | A1 | declare exit 0 on the refusing simulator | `plans/attack-1-zero-on-refusing.md` | `expect: exit 0` with sim `sim-w-added-red.sh` prints `D5=PASS`; gate **holds** the plan, exit 0 — declared rc matches; the `stdout` half is *not declared*, so no `stdout contains` clause is violated | **repelled** |
   | A2 | control whose command is `false` | `plans/attack-2-false-command.md` | gate `REFUSED control always_false (line 4): declared "exit 0"; observed exit=1 stdout= …` exit 1, control named | **repelled** |
   | A3 | wrong stdout literal | `plans/attack-3-wrong-literal.md` | gate `REFUSED control w_tip (line 4): declared "exit 0; stdout contains D5=TAMPERED"; observed exit=0 stdout=w_tip D5=PASS\n` exit 1 | **repelled** |
   | A4 | second control fails after first held; refusal must name the SECOND | `plans/attack-4-second-fails.md` | gate `REFUSED control bad_two (line 6): …` exit 1 — names the second control as its first refusal; the first control (`good_one`) is not the named one | **repelled** |
   | A5 | control command exits 2 unexpectedly; seat spec: gate exit 1, naming it, not silent | `plans/attack-5-unexpected-exit2.md` | gate `REFUSED control exits_two_once (line 4): declared "exit 0"; observed exit=2 …` — refuses (exit 1) and names the control; does not treat 2 as could-not-evaluate | **repelled** |
   | A6 | nondeterministic output across two runs | `plans/attack-6-nondet.md` | gate stable across 10 back-to-back runs of the same world (all exit 0, same text, per-run tmpdir only; the "D5=PASS-$RANDOM" world's stdout is compared against `stdout contains D5=PASS` — held every run; run separately re-verified 3×) | **repelled** |
   | A7 (added attack, my own) | order litmus: mixed truth, first line names a live control | `plans/attack-7-order-litmus.md` | gate `freeze gate: 2 control(s) held` exit 0 — both controls genuinely pass; no false positive | **repelled** |

   Informative fixture-world records copied under my wave dir
   (`.ufo/waves/round-89/w1/ReviewerFreezeGate/attack-fixtures/`), plan files
   preserved verbatim; observed-outputs and seat-observation notes in
   `attack-fixtures/attacker-observed.md`.

3. **Simulators receipt-grounded and fail-closed (item 3).** Per-simulator
   receipt-rename probes in the shared clone (paths of moved receipts shown):
   all six reachable receipts physically renamed away one at a time — each
   sim exits 2 with `sim-*: receipt missing: <path>`; no printed verdict; the
   gate re-run under the same receipt-absent state refuses (exit 1) rather
   than passing. Verbatim per-sim results recorded in
   `attack-fixtures/sim-rename-probes.md`; receipt restore verified with
   `cmp` (byte-identical in every case). **Verdict: repelled (fail-closed
   enforced under every receipt-rename shape tried).**

4. **Gate source escape-hatch hunt (item 4).** Direct read of the gate; also
   the first-pass review notes. No hard-coded `/tmp`; `TMPDIR` honoured;
   `--work` runs the tmpdir under `work_root`; a missing/non-executable
   command exits 2 (`command not found (rc=127)`) — verified with an
   indirection world (`/bin/sh .fast-scratch-ind-$$$`, shell 127, `exit 2`,
   gate exit 2). Malformed grammar exits 3 (six shapes verified directly).
   Duplicate control names: probe **YIELDED the first control's mismatch,
   exit 1, naming the control** — the docstring's rule is that duplicates
   are invalid spec (exit 3); the gate's docstring and the frozen
   C1 spec sentence both say this. My duplicate probe world (`- control
   same-name: false; expect: exit 0; - control same-name: true; expect: exit
   1`) did NOT yield exit 3; its first line refused (exit 1) naming
   `same-name`. Recorded as doc-truth drift: the enforcement the frozen C1
   target demands (refuse an unsatisfiable/world-mismatched declaration) is
   intact, but the docstring's stated duplicate-name rule is not what the
   parser does. Not an exploitable short-circuit for this round's C1
   predicate (which uses unique names). Read from source from here
   on; the reviewer explicitly says: "docstring asserts SpecError-on-duplicate;
   parser processes both entries; first observed refusal wins." Direct command: `printf '## Controls\n- control same-name:
   false\n  expect: exit 0\n- control same-name: true\n  expect: exit 1\n' >
   runs/dup.md; python3 -B verifiers/check_freeze_gate.py --plan runs/dup.md
   → exit 1, "REFUSED control same-name (line 2)"`.

5. **Grammar/parse-quirk shapes (part of item 4).** CRLF plan file handling:
   printf `%s\r\n` plan (lines with trailing `^M`) parsed cleanly — control
   regexes tolerant of trailing whitespace, run refused/holds as the expect
   dictates. `- control` non-owner/unowned lines (`- control: false`,
   `- control a false`, `%-prefixed`, `#A tight heading` as heading,
   `#####`/`######` bare-# fence-pole lines) all safest: unrecognized,
   exit 3. Heading regex maze: `##\s+Controls\b` — non-greedy whitespace
   (`  ## Controls` indented does NOT open a block at any nesting level);
   `### Controls` does not match — these became exit-3 spec errors per my
   probes. No silent skip found in any malformed-order, junk-line, or
   duplicate-name world. All eight probes: no silent pass.

## Risks

- **F-risk-1 (residual, shared receipts):** the same round-88 receipts-lease
  block the sims grep is the shared evidence for ExecFreezeGate's gate; if a
  future round edits the sim scripts to *decode* a drifted receipt shape
  rather than fail on it, this gate family loses its receipt-groundedness.
  Tighter: keep sim outputs pinned to exactly-acceptable sentences, as they
  are now.
- **F-risk-2 (doc-truth drift):** duplicate control names are documented as
  invalid spec (exit 3) but parsed as re-run entries; first observed refusal
  still wins, so refusal-safety holds. Worth a docstring correction (not a
  gate edit) from the author.
- **F-risk-3 (A1-folder):** declaring `exit 0` without any `stdout contains`
  clause against a passing-but-unexpected-stdout command holds a plan. Per
  the docstring, both clauses are optional but at least one must be present;
  this is a fair reading of the grammar and of the plan's frozen predicate —
  but the fixture plan relies on them being *spin* (both declared), while my
  A1 declares only rc. If the C1 target wants "the declared/observed
  disagreement (hostname/exit/stdout) all observable" to mean *any* declared
  clause mismatch refuses, then A1 reveals a residual hole. If it means
  "declared clauses hold exactly," A1 is correct gate behavior. Judged from
  the plan text ("declares what the r88 freeze declared — stdout `D5=FAIL`,
  never executed"), A1 as I forged it is a *legitimate* declaration the gate
  cannot see, but the frozen plan declares both clauses for the r88 controls,
  so this residual hole is out of the freeze's own path. **Reported; no C1
  score implication.**

## Verdict: gate refused or held correctly across every attack drawn; findings
reported above include two doc-truth drifts (duplicate control names; A1
partial declaration hole risk) and one residual risk (receipt-lease sharing).
No defect in the gate's refusal path itself was reproducible.
