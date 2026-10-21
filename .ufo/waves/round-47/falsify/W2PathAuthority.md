verdict: PARTIAL — the opencode path authority itself HOLDS (all three constants name one byte-identical file, and that file is provably the ELF the `~/.local/bin/opencode` npx wrapper execs), but one of the three constant sites is fail-open on a missing binary and the lane sweep still carries three unexpired present-tense `~/.opencode/bin` claims plus one corpus file that now names the *current* rule set wrongly.

# W2PathAuthority — falsification of the opencode default path at 7ad7fad

Lane: `KotobaR47-2.W2PathAuthority-2` (leaf reviewer). Attacked: the opencode default-path authority claim in
`verifiers/verify_surfaces.py`, `verifiers/check_substrate_pins.py`, `verifiers/verify_harness_claims.py`, and every
remaining `~/.opencode/bin` claim in `verifiers/`, `SKILL.md`, `corpus/`, `README.md`.

Tip under attack: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`).
Scratch clone (canonical layout, detached at the tip): `/fast/scratch/kotoba-r47/w2/W2PathAuthority/kotoba-shokunin`.
No file in `/home/vgpnk/Projects/shokunin/kotoba-shokunin` was modified; no git mutating command was run there
(`git rev-parse HEAD` → `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`, read-only). No subagent dispatched.

---

## 0. Verdict summary per axis

| axis | verdict | one line |
|---|---|---|
| freshness | **HOLDS** | the pinned ELF is the live wrapper-resolved ELF (sha256 `179ca421…` at both the host path and the frozen snapshot), the frozen dump is byte-reproducible from it, and the registry's `latest` for `opencode-ai` is still `1.19.3` — no channel drift since the landing |
| operability | **HOLDS with one defect (F1)** | `verify_surfaces.py` and `check_substrate_pins.py` fail closed (exit 2) on a missing opencode binary; `verify_harness_claims.py` does **not** — it silently drops the datum and reports DRIFT (F1) |
| calibration | **PARTIAL** | 3 unexpired present-tense `~/.opencode/bin` claims (F2) and 1 corpus file whose "current rule set" sentence is now false (F4) survive at the tip; the identity triple used by the round-8 record is not a discriminator (F3) |

---

## 1. The three constants name the same file — CONFIRMED (attack failed to break it)

Programmatic comparison at the tip (not a hand-read):

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 - <<'EOF'   # exit 0
import re,pathlib
vs=pathlib.Path('verifiers/verify_surfaces.py').read_text()
pins=pathlib.Path('verifiers/check_substrate_pins.py').read_text()
claims=pathlib.Path('verifiers/verify_harness_claims.py').read_text()
a=re.search(r'"opencode":\s*"([^"]+)"',vs).group(1)
b=re.search(r'"opencode":\s*"([^"]+)"',pins).group(1)
c="/home/vgpnk/"+re.search(r'OC_BIN = HOME / "([^"]+)"',claims).group(1)
print(a); print(b); print(c); print("all three byte-identical:", a==b==c)
EOF
```

Output:

```
/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
all three byte-identical: True
```

Sites, cited at `7ad7fad`:

- `verifiers/verify_surfaces.py:130` — `DEFAULT_BINARIES["opencode"]` (absolute string)
- `verifiers/check_substrate_pins.py:66` — `BINARIES["opencode"]` (absolute string)
- `verifiers/verify_harness_claims.py:56` — `OC_BIN = HOME / ".npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe"` (HOME-joined; identical absolute path)

