# N01Sentinel — seat report, kotoba round 77 w1 (hygiene sentinel sweep)

This is the seat report; the identical deliverable copy lives at
`.ufo/waves/round-77/build/N01Sentinel.md`.

Seat: `N01Sentinel`, sentinel, leaf, read-only. Lane:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin` at `6523aced1ee0ebe07dca996213bdc645a6acbd1e`
(r77 freeze; HEAD re-read after the sweep: unchanged). Fleet root:
`/home/vgpnk/Projects/shokunin`.

Scope swept (every file): `.ufo/waves/round-76/build/` (20 files),
`.ufo/waves/round-76/snapshots/` (5), `.ufo/waves/round-77/build/` (79 files before this
report), `.ufo/waves/round-77/w1/` (38 reports + `swarm-registry.json`),
`.ufo/waves/round-77/receipts/` (26), plus the scratch root
`/fast/scratch/hyaku/kotoba-r77/` and the fleet root's git status.

Method: `.ufo/waves/round-77/build/N01Sentinel.sweep.sh` (read-only; no writes, no git/jj
mutation, no rm, no network, no mktemp). It excludes its own files (`N01Sentinel.*`) from the
citation grep so the sweep cannot count its own text; that exclusion is disclosed and is the
only self-exclusion. Canonical run, exit status captured from the script itself:

```sh
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build
bash N01Sentinel.sweep.sh > N01Sentinel.sweep-output.txt 2>&1; echo "exit=$?" >> N01Sentinel.sweep-output.txt
# -> SWEEP FINDING CLASSES NON-EMPTY: 3
# -> exit=1
```

Full transcript: `.ufo/waves/round-77/build/N01Sentinel.sweep-output.txt`.

Tool installs: none. `pacman` was never invoked. Scratch: none created by this seat (no clone,
no temp); nothing had to be removed, and nothing of another seat was moved or deleted.

## 1. Pinned inputs verified (not trusted)

```sh
$ sha256sum verifiers/check_desc_craft.py verifiers/check_r75_routed_repairs.py
cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e  verifiers/check_desc_craft.py
989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63  verifiers/check_r75_routed_repairs.py
$ cd .ufo/waves/round-76/snapshots && sha256sum -c MANIFEST.sha256
optimizing-descriptions.md: OK
evaluating-skills.md: OK
best-practices.md: OK
```

Both counter digests equal the r77 plan pins. `fetch-record.json` (3x HTTP 200) carries the
same three digests as `MANIFEST.sha256`; the r76 build tree is fully tracked
(`git ls-files .ufo/waves/round-76/build | wc -l` = 20, no untracked entries, no symlinks).
The three live re-opens of S213 by independent seats agree with the pin
(`7cc54fbb…bd837`, 13,403 bytes): S01 (curl, 2026-10-27T19:44:56Z) and S02 (urllib) both
HTTP 200 and `cmp`-identical to the committed snapshot; SC01's receipt records the same
digest. The snapshot bytes themselves are confirmed by the `sha256sum -c` above.

## 2. Findings

Severity is this seat's judgement from local evidence; each item names the exact bytes.

### F1 (high) — untracked file written at the FLEET ROOT during the wave

- Path: `/home/vgpnk/Projects/shokunin/o.bin` — 5,867 bytes, mode 644, mtime
  `2026-10-27 16:58:36 -0300`, sha256
  `5d670538e975a622f5380465e444002f71c30e5a392570b4fc6abce6d8d23757`.
- Content: an HTML document, identified by `file` as "HTML document, ASCII text"; it is a
  Cloudflare interstitial ("Just a moment…", `cf_chl`/`_cf_chl_opt`/`challenges.cloudflare.com`),
  i.e. a failed fetch body. No URL of the intended page is present in the bytes.
- Evidence: `git -C /home/vgpnk/Projects/shokunin status --porcelain` lists `?? o.bin`; the
  file is not git-ignored (`git check-ignore -v o.bin` exits 1). It is the only fleet-root
  entry created after the wave started (all other status entries carry pre-wave mtimes; see §3).
- Attribution: **not provable from local evidence.** No wave artifact mentions `o.bin` (the
  only string match is this sweep's own output), no `curl -o o.bin` occurs in any r77 script,
  and the fleet root is the cwd of every lane's seats while several lanes run concurrently
  (kama, kotodama, mori). Reported, not moved, per the assignment.
- Impact: a write outside the lane repo in the fleet root — the exact host-guard failure mode;
  left in place it can be picked up by a fleet-wide `git add -A`.
- Smallest fix: the writer deletes it (or relocates it under its own lane/scratch); seat
  fetches must use an absolute `-o` path inside the seat's scratch or the wave dir, never a
  bare relative filename with cwd = fleet root.

### F2 (medium) — `/tmp` path inside a committed evidence chain (SC01)

- `.ufo/waves/round-77/build/SC01Lesson76.counter-receipts.txt`, lines 115, 117, 119, 120:

```text
cmd: curl -sS -m 25 -o /tmp/sc01-page.md -w 'http=%{http_code} bytes=%{size_download}\n' https://agentskills.io/skill-creation/optimizing-descriptions.md
sha256 7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837  /tmp/sc01-page.md
cmp /tmp/sc01-page.md .ufo/waves/round-76/snapshots/optimizing-descriptions.md -> exit 0 (byte-identical)
grep -c -F "A few sentences to a short paragraph is usually right" /tmp/sc01-page.md -> 1
```

- The seat's report (`w1/SC01Lesson76.md` line 9) points at this receipt as the full record.
  The bytes are still present: `/tmp/sc01-page.md`, 13,403 B, sha256 `7cc54fbb…bd837`, i.e.
  equal to the committed snapshot — so the *fact* remains re-verifiable from committed bytes,
  and the `cmp` line itself anchors the same digest to the snapshot.
- Impact: a receipt cites non-citable `/tmp` bytes as its measured page; the "nothing under
  /tmp is citable evidence" rule is broken even though the content is benign (the same bytes
  are committed).
- Smallest fix: change the receipt to cite the committed snapshot
  `.ufo/waves/round-76/snapshots/optimizing-descriptions.md` (or write the fresh fetch under
  `.ufo/waves/round-77/build/SC01Lesson76.s213-fetch.md` and cite that path), and delete
  `/tmp/sc01-page.md`.

### F3 (medium) — hardcoded `/tmp` fallback in a seat-written script (E10)

- `.ufo/waves/round-77/build/E10GateRepair.refresh_baseline.sh:69`:

```sh
tmp=$(mktemp -d "${TMPDIR:-/tmp}/e10-baseline.XXXXXX") || die "cannot create a temp dir"
trap 'rm -rf -- "$tmp"' EXIT
```

- With `TMPDIR` unset (the wave environment: `echo "${TMPDIR:-<unset>}"` → `<unset>`) this
  creates its working dir under `/tmp`. No `/tmp/e10-baseline.*` remained at any of the six
  sweep observations (16:48–17:00), so the trap does clean up; the defect is the hardcoded
  root itself, which the §7 scratch rule forbids (`mktemp` work belongs under
  `/fast/scratch/hyaku/kotoba-r77/<Seat>`).
- Smallest fix: `WORK=/fast/scratch/hyaku/kotoba-r77/E10GateRepair; mkdir -p "$WORK";
  tmp=$(mktemp -d "$WORK/e10-baseline.XXXXXX")`, or `die` when `TMPDIR` is unset.
- Positive controls found in the same sweep (compliant, listed so the class is not over-read):
  `E01ControlsC1.build_controls.py:14,312` explicitly refuses a `TMPDIR` under `/tmp`;
  `E12BatteryScript.battery.sh:63,152-153` uses
  `SCRATCH_PARENT=/fast/scratch/hyaku/kotoba-r77/E12BatteryScript` with
  `mktemp -d "$SCRATCH_PARENT/run.XXXXXX"`; `round-76/build/check_receipt_revs.sh:261` uses
  `mktemp -d` (TMPDIR-honoring) with a trap.

### F4 (medium, systemic) — lane instruments default to `/tmp`, producing 150–190 MB `/tmp` trees

With `TMPDIR` unset, the wave's own gate runs created lane clones under `/tmp`, each far over
the "/tmp is for files under 50 MB only" limit:

| path (observed, then gone) | size | first seen | created by |
|---|---:|---|---|
| `/tmp/k72-tip-8ibcz673` | 190 M | 16:47 | `check_tip_battery.py` (`verifiers/check_tip_battery.py:363`, `TemporaryDirectory(prefix="k72-tip-")`, no `dir=`) |
| `/tmp/k72-tip-1qfw5ci7` | 190 M | 16:48 | same (a self-test child was still running in it) |
| `/tmp/k76-c2-gates-e5ng671r` | 151 M | 16:49 | `check_r75_routed_repairs.py:135`, `mkdtemp(prefix="k76-c2-gates-", dir=… if self.work_dir else None)` → `/tmp` when `--work` is absent |
| `/tmp/k72-tip-z3j_9o11` | 188 M | 16:58 | E12's `check_tip_battery.py` run (pid 3257519, `--repo /fast/scratch/hyaku/kotoba-r77/E12BatteryScript/run.tCXMlw/fleet/kotoba-shokunin`) |

All four were removed when their processes exited (absent by 16:50 / 17:00 respectively), so
the residue today is pre-wave r76 material, not r77:

```text
188M  /tmp/k72-tip-spumbf__      (2026-10-27 14:42; symlink farm to the deleted kotoba-r76 scratch)
187M  /tmp/k76-b28-c2-mz94vv3_   (14:38)
187M  /tmp/k76-b28-c2-0uaxs7lr   (14:38)
4x 0-byte /tmp/k76-b28-c2-* dirs (14:38)
```

- Impact: every battery run transiently puts ~190 MB in `/tmp`; a SIGKILLed gate (the
  timeout path in E12's script) leaves it behind; `/tmp` is a real filesystem on
  `/dev/nvme1n1p1` (128 G, 5–6 G used), so this is hygiene, not an emergency.
- Smallest fix (no counter edits needed): export
  `TMPDIR=/fast/scratch/hyaku/kotoba-r77/<Seat>/tmp` in every seat shell that runs a gate
  accepting `$TMPDIR`, and pass `--work` where offered (`check_desc_craft.py --work`,
  `check_r75_routed_repairs.py --work`). A later round should plumb `--work`/`TMPDIR` into
  `check_tip_battery.py:363` and `check_desc_craft.py:1257` so a seat cannot forget.

### F5 (low-medium) — finished seat left its 190 MB scratch tree (C02)

- `/fast/scratch/hyaku/kotoba-r77/C02CritPredicate/` — 190 M, dir mtime 16:47, present at
  every sweep from 16:47 to 17:00.
- C02 is finished: `agent://C02CritPredicate` returns its final structured result
  (deliverables, `counterexample`, `smallest_safe_correction`); its report exists at
  `w1/C02CritPredicate.md` (16:47). That report line 24 states
  "No clone/commit was made; scratch was removed on shell exit" — the observed tree
  contradicts the claim.
