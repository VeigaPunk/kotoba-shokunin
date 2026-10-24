# RevC2Mechanism — round 65, wave 1: GOVERNANCE_CORRECTIONS laundering doors

Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (jj-colocated, read-only seat).
Subject: claim C2's new `GOVERNANCE_CORRECTIONS` excusal machinery
(`verifiers/verify_skill_checklist.py:415-431` rows, `:1699` `correction_problems`,
`:1737` `check_governance_citations`, `:2762` the one production call site) and the three
appended `LOG.md:2619-2621` notices it cites.
Interrogation question: can a correction excuse a subject that is not really red, excuse two
subjects, excuse a red subject outside the two governance files, or ride on a line that also
introduces a new dead token (M100 class)?
No repo, jj, or Git-index bytes were written; every fixture lives under `/tmp/revc2*`.

## Verdict

The **frozen counted predicate holds** and every door that does not depend on the row's own
contents is closed. Exactly one door is **open and structural**: a correction row whose subject
line is its own notice line (`sline == line`) authenticates the dead token it excuses, because
nothing binds the notice line's *provenance* to the subject (no ordering, no distinct-line, no
subject-line pin). A second door is open at the narrative layer: the notice text is never
compared with the row's `(sfile, sline)` and every naming test is a substring test.

Findings are ordered by severity. "Closed" means I produced a FAIL for that shape on the landed
bytes — not that I believe it fails.

---

## F1 — MEDIUM — self-authenticating correction: a row can mint the red subject it excuses

**Door.** `correction_problems` requires `(sfile, sline, stale)` to be a live red subject
(`:1726`), the stale token to still be unresolvable (`:1728`), the corrected token to resolve
(`:1730`), and the notice line to contain both tokens as substrings (`:1724`). It never requires
`sline != line`, never requires `sline < line` for same-file subjects, and never requires the
notice to postdate the round in which the subject appeared. The excused set is keyed by the
subject identity (`:1733`), so when the subject *is* the notice line the notice authenticates
itself.

The docstring (`:206-214`) claims the subject is "superseded by an **appended**, byte-pinned
`LOG.md` notice", and the plan's C2 text claims "the check then excuses the **superseded**
subject". Neither "appended" nor "superseded" is enforced by any line of code.

**Evidence (fixtures under `/tmp`, module loaded from the lane path):**

```
P25b pure self-mint world, two rows                    PASS ev=3   3 governance citation token(s) resolve across 2 files; 0 quoted meta-finding(s), 0 schematic token(s) excluded, 0 recorded absence(s) excused, 2 recorded correction(s) excused
P9 self-referential: notice mints its own dead         FAIL ev=3   SCORECARD.md:2: 'corpus/gone.md' does not resolve ...; 1 recorded correction(s) excused
P10 notice==subject line (no append)                   PASS ev=1   1 governance citation token(s) resolve ...; 1 recorded correction(s) excused
P11b notice at line 2 seals a later LOG.md:9           PASS ev=1   1 governance citation token(s) resolve ...; 1 recorded correction(s) excused
P29b backticked, notice==subject line                  PASS ev=2   2 governance citation token(s) resolve ...; 1 recorded correction(s) excused
```

`P25b` is the clean form: the world has **zero pre-existing red cells**; `LOG.md:2` reads
``also `corpus/mint1.md` -> `corpus/live.md`; and `corpus/mint2.md` -> `corpus/live.md` `` and
two rows name `(LOG.md, 2, corpus/mint1.md)` / `(LOG.md, 2, corpus/mint2.md)`. The check prints
**PASS with 2 corrections excused** while two dead tokens sit in `LOG.md` and stay dead. In `P9`
the minted token is silently excused (`1 recorded correction(s) excused`) and the only complaint
is about an unrelated cell. `P29b` shows the same door works in the fully backticked shape.

