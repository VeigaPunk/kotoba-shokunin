# CriticClaimR95 — falsification of frozen claim C1 (round 95, kotoba)

Status: final. Full candidate built from both READY patches; all counters and controls re-run;
scratch removed before yield.

## Verdict

**C1 on the full candidate: MET.** Candidate revision
`7e0b8475719958cbd0c7e1ac7f236423515a6bff` (= 673d1e2e6f850bb54dda9698cf825cf6788c7d0d +
ExecBatteryKills.patch f9506fe3… + ScribeCorpusR95.patch 6007a3a4…, applied and committed in my
scratch clone, identity `scratch <scratch@invalid>`, toplevel asserted; changed paths exactly
`verifiers/check_mutation_battery.py` (+67), `corpus/SOURCES.md` (+1), `corpus/lessons/round-95.md`
(new 174), `corpus/README.md` (+1)). No counter defect found that changes the verdict. Findings
F1–F3 below are provenance/sharpness notes, not predicate defects.

Evidence (my runs, receipts under `w1/CriticClaimR95/`):

- `candidate-c1.txt`: honest rc 0 CLEAN `0 failure(s) over 46 assertions`; n1 KILLED (2 failures),
  n5 KILLED (1), n11 KILLED (2); positive n10 KILLED (2); comment decoys held 3/3; code decoys held
  3/3; `C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1` → **`C1-PREDICATE-MET`,
  rc 0**.
- `candidate-r94c1.txt`: k1/k2/k3/k0 all KILLED, honest CLEAN, decoys 3/3+3/3 →
  **`R94C1-PREDICATE-MET`, rc 0** (the v3 rules do not refuse honest arms).
- `census-candidate.txt`: `sources-census.sh validate --file <candidate>/corpus/SOURCES.md` → rc 0,
  34 W04 (no new; last is the pre-existing S269), 0 E; row count 195 → **196**.

## Pre-data receipts reproduced

- Do-nothing control at `2d886a91` (`redbefore-repro.txt`): line-for-line equal to
  `receipts/redbefore-c1-base.txt` — 3 targets SURVIVED rc 0, positive KILLED, honest CLEAN 38
  assertions, decoys 3/3+3/3, `C1-PREDICATE-UNMET`, rc 1. ✓
- Forgery worlds: I re-ran the frozen builder (`build-forgeries.py 2d886a91 <scratch>/forgeries`)
  and all six regenerated patches are **byte-identical** to the frozen
  `verifiers/fixtures/round-95/forgeries/*.patch`. Counter runs on my world commits (`f1..f6-repro.txt`):
  all six `C1-PREDICATE-UNMET` rc 1, and all 13 run lines of each are identical to the pre-data
  receipts `receipts/forgery-<world>.txt` (the receipts additionally carry an appended `rc=` line).
  f6 reads `run errors 1` — rule 1 refusing the crash-signal. ✓

## Attack answers

- **Do-nothing or cheaper change?** Do-nothing is UNMET (verified at base). A cheaper honest
  change does not exist: the frozen mutants are behaviour gaps (rev≠HEAD manifest, target-set
  refusal label, +2 rows), every anchor-preserving non-arm edit either leaves rc 0 survivors or
  breaks an anchor (→ NOT-EVALUATED, never MET), and source-sniffing routes are dead under rules
  2–3 (f1–f5 all UNMET). The +67-line insertion in `self_test()` is the minimal surface.
- **Is C1 named by the surface it changes (§9)?** The §9 pointer dangles — no committed document
  in the lane carries a §9 (searched gen-w1.py context/items, plans/, SKILL.md headings; round-94's
  gen asked the same "(§9)" question and its critic answered substantively via D6). Substantively:
  the surface is behavioural kill-capability arms in a mutation-testing gate — the same family as
  round-94 C1, which the round-94 closure scored **depth**. S270 is grounding for the kill rule,
  not the claim surface. "depth" fits; not quality work mislabelled.
