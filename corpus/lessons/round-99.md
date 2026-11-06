# Round 99 — kotoba (Linux host, omp): lesson

Author: **ScribeCorpusR99** (curation draft, scaffold). A seat review is lane evidence, not the
independent non-author admission judgment; the L1 (KotobaR99) integrates and settles, and
`## Settlement` is its placeholder.

Round: 99, plan `plans/round-99.md` (frozen at `b53e209603e7c480cd975ea543e415b66f695438`), base
`52e8e95ac4faf4ded84d7b82cbc204792590d0f7`, instrument commit
`c0489d14156a7687d10ae5389d72eaa923b2bc29` (the v6.1 counter
`verifiers/fixtures/round-99/selftest-kills.py` and the C2 runner
`verifiers/fixtures/round-99/carried-reds.py`). Pre-data receipts (frozen with the plan, before any
scored reading): `.ufo/waves/round-99/receipts/` — `redbefore-c1-base.txt` (`C1 targets killed 0 of
12`, `C1-PREDICATE-UNMET`), `redbefore-c1-base-rulesv5.txt`, `poscontrol-r98c1-base.txt` and
`poscontrol-r97c1-base.txt` (MET), `c2-base.txt` (`carried reds green 0 of 3`,
`C2-PREDICATE-UNMET`), the five C2 forgery controls `c2-ctl-w1..w5.txt` (all UNMET), and
`sources-opened.txt` (the S281 access record, taken on the rolling `/3/` alias — superseded by the
version-pinned URL the row cites; see § Gate and § Corrections C99-4).

## Gate

Candidates considered, with the decision and the reason. The access record below is this seat's own
re-fetch on 2026-11-06 (`curl -sS -L`, then `sha256sum`), cross-checked against the frozen L1
receipt `receipts/sources-opened.txt` and against `ScoutSourcesR99.md` § 1.

