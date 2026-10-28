# Kb81M01Instruments — mutation test of the R1+R2 patches (C1, wave w1)

Seat: mutation-tester, leaf. Date 2026-10-27. Lane base `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Patches under test (consumed read-only from `.ufo/waves/round-81/build/`):

- `Kb81E01Integrity.patch` (R1+R2a, `verify_corpus_integrity.py` + `external-commits.json`),
  sha256 `6bbb304bea83968ced6c2ba3f33afa26b7d4256334303ea99a32279079495fe7` (mtime 23:37:12).
- `Kb81E02Independent.patch` (R2b, `verify_corpus_independent.py`),
  sha256 `d8bf88c8ef5daf99ddf861ab2a5aeaa1193a57a90200e1d314134750e2e7f9d1` (mtime 23:39:45).

Method: every configuration is a fresh `git clone --shared` of the lane checked out at the base,
patches applied with `git apply`, the patched state committed, the mutant applied as a one-line
edit (diff + sha256 receipted), then `--self-test` runs of the patched/mutated bytes. Gate-level
world probes run `verify_corpus_{integrity,independent}.py --repo <clone> --no-baseline --json`
(exit captured from the command itself, never a pipeline). Mutants lived only in
`/fast/scratch/hyaku/kotoba-r81/Kb81M01Instruments/` (removed before yield). No lane file outside
`.ufo/waves/round-81/` was written; lane verifier bytes are unchanged
(`verify_corpus_integrity.py 3e600f4b70e4664048c0c09b06bf6a28cb00ff37fbb8c78f597a1f1452c03748`,
`verify_corpus_independent.py c9cef5b3ecca5e9cfdac26b77702ac39186049ed782ce4a250776939a06e7ff2`,
both identical to session start; `git status --porcelain -- verifiers/` empty).

Patch-churn disclosure: E02 rewrote its patch mid-probe (19622 B @23:33 → 15664 B @23:39; the
rewrite dropped the draft's `_fixture_revpointers` fleet-object fixture and the
`external_commits` in-receipt association checks visible in the early read). E01 rewrote at
23:37:12 before my first run. All configurations below ran after 23:40 and therefore applied the
final bytes; each mutant receipt pins its own applied-file sha256. Two driver defects were hit and
fixed en route (first `pyrep` asserted on the non-target file before mutating, producing one bogus
"survival" each for MaE02/MbE02; the McE02 case body regenerated a stale anchor). Affected configs
were rerun under the guarded driver (`MUTANT-ANCHOR-NOT-FOUND` / `MUTANT-DIFF-EMPTY` hard fails);
every surviving/killed verdict below is backed by a mutant.diff plus a mutant.sha256 that proves
the mutation was in the tested bytes.

## Pristine phase (no mutation)

- E01 self-test: `python3 -B verifiers/verify_corpus_integrity.py --self-test` → exit 0,
  `self-test: 0 failure(s) over 178 assertions` (`Kb81M01Instruments-P.selftest-integrity.txt`).
- E02 self-test: `... verify_corpus_independent.py --self-test` → exit 0,
  `self-test: 109 assertions, 0 failures` (`Kb81M01Instruments-P.selftest-independent.txt`).
- Gate baseline over base corpus + patches: integrity `report_dead 0`,
  `commit_unresolvable 0`, `commit_external 2` (S230/S231 manifest-bound);
  independent witness agrees (`Kb81M01Instruments-P.r77-baseline-{integrity,independent}.json`).
  Both exit 1 solely on the pre-existing `unindexed` class — not this repair's.
- W8-world control (a real lane-created commit `7571ee2051b11be93a1a64c5548e041596d92b88`
  created in an isolated scratch repo, cited as bare hex with an `owner/repo@` + URL marker on the
  line, absent from manifest): BOTH pristine witnesses keep it `commit_unresolvable 1`,
  `commit_external` stays 2 (`Kb81M01Instruments-W8P.world-w8-*.json`). The strengthened R2
  closes the r80 W8 attack shape in both witnesses.

## Mutants

| id | patch | one-line mutation | self-test result | verdict |
|---|---|---|---|---|
| MaE01 | E01 | `REPORT_MARKER, REPORT_MIN_BYTES = b"## SHONEN", 400` → `b"## ", 400` | 178 assertions, 0 failures, exit 0 | **SURVIVED** |
| MaE02 | E02 | identity tuple marker `b"## SHONEN"` → `b"## "` | 109 assertions, 0 failures, exit 0 | **SURVIVED** |
| MbE01 | E01 | `external_binding`: `return True` inserted before the manifest read | 10 failures / 178, exit 1 | **KILLED** |
| MbE02 | E02 | `analyse_commits`: `(external if token.lower() in externals else unresolvable).append(site)` → `external.append(site)` | 6 failures / 109, exit 1 | **KILLED** |
| McE01 | E01 | rev branch: `for repo in ([lane] if lane else []) + [fleet_root]` → drop `+ [fleet_root]` | 178 assertions, 0 failures, exit 0 | **SURVIVED** |
| McE02 | E02 | object route: `for candidate in [repo] + fleet:` → `for candidate in [repo]:` | 109 assertions, 0 failures, exit 0 | **SURVIVED** |
| MdE01 | E01 | `REPORT_MIN_BYTES` 400 → 0 | 178 assertions, 0 failures, exit 0 | **SURVIVED** |

### MbE01 — which arms caught it (all 10, exact receipt text)

`external/absent-hash-red`, `external/unbound-marker-red` (the W8 arm), `external/wrong-digest-red`,
`external/conflicting-duplicate-red`, `external/receipt-not-committed-red`,
`external/abbreviated-hash-red`, `external/receipt-names-other-repo-red`,
`external/no-manifest-red`, `external/line-marker-not-exempt` (the W8/W9 line-shape arm:
got `(2, 0)` want `(1, 1)`), `external/bound-detail`. The tasking's requirement — W8/W9 arms go
red when the manifest binding is dropped — holds with a wide margin; the arms are not vacuous.
The same clone's pristine E02 self-test stayed 109/0 (witness intact), and the W8 world gate run
shows the operational divergence: mutated integrity launders the W8 commit
(`commit_unresolvable 0`, `commit_external 3`), pristine independent still holds it red
(`commit_unresolvable 1`) — so even if the self-test were weakened, the two-witness battery plus
the W6/W8 control worlds would still catch a unilateral manifest-binding drop
(`Kb81M01Instruments-MbE01.selftest-integrity.txt`, `.selftest-independent.txt`,
`.world-w8-integrity.json`, `.world-w8-independent.json`).

### MbE02 — which arms caught it

`not ok 75` deadbeef-unresolvable, `not ok 76` exactly-one-hex-resolves, `not ok 83` unresolvable
detail, `not ok 88` only-genuinely-absent-stays-unresolved (pre-existing r80-era arms — the
mutant externalizes every absent token, not just marker lines), plus the two r81 arms:
`not ok 91 - r81: the receipt-pinned hash is external, the marker-bound one is not: got (2, 0)
want (1, 1)` and `not ok 93 - r81: a wrong receipt pin binds nothing; a line marker never
exempts: got 2 want 0`. W8/W9 arms went red as required
(`Kb81M01Instruments-MbE02.selftest-independent.txt`).

### MaE01 / MaE02 — the tasking's prediction is falsified (coverage finding 1)

The tasking expected "at least one arm fails" when `## SHONEN` weakens to `## `. Neither
witness has any arm that pins the exact marker: both self-tests stayed fully green with the
generic-H2 marker. The hole is operationally real — the near-miss probe built a fleet report
target of `## Executive Summary` + padding (821 B): pristine
`report_pointer_exists -> False`, mutant `-> True`
(`Kb81M01Instruments-MaE01.nearmiss-probe.txt`). A W10-style attacker does not need `## SHONEN`;
any H2 heading of ≥400 B passes the mutated identity check in both gates. Suggested arm (for the
L1/integrators, not implemented by me): extend the marker-file fixture with a generic-H2 file of
≥400 B that must stay `report_dead`, in both witnesses.

