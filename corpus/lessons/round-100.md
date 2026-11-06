# Round 100 — kotoba (Linux host, omp): lesson

Author: **ScribeCorpusR100** (curation draft, scaffold). A seat review is lane evidence, not the
independent non-author admission judgment; the L1 (KotobaR100) integrates and settles, and
`## Settlement` is its placeholder.

Round: 100, plan `plans/round-100.md` (frozen at `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`), base
`7b449a637c03d9b4c43a81b4df37cb38c2ea89ee`, instrument commit
`d1e1170d950fc378bb6a28bbfc5a62802669be86` (the v6.2 counter
`verifiers/fixtures/round-100/selftest-kills.py` and the C2 runner
`verifiers/fixtures/round-100/anchor-lists.py`). Pre-data receipts (frozen with the plan, before any
scored reading): `.ufo/waves/round-100/receipts/` — `redbefore-c1-base.txt` (`C1 targets killed 0 of
6`, `C1-PREDICATE-UNMET`), `redbefore-c1-base-rulesv5.txt`, `poscontrol-r99c1-base.txt` and
`poscontrol-r98c1-base.txt` (MET), `c2-base.txt` (`C2 mismatches 8 of 28`,
`C2-PREDICATE-UNMET`), the five C2 forgery controls `c2-ctl-f1..f5.txt` plus the truth-table positive
`c2-ctl-p1-fixline-only.txt` (all UNMET), `census-before.txt` (`W04` 34), the committed control-world
patches `receipts/ctl-worlds/*.patch`, and `sources-opened.txt` (the access record for the four
sources this round's rows cite).

## Gate

Candidates considered, with the decision and the reason. Every access record below is this seat's own
fetch on 2026-11-06 (`curl -sS -L`, then `sha256sum`), re-fetched twice more to prove the digest is
stable; each fetch's HTTP code, byte count and sha256 are recorded, and the bytes themselves are not
kept in the lane (the digests are the evidence). The frozen L1 receipt
`receipts/sources-opened.txt` recorded the same four URLs on the same day and its digests are
reproduced exactly here — see the "L1 cross-check" line under each row.

- **S282 — Python documentation, `pathlib`
  (`https://docs.python.org/release/3.15.2/library/pathlib.html`). Admitted** as tier A, kind
  `docs`, status `mined`, opened 2026-11-06, recheck `on-release`, used-by
  `corpus/lessons/round-100.md`.
  - Access record: 2026-11-06; HTTP 200; **270630 B**; sha256
    `090f3b03b648c271f4d810f0c37a51b2b54ebbdaa8130466d695e836e7a399ca` — identical across three
    fetches (12:28Z, 12:33Z, 12:44Z). The page's own version pin is "Python 3.15.2 documentation"
    (HTML line 19) and its footer reads `Last updated on Oct 25, 2026 (17:03 UTC)` (HTML line
    2566).
  - HTML line excerpt (the `Path.is_dir` entry, HTML lines 1362-1367):
    ```
    <dt class="sig sig-object py" id="pathlib.Path.is_dir">
    ...
    <dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if the path points to a directory. <code class="docutils literal notranslate"><span class="pre">False</span></code> will be
    returned if the path is invalid, inaccessible or missing, or if it points
    to something other than a directory. Use <a class="reference internal" href="#pathlib.Path.stat" title="Path.stat()">…</a> to distinguish
    between these cases.</p>
    ```
  - Located quote (≤25 words): "False will be returned if the path is invalid, inaccessible or
    missing, or if it points to something other than a directory." — **22 words**
    (`printf '%s\n' "<quote>" | wc -w` → 22), at **HTML lines 1364-1366** (the `<dd><p>` body of the
    `Path.is_dir` entry), quote-equal after the rendered `True` / `False` code spans are folded to
    their text. The sentence occurs **exactly once** on the page (the bare marker `is_dir` occurs
    many times, so a quote match must carry the surrounding words).
  - **The contrast entry, on the same page and the same digest.** § `pathlib.Path.exists`
    (`<dt class="sig sig-object py" id="pathlib.Path.exists">`, HTML line 1323; body HTML lines
    1325-1326): "Return True if the path points to an existing file or directory and False if the
    path is invalid, inaccessible or missing." — **22 words**
    (`printf '%s\n' "<quote>" | wc -w` → 22), quote-equal after the rendered `True` / `False` code
    spans are folded, and occurring **exactly once** on the page. This entry is carried by the same
    row because both entries are on this one page under this one digest; the pair is what carries
    the contrast the C1 t04 arm needs (a plain file is **not a directory**, yet it **does exist**),
    and the `is_dir` entry alone states only the first half. `ScoutSourcesR100` § 3.2 and § 8 item 1
    flagged exactly this gap in the plan's S282 line, and the flag was checked against this seat's
    own bytes before it was acted on.
  - **L1 cross-check:** the frozen receipt `receipts/sources-opened.txt` records the same URL at
    HTTP 200, 270630 B, sha256 `090f3b03…` — reproduced byte for byte here, and the receipt's own
    re-fetch line reads "pathlib refetch sha256 identical".
  - **Why this row supersedes S276:** S276 cites the **rolling** `/3/` alias
    `https://docs.python.org/3/library/pathlib.html`, whose digest moves with the documentation
    build's `Last updated on … (HH:MM UTC)` footer. Measured here on 2026-11-06, the alias served
    HTTP 200, 271233 B, sha256 `eda0d4a582da98b124c44db6cf45785d62f352e5b188aeadf972edcef0921d1d` —
    a different byte count and digest from the pinned release page, and the two byte streams differ
    in the page's metadata (the alias carries the 3.15 social-preview images, the pinned release
    carries the static preview). A digest recorded against the alias is a build stamp, not a
    content identity; the version-pinned release snapshot is stable across fetches and is what this
    row cites.
  - **What this row adds:** the stdlib semantics the C1 **t04** arm observes. The frozen mutant
    `t04-dircheck-exists` (`verifiers/fixtures/round-100/selftest-kills.py:149`) replaces
    `if not path.is_dir():` with `if not path.exists():` in `verifiers/verify_dispatch_prompts.py`,
    so a plain file would pass the directory substrate check and reach directory iteration. The
    documented pair — `is_dir()` is False for "something other than a directory" **and** `exists()`
    is True for an "existing file or directory" — is what makes that mutant a defect rather than an
    equivalent change: a plain file is not a directory, yet it does exist. The page is the authority
    for the stdlib semantics only; the lane's own check is the lane's own code.
