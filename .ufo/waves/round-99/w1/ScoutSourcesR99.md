# ScoutSourcesR99 — re-open S281 and the S279 conjunct

Seat: ScoutSourcesR99 (scout, r99-w1). Lane: kotoba-shokunin. Access date: **2026-11-06 (UTC)**.
Tooling: system `curl`, `sha256sum`, `python3 -B` (stdlib only). **No tool installs this seat.**
Scratch (created and deleted): `/fast/scratch/hyaku/kotoba-r99/ScoutSourcesR99/web` — fetched bytes
transient; **no HTML page is stored under `.ufo/waves/round-99/w1`**. Digests, byte counts and short
excerpt lines are in `.ufo/waves/round-99/w1/ScoutSourcesR99/receipts.txt`.

**No repo writes.** This seat wrote only its own receipt file and this report. It did not touch
`corpus/SOURCES.md`, the plan, the counters, or any other seat's files.

---

## 0. Answers in one line each

1. **S281 (argparse) — REJECT the L1's digest, ACCEPT the source.** The URL opens HTTP 200 and the
   `'append'` quote is real, unique and correctly located — but the L1's recorded sha256
   `bcd717f2…` **does not reproduce**: the `/3/` alias is a *rolling* page whose bytes change on
   every upstream docs rebuild. The L1's own bytes are provably the same page 20 minutes earlier
   (one 5-byte footer field differs). **S281 must cite a version-pinned URL** (`/release/3.15.2/…`,
   digest stable across five fetches), or cite `/3/` with an explicit "rolling build" note.
2. **S279 conjunct — CONFIRMED, and the registry row under-quotes it.** ptrace(2)'s access-check
   step (4) is at HTML lines 1516–1520 and does carry the `CAP_SYS_PTRACE` conjunct, which the S279
   row's quote stops before. The ≤25-word conjunct quote is in §2. The ptrace page digest
   **reproduces exactly** — unlike argparse.
3. **C2's honest-route candidate (`git-hash-object`) — REJECT for C2's route, ADMIT as a
   general row.** The `INSTRUMENT_PINS` admission does **not** rely on `git hash-object`: the pin
   value is read out of a committed tree by `git rev-parse <rev>:<path>`
   (`verifiers/check_tip_battery.py:344`). `git-hash-object` grounds a *different* fact (what an
   object ID is computed from), which is the fact that makes a hand-copied pin value meaningful.
   See §3 for the full reasoning and flip condition.

---

## 1. https://docs.python.org/3/library/argparse.html — the S281 candidate

### 1.1 Access record

| field | value |
|---|---|
| access date | 2026-11-06, 13:53:44Z – 14:13:36Z (five fetches, `curl -sS -L`) |
| HTTP | **200** (all five) |
| bytes | **334 994** (all five) |
| sha256 (observed) | **`906919fda1b652a56d07a61823ce6e169ae6acfd2afa3233a56d3c26bf4e732e`** |
| sha256 (L1, `receipts/sources-opened.txt`) | `bcd717f244b432fbee39f45742910347599f5f8b9f1dc6d4377a23c5c8faac16` |
| equal? | **NO.** Same byte length (334 994 B), different digest. |
| server | `last-modified: Fri, 06 Nov 2026 13:49:15 GMT`, `etag: "6aeddadb-51c92"` (`0x51c92` = 334 994 = `content-length`) |

**The L1's digest is real but not re-fetchable, and the cause is byte-exact.** The two byte strings
differ in **exactly 5 bytes** — the Sphinx footer field `Last updated on Nov 06, 2026 (HH:MM UTC)`
(HTML line 2712). Substituting only the minute field `13:47` → `13:27` in today's bytes reproduces
the L1's sha256 exactly:

```
python3 -B -c "import hashlib,re; d=open('argparse.html','rb').read(); \
  m=re.search(rb'Last updated on Nov 06, 2026 \((\d\d):(\d\d) UTC\)', d); \
  t=d[:m.start(1)]+b'13:27'+d[m.end(2):]; \
  print(hashlib.sha256(t).hexdigest()=='bcd717f244b432fbee39f45742910347599f5f8b9f1dc6d4377a23c5c8faac16')"
→ True
```

