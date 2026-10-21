verdict: PARTIAL — the pin count 3/3 and every pinned value re-derives correctly at 7ad7fad (exit 0, 3/3; sha256 == frozen SHA256SUMS; omp mtime ns-exact at 9 fractional digits; `--self-test` 0/62), but the opencode pin is bytes-at-a-constant-path whose *premise* (the npx launcher) is unpinned, so a launcher re-point leaves the guard GREEN — and the discovery rule silently ignores a compound-kind pin key.

Lane: W2PinsRerun (reviewer). Base: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.
Scratch clone: `/fast/scratch/kotoba-r47/w2/W2PinsRerun/kotoba-shokunin` (`git clone --no-hardlinks` of the fleet repo, `git checkout --detach 7ad7fad`). No production file was read-only-violated; nothing in the fleet repo was written except this report.

Targets:
- `verifiers/check_substrate_pins.py` @ 7ad7fad — sha256 `9615d5476ca1d8031880aca92c137526e989ce13d69298379b9dc95a2067e4ee` (BASE `c61a973b`: `bcfd5230eabb8b16343e11b21ec354d9860c65e4712187fc6650fc3f329495ce`)
- `verifiers/baseline.json` @ 7ad7fad — sha256 `0cc0e0b036274bf50d2c824a9915ae286390eba4c0c2abd487f2b36eb8a051fd`

---

## A. The acceptance battery — every item PASSES

### A1. Counting command, live tree and canonical-layout clone

```
$ cd /fast/scratch/kotoba-r47/w2/W2PinsRerun/kotoba-shokunin && python3 -B verifiers/check_substrate_pins.py
PASS omp_binary_sha256: fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
PASS opencode_binary_sha256: 179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9
OK 3/3 pins hold
EXIT=0
```