- **S283 — Python documentation, `tempfile`
  (`https://docs.python.org/release/3.15.2/library/tempfile.html`). Admitted** as tier A, kind
  `docs`, status `mined`, opened 2026-11-06, recheck `on-release`, used-by
  `corpus/lessons/round-100.md`.
  - Access record: 2026-11-06; HTTP 200; **74630 B**; sha256
    `0eef90989f9e1e4d261b8259e620244270f0bb8773e6b56b221b9575df60ab41` — identical across three
    fetches (12:28Z, 12:33Z, 12:44Z). Version pin "Python 3.15.2 documentation" (HTML line 19);
    footer `Last updated on Oct 25, 2026 (17:03 UTC)` (HTML line 808).
  - HTML line excerpt (the `cleanup()` entry, HTML lines 386-392):
    ```
    <dt class="sig sig-object py" id="tempfile.TemporaryDirectory.cleanup">
    ...
    <dd><p>The directory can be explicitly cleaned up by calling the
    <code class="xref py py-meth docutils literal notranslate"><span class="pre">cleanup()</span></code> method. If <em class="property">ignore_cleanup_errors</em> is true, any unhandled
    exceptions during explicit or implicit cleanup (such as a
    <a class="reference internal" href="../builtins/exceptions.html#PermissionError" title="PermissionError">…</a> removing open files on Windows) will be ignored,
    and the remaining removable items deleted on a “best-effort” basis.
    ```
  - Located quote (≤25 words): "If ignore_cleanup_errors is true, any unhandled exceptions during
    explicit or implicit cleanup (such as a PermissionError removing open files on Windows) will be
    ignored" — **24 words** (`printf '%s\n' "<quote>" | wc -w` → 24), at **HTML lines 389-391**,
    quote-equal after the rendered `ignore_cleanup_errors` emphasis and the `PermissionError` link
    text are folded to their text. The sentence occurs **exactly once** on the page.
  - **L1 cross-check:** the frozen receipt records the same URL at HTTP 200, 74630 B, sha256
    `0eef9098…` — reproduced byte for byte.
  - **Why this row supersedes S253:** S253 cites the rolling `/3/` alias
    `https://docs.python.org/3/library/tempfile.html`. Measured on 2026-11-06, that alias served
    HTTP 200, **75198 B**, sha256 `2bef9acdef026a012eada84114db8ff3ce0e80f30fac0532149b14882a238812`
    — eight bytes longer than the 75190 B S253 recorded, because the rolling build's content moved
    as well as its footer. The pinned release snapshot is the stable reading.
  - **What this row adds:** the stdlib name of the r83 loss class — a `PermissionError` removing
    open files on Windows — and the stdlib's own remedy, `ignore_cleanup_errors=True`, which the
    r83 `check_tip_battery.py` amendment adopts. The page grounds the stdlib wording; the lane's
    amendment and its before-world discriminator are the lane's own evidence.
