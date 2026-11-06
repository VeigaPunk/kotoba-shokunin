# ConnectorOverlapR94 — overlap scan and planning data-walk (read-only)

Seat: ConnectorOverlapR94, round 94, wave r94-w1. Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin.
Status: COMPLETE (report file written first, updated as evidence landed; round-93 closure defect 4 discipline).
Scope honoured: no subagent dispatch (leaf member); no repo writes except this report file; read-only
git only (`ls-files` once); scratch /fast/scratch/hyaku/kotoba-r94/ConnectorOverlapR94/ created, unused, removed.

## Part 1 — cross-claim separability (C1 vs C2): CONFIRMED SEPARABLE

C1's builder touches only `verifiers/check_mutation_battery.py`; C2's only
`verifiers/check_tip_battery.py`. Evidence, exact lines:

1. **Neither instrument imports or runs the other.**
   - `check_mutation_battery.py:34-46`: imports are stdlib only (argparse, ast, contextlib,
     hashlib, io, json, os, re, shutil, subprocess, sys, tempfile, tokenize, dataclass, Path).
     `grep tip` over the file: 0 hits. Its PROBES run only FG (`check_freeze_gate.py`),
     D5 (`check_r86_routed_repairs_v3.py`) and BAT (itself) — file constants at lines 28-31.
   - `check_tip_battery.py:178-185` BATTERY tuple runs exactly six scripts:
     `check_gate_registry.py --rev <rev>`, `check_assertion_floors.py`,
     `verify_skill_checklist.py`, `verify_corpus_integrity.py`,
     `verify_corpus_independent.py`, `check_correction_sweep.py --root .` — neither C1 nor C2
     file among them. `grep mutation` over check_tip_battery.py: one comment hit only (line 656,
     "r73 mutation run", a self-test fixture label).
   - Frozen counter `verifiers/fixtures/round-94/selftest-kills.py:60-87` CLAIMS: c1 →
     `"instrument": "verifiers/check_mutation_battery.py"`; c2 →
     `"verifiers/check_tip_battery.py"`; `main()` executes only `spec["instrument"] --self-test`
     (`path = clone / spec["instrument"]`). Each counter run reads only its own instrument.

2. **The tip battery pins neither instrument.**
   - `INSTRUMENT_PINS` (`check_tip_battery.py:92-133`) has 7 keys: check_gate_registry.py,
     check_assertion_floors.py (5 admitted blobs), check_freeze_gate.py (3),
     verify_skill_checklist.py (3), verify_corpus_integrity.py (2),
     verify_corpus_independent.py (2), check_correction_sweep.py (1).
     `check_mutation_battery.py` and `check_tip_battery.py` are absent from the table and absent
     from BATTERY, so the per-key blob check (`check_tip_battery.py:345-348`) and the
     unpinned-battery-instrument arm (`:349-352`, the C2 anchor block) never read either file.
   - The instrument-size guard sums `git diff --numstat --no-renames base rev -- *scripts`
     (`run_guards`, `check_tip_battery.py:~330`) over the six BATTERY paths only; the
     no-deletions, floors and spotcheck-identity guards likewise read other paths. A C1 or C2
     edit cannot move any tip-battery guard reading ("base guards 5 of 5; 3 of 6" stays what it
     is for reasons unrelated to r94).

3. **The floors guard pins neither instrument.**
   - `grep mutation_battery|tip_battery|check_tip|check_mutation` over
     `verifiers/check_assertion_floors.py`: 0 hits (not in EXPECTED_INSTRUMENTS or INSTRUMENTS).
   - `grep battery|tip` over `verifiers/floors-registry.json`: 0 hits (no registry row).
   - The guard never runs or counts either self-test; the tip battery's floors compare
     (`check_tip_battery.py:299-322`) fails only on dropped registry rows or lowered floors, and
     C1/C2 touch neither file. Floors are minimums, so even a future registration is not
     endangered by r94's added arms.

