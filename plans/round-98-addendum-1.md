# Round 98 — addendum 1 (frontier-step source rows; before any landing reading)

Author: KotobaR98 (L1). Written after ScribeCorpusR98 and ScoutSourcesR98 reported and before the
landing revision exists. No predicate, counting command, kill rule, target or frozen mutant of C1 or
C2 changes: this addendum touches only which registry rows the frontier step lands and which rows
C2's "Sourced" line cites.

## A1 — the Python `subprocess` page is cited by its existing id S265, not a new row (Q84)

The freeze named a new row "S277-candidate" on https://docs.python.org/3/library/subprocess.html.
The registry already holds two rows on that URL, S263 and S265 (S265 supersedes S263; both scoped to
the `run()` timeout contract). `corpus/QUALITY.md` Q84: a plan names the source a claim rests on, never
the registry row it will add; a URL the registry holds is re-opened and cited by its existing id. The
scribe's candidate that appended the row as planned read census `W04` 34 → 35 (`S277 duplicate url …
across scopes`, `.ufo/waves/round-98/w1/ScribeCorpusR98.md`). Correction: no new row on that URL; C2's
rule-9 citation is **S265**, re-opened 2026-11-06 (HTTP 200, 208648 B, sha256 `86b575bf…65c5`), with the
Popen-constructor occurrence of the quote located at HTML lines 881–884 (the same sentence recurs in the
`run()` entry at lines 311–312) — recorded in `corpus/lessons/round-98.md` § Gate.

## A2 — ptrace(2) is admitted as the denial authority for the non-dumpable counter

ScoutSourcesR98 § S279 and § Extra candidate: proc_pid_environ(5) states only that an `environ` read
is governed by a ptrace access-mode check; the denial for a non-dumpable target is ptrace(2) access
check step (4) ("Deny access if the target process "dumpable" attribute has a value other than 1",
HTML lines 1516–1520), and its `PTRACE_MODE_READ` list names `environ` but not `cmdline` (the located
basis of the disclosed cmdline bound). It is admitted as a row.

## Resulting rows (append-only, ids continue the registry; re-pointed by document)

| id | document | status |
|---|---|---|
| S277 | git-archive(1) — https://git-scm.com/docs/git-archive (grounds rule 8) | mined |
| S278 | proc_pid_environ(5) — https://man7.org/linux/man-pages/man5/proc_pid_environ.5.html (the check that governs environ reads) | mined |
| S279 | ptrace(2) — https://man7.org/linux/man-pages/man2/ptrace.2.html (step (4) dumpable denial; `PTRACE_MODE_READ` list) | mined |
| S280 | PR_SET_DUMPABLE(2const) — https://man7.org/linux/man-pages/man2/pr_set_dumpable.2const.html | rejected (its located text states PTRACE_ATTACH refusal, not the /proc access check; ptrace(2) carries the denial) |

The freeze's "S278-candidate" (git-archive) is S277 here, "S279-candidate" (environ) is S278, and
"S280-candidate" stays S280; the plan's frontier line "S277–S279 admitted, S280 rejected" holds with
these documents. Quote word counts measured by the scout and recorded as corrections in the lesson:
git-archive 23 words (the freeze receipt says 22), proc_pid_environ 14 words (the receipt says 15).
