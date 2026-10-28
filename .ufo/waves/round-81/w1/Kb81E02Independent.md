# Kb81E02Independent — C1 repair R2b: the external-commit binding and report identity in the SECOND corpus witness

Leaf seat, executor. Base `b284223105f4d106f7e8f56ed4fd296c643cda0e` (lane). Deliverable form:
one patch + receipts under `.ufo/waves/round-81/build/`, no lane edit, no lane git mutation.
I dispatched no subagent (leaf); I consumed peer bytes read-only: `plans/round-81.md`,
`verifiers/verify_corpus_independent.py` (my subject), `verifiers/verify_corpus_integrity.py`
(read for architecture only, never copied), `.ufo/waves/round-80/w1/Kb80E05GrammarFix.md`,
`w1/Kb80C01C1.md`, `.ufo/waves/round-80/build/Kb80E04DeadPointer.patch`, and at integration
time E01's `Kb81E01Integrity.patch` + its manifest bytes and E03's `Kb81E03ExtManifest.json`.

## 1. What lands

| field | value |
|---|---|
| patch | `.ufo/waves/round-81/build/Kb81E02Independent.patch`, sha256 `d8bf88c8ef5daf99ddf861ab2a5aeaa1193a57a90200e1d314134750e2e7f9d1` |
| file touched | `verifiers/verify_corpus_independent.py` only (no manifest, no corpus, no README row) |
| numstat vs `b2842231` | **170 added / 16 deleted** (`git apply --numstat` on a pristine base clone) |
| post-image blob | `59602942075d8fe77061876fb52eb32a44313697` (1307 lines) |
| post-image sha256 | `7efc431b5ec39e50ed38c242b520b60c606bbf3682cfb224a6af11feaf57554b` |
| base blob | `edac0df79324ba62ee25ff10a6a4d422ef59da61` |
| apply | `git apply --check` rc=0, `git apply` rc=0 on a fresh clone at `b2842231`; post-image `git hash-object` reproduces `59602942…` |
| order-independence | disjoint files from E01 (`verify_corpus_integrity.py` + the manifest); E01's patch and mine both apply to a pristine base in either order (E01's applied cleanly on top of mine in the composed scratch: HEAD `9f3643c`) |
| pin trail | first publication `7b37461a…` (247/18) was compressed before freeze to these bytes; E6/E14 verified them from patch bytes in a pristine clone and E6 re-pinned `59602942…` in the republished counter (`build/Kb81E05Erratum.*`); the plan's E6 bound was revised pre-freeze to `LINE_CAP` 900 with tight tuples (§5 F3). No minimal variant was built: the L1 requested one and cancelled that request in the same wave; the plan text on disk declares 900, which these bytes fit. No further revision is planned. |

The independent verifier keeps its own tokenizer, its own counter and its own fixtures: nothing in
this patch is ported from E01's diff, and the two instruments were re-derived from the class
sentence independently. The agreement in §4 is therefore evidence, not restatement.

## 2. Semantics implemented (as agreed with E01, check for check)

**Pointer tokenizer.** A `<rev>:` glued immediately to a `.ufo/reports/round-N/….md` match becomes
part of the token (`HEAD:.ufo/reports/round-77/kotoba.md`). The revision grammar is a ref name that
carries a letter (`HEAD`, `nosuchrev`, `main~1`) or 7–40 hex, so a `file.md:15:` line reference never
turns into an object expression. `report_total` is unchanged (111) and the shape census is unchanged
(`absolute 44, bare 65, relative 1, tilde 1`) because the token the prefix joins was already counted.

**Pointer resolution.** `report_target()` returns `(route, bytes)`:
- `object` — `<rev>:<path>` read with `git cat-file blob <token>` from the citing repository, then the
  fleet root;
- `path` — `resolve_pointer()` from the citing file (rooted as-is, `~` against `$HOME`);
- `fallback` — the fleet-root hop for a bare `.ufo/reports/...` path;
- `dead` — nothing resolves.

