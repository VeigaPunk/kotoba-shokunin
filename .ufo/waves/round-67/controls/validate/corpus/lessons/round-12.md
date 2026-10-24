# Lessons — round 12

Round: 12. Axis move: **consistency** (declared calibration sub-axis), 9 → 10.
Artifact half: `corpus/knowledge/independent-verification-round12.md`; machine half:
`verifiers/verify_corpus_independent.py` (second instrument) +
`verifiers/fault_injection_corpus.sh` (fault harness) + two repairs inside
`verifiers/verify_corpus_integrity.py`.
Landing hash: `assigned at landing`.

## Worked

- **A second *run* is not a second *witness*.** Round 11's cold run re-executed the
  author's script and spot-checked its numbers — useful, but it inherits whatever the
  script's *model* gets wrong. Round 12's lane derived the classes from the spec with its
  own tokenizer and counting code (`verify_corpus_independent.py`, 776 lines, 52-assertion
  self-test) and the two agreed on every count, shape and detail site in two worlds
  (green live; red on a clone at `d49dfa5` with the same ten dead-pointer sites). The
  agreement is evidence only because the paths were different.
- **The comparison paid for itself in the first hour.** Two claim/behaviour gaps in the
  author's script were named by the derivation rather than by its author: the docstring's
  quoted-context rule for report pointers could *never* fire (the tokenizer swallowed the
  opening quote — proven on a fixture world: quoted token counted dead before, context
  after), and the index census read column 2 of *any* table row in `corpus/README.md`
  while the docstring claimed the coverage-map section (measured difference today: 0
  tokens — a latent false-positive class, not a live number). Both repaired with self-test
  pins; live verdicts unchanged.
- **Counting claims are claims, and they were 24-deep stale.** A census of every counting
  claim in this repo's artifacts (84 rows, executed commands) found the round-11 landing
  had moved 24 numbers, 4 claims were false at HEAD, 9 were unexpressible, and one
  (round-10's "4 unindexed files") had no command at all. All live sites repaired; the
  unexpressible ones labelled. The sharpest of the four false claims was in `SHONEN.md`:
  the *command* printed in box 1 (`awk … END{print c[h]}`) prints one empty line and cannot
  produce the `13/9/9/8` it claimed — the fourth instance of the round-11 defect class, in
  the very file the round-6 audit used that expression to correct.
- **A claim site is a place, not a number.** Adding one checklist box (the second-witness
  rule) moved the box count 39 → 40 and the split to 14/9/9/8, which made ~6 live claim
  sites stale in one edit. The sweep updated every live site (`SCORECARD.md` rows,
  `corpus/README.md`, `SHONEN.md`'s embedded expected output, the two artifacts' gap lists)
  and adopted the rule that makes the rest defensible: **a per-round record keeps its
  round's value; a live document carries the current one.** That rule is now why
  `LOG.md`'s round-10/11 entries and `lessons/round-10.md` are not "stale" — they are
  records.
- **Faults belong in the repo.** Round 11's "10/10 planted faults surfaced" was
  unreproducible: the harness lived in `/tmp/round11`, wiped under disk quota. Round 12
  commits `verifiers/fault_injection_corpus.sh` (10 classes, one clone per fault, JSON
  assertions against **both** instruments, `--self-test` 4 probes, exit 0/1/2). Its table
  also exercises the repaired quoted-idiom (context 0→1, checked total unchanged) and
  answers the open question in `verifiers/corpus-baseline.json`.

## Did not work / rejected

- **Renaming `commit_total`.** The derivation showed the author's key counts hex-shaped
  citations while its name reads like "all citations" (the independent publishes both
  `commit_total` and `commit_hex_total`). Renaming would move the baseline key and three
  artifacts for a naming gain; instead the baseline note now states the exact scope. Cost
  beats clarity here — recorded, not repaired.
- **Rewriting historical records to remove "stale" numbers.** `LOG.md` is append-only by
  protocol and per-round lessons are records; a census that marks them stale is measuring
  the wrong property. The fix is the scope rule above, stated once, plus the round-12
  entry naming every count that moved.
- **Trusting agreement.** Both instruments share the class definition, so their agreement
  cannot see a token that *leaves the grammar*: labrat's fault (f) (a resolving pointer
  moved into `.ufo/round-4/`) is invisible to both, and only the `equal`-mode count
  detector notices (`report_total` 24 → 23), in default mode only. Two witnesses agreeing
  is not the same as two witnesses *covering*; the class boundary is now written down.
- **Round 11's "pointer-shape-only rewrite ≡ no-op" (incomplete).** True for a rewrite that
  stays inside the grammar; a rewrite that leaves it removes the token from the checked
  population. The round-12 reviewer narrowed the claim before it landed; the correction is
  recorded in the round-12 artifact rather than rewritten into the round-11 file.
- **The independent instrument's `missing_paths` first revision.** It path-checked a brace
  token unexpanded and reported `missing_paths=1` in both worlds; its own fixture
  assertion on brace tokens caught it before any world run. A derivation written from a
  spec inherits the spec's *ambiguities* (its METHOD.md names eleven) — that is the cost
  side of independence.

## Carry forward

- **Hermeticity**: 23 of 24 checked pointers are host-absolute, so a clone's green verdict
  depends on the host's `.ufo` tree (hidden → dead = checked, identically in both
  instruments). Repo-relative pointers remain the fix.
- **Coverage of the checkers**: `LOG.md`/`SCORECARD.md`/`SKILL.md` are outside both
  instruments' scan; the census walked them by hand this round, nothing will next round.
- **`SKILL.md`'s 40 checklist boxes** (14/9/9/8) are still only counted. Round 13's
  candidate (scratch plan, `/tmp/round12/PlanRound13/plan.md`, not an in-repo artifact):
  make one box executable (`skill.trigger.name_directory` — six of six lanes match today)
  with a missing-name fixture that must exit 1 while the live tree exits 0. Do not cite
  that plan as evidence until it lands in-repo.
- **Fault (f)** and the `equal`-mode reliance it exposes: the harness's own table is the
  evidence; a future round should decide whether out-of-grammar pointer rewrites deserve a
  check of their own (the count detector is the current answer).

## L2 lanes (12 this round; MISSION.md floor 8)

Batch 1 (one call, 8 lanes): `ExecIndependentVerifier` (the second instrument + its
comparison), `ScoutWorlds` (worlds and both instruments' exit codes), `LabratFaults` (the
committed harness + 10 fault classes), `CriticSpec` (attack on the claim before it landed),
`SentinelCross` (five cross-domain re-verifications), `ConnectorCross` (sibling overlap:
kengaku already ships a non-author oracle; two sibling stale-count defects routed),
`PlanRound13` (round-13 plan + axis-reconciliation recommendation), `ScoutClaimCensus`
(the 84-row counting-claim census). Batch 2 (one call, 4 lanes): `CriticRound12`
(adversarial read of the delivered instrument and the artifact), `ReviewerRound12`
(re-run both instruments on the landed tree, verify every citation), `ScoutReCensus`
(delta against the first census), `ReviewSHONEN` (non-author verdicts on boxes 1 and 3).