# Kb81Z01Sec — security review of the round-81 instrument changes (w1, 2026-10-28)

Reviewer seat (leaf, no subagents). Scope per dispatch: (a) `external-commits.json` parsing
under malformed JSON / missing keys; (b) corpus-line smuggling of a lane-committed object into
`commit_external` (exemption direction); (c) `<rev>:<path>` resolution — `..` and option
injection into `git cat-file`; (d) unquoted/unvalidated shell-outs in new code; (e) path
sanitization in refresh-corpus-baseline.py and c1_controls.py.

Method: static read of the published bytes PLUS dynamic probes — both corpus-gate patches
applied to a pristine base clone (`/fast/scratch/hyaku/kotoba-r81/Kb81Z01Sec/clone` at
b284223105f4d106f7e8f56ed4fd296c643cda0e, toplevel-asserted) and 11 crafted worlds run against
the patched modules. Every probe result below is from an executed command, pasted verbatim.

## Reviewed bytes

- `build/Kb81E01Integrity.patch` (20175 B, sha256 6bbb304bea83968ced6c2ba3f33afa26b7d4256334303ea99a32279079495fe7)
  — R1 `<rev>:<path>` + content identity + R2 `external_binding` + the new
  `verifiers/external-commits.json` (dict form, one pinned row). Applied cleanly on base;
  post-image blob reproduced `bbee51f2bae5b33b123a546150e83352d68eeebc` = pin 1.
  Self-test on applied bytes: `self-test: 0 failure(s) over 178 assertions`, rc 0.
- `build/Kb81E02Independent.patch` (15664 B, sha256 d8bf88c8ef5daf99ddf861ab2a5aeaa1193a57a90200e1d314134750e2e7f9d1)
  — R2 for the independent gate. NOTE: first published at 19622 B (post-image 7b37461a…,
  247/18), revised 23:39 to the current bytes (170/16); post-image blob reproduced
  `59602942075d8fe77061876fb52eb32a44313697` = pin 2. Self-test: `109 assertions, 0 failures`, rc 0.
- `build/Kb81E05Erratum.patch` (6037 B) — E6 as landed: `LINE_CAP = 900`, TIGHT
  `(base blob, reviewed r81 blob)` tuples, self-test constants derived from LINE_CAP
  (`range(LINE_CAP + 1)`, `"%d lines > %d" % (LINE_CAP + 1, LINE_CAP)`, `padding=LINE_CAP + 1`);
  no hardcoded 141/901 anywhere (grep: derivation-only).
- `build/c1_controls.py` (988 lines), `build/check_sdk_allowed_tools.py` (1638 lines),
  `build/refresh-corpus-baseline.py` (419 lines, byte-identical port of the r80-reviewed
  script — `diff -q` vs round-80/build: identical).
- `plans/round-81.md` as on disk (amended: LINE_CAP 900 — see INFO-5), w1 reports
  Kb81E01Integrity.md / Kb81E02Independent.md / Kb81E03ExtManifest.md / Kb81E05Erratum.md.

## Findings

### MEDIUM-1 — E01 `external_binding` crashes (uncaught TypeError, exit 1) on a non-list `commits` member

`verify_corpus_integrity.py` (applied bytes): the try wraps only `json.loads(...)["commits"]`;
the iteration over `entries` is outside it. A committed manifest `{"commits": 5}` (or a
string/number member) raises inside the set comprehension:

    commits:5 -> CRASH: TypeError: 'int' object is not iterable

Uncaught → traceback → interpreter exit 1. The gate's exit contract is 0/1/2 where 1 means
"corpus violations found"; a broken manifest is an environment fault that must fail closed as
could-not-evaluate (exit 2) or a plain red — exit 1 misattributes it, and inside the tip
battery it surfaces as a corpus-gate red instead of an instrument fault. NOT silent-green
(never passes); E02 guards the same shape (`isinstance(rows, list) else []` + wide except →
`external_commits` returned `{}` in the identical probe: "E02 commits:5 -> no crash").
Minimal fix before freeze: after the try, `if not isinstance(entries, list): return False`.
Cost: changes the E01 post-image blob → pin 1 and its provenance line must be re-derived
(apply + `git hash-object`), or the L1 declines and records the shape as known-fail-red.

### LOW-1 — "absent from lane and fleet" is commit-peel-specific: a lane-present non-commit object can be exempted as `commit_external`

Both gates classify with resolution FIRST, then the manifest (direction safe — see INFO-3),
but "absent" is implemented as `git cat-file -e <hex>^{commit}` failing. A hash that EXISTS in
the lane as a blob (not a commit) fails the peel, and a fully pinned manifest row then exempts
it. Probe (dict-form manifest `{hash, repository, receipt, receipt_sha256}`, committed receipt
carrying hash+repo, hash-object-written lane blob, corpus line `commit `<blob>``):

    E02 lane-blob PINNED: external 1 unresolvable 0
    E01 lane-blob PINNED: class external

