# FalsifySubmissionSweep — fleet-root misroot (round 62, wave 2)

Verdict at 2026-10-23T18:36:34-0300 (`date -u` → `2026-10-23T21:36:34Z`): **no untracked fleet-root file contains `kotoba`, `round-62`, `round 62`, `KotobaR62`, `L1kotoba62`, or `kotoba-r62`.** No round-62 seat report is sitting at the fleet root. Every wave-2 seat report that had landed by that clock is under the lane's `.ufo/waves/round-62/w2/`. This seat is inside the wave, so the check does not cover seats that had not written yet.

No tools installed. No language server: the question is byte content of untracked files, answered with `git` / `grep -a` / `stat`. Nothing outside this report was written by this seat.

## 1. Fleet porcelain (exit 0)

`git -C /home/vgpnk/Projects/shokunin status --porcelain -uall` at 18:36:34-0300, exit 0. Fleet HEAD `3f5ef690beb605b308ee0fde0dda98a6e57f3835` (`2026-10-23T18:15:07-03:00`, phase5 ledger). 12 tracked modifications, 20 untracked paths:

```
 M .ufo/state/chousa.report-baseline
 M .ufo/state/kagi.report-baseline
 M .ufo/state/kaidoku.report-baseline
 M .ufo/state/kake.report-baseline
 M .ufo/state/kama.report-baseline
 M .ufo/state/kengaku.report-baseline
 M .ufo/state/kumitate.report-baseline
 M .ufo/state/mado.report-baseline
 M .ufo/state/mori.report-baseline
 M .ufo/state/tameshi.report-baseline
 M .ufo/state/tsukuroi.report-baseline
 M .ufo/watchdog.log
?? .omp/mcp.json
?? .ufo/reports/round-36/chousa.md
?? .ufo/state/kotoba.report-baseline
?? .ufo/state/kotodama.report-baseline
?? .ufo/state/revenger.report-baseline
?? 0
?? AGENTS.md
?? bm.json
?? live.html
?? live_s228.html
?? nama.html
?? s395.txt
?? scripts/hyaku/__pycache__/append-closure.cpython-314.pyc
?? scripts/hyaku/__pycache__/wave-live.cpython-314.pyc
?? scripts/hyaku/append-closure.py.bak-20261023T040735Z
?? scripts/hyaku/fleet-commit.sh.bak-20261023T040735Z
?? tf_bavelas.html
?? wb2.html
?? write
?? xc.xml
```

`git ls-files --others --exclude-standard` lists the same 20 `??` paths. `.ufo/reports/round-36/chousa.md` was not in the 18:34 porcelain; it appeared at mtime 18:36:27. First line: `# chousa — round 36 (attempt 2)`. Not a kotoba file.

## 2. Grep verdict — untracked content does not name kotoba/round-62

Pattern `kotoba/round-62|round-62|round 62|KotobaR62|L1kotoba62|kotoba-r62`, case-insensitive, `grep -a -c -E` on each untracked path, plus a separate `grep -a -c -i kotoba`. Every file: pattern exit 1, count 0, `kotoba` count 0. That includes the two binary `.pyc` files and the empty `s395.txt`.