Same three lines and `exit 0` from the fleet tree (`/home/vgpnk/Projects/shokunin/kotoba-shokunin`, `git status --porcelain verifiers/` empty, `git diff 7ad7fad -- verifiers/check_substrate_pins.py verifiers/baseline.json` empty → the fleet tree's two target files are byte-identical to 7ad7fad).

### A2. `--json` at the tip — exit 0, `pass: 3`, `fail: 0`, `exit_code: 0`

```
$ python3 -B verifiers/check_substrate_pins.py --json     # EXIT=0
{"checks":[{"binary":"/home/vgpnk/.local/bin/omp","expect":"fdbc8136…","kind":"sha256","observed":"fdbc8136…","pin":"omp_binary_sha256","substrate":"omp","verdict":"PASS"},
 {"binary":"/home/vgpnk/.local/bin/omp","delta_ns":0,"expect":"2026-10-21T03:30:38.135013187-03:00","kind":"mtime","observed":"1792564238135013187","pin":"omp_binary_mtime","substrate":"omp","tolerance_ns":0,"verdict":"PASS"},
 {"binary":"/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe","expect":"179ca421…","kind":"sha256","observed":"179ca421…","pin":"opencode_binary_sha256","substrate":"opencode","verdict":"PASS"}],
 "exit_code":0,"fail":0,"pass":3}
```
Determinism: two consecutive `--json` runs are byte-identical (`sha256sum` of stdout `4ffc77c1690ad942f736b638862f700bc1c56370b9907e80ed0aeb6f2331576d` both times).

### A3. Every pinned sha256 == the frozen `SHA256SUMS` == the live bytes

```
$ cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS
bin/omp-18.12.5: OK
bin/opencode-1.19.3: OK
omp-18.12.5.strings: OK
opencode-1.19.3.strings: OK
EXIT=0
```
`SHA256SUMS` lines 1–2 are `fdbc8136…  bin/omp-18.12.5` and `179ca421…  bin/opencode-1.19.3` — byte-for-byte the two `measured_against` sha pins (`verifiers/baseline.json:5`, `:11`). The frozen snapshot files are byte-identical to the live pinned artifacts:
```
$ cmp /fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3 /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe   # BYTE-IDENTICAL
$ cmp /fast/scratch/kotoba-r47/shared/bin/omp-18.12.5        /home/vgpnk/.local/bin/omp                                            # BYTE-IDENTICAL
$ sha256sum /home/vgpnk/.local/bin/omp /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e  /home/vgpnk/.local/bin/omp
179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9  …/opencode-ai/bin/opencode.exe
```
So the C1 claim "re-pinned from the frozen snapshot the surfaces re-derivation was measured on" is *true*: the pinned bytes are the snapshot bytes, and the snapshot bytes are the live bytes.

### A4. The omp mtime pin has 9 fractional digits and is ns-exact

`verifiers/baseline.json:6` — `"omp_binary_mtime": "2026-10-21T03:30:38.135013187-03:00"`. Fractional part `135013187` = **9 digits**. Independent re-derivation (not via the guard):

```
$ stat -c '%n mtime=%y' /home/vgpnk/.local/bin/omp
/home/vgpnk/.local/bin/omp mtime=2026-10-21 03:30:38.135013187 -0300
$ python3 -c "…calendar.timegm(datetime.fromisoformat('2026-10-21T03:30:38-03:00').utctimetuple())*10**9 + 135013187"
1792564238135013187
$ python3 -c "import os;print(os.stat('/home/vgpnk/.local/bin/omp').st_mtime_ns)"
1792564238135013187     # identical
```
Guard reports `delta 0 ns`, `tolerance_ns 0` — with 9 digits the pin's acceptance window is 1 ns, i.e. exact (`verifiers/check_substrate_pins.py:150` — `tolerance_ns = 10 ** (9 - len(digits)) - 1`).

Note the opencode artifact *does* have a pinnable mtime (`2026-10-20T18:33:42.152682158-03:00`, ns `1792532022152682158`) — it is the npm extraction time, not a 1985 packer constant. I verified the guard enforces an `opencode_binary_mtime` pin if one is planted (PASS, delta 0 ns; a 1985 value → DRIFT, exit 1). This is the factual error in the corpus record — see F4.

### A5. `--self-test` exit 0, 62 assertions

```
$ python3 -B verifiers/check_substrate_pins.py --self-test
0 failure(s) over 62 assertions
EXIT=0
```
Matches the floor registry (`verifiers/floors-registry.json` → `"pins": {"floor": 62}`) and `python3 -B verifiers/check_assertion_floors.py` → `PASS pins observed=62 floor=62`, exit 0, all 9 floors PASS.

### A6. The before-value reproduces byte-identically

```
$ git show c61a973b:verifiers/check_substrate_pins.py > /tmp/w2p_base_script.py
$ git show c61a973b:verifiers/baseline.json       > /tmp/w2p_base_bl.json
$ python3 -B /tmp/w2p_base_script.py --baseline /tmp/w2p_base_bl.json
ERROR UNREADABLE opencode_binary_sha256: [Errno 2] No such file or directory: '/home/vgpnk/.opencode/bin/opencode'
FAIL omp_binary_sha256: sha256 drift: expect=9513ef9f… got=fdbc8136…
FAIL omp_binary_mtime: mtime drift (sha256 not compared): pinned_ns=2026-10-19T12:35:55.628149917-03:00 observed_ns=1792564238135013187 delta_ns=140082506863270 tolerance_ns=0
FAIL opencode_binary_sha256: UNREADABLE: [Errno 2] No such file or directory: '/home/vgpnk/.opencode/bin/opencode'
DRIFT 3/3 pins failed: omp_binary_sha256, omp_binary_mtime, opencode_binary_sha256
EXIT=2
$ diff <(python3 -B /tmp/w2p_base_script.py --baseline /tmp/w2p_base_bl.json 2>&1) .ufo/waves/round-47/before/check_substrate_pins.py.out
# → BYTE-IDENTICAL to the recorded before
```
The recorded before is therefore honest, and the round-47 after-battery (`.ufo/waves/round-47/after/check_substrate_pins.out`) is byte-identical to my tip run.

### A7. Negative ladder still fail-closed at the tip (quick regression, not re-litigated)

`--opencode-binary /nonexistent/opencode.exe` → `UNREADABLE 1/3 pins failed`, **exit 2**; deleting `omp_binary_mtime` from a baseline copy → `PIN_ABSENT`, **exit 1**; `omp_binary_sha256x` planted → `UNSUPPORTED`, **exit 2**; `cursor_binary_sha256` planted → `UNSUPPORTED`, **exit 2**. The guard never executes the pinned binaries (`grep -n 'subprocess|os.system|Popen' verifiers/check_substrate_pins.py` → no match; `~/.local/share/opencode/log/opencode.log` mtime unchanged at `2026-10-20 07:52:21`).

**Verdict on the acceptance battery: HOLDS. Every literal item in my assignment passes.**

---

## B. Findings

### F1 (S1, HIGH) — the opencode pin is bytes-at-a-constant-path whose premise is unpinned: a launcher re-point leaves the guard GREEN

`verifiers/check_substrate_pins.py:64-67`:
```python
BINARIES = {
    "omp": "/home/vgpnk/.local/bin/omp",
    "opencode": "/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe",
}
```
The pinned path is a **derived** path: it is `~/.npm/_npx/<sha512("opencode-ai")[:16]>/node_modules/opencode-ai/bin/opencode.exe`. The thing that *decides* which artifact runs is the launcher `/home/vgpnk/.local/bin/opencode` (1460 B bash script, sha256 `b240efa9d6020bdc513bbf48e46b6d312493d2c408f7d070555e993feea0a89b`), which resolves the spec at run time via `npx --yes --package opencode-ai -- which opencode` (`/home/vgpnk/.local/bin/opencode:42-47`). **Nothing in `measured_against` pins the launcher, and no verifier reads it** (`grep -rn 'local/bin/opencode' verifiers/` → 1 hit, a prose mention at `verifiers/check_substrate_pins.py:43`, not a constant). The docstring at `:42-45` states the position ("the wrapper itself is never the pinned file, its sha says nothing about the ELF that runs") — but that is the wrong half of the argument: the wrapper's sha does not describe the ELF, yet the wrapper *is* the premise that selects the ELF, and nothing constrains it.

**Repro (my own, first-hand — not read from the wave-1 report).** I modelled the host shape exactly (npx cache dir named by `sha512(spec)[:16]`, `node_modules/.bin/opencode` symlink → `../opencode-ai/bin/opencode.exe`, package `postinstall` hardlink), then re-pointed the launcher at a different spec. Fixture: `/tmp/w2p_swap/` (`repro.sh`, `host/`).

```
$ /tmp/w2p_swap/repro.sh
== BEFORE: launcher spec=opencode-ai ; it execs:
   /tmp/w2p_swap/host/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
PASS omp_binary_sha256: fdbc8136…
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
PASS opencode_binary_sha256: 179ca421…
OK 3/3 pins hold
   guard EXIT=0

== AFTER: launcher re-pointed at spec opencode-ai@2 ; it execs:
   /tmp/w2p_swap/host/.npm/_npx/7a4e98aa068b844b/node_modules/opencode-ai/bin/opencode.exe
   launcher-resolved sha: 87084ea27c32bebbdcae6088527aff86895f051345e15bdbc9f61576a8a63b6c
PASS omp_binary_sha256: fdbc8136…
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
PASS opencode_binary_sha256: 179ca421…
OK 3/3 pins hold
   guard EXIT=0
```
The launcher now executes bytes the guard has never seen (`87084ea2…` vs the pinned `179ca421…`), and the guard reports **`OK 3/3 pins hold`, exit 0**. The old artifact is still on disk at the constant path, so the content pin holds. This is the round-21 defect class in a new costume — *the pin is enforced, but on the wrong object* — and it is exactly the failure mode the guard exists to prevent ("an unenforced pin is the defect", `LOG.md` round-21).

**Why the constant path is not self-validating.** The `_npx` directory name is `sha512(spec)[:16]`, i.e. it is stable across upstream *releases* of the same spec (verified independently: `sha512("opencode-ai")[:16] == e2094862b59aac7b`, matching the live dir; `sha512("rea-agents@6.7.0")[:16] == a1722018f28f9df2`, matching the other npx dir on this host). So a *new upstream version* replaces the bytes **in place** → the sha256 pin does fire (good). But a *spec change* (launcher edit) produces a **different directory** → the pinned path keeps the old bytes → the guard is green while a different artifact runs. The guard cannot see the difference because it never asks the launcher.

**This was already found in wave 1 and was not integrated.** `.ufo/waves/round-47/build/RevPinsContract.md` §1-F1 rates it HIGH, with a counterexample of the same shape; `RevPinsContract.patch` proposes pinning the launcher as a substrate of its own (`EXPECTED_PINS` 3 → 4, sha `b240efa9…`) plus a one-character widening of the discovery kind class. `.ufo/waves/round-47/build/C1CriticRepin.md:83` independently reaches the same conclusion and adds it to the wave-2 checklist as item (12). **Neither was integrated:** the whole BASE→tip diff of `verifiers/check_substrate_pins.py` is 2 hunks — the docstring paragraph and the one `BINARIES["opencode"]` string:
```
$ git diff c61a973b 7ad7fad -- verifiers/check_substrate_pins.py | grep -E '^[+-]' | grep -v '^[+-][+-]'
-Host-anchored: the default binary paths are this host's installs (same constants
-as verify_harness_claims.py:52,55), so a clone's green is a statement about that
+Host-anchored: the default binary paths are this host's installs (same values
+as verify_harness_claims.py OMP_BIN/OC_BIN and verify_surfaces.py
+DEFAULT_BINARIES; round 47 moved opencode to the npm `opencode-ai` bytes the
+`~/.local/bin/opencode` npx wrapper executes — the wrapper itself is never the
+pinned file, its sha says nothing about the ELF that runs), so a clone's green is a statement about that
-    "opencode": "/home/vgpnk/.opencode/bin/opencode",
+    "opencode": "/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe",
```
`EXPECTED_PINS` is still 3 entries (`:75-79`); the launcher is not among them; `DISCOVER_RE` is untouched (`git show 7ad7fad -- verifiers/check_substrate_pins.py | grep -c DISCOVER_RE` → 0).

**And it is not recorded as carried debt.** `grep -rn 'RevPinsContract\|launcher\|opencode_launcher' LOG.md plans/ PROVINCE.md SCORECARD.md` → **0 hits**. `corpus/lessons/round-47.md` `## Mistakes` (M20–M22) does not mention it. The round-47 landing entry (`LOG.md:2321-2327`) claims C1 freshness "improved" without naming the residual. So the round currently asserts a strengthened pin guard while the two HIGH wave-1 findings on that same guard were dropped silently. (Note: a sibling falsify lane `W2PinsSentinel` is dispatched on exactly this npx-cache question, and `W2PathAuthority` on the three-constant duplication — my finding overlaps theirs by design; the distinct part I add is the *first-hand reproduction* and the observation that the fix was authored and dropped, not merely unconsidered.)

**Cheapest closure** (integrator's call, not mine): pin the launcher as a fourth substrate (`opencode_launcher_binary_sha256` = `b240efa9…`, `BINARIES["opencode_launcher"] = "/home/vgpnk/.local/bin/opencode"`), which turns any spec re-point into a DRIFT. The prefix class `[a-z0-9_]+` already admits underscores, so this needs **no regex change**; the cost is one more pin to re-record per install change, which is the point. A stronger alternative is to re-derive the npx directory at check time from the launcher (npm's `libnpmexec/lib/index.js:250-262` hash rule) — that also closes the npm-cache-root and node/npm-upgrade residuals (R-1/R-1b in `RevPinsContract.md` §4), at the price of coupling the guard to an npm internal (which would fail loudly, never silently).

### F2 (S1, HIGH) — a compound-kind pin key is SILENTLY IGNORED: the guard reports 3/3 while a 4th pin-shaped key sits unenforced

`verifiers/check_substrate_pins.py:80-81`:
```python
DISCOVER_RE = re.compile(r"^(?P<prefix>[a-z0-9_]+)_binary_(?P<kind>[A-Za-z0-9]+)$",
                         re.IGNORECASE)
```
The **kind** class is `[A-Za-z0-9]+` — no underscore. The discovery loop at `:179-186` only enqueues a key if `DISCOVER_RE.match(key)` matches (or its hygiene-stripped form does, or it has hygiene offenders). A key shaped `opencode_binary_resolved_sha256` matches **nothing** and is therefore never enqueued — it is not reported, not verified, not counted.

**Repro (first-hand, at the tip):**
```
$ python3 -B verifiers/check_substrate_pins.py --baseline <copy with opencode_binary_resolved_sha256="0"*64> --json
EXIT=0   pass=3 fail=0   checks=3   ['omp_binary_sha256','omp_binary_mtime','opencode_binary_sha256']
```
Four pin-shaped keys are in `measured_against`; the guard says `OK 3/3 pins hold`, **exit 0**, and never mentions the fourth. Same for `omp_binary_sha256_r47`, `omp_binary_sha256_extra`, `opencode_binary_sha_256`, `omp_binary_`.

The contrast with a *single-token* kind is stark and shows the failure is in the regex, not the design:
```
+ 'opencode_binary_resolved_sha256'   exit=0  checks=3   (silently dropped)
+ 'omp_binary_sha256_extra'           exit=0  checks=3   (silently dropped)
+ 'omp_binary_'                       exit=0  checks=3   (silently dropped)
+ 'omp_binary_sha256x'                exit=2  checks=4   UNSUPPORTED (discovered, fail-closed)
+ 'cursor_binary_sha256'              exit=2  checks=4   UNSUPPORTED (discovered, fail-closed)
+ 'omp_binary_sha256 '                exit=2  checks=4   UNSUPPORTED (hygiene)
+ 'opencode_binary_resolved_sha256'   exit=0  checks=3   ← the hole
```
This is the guard's own stated contract violated: `verifiers/check_substrate_pins.py:69-73` says discovery exists so that "a pin the guard cannot resolve is UNSUPPORTED (exit 2), **never a silent skip** — the round-21 vacuity lesson applied to coverage." The compound-kind key is the one shape where the guard *can* neither resolve nor report it.

**Why this matters for C1 specifically.** The C1 re-pin is exactly the operation that wants a compound-kind key: the substrate moved from a fixed `~/.opencode/bin/opencode` to a *resolved* npx artifact, and the natural record of that is `opencode_binary_resolved_sha256`. The moment round 48 (or a future re-pin) writes such a key, it becomes a pin that is enforced by nothing, reported by nothing, and counted in neither the pass nor the fail total — while every gate stays green. This is the round-21 vacuity class recurring.

**Also found in wave 1, also not integrated.** `RevPinsContract.md` §1-F2 (HIGH) with the identical observation and the fix (widen `[A-Za-z0-9]+` → `[A-Za-z0-9_]+`, one character); `C1CriticRepin.md:82` independently confirms it and files it as wave-2 checklist item (12): *"no `measured_against` key matching `_binary_` is absent from the guard's verdict list (count keys vs `--json` `checks`), and a planted compound-kind key must not leave the guard green."* Neither the fix nor a carried-debt record exists at the tip.

**I verified the checklist item is currently unmet**, by counting keys against `--json` checks: at the tip, `measured_against` has 8 keys; the regex discovers exactly the 3 contract pins; `undeclared-but-pin-shaped` = `[]`; the 5 non-pin keys are `omp_round21_note`, `omp_round44_note`, `command`, `round18_move`, `round47_note`. So the *current* block is clean — the hole is latent, and it opens the moment a compound-kind key is written.

### F3 (S2, MEDIUM) — `as_of` is stale by 7 days and now understates the substrate it certifies

`verifiers/baseline.json:2` — `"as_of": "2026-10-14T09:58:47.702772-03:00"`. Unchanged across `6fbbff5` → `c61a973b` → `7ad7fad` (verified by `git show <c>:verifiers/baseline.json | python3 -c '…print(as_of)'` for all three — identical string). Round 47 re-derived and re-pinned both substrates on 2026-10-21 and recorded the fact in `round47_note` (`verifiers/baseline.json:12`, "Re-pinned round 47 (2026-10-21) …"), but left `as_of` pointing at 2026-10-14 — the date of the *previous* pin (18.12.2 / d9123b9b). A reader of `as_of` alone concludes the pins were measured a week before the substrate they describe. The field is read by no instrument (`grep -n as_of verifiers/*.py` → 0 hits), so it is documentation-only, but it is the timestamp a human cites, and it is now wrong in the direction that matters (older than the substrate).

### F4 (S2, MEDIUM) — the corpus record for this guard is stale in five places and was not touched at 7ad7fad

`corpus/knowledge/substrate-pin-guard-round23.md` was **not modified** by round 47 (`git diff --name-only c61a973b 7ad7fad | grep -c substrate-pin-guard-round23` → 0). Its claims vs. the tip:

| line | claim in the record | measured at 7ad7fad |
|---|---|---|
| `:11` | guard "file sha256 `fafe88d881eb…`" | `9615d5476ca1d8031880aca92c137526e989ce13d69298379b9dc95a2067e4ee` |
| `:17-18` | "opencode's mtime is a 1985 packer constant and unpinnable; only its sha is enforced" | **False.** The opencode ELF's mtime is the npm extraction time `2026-10-20 18:33:42.152682158-03:00` (ns `1792532022152682158`), and it *is* pinnable — the guard enforces a planted `opencode_binary_mtime` at that value with PASS/delta 0 ns, and DRIFTs a 1985 value. The *reason* only-sha-is-enforced changed (it now moves on every npm re-extract); the sentence as written is untrue. |
| `:32-33` | "live: … exit 0, `OK 3/3 pins hold`" | true at the tip, but the record is presented as the round-23 landing battery and was false at round 23 (it was exit 2 then) |
| `:34` | "`--self-test` → `0 failure(s) over 51 assertions`" | `0 failure(s) over 62 assertions` |
| `:35-38` | "tripwire.bin is a 0755 sentinel that appears only if exec'd, turning hash-never-exec into an assertion" | **No assertion uses it.** `grep -rn tripwire verifiers/` → **0 hits**. The fixture exists (`verifiers/fixtures/pins/tripwire.bin`, 0755, 41 B) and is committed, but nothing consumes it — the record advertises a verification the code does not perform. |

`corpus/README.md:58` (the coverage row, indexed and path-verified by `verify_corpus_integrity.py`) repeats the same stale clauses: "opencode sha256 only — its mtime is a 1985 packer constant", "at landing: live exit 0 (`OK 3/3 pins hold`…)", "0 failure(s) over…". Round 47 *did* touch `corpus/README.md` (2 rows changed: the round-46 spot-check row and the round-47 lessons row) but left line 58 — the substrate-pin row — alone.

This is squarely on the calibration axis: the corpus is the instrument-facing record of what the guard does, and it now misdescribes both the pin set and the guard's own file. Note the round-47 C3 work *did* add an in-source `GOVERNANCE_ERRATA` mechanism for a false red — the same mechanism is the right home for this false green, and it was not used here.

### F5 (S3, LOW) — three copies of the opencode path constant, no single source

`verifiers/check_substrate_pins.py:66`, `verifiers/verify_surfaces.py:130`, `verifiers/verify_harness_claims.py:56` each carry the same absolute npx path. Round 47 moved all three together (verified: `grep -n e2094862b59aac7b verifiers/*.py` → 3 hits, all identical) — the round-47 wave-1 finding F5 was correctly closed for this round. But the guard's docstring `:41-43` claims the constants are "the same values as verify_harness_claims.py OMP_BIN/OC_BIN and verify_surfaces.py DEFAULT_BINARIES" with **no line anchors** (the BASE text said ":52,55"), while `RevPinsContract.md` §1-F5 notes the anchors go stale on the next edit. A shared constant (or an assertion the guard makes about the other two files' values) would remove the class. Low severity: the three agree today.

