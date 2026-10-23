# ScoutMisroot — fleet-root misroot sweep (kotoba round 55, wave 2 FALSIFY)

Result: HOLDS — zero untracked fleet-root files name kotoba round 55 or any KotobaR55 seat; fleet root has no
`.ufo/waves/round-55/` at all, and the round's receipts live only in the lane. Two sweep blind spots and one
namespace collision are recorded below as weaknesses, not defects in lane files.

Role: scout, axes `[calibration]`, read-only on the lane. No lane file edited, nothing moved or deleted.
Access time of every observation: `date -u` → `Fri 23 Oct 2026 12:09:36 AM UTC` (host local `-0300`, `date`
→ `Thu 22 Oct 2026 09:09:57 PM -03`). All commands below are read-only git / ls / grep / find.

## 1. Fleet-root status, verbatim

```
$ git -C /home/vgpnk/Projects/shokunin status --porcelain    # exit 0
 M .ufo/state/chousa.report-baseline        M .ufo/state/kagi.report-baseline
 M .ufo/state/kaidoku.report-baseline       M .ufo/state/kake.report-baseline
 M .ufo/state/kama.report-baseline          M .ufo/state/kengaku.report-baseline
 A .ufo/state/kotoba.report-baseline        A .ufo/state/kotodama.report-baseline
 M .ufo/state/kumitate.report-baseline      M .ufo/state/mado.report-baseline
 M .ufo/state/mori.report-baseline          A .ufo/state/revenger.report-baseline
 M .ufo/state/tameshi.report-baseline       M .ufo/state/tsukuroi.report-baseline
 M .ufo/watchdog.log
 A scripts/hyaku/__pycache__/append-closure.cpython-314.pyc
 A write
?? AGENTS.md
?? bm.json
?? live_s228.html
?? nama.html
?? s395.txt
?? scripts/hyaku/__pycache__/wave-live.cpython-314.pyc
?? tf_bavelas.html
?? wb2.html
```

Code census: `git status --porcelain | awk '{print substr($0,1,2)}' | sort | uniq -c` → `8 ??`, `5  A`, `12  M`.
Canonical untracked set, `git ls-files --others --exclude-standard` (exit 0): `AGENTS.md`, `bm.json`,
`live_s228.html`, `nama.html`, `s395.txt`, `scripts/hyaku/__pycache__/wave-live.cpython-314.pyc`,
`tf_bavelas.html`, `wb2.html`. Eight files, all at the fleet root, none under `.ufo/` —

```
$ git status --porcelain | grep -E '^\?\?' | grep -c '\.ufo/'
0
```

Note `write` and `append-closure.cpython-314.pyc` are `A` (in the index), **not** untracked; they are not part of
the untracked set and are called out separately in §5.

## 2. Untracked files whose content names our round: none

Grepped all eight untracked files for `round.?55|KotobaR55|misroot` (`grep -a -n -i -E`, per file) and for
`round.?55|KotobaR55|kotoba-r55` (`grep -rl -a`, recursive over the whole set): **exit 1, no output, no match**.
Case-insensitive `kotoba` counts, `grep -c -a -i 'kotoba' AGENTS.md bm.json live_s228.html nama.html
tf_bavelas.html wb2.html write` → every file `0`, exit 1. The two `.pyc` files likewise: `grep -a -c -i kotoba`
→ `0` each, and the round/seat pattern → no match.

Item-by-item identification (so the negative is auditable, not a blanket claim):

| path | bytes | mtime (local) | content | names our round? |
|---|---|---|---|---|
| `AGENTS.md` | 5921 | 2026-10-22 15:12:23 | fleet-root orientation doc; `git log -- AGENTS.md` empty and `git ls-files --error-unmatch` → error, so never tracked | no |
| `bm.json` | 5563 | 2026-10-22 18:28:48 | `<title>Just a moment...</title>` = Cloudflare interstitial | no |
| `live_s228.html` | 5196 | 2026-10-22 12:45:20 | Anubis challenge, `"anubis_version"`/`"v1.26.2"`, `/.within.website/x/cmd/anubis/static/...` | no |
| `nama.html` | 68855 | 2026-10-22 14:24:25 | `<title>Page not found - National Archaeological Museum</title>` (a 404 body) | no |
| `s395.txt` | 0 | 2026-10-22 19:12:41 | empty file | no (no content at all) |
| `tf_bavelas.html` | 5583 | 2026-10-22 12:45:19 | `<title>Just a moment...</title>` = Cloudflare interstitial | no |
| `wb2.html` | 620 | 2026-10-22 20:37:37 | Wayback Machine abuse-block text: "flagged it as suspected abusive bot traffic" | no |
| `scripts/hyaku/__pycache__/wave-live.cpython-314.pyc` | 10708 | 2026-10-22 14:06:56 | bytecode of `scripts/hyaku/wave-live.*` | no |

