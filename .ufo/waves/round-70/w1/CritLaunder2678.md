# CritLaunder2678 — K69-11 `LOG.md:2678` repair: laundering attack (round 70, wave 1)

**Verdict: an honest pointer to the record, filed in the correction slot. It is not a true
correction and not a masked red.** The facts in the appended notice (`LOG.md:2724`) check out, and
the red is real: the gate turns red at `LOG.md:2678` when the row is removed. The notice itself is
not laundering. What is wrong sits in the gate:

1. **False label.** The gate counts the row as one of "5 recorded correction(s) excused". But the
   cited token was never wrong. The directory existed when line 2678 was written, and nothing
   moved to `corpus/lessons/round-68.md`.
2. **Laundering surface.** The correction slot accepts *any* live file as the "corrected token".
   Swapping in `SKILL.md`, `verifiers/README.md` or even `LOG.md` gives the same PASS.

The strictly more honest alternative: keep the committed notice and change the gate (P1 below).
Splitting relocations from record pointers gives the row its honest label and closes the
any-live-file hole. Measured cost: +44/−11 lines in `verify_skill_checklist.py`, 3 new self-test
assertions (1862 → 1865, 0 failures), no horizon raise, no `LOG.md`/`SCORECARD.md` append, and no
`SKILL.md` lines (it stays at 600/600).