The chain composes: `P25` (one legitimate `SCORECARD.md:2` correction plus two minted rows on the
same notice line) also prints `PASS … 3 recorded correction(s) excused`, so a reviewer looking at
the count sees one plausible correction and two anonymous ones.

**Why this is Medium, not High.** The rows are in-source, so exploiting the door requires editing
`GOVERNANCE_CORRECTIONS`; the live self-test arm (`:2502-2507`) pins the exact string
`3 recorded correction(s) excused`, so a fourth row fails the self-test until the arm's literal is
bumped. That is a real compensating control (a count bump is visible) but it does not *name* the
shape: a reviewer who sees "3 → 4" has no assertion that the fourth subject predates its notice.

**Close (one line each, if this round reopens C2).**

- `if sfile == "LOG.md" and sline >= line: problem` — a notice cannot excuse itself or a later
  line; cross-file subjects (`SCORECARD.md`) need no ordering rule.
- Optionally pin the subject line: add its sha to the row, which would also close F3 and make the
  correction as strong as `GOVERNANCE_ERRATA` is.
- Add the missing arm: "a correction naming its own notice line fails" and "a correction naming a
  later line of the same file fails". No such arm exists today (see Verification gaps).

## F2 — MEDIUM-LOW — the notice text is never bound to the row; every naming test is a substring test

Four independent gaps, all at `:1724` (the only text check):

```
P15 notice denies the correction                        PASS  … "CORRECTION NOT MADE: token "corpus/gone.md" was never corrected to "corpus/live.md"" is accepted
P39 corrected token only as substring                   PASS  … row's corrected token `corpus/live.md` is "named" by the text `corpus/live.md.orig`
P41 text names LOG.md:999, row names SCORECARD:2         PASS  … the notice text cites a different (file, line) than the row excuses
P24 notice omits subject file:line                      PASS  … no anchor in the notice at all
```

`stale in text and corrected in text` is a raw substring test with no polarity, no token
boundary, and no cross-check against `sfile`/`sline`. Because `citation_subjects` only harvests
tokens from **backticked** spans, the notice's plain-text tokens are not citations at all
(`P43`: a plain `"corpus/unrelated-dead.md"` on the notice line prints `0 quoted meta-finding(s)`
and PASSes). The consequence is structural, not cosmetic: the LOG notice is the human-readable
audit trail of *which* cell was corrected and the gate never reads it as a statement — a
byte-pinned line that says "we did not correct this, and here is why" passes identically to a
genuine correction.

**Close.** Require the notice text to contain the literal `<sfile>:<sline>` (or `file.md:<line>`)
and an explicit `->` between the two token occurrences, and match `corrected` on the token that
follows the arrow rather than on the whole line.

## F3 — LOW — the subject line's bytes are not pinned (asymmetry with `GOVERNANCE_ERRATA`)

An erratum pins the bytes of the line it excuses (`:1686-1687`, the row's `line` *is* the subject
line). A correction pins only the notice line; the subject is named by `(file, line number, token)`
and its text may drift.

```
P40 subject line gains an extra dead token             FAIL  … the extra dead token is caught (fail-closed)
P26 same token dead on lines 2 and 3                   FAIL  … one row excuses one line only (correct)
```

Drift is fail-closed when the token leaves the line, but a later in-place rewrite of
`LOG.md:2533` that keeps the token passes silently, and a shifted line number re-binds to whatever
cell carries the same token at that number. Severity is low because it cannot create a pass for a
token that is not red, but the audit trail is weaker than the errata mechanism it is modelled on.

## F4 — LOW — the M99 "errata default leaks into fixture" shape is still in the signature

`check_governance_citations` still defaults `errata=GOVERNANCE_ERRATA` and `horizon=2315`
(measured: `__defaults__` = the live row, `2315`, `()`, `2621`), while the docstring's
"Default () keeps fixture worlds hermetic" is true only for `corrections`. Any future arm that
omits `errata=` gets `erratum LOG.md:2111 … past horizon 2315 or absent` and a spurious FAIL.
Fail-closed (a trap, not a laundering door) — but it is the exact shape the M99 receipt
(`receipts/M99-fixture-leak.txt`) recorded and the round fixed per-call, not structurally.
`main` at `:2762` depends on the errata default, so the close is a docstring correction or an
explicit `errata=GOVERNANCE_ERRATA` at the production call site.

