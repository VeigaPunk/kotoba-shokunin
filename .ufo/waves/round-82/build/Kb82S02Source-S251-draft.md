# S251 — integration draft, not an admitted source

Axes: freshness; operability. Base named by assignment and opened plan: `47dbe8781657de563ff867caca6244d28e3db504` (not independently revision-verified by this seat).

## Registry-shaped draft

The registry has 11 columns (`corpus/SOURCES.md:12`). Preserve that schema. Do not append this provisional row until the pending evidence fields below have been resolved by L1.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S251 | kotoba own work — current-host omp 18.14.0 loader re-derivation; proposed committed receipt `.ufo/waves/round-82/receipts/host-loader-derivation.txt` (PENDING: filename, content and committed revision not established) | own-work | A | Host-bound extraction of loader-group calls and instruction literals from the measured omp bytes, with independent byte identity and historical census-class preservation; not runtime injection or exhaustive discovery | PENDING: open the actual derivation receipt, record exact lines/byte offsets, command-owned exit codes, measured revision, binary sha256/mtime and a short verbatim located quote | PENDING receipt: a path-only or pin-only update cannot establish that the current host's loader shapes were independently re-derived; admit only the observations the opened receipt actually supports | queued | PENDING: derivation receipt not opened; baseline receipt opened 2026-10-30 only | on-host-binary-change | corpus/knowledge/host-loader-refresh-round82.md#current-byte-evidence (planned integration path, not observed landed) |

`host-loader-derivation.txt` is an explicitly proposed destination, not an assertion that a file exists. Replace it with L1's actual committed receipt path. Tier A is requested own-work scope only, not independent/non-author attestation. Do not set `mined` or substitute today's baseline-access date for the derivation receipt's access date before opening it.

## Opened evidence and located quote

Opened `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/receipts/before-pins.txt:1-40` on 2026-10-30. Located quote at lines 35–37:

> `"exit_code": 2,`
> `"fail": 2,`
> `"pass": 1`

This quote is baseline pin failure evidence only. It is **not** the missing current-host loader-derivation quote. Lines 6–13 and 16–23 identify absent `omp.real` and UNREADABLE sha256/mtime checks; line 32 identifies the opencode pin PASS. Line 40 records `exit=2`.

The receipt labels its measured branch revision at line 1 and command at line 2: `python3 -B verifiers/check_substrate_pins.py --json`. This seat opened that record; it did not execute that command or verify its commit membership.

## Admission boundary

Before this draft can become a landed row, L1 must bind the source to the actual committed round82 derivation receipt and its measured revision, open it, replace the pending anchor with a short exact located quote, and bind the landed knowledge entry. The independent host identity, extraction witnesses, class-set comparison and removal ledger must remain distinguishable from the unchanged C1 counter's execution result.

No claim here of `pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified`, C2 `0 failure(s)`, a production after-value, or a 6/6 tip battery. Those are not observations made by this seat.

VERDICT: PENDING SOURCE ADMISSION — schema-complete draft; derivation receipt, committed locator and quote remain explicitly unobserved.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S02Source-S251-draft.md
