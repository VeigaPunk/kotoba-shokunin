# MutTesterTip94 — round-94 w1 — mutants beyond the frozen set (C2) and the receipt-check fix

Status: IN PROGRESS (waiting for ExecTipSelfTest_READY and ExecReceiptHeaders_READY)

Seat: MutTesterTip94 (mutation-tester, leaf — no subagent dispatch).
Base for both candidates: freeze commit edc731a91a956f6df20c27a74fb981b286f6ba58.
Scratch: /fast/scratch/hyaku/kotoba-r94/MutTesterTip94 (TMPDIR and HYAKU_SCRATCH point here; removed before yield).

## Method (same bounded behavioural detector as the frozen counter, applied to non-frozen mutants)

For (a), per mutant of verifiers/check_tip_battery.py at the candidate revision:
- clone the candidate rev from the seat scratch clone (`git clone --shared`), never committing the mutant;
- honest run: `python3 -B verifiers/check_tip_battery.py --self-test` → expect rc 0 and `0 failure(s)`;
- anchor must match exactly the declared number of times and the mutated bytes must compile, else could-not-evaluate;
- mutant KILLED iff the self-test exits non-zero within 600 s;
- decoy per target mutant: unmodified instrument with the replacement appended as `# r94-decoy <line>` comments must exit 0 (anti-sniffing control);
- instrument bytes restored and hash-compared after every run.

For (b), per mutant of the fixed MALFORMED rule in verifiers/fixtures/round-93/check-receipt-revs.sh:
- run the mutated checker on the committed fixture worlds under verifiers/fixtures/round-94/receipt-headers/
  and on the round-93 landing receipts;
- expected (fix, unmutated): MALFORMED verdict + rc 1 on each malformed fixture world, rc 0 + `9 resolved, 0 unresolved` on the landing receipts;
- mutant KILLED iff any expected rc/verdict line differs (i.e. the committed fixture world catches the weakened rule).

A surviving mutant is a coverage finding, not a contract change. No frozen file is edited; all probes run in the seat scratch clone.

## Part (a) — NEW mutants of the C2 key-coverage block (beyond p0–p2)

Probe harness: /fast/scratch (seat scratch) `probe_tip.py` — the frozen counter's mechanics (clone REV,
literal substitution in the probe clone only, honest/mutant/decoy, KILLED iff self-test rc != 0 within
600 s, anchor count and compile checked, restore + sha256 compared). The frozen counter file is not
modified; these five mutants are NOT in its frozen tables.

Mutants (anchor = the pinned two-line key-coverage block of run_guards; n3 uses the three-line form
ending in the `failures.append` line):

| mutant | concept | replacement core |
|---|---|---|
| n1-skip-middle-key | skip the middle key (BATTERY[3]) | `for path in scripts[:3] + scripts[4:]:` |
| n2-threshold-gate | coverage only when a key count threshold holds | `for path in (scripts if len(INSTRUMENT_PINS) >= 7 else []):` |
| n3-fail-other-guard | FAIL filed under another guard id | append guard id `instrument-pin` → `instrument-size` |
| n4-pins-keys-not-battery | coverage over INSTRUMENT_PINS keys instead of BATTERY | `for path in INSTRUMENT_PINS:` |
| n5-normalised-compare | path compared after normalisation | `if os.path.normpath(path) not in INSTRUMENT_PINS:` |

### Baseline at edc731a91a956f6df20c27a74fb981b286f6ba58 (BEFORE the C2 fix — pristine bytes)

Receipt: baseline-tip-edc731a.txt (copied to w1/MutTesterTip94/).

- honest rc 0: `self-test: 0 failure(s) over 80 assertions`
- n1-skip-middle-key rc 0 SURVIVED — the base self-test drops only BATTERY[5], so a skipped middle key is invisible
- n2-threshold-gate rc 1 KILLED — dead loop removes even the BATTERY[5] missing-key failure
- n3-fail-other-guard rc 1 KILLED — FAIL line moves to instrument-size; the `guards 4 of 5` tally arm breaks (3 of 5)
- n4-pins-keys-not-battery rc 1 KILLED — iterating INSTRUMENT_PINS makes `path not in INSTRUMENT_PINS` always false
- n5-normalised-compare rc 0 SURVIVED — BATTERY paths are already normalised; equivalent over every fixture world
- decoys held 5 of 5 (all rc 0 — no sniffing)
- instrument sha256 before 7c8e741cce4ee416be9e673c184aaf6fd6be569023a44842cacacef26b31464b == after, restored True

Prediction for the candidate (base + ExecTipSelfTest.patch): the C2 behavioural arms must kill n1; n5 is
an expected survivor (equivalent mutant) unless an arm introduces a non-normalised path.

