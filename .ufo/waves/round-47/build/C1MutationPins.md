verdict: BASE --self-test kills 5/10 mutants; 5/10 survive; 0 inconclusive. All ten exact-byte restorations and their restored detectors pass.

# C1 baseline pin-verifier mutation probe

## Scope and axes

- BASE: `c61a973b2e02e1ded169703ddcb06466f4edd8bd`; target: `verifiers/check_substrate_pins.py`.
- **Freshness:** challenge complete digest, mtime, and declared-pin enforcement. **Operability:** execute the existing bounded `--self-test` on isolated files. **Calibration:** distinguish surviving coverage gaps from killed defects and from C1 integration acceptance.
- Unique scratch clone: `/fast/scratch/kotoba-r47/C1MutationPins/lane`. Each `probes/M01` through `probes/M10` has its own initially identical `verifiers/check_substrate_pins.py`; mutations never overlapped. Each mutant is one independent plausible defect, not a cumulative sequence. The original scratch target stayed pristine.
- Primary detector: the unmodified `--self-test` assertions. A survivor means this detector missed that defect, not that the contract permits it. A second, independent contract witness was run on the same pristine/mutated/restored files to demonstrate each mutation's effect; it does **not** retrospectively turn primary-detector survivors into kills.
- Python `3.14.8`, effective UID `1000`. No substrate binary was executed. No tool installation/update was needed.

## Commands and actual results

All commands ran in the isolated scratch clone, not the production checkout.

1. `git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/kotoba-r47/C1MutationPins/lane && git -C /fast/scratch/kotoba-r47/C1MutationPins/lane checkout -q --detach c61a973b2e02e1ded169703ddcb06466f4edd8bd` — exit **0**, no output.
2. `git rev-parse HEAD && sha256sum verifiers/check_substrate_pins.py && python3 --version` — exit **0**; output named the stated BASE, SHA-256 `bcfd5230eabb8b16343e11b21ec354d9860c65e4712187fc6650fc3f329495ce`, and Python `3.14.8`.
3. `python3 -B /fast/scratch/kotoba-r47/C1MutationPins/lane/verifiers/check_substrate_pins.py --self-test` — exit **0**, stdout exactly `0 failure(s) over 62 assertions`, empty stderr.
4. For each ID `M01`–`M10`, execute `python3 -B /fast/scratch/kotoba-r47/C1MutationPins/lane/probes/<ID>/verifiers/check_substrate_pins.py --self-test` on pristine, mutated, and restored bytes. All **20 pristine/restored runs** exited **0**, stdout exactly `0 failure(s) over 62 assertions`, empty stderr. Mutated exits/output summaries are below. This is 30 per-copy self-test processes plus the original-target baseline above.
5. At all three phases for every ID, execute `python3 -B /fast/scratch/kotoba-r47/C1MutationPins/lane/mutation_witness.py /fast/scratch/kotoba-r47/C1MutationPins/lane/probes/<ID>/verifiers/check_substrate_pins.py <ID>`. All **20 pristine/restored witnesses** exited **0**; all **10 mutated witnesses** exited **1**, meaning their actual gate exit differed from the independently stated contract expectation. Each witness invokes the selected verifier's `run_capture` with `--baseline <temporary JSON> --omp-binary <fixture> --opencode-binary <fixture-or-absent> --json`; gate exits are reported separately below.
6. Final `sha256sum` over the original scratch target and the ten restored probe files — exit **0**, empty stderr; all **11** hashes equal B below. The exact expanded argument list and all output are in the evidence artifact.

Exact command arrays, full stdout/stderr, fixture pins, mutation diffs, gate JSON, and before/mutated/restored hashes: `.ufo/waves/round-47/build/C1MutationPins.evidence.json`. Its embedded `witness.source` contains the complete small witness script for reproduction. IDs in command templates above are placeholders expanded to the ten explicit command arrays recorded there.

## Kill table

Every row started and ended with primary-detector exit **0** and `0 failure(s) over 62 assertions`. All locations below are at BASE, not shifted mutant line numbers. Last column is the independent witness's **gate** exit on pristine → mutated → restored; the witness process itself reports 0/1 as described above.