### McE01 / McE02 — fleet fallback unpinned in both witnesses (coverage finding 2)

Both self-tests stayed green with the fleet fallback removed from `<rev>:<path>` resolution.
The r77-world gate probe is what catches the mutant, in both witnesses: over the base corpus
(where `corpus/lessons/round-77-verifier-spotcheck.md:15` cites `HEAD:.ufo/reports/round-77/kotoba.md`,
a fleet-only object — fleet HEAD `8566072e04f235b23b48786cbb61589837017c97` carries it, 8547 B,
`## SHONEN` present), pristine gates read `report_dead 0` and both mutants read
`report_dead 1` (`Kb81M01Instruments-P.r77-baseline-*.json` vs
`Kb81M01Instruments-McE01.r77-world-integrity.json`,
`Kb81M01Instruments-McE02.r77-world-independent.json`). The fallback is load-bearing but no
self-test arm asserts a fleet-only object resolves (E02's 23:39 rewrite dropped the
fleet-object fixture its 23:33 draft had). Suggested arm: one `<rev>:<path>` token whose object
exists only in the fixture fleet, expected alive.

### MdE01 — the size floor is load-bearing and arm-vacuous (coverage finding 3)

With `REPORT_MIN_BYTES = 0` the self-test stays green (178/0), and the short-marker probe — the
exact W8-world question the tasking asked — answers YES: a 10-byte `## SHONEN\n` file
substituted at a cited report path reads `report_pointer_exists -> False` pristine and
`-> True` under the mutant (`Kb81M01Instruments-MdE01.shortshonen-probe.txt`). The
`## SHONEN` conjunct alone does not stop a minimal forged report; only the ≥400 B bound does,
and no arm asserts it. Suggested arm: a short `## SHONEN`-bearing target (e.g. 12 B) expected
`report_dead`.

## Honesty notes

- Self-test assertion totals: E01 178, E02 109 on the bytes under test; per-config applied-file
  sha256 in `Kb81M01Instruments-<cfg>.mutant.sha256`; exact mutations in
  `Kb81M01Instruments-<cfg>.mutant.diff` / `.mutation-expr.py`.
- No tools were installed or upgraded (operator 2026-10-19 authorization unused); only `git`,
  `python3`, coreutils were used. The tip battery was not run (not needed for gate-level
  mutation verdicts; the heaviest single command here is a gate self-test, seconds).
- Scratch removed: `/fast/scratch/hyaku/kotoba-r81/Kb81M01Instruments` deleted after receipts
  were copied to build/. Restoration evidence: lane verifier hashes above are identical to the
  session-start hashes taken before any clone was created.
- Verdicts "SURVIVED" are coverage findings about the self-tests, not defects in the R1/R2
  contract; no contract text was changed and no lane bytes were touched.

VERDICT: R1+R2 are mutation-hard where it matters — the manifest binding is red-arm-pinned in both witnesses (MbE01 10 arms, MbE02 6 arms incl. the W8/W9 arms) and the r77 fleet-fallback world is gate-red under both fleet-drop mutants — but three arms are missing from both self-tests (exact `## SHONEN` vs generic H2, the ≥400 B floor, fleet-only `<rev>:<path>` objects), each demonstrated live with a passing-attacker probe.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81M01Instruments.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81M01Instruments-*
