# ExecRepinControls — C2 shortcut-control worlds (round 72, wave 1)

**Verdict.** The four worlds the frozen plan names in § C2 are built as replayable overlay
bundles and were replayed here; each reads **below** the frozen target on the conjunct it was
built to attack. The **headline counter-design finding**: the composite world
`w3b-stub-full-ledger` (a 358-byte text stub at the pinned opencode path, its sha pinned, plus a
ledger naming all nine base opencode classes) satisfies `pins OK 3/3` **and** the ledger conjunct
**exactly**, and fails only `surfaces pass p of 7`. The plan permits that surface target to be
lowered before data (Q45: "the target stays `p == 7` only if that census reaches 7"; dropped: the
clause naming the census seat, 9 words). If it is lowered to 5 or less, **a shortcut world reads
exit 0** — so the counter needs a substrate-identity conjunct that neither existing instrument
supplies, before any data is scored.

Base: `c69711ee08279609374d895bb0f3c8c18ccf15c9`. Lane HEAD while working:
`e61fd294c2e1cdd16d594b57b310254183ace1e7` (no committed lane file edited by this seat:
`git status --porcelain` shows only untracked `.ufo/waves/round-72/…` paths).

## Deliverables (all under `.ufo/waves/round-72/w1/build/ExecRepinControls/`)

| path | contents |
|---|---|
| `README.md` | index, cross-world table, the headline finding, counter-run recipe, probe, caveats |
| `w1-repin-only/` | overlay (3 files) + `world.patch` (43 lines) + `replay.sh` + `replay.out` + `observed-pins.json` + `observed-surfaces.json` + `README.md` |
| `w2-ledger-all/` | w1 + `verifiers/census-removals.json` (9 rows) + patch (119 lines) + the same five artefacts |
| `w3-stub-pinned/` | w1 + `verifiers/fixtures/opencode-stub.bin` (358 B) + pinned stub sha + patch (55 lines) + the same five artefacts |
| `w3b-stub-full-ledger/` | added composite: w3 + w2's ledger + patch (131 lines) + the same five artefacts |
| `w4-omp-mtime-stale/` | w1 + `omp_binary_mtime` at the round-47 stamp + patch (48 lines) + the same five artefacts |
| `ledger-probe.py` | standalone probe of **only** the ledger conjunct (not the counter) |
| `base-do-nothing/` | the do-nothing control re-run at the base, default paths **and** flag-overridden |

Every `world.patch` was verified with `git apply --check` against a fresh clone of the base
(`w1-repin-only: patch applies clean (43 lines)` … `w4-omp-mtime-stale: patch applies clean (48
lines)`); every `replay.sh` builds a fleet-shaped `/tmp` parent (38 symlinks of
`/home/vgpnk/Projects/shokunin/*` minus the lane), `git clone --shared` of the lane named
`kotoba-shokunin`, `checkout --detach` the base, asserts
`git -C $C rev-parse --show-toplevel == $C`, commits the overlay **inside that clone only**, then
runs both instruments at their own default paths with no flags.

## What each world changes, and what it measures

| world | change vs base | pins | surfaces | ledger conjunct |
|---|---|---|---|---|
| w1-repin-only | `opencode_binary_sha256` → `ca9b3ee2…`; both default path constants → `~/.local/bin/omp.real`, `~/.opencode/bin/opencode`. Census + `surfaces-baseline.json` + every OC rule byte-identical. | **3/3 exit 0** | **5/7 exit 1** | n/a |
| w2-ledger-all | w1 + `verifiers/census-removals.json` naming all 9 opencode classes | 3/3 exit 0 | 5/7 exit 1 | **FAILS** (9 vs 1) |
| w3-stub-pinned | w1, but the pinned opencode path is a 358-byte stub in the clone; its sha pinned | **3/3 exit 0** | 5/7 exit 1 | n/a |
| w3b-stub-full-ledger | w3 + w2's ledger | **3/3 exit 0** | 5/7 exit 1 | **HOLDS** (9 == 9) |
| w4-omp-mtime-stale | w1 + `omp_binary_mtime` → `2026-10-21T03:30:38.135013187-03:00` | **2/3 exit 1** (mtime DRIFT) | 5/7 exit 1 | n/a |