- **Is S270 a fair ground?** Verified live (2026-11-05): docs.python.org/3/library/unittest.html →
  HTTP 200, 336978 B, sha256 `f9510cd7…ff3506d` = the plan's digest; quotes found at raw HTML
  lines 2413–2414 ("…raised an unexpected exception.") and 2421–2422 ("…explicitly signalled…"),
  title pin `Python 3.15.2 documentation` (line 20), footer `Last updated on Nov 05, 2026 (22:32
  UTC)` (line 3179) — all as the lesson states. Fairness: the self-test is a custom `t.check`
  tally, not unittest, so S270 grounds by analogy; the context-matched ground is S260 (verified
  live too: 27068 B, sha `8641c389…`, "Runtime error — The running of the tests resulted in an
  error (rather than a failed test)" verbatim at HTML line 24; "Killed" sentence at line 12). The
  decision "a crash is never a kill" remains the counter's rule choice; the lesson discloses
  exactly that scope ("not a mutation-testing vocabulary row and not a kill-rule formula"). Fair.
- **Mined mistake's fix fails on its committed control?** Yes at run granularity: in f6 the n11
  run drives two-added-rows behaviour and signals by uncaught `RuntimeError` rc 1 → RUN-ERROR,
  killed 0 of 3, UNMET; the round-94 rule (`rc != 0` = KILLED) scores the same run KILLED.
  Caveat F2 below: f6 does not flip the *predicate* between rule sets.
- **Lesson Gate: real same-round reject?** Yes — the Apache Ant `junit` task manual, sha-pinned
  (33365 B, `3f1ee369…`), rejected because it conflates the classes ("errors are considered
  failures as well", HTML line 104) and has 0 hits for "unexpected exception", with a stated flip
  condition; two more scout candidates (pytest exit codes, TAP 13) are honestly dispositioned as
  not-written with reasons, and the scout's 404s are disclosed.
- **Round-94 routed-defect list honestly dispositioned?** Yes, all six: 1 → L1 QUALITY criterion
  at integration (consistent with "L1 lands SCORECARD/LOG/QUALITY"), 2 → rule 1 (f6), 3 → rules
  2–3 (f2–f5), 4 → C1 with D3 carried and reasoned, 5 → carried and measured (ExecBaseBattery),
  6 → orchestrator-side. Provenance nit F1 below.

## Findings / defects

- **F1 (low, plan provenance)** — plans/round-95.md § C1 says round-94 MutTesterBattery94
  "recorded three mutants that the landed --self-test does not kill"; the report records **four**
  survivors (N1, N4, N5, N11). N4 (pin check moved after the probes) is dispositioned as
  "probably an equivalence in practice" only inside the attack report; the plan and the round-94
  lesson's routed defect 4 name only N1/N5/N11. Not a predicate defect (targets are frozen and
  well defined), but the count attribution is off by one and N4's rationale is not carried into
  the plan.
- **F2 (low, control-world sharpness)** — f6 demonstrates rule 1 at RUN granularity only. Under
  the round-94 rule f6 still reads UNMET (n1/n5 remain rc 0 survivors), so the world does not
  flip the PREDICATE between rule sets. A crash-only forgery whose detector drives all three
  targets would flip MET→UNMET between rule sets; f6 is the weaker half of that demonstration.
  ExecCounterForgery may add the sharper world; no action needed for this round's verdict.
- **F3 (info)** — the wave item's "(§9)" pointer names no committed document in the lane (see
  attack answers). Substantive question answered; pointer should name its document or be dropped.
- **F4 (info, lane hygiene)** — `verifiers/fixtures/round-95/__pycache__/` exists untracked in the
  lane working tree (gitignored bytecode residue from a non `-B` run). Harmless; not mine to clean.

## Receipts (this seat, `w1/CriticClaimR95/`)

`redbefore-repro.txt`, `f1-repro.txt` … `f6-repro.txt`, `candidate-c1.txt`,
`candidate-r94c1.txt`, `census-candidate.txt`.

## Tooling

No install performed. No pacman. No host/kernel setting touched. No git/jj write in the lane;
only scratch-clone commits (candidate + forgery worlds in scratch). Scratch
`/fast/scratch/hyaku/kotoba-r95/CriticClaimR95` removed after this report.
