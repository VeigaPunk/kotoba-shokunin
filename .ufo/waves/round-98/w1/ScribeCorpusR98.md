# ScribeCorpusR98 — round 98, wave r98-w1 (corpus rows S277–S280 and the round-98 lesson scaffold)

Seat: ScribeCorpusR98. Lane: `kotoba-shokunin`. Freeze base for every patch:
`63cd48d9de2c44eb40691ca05d3a41cc2f9a3248`. Scratch clone:
`/fast/scratch/hyaku/kotoba-r98/ScribeCorpusR98/repo` (`git rev-parse --show-toplevel` asserted equal
before any `git add`). No git or jj write was run in the lane or the fleet.

## Behaviour (what this seat did)

1. **`corpus/SOURCES.md` — four rows appended** after S276, before `## Paths`; no existing row edited.
   - **S277** Python `subprocess` § Popen constructor, `env` — `docs`, tier A, `mined`, opened
     2026-11-06, recheck `180d`, used-by `corpus/lessons/round-98.md,plans/round-98.md`.
   - **S278** `git-archive(1)` § DESCRIPTION — same shape, `mined`.
   - **S279** `proc_pid_environ(5)` § DESCRIPTION — same shape, `mined`.
   - **S280** `PR_SET_DUMPABLE(2const)` § DESCRIPTION — same shape but `rejected` (redundant), with a
     corrected reason and a flip condition; used-by `corpus/lessons/round-98.md`.
2. **`corpus/lessons/round-98.md` — new scaffold** (author ScribeCorpusR98, 282 lines) with
   `## Gate` (per-row URL, access date, HTTP, bytes, sha256, HTML line excerpt, ≤25-word located quote
   and word count; the scout cross-check; the deferred `ptrace(2)` candidate; the `cmdline` lead),
   `## Corrections` (C98-1, C98-2, C98-3), `## Mistakes` (one row, class
   `measured-child-reads-counter-state`, evidence round-97 addendum A1/A2 and ExecForgeryV5 F1/F2,
   captured-by Q87, fix v6 rules 8-9 shown able to fail by `c2-v6-as-v5.txt` refused 3 of 5),
   `## Status changes` (none), `## Considerthese` (proposals 1–5 measured and carried), `## Settlement`
   (L1 placeholder).
3. **`corpus/README.md` — one index row** for the new lesson, inserted directly under the round-97
   row so the lessons table stays contiguous.

## Gates (commands and observed lines)

| gate | command | observed |
|---|---|---|
| census before | `scripts/sources-census.sh validate --file <freeze>/corpus/SOURCES.md` | rc 0, 34 `W04`, last line `file ok …/corpus/SOURCES.md` (`.ufo/waves/round-98/w1/ScribeCorpusR98/census-before.txt`) |
| census after | same command on the patched clone | rc 0, 35 `W04`, no `E`-code, last line `file ok …` (`census-after.txt`) |
| the one new W04 | `grep 'S277 duplicate' census-after.txt` | `file	W04	S277 duplicate url docs.python.org/3/library/subprocess.html across scopes` |
| frozen manual census | `grep -cE '^\| *S[0-9]{3,} *\|'`; NF≠13; duplicate ids; enum check; mined used-by existence | rows **202 → 206**; malformed **0**; duplicate ids **0**; enum violations **0**; missing used-by paths **0**; S277–S280 each `NF=13` |
| patch applies | fresh clone at `63cd48d9`, `git apply --check <patch>` | rc 0; applied; census on the patched clone rc 0, 35 `W04` (`census-patched-clone.txt`); clone removed |
| patch scope | `git diff --cached --stat 63cd48d9` | `corpus/README.md 1 +`, `corpus/SOURCES.md 4 +`, `corpus/lessons/round-98.md 282 +`; 287 insertions, 0 deletions |
| source re-open | `curl -sS -L -w '%{http_code} %{size_download}'` + `sha256sum`, six URLs | all six agree with the L1 receipt and the scout (`fetch-digests.txt`) |

## Touched surfaces

- `corpus/SOURCES.md` — 4 appended rows (S277–S280); no other line changed.
- `corpus/lessons/round-98.md` — new file.
- `corpus/README.md` — 1 appended index row.
- Receipts: `.ufo/waves/round-98/w1/ScribeCorpusR98/` — `census-before.txt`, `census-after.txt`,
  `census-patched-clone.txt`, `fetch-digests.txt`, `ScribeCorpusR98.patch`.
