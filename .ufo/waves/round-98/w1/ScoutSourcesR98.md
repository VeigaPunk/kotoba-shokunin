# ScoutSourcesR98 — C2's four sources re-opened and judged

Seat: ScoutSourcesR98. Access date for every fetch below: **2026-11-06**. Fetch command, run in
`/fast/scratch/hyaku/kotoba-r98/ScoutSourcesR98` with `TMPDIR`/`HYAKU_SCRATCH` set to it:

```sh
curl -sS -L -o <id>.html -w '<id> %{url_effective} %{http_code} %{size_download}\n' <url>
sha256sum <id>.html
```

No HTML is stored under `.ufo/waves/round-98/w1`; only the digest and a line excerpt below. Scratch
dir deleted at exit.

## Re-open table (all four match the L1's `receipts/sources-opened.txt`)

| id | URL | HTTP | bytes | sha256 | equals L1 receipt |
|---|---|---|---|---|---|
| S277 | https://docs.python.org/3/library/subprocess.html | 200 | 208648 | `86b575bfa9b6b7808b598dbefa0467e6ea2e3b05677f6d583cafe381438165c5` | **yes** (code, bytes and sha256 identical) |
| S278 | https://git-scm.com/docs/git-archive | 200 | 50116 | `fc4bbcfabdafe9f06b919e439fc8ef79fb573f661a694d0c4849f9f3facf2d66` | **yes** |
| S279 | https://man7.org/linux/man-pages/man5/proc_pid_environ.5.html | 200 | 7747 | `93394d9edb801ad44e342e8e8ab057bea619d995803221edaf008226b2062c46` | **yes** |
| S280 | https://man7.org/linux/man-pages/man2/pr_set_dumpable.2const.html | 200 | 10905 | `8336e5a50cf8c3d4e7f717d44f6ce4c5959397a9c4427f3a1898a0dba1e7220c` | **yes** |

No page differed from the L1's bytes, so no re-location of a quote was needed. Two pages *outside*
the L1 receipt were opened for the extra-candidate slot (digests in § Extra candidate).

## S277 — Python `subprocess` docs, Popen `env`

- Located quote (HTML line 882, second line of the paragraph opened at 881):
  `these are used instead of the default behavior of inheriting the current process’ environment.`
  Word count: `printf '%s\n' "these are used instead of the default behavior of inheriting the current process’ environment." | wc -w` → **14** (L1 said 14 — agrees).
- Section: `<h3>Popen Constructor</h3>` at HTML line 600; the quote's paragraph is at 881–884.
- **Verdict: ADMIT**, bounded teaches: *passing `env=` replaces the inherited environment, so a
  counter can hand its child a minimal environment.* The page states the mechanism only; it does not
  state that isolation requires a minimal environment — that prescription is the lane's (v6 rule 9),
  and the row's `teaches` must not attribute it to Python.
- **Defect 1 (anchor ambiguity):** the same sentence occurs **twice** in the page — line 882 (Popen
  Constructor) and line **311** (inside `subprocess.run` in § Using the subprocess Module, where the
  paragraph continues "It is passed directly to `Popen`"). The L1's anchor "HTML lines 881–883" is the
  *second* occurrence; a re-open that greps the quote lands on 311 first and would read the anchor as
  wrong. The row must say "Popen Constructor occurrence, HTML lines 881–884; the same sentence
  recurs at HTML lines 311–312 (paragraph 310–314) in the `run()` entry and is a different claim
  (run forwards `env` to `Popen`)". `grep -n "these are used instead of the default" S277.html` →
  `311:` and `882:`.
- **Defect 2 (shaping note):** the quoted text is the second clause of a semicolon sentence that
  begins `If <em>env</em> is not None, it must be a mapping that defines the environment variables
  for the new process;`. Q42 requires the note to name exactly which bytes were removed; the L1
  receipt does not. The quote is verbatim from the page — it is a *fragment*, not a standalone
  sentence, and must be labelled so.
- **Defect 3 (Q84 duplicate-URL):** the registry already holds **two** rows on this exact URL —
  `grep -n "docs.python.org/3/library/subprocess.html" corpus/SOURCES.md` → lines 204 (S263) and 206
  (S265) — both scoped to the *timeout* contract, with S265 declared `supersedes S263`. S277's scope
  (Popen `env` parameter) is distinct, so admission is legitimate under Q84's "distinct document or
  scope" clause **only if the Gate entry states the distinct scope and cites S265 as the existing
  row**. A third row on one URL is a curation cost that the Gate must record, not absorb silently.