The plan's sentence is "absent from lane and fleet"; the implementation delivers "absent as a
commit from lane and fleet". Impact: a dead `commit `<hex>`` citation whose hex is a
lane-committed blob/tree reads INFO instead of `commit_unresolvable` red. Exploitation needs
the manifest row + pinned receipt committed too (fully visible to review), and the W6 class
(lane COMMIT masked by a marker) stays caught — a lane commit peel-succeeds → `resolved`, and
E01's self-test pins `external/lane-owned-never-external`. Fix shape if adopted: probe
`cat-file -e <hex>` (any type) before the external branch in both gates, or record the
peel-specific semantics in the round lesson so the plan wording is not over-read.

### INFO-1 — E01's object route pretty-prints any object type; E02's reads blobs only (asymmetry, contrived false-alive)

E01 `git_blob_bytes` runs `git cat-file -p <token>`; E02 runs `git cat-file blob <token>`.
A token naming a TREE (`HEAD:.ufo/reports/` — probe: `cat-file -e` rc=0) succeeds under `-p`
and prints the directory listing; `report_content_ok` (>=400 B AND literal `## SHONEN`) then
passes only if the listing is >=400 B and contains that literal — i.e. a committed entry
literally named `## SHONEN` inside the cited directory. Contrived and review-visible; under
E02's `blob` form a tree fails (rc!=0) → dead. No action required; noted so the identity
asymmetry between the gates is on record.

### INFO-2 — injection and traversal surfaces: clean, probed

- Option-shaped revs: `git cat-file -e "-x:.ufo/reports/round-76/kotoba.md"` →
  `error: unknown switch 'x'`; `"--:..."` → `error: unknown option ':.ufo/reports/x'` — the
  token travels as ONE list-form argv element, git errors, `git_ok`/returncode!=0 → dead
  (fails closed). No `-`-prefix rev reaches a parsed option.
- `..` inside tree paths: `git cat-file -e "HEAD:.ufo/reports/../corpus"` →
  `fatal: path '.ufo/reports/../corpus' does not exist in 'HEAD'` (rc 128) → dead.
- Manifest-controlled receipt paths: E01 rejects leading `/` and any `..` segment
  (`receipt.split("/")`), then reads only committed bytes via `HEAD:<receipt>`;
  E02 reads via `ls-files --error-unmatch` + `cat-file blob HEAD:<rel>` — untracked,
  absolute, home, and traversal receipts all fail closed (probed in the bad-shape worlds:
  `/etc/passwd` and `corpus/untracked.md` rows bind nothing).
- Shell-out sweep: `shell=True|os.system|popen|eval(|exec(` over c1_controls.py and
  check_sdk_allowed_tools.py → 0 hits; every new subprocess call is list-form
  (`["git", "-C", repo, "cat-file", "blob", token]` etc.).

### INFO-3 — exemption direction safe, malformed inputs fail closed (probed)

- Lane-resolvable commit whose sha IS bound in the manifest: classified `resolved`, never
  external (S1: `external 0 unresolvable 0`; E01 self-test `external/lane-owned-never-external`).
  The dangerous direction (manifest entry masking a lane object) requires the object to also
  fail the commit peel — see LOW-1 for the blob-shaped residue.
- Malformed manifest JSON: `external 0 unresolvable 1`, no traceback (both gates).
- Manifest absent at HEAD, non-dict rows, missing keys, 41-hex hash, slash-less repo,
  abbreviated 7-hex hash, uncommitted receipt, wrong `receipt_sha256`, conflicting duplicate
  rows, empty manifest `[]`: every row unbinds → `commit_unresolvable` stays red
  (S3-redo: `external 0 unresolvable 6 nonhash 1`; E01 self-test asserts each red arm).
- Bare-list manifest (the old E02 accepted it): current bytes require the dict form —
  `{"commits": [...]}` — bare lists fail closed in BOTH gates.
- Self-referential receipt (manifest naming itself as evidence): structurally impossible now —
  the mandatory `receipt_sha256` would have to equal sha256 of bytes containing it (fixed-point).
  Probed on the superseded bytes it bound (`external 1`); on current bytes `external 0`.

### INFO-4 — pin freeze reproduced, correct against the published patches

Both pins independently reproduced in a pristine base clone by apply + `git hash-object`:
E01 → `bbee51f2bae5b33b123a546150e83352d68eeebc` (matches pin 1 and the patch's own index
line `e470eaa..bbee51f`); E02 → `59602942075d8fe77061876fb52eb32a44313697` (matches pin 2).
Publication-control caveat I hit and resolved: the E02 patch was republished at 23:39
(19622 B → 15664 B); an application of the superseded file yields 7b37461a… — the CURRENT
build/ file is the pinned one. No defect; recorded so the freeze audit does not mistake the
older 7b37461a references (Kb81C05Closure.md:52, Kb81E02Independent.md:88) for a mismatch.