Plan-item quotes (each copied from `plans/round-72.md` § C2, ≤25 words, nothing dropped):
"a re-pin that edits only the baseline shas and paths and leaves rules OC-1…OC-6 unchanged (must
read `p < 7`)" (20 words); "a world that ledgers every opencode class (must fail the exact-set
conjunct)" (13); "a stub file at the pinned opencode path whose sha is pinned (must fail extraction
vacuity)" (17); "a world that pins `omp.real` but leaves `omp_binary_mtime` at the old value" (14).

## Evidence — exact commands and observed output

### 0. Do-nothing control at the base (re-run by me, not read from the receipt)

Fleet-shaped sandbox, clone at `c69711e`, run from the clone root, no flags:

```
$ python3 -B verifiers/check_substrate_pins.py --json ; echo exit=$?
{"pass":0,"fail":3,"exit_code":2}      exit=2     # DRIFT omp sha, DRIFT omp mtime, UNREADABLE opencode
$ python3 -B verifiers/verify_surfaces.py --json ; echo exit=$?
{"checks":[],"error":"opencode binary not found: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe","exit_code":2,"fail":0,"pass":0}   exit=2
```

With the substrate named explicitly (`--omp-binary ~/.local/bin/omp.real --opencode-binary
~/.opencode/bin/opencode`), the same base reads `{"pass":2,"fail":1,"exit_code":1}` (pins) and
`{"pass":5,"fail":2,"exit_code":1}` (surfaces). Retained in `base-do-nothing/`.

### 1. Replays (each `replay.out` is the shipped script's own stdout)

```
w1-repin-only:          world commit b6c2e11b6218c5a7909cb2f676966fd82b2cdc2c
                        check_substrate_pins.py exit=0 / verify_surfaces.py exit=1
w2-ledger-all:          world commit 5597aa2d575945ac296d504a13b88d34d96b4f7a
                        check_substrate_pins.py exit=0 / verify_surfaces.py exit=1
w3-stub-pinned:         world commit 5a2621a6b2792d216341b5eb55090bc4d103d6f3
                        check_substrate_pins.py exit=0 / verify_surfaces.py exit=1
w3b-stub-full-ledger:   world commit b04a34b94a9bd10c2fe88053fbe876a3d87677ec
                        check_substrate_pins.py exit=0 / verify_surfaces.py exit=1
w4-omp-mtime-stale:     world commit 1e997d59403ec8b61fe1b1dc2e51c8ca8612f688
                        check_substrate_pins.py exit=1 / verify_surfaces.py exit=1
(each also prints: check_substrate_repin_v2.py absent in the lane; counter not run)
```

`ls verifiers/check_substrate_repin_v2.py verifiers/census-removals.json` at the lane:
`No such file or directory` for both — the counter does not exist yet, so no world was scored
against it here; the ledger conjunct is measured with the probe instead (below).

```
$ for w in …; do printf '%s pins=%s/%s exit=%s surfaces=%s/%s exit=%s\n' …; done
w1-repin-only          pins=3/3 exit=0  surfaces=5/7 exit=1
w2-ledger-all          pins=3/3 exit=0  surfaces=5/7 exit=1
w3-stub-pinned         pins=3/3 exit=0  surfaces=5/7 exit=1
w3b-stub-full-ledger   pins=3/3 exit=0  surfaces=5/7 exit=1
w4-omp-mtime-stale     pins=2/3 exit=1  surfaces=5/7 exit=1
```

Pin row counts are exactly 3 in all five worlds (`.pass + .fail` = 3), so the counter's
"exactly 3 rows" guard is not tripped by any world; no key shaped `opencode_binary_<word>` was
added anywhere.

Per-check verdicts, w1 (the shape all five share on the surface side):

