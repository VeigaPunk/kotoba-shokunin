# ScribeCorpusR100 — round 100 corpus scribe

Seat: **ScribeCorpusR100** (scribe). Lane: `kotoba-shokunin`. Round 100, wave `r100-w1`.
Scope: `corpus/SOURCES.md` (APPEND rows S282-S285 only) and `corpus/lessons/round-100.md` (new).
Nothing else in the lane was written.

## What landed

**`corpus/SOURCES.md`** — four appended rows (11 columns, no `|` in any cell, opened 2026-11-06,
valid recheck cadence):

| id | source | kind | tier | status | recheck | used-by | `teaches` opens |
|---|---|---|---|---|---|---|---|
| S282 | Python docs `pathlib` @ `docs.python.org/release/3.15.2/library/pathlib.html` | docs | A | mined | on-release | `corpus/lessons/round-100.md` | `supersedes S276 —` — names **both** `Path.is_dir` (raw 1362) and the contrast entry `Path.exists` (raw 1323) |
| S283 | Python docs `tempfile` @ `docs.python.org/release/3.15.2/library/tempfile.html` | docs | A | mined | on-release | `corpus/lessons/round-100.md` | `supersedes S253 —` |
| S284 | Python docs `unittest` @ `docs.python.org/release/3.15.2/library/unittest.html` | docs | A | mined | on-release | `corpus/lessons/round-100.md` | `supersedes S270 —` |
| S285 | `man7.org/linux/man-pages/man2/ptrace.2.html` | docs | A | mined | 180d | `corpus/lessons/round-100.md` | `supersedes S279 —` |

