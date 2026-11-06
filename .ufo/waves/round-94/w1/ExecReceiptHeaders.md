# ExecReceiptHeaders — round-94 w1 — mined-mistake fix: receipt check fails closed on malformed headers

Status: DONE. Date: 2026-11-05. Patch base: freeze commit
`edc731a91a956f6df20c27a74fb981b286f6ba58`, produced as `git diff --cached --binary` from my
scratch clone (`--shared` clone of the lane checked out at the freeze commit; scratch deleted
after the run). Only my owned files were edited: `verifiers/fixtures/round-93/check-receipt-revs.sh`
and new files under `verifiers/fixtures/round-94/receipt-headers/`.

## Change (CriticClaimsR93 D2/D3, the round-94 mined mistake)

`check-receipt-revs.sh` previously dropped a header-shaped line it could not parse: a 41-hex
`REV=` header matched no `40-hex + non-hex` window (D2) and a space/tab-indented header failed the
`^`-anchored regexes (D3) — both read as "no receipt claim". Now: a line that is header-SHAPED
after stripping leading whitespace (`REV=`, `measured rev `, `rev ` followed by a hex run, or the
G1 prefix) but is not a well-formed header prints
`MALFORMED <path>:<line> <reason>` and is counted; the run exits 1 on any MALFORMED or
UNRESOLVED (`malformed declarations:` tally line added; exit ladder 0/1/2 otherwise unchanged).
Scratch declarations (`world rev`, `forgery`, `/scratch/`) keep exempting a line (unchanged
precedence: declared lines are skipped before shape checks). Well-formed header handling,
UNRESOLVED resolution and the existing tally line are byte-identical in format.

Reasons emitted: `leading whitespace before the declaration`; `hex run is N, not 40`;
`G1 hex run is N, not 12`; defensive `declaration is not a well-formed header` (unreachable by
construction: a non-indented 40-hex/12-hex run is caught by the well-formed regexes first).

Gate-registry coupling: none — `check_gate_registry.py`'s universe is blobs directly under
`verifiers/`; `verifiers/fixtures/` trees never count, so this file has no registry row and no
frozen instrument anchors on its bytes.

## Evidence (all commands run with REPO = the lane; script bytes measured)

- Pristine freeze script: sha256 `93063ed17737889ecc91be48381217f59f93cd543e2e904add3915a428e97f98`,
  blob `0ae1f39f10535e384c46b01eb111cb04928ee3e5` at `edc731a91a956f6df20c27a74fb981b286f6ba58`.
- Final patched script: sha256 `b896c8f863e7046c28cb12e5c9eee38c9b9f2c8166f8426145e89185092b4cf9`.
- Patch: `.ufo/waves/round-94/w1/ExecReceiptHeaders/ExecReceiptHeaders.patch`, sha256
  `5c3f3763022903549f37570cccf0889d7a0b2b220bd00740c430f6bbf2b9f974`; `git diff --cached --stat`:
  exactly 4 files (the script +34/−3, `good/headers.txt` +4, `hex41/headers.txt` +1,
  `indented/headers.txt` +2). `git apply --check` on a second fresh clone at the freeze commit:
  APPLY-CHECK-OK (clone removed after).

BEFORE (fail-open, pristine script) → AFTER (fail-closed, patched script):

| target | BEFORE | AFTER |
|---|---|---|
| `receipt-headers/good/` | `4 resolved, 0 unresolved`, EXIT=0 | `4 resolved, 0 unresolved, malformed 0`, EXIT=0 |
| `receipt-headers/hex41/` | `0 resolved, 0 unresolved`, EXIT=2, no finding | `MALFORMED …hex41/headers.txt:1 hex run is 41, not 40`, `malformed declarations: 1`, EXIT=1 |
| `receipt-headers/indented/` | `0 resolved, 0 unresolved`, EXIT=2, no finding | 2× `MALFORMED …indented/headers.txt:1,2 leading whitespace before the declaration`, EXIT=1 |
| `.ufo/waves/round-93/receipts` | `4 scratch-declared; 9 resolved, 0 unresolved over 19 files`, EXIT=0 | identical tally (`9 resolved, 0 unresolved`), `malformed declarations: 0`, EXIT=0 |
| `.ufo/waves/round-92/receipts/landing` | `1 resolved, 5 unresolved`, EXIT=1 | identical tally (`5 unresolved`: bat-rev.txt:24 `cd355c4796fa` + four `cd355c4796fa165ff2b7d822401b4027da29e4d0`), `malformed declarations: 0`, EXIT=1 |

Extra shape probes (scratch-only, `extra-shape-probes.txt`): 39-hex `REV=` → `hex run is 39,
not 40`; G1 prefix with 13 hex → `G1 hex run is 13, not 12` (was silently dropped); a mixed file
(valid `REV=` + 41-hex `REV=`) → 1 resolved + MALFORMED → EXIT=1 (closes the round-93
CriticClaimsR93 probe-p3 false-green); `world rev` / `forgery` lines stay exempt.

Full command+output receipts (BEFORE/AFTER per target) sit beside this report in
`.ufo/waves/round-94/w1/ExecReceiptHeaders/`.

## Files written by this seat

- `verifiers/fixtures/round-93/check-receipt-revs.sh` (in-patch edit; lane copy untouched by me)
- `verifiers/fixtures/round-94/receipt-headers/good/headers.txt` (in-patch, new)
- `verifiers/fixtures/round-94/receipt-headers/hex41/headers.txt` (in-patch, new)
- `verifiers/fixtures/round-94/receipt-headers/indented/headers.txt` (in-patch, new)
- `.ufo/waves/round-94/w1/ExecReceiptHeaders/ExecReceiptHeaders.patch` (patch)
- `.ufo/waves/round-94/w1/ExecReceiptHeaders_READY` (sha256 + one-liner)
- `.ufo/waves/round-94/w1/ExecReceiptHeaders.md` (this report)
- `.ufo/waves/round-94/w1/ExecReceiptHeaders/{before-good,before-hex41,before-indented,before-round93-receipts,before-round92-landing}.txt`
- `.ufo/waves/round-94/w1/ExecReceiptHeaders/{after-good,after-hex41,after-indented,after-round93-receipts,after-round92-landing,extra-shape-probes}.txt`

No lane file outside `.ufo/waves/round-94/w1/ExecReceiptHeaders*` was written by this seat. No git
or jj write in the lane (scratch-clone `git add` only, after asserting `rev-parse --show-toplevel`
== the clone). Scratch `/fast/scratch/hyaku/kotoba-r94/ExecReceiptHeaders/` deleted before yield.

## Installations

None. No packages installed or upgraded; pacman untouched.

## Risks / notes for the integrator

- New output lines (`MALFORMED …`, `malformed declarations: N`) are additive; the pinned
  tallies (`9 resolved, 0 unresolved`, `N resolved, M unresolved`) keep their exact format, and
  both lane receipt dirs read byte-identical tallies BEFORE/AFTER.
- The exit rule is now stricter by design: a receipts dir whose only defect is a malformed
  declaration moves from EXIT=2/0 to EXIT=1 (fail closed). Round-93 and round-92 measured dirs
  contain no such lines today (`malformed declarations: 0` in both AFTER runs), so landing
  readings are unchanged.
- `good/` fixtures pin the round base `4d3e8e4d290d67ecf94a019059f434c71f399919` (present in the
  lane object store) plus its 12-hex G1 prefix `4d3e8e4d290d`; they resolve via `git cat-file`,
  no network.
