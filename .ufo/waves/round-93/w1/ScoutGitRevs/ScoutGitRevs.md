# ScoutGitRevs — round-93 source receipts (read-only scout)

Seat: ScoutGitRevs. Round 93, wave 1. Access date: **2026-11-05**. Host: linux.
Fetch method: `curl -sSL -w '\n__HTTP_STATUS__%{http_code}\n'` (upstream api/raw fetches used
`curl -sSL -o <file> -w 'status=%{http_code} bytes=%{size_download}\n'`).
Nothing was written outside this receipt directory and the seat's scratch
(`/fast/scratch/hyaku/kotoba-r93/ScoutGitRevs/`, deleted on exit). No corpus file was written.
No git or jj command was run in the lane or the fleet that mutates anything (only read-only
`git rev-parse` / `git show` / `git cat-file` / `git ls-files`-class reads were used).

Files in this directory (all fetched bytes are committed because each is **under 200 KB**; the
one page over 200 KB is recorded by sha256 only):

| file | bytes | sha256 |
|---|---|---|
| `gitrevisions.html` | 74526 | `60bfaca3907710bdedcfaab0c6d82721b9b317a86ecc11d60d07027bf41a1a54` |
| `git-cat-file.html` | 79360 | `91180e9f7199b73531900776d4d4adc17b5413f26f7c6a7e2420eb34412d8be7` |
| `upstream-revisions.adoc` | 17313 | `263a2971c182471b6e83d57f73a9a5f392296cc7b642a9ff91185e13962710d7` |
| `upstream-git-cat-file.adoc` | 16203 | `3a8971e70ef50cc4b8c7b06c5696b382b30b4765303ab4dd986b140cd75cc847` |

**NOT committed (over 200 KB, sha256 recorded instead):**
`git-show.html` — `https://git-scm.com/docs/git-show`, HTTP 200, 246608 B,
sha256 `649a8a65b1e42283a12bc17f0e339d448e5c34d16085e0234cfcd502ea31d355`.

---

## (1) PRIMARY — gitrevisions, the `<rev>:<path>` syntax

| field | value |
|---|---|
| URL requested | `https://git-scm.com/docs/gitrevisions` |
| HTTP status | `200` (no redirect; `curl -sSI` reported `status=200 final=https://git-scm.com/docs/gitrevisions`) |
| `Last-Modified` header | `Thu, 05 Nov 2026 04:35:22 GMT` |
| byte size | 74526 |
| page title | `Git - gitrevisions Documentation` |
| version pin in page | `gitrevisions last updated in 2.56.0` (HTML line 1294) |
| anchor id | `Documentation/gitrevisions.txt-revpathegHEADREADMEmasterREADME` (HTML line 2438) |
| host git | `git version 2.56.0` |

### Located quote (≤25 words) — HTML lines **2440–2442**

> "names the blob or tree at the given path in the tree-ish object named by the part before the colon."

Word count command and result: `printf '%s\n' "names the blob or tree at the given path in the tree-ish object named by the part before the colon." | wc -w` → **20**.

Raw lines, verbatim (`sed -n '2440,2442p' gitrevisions.html`):

```
<p>A suffix <em>:</em> followed by a path names the blob or tree
at the given path in the tree-ish object named by the part
before the colon.
```

The `<dt>` that introduces this sentence is at **HTML line 2438**:

```
<dt class="hdlist1" id="Documentation/gitrevisions.txt-emltrevgtltpathgtemegemHEADREADMEememmasterREADMEem"><a id="Documentation/gitrevisions.txt-revpathegHEADREADMEmasterREADME" class="anchor" href="#Documentation/gitrevisions.txt-revpathegHEADREADMEmasterREADME"></a><em>&lt;rev&gt;:&lt;path&gt;</em>, e.g. <em>HEAD:README</em>, <em>master:./README</em> </dt>
```

**Shaping note (Q42/Q53/Q56 — exactly which bytes were removed).** The quote above is
**quote-equal after documented shaping**, not byte-exact: from the three raw HTML lines the
markup `<p>`, `<em>`, `</em>` was removed and the two folded newlines were joined to single
spaces; no other byte was changed. The whole three-line sentence begins
`A suffix ':' followed by a path …` — the leading clause is quoted separately below as the
upstream source form.

### Unshaped byte-exact form from upstream (the same page's own source)