The cross-reference claim in `verifiers/check_substrate_pins.py:41-45` ("same values as verify_harness_claims.py
OMP_BIN/OC_BIN and verify_surfaces.py DEFAULT_BINARIES") is **true at the tip** — verified by the equality run above,
not by reading the docstring.

**No fourth constant exists.** Sweep for any other opencode *binary* path literal in `verifiers/` (py/sh/json, caches
excluded): only the three above, plus CLI defaults derived from them
(`verify_surfaces.py:1125-1127`, `check_substrate_pins.py:309`, `verify_harness_claims.py:632`).
`verifiers/verify_harness_independent.py:126-127` holds an opencode **log/config** path, not a binary path — out of
this claim's scope, listed in §5.

---

## 2. Is the constant the ELF the wrapper actually execs? — CONFIRMED (wrapper read, never run)

Per the contract I did **not** execute `~/.local/bin/opencode` (its first npx call is `--prefer-online`, which can
swap the bytes) and did not run `npx`. I read the wrapper and followed the resolution by hand.

### 2.1 The wrapper (`/home/vgpnk/.local/bin/opencode`, 1460 B, read-only)

```
package="opencode-ai"; command="opencode"
"$node_bin" "$npx_bin" --yes --prefer-online --package "$package" -- true
package_bin_path=$("$node_bin" "$npx_bin" --yes --package "$package" -- which "$package" 2>/dev/null)
exec_package_bin "$package_bin_path" "$@"
# exec_package_bin: PATH="$node_root/bin:$PATH" exec "$package_bin_path" "$@"
```

So the wrapper execs exactly the path `npx … -- which opencode` prints — i.e. npx's own
`node_modules/.bin/opencode` shim, not a global binary.

### 2.2 Following `node_modules/.bin/opencode`

```
$ ls -la /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/.bin/
lrwxrwxrwx 1 vgpnk vgpnk 31 Oct 20 18:33 opencode -> ../opencode-ai/bin/opencode.exe
$ readlink -f /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/.bin/opencode
/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
```

The shim resolves to **the exact file the three constants name**. `package.json` of `opencode-ai` declares
`"bin": {"opencode": "./bin/opencode.exe"}`, `version` `1.19.3`.

### 2.3 It is the ELF, and it is the pinned bytes

```
$ file  …/node_modules/opencode-ai/bin/opencode.exe
ELF 64-bit LSB executable, x86-64, dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, … not stripped
$ sha256sum …/node_modules/opencode-ai/bin/opencode.exe
179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9
$ sha256sum /fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3
179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9      # == frozen SHA256SUMS line
$ sha256sum -c SHA256SUMS   # in /fast/scratch/kotoba-r47/shared → exit 0
bin/omp-18.12.5: OK
bin/opencode-1.19.3: OK
omp-18.12.5.strings: OK
opencode-1.19.3.strings: OK
```

`verifiers/baseline.json:9` pins `opencode_binary_sha256 = 179ca421…` → the pin, the live file and the frozen snapshot
are one artifact.

### 2.4 The hardcoded npx cache directory is *stable*, not accidental

`~/.npm/_npx/<hash>` is derived by libnpmexec from the package spec alone
(`/home/vgpnk/.local/share/mise/installs/node/26.12.0/lib/node_modules/npm/node_modules/libnpmexec/lib/index.js:250-260`:
`sha512(sorted(packages).join("\n")).slice(0,16)`). Verified:

```
$ python3 -c "import hashlib;print(hashlib.sha512(b'opencode-ai').hexdigest()[:16])"
e2094862b59aac7b
```

The directory in the constant is exactly `sha512("opencode-ai")[:16]` → the path does **not** depend on node/npm
version and will not move on a `mise use -g node@latest` bump. This is the strongest reason the constant is safe to
hard-code. Counterexample checked and *not* present: only one of the nine `~/.npm/_npx/*` dirs contains `opencode-ai`
(`ls -d ~/.npm/_npx/*/node_modules/opencode-ai` → 1 hit), and `which -a opencode` → only the wrapper — no global
`opencode` could shadow the npx shim.

### 2.5 Lineage of the bytes (self-report + absence of the old anchors)

```
$ grep -c 'var n="1.19.3"' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings   → 1
$ grep -c '2\.0\.26'      …/opencode-1.19.3.strings                                 → 0
```

Matches `corpus/knowledge/instruction-surface-census-round13.md:214-219` (§ B′ "the dump self-reports `var n="1.19.3"`
and contains no `2.0.26`").

### 2.6 The old path is really gone

```
$ test -e /home/vgpnk/.opencode/bin/opencode && echo EXISTS || echo GONE   → GONE
$ ls -la /home/vgpnk/.opencode/                                            → empty dir, mtime Oct 20 08:14
```

The record "`~/.opencode/bin/opencode` (v2.0.26, d9123b9b…) removed 2026-10-20"
(`verifiers/baseline.json:12`, census § B′) is consistent with the host.

---

## 3. Counting commands re-run at the tip (default resolution)

```
$ cd /fast/scratch/kotoba-r47/w2/W2PathAuthority/kotoba-shokunin
$ python3 verifiers/verify_surfaces.py                # exit 0, 7/7 PASS, 4.97 s
PASS surfaces.literal_present: 42 loader-kind entries verified against the dumps
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory

$ python3 verifiers/check_substrate_pins.py            # exit 0, OK 3/3 pins hold
PASS omp_binary_sha256: fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e
PASS omp_binary_mtime: delta 0 ns (tolerance 0 ns)
PASS opencode_binary_sha256: 179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9
```

Both re-derive at **default resolution**, i.e. they read the host path named by the constant — not a fixture — which is
the point of the claim. The opencode class set at the tip is 9 governed ids
(`verifiers/surfaces-baseline.json` `classes[]`: `opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md`,
`opencode:config/AGENTS.md`, `opencode:claude-home/CLAUDE.md`, `opencode:config/instructions`,
`opencode:config/instructions-remote`, `opencode:read-hook/instructions`,
`opencode:instruction-context/AGENTS.md`) versus 4 governed + 1 excluded at BASE — consistent with the ledger in
`corpus/knowledge/instruction-surface-census-round13.md:310-321`.

Dump provenance re-derived (the C1 measurement substrate):

```
$ strings -n 4 /fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3 | sha256sum
f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3   # == SHA256SUMS line
$ strings -n 4 /fast/scratch/kotoba-r47/shared/bin/omp-18.12.5    | sha256sum
33df0aeffc4565967bc1a3b42621f8eade0e6e4c2ae8733319fcd484902fb301   # == SHA256SUMS line
```

Registry freshness of the version claim (read-only query, no install):

```
$ npm view opencode-ai version   # exit 0 → version = '1.19.3'   (dist-tags.latest == 1.19.3)
```

So the pinned 1.19.3 is still the registry's `latest` today — no newer opencode has appeared under the wrapper's
`--package opencode-ai` spec.

---

## 4. Findings

### F1 — `verify_harness_claims.py` opencode binary is the one substrate read that is **not** fail-closed (MEDIUM, operability/calibration)

`verifiers/verify_harness_claims.py:477-479`:

```python
    builtin = 0
    if binary.is_file():
        builtin = 1 if b"customize-opencode" in binary.read_bytes() else 0
```

A missing/unreadable `OC_BIN` yields `builtin = 0` — **no `Inconclusive`, no exit 2** — while the file's own docstring
(`verifiers/verify_harness_claims.py:29-30`) promises: *"2 the environment is unreadable (missing binary / db / log)"*.

Repro (scratch clone, tip):

```
$ python3 verifiers/verify_harness_claims.py --oc-bin /nonexistent/opencode.exe   # exit 1  (expected 2)
… oc.roots.names_plus_builtin: observed=10 expected=7      # builtin silently 0 instead of 1
$ python3 verifiers/verify_harness_claims.py --omp-bin /nonexistent/omp             # exit 2  ← asymmetry
INCONCLUSIVE: omp binary not found: /nonexistent/omp
$ python3 verifiers/verify_harness_claims.py --oc-log /nonexistent/x.log            # exit 2  ← asymmetry
INCONCLUSIVE: opencode log not found: /nonexistent/x.log
```

With the **correct** constant the same run reports `oc.roots.names_plus_builtin: observed=11` (10 live root names + the
`customize-opencode` builtin, which I confirmed is present in the ELF: `grep -c customize-opencode <ELF>` → 2).

Why this is the load-bearing defect for *this* round: round 47 moved `OC_BIN` from a path that no longer exists to one
that does. Had the new path been wrong (a typo, a different npx hash, a package spec change), the verifier would have
reported a **value drift** (`10` instead of `11`) rather than the documented *environment unreadable* (exit 2) — the
one place in the file where a substrate mis-path is diagnosed at the wrong tier. The two sibling verifiers get this
right:

```
$ python3 verifiers/verify_surfaces.py --opencode-binary /nonexistent/opencode.exe   # exit 2
ERROR opencode binary not found: /nonexistent/opencode.exe
$ python3 verifiers/check_substrate_pins.py --opencode-binary /nonexistent/opencode.exe   # exit 2
ERROR UNREADABLE opencode_binary_sha256: [Errno 2] No such file or directory: '/nonexistent/opencode.exe'
UNREADABLE 1/3 pins failed: opencode_binary_sha256
```

Pre-existing defect (the guard has never been fail-closed for the opencode binary) — not introduced by round 47 — but
it is the weakest link in the very claim this lane attacks. Cheap fix consistent with the file's own contract: raise
`Inconclusive` when `not binary.is_file()` (the omp and log sites already do).

### F2 — Three **unexpired present-tense** `~/.opencode/bin` claims remain in `corpus/` (MEDIUM, calibration)

Full sweep at the tip (`git grep -n "\.opencode/bin" 7ad7fad -- verifiers SKILL.md corpus README.md`, caches excluded)
→ 10 hits; classified:

| site at 7ad7fad | tense | status |
|---|---|---|
| `corpus/knowledge/claude-md-surface.md:9` | **present** | **UNEXPIRED** — F2a |
| `corpus/knowledge/opencode-offer-trace-round8.md:6` | **present** ("Host: this workstation") | **UNEXPIRED** — F2b |
| `corpus/knowledge/skill-activation-telemetry.md:21` | **present** | **UNEXPIRED** — F2c |
| `corpus/knowledge/opencode-extraction-round14.md:98` | past, inside a dated section ("Falsifiers, run on the landed tree (2026-09-28)") | historical — acceptable, but see F4 for the same file's header |
| `corpus/knowledge/opencode-offer-trace-round8.md:130` | past, repro recipe inside the round-8 record | historical — acceptable |
| `corpus/knowledge/instruction-surface-census-round13.md:218` | past, explicit ("`~/.opencode/bin`, removed 2026-10-20") | correct |
| `verifiers/verify_surfaces.py:355` | past, code comment ("… is gone; the host now runs npm `opencode-ai` 1.19.3") | correct |
| `verifiers/baseline.json:12` | past, `round47_note` | correct |
| `SKILL.md:434` | past ("the round-8/18 `~/.opencode/bin` install is gone") | correct |
| `README.md` | — | no hit |

**F2a — `corpus/knowledge/claude-md-surface.md:9`.**
"**Loader exists in both harnesses.** `grep -o 'CLAUDE.md'` on the binaries: `~/.opencode/bin/opencode` → 9
occurrences, `~/.local/bin/omp` → 17;" — the named binary no longer exists (F2 §2.6), so the stated sweep cannot be
re-run today, and the evidence it offers is evidence the census itself **rejected**:
`corpus/knowledge/instruction-surface-census-round13.md:337-341` records the adjudication that "a reference count cannot
separate a loader from prompt text" and that the lane using the 9/17 count reached the *opposite* conclusion from the
lane that read the code. The corpus file keeps the rejected count and the dead path with no erratum. The index row
`corpus/README.md:18` still advertises the basis as "loader strings in binaries" — a live-sounding basis whose only
cited substrate is gone. (Substantively the *loader* claim survives; it is now carried by the census § B′ code shapes,
which the file does not point to.)

**F2b — `corpus/knowledge/opencode-offer-trace-round8.md:6`.**
"Host: this workstation, opencode `~/.opencode/bin/opencode` (ELF, 185030784 B, mtime 2026-09-14, BuildID
`c30f169b1bef81fa57467cd091ba53aab5235468`)" — present-tense host identity that is false today: the host's opencode is
186013824 B at `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`. The corpus index
row (`corpus/README.md:31`, "opencode offer trace (round-8)") still lists "opencode ELF" as its basis. See F3: the
BuildID it offers as an identity token does **not** discriminate the two binaries.

**F2c — `corpus/knowledge/skill-activation-telemetry.md:21`.**
"Not found in `~/.opencode/bin/opencode` or `pi_natives` — the prompt is omp's." — a present-tense **negative** claim
whose sweep names a removed binary; under the lane's own Q14 ("a negative claim carries its sweep") the sweep is
unrunnable as written. The substance survives on the current substrate, verified against the frozen 1.19.3 dump:

```
$ grep -c '<skills>'          /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings   → 0
$ grep -c '<available_skills>' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings   → 2
```

so the claim is true but its *sweep* needs re-pointing (one command, both counts reproducible).

None of F2a-c is a "the pin is wrong" defect: the landed C1 records (`verifiers/baseline.json:12`, census § B′,
`SKILL.md:431-434`) are correct and consistent with the host. These are the corpus's own hygiene debt on the C3 axis,
where the lane has explicitly committed to no present-tense path claims.

### F3 — BuildID is not a discriminator for this artifact family (LOW, calibration)

`readelf -n` on the **current** ELF:

```
$ readelf -n /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe
  Build ID: c30f169b1bef81fa57467cd091ba53aab5235468
```

— byte-identical to the BuildID the round-8 record (`corpus/knowledge/opencode-offer-trace-round8.md:6-8`) attributes to
the *removed* 185030784 B `~/.opencode/bin/opencode` (a 1.18.x-era build). The binary is a Bun single-file executable
(`strings … | grep -m1 'Bun v'` → `Bun v1.3.14 (Linux x64 baseline)`), and the GNU build-id is evidently a property of
the bun runtime image, not of the opencode build. Consequence: the round-8 doc's identity triple (path + size + mtime +
BuildID) would not have revealed the channel swap to a reader who checked only the BuildID; only sha256 does — which is
exactly what `corpus/SOURCES.md:28` (S015) teaches ("A substrate pin is the binary's sha256, not its version string or
path"). F2b's record should be expired with an explicit "BuildID collides; use sha256" note rather than left to be
re-cited as an identity token.

### F4 — `corpus/knowledge/opencode-extraction-round14.md:4-12` now names the *current* rule set wrongly (MEDIUM, calibration)

The file's round-18 errata header says:

> "The current rule set — OC-1…OC-6 over `ConfigInstructionPlugin.projectSource`, `ReadTool.Plugin`, the API-managed
> instruction entries and an env-gate — is the round-18 re-derivation recorded in
> `instruction-surface-census-round13.md` § B (errata block) and `verifiers/verify_surfaces.py`."

At the tip that sentence is **false**: the live rule set is the round-14 anchor set (OC-1, OC-2, OC-3a, OC-3b, OC-4,
OC-5, OC-6), § B is now explicitly the *historical* v2.0.26 model (`census:180` "are superseded-revision claims
preserved as historical, not live classes"), and the verifier contains none of the v2.0.26 anchors as live rules:

```
$ grep -n "ConfigInstructionPlugin|ReadTool.Plugin|SessionInstructions" verifiers/verify_surfaces.py
358:# 1.19.3 dump the v2.0.26 anchors `ConfigInstructionPlugin`, `ReadTool.Plugin`,     ← comment only
359:# `SessionInstructions`, `session.instructions.entry.put`, `j5(r.config,…)` and
```

The corpus index row for the same file (`corpus/README.md:39`) is also stale on the live numbers: it says "opencode's 5
instruction classes are now reproduced … by six named code-shape rules (OC-1…OC-6)", while the live gate reports
**9/9 classes from 7/7 rules** and the round-14 doc's own body says "seven named, fail-closed rules"
(`opencode-extraction-round14.md:16-18`).

Provenance check (so this is not charged to round 47): `git diff c61a973… 7ad7fad -- corpus/README.md` = 3 insertions,
1 deletion, and line 39 is byte-identical at BASE; the BASE baseline carried 4 governed opencode ids + 1 excluded, so
the "5 classes / six rules" wording was already stale at BASE (round 18) and round 47 both changed the live set *and*
left the row untouched. It is therefore **pre-existing staleness that round 47 widened** (live set moved 4+1 → 9 while
the index row stayed at 5). The corpus-integrity gate checks index *counts* and pointer liveness, not basis staleness,
so nothing flags it.

### F5 — No gate cross-checks the three constants against each other (LOW, residual risk, not a defect at the tip)

`grep -rn "DEFAULT_BINARIES|BINARIES\[|OC_BIN|OMP_BIN" verifiers/*.py` shows three independent literals and no
comparator. Today they agree (§1); a future one-file edit would leave the other two stale. The failure mode is loud,
not silent — each consumer fails closed (`verify_surfaces` exit 2 "binary not found", `check_substrate_pins` exit 2
UNREADABLE) — so this is a maintenance hazard rather than a live defect. The exception is F1: the *third* consumer does
not fail closed.

### F6 — The pinned path's *content* is CPU-selected at install time (LOW, residual risk)

`node_modules/opencode-ai/postinstall.mjs` selects a platform package by `os.platform()/os.arch()` **and AVX2 support**
(`supportsAvx2()`, `isMusl()`) and hard-links that binary to `bin/opencode.exe`
(`stat` → inode 43795736, link count 2, shared with `opencode-linux-x64/bin/opencode`). On this host all three
installed variants (`opencode-ai/bin/opencode.exe`, `opencode-linux-x64/bin/opencode`,
`opencode-linux-x64-baseline/bin/opencode`) hash to the same `179ca421…`, so the pin is variant-independent **here**.
On a non-AVX2 or musl host the same path could hold different bytes → the sha pin would report DRIFT (exit 1), i.e. loud,
not silent. Recorded as residual risk, not a finding against the round.

---

## 5. What I did NOT check

- **Did not execute** `~/.local/bin/opencode` and did **not** invoke `npx` (contract: `--prefer-online` can swap the
  binary; I resolved the wrapper's target statically from its source + the npx cache layout). Therefore the wrapper's
  *runtime* behaviour (its `which opencode` PATH ordering, its `ensure_bin_runtime` shebang probe on an ELF, its
  `exec` of the shim) is read, not executed. No claim here depends on executing it.
- Did not run any opencode session / TUI / server, so the round-47 lineage claim was checked at the **bytes + strings**
  level only (self-report `var n="1.19.3"`, absence of `2.0.26`, anchor counts) — not at runtime behaviour. Whether
  either opencode instruction subsystem actually fires on 1.19.3 is explicitly not decided by strings (census
  "Honest ceiling"), and I did not try to decide it.
- Did not audit the census's per-anchor counts (the ledger's 12 rows) or the OC-3b/OC-4 tightenings — other lanes own
  that; my §3 run confirms only the aggregate 9/9-from-7/7 parity.
- Did not audit the omp side of the pin (sha/mtime) beyond re-running the gate; the omp constant was not in my scope.
- Did not sweep the corpus for present-tense claims *other* than the `~/.opencode/bin` class (F2 is the requested
  sweep; broader present-tense hunting across `corpus/knowledge/` is not covered).
- Did not touch `verifiers/verify_harness_independent.py`'s `DEFAULT_OC_LOG` / `DEFAULT_OC_CONFIG`
  (`verifiers/verify_harness_independent.py:126-127`) — opencode **log/config** paths, not the binary path; they were
  checked for *existence* only as a side note and are outside the "three constants" claim.
- Did not check `LOG.md` / `SCORECARD.md` / `PROVINCE.md` / `plans/round-47.md` for path claims beyond reading the
  round-47 landing entry (`LOG.md:2317-2330`) and the plan's line 13; both are consistent with the host (LOG's
  "Not claimed: `verifiers/verify_harness_claims.py` 21/28 before and after (same seven DRIFT ids)" matches my run:
  21/28, exit 1, same seven drift ids — `omp.db.rows`, `omp.offered.skills`, `omp.cache.misses`,
  `omp.catalogue.total`, `omp.catalogue.missing_names`, `omp.cache.verified_skills`, `oc.roots.names_plus_builtin`).
- Did not commit or mutate anything in the scratch clone (mutations were CLI-override only), so no commit-state
  verification was needed for my own artifacts.

---

## 6. Recommended repairs (small, in-lane)

1. `verifiers/verify_harness_claims.py:477-479` — raise `Inconclusive` when the opencode binary is missing, matching
   the omp/log sites and the file's own exit-code contract (F1).
2. Add a one-line erratum to `corpus/knowledge/claude-md-surface.md`, `opencode-offer-trace-round8.md` and
   `skill-activation-telemetry.md` marking the `~/.opencode/bin` substrate as removed on 2026-10-20 and pointing at
   `census § B′` / the npx ELF (F2a-c), and a note that BuildID collides across opencode builds (F3).
3. `corpus/knowledge/opencode-extraction-round14.md:4-12` — append a round-47 erratum that the current rule set is the
   round-14 anchor set again (§ B′), not the round-18 one; and refresh `corpus/README.md:39`'s "5 classes / six rules"
   to the live 9 classes / 7 rules (F4).

## 7. Commands run (all in the scratch clone or read-only on the host)

```
git clone --no-hardlinks … && git checkout --detach 7ad7fad…        # exit 0
python3 verifiers/verify_surfaces.py                                 # exit 0 (7/7)
python3 verifiers/check_substrate_pins.py                            # exit 0 (3/3)
python3 verifiers/verify_harness_claims.py                           # exit 1 (21/28, 7 DRIFT ids; host-skill drift, "not claimed" in LOG.md)
python3 verifiers/verify_surfaces.py --opencode-binary /nonexistent/opencode.exe        # exit 2
python3 verifiers/check_substrate_pins.py --opencode-binary /nonexistent/opencode.exe  # exit 2
python3 verifiers/verify_harness_claims.py --oc-bin /nonexistent/opencode.exe           # exit 1  ← F1
python3 verifiers/verify_harness_claims.py --omp-bin /nonexistent/omp                    # exit 2
python3 verifiers/verify_harness_claims.py --oc-log /nonexistent/x.log                   # exit 2
sha256sum -c SHA256SUMS                       (in /fast/scratch/kotoba-r47/shared)        # exit 0
strings -n 4 <frozen bin> | sha256sum          (×2, both match SHA256SUMS)               # exit 0
readelf -n <ELF> ; file <ELF> ; stat <ELF> ; ls -la ~/.npm/_npx/*/node_modules/.bin/     # exit 0
npm view opencode-ai version                     # exit 0 → 1.19.3
git grep -n "\.opencode/bin" 7ad7fad -- verifiers SKILL.md corpus README.md             # exit 0
```

No tool was installed or upgraded by this lane (no package manager transaction; no `uv tool`/`cargo`/`npm -g` install
was needed — every check used the host's existing python3 / coreutils / binutils / node).

## 8. Artifacts

- This report: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/falsify/W2PathAuthority.md`
- Scratch clone used for the runs: `/fast/scratch/kotoba-r47/w2/W2PathAuthority/kotoba-shokunin` (detached at `7ad7fad`,
  unmodified — all mutations were CLI overrides).
