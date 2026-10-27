# Kb79E02LogCitation — C1 repair 2 of 4: the checklist/floors red

Item: round 79 w1, C1 consistency (calibration sub-axis). Leaf seat; no subagents, no background
jobs. Scratch tree removed at the end of the wave (see §9).

## 1. The red I was sent to repair, reproduced

Base of this seat: lane tip `daa3a09` (plan F1 `2c56622` + w1 dispatch freeze; the delta from
`2c56622` is `plans/round-79.md`, `w1-spec.json`, `w1-dispatch.json`, `build-w1-spec.py` — no
verifier, no LOG.md line). At `daa3a09`, from a fleet-shaped scratch clone:

    $ python3 -B verifiers/verify_skill_checklist.py            # rc=1, one FAIL
    FAIL governance.citation_resolves: evaluated 1312 — LOG.md:2818:
      '.ufo/reports/round-76/kotoba.md' does not resolve from <clone>;
      10 quoted meta-finding(s), 3 schematic token(s) excluded,
      2 recorded absence(s) excused, 4 recorded correction(s) excused

`LOG.md:2818` is `- **Pointer:** … fleet report \`.ufo/reports/round-76/kotoba.md\`.` — the round-76
report is a **fleet** artefact (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotoba.md`,
8,128 B, sha256 `a025051d389368ea3a1078b7a64d3847c1e6ff25328fc1645a7be34f30e3f78f`) and the cited
address is lane-relative, so it misses. One cause, two red gates: `check_assertion_floors.py`
fails because `verify_skill_checklist.py`'s **live** self-test arm re-reds on the same subject
(`self_test_failures=1`), not because a floor moved.

Receipt: `build/Kb79E02-base-checklist.txt`; the counter agrees at the same rev
(`build/Kb79E02-base-daa3a09-tipbattery.txt`: `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1).

**Measured tree ↔ current lane tip.** The lane's history was rewritten while this wave ran, so the
commit objects my receipts name (`daa3a09`, `b51f5f7`, `cd520ab`) live only in the removed scratch
clone. The *content* they measured is carried unchanged by the lane tip at report time
(`c469863`): `LOG.md` blob `4cbd144f07add1621ecdee241e51ae0d73d8e7c2` (2,825 lines; line 2818
sha256 `04425e95…877bb`, still the bare token), `verifiers/verify_skill_checklist.py` blob
`6aab16848…`, `verifiers/check_assertion_floors.py` blob `9cb860bd…`,
`verifiers/floors-registry.json` blob `005ffdb1…`, and `verifiers/check_tip_battery.py` sha256
`e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a` — the frozen C1 counter, with
the `INSTRUMENT_PINS` table of §2. Measured at that tip:
`git -C <lane> apply --check --binary build/Kb79E02LogCitation.patch` → rc=0, and
`.ufo/reports/round-76/kotoba.md` is absent from the lane tree. The two worlds differ by exactly
this one path.

## 2. The mechanism I was sent to use is unreachable under C1's frozen guards

I built the prescribed repair in full, in a second world (`row` = `cd520ab`):

- appended notice `LOG.md:2830` (append-only; the cited line is untouched), byte-pinned
  sha256 `8a6c9248…ba45`;
- one `GOVERNANCE_CORRECTIONS` row `(2830, <pin>, "LOG.md", 2818,
  ".ufo/reports/round-76/kotoba.md", "../.ufo/reports/round-76/kotoba.md")` + horizon `2723 → 2830`;
- the live self-test arm moved to five excused corrections, plus the Q05/Q18 fault arm
  ("LOG.md:2818 correction is load-bearing": drop the row, or lower the horizon to 2829, and the
  live check re-reds) — self-test `0 failure(s) over 1864 assertions`, rc=0;
- floors bumped in step: `check_assertion_floors.py` (both in-file tables + docstring) and
  `verifiers/floors-registry.json`, `checklist 1863 → 1864`.

It **greens the gate**: checklist rc=0 (`build/Kb79E02-row-checklist.txt`). But the frozen C1
counter rejects the world:

    FAIL guard instrument-size: instruments gain 56 lines > 40
    FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob 862c924e… is not a pinned blob
    FAIL guard instrument-pin: verifiers/verify_skill_checklist.py blob 6864134b… is not a pinned blob
    fleet root …; guards 3 of 5; tip battery exit 0: 3 of 6

(`build/Kb79E02-row-tipbattery.txt`, `build/Kb79E02-row-guards.txt`.) Three findings for the L1:

1. `check_tip_battery.py:INSTRUMENT_PINS` admits only **exact blobs** — for
   `verify_skill_checklist.py` `8d44c063…` or `6aab1684…`, for `check_assertion_floors.py` one of
   three `9cb860bd…`-era blobs. At base each of the six scripts *is* one of its pins
   (`git rev-parse b10bcbc6:verifiers/…` verified). **The round's effective instrument budget is
   zero bytes, not 40 lines**: the correction-row mechanism lives inside a pinned file, and the
   "bump the floors registry in step" step edits a second pinned file.