**Report content identity.** A target must be a report, not a marker file: `>= 400` bytes containing
`## SHONEN`. It binds **always for an object expression**, and **for a path/fallback target only when
the token names `round-N` with `N >= IDENTITY_FROM_ROUND = 19`**. The threshold is data-derived
(§5 F3) and stated in the module docstring; it is the same rule E01 adopted.

**External commits.** A hex token that resolves in neither the lane nor the fleet is
`commit_external` — counted INFO, never a drift class, no `CHECK_IDS` row, no baseline entry —
**iff** `verifiers/external-commits.json` is committed and yields a dict whose `commits` list carries
an entry with: `hash` exactly 40 lowercase hex **and byte-equal to the lowercased cited token**;
`repository` (`owner/repo`); `receipt` (repo-relative); `receipt_sha256` equal to the sha256 of the
receipt's **committed** blob at `HEAD`; and the receipt bytes containing both the hash and the
repository. Every failed binding leaves the token `commit_unresolvable` (fail closed). A line marker
(`owner/repo@`, a repository URL in the row) is never consulted — there is no marker grammar in this
instrument at all.

**Precedence.** lane → fleet → evidence. A manifest entry that pins a *resolvable* commit changes
nothing (control in §6.4): a pin cannot launder a resolvable object.

## 3. Divergences I had to adjudicate (the required finding)

**D1 — identity scope (the load-bearing one; it changed the design twice).** The plan sentence is
literal: *"a resolved report target — path or object — must bind report content identity"*. Applied to
all 111 checked pointers at `b2842231`, that reds **11 live targets**:

```
corpus/README.md:24,26,28,49          rounds 5,1,4,8   (no `## SHONEN`; round 8 is 120 B)
corpus/knowledge/checklist-execution-round15.md:70  round 14 (no `## SHONEN`)
corpus/lessons/round-1-aggregator-audit.md:9, round-1.md:4, round-4.md:4, round-5.md:5,
round-8.md:5, round-9-aggregator-corpus-verdict.md:24   (same rounds)
```
(measured by `/fast/scratch/…/sweep2.py`, superseded by the rule below; E01 reproduced the same 11 —
`build/Kb81E01Integrity/integrity-A-nomanifest.txt`.) Those reports predate the `## SHONEN` heading:
it is uniform from round 19 on (rounds 19–80 all carry it; round 8's report is itself a 120-byte
respawn marker). So the literal reading makes the C1 predicate unattainable at the tip *and* would
re-judge history — a completeness judgment, which the plan itself disclaims ("a report-marker
distinction arm, not a completeness judgment"). **Adjudication: adopt `IDENTITY_FROM_ROUND = 19`,
objects always.** Measured effect on the live corpus: object route applies to exactly one site
(`HEAD:.ufo/reports/round-77/kotoba.md`, 8547 B, `## SHONEN`) and the round-19 rule applies to 0
further path sites that fail identity → `report_dead 0`. E01 reached the same rule independently.

*A rejected intermediate.* My first published bytes scoped identity to the routes the instrument
resolves itself (object + fleet hop) and left explicit path locators existence-only. `Kb81C05Closure`
correctly scored a marker at an explicitly path-cited round-76 report green under that scope. It is
gone from the final bytes; the round-19 rule subsumes it. Recorded because the superseded patch blob
(`7b37461a…`) is still readable in the wave history.

**D2 — receipt content vs receipt digest.** E01 pins the receipt's sha256 and additionally requires
the receipt to name the repository; my predicate requires the digest **and** both the hash and the
repository in the committed receipt bytes. Both bind the single live record
(`7bb48f21…` → `mistralai/mistral-vibe` via `S231.fetch.json`); mine is stricter on a receipt that
is pinned but says nothing about the association. No live divergence; the strictness is deliberate
(Q75: the manifest must be *evidence*, and a pin of an unrelated file is not evidence).

**D3 — manifest reads.** `external-commits.json` and every receipt are read from **`HEAD:`**, never
the working tree. A manifest that is not committed, or a bare JSON list instead of
`{"commits": [...]}`, yields no exemptions (control §6.5). This is E01's contract exactly; my earlier
`repo`/`evidence` aliases and optional pin were removed.

**D4 — exact hash width.** 40 lowercase hex, matched byte-equal against the lowercased token (E01's
`HASH40_RE`). An abbreviated citation of a real commit is `commit_unresolvable` in both gates.

**D5 — `exists` → `isfile`.** The `path` route now requires a file, not any path object, aligning
with the integrity gate's `is_file()`. No live token resolves to a directory.

## 4. Agreement with E01, check for check (composed tree, HEAD `9f3643c`)

Same tree, same rev, both gates run directly (receipts in `build/Kb81E02Independent/`):

| class | Kb81E02Independent | E01 `verify_corpus_integrity.py` |
|---|---|---|
| `index.tracked_files` | 155 | 155 |
| `index.unindexed / stale / missing` | 0 / 0 / 0 | 0 / 0 / 0 |
| `pointers.report_total` | 111 | 111 |
| `pointers.report_dead` | 0 | 0 |
| pointer shapes | absolute 44, bare 65, relative 1, tilde 1 | identical |
| pointer-excluded | 8 | 8 |
| `pointers.commit_total` | 46 | 46 |
| `commit_unresolvable` | 0 | 0 |
| `commit_nonhash` | 0 | 0 |
| `commit_quoted` | 6 | 6 |
| `commit_external` | 2 — `SOURCES.md:171`, `:172` | 2 — same two sites |
| exit | 0 | 0 (`--no-baseline`); 1 default, on baseline cells only |

The one exit-1 in the default form is baseline drift (`tracked_files 155≠154`,
`report_total 111≠109`) — repair R4, not this seat's file. No class count differs.

## 5. Calibration findings (measured, not repaired by me)

**F1 — the plan's base-truth sentence for this gate is not what the base prints.** Plan § C1 says
`verify_corpus_independent.py` is red at base on "`commit_unresolvable` 2 plus `report_dead` 1". Base
`b2842231`, `--repo . --json`, prints `report_dead 0` (receipt
`build/Kb81E02Independent/base-independent-gate-lane-b2842231.json`): the lone `HEAD:` token was
captured as a bare `.ufo/reports/round-77/kotoba.md`, and the fleet's real round-77 report (8547 B,
`## SHONEN`, mtime 17:48 today) satisfies the existing fleet-root hop. The base red is
`commit_unresolvable 2` + `index.unindexed 1`. The plan's 1 is presumably a pre-landing fleet state;
either way the *tip* predicate is unaffected, and after this patch the same token is an object
expression bound to the committed fleet blob.

**F2 — the literal identity sentence is unattainable** (11 sites, §3 D1). Recorded so the L1 can see
that "path or object" was implemented as "path (round ≥ 19) or object", not silently narrowed later.

**F3 — cap arithmetic: declared at freeze vs landed, both recorded.** The plan as it stands when I
read it (`plans/round-81.md`, sha256 `4573a9ba34f1931b465989fccb57010d7a2c7ea27d0f609096d1bd3611558de6`,
mtime 23:37) declares at § C1 line 15 `LINE_CAP` 40→**900** with tight
`(<r72 base blob>, <reviewed r81 blob>)` pin tuples, and line 28's kill rule reads
`base-spent + measured added > 900`. The same plan's E6 justification (line 26) still carries the
freeze-time numbers — `+203/-10` for the integrity gate and `+247/-18` for this file's first
publication, i.e. `+472/-31` cumulative over a `22/3` base spend — while the **landed** bytes measure
`22/3 + 210/10 (E01) + 170/16 (mine) = 402/29`. Both figures are recorded here rather than chosen;
reconciling the superseded `247/18` with the landed `170/16` (my first publication was compressed
before the freeze and re-pinned by E6) is the freeze receipt's business. Under the plan text as it
stands the landed stack fits (402 ≤ 900). An earlier draft of the plan declared 140 and a 60–120 line
estimate for the two-gate repair; the measurement is that one witness alone costs ~170 lines
including its red-before arms, so that draft's bound was not reachable — which is presumably why the
bound moved pre-freeze. (The plan text moved again during the wave — `Kb81E14PinAudit` read sha256
`d6bd43eb…` minutes later — so the citation above is time-stamped by the digest I actually read, not a
summary of it. `Kb81E14PinAudit-final-024145.txt` reconciles the pins: all six instruments in their
tight tuples, `LINE_CAP` 900 fits the measured `+402/-29`, and the independent post-image is
`59602942…`.)

