# FalsifyQ57 — wave-2 attack on `corpus/QUALITY.md` Q57 (erratum-absorption criterion)

Seat: `L1kotoba62.FalsifyQ57` (reviewer, falsify). Scope: the Q57 row text, its
citations (M93, the C1 matrix), the clause-ownership line vs Q34/Q35/Q36/Q56, and the
criterion's verdict on the E2f survivor. Lane tip audited: `e6da78bbe420722dd18a13182a7c4b64ce02f005`
(`git show e6da78bb:corpus/QUALITY.md` line 68 identical to worktree; Q57 landed in
`e6da78b` per `git log -1 --format='%h %s' -- corpus/QUALITY.md`).

## Row text under attack (QUALITY.md:68, verbatim)

```
| Q57 | An erratum (or any amendment) counts as absorbed only when each fresh attack
instance of its class is rejected by the landed instrument and disabling that
erratum's guard in-process admits that same instance; a plan-text attack does not
establish absorption, and the receipt names both verdict directions and the disabled
guard. | erratum/amendment absorption claims and their receipts | M93 `erratum
recorded as absorbed without an arm-level receipt` (`corpus/lessons/round-62.md` §
Mistakes); C1 matrix (`.ufo/waves/round-62/controls/absorption-hollow.txt:16-27`;
`python3 -B verifiers/check_erratum_absorption.py --self-test`). Clause ownership:
Q34 owns SOURCES append-only claims; Q35 owns verifier inventory and `SKILL.md`
gate-registry/self-test declarations; Q36 owns receipt revision identity; Q56 owns
quote/source equality; Q57 owns absorption evidence. Bound: arm-level, not
world-level. | — |
```

## Attack item 1 — both directions and the guard: PRESENT

The row states both directions explicitly: (i) rejection "by the landed instrument"
and (ii) "disabling that erratum's guard in-process admits that same instance". The
guard is named: "that erratum's guard … in-process", and the receipt must name "the
disabled guard". The plan-text shortcut is excluded: "a plan-text attack does not
establish absorption". Code check of `verifiers/check_erratum_absorption.py`
(sha256 `afb4ff74…`, verified `sha256sum` on committed bytes): `summarize` lines
371–387 implement exactly this — `absorbed += 1` iff
`all(before.reasons) and all(not reasons for reasons in after.reasons)`, where
`before` is the committed-counter scoring and `after` is the scoring under that
erratum's admitting stubs (lines 303–310, `patched(counter, target.patches)`).
Off-diagonal isolation is enforced at lines 364–369.

## Attack item 2 — cites M93 and the matrix: PRESENT, citation lands on real bytes

- M93 exists: `corpus/lessons/round-62.md:25` (`grep -n 'M93'`) — class
  `erratum recorded as absorbed without an arm-level receipt`.
- The cited span `.ufo/waves/round-62/controls/absorption-hollow.txt:16-27` contains
  the real-instrument run: lines 17–27 print the counter sha, the per-direction
  instance counts, `guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0`,
  `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2` and six
  survivor lines. Committed bytes confirmed:
  `git show e6da78bb:.ufo/waves/round-62/controls/absorption-hollow.txt | md5sum`
  = `9eb20fa4e77d0fd8b10105f2fff5cbf7` == worktree `md5sum` = `9eb20fa4e77d0fd8b10105f2fff5cbf7`.

## Attack item 3 — arm-level bound: PRESENT

The evidence cell ends `Bound: arm-level, not world-level.` The instrument is
arm-level by construction: attacks call the counter's own arm functions
(`url_key`/`reopen_why`, `render_form`/`alias_why`, `alias_sha_why`,
`a1_conjunct`+`scope_conjunct`, `action_conjunct` — instrument lines 101–164) and
never run the seven worlds; `corpus/knowledge/erratum-absorption-round62.md` §
Limits repeats the bound.

## Attack item 4 — overlap with Q34/Q35/Q36/Q56: ownership line is accurate

Clause-ownership note in the row vs the cited rows' scope cells (QUALITY.md:45–47, 67):

