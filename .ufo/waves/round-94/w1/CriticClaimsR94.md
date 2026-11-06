# CriticClaimsR94 — falsify the frozen claims against the full candidate (round 94, w1)

Status: final. Candidate built from the four READY patches; all counters and companion checks run;
scratch removed before yield.

## Candidate

- Built by `git apply` of the four READY patches onto `edc731a91a956f6df20c27a74fb981b286f6ba58`, order:
  ExecBatterySelfTest, ExecTipSelfTest, ExecReceiptHeaders, ScribeCorpusR94. Each patch's sha256 matched the
  READY file: ExecBatterySelfTest `cbf44a34…4834`, ExecTipSelfTest `726e15b9…83d7`, ExecReceiptHeaders
  `5c3f3763…f974`, ScribeCorpusR94 `b5b2c9cd…57f3`.
- Candidate commit (scratch identity, scratch clone only): `8bb6f7202af58af24ad9346f34e3735e92687142`.
- Changed paths: `verifiers/check_mutation_battery.py`, `verifiers/check_tip_battery.py`,
  `verifiers/fixtures/round-93/check-receipt-revs.sh`, `verifiers/fixtures/round-94/receipt-headers/`,
  `corpus/SOURCES.md`, `corpus/lessons/round-94.md`, `corpus/README.md`.
- Causal separability holds on the candidate: the C1 surface is only `check_mutation_battery.py`; the C2
  surface is only `check_tip_battery.py`.

## Pre-data receipts reproduced (same counter, scratch REPO clones)

| receipt | my run | result |
|---|---|---|
| do-nothing c1 @ 4d3e8e4d | `C1 targets killed 0 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3`, `C1-PREDICATE-UNMET`, rc 1 | matches `redbefore-c1-base.txt` line for line |
| do-nothing c2 @ 4d3e8e4d | `C2 targets killed 0 of 2; positive killed 1 of 1; honest rc 0; decoys held 2 of 2`, `C2-PREDICATE-UNMET`, rc 1 | matches `redbefore-c2-base.txt` |
| forgery c1 (`forgery-sniff.patch` @ 4d3e8e4d, committed) | `targets killed 3 of 3; positive 1 of 1; decoys held 0 of 3`, `C1-PREDICATE-UNMET`, rc 1 | matches `forgery-c1-run.txt` |
| forgery c2 | `targets killed 2 of 2; positive 1 of 1; decoys held 0 of 2`, `C2-PREDICATE-UNMET`, rc 1 | matches `forgery-c2-run.txt` |

## Candidate readings @ 8bb6f72

- **c1:** `C1 targets killed 3 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3`,
  `C1-PREDICATE-MET`, rc 0. Honest `0 failure(s) over 38 assertions`. k1 KILLED (1 failure), k2 KILLED (3),
  k3 KILLED (2), k0 KILLED (4).
- **c2:** `C2 targets killed 2 of 2; positive killed 1 of 1; honest rc 0; decoys held 2 of 2`,
  `C2-PREDICATE-MET`, rc 0. Honest `self-test: 0 failure(s) over 102 assertions`. p1 KILLED (keydrop-4 world),
  p2 KILLED (keydrop-0 world), p0 KILLED by the new keyswap "names only that key" arm.
- Round-92 `controls-run.sh` on candidate: `shortcuts refused 2 of 2; honest held 2 of 2`, rc 0.
- Round-93 `c1-killpin-rev.sh 8bb6f72`: `honest world 8bb6f72… rc 0 names kill-set-size no: yes`,
  `C1-PREDICATE-MET`, rc 0.
- Round-93 `c2-pinkey.sh 8bb6f72` (no deadline; the first attempt hit my 1800 s cap, so the run is slow, about
  17 min): `C2-PREDICATE-MET`, rc 0.
- Mutation battery `--self-test` on candidate: `0 failure(s) over 38 assertions`, rc 0. Tip battery
  `--self-test`: `self-test: 0 failure(s) over 102 assertions`, rc 0.
- Receipt check on round-93 landing receipts (candidate script): `4 scratch-declared`, `malformed declarations: 0`,
  `9 resolved, 0 unresolved over 19 files`, rc 0.