### F6 (S3, LOW) — the `opencode_binary_mtime` omission is now a design choice with no recorded reason

The guard enforces omp's mtime but not opencode's, and `measured_against` records no rationale (the reason lives only in the now-false corpus sentence, F4). The live evidence supports *omission* for a different reason than the one on record — the npx artifact's mtime is the extraction time and moves on every npm re-extract, so pinning it would be a false-drift generator. But `omp_binary_mtime` is pinned at ns precision on a binary that is likewise reinstallable, so the two substrates are treated inconsistently without a stated rule. The right fix is a recorded reason in `measured_against` (the block already carries five prose keys for exactly this purpose), not silence.

---

## C. What I did NOT check

- **Did not execute the pinned binaries** (contract) — every conclusion about omp/opencode behaviour is from `sha256sum`, `stat`, `file`, and `strings` dumps; the loader-lineage claim (round-14 vs v2.0.26) is out of my slice and belongs to `W2OcLineage`/`W2PathAuthority`.
- **Did not run `~/.local/bin/opencode`** (contract) — the wrapper's resolution chain is derived statically: `sha512(spec)[:16]` read from `libnpmexec/lib/index.js:250-262`, the `.bin/opencode` symlink target read from the filesystem, and the inode identity confirmed (`opencode-ai/bin/opencode.exe` and `opencode-linux-x64/bin/opencode` are the **same inode 43795736**, links=2 — so the path choice is content-equivalent today, per `RevPinsContract.md` §1-F3).
- **Did not test the npm-cache-root relocation residual** (`NPM_CONFIG_CACHE` / `~/.npmrc`) beyond reading host state: `~/.npmrc` absent, `NPM_CONFIG_CACHE` unset, `npm config get cache` → `/home/vgpnk/.npm`. Not live here; the residual stands.
- **Did not test a node/npm upgrade** changing libnpmexec's `_npx` hash rule (R-1b).
- **Did not re-run the full round-47 after-battery** (`verify_surfaces.py`, `verify_skill_checklist.py`, corpus integrity/independent, fault harness) — those are other lanes' surfaces. I did run `check_assertion_floors.py` (exit 0, 9/9 PASS) because it directly carries the `pins` floor 62.
- **Did not audit the mutation battery** (`.ufo/waves/round-47/build/C1MutationPins.md`, M01–M10) — out of my slice; I did not re-run those 30 mutant probes.
- **Did not evaluate the C2/C3 claims** (no_xml_tag, GOVERNANCE_ERRATA, corpus baseline 58→60) beyond noticing that the C3 erratum mechanism was not applied to the false-green corpus claims (F4).
- **Did not verify the `--repo`/`--baseline` CLI surface under a hostile cwd**, nor the `check_pins` behaviour when `measured_against` contains a non-string value of a compound-kind key.
- **Did not modify any production file**, run any git write command in the fleet repo, or copy any strings dump or binary into the fleet tree. All mutations were in `/fast/scratch/kotoba-r47/w2/W2PinsRerun/` and `/tmp/w2p_swap/`.