- All other finished seats' scratch dirs are gone (loop over
  `/fast/scratch/hyaku/kotoba-r77/*/`: the only report-bearing seat with a dir is C02).
- Smallest fix: `rm -rf -- /fast/scratch/hyaku/kotoba-r77/C02CritPredicate`; the report's
  cleanup sentence should be corrected, not left as a false statement.

### F6 (low) — E12 writes transcripts at the shared scratch parent, outside its seat dir

- `/fast/scratch/hyaku/kotoba-r77/E12BatteryScript.stdout.txt` (27,779 B, 16:50),
  `…stdout2.txt` (27,858 B, 16:56), `…stdout3.txt` (25,913 B, 17:00) — three loose files in
  the parent root that all seats share, not under `.../E12BatteryScript/`.
- E12 was still running at sweep close (no `w1/E12BatteryScript.md` at 17:00:55), so this is
  not yet a "left by a finished seat" defect; it is a scratch-scope deviation. If the files
  survive E12's yield they are leftovers.
- Smallest fix: keep them under `.../E12BatteryScript/` and cite the committed
  `.ufo/waves/round-77/build/E12BatteryScript.*.txt` receipts instead.

### F7 (low; hazard) — E09's scratch was a 29-symlink mirror of the live fleet root

- Observed at 16:45 in `/fast/scratch/hyaku/kotoba-r77/E09D2D3Hygiene/`: 29 symlinks into
  `/home/vgpnk/Projects/shokunin/` (`.ufo`, `scripts`, `templates`, `AXES.md`, `CORPUS.md`,
  `PROTOCOL.md`, `MANIFEST.json`, `SCORECARD.md`, and each `*-shokunin` sibling), plus a real
  clone named `kotoba-shokunin` (`.git/objects/info/alternates` →
  `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.git/objects`) and `out/`, `work/`. The seat
  removed the tree by 16:49; its report §"fleet-layout shim" documents the technique.