- **S281 — Python documentation, `argparse`
  (`https://docs.python.org/release/3.15.2/library/argparse.html`). Admitted** as tier A, kind
  `docs`, status `mined`, opened 2026-11-06, recheck `180d`, used-by
  `corpus/lessons/round-99.md,plans/round-99.md`.
  - Access record (the row's URL, the version-pinned snapshot): 2026-11-06; HTTP 200; **327874 B**;
    sha256 `36e8d5361b591376bbf9255c08147ece82f5f1fe52a5abd3d149656e902bb8ae` — identical across
    five fetches (13:54Z–14:13Z; `ScoutSourcesR99.md` § 1.1 and § 1.4), and reproduced by this
    seat's own fetch at 2026-11-06T14:20:27Z. The page's own version pin is "Python 3.15.2
    documentation" (HTML line 19) and its footer reads `Last updated on Oct 25, 2026 (17:03 UTC)`
    (HTML line 2709).
  - HTML line excerpt, **HTML lines 989-990** (the `'append'` list item of the `action` section,
    whose `<section id="action">` opens at **HTML line 953**):
    ```
    <li><p><code class="docutils literal notranslate"><span class="pre">'append'</span></code> - This appends each argument value to a list.
    It is useful for allowing an option to be specified multiple times.
    ```
  - Located quote (≤25 words): "'append' - This appends each argument value to a list. It is useful
    for allowing an option to be specified multiple times." — **22 words**
    (`printf '%s\n' "<quote>" | wc -w` → 22), at **HTML lines 989-990**, quote-equal after the
    rendered `<span class="pre">` code span is folded to its text. The sentence occurs **exactly
    once** on the page (`grep -c` → 1); the bare marker `'append'` occurs **twice** (HTML lines 989
    and 1062), so a quote match must carry the surrounding words, not the marker (`ScoutSourcesR99`
    F4).
  - **The L1's `/3/` access, superseded by the pin (reason).** The frozen receipt
    `receipts/sources-opened.txt` records the rolling alias
    `https://docs.python.org/3/library/argparse.html`: HTTP 200, 334994 B, sha256
    `bcd717f244b432fbee39f45742910347599f5f8b9f1dc6d4377a23c5c8faac16`, quote at HTML lines 992-993,
    22 words. That access is **real but not re-fetchable**: `/3/` is a rolling build whose 5-byte
    `Last updated on ... (HH:MM UTC)` footer changes on every upstream docs rebuild, so the
    recorded digest goes stale within the hour. Measured here (this seat, 2026-11-06T14:17:07Z):
    the alias serves HTTP 200, 334994 B, sha256
    `906919fda1b652a56d07a61823ce6e169ae6acfd2afa3233a56d3c26bf4e732e`, and the two byte streams
    differ in **exactly five bytes** — the footer minute field at HTML line 2712 (`13:27` in the
    receipt's bytes, `13:47` in today's); substituting only that field reproduces the receipt's
    digest exactly (`sed 's/(13:47 UTC)/(13:27 UTC)/' | sha256sum` →
    `bcd717f244b432fbee39f45742910347599f5f8b9f1dc6d4377a23c5c8faac16`), and `diff` reports one
    differing line. The quote, its 22 words and its line numbers (992-993) are identical in both
    builds. **The row therefore cites the version-pinned `/release/3.15.2/` URL** (frozen release
    snapshot, digest stable over five fetches) as its access record, and names the rolling alias
    and its digest in the anchor cell as the superseded reading — L1 ruling
    `plans/round-99-addendum-1.md` A1, on `ScoutSourcesR99` F1. The alias is not a second row: it
    is the same document at a moving URL.
  - **What this row adds**: the registry held no `argparse` row — `grep -rn "library/argparse.html"
    corpus/` → no hits, and the single "argparse" hit is **S211**, a `kind=code` row on a GitHub
    URL about a different document (`ScoutSourcesR99` F5) — so this is a first row on a new URL and
    it adds **no** `W04`. It grounds **C1's t08 arm**'s stdlib half:
    `verifiers/verify_dispatch_prompts.py:527` declares `--check` with `action="append"`, and
    `verify_dispatch_prompts.py:1715` reads
    `wanted = list(args.check) if args.check else list(CHECK_IDS)` — the exact line the
    **t08-main-check-ignored** mutant replaces with `wanted = list(CHECK_IDS)`
    (`verifiers/fixtures/round-99/selftest-kills.py:148-150`). The page is the authority for what
    `action="append"` *means*; it is **not** the authority that the lane then honours `args.check`,
    which is the lane's own code and which the arm's kill must come from observing `main()`'s
    behaviour.
  - Bound: the page states the accumulation semantics of the `append` action; it says nothing about
    this instrument's check ids (`CHECK_IDS = ("dispatch.04", "dispatch.08")`,
    `verifiers/verify_dispatch_prompts.py:102`), its default, or its exit code. Those are the
    lane's production code, read at the lane, not the page's claim.
