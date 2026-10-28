# Kb81E03ExtManifest — C1 repair 2 evidence: the external-commit verified-binding manifest

Seat: `Kb81E03ExtManifest` (executor, leaf). Round 81 w1. Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`,
base `b284223105f4d106f7e8f56ed4fd296c643cda0e` (lane HEAD at start = base, verified `git -C <lane> rev-parse HEAD`).
Deliverable form: candidate data file + receipts under `.ufo/waves/round-81/build/`, no lane edit (freeze discipline).
I dispatched no labrat: the seat's own primary-byte re-derivation (ls-remote + commit-pinned fetch + cat-file)
answered every question the labrat would have been sent for.

Plan read first: `plans/round-81.md` § C1 repair 2. Consumed read-only: `.ufo/waves/round-79/snapshots/S231.fetch.json`,
`S230.fetch.json`, `S231-vibe.md`, `S230-pi.md`, `.ufo/waves/round-80/build/Kb80R03ReopenSix-S23{0,1}.fetch.json`,
`.ufo/waves/round-80/w1/Kb80E05GrammarFix.md`, `corpus/SOURCES.md:171-172`, `corpus/knowledge/allowed-tools-surfaces-round80.md:21`,
`verifiers/verify_corpus_integrity.py`, `verifiers/verify_corpus_independent.py`, `verifiers/check_tip_battery.py`,
`verifiers/check_gate_registry.py`.

## 1. Deliverables

| path | bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-81/build/Kb81E03ExtManifest.json` (candidate `verifiers/external-commits.json`) | 211 | `0af8afcb5cad173e0950437b4a3b07e0902bfe89cb87aaa65737648b43bcf4d7` |
| `.ufo/waves/round-81/build/Kb81E03ExtManifest-fetch.txt` (receipt, 146 lines) | — | `c9a70cbeee2c54bd5d675f9e264c0a7631cbf88dc1fdd5430669e649732821d0` |

Exact content of the manifest (top-level JSON **array**, exactly the four declared fields, validated with
`python3 -m json.tool` → exit 0):

```json
[
  {
    "hash": "7bb48f213ac677f943d5c791199ed3dddf302f00",
    "repo": "mistralai/mistral-vibe",
    "evidence": ".ufo/waves/round-79/snapshots/S231.fetch.json",
    "pinned_at": "2026-10-27T21:43:03Z"
  }
]
```

`evidence` is lane-repo-relative and is **already committed at the claim base** (`git cat-file -e
b2842231:.ufo/waves/round-79/snapshots/S231.fetch.json` → rc 0; `git ls-files` lists it), so the R2 gate's
"committed receipt" check passes on the landed tree without depending on this wave's own build files.
`pinned_at` is the ls-remote resolution instant recorded verbatim inside that receipt, which makes it a
machine-checkable invariant (§ 4), not a free-text date.

**SUPERSEDED SHAPE (see § 7).** `verifiers/external-commits.json` is authored by seat `Kb81E01Integrity`
(R2a) with the schema agreed with `Kb81E02Independent` (R2b): an object `{"note", "commits": [...]}` whose
rows are `{hash, repository, receipt, receipt_sha256}`, manifest and receipt read at **HEAD** via
`git cat-file -p HEAD:<path>`. That file, not this one, integrates; my JSON must not also land (one
manifest, one schema). Its single record is the same binding as mine — same hash, same repository, same
receipt path — and its `receipt_sha256` `e75f057a8e8f8319df227a254a42526ed096c7d0dc5364307365729a08ae738f`
is the blob digest I measured here independently (§ 2 row 8). This file is retained as the evidence-content
record only; `.ufo/waves/round-81/build/Kb81E03ExtManifest-superseded.txt` says so in the build dir.

## 2. Verification from primary bytes (all commands and exits are in the receipt)

