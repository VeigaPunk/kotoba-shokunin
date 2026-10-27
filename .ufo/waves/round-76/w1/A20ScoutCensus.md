# A20ScoutCensus — S213 used-by census check

Mirrored `/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus` with `cp -a` to `/fast/scratch/hyaku/kotoba-r76/A20ScoutCensus/corpus`. On that mirror, changed only S213's `used-by` cell by appending `corpus/knowledge/description-craft-round76.md`; no other corpus files were created or modified.

Command:
`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file /fast/scratch/hyaku/kotoba-r76/A20ScoutCensus/corpus/SOURCES.md`

Observed output includes pre-existing `W04` warnings, then E11 missing-path findings for several used-by references because this mirror contains only `corpus`, not the lane-root files those references name. Specifically S213 reports `file\tE11\tS213 missing used-by corpus/knowledge/description-craft-round76.md`. Process exit code: **1**, not 0. Therefore the requested exit-0 condition was not met under the specified corpus-only mirror and append-only experiment; the check is not clean unless the referenced target is present (and existing `SKILL.md` used-by references likewise require lane-root files). No E03 or E04 was emitted; S213 emitted W04 for its URL appearing under another scope, which is warning-only.