- **Note (page moved between rounds, length-preserving):** my footer at HTML line 2037 reads
  `Last updated on Nov 06, 2026 (08:38 UTC).` while S263/S265 recorded `Nov 05, 2026 (12:47 UTC)` at
  the same line and the same 208648 B. The rebuild changed only the timestamp, and the two strings
  are the same length. Consequence: the **sha256 is the identity**, not the byte count and not the
  line numbers; a re-open on a later date will see a different sha256 with the same quote line.
- **Flip condition:** reject if the row's `teaches` is written as "isolation requires a minimal
  environment" (a prescription the page does not state), or if the anchor is left ambiguous between
  lines 311 and 882, or if a later fetch moves the quote off 881–884 without the row being re-pinned.

## S278 — git-archive(1), DESCRIPTION

- Located quote (HTML lines 1708–1710, inside `<h2 id="_description">` at 1705):
  `Creates an archive of the specified format containing the tree structure for the named tree, and writes it out to the standard output.`
  Word count: `printf '%s\n' "Creates an archive of the specified format containing the tree structure for the named tree, and writes it out to the standard output." | wc -w` → **23**.
- **Verdict: ADMIT**, bounded teaches: *`git archive` writes an archive of the **tree structure** of
  the named tree to stdout.* That grounds the mechanism v6 rule 8 uses (a per-run copy materialised
  from a tree, not from a working directory). It does **not** state that the archive carries no
  repository metadata — that is the lane's construction from "tree structure … named tree", and the
  row must not quote the page as saying "not a repository".
- **Defect 4 (word count):** the L1 receipt says "quote (22 words)"; `wc -w` on the exact quoted
  string prints **23**. Q13/Q54-class count defect in a receipt that a lesson will cite. Correct to
  23 or drop the count.
- **Anchor facts for the row:** `git-archive last updated in 2.54.0` at HTML line 1328; first heading
  `NAME` at 1686 (quote lies after it, outside any subtitle block — Q70 satisfied); sha256 above.
- **Flip condition:** reject if the row's `teaches` asserts the archive is repository-free as a page
  statement (the page has no such sentence: `grep -n -i "not a repository\|bare repository" S278.html`
  → no match; the only "repository" hits are lines 1815–1817 and 1885, about `--remote`), or if a
  later fetch moves the sentence out of DESCRIPTION.

## S279 — proc_pid_environ(5), permission sentence

- Located quote (HTML lines 90–91):
  `Permission to access this file is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check`
  Word count: `printf '%s\n' "Permission to access this file is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check" | wc -w` → **14**.
- **Verdict: ADMIT, but only for the half it states** — *reading `/proc/<pid>/environ` is gated by a
  `PTRACE_MODE_READ_FSCREDS` access-mode check.* It does **not** state that a non-dumpable process
  makes that check fail: `grep -n -i "dumpable\|EPERM\|EACCES\|errno" S279.html` → **no match**, and
  the whole DESCRIPTION (lines 71–92) carries no denial sentence. The plan's line "grounds v6 rule 9
  non-dumpable counter" over-attributes; the denial lives in ptrace(2) step (4) (§ Extra candidate).
- **Defect 5 (word count):** L1 receipt says "quote (15 words)"; `wc -w` prints **14**.
- **Defect 6 (shaping note, Q42/Q56):** the recorded quote drops the `<b>`/`</b>` tags around
  `PTRACE_MODE_READ_FSCREDS` and drops the trailing `; see ptrace(2)`. The note must name exactly
  those removed bytes and the result must be called *quote-equal after documented shaping*, never
  byte-exact. The fetched line 91 is:
  `              access mode <b>PTRACE_MODE_READ_FSCREDS </b>check; see <a href="../man2/ptrace.2.html">ptrace(2)</a>.`
- **Anchor facts:** footline HTML line 113 `Linux man-pages 6.19            2026-02-08            proc_pid_environ(5)`;
  HTML rendering created 2026-09-09 at line 131. No man7.org row exists yet:
  `grep -c "man7.org" corpus/SOURCES.md` → **0** (first-of-kind for the lane; tier A is still right
  by contract — official kernel-interface documentation for this scope).
