# F31CheckcurityReadOnlyS — read-only scope sweep of the r77 changed evidence (kotoba round 77, w2)

Sentinel seat, leaf, read-only. Fleet root is my cwd; every lane path below is absolute.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` @ `6523aced1ee0ebe07dca996213bdc645a6acbd1e`
(`round-77: freeze plan, base receipts (counters unchanged from r76 freeze)`).
Round 77 launched `2026-10-27T16:37:22-03:00` (fleet `.ufo/watchdog.log:1777`).
Scratch: `/fast/scratch/hyaku/kotoba-r77/F31Security/Read-OnlyScope/` (removed before yield).
Tool installs: none. `pacman` never invoked. No writes outside the lane's `.ufo/waves/round-77/`.

Twin report (same content, the seat-item path): `.ufo/waves/round-77/w2/F31Security/Read-OnlyScope.md`.
Receipts, all under `.ufo/waves/round-77/receipts/`: `F31Security.base-claims.txt`,
`F31Security.draft-closure.txt`, `F31Security.draft-battery.txt`, `F31Security.mutations.txt`,
`F31Security.scope-lane.txt`, `F31Security.lane-checks.txt`, `F31Security.tip-battery.txt`.
Every exit status I quote is the command's own (`cmd > out 2>&1; echo exit=$?`); no pipeline status.

## Axis statement

This seat moves nothing and claims nothing on depth/consistency/coverage/freshness/adjacency. It
serves **operability** and **calibration** by falsifying the wave's premise and by measuring the
read-only scope of the changed evidence. No score movement is claimed.

## F1 — BLOCKER (honesty): the "landed r77 tip" contains no claim data, so neither claim is landed

The tag "wave 2, dispatched after w1 settled; attack only the landed r77 tip" is false at the tip.

```
$ git show --stat --oneline HEAD
6523ace round-77: freeze plan, base receipts (counters unchanged from r76 freeze)
 plans/round-77.md | 58 +++
 .ufo/waves/round-77/receipts/c1-base-…txt / c2-base-…txt / census-before.txt / selftests-base.txt
 5 files changed, 130 insertions(+)