| Row | Owns per its scope cell | Q57's note |
|-----|------------------------|------------|
| Q34 | `corpus/SOURCES.md` history and append-only claims | "SOURCES append-only claims" — match |
| Q35 | verifier inventory and registry rows (`SKILL.md` gate rows, self-test flag) | "verifier inventory and `SKILL.md` gate-registry/self-test declarations" — match |
| Q36 | receipts naming the measured revision | "receipt revision identity" — match |
| Q56 | `byte-exact` vs shaped quote equality | "quote/source equality" — match |
| Q57 | "absorption evidence" | no other row's scope cell claims absorption; `grep -n 'absorb' corpus/QUALITY.md` hits only line 68 |

No row superseded (`| — |` supersedes cell); Q57 adds a new clause, does not re-own
any of the four. No defect.

## Attack item 5 — the criterion vs the E2f survivor: forces NOT absorbed; the record complies

Re-run on committed bytes (leaf seat, `cd /home/vgpnk/Projects/shokunin/kotoba-shokunin &&
python3 -B verifiers/check_erratum_absorption.py --self-test`, `exit=0`):

```
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
exit=0
```

Under Q57's conjunct 1 ("each fresh attack instance of its class is rejected by the
landed instrument"), E2f fails: both `e2f-backticked-event-claim` and
`e2f-compound-purpose-outside-citation` score `[]` (ACCEPT) under the pinned counter —
`guard flips: E2f 0` and `absorbed` stays at 2, not 3+. Q57 therefore **forces E2f
to be recorded as NOT absorbed**, and the record complies everywhere checked:

- `.ufo/waves/round-62/C1-absorb-measure.txt:11-17` — `absorbed 2 of 5; surviving 6`,
  both E2f instances named as survivors.
- `corpus/knowledge/erratum-absorption-round62.md` — E2f row: "Both SURVIVE (`[]`);
  disabling `action_conjunct` causes no verdict change." (matches instrument patch
  `("action_conjunct", lambda *a, **k: [])`, line 229)
- `LOG.md` § Round 62 C1 line and `SCORECARD.md` round-62 annotations — survivors
  `E2c ×2, E2e ×2, E2f ×2 (G9 stays a declared bound)`.
- Successor (`C1-v31-successor.txt:22-23`): `e2f-backticked-event-claim: before
  accepted; after rejected` but `e2f-compound-purpose-outside-citation: before
  accepted; after accepted`, `bound: G9 remains unimplemented`. Under Q57 E2f is
  still NOT absorbed under v31 class-wide — and v31 records exactly that (bound,
  not absorbed).

Overclaim sweep: `grep -n 'absorb\|E2f\|surviv' LOG.md SCORECARD.md corpus/README.md SKILL.md`
— no surface records E2f as absorbed. Criterion applied consistently.

## Finding F1 (minor, adjacent — `corpus/lessons/round-62.md` M93, not the Q57 row)

M93's shown-able-to-fail clause asserts the hollow variant "exits 1, but its
diagnostic is a missing `check_scoped_rules.py` path, not the intended
guard-direction rejection". The committed receipt it cites,
`absorption-hollow.txt:6-9`, prints:

```
$ python3 -B /tmp/r62hollow/hollow.py --self-test
absorption self-test failed: guard-mutation direction is missing for one or more errata
exit=1
```

That diagnostic **is** the guard-direction rejection — raised by `validate_run`
line 336–337 (`require(set(run.mutations) == names, "guard-mutation direction is
missing for one or more errata")`). A third diagnostic exists — the constant-printing
`hollow_label_auditor()` inside `--self-test` fails at line 328 (`auditor supplied a
label/constant, not arm-level run records`, recorded at
`.ufo/waves/round-62/w1/ExecAbsorbInstrument.md:70-72` as "rejected as lacking run
records") — but nothing in the committed evidence produces "a missing
`check_scoped_rules.py` path". The lesson misdescribes its own cited receipt bytes;
Q57's row itself is accurate. Severity: minor (evidence-vs-prose mismatch inside
M93; the kill property itself is real and the citation range is correct).

## Finding F2 (very minor — citation precision, Q36/Q50-flavoured)