2. The size cap is summed over the six instruments *from the counter's own BASE `072048fa`*, and
   22 of the 40 lines were already spent before this round (`instruments added 22 / deleted 3` in
   the base receipt). The seat-spec-sized draft added 34 → 56.
3. Q64's correction-row form therefore needs a guard edit. The plan's C1 kill rule reads
   "a repair needs a guard to be edited → C1 stops as an honest stop". **That branch is not taken
   by the repair below**, which edits no guard; it is taken by the correction-row branch, which is
   why the row draft is delivered as evidence and *not* as the integration patch.

## 3. The repair delivered: the cited artefact's own address, inside the lane

`build/Kb79E02LogCitation.patch` adds exactly one path (1 insertion, no other change):

    .ufo/reports/round-76/kotoba.md      mode 120000, blob bf7c7e0c0c39a57c49224c87348afc74dca14db4
    readlink -> ../../../../.ufo/reports/round-76/kotoba.md
    resolves -> /home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotoba.md
    sha256   -> a025051d389368ea3a1078b7a64d3847c1e6ff25328fc1645a7be34f30e3f78f   (= the fleet file)

A relative symlink, four hops from `.ufo/reports/round-76/` to the fleet root, is the address of
**the same artefact**: one artefact, one set of bytes, no copy, no paraphrase, no record of a
removal (the Q64 prohibition), no widened regex, no double-quote exclusion, and `LOG.md:2818` is
not edited. The governance predicate is an existence test over the tree, so the record's claim
becomes true as written: a reader at the lane root who follows `.ufo/reports/round-76/kotoba.md`
lands on the round-76 report.

Measured on the same clone and the same fleet root (`--fleet /home/vgpnk/Projects/shokunin`):

| world | counter | guards | checklist | floors | corpus_integrity | corpus_independent |
|---|---|---|---|---|---|---|
| `daa3a09` (no repair) | 1 of 6 | 5 of 5 | rc 1 | rc 1 | rc 1 (5 DRIFT) | rc 1 (unindexed 6) |
| `b51f5f7` (+ patch) | **3 of 6** | 5 of 5 | **rc 0** | **rc 0** | rc 1, identical | rc 1, identical |
| `cd520ab` (row draft) | 3 of 6 | **3 of 5** | rc 0 | rc 0 | rc 1, identical | rc 1, identical |

- `build/Kb79E02-sym-tipbattery.txt`: `gate verifiers/check_assertion_floors.py exit 0`,
  `gate verifiers/verify_skill_checklist.py exit 0`, `guards 5 of 5`, exit 1 only because the
  battery is 3 of 6 (the three remaining reds are other seats' items and are unchanged, §4).
- `build/Kb79E02-sym-floors.txt`: `PASS checklist observed=1863 floor=1863` … rc=0, wall 114.6 s;
  `build/Kb79E02-sym-checklist.txt` / `.json`: rc=0, `PASS governance.citation_resolves: evaluated
  1312 — 1312 governance citation token(s) resolve across 2 files; … 2 recorded absence(s)
  excused, 4 recorded correction(s) excused` — the exact counts the live self-test arm asserts,
  which is why the floors gate goes green without touching a floor.
- `build/Kb79E02-sym-checklist.rc` captures the command's own status (`cmd > out 2>&1; rc=$?`).

`git apply --check --binary` on a clean `daa3a09` tree: rc=0; after applying, the link resolves and
`sha256sum` prints `a025051d…`. Receipt: this report and `build/Kb79E02-sym-lstree.txt`.

## 4. No new red (Q05/Q18) and the controls

- **The repair is what greens the gate** (fault control): the identical tree without the link
  (`daa3a09`) re-reds with the same single `FAIL governance.citation_resolves … LOG.md:2818`. No
  other line moved.
- **No collateral change**: `verify_corpus_integrity.py --json` observations are *identical*
  (`build/Kb79E02-base-integrity.json` vs `-sym-integrity.json`: `unindexed 6`, `report_total 106`,
  `report_dead 1`, `tracked_files 150`, all five DRIFTs the same); `verify_corpus_independent.py`
  output is byte-identical except its `HEAD` line (`dead=0`, `nonhash=0`, `unresolvable=0`);
  `check_correction_sweep.py --root .` exits 0 in both (`0 stale block(s)`);
  `check_gate_registry.py --rev HEAD` reads `60 of 62` in both (that red is the registry seat's).
- **The three remaining reds are not mine and are unchanged**: `check_gate_registry.py` (60 of 62),
  `verify_corpus_integrity.py`, `verify_corpus_independent.py` (`corpus.index.unindexed=6`).
- **Row world's usefulness**: it proves the correction row *is* load-bearing (its fault arm passes
  at 1864 assertions) — i.e. the row draft is correct; it is the counter's pin guard that rejects
  the route, not the row.

## 5. Why not a byte copy at the same path

A regular file copy (`mode 100644`, as the lane's 25 historical `.ufo/reports/round-20..45/kotoba.md`
are) would also green the predicate, and it would survive a standalone clone. Rejected because it
creates a **second address for one artefact** with no mechanism keeping it equal to the fleet
original, whereas the lane's live convention for fleet reports is citation by `../` (10 such tokens
in `LOG.md`, 18 in `SCORECARD.md`); the symlink has one address, one byte-stream, and fails closed
(dangling → red) if the fleet tree is ever absent — the same property the `../` citations have.
If the L1 prefers the copy, the receipt must pin `a025051d…` and the same three gates are measured
the same way.

