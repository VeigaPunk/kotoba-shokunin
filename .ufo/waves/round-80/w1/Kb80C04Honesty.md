# Kb80C04Honesty — Honest-stop audit of plans/round-80.md

Seat: Kb80C04Honesty (critic, honest-stop audit). Date: 2026-10-27.
Scope: plans/round-80.md read END TO END (all 63 lines; every display-truncated line
re-read whole via `:raw` — lines 10, 26, 28, 38). Method: enumeration of every
condition under which the round stops honestly, then a trigger walk per condition
(detector? declaring authority? declaration point? disposition?), then a completeness
pass for stop-shaped conditions the plan does NOT name. All claims grounded in plan
line numbers, receipt bytes, counter source lines, or grep exit codes named inline.
No gate was re-run; this is a plan-text audit, not a measurement.

Commands run (evidence discipline):
- `grep -n -i -E 'replacement|seat die|died|dies|dead seat|abort|halt' plans/round-80.md` → exit 1 (no match)
- `grep -n -i -E 'stop|kill|honest' plans/round-80.md` → exit 0, hits only lines 8, 20, 26, 28, 38, 40, 42
- read `.ufo/waves/round-80/receipts/tipbattery-base-dot.txt`, `m80-1-pipe-vs-direct.txt`
- `grep -n -E 'LINE_CAP|INSTRUMENT_PINS|instrument-pin|instrument-size|self.?test|__main__' verifiers/check_tip_battery.py` + `sed -n '700,760p'` of same
- `grep -n -E 'S22[6-9]|S23[0-1]' corpus/SOURCES.md` (rows 167–172; S229 = Microsoft Learn Agent Framework)
- cross-check of `.ufo/waves/round-80/w1-spec.json` seat prompts (orchestration layer; NOT plan text)

---

## 1. The enumerated condition set (every honest-stop condition the plan names)

| ID | Condition | Plan locus | Detector named? | Authority named? | Point named? | Disposition named? |
|----|-----------|-----------|-----------------|--------------------|--------------|--------------------|
| H1 | Any C1 control world W0–W7 reaches `6 of 6` | line 28 ("Any world reaching 6 of 6 is a counter or guard defect and stops C1") + line 26 kill rule | partially: worlds' expectations given; receipts "committed before any after-value" | NO | NO | NO |
| H2 | A repair needs a guard's *logic* edited | line 26 | NO (nothing mechanically diffs the counter; see G3) | NO | NO | "stops as an honest stop (no narrowing after data)" — stop semantics only |
| H3 | Repairs 4+5 land in instruments exceeding declared cap arithmetic (22 spent + 17 E04 + grammar ≤ 21 = 60) | line 26 | YES — `instrument-size` guard (LINE_CAP) + `instrument-pin` guard inside the counter; receipt tipbattery-base-dot.txt shows both live ("instruments added 22 / deleted 3 lines (cap 40)", "guard instrument-size PASS", "guard instrument-pin PASS") | L1 implied | the guard's own failure at the measured rev | "C1 stops as an honest stop" |
| H4 | Any C2 control the headline would misread as falsifying the form claim, or any world making the exit predicate lie | line 42 | partially: C0–C8 named with expectations | NO | NO | "is a counter defect and stops C2" |
| H5 | No narrowing after data; a world reaching target is reported as a counter defect, never repaired by narrowing | lines 26, 28, 42 | n/a (prohibition, not detection) | n/a | n/a | named as the boundary of every stop |

That is the COMPLETE set of stop conditions in the plan. Five. Everything else in the
plan is build/verify/receipt machinery with no attached stop.

## 2. Trigger walk — the four assigned probes

### P1. A control world reaches the target. Does the plan name WHO declares the stop, and when?

No. Line 28 says "stops C1"; line 42 says "stops C2". The declaring authority is never
named (the L1 is the sole committer and plan author, so authority defaults to the L1 by
silence — but silence is not a rule: a critic seat whose world reaches 6 of 6 could
equally claim the stop is already "declared" by the world itself, or hold it for the
report). The declaration POINT is never named: the worlds' receipts must be committed
"before any after-value", but the plan never says a stop may be declared only from
pre-after-value receipts — a world first constructed after seeing the repairs reaching
6 of 6 would trigger a stop under the literal text, which is exactly the
premature-saturation failure mode the rule exists to prevent. The DISPOSITION is never
named: nothing says the SCORECARD row for a stopped claim records `honest stop`, cites
the triggering receipt, and that the sister claim continues. **Gap G1.**