- **S284 — Python documentation, `unittest`
  (`https://docs.python.org/release/3.15.2/library/unittest.html`). Admitted** as tier A, kind
  `docs`, status `mined`, opened 2026-11-06, recheck `on-release`, used-by
  `corpus/lessons/round-100.md`.
  - Access record: 2026-11-06; HTTP 200; **336394 B**; sha256
    `90fb380940f290ed6611ab8907a0f11840d03cea258357b5b3702a6b2eba8387` — identical across three
    fetches (12:28Z, 12:33Z, 12:44Z). Version pin "Python 3.15.2 documentation" (HTML line 19);
    footer `Last updated on Oct 25, 2026 (17:03 UTC)` (HTML line 3179).
  - HTML line excerpt (the `errors` attribute entry, HTML lines 2410-2414):
    ```
    <dt class="sig sig-object py" id="unittest.TestResult.errors">
    ...
    <dd><p>A list containing 2-tuples of <a class="reference internal" href="#unittest.TestCase" title="TestCase">…</a> instances and strings
    holding formatted tracebacks. Each tuple represents a test which raised an
    unexpected exception.</p>
    ```
  - Located quote (≤25 words): "Each tuple represents a test which raised an unexpected exception."
    — **10 words** (`printf '%s\n' "<quote>" | wc -w` → 10), at **HTML lines 2413-2414**, quote-equal
    after the rendered `TestCase` link text is folded. Its counterpart on the same page, the
    `failures` entry (`id="unittest.TestResult.failures"`, HTML line 2418), reads "Each tuple
    represents a test where a failure was explicitly signalled using the assert* methods." — **15
    words** — at HTML lines 2421-2422, quote-equal after the `assert* methods` link text is folded.
    Each sentence occurs exactly once on the page.
  - **L1 cross-check:** the frozen receipt records the same URL at HTTP 200, 336394 B, sha256
    `90fb3809…` — reproduced byte for byte.
  - **Why this row supersedes S270:** S270 cites the rolling `/3/` alias
    `https://docs.python.org/3/library/unittest.html`. Measured on 2026-11-06, the alias served
    HTTP 200, 336978 B, sha256 `a3c45299b7b52d017dc5f7f7c90dd8f7f9ce4e5a8261192d41e9e653a5d6bbd4`
    — the same byte count S270 recorded but a different digest, and the difference is provably the
    build footer alone: substituting S270's footer string
    (`Last updated on Nov 05, 2026 (22:32 UTC)`) into the alias bytes reproduces S270's recorded
    digest `f9510cd7d7a67a32fb891016cbb42bf1dfcb80a370c689ed222058acbff3506d` **exactly**
    (`sed 's/…/…/' alias.html | sha256sum` → that digest). A digest recorded against the alias is
    therefore a build stamp; the pinned release snapshot is stable.
  - **What this row adds:** the error-versus-failure distinction the kill counters depend on. A
    kill must be a *reported* failure, and the runner's own result object keeps "raised an
    unexpected exception" and "a failure was explicitly signalled" in two different lists — so a
    crash and a signalled failure are different events, and only the signalled one is evidence that
    the check under test ran and reported. The page grounds the runner's semantics; the counters'
    reading of them is the lane's own code.