`https://raw.githubusercontent.com/git/git/0ffa3e35c7c82ab8d0de226149fb03b3f7674d05/Documentation/revisions.adoc`
— HTTP 200, 17313 B, sha256 `263a2971c182471b6e83d57f73a9a5f392296cc7b642a9ff91185e13962710d7`
(committed as `upstream-revisions.adoc`). Upstream commit `0ffa3e35c7c82ab8d0de226149fb03b3f7674d05`
is `master` as of `2026-11-04T19:04:29Z` (`https://api.github.com/repos/git/git/commits/master`,
HTTP 200, 7605 B, sha256 `429fcb19d93afe4559f8966dee1fce57e2e58d30da48bc7874cc813318cb55d0`;
the commit's `sha` field read `0ffa3e35c7c82ab8d0de226149fb03b3f7674d05`).

`upstream-revisions.adoc` lines **222–224** (byte-exact for the first line; the fold continues
on 223–224):

```
  A suffix ':' followed by a path names the blob or tree
  at the given path in the tree-ish object named by the part
  before the colon.
```

Byte-exact substring check: `A suffix ':' followed by a path names the blob or tree` is present
byte-for-byte at byte offset **9893** of `upstream-revisions.adoc` (`b.find(q.encode()) == 9893`).

Note: `Documentation/gitrevisions.adoc` is only a stub; the body lives in
`Documentation/revisions.adoc`, which `gitrevisions.adoc` includes (`include::revisions.adoc[]`,
`upstream-revisions.adoc` is the included file). Both were fetched; only the included file
carries the quote.

### Alias page (not the row's URL)

`https://git-scm.com/docs/revisions` — HTTP 200, 70426 B,
sha256 `3f32780175e93e997b241d76bca68cd05a27259a6f0615d8dd898c5c7d5442d7`, title
`Git - revisions Documentation`, same sentence at its HTML line 2338. **Different bytes from
`gitrevisions.html`** (70426 vs 74526). If a row is written against this alias, its anchor line
number and sha256 differ from the `gitrevisions` row's; do not mix the two.

---

## (2) PRIMARY — git-cat-file, the `-e` existence check

| field | value |
|---|---|
| URL requested | `https://git-scm.com/docs/git-cat-file` |
| HTTP status | `200` (no redirect; `final=https://git-scm.com/docs/git-cat-file`) |
| `Last-Modified` header | `Thu, 05 Nov 2026 04:35:21 GMT` |
| byte size | 79360 |
| page title | `Git - git-cat-file Documentation` |
| version pin in page | `git-cat-file last updated in 2.56.0` (HTML line 1324) |
| anchor id | `Documentation/git-cat-file.txt--e` (HTML line 2244) |

### Located quote A (≤25 words) — HTML lines **2246–2248**

> "Exit with zero status if <object> exists and is a valid object."

Word count: `printf '%s\n' "Exit with zero status if <object> exists and is a valid object." | wc -w` → **12**.

### Located quote B (≤25 words) — same lines 2246–2248

> "If <object> is of an invalid format, exit with non-zero status and emit an error on stderr."

Word count: `printf '%s\n' "If <object> is of an invalid format, exit with non-zero status and emit an error on stderr." | wc -w` → **17**.

Raw lines, verbatim (`sed -n '2246,2248p' git-cat-file.html`):

```
<p>Exit with zero status if <span class='synopsis'><em><span class="hover-term" data-term="object">&lt;object&gt;</span></em></span> exists and is a valid
object. If <span class='synopsis'><em><span class="hover-term" data-term="object">&lt;object&gt;</span></em></span> is of an invalid format, exit with non-zero
status and emit an error on stderr.</p>
```

**Shaping note.** Both quotes are **quote-equal after documented shaping**, not byte-exact:
the markup `<p>`, `<span class='synopsis'>`, `<em>`, `<span class="hover-term" data-term="object">`
and their closers were removed, and the HTML entity `&lt;object&gt;` was decoded to `<object>`;
the folded newlines were joined to single spaces. Nothing else was changed.

### Unshaped byte-exact form from upstream

`https://raw.githubusercontent.com/git/git/0ffa3e35c7c82ab8d0de226149fb03b3f7674d05/Documentation/git-cat-file.adoc`
— HTTP 200, 16203 B, sha256 `3a8971e70ef50cc4b8c7b06c5696b382b30b4765303ab4dd986b140cd75cc847`
(committed as `upstream-git-cat-file.adoc`).

`upstream-git-cat-file.adoc` lines **50–52**:

```
	Exit with zero status if `<object>` exists and is a valid
	object. If `<object>` is of an invalid format, exit with non-zero
	status and emit an error on stderr.
```

Byte-exact substring offsets in `upstream-git-cat-file.adoc`:
`Exit with zero status if \`<object>\` exists and is a valid` at **1347**;
`If \`<object>\` is of an invalid format, exit with non-zero` at **1414**;
`status and emit an error on stderr.` at **1473**.

### The `<object>` name spelling is defined by gitrevisions (cross-link, HTML lines 2226–2230)

> "For a more complete list of ways to spell object names, see the "SPECIFYING REVISIONS" section in gitrevisions[7]."

Word count: 18. HTML lines 2229–2230. This is why (1) and (2) are two rows and not one: the
`git-cat-file` page defers the spelling of `<object>` to the `gitrevisions` page, and
`<rev>:<path>` is such a spelling.

---

## (3) Observed tool behaviour for the receipt-revision check (read-only, lane repo)

Measured on the lane repo at the freeze commit `6d7eee0570912d9f3b9d3e3d0137f3c755451233`
with `git version 2.56.0`; command and observed exit codes:

```
$ git cat-file -e 6d7eee0570912d9f3b9d3e3d0137f3c755451233:plans/round-93.md   → rc 0   (blob)
$ git cat-file -e 6d7eee0570912d9f3b9d3e3d0137f3c755451233:plans               → rc 0   (tree)
$ git cat-file -e 6d7eee0570912d9f3b9d3e3d0137f3c755451233:nonexistent-file.md → rc 128 ("fatal: path … does not exist")
$ git cat-file -e 0000000000000000000000000000000000000000:plans/round-93.md   → rc 128 ("exists on disk, but not in …")
$ git cat-file -e notarev:plans/round-93.md                                    → rc 128 ("fatal: invalid object name")
$ git show 6d7eee0570912d9f3b9d3e3d0137f3c755451233:plans/round-93.md | head -3 → rc 0 (prints "# Round 93 — kotoba …")
$ git show 6d7eee0570912d9f3b9d3e3d0137f3c755451233:plans/nope.md              → rc 128
```

**Caution for the scribe (Q26/Q31).** The *page* grounds only "exit with zero status if
`<object>` exists and is a valid object" and "exit with non-zero status" for an invalid format.
The specific numeric code **128** for a path a revision does not carry is **not** stated on
either page; it is an observed behaviour of git 2.56.0 measured above. A row may cite the page
for the zero/non-zero contract; a claim that "the check exits 128" must cite the measurement
(or `corpus/QUALITY.md` Q60, which already records the 128), not the doc quote.

---

## (4) WEAKER CANDIDATE — REJECTED

| field | value |
|---|---|
| candidate | Stack Overflow question **38785015**, answer **38785081** by `blue112` (accepted answer) |
| canonical URL | `https://stackoverflow.com/questions/38785015/git-show-on-the-previouse-sha-on-a-specific-file` |
| canonical fetch result | **HTTP 403** (Cloudflare interstitial, 5917 B) to `curl` with a browser UA; `stackprinter.appspot.com` and `www.stackprinter.com` returned HTTP 200 but a 1213-byte "StackExchange server is too busy" page (sha256 `e86bf0ac276ceaeada202d8c04b2de8831e378cb8a0d5aa4ee7aacf29b1cb6d0`) |
| fetch route actually used | `https://api.stackexchange.com/2.3/questions/38785015/answers?order=desc&sort=votes&site=stackoverflow&filter=withbody` — HTTP 200, 2571 B, sha256 `a9706b6304d534d25c3e0a6ba3d79fb8f2c96183180cbd91ebe041c8ddee6521` |
| question fetch | `https://api.stackexchange.com/2.3/questions/38785015?site=stackoverflow&filter=withbody` — HTTP 200, 1012 B, sha256 `de4424dba8cd01eab8abc87b2f48b8decbe70dfe12c1ce9840f6289a3a289cd3` |
| answer dates | created 1470387016 = **2016-08-05T08:50:16Z**; last activity 1470388361 = 2016-08-05T09:12:41Z (never edited since) |
| answer score | 0 |
| answer body quote | "This commands shows the complete file as it was on the specific commit you're telling it to." (17 words; `wc -w` → 17) — located at byte offset **552** of the answers JSON, field `items[0].body` (answer_id 38785081 at byte offset 395) |

### Judgement against `corpus/QUALITY.md` and the SOURCES tier rules — **REJECT**

1. **Tier rules.** `CORPUS.md:93-97`: tier **A** is "primary or authoritative for that scope
   (spec, official docs, source code, original paper, maintainer statement, the lane's own
   re-runnable gate output)"; tier **C** is "lead only — never sole support for an admitted
   entry"; and "`community` is never A". The candidate's kind is `community`, so it can never be
   tier A; the best it can be is tier C, a lead. `SOURCES.md`'s own tier-3 rule 3 (no second
   method) keeps the claim-admission rule in QUALITY.md.