## 3. `.ufo/waves/round-55/` at the fleet root: absent

```
$ ls -la /home/vgpnk/Projects/shokunin/.ufo/waves/round-55/
ls: cannot access '.../.ufo/waves/round-55/': No such file or directory    # exit 2
$ ls .ufo/waves/ | grep -i -E '55|kotoba'
(no output, exit 1)
```

What the fleet root's `.ufo/waves/` does hold, with file counts (`find <d> -type f | wc -l` / `git ls-files <d> |
wc -l`): `round-15` 185/186, `round-16` 6/6, and `round-20`, `round-23`, `round-25`, `round-27`, `round-28` all
**0 files / 0 tracked** — empty directory furniture that git cannot represent. None is round 55 and none was
written by this round.

## 4. Namespace collision at `.ufo/reports/round-55/` (structural hazard, not a misroot)

```
$ ls .ufo/reports/round-55/
kotodama.md        # 10639 B, mtime 2026-10-22 17:43, tracked, clean
$ ls .ufo/reports/round-5[0-6]/   # per-dir filenames
round-50/ round-51/ round-52/ round-53/ round-54/: kotoba.md + kotodama.md
round-55/ round-56/: kotodama.md only
```

`MANIFEST.json:14523` records `"report": ".ufo/reports/round-55/kotodama.md"` for the kotodama lane's round 55
(completed 17:43 local per `MANIFEST.json:14532` notes). Our round's declared target is
`.ufo/reports/round-55/kotoba.md` (dispatch prompt `.ufo/prompts/kotoba-round-55.md:101`, restated at :253) and
that file **does not exist yet** — correct for an in-flight round, and it means no kotoba report has been
misrooted or double-filed. The collision is purely numeric: kotoba and kotodama both call it round 55 tonight;
filenames disambiguate, and rounds 50–54 show the same shared-directory pattern.

The only fleet-root artifacts whose content names round 55 for kotoba are fleet state, not seat output:

- `.ufo/state/kotoba.report-baseline` — staged addition (`A`, size 68), content `55 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
  `printf '' | sha256sum` → the same `e3b0c442…b855`, i.e. a driver receipt for "round 55, report hash = empty".
  Driver file; seats are forbidden to touch `.ufo/state/*`.
- `.ufo/watchdog.log:778` — `2026-10-22T19:58:15-03:00 launch kotoba round=55 pgid=2541774 driver=hyaku-inline attempt=1`.
  Tracked and modified by the driver; `grep -c 'KotobaR55' .ufo/watchdog.log` → `0`, so the log names the round
  but no seat id.
- `.ufo/prompts/kotoba-round-55.md` — tracked dispatch prompt (source of this very item).

## 5. Strays at the fleet root that are not ours

- `write` — 25 bytes, content `agent://U100N079H334f935b` exactly, mtime 2026-10-21 19:52:50, and staged (`A`),
  so not in the untracked set. It is the residue of a tool call whose destination argument was the literal word
  `write`, from a round before ours; the address has no lane or round in it.
- `live_s228.html` looks like a capture of a `SOURCES.md` row S228, but the lane registry has no such row:
  `grep -c 'S228' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md` → `0`. The name is a
  lookalike, not attribution; the file contains no http URL (Anubis serves its own inline scripts), so its host
  cannot be recovered from the capture. [INFERENCE] it came from some lane's source fetch that hit an Anubis
  wall at `issuedAt 2026-10-22T17:45:20+02:00`, not from kotoba round 55.
