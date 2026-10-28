# Kb81E14PinAudit — freeze-set pin audit (executor, leaf)

Base `b284223105f4d106f7e8f56ed4fd296c643cda0e`. Recompute-only seat: no lane edit, no commit.
Every number below is recomputed by me from the lane's committed bytes or from reviewed patch bytes
under `.ufo/waves/round-81/build/`; the harness that produced them is committed beside this receipt as
`Kb81E14PinAudit-recompute.py` and its base-mode output is `Kb81E14PinAudit-base.txt`.

Harness invocation (scratch clone at the r81 base, `--repo` names the clone, every git call uses `-C`):

```
S=/fast/scratch/hyaku/kotoba-r81/Kb81E14PinAudit
python3 -B .ufo/waves/round-81/build/Kb81E14PinAudit-recompute.py --repo "$S/clone" --no-patch-apply
```

## 1. The counter's own bytes at the base

| quantity | measured value | command |
|---|---|---|
| `verifiers/check_tip_battery.py` worktree sha256 | `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a` | `sha256sum verifiers/check_tip_battery.py` |
| same file as the base **blob** | `a356e9d101f3021687a80e73fca284e7436976d2` | `git rev-parse b2842231:verifiers/check_tip_battery.py` |
| size | 36343 B / 743 lines | `git cat-file -s a356e9d1` |
| worktree == base blob | yes (`git cat-file blob a356e9d1 \| diff - verifiers/check_tip_battery.py` → empty) | |
| sha256 of the blob's bytes | `e33b17d7…bc4a` (identical to the worktree value) | `git cat-file blob a356e9d1 \| sha256sum` |

Lane state at measurement: `git rev-parse HEAD` = the base, `git status --porcelain` = the three
untracked r81 items only (`.ufo/wapes`, `.ufo/waves/round-81/`, `plans/round-81.md`), i.e. no
worktree edit hides under these bytes.

## 2. The six instruments at the base vs `INSTRUMENT_PINS`

`git rev-parse b2842231:<path>` for each (BLOB ids, not `hash-object` of a worktree):

| instrument | base blob | allowed tuple (base counter) | base blob in tuple |
|---|---|---|---|
| `verifiers/check_gate_registry.py` | `95ffed389f483c3d6f93db3c08dcfdb9a2240576` | `95ffed38…` | **PASS** |
| `verifiers/check_assertion_floors.py` | `9cb860bda21ef8d24fcb0603aa85372b96f3ac41` | `780f6fe5…`, `50348420…`, `9cb860bd…` | **PASS** |
| `verifiers/verify_skill_checklist.py` | `6aab16849bd6d71ded8f3bcb3f95668f14f6a78f` | `8d44c063…`, `6aab1684…` | **PASS** |
| `verifiers/verify_corpus_integrity.py` | `e470eaaea5ef11c582b8353c9344ddf730c1a57a` | `71cb2730…`, `e470eaae…` | **PASS** |
| `verifiers/verify_corpus_independent.py` | `edac0df79324ba62ee25ff10a6a4d422ef59da61` | `176abae3…`, `edac0df7…` | **PASS** |
| `verifiers/check_correction_sweep.py` | `c94b771fa7d798ef45fc3bb640422ee7910f81a6` | `c94b771f…` | **PASS** |

Structural facts (same harness run):
- `INSTRUMENT_PINS` has **6 rows**, `BATTERY` has **6 rows**, and the two path sets are **equal**
  (no instrument run by the battery is unpinned; no pin row names a script the battery does not run).
- All **11 distinct** pin blob ids (12 tuple entries, `e470eaae`/`edac0df7` style duplicates are not
  present — the 6 rows carry 1+3+2+2+2+1 = 11 members) exist in the lane object database
  (`git cat-file -e <sha>` exit 0 for every one): no phantom/abbreviated pins. A 12-character pin
  is separately rejected by the counter's own self-test arm (`abbreviated pin does not match`).

## 3. Cap arithmetic — measured, not assumed

Source of truth: the guard diffs the six instruments from the pinned round-73 base
`072048fa8e8a52c707d25f7079772fa317244eb7` (not from the r81 base), so the "existing spend" is a
real diff, not a plan figure:

```
git diff --numstat 072048fa8e8a52c707d25f7079772fa317244eb7 b284223105f4d106f7e8f56ed4fd296c643cda0e \
  -- <the six instruments>
22  3  verifiers/check_assertion_floors.py        (only row; five instruments unchanged)
```

- pre-existing spend: **+22 / −3** (the round-76 D4 floors-guard bump).
- The base battery receipt `.ufo/waves/round-81/receipts/tipbattery-base-dot.txt` prints
  `instruments added 22 / deleted 3 lines (cap 40)` — my independent numstat reproduces it exactly.
- Headroom under E6's `LINE_CAP = 140`: **+118 added / −137 deleted** before either bound can trip.
  The plan's literal kill-rule phrasing ("40 base-spent + measured added ≤ 140") assumes a 40-line
  base spend that is **not** the measured value; see the arithmetic finding in §6.

## 4. Method calibration against the published r80 receipt

`Kb80E06CounterErratum`'s freeze receipt (`.ufo/waves/round-80/receipts/freeze-shas.txt`) publishes
two composed instrument blobs and a 38/5 patch arithmetic. Applying `Kb80E04DeadPointer.patch` then
`Kb80E05GrammarFix.patch` to the r81 base in my clone reproduces **both** values exactly:

```
git -C "$C" hash-object verifiers/verify_corpus_integrity.py   -> 68ccce1c152c915e16893a5157c9d5878df779fb
git -C "$C" hash-object verifiers/verify_corpus_independent.py -> e887de71892ecfc6be5b3f47e362ce8a766c5c89
numstat: 17/0 + 11/2 (integrity), 10/3 (independent)  = 38 added / 5 deleted
```

So the harness's `hash-object` and `apply --numstat` pipeline agrees with an independently published
round-80 receipt; the r81 pins can be judged with the same instrument. The r80 stack also still
applies cleanly to the r81 base (`git apply --check` exit 0 for E04 and E05), i.e. the superseded
blobs `68ccce1c…`/`e887de71…` are *reachable* but must **not** be the r81 pins: the plan supersedes
the marker-based external class with a verified binding, so the strengthened patches must compose to
different blobs. A r81 pin equal to either r80 value is a finding (§6).

## 5. The reviewed r81 instrument patches — measured, and the cap arithmetic

Observed at 2026-10-27T02:36–02:37Z (`Kb81E14PinAudit-obs-023652.txt`, plus the run overwritten into
`Kb81E14PinAudit-instruments.txt`). Both patches apply to `b2842231` with `git apply` exit 0.

| patch | sha256 | numstat |
|---|---|---|
| `Kb81E01Integrity.patch` | `5571c6d2f0295496e023d280c1b58219d6a1c5fcbd8ef7966dcdbe0a78b8b387` | `verifiers/verify_corpus_integrity.py` **+203 / −10**; `verifiers/external-commits.json` +11 (new file, not a battery instrument) |
| `Kb81E02Independent.patch` | `b4cfa37b53fd877463b2e80e0d08b5698416cbac49836c912110714b6a084066` | `verifiers/verify_corpus_independent.py` **+247 / −18** |

