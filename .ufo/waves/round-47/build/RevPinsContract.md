verdict: the pin contract is sound for omp and stale for opencode — a path pin is NOT the fix (it is tautological against the guard's own constant); the smallest contract-consistent change is a second pinned substrate (the npx launcher) plus a one-character widening of the discovery kind class, because a compound-kind pin key is currently SILENTLY IGNORED and the C1 re-pin is about to write one.

Lane: RevPinsContract (reviewer). BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.
Targets reviewed: `verifiers/check_substrate_pins.py` (contract docstring + pin contract) and
`corpus/knowledge/substrate-pin-guard-round23.md`.
Artifacts: `.ufo/waves/round-47/build/RevPinsContract.patch` (proposal diff, +140/-15 on
`verifiers/check_substrate_pins.py`), `.ufo/waves/round-47/build/RevPinsContract.experiments.json`
(every command below, re-run, with exit codes).
Scratch (not production): `/fast/scratch/kotoba-r47/RevPinsContract/{base,lane,exp}`.

---

## 0. The new opencode install shape (re-derived, not assumed)

`/home/vgpnk/.local/bin/opencode` is a **bash wrapper**, not the binary (1460 B, sha256
`b240efa9d6020bdc513bbf48e46b6d312493d2c408f7d070555e993feea0a89b`):

```
$ file /home/vgpnk/.local/bin/opencode
/home/vgpnk/.local/bin/opencode: Bourne-Again shell script, ASCII text executable
```

It runs `npx --yes --prefer-online --package opencode-ai -- true`, then
`npx --yes --package opencode-ai -- which opencode-ai` (the package's own bin name — **no such
shim exists** in the npx `.bin/`), and falls through to `which opencode` (the `command=` name),
which resolves to `node_modules/.bin/opencode -> ../opencode-ai/bin/opencode.exe`. It execs what
that resolves to. The resolution is **derivable without executing anything**:

```
$ python3 exp/proto_resolver.py /home/vgpnk/.local/bin/opencode
spec      opencode-ai
npx_dir   /home/vgpnk/.npm/_npx/e2094862b59aac7b
shim      /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/.bin/opencode
artifact  /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
sha256     179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9
```

Three facts make the derivation exact (not a guess):

1. The `_npx` directory name is a **hash of the requested spec string**, not of the resolved
   version — npm 11.19.0, `node_modules/libnpmexec/lib/index.js:250-262`:
   `crypto.createHash('sha512').update(packages.map(...).sort().join('\n')).digest('hex').slice(0,16)`.
   Verified: `sha512("opencode-ai")[:16] == e2094862b59aac7b` (and
   `sha512("rea-agents@6.7.0")[:16] == a1722018f28f9df2`, the other npx dir on this host).
   ⇒ **the directory is stable across upstream releases of the same spec**: a new opencode-ai
   version replaces the bytes *in place*, which the existing sha256 pin already sees.
2. The artifact the wrapper actually execs is `node_modules/opencode-ai/bin/opencode.exe`, a
   **hardlink** of the platform package's ELF (`stat`: both inode 43795736, `links=2`), and the
   `.bin/opencode` shim is a symlink to it. The *before*-measurement pinned the other horn of
   that link, `node_modules/opencode-linux-x64/bin/opencode` (same inode, same bytes today).
3. `opencode-ai`'s `postinstall.mjs` chooses the platform package **by CPU features**
   (`packageNames()`: `opencode-linux-x64` when AVX2 is present, else `opencode-linux-x64-baseline`),
   then hardlinks that binary to `opencode-ai/bin/opencode.exe`. So the *selected* artifact is a
   host-dependent choice; the platform-package path is a **source**, not the live file.

The pinned opencode path at BASE, `verifiers/check_substrate_pins.py:63`
(`"/home/vgpnk/.opencode/bin/opencode"`), no longer exists — `ls: cannot access
'/home/vgpnk/.opencode/bin/': No such file or directory`.

## 1. Findings

### F1 (HIGH) — the opencode pin is bytes-at-a-constant-path, so a silent swap leaves the guard GREEN

`verifiers/check_substrate_pins.py:61-64` (BINARIES) and `:72-76` (EXPECTED_PINS) pin *bytes at a
hardcoded path*. Nothing in the contract states that the path is the one the launcher resolves to,
and nothing checks it. Counterexample (fixture modelling the host shape exactly — launcher, npx
dir, `.bin` symlink, package dir; `exp/swap_experiment.py`):

```
== AFTER the swap ==   (launcher re-pointed at spec "opencode-ai@2"; old cache dir still on disk)
   live artifact (resolved): .../_npx/7a4e98aa068b844b/.../opencode.exe   (old dir still present: True)
   A) constant-path guard   exit=0   OK 3/3 pins hold
        PASS opencode_binary_sha256: 4458932bebe6eb347022d42a3d0bf51f5d609c95add41c994d2f25fbcc395aea
   C) resolver guard         exit=1
        FAIL opencode_binary_sha256: sha256 drift: expect=4458932b… got=b356ff2d…
```

The guard hashes the artifact it was told about, while the launcher now execs a different one. This
is the round-21 defect class ("an unenforced pin is the defect") in a new costume: the pin is
enforced, but it is enforced on the wrong object.

### F2 (HIGH) — the discovery rule SILENTLY IGNORES a compound-kind pin key (the C1 re-pin is about to write one)

`verifiers/check_substrate_pins.py:77-78`:

```python
DISCOVER_RE = re.compile(r"^(?P<prefix>[a-z0-9_]+)_binary_(?P<kind>[A-Za-z0-9]+)$", re.IGNORECASE)
```

The **kind** class forbids `_`; the **prefix** class allows it. So a key such as
`opencode_binary_resolved_sha256` — the natural name for a "resolved realpath" record — matches
nothing, and the discovery loop at `:176-186` never enqueues it. Observed at BASE:

```
$ python3 exp/discovery_cases.py compound
case=compound exit=0
   PASS omp_binary_sha256: …   PASS omp_binary_mtime: …   PASS opencode_binary_sha256: …
   OK 3/3 pins hold
```

Four keys sit in `measured_against`; the guard reports **3/3** and never mentions the fourth. That
is a pin-shaped key that is *not enforced* and *not reported* — precisely the failure this guard
was built (round 23) to make impossible. The contrast with a single-token kind is stark:

```
$ python3 exp/discovery_cases.py path        # opencode_binary_path
case=path exit=2   FAIL opencode_binary_path: UNSUPPORTED: … (1/4 pins failed)
```

**Consequence for this wave:** if the C1 re-pin records any compound-kind key
(`…_binary_resolved_sha256`, `…_binary_launcher_sha256`, `…_binary_path_sha256`), the guard goes
green with that pin dead. This is a *pre-landing* hazard, not a post-landing one.

### F3 (MEDIUM) — the substrate of record for opencode should be the artifact the wrapper execs, not the platform-package file

The before-value pinned `node_modules/opencode-linux-x64/bin/opencode`; the live file is
`node_modules/opencode-ai/bin/opencode.exe` (F0.2). Same inode and same sha256 **today**
(`179ca421…`, matching the frozen snapshot `/fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3`
and `SHA256SUMS`), so the content pin is unaffected — but the two paths are not the same object
under the package's own selection rule (F0.3): a host without AVX2, or a version that reorders
`packageNames()`, selects the `-baseline` build, and the platform-package path would then hold a
*different* build than the one that runs. Pinning the **live artifact** removes that class.

### F4 (MEDIUM) — `corpus/knowledge/substrate-pin-guard-round23.md` is stale in five places

| line | claim | measured at BASE |
|---|---|---|
| `:11` | guard "file sha256 `fafe88d881eb…`" | `bcfd5230eabb8b16343e11b21ec354d9860c65e4712187fc6650fc3f329495ce` |
| `:17-18` | "opencode's mtime is a 1985 packer constant and unpinnable; only its sha is enforced" | the npx ELF's mtime is the **extraction time** `2026-10-20 18:33:42.152682158 -0300`; the *reason* it is unpinned changed (it now moves on every npm re-extract), and the sentence as written is false |
| `:32-33` | "live: … exit 0, `OK 3/3 pins hold`" | `python3 -B verifiers/check_substrate_pins.py` → **exit 2**, `DRIFT 3/3 pins failed` |
| `:34` | "`--self-test` → `0 failure(s) over 51 assertions`" | **`0 failure(s) over 62 assertions`** (exit 0) |
| `:35-38` | "tripwire.bin is a 0755 sentinel that appears only if exec'd, turning hash-never-exec into an assertion" | `grep -n tripwire verifiers/check_substrate_pins.py` → **0 hits**: the fixture exists (`verifiers/fixtures/pins/tripwire.bin`, 0755) but **no assertion uses it**; the doc advertises a verification the code does not perform |

`corpus/README.md:58` (the coverage row for this record) repeats the same stale clauses
("its mtime is a 1985 packer constant", "OK 3/3 pins hold", "0 failure(s) over…"), so it needs the
same edit. The corpus index is path-based (`verifiers/verify_corpus_integrity.py` tracks
`git ls-files corpus/` and the README's row set, not content hashes), so editing these files does
**not** create index drift.

### F5 (LOW) — three verifiers carry the same opencode path constant; a re-pin must move all three

`verifiers/check_substrate_pins.py:63`, `verifiers/verify_surfaces.py:130`
(`DEFAULT_BINARIES["opencode"]`), `verifiers/verify_harness_claims.py:55` (`OC_BIN`). The guard's
docstring (`verifiers/check_substrate_pins.py:41-43`) claims "same constants as
verify_harness_claims.py:52,55" — those line numbers are correct today (`OMP_BIN`=52, `OC_BIN`=55),
but the claim becomes false the moment one of the three moves. Any C1 re-pin must update all
three, or the cross-reference must be re-worded.

### F6 (LOW) — a path/realpath *pin* cannot do the job the assignment asks of it

The assignment's question is whether a path pin or a resolved-realpath record is needed. Against
the current contract, **no**:

* A path pin compared against the guard's *own* constant reduces to `realpath(p) == p` — a
  statement about the filesystem, not about the live substrate. Its only failure modes are
  "the file vanished" (already `UNREADABLE`, exit 2) and "the file became a symlink to a
  different target" (already caught by the content pin, unless the bytes are identical — in which
  case the red means nothing). It is **tautological**: it cannot fail independently of the
  content pin.
* A path pin compared against a *live* resolution (the resolver in F1) is meaningful — but then the
  path is volatile: an npm re-extract that changes only the path (same bytes) becomes a red about
  nothing, and a `path` kind that is only *discovered* (not in `EXPECTED_PINS`) can be **deleted
  from the block with no verdict at all** — `verifiers/check_substrate_pins.py:176-186` only
  enqueues keys that are present. Any path pin that must not be deletable belongs in
  `EXPECTED_PINS`.

## 2. The smallest contract-consistent change (proposal)

`RevPinsContract.patch` (+140/-15, one file, `verifiers/check_substrate_pins.py`). Two changes,
no new verdict, no exit-ladder change, no new pin kind, **no change to the discovery semantics for
any existing key**:

**(a) Pin the launcher as a substrate of its own** — the launcher carries the *premise* of the
artifact path (which package, which spec, which install shape), so any re-pointing of it is loud:

```python
BINARIES = {..., "opencode_launcher": "/home/vgpnk/.local/bin/opencode"}
EXPECTED_PINS = (..., ("opencode_launcher_binary_sha256", "opencode_launcher", "sha256"))
```

plus `--opencode-launcher` (CLI) and one entry in the `binaries` map (`:317`). The *prefix* class
already admits underscores, so the new substrate needs **no regex change** — verified: a key
`opencode_launcher_binary_sha256` is discovered at BASE and reported `UNSUPPORTED` (exit 2), i.e.
the shape is live and fail-closed.
`baseline.json` then records `opencode_launcher_binary_sha256 =
b240efa9d6020bdc513bbf48e46b6d312493d2c408f7d070555e993feea0a89b`.

**(b) Widen the discovery kind class** by one character — `[A-Za-z0-9]+` → `[A-Za-z0-9_]+` — so a
compound-kind key is *discovered* and then `UNSUPPORTED` (exit 2) instead of silently ignored.

**(c) The contract docstring** (`:45-74` in the patch) gains the two sentences the old one lacked:
that substrates are *resolution chains* (`<npm cache>/_npx/<sha512(spec)[:16]>/node_modules/.bin/<bin>`
→ the package's bin), that the npx directory is spec-derived and therefore stable across upstream
releases (bytes change in place → the sha256 pin sees it), and that re-pinning opencode means
re-deriving the artifact path from the launcher and re-recording **both** shas plus a mechanism
note.

**Why (a)+(b) and not a path pin:** the *premise* of the opencode pin is the launcher; pinning the
premise is what makes a constant path honest. The path itself is derived, and the derivation is
re-derivable from the pinned launcher by anyone with npm's source.

### 2.1 Self-test arms (all implemented in the patch; 62 → 78 assertions)

| # | arm | expected | BASE result | proposal result |
|---|---|---|---|---|
| A1 | launcher pin holds | exit 0, `OK 4/4 pins hold` | exit 2 `UNSUPPORTED 1/4` | exit 0 ✓ |
| A2 | **npx-cache swap** (launcher re-pointed at another spec) | exit 1, `FAIL opencode_launcher_binary_sha256: sha256 drift` | exit 2, no verdict for the pin | exit 1 ✓ |
| A3 | launcher missing (install method changed) | exit 2, `FAIL opencode_launcher_binary_sha256: UNREADABLE` | exit 2, generic `UNSUPPORTED` | exit 2 ✓ (token) |
| A4 | launcher pin deleted from the block | exit 1, `PIN_ABSENT` | **exit 0 `OK 3/3 pins hold`** | exit 1 ✓ |
| A5 | launcher pin mis-cased | exit 2, "matches opencode_launcher_binary_sha256 except for case" | exit 2, generic message | exit 2 ✓ (token) |
| A6 | launcher pin whitespace-padded | exit 2, `U+0020 Zs` | exit 2, generic | exit 2 ✓ |
| A7 | extra kind on the launcher substrate (`opencode_launcher_binary_mtime`) | exit 0 when it holds — the new substrate is first-class in the discovery space | — | exit 0 ✓ |
| A8 | **compound-kind pin** (`opencode_binary_resolved_sha256`) | exit 2, `UNSUPPORTED` — never a silent skip | **exit 0 `OK 3/3 pins hold`** | exit 2 ✓ |
| A9 | compound-kind pin on omp | exit 2 | — | exit 2 ✓ |

Discrimination table (BASE vs proposal, same fixtures):
`exp/discriminate.py` → **6/6 cases: BASE discriminates, proposal satisfies** (JSON in
`RevPinsContract.experiments.json`).
Proposal self-test: `python3 -B verifiers/check_substrate_pins.py --self-test` → **exit 0,
`0 failure(s) over 78 assertions`** (BASE: 62).

### 2.2 The C1 re-pin, with the launcher pin in place

* `omp_binary_sha256` → `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e`
  (`/home/vgpnk/.local/bin/omp`, mtime `2026-10-21 03:30:38.135013187 -0300`).
* `opencode_binary_sha256` → `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`
  (= the frozen snapshot `shared/bin/opencode-1.19.3` and `shared/SHA256SUMS`).
* **Path of record: the live artifact** `…/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`
  (F3), not the platform-package horn of the same inode.
* `opencode_launcher_binary_sha256` → `b240efa9d6020bdc513bbf48e46b6d312493d2c408f7d070555e993feea0a89b`.
* Mechanism note (mandatory, per the corpus doc's own rule): "opencode moved from a fixed
  `~/.opencode/bin/opencode` to an npx wrapper; the pinned path is now inside the npm npx cache
  whose directory is `sha512("opencode-ai")[:16]`; the launcher is pinned because it decides which
  artifact resolves."

## 2.3 Integrator checklist (if the proposal is landed)

1. `plans/round-47.md` C1 after-target: **pins 4/4** (the proposal adds
   `opencode_launcher_binary_sha256` to `EXPECTED_PINS`), and the plan's before-value
   "3/3 pins failed" becomes "3/3 failed + 1 PIN_ABSENT" before the new pin is recorded.
2. `verifiers/baseline.json`: record the four pins from **one** host state — omp
   `fdbc8136…` / mtime `2026-10-21 03:30:38.135013187 -0300`; opencode artifact
   `179ca421…`; launcher `b240efa9…` — plus the mechanism note.
3. `verifiers/check_substrate_pins.py:94-99` — repoint `BINARIES["opencode"]` from the deleted
   `/home/vgpnk/.opencode/bin/opencode` to the re-derived live artifact
   `~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` (the patch deliberately
   leaves the round-23 value with a comment, because the value must come from the integrator's
   re-derivation, not from a reviewer).
4. The same value must land in `verifiers/verify_surfaces.py:128-131`
   (`DEFAULT_BINARIES["opencode"]`) and `verifiers/verify_harness_claims.py:55` (`OC_BIN`), or the
   guard's docstring claim "same constants as verify_harness_claims.py:52,55" becomes false.
5. `corpus/knowledge/substrate-pin-guard-round23.md` + `corpus/README.md:58` — §3 below.

## 3. What the C3 corpus record must say (precise edit list for
`corpus/knowledge/substrate-pin-guard-round23.md`; also `corpus/README.md:58`)

1. `:11` — replace the guard's file sha with the landed sha, or state the sha as "at round 23".
2. `:12-18` — replace "hashes the live omp and opencode binaries" with the resolution-chain
   description: the opencode substrate is the artifact the npx wrapper resolves
   (`_npx/<sha512(spec)[:16]>/node_modules/<pkg>/bin/<bin>`); the launcher is pinned too; opencode's
   mtime is now the **npm extraction time** (volatile by construction) rather than a 1985 packer
   constant, which is *why* only its sha is pinned.
3. `:30-38` — re-derive the battery: live `exit 0, OK 4/4 pins hold` (or 3/3 if the launcher pin
   is deferred), `--self-test` → the **new** assertion count (78 with the proposal; 62 at BASE),
   and drop the tripwire sentence or land an assertion that actually uses
   `verifiers/fixtures/pins/tripwire.bin` (recommended: land the assertion — "hash-never-exec"
   deserves a mechanical witness, and the fixture is already committed and unused).
4. `:60-68` (Honest ceiling) — add: "the opencode pin is a change detector over a *derived* path;
   it does not detect a relocation of the npm cache root (`NPM_CONFIG_CACHE` / `~/.npmrc`), which
   moves the resolution while the pinned artifact stays on disk. On this host the root is the
   default `~/.npm` (no `~/.npmrc`, `NPM_CONFIG_CACHE` unset — measured). Closing that residual
   needs the guard to re-derive the npx directory at check time (npm's `libnpmexec` hash rule),
   which couples the guard to an npm internal; that is the deliberate trade the integrator may
   take, and it is *not* taken by this proposal."
5. `corpus/README.md:58` — mirror 2 and 3 into the coverage row.

## 4. Residual risk of the proposal (stated, not hidden)

* **R-1 (accepted, named):** the npm cache root can move (`NPM_CONFIG_CACHE`, `~/.npmrc`) while the
  pinned artifact stays on disk → the launcher pin does not fire → the guard is green while the live
  substrate moved. Not live on this host (measured: default `~/.npm`, no `~/.npmrc`, env unset).
  Closure = re-derive the npx dir at check time (the resolver prototype:
  `exp/proto_resolver.py`; it resolves the real host correctly, sha `179ca421…`), which couples the
  guard to npm's internal hashing rule; a npm change there breaks the derivation **loudly**
  (`UNREADABLE`/exit 2), never silently.
* **R-1b (added after the C1 critic's review): the Node/npm runtime is unpinned.** The wrapper
  picks its runtime with `mise where node@latest` and then runs *that* npm's `npx`. Nothing in
  `measured_against` pins node (currently 26.12.0) or npm (currently 11.19.0). A Node/npm upgrade
  can change libnpmexec's `_npx` directory rule ⇒ the live artifact moves to a **different
  directory** while the launcher's sha is unchanged ⇒ under this proposal (constant path +
  launcher sha) the guard stays green. This is the same class as R-1 and has the same closure:
  re-deriving the npx directory *at check time* with the *current* npm's rule finds the new
  directory and hashes the live bytes ⇒ DRIFT. It is also a second reason the *node/npm version*
  deserves its own pinned record once the resolver lands (a `node_runtime` substrate, sha of the
  npm entry point, is a candidate — outside this proposal's scope).
* **R-2:** the launcher pin is a *second* pin to keep — a pin that is not recorded is `PIN_ABSENT`
  (exit 1), so it cannot be dropped silently, but it does add a re-pin obligation per install
  change. That obligation is the point.
* **R-3:** the proposal keeps the opencode artifact path a constant. If the integrator prefers the
  resolver, the launcher pin becomes redundant (the resolver reads the launcher anyway) — but the
  resolver alone cannot detect a launcher edit that keeps the same spec (the spec is what the
  resolver reads), so the launcher *sha* pin is still the cheapest way to make a wrapper edit loud.
  Recommended landing: (a)+(b) now, (R-1 closure) as a named follow-on.
* **R-4:** `DISCOVER_RE` widening means a *note* key that happens to contain `_binary_` (e.g.
  `opencode_binary_path_note`) becomes `UNSUPPORTED` (exit 2). That is the fail-closed direction
  (notes must not look like pins), but the baseline's existing keys (`omp_round21_note`,
  `omp_round44_note`, `round18_move`, `command`) are unaffected — verified against the live
  `verifiers/baseline.json`.

## 5. Commands run (exit codes)

All in the scratch clone `/fast/scratch/kotoba-r47/RevPinsContract/{base,lane}`; **no production
file was modified**; the production repo was only read (and the two lane artifacts written).

| command | exit | key output |
|---|---|---|
| `python3 -B verifiers/check_substrate_pins.py` (BASE, live) | 2 | `DRIFT 3/3 pins failed: omp_binary_sha256, omp_binary_mtime, opencode_binary_sha256` |
| `python3 -B verifiers/check_substrate_pins.py --self-test` (BASE) | 0 | `0 failure(s) over 62 assertions` |
| `exp/discovery_cases.py compound` (BASE) | **0** | `OK 3/3 pins hold` — the 4th key silently ignored |
| `exp/discovery_cases.py path` (BASE) | 2 | `FAIL opencode_binary_path: UNSUPPORTED` |
| `exp/discovery_cases.py launcher` (BASE) | 2 | `FAIL opencode_launcher_binary_sha256: UNSUPPORTED` (shape is live) |
| `exp/discovery_cases.py miscase` (BASE) | 2 | `FAIL opencode_Launcher_binary_sha256: UNSUPPORTED` |
| `exp/swap_experiment.py` | 0 | A) constant-path guard **exit 0 `OK 3/3 pins hold`** after the swap; C) resolver guard exit 1 `FAIL opencode_binary_sha256: sha256 drift` |
| `exp/discriminate.py` | 0 | 6/6 cases: BASE discriminates, proposal satisfies |
| `python3 -B verifiers/check_substrate_pins.py --self-test` (proposal) | 0 | `0 failure(s) over 78 assertions` |
| `python3 -B verifiers/check_substrate_pins.py` (proposal, live, BASE baseline.json) | 2 | `FAIL opencode_launcher_binary_sha256: PIN_ABSENT` + 3 pre-existing failures — expected until the C1 re-pin records the 4th pin |
| `exp/proto_resolver.py /home/vgpnk/.local/bin/opencode` | 0 | artifact `…/opencode-ai/bin/opencode.exe`, sha `179ca421…` |
| `sha256sum /fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3` | 0 | `179ca421…` (matches the live artifact) |
| `grep -n tripwire verifiers/check_substrate_pins.py` (BASE) | 1 | no hits — the corpus doc's tripwire assertion does not exist |
| `npm config get cache` | 0 | `/home/vgpnk/.npm` (no `~/.npmrc`; `NPM_CONFIG_CACHE` unset) |
| `git apply --check RevPinsContract.patch` on a fresh BASE clone | 0 | "PATCH APPLIES CLEANLY to BASE"; after applying, `--self-test` → exit 0, `0 failure(s) over 78 assertions` |

No package was installed or upgraded this lane (no tool was missing); no pacman transaction was
run.

## 6. What I did NOT check

* I did not execute `~/.local/bin/opencode`, `npx`, `npm install`, or any wrapper — the
  lane contract forbids it and the resolution above is derived statically from the wrapper's text
  plus npm's own source. I did not observe an actual npm re-resolve/re-install.
* I did not verify the omp side's install shape beyond `~/.local/bin/omp` being a regular file
  (`readlink -f` = itself, 256 575 456 B) — I did not check whether omp has or will get a wrapper
  shape, and I did not re-derive the omp instruction surface (other lanes' slice).
* I did not run `verify_surfaces.py` or `verify_harness_claims.py` (not this item's instruments);
  F5 is a static constant-location check, not a behavioural one. I did not check how
  `verify_harness_claims.py`'s `OC_BIN` read behaves with the path absent.
* I did not check the opencode log/DB surfaces, the corpus index rows beyond the path-based
  mechanics of `verify_corpus_integrity.py` (I did not run that gate), or the round-47 C2/C3 claims.
* I did not test the guard on a non-x86 or musl host, nor with a non-default npm cache root
  (R-1 is reasoned from npm's source + the wrapper's text, not executed).
* I did not modify `verifiers/baseline.json`, the corpus doc, or `corpus/README.md` — the
  production edits are the integrator's; the patch and this report are advice.
* I did not check whether any *other* recorded key in `verifiers/baseline.json` would be newly
  discovered by the widened kind class beyond the four noted keys (I checked those four by hand;
  the block holds exactly `omp_binary_sha256`, `omp_binary_mtime`, `opencode_binary_sha256`,
  `omp_round21_note`, `omp_round44_note`, `command`, `round18_move`).