- `bm.json`, `tf_bavelas.html`, `wb2.html`, `nama.html`, `s395.txt` are the same shape: fetch artifacts of
  access-controlled or missing pages (Cloudflare interstitial, Wayback abuse block, a 404 body, an empty dump).
  `wb2.html` (20:37 local) post-dates our launch at 19:58:15 by 39 minutes, but carries no lane, round, or seat
  marker, so it cannot be attributed to a KotobaR55 seat; content-wise it is a block page, not a quotation source.

Nothing at fleet-root depth ≤ 2 was written during the wave-2 window that opened 21:07 local:
`find . -maxdepth 2 -path ./.git -prune -o -type f -newermt '2026-10-22 21:00' -print` (with nested lane repos
filtered out) → no output, exit 0.

## 6. Two blind spots in the sweep control itself

The dispatch instruction is "run `git -C … status --porcelain` (no pathspec — seat notes have landed as plain
files at the fleet root)" (`.ufo/prompts/kotoba-round-55.md:256-262`). That command cannot see two shapes:

1. **Ignored scratch subtrees.** `.gitignore` line 4 is `.ufo/waves/*/*-scratch/` (commented "per-wave cross-lane
   seat scratch is transient"). Verified read-only against hypothetical paths:
   `git check-ignore -q .ufo/waves/round-55/falsify-scratch/note.md` → **YES (ignored)**; whereas
   `.ufo/waves/round-55/falsify/ScoutMisroot.md`, `.ufo/waves/round-55/KotobaR55.CriticAxes.md`,
   `KotobaR55.CriticAxes.md` and `.ufo/reports/round-55/kotoba.md` → **not ignored**, hence visible as `??`.
   A seat that writes into a fleet-root `…-scratch/` directory leaves no trace in the sweep.
2. **Empty directories.** `round-20`, `round-23`, `round-25`, `round-27`, `round-28` at the fleet root contain
   0 files each and therefore appear nowhere in `status`. A seat that creates only directories produces no
   signal.

Also worth stating because it is easy to over-read: `git status --porcelain` shows *only* untracked (`??`) and
index/tree diffs; it cannot show a misroot written into a nested `*-shokunin/` repo (gitignored at this root) or a
file inside a lane's own tree. Those are out of this sweep's reach by construction, not by oversight of the seat.

## 7. One dispatch path points at a fleet-root round-55 location that does not exist

The wave-2 spec `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-55/falsify-spec.json`
(`wave: kotoba-r55-falsify`, `reportDir: .ufo/waves/round-55/falsify`, 40 items) contains exactly two fleet-root
`.ufo/` paths: `.ufo/l0-questions.md` (legitimate — fleet-root by design, read-only for `ReviewL0Line`) and
`.ufo/waves/round-55/` — the latter only inside the `ScoutMisroot` item's text ("Also list files under
/home/vgpnk/Projects/shokunin/.ufo/waves/round-55/ if any"). That directory has never existed (§3); the sentence
is a deliberate probe, and a seat that read it as "the place to put things" would misroot. It did not: all 40
items carry the lane-relative sentence ("relative to /home/vgpnk/Projects/shokunin/kotoba-shokunin"), checked by
counting items whose blob contains `Report:` but not that clause → **0 of 40 missing**. `build-spec.json` is
cleaner still: its only fleet-root `.ufo/` path is `.ufo/l0-questions.md`, with 16 lane-`.ufo/` paths.

## 8. What this does and does not establish

Established by observation: the fleet root currently contains no untracked file naming kotoba round 55 or a
KotobaR55 seat; no fleet-root `.ufo/waves/round-55/` exists; our report target `.ufo/reports/round-55/kotoba.md`
is unwritten; every untracked file at the root is attributable by content to a blocked fetch, a `.pyc`, or the
never-tracked `AGENTS.md`.

[INFERENCE] the round has not misrooted anything into the fleet root as of 00:09 UTC; residual risk is confined
to (a) the ignored `-scratch` shape in §6.1, and (b) writes into a nested lane repo, which this sweep cannot
observe at all.

Not established: which lane wrote `bm.json`, `live_s228.html`, `nama.html`, `tf_bavelas.html`, `wb2.html`,
`s395.txt`. These predate or straddle our launch and carry no lane/round/seat marker; I left them untouched as
another lane's or a prior round's property.