Post-image instrument blobs (the values E6's two pin additions must carry **for these exact bytes**):

```
git -C "$S/clone" hash-object verifiers/verify_corpus_integrity.py    -> 1e5588cf97913e8332b3231e661a6862d31dddab
git -C "$S/clone" hash-object verifiers/verify_corpus_independent.py  -> 7b37461aa85f6193d77a23aa4a177155e2b3994a
```

Neither equals the r80 composition (`68ccce1c…`, `e887de71…`, reproduced in §4), so the pins do bind
the **r81** design (the post-image contains `REPORT_MARKER, REPORT_MIN_BYTES = b"## SHONEN", 400` and
`EXTERNAL_MANIFEST = "verifiers/external-commits.json"`), not the superseded marker grammar.

**Cap arithmetic (measured on a committed scratch tip, not derived from the plan's estimate).**
Applying both patches to the base, committing (`efeea649` in the clone), then the guard's own diff:

```
git diff --numstat 072048fa8e8a52c707d25f7079772fa317244eb7 HEAD -- <six battery scripts>
  vs r81 base:  203/10  integrity, 247/18  independent           = +450 / -28
  vs r73 base:  +22/-3 pre-existing (floors) + the above         = +472 / -31
```

- `LINE_CAP` 140 (E6) → the instrument-size guard measures **472 added** and would report
  `instruments gain 472 lines > 140`: 333 lines over, 4 of 5 guards, exit 1 — C1's frozen
  `guards 5 of 5; tip battery exit 0: 6 of 6` is unreachable on these bytes. (Counter arithmetic
  read from `check_tip_battery.py:316-320`; I did not run the claim's after-value.)
- Plan-literal reading of the kill rule ("40 base-spent + measured added ≤ 140" → added ≤ 100):
  also exceeded, by 350 added lines.
- Measured reading (22 + added ≤ 140 → added ≤ 118): 332 added lines of headroom consumed too much.
- The deletion side (`-31`) is inside the 140 bound; only additions are over.
- The plan's own E6 justification pre-declares this outcome: *"the freeze receipt records the
  measured numstat of the reviewed blobs before data and the claim stops if it exceeds the declared
  bound"*, and the kill rule names the same clause.

**Stability hazard observed (evidence, not a judgment).** `Kb81E01Integrity.patch` was observed at
two distinct byte sets inside 90 s: 19670 B / `5571c6d2…` (02:34:5x, 02:36:40, 02:37) and
19782 B / `e88f3fc7b254c2cdde59e117307c6b4adae733fe9adfd2eea53f56a1b527ec4f` (02:36), whose
integrity post-image was `19ef9268b430327bdb9a33e754a8775647d10814`. A pin recorded against the
transient bytes would fail `instrument-pin` at the tip. The pin values above are valid only for
`5571c6d2…`; a revised patch requires a regenerated E6 pin **before** the freeze receipt and the
after-value run.

## 6. E6 counter patch — line-set adjudication and pin reconciliation

Published erratum `Kb81E05Erratum.patch` (sha256
`782501f6a947b3698ce8660115af18259d6ff8d372519e81daed54c1fd930e04`, 5707 B) applies to
`b2842231` with exit 0 and touches **only** `verifiers/check_tip_battery.py` (numstat +21 / −15).
Hunk set, read line by line against the plan's E6 items (a)–(d):

| erratum item | lines | verdict |
|---|---|---|
| (a) cap | `@-111` `LINE_CAP = 40` → `LINE_CAP = 140` | as declared |
| (b) pins | `@-136` integrity tuple +`1e5588cf…`; `@-139` independent tuple +`7b37461a…`; base blobs kept | membership only, rows not rewritten |
| (c) self-test constants | `range(41)`→`range(LINE_CAP + 1)`; `padding=60`→`padding=LINE_CAP + 1`; both expectation strings → `%d`/`LINE_CAP` | semantics preserved |
| (d) prose | docstring 42-44, r73 comment 107-108, E2 pin comment 121 / 125-127 | text only |
| anything else | none — no guard id, guard body, `BATTERY`, `BASE`, `TOTAL`, printed line or exit code is touched | **clean** |

My harness's mechanical allowlist flags 26 changed lines as unclassified; on inspection every one is
either prose (item d), a pin-tuple value line, or a continuation line of a `LINE_CAP` expression —
i.e. inside the declared set. **No guard logic changed.**

The amended counter's own `--self-test` is green on these bytes: `self-test: 0 failure(s) over 69
assertions`, exit 0 (same 69 assertions as the base). That is necessary but **not** sufficient:
the self-test sets `INSTRUMENT_PINS` locally, so it cannot see whether the table's new members match
the patches that will be committed. Only the reconciliation in §5 / §7 checks that, and only the
`instrument-pin` guard at the landed tip enforces it.

**Stale pin in the published erratum (finding).** The integrity pin the erratum adds —
`1e5588cf97913e8332b3231e661a6862d31dddab` — is the post-image of the *earlier* E01 bytes
(19670 B / `5571c6d2…`). The E01 patch as it stands now (20175 B / `6bbb304b…`, +210/−10) produces
`bbee51f2bae5b33b123a546150e83352d68eeebc`, so that tuple member does not admit the tip's bytes:
`instrument-pin` would report `… blob bbee51f2… is not a pinned blob` and the guards would read
4 of 5. The independent pin (`7b37461a…`) does match E02's bytes. This is not a criticism of the
design — it is the churn the L1 has already ruled on pre-freeze (caps and pins are being revised);
the audit consequence is that **a pin must be regenerated from the final patch bytes, and the freeze
receipt must record the pair (patch sha256, pinned blob) together.**

**Size arithmetic on the 140 variant.** Instrument additions are +457 (E01 210 + E02 247) over the
r81 base, +479 over the guard's r73 base, against `LINE_CAP` 140: `instrument-size` would fail by
339 added lines (4 of 5 guards, exit 1). The deletion side (−31) is inside the bound.

## 7. Reconciliation of the current stack (observation O6, 2026-10-27T02:41Z)

Patch bytes audited (`sha256sum` of each file, at the timestamps below; all apply to `b2842231`
with `git apply` exit 0 and no mode change):

| patch | size | sha256 | instrument numstat |
|---|---|---|---|
| `Kb81E01Integrity.patch` | 20175 B | `6bbb304bea83968ced6c2ba3f33afa26b7d4256334303ea99a32279079495fe7` | integrity **+210 / −10**; `external-commits.json` +11 (new) |
| `Kb81E02Independent.patch` | 15664 B | `d8bf88c8ef5daf99ddf861ab2a5aeaa1193a57a90200e1d314134750e2e7f9d1` | independent **+170 / −16** |
| `Kb81E05Erratum.patch` | 6037 B | `c66103f3770736652514e78ba7c8e0f5baac22fc565b61168626c44be9acf32c` | counter +24 / −16 (not an instrument) |

Post-image identities produced by those bytes:

| file | git blob | sha256 | lines |
|---|---|---|---|
| `verifiers/verify_corpus_integrity.py` | `bbee51f2bae5b33b123a546150e83352d68eeebc` | `a0b52d2419e28bf45bfcdf167dff5dfd44fdd7356cbc606eea1ea2ee8304b011` | 1670 |
| `verifiers/verify_corpus_independent.py` | `59602942075d8fe77061876fb52eb32a44313697` | `7efc431b5ec39e50ed38c242b520b60c606bbf3682cfb224a6af11feaf57554b` | 1307 |
| `verifiers/check_tip_battery.py` (amended) | `a0796d74a9db609d0c35f378d9c0281031cc0ad8` | `9d5aaa3f24f3c5a7be0174773085b2e31ede3a918f5927f1cd3b864bea9b7dcf` | 751 |
| `verifiers/external-commits.json` (new) | `402ac290baef66e19a4ac6bcc3b801e78ca5a035` | `326fab4c090eb4299afbf13efebe0cc2eef833dd020e7a27d64f9afb6a8633d8` | 11 |

Pin reconciliation on these bytes (harness §5/§6 output, `Kb81E14PinAudit-obs-0241*.txt`):

- integrity `bbee51f2…` **in tuple** (erratum pins it) — PASS
- independent `59602942…` **NOT in tuple**: the erratum still pins `7b37461a…`, the post-image of
  E02's *previous* 247/18 bytes — **FAIL / stale pin** (F2, F6)
- the other four instruments byte-identical to their base blobs — PASS
- cap arithmetic: instruments vs the guard's r73 base **+402 / −29** (floors 22/3 + E01 210/10 +
  E02 170/16) against `LINE_CAP` 900 → **fits**, 498 added / 871 deleted lines of headroom.
- amended counter `--self-test`: `0 failure(s) over 69 assertions`, exit 0.

Composed-set check (all reviewed r81 patches applied to the base in one clone:
E01, E02, E04Baseline, E05, S05, S09, S10): the six battery instruments end at exactly
`95ffed38 / 9cb860bd / 6aab1684 / bbee51f2 / 59602942 / c94b771f` — i.e. four base blobs and the two
r81 repair blobs, no third party writes an instrument, so the pin table's admitted set is sufficient
for the whole reviewed set (the single exception was the stale pin above).

Registry coupling (why C1's `6 of 6` also depends on the C2 files): `check_gate_registry.py`'s
universe is every `verifiers/*.py|*.sh` at the measured rev (`Tree.universe`), **63** at the base;
`check_sdk_allowed_tools.py` makes it 64, so a missing or non-conformant `SKILL.md` row for it turns
`check_gate_registry` red and the battery can read at most 5 of 6. `Kb81S09SkillRule-SKILL.patch`
adds that row (8 cells, `--self-test`, `in-file`, owner `kotoba`) and the counter implements
`--self-test`. `verifiers/external-commits.json` is `.json`, outside the universe — no row is needed
for it (8 JSON files exist under `verifiers/` at the base, none indexed as a verifier).

## 8. Findings

- **F1 (fixed by the pre-freeze revision).** At `LINE_CAP` 140 the reviewed repair blobs measured
  402–479 added lines over the guard's r73 base across the observed byte sets (472/473/479 before
  E02 slimmed, 402 on the current pair): `instrument-size` could not pass at 140 in any of them, so C1
  could not print `guards 5 of 5`. The L1's pre-freeze revision to 900 clears it with 498 lines of
  headroom on the current bytes.
- **F2 (open at O6, RESOLVED at O7).** `Kb81E05Erratum.patch` pinned `verify_corpus_independent.py` to `7b37461a…`;
  the current `Kb81E02Independent.patch` produces `59602942…`. With these bytes at the tip the
  `instrument-pin` guard fails and guards read 4 of 5. Repin required before freeze.
- **F3 (open at O6, RESOLVED at O7 — sidecars re-derived).** Erratum sidecars were stale and would corrupt a freeze receipt assembled from them:
  `Kb81E05Erratum.sha256` = `782501f6…` (actual patch `c66103f3…`); `Kb81E05Erratum.counter-sha256.txt`
  describes the 140-byte version (`patch 782501f6`, counter blob `4b14ffe1…`, sha256 `7afbd236…`);
  `Kb81E05Erratum.hunk-inventory.txt` says `LINE_CAP 40 -> 140` and "existing members are untouched";
  `Kb81E05Erratum.pin-provenance.txt` names E01 `5571c6d2…`/`1e5588cf…`. Correct current values are in
  §7 and in `Kb81E14PinAudit-obs-*.txt`.
- **F4 (minor, RESOLVED at O7).** The erratum's r73 comment said the repair blobs "measured 203 and
  247 added lines"; the republished comment names 210 (integrity) and 170 (independent), matching §10.
- **F5 (design change, authorized).** The revised tuples are *tight*: `(base blob, r81 blob)` for both
  corpus gates. The r72 draft members `71cb2730…` (integrity) and `176abae3…` (independent) leave the
  admitted set. Effect measured: base blobs remain admitted (the base run still reads `guards 5 of 5`),
  r81 blobs admitted, and no r81 control world needs a draft blob (W2/W3 patch only one gate, leaving
  the other at its base blob). Scope note: the r81 counter would now reject an r72-era intermediate
  blob for those two files — outside this round's measurements, stated so nobody rediscovers it as a
  regression.
- **F6 (process).** Patch churn inside ~12 minutes: E01 observed at `5571c6d2…` (19670 B),
  `e88f3fc7…` (19782 B, post-image `19ef9268…`) and `6bbb304b…` (20175 B); E05 at `782501f6…`
  (cap 140), `adb35625…` and `c66103f3…` (cap 900); E02 at `b4cfa37b…` (247/18) and `d8bf88c8…`
  (170/16). The freeze receipt must therefore record **(patch sha256, post-image blob)** as a pair
  taken atomically, and the counter's own self-test cannot catch a stale pair (it sets
  `INSTRUMENT_PINS` locally and passed on both the stale and the fresh erratum). This audit is the
  check that catches it.
- **F7 (integration hazard).** `Kb81E04Baseline.patch` and `Kb81S08ReadmeRows.patch` both edit
  `corpus/README.md` in the same region: S08 applies cleanly to the base (`git apply --check` exit 0)
  but fails after E04 (`patch failed: corpus/README.md:157`). The L1 must pick one README edit or
  hand-merge; no instrument or pin is involved.
- **F8 (verification that holds).** `verifiers/external-commits.json` binds the S230/S231 token to
  `mistralai/mistral-vibe` with `receipt_sha256 e75f057a8e8f8319df227a254a42526ed096c7d0dc5364307365729a08ae738f`,
  which equals the sha256 I compute for the committed
  `.ufo/waves/round-79/snapshots/S231.fetch.json` (tracked at the base). The binding is content-verified,
  not a marker.
- **F9 (freeze inputs outside the battery).** The new C2 counter is neither pinned by
  `INSTRUMENT_PINS` (six battery scripts only) nor measured by `instrument-size`; its identity rests on
  the freeze receipt and its registry row. Measured now: `build/check_sdk_allowed_tools.py`
  sha256 `8e15a1177ef89bcf6b3360769360e3d30075a8930c9dfe5d0c902a4f01f807c4` (1572 lines), entry
  `build/allowed-tools-sdk-round81.md` sha256 `fe57322c535b281a7c60ddf89f31812ebff26ec4739b8daa3b9b3a8d3eecb8be`,
  snapshot `.ufo/waves/round-81/snapshots/S249.md` sha256
  `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2` (28395 B) — equal to the plan's
  pin and to `S249.fetch.json`'s recorded digest. The snapshot is **not** in the base tree
  (`git cat-file -e b2842231:.ufo/waves/round-81/snapshots/S249.md` fails), so it lands with the wave.

## 9. Patch inventory observed (sha256, at the last observation)

```
5571c6d2… / e88f3fc7… / 6bbb304b…   Kb81E01Integrity.patch        (churn; final measured 6bbb304b…)
b4cfa37b… / d8bf88c8…               Kb81E02Independent.patch      (churn; final measured d8bf88c8…)
7b5781ca4  Kb81E04Baseline.patch                  +5 dispositions/wapes.txt, +1 corpus/README.md
fd5966683  Kb81E04Baseline.disposition-only.patch +5 dispositions/wapes.txt
782501f6… / adb35625… / c66103f3…   Kb81E05Erratum.patch         (churn; final measured c66103f3…)
6d0d571795341fb99bb2ce326e48a3c6f805857376e0b93d06b5d4848ecea2c0  Kb81S05SourcesEdits.patch
f6f4b3aeb37251fe4014e6b807e812605b780e0c7299dd71d6a43fa53b376ce0  Kb81S08ReadmeRows.patch
2b413beabbda1430e3cbce2cae230e231021d5d123bf40727c74b9e5f5664c03  Kb81S08ReadmeRows.stageA.patch
77649aeb5a2eddd2777dc4fc877de44fc895273cc6ad002df60a9bce0120999f  Kb81S09SkillRule-SKILL.patch
304fd286a864739908277ffa165ecdc341d60c5ed2c5d14e65b8c6d29a0d44d3  Kb81S10Province.patch
f53a503661ef3599f25599f5cebd79a8ec0aafec00a67db9374ac47d03e598d7  Kb81E12Census-derived-alternative.patch
```
(Full 64-hex values for the churned patches are in §7; the regex-churn rows above are the earlier
observations kept so the churn is auditable.)

## 10. Final reconciliation (O7, after the erratum repin) — the values a freeze receipt may cite

Republished erratum `Kb81E05Erratum.patch` sha256
`c15680f81d2684fc40ef7aeef21143f217ecf4e4fc62b9ea91a7bd5787cfcf4f` (6037 B, `+24 / −16` on the
counter only). Audit run: `Kb81E14PinAudit-final-*.txt`; command

```
python3 -B .ufo/waves/round-81/build/Kb81E14PinAudit-recompute.py --repo "$S/clone" \
  --patch .ufo/waves/round-81/build/Kb81E01Integrity.patch \
  --patch .ufo/waves/round-81/build/Kb81E02Independent.patch \
  --patch .ufo/waves/round-81/build/Kb81E05Erratum.patch
```

| item | value | check |
|---|---|---|
| E01 patch | `6bbb304bea83968ced6c2ba3f33afa26b7d4256334303ea99a32279079495fe7` (20175 B) | applies rc=0 |
| E02 patch | `d8bf88c8ef5daf99ddf861ab2a5aeaa1193a57a90200e1d314134750e2e7f9d1` (15664 B) | applies rc=0 |
| E05 patch | `c15680f81d2684fc40ef7aeef21143f217ecf4e4fc62b9ea91a7bd5787cfcf4f` (6037 B) | applies rc=0 |
| integrity post-image | blob `bbee51f2bae5b33b123a546150e83352d68eeebc`, sha256 `a0b52d24…04b011` | **in tuple** |
| independent post-image | blob `59602942075d8fe77061876fb52eb32a44313697`, sha256 `7efc431b…af57554b` | **in tuple** |
| amended counter | blob `eb00200ee6987a2fd95086915a333fe258aa6c82`, sha256 `1753b11c11c6f907be838cb28842e28d01e7935e19d5afb3a6b46afdac51d660`, 751 lines | matches the erratum's own receipt |
| `LINE_CAP` | 900 (base 40) | as revised pre-freeze |
| instrument arithmetic vs the guard's r73 base | **+402 / −29** (floors 22/3, integrity 210/10, independent 170/16) | fits 900: 498 added / 871 deleted headroom |
| pin rows vs `BATTERY` | 6 vs 6, equal sets; every post-image blob in its tuple | PASS |
| base blobs still admitted (guards at the base rev) | all six base blobs present in their tuples | PASS |
| amended counter `--self-test` | `0 failure(s) over 69 assertions`, exit 0 | PASS |
| counter diff line set | cap, two pin members (tight tuples), four derived self-test constants, prose | no guard id, body, `BATTERY`, `BASE`, printed line or exit code touched |

All six battery instruments on the composed reviewed set are `95ffed38 / 9cb860bd / 6aab1684 /
bbee51f2 / 59602942 / c94b771f` — four base blobs plus the two r81 repair blobs, i.e. exactly the
admitted set. Nothing else in the reviewed r81 patches writes an instrument.

Residual risks the L1 owns (unchanged by this audit): (i) any further E01/E02 revision invalidates the
pin again — repin and re-record before the freeze receipt; (ii) the E04/S08 `corpus/README.md` overlap
(F7) needs one edit chosen; (iii) the C2 counter's registry row must land with the counter (F7/§7), or
`check_gate_registry` reads red and the battery cannot reach 6 of 6.

Not measured by this seat: the claim after-values (`6 of 6`, `N of 1`) — by assignment nobody scores
them here; and the control worlds W0–W9, which belong to the controls/mutation seats.

Tooling record: no tool installed or upgraded; `pacman` never invoked. Scratch clone
`/fast/scratch/hyaku/kotoba-r81/Kb81E14PinAudit/` was used for every measurement and removed before
this report was finalised; every git mutation was confined to it (`git rev-parse --show-toplevel`
asserted equal to the clone before the first commit).

## 11. Addendum — the plan's revised E6 text vs the measured tuple (read after the wave's repins)

Measured on the plan file as it stands (sha256 `d6bd43ebfe7ba253898cba8df7cdcb1ceba2e5513485ac760e700b8ec6af701c`,
which is **not** the `4573a9ba…` another seat quoted minutes earlier — the plan itself is moving, so cite
it by value and time): `plans/round-81.md:15` now declares `LINE_CAP` 40→900 and the two corpus-gate
tuples as "TIGHT tuples `(<r72 base blob>, <reviewed r81 blob>)`"; `:26` declares the cap 900 bound with
my measured `+402/-29` (E01 +210/−10, E02 +170/−16) and reconciles the earlier `+472/-31` figure;
`:28` reads `base-spent + measured added > 900`.

One wording disagreement to fix before anyone else reads it: the tuple the erratum actually writes is
`(e470eaae…, bbee51f2…)` for integrity and `(edac0df7…, 59602942…)` for independent — i.e.
**(r81 base blob, r81 post-image)**. The r72-era drafts `71cb2730…` and `176abae3…` are the members that
leave the set. A reader taking "<r72 base blob>" literally would expect `71cb2730…` to remain admitted;
it does not, and at the r81 base the admitted blob is `e470eaae…` (verified: base blob of
`verifiers/verify_corpus_integrity.py` at `b2842231`). The erratum's own comment says "TIGHT (base blob,
reviewed r81 blob)", which is the accurate wording; the plan parenthetical should say the same.

E02 confirmed final bytes (patch `d8bf88c8…`, post-image `59602942…`, 170/16) and states no `.min`
variant exists — no additional E02 patch is expected, so the §10 pins are final for the wave unless
E01 or E05 change again.

VERDICT: Pins reconcile at O7 — all six instruments in their tuples, LINE_CAP 900 fits the measured +402/−29, amended counter self-test 0/69 — but the freeze receipt MUST cite the (patch sha256, post-image blob) pairs in §10, not the stale 140-era sidecars seen at O6.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E14PinAudit.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-recompute.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-obs-023649.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-obs-023742.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-obs-023822.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-obs-023932.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-obs-024022.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-instruments.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-final-024145.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-cap900-selftest.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E14PinAudit-cap900-probe.diff