- No mutation was observed through the links: lane `git status` shows only round-77 untracked
  paths and an empty tracked diff; fleet status entries all predate the wave except F1.
- Impact: any command run with cwd = that scratch root and a lane-relative path follows the
  symlink and writes into the live fleet root — the R76-D1 misroot class by construction.
- Smallest fix: never symlink live repos into scratch; clone the lane and run with `-C`
  / absolute paths inside the clone.

### F8 (info) — `/tmp` leftovers of kotoba-lane bytes, none cited

- `/tmp/SC03-skill.md` 78,647 B and `/tmp/skill.3047691.md` 78,647 B, both sha256
  `7b1263b5ccbe2ba8b6ffd5d0f4c87ffc5ab3292c9ce792aeee96de283a06464a` = the lane's `SKILL.md`
  at HEAD (byte-identical).
- `/tmp/SC03-direct.txt` 4,364 B, `/tmp/SC03-indep-direct.txt` 4,078 B,
  `/tmp/SC03-pipe.txt` 12 B — gate JSON / exit-capture experiments from SC03QualityRows
  (whose `/fast` scratch was correctly removed; its report cites none of them).
- `/tmp/r75base.md` and `/tmp/r75head.md`, 2,175 B each, sha256
  `7f260fd517495ffa680f0088f0e1dd17906fe562fe2158dbffa6807e79d57db6` = `corpus/lessons/round-75.md`
  at HEAD (two copies of the same blob; writer not attributable from local evidence).