```
surfaces.literal_present     FAIL   1 loader literal not verifiable: opencode:instructions/CONTEXT.md
surfaces.no_uncovered_class  PASS   all 8 extracted loader classes declared
surfaces.opencode_extract    FAIL   vacuity: 0 class(es) from 7 rule(s); 9 declared produced by no rule
surfaces.table_parity        PASS   42 ids
surfaces.literal_parity      PASS   42 literals
surfaces.kind_parity         PASS   42 kinds
surfaces.excluded_reason     PASS   8 excluded entries
```

w4's failing pin, verbatim from `observed-pins.json`:
`"pin":"omp_binary_mtime","verdict":"DRIFT","expect":"2026-10-21T03:30:38.135013187-03:00",
"observed":"1792625844615549837","delta_ns":173397942086864,"tolerance_ns":0`.

### 2. The ledger conjunct (`ledger-probe.py`, not the counter)

```
$ python3 -B ledger-probe.py --dump /tmp/k72-oc-strings.txt --ledger w2-ledger-all/overlay/verifiers/census-removals.json
base opencode classes 9; ledgered 9; required 1
  opencode:instructions/CONTEXT.md   literal CONTEXT.md  count 0  absent
  (8 more, all "present": AGENTS.md 15, CLAUDE.md 3, instructions 281, https:// 1282, <system-reminder> 15)
FAIL ledgered but literal present: opencode:claude-home/CLAUDE.md, opencode:config/AGENTS.md,
  opencode:config/instructions, opencode:config/instructions-remote,
  opencode:instruction-context/AGENTS.md, opencode:instructions/AGENTS.md,
  opencode:instructions/CLAUDE.md, opencode:read-hook/instructions
ledger conjunct FAILS        exit=1

$ strings -n 4 w3-stub-pinned/overlay/verifiers/fixtures/opencode-stub.bin > /tmp/stub-strings.txt
  sha256 80bb558fc717ff9df2837e0f26916852ce5df75740682681db2967ea6b192aac   (== the stub's own sha)
$ python3 -B ledger-probe.py --dump /tmp/stub-strings.txt --ledger w2-ledger-all/overlay/verifiers/census-removals.json
base opencode classes 9; ledgered 9; required 9
  (all nine literals count 0, absent)
ledger conjunct HOLDS        exit=0

$ python3 -B ledger-probe.py --dump /tmp/k72-oc-strings.txt --ledger <one-row ledger: CONTEXT.md only>
base opencode classes 9; ledgered 1; required 1
ledger conjunct HOLDS        exit=0
```

So: the wholesale ledger **fails** on the live dump and **holds** on the stub's dump; the honest
minimal ledger (one row) holds on the live dump. The live dump `/tmp/k72-oc-strings.txt`
(sha256 `020fb253…`) counts `CONTEXT.md` 0, `AGENTS.md` 15, `CLAUDE.md` 3, `instructions` 281,
`https://` 1282, `<system-reminder>` 15 (substring counts; `grep -c -F` line counts 0/13/3/145/827/14
agree on presence/absence).

## Findings

**F1 (headline, counter-design).** A 358-byte text stub plus a wholesale ledger is one surface
count away from passing the frozen predicate. Measured: `w3b` reads `pins 3/3 exit 0`, and
`ledger conjunct HOLDS (required 9 == ledgered 9)`; its only failure is `surfaces pass 5 of 7`.
The Q45 lowering is permitted *before data*, and if the wave-1 census lands on 5, `w3b` reads
exit 0. Fix before data: require that the pinned opencode path's bytes are the live ELF
(`~/.opencode/bin/opencode`, `ca9b3ee2…`, 240 416 944 bytes) — or, weaker, a size/ELF-magic floor
plus the dump's sha recorded in the receipt.

**F2.** `check_substrate_pins.py` green is not freshness: four of five worlds read `3/3 exit 0`,
including both stub worlds. The pin instrument compares one sha and one mtime and has no notion of
"binary".