| # | command | rc | observed |
|---|---|---|---|
| 1 | `git -C <lane> cat-file -t 7bb48f21…2f00` | **128** | `fatal: git cat-file: could not get object info` → ABSENT from the lane |
| 2 | `git -C /home/vgpnk/Projects/shokunin cat-file -t 7bb48f21…2f00` | **128** | same fatal → ABSENT from the fleet |
| 3 | `git ls-remote https://github.com/mistralai/mistral-vibe refs/heads/main` (2026-10-28T02:28:14Z) | 0 | `7bb48f213ac677f943d5c791199ed3dddf302f00 refs/heads/main` |
| 4 | `git ls-remote https://github.com/mistralai/mistral-vibe HEAD` | 0 | same hash → it is mistral-vibe's head today |
| 5 | `git ls-remote https://github.com/badlogic/pi-mono refs/heads/main` | 0 | `a92283056d915c758799fcd904948ff0cb42628c` (the branch moved twice since r79: `bb65e3e4…` at r79, `85c2ee3e…` at r80, `a9228305…` now) |
| 6 | `git ls-remote https://github.com/badlogic/pi-mono` (full advertisement, 2026-10-28T02:28:16Z) | 0 | 4120 refs, **0** lines containing `7bb48f21…` |
| 7 | `curl … /mistralai/mistral-vibe/7bb48f21…2f00/README.md` | 0 | `HTTP=200 BYTES=77634 REDIRECTS=0`, sha256 `fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0`, **byte-identical** (`cmp`) to committed `.ufo/waves/round-79/snapshots/S231-vibe.md` |
| 8 | `git -C <lane> cat-file -p b2842231:.ufo/waves/round-79/snapshots/S231.fetch.json` | 0 | 866 B; contains `url …/mistralai/mistral-vibe/main/README.md`, the hash, and `pinned_at` verbatim |
| 9 | `python3 -B verifiers/verify_corpus_integrity.py --repo <lane>` | **1** | `commit_total=46 unresolvable=2`; sites `corpus/SOURCES.md:171` and `:172`, both the same token |
| 10 | `python3 -B verifiers/verify_corpus_independent.py --repo <lane>` | **1** | `commit_total 46 INFO`, `commit_unresolvable observed=2 DRIFT` |

So the binding is a three-way identity, re-derived today, not inherited: **repo → hash → content bytes**
(`ls-remote` says the hash is mistral-vibe's ref, the commit-pinned raw URL at that hash serves exactly the
bytes of the committed snapshot), while the hash is **absent from both the lane and the fleet** — i.e. the
Q61 "unresolvable here" precondition holds and the third-repository attribution holds. The mistral-vibe
binding **can** be verified today; the manifest is therefore populated, not empty.

Live disproof of the r80 defect, from the same primary channel: both of pi-mono's own commits recorded in
the S230 receipt (`bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923`, `25cc5c7bf4cbc76b2e134c729eb8d57d521ed749`)
return HTTP 200 at their commit-pinned raw URLs and serve the pinned skills.md bytes
(sha256 `5b98055…469e5`); neither is `7bb48f21…`. The S230 row's anchor is a wrong-repository attribution,
exactly as R80-D4 routes it.

## 3. Does S230 need a second entry for pi-mono's head? **No — one entry, one hash.**

- The manifest is keyed by the **cited token**, and the corpus contains exactly one external 40-hex token:
  `7bb48f213ac677f943d5c791199ed3dddf302f00`, cited twice (`SOURCES.md:171` under the wrong repo name,
  `:172` under the right one). Both sites are the *same* hash, so one manifest row clears both. The plan's
  own phrasing agrees ("The two S230/S231 tokens bind to `mistralai/mistral-vibe`").