4. **Anchor counts intact at the working tree today** (the counter's anchor-count guard makes any
   extra occurrence a NOT-EVALUATED, so these are the C1/C2 builders' hard constraints):
   - `ok_pin, pin_detail = kill_set_check(committed, pinned)` — exactly 1x
     (`check_mutation_battery.py:370`).
   - `print("could-not-evaluate: %s" % exc)` — exactly 3x (`:467`, `:470`, `:643`).
   - `return n == want, "observed` — exactly 1x (`:189`).
   - `        for path in scripts:` / `            if path not in INSTRUMENT_PINS:` — exactly 1x
     as code (`check_tip_battery.py:350-351`).

**Verdict:** C1 and C2 are causally separable at every layer checked (imports, process spawns,
pin tables, size sums, floors registry). The plan's separability sentence holds; no amendment
needed. Neither claim changes a no-harm reading of the other's instrument.

## Part 2 — sibling lanes: prior art and overlap

Scan method (with caveat): fleet-wide greps over /home/vgpnk/Projects/shokunin for `sniff`,
`decoy`, `selftest-kills` (excluding `!**/.ufo/**;!**/.tower/**;!**/node_modules/**`) proved
unreliable on nested lane repos (one call returned "no matches" while kotoba's own tracked
`verifiers/fixtures/round-94/selftest-kills.py:3` contains the token — confirmed tracked via
`git ls-files verifiers/fixtures/round-94`, which lists `forgery-sniff.patch` and
`selftest-kills.py`). Fleet-root bookkeeping (LOG.md, MANIFEST.json) was covered; per-lane scans
(tameshi corpus + evidence, kengaku, revenger, kumitate) are the authoritative results below.

- **No sibling ships a decoy-guarded self-test-kill counter over its own instruments.** No
  tracked sibling source matches `selftest-kills`, `anti-sniff`, `must-kill`, `decoy comments`,
  or `mutant-kill counter`-style decoy guards. The only fleet-root `decoy` hits are historical
  campaign notes (LOG.md kaidoku25/r40/r48/r59 rows; MANIFEST.json spotcheck blurbs), not code.
- **Closest prior art to kotoba's r94 decoy/anti-sniffing guard — tameshi (method owner):**
  - `tameshi-shokunin/corpus/knowledge/runner-tally-audit.md:19`: the frozen counter passes
    "8 must-accept copies: the pristine runner, the equivalent guard T07, reordered operands,
    **decoy comments that carry every frozen mutant's text**, cosmetic edits, a renamed harness
    variable…" — the same anti-sniffing shape as kotoba's r94 decoy (unmodified target + inert
    mutant-text comments must still pass), documented in tameshi's held knowledge.
  - `tameshi-shokunin/corpus/knowledge/witness-equivalence-rule.md:23`: "Cosmetic/decoy clones
    (comments, nonces, spacing) are satisfiable — as they must be".
  - tameshi round-35 lesson A7: a here-doc decoy carrying a pristine block copy fooled an
    earlier counter (decoy as attack vector); round-76/83/86 record forgery/cheat-class
    batteries against frozen counters.
- **Adjacent, different guard (attribution, not anti-sniffing):**
  - kengaku rounds 40-44 are a documented "mutant-kill counters" class
    (`kengaku-shokunin/.ufo/waves/round-45/w1/R45ConnPattern.md:92` — pinned tools, frozen
    literal mutant table, attributed kills); SCORECARD rows `attributed-mutant-kills` (r42,
    :1774) and `value-attributed-mutant-kills` (r43, :1893) count a kill only when a traced
    re-run executes the replaced span and differs — a stricter kill-attribution guard than
    kotoba's r94 decoy guard, which addresses a different failure (source-text sniffing).
  - revenger: every sweep instrument since r82 ships "ONE frozen sed mutant dies exit 1
    attributed" receipts (`sweepN-mutant-kill-after.log`, LOG.md:1171/1178/1186/1195/1204);
    r87 adds a two-mutant attributed pair. Discipline overlap, no decoy guard.
  - kumitate: `scripts/gate-mutants.mjs`, described in kengaku's overlap table
    (`.ufo/waves/round-55/w1/CN1SiblingArgv/overlap.md:44`) as a "mutant-kill fence for
    kumitate's own gates"; r63/r64 wave mutant-killer controls (pristine-pass 19/19,
    mutant-killed 19/19).
- **Province check:** kotoba's PROVINCE.md § Adjacent (tameshi row, pinned a944eb55) already
  cedes "the reusable fixture and mutation method" to tameshi while "each lane's gate stays its
  own", and records that kotoba's `verifiers/*` are "unsurveyed sightings" in tameshi's ledger.
  Kotoba's r94 counter guards kotoba's own instruments — no absorption of tameshi's method, no
  sibling names kotoba's instruments as theirs. **No province violation; overlap is
  method-level and already arbitrated.** Finding for the L1/scribe (no seat acts): the r94
  lesson could cite tameshi `runner-tally-audit.md` as prior art for the decoy-comment guard,
  the way S269 (PIT) is cited for the outcome classes.

## Part 3 — three candidate round-95 claims (evidence-backed; no freeze)

