# ScribeCorpusR94 — round 94, r94-w1 — SOURCES row S269 and the round-94 lesson scaffold

Seat: ScribeCorpusR94 (scribe, leaf member — no subagent dispatch).
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Repo writes: **the three owned corpus files
only**, via a patch. No lane file was written in place; no git/jj write was run in the lane or the
fleet.

## What this seat produced

| artifact | path (lane-relative) | note |
|---|---|---|
| S269 row | `corpus/SOURCES.md` | **one appended row**, no other cell touched (see the append-only evidence) |
| lesson scaffold | `corpus/lessons/round-94.md` | new file: `## Gate`, `## Mistakes`, `## Status changes`, `## Sources`, `## Considerthese`, `## Settlement` |
| index row | `corpus/README.md` | **one** row added to the coverage map, for the new lesson only |
| patch | `.ufo/waves/round-94/w1/ScribeCorpusR94/ScribeCorpusR94.patch` | sha256 `b5b2c9cdf75064dadeacc2ccfe3ef2d00f7b866428ba697d4cb575ec199357f3` |
| receipts | `.ufo/waves/round-94/w1/ScribeCorpusR94/` | `census-after.txt`, `rows-and-gates.txt`, `source-fetch.txt` |

Scratch clone: `/fast/scratch/hyaku/kotoba-r94/ScribeCorpusR94/repo`, a `git clone --shared` of the
lane checked out at the freeze commit `edc731a91a956f6df20c27a74fb981b286f6ba58`; this seat's
commit there is `e12f88336b05de8f0a85886f66fd172cdf01b612` (identity `scratch <scratch@invalid>`).

## The S269 row

`corpus/SOURCES.md` row 210, appended after S268:

- **id** `S269` · **source** PIT (pitest) documentation — "Basic concepts" —
  `https://pitest.org/quickstart/basic_concepts/` · **kind** `docs` · **tier** `A` · **status**
  `mined` · **opened** `2026-11-05` · **recheck** `90d` · **used-by**
  `corpus/lessons/round-94.md,plans/round-94.md`.
- **anchor**: § Running the tests; the Killed and Survived sentences at HTML lines 175 and 177, the
  outcome-class list at HTML lines 166-172, the timed-out definition at HTML lines 181-182 and the
  non-viable definition at HTML lines 184-185; the page carries **no version or date pin**; fetched
  2026-11-05, HTTP 200, 12155 B, sha256
  `c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a`; the unshaped upstream form at
  markdown lines 107-117 of `quickstart/basic_concepts.markdown` in hcoles/pitest-site at commit
  `e8995cd59e3cf1b1a35a979b3e735bc2fe413fea` (2025-10-24), sha256
  `2d2b7f5d3d27ace19949b4cc1948193e23cc901335c0dc8f0a24415b67613a13`, the revision whose own patch
  renames the class `Lived` to `Survived`; located quote "Killed means a test caught the mutation
  successfully." (8 words).
- **teaches**: a counter that scores a mutant as killed because its test failed must not also score
  a mutant the tool could not even load as killed — PIT classes the unloadable mutant apart from
  the killed and the survived ones, so a counter can name could-not-evaluate as its own class
  instead of folding it into either.