### INFO-5 — the E6 cap on disk is 900, not the 140 my dispatch carried; one stale artifact

`plans/round-81.md` as on disk declares `LINE_CAP 40→900` with a pre-freeze revision note and
a reconciled composition (+402/-29 = base-spent 22/3 + E01 +210/-10 + E02 +170/-16; I
re-measured both numstats with `git apply --numstat`: 210/10 ✓ and 170/16 ✓), and the kill
rule on disk uses 900. My dispatch summary (140) is stale; the plan text is authoritative.
`build/Kb81E05Erratum.hunk-inventory.txt` still says 140 — a stale superseded artifact next to
the landed patch; the freeze owner should make `receipts/freeze-shas.txt` explicitly record
the 900 revision so the audit trail is coherent (the inventory predates the revision).

### INFO-6 — the superseded E02 revision fixed three real gaps (history note)

Against the first publication (7b37461a) I measured: explicit-path report pointers
existence-only (a planted 7 B marker at `.ufo/reports/round-53/kotoba.md` cited as
`../../.ufo/reports/...` read ALIVE while E01 read DEAD — `E02 independent: dead 1 of 2` vs
`E01 integrity: dead 2 of 2`), optional `receipt_sha256` (self-referential receipt bound),
and bare-list manifest acceptance. The current bytes close all three: planted marker
`dead 2 of 2` in BOTH gates on the identical world; pin mandatory; dict form required.
No action; recorded because w1 prose still cites the old bytes.

### Clean verdicts

- c1_controls.py: every `shutil.rmtree` bounded under `ctx.work` (world dirs under
  `--work`/`$TMPDIR`); `assert_toplevel` before each mutation; isolated source clone per tag;
  no shell-outs; `--real-fleet`/`--work`/`--out` are operator-settable destinations (trust
  boundary, seat-run — no elevation path). Clean.
- refresh-corpus-baseline.py (r81 port): byte-identical to the r80-reviewed script — r80-Z01's
  LOW-2 (only the baseline leaf is symlink-refused; a committed `verifiers/` symlink would
  redirect both gate execution and the write) carries unchanged; operator-run on a clean tree,
  dirty-tree refusal (incl. untracked non-ignored files) means R3's `.ufo/wapes` disposition
  must land before the refresh run — operability note, matches the published run order.
- check_sdk_allowed_tools.py: shell-out sweep clean; deeper C2 semantics are outside my
  items (a)-(e); its freeze sha is the freeze seat's gate.
- Carried hardening notes from r80-Z01, unchanged in shape: the rewritten E01 object route
  still appends `fleet_root` unconditionally (`([lane] if lane else []) + [fleet_root]`) —
  fails closed, documented two-probe; fleet-shaped sandboxes stay write-through by design.

## Residual risk and verification gaps

1. I did not run the full ~105 s amended tip battery (battery/L1 territory). The guard logic
   was exercised via self-tests (E01 178/0, E02 109/0, both rc 0 on applied bytes) and the pin
   anchoring was reproduced, which excludes the stale-pin red class at the landed tip.
2. MEDIUM-1's fix, if adopted, changes the E01 blob → pin 1 + provenance must be re-derived
   before freeze (method already proven: apply + hash-object). If declined, record the
   `{"commits": <non-list>}` shape as known-fail-red in the round lesson.
3. LOW-1's fix would change BOTH gate blobs (both classify). If declined, the peel-specific
   wording should be recorded so "absent from lane and fleet" is not over-read next round.
4. E01's `report_pointer_exists` reads cited targets fully into memory (`read_bytes()` /
   `-p` stdout); pointer shape (`round-N/<name>.md`) bounds realistic targets; no action.
5. The 900-revision receipt in `receipts/freeze-shas.txt` is asserted by the plan text but was
   not re-verified by me (freeze seat's gate; the stale hunk inventory is my evidence to them).

Tooling: nothing installed (operator 2026-10-19 authorization unused); no pacman; no host
services touched. Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81Z01Sec/` removed before yield.

VERDICT: instrument changes are direction-safe and fail closed on every malformed-input probe with pins correctly anchored to the published bytes; one MEDIUM (E01 external_binding TypeError crash on a non-list commits member, exit-1 misattribution — fix or record before freeze), one LOW (peel-specific absence lets a lane-present blob sha read external INFO — record or probe any-type), injection/traversal/shell surfaces clean with named sweeps; the landed E02 revision closed the explicit-path identity gap and self-reference holes found in its first publication.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81Z01Sec.md