- **S285 — Linux man-pages, `ptrace(2)`
  (`https://man7.org/linux/man-pages/man2/ptrace.2.html`). Admitted** as tier A, kind `docs`,
  status `mined`, opened 2026-11-06, recheck `180d`, used-by `corpus/lessons/round-100.md`.
  - Access record: 2026-11-06; HTTP 200; **104833 B**; sha256
    `69cd309ece177d54086771701b2085e31cabd14a92484647392bcda468f7bd35` — identical across three
    fetches (12:28Z, 12:33Z, 12:44Z) and byte-identical to the digest S279 records. Footline
    "Linux man-pages 6.19 2026-06-05 ptrace(2)" (HTML line 1713).
  - HTML line excerpt (access-check algorithm step (4), HTML lines 1516-1520):
    ```
       (4)  Deny access if the target process "dumpable" attribute has a
            value other than 1 (<b>SUID_DUMP_USER</b>; see the discussion of
            <b>PR_SET_DUMPABLE </b>in <a href="../man2/prctl.2.html">prctl(2)</a>), and the caller does not have
            the <b>CAP_SYS_PTRACE </b>capability in the user namespace of the
            target process.
    ```
  - Located quote (≤25 words): "the caller does not have the CAP_SYS_PTRACE capability in the user
    namespace of the target process" — **16 words**
    (`printf '%s\n' "<quote>" | wc -w` → 16), at **HTML lines 1518-1520**, quote-equal after the
    bold `CAP_SYS_PTRACE` markup is removed and the whitespace folded. The step's first conjunct,
    "Deny access if the target process "dumpable" attribute has a value other than 1", is **14
    words** at HTML lines 1516-1517, and step (3)'s permissive disjunct "The caller has the
    CAP_SYS_PTRACE capability in the user namespace of the target." is **13 words** at HTML lines
    1513-1514. Each occurs exactly once on the page.
  - **L1 cross-check:** the frozen receipt records the same URL at HTTP 200, 104833 B, sha256
    `69cd309e…` — reproduced byte for byte.
  - **Why this row supersedes S279:** S279's located quote stops **before** the parenthetical on
    `SUID_DUMP_USER` and `CAP_SYS_PTRACE`, so it carries only the first conjunct of step (4). The
    rule is a conjunction — access is denied when the target is non-dumpable **and** the caller
    lacks the capability — while step (3) carries the permissive, capability-bearing disjunct. A
    reader working from the truncated quote alone would read step (4) as "non-dumpable ⇒ deny"
    and miss the capability condition, and a fragment must not be able to flip either side. This
    row is the registry form of that correction (round-99 lesson `C99-3`, which recorded the
    conjunct in prose only). The page's bytes are unchanged: this is a superseding row on the same
    URL, not an edit to S279.
  - **What this row adds:** the full conjunction in one located quote, so the rule can be cited
    without a reader having to reconstruct the second conjunct from a parenthetical.