- All are under 50 MB (so permitted as transient scratch), but they are uncited, un-removed
  copies of lane data outside the lane; delete them and keep working copies under
  `/fast/scratch/hyaku/kotoba-r77/<Seat>/`.

## 3. Clean classes and exact counts

### Credentials — 0 hits

```sh
$ grep -RInE 'op://[A-Za-z0-9]|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|Authorization: *Bearer [A-Za-z0-9]|xox[baprs]-[A-Za-z0-9-]{10,}|sk-[A-Za-z0-9]{32,}' \
    .ufo/waves/round-76/build .ufo/waves/round-76/snapshots \
    .ufo/waves/round-77/build .ufo/waves/round-77/w1 .ufo/waves/round-77/receipts
$ echo $?
1          # no match
```

No `op://` reference, token, cookie, session URL or private key was found. The only
pattern-shaped strings in the round-77 tree are the dispatch text itself (`w1-spec.json:483`,
`w1-dispatch.json:792`, which name `op://` as a thing to look for) and S05's sentinel row
quoting CORPUS rule 6 ("no credentials, no tokens, no private URLs, no op://") — neither is
credential material. The three snapshots contain the word "token(s)" only as page prose about
LLM token counts.

### `/tmp` mentions — 12 lines, classified

```text
build/E10GateRepair.refresh_baseline.sh:69                      hardcoded root            (F3)
build/E01ControlsC1.build_controls.py:14, :312                  refusal policy            (compliant)
build/SC01Lesson76.counter-receipts.txt:115, :117, :119, :120   evidence-chain citation   (F2)
w1/E01ControlsC1.md:138, :154                                   prose (policy)            (compliant)
w1/E10GateRepair.md:149                                         prose ("nothing in /tmp cited")
w1/SC02Lesson77.md:154                                          prose ("nothing written under /tmp")
round-76/build/B10RepairD2D3.measurements.txt:20                prose ("nothing under /tmp cited")
```