- pi-mono's head is **not** a corpus citation today (`git -C <lane> grep bb65e3e49710fbd14f10c77
  b2842231 -- corpus/` → rc 1; the only other occurrences are truncated `bb65e3e4…` / `25cc5c7b…` prose in
  `corpus/lessons/round-80.md:49` and `corpus/knowledge/allowed-tools-surfaces-round80.md:21`, which are not
  `commit `<hex>`` tokens at all). A manifest entry for a hash nobody cites would exempt a hash with no
  citation — pure attack surface, zero benefit.
- Adding pi-mono as the repo for `7bb48f21…` (to make the S230 line "match") is forbidden twice over: it
  endorses a false binding, and it violates "one object per exempted external commit hash".
- **Contingency, if the R5/S250 supersede row cites pi-mono's r79 head as a full token** (recommended
  instead: write it truncated, `bb65e3e4…`, which classifies `commit_truncated` and needs no entry — that is
  how `plans/round-81.md` § C1 repair 5 itself writes it), then a second row is *required*:

  ```json
  {
    "hash": "bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923",
    "repo": "badlogic/pi-mono",
    "evidence": ".ufo/waves/round-79/snapshots/S230.fetch.json",
    "pinned_at": "2026-10-27T21:41:14Z"
  }
  ```

  This is verified live today (receipt § 10b: HTTP 200 at the commit-pinned URL, bytes = the committed
  S230 snapshot). It is **not** in the candidate file because the citation does not exist yet; adding it
  now would be a speculative exemption. Same caution applies to `25cc5c7bf4cbc76b2e134c729eb8d57d521ed749`.

## 4. What the R2 gate patch must do with this file (operability)

The file is inert data; it changes **no** classification by itself — measured, not asserted: control clone
at base + the manifest committed + gates unpatched (control rev `2aa18a18937440a4acecd8caa7e5e7fafd96784d`)
→ integrity `unresolvable=2` rc 1, independent `unresolvable=2` rc 1, identical to § 2 rows 9–10. Only the
patch that *consumes* the manifest is load-bearing.

Required semantics (fail-closed; both gates, implemented independently — sharing the data file is fine,
sharing the implementation is not):

1. **Load from the measured repo**: `<repo>/verifiers/external-commits.json`, where `<repo>` is the tree the
   gate is measuring. In the tip-battery sandbox that is the clone checked out at `<rev>`, so the manifest at
   the measured revision governs and the base (no manifest) keeps its declared red.
2. **Absent / unreadable / not a JSON array / entry missing any of the four fields / non-string field** →
   that entry does not exempt anything; never raise, never degrade to exit 2. (Precedent: `commit_resolves`'s
   missing-fleet-root arm reads False, never raises.)
3. **Match is exact and hash-keyed**: `token.lower() == entry["hash"]` with the manifest hash required to be
   40 lowercase hex. A 7-hex or 39-hex token must never match — probed (§ 5): 39-hex prefix and `deadbeef`
   both fall through to `commit_unresolvable`. No prefix matching, ever.
4. **The `repo` field is the verified owner, NOT a per-line assertion.** Do not require the citing line to
   name `entry["repo"]`: `SOURCES.md:171` names `badlogic/pi-mono`, and requiring agreement would leave the
   site red and stop C1 (S230 is append-only; the correction is the S250 supersede row, R5). The manifest
   states where the hash actually lives; provenance correction lives in the source register.
5. **Evidence is checked, not trusted**: the `evidence` path must (a) be repo-relative with no `..`,
   (b) exist at the measured tree / be tracked, and (c) contain all three of `entry["repo"]`,
   `entry["hash"]`, `entry["pinned_at"]` as substrings. All three hold for this entry (receipt § 9:
   `True`/`True`/`True`). Recommended strengthening over bare substring: also require the receipt to parse
   as JSON whose `url` contains `github.com/<repo>/` and whose `sha256` field is 64 hex — that turns the
   check from "the string appears somewhere" into "this is structurally a fetch record for this repo".
6. **Hook points, so `commit_total` cannot move.** `commit_total` is a baseline-`equal` observation
   (`46` today, `corpus.pointers.commit_total` in both gates). In `verify_corpus_integrity.py` the divert
   belongs inside `citation_findings` **after** `commit_total += 1` (currently line 536) and **at** the
   `if not commit_resolves(token.lower()):` test (line 537) — i.e. `unresolvable` is skipped when the token is
   in the manifest, but the token still counts in `commit_total`. In `verify_corpus_independent.py` the
   divert belongs inside `analyse_commits` at the `if proc.returncode != 0:` block (lines 498-499), before
   `unresolvable.append`; `commit_total = len(citations)` is already incremented upstream, so it stays 46.
   Diverting earlier (before the count) would drop `commit_total` to 44 and break the `equal` check.
7. **New class**: `commit_external` (+ `commit_external_detail`), a counted INFO class like
   `commit_truncated` / `commit_quoted_excluded` — **no** CHECKS/CHECK_IDS row, so it can never be a drift
   class and needs no baseline entry; observable via `--json`. Both self-tests gain one arm
   (manifest hit → external, not unresolvable; manifest miss → unresolvable; prefix → unresolvable).
8. **No accounting side-effects**: `verifiers/external-commits.json` is not under `corpus/`
   (`corpus.index.tracked_files` counts `git ls-files corpus/` only → unchanged), is not `.py`/`.sh`
   (`check_gate_registry.py` enumerates only those, `git ls-tree` non-recursive → **no registry row**), is
   not one of the six battery instruments (`instrument-size` / `instrument-pin` untouched → **no pin, no
   line-cap spend**; E6's 140 cap stays available to the two gate blobs). `no-deletions` is unaffected
   (addition only). **No `corpus/README.md` coverage row is needed** either — the index covers `corpus/`
   files, and this path is outside it.

## 5. Calibration: what this manifest does and does not stop

Measured probe (receipt § 7, a reference lookup, explicitly *not* a verifier):

| token | verdict |
|---|---|
| `7bb48f213ac677f943d5c791199ed3dddf302f00` (the live token) | external: `mistralai/mistral-vibe` |
| `7bb48f213ac677f943d5c791199ed3dddf302f0` (39-hex prefix) | not in manifest → `commit_unresolvable` |
| `0000…0000` (fabricated) | not in manifest → `commit_unresolvable` |
| `deadbeef` (7-hex) | not in manifest → `commit_unresolvable` |

Against the r80 killing worlds: **W8** (real lane-created commit absent from lane+fleet masked by an
`owner/repo@` marker) is dead — a marker is not a manifest row, so the token stays `commit_unresolvable`.
**W9** (marker-only attribution) is dead for the same reason, and additionally because the row must carry a
committed receipt that names repo *and* hash *and* pinned instant. The class is now a **closed, reviewed
set of hashes** rather than "any hex on a line that mentions a third repository": the r80 R1 residual
(line scope is spoofable by construction) narrows to "the one reviewed hash can be re-cited on any line",
which is a provenance claim, not a resolution lie.

Named residuals (not repaired here):

- **R-1 (provenance of the receipt).** The gate runs offline, so it cannot re-run `ls-remote`; the binding
  is a *reviewed assertion with committed corroboration*, machine-checked only for (absent from lane+fleet)
  ∧ (receipt committed) ∧ (receipt names repo/hash/instant). A forged receipt committed together with a
  forged manifest row would pass. Today's mitigation is human review of exactly one row; the r81 freeze
  receipt should record this file's blob sha so any later edit is visible. My live re-derivation (receipt
  § 3–4) is the freshness evidence for *this* round.
- **R-2 (class width, bounded).** Any line may cite the exempt hash and be classified external. Bounded to a
  one-element set; a second entry must clear the same review.
- **R-3 (branch heads move).** pi-mono's `main` moved twice between r79 and now. An entry must pin a
  *commit*, never "main"; `pinned_at` records the resolution instant, not a claim of branch stability.
- **R-4 (bounded negative).** "Absent from pi-mono" is proven only over its 4120 advertised refs; an
  unreferenced object in its store is invisible to `ls-remote`. Stated, not glossed.
- **R-5 (base stays red by construction).** No manifest exists at `b2842231`, so the base measurement is
  unaffected: the declared `4 of 6` / `unresolvable=2` base truth is preserved exactly (receipt § 5).

## 6. Tooling and scratch

No tool installed or upgraded (nothing needed: `git`, `curl`, `python3` sufficed; pacman untouched).
Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81E03ExtManifest/` (clone, pinned fetches, `TMPDIR`) removed
before yield; no mutating git ran anywhere except that scratch clone, whose toplevel was asserted
(`rev-parse --show-toplevel` → the clone, recorded in the receipt § 6). Lane, fleet and sibling repos
untouched by this seat (read-only git only; the lane HEAD moved from the base to
`e6d48e6a9b11da4660df8145bd2f28c3238c5b83` at 23:37:45 −0300 under another seat's
"round-81 plan: claims frozen" commit, one commit past base — not mine, and every measurement above was
taken against `b2842231…`). No lane file edited; nothing committed by this seat.