2. **It does not state the rule C1 rests on.** The answer asserts the *effect* of the command
   and never states the `<rev>:<path>` naming rule: a programmatic check of the two answer
   bodies for `tree-ish`, `blob`, `exit status` and `cat-file` returned **False for every arm
   in both answers** (answer 38785081 and answer 38785432). The sibling answer 38785432 quotes
   only git-show's "For commits it shows the log message and textual diff." — a different
   subject (commit diffs, not `<rev>:<path>`).
3. **Undated / unpinned.** The answer is from 2016-08-05 and carries no git version pin; the
   primary it would stand in for is version-pinned ("last updated in 2.56.0"). `QUALITY.md` Q23
   requires a rule attribution to carry a located quote **plus** the sweep of what other
   authorities state — here the sweep's answer is that this source states the rule not at all.
4. **Not re-openable as cited.** The canonical page answers 403 to `curl` on this host; only
   the StackExchange API route works. A row whose `recheck:` is a human re-read of the canonical
   URL would fail on this host, so the source is not a stable row even as a lead.
5. **Q62 (refusal grounded).** The refusal is grounded on the observed facts above (kind
   `community`; the four keyword arms absent from both answer bodies; the 2016 creation date;
   the 403 canonical fetch), not on an assertion about what the source might contain.