- **Flip condition:** reject if the row's `teaches` claims the dumpable denial (that sentence is not
  on this page), or if the shaping note is left implicit.

## S280 — PR_SET_DUMPABLE(2const)

- Located quote (HTML lines 109–110):
  `Processes that are not dumpable can not be attached via ptrace(2) PTRACE_ATTACH`
  Word count: `printf '%s\n' "Processes that are not dumpable can not be attached via ptrace(2) PTRACE_ATTACH" | wc -w` → **12**.
- **Verdict: REJECT — agree with the L1, but the stated reason must be corrected.** The receipt's
  reason is "speaks of PTRACE_ATTACH, not /proc/<pid>/environ reads; S279 carries the rule the
  counter relies on". The first clause is an observed fact; the second is **false as written** —
  S279 carries the check's *name and target file*, not the denial. The correct reason: this page
  grounds (a) the dumpable attribute's effect on `PTRACE_ATTACH` and (b) `/proc/<pid>` file
  *ownership* (`If a process is not dumpable, the ownership of files in the process's /proc/pid
  directory is affected`, lines 112–114) — neither is the read denial v6 rule 9 relies on. The
  denial is ptrace(2) step (4). Q62: a refusal whose reason is false teaches the gate the wrong
  lesson; the reason is corrected here rather than rewritten in the frozen plan.
- **Flip condition:** a round that relies on `PTRACE_ATTACH` refusal, or on the dumpable attribute's
  `/proc/<pid>` ownership effect, admits this page. Footline anchor: HTML line 160
  `Linux man-pages 6.19            2026-02-08        PR_SET_DUMPABLE(2const)`.

## Extra candidate — ptrace(2) (the missing denial authority)

Opened 2026-11-06: https://man7.org/linux/man-pages/man2/ptrace.2.html — HTTP **200**, **104833** B,
sha256 `69cd309ece177d54086771701b2085e31cabd14a92484647392bcda468f7bd35`. Not in the L1 receipt.

- Quote A (HTML lines 1423–1424, `PTRACE_MODE_READ` entry opened at 1421):
  `reading /proc/pid/auxv, /proc/pid/environ, or /proc/pid/stat`
  Word count: `printf '%s\n' "reading /proc/pid/auxv, /proc/pid/environ, or /proc/pid/stat" | wc -w` → **5**.
  (A clause of the `PTRACE_MODE_READ` entry, not a standalone sentence; markup removed: the
  `<i>`/`</i>` around `/proc/`, `pid`, `auxv`, `environ`, `stat`.)
- Quote B (HTML lines 1516–1520, algorithm step (4)):
  `Deny access if the target process "dumpable" attribute has a value other than 1`
  Word count: `printf '%s\n' "Deny access if the target process \"dumpable\" attribute has a value other than 1" | wc -w` → **14**.
  (The source line continues `(<b>SUID_DUMP_USER</b>; see the discussion of <b>PR_SET_DUMPABLE</b> in prctl(2)), and the caller does not have the <b>CAP_SYS_PTRACE</b> capability...` — the quote stops before the parenthetical; the shaping note must say so.)