## 7. Coordination: schema ownership (mid-wave)

`Kb81E01Integrity` (R2a, `verify_corpus_integrity.py`) authored `verifiers/external-commits.json` before
this seat's candidate was in `build/`, with the schema both corpus gates implement:
`{"note": "...", "commits": [{"hash", "repository", "receipt", "receipt_sha256"}]}`, manifest **and**
receipt read at `HEAD` via `git cat-file -p HEAD:<path>`, duplicate hash with conflicting
`(repository, receipt, digest)` dropping out fail-closed. I confirmed that path: **one file, their schema**;
my flat-array candidate does not land (§ 1). Their record is the same binding as mine, and their
`receipt_sha256` is the digest I measured here independently from the base blob.

Verified against their derivation, from bytes I read myself: S230.fetch.json does not contain the token (its
full 40-hex strings are `19d2bf28…`, `25cc5c7b…`, `5b980552…`, `bb65e3e4…`), and the base gate's two
`commit_unresolvable` sites are one distinct hash (`commit_total=46`, § 2 rows 9–10) — so the one-record
manifest is complete and no second entry is needed this round.

Two hardening asks sent, neither a blocker: (a) the manifest `hash` should be exactly 40 lowercase hex with
**exact-equality** matching — a `7-40 hex` range with prefix matching re-opens laundering (git treats
abbreviated hashes as ambiguous; my probe pins that a 39-hex prefix, an all-zero hash and `deadbeef` must
fall through to `commit_unresolvable`); (b) `receipt_sha256` pins the receipt file but nothing yet asserts
the receipt *names* the repository — one `repository in receipt_bytes` substring closes the "valid receipt
for a different repo" substitution. Their digest binding is strictly stronger than my substring-only design;
(b) is the only gap left.