| path | bytes | mtime (-0300) | names kotoba/round-62? |
|---|---:|---|---|
| `.omp/mcp.json` | 285 | 2026-10-22 21:45:41 | no |
| `.ufo/reports/round-36/chousa.md` | 15884 | 2026-10-23 18:36:27 | no (chousa r36; see §1) |
| `.ufo/state/kotoba.report-baseline` | 68 | 2026-10-23 18:14:08 | no string match; driver token, §3 |
| `.ufo/state/kotodama.report-baseline` | 68 | 2026-10-23 17:04:11 | no (`64` + empty digest) |
| `.ufo/state/revenger.report-baseline` | 68 | 2026-10-21 14:54:50 | no (`62` + empty digest; revenger, Oct 21) |
| `0` | 31 | 2026-10-23 09:09:03 | no (`NF=13 cells=11 double_quotes=0`) |
| `AGENTS.md` | 5921 | 2026-10-22 15:12:23 | no |
| `bm.json` | 5563 | 2026-10-22 18:28:48 | no (Cloudflare interstitial) |
| `live.html` | 57113 | 2026-10-23 07:02:11 | no |
| `live_s228.html` | 5196 | 2026-10-22 12:45:20 | no (Anubis) |
| `nama.html` | 68855 | 2026-10-22 14:24:25 | no |
| `s395.txt` | 0 | 2026-10-22 19:12:41 | no (empty) |
| `scripts/hyaku/__pycache__/append-closure.cpython-314.pyc` | 10738 | 2026-10-22 05:01:42 | no |
| `scripts/hyaku/__pycache__/wave-live.cpython-314.pyc` | 10708 | 2026-10-22 14:06:56 | no |
| `scripts/hyaku/append-closure.py.bak-20261023T040735Z` | 5757 | 2026-10-19 23:04:54 | no |
| `scripts/hyaku/fleet-commit.sh.bak-20261023T040735Z` | 2857 | 2026-10-19 23:04:54 | no |
| `tf_bavelas.html` | 5583 | 2026-10-22 12:45:19 | no (Cloudflare interstitial) |
| `wb2.html` | 620 | 2026-10-22 20:37:37 | no (Wayback block) |
| `write` | 25 | 2026-10-21 19:52:50 | no (`agent://U100N079H334f935b`) |
| `xc.xml` | 237 | 2026-10-23 08:03:49 | no (Perseus "Too many requests") |

An earlier `xargs grep -a -l -E 'Falsify|L1kotoba62|ScribeEntry62|ExecAbsorb'` over the then-19 untracked paths (before `chousa.md` appeared) returned xargs exit 123, i.e. grep found nothing. `chousa.md` was then covered by the pattern above (exit 1) and by its H1.

## 3. The one adjacent file is the driver baseline, not a seat