1. **Floors ratchet for the two r94-hardened self-tests (consistency/anti-shrink; the
   compatible synthesis of C1+C2).** Neither `check_mutation_battery.py` nor
   `check_tip_battery.py` has a floors-registry row or an in-file floors entry (Part 1 §3
   greps: 0 hits). After r94 lands its new behavioural arms, the only protections are the five
   frozen anchor lines and the counter's frozen mutants — an arm dropped by a future round
   (without touching an anchor) stays green: the exact defect class the floors guard exists for
   (its own docstring records the round-58 correction_sweep registration: "its self-test was
   unfloored, so a dropped case … still read green"). Claim shape: register
   `mutation_battery` and `tip_battery` self-test floors in `verifiers/floors-registry.json`
   plus both in-file tables of `check_assertion_floors.py`, at the r94 landed counts.
   Coupling to declare up front: `check_assertion_floors.py` is pinned by INSTRUMENT_PINS
   (`check_tip_battery.py:96-115`), so the bump needs a new admitted blob row there — the
   r91/r92 precedent ("round-91 claim C2 leg A(d) admission… the earlier blobs are kept") is
   the template; the tip battery's floors compare fails only on drops/lowerings, so no-harm is
   structural.
2. **AST-sniffer disclosed-bound probe (depth).** The counter's bound is frozen in its own
   header (`selftest-kills.py:33-35`: "a sniffer that skips comments (e.g. AST-based) is not
   caught by this guard") and the plan's disclosed bounds. Round 95 could freeze a
   `forgery-sniff-v2.patch` whose self-test "kills" mutants by AST-level inspection of its own
   source (comment-skipping), take a receipt showing the r94 decoy guard does NOT catch it
   (`C1-PREDICATE-UNMET` via the honest guard, i.e. the bound measured, not just disclosed),
   then a successor claim adds a behavioural arm that kills the AST sniffer — the r86
   cheat-class playbook (committed attack classes + pre-freeze controls) is the lane's proven
   route.
3. **Fail-closed receipt-header parsing, class-wide (mined-mistake generalization).** The r94
   mined mistake is `verifiers/fixtures/round-93/check-receipt-revs.sh` failing open on
   header-shaped lines it cannot parse (41-hex `REV=` dropped; indented header ignored —
   plan § Frontier step, CriticClaimsR93 D2/D3), fixed this round by ExecReceiptHeaders with
   committed fixtures under `verifiers/fixtures/round-94/receipt-headers/`. Round 95 could
   census every committed fixture that parses `REV=`/hex header lines across
   `verifiers/fixtures/round-91/-92/-93` drivers and claim each fails closed the same way
   (MALFORMED + exit 1), one committed fixture per instrument — converting a one-file fix into
   a held class.

## Findings

- F1 (claim-supporting): C1/C2 causally separable at every checked layer — plan sentence holds,
  exact lines cited above.
- F2 (prior art): tameshi `runner-tally-audit.md:19` documents the decoy-comment must-accept
  shape kotoba's r94 guard implements; attribution-style kill guards exist in kengaku (r42-43
  SCORECARD rows), revenger (per-instrument frozen sed mutants), kumitate
  (`scripts/gate-mutants.mjs`). No sibling ships the kotoba shape; no province violation.
- F3 (counter defect check — none found): anchors match their declared counts exactly at the
  working tree (1x/3x/1x/1x); the counter's CLAIMS, predicate and decoy construction are
  self-consistent with the plan. No rescue needed; no amendment indicated.
- F4 (tooling caveat): the grep tool's fleet-root scans over nested lane repos are unreliable
  (one false "no matches" against a tracked, existing token). Per-lane scoped scans are
  trustworthy. Recorded so a later seat does not read a fleet-wide "no matches" as evidence.

## Risks

- R1: C1 arms grow the mutation-battery self-test runtime; the counter kills only within 600 s
  (`selftest-kills.py:58` TIMEOUT_S). Stub-world self-tests are fast today (pre-data receipt
  `receipts/redbefore-c1-base.txt` honest rc 0), so headroom is large — noted, not blocking.
- R2: C2's new coverage loop must not restate the two-line anchor block (`:350-351`); C1 must
  not restate any of its three anchors — a second occurrence is an instant NOT-EVALUATED
  (anchor-count guard), an honest stop that wastes a landing.
- R3: post-r94, the new arms are anchored only by the frozen lines and mutants; until a floors
  row exists (Part 3 candidate 1) a future non-anchor-touching edit could drop an arm silently.

No tool installs or upgrades were needed (stdlib reads and repo greps only). No processes
started beyond the shell calls themselves; scratch removed.
