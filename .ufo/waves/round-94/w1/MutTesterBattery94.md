# MutTesterBattery94 — round 94 w1 (C1 mutation attack)

Status: DONE (attack seat). Measured the freeze base (edc731a) and the candidate
(edc731a + ExecBatterySelfTest.patch, sha256 cbf44a34c6f99bf4ae3fb353c5e34fc34d4efc1567f67a1c3f29037991d04834,
matching ExecBatterySelfTest_READY). Candidate commit in scratch: c3de7869b5831ea980e8adc31cb1bbe77bb51da0 (scratch clone only).

Scratch: /fast/scratch/hyaku/kotoba-r94/MutTesterBattery94 (repo at edc731a; `git rev-parse --show-toplevel` checked).
Receipts (lane, this seat only): `.ufo/waves/round-94/w1/MutTesterBattery94/`
- `mutrun.py` (harness), `base-run.txt`, `candidate-run.txt`, `candidate-c1-counter.txt`,
  `forgery-c1-token-sniff.txt`, `forgery-token-sniff.patch` (sha256 4ca633b0…f8c80, scratch-only, NOT committed).

## Method
- Each new mutant is a literal substitution with its anchor count asserted, in a scratch clone's
  `verifiers/check_mutation_battery.py`; the unmodified self-test runs (`python3 -B … --self-test`);
  rc != 0 = KILLED (the counter's definition). Bytes restored and compared (`RESTORED identical=True`).
- None of these mutants is the frozen k0-k3; none is committed.

## Results on the candidate (c3de786): honest `0 failure(s) over 38 assertions`, rc 0

| id | mutant | base (edc731a) | candidate (c3de786) |
|---|---|---|---|
| N1 | committed manifest read at `HEAD` not `--rev` | SURVIVED | **SURVIVED** |
| N2 | off-by-one `n == want + 1` | KILLED | KILLED |
| N3 | kill count also counts `equivalent` rows | KILLED | KILLED |
| N4 | pin check moved after the probe loop | SURVIVED | **SURVIVED** |
| N5 | target-set CNE labelled `arm kill-set-size:` (rev path) | SURVIVED | **SURVIVED** |
| N6 | `pinned` argument ignored | KILLED | KILLED |
| N7 | accept fewer rows (`n <= want`) | KILLED | KILLED |
| N8 | malformed manifest accepted | KILLED | KILLED |
| N9 | rev path never refuses on the pin | KILLED | KILLED |
| N10 | accept exactly one added row (`n == want or n == want + 1`) | SURVIVED | KILLED (new k3 arms) |
| N11 | accept exactly two added rows (`n == want or n == want + 2`) | SURVIVED | **SURVIVED** |
| N12 | AST-level None-test inversion | KILLED by crash | KILLED by crash |
| N13 | equivalence control (`not (n != want)`) | SURVIVED (expected) | SURVIVED (expected) |

Of the 12 non-control mutants, 8 are killed by the candidate (N2, N3, N6-N10, N12) and 4 survive (N1, N4, N5, N11).
N10 is the one the candidate's new added-row arms newly kill; the other 7 kills were already present at base.

Candidate survivor details:
- N11 (accept exactly two added rows): the candidate's added-row arms append one kill row only (`+1`), so a
  pin that accepts `want + 2` is never tested. Gap in the new k3 arms (not in the frozen k3 `n >= want`).
- N1 (rev-head): every rev-path fixture has `rev == HEAD`, so reading the pinned manifest from HEAD is
  indistinguishable from reading it from `--rev`. Gap outside k0-k3.
- N5 (label on target-set refusal): the rev-path refusal `manifest must name exactly the targets` can be
  labelled `kill-set-size:` without any arm noticing. Gap in the label arms (k2 covers only the print site).
- N4 (check moved after probes): order is not observable in any fixture (the refusal is the same exit and
  line). Probably an equivalence in practice; recorded as a survivor, not a bug.
- N12 is a crash kill: a `TypeError` traceback (rc 1) counts as KILLED by the counter's rule. The kill is not a
  named behavioural arm. Counter-definition note, not a fix.

## Counter attack (scratch only): a comment-blind token sniffer meets C1 with no behavioural arm
- Forgery (scratch clone only, commit `3667124…` in scratch, never in the lane): a block at the end of `self_test()`
  that tokenizes the file's own code (`tokenize`, comment-blind) and fails on three forbidden token sequences: the
  k1 call shape, the k2 full CNE string, and the k3 `n >= want` tokens. The honest code contains none of them;
  the forbidden strings are split across literals.
- Run on the frozen counter: `python3 -B verifiers/fixtures/round-94/selftest-kills.py c1 3667124… <scratch repo>`
  → `honest rc 0: 0 failure(s) over 34 assertions`; k1/k2/k3/k0 KILLED; decoys k1/k2/k3 HELD (the decoy appends
  comments, which the tokenizer skips); `C1 targets killed 3 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3`;
  **`C1-PREDICATE-MET`, rc 0**.
- Finding (counter defect, L1 decision): the decoy guard catches only sniffers that read comment lines. A
  plain `tokenize` (or `ast`) sniffer of the instrument's code passes the decoy guard and meets the predicate. The
  plan's disclosed bound ("an AST-aware sniffer is out of its reach") understates this. Not rescued here: the
  predicate is frozen; any fix is an L1 addendum before a scored reading.
- The candidate's behavioural arms are real and satisfy C1 on their own (`C1-PREDICATE-MET` on c3de786); the
  forgery shows the counter would also meet the predicate without them.

## Not run (out of seat scope)
- The round-92 `controls-run.sh`, round-93 `c1-killpin-rev.sh`, the gate registry, and the tip battery are the
  L1's no-harm battery at landing. I did not run them. Frozen counter C1 is the only counter I ran on the candidate.

## Tooling
- No install performed. No pacman. No host-setting change. No kernel setting touched.

## Attribution
- Seat MutTesterBattery94 only. No lane commits. No writes to the lane tree except this report and receipts.