`.ufo/state/kotoba.report-baseline` bytes are `62 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\n`. `printf '' | sha256sum` → `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. The string `kotoba` is not in the file; the lane is the filename. `scripts/shokunin-watchdog.sh:31` says the baseline holds `round SHA256` captured before launch; the writer is `scripts/shokunin-watchdog.sh:121-137`. Mtime 18:14:08 is two seconds before `.ufo/watchdog.log:985`: `2026-10-23T18:14:10-03:00 launch kotoba round=62 pgid=4142816 driver=hyaku-inline attempt=2`. The watchdog line is in a **tracked** modification, outside the untracked criterion. Revenger's untracked baseline also starts with token `62`, dated 2026-10-21, filename `revenger`. Neither file is a seat report.

No round-62 seat wrote an untracked fleet-root file that names this round: the grep set is empty, and the only kotoba-named untracked file is that driver baseline.

## 4. Wave-2 seat writes vs `.ufo/waves/round-62/w2`

Lane HEAD moved during the sweep. At 18:34:17 it was `e6da78bbe420722dd18a13182a7c4b64ce02f005`. At 18:34:25 integrator commit `3f911504ce76d9ca186f297d6d4a9cd8ed77508a` (author `kotoba-shokunin`) landed: "wave-2 dispatch (39 falsify seats…) + F1 quote correction + final census receipt + seat-count receipt". `git diff --name-status e6da78b 3f911504` is ten paths, none of them a `Falsify*.md`:

```
A  .ufo/waves/round-62/census-after.txt
M  .ufo/waves/round-62/controls/seat-counts-r62.txt
A  .ufo/waves/round-62/w2-assignments.json
A  .ufo/waves/round-62/w2-dispatch.json
A  .ufo/waves/round-62/w2-spec.json
A  .ufo/waves/round-62/w2/swarm-registry.json
M  LOG.md
M  SCORECARD.md
M  corpus/knowledge/erratum-absorption-round62.md
M  corpus/lessons/round-62.md
```

`w2-dispatch.json` mtime 18:32:32; `w2-spec.json` mtime 18:31:14. Those are the dispatch artifacts, not seat reports.

Seat reports present under `kotoba-shokunin/.ufo/waves/round-62/w2/` at 18:36:35 (lane `status --porcelain -uall`, exit 0):

| file | mtime | bytes |
|---|---|---:|
| `swarm-registry.json` (committed in `3f911504`) | 18:34:05 | 15949 |
| `FalsifyS118.md` | 18:34:08 | 5166 |
| `FalsifyC2RevArg.md` | 18:35:33 | 3812 |
| `FalsifyC2Shortcuts.md` | 18:35:34 | 21366 |
| `FalsifySeatCounts.md` | 18:35:34 | 8658 |
| `FalsifyC2Rerun.md` | 18:35:36 | 4921 |
| `FalsifySourcesRow.md` | 18:35:40 | 6773 |
| `FalsifySOURCESCensus.md` | 18:36:35 | 7690 |

`find` for `Falsify*.md` or `L1kotoba62*` under the fleet root, the lane, `/tmp`, and `/home/vgpnk` (maxdepth 4), excluding `w2/`, printed nothing. Direct absence checks:

- `/home/vgpnk/Projects/shokunin/.ufo/waves/round-62` — ABSENT (`ls` exit 2)
- `…/round-62/falsify-scratch` and `…/round-62/w2` at the fleet root — ABSENT
- `kotoba-shokunin/.ufo/waves/round-62/falsify-scratch` — ABSENT
- `/home/vgpnk/Projects/shokunin/.ufo/reports/round-62/kotoba.md` — ABSENT

`git check-ignore -v --no-index .ufo/waves/round-62/w2/FalsifyX.md` from the fleet root → exit 1 (would show as `??`). The same for `.ufo/waves/round-62/falsify-scratch/note.md` → exit 0, `.gitignore:5:.ufo/waves/*/*-scratch/`. That scratch path does not exist. `kotoba-shokunin/…` is ignored by `.gitignore:1:*-shokunin/`, which is why the lane status was run separately.

Dirty lane paths **outside** `w2` at 18:36:34, and why they are not wave-2 seat writes:

- `ScribeEntry62.md` mtime 18:30:18, `ScribeLessonQ57.md` mtime 18:28:04. Both are before `w2-spec.json` (18:31:14) and before dispatch. `git diff --numstat` vs `3f911504`: `8 6` and `1 1`. Wave-1 scribe text still dirty. Not a `Falsify*` seat.
- `SCORECARD.md` mtime 18:35:43, after commit `3f911504`. `git diff -U0` is one line (369): the report citation changes from `` `.ufo/reports/round-62/kotoba.md` `` to `` `../.ufo/reports/round-62/kotoba.md` (fleet repo, sibling of this lane) ``. A repo grep for `fleet repo, sibling of this lane` hits only `SCORECARD.md`. `fuser` on that file returned no holder. [INFERENCE] integrator continuation of the sentence `3f911504` just edited, not a falsify seat: no `Falsify*.md` contains the phrase, and the seats' observed writes are the `w2` reports above. Not proved by a process id.

`LOG.md`, `corpus/knowledge/erratum-absorption-round62.md`, `corpus/lessons/round-62.md`, `census-after.txt`, and `controls/seat-counts-r62.txt` match `3f911504` (worktree git hash equals `HEAD:`). Their mtimes (18:33:52–18:34:20) are the integrator commit's writes. `census-after.txt` records `date -u` `2026-10-23T21:33:52Z` and `sources-census.sh validate` exit 0. `seat-counts-r62.txt` records the same timestamp and `check_seat_counts.py` exit 1 (`35 of 39`).

Fleet files touched after kotoba attempt-2 launch (17:40:02) outside `*-shokunin/` are driver/sibling surfaces, not seat reports: `MANIFEST.json`, `.ufo/watchdog.log`, other lanes' reports and prompts, the four launch baselines, `.ufo/prompts/kotoba-round-62.md` (18:14:08), `.ufo/waves/hyaku/PHASE5.md` (18:15:07). Tracked `.ufo/reports/round-62/` holds `audio.md`, `game-dev-2d.md`, `kotodama.md` only (`git ls-files`); no `kotoba.md`.

## 5. What this does not close

Seven of 39 falsify reports had reached `w2` by 18:36:35, plus this file after that. A seat that writes later can still misroot. The round-51 lesson's rule (sweep after the last seat write) is not met by an in-wave seat. Ignored `*-scratch/` trees and anything under another `*-shokunin/` repo are invisible to fleet porcelain; the scratch dir checked above is absent, and the kotoba lane was statused on its own. `/tmp` was only searched to maxdepth 4 for `Falsify*.md` names.
