verdict: BROKEN — the default pin is the current ELF, but stale-path/race checks and compound-key discovery admit false greens

## Axis summary
- **Freshness:** default pin currently matches the intended ELF; the guard can nevertheless attest stale bytes during a path swap, and every opencode reader uses a fixed cache path rather than deriving the wrapper's current resolution.
- **Operability:** default pin command exits 0; self-test is 62/62. A stable byte replacement before checking is correctly rejected.
- **Calibration:** `opencode_binary_resolved_sha256` is silently ignored; wrapper-vs-ELF is correct by default but not enforced when the path is overridden/re-pinned.

All repository citations below refer to `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.

## Findings

### MEDIUM — the cache-path digest is not an atomic attestation of the current pathname
**Exploit path:** a cache refresh atomically replaces the pinned pathname after `sha256_of()` has opened it. The checker hashes the old open file/FIFO stream and reports PASS even though the pathname names new bytes before the check returns. Separately, if the wrapper later resolves a different npx cache location while the old cache directory remains, the hardcoded readers can continue attesting the old file. The latter is conditional: I did not run npx or establish that this wrapper's refresh chooses a new cache path.

**Evidence:** `verifiers/check_substrate_pins.py:64-67` hardcodes `/home/vgpnk/.npm/_npx/e2094862b59aac7b/.../opencode.exe`; `:133-138` opens and hashes the path without checking file identity before/after; `:233-240` treats a matching digest as PASS. `verifiers/verify_harness_claims.py:56` and `verifiers/verify_surfaces.py:128-130` hardcode the same path. The observed wrapper is a dynamic resolver: `~/.local/bin/opencode:38-43` runs `npx --prefer-online` and then separately asks npx `--which` for the executable.

**Repro (scratch clone, temporary baseline):** I used a FIFO as `--opencode-binary`, pinned its stream bytes (`b8e5e816…`), started the guard, then after its reader opened atomically replaced the FIFO pathname with a regular file containing different bytes (`a918fa9a…`) and wrote the pinned bytes to the already-open FIFO. `python3 verifiers/check_substrate_pins.py --baseline /fast/scratch/kotoba-r47/w2/W2PinsSentinel/kotoba-shokunin/.w2-pins-race-1zp0xepf/baseline.json --opencode-binary /fast/scratch/kotoba-r47/w2/W2PinsSentinel/kotoba-shokunin/.w2-pins-race-1zp0xepf/opencode-path --json` returned **exit 0**, PASS 3/3; after exit, the path SHA-256 was `a918fa9a187ee5df711c0387b553306038e7228aea26005a14b2cad94a3ac685`, not the pinned `b8e5e816069efb45cff322928a930e5bde2d43955859fd599b058b4fd32df54b`. This is a deterministic same-path replacement repro, not a claim that npx itself was run or observed to perform this exact rename.

**Impact:** a green result can describe bytes no longer reachable through the pinned path; the other two default opencode readers also do not prove that the dynamically selected executable is the file being checked. The verifier's prose at `verifiers/check_substrate_pins.py:40-45` asserts that this fixed file is what the wrapper executes, but it does not resolve or bind that relationship at check time.

**Smallest remediation:** hash a stable, content-addressed executable artifact selected by the same resolution used for analysis; at minimum open once, compare `fstat()` identity with the current path before/after hashing, and fail on replacement. Treat any claim that the fixed cache path is the wrapper's current target as unverified until the paths are resolved together.

### LOW — the guard accepts a wrapper as the pinned binary if a caller re-pins it
**Evidence:** the live default at `verifiers/check_substrate_pins.py:64-67` is the ELF path, not `~/.local/bin/opencode`; the baseline note at `verifiers/baseline.json:12` names the resolved ELF. Host inspection (read-only, no execution) found the wrapper is a 1,460-byte Bash script, SHA-256 `b240efa9d6020bdc513bbf48e46b6d312493d2c408f7d070555e993feea0a89b`, while the pinned target is an 186,013,824-byte x86-64 ELF, SHA-256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`. Thus the **current default is not vacuous**.