Differing byte range: **334740–334745**. So the L1's fetch (13:41:12Z) was served a rebuild stamped
`13:27 UTC`; my first fetch (13:53:44Z) was served a rebuild stamped `13:47 UTC`. `docs.python.org/3/`
is a **rolling alias**: its bytes move on every upstream docs rebuild, so **any digest recorded
against `/3/` is stale within the hour** and cannot be re-verified by a later reader.

This is not argparse-specific. The same rolling-footer mechanism breaks two other `docs.python.org/3/`
rows already in the registry, each provably by the footer field alone:

| row | URL | recorded sha256 | today's bytes | footer-only reconstruction |
|---|---|---|---|---|
| S253 | `/3/library/tempfile.html` | `cb28e1b2…` | 75 198 B (**recorded 75 190 B — length differs by 8**) | no footer-only match (content changed too) |
| S270 | `/3/library/unittest.html` | `f9510cd7…` | 336 978 B (length matches) | **`Nov 5, 22:32` → matches exactly** |
| S276 | `/3/library/pathlib.html` | `b55e4f28…` | 271 233 B (length matches) | **`Nov 5, 22:32` → matches exactly** |

**Scope note (not this seat's to fix):** S253/S270/S276 are frozen registry cells — `SOURCES.md` is
append-only and `check_sources_append_only.py` forbids editing their protected columns in place. The
only correct repair for them is a **new superseding row** whose `teaches` opens `supersedes S0NN —`
(SOURCES contract rule 2) — which is `ScribeCorpusR99`'s file to own, not mine. I record the fact
here so the L1 can decide whether to route it.

### 1.2 The located quote — and why it *does* ground the t08 arm

**Located quote** (on `/3/`, HTML lines **992–993**; markup removed, whitespace folded):

> `'append' - This appends each argument value to a list. It is useful for allowing an option to be specified multiple times.`

`wc -w` = **22** (the L1's recorded count reproduces exactly). The sentence occurs **exactly once**
per page (`grep -c` = 1 on `/3/`, on `/3.14/` and on `/release/3.15.2/`).

**Anchor-hygiene note for S281.** The bare marker text `'append'` occurs **twice** in the page —
HTML line 992 (the action entry) and HTML line 1065 (the `add_argument()` signature line). A quote
match must therefore carry the surrounding words, not the bare token; the located sentence above
does. (QUALITY **Q32** — a counter matching a quote must match the recorded quote, not a fragment.)

**Verdict on the t08 grounding: ACCEPT, with the scope narrowed.** The arm grounds the *stdlib
semantics* the t08 mutant attacks, and nothing more:

- `verifiers/verify_dispatch_prompts.py:527` declares `--check` with `action="append"` and
  `choices=CHECK_IDS`.
- `verify_dispatch_prompts.py:1715` reads `wanted = list(args.check) if args.check else list(CHECK_IDS)`
  — this is the exact line the **t08-main-check-ignored** mutant replaces with
  `wanted = list(CHECK_IDS)` (`verifiers/fixtures/round-99/selftest-kills.py:148-150`).
- The argparse doc is the authority for *what `action="append"` means*: each occurrence appends its
  value to a list, so `--check dispatch.04` yields `args.check == ['dispatch.04']` and therefore
  selects exactly that one check. The doc grounds the **option semantics**; it does **not** ground
  that the lane then honours `args.check` — that is the lane's own code, and the arm's kill must
  come from observing `main()`'s behaviour, not from the doc.

**Recommended S281 scope (tier A, kind `docs`):** "what `action='append'` does to a repeatable
option's values — each occurrence appends to a list, so `--check dispatch.04` leaves `args.check`
holding exactly `['dispatch.04']`" — scoped to the argparse option semantics, **not** to the lane's
selection behaviour. Under the tier definitions in `/home/vgpnk/Projects/shokunin/CORPUS.md` (rule 3,
tier A = "primary or authoritative for that scope (spec, official docs, …)"), Python's own
documentation is tier A for argparse's own semantics.

### 1.3 Registry check for the URL — **no existing row; S281 is a first row**

```
$ grep -n "argparse" corpus/SOURCES.md
157: | S211 | anthropics/skills — skill-creator scripts/run_eval.py — https://github.com/anthropics/skills/… | code | A | … argparse defaults at lines 266-267 …

$ grep -rn "library/argparse.html" corpus/
(no hits)
```

Only **one** hit for "argparse" in the whole registry, and it is **S211** — a *code* row on a
*GitHub* URL (anthropics/skills `run_eval.py`) that mentions argparse defaults in passing. **The
docs.python.org argparse URL is not held by any row.** So S281 is not a second row on a held URL
(no E04/W04 duplicate risk) — it is a first row on a new URL, which is exactly what Q84 permits
("a URL the registry already holds is re-opened and cited by its existing id … a second row on the
same URL is admitted only when the scout's Gate entry shows a distinct document or scope"). The
distinct-document test is met: S211 is `kind=code` on a different document about a different
subject; S281 is `kind=docs` on argparse's own reference page.

Registry measurements (read-only):

- rows: **206** (both `grep -cE '^\|[[:space:]]*S[0-9]{3,}'` and the distinct-id count agree);
  next unused id is **S281** (highest present is S280; `grep -c "S281"` = 0) — consistent with the
  L1's naming.
- W04 warnings at freeze: **34** (`grep -c W04 .ufo/waves/round-99/receipts/census-before.txt`).
  Adding S281 does not add a W04, because the argparse URL is unique across scopes.

### 1.4 What S281 should record (recommendation to the scribe, not an edit)

- **URL**: prefer the version-pinned `https://docs.python.org/release/3.15.2/library/argparse.html`
  — HTTP 200, **327 874 B**, sha256
  **`36e8d5361b591376bbf9255c08147ece82f5f1fe52a5abd3d149656e902bb8ae`**, identical across **five**
  fetches (13:54Z–14:12Z) because the release snapshot is frozen; its footer reads
  `Last updated on Oct 25, 2026 (17:03 UTC)`. On that URL the quote sits at **HTML lines 989–990**.
- If `/3/` is kept, the row must say in its `anchor` cell that the page is a **rolling build** whose
  `Last updated on <date> (<HH:MM> UTC)` footer changes on each upstream rebuild, and the recorded
  sha256 will not re-verify. (Same caveat applies to the `/3.14/` URL — its digest
  `d900b72d3716f848c3bbb8ae6c2ad5da232738ad061c56879f5bed07787968e7` is likewise build-stamped.)
- `status` = `mined`; `kind` = `docs`; `tier` = `A` (scoped as in §1.2); `recheck` — a cadence, not a
  one-shot date, is the safe form for a page that moves.
- `used-by` must name a path that exists on disk (census **E11**), e.g. `corpus/lessons/round-99.md`
  plus the plan.

---

## 2. https://man7.org/linux/man-pages/man2/ptrace.2.html — the S279 conjunct

### 2.1 Access record

| field | value |
|---|---|
| access date | 2026-11-06, 13:54Z |
| HTTP | **200** |
| bytes | **104 833** |
| sha256 | **`69cd309ece177d54086771701b2085e31cabd14a92484647392bcda468f7bd35`** |
| equal to S279's recorded digest? | **YES — byte-identical.** S279 records `fetched 2026-11-06 by ScoutSourcesR98, HTTP 200, 104833 B, sha256 69cd309e…`. |

**This page is stable and its digest reproduces exactly** — the opposite of argparse. The S279 row
needs no digest repair.

### 2.2 Access-check step (4) in full — HTML lines **1516–1520**

> (4)  Deny access if the target process "dumpable" attribute has a value other than 1 (SUID_DUMP_USER; see the discussion of PR_SET_DUMPABLE in prctl(2)), and the caller does not have the **CAP_SYS_PTRACE** capability in the user namespace of the target process.

`wc -w` = 40 (whitespace-normalised, markup removed).

**The ≤25-word quote for the conjunct (16 words):**

> the caller does not have the CAP_SYS_PTRACE capability in the user namespace of the target process

Verified as an exact substring of the whitespace-normalised step-(4) text. Its HTML lines are
**1518–1520** (`…and the caller does not have / the CAP_SYS_PTRACE capability in the user namespace of the / target process.`).

### 2.3 The defect this closes (round-98 closure routed defect 5)

The S279 row's `teaches` cell already reads *"a non-dumpable counter denies a child **without
CAP_SYS_PTRACE** the PTRACE_MODE_READ check that environ reads go through"* — the substance is
right — but the row's `anchor` cell quotes only

> "Deny access if the target process "dumpable" attribute has a value other than 1" (14 words)

"at HTML lines 1516-1520, **stopped before the parenthetical on SUID_DUMP_USER and CAP_SYS_PTRACE**".
So the row's *quote* is a truncated prefix of a **conditional** rule, and the truncation is exactly
where the second conjunct lives. A reader working from the quoted text alone would read step (4) as
"non-dumpable ⇒ deny", missing that the rule is a conjunction: non-dumpable **AND** caller lacks
`CAP_SYS_PTRACE`.

**Verdict: the conditional reading in the row's `teaches` cell is CONFIRMED by the source.** The
correction the round-99 lesson records is therefore *not* a change of substance — it is the
**completion of the located quote** so the citation carries the whole rule it cites.

Two further readings worth carrying into the note:

- **Step (3), HTML lines 1506–1514**, carries the *other*, permissive `CAP_SYS_PTRACE` disjunct:
  "The caller **has** the CAP_SYS_PTRACE capability in the user namespace of the target."
  (HTML lines 1513–1514). Two `CAP_SYS_PTRACE` mentions sit in the same algorithm, with opposite
  polarity — a quote fragment must not be able to flip either.
- **PTRACE_MODE_READ**, HTML lines 1421–1425: "reading /proc/pid/auxv, /proc/pid/environ, or
  /proc/pid/stat" at lines 1423–1424; `cmdline` is absent, which is the located basis of the
  disclosed cmdline bound.
- Footline, HTML line 1713: `Linux man-pages 6.19            2026-06-05                      ptrace(2)`.

### 2.4 Placement (ownership, not mine to decide)

`corpus/SOURCES.md` is append-only and S279's protected cells cannot be edited in place
(`verifiers/check_sources_append_only.py`, SOURCES contract rule 2). The completed quote therefore
belongs in the **round-99 lesson's correction note** (which the plan already routes: *"the round-99
lesson records the conjunct as a correction note"*), and — if a registry row is wanted — as a **new
superseding row** whose `teaches` opens `supersedes S279 —`, not as an edit of S279. `ScribeCorpusR99`
owns `corpus/lessons/round-99.md`; `ExecRedsR99` owns `corpus/SOURCES.md` rows only for the
coverage-map row and the baseline. I report the facts; I do not route a file change.

---

## 3. One candidate for C2's honest route — `git-hash-object(1)`

**URL:** https://git-scm.com/docs/git-hash-object — access 2026-11-06 13:55Z, **HTTP 200**,
**29 933 B**, sha256 **`b7e8f95355c38df94c9355d31b0ed985d5c22cb5ca7c4d640364c801100eb798`**
(identical on three fetches; the page is stable, unlike `/3/`).
**Registry check:** `grep -c "hash-object" corpus/SOURCES.md` = **0** — the URL is not held.

**Located quotes** (markup removed, whitespace folded):

- DESCRIPTION, HTML lines **1607–1611** (`wc -w` = 53):
  > Computes the object ID value for an object with specified type with the contents of the named file (which can be outside of the work tree), and optionally writes the resulting object into the object database. Reports its object ID to its standard output. When <type> is not specified, it defaults to "blob".
- `-t <type>`, HTML lines **1620–1623** (`wc -w` = 20):
  > -t <type> Specify the type of object to be created (default: "blob"). Possible values are commit, tree, blob, and tag.
- `--path`, HTML lines **1638–1647** (`wc -w` = 89):
  > --path Hash object as if it were located at the given path. The location of the file does not directly influence the hash value, but the path is used to determine which Git filters should be applied to the object before it can be placed in the object database. As a result of applying filters, the actual blob put into the object database may differ from the given file.
- version pin, HTML line 1318: `git-hash-object last updated in 2.43.0`.

### 3.1 Verdict: **ADMIT as a general registry row (tier A, kind `docs`）；REJECT as the authority for C2's INSTRUMENT_PINS admission**

**Reasoning.** The C2 counter's frozen conjunct (3) requires `verifiers/check_tip_battery.py` to be
byte-identical to the round base outside its `INSTRUMENT_PINS = {...}` block, and the honest route
admits one new blob sha there. But the admission is *not* grounded by `git hash-object`:

- The pin is **read out of a committed tree**, not computed:
  `verifiers/check_tip_battery.py:344` — `got = git(clone, "rev-parse", "%s:%s" % (rev, path))`,
  `blob = got.stdout.strip()`, then `if blob not in allowed`. The value is whatever the tree says the
  path's blob is. That mechanism's authority is **S267** (`gitrevisions(7)`, `<rev>:<path>`, already
  in the registry, mined 2026-11-05) and **S268** (`git-cat-file(1) -e`, the existence check).
- `git hash-object` is used in this lane only in **self-test fixtures**, to fabricate a gitlink blob:
  `verifiers/check_command_files.py:1110`, `verifiers/check_hook_files.py:1285`,
  `verifiers/check_plugin_manifests.py:1072` — all `hash-object -w --stdin`. None of these is on
  C2's path.
- So the fact `git-hash-object` actually grounds — *an object ID is computed from a file's contents
  with a stated type, defaulting to `"blob"`* — is the fact that makes a **hand-copied** pin sha
  meaningful (it names exactly those bytes, with the type fixed), and it is the fact the `--path`
  text then qualifies (filters can make the stored blob differ from the given file — i.e. a pin
  computed from a *working-tree* file need not equal the blob the tree records). That is a real,
  distinct scope from S267/S268, and no row currently holds it.

**Flip condition.** Admit the row for C2's route **only if** the landed candidate actually
computes a pin value rather than reading it from the tree — e.g. if `INSTRUMENT_PINS` is populated
by running `git hash-object` over a working copy. If the candidate's pin values come from
`git rev-parse <rev>:<path>` (as the current battery does), the row is **not** a dependency of C2
and should be filed as `mined` with `used-by` naming the general knowledge it supports, not the C2
claim. If the candidate hashes a **working-tree** file, the `--path` filter caveat becomes load-bearing
and must be carried in the row's `teaches` cell.

**Also worth flagging to the L1 (data-level, not code):** the corpus gates do **not** read
`corpus/SOURCES.md` — `grep -n SOURCES verifiers/verify_corpus_integrity.py` → 0 hits, same for
`verify_corpus_independent.py` (only `verifiers/check_sources_append_only.py` reads it). So a
mis-recorded S281 digest does not turn a C2 gate red directly; it degrades the *recheck* a future
reader can perform. That is exactly why the pinned-URL recommendation in §1.4 matters even though
no gate enforces it.

---

## 4. Findings, in the lane's own vocabulary

| # | class | finding |
|---|---|---|
| **F1** | `rolling-source-digest` | The L1's S281 digest `bcd717f2…` is **not re-fetchable**: `docs.python.org/3/library/argparse.html` is a rolling build whose 5-byte `Last updated on … (HH:MM UTC)` footer changes on each upstream rebuild. Proven byte-exact (only that field differs). Same mechanism breaks **S270** and **S276** by the footer field alone, and **S253** by content + footer. **Fix for S281: cite the version-pinned `/release/3.15.2/` URL** (digest stable over five fetches) or disclose the rolling build in the anchor cell. **Fix for S253/S270/S276: a new superseding row, never an in-place edit** (`SOURCES.md` is append-only). |
| **F2** | `quote-truncation` | The S279 row's located quote stops mid-rule, before the `CAP_SYS_PTRACE` conjunct of access-check step (4) (HTML lines 1516–1520). The row's `teaches` already states the conditional correctly; the **quote** is what is short. The ≤25-word conjunct quote is in §2.2. The completion belongs in the round-99 lesson's correction note (and/or a `supersedes S279 —` row), not in an edit of S279. |
| **F3** | `wrong-authority` | `git-hash-object` is **not** what the `INSTRUMENT_PINS` admission relies on (the pin is read from a committed tree via `git rev-parse <rev>:<path>`, `check_tip_battery.py:344`; `hash-object` appears only in three self-test fixtures). The doc grounds a *different* fact — object-ID-from-contents with type defaulting to `"blob"`, plus the `--path` filter caveat — which is real and unheld by any row. **Admit as a general row; admit for C2 only if the candidate computes a pin rather than reading it** (flip condition in §3.1). |
| **F4** | `anchor-ambiguity` | The marker `'append'` occurs **twice** on the argparse page (HTML lines 992 and 1065). Any counter or recheck matching the quote must match the **sentence** (22 words), not the bare token — QUALITY **Q32**. |
| **F5** | `scope-drift` (checked, **no defect**) | The registry holds **no** row on the argparse URL (`grep -rn "library/argparse.html" corpus/` → 0 hits); the single "argparse" hit is **S211**, a `kind=code` row on a GitHub URL about a different document. S281 is therefore a first row on a new URL and adds **no** E04/W04 duplicate-URL finding. Row count moves 206 → 207; W04 stays 34. |
| **F6** | `gate-scope` (checked, **no defect**) | The three C2 corpus gates do not read `corpus/SOURCES.md`, so F1 cannot turn a C2 gate red directly; it degrades recheckability only. Stated so the L1 does not over-weight it. |

---

## 5. Risks and unknowns

- **Not a counter defect.** No predicate, anchor or counted byte of
  `verifiers/fixtures/round-99/selftest-kills.py` or `carried-reds.py` was touched or found wanting;
  both were read only (headers plus the `CLAIMS["c1"]` anchor block). **No FINDING against a
  counter is claimed.**
- **The argparse digest has a second, unresolved dimension.** I proved the *difference* between the
  L1's bytes and today's is the footer minute — but I could **not** re-fetch the L1's exact bytes,
  so I cannot say *when* `/3/` will next rebuild. Any row citing `/3/` will drift again. The
  `/release/3.15.2/` snapshot was stable over five fetches but I did not observe it across a
  release boundary.
- **Line numbers are build-specific.** The quote sits at HTML 992–993 on `/3/`, 989–990 on
  `/release/3.15.2/`, and 983 on `/3.14/`. A row must name the URL it anchored on together with the
  line numbers, or the anchor is unverifiable.
- **The ptrace quote is markup-shaped.** The step-(4) text spans five HTML lines and carries
  `<b>` markup around `SUID_DUMP_USER`, `PR_SET_DUMPABLE` and `CAP_SYS_PTRACE`; the conjunct quote
  above is therefore **quote-equal after documented shaping** (markup removed, whitespace
  folded), not byte-exact — QUALITY **Q56** requires that wording, and **Q42/Q53** require the
  shaping note to name the removed bytes. This report supplies the byte ranges so the note can.
- **Not opened (and not needed).** I did not open a third-party "append-only correction notice"
  convention (e.g. a changelog-convention page) for C2: the C2 honest route's correction notice is
  an *append to this lane's own LOG.md*, governed by this lane's own append-only rule (SOURCES
  contract rule 2 / QUALITY **Q64**), so an external convention would be a second method for a
  rule the lane already holds. Recorded here as a deliberate non-opening, not an omission.
- **Machine-local.** All digests are host-bound: `curl` from this lane's host on 2026-11-06 UTC.
  The `/3/` figures are time-of-day sensitive by construction (§1.1).

---

## 6. Evidence index (commands run; observed lines quoted)

| command | observed |
|---|---|
| `curl -sS -L -o argparse.html -w '%{http_code}' https://docs.python.org/3/library/argparse.html` (×5, 13:53Z–14:13Z) | `200`, 334 994 B, sha `906919fd…` each time |
| sha of the L1's recorded digest | `bcd717f2…` ≠ `906919fd…`; same length 334 994 |
| footer-only substitution `13:47`→`13:27` | sha becomes **exactly** `bcd717f2…` → `True`; differing range 334740–334745 |
| `curl … https://docs.python.org/release/3.15.2/library/argparse.html` (×5) | `200`, 327 874 B, sha `36e8d536…` every time |
| `grep -c "This appends each argument value to a list" rel-1.html` | `1` |
| `grep -n "class=\"pre\">'append'</span>" argparse.html` | lines **992** and **1065** (two occurrences) |
| quote word count (`wc -w` on the 22-word quote) | `22` |
| `grep -n argparse corpus/SOURCES.md` | line 157 only (S211, GitHub URL) |
| `grep -rn "library/argparse.html" corpus/` | no hits |
| `grep -cE '^\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` | `206`; distinct ids `206`; `grep -c "S281"` → `0` |
| `grep -c W04 .ufo/waves/round-99/receipts/census-before.txt` | `34` |
| `curl … https://man7.org/linux/man-pages/man2/ptrace.2.html` | `200`, 104 833 B, sha `69cd309e…` = S279's recorded digest |
| `awk 'NR>=1516 && NR<=1520' ptrace.2.html` | step (4) full text, lines 1516–1520; conjunct at 1518–1520 |
| `grep -n "CAP_SYS_PTRACE" ptrace.2.html` | 1360, **1513–1514** (step 3, permissive), **1518–1520** (step 4, conjunct) |
| `wc -w` on the conjunct quote | `16` (≤ 25) |
| `curl … https://git-scm.com/docs/git-hash-object` (×3) | `200`, 29 933 B, sha `b7e8f953…` every time |
| `grep -c "hash-object" corpus/SOURCES.md` | `0` |
| `grep -n "hash-object" verifiers/*.py` | `check_command_files.py:1110`, `check_hook_files.py:1285`, `check_plugin_manifests.py:1072` (self-test fixtures) |
| `grep -n "rev-parse" verifiers/check_tip_battery.py` | line **344** (`git(clone, "rev-parse", "%s:%s" % (rev, path))`) — the pin read |
| `grep -n SOURCES verifiers/verify_corpus_integrity.py` / `…_independent.py` | 0 hits each |

---

## 7. Handoff

- **To the L1 (`KotobaR99`):** F1 is the actionable one — S281's digest as recorded will not
  re-verify, and the same defect already sits in S253/S270/S276. **The pinned
  `https://docs.python.org/release/3.15.2/library/argparse.html` URL (327 874 B,
  `36e8d5361b591376bbf9255c08147ece82f5f1fe52a5abd3d149656e902bb8ae`, quote at HTML 989–990,
  22 words) is the version I can vouch for.** I did **not** amend the plan, the counters or any
  frozen predicate; nothing here is an L1 act on its own.
- **To `ScribeCorpusR99`** (owns `corpus/SOURCES.md` row S281 and `corpus/lessons/round-99.md`):
  S281's scope should be argparse's *option semantics* (tier A, `kind=docs`), its anchor must carry
  the 22-word sentence (not the bare `'append'`, which occurs twice), and the round-99 lesson's
  correction note should carry F2's completed step-(4) quote with its shaping note.
- **To `ExecRedsR99`** (owns `verifiers/check_tip_battery.py`'s `INSTRUMENT_PINS` block): F3's flip
  condition is yours to answer — if the pin value is **read** from the tree (the current
  `git rev-parse <rev>:<path>` at line 344), `git-hash-object` is not a dependency of the C2 route.
- **Nothing here requires a counter change.** A counter defect would be a FINDING in an answer, not
  a rescue — and I found none.

---

*Report written by ScoutSourcesR99, r99-w1. Repo writes: none outside
`.ufo/waves/round-99/w1/ScoutSourcesR99/receipts.txt` and this file. Scratch
`/fast/scratch/hyaku/kotoba-r99/ScoutSourcesR99/` deleted before yield.*
