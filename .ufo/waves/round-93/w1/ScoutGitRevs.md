# ScoutGitRevs — round 93, wave 1 — source findings

Seat: ScoutGitRevs (read-only scout; no repo file was written except this seat's own receipts
under `.ufo/waves/round-93/w1/ScoutGitRevs/`). Access date **2026-11-05**, host linux,
`git version 2.56.0`.

**Full receipt with byte sizes, sha256s, raw line dumps, shaping notes, the observed
exit-code measurements and the proposed SOURCES cells:**
`.ufo/waves/round-93/w1/ScoutGitRevs/ScoutGitRevs.md`

## What is opened and what it grounds

| # | source | HTTP | bytes | sha256 | grounds |
|---|---|---|---|---|---|
| 1 | `https://git-scm.com/docs/gitrevisions` | 200 | 74526 | `60bfaca3907710bdedcfaab0c6d82721b9b317a86ecc11d60d07027bf41a1a54` | C1's `git show <rev>:<path>` grounding |
| 2 | `https://git-scm.com/docs/git-cat-file` | 200 | 79360 | `91180e9f7199b73531900776d4d4adc17b5413f26f7c6a7e2420eb34412d8be7` | the receipt-revision check's exit-status contract |

Both pages carry the version pin "last updated in 2.56.0" (gitrevisions HTML line 1294;
git-cat-file line 1324), matching the host's git 2.56.0. Fetched bytes are committed under
`.ufo/waves/round-93/w1/ScoutGitRevs/` (each under 200 KB), together with the unshaped upstream
sources `Documentation/revisions.adoc` and `Documentation/git-cat-file.adoc` at git.git
`0ffa3e35c7c82ab8d0de226149fb03b3f7674d05` (2026-11-04), so each quote has a byte-exact form.

### Located quotes (≤25 words each, with line numbers)

**gitrevisions, HTML lines 2440–2442** (dt at line 2438):

> "names the blob or tree at the given path in the tree-ish object named by the part before the colon."  *(20 words, `wc -w`)*

**git-cat-file `-e`, HTML lines 2246–2248** (dt at line 2244):

> "Exit with zero status if <object> exists and is a valid object."  *(12 words)*

> "If <object> is of an invalid format, exit with non-zero status and emit an error on stderr."  *(17 words)*

Both HTML quotes are *quote-equal after documented shaping* (markup removed, `&lt;object&gt;`
decoded, folded newlines joined); the byte-exact upstream forms are at
`upstream-revisions.adoc:222` and `upstream-git-cat-file.adoc:50-52`.

## Weaker candidate — REJECTED

Stack Overflow **38785015 / answer 38785081** (`blue112`, accepted, score 0, created
2016-08-05, never edited): *"This commands shows the complete file as it was on the specific
commit you're telling it to."* (17 words).

Reject, on four observed grounds: (1) its kind is `community`, which `CORPUS.md:97` says is
**never tier A**, and tier C is "lead only — never sole support"; (2) it does not state the
rule C1 rests on — a programmatic check of both answer bodies for `tree-ish`, `blob`,
`exit status`, `cat-file` is **False on every arm**; (3) it is a 2016 answer with no git version
pin, against a version-pinned primary; (4) its canonical URL answers **403** to `curl` on this
host (only the StackExchange API route works), so a `recheck:` on the cited URL cannot run.

**Flip condition:** the body is edited (or superseded by a maintainer) to state the
`<rev>:<path>` naming rule with a version pin **and** the canonical URL becomes re-fetchable
**and** the scope stays distinct from the two primary rows' scopes. Even then it stays tier C —
corroboration, never support.

## Duplicate-URL check against `corpus/SOURCES.md`

`grep -c 'gitrevisions' corpus/SOURCES.md` → **0**; `grep -c 'git-cat-file' corpus/SOURCES.md`
→ **0**. The lane's only `git-scm.com` row is **S252** (`docs/gitrepository-layout`). So both
primaries are **new append rows**, not corrections and not refusals; next free id in this lane is
**S267** (highest present S266). Other lanes (`kaidoku`, `kama`, `souji`, `revenger`, `tabi`,
`tameshi`) do carry these URLs — the census's duplicate-id/url state is per lane file, so that
does not collide; `souji` carries the anchored `…/git-cat-file#Documentation/git-cat-file.txt--e`
form, which sets the house shape for row 2.

## Caution the scribe must carry into the row

The pages ground the **zero / non-zero** exit contract of `git cat-file -e`. They do **not** state
the numeric exit code **128** for a path a revision does not carry. That 128 was measured here on
git 2.56.0 (present blob rc 0, present tree rc 0, absent path rc 128, absent revision rc 128,
malformed revision rc 128) and is already recorded in `corpus/QUALITY.md` Q60. A row claiming
"exits 128" must cite the measurement, not the doc quote.

## Also observed

`git show <rev>:<path>` reads the committed manifest in
`verifiers/check_mutation_battery.py` (`git_show()` at lines 127–131, used at 365/368/376), and
the frozen C1 counter builds its three committed worlds from that same read — so row 1 is the
authority C1's "Sourced" line needs. `https://git-scm.com/docs/revisions` is an alias serving the
same sentence under different bytes (70426 B, sha256 `3f32780175e93e997b241d76bca68cd05a27259a6f0615d8dd898c5c7d5442d7`,
sentence at its line 2338): if it is cited instead, the anchor line and sha256 differ — do not mix.