---

## D. Residual risk if F1/F2 are not closed

1. A launcher edit (a 1-line change to a 1460-byte user script) re-points opencode to a different npx spec/directory; the guard stays `OK 3/3`, exit 0, and every other gate stays green. The pinned bytes are still on disk, so nothing observes the move. **This is the exact 2026-10-16 omp-rebuild scenario the guard was built to catch, reproduced for the new channel.**
2. A future re-pin that records a compound-kind key (`opencode_binary_resolved_sha256`, `opencode_binary_launcher_sha256`, `opencode_binary_path_sha256`) becomes a pin enforced by nothing, reported by nothing, and counted in neither total. The C1 re-pin is the operation most likely to write exactly such a key.
3. `corpus/knowledge/substrate-pin-guard-round23.md` + `corpus/README.md:58` continue to describe a guard that pins two sha256s and one mtime against a fixed path, with an untrue reason for omitting the opencode mtime, a stale file sha, a stale assertion count, and a tripwire fixture no assertion uses. Any lane that trusts the corpus row inherits those errors.

## E. Recommended disposition (integrator's call)

- **F1** — add the launcher as a pinned substrate (3 → 4 pins; `opencode_launcher_binary_sha256` = `b240efa9d6020bdc513bbf48e46b6d312493d2c408f7d070555e993feea0a89b`), or re-derive the npx directory from the launcher at check time. Update the C1 after-target to **pins 4/4** if the former. `RevPinsContract.patch` is on disk and self-tests green (62 → 78 assertions) but is **not** integrated at 7ad7fad.
- **F2** — one character: `[A-Za-z0-9]+` → `[A-Za-z0-9_]+` at `verifiers/check_substrate_pins.py:80`, so a compound-kind key is discovered and reported `UNSUPPORTED` (exit 2) instead of vanishing. Add the checklist assertion (12): count `measured_against` keys against `--json` `checks` and require every `_binary_`-shaped key to appear in the verdict list.
- **F3** — bump `as_of` to the re-derivation instant (2026-10-21T…), or add a `round47_as_of` key beside `round47_note`.
- **F4** — bring `corpus/knowledge/substrate-pin-guard-round23.md` and `corpus/README.md:58` to the tip: current guard sha, the true opencode-mtime rationale (npm extraction time, not a 1985 packer constant), the current assertion count (62), and either land an assertion that consumes `verifiers/fixtures/pins/tripwire.bin` or delete the tripwire sentence. The corpus index is path-based, so editing these files creates no index drift (no `corpus-baseline.json` re-record needed).
- **F5/F6** — record the "why opencode's mtime is not pinned" reason in `measured_against` next to the pins, and either de-duplicate the path constant or assert the three copies agree.

