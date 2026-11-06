# SentinelScopeR94 — scope, safety and no-harm on the round-94 w1 candidate

Status: COMPLETE — all four READY files observed; candidate `86fe8bb4a6671d770e9d84fc6e47b113ddbd0e39`
built, checked and reported below. Scope PASS, no-harm PASS, safety PASS.

Assignment: after the four READY files appear, build the candidate = freeze commit
`edc731a91a956f6df20c27a74fb981b286f6ba58` + the builder patches, in a scratch clone, then:

1. scope — `git diff --stat edc731a…` lists only owned files; SKILL.md byte-identical; no
   spotcheck file, manifest.tsv, round-91/92 fixture or other verifier touched.
2. no-harm — gate registry (base 74 of 74), tip battery (base guards 5 of 5; 3 of 6 carried reds),
   `check_assertion_floors.py --self-test`, round-93 counters c1-killpin-rev.sh and c2-pinkey.sh
   (MET), census `--file` on the candidate SOURCES.md.
3. safety — no hardcoded /tmp in new committed code, no network in self-tests, no credential-shaped
   strings, no git writes outside a fixture tmpdir in the new arms.

Each check recorded as: command, observed line, PASS/FAIL. Findings appended below as they land.

## Base controls at the freeze commit `edc731a91a956f6df20c27a74fb981b286f6ba58`

All run from my scratch clone (`HYAKU_SCRATCH`/`TMPDIR` pointed at
`/fast/scratch/hyaku/kotoba-r94/SentinelScopeR94`), one heavy counter at a time:

| Check | Command | Observed | Verdict |
|---|---|---|---|
| gate registry | `python3 -B verifiers/check_gate_registry.py --rev edc731a…` | `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, rc 0 | PASS (base 74/74 confirmed) |
| assertion floors | `python3 -B verifiers/check_assertion_floors.py --self-test` | `0 failure(s) over 176 assertions`, rc 0 | PASS |
| census | `scripts/sources-census.sh validate --file <clone>/corpus/SOURCES.md` | rc 0, last line `file ok …/corpus/SOURCES.md` (W04 duplicate-url warnings only) | PASS |
| r93 c1 counter | `bash verifiers/fixtures/round-93/c1-killpin-rev.sh edc731a… <clone>` | `C1-PREDICATE-MET`, rc 0 | PASS (MET) |
| r93 c2 counter | `bash …/c2-pinkey.sh edc731a… <clone>` (fleet `/home/vgpnk/Projects/shokunin`) | `C2-PREDICATE-MET`, rc 0; honest world `guards 5 of 5; tip battery exit 0: 3 of 6` | PASS (MET; base guards 5/5, 3 carried reds) |

Receipts: `census-base.txt`, `c2-pinkey-base.txt` under `w1/SentinelScopeR94/`.

## Candidate

Candidate built per the handoff protocol in scratch clone
`/fast/scratch/hyaku/kotoba-r94/SentinelScopeR94/repo` (toplevel asserted equal to the clone):
freeze `edc731a91a956f6df20c27a74fb981b286f6ba58` + the four builder patches, single scratch commit
(identity `scratch <scratch@invalid>`):

**candidate rev `86fe8bb4a6671d770e9d84fc6e47b113ddbd0e39`**

Patch shas verified against the READY files before applying:
`cbf44a34…04834` (ExecBatterySelfTest), `726e15b9…e7983d7` (ExecTipSelfTest),
`5c3f3763…b9f974` (ExecReceiptHeaders), `b5b2c9cd…c199357f3` (ScribeCorpusR94) — all match.
All four applied clean (`git apply --check` OK on the untouched freeze tree).

### 1. Scope — PASS

`git -C $D diff --stat edc731a… 86fe8bb…` — 9 files, exactly the owned set, 225 insertions,
10 deletions:

| File | Owner |
|---|---|
| `verifiers/check_mutation_battery.py` (+26) | ExecBatterySelfTest (C1) |
| `verifiers/check_tip_battery.py` (+20/-10) | ExecTipSelfTest (C2) |
| `verifiers/fixtures/round-93/check-receipt-revs.sh` (+34/-10) | ExecReceiptHeaders |
| `verifiers/fixtures/round-94/receipt-headers/{good,hex41,indented}/headers.txt` (new) | ExecReceiptHeaders |
| `corpus/SOURCES.md` (+1 row), `corpus/README.md` (+1 row), `corpus/lessons/round-94.md` (new, 146) | ScribeCorpusR94 |

- SKILL.md byte-identical: `git diff edc731a… 86fe8bb… -- SKILL.md` empty, 600 lines. PASS.
- No spotcheck file, no `manifest.tsv`, no round-91/92 fixture, no other verifier touched
  (name-status lists only the 9 files above). PASS.
- FROZEN ANCHORS on the candidate blobs, byte-exact counts:
  `ok_pin, pin_detail = kill_set_check(committed, pinned)` ×1;
  `print("could-not-evaluate: %s" % exc)` ×3; `return n == want, "observed` ×1;
  tip battery two-line `for path in scripts:` / `if path not in INSTRUMENT_PINS:` block ×1.
  No new occurrences. PASS.

### 2. No-harm — PASS

