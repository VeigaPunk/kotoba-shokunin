Result: HOLDS — an independently generated dump of the verifier-selected installed opencode binary and the specified omp binary was consumed by the gate; both it and the supplied opencode 1.19.3 dump pass 7/7.

## Attack: C1 erratum guard (b) — HOLDS

Sandbox clone: `/fast/scratch/hyaku/kotoba-r53/w2/W2GuardDumpC1`, checked out at `c775d6823bfca8f0de8c0874032a954438b38edc` (clone/checkout command returned that revision).

`verifiers/verify_surfaces.py:163-166` selects `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` as its opencode binary. I ran `strings -n 4` on that installed ELF binary and on `/home/vgpnk/.local/bin/omp`, writing the dumps inside my sandbox clone. The opencode binary reports version `1.19.4`.

Recorded SHA-256:

- Installed opencode binary: `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`
- My opencode strings dump (`opencode-installed.strings`): `2d72d83f8c90b15c4ba12037c305a838fefe03401e0762c90efdfe04f5a4bd98`
- Installed omp binary (`/home/vgpnk/.local/bin/omp`): `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`
- My omp strings dump (`omp-host.strings`): `953b19dffc4d51bd877330b90f0e994db38e90ee5f80575f08a31f3b73e7d96f`
- Supplied read-only opencode 1.19.3 dump (`/fast/scratch/hyaku/kotoba-r53/RevOcLoader/oc-1.19.3.strings`): `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3`

### Installed opencode 1.19.4 dump

Command: `python3 -B verifiers/verify_surfaces.py --json --opencode-strings /fast/scratch/hyaku/kotoba-r53/w2/W2GuardDumpC1/opencode-installed.strings --omp-strings /fast/scratch/hyaku/kotoba-r53/w2/W2GuardDumpC1/omp-host.strings` — exit 0 (`exit_code: 0`, 7 pass, 0 fail).

Every check row:

```json
{"detail":"42 loader-kind entries verified against the dumps","id":"surfaces.literal_present","status":"PASS"}
{"detail":"all 8 extracted loader class(es) declared","id":"surfaces.no_uncovered_class","status":"PASS"}
{"detail":"opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)","id":"surfaces.opencode_extract","status":"PASS"}
{"detail":"inventory id set == baseline id set (42 ids)","id":"surfaces.table_parity","status":"PASS"}
{"detail":"42 inventory row literal(s) match the baseline per id","id":"surfaces.literal_parity","status":"PASS"}
{"detail":"42 inventory row kind(s) match the baseline per id","id":"surfaces.kind_parity","status":"PASS"}
{"detail":"8 excluded entries, all reasoned and listed in the inventory","id":"surfaces.excluded_reason","status":"PASS"}
```

The JSON substrate entries reported `source: "dump"` and the exact two dump paths above.

### Supplied opencode 1.19.3 dump

Command: `python3 -B verifiers/verify_surfaces.py --json --opencode-strings /fast/scratch/hyaku/kotoba-r53/RevOcLoader/oc-1.19.3.strings --omp-strings /fast/scratch/hyaku/kotoba-r53/w2/W2GuardDumpC1/omp-host.strings` — exit 0 (`exit_code: 0`, 7 pass, 0 fail).

Every check row:

```json
{"detail":"42 loader-kind entries verified against the dumps","id":"surfaces.literal_present","status":"PASS"}
{"detail":"all 8 extracted loader class(es) declared","id":"surfaces.no_uncovered_class","status":"PASS"}
{"detail":"opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)","id":"surfaces.opencode_extract","status":"PASS"}
{"detail":"inventory id set == baseline id set (42 ids)","id":"surfaces.table_parity","status":"PASS"}
{"detail":"42 inventory row literal(s) match the baseline per id","id":"surfaces.literal_parity","status":"PASS"}
{"detail":"42 inventory row kind(s) match the baseline per id","id":"surfaces.kind_parity","status":"PASS"}
{"detail":"8 excluded entries, all reasoned and listed in the inventory","id":"surfaces.excluded_reason","status":"PASS"}
```

The JSON substrate entries reported `source: "dump"`, using the supplied 1.19.3 dump and my omp dump. Thus the independent-dump check is reproducible, the current installed binary dump passes, and the 1.19.3 compatibility case remains reachable at 7/7.