- Patch: `.ufo/waves/round-98/w1/ScribeCorpusR98/ScribeCorpusR98.patch`, 36658 B, sha256
  `6eae5cf25c15441ef7b783bb37982ba9a641469f7798159777eb38ca7d014d20`.
- READY: `.ufo/waves/round-98/w1/ScribeCorpusR98_READY`.

## Out of scope (not touched)

No edit to `verifiers/` (counter, runner, self-test, fixtures), `plans/`, `SKILL.md`,
`corpus/QUALITY.md`, `corpus/knowledge/`, `corpus/lessons/round-*-verifier-spotcheck.md`, `scripts/`,
`templates/`, `MANIFEST.json`, `.ufo/state/`, the fleet root, any sibling lane, or `considerthese/`.
No counter or C2 run was made (this seat owns no claim reading). No install or upgrade was made.

## Findings

1. **The "no new W04" instruction is unsatisfiable for the plan's row set (needs an L1 decision).**
   S277's URL is already held twice — S263 and S265 (S265 declares `supersedes S263`) — and a new scope
   on a held URL is exactly what `W04` reports. Measured: 34 → 35, the one new line naming S277.
   I wrote the row as the frozen plan declares it, left S263/S265 byte-untouched, and recorded the
   conflict verbatim in the lesson § Gate. Options for the L1: (a) accept the 35th `W04` and log it
   (precedent: round 94's S269 → 34th `W04`, routed as a defect by the round-94 spot-check);
   (b) fold S277 into S265 by addendum (changes S265's scope or used-by — an L1 act, not a scribe
   act); (c) drop S277 and let the lesson cite S265 with a bound. I did not choose among them.
2. **Two word-count drifts in the frozen receipt** (`receipts/sources-opened.txt`): S278 says 22
   words, the same string measures **23**; S279 says 15, the same string measures **14**. Both are
   within the ≤25-word limit, so nothing is re-admitted; the receipt stays frozen and the rows carry
   the true counts. Recorded as C98-1/C98-2. The scout measured the same two numbers independently.
3. **S280's reject reason was half false as written.** The receipt's second clause, "S279 carries the
   rule the counter relies on", does not hold: S279 names the check and the file, not the denial
   (`grep -n -i "dumpable\|EPERM\|EACCES\|errno"` on the S279 bytes → no match). The verdict
   (reject) stands; the row carries the corrected reason (C98-3).
4. **Rule 9's denial half is unsourced by the plan's three pages.** The authority is `ptrace(2)`
   step (4) — `Deny access if the target process "dumpable" attribute has a value other than 1`
   (HTML lines 1516-1517, sha256 `69cd309e…`) — plus the `PTRACE_MODE_READ` clause naming
   `/proc/pid/environ` (HTML lines 1423-1424). The scout judged it **ADMIT**; the frozen plan names
   S277–S279 only, so I recorded it as **judged-ADMIT, deferred** with its digest and did **not**
   add S281. Landing it needs an L1 addendum before a scored reading.
5. **S277's quote occurs twice in the page** (`grep -n` → `311:` and `882:`). The row's anchor names
   the Popen Constructor occurrence (881-884) and records the recurrence at 311-312 (the `run()`
   entry, a different claim), so a re-open that greps first cannot read the anchor as wrong.
6. **The subprocess page moved between rounds with an unchanged byte count** (footer
   `Nov 05, 2026 (12:47 UTC)` at S263/S265 → `Nov 06, 2026 (08:38 UTC)` today, both 208648 B). The
   sha256 is the identity, not the size or the line numbers; the row says so.
7. **`proc_pid_cmdline(5)` is a lead, not a row** (7918 B, sha256 `1fc68168…`): it grounds the
   *content* of the counter's disclosed `/proc/<ppid>/cmdline` bound and carries no access-control
   sentence. Recorded in the lesson § Gate with its digest.

## Limits

- The lesson is a **scaffold**: the L1 settles `## Settlement` and disposes of findings 1 and 4.
- Whole-page digests are not reproducible across a page rebuild by design; the line excerpts and
  greps in `fetch-digests.txt` are the re-open check (round-97 closure defect 7).
- No second same-day fetch was made for the four rows, so a move between my fetch and the landing is
  excluded only by the sha256 pin.