### Candidate A: edc731a + ExecTipSelfTest.patch (commit 189ca33c551aef6499b5f91cede471378cd9d617)

Patch sha256 726e15b9c617a6e690a46e6b2748428c283186223dd51568232346928e7983d7 (verified against the
builder's claim). READY has not landed yet, so this is a pre-READY probe; it is rerun if the patch bytes change.
Built in a separate scratch clone: `git apply --check` ok, committed, instrument blob `66171de4eb2f`.
Receipt: candA-tip-189ca33c.txt.

Honest: `self-test: 0 failure(s) over 102 assertions`, rc 0.

| mutant | candidate A | at base (edc731a) | decoy |
|---|---|---|---|
| n1-skip-middle-key | **KILLED** rc 1 (`FAIL pin keydrop-3 world tally reads guards 4 of 5`) | SURVIVED | HELD rc 0 |
| n2-threshold-gate | **KILLED** rc 1 (`FAIL pin keyswap world names only that key: []`) | KILLED | HELD rc 0 |
| n3-fail-other-guard | **KILLED** rc 1 (`FAIL pin keyswap world tally reads guards 4 of 5`, guards 3 of 5) | KILLED | HELD rc 0 |
| n4-pins-keys-not-battery | **KILLED** rc 1 (`FAIL pin keyswap world names only that key`) | KILLED | HELD rc 0 |
| n5-normalised-compare | SURVIVED rc 0 (`0 failure(s) over 102 assertions`) | SURVIVED | HELD rc 0 |

Instrument sha256 before == after (`d5bf4e64…`), restored True.

Interpretation:
- Candidate A kills n1, the mutant the base self-test could not see (a middle key skipped). The per-key
  keydrop-3 world catches it; the base's BATTERY[5]-only arm missed it.
- n2–n4 were already killed at base and stay killed (no regression).
- n5 is an equivalent mutant over the committed fixtures: every BATTERY path is already a normalised
  repo-relative path, so `os.path.normpath` is the identity on the compared keys. A non-normalised key
  (e.g. `./verifiers/...`) would be the behavioural test, and no fixture world carries one. Residual, not a defect.

## Part (b) — mutants of the fixed MALFORMED rule

Detector: run the (mutated) checker on committed fixture worlds under
verifiers/fixtures/round-94/receipt-headers/ plus the round-93 receipts dirs, and compare rc and
verdict lines against the fix's honest readings.

### Baseline at edc731a (BEFORE the fix — base checker)

- `.ufo/waves/round-93/receipts/landing` → `2 scratch-declared / receipt revisions: 7 resolved, 0 unresolved over 14 files`, rc 0
- `.ufo/waves/round-93/receipts` (full) → `4 scratch-declared / receipt revisions: 9 resolved, 0 unresolved over 19 files`, rc 0 — matches the plan's `9 resolved, 0 unresolved` reading
- receipt-headers/ fixtures do not exist at edc731a (they land with the fix patch)

### Candidate edc731a + ExecReceiptHeaders.patch

Planned mutants of the fixed MALFORMED rule (smallest behaviour-bearing substitution of the fixed
script bytes; anchors chosen from the patched bytes, each required to match exactly once):

| mutant | concept | replacement core | result on candidate 4c8c3c9d |
|---|---|---|---|
| r1-39hex-accepted | header-shaped line with ≤39 hex no longer "shaped" → silently dropped (fail-open at sub-40) | `shaped_header` hex run `[0-9a-fA-F]+` → `[0-9a-fA-F]{40,}` | **SURVIVED** — all worlds identical |
| r2-tab-indent-ignored | leading-tab header no longer stripped → header shape unseen | `body.lstrip()` → `body.lstrip(' ')` | **KILLED** — indented world loses the TAB line `MALFORMED …/indented/headers.txt:2 leading whitespace before the declaration` |
| r3-malformed-exit-0 | MALFORMED counted and printed but does not drive exit | exit cond drops `malformed` | **KILLED** — hex41 and indented rc 1 → 2 (`resolved` 0 → no candidates) |
| r4-scratch-swallows-malformed | declared lines escape the MALFORMED branch | `if shape is None:` → `if shape is None or scratch_line.search(line):` | **SURVIVED** — all worlds identical |
| r5-malformed-not-printed | MALFORMED counted, exit intact, report line suppressed | `print(f'MALFORMED …')` → harmless assignment | **KILLED** — hex41/indented lose their MALFORMED lines (rc unchanged) |

Detector: probe_receipts.py (frozen-counter mechanics adapted to a bash+heredoc instrument: clone REV,
literal substitution in the probe clone only, heredoc python `compile()` gate — compile failure is
could-not-evaluate, never a kill — and per-world (rc, full stdout) comparison against the honest
readings recorded first in the same run). Receipt: candB-receipts-4c8c3c9d.txt (copied to
w1/MutTesterTip94/). Script sha256 before == after (`b896c8f8…`), restored True.

### Honest readings of the fix at candidate 4c8c3c9d3b28949ad1e664d062823f5788549dee

| world | rc | reading |
|---|---|---|
| receipt-headers/good | 0 | `malformed declarations: 0`, all 4 declarations resolved |
| receipt-headers/hex41 | 1 | `MALFORMED …hex41/headers.txt:1 hex run is 41, not 40` |
| receipt-headers/indented | 1 | two MALFORMED lines (space- AND tab-indented), `malformed declarations: 2` |
| round-92 receipts/landing | 1 | `2 scratch-declared; malformed declarations: 0; 1 resolved, 5 unresolved over 18 files` — **identical counts at base** (the 5 UNRESOLVED `cd355c47…` lines pre-exist; that rev is not an object of the lane repo); the fix adds only the `malformed declarations: 0` line → no regression |
| round-93 receipts/landing | 0 | unchanged (`7 resolved, 0 unresolved over 14 files`) |
| round-93 receipts (full) | 0 | unchanged (`9 resolved, 0 unresolved over 19 files`) — the plan's no-harm reading |

### Part (b) findings

1. **r1 SURVIVED — coverage gap.** No committed fixture carries a sub-40 hex header (only 41 and 12/G1
   are exercised), so the fail-open-at-39 mutant is invisible to the committed fixture world. A
   `receipt-headers/hex39/` world (one `REV=<39 hex>` line, expected `MALFORMED … hex run is 39, not 40`
   + rc 1) would kill it. Owned by ExecReceiptHeaders/L1 — I do not edit their files.
2. **r4 SURVIVED — equivalent-by-construction, interaction undemonstrated.** In the fixed script the
   `declared` (scratch) branch precedes the MALFORMED branch, so no line that matches
   `world rev\|forgery\|/scratch/` can ever reach the MALFORMED rule: my "exemption swallows malformed"
   mutant never changes behaviour on ANY input. The real risk is by-design: a header-SHAPED line that
   also matches a scratch pattern is exempt (not MALFORMED) — and no committed fixture demonstrates
   that interaction. A fixture world with one such line plus its expected reading would pin the
   intended semantics.
3. r2's kill needs the OUTPUT comparison, not rc: the tab fixture line is dropped silently but the
   world still exits 1 (the space-indented line still fires). Likewise r5 (report suppressed, count and
   rc intact) is killed only by comparing printed lines. A validator that reads only exit codes would
   pass both mutants — the receipts should carry the MALFORMED lines, which the builder's after-*.txt
   receipts do.

## Findings

1. C2 (candidate A, 189ca33c): the per-key arm kills the mutant the base misses (n1, a skipped middle key), and
   keeps n2–n4 killed. Residual: n5 (normalised compare) is an equivalent mutant over the committed fixtures.
2. Receipt-check fix (candidate B, 4c8c3c9d): kills r2 (tab indent), r3 (exit), r5 (report line). Survivors:
   r1 (39-hex fail-open, a coverage gap: add `receipt-headers/hex39/`) and r4 (equivalent by construction;
   the intended scratch-plus-malformed interaction is undemonstrated).
3. No regression: round-93 landing receipts stay `9 resolved, 0 unresolved` rc 0 (full dir) and `7 resolved, 0 unresolved`
   rc 0 (landing); round-92 landing reads rc 1 at both base and candidate with identical counts (pre-existing UNRESOLVED
   `cd355c47…` lines, not caused by the fix).

## Risks

- The part-(a) and part-(b) probes are not the frozen counter; they show detection of the listed mutants, not of
  every mutant (plans/round-94.md, "Disclosed bounds").
- The receipt-check fixtures do not cover a 39-hex header (r1) or a scratch-plus-malformed line (r4); a regression
  in those shapes would pass the committed fixtures.
- Scratch clones (repo, repo2, repo3, probe dirs) under /fast/scratch/hyaku/kotoba-r94/MutTesterTip94 are removed before
  yield; the copied receipts under w1/MutTesterTip94/ are the retained evidence.

## Status

Final. READY landed for both builders (ExecTipSelfTest sha 726e15b9…, ExecReceiptHeaders sha 5c3f3763…). Probes ran on
the verified patch bytes. Frozen counter `c2` on candidate A (189ca33c): C2-PREDICATE-MET, rc 0
(receipt counter-c2-candA.txt).