**`corpus/lessons/round-100.md`** (new, 325 lines) — sections `## Gate`, `## Corrections`,
`## Mistakes`, `## Status changes`, `## Considerthese`, `## Settlement`, authored
`ScribeCorpusR100` (curation draft, scaffold; `## Settlement` is the L1's placeholder).

## Gates run (observed output)

| command | observed |
|---|---|
| `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` | `rc=0`, last line `file	ok	…/repo/corpus/SOURCES.md`, **`W04` 35** (34 at the base + exactly one new: `S285 duplicate url man7.org/linux/man-pages/man2/ptrace.2.html across scopes`) — receipt `.ufo/waves/round-100/w1/ScribeCorpusR100/census-scribe.txt` |
| same census against the base `corpus/SOURCES.md` (from `git show HEAD:corpus/SOURCES.md`) | `W04` **34** — the delta is exactly the one expected S285 warning |
| `python3 -B verifiers/verify_corpus_integrity.py` (scratch clone, `--no-baseline`) | `DRIFT corpus.index.tracked_files: observed=206 expected=204`; `DRIFT corpus.index.unindexed: observed=2 expected=0`; `4/9 checks pass` — **the expected landing drift**, see "Out-of-scope drift" below |

Census W04 count = **35** (34 base + 1 for S285 sharing S279's URL). No `E01`-`E12` finding: the four
rows have 11 columns (NF=13), no duplicate id, kind/tier/status enums valid, `opened` an ISO date
not in the future, `recheck` valid (`on-release` symbolic, `180d`), and no duplicate-URL **within**
a scope (each new row's `teaches` opens `supersedes S0NN —`, which the census's `E04` exemption
requires). The `mined` rows' `used-by` path `corpus/lessons/round-100.md` exists in the same patch,
so no `E11`.

## Sources opened (bytes fetched by this seat, not taken from the receipt)

All four URLs were fetched three times by this seat on 2026-11-06 (12:28Z, 12:33Z, 12:44Z) with
`curl -sS -L`; the digests are identical across the three fetches and reproduce the L1's frozen
receipt `receipts/sources-opened.txt` byte for byte. Receipt:
`.ufo/waves/round-100/w1/ScribeCorpusR100/sources-fetch.txt`.

| row | URL | HTTP | bytes | sha256 |
|---|---|---|---|---|
| S282 | `https://docs.python.org/release/3.15.2/library/pathlib.html` | 200 | 270630 | `090f3b03b648c271f4d810f0c37a51b2b54ebbdaa8130466d695e836e7a399ca` |
| S283 | `https://docs.python.org/release/3.15.2/library/tempfile.html` | 200 | 74630 | `0eef90989f9e1e4d261b8259e620244270f0bb8773e6b56b221b9575df60ab41` |
| S284 | `https://docs.python.org/release/3.15.2/library/unittest.html` | 200 | 336394 | `90fb380940f290ed6611ab8907a0f11840d03cea258357b5b3702a6b2eba8387` |
| S285 | `https://man7.org/linux/man-pages/man2/ptrace.2.html` | 200 | 104833 | `69cd309ece177d54086771701b2085e31cabd14a92484647392bcda468f7bd35` |

Located quotes (each ≤25 words, each `printf '%s\n' … | wc -w` counted, each verified to occur
exactly once on its page after tag-stripping, and each located at a stated HTML line):

- S282 — "False will be returned if the path is invalid, inaccessible or missing, or if it points to
  something other than a directory." — **22 words**, HTML lines 1364-1366 (§ `pathlib.Path.is_dir`,
  `dt` at HTML line 1362); **and the contrast entry** "Return True if the path points to an existing
  file or directory and False if the path is invalid, inaccessible or missing." — **22 words**, HTML
  lines 1325-1326 (§ `pathlib.Path.exists`, `dt` at HTML line 1323). Both occur exactly once, and
  the pair is what carries the contrast the t04 mutant exploits.
- S283 — "If ignore_cleanup_errors is true, any unhandled exceptions during explicit or implicit
  cleanup (such as a PermissionError removing open files on Windows) will be ignored" — **24 words**,
  HTML lines 389-391 (§ `tempfile.TemporaryDirectory.cleanup`, `dt` at HTML line 386).
- S284 — "Each tuple represents a test which raised an unexpected exception." — **10 words**, HTML
  lines 2413-2414 (§ `unittest.TestResult.errors`, `dt` at HTML line 2410); counterpart "Each tuple
  represents a test where a failure was explicitly signalled using the assert\* methods." — **15
  words**, HTML lines 2421-2422 (§ `unittest.TestResult.failures`, `dt` at HTML line 2418).
- S285 — "the caller does not have the CAP_SYS_PTRACE capability in the user namespace of the target
  process" — **16 words**, HTML lines 1518-1520 (access-check algorithm step (4)); its first conjunct
  (14 words) at 1516-1517 and step (3)'s permissive disjunct (13 words) at 1513-1514.

### The digest reason, measured (why the pinned rows supersede the rolling-alias rows)

The three Python rows cite the **version-pinned** `release/3.15.2/` snapshots because the rolling
`/3/` aliases the superseded rows cite are build stamps, not content identities. Measured today:

- **S253 → S283 (tempfile):** the alias `https://docs.python.org/3/library/tempfile.html` served
  HTTP 200, **75198 B**, sha256 `2bef9acd…` — eight bytes *longer* than the 75190 B S253 recorded, so
  the rolling build's **content** moved as well as its footer.
- **S270 → S284 (unittest):** the alias served HTTP 200, 336978 B, sha256 `a3c45299…` — the same byte
  count S270 recorded but a different digest, and the difference is **provably the footer alone**:
  substituting S270's footer string (`Last updated on Nov 05, 2026 (22:32 UTC)`) into the alias bytes
  reproduces S270's recorded digest `f9510cd7d7a67a32fb891016cbb42bf1dfcb80a370c689ed222058acbff3506d`
  **exactly**.
- **S276 → S282 (pathlib):** the alias served HTTP 200, 271233 B, sha256 `eda0d4a5…` — a different
  byte count and digest from the pinned page, and the two byte streams differ in the page metadata
  (the alias carries the 3.15 social-preview images, the pinned release the static preview).
- **S279 → S285 (ptrace):** the page's bytes are **unchanged** — the pinned digest equals S279's own.
  The supersession is not a digest fix here; it is the **quote** fix (round-99 `C99-3`): S279's
  located quote stops before the parenthetical carrying `SUID_DUMP_USER` and `CAP_SYS_PTRACE`, so it
  carries only the first conjunct of step (4), while step (3) carries the permissive disjunct. S285
  quotes the whole conjunction.

### One REJECT (opened, not rowed)

**Sphinx `literalinclude`'s `:lines:` option** —
`https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html` — HTTP 200, 170372 B,
sha256 `0607fc1b47e0546a247cc9fd66bc7e98e141a1c7a652e9033fa889c5230dce2b` (12:44Z) vs
`d629d47b0aef1ab9ef2f8e30e59f3fbb37a31ad803544d912897937c676af5b3` (12:28Z) — the two byte streams
differ in **exactly one line** (HTML line 1620, whose Cloudflare e-mail-protection token rotates per
response). Located quote "line numbers (comma separated numbers)" — **5 words**, HTML line 1421 (the
`:lines:` option signature; `dt` at 1420; the same wording recurs at 1166 and 1379 for
`:emphasize-lines:`, so a match must carry the option name).

**REJECTED:** it is the closest external candidate for a comma-list line anchor, but it is a
document build's *source-inclusion filter*, not a citation-anchor convention for a repository's
governance files — it selects which lines of an included file to paste into generated documentation,
and its own example (`1,3,5-10,20-`) admits ranges and open-ended ranges that the lane's anchor form
does not. The lane's `file.md:30,37` form is the lane's own convention, carried by `SKILL.md` and read
by the lane's own checklist gate; an external tool's inclusion syntax is not its authority. The page
is also not digest-stable — the same defect this round's superseding rows repair.
**Flip:** a round that defines the lane's comma-list anchor grammar by reference to an external
specification rather than by the lane's own `SKILL.md` usage and checker would make this page the
authority, and it would have to be re-read from a pinned (non-`master`) URL first. **Not rowed**
because this seat's `corpus/SOURCES.md` ownership is rows S282-S285 only; the rejection is recorded
in the lesson's `## Gate` (contract rule 1) and the L1 may row it as S286.

## Correction C100-1 (the mined mistake)

`corpus/lessons/round-99.md:88` cites `verifiers/check_tip_battery.py:344` for the
`git rev-parse <rev>:<path>` read. Line 344 is that read **at the round-99 base**
`52e8e95ac4faf4ded84d7b82cbc204792590d0f7`; at the round-99 tip
`0a65cceb5b8fa5bb25a095828a1e6cd0e3681ee3` it is line **349**. Verified read-only with
`git show <rev>:<path> | sed -n Np` (receipt
`.ufo/waves/round-100/w1/ScribeCorpusR100/c100-1-correction.txt`):

```
$ git show 52e8e95a:verifiers/check_tip_battery.py | sed -n 344p
        got = git(clone, "rev-parse", "%s:%s" % (rev, path))
$ git show 0a65cceb:verifiers/check_tip_battery.py | sed -n 349p
        got = git(clone, "rev-parse", "%s:%s" % (rev, path))
$ git show 0a65cceb:verifiers/check_tip_battery.py | sed -n 344p
            failures.append(("instrument-size", "binary diff at %s" % path))
```

Corrected form: `52e8e95a:verifiers/check_tip_battery.py:344` =
`0a65cceb:verifiers/check_tip_battery.py:349`. The tip's line 344 carries no `rev-parse`, so the
mistake is **shown able to fail** by that one-line command. The round-99 lesson's bytes are not
edited (append-only; the round-99 seat owns that file); the correction is a new entry, as the round-99
and round-98 lessons do.

Mistake row: class `line-pointer-cited-at-base-revision`, evidence
`corpus/lessons/round-99-verifier-spotcheck.md` § Routed defects item 1 (the closure measured the
same drift independently: "line 344 at base, line 349 at tip"), captured-by **none** (no lane
instrument captures it), fix = C100-1 + a QUALITY criterion, which the **L1 adds as Q90** at
settlement (this seat does not write `corpus/QUALITY.md`).

## Status changes

**None.** No existing row's `status`, `recheck` or `used-by` cell was changed — S253, S270, S276 and
S279 are re-opened and deliberately **not** edited; the repair for each is the new superseding row
(contract rule 2). The lesson's `## Status changes` says so explicitly.

## Considerthese

`considerthese/2026-10-26.md` re-read (newest file in `considerthese/`; proposals only, nothing
implemented by this seat). All five proposals are still unimplemented at the freeze
`03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`, measured in the scratch clone:
`SKILL.md` 600 lines / 92672 B with 165 lines over 120 chars, 94 over 300, longest 1491 chars at
line 518; `verifiers/floors-registry.json` holds 19 instrument rows, none a byte or line ceiling on
`SKILL.md`; `## Gate registry` sits at `SKILL.md` line 443 and `verifiers/REGISTRY.md` does not
exist; the frontmatter description is still 1021 chars with a 151-char first sentence and `SKILL.md`
is at 600 of 600; wave `r100-w1` carries 11 seats of which 6 are attack seats (2 reviewers, 2
mutation-testers, 1 critic, 1 sentinel); `.ufo` is 355 MB of a 596 MB working tree. **Assimilation:
none** — no proposal is newly implemented this round and none is trivially citable as a registry row,
so no row was written for any of them.

## Out-of-scope drift (not a C1 or C2 failure)

The corpus gates stay red at the candidate, as the plan anticipates: the closure-landed
`corpus/lessons/round-99-verifier-spotcheck.md` is unindexed, and this seat's new
`corpus/lessons/round-100.md` is unindexed too until the L1 adds the coverage-map rows and
re-records `verifiers/corpus-baseline.json` at integration. The C2 counter does not read the corpus
gates, so this drift is landing no-harm work (Q89), not a claim failure.

## Findings

1. **A counter defect was not found.** The C1 and C2 counters were run against this seat's scratch
   candidate and their readings are recorded in `.ufo/waves/round-100/w1/ScribeCorpusR100/c1-scribe.txt`
   and `…/c2-scribe.txt`. No predicate was rescued or edited by this seat; the counters and the plan
   are untouched.
2. **The C1 counter reads `C1-PREDICATE-UNMET` at this seat's candidate — correctly so, and it is
   not a failure of this patch.** The reading is `C1 targets killed 0 of 6 (run errors 0); positive
   killed 1 of 1; honest CLEAN; comment decoys held 6 of 6; code decoys held 6 of 6` — the same
   tally as the frozen red-before at the base (`receipts/redbefore-c1-base.txt`). The reason is
   scope, not defect: **the six C1 self-test arms land in `ExecArmsR100`'s patch**, not in this
   seat's. This seat's patch touches `corpus/` only, so the counter's reading is a **no-harm
   check**: it confirms the corpus change moves the C1 counter by nothing at all (honest runs CLEAN,
   positive killed, all six decoys held, `run errors 0`). C1 can only reach
   `C1-PREDICATE-MET` at the landing revision, where all three builder patches are applied in the
   order ScribeCorpusR100 → ExecAnchorR100 → ExecArmsR100.
3. **`W04` count = 35** (34 base + 1 for S285/S279 sharing the ptrace URL), as the item predicted.
   The superseding rows keep it a warning rather than an `E04` because each opens
   `supersedes S0NN —`.
4. **The C2 truth table's environment is sensitive to the corpus-gate state**, not to the registry:
   the counter builds its sandbox from the *round-base* bytes of `check_tip_battery.py`, so the
   candidate's own corpus drift does not reach it.
5. **The round-99 lesson's stale pointer is the only line-pointer defect the corpus carries today**;
   the lesson's own `## Gate` cites `verifiers/check_tip_battery.py:344` at line 88, and the closure
   measured the same drift at its own revision.
6. **One word count in the first draft of S285's anchor was wrong and was corrected before the
   patch was frozen.** The step (3) permissive disjunct "The caller has the CAP_SYS_PTRACE
   capability in the user namespace of the target." is **13 words**, not the 16 first written; every
   quote's word count in the final `corpus/SOURCES.md` and `corpus/lessons/round-100.md` was then
   re-verified against the fetched bytes by script (claimed == actual, and each quote's occurrence
   count == 1), and the patch was regenerated. The Sphinx REJECT quote is the one deliberate
   exception: "line numbers (comma separated numbers)" occurs **3** times on that page (the
   `:emphasize-lines:` option carries the same wording at HTML lines 1166 and 1379), which both the
   row and the lesson state, so a match must carry the option name.
7. **The scout's material finding was acted on: S282 now names BOTH `Path.is_dir` and
   `Path.exists`.** `ScoutSourcesR100` § 3.2 / § 8 item 1 flagged that the plan's S282 line (and
   the L1's opened receipt `receipts/sources-opened.txt`) quote `Path.is_dir` alone, while the t04
   mutant (`is_dir()` → `exists()`) needs the **contrast**: `is_dir` says a plain file is not a
   directory, but only `exists` — "Return True if the path points to an existing file **or
   directory**" — carries the half that shows the mutant's replacement behaves differently. Both
   entries are on the same page under the same digest, so no second row is needed; **S282's `anchor`
   cell now names both anchors** (`Path.is_dir` @ raw 1362 and `Path.exists` @ raw 1323), its
   `scope` cell names the pair, and its `teaches` cell carries the contrast. This seat **re-opened
   the page in its own bytes before acting** (not taking the scout's finding on trust): `Path.exists`
   id at raw **1323**, body **1325-1326**, quote "Return True if the path points to an existing file
   or directory and False if the path is invalid, inaccessible or missing." — **22 words**,
   occurring **exactly once** on the page — all confirmed against this seat's own fetch.
8. **The line-number trap was already avoided.** `ScoutSourcesR100` § 4.2 warns that the same
   pages sit at different raw HTML line numbers on the rolling `/3/` alias and on the pinned
   `/release/3.15.2/` URL, and that the existing rows quote the **alias** numbers. This seat's four
   rows were written from the **pinned** bytes and cite the pinned numbers throughout — `is_dir`
   1362 / 1364-1366, `exists` 1323 / 1325-1326, `cleanup` 386 / 389-391, `errors` 2410 / 2413-2414,
   `failures` 2418 / 2421-2422, `ptrace` step (4) 1516-1520 — and each was re-verified by script
   against this seat's own fetch. No alias number was copied into a frozen cell.
9. **The scout reached the same REJECT verdict on the Sphinx candidate, by a second route.** Its § 5
   rejects it for the same first reason (a directive *option value*, not a `path:N,M` citation
   token) and adds that the **real ground is already in the lane** — `SKILL.md:116`'s
   ``(S090 `:10,18,34,40-42`)`` and `corpus/QUALITY.md:50`'s
   `corpus/lessons/round-55-verifier-spotcheck.md:82,135` (both `own-work`, tier A). This seat
   added that ground to the lesson's `## Gate` REJECT entry and **verified both citations in the
   lane's own bytes** (`sed -n 116p SKILL.md` → the comma list with a range;
   `sed -n 50p corpus/QUALITY.md` → `:82,135`) before writing them. The lesson also records the
   `git-log(1)` counter-example the scout supplies, so a future reader cannot conclude the comma
   always means a list.
10. **Neither frozen counter has a defect.** The scout re-derived the C2 truth table by hand
    (§ 7) and it agrees with the frozen base receipt on all eight comma rows; the C1 anchor-hygiene
    check found no frozen anchor missing. This seat's own C1 and C2 runs at the scratch candidate
    read **byte-identically** to the frozen base receipts — the expected no-harm signature for a
    `corpus/`-only patch. The C2 comparison, verbatim:
    ```
    base   (receipts/c2-base.txt): C2 mismatches 8 of 28; gate GREEN; self-test HELD; revert mutant ABSENT; frozen 2 of 3; battery ok
    scribe (c2-scribe.txt):        C2 mismatches 8 of 28; gate GREEN; self-test HELD; revert mutant ABSENT; frozen 2 of 3; battery ok
    ```
    and the C1 comparison:
    ```
    base   (receipts/redbefore-c1-base.txt): C1 targets killed 0 of 6 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 6 of 6; code decoys held 6 of 6
    scribe (c1-scribe.txt):                C1 targets killed 0 of 6 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 6 of 6; code decoys held 6 of 6
    ```
    The C2 verdict is `C2-PREDICATE-UNMET` at this seat's candidate for the same scope reason as
    C1's: the C2 fix line, its self-test arm and the retirement of the one correction row land in
    `ExecAnchorR100`'s patch, not in this seat's. C2 can only reach `C2-PREDICATE-MET` at the landing
    revision, where all three builder patches are applied together.

## Patch and handoff

- Patch: `.ufo/waves/round-100/w1/ScribeCorpusR100/ScribeCorpusR100.patch`
  — sha256 `042c22700eb5b0ac343686ba67cbaf6ba77acbcabdbccf234d971b964ccc67d1`,
  `git diff --binary 03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687` from the scratch clone
  `/fast/scratch/hyaku/kotoba-r100/ScribeCorpusR100/repo` (scratch identity
  `scratch <scratch@invalid>`, scratch commit `8ed224c5be89b112d3d93a377b2050d7add20004`).
  Stat: `corpus/SOURCES.md | 4 +`, `corpus/lessons/round-100.md | 347 +` — 351 insertions, 0
  deletions.
- **Apply proven**: on a *second* fresh scratch clone at `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`
  (`git -C "$D2" rev-parse --show-toplevel` = that clone), `git apply --check` returned 0 and
  `git apply` reproduced files **byte-identical** to the scratch clone's (`diff` on both
  `corpus/SOURCES.md` and `corpus/lessons/round-100.md` → no differences). That clone was then
  removed.
