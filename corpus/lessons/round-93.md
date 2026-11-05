# Round 93 — kotoba (Linux host, omp 18.15.0): lesson

Author: **ScribeCorpusR93** (scribe seat). This file is the round-93 **scaffold**: the Gate record,
the Mistakes row and the Considerthese entry below are written; **the L1 completes the settlement**
(the seat record, the claim verdicts, the wave disposition and the final numbers).
Round: 93, plan `plans/round-93.md` (frozen at `6d7eee0570912d9f3b9d3e3d0137f3c755451233`), base
`5549fa9ed3cd91aeb0349178b5ba75dfe41711e7`.
Pre-data receipts (frozen with the plan, before any scored reading):
`.ufo/waves/round-93/receipts/redbefore-c1-base.txt` (`C1-PREDICATE-UNMET` at the base),
`redbefore-c2-base.txt` (`C2-PREDICATE-UNMET` at the base), `forgery-c1-run.txt`
(`C1-PREDICATE-UNMET` via the forgery world), `forgery-c2-run.txt` (`C2-PREDICATE-UNMET` via the
forgery world) and `census-before.txt` (33 pre-existing `W04` warnings, no `E`-code, `ok`).

## Gate

Candidates considered, with the decision and the reason:

- **S267** — Git documentation, `gitrevisions(7)`, the `<rev>:<path>` syntax
  (`https://git-scm.com/docs/gitrevisions`). **Admitted** as tier A, as a *new* row (not a
  correction row: the registry carries no `git-scm.com/docs/gitrevisions` row and no `git-scm.com`
  row other than S252, `gitrepository-layout` — `grep -o 'https://git-scm\.com[^ |)]*'
  corpus/SOURCES.md | sort -u` prints only
  `https://git-scm.com/docs/gitrepository-layout`). Access date 2026-11-05; HTTP 200; 74526 B;
  sha256 `60bfaca3907710bdedcfaab0c6d82721b9b317a86ecc11d60d07027bf41a1a54`; page title
  "Git - gitrevisions Documentation"; the page's own version pin "gitrevisions last updated in
  2.56.0" at HTML line 1294. The `<rev>:<path>` definition-list entry is at **HTML line 2438**
  (anchor id `Documentation/gitrevisions.txt-revpathegHEADREADMEmasterREADME`). Located quote
  (§ `<rev>:<path>`, HTML lines 2440-2442, 20 words — `printf '%s\n' "names the blob or tree at
  the given path in the tree-ish object named by the part before the colon." | wc -w` → 20):
  "names the blob or tree at the given path in the tree-ish object named by the part before the
  colon." The quote is **quote-equal after documented shaping**, not byte-exact: from the three
  raw HTML lines the markup `<p>`, `<em>`, `</em>` was removed and the two folded newlines were
  joined to single spaces; no other byte was changed. The unshaped byte-exact form is the same
  sentence in git's own documentation source, `Documentation/revisions.adoc` lines 222-224 at
  git.git `0ffa3e35c7c82ab8d0de226149fb03b3f7674d05` (2026-11-04), sha256
  `263a2971c182471b6e83d57f73a9a5f392296cc7b642a9ff91185e13962710d7`, where
  `A suffix ':' followed by a path names the blob or tree` sits at byte offset **9893**.
  - **Why this row grounds C1** — the frozen counting command
    `bash verifiers/fixtures/round-93/c1-killpin-rev.sh [REV]` builds its three committed worlds and
    reads the manifest through `git show <rev>:<path>` (`verifiers/check_mutation_battery.py:127`,
    called at lines 365, 368 and 376). The `<rev>:<path>` reading is what makes the committed
    manifest's kill-row count the thing the counter sees, so the row is the authority for that
    address form and is cited by this lesson and by `plans/round-93.md` § C1 "Sourced".
  - **Why the `revisions` alias page is not this row's URL** — `https://git-scm.com/docs/revisions`
    answers HTTP 200 with 70426 B and carries the same sentence at its HTML line 2338; its bytes
    differ from `gitrevisions.html` (70426 vs 74526 B), so an anchor line number or sha256 from one
    page must never be mixed with the other's.