$ git cat-file -e HEAD:corpus/knowledge/description-craft-round76.md   -> exit 128 (absent)
$ git cat-file -e HEAD:corpus/lessons/round-76.md                      -> exit 128 (absent)
```

Frozen counters, unedited (both byte-identical to the plan pins, hashed from `git show HEAD:` and from
the worktree), re-run on a `git clone --shared` of the lane at that revision:

| claim | command | output | exit |
|---|---|---|---|
| C1 | `python3 -B verifiers/check_desc_craft.py --repo <clone> --rev 6523ace…` | `description craft backed 0 of 6` (a–f all fail: entry and lesson not committed; no Body craft row; S213 used-by absent) | **1** |
| C2 | `python3 -B verifiers/check_r75_routed_repairs.py --repo <clone> --rev 6523ace… --work <fresh>` | `r75 routed repairs closed 0 of 4` (R1–R4 open) | **1** |

Reading: 40 w1 seats produced 40 reports and a build/ draft set; nothing was integrated. The two
claims are **unlanded**, so no w2 seat may report them verified against the lane. This is the honest
state, and it matches the r76 pattern; the defect is the wave framing, not the drafts.

Positive, and the reason the blocker is narrow: the draft set **does** close both claims when
assembled verbatim from `build/` in a scratch clone — `6 of 6` exit 0 and `4 of 4` exit 0 at
`9614316` (`F31Security.draft-closure.txt`, all five patches applied `exit=0`). So the landing is a
single integration commit away, not a research gap.

**Smallest remediation:** the L1 lands the data commit (build drafts + index rows + baseline
refresh), then re-announces the tip; w2's claim checks are re-run against that commit. No axis is
harmed: nothing else changes.

## F2 — HIGH: the tracked misroot is still in the branch tip, and one stray file is the only copy

`plans/round-77.md` Trigger says "**R76-D1** stray `kotoba-shokukin/` path removed". The bytes say
otherwise at `6523ace`:

```
$ git ls-files kotoba-shokukin
kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md          (1201 B)
kotoba-shokukin/.ufo/waves/round-76/w1/A18ScoutSnapshot.md    (3543 B)
$ git cat-file -e HEAD:.ufo/waves/round-75/w1/R75Facet48.md   -> exit 128   (the correct path is ABSENT)
$ git cat-file -e HEAD:.ufo/waves/round-76/w1/A18ScoutSnapshot.md -> present (duplicate, byte-identical)
$ git log --oneline --all -- kotoba-shokukin
6ce2724 round-76: recover fleet-root A18 seat report   (ADDED the typo'd copy)
ac9f295 round-75: preserve recovered misroot seat report (ADDED the typo'd copy)
```

Exploit path (scope class, not a remote exploit): a lane evidence file lives under a directory whose
name is a *typo of the lane root*, one level inside the lane. Two consequences: (i) `git add -A`-style
tooling and future sweeps keep counting a phantom tree; (ii) the r75 seat report `R75Facet48` exists
**only** there, so a blind `rm -rf kotoba-shokukin` — the obvious reading of R76-D1 — destroys a real
seat report. E11 (`w1/E11StrayAndMisroot.md`) reached the same determination independently; I
re-derived it from the tree and confirm it.

**Smallest remediation (one commit, no gate coupling):** copy
`kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` to `.ufo/waves/round-75/w1/R75Facet48.md`
(byte-exact, `cmp`), then delete both `kotoba-shokukin/` paths. **Harm check:** `grep -rn
"kotoba-shokukin" verifiers/` returns nothing and no verifier globs `.ufo/waves/**`, so the deletion
cannot move C1, C2 or any no-harm gate. Side effect: the lesson sentence that calls this recovery
"removed only the fleet-root copy" (`corpus/lessons/round-75.md:12`) becomes true.

## F3 — HIGH: three no-harm battery items are red at the landed tip; two are a round-76 regression

Measured **in the lane** (not in a clone — both gates are location-dependent, see F7):

| battery item | at r76 base `b7f13f4` | at the r77 tip `6523ace` | cause |
|---|---|---|---|
| `verify_skill_checklist.py --json` | `pass 11`, exit 0 | `pass 10 / fail 1`, **exit 1** | `LOG.md:2818` cites the r76 fleet report lane-relative: `.ufo/reports/round-76/kotoba.md` does not resolve from the lane; the file is `../.ufo/reports/round-76/kotoba.md` (8128 B) |
| `check_assertion_floors.py` | green | **exit 1** — `FAIL checklist observed=1863 floor=1863 self_test_failures=1` | the same resolution arm |
| `check_skill_evals_v2.py --rev` | exit 1, `2 of 10` | exit 1, `2 of 10` (identical message) | pre-existing; the r77 SKILL row does **not** move it (measured at the full draft tip too) |

Provenance: `git log -S'.ufo/reports/round-76/kotoba.md' -- LOG.md` → `ec7f853` (round 76's own
honest-stop commit), i.e. round 76 introduced this and no gate caught it at freeze. `E12BatteryScript`'s
base receipt already recorded the same `verify_skill_checklist.py --json 1` and `FAIL checklist …
self_test_failures=1`, so the red is *known* but was never routed as a defect.

**Smallest remediation (one token):** in `LOG.md:2818` change
`.ufo/reports/round-76/kotoba.md` → `../.ufo/reports/round-76/kotoba.md`. Proven in a fleet-shaped
sandbox: the `round-76` item disappears from the failure detail and no other item changes; in the lane
that was the only failing item, so both the checklist and the floors gate go green. Axis harm: none —
it restores a pointer, it does not alter a claim or a number. The evals item stays red and must be
reported as pre-existing, not as this round's work.

## F4 — MEDIUM (operability): the data commit cannot be corpus-green under SC06's index patch

`build/SC06ReadmeCorpus.patch` (the superset of the two README patches; E10 documents that exactly one
may be applied) carries a row for `lessons/round-77.md`. The plan's landing order puts the round-77
lesson **after w2** (`plans/round-77.md` § Landing order step 4), and the only draft is
`build/SC02Lesson77.round-77.md`, a skeleton with **20** `[[SLOT: …]]` markers. Measured on the
data commit:

```
$ python3 -B verifiers/verify_corpus_integrity.py --json     -> exit 1
  missing_paths 1: corpus/README.md:154: lessons/round-77.md
  stale_patterns 1: corpus/README.md:154: lessons/round-77.md
  (plus the equal-id drifts: tracked_files 148/144, report_total 102/99, commit_total 45/43)
```

With the skeleton added the zero-modes close (`unindexed 0 / missing 0 / stale 0`) but the artifact
would be a scaffold, not a lesson — not an acceptable landing. With the full recipe (SC06 + drafts +
skeleton + `E10GateRepair.refresh_baseline.sh` → `exit=0`, `wrote …corpus-baseline.json`) all four
gates go green at `00aff3d`: integrity 0, independent 0, C1 `6 of 6` 0, C2 `4 of 4` 0.

**Smallest remediation:** at the data commit, apply SC06 **minus** the `lessons/round-77.md` row (or
apply E10's two spot-check rows plus the four data-file rows), refresh the baseline, and add the
round-77 row **with** the filled lesson in the post-w2 commit — then refresh the baseline again. Harm:
none; the row indexes a file that will exist, and deferring it keeps both gates green meanwhile.

## F5 — MEDIUM: the plan's Trigger paragraph states four repairs as accomplished that the bytes lack

`plans/round-77.md`: "Routed r76 defects handled: R76-D1 … removed; R76-D2 `corpus/lessons/round-76.md`
written (Gate + Mistakes); … R76-D4 the two corpus gates … repaired and the no-harm battery run at the
final tip". At `6523ace`: the stray is present (F2), the lesson is absent, the two claim counters print
`0 of 6` and `0 of 4`, and the battery is red (F1/F3). Present-perfect claims about unlanded work are the
fabricated-readiness class the closure grades; a reader who trusts the Trigger skips the checks.

**Smallest remediation:** rewrite the paragraph in the round's future/planned aspect (or add a pre-data
addendum that restates it as "to land"), or leave it and correct it in the round lesson. Harm: none.

## F6 — MEDIUM (operability): the C2 base receipt is not verbatim reproducible

`.ufo/waves/round-77/receipts/c2-base-2f675548….txt` records
`cmd: … --work <scratch>` — a literal placeholder, not a path. The revision is named, so the result is
re-derivable, but the recorded command cannot be replayed as written (and `<scratch>` in a receipt is
the same class as the `/tmp` citations N01 flagged). **Smallest remediation:** name the actual work
dir or state "fresh empty dir under the seat's scratch, removed after the run"; re-emit the receipt
with the resolved path at the final run. Harm: none.

## Mutations — the frozen gates are live and fail closed (all on scratch commits of the draft world)

| world | mutation | output | exit |
|---|---|---|---|
| M1 `c0a61f8` | entry absent | `backed 3 of 6` | 1 |
| M2 `14cc07b` | counting Body craft row carries only best-practices (wrong-page) quotes | `backed 4 of 6`, (c) fail: "0 quote fragment(s) located in the optimizing-descriptions snapshot, 2 required" | 1 |
| M3 `073f940` | audit `1022` → `1023` | `backed 5 of 6`, (d) fail: "…[1023] does not equal the recomputed clip render 1022 (stripped variant 1021)" | 1 |
| M4 `293bcd0` | S213 `used-by` renamed | `backed 3 of 6`, (c)/(d)/(e) fail | 1 |
| M5 `7e9d9a5` | R2 receipt transcript tampered by one character (`unindexed 0`→`1`) | `closed 3 of 4`, R2 open: "…does not match the normalized stdout re-run at `ac9f295…`" | 1 |

Two notes for the L1. (i) E06's recorded slack arms (M3a/M3b/M3c = `6 of 6`) are **not reproducible
now**: they are named only by revs in a deleted scratch clone, and my independent M2 (same intent, the
counting row's fragments replaced) fails (c). Do not rely on the slack claim either way without a
re-runnable world. (ii) E01's W0 "honest world" reaches `6 of 6` by design (satisfying fixture); the
plan's sentence "a control that meets the target is a counter defect and stops the round" must name
W0 as the satisfying fixture, else the discipline reads as self-contradictory at closure (addendum
sentence, no gate move).

## Read-only scope verification (what I could prove, and what I could not)

- Lane write scope clean: no tracked modification, `git diff --cached --stat` empty, HEAD unchanged,
  no lock files, read-only areas (`MANIFEST.json`, `templates/`, `scripts/`, `.ufo/state/`,
  `considerthese/`, `.scratch/`) with zero tracked/untracked/ignored change. Reflog shows only the L1's
  `export from jj` entries — no seat checkout/reset. One pre-existing stash (`stash@{0}`, round-48 era).
- Counters are pure readers of `--repo`: index sha256 unchanged and `git status` still clean after a
  C1+C2 run; the only verbs are `show`/`cat-file`/`merge-base`/`ls-tree`/`rev-parse`; every write goes
  to `tempfile`/`--work`. No `eval`/`exec`/`yaml.load`/`shell=True` in either counter.
- Snapshots: `sha256sum -c MANIFEST.sha256` all OK; the three digests match `fetch-record.json`
  (3× HTTP 200, 2026-10-27) and the counter's pinned table (incl. `7cc54fbb…bd837`).
- No secrets in `.ufo/waves/round-77/**` or the snapshots; no token/credential reference in any r77
  script.
- Fleet root: `o.bin` (5867 B, 16:58) is inside this wave's window but **not attributable** — no r77
  artifact mentions it and no `curl -o` appears in any kotoba r77 script (N01 F1 says the same). The
  fleet-root `.ufo/waves/round-75/w1/RevEntryQuality.md` is **kotodama's** artifact with a 14:07 mtime,
  i.e. before the 16:37 launch; E11's `--extra` disclosure is accurate and its required filter
  (`kotoba|round-77`) is clean. I moved nothing (fleet root is outside my write scope).
- Wave arithmetic: w1 40 spec seats / 40 results / 40 reports (0 dead); w2 32 seats.
- Cannot verify from local evidence: the HTTP live re-open of S213 (two w1 seats recorded it; the
  committed snapshot is byte-consistent with the pin and I did not fetch the network). Nothing in my
  report depends on a live fetch.

## What I did not run

`jj-lane.sh`, `jj`, any lane git/jj mutation, any wave integration, the network, `pacman`. The
claim counters were run only with `--repo` pointing at scratch clones or (for the two location-dependent
gates) read-only in the lane.

VERDICT: BLOCKER — no claim data is landed at the r77 tip (C1 `0 of 6` exit 1, C2 `0 of 4` exit 1 at `6523ace`); the draft set does close both (`6 of 6`, `4 of 4` in a scratch clone), so the round's real defects are (1) the wave attacked an unlanded tip, (2) the tracked `kotoba-shokukin/` misroot is still in the tip with `R75Facet48` only there, (3) three battery items are red at the tip — checklist and floors from a one-token lane-relative pointer in `LOG.md:2818` (round-76 regression, proven fix), evals pre-existing — and (4) SC06's `lessons/round-77.md` row makes the data commit corpus-red; all four have minimal, harm-free repairs.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F31CheckcurityReadOnlyS.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F31Security/Read-OnlyScope.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F31Security.base-claims.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F31Security.draft-closure.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F31Security.draft-battery.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F31Security.mutations.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F31Security.scope-lane.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F31Security.lane-checks.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/F31Security.tip-battery.txt