**F4 — the SHONEN epoch.** `## SHONEN` is uniform from round 19 (19–80 checked); rounds 1–17 predate
it. The threshold is therefore a fact about the report corpus, not a convenience: any *new* citation
of a pre-19 report stays existence-only by design, and that is the named residual (§7 R1).

## 6. Controls (all scored on the patched bytes; receipts in `build/Kb81E02Independent/`)

### 6.1 W10-equivalent — a marker substituted for a cited report (the r80 kill)
Fleet-shaped control: `git clone --shared /home/vgpnk/Projects/shokunin fakefleet`, then
`printf 'marker' > .ufo/reports/round-76/kotoba.md`, commit `7cf7f87c` (6 bytes; `git show
HEAD:.ufo/reports/round-76/kotoba.md | wc -c` = 6). Both instruments are run with their `FLEET_ROOT`
constant retargeted at the control fleet by `build/Kb81E02Independent/control-driver.py` (it execs the
instrument's own source with that one constant line replaced, then calls its `main`; the measured
logic is byte-identical otherwise).

| world | command | result |
|---|---|---|
| patched independent | `python3 -B control-driver.py clone/verifiers/verify_corpus_independent.py fakefleet --repo clone` | `report_dead 1` at `corpus/lessons/round-76-verifier-spotcheck.md:14`, exit 1 — `w10-independent-patched.txt` |
| **base independent (ablation)** | same with the base blob of the instrument | `report_dead 0` PASS, exit 1 only on `commit_unresolvable 2` — `w10-independent-base-ablation.txt` |
| patched integrity (E01) | same with `verify_corpus_integrity.py … --no-baseline` | `report_dead 1/111` at the **same** site, 8/9, exit 1 — `w10-integrity-patched.txt` |

The base row is the load-bearing control: the class difference between the two independent runs is
exactly the report identity arm, and E01's gate agrees on the site and the count.

### 6.2 W8/W9-equivalent — a line marker on an absent hash
A citing line carrying `1111…1111` **and** `acme/widget@` **and** `https://github.com/acme/widget`,
with no manifest entry: `unresolvable 1`, `external 2` (unchanged), exit 1 —
`marker-bound-absent-hash.txt`. Markers are not read at all, so this cannot pass.

### 6.3 W6-equivalent — empty / unbound manifests
Bare-list manifest (E01's contract violated): `external 0`, `unresolvable 3` (both SOURCES sites plus
the §6.2 probe), exit 1 — `bare-list-manifest-fail-closed.txt`. A wrong `receipt_sha256` binds nothing
(self-test arm `r81: a wrong receipt pin binds nothing`).

### 6.4 Lane-owned precedence
Manifest entry pinning the resolvable lane commit `b2842231…`, with a committed receipt that names it:
`external 2` (unchanged), `commit_total 46→48`, exit 1 only on the §6.2 probe —
`manifest-pin-lane-owned.txt`. Matches E01's `external/lane-owned-never-external`.

### 6.5 Self-test (my own fixtures, falsifying each arm)
`python3 -B verifiers/verify_corpus_independent.py --self-test` on a pristine base clone with only this
patch: **exit 0, 109 assertions, 0 failures** (`selftest-base-plus-patch.txt`). New arms, all red-before:

- `r81: the receipt-pinned hash is external, the marker-bound one is not` — (external, unresolvable) =
  (1, 1) over a repo holding a pinned 40-hex record and a marker-bound absent hash;
