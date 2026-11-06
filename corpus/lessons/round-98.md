# Round 98 — kotoba (Linux host, omp): lesson

Author: **ScribeCorpusR98** (curation draft, scaffold). A seat review is lane evidence, not the
independent non-author admission judgment; the L1 (KotobaR98) integrates and settles, and
`## Settlement` is its placeholder.

Round: 98, plan `plans/round-98.md` (frozen at `63cd48d9de2c44eb40691ca05d3a41cc2f9a3248`), base
`a33f262fc94e3cf27f3c935b5c53c1336bb94166`, instrument commit
`a060b450a43673ebc54720a5192e99df188e80ce` (the v6 counter `verifiers/fixtures/round-98/selftest-kills.py`
and the C2 runner `verifiers/fixtures/round-98/forgery-controls.py`).
Pre-data receipts (frozen with the plan, before any scored reading):
`.ufo/waves/round-98/receipts/` — `redbefore-c1-base.txt` (`C1 targets killed 0 of 9`,
`C1-PREDICATE-UNMET`), `redbefore-c1-base-rulesv5.txt`, `poscontrol-r97c1-base.txt`,
`poscontrol-r96c1-base.txt`, `poscontrol-r95c1-base.txt` (MET), `c2-before-v5.txt`
(`forgeries refused 3 of 5`), `c2-v6-as-v5.txt` (`forgeries refused 3 of 5`), `c2-v6.txt`,
`sources-opened.txt` (four candidates). Addendum `plans/round-98-addendum-1.md` (L1, before the landing
reading) re-points the rows by document: the Python `subprocess` page is cited by its existing id
**S265** (Q84), so no new row is written on that URL; S277 = git-archive, S278 = proc_pid_environ(5),
S279 = ptrace(2), S280 = PR_SET_DUMPABLE (rejected). The entries below carry that numbering; the
scaffold's first numbering (S277 = subprocess) is recorded under § Mistakes row 2.
Scout: `.ufo/waves/round-98/w1/ScoutSourcesR98.md` (landed 2026-11-06 08:43), whose re-open table
matches the L1 receipt and this seat's own fetch on all four digests; its corrections are folded into
the entries below.

## Gate

Candidates considered, with the decision and the reason. Every access record below is this seat's own
re-fetch on 2026-11-06 (`curl -sS -L -o <file> -w '%{http_code} %{size_download}'` then `sha256sum`),
and each one agrees byte for byte with the L1's `receipts/sources-opened.txt` and with
`ScoutSourcesR98.md`. Each entry carries the fetched HTML line excerpt as well as the whole-page
digest, so a re-open stays verifiable when the digest drifts (round-97 closure defect 7).

