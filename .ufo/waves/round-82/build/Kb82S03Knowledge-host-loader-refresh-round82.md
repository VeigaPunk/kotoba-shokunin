source: S251 — kotoba own work, round-82 host substrate refresh — `.ufo/waves/round-82/build/Kb82S03Knowledge-current-bytes.txt`, exact stdout of `stat`, `file`, and `sha256sum` on `/home/vgpnk/.local/bin/omp`; located quote "ELF 64-bit LSB executable". S251 is reserved in `plans/round-82.md`; this draft does not assert its registry row has landed or that loader re-derivation has completed.
verified-at: 2026-10-30 — byte identity and file type only; named intake base `47dbe8781657de563ff867caca6244d28e3db504`.
recheck: on-release or any executable path/hash/mtime change — resolve the executable again, record bytes, independently rederive loader registrations and instruction literals, compare the historical class set, and only then update pins; never re-pin solely to silence a red gate.
ground: `verifiers/check_substrate_pins.py:9-36` defines the exit ladder and hash-without-exec policy; `verifiers/verify_surfaces.py:58-69` defines the extraction ceiling; `plans/round-82.md:7-19` freezes C1/C2 and their separate predicates.

# Host loader refresh (round 82)

## Current-byte evidence

The installed `/home/vgpnk/.local/bin/omp` is now an ELF, not the historical crash-restart shell wrapper. On the access date, the independent S251-supporting observation recorded:

| Identity field | Observed value |
|---|---|
| Path | `/home/vgpnk/.local/bin/omp` |
| SHA-256 | `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f` |
| Size | 276244656 bytes |
| mtime | `2026-10-29T23:19:46.168359786-03:00` |
| Type | ELF 64-bit LSB executable, x86-64 |

The round-82 plan identifies this installation as omp 18.14.0. This seat did not run `omp --version`; the version is plan provenance, not this observation's execution evidence. The read-only byte observation executed no harness and establishes no runtime behaviour.

The opened before receipt `.ufo/waves/round-82/receipts/before-pins.txt` names intake revision `47dbe8781657de563ff867caca6244d28e3db504`: both omp pins are `UNREADABLE` because `/home/vgpnk/.local/bin/omp.real` is missing; the opencode SHA pin passes; command-owned `exit=2`, 1 PASS / 2 UNREADABLE. This is inherited before evidence, not a newly rerun gate or a production after-value. Round 51's 18.12.6 bytes and round 72's wrapper-to-`omp.real` path are historical context, not the latest host identity.

## Refresh action table

| Observation | Action | Evidence required before declaring success |
|---|---|---|
| The command path may be a wrapper, symlink, or ELF | Inspect the command and resolve the actual executable it invokes. Hash/stat that executable; do not assume the filename `omp.real` remains valid and do not pin only a wrapper. On this host the observed command itself is an ELF. | Exact resolved path, ELF/type evidence, SHA-256 and ns-exact mtime tied to the measured bytes; record a new identity if they change. |
| Host bytes or minified loader names changed | Independently derive registration callees, group bindings and `.md` filenames from the current `strings -n 4` dump, then compare distinct `(group, file)` pairs with the declared classes. Read instruction literals and non-registration loader context separately. Only after this mechanism note, align all reader defaults and update the pin values. | Raw anchors and derivation receipt bound to the binary/dump hashes; before/after byte hashes; parity over the documented extraction. Variable-bound groups must resolve in the proper module context, not by guessing from a reused name. |
| A census class is not found by the new extractor | Investigate whether the call shape changed or the class was actually removed. Preserve the historical class set unless absence has explicit evidence. | Named reason and exact absence evidence; preserve the frozen three-entry opencode removal ledger, not a silently smaller census. |
| A pinned executable is missing or unreadable | Repair path resolution or the environment first. Do not label this a measured byte mismatch and do not change the exit policy to force green. | Pin guard exit **2** (`UNREADABLE`); the current before receipt demonstrates this branch. |
| Executable is readable but its hash/mtime differs from the pin | Treat as substrate drift; rederive first and pin second. A missing required pin also belongs to the failed-pin tier. | Pin guard exit **1**, not exit 2. This is the opened guard contract; this seat did not execute a mismatch control. |
| Baseline is unreadable, malformed, or has an uninterpretable pin value | Repair the pin document, keeping the distinct error classification. | Pin guard exit **3**. Precedence is 3 > 2 > 1 > 0; a simultaneous unreadable path outranks a drift. |
| Refreshed defaults and pins are integrated | Let L1 measure the unchanged frozen C1 counter at the named integrated revision after the freeze receipt and independent shortcut controls exist. | Target only: `host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified`, exit 0. This draft does not report that result as executed. |

The affected default-reader surfaces are `verify_surfaces.py`, `check_substrate_pins.py`, `verify_harness_claims.py`, and `verify_harness_independent.py`; pin data lives in `verifiers/baseline.json`. The frozen `check_substrate_repin_v2.py` is the counter, not a place to redefine the target. Its execution of the measured revision's gates is an explicit trust boundary: independent byte identity, derivation and shortcut controls must remain outside those gates.

## Runtime and certification limits

- Extraction is static, host-bound evidence. A compiled-in loader call does not prove the loader fires, discovers every runtime source, reaches a prompt, wins precedence, or improves instruction effectiveness.
- The `.md` registration extractor excludes non-`.md` registrations and differently shaped loaders. Instruction literals and manually declared classes need their own context evidence; an unresolved binding must fail rather than disappear from the set.
- Pin equality detects change; it does not establish the original measurement's provenance, and an ELF file type does not independently establish binary authenticity. Neither a path-only fix nor a pin-only update establishes loader parity.
- This entry reports no production C1 after-value, axis score increase, or 6/6 tip-battery result. No loader pairs are asserted from a peer's unexecuted probe.
- C2 is separate: the authorized checklist self-test target is `0 failure(s) over N assertions`, N >= 1863. Hermetic fixture correction evidence must replace the failing live-governance dependency, while genuinely dead citations must remain red. Neither C1 byte identity nor a fixture self-test demonstrates that the live corpus is clean.

## Integration provenance

Intended destination: `corpus/knowledge/host-loader-refresh-round82.md`. The source row S251, this entry and the round-82 lesson Gate quote should point to the actual opened derivation/identity receipts. The quote above is already grounded in this seat's byte observation; loader-derivation claims require their own opened receipt before integration. Registry and lesson mutations belong to their assigned owners/L1, not this leaf seat.
