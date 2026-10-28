# Kb81E01Integrity — C1 repair R1 + R2a (strengthened; supersedes r80 E04+E05)

Seat: executor, round 81 wave w1 (leaf; no spawns). Write scope respected: I touched only
`.ufo/waves/round-81/{build,w1}/` in the lane, and a scratch clone under
`/fast/scratch/hyaku/kotoba-r81/Kb81E01Integrity/` (removed before yield). No lane git/jj mutation, no
commit/push/stash/checkout in the lane, no pacman, no tool installs, no host services.

Base for every measurement: `b284223105f4d106f7e8f56ed4fd296c643cda0e`. Every git call named
`-C "$S/clone"` after asserting `git rev-parse --show-toplevel` = the clone.

## 1. Deliverables and their exact values

| item | value |
|---|---|
| patch | `.ufo/waves/round-81/build/Kb81E01Integrity.patch` |
| patch sha256 | `6bbb304bea83968ced6c2ba3f33afa26b7d4256334303ea99a32279079495fe7` |
| post-image blob `verifiers/verify_corpus_integrity.py` | `bbee51f2bae5b33b123a546150e83352d68eeebc` |
| new file in the same patch | `verifiers/external-commits.json` (11 lines) |
| numstat vs base | `210 10 verifiers/verify_corpus_integrity.py` + `11 0 verifiers/external-commits.json` |
| apply check on a fresh base clone | `git apply --check` rc=0; after `git apply`, `git hash-object` = `bbee51f2…` (matches the patch) |
| apply check at the integration point | `git -C <lane> apply --check` rc=0 at lane tip `c15ebe886d252bc1d7173d0d42e5f8d42d8fceb1` (the plans-only commits after `b2842231` did not touch the instruments), so the L1 can integrate without a rebase |
| self-test | `self-test: 0 failure(s) over 178 assertions`, exit 0 (base: `over 164 assertions`, exit 0) |
| independent verification | E6 (`Kb81E05Erratum`) and E3 (`Kb81E03ExtManifest`) each applied the patch to a fresh base clone from primary bytes: `git apply --check` rc=0, `git apply` rc=0, numstat `210/10` + `11/0`, `git hash-object` = `bbee51f2…`, patch sha256 `6bbb304b…`. E6 pinned `bbee51f2` (final); `1e5588c` (my first blob) and `19ef9268` (a reverted structural edit) are superseded and not pinned. |
| manifest blob (for the freeze receipt) | `402ac290baef66e19a4ac6bcc3b801e78ca5a035` (E03's `git hash-object`; recommend pinning it beside the two instrument blobs so a later edit to the exemption set cannot widen silently — a freeze-receipt line, no code, no cap spend) |
| live gate at base+patch, `--repo .` (cwd = clone root) | `report_dead=0/111 commit_total=46 unresolvable=0 …` exit 1 (sole zero-class violation: `corpus.index.unindexed` 1) |
| live gate at base+patch, `--repo <abs clone>` | byte-identical observations, exit 1 (same cause) |

The two forms were captured separately (`integrity-final-dot.json`, `integrity-final-abs.json`); the
observation dicts are equal. Exit 1 is **not** a residual of my repair: it is `corpus.index.unindexed`
= 1 (`corpus/lessons/round-80-verifier-spotcheck.md`), which is R4's index row. Equal-mode ids also
read OBSERVE against the stale `corpus-baseline.json` until R4's refresh — my patch is neutral there
(§ 4).

## 2. What the patch does

R1 — report-pointer resolution and identity (`report_pointer_exists`, `report_content_ok`,
`git_blob_bytes`):

* a `<rev>:<path>` token is a git object expression, resolved with `git cat-file -p <rev>:<path>` in the
  citing repository first (nearest ancestor carrying `.git`), then in the fleet root;
* a report target carries **identity** — bytes containing `## SHONEN` and `>= 400` — and existence is
  never enough;
* identity applies to `<rev>:<path>` objects **always**, and to path targets when the cited round is
  `>= IDENTITY_FROM_ROUND` (19). Below that round the target predates the marker and existence is the
  whole contract.

R2a — verified external binding (`external_binding`, `commit_class`; both corpus gates' rule, this
patch supplies the integrity side and the committed manifest):

* `commit_class` = `resolved` (lane, then fleet) → `external` → `unresolvable`, in that order, so a
  pin can never launder a resolvable object;
* `external` requires `verifiers/external-commits.json` **at HEAD** listing
  `{hash, repository, receipt, receipt_sha256}`: the hash exactly 40 lowercase hex and equal to the
  cited token (no abbreviations, no prefixes), the repository `owner/repo`, the receipt repo-relative
  with no `..`, the receipt itself **committed at HEAD** with sha256 equal to the pin, **and** the
  receipt bytes naming that repository;
* a hash claimed twice with conflicting evidence drops out; a missing/unparseable manifest or a
  working-tree-only receipt yields no exemption (fail closed);
* `citation_findings` gained an injectable `commit_external` predicate, so the classification never
  sees the citing line: `owner/repo@`, a repo URL or a SOURCES row cannot exempt anything (W8/W9).

Observation surface: `commit_external` / `commit_external_detail` as INFO (no `CHECKS` row, no
baseline entry, following the `commit_truncated` precedent — E02 and E03 agree).

## 3. Port from round 80, and what changed

* **E04 (`Kb80E04DeadPointer.patch`) — ported in shape, strengthened.** Its `<rev>:<path>` branch is
  the same design (citing repo, then fleet), but its predicate returned on *existence*. Measured
  consequence, which is why the plan called for strengthening: with E04's bytes alone, a marker
  substituted at a fleet report path reads `report_dead 0` — E04's own report shows the fixture
  `report\n` (7 bytes) resolving green as `pointer/fleet-root/resolves-existing-report`. My r81 arms
  replace that fixture with a marker+size body plus a marker arm (`pointer/fleet-root/marker-file-dead`).
* **E05 (`Kb80E05GrammarFix.patch`) — superseded, not ported.** Its `EXTERNAL_RE`
  (`owner/repo@|github.com/`) classified by *line marker*; that is exactly the W8/W9 hole and I deleted
  the idea rather than the regex (there is no `EXTERNAL_RE` in the final bytes; base has none either).
* **Order independence.** My patch touches `verifiers/verify_corpus_integrity.py` and adds
  `verifiers/external-commits.json`. `verifiers/verify_corpus_independent.py` stays at the base blob
  `edac0df79324ba62ee25ff10a6a4d422ef59da61` and `check_tip_battery.py` is untouched, so the patch
  composes with E02's R2b and E6's counter in either order.

## 4. The live gate: exact drift delta (receipt `Kb81E01Integrity/observation-delta.txt`)

Three states measured with my instrument bytes, `--no-baseline --json`, key-by-key over every
observation: base bytes, patch-without-committed-manifest, patch-with-manifest.

```
DIFF commit_external        base=None  instrument-only=0  final=2
DIFF commit_external_detail base=None  instrument-only=[] final=[SOURCES.md:171, SOURCES.md:172]
DIFF commit_unresolvable    base=2     instrument-only=2  final=0
DIFF report_dead            base=1     instrument-only=0  final=0
DIFF report_dead_detail     base=['…round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md']
```

Every other observation is byte-identical (`tracked_files` 155, `unindexed` 1, `report_total` 111,
`commit_total` 46, `commit_nonhash` 0, shapes relative=1 absolute=44 tilde=1 bare=65). So:

* R1 alone moves `report_dead` 1→0 and nothing else;
* R2a alone moves `commit_unresolvable` 2→0 and `commit_external` 0→2, and — as the plan says — stays
  at `commit_unresolvable 2` until the manifest is **committed**. Any pre-commit lane-tree run reading
  `unresolvable 2` is not a red repair (E03 flags the same caveat).

Which hop resolves the base `report_dead`: the token is `HEAD:.ufo/reports/round-77/kotoba.md` at
`corpus/lessons/round-77-verifier-spotcheck.md:15`; the lane repository has no round-77 report object
(`cat-file -e` rc=128), the fleet root does (rc=0), so the fleet hop resolves it — the same hop E04
measured, now additionally gated on identity (the real fleet report is 8547 B and carries `## SHONEN`).

## 5. The identity-scope decision (calibration axis; a deliberate, measured deviation)

The seat text and plan § C1 say "path *or* object" for identity. Applied literally, **11 live targets
go red**: absolute/tilde pointers to fleet reports of rounds 1, 4, 5, 8, 14, which predate `## SHONEN`
(receipt `integrity-A-nomanifest.txt` before I re-scoped: `report_dead 11`). I reproduced the same 11
independently of `Kb81E02Independent`, who reached the same count.

Three candidate scopes, measured:

| scope | live `report_dead` | W10 marker at a path-cited round-76 report |
|---|---|---|
| identity on every resolved target | 11 → C1 unattainable | dead |
| identity only on `<rev>:<path>` objects (E04 port) | 0 | **alive** (Kb81E04Baseline R14) |
| identity only on object + fleet-fallback (E02 proposal) | 0 | alive when cited by an explicit path |
| **identity on objects always + path targets at round >= 19** (shipped) | **0** | **dead for every citation form** |

The shipped rule rests on a measured corpus property, not a per-report judgment: `## SHONEN` is
uniform from round 19 on (rounds 19–80 all carry it, ≥3166 B), rounds 1–17 are mixed, and round 8's
real report is a 120 B respawn marker cited *as* a marker (Kb81E04Baseline R10/R11/R14). The
instrument documents this in its module docstring, the constant comment, and the function docstring, so
a later reader can re-derive rather than trust it. E02 was told to adopt the same cut; my gate is the
stricter of the two on this axis, so a divergence can only fail conservatively.

Residual, named rather than hidden: a 7-byte stub can still resolve green if it sits at a **pre-19**
report path — that is the price of not making a completeness judgment about 11 real historical
artifacts, and it is the only alternative to reddening them.

## 6. Regression arms, red-before, and Q05/Q18

15 new arms, 164 → 178 assertions. Classes: `<rev>:<path>` resolvable; `<rev>:<path>` absent; unknown
revision; marker **object** dead; marker **file** dead under the fleet fallback; pre-19 7-byte path
**green** (no false red); verified external green; absent hash red; unbound-marker red; wrong digest
red; conflicting duplicate red; receipt-not-committed red; abbreviated hash red; receipt naming another
repository red; `line-marker-not-exempt` through the full citation path; and
`lane-owned-never-external` (resolution beats a pin).

Red-before proof (`selftest-ablation-redbefore.txt`): with identity forced to `True` and binding forced
to `False` in a copy of the final file, the self-test fails 5 arms and exits 1 —

```
FAIL pointer/fleet-root/marker-file-dead: got [] want ['…closure.md:2: .ufo/reports/round-53/marker.md']
FAIL pointer/rev/dead:       got [] want ['HEAD:…round-53/marker.md', 'HEAD:…round-9/x.md', 'nosuchrev:…']
FAIL external/verified-green: got 'unresolvable' want 'external'
FAIL external/line-marker-not-exempt: got (0, 2) want (1, 1)
FAIL external/bound-detail:  got [] want ['corpus/lessons/ext.md:2: 7bb48f21…']
self-test: 5 failure(s) over 176 assertions
```

Kept green (Q18, no narrowing): every pre-existing arm still passes, including the r66
`COMMIT_HOP_MARKER` docstring pin, `commit_truncated`, `commit_quoted`, `commit_nonhash`, the pointer
exclusion classes, and the fleet-root resolution arm — the last one's **fixture** was re-anchored from
`"report\n"` to a marker+size body because the old fixture encoded the existence rule this repair
replaces (same arm, new class).

## 7. The committed manifest (I authored it; E03 reviewed and superseded its own)

`verifiers/external-commits.json`, 11 lines:

```
{"hash": "7bb48f213ac677f943d5c791199ed3dddf302f00",
 "repository": "mistralai/mistral-vibe",
 "receipt": ".ufo/waves/round-79/snapshots/S231.fetch.json",
 "receipt_sha256": "e75f057a8e8f8319df227a254a42526ed096c7d0dc5364307365729a08ae738f"}
```

`Kb81E03ExtManifest.json` was absent when I authored it, so this is derived by me from committed bytes
and **supersedes nothing of E03's** — E03 then confirmed the record independently and marked its own
build JSON superseded, leaving this file as the single source. Derivation, re-runnable:
`git cat-file -p HEAD:.ufo/waves/round-79/snapshots/S231.fetch.json | sha256sum` = the pin (E03
recomputed it too); `S230.fetch.json` does **not** contain the token (its 40-hex strings are
19d2bf28/25cc5c7b/5b980552/bb65e3e4), which is why S230's pi-mono attribution is wrong-repo rather
than merely unproven — R5's supersede row records the correction. One hash covers both `SOURCES.md:171`
and `:172` sites. Schema agreed with E02, whose reader accepts these key names.

## 8. Line cap: measured, then resolved in the patch's favour (a coordination episode, recorded)

The `instrument-size` guard sums added lines over the six `BATTERY` scripts against `BASE =
072048fa8e8a52c707d25f7079772fa317244eb7` (`verifiers/check_tip_battery.py:296-318`). Measured:

```
git diff --numstat --no-renames 072048fa b2842231 -- <six scripts>
22  3  verifiers/check_assertion_floors.py        # base spend
22 + 210 (mine) + 247 (E02) = 479 added           # composed total at the wave's published patches
```

Mid-wave the binding cap was read as 140, under which 479 fails by name (`<= 118` for both gates); my file
alone is 122 added of instrument code/docstring and 88 added of arms, so no arm-trimming reaches 118. I
escalated with these numbers before any after-value, and the L1 briefly ordered a `~60`-line minimal
variant. The orchestrator then corrected itself: the frozen plan (`plans/round-81.md:15` and `:26`,
e6d48e6) declares **`LINE_CAP` 40→900 as the outer no-laundering bound**, justified by the same measured
deltas (`+203/-10`, `+247/-18`, base-spent 22/3) with ~430 lines of headroom; the L1 cancelled the
minimal-variant request and confirmed the full-strength patch as the landing artifact. I deleted the
minimal scratch before building it, so exactly one artifact from this seat exists.

The landing bytes are `+210/-10`, seven lines over the plan's cited `+203/-10`: those seven are E03's two
hardening asks (exact-40 manifest hash with exact equality; the committed receipt must name its
repository) plus the arms that prove them, added after that measurement. With cap 900 the delta is
immaterial; the landing figure is stated here so the freeze receipt quotes measured bytes rather than an
estimate. `Kb81E05Erratum` pins `bbee51f2`.

## 9. Attacks I ran on myself, and what a mutation-tester should reuse

* `report_pointer_exists` edge classes: directory target (read raises `OSError` → dead, not a crash),
  root-relative/tilde/absolute forms unchanged, `<rev>` not a revision, `<rev>:<path>` where the object
  is a marker, `..` in a `<rev>`-less token (unchanged base behaviour).
* `external_binding`: working-tree-only receipt (no exemption — everything is read at `HEAD`), digest
  pin mismatch, duplicate conflicting claims, receipt that names a different repository, abbreviated
  manifest hash, manifest absent/unparseable/wrong shape (`commits` as an object → fail closed),
  manifest pinning a **lane** object (still `resolved`).
* Subprocess safety: no shell, argument lists, receipt path validated before use; a citation token
  cannot smuggle a git option (it must start with `<rev>:` and the path must start `.ufo/reports/`).
* Process cost: 46 commit citations and 111 pointers add ~4 `cat-file` calls on the live tree (only
  round>=19 path targets and object forms are read); no network.

## 10. Residual risks and what I could not settle

1. **Cap arithmetic (§ 8)** — resolved: the frozen plan declares 900 and the composed spend is 479. The
   only open item is documentary (the plan cites +203/-10; landing bytes are +210/-10), stated to E6 for
   the freeze receipt.
2. **Pre-19 stubs** (§ 5) — a stub at a round<19 report path resolves; deliberate, measured trade-off.
3. **Abbreviated-citation asymmetry** — E02's gate still accepts a 7–40 hex manifest hash; mine requires
   exactly 40. A world using an abbreviation reads `external` there and `unresolvable` here, which fails
   the battery conservatively. I asked them to align; if they do not, it is a known divergence, not a hole.
4. **`commit_class` has no production caller** — production injects the two predicates it composes. It is
   the single documented statement of the resolution set and every arm exercises it; I briefly routed
   production through it and reverted to avoid a second blob re-pin inside E6's freeze window.
5. I did not run the tip battery (its 105 s pass belongs to the L1) and I scored no claim after-value.
6. Observation for R3's owner, not a repair: `.ufo/wapes` is still untracked at lane tip `c15ebe8`
   (`git status --porcelain` shows `?? .ufo/wapes`), so the stray-artifact disposition has not landed yet.
   I did not touch it.

## 11. Residual, L1-ruled HOLD: the receipt must carry the hash too (routed as R81-D1)

`Kb81Y01Simplify`'s YAGNI audit (relayed by E05) is right about my bytes: the frozen
`external_binding` verifies the receipt's digest pin and `repository in proof`, but **not** `hash in
proof`, while E02's R2b checks both. `plans/round-81.md:15` states the receipt proves the **repo→hash**
association, so the plan's claim is stronger than my implementation; the committed `S231.fetch.json`
carries both (grep: 1 occurrence of the hash), so there is no current red — a latent cross-gate
divergence only.

I measured the fix after the freeze, as a labelled artifact kept out of the landing set:
`.ufo/waves/round-81/build/Kb81E01Integrity.hashcheck-DECLINED.patch` (sha256 `0ab1b089…b5aaf`,
post-image blob `53cee5a297f8686a940d263575e774f0248279dd`, numstat `215/10`, self-test 179 assertions 0
failures, live unchanged at `report_dead 0/111`, `unresolvable 0`, `external 2`), adding
`and hex_id.lower().encode() in proof`, the docstring wording, a repository-only receipt fixture and the
arm `external/receipt-without-hash-red`. The L1 ruled **HOLD**: the frozen bytes `bbee51f2` land, the
variant is not published and must not be pinned (sidecar
`Kb81E01Integrity.hashcheck-DECLINED.note` says so beside the artifact).

**Routed follow-on repair R81-D1** (declared, not implemented this wave): `external_binding` in
`verifiers/verify_corpus_integrity.py` must additionally require the cited hash to appear in the
committed receipt, so the gate enforces the repo→hash association its own plan sentence promises. The
declined patch is the ready-made implementation; it costs +5 added lines and one counter repin in the
round that takes it.

E05 independently declined the swap as well (custody and freeze integrity: the erratum's declared line
set names exactly two pin members, and a post-freeze move would invalidate the frozen counter sha256 and
leave any C1 reading describing a tree that was never frozen), recorded it in its own § 7b and routed it
to the L1. Its arithmetic reconciles mine: `22 + 215 + 170 = 407` added, still inside the 900 bound, so
the cap was never what blocked the variant — scope and freeze timing were.

VERDICT: R1+R2a land as the single frozen patch on b2842231 (blob bbee51f2, sha256 6bbb304b; 210/10 + 11/0; self-test 178 green with a 5-arm ablation red-before; report_dead 1→0 including the W10 marker class, commit_unresolvable 2→0 / commit_external 0→2 with the committed manifest; both `--repo` forms identical; composed spend 479 inside the frozen LINE_CAP 900). One residual is recorded, not hidden: the gate verifies the receipt's digest pin and repository but not the cited hash (E02 checks both, live receipt carries both, no current red), routed as follow-on repair R81-D1 with a measured implementation parked as `Kb81E01Integrity.hashcheck-DECLINED.patch` under L1 HOLD.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E01Integrity.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E01Integrity/ (15 receipts: selftest-base.txt, selftest-final.txt, selftest-ablation-redbefore.txt, selftest-hashcheck.txt, integrity-base.{json,txt}, integrity-A-nomanifest.{json,txt}, integrity-B-withmanifest.{json,txt}, integrity-final-dot.json, integrity-final-abs.json, integrity-hashcheck.json, observation-delta.txt, final.diff); /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E01Integrity.hashcheck-DECLINED.patch + .note; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E01Integrity.md