## F5 — LOW (documentation) — "those three counted exclusions" is now four

Docstring `:211-214`: `evaluated` is described as checked subjects "after those three counted
exclusions", but the paragraph enumerates four exclusion classes: same-line quoted meta-findings,
schematic tokens, `GOVERNANCE_ERRATA`, `GOVERNANCE_CORRECTIONS`. The live detail string counts
all four (`10 quoted … 3 schematic … 1 recorded absence … 3 recorded correction`). One-word fix.

## F6 — INFO / residual (open by design) — "the corrected token resolves" is existence-only

`citation_resolve` (`:1514-1537`) accepts any existing path within three ancestors, including a
**directory**:

```
P31 dir tokens: True True        # citation_resolve("../reports", LANE) is True; the path is a dir
P27 resolve directory: True | out-of-repo: False | 4 hops: False
```

So the corrected-token conjunct can be satisfied by an unrelated existing path, a directory, or a
path outside the repo. The three live rows do point outside the lane
(`../.ufo/reports/round-60/kotoba.md`, `../.ufo/watchdog.log`) — I verified both targets exist and
are the intended artifacts (`# kotoba — round 60 report …`; `2026-09-28T15:44:59-03:00 watchdog
tick …`), so the live corrections are substantively right. The `trigger.citation_resolves` LIMITS
clause already names "prefixing a base quiets the check"; the governance docstring does not
restate that limit, and the C2 claim's "MUST resolve via `citation_resolve`" should be read as
"must exist", not "must be the intended file".

---

## Door table (every shape I could construct / every shape ruled out)

| # | Attempted door | Result | Probe / code |
|---|---|---|---|
| 1 | excuse a subject that is not really red | **closed** — `:1728` "stale, the old token now resolves" | P3 FAIL; restore arms `:2485-2490` |
| 2 | one row excuses two subjects | **closed** — one excusal key per row; the sibling dead token still fails | P4 FAIL (`SCORECARD.md:1 'corpus/gone2.md' does not resolve`); P5 |
| 3 | red subject outside the two governance files | **closed** — `live` is built only from `LOG.md`/`SCORECARD.md` subjects; no explicit `sfile` whitelist needed | P7 (`SKILL.md`) and P7b (`./LOG.md`) FAIL "names no live red subject" |
| 4 | ride a line that also introduces a *foreign* dead token (M100) | **closed, structurally** — the notice line is scanned like any LOG line | P8 FAIL (`LOG.md:2: 'corpus/newdead.md' does not resolve`); P29 FAIL (backticked form) |
| 5 | ride a line that introduces the *named* dead token (`sline == line`) | **OPEN** | P9, P25b, P29b, P10 PASS — F1 |
| 6 | append-only: notice == subject line, or notice *before* subject | **OPEN** (same root as 5) | P10, P11b, P29b PASS |
| 7 | notice text contradicts, omits, or mis-anchors the row | **OPEN** | P15, P24, P39, P41 PASS — F2 |
| 8 | double-excuse: errata and correction on one subject | **closed** — the correction pass receives subjects post-errata (`:1772-1779`) | P30 FAIL "names no live red subject"; P30b control PASS |
| 9 | empty the check by excusing everything | **closed** — `evaluated == 0` is a FAIL (`:1782-1785`) | P42 FAIL "no checked governance citation subjects" |
| 10 | inflate the excused count with duplicate rows | **closed** — a set, so N identical rows count 1 | P12 "1 recorded correction(s) excused" |
| 11 | corrected token deleted later | **closed** — `:1730` | P45b FAIL "corrected token … does not resolve" |
| 12 | corrected token unrelated / a directory / out-of-repo | **open by design** (existence-only) | P31 — F6 |
| 13 | plain-text (non-backticked) dead paths in the notice prose | not a subject at all (general citation model); `0 quoted meta-finding(s)` | P43 — F2's root cause |
| 14 | subject line drifts / line number shifts | fail-closed only when the token leaves the line | F3 |