However, `--opencode-binary` is accepted at `verifiers/check_substrate_pins.py:308-309`, and SHA mode only hashes arbitrary bytes (`:227-240`). With a scratch baseline pinned to the wrapper's hash, `python3 verifiers/check_substrate_pins.py --baseline verifiers/.w2-pins-compound.json --opencode-binary /home/vgpnk/.local/bin/opencode --json` returned **exit 0**, PASS 3/3. The guard cannot distinguish a repinned wrapper from the payload; a static wrapper digest can stay green while its npx-resolved payload changes.

**Smallest remediation:** keep production baselines tied to the canonical resolved ELF and reject/restrict overrides in non-fixture runs, or record and validate the resolved payload identity separately. Do not claim this is a current default-path defect.

### MEDIUM — compound-kind pin keys bypass discovery
**Exploit path:** add a key such as `opencode_binary_resolved_sha256` to `measured_against` with a wrong/stale digest. `DISCOVER_RE` allows only alphanumerics in `kind` (`verifiers/check_substrate_pins.py:80-81`), so its underscore-containing kind is not discovered; the expected-pin loop never examines it (`:178-187`).

**Repro (scratch clone):** `verifiers/.w2-pins-compound-default.json` used the default ELF's correct `opencode_binary_sha256` plus `opencode_binary_resolved_sha256` set to 64 zeroes. `python3 verifiers/check_substrate_pins.py --baseline verifiers/.w2-pins-compound-default.json --json` returned **exit 0**, PASS 3/3; output omitted the wrong compound pin. This isolates the discovery hole from wrapper-path selection. Separately, `verifiers/.w2-pins-compound.json` used the wrapper hash and the v1 fixture's resolved hash; after changing the fixture v1→v2 (`cbbdb496…`→`7038b206…`), rerunning with `--opencode-binary /home/vgpnk/.local/bin/opencode` also returned **exit 0** and omitted the compound key.

**Impact:** a future resolved-binary pin can look present in the baseline while no gate checks it; changing/removing its target cannot make this guard fail.

**Smallest remediation:** let the discovered kind grammar include underscore-separated tokens, then classify unsupported kinds as `UNSUPPORTED` (exit 2), or explicitly reject any otherwise pin-like key that the guard cannot interpret.

## Commands and checks exercised
- `python3 verifiers/check_substrate_pins.py --json` — **exit 0**, 3/3 PASS; observed omp SHA `fdbc8136…`, mtime delta 0 ns, opencode ELF SHA `179ca421…`.
- `python3 verifiers/check_substrate_pins.py --self-test` — **exit 0**, `0 failure(s) over 62 assertions`.
- Temp payload pinned v1, unchanged: same checker with `--baseline verifiers/.w2-pins-drift.json --opencode-binary verifiers/.w2-pins-payload-v1.txt --json` — **exit 0**, 3/3 PASS. After replacing the fixture bytes with v2, same command — **exit 1**, `opencode_binary_sha256: DRIFT` (expected `cbbdb496…`, observed `7038b206…`). This confirms a stable pre-check replacement is detected.
- Default-path compound-key fixture above — **exit 0**, PASS 3/3 with the default ELF digest correct and `opencode_binary_resolved_sha256` set to all zeroes; no row for that key.
- Wrapper/compound fixture — **exit 0** before and after fixture refresh; only the three canonical pins were reported.

## Not checked
I did not execute `~/.local/bin/opencode`, npx, `npx --prefer-online`, or either binary; did not trigger a real cache refresh/network access; did not run `verify_surfaces.py` or `verify_harness_claims.py`; and did not review the other round-47 axes. The atomic rename and payload-refresh tests used scratch-clone temporary baselines/fixtures only. No tools were installed or updated.