- **No lane git/jj mutation was performed.** The lane repo was read only
  (`git show`, `git log`, `git rev-parse`, `git status`, `git ls-files`, `grep`).
- **No file outside the owned scope was written**: no `corpus/README.md`, no
  `verifiers/corpus-baseline.json`, no `LOG.md`, no `SCORECARD.md`, no `corpus/QUALITY.md`, no
  `SKILL.md`, no `verifiers/*`.

## Receipts (this seat's directory)

`.ufo/waves/round-100/w1/ScribeCorpusR100/`

- `ScribeCorpusR100.patch` — the patch (sha256 above).
- `census-scribe.txt` — `sources-census.sh validate` output, rc 0, `W04` 35.
- `sources-fetch.txt` — the access record (URL, HTTP, bytes, sha256 × 3 fetches) for S282-S285 and
  the REJECT candidate.
- `c100-1-correction.txt` — the three `git show … | sed -n Np` readings and the grep of the round-99
  lesson's stale citation.
- `c1-scribe.txt` — the C1 counter's reading at this seat's scratch candidate (no-harm reading; the
  six C1 arms land in `ExecArmsR100`'s patch).
- `c2-scribe.txt` — the C2 counter's reading at this seat's scratch candidate.
- `scout-crosscheck.txt` — this seat's cross-check against `ScoutSourcesR100.md`: the material
  `Path.exists` finding re-verified in this seat's own bytes before it was acted on, the
  line-number trap checked, the REJECT verdict cross-checked against the lane's own `own-work`
  ground, and the digest findings confirmed.

## Tooling

No package was installed, upgraded or removed this round; no tool channel was touched. The seat used
only the tools already present on the host (`git`, `curl`, `sha256sum`, `python3 -B`, `awk`, `sed`,
`grep`, `diff`, and the fleet's `scripts/sources-census.sh`). No `pacman` transaction of any kind
(host-wide pause honoured); no `uv tool`/`npx`/binary install was needed.

## Checks the main agent should run

1. `git apply --check` the patch on a fresh clone at `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687` and
   confirm the two files match.
2. After the three builder patches are applied in the order ScribeCorpusR100 → ExecAnchorR100 →
   ExecArmsR100, run the two counters at the candidate revision:
   `python3 -B verifiers/fixtures/round-100/selftest-kills.py c1 <rev> "$D"` and
   `python3 -B verifiers/fixtures/round-100/anchor-lists.py <rev> "$D"`.
3. `scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` → expect rc 0 and `W04` 35.
4. L1 integration steps this seat did **not** perform (by ownership): add the coverage-map rows for
   `corpus/lessons/round-100.md` and `corpus/lessons/round-99-verifier-spotcheck.md` to
   `corpus/README.md`; re-record the three equal-mode counts of `verifiers/corpus-baseline.json`
   after every corpus file of the landing tree is in place; add QUALITY **Q90** for the
   `line-pointer-cited-at-base-revision` mistake; decide whether the rejected Sphinx candidate
   becomes row S286.