**Answer to the M100 sub-question.** The backticked-notice shape is **structurally prevented**,
not merely conventionally avoided: a backticked dead token on a notice line fails (`P8`, `P29`)
because the notice line is scanned exactly like any other `LOG.md` line and the excusal set is
keyed by subject identity. The live notices use *plain* double-quoted text (`LOG.md:2619-2621`),
which the subject scanner never sees — that avoidance is a convention, but it is not load-bearing:
a backticked notice that names the same token pair also passes. The one shape the structure
admits is the self-named token at `sline == line` (F1), which is exactly the M100 class one level
in: the correction rides on a line that introduces a dead token — its own.

---

## Claim check (C2, as frozen in `plans/round-65.md`)

Frozen predicate: `--json` prints `"fail": 0`, exit 0 (11/11) at the measured rev, with
`governance.citation_resolves` PASS, floors row bumped in step.

```
$ python3 -B verifiers/verify_skill_checklist.py --json            # exit 0
exit 0 pass 11 fail 0
governance.citation_resolves PASS 1206 governance citation token(s) resolve across 2 files;
  10 quoted meta-finding(s), 3 schematic token(s) excluded,
  1 recorded absence(s) excused, 3 recorded correction(s) excused
$ python3 -B verifiers/verify_skill_checklist.py --check governance.citation_resolves   # rc 0
PASS governance.citation_resolves: evaluated 1206 — …
$ python3 -B verifiers/verify_skill_checklist.py --self-test       # rc 0
0 failure(s) over 1862 assertions
$ python3 -B verifiers/check_assertion_floors.py                   # rc 0
PASS checklist observed=1862 floor=1862
PASS scoped_rules_v32 observed=240 floor=240
$ python3 -B verifiers/verify_skill_checklist.py  # corrections=() red-before control
FAIL … LOG.md:2533: '.ufo/reports/round-60/kotoba.md' does not resolve …
       LOG.md:2580: '.ufo/watchdog.log' does not resolve …
       SCORECARD.md:158: '.ufo/reports/round-60/kotoba.md' does not resolve …; 0 recorded correction(s) excused
```

- **Supports** the claim's counted predicate: 11/11 at exit 0, `fail: 0`, 1862 assertions,
  floors row `checklist 1862` in step (`floors-registry.json`, `check_assertion_floors.py:166`,
  `:211`, docstring `:8`, `:14`). The three base cells are genuinely red without the rows, and
  the rows genuinely excuse them (evidence above).
- **Supports** the fail-closed discipline for every door that does not depend on row contents
  (rows 1, 2, 3, 4, 8, 9, 10, 11).
- **Falsifies** the descriptive clauses "superseded by an **appended** `LOG.md` notice"
  (docstring `:210-211`) and "the correction then excuses the **superseded** subject" (plan §C2):
  neither appendedness nor supersession is enforced (F1).
- **Does not falsify** the frozen predicate; F1/F2 require an in-source row edit and are
  review-gated, so the mechanism's advertised red count is honest for the three landed rows.
- **Canonical runtime:** one production path (`main` → `:2762` with
  `corrections=GOVERNANCE_CORRECTIONS`). AST enumeration found 15 `check_governance_citations`
  call sites: 14 in the self-test block (`:2372-2502`, one at `:2502` against the live repo) and
  one in `main` (`:2762`). No other module calls it: `verify_alwayson.py:577-578` imports the
  module only for `extract_boxes`; `check_r64_routed_repairs.py` is a committed-line counter, not
  a governance rescan; `check_correction_sweep.py` is a *different* correction convention
  (stale pattern + declared pattern in the same block, i.e. in-place) over different files, and
  shares only `SCORECARD.md` with this mechanism — no row of either registry collides today, but
  the lane now documents two correction conventions and a future SCORECARD cell that needs both
  would have to satisfy an in-place rule and an append-only rule at once (residual risk, not a
  defect).