### Flip condition

Flip only if **all** of: (a) the answer body is edited to state the `<rev>:<path>` naming rule
with a git version pin, or is superseded by an answer from a Git maintainer; **and** (b) the
canonical URL becomes re-fetchable (HTTP 200, not 403) so a `recheck:` command can run; **and**
(c) the row's scope is distinct from the two primary rows' scopes so the census `E04`
duplicate-url-within-scope check does not fire. Even after a flip it stays `community` →
tier **C** (lead only, never sole support); it can corroborate, never carry, C1's grounding.

---

## (5) Duplicate-URL check against `corpus/SOURCES.md` (the lane registry)

```
$ grep -c 'gitrevisions'  corpus/SOURCES.md   → 0
$ grep -c 'git-cat-file'  corpus/SOURCES.md   → 0
$ grep -o 'https://git-scm\.com[^ |)]*' corpus/SOURCES.md | sort -u
https://git-scm.com/docs/gitrepository-layout
```

**No existing row in this lane's registry carries either URL.** The only `git-scm.com` row in
`corpus/SOURCES.md` is **S252** (`https://git-scm.com/docs/gitrepository-layout`, tier A,
`mined`, opened 2026-11-01). So both candidate rows are **new append rows**, not correction
rows and not refusals, and the next free id in this lane is **S267** (highest present: S266;
`grep -c 'S267' corpus/SOURCES.md` → 0).

Cross-lane note (not a duplicate for kotoba): other lanes' registries do carry these URLs —
`kaidoku`, `kama`, `souji`, `revenger`, `tabi`, `tameshi` have `git-scm.com/docs/gitrevisions`
and/or `git-scm.com/docs/git-cat-file`, and `souji` carries the anchored form
`https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt--e`. The census
duplicate-id/duplicate-url state (`seen`, `url_seen`, `url_scopes`) is **per lane file** — the
validator runs `row_pass` once per lane's `corpus/SOURCES.md` with a fresh `gawk` process, so
those lanes' rows neither collide with nor block a kotoba row. They do set a house precedent
for how such a row is shaped (anchored `git-cat-file` URL, `docs` kind, tier A).

---

## (6) Suggested row cells for the scribe (not written by this seat)