- **REJECTED candidate — Sphinx `literalinclude`'s `:lines:` option
  (`https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html`). Not rowed.**
  - Access record: 2026-11-06; HTTP 200; **170372 B**; sha256
    `0607fc1b47e0546a247cc9fd66bc7e98e141a1c7a652e9033fa889c5230dce2b` (12:44:57-03:00). A fetch
    16 minutes earlier (12:28Z) gave the same HTTP code and byte count but sha256
    `d629d47b0aef1ab9ef2f8e30e59f3fbb37a31ad803544d912897937c676af5b3`; the two byte streams differ
    in **exactly one line** (HTML line 1620, whose Cloudflare e-mail-protection token rotates per
    response). The page is therefore not digest-stable either.
  - Located quote (≤25 words): "line numbers (comma separated numbers)" — **5 words**
    (`printf '%s\n' "<quote>" | wc -w` → 5), at **HTML line 1421**, the signature of the
    `literalinclude` directive's `:lines:` option (`<dt class="sig sig-object rst"
    id="directive-option-literalinclude-lines">`, HTML line 1420). The marker occurs three times on
    the page (the `:emphasize-lines:` option at HTML lines 1166 and 1379 carries the same wording),
    so a quote match must carry the option name.
  - **REJECTED:** it is the closest external candidate for a comma-list line anchor — the
    `literalinclude` `:lines:` option is exactly "comma separated numbers" — but it is a **document
    build's source-inclusion filter**, not a citation-anchor convention for a repository's
    governance files: it selects which lines of an included file to paste into generated
    documentation, and its own example (`1,3,5-10,20-`) admits ranges and open-ended ranges that
    the lane's anchor form does not. The lane's comma-list anchor (`file.md:30,37`) is the lane's
    own convention, carried by `SKILL.md` and read by the lane's own checklist gate; an external
    tool's inclusion syntax is not its authority. The row is also not digest-stable, which is the
    same defect this round's superseding rows exist to repair.
  - **The ground the lane already has** (so nothing is left uncited): the lane's own committed bytes
    use the comma-list form — `SKILL.md:116` reads ``(S090 `:10,18,34,40-42`)``, a comma list **with
    a range**, and `corpus/QUALITY.md:50` reads
    `corpus/lessons/round-55-verifier-spotcheck.md:82,135`. That is `kind: own-work`, tier A, and it
    is the form the C2 counter's own truth-table rows `r01`/`r02`/`r04` encode — the counter's
    header says so outright ("the form SKILL.md already uses"). No counter defect was found: the
    truth table re-derived by hand agrees with the frozen base receipt on all eight comma rows.
  - **Flip:** a round that defines the lane's comma-list anchor grammar by reference to an
    external specification — rather than by the lane's own `SKILL.md` usage and its checker — would
    make this page the authority, and the `:lines:` option would have to be re-read from a pinned
    (non-`master`) URL before it could be cited. If that happens, the row must also be cited **with**
    a counter-example so no reader concludes the comma always means a list: `git-log(1)`'s
    `-L <start>,<end>:<file>` uses the comma for a **range** and puts the path after the colon —
    the opposite reading of the lane's form.
  - **Why it is not a registry row:** this seat's write ownership of `corpus/SOURCES.md` is the four
    new rows S282-S285 only. A rejected row would be a fifth row; recording it in this lesson's
    `## Gate` keeps the rejection as evidence of taste (contract rule 1) without exceeding the
    ownership. The L1 may row it as S286 if the registry should carry it.

**Census.** `scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md"` → rc 0, `file ok`,
`W04` **35** — 34 before, plus exactly one new warning, `S285 duplicate url
man7.org/linux/man-pages/man2/ptrace.2.html across scopes`, which is the expected consequence of
S285 sharing S279's URL with a different scope (S285's scope is step (4) in full; S279's is the
environ-read denial). The supersedes exemption keeps it a warning and not an `E04`: the four new
rows carry `supersedes S0NN —` in their `teaches` cell, so none of them is a duplicate-URL-plus-scope
error. Rows 207 → 211.

## Corrections

Named, append-only correction entries. A frozen receipt is never edited; a correction is a new entry
that points at it.