- **Verdict: ADMIT** — tier A, scope *the ptrace access-mode check that governs `/proc/<pid>/environ`
  reads and its dumpable denial*. This is the authority the plan's rule 9 is missing: quote A puts
  `environ` inside `PTRACE_MODE_READ`, quote B states the denial when dumpable ≠ 1. Together with
  S279 (which names the file's check) they carry both halves of v6 rule 9.
- **It also grounds the disclosed bound's direction:** the `PTRACE_MODE_READ` list names
  `auxv`, `environ`, `stat` and `readlink` of `ns/*`, and **not** `cmdline` —
  `grep -n "cmdline" S282cand.html` → no match. So "`/proc/<ppid>/cmdline` names the counter path,
  REV and REPO and is not refused by an access-mode check" has a located basis, which the plan
  currently states as a bare bound.
- **Landing caveat:** the frozen plan's frontier step names rows S277–S279 only. Landing this as a
  fourth row is a plan deviation unless the L1 issues `plans/round-98-addendum-*.md` before the
  scored reading; otherwise the round-98 lesson `## Gate` records it as **judged-ADMIT, deferred**
  with this digest, and the next round writes the row. Do not let the scribe add S281 silently.
- Footline anchor: HTML line 1713 `Linux man-pages 6.19            2026-06-05                      ptrace(2)`;
  rendering created 2026-09-09 at line 1780.

## Auxiliary — proc_pid_cmdline(5) (lead, not a row)

Opened 2026-11-06: https://man7.org/linux/man-pages/man5/proc_pid_cmdline.5.html — HTTP **200**,
**7918** B, sha256 `1fc6816805fa28c1fe015700e7c40efc21d9bbc032e02c35a447004075a91f15`.
Its DESCRIPTION (lines 71–96) carries **no** access-control sentence (`grep -n -i "permission\|readable\|access\|PTRACE" S281cand.html` → no match) and states
`This read-only file holds the complete command line for the process` (lines 73–74) and
`Think of this file as the command line that the process wants you to see.` (lines 96–97).
**Verdict: lead only, not a row** — it grounds the *content* of the disclosed bound
(`/proc/<ppid>/cmdline` is readable and carries argv), but a disclosed bound is not a claim, and the
absence of an access-control sentence is an observed absence, not a page statement. Keep it in
`## Leads (unopened)`-style prose in the Gate with this digest; admit it only if a round makes a
claim about cmdline readability.

## Findings for the L1 / scribe (ranked)

1. **Rule 9's denial half is unsourced by the plan's three pages.** S279 names the check; no page in
   the receipt states that a non-dumpable process fails it. ptrace(2) step (4) (HTML lines 1516–1520,
   sha256 `69cd309e…`) is that authority. Either land it (addendum) or bound rule 9's source line to
   "the check exists" and name the denial as the lane's construction.
2. **Two word counts in the L1 receipt are wrong:** S278 says 22, `wc -w` gives **23**; S279 says 15,
   `wc -w` gives **14**. S277 (14) agrees.
3. **S277's quote is duplicated in the page** (HTML lines 311 and 882). The anchor must name the
   Popen Constructor occurrence and the shaping note must name the dropped preceding clause.
4. **S280's rejection reason is half false** ("S279 carries the rule the counter relies on"). The
   verdict (reject) stands; the reason is corrected in § S280 above (Q62).
5. **Third row on one URL:** S277 joins S263/S265 on the subprocess URL. Legitimate under Q84's
   distinct-scope clause, but the Gate must say so and cite S265.
6. **The subprocess page moved between rounds with an unchanged byte count** (footer Nov 05 12:47 →
   Nov 06 08:38 at line 2037, both 208648 B). Any future re-open must compare sha256, not size.
7. **No man7.org row exists yet** (`grep -c "man7.org" corpus/SOURCES.md` → 0); S279 and the ptrace(2)
   candidate are first-of-kind, so the Gate should state the tier-A justification once.

## Unresolved

- Whether the scribe lands ptrace(2) as S281 needs an L1 decision (addendum vs deferred Gate entry);
  I do not write `corpus/SOURCES.md`.
- I did not re-open the pages at a second time on 2026-11-06, so a same-day move between my fetch and
  the landing is not excluded; the sha256 in this file is the pin.

## Evidence commands (observed lines)

```
curl … → S277 200 208648 | S278 200 50116 | S279 200 7747 | S280 200 10905 | cmdline 200 7918 | ptrace 200 104833
sha256sum → 86b575bf… / fc4bbcf… / 93394d9e… / 8336e5a5… / 1fc68168… / 69cd309e…
grep -n "these are used instead of the default" S277.html          → 311:, 882:
grep -n "Creates an archive of the specified format" S278.html     → 1708:
grep -n "PTRACE_MODE_READ_FSCREDS" S279.html                       → 91:
grep -n "can not be attached via" S280.html                        → 109:
grep -n "Deny access if the target process" S282cand.html          → 1516:
grep -n "pid<i>/environ" S282cand.html (PTRACE_MODE_READ)    → 1424 (entry 1421, "reading" at 1423)
grep -n -i "dumpable|EPERM|EACCES|errno" S279.html                 → no match
grep -n "cmdline" S282cand.html                                    → no match
grep -c "man7.org" corpus/SOURCES.md                               → 0
grep -n "docs.python.org/3/library/subprocess.html" corpus/SOURCES.md → 204 (S263), 206 (S265)
```