Row 1 — the C1 grounding row the plan asks for
(`plans/round-93.md` § C1 "Sourced: … grounded in a SOURCES row opened this round
(gitrevisions `<rev>:<path>`)"):

- id: **S267** (next free; confirm against the registry at write time)
- source: `Git — gitrevisions(7), <rev>:<path> — https://git-scm.com/docs/gitrevisions`
- kind: `docs` · tier: **A** (official Git documentation, primary for its scope)
- scope: what `<rev>:<path>` names, and that the path resolves inside the tree-ish named
  before the colon
- anchor: `§ <rev>:<path> (anchor id Documentation/gitrevisions.txt-revpathegHEADREADMEmasterREADME);
  fetched 2026-11-05, HTTP 200, 74526 B, sha256 60bfaca3907710bdedcfaab0c6d82721b9b317a86ecc11d60d07027bf41a1a54;
  page version pin "gitrevisions last updated in 2.56.0" (HTML line 1294); located quote at
  HTML lines 2440-2442: "names the blob or tree at the given path in the tree-ish object named
  by the part before the colon." (20 words, quote-equal after tag-stripping, sed -n '2440,2442p');
  unshaped upstream form at upstream-revisions.adoc line 222 of Documentation/revisions.adoc at
  git.git 0ffa3e35c7c82ab8d0de226149fb03b3f7674d05 (2026-11-04), sha256
  263a2971c182471b6e83d57f73a9a5f392296cc7b642a9ff91185e13962710d7`
- teaches: a colon followed by a path names the blob or tree **at that path in the tree-ish
  named before the colon** — the authority for `git show <rev>:<path>` addressing a committed
  file, and the reason `verifiers/check_mutation_battery.py` can read the committed manifest
  (`git_show()` at `verifiers/check_mutation_battery.py:127-131`, used at lines 365/368/376)
- status: `mined` · opened: `2026-11-05` · recheck: `90d`
- used-by: `corpus/lessons/round-93.md, plans/round-93.md`

Row 2 — the receipt-revision check's grounding:

- id: **S268**
- source: `Git — git-cat-file(1), -e — https://git-scm.com/docs/git-cat-file#Documentation/git-cat-file.txt--e`
- kind: `docs` · tier: **A**
- scope: the exit-status contract of `git cat-file -e`
- anchor: `§ -e (anchor id Documentation/git-cat-file.txt--e); fetched 2026-11-05, HTTP 200,
  79360 B, sha256 91180e9f7199b73531900776d4d4adc17b5413f26f7c6a7e2420eb34412d8be7; page
  version pin "git-cat-file last updated in 2.56.0" (HTML line 1324); located quotes at HTML
  lines 2246-2248: "Exit with zero status if <object> exists and is a valid object." (12 words)
  and "If <object> is of an invalid format, exit with non-zero status and emit an error on
  stderr." (17 words) — both quote-equal after tag-stripping and entity decoding; unshaped
  upstream form at upstream-git-cat-file.adoc lines 50-52 of Documentation/git-cat-file.adoc at
  git.git 0ffa3e35c7c82ab8d0de226149fb03b3f7674d05, sha256
  3a8971e70ef50cc4b8c7b06c5696b382b30b4765303ab4dd986b140cd75cc847`
- teaches: `-e` exits zero **iff** the named object exists and is valid, and non-zero
  otherwise — the authority for a receipt-revision check that asks whether a path exists at a
  named revision; the page does **not** state the numeric exit code 128 for an absent path
  (that is the measured behaviour of git 2.56.0, §(3) above, and is already recorded in
  `corpus/QUALITY.md` Q60)
- status: `mined` · opened: `2026-11-05` · recheck: `90d`
- used-by: `corpus/lessons/round-93.md, plans/round-93.md`

Rejected candidate (if the scribe records rejections as rows, as `SOURCES.md` does for
`S011`/`S244`/`S247`/`S264`): id **S269**, kind `community`, tier **C**, status `rejected`,
opened `2026-11-05`, recheck `180d`, used-by `corpus/lessons/round-93.md`, with the reason and
flip condition of §(4).

---

## (7) Cross-page quote uniqueness (Q70-shaped check, run for the two primary quotes)

Tag-stripped, whitespace-collapsed text of each fetched page, checked for the other page's
quote:

| page | contains gitrevisions quote | contains cat-file `-e` quote |
|---|---|---|
| `gitrevisions.html` | True | False |
| `git-cat-file.html` | False | True |
| `git-show.html` (not committed) | False | False |
| `revisions-alias.html` (alias of gitrevisions) | True | False |

Each primary quote occurs on its own page and on no other fetched page of this set. The alias
page carries the gitrevisions quote because it is the same document under a second URL — a
reminder that a counter keying on the quote must pin the URL, not the quote alone.