## 6. Declared limits (what this repair does not prove)

- **Existence ≠ identity**: the gate tests existence, so a link to a *wrong* file would also pass.
  The sha256 equality in §3 (and the fleet file's size) is the identity evidence the gate does not
  give; keep it in the round's receipt set.
- **Dangling outside the fleet**: a clone of the lane with no fleet parent resolves the link to
  nothing. That is the same declared limit as every `../` citation in `LOG.md`/`SCORECARD.md`;
  `check_tip_battery.py`'s own sandbox is fleet-shaped for exactly this reason.
- **Depth assumption**: the target has four `..` hops, correct while the lane sits one level under
  the fleet root (today: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`).
- **Landmine for the record text**: `citation_resolve` allows at most **3** leading `..` hops, so
  the string `../../../../.ufo/reports/round-76/kotoba.md` must never be written *backticked* in
  `LOG.md`, `SCORECARD.md` or `SKILL.md` — it would be a fresh red. Cite the link as
  `` `.ufo/reports/round-76/kotoba.md` `` (resolves) and describe the target in prose.
- **The instrument inconsistency stays**: the corpus verifier resolves a bare `.ufo/reports/…`
  token against the fleet root, the governance verifier does not
  (`verify_skill_checklist.py:citation_resolve` is lane-relative only, and the `../` form it does
  accept is capped at 3 hops). Aligning the two is a one-line predicate change — inside a pinned
  blob, so it is a post-freeze erratum for a future round, not this wave.
- **Not measured here**: `check_report_pointers.py` (needs the round report), the census, `wc -l
  SKILL.md` — outside this item and untouched by a `.ufo/` addition.

## 7. What the L1 should do

1. Integrate `build/Kb79E02LogCitation.patch` as the C1 repair commit (it applies cleanly to
   `daa3a09`, and to any later tip that does not already carry the path).
2. Do **not** integrate `build/Kb79E02LogCitation-correction-row-DRAFT.patch` while C1's counter is
   frozen: it reads `guards 3 of 5` (two pin failures, size 56 > 40). If a future round unfreezes
   the counter and pins a reviewed blob, the row draft is the canonical Q64 form and supersedes the
   symlink; the two are not meant to land together.
3. In the round-79 `LOG.md` entry, record the repair append-only, e.g.:
   "LOG.md:2818 cites the round-76 fleet report in bare form; the lane now carries that address as a
   relative symlink to the fleet artefact (`.ufo/reports/round-76/kotoba.md`, sha256
   `a025051d389368ea3a1078b7a64d3847c1e6ff25328fc1645a7be34f30e3f78f`, 8,128 B), so
   `governance.citation_resolves` reads 1312 of 1312 at this tip. The Q64 correction-row form is
   unreachable under the frozen `instrument-pin` guard; its reviewed draft is
   `.ufo/waves/round-79/build/Kb79E02LogCitation-correction-row-DRAFT.patch`."
   Any *new* citation of a fleet report must use the `../` form
   (`../.ufo/reports/round-79/kotoba.md`), never the bare `.ufo/` form, or the same red recurs on a
   new line — and that token resolves only once the fleet file exists, so append the entry after the
   report lands (or name the report unbackticked).
4. Re-run the C1 counter at the final tip (both `--repo .` and absolute forms) and paste the
   receipt: with the other three seats' repairs in, the six gates are what the claim measures.

## 8. Tooling

No installs or upgrades were needed; no `pacman`, no host service changes. Only `git`, `python3`
and coreutils, all existing. Disk guard read once before the heavy pass
(`/home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh status`: `/fast/scratch/hyaku` 27 %,
591.9 G free).

## 9. Scratch

`/fast/scratch/hyaku/kotoba-r79/Kb79E02LogCitation/` (clone at `kotoba-shokunin`, three branches
`base`-by-commit/`sym`/`row`, the fleet-shim symlinks, `tmp/`) — removed before yielding; every
receipt quoted above is already in `build/`. No lane file outside
`.ufo/waves/round-79/{build,w1}/` was written; no commit, checkout or index operation in the lane.

VERDICT: the prescribed correction-row repair is correct but unmeasurable under C1's frozen counter (instrument-pin rejects both edited instruments, size 56>40); the delivered one-path symlink — the cited fleet artefact's own lane-root address — takes the battery from 1 of 6 to 3 of 6 with guards 5 of 5, checklist rc 0 and floors rc 0 (114.6 s), and changes no other gate.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E02LogCitation.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E02LogCitation-correction-row-DRAFT.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79E02-receipts.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79E02LogCitation.md