- **S268** — Git documentation, `git-cat-file(1)`, `-e`
  (`https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt--e`). **Admitted** as tier
  A, as a *new* row (no `git-cat-file` row exists in this lane's registry). Access date 2026-11-05;
  HTTP 200; 79360 B; sha256 `91180e9f7199b73531900776d4d4adc17b5413f26f7c6a7e2420eb34412d8be7`;
  page title "Git - git-cat-file Documentation"; the page's own version pin "git-cat-file last
  updated in 2.56.0" at HTML line 1324. The `-e` definition-list entry is at **HTML line 2244**
  (anchor id `Documentation/git-cat-file.txt--e`). Located quote A (§ `-e`, HTML lines 2246-2248,
  12 words — `printf '%s\n' "Exit with zero status if <object> exists and is a valid object." |
  wc -w` → 12): "Exit with zero status if <object> exists and is a valid object." Located quote B
  (same lines, 17 words — `printf '%s\n' "If <object> is of an invalid format, exit with non-zero
  status and emit an error on stderr." | wc -w` → 17): "If <object> is of an invalid format, exit
  with non-zero status and emit an error on stderr." Both are **quote-equal after documented
  shaping**, not byte-exact: the markup `<p>`, `<span class='synopsis'>`, `<em>`,
  `<span class="hover-term" data-term="object">` and their closers were removed, the HTML entity
  `&lt;object&gt;` was decoded to `<object>`, and the folded newlines were joined to single spaces;
  nothing else was changed. The unshaped byte-exact forms are `Documentation/git-cat-file.adoc`
  lines 50-52 at git.git `0ffa3e35c7c82ab8d0de226149fb03b3f7674d05`, sha256
  `3a8971e70ef50cc4b8c7b06c5696b382b30b4765303ab4dd986b140cd75cc847` (`Exit with zero status if
  \`<object>\` exists and is a valid` at byte offset **1347**, `status and emit an error on
  stderr.` at offset **1473**).
  - **Why a second row and not a continuation of S267** — the `git-cat-file` page defers the
    spelling of `<object>` back to `gitrevisions` ("For a more complete list of ways to spell object
    names, see the "SPECIFYING REVISIONS" section in gitrevisions[7]." — HTML lines 2229-2230,
    18 words — `printf '%s\n' "For a more complete list of ways to spell object names, see the
    \"SPECIFYING REVISIONS\" section in gitrevisions[7]." | wc -w` → 18), and `<rev>:<path>` is
    one of those spellings, so the two documents carry two
    different rules: what a revision-qualified path names (S267) and what an existence check's exit
    status means (S268).
  - **What this row does not say** — neither page states the numeric exit code **128** for a path
    a revision does not carry. That number is an observed behaviour of git 2.56.0 (measured by the
    scout: `git cat-file -e <rev>:nonexistent-file.md` → rc 128, and `git cat-file -e
    0000000000000000000000000000000000000000:plans/round-93.md` → rc 128), already recorded in
    `corpus/QUALITY.md` Q60. A claim that the check "exits 128" cites the measurement, not this
    page.
- **Rejected candidate — Stack Overflow question 38785015, answer 38785081** (`blue112`, accepted
  answer; canonical URL `https://stackoverflow.com/questions/38785015/git-show-on-the-previouse-sha-on-a-specific-file`).
  **Rejected.** Access date 2026-11-05; the canonical page answers **HTTP 403** to `curl` on this
  host, and only the StackExchange API route
  `https://api.stackexchange.com/2.3/questions/38785015/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody`
  reads (HTTP 200, 2571 B, sha256
  `a9706b6304d534d25c3e0a6ba3d79fb8f2c96183180cbd91ebe041c8ddee6521`); the answer was created
  2016-08-05T08:50:16Z and never edited since, and carries score 0. Its body quote (byte offset
  552 of the answers JSON, `items[0].body`) is "This commands shows the complete file as it was on
  the specific commit you're telling it to." (17 words — `printf '%s\n' "This commands shows the
  complete file as it was on the specific commit you're telling it to." | wc -w` → 17). Four
  grounded reasons, per
  `corpus/QUALITY.md` and the SOURCES tier rules: (1) the kind is `community`, which is never tier
  A and at best a tier-C lead; (2) it states the *effect* of the command and never states the
  `<rev>:<path>` naming rule — a programmatic check of both answer bodies for `tree-ish`, `blob`,
  `exit status` and `cat-file` returns False for every arm in both answers, and the sibling answer
  38785432 quotes only git-show's "For commits it shows the log message and textual diff.", a
  different subject; (3) it is from 2016 and carries no git version pin, while the primary it would
  stand in for is pinned to 2.56.0 — Q23 requires the sweep of what other authorities state, and
  this sweep's answer is that this source states the rule not at all; (4) the canonical URL is not
  re-fetchable on this host, so a `recheck:` command over the cited URL would fail. The refusal is
  grounded on these observed facts (Q62), not on an assertion about what the source might contain.
  - **Flip condition:** flip only if **all** of (a) the answer body is edited to state the
    `<rev>:<path>` naming rule with a git version pin, or is superseded by an answer from a Git
    maintainer; **and** (b) the canonical URL becomes re-fetchable (HTTP 200, not 403) so a
    `recheck:` command can run; **and** (c) the row's scope is distinct from S267's and S268's
    scopes so the census `E04` duplicate-url-within-scope check does not fire. Even after a flip it
    stays `community` → tier **C** (lead only, never sole support): it can corroborate, never
    carry, C1's grounding.

**Census before → after.** Rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → **192** before this round (receipt
`.ufo/waves/round-93/receipts/census-before.txt`, validate rc 0 with the 33 pre-existing `W04`
duplicate-URL warnings) and **194** after — the two rows appended above (S267, S268), no row
dropped, no row rewritten. Validation:
`bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file
corpus/SOURCES.md --today 2026-11-05` → exit 0, the same 33 pre-existing `W04` warnings and no
`E`-code. The two new rows are ordinary appends, not corrections, so no row's `teaches` cell opens
`supersedes S0NN — ` and the append-only gate
(`python3 -B verifiers/check_sources_append_only.py`) has no protected-cell rewrite to see.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `receipt-identity`: a landing receipt names a scratch revision that resolves in no repository, so the receipt cannot be re-opened at the revision it claims — the round-92 landing receipts name `cd355c4796fa165ff2b7d822401b4027da29e4d0`, a revision `git cat-file -t` cannot find ("could not get object info") and no ref in the lane contains, while the round's report and SCORECARD name `c679a631` as the landing revision | `corpus/lessons/round-92-verifier-spotcheck.md` defect 1 (the receipt itself is `.ufo/waves/round-92/receipts/landing/landing-rev.txt`, whose single line reads `REV=cd355c4796fa165ff2b7d822401b4027da29e4d0`; the same hash appears in `bat-rev.txt` line 24 as `G1 revision identity PASS: rev cd355c4796fa`, and in `controls-run.stderr` lines 23 and 52 and `tip-battery.txt` line 1) | `none` — no criterion in `corpus/QUALITY.md` requires a landing receipt's recorded revision to resolve in the lane; Q36 requires a receipt to *name* a revision, not that the named revision exists | `verifiers/fixtures/round-93/check-receipt-revs.sh` — the check scans a receipts directory, resolves each named revision in the lane repo (`git rev-parse --verify -q <prefix>^{commit}` then `git cat-file -e <hex>^{commit}`), separates scratch-declared world revisions line-locally, and exits 1 on an unresolved occurrence; shown failing on `.ufo/waves/round-92/receipts/landing/` (the L1 fills the observed line) |

## Status changes

- **S267 — new row**, `mined` at opening (2026-11-05), tier A, kind `docs`, recheck `90d`, used-by
  `corpus/lessons/round-93.md,plans/round-93.md`. No prior row's `status`, `recheck` or `used-by`
  cell changed.
- **S268 — new row**, `mined` at opening (2026-11-05), tier A, kind `docs`, recheck `90d`, used-by
  `corpus/lessons/round-93.md`. No prior row's `status`, `recheck` or `used-by` cell changed.
- No other row was touched; the registry is append-only and every row present at the freeze commit
  is present here with identical protected cells.

## Sources

- **S267** — Git documentation, `gitrevisions(7)`; URL `https://git-scm.com/docs/gitrevisions`;
  access 2026-11-05; HTTP 200; 74526 B; sha256
  `60bfaca3907710bdedcfaab0c6d82721b9b317a86ecc11d60d07027bf41a1a54`; page title "Git -
  gitrevisions Documentation"; version pin "gitrevisions last updated in 2.56.0" (HTML line 1294);
  the `<rev>:<path>` entry dt at HTML line 2438; the located quote at HTML lines 2440-2442 (20
  words — `printf '%s\n' "names the blob or tree at the given path in the tree-ish object named by
  the part before the colon." | wc -w` → 20 — quote-equal after tag-stripping); the unshaped
  upstream form at
  `Documentation/revisions.adoc` lines 222-224 of git.git
  `0ffa3e35c7c82ab8d0de226149fb03b3f7674d05`, sha256
  `263a2971c182471b6e83d57f73a9a5f392296cc7b642a9ff91185e13962710d7`. Tier A scoped to what
  `<rev>:<path>` names. Status `mined`; used-by `corpus/lessons/round-93.md,plans/round-93.md`.
- **S268** — Git documentation, `git-cat-file(1)`, `-e`; URL
  `https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt--e`; access 2026-11-05;
  HTTP 200; 79360 B; sha256
  `91180e9f7199b73531900776d4d4adc17b5413f26f7c6a7e2420eb34412d8be7`; page title "Git -
  git-cat-file Documentation"; version pin "git-cat-file last updated in 2.56.0" (HTML line 1324);
  the `-e` entry dt at HTML line 2244; the located quotes at HTML lines 2246-2248 (12 words —
  `printf '%s\n' "Exit with zero status if <object> exists and is a valid object." | wc -w` → 12 —
  and 17 words — `printf '%s\n' "If <object> is of an invalid format, exit with non-zero status
  and emit an error on stderr." | wc -w` → 17 — both quote-equal after tag-stripping and entity
  decoding); the unshaped upstream form at
  `Documentation/git-cat-file.adoc` lines 50-52 of git.git
  `0ffa3e35c7c82ab8d0de226149fb03b3f7674d05`, sha256
  `3a8971e70ef50cc4b8c7b06c5696b382b30b4765303ab4dd986b140cd75cc847`. Tier A scoped to the exit
  status contract of `-e`; the page does **not** state the numeric exit code 128. Status `mined`;
  used-by `corpus/lessons/round-93.md`.

## Considerthese

`considerthese/2026-10-26.md` was re-read (proposals only; nothing implemented).

- **No proposal implemented this round.** Both claims are instrument-deepening with frozen
  predicates — C1 is a named refusal in the `--rev` path of the mutation battery and C2 is a
  required-pin-key check in the tip battery — so no proposal of this file is inside either claim's
  scope, and no proposal is implemented outside them.
- **Proposal 3** (land the page round 74 rejected and use it on the skill's own description) stays
  carried: it needs a SKILL.md description rewrite, and the 600-line budget cannot absorb one —
  `SKILL.md` is already 600 lines / 92 672 B at the freeze, so a rewrite of the frontmatter
  description has to be paid for by lines saved elsewhere, which is a claim-adjacent edit this
  round's frozen predicates do not admit.
- **Proposals 1, 4 and 5** (a byte/line ceiling; "do not close a round before its falsify wave
  runs"; a per-round evidence budget) are carried unchanged from the previous rounds; proposals 1
  and 5 are already mined as criteria Q78 and Q82 and are not re-mined here.

## Settlement

Round-92 cross-reference: the round-92 lesson's 'Non-author spot-check: pending' is answered by
corpus/lessons/round-92-verifier-spotcheck.md (closure of round 92); round-92 lesson bytes are not rewritten.

L1 settlement: pending (KotobaR93)
