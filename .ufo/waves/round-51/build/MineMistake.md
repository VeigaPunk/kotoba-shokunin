# MineMistake — round-51 frontier step: two mined mistakes for § Mistakes (draft text only)

Seat: `KotobaR51.MineMistake` (frontier, build wave, round 51). Lane read-only except this file.
Scope: draft text for `corpus/lessons/round-51.md` § Mistakes. No lane file was edited; no `git`
write command and no mutating `jj` command was run in the lane, the fleet repo or a sibling lane.
No tool was installed or upgraded. No subagent dispatched.

## Result

**Two mistake classes admitted for the round-51 lesson — M33 (D4: a rejection reason written with no
page line behind it) and M34 (D1: a seat the report called cancelled wrote its report after the
report was filed, and the leftover sweep was gated on seat return, not on seat write) — with a new
criterion Q27 proposed for M34 and shown able to fail on the round-50 record.**

Pick: **both.** The two classes have different evidence kinds, so "stronger" does not settle between
them on a single scale, and each carries a different part of the round-51 plan (D4 and D1):

- **M33 is stronger on the contradiction.** The rejected page's own bytes carry the contradicting
  text at three places (lines 11, 289, 805-810), two independent fetches agree byte-for-byte
  (sha256 `64856ff4…`, 35,455 B, HTTP 200), and the closure seat reached the same reading. The
  defect is a false statement on the record, and it is narrow: no claim needed the row.
- **M34 is stronger on the timestamps.** Everything in it is mechanical (file mtimes, commit times,
  tree membership) and reproducible without interpretation. The one soft term is "returned" — a
  seat's return is not a file event — so the load-bearing part is the 10-second gap between the
  filing and the last write.

## Draft text for `corpus/lessons/round-51.md` § Mistakes

Table shape copied from `corpus/lessons/round-50.md:15-18` (`|class|evidence pointer
(command → output)|captured-by|fix|`). Numbering continues after the last M in round-50.md (M32).