### P2. A seat dies mid-wave. "The plan says no replacement" — does it, and is the claim still verifiable with seat X dead?

False provenance, caught: the dispatch brief asserts "the plan says no replacement".
`grep -i -E 'replacement|seat die|died|dies|dead seat|abort|halt' plans/round-80.md`
returns **exit 1 — no match**. The plan is silent on seat death, replacement,
re-dispatch, and on which seats are load-bearing. The brief's sentence attributes to
the plan a rule the plan does not contain.

Verifiability analysis (my own, since the plan offers none): both frozen predicates are
exact commands over committed bytes — `python3 -B verifiers/check_tip_battery.py --rev
<rev>` and `python3 -B verifiers/check_allowed_tools.py --rev <rev>` — runnable by the
L1 with no seat alive; the L1 is the only committer; build outputs are derivable from
the r79 reviewed drafts (the seat spec sanctions derivation, but the plan does not). So
the claims ARE verifiable with any seat dead — including the BatteryRunner seat, whose
run-battery.sh already exists in build/ but whose absence would not void the predicate.
The only fatal seat is the L1 itself, which no plan clause can cover. The plan should
SAY this; today it says nothing. **Gap G2.**

### P3. The erratum diff exceeds its declared bounds. Is there a mechanical check?

No — and this is the strongest finding of the audit. The plan (line 14) declares E5 =
"`LINE_CAP` 40→60 and `INSTRUMENT_PINS` gaining exactly the two reviewed blobs named in
the freeze receipt, nothing else", and the freeze receipt records the amended counter's
sha256. A recorded sha256 is a record, not a check: nothing in the plan's named
commands diffs the round-72 counter bytes against the amended bytes and asserts the
hunk set. The counter is not one of the six battery instruments, so `instrument-pin`
does not cover it and `instrument-size` does not cover it. The counter DOES carry a
`--self-test` mode (check_tip_battery.py lines 464–713) that exercises the guards on
fixture worlds — but `main()` runs it only under `--self-test` (line 726), the plan
never names `--self-test` as a round step, and a normal `--rev` run never executes it.
So the kill rule H2 ("a repair needs a guard's logic edited") has no mechanical
tripwire anywhere in the round's named commands: a third line in the E5 diff that kept
all six gates green would sail through every check the plan names.