| ID | Small defect and BASE location | Mutated self-test exit | Actual self-test summary | Primary verdict | Witness gate exits |
|---|---|---:|---|---|---|
| M01 | `verifiers/check_substrate_pins.py:254` — Force mtime comparison verdict to PASS (skip mtime enforcement). | 1 | 4 failure(s) over 62 assertions | **KILLED** | 1 → 0 → 1 |
| M02 | `verifiers/check_substrate_pins.py:223` — Treat a nonexistent binary as PASS before hashing/stat checking. | 1 | 5 failure(s) over 62 assertions | **KILLED** | 2 → 0 → 2 |
| M03 | `verifiers/check_substrate_pins.py:173` — Case-fold measured_against pin names before discovery/checking. | 1 | 5 failure(s) over 62 assertions | **KILLED** | 2 → 0 → 2 |
| M04 | `verifiers/check_substrate_pins.py:182-184` — Discover extra keys only for registered substrates; ignore unknown pins. | 1 | 5 failure(s) over 62 assertions | **KILLED** | 2 → 0 → 2 |
| M05 | `verifiers/check_substrate_pins.py:237` — Compare only the first eight SHA-256 hex characters. | 0 | 0 failure(s) over 62 assertions | **SURVIVED** | 1 → 0 → 1 |
| M06 | `verifiers/check_substrate_pins.py:109` — Drop the SHA-256 syntax regex end anchor. | 0 | 0 failure(s) over 62 assertions | **SURVIVED** | 3 → 1 → 3 |
| M07 | `verifiers/check_substrate_pins.py:254` — Compare signed mtime delta instead of absolute delta. | 1 | 1 failure(s) over 62 assertions | **KILLED** | 1 → 0 → 1 |
| M08 | `verifiers/check_substrate_pins.py:182-184` — Skip discovery of extra *_binary_mtime keys. | 0 | 0 failure(s) over 62 assertions | **SURVIVED** | 1 → 0 → 1 |
| M09 | `verifiers/check_substrate_pins.py:134` — Stop SHA-256 streaming after the first 1 MiB chunk. | 0 | 0 failure(s) over 62 assertions | **SURVIVED** | 1 → 0 → 1 |
| M10 | `verifiers/check_substrate_pins.py:152-153` — Truncate fractional mtime digits past nine instead of rejecting the pin. | 0 | 0 failure(s) over 62 assertions | **SURVIVED** | 3 → 0 → 3 |

### Which existing arms killed defects

- **M01:** the mtime-drift exit/name assertions at `verifiers/check_substrate_pins.py:407-409`, the 1 ns drift assertion at `:414-419`, and the off-window microsecond assertion at `:486-488` failed. Four failures; no parser or fixture failure.
- **M02:** missing-binary exit/name at `:494-497`, dangling symlink at `:500-504`, unreadable-over-drift precedence at `:542-544`, and JSON missing-binary agreement at `:548-555` failed. Five failures.
- **M03:** the alias key's exit, precise UNSUPPORTED text, and 1/4 summary at `:443-452`, plus separator/kind case arms at `:453-456`, failed. Five failures. The independent witness uses a correctly valued case-variant replacement, which the mutant wrongly accepts with exit 0.
- **M04:** unknown substrate exit/name at `:438-442`, all-whitespace key at `:475-477`, and padded stray-substrate keys at `:478-482` failed. Five failures. The added prefix filter also suppresses these noncanonical extra keys.
- **M07:** the future pin 2 µs away at microsecond precision (`:486-488`) caught the signed-delta bug; its negative delta was wrongly accepted. One failure. The independent witness separately confirms the same defect for a future pin exactly 1 ns away.

The full failure messages are retained verbatim in the JSON artifact; no killed result rests on a crashing or already-red pristine test.

## Surviving counterexamples and arms C1 should add

These are baseline **self-test coverage findings**, not a recommendation to weaken pin syntax or discovery.