Impacted axes: **consistency** (C1 item K69-11; the gate tally the in-place receipt quotes),
**calibration** (the false "correction" label in `receipts/K69-11-inplace.txt`'s detail string),
and the no-harm battery (the `verify_skill_checklist.py` self-test).

Sandbox for every run: `mktemp -d /tmp/k70w1-CritLaunder2678.XXXX` → `/tmp/k70w1-CritLaunder2678.pyHd`.
Inside it: `git clone --shared` of the lane, checkout `16b212a390c7ce68b6bce49b2c3766b154fbcbae`,
and every fleet-root entry except `kotoba-shokunin` symlinked into the sandbox parent so `../`
tokens resolve as they do in the real lane. Deleted before return. No lane file other than this
report was written.

## Findings

### F1 — The red is real, and only this row excuses it

At the tip, unmodified (`python3 -B verifiers/verify_skill_checklist.py --json` in the sandbox), the
check reads:

```
PASS 1253 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused, 5 recorded correction(s) excused
```

This is the same detail string as `.ufo/waves/round-70/receipts/K69-11-inplace.txt:8`.

Probe E2 calls `check_governance_citations(R, corrections=G[:-1])`, dropping the `LOG.md:2724` row:

```
[E2 drop LOG.md:2724 row] FAIL evaluated=1254 :: LOG.md:2678: '.ufo/waves/round-67/w1/controls/junk-world/' does not resolve ...; ... 4 recorded correction(s) excused
```

So the row excuses exactly one live red subject. Nothing else is masked:
`verify_skill_checklist.py:1734` requires a named live subject, and the self-test arm "correction
never masks another dead subject" (`:2505`) still holds.

### F2 — The notice's facts are true and sourced

- **Never tracked.** `git log --all --oneline -- '.ufo/waves/round-67/w1/controls/junk-world/' | wc -l`
  gives `0`, across 968 refs of which 951 are `refs/jj/*` (`git for-each-ref | rg -c refs/jj` →
  `951`). No jj snapshot ever held it.
- **Removed.** `ls -d .ufo/waves/round-67/w1/controls/junk-world` gives `No such file or
  directory`. The non-author r68 closure observed the same thing:
  `corpus/lessons/round-68-verifier-spotcheck.md:74`, "`test -e .ufo/waves/round-67/w1/controls/junk-world` | `REMOVED`".
- **254 MB.** The non-author r67 closure measured it: `corpus/lessons/round-67-verifier-spotcheck.md:93`
  (`du -sh … → 254M`).
- **Record is M109.** `corpus/lessons/round-68.md:154-159` names the path and states the removal.
- The notice text (`LOG.md:2724`) says all of this in its own bytes: "removed from the working tree
  in round 68 and never tracked; its record is M109 in the round-68 lesson". A reader of `LOG.md` is
  not misled. The disclosure is honest.

### F3 — It is not a correction

The verifier comment at `verify_skill_checklist.py:407-414` defines the slot as "A stale citation
cell … is fixed by an appended LOG.md notice … names the subject … and its replacement". The
docstring at `:206-211` says a "named stale subject … superseded by" a notice naming "the stale and
corrected tokens".

`LOG.md:2678` is not stale-by-mistake. It was accurate when written (the r68 entry discloses a then-
existing directory, and line 2681 records its removal in the same bullet). `corpus/lessons/round-68.md`
is not its replacement.

Probe E5 tests "basename(stale) == basename(corrected)" over all five shipped rows:

```
E5 LOG.md:2619 LOG.md:2533 reloc(basename-equal)=True record-names-stale=False
E5 LOG.md:2620 LOG.md:2580 reloc(basename-equal)=True record-names-stale=False
E5 LOG.md:2621 SCORECARD.md:158 reloc(basename-equal)=True record-names-stale=False
E5 LOG.md:2723 LOG.md:2676 reloc(basename-equal)=True record-names-stale=False
E5 LOG.md:2724 LOG.md:2678 reloc(basename-equal)=False record-names-stale=True
```

Four rows are true relocations. The census row 2723 is a genuine correction: the file exists at
`.ufo/waves/round-67/controls/census-validate-append.txt` per `git ls-tree -r --name-only HEAD --
.ufo/waves/round-67/`. Row 2724 is the only one of another kind: it points at a record. The gate
output folds it into "5 recorded correction(s)", which is a false provenance label in the gate
tally and in the receipt that quotes it.

### F4 — Counterexample: the correction slot launders any dead path into any live file

Probe E3 rewrites notice line 2724 in the sandbox to point at an unrelated file, re-pins its
SHA-256, and re-runs the check:

```
[E3 corrected->SKILL.md (unrelated)] PASS evaluated=1253 :: ... 5 recorded correction(s) excused
[E3 corrected->verifiers/README.md (unrelated)] PASS evaluated=1253 :: ... 5 recorded correction(s) excused
[E3 corrected->LOG.md (unrelated)] PASS evaluated=1253 :: ... 5 recorded correction(s) excused
```

`correction_problems` (`verify_skill_checklist.py:1736-1742`) checks only that the stale token is
dead and the corrected token resolves. The relation between them is never checked. The round-70
change (`git diff 7d51253 HEAD -- verifiers/verify_skill_checklist.py`: horizon 2621 → 2724, two
rows, and a count bump 3 → 5 in the live arm at `:2516`) added no self-test arm for the new kind
of row. The r69 closure asked for "its own self-test arms"
(`corpus/lessons/round-69-verifier-spotcheck.md:208-212`). The round-65 fixture itself uses an
unrelated replacement (`corpus/gone.md` → `corpus/live.md`, `:2457-2466`). The vacuity is
inherited, not new in round 70, but round 70 is the first round to depend on it.

### F5 — The recorded-absence (errata) form is not cheaper and not strictly better

Line 2678's own bytes are:
`- **Routed defect R67-3 (disclosure).** \`.ufo/waves/round-67/w1/controls/junk-world/\` — a 254 MB`.
The absence wording ("removes it from the working tree") sits on line 2681.

Probe E4 adds a `GOVERNANCE_ERRATA` row for 2678:

```
[E4 errata quote='removes it from the working tree' horizon=2315] FAIL ... is past horizon 2315 or absent
[E4 errata quote='removes it from the working tree' horizon=2682] FAIL ... absence wording not on the line
[E4 errata quote='(disclosure)' horizon=2682] PASS ... 2 recorded absence(s) excused, 4 recorded correction(s) excused
```

The only code-free errata row that passes uses "(disclosure)" as its "absence wording". That would
be a worse laundering: a quote that does not state absence.

Prototype P2 makes the errata match the subject's bullet continuation lines (`bullet_text`), raises
`GOVERNANCE_ERRATA_HORIZON` 2315 → 2682, adds the row
`(2678, sha256(line), token, "removes it from the working tree")` and drops correction row 2724.
Results: `git diff --stat` → `26 ++++++++++++++++++--------` (+18/−8); `--self-test` →
`0 failure(s) over 1862 assertions`; live check `PASS … 2 recorded absence(s) excused, 4 recorded
correction(s) excused`. The taxonomy is honest, but the costs are real:

- The errata horizon widens by 367 `LOG.md` lines.
- It contradicts the errata comment (`:396-397`, "lines that … predate the same-line quote
  convention"), because line 2678 is a round-68 line.
- It still needs ≥2 new arms (wording in the continuation passes; wording in the next bullet fails).
- The committed notice `LOG.md:2724` would be orphaned (still worded as a "->" correction, no
  longer registered), which forces a further appended `LOG.md` line explaining the reclassification.

Not recommended.

### F6 — Recommended correction P1: split relocation from record pointer (prototyped, green)

In `correction_problems`, after the corrected token resolves:

- **Relocation** (counted as a correction): `PurePosixPath(stale).name == PurePosixPath(corrected).name`.
- **Record pointer** (counted separately): otherwise, the corrected token is a file outside
  `GOVERNANCE_FILES` whose bytes contain the stale token.
- **Any other row:** FAIL with "corrected token … neither relocates the stale path nor records it".

The detail string gains `, %d record pointer(s) excused`. In the self-test fixture, the round-65
replacement becomes the relocation `corpus/moved/gone.md`. Three arms are added: a record file
naming the stale token → PASS "1 record pointer(s) excused"; unrelated live `corpus/live.md` → FAIL;
the governance file `LOG.md` as the "record" → FAIL. The live arm now asserts "4 recorded
correction(s) excused, 1 record pointer(s)".

Measured in the sandbox:

- `git diff --stat` → `55 ++++++++++++++++++++++++++++++-------` (+44/−11).
- `--self-test` → `0 failure(s) over 1865 assertions`.
- `--json` → exit 0, with
  `PASS 1253 … 1 recorded absence(s) excused, 4 recorded correction(s) excused, 1 record pointer(s) excused`.
- E3 under P1 FAILs for every unrelated target, e.g.
  `[E3 corrected->SKILL.md (unrelated)] FAIL … corrected token 'SKILL.md' neither relocates the stale path nor records it`.

Cost summary for P1: no horizon raise, no governance append (`LOG.md:2724` stays valid byte-for-
byte), no `SKILL.md` lines, +3 self-test arms. `check_r69_routed_repairs.py:248-250` reads only the
status, so C1's K69-11 item is unaffected. No other verifier pins the detail string
(`rg -n 'recorded correction\(s\)' --glob '!verifiers/verify_skill_checklist.py' verifiers scripts`
gave no output). `receipts/K69-11-inplace.txt` stays a historical receipt. Its "5 recorded
correction(s)" wording should get an appended note rather than an edit if P1 lands.

Residual, disclosed: "the record names the stale token" also passes for a file that names the path
without recording its absence. Probe E5b: `corpus/lessons/round-67-verifier-spotcheck.md`, which
records it *existing* at 254M, would pass.

A stricter form would require absence wording on the record's token line. It costs about +4 lines
and +1 arm, but `corpus/lessons/round-68.md:155` would then fail ("untracked" is on that line;
"removes" is on `:159`). The row would have to point at the non-author observation
`corpus/lessons/round-68-verifier-spotcheck.md:74` (`test -e … REMOVED`, same line). That means one
new appended `LOG.md` notice (line 2725), raising `GOVERNANCE_CORRECTIONS_HORIZON` 2724 → 2725 and
re-pinning the row. It gives stronger provenance (a non-author observation instead of the author's
lesson), but it is optional, not required for honesty.

## Side finding (scope-adjacent, for the K69-11 sandbox critics)

M116 (`corpus/lessons/round-70.md:136-151`) says that "In any `/tmp` sandbox" the `../.ufo/…`
tokens are dead, so the item reads FAIL at every revision. That holds for the sandbox the counter
builds (a bare `git clone --shared`). It is false for a sandbox whose parent mirrors the fleet
root. My sandbox (fleet-root entries symlinked beside the clone, `/tmp/k70w1-CritLaunder2678.pyHd`)
read `governance.citation_resolves PASS 1253` at `16b212a`, exit 0.

The item is unsatisfiable *as constructed*, not in principle. The lesson's "any" overstates it.
That is a wording calibration issue; the frozen predicate and the declared miss are untouched.

## Tooling

No tools installed or upgraded.