Q57 (and M93's captured-by clause) cite the matrix data at
`controls/absorption-hollow.txt:16-27` — the real-run block inside the kill-control
receipt, measured at `9228be47` — while the canonical matrix data receipt is
`.ufo/waves/round-62/C1-absorb-measure.txt`, measured at `3e7aed9b` (and that is what
`LOG.md` § Round 62 and `SCORECARD.md` cite). Both contain byte-identical matrix
output (verified: my re-run matches both), so no number is wrong; the named receipt
is the control, not the data run. Not a falsification — the cited range literally
contains the matrix output — but the row's "C1 matrix" citation points at a control
receipt.

## Observations (no defect)

- "the receipt names … the disabled guard" is satisfied at class granularity
  (`guard flips: E2f 0`; `survivor E2f <id>`). Function-level naming exists in the
  knowledge entry (`disabling \`action_conjunct\``, `disabling \`alias_sha_why\``)
  and the v31 must-fail arms (`must-fail G7 disabled admits e2f-backticked-event-claim`).
  E2e's patch is two functions (`a1_conjunct`, `path_value`; instrument lines
  208–210) — receipts name only the class.
- Vacuous edge closed in code, not in row text: `validate_run` requires exactly two
  frozen instances per class (lines 334, 344), so an erratum class with zero fresh
  instances cannot score `absorbed` under Q57's `all()`-style conjuncts.
- `exit=0` requires only `measured == 5` and `controls == 2` (lines 494–496);
  absorbed/surviving counts are computed, not gated — matching the E1-amended
  frozen predicate (`plans/round-62.md` § Erratum E1).

## Verdict

Q57 calibrates correctly: it states both verdict directions, names the disabled
guard and the plan-text exclusion, cites M93 and a receipt range containing the
real matrix bytes, states the arm-level bound, and its clause-ownership line is
accurate against Q34/Q35/Q36/Q56. Against the E2f survivor it forces — and the
committed record everywhere shows — NOT absorbed (`absorbed 2 of 5`, both E2f
instances named survivors). Residual defects are adjacent to the row: F1 (lesson
M93 misdescribes the hollow diagnostic) and F2 (matrix citation points at the
control receipt rather than `C1-absorb-measure.txt`).

## Evidence appendix — commands run

- `python3 -B verifiers/check_erratum_absorption.py --self-test` → exit 0, output quoted above (2026-10-23, leaf re-run).
- `sha256sum verifiers/check_erratum_absorption.py` → `afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b`; `verifiers/check_scoped_rules.py` → `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`; `verifiers/check_scoped_rules_v31.py` → `a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858`.
- `git show e6da78bb:corpus/QUALITY.md | sed -n '68p'` — identical to worktree line 68.
- `git show e6da78bb:.ufo/waves/round-62/controls/absorption-hollow.txt | md5sum` → `9eb20fa4e77d0fd8b10105f2fff5cbf7`; worktree `md5sum` identical.
- `git log -1 --format='%h %s' -- corpus/QUALITY.md` → `e6da78b` (Q57 landed at the audited tip).
- `git merge-base --is-ancestor e6da78bb… HEAD` → true (HEAD `3f911504` = tip + wave-2 dispatch commit; working-tree edits are w2 peer files, not Q57 surfaces).
- `grep -n 'absorb' corpus/QUALITY.md` → only line 68.
- Reads: `verifiers/check_erratum_absorption.py` (lines 1–500 in ranges 1–123, 123–279, 276–363, 358–500); `corpus/lessons/round-62.md:25`; `corpus/knowledge/erratum-absorption-round62.md`; `.ufo/waves/round-62/controls/absorption-hollow.txt`; `.ufo/waves/round-62/C1-absorb-measure.txt`; `.ufo/waves/round-62/C1-v31-successor.txt`; `plans/round-62.md` (incl. Erratum E1 + addenda); `.ufo/waves/round-62/w1/ExecAbsorbInstrument.md:60-80`; LOG.md/SCORECARD.md/README.md/SKILL.md grep sweep.

No tools installed (none needed). No lane files written except this report.