Counts by directory: build 7, w1 4, receipts 0, r76 build 1. No `/tmp` citation in any seat
report (the four citation lines are inside SC01's receipt; the report points at the receipt).

### Scratch trees vs finished seats — 1 leftover

```sh
for d in /fast/scratch/hyaku/kotoba-r77/*/; do s=$(basename "$d"); \
  [ -f .ufo/waves/round-77/w1/$s.md ] && printf 'REPORT+SCRATCH %s %s\n' "$s" "$(du -sh "$d"|cut -f1)"; done
REPORT+SCRATCH C02CritPredicate 190M
```

`/fast/scratch/hyaku/kotoba-r77/` total 3.2 G at 16:48 (17 clones; all carry
`objects/info/alternates` — 16 → the lane's `.git/objects`, 1 → a sibling clone — and each
`git rev-parse --show-toplevel` equals its own path: the host guard held). The 3.2 G is
working-tree size (~190 M per clone), not duplicated object stores.

### Files written outside the lane repo

```text
$ git -C /home/vgpnk/Projects/shokunin status --porcelain
 M .ufo/reports/round-58/chousa.md          mtime 15:04  (pre-wave)
?? .scratch/closure-mado-r50.json           mtime 06:38  (pre-wave)
?? .scratch/source-routing-queue.md         mtime 14:40  (pre-wave)
?? .ufo/waves/round-75/                     mtime 14:07  (pre-wave)
?? o.bin                                    mtime 16:58  (F1, during the wave)
```

Sibling-lane scan (`git -C <each sibling repo> status --porcelain | grep -iE 'kotoba|round-77'`)
returned nothing outside `kotoba-shokunin` itself. `~/.local/bin`: no file modified since
16:35 (`find ~/.local/bin -maxdepth 1 -newermt '2026-10-27 16:35:00'` → empty). Lane repo:
`git rev-parse HEAD` = `6523aced…`, tracked diff empty, and every untracked path is under
`.ufo/waves/round-77/` (build/, receipts/, w1/, `w1-spec.json`, `w1-dispatch.json`,
`w1.ready*`) — i.e. seats wrote only inside their wave directory.

## 4. Limits

- `E12BatteryScript` had not published a report at sweep close (17:00:55; its r76-base battery
  was still in flight). F6 is therefore "pending", not a final leftover; no other seat was
  pending (`w1` held 38 reports of 40 seats; the 40th is this seat).
- `o.bin`, `/tmp/skill.3047691.md`, `/tmp/r75base.md`, `/tmp/r75head.md` cannot be attributed
  to a named seat from local bytes; they are reported as observed. Several lanes run
  concurrently in the same fleet root, which is why fleet-root writes are not attributable
  without a command log.
- The sweep's own three files are excluded from its greps by name (`N01Sentinel.md`,
  `N01Sentinel.sweep.sh`, `N01Sentinel.sweep-output.txt`); this is the only exclusion.
- No verification of claim data was attempted (out of this seat's scope): the counters, their
  base receipts and the no-harm battery belong to the other seats and the L1.

VERDICT: No credential material anywhere in scope (0 hits) and every r77 seat wrote only inside `.ufo/waves/round-77/`, but the wave is not hygiene-clean: a fleet-root `o.bin` write (F1), a `/tmp` path used as evidence in SC01's receipt (F2), a hardcoded `/tmp` fallback in E10's script (F3), gate instruments that put 150–190 MB trees in `/tmp` per run (F4), and one finished seat's 190 MB scratch tree left behind against its own cleanup claim (F5); E12's parent-root transcripts are still open (F6).

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/N01Sentinel.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/N01Sentinel.sweep.sh /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/N01Sentinel.sweep-output.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/N01Sentinel.md