| Check | Command | Observed | Verdict |
|---|---|---|---|
| gate registry | `python3 -B verifiers/check_gate_registry.py --rev 86fe8bb…` | `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, rc 0 | PASS (base 74/74 held) |
| tip battery | `python3 -B verifiers/check_tip_battery.py --rev 86fe8bb… --repo $D --fleet /home/vgpnk/Projects/shokunin` | (below) | (below) |
| assertion floors | `python3 -B verifiers/check_assertion_floors.py --self-test` (candidate tree) | `0 failure(s) over 176 assertions`, rc 0 | PASS |
| r93 c1 counter | `bash …/c1-killpin-rev.sh 86fe8bb… $D` | `C1-PREDICATE-MET`, rc 0 (217.5 s) | PASS (MET) |
| r93 c2 counter | `bash …/c2-pinkey.sh 86fe8bb… $D` | `C2-PREDICATE-MET`, rc 0; honest world `guards 5 of 5`; all three worlds hold | PASS (MET) |
| tip battery | `python3 -B verifiers/check_tip_battery.py --rev 86fe8bb… --repo $D --fleet /home/vgpnk/Projects/shokunin` | `guards 5 of 5` (no-deletions, floors, instrument-size, instrument-pin, spotcheck-identity all PASS); gates: gate_registry exit 0, correction_sweep exit 0, skill_checklist/corpus_integrity/corpus_independent exit 1 (the 3 carried reds), assertion_floors `exit none` (280 s cap timeout) → tally `tip battery exit 0: 2 of 6`, rc 1 | PASS — identical guard set and identical red set as the base; the only tally difference is the floors gate straddling its 280 s cap (see F-S1) |
| census | `sources-census.sh validate --file $D/corpus/SOURCES.md` at the candidate worktree | rc 0, last line `file ok …/corpus/SOURCES.md`; S269 W04 duplicate-url warning only (matches the scribe's receipt) | PASS |

Census harness note: my first census attempt extracted SOURCES.md alone into scratch
(`git show > scratch/cand-sources.md`) and read E11 `missing used-by` rc 1 — used-by paths resolve
against the `--file` parent directory, which did not contain the candidate tree. Rerun at the
candidate worktree reads rc 0. Harness artifact, not a candidate defect.

### 3. Safety — PASS

- Hardcoded `/tmp` in added lines: NONE (`grep -n '^+' candidate diff | grep -F '/tmp'`).
- Network in new committed code: NONE in code. One added `curl -sS …` mention is documentation
  prose in `corpus/lessons/round-94.md` (the S269 access record describing the fetch that
  produced the kept sha256) — not executed by any self-test.
- Credential-shaped strings in added lines: NONE (`password|passwd|secret|api_key|access_token|bearer|PRIVATE KEY` scan).
- Git writes in the new arms: C1 arms build/commit fixture worlds under the self-test tempdir
  (`build_fixture`/`_git_fixture` under `root`, removed in `finally`); C2 uses
  `_fixture_git`/`_commit_all` inside its per-world tempdirs; the receipt fix's embedded python
  only reads (`git -C repo` rev lookups). No git write outside fixture tmpdirs. PASS.
- New arms are behavioural (fixture runs, rc/output assertions; `kill_set_check` on fixture
  manifest text) — no self-test reads its own checker's source text. Anti-sniffing PASS.

### Receipt fix end-to-end spot-check (candidate bytes, executed from $D)

- round-93 landing receipts: `9 resolved, 0 unresolved over 19 files`, `malformed declarations: 0`, rc 0.
- `receipt-headers/good`: rc 0. `hex41`: `MALFORMED …:1 hex run is 41, not 40`, rc 1.
  `indented`: two `MALFORMED … leading whitespace before the declaration`, rc 1. Fail-closed as claimed.

## Findings

- F-S1 (harness note, not a candidate defect): the tip battery's floors gate
  (`check_assertion_floors.py`, 280 s per-gate cap inside the battery) straddles its cap on this
  host. Observed: base direct run timeout (2 of 6); base c2-pinkey honest world pass (3 of 6);
  candidate direct run timeout (2 of 6); candidate c2-pinkey honest world timeout (2 of 6).
  Mechanism check: `verifiers/floors-registry.json` (`instrument_total: 19`) registers neither
  `check_mutation_battery.py` nor `check_tip_battery.py`, so the floors gate never reruns the two
  edited instruments and the candidate cannot have lengthened it. The three carried reds
  (skill_checklist, corpus_integrity, corpus_independent) are red in every world at base and
  candidate alike; no guard and no carried verdict changed.
- No counter defect found: the frozen counter's header, mutant tables and anchors are consistent
  with the plan; both round-93 counters and the gate registry hold their base readings on the
  candidate.
- Census E11 during my first attempt was my harness artifact (see the census harness note), not a
  candidate defect; the correct invocation matches the scribe's receipt.

## Verdict

Scope PASS · No-harm PASS · Safety PASS on candidate
`86fe8bb4a6671d770e9d84fc6e47b113ddbd0e39` (= freeze `edc731a91a956f6df20c27a74fb981b286f6ba58` +
the four builder patches ExecBatterySelfTest / ExecTipSelfTest / ExecReceiptHeaders /
ScribeCorpusR94).

Receipts in this directory: `census-base.txt`, `c2-pinkey-base.txt`, `tipbattery-base-direct.txt`,
`gatereg-cand.txt`, `floors-cand.txt`, `census-cand2.txt`, `c1killpin-cand.txt`,
`c2pinkey-cand.txt`, `tipbattery-cand.txt`, `candidate-full.diff`. Scratch
`/fast/scratch/hyaku/kotoba-r94/SentinelScopeR94/` removed before yielding.
No tools installed (none needed); pacman untouched; no kernel/host setting changed.