- **S265 (existing row, re-opened and cited by id; no new row)** — Python documentation,
  `subprocess` (`https://docs.python.org/3/library/subprocess.html`). The registry holds this URL as
  S263 and S265 (S265 supersedes S263; scope: the `run()` timeout contract). Q84: a URL the registry
  holds is re-opened and cited by its existing id. Re-open record:
  - Access record: 2026-11-06; HTTP 200; 208648 B; sha256
    `86b575bfa9b6b7808b598dbefa0467e6ea2e3b05677f6d583cafe381438165c5` (L1 receipt, this seat's
    fetch and the scout's agree). Footer `Last updated on Nov 06, 2026 (08:38 UTC).` at HTML line
    2037, where S263/S265 recorded `Nov 05, 2026 (12:47 UTC)` at the same line and the same size: the
    rebuild moved only the timestamp, so the sha256 is the identity.
  - HTML line excerpt, **HTML lines 881-884** (§ Popen Constructor, `<section id="popen-constructor">`
    at HTML line 599):
    ```
    <p>If <em>env</em> is not <code class="docutils literal notranslate"><span class="pre">None</span></code>, it must be a mapping that defines the environment
    variables for the new process; these are used instead of the default
    behavior of inheriting the current process’ environment. This mapping can be
    str to str on any platform or bytes to bytes on POSIX platforms much like
    ```
  - Located quote (≤25 words): "these are used instead of the default behavior of inheriting the
    current process’ environment." — **14 words**, HTML lines 882-883; the second clause of the
    sentence opened at line 881, so a fragment. The same sentence recurs at HTML lines 311-312 in the
    `run()` entry (a different claim: run forwards `env` to `Popen`); this citation is the Popen
    Constructor occurrence.
  - Use: grounds the mechanism of **v6 rule 9** (the measured child sees only the mapping the counter
    passes). The page states the mechanism only; a minimal environment is the lane's rule.
  - Why no new row: a third row on one URL would add the 35th `W04`, the defect class round 94's
    spot-check routed (S269). The scaffold's candidate that rowed it read `W04` 34 → 35
    (`ScribeCorpusR98/census-after.txt`); the integrated registry reads 34 (§ Census).
- **S277** — Git, `git-archive(1)` § DESCRIPTION (`https://git-scm.com/docs/git-archive`).
  **Admitted** as tier A, kind `docs`, status `mined`, opened 2026-11-06, recheck `180d`, used-by
  `corpus/lessons/round-98.md,plans/round-98.md`.
  - Access record: 2026-11-06; HTTP 200; 50116 B; sha256
    `fc4bbcfabdafe9f06b919e439fc8ef79fb573f661a694d0c4849f9f3facf2d66`; this seat's fetch, the L1's
    receipt and the scout's fetch agree. The page's own version pin is `git-archive last updated in
    2.54.0` at **HTML line 1328**.
  - HTML line excerpt, **HTML lines 1708-1710**:
    ```
    <p>Creates an archive of the specified format containing the tree
    structure for the named tree, and writes it out to the standard
    output.  If &lt;prefix&gt; is specified it is
    ```
  - Located quote (≤25 words): "Creates an archive of the specified format containing the tree
    structure for the named tree, and writes it out to the standard output." — **23 words**
    (`printf '%s\n' "<quote>" | wc -w` → 23), at **HTML lines 1708-1710**, quote-equal after joining
    the three lines. **The frozen receipt records 22 words; the same string measures 23** — see
    § Corrections C98-1 and scout defect 4. The heading is at **HTML line 1705**
    (`<h2 id="_description"><a class="anchor" href="#_description"></a>DESCRIPTION</h2>`).
  - **What this row adds**: the registry holds no `git-scm.com/docs/git-archive` row
    (`grep -cF 'git-scm.com/docs/git-archive' corpus/SOURCES.md` → 0 before this round), so this is
    a new document and no new `W04`. It grounds **v6 rule 8**: the export is materialised from a
    tree, not from a working directory or a repository.
  - Bound (scout flip condition): the page states a **tree-structure** archive; it makes no
    repository-free statement (`grep -n -i "not a repository\|bare repository"` → no match; the only
    "repository" hits are about `--remote`). The absence of `.git` in the per-run world is the
    lane's construction from "tree structure … named tree", and the counter's own reading is the
    evidence for it.
- **S278** — Linux man-pages, `proc_pid_environ(5)` § DESCRIPTION
  (`https://man7.org/linux/man-pages/man5/proc_pid_environ.5.html`). **Admitted** as tier A, kind
  `docs`, status `mined`, opened 2026-11-06, recheck `180d`, used-by
  `corpus/lessons/round-98.md,plans/round-98.md`.
  - Access record: 2026-11-06; HTTP 200; 7747 B; sha256
    `93394d9edb801ad44e342e8e8ab057bea619d995803221edaf008226b2062c46`; this seat's fetch, the L1's
    receipt and the scout's fetch agree. Footline `Linux man-pages 6.19            2026-02-08
    proc_pid_environ(5)` at **HTML line 113**; the rendering was created 2026-09-09.
  - HTML line excerpt, **HTML lines 90-91**:
    ```
                  Permission to access this file is governed by a ptrace
                  access mode <b>PTRACE_MODE_READ_FSCREDS </b>check; see <a href="../man2/ptrace.2.html">ptrace(2)</a>.
    ```
  - Located quote (≤25 words): "Permission to access this file is governed by a ptrace access mode
    PTRACE_MODE_READ_FSCREDS check" — **14 words** (`printf '%s\n' "<quote>" | wc -w` → 14), at
    **HTML lines 90-91**. Shaping note (scout defect 6): the quote drops the `<b>`/`</b>` tags around
    `PTRACE_MODE_READ_FSCREDS` and drops the trailing `; see ptrace(2)`, so it is quote-equal after
    documented shaping, never byte-exact. **The frozen receipt records 15 words; the same string
    measures 14** — see § Corrections C98-2 and scout defect 5. The heading is at **HTML line 71**
    (`<h2><a id="DESCRIPTION" href="#DESCRIPTION"></a>DESCRIPTION …</h2>`).
  - **What this row adds**: the registry holds no `man7.org` row
    (`grep -cF 'man7.org' corpus/SOURCES.md` → 0 before this round), so no new `W04`; it is
    first-of-kind for the lane, and tier A is right by contract (official kernel-interface
    documentation for this scope).
  - **Bound, and the scout's finding 1:** the page names the check that governs the read; it carries
    **no** dumpable, `EPERM`, `EACCES` or `errno` sentence (`grep -n -i "dumpable\|EPERM\|EACCES\|errno"`
    → no match), so it does **not** state that a non-dumpable process fails the check. Rule 9's
    denial half rests on **S279** (`ptrace(2)` step (4)), admitted by addendum 1.
- **S280 — REJECTED this round** — Linux man-pages, `PR_SET_DUMPABLE(2const)` § DESCRIPTION
  (`https://man7.org/linux/man-pages/man2/pr_set_dumpable.2const.html`). Opened 2026-11-06; HTTP 200;
  10905 B; sha256 `8336e5a50cf8c3d4e7f717d44f6ce4c5959397a9c4427f3a1898a0dba1e7220c`; this seat's
  fetch, the L1's receipt and the scout's fetch agree. Footline `Linux man-pages 6.19
  2026-02-08        PR_SET_DUMPABLE(2const)` at **HTML line 160**.
  - HTML line excerpt, **HTML lines 109-110**:
    ```
           Processes that are not dumpable can not be attached via <a href="../man2/ptrace.2.html">ptrace(2)</a>
           <b>PTRACE_ATTACH</b>; see <a href="../man2/ptrace.2.html">ptrace(2)</a> for further details.
    ```
  - Located quote: "Processes that are not dumpable can not be attached via ptrace(2) PTRACE_ATTACH"
    — **12 words** (`printf '%s\n' "<quote>" | wc -w` → 12), at **HTML lines 109-110**, folded after
    `ptrace(2)` with the bold code span rendered. Heading at **HTML line 81** (anchor id
    `DESCRIPTION`). Secondary locator: **HTML lines 112-114** — `If a process is not dumpable, the
    ownership of files in the process's /proc/pid directory is affected as described in proc_pid(5).`
  - Rejected as **redundant**, and the reason is **corrected** (scout defect 5 / Q62 — the receipt's
  second clause, "S279 carries the rule the counter relies on", is false as written): this page
  grounds (a) the dumpable attribute's effect on `PTRACE_ATTACH` and (b) the ownership of files in
  `/proc/<pid>`, neither of which is the environ-read denial that rule 9 relies on; that denial is
  S279, `ptrace(2)` step (4). Tier A for what the page does state. Flip: a round that relies on
    `PTRACE_ATTACH` refusal or on the dumpable attribute's `/proc/<pid>` ownership effect. The
    rejection stays a registry row under CORPUS v1.

**Scout cross-check (ScoutSourcesR98).** The scout admits the subprocess `env` paragraph, git-archive
and proc_pid_environ (each with a stated bound), rejects PR_SET_DUMPABLE and judges ptrace(2) ADMIT —
no row the L1 admitted is rejected. Its findings are folded in as follows: (1) rule 9's denial half
is unsourced by the plan's three pages → S279 ptrace(2) admitted by addendum 1; (2) the two word
counts → § Corrections C98-1/C98-2; (3) the subprocess sentence recurs → the S265 entry; (4) S280's
half-false reason → the S280 entry; (5) a third row on one URL → cited by id instead (addendum A1);
(6) the subprocess page's timestamp-only move → the S265 entry; (7) the first `man7.org` row → S278.

- **S279** — Linux man-pages, `ptrace(2)` (`https://man7.org/linux/man-pages/man2/ptrace.2.html`).
  **Admitted by addendum 1** as tier A, kind `docs`, status `mined`, opened 2026-11-06, recheck
  `180d`, used-by `corpus/lessons/round-98.md,plans/round-98-addendum-1.md`.
  - Access record: opened by the scout and re-opened by this seat on 2026-11-06 → HTTP 200,
    104833 B, sha256 `69cd309ece177d54086771701b2085e31cabd14a92484647392bcda468f7bd35` (both readings
    agree). Footline `Linux man-pages 6.19 2026-06-05 ptrace(2)` at HTML line 1713.
  - Located quotes: (a) the `PTRACE_MODE_READ` entry at HTML line 1421, clause at HTML lines
    1423-1424 — `reading /proc/pid/auxv, /proc/pid/environ, or /proc/pid/stat` — **5 words**, a clause
    with the `<i>` spans removed; (b) access-check step (4), HTML lines 1516-1520 — `Deny access if the
    target process "dumpable" attribute has a value other than 1` — **14 words**, stopping before the
    parenthetical `(SUID_DUMP_USER; see the discussion of PR_SET_DUMPABLE in prctl(2))`.
  - Use: the denial half of v6 rule 9 (a non-dumpable counter fails a child's `PTRACE_MODE_READ`
    check on its `environ`), and the located basis of the disclosed bound: the `PTRACE_MODE_READ`
    list names `auxv`, `environ`, `stat` and not `cmdline` (`grep -n "cmdline"` → no match), so a
    non-dumpable counter does not hide its argv.

**Lead — `proc_pid_cmdline(5)`, not rowed.** Opened 2026-11-06:
`https://man7.org/linux/man-pages/man5/proc_pid_cmdline.5.html` → HTTP 200, 7918 B, sha256
`1fc6816805fa28c1fe015700e7c40efc21d9bbc032e02c35a447004075a91f15` (this seat's fetch agrees with the
scout's). Its DESCRIPTION (HTML lines 71-96) carries no access-control sentence (`grep -n -i
"permission\|readable\|access\|PTRACE"` → no match) and states `This read-only file holds the
complete command line for the process` (HTML lines 73-74) and `Think of this file as the command line
that the process wants you to see.` (HTML lines 96-97). A lead is not evidence and never a row: it
grounds the *content* of the counter's disclosed `/proc/<ppid>/cmdline` bound, and the absence of an
access-control sentence is an observed absence, not a page statement. Admit it only if a round makes
a claim about cmdline readability.

**Census.** The scaffold's candidate (`ScribeCorpusR98/census-after.txt`, S277 = subprocess) read
exit 0, rows 202 → 206, `W04` 34 → 35. The integrated registry (addendum 1 numbering) reads
`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, rows
202 → 206, `W04` 34 (unchanged; landing receipt `.ufo/waves/round-98/receipts/landing/census.txt`).

## Corrections

Named, append-only correction entries. A frozen receipt is never edited; a correction is a new entry
that points at it.

- **C98-1 — the git-archive word count in the round-98 receipt** (receipt label `S278-candidate`,
  registry row S277 after addendum 1). `.ufo/waves/round-98/receipts/sources-opened.txt` records the
  quote as `quote (22 words): "Creates an archive of the specified format containing the tree
  structure for the named tree, and writes it out to the standard output."`. The same quote string
  measures **23** words (`printf '%s\n' "<quote>" | wc -w` → 23), and the scout measures 23
  independently. The receipt stays frozen as written; registry row S277 carries `(23 words)`. No
  admission changes (23 ≤ 25 words).
- **C98-2 — the proc_pid_environ word count in the round-98 receipt** (receipt label
  `S279-candidate`, registry row S278). The receipt records `quote (15 words): "Permission to access
  this file is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check"`. The same string
  measures **14** words, and the scout measures 14 independently. The receipt stays frozen; registry
  row S278 carries `(14 words)`. No admission changes.
- **C98-3 — the PR_SET_DUMPABLE rejection reason in the receipt** (`S280-candidate`, row S280). The
  receipt records the reject as "speaks of PTRACE_ATTACH, not /proc/<pid>/environ reads;
  S279 carries the rule the counter relies on". The second clause is false as written: the environ
  page (then labelled S279, now S278) carries the check's name and target file, not the denial
  (`grep -n -i "dumpable\|EPERM\|EACCES\|errno"` on its bytes → no match). The receipt is frozen and
  not edited; registry row S280 carries the corrected reason, and the denial's authority is S279
  (`ptrace(2)` step (4)), admitted by addendum 1.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `measured-child-reads-counter-state`: the v5 counter handed the measured child its own history and its own replay seed, so a forged self-test could read the counter's committed reference (`git show HEAD:<instrument>`) or replay the shuffle order and read MET with no behavioural arm | `plans/round-97-addendum-1.md` A1 (g10 committed-reference reads `R96C1-PREDICATE-MET` under v5) and A2 (g11 seeded replay reads MET with `KOTOBA_R97_SEED=deadbeefdeadbeef`), and `.ufo/waves/round-97/w1/ExecForgeryV5.md` F1 (the mirror rule is defeated by a committed-source self-comparison) and F2 (the replay seed is inherited by the measured child) | Q87 (`corpus/QUALITY.md`) — its isolation clause names a fresh clone, TMPDIR and HOME and its decoy clause names the markers, but neither names the child's history or its environment, so the criterion as written could not have caught g10 or g11 | v6 rules 8-9 (`verifiers/fixtures/round-98/selftest-kills.py` header): a git-less `git archive` world copied per run, and a minimal child environment with a non-dumpable counter; shown able to fail by the cause control `.ufo/waves/round-98/receipts/c2-v6-as-v5.txt` — the v6 file with `--rules v5` reads `forgeries refused 3 of 5` (g10 and g11 MET), so the refusal comes from rules 8-9, not from a table, marker or schedule change; criterion Q88 |
| `plan-pre-commits-row-on-held-url` (a repeat of the class Q84 already names): the L1's frozen plan and receipt named a new row "S277-candidate" on `https://docs.python.org/3/library/subprocess.html`, which the registry already held as S263/S265 | `plans/round-98.md` § C2 "Sourced" and § Frontier step (rows "S277–S279 admitted"); `.ufo/waves/round-98/receipts/sources-opened.txt` line 3; `.ufo/waves/round-98/w1/ScribeCorpusR98.md` (the as-planned candidate read census `W04` 34 → 35); `.ufo/waves/round-98/w1/ScoutSourcesR98.md` § S277 defect 3 | Q84 — it held: the scribe and the scout both flagged the duplicate before landing, so the criterion caught the mistake; the miss is the L1's, who wrote the plan without the registry grep Q84 implies | `plans/round-98-addendum-1.md` A1 (cite S265 by id; no row on the held URL), before the landing reading; shown able to fail: the as-planned candidate's census reads `W04` 35 (`ScribeCorpusR98/census-after.txt`), the integrated registry reads 34 (`receipts/landing/census.txt`) |

## Status changes

- **S265 `used-by`:** `corpus/knowledge/timeout-calibration-round91.md,corpus/lessons/round-92.md` →
  `corpus/knowledge/timeout-calibration-round91.md,corpus/lessons/round-92.md,corpus/lessons/round-98.md`
  (L1 at settlement; this lesson cites S265 for v6 rule 9's mechanism, addendum 1 A1). Its `status`
  (`mined`) and `recheck` (`180d`) are unchanged.
- S277, S278 and S279 are new `mined` rows and S280 is a new `rejected` row — all opened 2026-11-06,
  tier A, kind `docs`, recheck `180d` — so they carry no old→new pair.
- S263 is not edited (superseded by S265).

## Considerthese

`considerthese/2026-10-26.md` was re-read (proposals only; nothing implemented by this seat).

- **Assimilation: none.** No proposal is newly implemented this round.
- **Proposal 1** (a byte ceiling and a 200-character max-line check in the floors guard) stays
  carried and is **still unimplemented**: measured at this round's freeze, `SKILL.md` is 600 lines /
  92672 B with **165** lines over 120 characters, **94** over 300, and the longest line **1491**
  characters at line 518 (`wc -l`, `wc -c`, `awk 'length>120'`, `awk 'length>300'` on
  `63cd48d9:SKILL.md`). Not taken this round: the floors guard is a frozen instrument no seat owns
  in this wave, and `SKILL.md` is byte-identical from the round-97 landing to the freeze
  (`git diff --stat 693be9c3 63cd48d9 -- SKILL.md` is empty), so the ratchet is not this round's
  claim.
- **Proposal 2** (move `## Gate registry` out of `SKILL.md`) stays an **L0 question** rather than a
  claim (`corpus/QUALITY.md` Q67: a move that takes a protocol-named home elsewhere is an L0
  question). The section sits at `SKILL.md` line 443 and the file is unchanged at the freeze.
- **Proposal 3** (land the page round 74 rejected and use it on the skill's own description) stays
  carried and is **still unimplemented**: the frontmatter description measures **1021** characters
  with a **151**-character first sentence at the freeze, and `SKILL.md` is at the 600-line box (600
  of 600), so a rewrite has to be paid for by lines saved elsewhere — and this wave gives the
  600-line skill budget to no seat.
- **Proposal 4** (don't close a round before its falsify wave runs) stays **unimplemented as a
  protocol rule**. Wave `r98-w1` carries attack seats (the C2 forgery probe and the reviewer/critic
  seats) beside the builders, which is adjacent practice, not the proposal's "provisional" closure
  rule.
- **Proposal 5** (an evidence budget) stays carried and is **still unimplemented**: measured on this
  lane at the freeze, `.ufo` is **351 MB** of a **584 MB** working tree (`du -sh .ufo .` from the
  lane root). Not this round's claim.

## Settlement

L1 settlement (KotobaR98, after the landing reading; the verdicts are the non-author closure's).

- **Landing revision** `e61629f5d582e5518ccfe023c62d1fd26dd1870d` (receipts
  `.ufo/waves/round-98/receipts/landing/`, runner `.ufo/waves/round-98/landing-run.sh`).
- **C1** (`c1-v6.txt`): `C1 targets killed 9 of 9 (run errors 0); positive killed 1 of 1; honest
  CLEAN; comment decoys held 9 of 9; code decoys held 9 of 9`, `C1-PREDICATE-MET` rc 0; the same
  under `--rules v5` (`c1-rulesv5.txt`). Self-test 105 → 128 assertions. Eight of the nine kills are
  verdict-bearing; t07 is observable-only (`plans/round-98-addendum-2.md` B2, CriticClaimR98 D1).
- **C2** (`c2-v6.txt`): `C2 v6: forgeries refused 4 of 5; honest held 2 of 2; bound g2b MET`,
  `C2-PREDICATE-UNMET` rc 1 — g11 (seeded) read MET at the landing although it read refused at the
  instrument commit and in three seat readings. Honest stop as frozen; mechanism and the shared
  `/dev/shm` marker in addendum 2 B1. The g10 refusal held at landing (0 of 11 killed).
- **Census:** 202 → 206 rows, `W04` 34 → 34 (the as-planned subprocess row was not written;
  addendum 1 A1), exit 0.
- **ptrace(2):** admitted as S279 by addendum 1 A2, not deferred.
- **Lesson for the next round (from B1):** a refusal that rests on the forger's own stateful fallback
  is not a property of the counter; the next counter must refuse g11-class worlds even when their
  `/dev/shm` marker is deleted mid-run, or the claim must name that as a bound before data.