- **Identity:** excusal keys use the normalised token (exact tuple equality), and
  `strip_token_dressing` only drops trailing punctuation and `file.md:NN` anchors, so a line
  anchor does not change identity and a prefix does not match (`P18`: `corpus/gone.md.bak` is not
  the subject `corpus/gone.md`). No same-identity rerouting.

## Sibling corroboration (read-only cross-check, not part of my evidence)

- `MutGovArms.md:53` reports mutation M1 (`elif not citation_resolve(corrected, repo):` →
  `elif False:`) **survives** the self-test, and `ExecGovProbe.md:262` independently calls the
  suite's `corrected-dead` arm "not isolating". My door-table row 11 therefore rests on the
  landed branch (`P45b` FAIL), not on an arm that would notice the branch being removed; the
  two seats and I agree the landed bytes are fail-closed there.
- `ExecGovProbe.md:165,178` re-measured the same live numbers I did (`1206 … 3 recorded
  correction(s) excused`) and the same horizon friction (`:247,:314`: a correction appended
  today is rejected until `GOVERNANCE_CORRECTIONS_HORIZON` is bumped).
- Neither sibling probed the provenance shape: no report on disk names `sline == line`, notice
  ordering, or a row minting its own subject. F1 is the gap this seat adds; F2 is the reason the
  `wording` arm (MutGovArms M7) can only ever be killed by attribution, since the text it checks
  is not tied to the row.

## Residual risk

1. **F1** is the load-bearing one. The mechanism's shape guards make *foreign* dead tokens fail
   closed, but provenance is unverified: a future round can append one notice line carrying N new
   dead citations and N rows, each self-excused, and the gate prints PASS. The only defence today
   is the literal `3 recorded correction(s) excused` arm, which fails when the count changes but
   does not describe the change.
2. **F2** means the LOG notice is not an authenticated statement; the row is the only record.
   Combined with F6, a row can rewrite any red cell to a resolving-but-unrelated path and the
   notice text can say the opposite.
3. `GOVERNANCE_CORRECTIONS_HORIZON = 2621` equals the last live row and `LOG.md` is 2633 lines
   today: any new correction row requires bumping the horizon, which is the intended pinning
   discipline, but it also means the horizon constant is a *manual* per-round edit that nothing
   cross-checks against the row lines (a row past the horizon fails closed — verified by the
   "past horizon" arm — so this is a friction note, not a door).

## Verification gaps

- No `lsp` device is mounted on this host (`read xd://lsp` → "No such tool: xd://lsp. Mounted
  devices: ast_edit, debug"), so caller/definition checks were done by AST enumeration plus
  direct reads of `verifiers/verify_skill_checklist.py` and its importers, not by a language
  server. Recorded as a tooling gap, not as semantic proof.
- The self-test has **no arm** for the F1 shapes (self-naming row, later-line row) and **no arm**
  for the F2 shapes (anchored notice, negated notice); the mechanism therefore cannot falsify its
  own provenance hole. Every F1/F2 probe above was written and run by this seat against the
  landed module, not against an arm.
- Probes ran as single-process fixtures (well under the 4-process / 120 s cap); no contention was
  generated, no lane file was opened for write.
- I did not mutation-test the three live rows (delete a row, edit a notice byte) — the self-test's
  own arms cover those predicates and I re-derived each as a real FAIL independently.
- Content-support of the corrected tokens (does the fleet report say what `LOG.md:2533` claims) is
  out of scope: the check is existence-only by construction (F6).

## Tooling

No installs, no upgrades, no pacman transactions. Python 3 (host), `sha256sum`, and the lane's
own instruments only.
