# ConnectorOverlapR95 — overlap scan and planning data-walk (round 95, wave r95-w1)

Seat: ConnectorOverlapR95 (connector, leaf — no subagent dispatch). Read-only: every repo claim below is
read from committed bytes at the freeze commit `673d1e2e6f850bb54dda9698cf825cf6788c7d0d` or from
frozen instrument files; no repo writes except this report and `ConnectorOverlapR95/anchors-at-freeze.txt`.
Working-tree drift check at scan time: `git diff --stat 673d1e2e -- verifiers/check_mutation_battery.py
verifiers/fixtures/mutation-battery/manifest.tsv verifiers/floors-registry.json verifiers/check_tip_battery.py`
→ empty (no sibling had landed on the coupled files when this scan ran; line numbers below are freeze-commit
lines and stay valid for the builder's base).

## Part 1 — does any no-harm instrument pin a blob/line/assertion count of check_mutation_battery.py?

**Verdict: no.** No no-harm instrument pins the battery's blob, its line count, or its self-test assertion
count. Adding behavioural arms inside `self_test()` (L661) plus helpers adjacent to it changes no no-harm
reading, subject to the five byte-couplings in (5)–(6). Exact lines:

1. **Floors gate — the battery is NOT floored.** `verifiers/floors-registry.json`: `"instrument_total": 19`
   with rows checklist 1863, compare_harness_independent 330, corpus_independent 105, corpus_integrity 164,
   floors_guard 176, freeze_gate 34, harness 10, harness_independent 123, pins 62, overlap_levers 51,
   surfaces 218, dispatch_prompts 56, sibling_census 68, alwayson 89, correction_sweep 25, scoped_rules_v32
   240, spec_craft 250, sibling_reread 47, omp_root_semantics_v2 68 — no `check_mutation_battery` row.
   `verifiers/check_assertion_floors.py` agrees: `EXPECTED_INSTRUMENTS` (L185+) and `INSTRUMENTS` (L238+)
   carry the same 19, none the battery. The only count-shaped pin in the floors world is the registry size
   (floors self-test F6 arm hardcodes `"instrument_total": 19`, check_assertion_floors.py:878) — it pins the
   REGISTRY, which no seat touches. No floor anywhere reads the battery's `0 failure(s) over N`.
2. **Tip battery — the battery is UNPINNED and OUT of the measured battery.**
   `verifiers/check_tip_battery.py`: `INSTRUMENT_PINS` L132–165 pins 7 blobs (check_gate_registry,
   check_assertion_floors, check_freeze_gate, verify_skill_checklist, verify_corpus_integrity,
   verify_corpus_independent, check_correction_sweep) — no battery key. `BATTERY` L178–186 runs six scripts,
   none the battery, so the instrument-size guard (numstat over those six, L329–357, LINE_CAP 900) never
   sees battery line deltas. The no-deletions guard (docstring L38–39, code L285–297) fails only on a
   verifiers/-prefixed path tracked at base being ABSENT at rev — an edit keeps the path present.
   The instrument-pin guard (L343–352) iterates the pin table and the six BATTERY scripts only.
3. **Gate registry.** SKILL.md L522 (the battery's row): Pinned values cell = `verifiers/fixtures/mutation-battery/manifest.tsv`
   only; entry command and verdict map unchanged by arms. `check_gate_registry.py` compares rows with files
   (existence) — no byte/count pin.
4. **Manifest anchors (frozen).** `verifiers/fixtures/mutation-battery/manifest.tsv` has exactly three kill
   rows targeting the battery — mb-m2-g1-commit-check-skipped (G1 commit-check regex), mb-m15-clean-tree-guard-off
   (`git(dest, "status", "--porcelain")` guard), mb-m16-restore-unverified (`place(dest / row.target, ...)`
   restore read-back). All three anchor regions sit in the G1/G2 machinery OUTSIDE `self_test()` (which starts
   L661), so arms cannot break them; the builder simply must not edit those lines. `KILL_SET_PINNED = 17`
   (L87) pins the manifest's kill-row count — the manifest is frozen, no row may be added or removed.
5. **Counter anchor bytes inside the battery** (byte-identical, matching exactly as declared; ANTI-SNIFFING
   forbids adding occurrences anywhere in the file, arm messages included):
   - `committed = git_show(lane, rev, MANIFEST).decode("utf-8")` — L366 (1×; c1 n1)
   - `raise CouldNotEvaluate("manifest must name exactly the targets %s"` — L369 (1×; c1 n5)
   - `return n == want, "observed` — L189, `kill_set_check()` (1×; c1 n11 and positive n10)
   - `ok_pin, pin_detail = kill_set_check(committed, pinned)` — L370 (1×; r94c1 k1, also r94 c1 k1)
   - `print("could-not-evaluate: %s" % exc)` — L467, L470, L643 (3×; r94c1 k2, also r94 c1 k2).
     **L643 is in the helper immediately before `self_test()`** — inside the builder's writable region; if
     that helper is edited the 3-count must be preserved. All five mutated statements live outside
     `self_test()` and keep their line counts under the frozen replacements, so an arms-only edit is
     line-safe by construction.
6. **Round-94 counter (no-harm requires its c1+c2 MET at the landing rev).**
   `verifiers/fixtures/round-94/selftest-kills.py`: c1 anchors are the same strings as r95's r94c1 table
   (L61–78 there); c2 targets `check_tip_battery.py` (L80–96) and is untouched by a battery edit. Honest
   conjunct of BOTH counters: the battery self-test must be CLEAN at the landing rev (r94 form `"0 failure(s)"`,
   v3 form exit 0 + N = 0) — every new arm must pass on honest bytes.
7. **Public-path controls are arm-insensitive.** r92 `controls-run.sh` (step lines 24–27, ctl-c1-*/ctl-c2-*)
   and r93 `c1-killpin-rev.sh` (L6–10, battery() L43–45, named() L47) drive the battery's public `--rev`
   path against committed fixture worlds, not `--self-test`; arms change nothing they read. r93 `c2-pinkey.sh`
   likewise exercises the public pin path.

Precedent that this stays true when arms grow: round 94 grew the battery self-test from 19 to 38 assertions
(fleet `.ufo/reports/round-94/kotoba.md`:59) and every table in (1)–(4) was unaffected — nothing in the
no-harm set counts assertions.

### Second-order effect for ExecBatteryKills (risk, not a pin)

Under the v3 runner, a mutant run compiles the mutated text and executes it as `__main__` **while the file on
disk holds the honest bytes**. An arm that observes behaviour by re-spawning the instrument as a subprocess
(`python3 <instrument> --self-test …`) therefore runs the HONEST bytes during every mutant run: it cannot kill
any mutant, the counter reads `targets killed 0 of 3`, and C1 is honestly unmet. New arms must observe
IN-PROCESS behaviour — drive the module functions the mutants change (the rev-path manifest read behind L366,
the L369 refusal, `kill_set_check` at L189) on fixture worlds inside the same interpreter, tallied through
`t.check` so kills are REPORTED failures. No new occurrence of any of the five anchor strings may appear
anywhere in the file (a new arm's assertion text included).

## Part 2 — sibling prior art and province overlap

Method note: the grep glob `*-shokunin/verifiers` does not expand in the grep tool (re-probed with the
trivial pattern `def self_test|self-test`, which certainly exists in kotoba — also empty), so two early
scoped sweeps are void; the findings below come from fleet-root greps excluding `.ufo/prompts/**` and
`.git/**`, plus targeted reads of sibling files.

- **tameshi — the method lane (adjacent; nothing to absorb).** tameshi PROVINCE.md:1–19 owns "the reusable
  method of honest checks … mutation testing, fail-closed arms, verdict-line discipline" while "every lane's
  gate remains its own"; kotoba's PROVINCE tameshi row states the same split, and
  `tameshi-shokunin/corpus/knowledge/fleet-kill-rate-ledger.md` §3 (~L117–121) records kotoba `verifiers/*`
  as **sightings — file existence O, gate-ness U until a survey admits them**. So kotoba building its own
  kill counter is inside its province (PROVINCE.md Core names `check_mutation_battery.py` as its instrument),
  and tameshi's corpus is the prior art to CITE: `corpus/knowledge/mutation-score-semantics.md:21-23` —
  "Inconclusive — timeout, crash before summary, or missing count is not a kill and is excluded" — is
  exactly kotoba v3 rule 1's class (RUN-ERROR never a kill; timeout could-not-evaluate, stricter than
  Stryker who counts timeouts detected, per the same file's S001 rows). Survivor vocabulary: the ledger §4
  classes (a) reported-but-unasserted, (b) unreached fixture/arm map cleanly onto N5 (wrong-label refusal
  never exercised) and N1/N11 (unreached arms — rev==HEAD everywhere; +2 unexercised).
- **chousa r75 — the forgery-class family catalogued.** `chousa-shokunin/.ufo/waves/round-75/w1/R75Connect/`
  (sibling-scan.md/.json) + R75Critic.md + R75Mutation.md survey the same defect class across lanes: kama r28
  CtlSourceBlind (pre-freeze source-blind ceilings, round-28.md:34), kumitate Q43/A48/R68 (frozen-and-executed;
  per-case line corroboration; answer-key masking), kaidoku Row 78 ("a battery's forgery must differ where it
  claims to"), tsukuroi r35 K08 (shuffling kills order oracles), tabi Q90/Q112, mado QUALITY 88, souji Q120.
  Chousa's M2 finding is the sharpest parallel: its battery killed its order forgery for the WRONG reason
  (9-entry oracle starved by 12 cases, not by shuffling; R75Mutation.md "case-count starvation"). v3's
  count-checked anchors plus comment+code decoys are kotoba's answer to the same "killed for the declared
  reason" requirement (cf. check_assertion_floors.py:711-713 "count-checked, so a no-op mutation cannot
  masquerade as a passing fixture").
- **What is novel (no sibling overlap):** no sibling counter runs mutants SOURCE-BLIND (mutated code object
  executed as `__main__` while the disk file holds honest bytes) or inserts mutated statements under a
  run-time-false `__decoy__` guard; `RUN-ERROR` as a counter outcome class exists only in kotoba's v3.
  Searches: `__decoy__`, `source.blind`, `RUN-ERROR`, `selftest-kills` over all lanes (prompt archive
  excluded) return only kotoba's round-94/95 machinery, kotoba's own r37/r38 blindness-boundary history
  (MANIFEST.json:4527 — a different, intentional use), and the chousa/tameshi records above.
- **kotoba round-94 receipt** (fleet `.ufo/reports/round-94/kotoba.md:44-65`): r94 landed f65347a6 with the
  A2 bound "the frozen predicate can also be met by a comment-skipping source sniffer" — v3's rules 2–3 close
  exactly that, and my Part 1 scan shows the no-harm set tolerated the r94 assertion growth, so it tolerates
  the r95 arms for the same reason.

## Part 3 — three candidate round-96 claims (frontier walk from r95 evidence)

1. **C-r96a (skill-craft, preferred — prompt/skill craft, not verifier internals):** depth on a
   province-owned instrument — bring the v3 pattern to `verifiers/verify_dispatch_prompts.py` (floors row
   `dispatch_prompts`, floor 56): behavioural arms that kill a frozen mutant set of the dispatch-prompt
   verifier, decoy-guarded and source-blind, measured by a counter in the selftest-kills shape. This moves
   the r95 machinery onto the lane's actual domain (dispatch-prompt craft) instead of the battery that
   watches the watchers. Evidence: the instrument is registered and floored; the v3 counter is proven on the
   battery this round; the subprocess trap in Part 1 becomes part of the claim's disclosed bounds.
2. **C-r96b (depth on the v3 counter's disclosed bound):** the plan discloses that "a self-test that sniffs
   its own compiled code objects (not its source file) and proves the decoy guard dead is not caught". Land
   that sniffer as a forgery world (inspect co_consts/bytecode of its own frame, evaluate the decoy guard's
   reachability) and show an extended counter reads it UNMET — closing the last disclosed sniffer class.
   Prior art: chousa M2 + kaidoku Row 78 (a forgery must be rejected for the reason the claim names).
3. **C-r96c (consistency, verifier-internal):** N1's root cause is fixture-shape, not code: every rev-path
   fixture world has `rev == HEAD`. A claim that every rev-consuming fixture world under `verifiers/fixtures/`
   exercises at least one `rev != HEAD` world (a coverage floor over fixture worlds, checked by a small
   guard), so rev-vs-HEAD confusions cannot survive in ANY instrument, not just the battery. Maps to tameshi
   survivor-class (b) "unreached fixture/arm". Run only if the wave wants more verifier depth after C-r96a.

## Risks

- **Subprocess-arm trap** (Part 1 closing note): the most likely honest failure of C1; if arms are written
  as subprocess re-invocations the counter reads 0 of 3 with run errors 0 and nobody misbehaved. Routed to
  Main via this report; ExecBatteryKills should design arms in-process from the start.
- **L643 helper**: the only counter anchor inside the builder's writable region; a refactor there must keep
  the `print("could-not-evaluate: %s" % exc)` count at exactly 3.
- **Anchor-string hygiene**: new arm names/messages must not contain any of the five anchor substrings
  (`raise CouldNotEvaluate("manifest must name exactly the targets %s"` is a prefix of the n5 REPLACEMENT, so
  the replacement text must never appear in honest bytes either).
- Sibling grep glob limitation documented above — findings rest on exclusion-filtered fleet greps plus
  targeted reads, not on a verified per-lane verifiers sweep.

## Verification performed (all read-only)

- `git show 673d1e2e:verifiers/check_mutation_battery.py | grep -n <anchors>` → lines recorded in
  `ConnectorOverlapR95/anchors-at-freeze.txt`; `git diff --stat 673d1e2e -- <4 coupled files>` → empty.
- Read: plans/round-95.md (full), selftest-kills.py (r95, header + CLAIMS + runner/decoy code), floors-registry.json,
  check_assertion_floors.py (tables + self-test pins), check_tip_battery.py (INSTRUMENT_PINS/BATTERY/guards/self-test),
  SKILL.md:522 raw, manifest.tsv, round-92 controls-run.sh, round-93 c1-killpin-rev.sh, round-94 selftest-kills.py,
  kotoba PROVINCE.md, tameshi PROVINCE.md + fleet-kill-rate-ledger.md + mutation-score-semantics.md,
  chousa round-75 wave records. No tools installed; no counter runs (read-only seat; scratch dir created and removed).