- **C100-1 — the round-99 lesson's `rev-parse` line pointer is cited at the base revision, not at
  the tip.** `corpus/lessons/round-99.md` § Gate cites `verifiers/check_tip_battery.py:344` for the
  `git rev-parse <rev>:<path>` read that the pin admission uses. Line 344 is that read **at the
  round-99 base** `52e8e95ac4faf4ded84d7b82cbc204792590d0f7`; at the round-99 tip
  `0a65cceb5b8fa5bb25a095828a1e6cd0e3681ee3` the same read is at **line 349**, because the C2 pin
  admission inserted five lines above it. The pointer as written therefore names a line that holds
  something else once the tip lands — and it names the *wrong* line even at the base if the reader
  takes it as a tip pointer, because a base revision and a tip revision are different objects.
  Verified both readings with `git show <rev>:<path> | sed -n Np` (read-only, in the lane):
  - `git show 52e8e95a:verifiers/check_tip_battery.py | sed -n 344p` →
    `        got = git(clone, "rev-parse", "%s:%s" % (rev, path))`
  - `git show 0a65cceb:verifiers/check_tip_battery.py | sed -n 349p` →
    `        got = git(clone, "rev-parse", "%s:%s" % (rev, path))`
  - `git show 0a65cceb:verifiers/check_tip_battery.py | sed -n 344p` →
    `            failures.append(("instrument-size", "binary diff at %s" % path))`
  - **The corrected citation form is revision-qualified:** `52e8e95a:verifiers/check_tip_battery.py:344`
    = `0a65cceb:verifiers/check_tip_battery.py:349`. A line pointer without its revision is a
    promise about an object that moves; with the revision it is a promise about a fixed object.
  - The round-99 lesson's own bytes are **not** edited here: the registry is append-only, the
    lesson file is the round-99 seat's, and this entry is the correction of record. The L1 records
    the resolved pointer where the round-99 lesson's sentence is cited going forward.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `line-pointer-cited-at-base-revision`: a citation names `file.py:NNN` without the revision it was read at, so the line it names is true at one revision and something else at the next; the round-99 lesson cited `verifiers/check_tip_battery.py:344` for the `rev-parse <rev>:<path>` read — true at the round-99 base `52e8e95a`, but at the round-99 tip `0a65cceb` that read is at line 349 | `corpus/lessons/round-99-verifier-spotcheck.md` § Routed defects item 1 ("Lesson pointer drift"), which measured the same drift independently (`verifiers/check_tip_battery.py`: line 344 at base, **line 349 at tip**); `corpus/lessons/round-99.md:88` carries the uncorrected citation | none (the defect was routed by the non-author closure and no lane instrument captures it) | correction **C100-1** above — cite the pointer revision-qualified (`<rev>:<path>:<line>`) so the cited object cannot move under the citation — plus a QUALITY criterion for it (the L1 adds **Q90** to `corpus/QUALITY.md` at settlement; this seat does not write `corpus/QUALITY.md`) |

Shown able to fail: the pointer is read at the tip revision it is used at. `git show
0a65cceb:verifiers/check_tip_battery.py | sed -n 344p` prints
`            failures.append(("instrument-size", "binary diff at %s" % path))` — no `rev-parse` in
the line — so a reader who follows the round-99 citation at the round-99 tip lands on an unrelated
line and finds no `rev-parse` read at all. The criterion is thus falsifiable by a one-line command
against the revision under discussion, and it fails there.

## Status changes

- **None.** The registry is append-only and this seat's ownership of `corpus/SOURCES.md` is
  append-rows-only: **S282, S283, S284 and S285 are new rows** (`mined` at opening, 2026-11-06,
  tier A, kind `docs`; recheck `on-release` for the three release-pinned Python rows and `180d` for
  the man-pages row; used-by `corpus/lessons/round-100.md`), and **no existing row's `status`,
  `recheck` or `used-by` cell was changed** — so there is no old→new pair to log here.
- **S253, S270, S276, S279 — re-opened, deliberately not edited.** Each was re-fetched at the
  rolling alias it cites and each was found to have a digest that no longer reproduces (S253: the
  alias's content moved as well as its footer; S270: the footer alone, proved by exact digest
  substitution; S276: the alias carries different metadata; S279: its bytes are unchanged, and its
  defect is the truncated quote, not the digest). The repair for each is a superseding row, which
  this round writes: S283 supersedes S253, S284 supersedes S270, S282 supersedes S276 and S285
  supersedes S279. The superseded rows stay exactly as they are, per contract rule 2.
- **S276, S280 — re-opened as rejected rows, unchanged.** Both remain `rejected` with their reasons
  intact; nothing in this round reopens them.

## Considerthese