| M33 A gate rejection reason characterized a source page's content with no line behind it, and the page contradicted the reason | `corpus/lessons/round-50.md:44-45` reads "the Copilot SDK skills page (provider catalogs, not SKILL.md routing)"; the page, fetched 2026-10-22T14:19:50Z (HTTP 200, 35,455 B, sha256 `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3`, byte-identical to the round-50 closure's fetch) reads at line 11 "A skill is a named directory containing a `SKILL.md` file", at line 289 "**`description`**: A short description of what the skill does." and at lines 805-810 § Skill conflicts: "Use `disabledSkills` to exclude conflicting skills" / "Reorganize skill directories to avoid overlaps" — file-based `SKILL.md` skills, the `description` field and a remedy for overlapping skills, so the reason is false on the page's own bytes | Q23 (a rule attributed to an authority carries a located quote from that authority; violated, and not applied in-lane) and Q14 (the same reason is a negative claim about the page's content with no sweep behind it); caught only by the non-author closure (`corpus/lessons/round-50-verifier-spotcheck.md:189,260-262`) | every Gate reject reason names the located line of the rejected source that decides it, or the sweep command that produced the absence; a reason may not characterize a page without a line. Round 51 appends the correction to the round-50 Gate and writes the page as a source row, because C2 cites it (`plans/round-51.md` D4). |
| M34 A seat recorded as cancelled wrote its report after the round report was filed, and the leftover sweep was gated on seat return, not on seat write | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-50/kotoba.md:96-97` reads "0 died; 2 cancelled by the L1 after an hour without a report (`DescDraft`, `D2D4Wording`; their work was done by the L1)" and line 112 reads "Misroot sweep (run after every seat returned): one round-49 kotoba seat report found in the fleet root, moved into the lane byte-exact and removed (lesson M32); nothing from round-50 seats"; the report was filed at fleet `cc7d642` (2026-10-22T10:52:09-03:00); `.ufo/waves/round-50/build/D2D4Wording.md` (18,592 B, sha256 `bb7679ad…`) was written 10:51:16-03:00 and is committed in the lane tree at the round-51 base (`git ls-tree 43ca0bfb .ufo/waves/round-50/build/D2D4Wording.md` → blob `c26b2465…`), and `.ufo/waves/round-50/build/DescDraft.md` (10,079 B, sha256 `0181a459…`) was written 10:52:19-03:00 — 10 s after the filing and 30 s before the driver completion (`/home/vgpnk/Projects/shokunin/.ufo/watchdog.log:705`, 10:52:49-03:00) — and is still untracked at the round-51 base (`git status --porcelain` → `?? .ufo/waves/round-50/build/DescDraft.md`); M32's own fix cell (`corpus/lessons/round-50.md:18`) gates the sweep on "the last seat returns", which is the gate the round-50 record used | none → Q27 (Q06's denominator was right: 33 declared build seats in `.ufo/waves/round-50/build-spec.json`, and the report's "33" matches it; Q05 in form: M32's fix shipped no arm that could fail on a seat writing after the sweep) | the seat record counts a seat that wrote as written whatever its status, and the leftover sweep runs after the last seat write, over every directory a seat can write to, with its command printed. Round 51 commits `DescDraft.md` byte-exact with a disposition line, corrects the seat accounting in the lesson and the LOG, and runs the sweep after the last seat write (`plans/round-51.md` D1). |

## Proposed criterion Q27 (full row, `corpus/QUALITY.md` table shape)

| id | criterion | applies to | grounded in | supersedes |
|---|---|---|---|---|
| Q27 | A wave's seat record and its completeness sweep are bound to the seats' output, not to a seat's return or cancellation: a seat recorded as returned or cancelled that later writes a file is counted as written, and the leftover sweep runs after the last seat write, over every directory a seat can write to, with its command printed. | round reports, lesson § Gate records, wave-evidence dispositions | M34 A seat recorded as cancelled wrote its report after the report was filed, and the leftover sweep was gated on seat return, not seat write (`corpus/lessons/round-51.md` § Mistakes) | — |

`supersedes` is `—`: Q27 adds a binding no row carries; it does not replace Q06 (the denominator
source) or Q14 (a negative claim's sweep). It is the criterion M32 lacked — M32 named an instrument
(the addendum's misroot sweep), not a rule about when the sweep may run.

### Q27 shown able to fail (applied literally to the round-50 record)

It fails on two lines of the round-50 fleet report, and on neither of the two classes is the failure
a matter of interpretation:

1. `/home/vgpnk/Projects/shokunin/.ufo/reports/round-50/kotoba.md:96-97` — "0 died; 2 cancelled by
   the L1 after an hour without a report (`DescDraft`, `D2D4Wording`; their work was done by the
   L1)". Q27's first clause fails: both seats wrote files. `D2D4Wording.md` was written
   10:51:16-03:00 and is committed in the lane tree at the round-51 base; `DescDraft.md` was written
   10:52:19-03:00, ten seconds after the report was filed at 10:52:09-03:00.
2. `/home/vgpnk/Projects/shokunin/.ufo/reports/round-50/kotoba.md:112` — "Misroot sweep (run after
   every seat returned): one round-49 kotoba seat report found in the fleet root, moved into the
   lane byte-exact and removed (lesson M32); nothing from round-50 seats." Q27's second clause
   fails: the sweep is gated on seat return and was filed before the last seat write, and the lane
   still holds the untracked round-50 seat report at the round-51 base.

Control (the criterion passes on a compliant record): all 38 falsify-wave seat reports are committed
in the lane tree at the round-51 base (`git ls-files .ufo/waves/round-50/falsify/ | grep -c '\.md$'`
→ 38) and the only untracked round-50 file is `DescDraft.md`.

### Q23 on the same record (M33's captured-by, for the integrator's check)

Q23 applied to the round-50 record fails on `corpus/lessons/round-50.md:44-45`: the reject reason
carries no located quote from the page it characterizes, and the page's own lines 11, 289 and 805-810
contradict it. Contrast: the sibling reject reason on `corpus/lessons/round-50.md:43` (the Copilot
concept page) does carry a sweep — `grep -ci description` → 0, HTTP 200, 2,622 B, sha256
`ed1e2944…` — so Q14 was met in form there and missed on the SDK page.

## Evidence (commands and exit codes)

All commands run from the lane checkout; every one is read-only.

| command | output | exit |
|---|---|---|
| `git -C …/kotoba-shokunin log --format='%h %ad %s' --date=iso-strict -12 master` | last round-50 lane commit `2abd290` 10:51:22-03:00; base `43ca0bf` 11:04:58-03:00 | 0 |
| `stat -c '%n %y %s' .ufo/waves/round-50/build/{DescDraft,D2D4Wording}.md` | DescDraft 10:52:19.554935837 -0300 10079; D2D4Wording 10:51:16.487390231 -0300 18592 | 0 |
| `sha256sum` of the same two files | `0181a459…` and `bb7679ad…` | 0 |
| `git show 2abd290 --numstat -- .ufo/waves/round-50/build/D2D4Wording.md` | `26 1` — the "cancelled" seat's report is committed | 0 |
| `git ls-tree 43ca0bfb .ufo/waves/round-50/build/D2D4Wording.md` / `… DescDraft.md` | blob `c26b2465…` / empty (not in the tree) | 0 |
| `git status --porcelain` (lane) | `?? .ufo/waves/round-50/build/DescDraft.md` (plus round-51 artifacts) | 0 |
| `git -C /home/vgpnk/Projects/shokunin log --format='%h %ad %s' -- .ufo/reports/round-50/kotoba.md` | `cc7d642` 2026-10-22T10:52:09-03:00 | 0 |
| `grep -n 'round=50' /home/vgpnk/Projects/shokunin/.ufo/watchdog.log` | line 705: `2026-10-22T10:52:49-03:00 complete kotoba round=50` | 0 |
| `git ls-files .ufo/waves/round-50/falsify/ \| grep -c '\.md$'` | 38 | 0 |
| `python3` walk of `.ufo/waves/round-50/build-spec.json` + `grep -c 'DescDraft'/'D2D4Wording'` | 33 declared seat names; both seats declared (1 each) | 0 |

Web sources (fetched with `curl -sSL`; no browser, no challenge bypass; fetched code not executed):

| URL | accessed (UTC) | HTTP | bytes | sha256 | quotes (line in the fetched bytes) |
|---|---|---|---|---|---|
| `https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills.md` | 2026-10-22T14:19:50Z | 200 | 35,455 | `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3` | line 11 "A skill is a named directory containing a `SKILL.md` file"; line 289 "**`description`**: A short description of what the skill does."; line 805 "### Skill conflicts"; line 809 "Use `disabledSkills` to exclude conflicting skills"; line 810 "Reorganize skill directories to avoid overlaps" |
| `https://docs.github.com/en/copilot/concepts/customizations/agent-skills.md` | 2026-10-22T14:22:40Z | 200 | 2,622 | `ed1e29440ec3aeadef2f461d1dc29910eb4014f0a1b451d8f04e73763605d4a7` | `grep -ci description` → 0 (no quote to take) |

Both fetches are byte-identical to the hashes the round-50 closure recorded
(`corpus/lessons/round-50-verifier-spotcheck.md:188-189`), so M33 rests on reproduced bytes, not on
a summary.

## Calibration notes and out of scope

- **What M33 does not claim.** The round-50 *decision* to not write the row was defensible ("no claim
  needs it", spot-check line 189); M33 is about the stated reason being false, not about the
  decision. Round 51 writes the row because C2 cites it, not as a repair of a lost claim.
- **What M34 does not claim.** The round-50 falsify wave left no untracked report (38 of 38
  committed), and the misroot sweep did find and move the round-49 file (M32's fix worked on the
  fleet-root scope). M34 is about the sweep's gate and the seat status, not about a lost report.
- **Not done here (other owners):** the D1 disposition of `DescDraft.md`, the Q27 row landing in
  `corpus/QUALITY.md`, the round-51 lesson file and the round-50 Gate erratum are the integrator's;
  this seat produced draft text only.
- **Tooling:** no install or update was needed; `curl`, `git`, `python3` and `stat` were already
  present. Nothing was written outside this report file and `/tmp` (fetched page bytes).

Report: .ufo/waves/round-51/build/MineMistake.md