- `r81: absent objects and markers are dead on the object and fleet routes` — (total, dead) = (5, 3):
  an absent object, an object whose committed blob is a marker, and a round-21 fleet marker;
- `r81: a wrong receipt pin binds nothing; a line marker never exempts` — external 0 after the pin is
  corrupted and committed;
- `r81: substituting a marker for a cited report turns it dead` — dead 3→4 when the round-5 report
  blob becomes a marker;
- `pointers: a real fleet report binds identity; a marker would not` — the pre-existing fleet-hop arm,
  whose fixture body was raised to a real report (the old 7-byte `"report\n"` body now correctly dies,
  which is the arm firing).

`report_candidates 121 / report_total 111 / excluded 8` and every pre-existing assertion are
unchanged; the counts moved only where the new arms live (106 → 109 assertions).

## 7. Residuals — named, not repaired

- **R1** A marker at an **explicitly path-cited pre-19 report** stays live (identity is existence-only
  there by adjudication §3 D1). No such marker exists in the corpus and no round-19+ path citation is
  affected.
- **R2** The fleet-root hop uses the module constant `FLEET_ROOT`, as at base; a control that swaps the
  fleet worktree without retargeting that constant is invisible to both corpus gates (unchanged
  behaviour, not this repair's scope).
- **R3** An abbreviated citation (7–39 hex) of a manifest-bound commit is `commit_unresolvable` in both
  gates even when the full hash is bound. Deliberate (§3 D4); it fails closed.
- **R4** `commit_external` is INFO: two absent-but-bound tokens do not make a gate red, and an
  unbindable token is red. A *wrong* repository attribution that still satisfies digest + substring
  (a receipt naming both repositories) is a review question, not a mechanical one.
- **R5** The default (baseline) run of either corpus gate stays red until R4's baseline refresh lands
  (measured cells above). Not this seat's file.
- **R6 (my defect, disclosed, deliberately not fixed in these bytes)** `_committed_blob` is defined
  **twice** in the result: the first definition (with an `ls-files --error-unmatch` guard) is shadowed
  by the second. Behaviour is identical — `git cat-file blob HEAD:<rel>` succeeds only for a path
  present at the measured commit, so the dropped guard changes nothing — and every class count and
  self-test assertion is unaffected (`Kb81C05Closure` found it and re-verified the patched classes on
  these bytes afterwards). I did not remove it: the tip-battery counter that pins this blob is frozen
  (`.ufo/waves/round-81/build/Kb81E05Erratum.*`, tight `INSTRUMENT_PINS` tuples), so any revision now
  makes the tip read `instrument-pin` FAIL for a cosmetic edit. Routed as a one-definition cleanup for
  the next round; independently corroborated by `Kb81Y01Simplify`
  (`build/Kb81Y01-receipts.txt`: two defs, the live one is the copy without the `ls-files` gate, and
  untracked paths already fail at `HEAD:`), which routes the dedupe to w2 rather than a freeze respin.

## 8. Process notes

No tool installs, no host service changes, no pacman. Scratch was `/fast/scratch/hyaku/kotoba-r81/Kb81E02Independent/`
(one clone at the base, one pristine apply-check clone, one fleet clone for the W10 control, fixtures
under `TMPDIR` inside it); at most three concurrent processes. A stray receipt (`/fast/scratch/r81-base-indep.json`)
written outside the seat scratch dir early in the run was copied into the build receipts and deleted;
that is my own defect, recorded here. Every `git` call named `-C <scratch clone>`; the lane was read
only. Scratch removed before yield; receipts were copied into the build dir first.

VERDICT: viable — the external-commit binding and report identity land in the second witness with evidence-bound semantics, 0 live drift on either route, exit 0 composed (E01 9/9, mine 9/9, same class counts), and both r80 kill classes (W8/W9 marker, W10 marker target) red in the patched gate and green in the base ablation; two definitional adjudications (identity scope → round ≥ 19, receipt content check) are divergences from the plan's literal sentence, stated with their measured 11-site cost.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E02Independent.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E02Independent/ (16 receipts); /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E02Independent.md