HEAD-read caveat recorded for integration: correct for the tip battery (clone HEAD = `<rev>`), but the
manifest must be **committed** before any direct lane-tree gate run sees it — a pre-commit run still reads
`commit_unresolvable 2` and that is not a red repair.

**Confirmed after their follow-up** (fresh `--shared` clone at base, toplevel asserted, no patched-gate run —
this seat does not score claim after-values): `Kb81E01Integrity.patch` sha256
`6bbb304bea83968ced6c2ba3f33afa26b7d4256334303ea99a32279079495fe7`; `git apply --check` rc 0 and `git apply`
rc 0 on the clean base checkout; the patched `verifiers/verify_corpus_integrity.py` hashes to
`bbee51f2bae5b33b123a546150e83352d68eeebc` (the exact value E6's `INSTRUMENT_PINS` entry must carry), and
`verifiers/external-commits.json` hashes to `402ac290baef66e19a4ac6bcc3b801e78ca5a035` (11 lines, one
record, `receipt_sha256` = the digest measured here). Both hardening asks landed: 40-hex exact-equality
matching with arms for the short/all-zero class, and `repository in receipt_bytes` after the digest pin.

Two recommendations to the L1 from this exchange: (a) the manifest's `note` stays **frozen** — freshness
lives in the committed receipt, and a re-cut would cost a blob re-pin through E6 for no machine-checked gain;
(b) record the manifest blob sha `402ac290baef66e19a4ac6bcc3b801e78ca5a035` in the freeze receipt beside the
two instrument blobs — that closes residual R-1 (the exemption set has no instrument pin) at zero code cost,
so any later widening shows up as a pin mismatch instead of a silent edit.

`Kb81C05Closure` independently flagged the same divergence from the other side (bare list vs
`json.loads(blob)["commits"]`, and `receipt_sha256` mandatory in `Kb81E01Integrity.patch:197`); confirmed
resolved: the flat-array candidate never lands, and the dict form is the integrated manifest. Their finding
is grounded in the patch bytes I quoted back (`line 186` indexes `["commits"]`, so a list raises TypeError →
`external_binding` False → the two sites stay red). Carried forward for the closure audit as a latent,
non-live risk: if `Kb81E02Independent`'s reader tolerates *both* shapes while E01's requires the dict, the
two gates disagree on what a manifest is and a future shape change flips one gate and not the other — the
cheap fix is E02 asserting the same dict-only contract with a bare-list fail-closed arm (E02's seat).



VERDICT: The external-commit binding is complete and verified from primary bytes today at ONE entry (the flat-array candidate is superseded by Kb81E01Integrity's `{"note","commits"}` schema, which carries the identical record with a stronger `receipt_sha256`) — the token `7bb48f21…2f00` is absent from lane (cat-file rc 128) and fleet (rc 128), is `mistralai/mistral-vibe`'s head by `git ls-remote`, and its commit-pinned raw URL serves bytes byte-identical to the committed S231 snapshot (sha256 `fc48a5db…`), with a committed receipt whose blob digest matches the manifest's `receipt_sha256`; S230 needs **no** second entry (its one token is that same hash; pi-mono's head is not a corpus citation, and adding it would be a speculative exemption) — measured controls show the file is inert without the R2 gate patch (control rev `2aa18a1…`: both gates still `unresolvable=2`, rc 1) and that prefix laundering cannot reach it.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E03ExtManifest.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E03ExtManifest-fetch.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E03ExtManifest-superseded.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E03ExtManifest.md