`considerthese/2026-10-26.md` was re-read (proposals only; nothing implemented by this seat). It is
the newest note in `considerthese/` (the directory's latest file by date). All five proposals of that
note are still unimplemented at this round's freeze `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`,
measured in the scratch clone:

- **Proposal 1** (a byte ceiling and a 200-character max-line check in the floors guard) stays
  carried and is **still unimplemented**: `SKILL.md` is 600 lines / 92672 B with **165** lines over
  120 characters, **94** over 300, and the longest line **1491** characters at line 518 (`wc -l`,
  `wc -c`, `awk 'length>120'`, `awk 'length>300'`), and `verifiers/floors-registry.json` holds
  **19** instrument rows, none a byte or line ceiling on `SKILL.md` (all 19 are assertion-count
  floors on other instruments). **Not taken this round:** the floors guard is a frozen instrument no
  seat in this wave owns, and `SKILL.md` is at the 600-line box (600 of 600), so a promised row add
  has nowhere to land.
- **Proposal 2** (move `## Gate registry` out of `SKILL.md`) stays an **L0 question** rather than a
  claim (`corpus/QUALITY.md` Q67). The section sits at `SKILL.md` line 443 and
  `verifiers/REGISTRY.md` does not exist. **Not taken this round:** `SKILL.md` is at 600 of 600
  lines and no seat owns it.
- **Proposal 3** (land the page round 74 rejected and use it on the skill's own description) stays
  carried and is **still unimplemented** in the part that matters: the page is admitted (S213) and
  `corpus/knowledge/description-trigger-discipline-round85.md` exists, but the frontmatter
  description still measures **1021** characters with a **151**-character first sentence, and
  `SKILL.md` is at 600 of 600 lines, so a rewrite has to be paid for by lines saved elsewhere — and
  this wave gives the 600-line skill budget to no seat. Not trivially citable: the remaining work is
  the description rewrite, not a new registry row.
- **Proposal 4** (don't close a round before its falsify wave runs) stays **unimplemented as a
  protocol rule**. Wave `r100-w1` carries 11 seats, of which 6 are attack seats (2 reviewers, 2
  mutation-testers, 1 critic, 1 sentinel) beside 3 builders, 1 scout and 1 connector — adjacent
  practice, not the proposal's "provisional" closure rule.
- **Proposal 5** (an evidence budget) stays carried and is **still unimplemented**: measured on
  this lane at the freeze, `.ufo` is **355 MB** of a **596 MB** working tree (`du -sh .ufo` and
  `du -sh --exclude=.ufo` from the lane root). Not this round's claim.

**Assimilation: none.** No proposal is newly implemented this round, and none of them is trivially
citable as a registry row, so this seat writes no row for any of them.

## Settlement

Settled by KotobaR100 (L1) at integration, after WAVE-DONE for `r100-w1` (11 of 11 seats settled).

- **Applied** onto the freeze `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`, in order: ScribeCorpusR100
  (`042c2270…`), ExecAnchorR100 (`f2d1efee…`), ExecArmsR100 (`7b4e2dbc…`); each `git apply --check`
  clean, sha256 equal to its READY file.
- **L1 additions:** coverage-map rows for this lesson and for
  `corpus/lessons/round-99-verifier-spotcheck.md` (closure-authored, indexed, never edited — it was
  the cause of the base's two red corpus gates, `corpus.index unindexed=1`); QUALITY **Q90** for the
  mistake above; an equal-mode re-record of `verifiers/corpus-baseline.json` taken after every corpus
  file of the landing tree was in place (Q89).
- **S276 flip.** S276 is a `rejected` row whose flip condition reads "a sourced pathlib-semantic rule
  is itself the claim". C1's t04 arm is that claim, so the flip condition is met; per rule 2 the
  repair is the new row S282 (`supersedes S276 —`), and S276's cells stay as they are
  (ScoutSourcesR100 § 4.1).
- **Rejected this round:** a comma-list line-anchor authority (Sphinx `:lines:`), ScoutSourcesR100 § 5
  — a directive option value, not a citation convention; the ground for C2 is the lane's own
  documented contract (`strip_token_dressing` docstring) and its own usage in `SKILL.md`.
- **Post-freeze counter findings (disclosed, not rescued; the frozen kill rule names only the frozen
  controls):** MutTesterAnchorR100 built three worlds that read `C2-PREDICATE-MET` without the honest
  shape — `w2-source-sniff-arm` (the bound the counter header already names), `w3b-blind-window-extra`
  (`SELFTEST_RE` deletes module-level text between `self_test` and `build_parser`), `w5-dynamic-pin`
  (an `INSTRUMENT_PINS` entry computed by code). The landing uses none: its arm calls both public
  checks, nothing changes between `self_test` and `build_parser`, and the admitted pin is a literal
  40-hex blob. MutTesterDispatchR100 measured 13 survivors among 16 new C1 mutants (state/fleet
  substrate paths, the `--json` payload's other fields); routed to a successor round.
- **Readings** (landing revision, C1/C2 counters, census, no-harm) are in `LOG.md` § Round 100 and
  `.ufo/waves/round-100/receipts/landing/`. The verdict belongs to the non-author closure.