- No `|` character appears inside any cell (the census's 11-column shape is verified below).

## Verification (commands and observed lines)

Every command below was run in this seat's scratch clone at the freeze commit plus this seat's
commit; the raw output is in `.ufo/waves/round-94/w1/ScribeCorpusR94/`.

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <scratch>/corpus/SOURCES.md
file	W04	S269 duplicate url pitest.org/quickstart/basic_concepts across scopes
file	ok	<scratch>/corpus/SOURCES.md
EXIT=0
```
→ **rc 0**, no `E`-code, and **34** `W04` warnings (the 33 pre-existing in
`.ufo/waves/round-94/receipts/census-before.txt`, plus **one new** for the same URL across scopes —
see the finding below). Receipt: `census-after.txt`.

```
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
195                      # 194 at the freeze commit -> 195 after
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
0                        # every row has the 11-column shape
$ git diff --stat edc731a91a956f6df20c27a74fb981b286f6ba58 HEAD -- corpus/SOURCES.md corpus/README.md corpus/lessons/round-94.md
 corpus/README.md           |   1 +
 corpus/SOURCES.md          |   1 +
 corpus/lessons/round-94.md | 146 +++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 148 insertions(+)
$ git diff edc731a91a956f6df20c27a74fb981b286f6ba58 HEAD -- corpus/SOURCES.md | grep -c '^-[^-]'
0                        # SOURCES.md is a pure one-line append; no row removed or rewritten
$ python3 -B verifiers/check_sources_append_only.py --repo <scratch> --rev HEAD | grep -c 'e12f883'
0                        # no append-only breach names this seat's commit
```
The append-only gate's own summary is unchanged by this seat: at the freeze commit it reads
`19 change(s) in 9 of 60 commits`; at this commit it reads `19 change(s) in 9 of 61 commits` — the
19 pre-existing breaches (in older commits, `bf109cacc`, `e792607e8`, `dad926c48`, `a02ba7e42`,
`278b9dc4a`, `bf98d2837`, `747a07ce4` …) are the lane's inherited state, not this seat's.
Receipt: `rows-and-gates.txt`.

```
$ python3 -B verifiers/verify_corpus_integrity.py --no-baseline --repo <scratch> --json
tracked_files = 194            (193 at the freeze commit; the one new file is the lesson)
unindexed = 3                  (unchanged: round-91/92/93-verifier-spotcheck.md — pre-existing)
stale_patterns = 0   missing_paths = 0
report_total = 154  commit_total = 66   (both unchanged from the freeze commit)
report_dead = 1  commit_unresolvable = 1  (both pre-existing, in corpus/lessons/round-81.md)
```
The new lesson file is **indexed**: `corpus.index.unindexed` stays at 3, and the three names are the
same three `-verifier-spotcheck.md` files that were unindexed before this seat ran.

```
$ git clone -q --shared <lane> <second fresh clone> && git -C <second> checkout -q edc731a91a956f6df20c27a74fb981b286f6ba58
$ git -C <second> apply --check <patch>
APPLY CHECK OK (second fresh clone at the freeze commit)
```
The second clone was removed after the check.

**Tip battery (the no-harm battery item the plan names for this lane), base vs. this seat's
commit, both with `--fleet /home/vgpnk/Projects/shokunin`:**

```
$ python3 -B verifiers/check_tip_battery.py --rev edc731a91a956f6df20c27a74fb981b286f6ba58 --repo <base worktree> --fleet /home/vgpnk/Projects/shokunin
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
guard instrument-pin PASS
guard spotcheck-identity PASS
fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 2 of 6

$ python3 -B verifiers/check_tip_battery.py --rev HEAD --repo <scratch> --fleet /home/vgpnk/Projects/shokunin
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
guard instrument-pin PASS
guard spotcheck-identity PASS
fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 2 of 6
```
**Identical.** The two carried reds (`verify_skill_checklist.py` exit 1,
`verify_corpus_integrity.py` exit 1) and the `check_assertion_floors.py` 280 s timeout are the same
before and after; the `2 of 6` figure is unchanged. The base worktree used for the comparison was
removed after the run. The `spotcheck-identity` guard is unaffected by this seat: the new file is
`corpus/lessons/round-94.md`, which does not match the guard's `-verifier-spotcheck.md` pattern, and
the guard's own tree check reports all 27 base spot-check files byte-identical at this commit.

**Source facts (re-fetched by this seat, not copied from the scout):** receipt `source-fetch.txt`.
`https://pitest.org/quickstart/basic_concepts/` → HTTP 200, 12155 B, sha256
`c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a`; the slash-less form returns the
**byte-identical** body (same sha256, same size). The two located sentences are at raw HTML lines
**175** ("Killed means a test caught the mutation successfully.", **8 words**) and **177** ("Survived
means the mutation was not detected by the covering test.", 11 words). The page carries **no version
or date pin** (`grep -n -i 'last updated|version|copyright|©|generated on'` → no hits;
`grep -c '20[0-9][0-9]'` → 0). The unshaped upstream markdown at commit
`e8995cd59e3cf1b1a35a979b3e735bc2fe413fea` (2025-10-24, "Update basic_concepts.markdown", 4371 B,
sha256 `2d2b7f5d…13a13`) carries the same strings at markdown lines 107 and 109, and that revision's
own patch renames `Lived` → `Survived`.

## FINDING — the plan's "S269" row duplicates an existing registry row (for the L1)

The frozen plan names S269 as the PIT row opened this round
(`plans/round-94.md` §C1 "Sourced" and §Frontier step). **The registry already holds that URL as
S262** (`corpus/SOURCES.md` row 203, kind `docs`, tier A, `mined`), which quotes the same two
sentences at the same HTML lines and pins the same upstream commit. The scout reached the same
conclusion independently — `.ufo/waves/round-94/w1/ScoutMutSources.md` §2: "S262 already holds that
URL and quotes the same two sentences" and §5 risk 1: "do not add a second PIT row".

What this seat did, and why:

- The row **is** written, because the plan is frozen and names S269 in two places; a plan whose
  citation resolves to nothing would be worse. Its scope is deliberately **not** S262's scope — S262
  holds the outcome-**vocabulary list** and the equivalent-mutation grounds; S269 holds what each
  class **means for a kill rule** (the unloadable-mutant class a counter may not score as a kill)
  and the upstream revision that renamed `Lived` to `Survived` — and its anchor carries the page's
  sha256 (S262 records the byte count only) and the non-viable and timed-out definitions (S262's
  anchor cites lines 122-123, 175 and 177 only).
- The consequence is visible in the census: **one new `W04`** ("duplicate url … across scopes"),
  rc still 0. That warning is the honest signal that two rows now name one URL.
- **S262's own row bytes were not touched** — this seat's ownership of `corpus/SOURCES.md` is
  append-rows-only, and `corpus/QUALITY.md` Q62 makes a supersede row the mechanism for a
  *correction*, which this is not: S262 is accurate, and the two rows claim different scopes.
- **This is an L1 act.** Folding S269 into S262 (an addendum naming the merged scope, or a
  `supersedes S262 — ` correction row) is the L1's decision, and this seat's §Status changes records
  that S262's `used-by` may still gain `corpus/lessons/round-94.md` at settlement — a permitted
  in-place change, to be logged old→new there. Until then the lesson's §Gate carries the conflict
  verbatim.

## Same-round rejections (from the scout's candidates, re-verified by this seat)

Both are in the lesson's `## Gate` with reason and flip condition; the fetch facts are in
`source-fetch.txt`.

1. **mutmut documentation index** (`https://mutmut.readthedocs.io/en/latest/`) — HTTP 200, 51074 B,
   sha256 `07453b3f…8ec9cad`; the fetched bytes carry **0** hits for "equiv" and **0** for
   "killed"/"survived", so the index defines no outcome class. Rejects the round-90 verdict's
   re-probe. **Flip:** a glossary or how-it-works subpage under the same host that defines killed
   and survived.
2. **Cosmic Ray documentation** (`…/theory.html`, `…/concepts.html`) — HTTP 200, 5939 B / 18482 B;
   its class set folds a timeout and a crash into `incompetent`, so it is not the PIT class set the
   counter reads. **Flip:** a versioned Cosmic Ray page that separates its outcome enum, admitted as
   a tier-A row scoped to the Cosmic Ray tool only.

## Mined mistake (the round's mined mistake, recorded in the lesson)

Class `receipt-header-fail-open` · evidence
`.ufo/waves/round-93/w1/CriticClaimsR93/CriticClaimsR93.md` defects **D2** (a 41-hex `REV=` header
is silently dropped) and **D3** (an indented declaration is ignored) · captured-by `none` · fix
`verifiers/fixtures/round-93/check-receipt-revs.sh` gains a **MALFORMED** rule. The numbers are left
as `L1 fills at settlement` because the round's settlement numbers are the L1's; the owning seat's
receipts under `.ufo/waves/round-94/w1/ExecReceiptHeaders/` are complete (that seat's report reads
`Status: DONE`) and are quoted in the lesson with their observed lines
(`before-hex41.txt` → `EXIT=2` fail-open; `after-hex41.txt` → `MALFORMED … hex run is 41, not 40`,
`malformed declarations: 1`, `EXIT=1`; `before-indented.txt` → `EXIT=2`;
`after-indented.txt` → two `MALFORMED … leading whitespace before the declaration` lines, `EXIT=1`;
no-harm legs `after-good.txt` `4 resolved, 0 unresolved` `EXIT=0`, `after-round92-landing.txt`
`1 resolved, 5 unresolved over 18 files` `EXIT=1`, `after-round93-receipts.txt`
`9 resolved, 0 unresolved over 19 files` `EXIT=0` — the round-93 landing receipts still read
`9 resolved, 0 unresolved`, rc 0, as the plan's Frontier step requires).

## Boundaries observed

- **Files written in the lane:** only `.ufo/waves/round-94/w1/ScribeCorpusR94.md` (this report), the
  three receipts and the patch under `.ufo/waves/round-94/w1/ScribeCorpusR94/`, and the READY file
  `.ufo/waves/round-94/w1/ScribeCorpusR94_READY`. **No** corpus file was written in the lane — the
  three corpus files land through the patch. The lane tip is still
  `edc731a91a956f6df20c27a74fb981b286f6ba58` and `git status --porcelain` in the lane shows only the
  orchestrator's own untracked round-94 wave files.

## Risks and open items for the L1

1. **The plan's "S269" duplicates the existing S262 row** (see the FINDING above). This seat wrote
   the row because the plan is frozen and names it, gave it a scope that is **not** S262's, and left
   S262's bytes untouched. The census shows the duplication as one new `W04` (rc still 0). If the
   L1 prefers one row, an addendum naming the merged scope — or a `supersedes S262 — ` correction
   row — is the mechanism, and it is an L1 act (this seat's ownership is append-rows-only).
2. **S262's `used-by` may need the round-94 lesson added** at settlement (a permitted in-place
   change, to be logged old→new in the lesson's §Status changes). This seat did not make it,
   because it is an edit to a row it does not own.
3. **The lesson is a scaffold.** Its `## Settlement` section is a placeholder; the L1 fills the seat
   record, the C1/C2 claim verdicts with their landing revision, the wave disposition and the final
   numbers. The round's settlement numbers are deliberately left as `L1 fills at settlement` in the
   Mistakes row.
4. The PIT page carries **no version or date pin**, so the row pins it by digest and by the upstream
   commit that renamed `Lived` to `Survived`; a re-fetch after that commit changes would move the
   `90d` recheck.
5. Two carried reds in the tip battery (`verify_skill_checklist.py` exit 1,
   `verify_corpus_integrity.py` exit 1) and the `check_assertion_floors.py` 280 s timeout are
   **pre-existing and unchanged** by this seat (identical base and post-commit readings). The
  corpus-integrity gate's own `report_dead = 1` and `commit_unresolvable = 1` findings both sit in
  `corpus/lessons/round-81.md` — a file this seat did not touch and may not touch.

- The plan, the counter (`verifiers/fixtures/round-94/selftest-kills.py`), the forgery patch, the
  frozen anchors, `SKILL.md`, `MANIFEST.json`, `scripts/`, `templates/`, `considerthese/`,
  `.ufo/state/`, `.ufo/watchdog.log` and every other lane file were not touched. The fleet root and
  every sibling lane were read only. No git or jj write was run in the lane or the fleet.
- No `SKILL.md` edit (the file is 600 lines / 92 672 B at the freeze) and no
  `corpus/lessons/round-*-verifier-spotcheck.md` edit.
- **Install record: none.** No tool was installed or upgraded: the seat used only `curl`,
  `sha256sum`, `grep`, `awk`, `wc`, `sed`, `git` and the python3 standard library, all already on
  the host. No pacman transaction was run (the host-wide pacman pause was respected), and no kernel
  or host setting was changed — nothing needed one.