## Verdicts

- **C1 (depth), on candidate: MET.** The counter reads MET. I read the three new arm groups in the diff:
  `kill_set_check` on a dirty working-tree manifest (k1), labelled-refusal output checks (k2), and
  `run_evaluate` on a committed manifest with one appended kill row (k3). Each runs the checker on a fixture
  world and reads exit code and output, so it is behavioural, not sniffing. The counter's MET alone is weaker
  evidence than that: see D4 and D8.
- **C2 (consistency), on candidate: MET.** Keydrop per BATTERY key plus keyswap; each world runs the tip battery
  and checks the named FAIL line. Behavioural. Label: see D6.
- **Mined-mistake receipt-header fix: UNMET as stated.** The plan says such lines "are reported MALFORMED and exit
  1". The committed fixtures behave as stated (`good` rc 0, `hex41` rc 1, `indented` rc 1), and the round-93
  landing receipts still read `9 resolved, 0 unresolved`, rc 0. The same fail-open class survives in two shapes
  the fixtures do not cover (D1, D2).
- **Do-nothing and cheaper change:** the do-nothing change is UNMET on both targets, as pre-registered. A cheaper
  route to the counter's MET exists through a comment-skipping sniffer (D4). I did not search for cheaper honest
  changes exhaustively.

## Defects

- **D1 (fix, high) — fail-open on a scratch-tagged malformed header.** `check-receipt-revs.sh` applies the
  `scratch_line` exemption before the malformed check. A line with a 41-hex `REV=` and the token `forgery` or
  `/scratch/` is dropped silently: not counted as scratch, not reported MALFORMED. Reproduced: a directory with
  `good.txt` = `REV=4d3e…919` and `scratchy.txt` = `REV=4d3e…9190 forgery` → `0 scratch-declared`,
  `malformed declarations: 0`, `1 resolved, 0 unresolved over 2 files`, **rc 0** (false green). This is the
  mined mistake's own class.
- **D2 (fix, high) — a second declaration on a header-matched line is never examined.** The malformed branch runs
  only when `header.match(line)` fails. `REV=<40hex> REV=<41hex>` → `1 resolved`, `malformed declarations: 0`,
  **rc 0**.
- **D3 (fix, medium, residual scope) — header-shaped lines outside the line-start pattern are invisible.**
  `receipt: REV=<41hex>`, `rev=<40hex>`, `REV: <40hex>`, `rev<TAB><40hex>` and `- REV=<41hex>` yield no MALFORMED
  and no resolution (rc 2 alone; silently dropped in a mixed directory). The fix's own shape definition is
  line-anchored, so this is bounded, not a broken promise. The plan should name the bound.
- **D4 (counter, high) — the decoy guard is bypassed by a comment-skipping text sniffer; the plan understates the
  bound.** Forgery `ade2c02c` (candidate plus a self-test prelude that reads `Path(__file__)`, drops lines starting
  with `#`, and returns 1 when a mutant token appears in code): c1 reads **`C1-PREDICATE-MET`, rc 0** (k1, k2, k3,
  k0 KILLED; honest rc 0; decoys held 3 of 3). The plan's §Disclosed bounds says "an AST-aware sniffer is out of its
  reach"; the counter header says "a sniffer that skips comments (e.g. AST-based) is not caught". A plain line filter
  is a text sniffer, not AST, and it passes. The predicate is satisfiable by a forgery. Not fixed here: frozen
  predicate, FINDING only.
- **D5 (counter docs, low) — stale positive attribution.** The counter header says the positive `p0-skip-last-key`
  is "killed by the existing BATTERY[5] arms". On the candidate it is killed by the new keyswap "names only that key"
  arm. The kill counts; the narrative is out of date.
- **D6 (claim label, low) — C2 "consistency (calibration sub-axis)" has no calibration evidence.** The change adds
  per-key self-test arms: parity between BATTERY and INSTRUMENT_PINS, which fits "consistency". Nothing measures
  calibration. The surface is the same self-test-depth family as C1. Drop the calibration sub-axis or argue it.