Two sub-defects compound this:
(a) The declared hunk set is under-specified against the counter's own bytes. The
    self-test arms hardcode cap-40 strings (line 522: `"FAIL guard instrument-size:
    instruments gain 41 lines > 40"`; line 559: `"instruments lose 60 lines > 40"`).
    Under `LINE_CAP = 60` a gain of 41 lines PASSES, so a correct amendment MUST touch
    those arm strings — the literal text "nothing else" forbids exactly the lines a
    correct patch contains. The V01C1 seat prompt resolves this ("exactly LINE_CAP +
    pins + in-step self-test arms"), but that is seat level, not plan text.
(b) Seat-level mitigations exist OUTSIDE the plan — V01C1 line-reviews the erratum
    diff, M02Battery mutates it (pin-table gain, LINE_CAP 500, BASE change, guard-logic
    flip, W0 expectation string), E16PinAudit recomputes pins, S15FreezeShas assembles
    the receipt. None of these is named in the plan, so none of them triggers the kill
    rule; if a seat skips its prompt, the plan as written does not notice. **Gap G3.**

### P4. The S229 page has moved semantically. Does any check notice?

S229 is the Microsoft Learn Agent Framework page (corpus/SOURCES.md row 170; the C2
table labels it msaf=experimental). No gate input reads a live page: the C2 counter
checks committed bytes — r79 snapshots (".ufo/waves/round-79/snapshots/, committed
bytes, re-verified pins", line 38), fetch records, rows, quotes. If Microsoft rewrites
the page so that `allowed-tools` is gone or means something else, the snapshot still
matches the committed bytes, every conjunct (a)–(i) still holds, and the frozen counter
still prints `documented 6 of 6` — the claim, being form-level over snapshots, is
computed as true while its factual premise has silently died. The plan's only live-page
machinery is "the six pages are re-opened live this round, receipt
.ufo/waves/round-80/w1/Kb80ReopenSix.md" (line 38): a seat REPORT. The ReopenSix seat
prompt does byte-compare live fetches against snapshots (fetch twice, record variance)
— so detection exists at seat level — but the plan names no disposition for variance:
nothing says a semantic move withdraws the row, drops N below 6, and stops C2; nothing
forbids quietly keeping `opened = 2026-10-27` on a moved page. **Gap G4.**

## 3. Completeness pass — stop-shaped conditions the plan does not name at all

- G5 Freeze ordering. The freeze receipt must land "before any after-value is
  measured", but no consequence is named if an after-value is measured first. The
  entire anti-M79 architecture rests on that ordering having teeth.
- G6 No-harm new redness. The no-harm battery (line 59) is named, and individual
  concerns are asserted inline (e.g. "must not move the sibling guard"), but no kill
  condition is attached: if the landed repairs turn a base-green gate red — a
  report-pointer failure at the report commit, a census DRIFT from the SOURCES.md
  edits, the floors gate tripping on the lesson text — the plan names no stop.
- G7 Exploratory rider review failure. The grant-semantics matrix's reviewers of
  record are "the round-80 non-author closure spot-check" (line 40). If that closure
  never reviews, or disputes the matrix, the SCORECARD row carries "the verdict and
  reviewer pointer" — but there is no verdict in that case, and the plan does not say
  the row records `unreviewed` rather than something that reads as approval.
- G8 Port failure at integration. The plan ports five reviewed r79 repairs and warns
  anchors may have drifted ("re-derive anchors from the CURRENT bytes" — dispatch
  brief), but names no rule for a patch that cannot be re-derived within the erratum
  bounds: is that H2 (guard logic)? a fresh stop? silently deriving anyway?
- G9 Base-clause deviation. The frozen predicate includes the base clause (`1 of 6`,
  exit 1). The receipt exists (tipbattery-base-dot.txt, `exit=1`, measured
  22:57:17Z). If a re-measurement ever disagrees — environment drift, sandbox shape —
  no disposition exists, yet every after-value is measured against that base.
- G10 Round-level semantics. Claim-level stops are declared; the plan never says the
  stop of C1 does not stop C2, or what a double stop means for the round.
- G11 Control expected-value deviation. Worlds carry expectations (W1 ≤3 of 6, etc.).
  A world scoring 4 of 6 — inside the target band's complement yet outside its
  expectation — breaks the plan's load-bearing attribution ("proves repairs 4+5
  load-bearing") without triggering anything; the expectation table is the kind of
  thing that gets silently "corrected" after data, which is narrowing by the back door.

## 4. Proposed plan amendments (verbatim-adoptable; one per gap)

A1 (G1, P1) — append to both kill-rule paragraphs:
"Stop authority and point. Every honest stop in this plan is declared by the L1 alone,
in the stopped claim's SCORECARD row, as `honest stop (<trigger>, receipt <path>)`, and
only from a receipt committed before any after-value was measured; a world first run
after an after-value is advisory, not a trigger. No seat may declare or retract a stop.
A stop of one claim never stops the other; both claims stopped is a round-level honest
stop recorded the same way, and the round's lesson records the stopped predicate
verbatim."

A2 (G2, P2) — new paragraph under § Round shape and seats:
"Seat death. Seats are anonymous workers and no seat is replaced. No seat is
load-bearing for verification: both frozen predicates name exact commands over
committed bytes that the L1 can run without any seat. If a seat dies or stalls, the L1
either completes its build output by deriving it from the round-79 reviewed drafts
(naming the derivation in the receipt) or proceeds without it; the frozen predicates
and kill rules are unchanged and the wave is never re-dispatched. L1 incapacity is the
only terminal event and is outside this plan's authority."

A3 (G3, P3) — replace the parenthetical bounds in the C1 kill rule with:
"Erratum bounds, mechanically checked before any after-value: the unified diff between
the round-72 frozen counter's bytes and the amended counter's bytes is computed
(`git apply --numstat` of the E5 patch, or `git diff --no-index` of the two byte
streams) and must touch exactly: the `LINE_CAP` line; the two `INSTRUMENT_PINS`
additions; and the self-test arm strings whose expected cap text depends on `LINE_CAP`
— and nothing else. Any hunk outside that set is a guard-logic edit and stops C1 under
the kill rule above. The no-harm battery gains one command run on the amended counter:
`python3 -B verifiers/check_tip_battery.py --self-test`, exit 0 required. The
freeze receipt's sha256 is a record; these two checks are the tripwire."

A4 (G4, P4) — append to the C2 measured-part paragraph:
"Live re-open variance. If a live re-open of S226–S231 disagrees with the committed
snapshot — byte variance that survives a double-fetch, or a semantic move (the page no
longer documents `allowed-tools` as the row asserts) — the surface is not 'opened this
round': the L1 records the variance in the lesson `## Gate`, withdraws or marks the
affected rows, and if N < 6 at the measured tip the frozen predicate is not met and C2
stops as an honest stop. Surviving rows are never re-promoted to N = 6 after data."

A5 (G5) — one sentence in the freeze sentence:
"An after-value measured before the freeze receipt is committed is void: it is re-run
after the freeze, both receipts are kept and named in the lesson, and a second such
measurement is recorded as a process defect in the SCORECARD process row."

A6 (G6) — append to § No-harm battery:
"No-harm kill condition. If the final pre-report battery shows a gate red that was
green at base and is neither named red in § Trigger nor repaired by the declared repair
set, the claim whose files touched that gate stops as an honest stop; if no claim owns
the redness the round stops at the report commit with the redness named. New redness is
never repaired improvisationally mid-round; it is routed to the next plan."

A7 (G7) — append to the exploratory-part paragraph:
"Rider disposition. If the non-author closure spot-check does not review the
grant-semantics matrix, or disputes it, the SCORECARD row records `unreviewed` or
`disputed (<pointer>)` — never a verdict — and the measured part of C2 is unaffected;
the exploratory part cannot stop, and cannot pass, the measured part."

A8 (G8) — one sentence in § C1 repair set:
"If a reviewed repair cannot be ported to the base — anchors drifted, blob absent — the
L1 re-derives it from the round-79 reviewed drafts against the current bytes and names
the re-derivation in the receipt; a repair that cannot be re-derived within the erratum
bounds stops C1 under the guard-logic kill rule."

A9 (G9) — one sentence in the C1 frozen predicate:
"If a re-measurement of a base value recorded in § Trigger disagrees with the recorded
value, the round stops at the report commit with both receipts named: a frozen
predicate whose base clause does not reproduce measures nothing."

A10 (G11) — append to the control-worlds sentence:
"If a control world scores outside its declared expectation — either side — the
load-bearing attribution the plan asserts is wrong; the world is reported as a counter
defect and the L1 either names the additionally-load-bearing repair in the lesson or
stops the claim. The expectation table is never corrected after data."

## 5. What is already sound (do not over-correct)

- H3 is fully armed: instrument-size and instrument-pin are mechanical, exercised, and
  the receipt at base shows all five guards PASS with the counter's own self-test arms
  verifying the guard worlds (counter lines 521–559, 660–698). The cap arithmetic
  (22+17+≤21=60) is checkable by the named predicate alone.
- The both-forms requirement (`--repo .` and absolute) closes the M127 class of
  sandbox-shape bugs; the base receipt shows the predicate was actually measured, not
  asserted.
- The M80-1 fix is in place with a two-form receipt (m80-1-pipe-vs-direct.txt:
  pipe-rc=0 vs direct-rc=1 for the same gate) — the measurement-honesty lesson is
  operationalized, not just mined.
- The no-narrowing clauses (H5) are correctly placed on every stop.
- C2's split (measured form backbone / exploratory semantics with named reviewers of
  record) is the right shape for an axis that must not launder judgement through a
  counter; the gaps found are about dispositions, not the split itself.

## 6. Counterexample summary (strongest available from local evidence)

Strongest single counterexample to "the plan's kill rules trigger on the named
conditions": amend the E5 diff with one extra line — e.g., delete the
`no-deletions` guard's `failures.append` call and print `guard no-deletions PASS`
unconditionally, keeping pins and size inside bounds. Every gate stays green, all six
battery gates pass at a laundering tip, `guards 5 of 5` prints, the plan's named
commands notice nothing (the counter is unpinned, un-diffed, and its `--self-test` is
uninvoked), and the round lands `6 of 6` on a counter whose guard logic was edited —
the exact event H2 declares an honest stop, with no tripwire. Only seat-level prompts
(V01C1, M02Battery) stand between this world and a false claim, and the plan binds no
seat to them. A3 closes it with two commands and no new code.

VERDICT: 5 plan-named stop conditions audited — 1 fully armed (cap arithmetic), 4 missing authority, tripwire, or disposition; all 4 assigned probes confirm real gaps incl. one false-provenance finding (the plan never says "no replacement", grep exit 1) and one unarmed kill rule (E5 diff bounds: unpinned counter, uninvoked --self-test); 10 verbatim amendments proposed as the smallest safe corrections.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80C04Honesty.md