**F3.** Worlds 1 and 2 are the *same measurement* on the existing instruments:
`observed-surfaces.json` for w1, w2 and w4 are byte-identical (`sha256 2afd5745a13675f3…`), and
w2's `observed-pins.json` is byte-identical to w1's (`2377e3e5ba8cbf2b…`). Neither instrument
opens `census-removals.json`; the ledger conjunct exists only in the new counter, so it must be
implemented and shown to fail w2 before data.

**F4.** The 7-check `(id, status)` vector is byte-identical across **all five** worlds —
`jq -c '[.checks[]|{id,status}]' observed-surfaces.json | sha256sum` → `93cd5b3e29136d8c…` for
each. A counter that counts passes cannot tell honest new bytes (w1) from a stub (w3/w3b). The
only discriminating signal in the output is `detail` text (w1: "1 loader literal(s) not
verifiable"; w3: "9 loader literal(s) not verifiable"), which the frozen predicate does not read.

**F5.** At the base with **default** paths both instruments refuse to evaluate: pins
`{"pass":0,"fail":3,"exit_code":2}`, surfaces `{"checks":[],"exit_code":2,"error":"opencode
binary not found"}`. The plan's `DRIFT 3/3` base row is the flag-overridden reading. Consequence
for the counter: at the base its own default-path run reads `pins OK 0/3; surfaces pass 0 of 7`
because nothing was measured, not because 7 checks failed — a `checks == []` result must be
treated as could-not-evaluate, never as 0 of 7.

**F6.** The mtime half is genuinely two-sided: w4 keeps the correct sha (`85d9daf3…` on
`omp.real`) and a stale mtime and reads `2/3 exit 1` with `delta_ns 173397942086864`. Nothing else
in w4 moves the surface half (byte-identical to w1), so the two conjuncts are independent.

## Risks / caveats for the L1

* **Host-anchored.** Every reading names the substrate it measured. `~/.local/bin/omp` is now a
  1 680-byte wrapper (`ed62a41e…`, 2026-10-23) — that is the base's omp path drift;
  `~/.local/bin/omp.real` is `85d9daf3…` with the r51 mtime, so the omp pins hold once the path
  moves. `~/.opencode/bin/opencode` is `ca9b3ee2…`, 240 416 944 bytes. A rebuilt host binary
  changes every number; re-run `replay.sh` (it overwrites `observed-*.json`).
* **w3/w3b pin an absolute path into the sandbox.** The counter must run while that sandbox
  exists (`KEEP=1 ./replay.sh`, then `--rev <world commit> --repo <sandbox>/kotoba-shokunin`);
  a deleted sandbox turns them into UNREADABLE (exit 2), not a verdict. `replay.sh` already runs
  the counter when `verifiers/check_substrate_repin_v2.py` exists in the lane.
* **Counter CLI assumed.** The counter step uses `--rev` / `--repo`, modelled on
  `check_opencode_repin.py`; it is guarded by a file-existence test and its own error is the
  signal. No world depends on the flags — the instruments in each world read only their own
  default paths.
* **Schema coordination, not a claim.** `census-removals.json`'s shape (`removals[].class_id`)
  was agreed with the counter seat by message; I verified it against my own probe, not against
  their code, which does not exist at the lane yet (`ls` above).
* **Nothing was installed or upgraded** for this seat (no `uv tool`, `npx`, `pacman`, no
  `~/.local/bin` binary); `jq` and `python3` were already present.

## The frozen counter, run by me (post-build; ExecRepinCounter's draft)

Once ExecRepinCounter's draft landed in `w1/build/ExecRepinCounter/check_substrate_repin_v2.py`
(not yet at `verifiers/check_substrate_repin_v2.py`), I rebuilt w1 and w3b with `KEEP=1
./replay.sh` and ran the counter myself:

```
$ python3 -B <build>/ExecRepinCounter/check_substrate_repin_v2.py --rev <world commit> --repo <sandbox>/kotoba-shokunin
w1-repin-only:   exit 1
  host substrate re-derived: pins OK 3/3; surfaces pass 5 of 7; removal ledger 0 of 1 verified
  FAIL surfaces: 5 of 7 check(s) PASS, 7 check(s) reported, 7 expected
w3b-stub-full-ledger:   exit 1
  host substrate re-derived: pins OK 2/3; surfaces pass 5 of 7; removal ledger 1 of 9 verified
  FAIL substrate identity: pin(s) opencode_binary_sha256 PASS on bytes that are not the live
  opencode the counter dumped (sha256 ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7)
```
A sixth world, `w5-repin-plus-honest-ledger` (w1's overlay + the honest one-row ledger
`opencode:instructions/CONTEXT.md`), was built at the counter seat's request to make the lowering
hazard a measured world. My replay and counter run:

```
world commit: 752764508ac377ebc5704b7ba2fcd12273740acc
check_substrate_pins.py exit=0 / verify_surfaces.py exit=1
ledger-probe: base opencode classes 9; ledgered 1; required 1 -> ledger conjunct HOLDS (exit 0)
$ python3 -B <build>/ExecRepinCounter/check_substrate_repin_v2.py --rev 7527645… --repo <sandbox>/kotoba-shokunin
host substrate re-derived: pins OK 3/3; surfaces pass 5 of 7; removal ledger 1 of 1 verified
substrate opencode: /home/vgpnk/.opencode/bin/opencode sha256 ca9b3ee2… bytes 240416944 strings 1237844
FAIL surfaces: 5 of 7 check(s) PASS, 7 check(s) reported, 7 expected
exit=1
```

At the frozen target this reads exit 1 (below target on surfaces). The lowering hazard was then
measured, not inferred: a throwaway copy of the counter with `CHECKS_TOTAL = 5` (lane file
untouched, /tmp copy deleted after) run against this world still reads **exit 1** —
`FAIL surfaces: 5 of 7 check(s) PASS, 7 check(s) reported, 5 expected` — because the counter's
row-count guard requires the instrument to report exactly `CHECKS_TOTAL` checks and
`verify_surfaces.py` still reports 7. So **a lowering alone cannot green this world**; the
reachable hazard is a lowering **plus** retiring two checks from `CHECK_IDS` in
`verifiers/verify_surfaces.py`, a visible instrument change whose self-test assertion count moves
the `floors-registry.json` floor. What neither the target number nor the verdict vector can see
is the identity of the failing checks (this world's 7-check `(id, status)` vector is byte-identical
to w1's, `sha256 93cd5b3e29136d8c…`), so the retirement-plus-lowering combination would read
clean while the OC rules stay un-derived — the load-bearing reason a lowering below 7 must carry
a detail-reading check or an extraction-population floor.

Both exit 1; the counter's output line matches the frozen predicate shape. Notably the counter
folded the substrate-identity check into the pins count (the live-dump referent is
`~/.opencode/bin/opencode`, never the tree's pinned path; its substrate line prints path/sha256/
bytes/strings). That closes the w3b lowering hole I raised in F1 **for w3b** (it now fails both
identity and the ledger). What remains open is **F4's residual**: the reachable green-reading
shortcut is a lowering **plus** retiring the two failing checks (`surfaces.literal_present`,
`surfaces.opencode_extract`) from `CHECK_IDS` — a combination the pass-count cannot see because
the remaining checks' `(id, status)` vector is byte-identical to honest work (w1/w5,
`sha256 93cd5b3e29136d8c…`); only the `detail` text distinguishes, and the frozen predicate does
not read `detail`. The floors gate sees the retirement (self-test assertion count), so the counter
is protected exactly as long as `floors-registry.json` is enforced; the detail-reading floor
remains the recommendation for any lowering below 7.

## Blockers

None. Every conjunct is now measured — by the existing instruments, by my probe, or by my own run
of the counter's draft on w1 and w3b — with exit codes and per-check verdicts recorded above and
in each world's `observed-counter.txt`.