- **D7 (lesson Gate, low–medium) — S269 overreaches on timeouts.** The lesson says S269 grounds "the separate
  `Non viable` and `Timed Out` classes, which is why a mutant … is could-not-evaluate and never a kill". The captured
  page (12155 B, sha256 `c51d8423…2b92b3a`, matching the row) defines Killed as "a test caught the mutation", and
  says only "A mutation may time out if it causes an infinite loop". It does not classify a timeout as not-a-kill.
  The rule is the counter's choice. The row's digests and quoted lines do match the captured bytes.
- **D8 (counter, high) — KILLED is `rc != 0`, so a run error scores as a kill.** The captured S269 page lists `Run
  error` as its own class: "something went wrong when trying to test the mutation". Probe `375b0d67` (candidate
  plus a sniffer that raises `RuntimeError` instead of returning 1; receipt `CriticClaimsR94/c1-runerror-probe.txt`)
  reads **`C1-PREDICATE-MET`, rc 0**: all four mutants reported `KILLED: RuntimeError: r94 probe: the self-test run
  itself failed`. A crashing mutant satisfies the predicate. The counter should require the self-test to report a
  failure, not just a non-zero exit. Not fixed here: FINDING only.

## Attack list

- Pre-registered forgery: caught (decoys 0 of N). A comment-skipping sniffer passes (D4). A raising sniffer passes
  (D8).
- Mined-mistake fixtures: `good`, `hex41`, `indented` behave as stated. The fix fails on the D1 and D2 shapes, which
  the fixtures do not include (fixture coverage gap).
- S269: digest and quoted lines match the captured bytes. Its grounding is partial: it supports the Killed
  definition and the non-viable class, not the timeout rule (D7), and the run-error-as-kill rule runs against its
  own Run error class (D8).
- Lesson Gate: rejected candidates (mutmut, Cosmic Ray) have digests matching the scout captures. A same-round
  reject is recorded.

## Receipts (this seat)

Under `.ufo/waves/round-94/w1/CriticClaimsR94/`: `c2-pinkey-candidate.txt`, `tip-selftest.txt`,
`mut-selftest.txt`, `receipt-r93-candidate.txt`, `c1-runerror-probe.txt`. The receipt-fixture checks were run in
the scratch candidate and are recorded above.

## Verdict summary

| claim / item | verdict on 8bb6f72 | notes |
|---|---|---|
| C1 battery self-test kills k1-k3 | MET (counter rc 0; arms behavioural) | D4, D8: the counter predicate is satisfiable by forgeries |
| C2 tip self-test covers six pin keys | MET (counter rc 0; arms behavioural) | D5, D6 |
| receipt-header fail-closed fix | UNMET as stated | D1, D2 (fail-open persists); D3 bounded |
| S269 PIT row | row is faithful to the captured bytes | D7 overreach on timeout rule |
| pre-data receipts reproduce | yes, line for line | — |

## Post-candidate note (read-only re-check of the lane's working tree)

The lane's working tree (uncommitted, L1 addendum 1 A1) repairs D1 and D2. I re-ran the D1/D2 probes read-only
against the lane's current `check-receipt-revs.sh` (scratch probe dirs, removed): `good` rc 0; `REV=<40hex>` plus
`REV=<41hex>` on one line → `MALFORMED … a further declaration on the header line has hex run 41` rc 1;
`REV=<41hex> forgery` → `MALFORMED … scratch-tagged hex run is 41` rc 1; the good file combined with the
scratch-tagged 41-hex file → rc 1. Committed fixtures `hex41`, `indented`, `hex39`, `scratch-hex41`,
`double-decl` all rc 1. The repair was not in the candidate I scored (`8bb6f72`), so the table's receipt-fix row
remains UNMET **as scored**; the repaired shapes read correctly on the working tree. D3 stays a stated bound (A1 says so).

D8 (KILLED = rc≠0 conflates a run error with a kill) is NOT addressed by addendum 1 and remains open: the counter
still scores the `375b0d67` raising probe as C1-PREDICATE-MET.

D4 (comment-skipping sniffer passes the decoy guard), D6 (C2 label), D7 (S269 timeout overreach) are disclosed in
addendum 1 A2–A4 and match my findings.