## F. Commands run (exact argv → exit code)

| # | command | exit | key output |
|---|---|---|---|
| 1 | `python3 -B verifiers/check_substrate_pins.py` (clone @7ad7fad) | **0** | `OK 3/3 pins hold`, omp mtime `delta 0 ns` |
| 2 | same, in the fleet tree `/home/vgpnk/Projects/shokunin/kotoba-shokunin` | **0** | identical 3 PASS lines |
| 3 | `python3 -B verifiers/check_substrate_pins.py --json` | **0** | `pass 3 / fail 0 / exit_code 0`; two runs byte-identical (`4ffc77c1…`) |
| 4 | `python3 -B verifiers/check_substrate_pins.py --self-test` | **0** | `0 failure(s) over 62 assertions` |
| 5 | `sha256sum -c SHA256SUMS` in `/fast/scratch/kotoba-r47/shared` | **0** | 4/4 OK |
| 6 | `cmp shared/bin/opencode-1.19.3 <npx artifact>`; `cmp shared/bin/omp-18.12.5 ~/.local/bin/omp` | 0 | BYTE-IDENTICAL (both) |
| 7 | `stat -c '%n %y' ~/.local/bin/omp`; python `st_mtime_ns` | 0 | `2026-10-21 03:30:38.135013187 -0300`; `1792564238135013187` == parsed pin ns |
| 8 | `git show c61a973b:verifiers/check_substrate_pins.py` + `:baseline.json` → live run | **2** | `DRIFT 3/3 pins failed` + `ERROR UNREADABLE opencode_binary_sha256`; stdout+stderr **byte-identical** to `.ufo/waves/round-47/before/check_substrate_pins.py.out` |
| 9 | probe: baseline copy + `opencode_binary_resolved_sha256` → `--json` | **0** | `checks=3`, 4th key never mentioned |
| 10 | probe: baseline copy + `omp_binary_sha256x` / `cursor_binary_sha256` | **2** | `checks=4`, `UNSUPPORTED` |
| 11 | probe: baseline copy + `omp_binary_sha256_extra` / `omp_binary_` / `opencode_binary_sha_256` | **0** | `checks=3` — silently dropped |
| 12 | probe: baseline copy + `opencode_binary_mtime` = live ns value | **0** | PASS, `delta_ns 0`, `tolerance_ns 0`; `checks=4` → opencode mtime IS pinnable |
| 13 | probe: baseline copy + `opencode_binary_mtime` = 1985 constant | **1** | DRIFT, `delta_ns 1319135622152682158` |
| 14 | `/tmp/w2p_swap/repro.sh` (launcher re-point, my fixture) | **0** | guard `OK 3/3 pins hold` **before and after** the swap; launcher-resolved sha `87084ea2…` ≠ pinned `179ca421…` |
| 15 | `python3 -B verifiers/check_substrate_pins.py --opencode-binary /nonexistent/opencode.exe` | **2** | `UNREADABLE 1/3 pins failed` |
| 16 | `python3 -B verifiers/check_assertion_floors.py` | **0** | `PASS pins observed=62 floor=62`; 9/9 floors PASS |
| 17 | `grep -rn tripwire verifiers/` | 1 (no match) | 0 hits — the committed fixture is unused |
| 18 | `grep -rn 'RevPinsContract\|launcher\|opencode_launcher' LOG.md plans/ PROVINCE.md SCORECARD.md` | 1 | 0 hits — the wave-1 HIGH findings are not carried as debt |
| 19 | `git diff --name-only c61a973b 7ad7fad \| grep -c substrate-pin-guard-round23` | 1 | `0` — the corpus record was not touched |
| 20 | `git show 6fbbff5/c61a973b/7ad7fad:verifiers/baseline.json` → `as_of` | 0 | identical `2026-10-14T09:58:47.702772-03:00` at all three |
| 21 | `sha512("opencode-ai")[:16]`; `sha512("rea-agents@6.7.0")[:16]` | 0 | `e2094862b59aac7b` (live npx dir) / `a1722018f28f9df2` (live npx dir) — the dir name is a hash of the **spec**, stable across releases, different across specs |
| 22 | `stat -c '%i %h' …/opencode-ai/bin/opencode.exe …/opencode-linux-x64/bin/opencode` | 0 | same inode `43795736`, links=2 — the two paths are the same file today |
| 23 | `npm config get cache`; `ls ~/.npmrc`; `echo $NPM_CONFIG_CACHE` | 0/1 | `/home/vgpnk/.npm`; no `.npmrc`; env unset — cache-root relocation not live |
| 24 | `grep -n 'subprocess\|os.system\|Popen' verifiers/check_substrate_pins.py` | 1 | 0 hits — hash-never-exec holds; `~/.local/share/opencode/log/opencode.log` mtime unchanged (`2026-10-20 07:52:21`) |

**Tooling:** no packages installed, no upgrades performed. `python3` 3.14.8 (system), `npm` 11.19.0 / node 26.12.0 (read only, to read npm's own hash rule), `coreutils` `sha256sum`/`cmp`/`stat`. The lane's only writes were this report and `/tmp/w2p_swap/` scratch fixtures.

**Scratch clone integrity:** `git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin kotoba-shokunin && git checkout --detach 7ad7fad` — `git status --porcelain` clean, `git log --oneline -1` = `7ad7fad`. No mutating git command was run in the fleet repo; no `.ufo/state`, MANIFEST.json, sibling lane, or git index/ref was touched.