1. **M05 — full digest equality is not discriminated.** BASE compares all characters at `verifiers/check_substrate_pins.py:237`, but its drift fixture changes the entire value to zeros (`:404-406`). Witness fixture digest is `cf8bc79aef46e2fac5a99293fecfb03bb58add7fa60cee9a205eb2b1cdde458f`; pin `cf8bc79a0f46e2fac5a99293fecfb03bb58add7fa60cee9a205eb2b1cdde458f` shares eight leading characters but differs afterward. Pristine/restored: exit **1**, DRIFT. Mutant: exit **0**, PASS. **Add:** a 64-hex pin differing only in its last character, with a correct-digest positive control; assert exit 1, named DRIFT, and text/JSON agreement. A final-character difference also discriminates longer fixed-prefix shortcuts.
2. **M06 — malformed suffix loses BAD_PIN classification.** The syntax guard is `:109` / `:225-229`; present malformed-value fixtures cover wrong type and short length (`:524-528`), not valid-length prefixes with trailing junk. Witness `cf8bc79aef46e2fac5a99293fecfb03bb58add7fa60cee9a205eb2b1cdde458f:ignored` yields pristine/restored exit **3**, BAD_PIN, but mutant exit **1**, DRIFT. This survivor changes classification, not a false pass. **Add:** a valid digest plus a nonhex suffix; assert exit 3, BAD_PIN on the exact pin, and JSON `exit_code == 3`.
3. **M08 — an exit-only extra-pin positive arm can pass after silent shrink.** Discovery is `:175-184`. Existing extra `opencode_binary_mtime` fixture (`:483-485`) checks only exit 0 when the extra pin holds, so skipping the pin leaves it green. Witness adds that supported extra pin set to `2000-01-01T00:00:00.000000000+00:00` while the three mandatory pins hold. Pristine/restored: exit **1**, named DRIFT. Mutant: exit **0** and the extra pin is **absent from the report**. **Add:** assert the holding extra pin is explicitly PASS with four returned checks, then set only that pin stale and require exit 1 / named DRIFT in text and JSON.
4. **M09 — short, self-derived hash fixtures miss a one-chunk hash.** The streaming loop is `:130-135`; the mini fixture is only 93 bytes and derives its expected digest using the same `sha256_of` under test (`:360-362`). The independent witness uses **1,048,594 bytes**, a 1 MiB `A` prefix plus an 18-byte tail. Full digest is `42a5e8e9a757904075b418fc5750312deefc42daf734f54c9e71cd53be625ec9`; first-chunk digest is `4e29ad18ab9f42d7c233500771a39d7c852b200baf328fd00fbbe3fecea1eb56`. With both SHA pins set to the first-chunk digest, pristine/restored exit **1**, DRIFT; mutant exit **0**, PASS. **Add:** a >1 MiB fixture whose expected digest comes from an independent known digest or direct `hashlib.sha256` over the complete fixture; require its correct full pins to pass, then alter only a tail byte beyond 1 MiB and require DRIFT. Do not derive both sides through the same potentially defective helper.
5. **M10 — precision overflow has no rejecting arm.** BASE explicitly rejects >9 fractional digits at `:152-153`; existing mtime syntax fixtures at `:529-535` cover garbage, wrong type, and missing UTC offset, not overflow. Witness `2023-11-14T22:13:20.1234567890+00:00` yields pristine/restored exit **3**, BAD_PIN, but mutant exit **0**, PASS after truncation to the fixture's 9-digit mtime. **Add:** a 10-digit fractional pin with otherwise matching instant, requiring exit 3 and BAD_PIN; retain matching 9-digit and truncated-microsecond positive controls (`:372-373`, `:410-411`).

Keep the existing killed-mutant arms when C1 changes binary resolution/re-pins. The proposed additions above are not implemented or integrated by this leaf.

## Exact-byte restoration

B = SHA-256 `bcfd5230eabb8b16343e11b21ec354d9860c65e4712187fc6650fc3f329495ce`.

For **every** row: pristine hash = B; mutated hash differs; restoration hash = B. Restoration used the saved exact original UTF-8 source in a `finally` block before any restored detector ran. The final raw-byte `sha256sum` independently confirms B for every restored copy and the untouched original scratch target. Both detectors were run again after restoration; their results reverted to the pristine results.

| ID | Mutated SHA-256 | Pristine / restored SHA-256 |
|---|---|---|
| M01 | `70ba66ba4e8590e631964ce6959e206dbd23dac64f47c03367b7bed3e424ed45` | B / B |
| M02 | `6a4e270428e47a5b4e205441aef1e3b12e18217207d17389498e41a5df8091d4` | B / B |
| M03 | `6ad9cac05fd04fbe5f845da2ca86ca87b36111a00cf9bba3b7db7a02937b035f` | B / B |
| M04 | `74b98d23709246e92872436c3fc909b3b0520cbece425cffea0608823fe51e86` | B / B |
| M05 | `2fde9534bbc434f650d8dc39bb367b6abde7a6d0654693f23414eba8d7351b3a` | B / B |
| M06 | `24f073271699180536cc1a0471d76ab221756ec3e456e7fe76d94b81e5739973` | B / B |
| M07 | `073e3051958323b697265a73836ac7b37d1608aec5f1b11f5a3916a2af1fcbe7` | B / B |
| M08 | `60a8dc0564b758aa82bcf599ab116faea4ca39521d21741136cd855bd9735dd2` | B / B |
| M09 | `7e07b4250230520f4e6134b3e192ea29c4735271bb5930bf3da7df0e2c4b1b76` | B / B |
| M10 | `defb2df17fe07631eae386bef7b364045fc4a2bca56120cd22740e66502a61d0` | B / B |

Temporary fixture directories were scoped by `TemporaryDirectory` and removed on exit. The standalone scratch witness script is removed after its source is saved in the evidence JSON. No mutation patch is proposed for production.

## Not checked / boundaries

- Did not run live/default `check_substrate_pins.py` against host installs, re-hash the frozen omp/opencode snapshot, execute either binary or the network-fetching opencode wrapper, or assess the correctness of the new C1 binary resolver.
- Did not run `verify_surfaces.py`, other lane-wide gates, C2/C3 checks, or any production-checkout detector; this does not establish C1's planned 3/3 live-pin or 7/7 surface acceptance.
- Did not review or integrate sibling changes, alter production verifier/baseline bytes, change pin contracts, write SHONEN marks, or create commits.
- Only the ten named single-defect mutants and the recorded witnesses were exercised. Surviving mutants are coverage findings; there is no claim that these ten exhaust all defects.
- Production writes are limited to this requested report and its uniquely named evidence JSON. No tools installed or updated.