- **Lead — `git-hash-object(1)`, not rowed.** `ScoutSourcesR99` § 3 screened
  `https://git-scm.com/docs/git-hash-object` (2026-11-06, HTTP 200, 29933 B, sha256
  `b7e8f95355c38df94c9355d31b0ed985d5c22cb5ca7c4d640364c801100eb798`, stable over three fetches;
  the registry holds no such URL). The scout **rejects** it as C2's authority: the
  `INSTRUMENT_PINS` admission reads the pin out of a committed tree via
  `git rev-parse <rev>:<path>` (`verifiers/check_tip_battery.py:344`), not by hashing a file — the
  authority for that mechanism is **S267** (`gitrevisions(7)`) and **S268** (`git-cat-file(1) -e`),
  both already in the registry. The fact `hash-object` grounds (an object ID is computed from a
  file's contents with a stated type, defaulting to `"blob"`, and the `--path` filter caveat) is
  real but is not a fact this round's claims rest on, so no row is minted for it: a lead is not
  evidence and never a row. Flip: a round that computes a pin value from a working-tree file.

**Census.** `scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` → rc 0, `file ok`,
`W04` **34** (unchanged — the argparse URL is unique across scopes). Rows 206 → 207.

## Corrections

Named, append-only correction entries. A frozen receipt is never edited; a correction is a new entry
that points at it.

- **C99-1 — the round-98 report's line count for `self_test()`.** The round-98 fleet report's
  landed-changes row (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-98/kotoba.md`, the
  `e61629f5d582e5518ccfe023c62d1fd26dd1870d` row) reads "+183 lines inside `self_test()`". The
  measured insertion is **182** lines: `git diff -U0 a33f262fc94e3cf27f3c935b5c53c1336bb94166
  e61629f5d582e5518ccfe023c62d1fd26dd1870d -- verifiers/verify_dispatch_prompts.py | grep '^@@'`
  → `@@ -1333,0 +1334,182 @@ def self_test() -> int:`. **183** is the *two-file* total:
  `git diff --numstat` for the same pair gives `182 0 verifiers/verify_dispatch_prompts.py` and
  `1 0 corpus/QUALITY.md` (the Q88 row). The report's bytes are filed and are not rewritten here;
  this entry names the number the diff supports.
- **C99-2 — the SCORECARD round-98 C1 annotation names the wrong revision for the red-before.**
  `SCORECARD.md`'s round-98 axis annotations read "`C1-PREDICATE-UNMET` rc 1 at the freeze
  `63cd48d9` (`.ufo/waves/round-98/receipts/redbefore-c1-base.txt`)", but that receipt's own
  command line measures the **instrument** revision
  `a060b450a43673ebc54720a5192e99df188e80ce`, not the freeze. The value itself stands — the two
  revisions carry byte-identical `verifiers/verify_dispatch_prompts.py`
  (`git cat-file -p 63cd48d9:verifiers/verify_dispatch_prompts.py | sha256sum` and the same for
  `a060b450` both read `1e67db315d22b41cfe4760983708af7815860a926f6ad5f9f25137d12110690f`), so
  `C1 targets killed 0 of 9` measured at either revision is the same measurement. The correction is
  to the *named revision* only.
- **C99-3 — S279's located quote stops before step (4)'s second conjunct.** The `ptrace(2)` row
  S279 anchors its denial on step (4)'s first clause: the located quote is "Deny access if the
  target process "dumpable" attribute has a value other than 1" (14 words) at HTML lines 1516-1520,
  and the anchor cell says so — "stopped before the parenthetical on SUID_DUMP_USER and
  CAP_SYS_PTRACE". The conjunct that follows is load-bearing: the same page's HTML lines 1518-1520
  read "the caller does not have the CAP_SYS_PTRACE capability in the user namespace of the target
  process" — **16 words**
  (`printf '%s\n' "<quote>" | wc -w` → 16), quote-equal after the `<b>` markup around
  `CAP_SYS_PTRACE` is removed and the whitespace folded. The rule is a **conjunction**, so a reader
  working from the truncated quote alone would read step (4) as "non-dumpable ⇒ deny" and miss that
  the caller must also lack the capability; the same algorithm's step (3) carries the *other*,
  permissive `CAP_SYS_PTRACE` disjunct at HTML lines 1513-1514 ("The caller **has** the
  CAP_SYS_PTRACE capability in the user namespace of the target."), so a fragment must not be able
  to flip either. This is the round-98 closure's routed defect 5
(`corpus/lessons/round-98-verifier-spotcheck.md` § Routed defects item 5; `ScoutSourcesR99` F2). The page's
  bytes are re-opened and re-verified here (2026-11-06, HTTP 200, 104833 B, sha256
  `69cd309ece177d54086771701b2085e31cabd14a92484647392bcda468f7bd35` — **identical to the digest
  S279 itself records**, so this page, unlike the argparse one, is stable and its anchor
  re-verifies). The row's `teaches` cell already states the conditional correctly; what is short is
  the *quote*. This seat does not amend S279: the registry is append-only and this seat's ownership
  of `corpus/SOURCES.md` is the S281 row, so the registry-form correction (a new row whose
  `teaches` opens `supersedes S279 —`) is the L1's call. Until it lands, this entry is the record
  of the conjunct.
- **C99-4 — the S281 digest is not stable across documentation rebuilds.** The L1's frozen receipt
  records `bcd717f244b432fbee39f45742910347599f5f8b9f1dc6d4377a23c5c8faac16` for the **rolling
  alias** `https://docs.python.org/3/library/argparse.html`; this seat's re-fetch on the same day
  records `906919fda1b652a56d07a61823ce6e169ae6acfd2afa3233a56d3c26bf4e732e` for the same 334994 B.
  The two byte streams differ in exactly five bytes — the page's own `Last updated on Nov 06, 2026
  (HH:MM UTC).` footer at HTML line 2712 — and restoring the receipt's footer string reproduces the
  receipt's digest exactly. The quoted passage, its word count (22) and its line numbers (992-993)
  are identical in both. A digest recorded against a rolling documentation alias is therefore a
  build stamp, not a content identity; the row records the version-pinned URL as its access record
  and names the alias reading as superseded (§ Gate), and the drift is measured, not assumed.
  **The same mechanism already sits on three registry rows** — S253 (`/3/library/tempfile.html`,
  whose recorded 75190 B also differs in length from today's 75198 B, so content moved as well),
  S270 (`/3/library/unittest.html`) and S276 (`/3/library/pathlib.html`), each provably broken by
  the footer field alone (`ScoutSourcesR99` F1). **No registry edit is made for them this round:**
  `corpus/SOURCES.md` is append-only and their protected cells may not change in place, so the
  only correct repair is a new superseding row whose `teaches` opens `supersedes S0NN —` — a round-100
  routing, not this round's claim. The bound is named so a later reader does not read a digest
  mismatch as a content change.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `governance-cell-cites-fleet-path-repo-rooted`: rounds 82+ wrote governance cells in `LOG.md` and `SCORECARD.md` that cite fleet-root files as repo-rooted — the fleet report path written with the lane-rooted prefix, e.g. ".ufo/reports/round-82/kotoba.md", and likewise ".ufo/watchdog.log" and ".ufo/l0-questions.md" — when the file exists only at the fleet root — the lane's own convention (round-57/58/59 rows, the round-65 correction rows) is the `../` hop, so each of those cells is a citation that resolves to nothing from the lane root | `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-98/w1/ScoutTipReds.md` § 2.1 row 4 (the 16 unique subjects introduced by `747a07c` (r82), `84c2963`/`d84c7c8` (r83), `462d240` (r84), `d1c0318` (r87), `010d3b8` (r92), `38361a2` (r97)) and § 4 F6 (the normalized red) | `governance.citation_resolves` — it *did* fire and name the offending cells; what did not catch it is the landing no-harm rule, which since round 92 accepts "the base red set" as a conjunct, so the red never heals and the class keeps growing (the checklist gate is red since round 81's record `23e838c` and `verify_corpus_integrity.py`/`verify_corpus_independent.py` since round 88) | claim **C2** (the three carried tip-battery reds read green at the landing without weakening a gate) **plus a QUALITY criterion** that a landing's no-harm reading requires the carried-reds counter MET, not "red set unchanged" — the L1 adds **Q89** for this round. Shown able to fail: `.ufo/waves/round-99/receipts/c2-base.txt` reads `C2 carried reds green 0 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` and `C2-PREDICATE-UNMET` rc 1 at the round base — the same bytes the criterion would have to accept at a landing |

## Status changes

- **None.** The registry is append-only and this seat's ownership of `corpus/SOURCES.md` is
  append-rows-only: **S281 is a new row** (`mined` at opening, 2026-11-06, tier A, kind `docs`,
  recheck `180d`, used-by `corpus/lessons/round-99.md,plans/round-99.md`), and **no existing row's
  `status`, `recheck` or `used-by` cell was changed** — so there is no old→new pair to log here.
- **S279 — re-opened, deliberately not edited.** The re-open (above, C99-3) confirmed the row's own
  digest byte for byte and located the conjunct its quote stops before; the cell change that would
  carry the conjunct into the registry is a superseding row, which this seat does not own (§ C99-3).
- **S253, S270, S276 — re-opened, deliberately not edited.** Their rolling-alias digests no longer
  reproduce (§ C99-4); the repair is a superseding row each, which this seat does not own this
  round (routed to round 100).

## Considerthese

`considerthese/2026-10-26.md` was re-read (proposals only; nothing implemented by this seat). All
five proposals of that note are still unimplemented at this round's freeze, measured on
`b53e209603e7c480cd975ea543e415b66f695438`:

- **Proposal 1** (a byte ceiling and a 200-character max-line check in the floors guard) stays
  carried and is **still unimplemented**: `SKILL.md` is 600 lines / 92672 B with **165** lines over
  120 characters, **94** over 300, and the longest line **1491** characters at line 518 (`wc -l`,
  `wc -c`, `awk 'length>120'`, `awk 'length>300'`), and `verifiers/floors-registry.json` holds no
  size instrument for `SKILL.md` (19 instrument rows, none a byte or line ceiling). Not taken this
  round: the floors guard is a frozen instrument no seat owns in this wave, and `SKILL.md` is at the
  600-line box (600 of 600), so a promised row add has nowhere to land.
- **Proposal 2** (move `## Gate registry` out of `SKILL.md`) stays an **L0 question** rather than a
  claim (`corpus/QUALITY.md` Q67). The section sits at `SKILL.md` line 443 and
  `verifiers/REGISTRY.md` does not exist.
- **Proposal 3** (land the page round 74 rejected and use it on the skill's own description) stays
  carried and is **still unimplemented** in the part that matters: the page is admitted (S213) and
  `corpus/knowledge/description-trigger-discipline-round85.md` exists, but the frontmatter
  description still measures **1021** characters with a **151**-character first sentence, and
  `SKILL.md` is at 600 of 600 lines, so a rewrite has to be paid for by lines saved elsewhere — and
  this wave gives the 600-line skill budget to no seat. Not trivially citable: the remaining work
  is the description rewrite, not a new registry row.
- **Proposal 4** (don't close a round before its falsify wave runs) stays **unimplemented as a
  protocol rule**. Wave `r99-w1` carries attack seats (reviewer, critic, mutation-tester and
  sentinel roles, 6 of 11 members) beside the three builders, which is adjacent practice, not the
  proposal's "provisional" closure rule.
- **Proposal 5** (an evidence budget) stays carried and is **still unimplemented**: measured on
  this lane at the freeze, `.ufo` is **353 MB** of a **590 MB** working tree (`du -sh .ufo .` from
  the lane root). Not this round's claim.

**Assimilation: none.** No proposal is newly implemented this round, and none of them is trivially
citable as a registry row, so this seat writes no row for any of them.

## Settlement

Integrated by the L1 (KotobaR99). The three builder patches (ExecRedsR99, ScribeCorpusR99,
ExecArmsR99) were applied in that order onto the lane tip after addendum 1
(`plans/round-99-addendum-1.md`: S281 cites the version-pinned argparse page). The L1 added QUALITY
Q89 (the mistake above) and re-recorded the three equal-mode counts of
`verifiers/corpus-baseline.json` after every corpus file of the landing tree was in place (the
lesson's own bytes included), so the re-record is the last corpus change of the landing commit.
The landing revision, the C1 and C2 counter readings, the census counts and the no-harm readings
are recorded in `LOG.md` § Round 99 and in the round's landing receipts, not here, so this lesson's
bytes (and the baseline counted over them) do not change after the measurement. Verdicts belong to
the non-author closure.

A second mistake of this round, found by the L1 during integration:

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `seat-scratch-clone-misrooted-in-lane`: an untracked 366 MB clone appeared at the LANE root (`repo/`, created 10:59, its alternates pointing at another seat's scratch clone), i.e. a seat ran `git clone … repo` with the lane root as its working directory | the L1's `git status --porcelain` of the lane during integration listed "?? repo/"; ReviewerRedsR99 (whose scratch the alternates name) answered that every clone it made had an absolute scratch destination | the wave context's scratch rule ("create ONE dir under the scratch root … every path you write is absolute"); the round-end misroot sweep covers the fleet root only, not the lane root | the clone was removed before the landing commit (it was never tracked: the lane helper commits named paths only), and the misroot sweep of this round ran `git status --porcelain` on the lane as well as the fleet root; shown able to fail: the lane status before removal listed the stray directory |
