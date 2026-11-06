# ScoutSourcesR100 — re-open S282–S285 and the C2 comma-anchor authority

Seat: ScoutSourcesR100 (scout, r100-w1). Lane: kotoba-shokunin. Access date: **2026-11-06**.
Tooling: system `curl`, `sha256sum`, `wc -w`, `python3 -B` (stdlib only). **No tool installs this seat.**
Scratch (created and deleted on exit): `/fast/scratch/hyaku/kotoba-r100/ScoutSourcesR100`.
**No HTML page is stored under `.ufo/waves/round-100/w1`** — digests, byte counts, line numbers and
short excerpt lines only, in `.ufo/waves/round-100/w1/ScoutSourcesR100/receipts.txt`.

**No repo writes.** This seat wrote only its own receipt file and this report. It did not touch
`corpus/SOURCES.md`, the plan, the counters, `verifiers/`, or any other seat's files.

---

## 0. Answers in one line each

1. **All four pinned sources reproduce the L1's digests byte-for-byte, twice.** `pathlib`
   `090f3b03…`, `tempfile` `0eef9098…`, `unittest` `90fb3809…`, `ptrace` `69cd309e…` — each equal to
   `receipts/sources-opened.txt`, and each stable across two independent fetches. **No finding.**
2. **S282 grounds the t04 arm, but the L1's opened quote is half of what t04 needs.** The t04 mutant
   swaps `path.is_dir()` for `path.exists()`; only the **§ Path.exists** entry ("Return True if the
   path points to an existing file or directory") carries the *contrast* the mutant exploits. Both
   entries are on the same page and the same digest — **S282's `anchor` cell must name both**
   (§ Path.is_dir @ raw 1362 **and** § Path.exists @ raw 1323), not is_dir alone. Tier **A**, kind
   **docs**, scope narrowed to the pathlib semantics (not to the lane's arm).
3. **Line numbers differ between the `/3/` alias and the pinned `/release/3.15.2/` URL** — the
   registry's existing rows quote the *alias* numbers. S282–S284 must quote the **pinned** numbers
   (is_dir 1362, exists 1323, read_text 1521; cleanup 386; errors 2410, failures 2418). The existing
   rows' numbers are off by 2–3. Concrete trap, flagged in §4.
4. **The C2 comma-anchor candidate authority: REJECTED as C2's ground.** Sphinx's `literalinclude`
   `:lines:` option *is* a documented comma-separated line-anchor list — but it is a **directive
   option value**, not a `path:N,M` citation token, so citing it would credit the rule to the wrong
   authority (QUALITY **Q23**/M24). The real ground for the lane's `file:N,M` form is the lane's own
   `SKILL.md:116` (`S090 :10,18,34,40-42`) — `own-work`, tier A. Flip condition in §5.
5. **The `/3/` alias digests of S253/S270/S276 do NOT reproduce today** (all three), independently
   re-confirming round-99's finding; the pinned `/release/3.15.2/` URLs are stable. The frontier
   step's re-pinning is correct.

---

## 1. Access records — HTTP, bytes, sha256, twice

Two independent fetches of each URL (`curl -sS -o <file> -w '%{http_code}' -L <url>`), into the
seat's scratch dir; `cmp` on the two copies; `sha256sum` on each.

| URL | HTTP | bytes | sha256 (pass 1) | sha256 (pass 2) | equal? | = L1's `sources-opened.txt`? |
|---|---|---|---|---|---|---|
| `https://docs.python.org/release/3.15.2/library/pathlib.html` | 200 | 270 630 | `090f3b03b648c271f4d810f0c37a51b2b54ebbdaa8130466d695e836e7a399ca` | same | **yes** | **EQUAL** |
| `https://docs.python.org/release/3.15.2/library/tempfile.html` | 200 | 74 630 | `0eef90989f9e1e4d261b8259e620244270f0bb8773e6b56b221b9575df60ab41` | same | **yes** | **EQUAL** |
| `https://docs.python.org/release/3.15.2/library/unittest.html` | 200 | 336 394 | `90fb380940f290ed6611ab8907a0f11840d03cea258357b5b3702a6b2eba8387` | same | **yes** | **EQUAL** |
| `https://man7.org/linux/man-pages/man2/ptrace.2.html` | 200 | 104 833 | `69cd309ece177d54086771701b2085e31cabd14a92484647392bcda468f7bd35` | same | **yes** | **EQUAL** |

`cmp pass1 pass2`: pathlib identical · tempfile identical · unittest identical · ptrace.2 identical.

**All four are byte-identical to the L1's receipt.** The ptrace digest also equals the digest
recorded in registry row **S279** (`corpus/SOURCES.md:220`, `69cd309e…`, 104 833 B) — that row's
digest still reproduces; only its *quote* stops short (§4.3).

---

## 2. Located quotes, with HTML line numbers and `wc -w`

Line numbers are **raw HTML lines in the PASS-1 bytes of the pinned `/release/3.15.2/` URL**
(`pathlib.html`, `tempfile.html`, `unittest.html`) and of `ptrace.2.html`. Each quote is a single
≤25-word sentence, per the SOURCES contract rule 1.

### 2.1 pathlib — § Path.is_dir and § Path.exists

`pathlib.html` raw 1362: `<dt class="sig sig-object py" id="pathlib.Path.is_dir">`; body raw
1364–1367.

> **"False will be returned if the path is invalid, inaccessible or missing, or if it points to something other than a directory."**

`wc -w` = **22**. Occurs **exactly once** on the page (checked against the whole tag-stripped page).
Excerpt lines: 1364 `Return True if the path points to a directory. False will be` · 1365 `returned
if the path is invalid, inaccessible or missing, or if it points` · 1366 `to something other than a
directory. Use Path.stat() to distinguish` · 1367 `between these cases.`

`pathlib.html` raw 1323: `id="pathlib.Path.exists"`; body raw 1325–1326.

> **"Return True if the path points to an existing file or directory and False if the path is invalid, inaccessible or missing."**

`wc -w` = **22**. Occurs **exactly once** on the page. Excerpt: 1325 `Return True if the path points
to an existing file or directory and` · 1326 `False if the path is invalid, inaccessible or missing.`

### 2.2 pathlib — § Path.read_text (encoding)

`pathlib.html` raw 1521: `id="pathlib.Path.read_text"`; signature raw 1522
`Path. read_text ( encoding = None , errors = None , newline = None ) ¶`; body raw 1523 and 1531–1532.

> **"Return the decoded contents of the pointed-to file as a string."**

`wc -w` = **11** (body raw 1523). Companion, the sentence that carries the `encoding` parameter's
meaning:

> **"The file is opened and then closed. The optional parameters have the same meaning as in open()."**

`wc -w` = **17** (raw 1531–1532). **Shaping note (QUALITY Q42/Q53/Q56):** in the raw bytes this
renders as `meaning as in open() .` — a space before the period from the `<code>`/`<a>` markup. The
quote is *quote-equal after documented shaping* (markup removed, whitespace folded), **not
byte-exact**.

Deeper ground for the encoding default, fetched for the t05 arm's benefit (not a row candidate):
`https://docs.python.org/release/3.15.2/builtins/functions.html` — HTTP 200, 330 766 B, sha256
`2cda7dad887b0316555e75a175d0adb8199d5e07f49b0a1d48e77effac4c18cf`, identical on two fetches. § open
raw 1644–1647: `In text mode, if encoding is not specified, UTF-8 is used by default; if Python
UTF-8 Mode is disabled, locale.getencoding() is called …`; raw 1821–1822: `Changed in version
3.15: UTF-8 is now the default encoding, instead of the platform-dependent locale encoding ( PEP 686 ).`

### 2.3 tempfile — ignore_cleanup_errors (the S253 quote)

`tempfile.html` raw 386: `id="tempfile.TemporaryDirectory.cleanup"`; body raw 389–391.

> **"If ignore_cleanup_errors is true, any unhandled exceptions during explicit or implicit cleanup (such as a PermissionError removing open files on Windows) will be ignored"**

`wc -w` = **24**. Occurs **exactly once** on the page. Excerpt: 389 `cleanup() method. If
ignore_cleanup_errors is true, any unhandled` · 390 `exceptions during explicit or implicit cleanup
(such as a` · 391 `PermissionError removing open files on Windows) will be ignored,`

**Byte-for-byte the sentence S253 already records** (`corpus/SOURCES.md:194`, 24 words) — the
substitution row is quote-identical, only the URL/digest change.

### 2.4 unittest — TestResult.errors vs TestResult.failures (the S270 quote)

`unittest.html` raw 2410: `id="unittest.TestResult.errors"`; body raw 2412–2414.
`unittest.html` raw 2418: `id="unittest.TestResult.failures"`; body raw 2420–2422.

> **"Each tuple represents a test which raised an unexpected exception."** — `wc -w` = **10** (raw 2413–2414)

> **"Each tuple represents a test where a failure was explicitly signalled using the assert* methods."** — `wc -w` = **15** (raw 2421–2422)

Excerpts: 2413 `holding formatted tracebacks. Each tuple represents a test which raised an` · 2414
`unexpected exception.` · 2421 `holding formatted tracebacks. Each tuple represents a test where a
failure` · 2422 `was explicitly signalled using the assert* methods .`

**Shaping note:** raw 2422 reads `assert* methods .` (space before the period from the `<code>`
markup) — *quote-equal after documented shaping*, not byte-exact. The errors quote needs no shaping
(it ends `exception.`).

The pair is the whole point of S284: an **error** is "a test which raised an unexpected exception";
a **failure** is "a test where a failure was explicitly signalled using the assert* methods" — the
distinction the C1 kill rule turns on (a crash is a RUN-ERROR, a reported failure is a kill).

### 2.5 ptrace — access-mode check step (4) IN FULL, including the `CAP_SYS_PTRACE` conjunct

`ptrace.2.html` raw 1516–1520, § *Ptrace access mode checking*, algorithm step (4), in full:

> **"Deny access if the target process "dumpable" attribute has a value other than 1 (SUID_DUMP_USER; see the discussion of PR_SET_DUMPABLE in prctl(2)), and the caller does not have the CAP_SYS_PTRACE capability in the user namespace of the target process."**

`wc -w` = **39** — over the 25-word SOURCES bound, so the **row quote** is the conjunct alone:

> **"and the caller does not have the CAP_SYS_PTRACE capability in the user namespace of the target process."**

`wc -w` = **17**, raw 1518–1520. Occurs **exactly once** on the page. Excerpt: 1518 `PR_SET_DUMPABLE
in prctl(2) ), and the caller does not have` · 1519 `the CAP_SYS_PTRACE capability in the user
namespace of the` · 1520 `target process.`

Footline raw 1713: `Linux man-pages 6.19 2026-06-05 ptrace(2)` — man-pages content is version-pinned,
which is why this page's digest is stable while the `docs.python.org/3/` aliases are not.

**This confirms round-99's ScoutSourcesR99 finding exactly:** S279's recorded quote (14 words,
"…value other than 1") **stops before** the `CAP_SYS_PTRACE` conjunct; the conjunct is real and is
in the same step (4) at the same anchor. S285's whole reason to exist is to carry it.

---

## 3. Does S282 ground the C1 t04 arm? — **Yes, with the scope narrowed and one anchor added**

### 3.1 What the t04 arm actually attacks

`verifiers/verify_dispatch_prompts.py:1973–1984` — `main()`'s substrate check, in this order:
`prompts`, `state_dir`, `fleet`:

```
1973    for path, what in ((prompts, "prompts directory"),
1974                       (state_dir, "state directory"),
1975                       (fleet, "fleet root")):
1976        if not path.is_dir():
...
1984            return 2
```

The t04 mutant (`verifiers/fixtures/round-100/selftest-kills.py:149–150`) replaces
`        if not path.is_dir():` with `        if not path.exists():`. With the mutant, a **plain
file** passed as `--prompts` passes the substrate check and execution reaches
`evaluate_dispatch_04` → `verifiers/verify_dispatch_prompts.py:351`
`names = sorted(p.name for p in prompts_dir.iterdir() if p.is_file())` → **`NotADirectoryError`**.

Two facts I verified for the arm's author (ExecArmsR100):

- `NotADirectoryError` is `OSError`/`Exception`, **not** `EnvError`
  (`verifiers/verify_dispatch_prompts.py:151 class EnvError(Exception)`), and `main()` catches only
  `EnvError` at line 1988 — so under the mutant the exception **propagates out of `main()`**. An arm
  that calls `main()` without catching it crashes the self-test → **RUN-ERROR, not a kill** (the
  plan states this constraint for t04; the code confirms it).
- The arm must therefore assert on **behaviour** (the exit code / payload / stderr of `main()` with
  argv passed explicitly), never on the checker's source.

### 3.2 The tier/scope judgement (CORPUS.md + corpus/QUALITY.md)

- **CORPUS.md tier A** = "primary or authoritative for that scope (spec, official docs, source
  code, original paper, maintainer statement, the lane's own re-runnable gate output)". Python's
  *own* documentation of `pathlib` is tier **A** for the scope "what `Path.is_dir` / `Path.exists`
  return for a plain file in CPython 3.15.2". Kind **docs**.
- **Scope must not be widened** to the lane's t04 arm or to "directory checks in general". The
  doc grounds *the stdlib semantics*; the arm grounds *the lane's behaviour*. QUALITY **Q20/Q23**:
  "a check that approximates an authority's rule names the parsed rule it approximates and carries
  run counterexamples in both directions" — the C1 arm observes `main()`'s exit code; it never reads
  the doc, and the doc never mentions the lane.
- **QUALITY Q23 (the real gap):** "A rule attributed to an authority carries a located quote from
  that authority **plus the sweep showing whether the other authorities state it**". The t04 mutant
  is `is_dir` → `exists`. The **§ Path.is_dir** quote alone (22 words, "…if it points to something
  other than a directory") states only that a plain file is *not* a directory. It does **not** show
  that the mutant's replacement behaves differently. That half is carried by **§ Path.exists**
  ("Return True if the path points to an existing file **or directory**"). **Both entries are on
  the same page and the same digest**, so no second row is needed — but S282's `anchor` cell must
  name **both** anchors, and the `teaches` cell should carry the contrast. The L1's opened receipt
  (`receipts/sources-opened.txt`) quotes **is_dir only**, which is why the plan's S282 line reads as
  if is_dir alone grounds the arm. **Flagged to the L1 and ScribeCorpusR100** (whose file it is).

### 3.3 The supersession is well-formed

S276 (`corpus/SOURCES.md:217`) is status `rejected`, with the reason "REJECTED: additional
primitive-authority row deferred while this round observes t06 directly; not a rejection of the
documented semantics; **flip: a sourced pathlib-semantic rule is itself the claim**", `used-by
corpus/lessons/round-97.md`.

Round 100 makes a sourced pathlib-semantic rule **exactly** the claim (C1 cites S282 for t04), so the
flip condition is met, and the append-only repair (CORPUS.md rule 2 — "A correction is a new row
whose `teaches` opens `supersedes S0NN —`") is a **new row S282**, with S276's protected cells left
untouched. The URLs differ (`/3/library/pathlib.html` vs `/release/3.15.2/library/pathlib.html`), so
QUALITY **Q84**'s "second row on the same URL" clause does not bar it. S282's `teaches` should open
`supersedes S276 —` and say why (the alias digest does not reproduce; see §6).

---

## 4. Registry check for each URL, and the line-number trap

### 4.1 Grep of `corpus/SOURCES.md` (207 rows, ids S001–S281, no duplicate ids)

```
$ grep -n 'docs.python.org/release/3.15.2/library/pathlib.html'   corpus/SOURCES.md   -> no match
$ grep -n 'docs.python.org/release/3.15.2/library/tempfile.html'  corpus/SOURCES.md   -> no match
$ grep -n 'docs.python.org/release/3.15.2/library/unittest.html'  corpus/SOURCES.md   -> no match
$ grep -n 'man7.org/linux/man-pages/man2/ptrace.2.html'            corpus/SOURCES.md   -> line 220 (S279, mined)
$ grep -n 'docs.python.org/3/library/pathlib.html'                 corpus/SOURCES.md   -> line 217 (S276, rejected)
$ grep -n 'docs.python.org/3/library/tempfile.html'                corpus/SOURCES.md   -> line 194 (S253, mined)
$ grep -n 'docs.python.org/3/library/unittest.html'                corpus/SOURCES.md   -> line 211 (S270, mined)
$ grep -n 'sphinx-doc.org'                                        corpus/SOURCES.md   -> no match
$ grep -n 'git-scm.com'                                           corpus/SOURCES.md   -> lines 193, 208, 209, 218 (no git-log row)
```

- **S282, S283, S284** — the pinned `/release/3.15.2/` URLs are **not in the registry**: first rows
  on those URLs. Precedent for the pinned-release convention already exists: **S281**
  (`corpus/SOURCES.md:222`) cites `https://docs.python.org/release/3.15.2/library/argparse.html`.
- **S285** — the ptrace URL **is** held, by **S279** (`mined`, `used-by corpus/lessons/round-98.md,
  plans/round-98-addendum-1.md`). QUALITY **Q84**: "a second row on the same URL is admitted only
  when the scout's Gate entry shows a distinct document or scope". The distinct scope here is
  narrow but real — S279's scope is *"the access-mode check that governs /proc/<pid>/environ reads
  and its denial for a non-dumpable target"*, anchored on the `PTRACE_MODE_READ` entry (raw 1421) and
  on step (4) **truncated before the parenthetical**; S285's scope is *"the `CAP_SYS_PTRACE`
  conjunct of access-check step (4) itself"*. Because S279's `teaches`/`anchor` cells are protected
  (CORPUS.md rule 2: only `status`, `recheck`, `used-by` change in place), the append-only way to
  carry the fuller quote is a **new row opening `supersedes S279 —`** — which is what the plan's
  frontier step already does. **Admissible, conditional on the Gate entry stating that distinct
  scope explicitly.** S279's own status stays `mined` (it is genuinely cited by round-98); the
  superseding row does not retire it.
- Free ids for the frontier: **S282–S285** are free (max existing id S281, no duplicates).

### 4.2 The line-number trap (highest-value finding for the scribe)

The **same page** sits at **different raw HTML line numbers** on the `/3/` alias and on the pinned
`/release/3.15.2/` URL — the alias carries three extra lines above `pathlib` and three above
`tempfile`. The existing registry rows quote the **alias** numbers:

| anchor | registry row (alias URL) | pinned `/release/3.15.2/` URL |
|---|---|---|
| `pathlib.Path.is_dir` id | S276: "HTML lines 1367-1369" (quote body) | id **1362**, body **1364–1367** |
| `pathlib.Path.exists` id | — | id **1323**, body **1325–1326** |
| `pathlib.Path.read_text` id | — | id **1521**, sig 1522, body 1523 / 1531–1532 |
| `tempfile.TemporaryDirectory.cleanup` id | S253: "lines 391-395" (stripped) | id **386**, body **389–391** |
| `unittest.TestResult.errors` id | S270: "HTML line 2410" | id **2410**, body 2412–2414 |
| `unittest.TestResult.failures` id | S270: "HTML line 2418" | id **2418**, body 2420–2422 |
| `ptrace` step (4) | S279: "HTML lines 1516-1520" | **1516–1520** (identical — man-pages is version-pinned) |

Verified on the alias today: `Path. is_dir` id 1365 / quote 1367 · `Path. exists` id 1327 ·
`cleanup` id 389 / quote 392 · `errors` id 2411 / quote 2413.

**Consequence:** S282–S284 must quote the **pinned** numbers in the `anchor` cell; copying the
alias numbers (or S276/S253/S270's numbers) into the new rows would put a wrong pointer into a
frozen corpus cell — the very class this round mines (see §7).

### 4.3 S285 / S279 — the quote gap is confirmed, not closed by S279

S279's recorded quote is 14 words and its `anchor` cell says it "stopped before the parenthetical on
SUID_DUMP_USER and CAP_SYS_PTRACE". I re-opened the same bytes (digest identical to S279's) and the
conjunct is there at raw 1518–1520. **S279 cannot be edited in place** (protected cells), so S285
as a superseding row with the 17-word conjunct quote is the correct append-only shape.

### 4.4 Quote uniqueness (QUALITY Q32 — a counter must match the recorded quote exactly)

Checked against the whole tag-stripped page, each quote occurs exactly once:
is_dir 1 · exists 1 · ignore_cleanup_errors 1 · unittest errors 1 · unittest failures 1 (the
`assert* methods .` spacing is a shaping artifact of the strip, not a second occurrence) ·
`CAP_SYS_PTRACE` conjunct 1. No sibling-page ambiguity: the pathlib `False will be returned …`
sentence also appears for `is_file`, `is_symlink`, `is_socket`, `is_fifo`, `is_block_device`,
`is_char_device` — each with its **own** final noun ("…other than a regular file", "…other than a
symbolic link", …), so the **whole 22-word sentence** is unique, but a bare substring such as
"False will be returned if the path is invalid, inaccessible or missing" is **not** (7 occurrences on
the page). **A quote match must carry the full sentence.**

---

## 5. The C2 candidate authority — **REJECTED as C2's ground** (with flip condition)

**Candidate opened:** the Sphinx documentation's `literalinclude` directive option `:lines:`
(upstream source pinned at tag `v8.2.3`).

- Rendered URL `https://www.sphinx-doc.org/en/stable/usage/restructuredtext/directives.html`:
  HTTP 200, 170 372 B, **sha256 differs between two consecutive fetches**
  (`9a4377f1…` then `d629d47b…`) — same byte length, one Cloudflare email-protection token differs
  at raw line 1620. **Not digest-stable.**
- Pinned upstream source
  `https://raw.githubusercontent.com/sphinx-doc/sphinx/v8.2.3/doc/usage/restructuredtext/directives.rst`:
  HTTP 200, 55 809 B, sha256 `97282c43253cfbc6c67461f8754bcc60137a207acc6d1c78cf1e8d9f698bb458`,
  **identical on two fetches**. Stable.
- Located quotes (rst line numbers): 1045 `.. rst:directive:option:: lines: line numbers` ·
  1046 `:type: comma separated numbers` · 1051 `:lines: 1,3,5-10,20-` · 1053 `This includes line 1,
  line 3, lines 5 to 10, and line 20 to the end.`
  - **"comma separated numbers"** — `wc -w` = **5** (line 1046)
  - **"This includes line 1, line 3, lines 5 to 10, and line 20 to the end."** — `wc -w` = **16**
    (line 1053)
- Contrast source (fetched, not a candidate): `https://git-scm.com/docs/git-log` — HTTP 200,
  375 834 B, sha256 `f206647fba42b627f46d29993490fbb585adedaa5d27b9ed575f50ef9002f69b`, identical on
  two fetches. `-L <start> , <end> : <file>` at raw 3794, "Trace the evolution of the line range given
  by <start> , <end> ," at 3797–3798: in git the comma means a **range**, and the path follows the
  colon — the **opposite** reading of the lane's form.

**Verdict: REJECT — do not admit a row for this in round 100, and do not cite it as C2's
authority.** Reasons:

1. **Wrong surface.** Sphinx's `:lines:` is a *directive option value* (`:lines: 1,3,5-10`), not a
   `path:N,M` **citation token**. C2's fix is in `strip_token_dressing`, whose job is to strip a
   trailing anchor off a *path token*. Citing Sphinx would credit the rule to the wrong authority —
   QUALITY **Q23**/M24 ("Rule credited to the wrong authority") and **Q20** ("a check that
   approximates an authority's rule names the parsed rule it approximates").
2. **No round-100 claim rests on it.** C2's predicate is frozen and reads the *lane's* own files;
   the anchor-lists counter's truth table is built on the lane's own token forms. SOURCES contract
   rule 4: "Expansion is knowledge, not rows … a short registry of opened, honestly tiered rows
   beats a long one."
3. **The real ground is already in the lane.** The `file:N,M` form is the lane's own convention:
   `SKILL.md:116` reads `(S090 `:10,18,34,40-42`)` — a comma list **with** a range — and
   `corpus/QUALITY.md:50` reads `corpus/lessons/round-55-verifier-spotcheck.md:82,135`, `:32,36-37`,
   `:69-72,133`. That is `kind: own-work` (contract: "`source` — … a repo path or command for
   `own-work`"), tier **A** (the lane's own committed bytes), and it is the form the C2 truth table
   rows `r01`/`r02`/`r04` encode. The counter header itself says so: "a comma-list anchor `:N,M`
   (the form SKILL.md already uses, `S090 :10,18,34,40-42`)".
4. **The rendered URL is not citable as-is** even if a row were wanted — it is a rolling alias whose
   bytes move (two fetches, different digests). Any future row must cite the pinned upstream `.rst`
   at a tag, as recorded above.

**Flip condition (for a future round to admit it):** admit a row — kind `docs`, tier A, source
`https://raw.githubusercontent.com/sphinx-doc/sphinx/v8.2.3/doc/usage/restructuredtext/directives.rst`,
sha256 `97282c43…`, anchor "§ literalinclude, the `:lines:` option (rst lines 1045–1053)", quote
"comma separated numbers" (5 words) — **iff** some claim needs the *external* existence of a
comma-separated line-anchor list (e.g. a claim that `path:N,M` is a general convention rather than a
lane-local one). Then, and only then, it must be cited **with** the git-log counter-example
(`-L <start>,<end>:<file>`, comma = range) so no reader concludes the comma always means a list.
Note the round-100 plan fixes the frontier at S282–S285; adding a sixth row would be an L1 act.

---

## 6. Why the re-pinning to `/release/3.15.2/` is right (alias digests do not reproduce)

The `/3/` alias digests recorded in **S253, S270, S276** all fail to reproduce today (this seat's
independent fetch, 2026-11-06):

| row | recorded (alias) | today's alias fetch | verdict |
|---|---|---|---|
| S276 `pathlib` | 271 233 B `b55e4f28…` | 271 233 B `eda0d4a5…` | same length, **different digest** (footer minute) |
| S253 `tempfile` | 75 190 B `cb28e1b2…` | **75 198 B** `2bef9acd…` | **length differs by 8** (content changed, not only the footer) |
| S270 `unittest` | 336 978 B `f9510cd7…` | 336 978 B `a3c45299…` | same length, **different digest** |

The alias footers now read `Last updated on Nov 06, 2026 (14:48 UTC)`; the pinned
`/release/3.15.2/` pages read `Last updated on Oct 25, 2026 (17:03 UTC)` and are byte-stable across
both fetches. This independently re-confirms round-99's ScoutSourcesR99 finding, and it is why
S282–S284 must be pinned rows citing the release URL (with the pinned line numbers of §4.2), not
re-pointed alias rows.

---

## 7. Cross-checks on the frozen instruments (read-only; no edits)

**Counter anchor hygiene (C1).** I parsed `verifiers/fixtures/round-100/selftest-kills.py`'s
`CLAIMS` (via `importlib`, no execution of the counter) and checked every frozen anchor against
`verifiers/verify_dispatch_prompts.py`: **52 distinct anchor strings** across
`c1/r99c1/r98c1/r97c1/r96c1/r95c1`; **49 occur exactly once** in the dispatch checker; the 3
exceptions are all `r95c1` anchors that belong to the *other* instrument
(`verifiers/check_mutation_battery.py`) and correctly occur 0 times there.

Consequence for **ExecArmsR100**: the counter's `mutant_text()` requires `original.count(anchor) == 1`
and raises `NotEvaluated("anchor miss: …")` otherwise — a **could-not-evaluate (exit 2)**, not a
kill. So **no new `self_test()` code in `verify_dispatch_prompts.py` may contain any frozen anchor
text verbatim** — in particular not `        if not path.is_dir():`, not `    for cid in wanted:`,
not `        return path.read_text(encoding="utf-8")`, not `    wanted = list(args.check) if args.check
else list(CHECK_IDS)`, and none of the other 49. (`    for cid in wanted:` appears **twice** in the
counter file itself — lines 153 and 173, for the c1 and r99c1 tables — but exactly once in the
instrument, which is what the counter counts.)

**C2 fix line.** `    m = re.match(r"^(.+\.\w+):\d+(-\d+)?(,\d+(-\d+)?)*$", tok)` occurs **0** times
in the base `verifiers/verify_skill_checklist.py`; the base line occurs **1** time. The C2 fix line
is genuinely absent at the base, and the counter's `FIX_LINE`/`BASE_LINE` pair matches the file.

**Behavioural check of the C2 regex (my own simulation, no counter run).** With the counter's
`TRAILING_PUNCT = ",;:)]}\"'"` rstrip applied first and the FIX regex
`^(.+\.\w+):\d+(-\d+)?(,\d+(-\d+)?)*$`:

| truth-table row | token | base `strip_token_dressing` | with FIX |
|---|---|---|---|
| r01 `:30,37` | `corpus/lessons/x.md:30,37` | unchanged → red | → `corpus/lessons/x.md` → resolves |
| r02 `:3,7-9` | `…/x.md:3,7-9` | unchanged → red | → `…/x.md` → resolves |
| r03 `:30,37,` | `…/x.md:30,37,` | rstrip → `…/x.md:30,37` → red | → `…/x.md` → resolves |
| r04 `:10,18,34,40-42` | `…/x.md:10,18,34,40-42` | unchanged → red | → `…/x.md` → resolves |
| r10 `:30,abc` | `…/x.md:30,abc` | unchanged → red | unchanged → red |
| r11 `:30,,37` | `…/x.md:30,,37` | unchanged → red | unchanged → red |
| r12 `:5-` | `…/x.md:5-` | unchanged → red | unchanged → red |
| r13 `:,30` | `…/x.md:,30` | unchanged → red | unchanged → red |
| r14 `:abc` | `…/x.md:abc` | unchanged → red | unchanged → red |

The 4 comma rows are exactly the base's 8 mismatches (4 rows × 2 check paths) — consistent with
`receipts/c2-base.txt` ("C2 mismatches 8 of 28"). **No counter defect found**; the C2 counter's
truth table, the plan's frozen fix line, and the base behaviour all agree.

---

## 8. Risks / open items for the L1

1. **S282's `anchor` must cite both § Path.is_dir (raw 1362) and § Path.exists (raw 1323)** — the
   t04 mutant's contrast lives in `exists()`. Flagged to ScribeCorpusR100 (§3.2). The L1's
   `receipts/sources-opened.txt` quotes is_dir only.
2. **S282–S284 must use the pinned URL's line numbers** (§4.2), not the alias numbers in
   S276/S253/S270.
3. **S285 is a second row on a URL the registry already holds (S279)** — admissible only with the
   Gate entry stating the distinct scope (the `CAP_SYS_PTRACE` conjunct of step (4)) and opening
   `supersedes S279 —`; S279's protected cells stay untouched and its status stays `mined`.
4. **The C2 comma-anchor authority is rejected** for this round (§5); the ground is the lane's own
   `SKILL.md:116` / `corpus/QUALITY.md:50` (`own-work`, tier A). If the L1 wants an external row it
   is an L1 act (the plan fixes the frontier at S282–S285) and must cite the pinned upstream `.rst`,
   never the rolling rendered page.
5. **No counter defect found** in either frozen counter, on the evidence re-checked here (§7).

## 9. Reproducibility of this seat's receipts

Every command is stdlib + `curl`/`sha256sum`/`wc`. Re-run:

```sh
S=/fast/scratch/hyaku/kotoba-r100/ScoutSourcesR100; mkdir -p $S/p1 $S/p2; cd $S
for u in https://docs.python.org/release/3.15.2/library/pathlib.html \
         https://docs.python.org/release/3.15.2/library/tempfile.html \
         https://docs.python.org/release/3.15.2/library/unittest.html \
         https://man7.org/linux/man-pages/man2/ptrace.2.html; do
  n=$(basename "$u" .html)
  for p in p1 p2; do
    curl -sS -o "$S/$p/$n.html" -w "$u %{http_code} " -L "$u"
    printf '%s B sha256 %s\n' "$(stat -c%s $S/$p/$n.html)" "$(sha256sum $S/$p/$n.html | cut -d' ' -f1)"
  done
  cmp $S/p1/$n.html $S/p2/$n.html && echo "$n identical"
done
```

Line numbers and quotes: `receipts.txt` in this seat's directory (excerpt lines, digests, `wc -w`
outputs). **No HTML is stored in the lane.**
