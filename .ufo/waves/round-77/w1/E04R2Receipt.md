# E04R2Receipt — C2-R2 no-harm receipt for the r75 final tip (round 77, wave w1)

Seat: `E04R2Receipt` (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(lane HEAD read at `6523aced1ee0ebe07dca996213bdc645a6acbd1e`; working tree clean apart
from untracked `.ufo/waves/round-77/…`).
Scratch: `/fast/scratch/hyaku/kotoba-r77/E04R2Receipt/` (shared clone + `work/`); removed
before this report was yielded.

## Axes named

- **calibration** — the C2-R2 arm is the one arm that can only be closed by re-measuring a
  *historical* revision; this seat produces the measured receipt and proves the arm
  discriminates (controls A–G below).
- **consistency** — R2 is the second of the four r75 routed repairs; at the scratch commit
  the frozen counter moves from `0 of 4` to `1 of 4` with **no R2 finding**.
- **operability** — the deliverable is one file plus one exact LOG.md line; the L1 can land
  both without touching the frozen counter.
- **freshness** — both gates were re-run today (2026-10-27) at the pinned revision in a
  fresh `git clone --shared`; nothing is copied from `.ufo/waves/round-76/`.
- **depth** — untouched by this seat (no sourced claim here).

## What was measured (ground truth)

1. Shared clone of the lane, `user.name`/`user.email` set before any scratch commit,
   `rev-parse --show-toplevel` = the scratch clone dir (checked), then checkout of the r75
   final tip:

```
git clone --shared -q /home/vgpnk/Projects/shokunin/kotoba-shokunin $S/clone
git -C $S/clone config user.name scratch-r77
git -C $S/clone config user.email scratch@example.invalid
git -C $S/clone rev-parse --show-toplevel      # /fast/scratch/hyaku/kotoba-r77/E04R2Receipt/clone
git -C $S/clone checkout -q ac9f29510d3914a6edb97c8dbdb3445cab9141de
git -C $S/clone rev-parse HEAD                 # ac9f29510d3914a6edb97c8dbdb3445cab9141de
```

2. Both corpus gates **at that revision**, each gate's own exit status appended by the shell
   after that gate (no pipeline, no shared status):

```
cd $S/clone
python3 -B verifiers/verify_corpus_integrity.py   --repo $S/clone --json > int.out   2>&1; echo "exit=<own status>"   >> int.out
python3 -B verifiers/verify_corpus_independent.py --repo $S/clone --json > indep.out 2>&1; echo "exit=<own status>"   >> indep.out
```

Result: **both exit 0 (GREEN)**. Integrity: `corpus.index.tracked_files 144 == 144 PASS`,
`unindexed 0`, `stale_patterns 0`, `missing_paths 0`, `report_total 99 == 99`,
`report_dead 0`, `commit_total 43 == 43`, `commit_unresolvable 0`, `commit_nonhash 0`.
Independent: same totals as observed values (`tracked_files 144`, `report_total 99`,
`commit_total 43`, `unindexed 0`, `stale 0`, `missing 0`, `report_dead 0`,
`commit_unresolvable 0`, `commit_nonhash 0`) with `PASS` on every zero/equal check and
`INFO` on the three `observe` checks. Raw bytes:
`E04R2Receipt.gates-at-tip.txt` (sha256 `89fd7a87…b1cb38`).

3. **Revision-specificity control** (same commands at the r77 base
   `2f675548eaad2a037a899d39247c1fd7a88aaf48`): **both gates exit 1 (RED)** —
   `corpus.index.tracked_files observed 146 expected 144 DRIFT`,
   `corpus.index.unindexed observed 2 DRIFT`, `corpus.pointers.report_total 102 vs 99 DRIFT`,
   `corpus.pointers.commit_total 44 vs 43 DRIFT` (integrity), `unindexed 2 DRIFT`
   (independent). Byte-for-byte the r76-D4 defect, still open in the lane tree at this
   moment (D4 is another seat's route; reported, not touched). Raw bytes:
   `E04R2Receipt.gates-at-base-2f675548.txt` (sha256 `9b76a29c…b28338ed`).
   Consequence for R2: the transcript is *not* reproducible from base bytes — the recorded
   stdout differs from base stdout in 196 (integrity) / 198 (independent) characters, and
   base output is red anyway. The "copy green stdout under the r75 label" shortcut is
   therefore measured, not assumed: it fails at two independent points (control B, and the
   base run above).

## The receipt

`E04R2Receipt.noharm-at-tip.txt` (sha256 `bb81f3d0fff0536fdb9f52a6ddb1fc407a24eea8d721ed6f42dc09764193ca7f`,
8521 bytes, 266 lines). Shape:

- line 1: `tip: ac9f29510d3914a6edb97c8dbdb3445cab9141de` (the only 40-hex on that line);
- a 4-line `#` header stating that `<repo>` is the sandbox clone root, canonicalized
  exactly as `gates_at()` does (`proc.stdout.replace(str(clone), "<repo>")`);
- `$ python3 -B verifiers/verify_corpus_integrity.py --repo <repo> --json`, then the
  gate's stdout verbatim (canonicalized, no trailing whitespace), then `exit=0`;
- `$ python3 -B verifiers/verify_corpus_independent.py --repo <repo> --json`, then the
  gate's stdout verbatim, then `exit=0`.

Why `<repo>`: `Repo.gates_at` re-runs the gates in its own ephemeral `--shared` clone and
canonicalizes only that clone root, then requires `rerun_out.strip() in recorded_block`.
Recording a literal scratch path would fail the match. The integrity gate emits no path;
the independent gate emits `"repo": "<repo>"`. The file contains no `DRIFT` token and no
literal `$?` (both are R2 failure conditions).

## Counter confirmation (the arm turns closed)

Scratch commit holding the receipt at the **counter's** path plus one LOG line
(`a26c0da45718b1f8e2328784e8169194e99bf26d`, tree = r77 base + those two files):

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
python3 -B verifiers/check_r75_routed_repairs.py --repo $S/clone \
      --rev a26c0da45718b1f8e2328784e8169194e99bf26d --work $S/work
```

Output (exit 1, only because R1/R3/R4 do not exist in that scratch tree):

```
measured-rev: a26c0da45718b1f8e2328784e8169194e99bf26d
R1: open
R2: closed
R3: open
R4: open
r75 routed repairs closed 1 of 4
  - R1: corpus/lessons/round-75.md carries no appended correction
  - R1: .ufo/waves/round-76/receipts/r1-folded-render.txt is not committed at the measured revision
  - R3: .ufo/waves/round-76/w2-registry-note.md is not committed at the measured revision
  - R3: LOG.md § Round 75 does not cite .ufo/waves/round-76/w2-registry-note.md
  - R4: LOG.md § Round 75 records no `63 of 64` report-file/seat pair after the `w2 falsify results pending` text
  - R4: LOG.md § Round 75 records no `0 dead` seat count after the `w2 falsify results pending` text
  - R4: LOG.md § Round 75 records no R75Attack28 settlement after the `w2 falsify results pending` text
```

**Zero R2 findings**; the R2 row reads `closed`.

Second, integration-shaped confirmation — the **delivered blob copied verbatim** onto the
real lane HEAD tree (`6523aced`), plus the LOG line, committed in a second shared clone
(`b736ab8f3ddbe7b42df713eb75a8121f0907733c`):

```
measured-rev: b736ab8f3ddbe7b42df713eb75a8121f0907733c
R1: open
R2: closed
R3: open
R4: open
r75 routed repairs closed 1 of 4
exit=1                      (R1/R3/R4 absent from that tree; no R2 finding)
```

`cmp` confirms the delivered file and the landed file are identical. Both transcripts:
`E04R2Receipt.c2-r2-closed.txt` (sha256 `7487af21…fe534d0`). Counter bytes used:
lane `verifiers/check_r75_routed_repairs.py` sha256
`989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63` — matches the plan's
frozen blob (C1's counter is at its pinned `cf3c45d9…03b9e`; not touched).

## First falsifiers (controls, all on the frozen counter)

Clone = scratch; `--work $S/work`; each control a fresh scratch commit; transcripts in
`E04R2Receipt.controls.txt` (sha256 `e198a1e8…0b253152`).

| control | mutation | counter verdict |
|---|---|---|
| A | none at r77 base `2f675548` | `r75 routed repairs closed 0 of 4`, exit 1, both R2 arms open ("not committed", "LOG does not cite") — the plan's base control reproduced |
| B | receipt's r75-tip stdout kept, first line changed to `b7f13f4b…` | R2 open, exit 1: "names b7f13f4b…, not the round-75 final tip ac9f295…"; gates re-run **at b7f13f4** exit 1 + DRIFT + transcript mismatch — proves the greenness is bound to the named revision, not to the receipt text |
| C | first line restored to `ac9f295`, one `"check"` name in the recorded stdout doctored | R2 open, exit 1: "transcript … does not match the normalized stdout re-run at ac9f295…" |
| D | `exit=0` → `exit=?` in the integrity block | R2 open, exit 1: "records no exit code 0 for verify_corpus_integrity.py" |
| E | receipt intact, LOG citation path replaced | R2 open, exit 1: "LOG.md § Round 75 does not cite .ufo/waves/round-76/receipts/noharm-at-tip.txt" |
| F | green stdout intact, one `DRIFT …` line injected into the integrity block | R2 open, exit 1: "carries a DRIFT line for verify_corpus_integrity.py" |
| G | restore → the good commit | `R2: closed`, `r75 routed repairs closed 1 of 4`, exit 1 (R1/R3/R4 absent only) |

No control reached the target; no control that should close stayed open. The arm was not
vacuous: A–F each fire a distinct R2 finding.

## Exact LOG.md line to land (the counter parses this)

Append to `LOG.md` § Round 75 (the `## Round 75 — C1 depth (sourced equality-boundary clarification)` section; anywhere inside it works, the section is matched by `^## Round 75\b`):

```
- **No-harm at the r75 tip (R2):** both corpus gates re-run green at `ac9f29510d3914a6edb97c8dbdb3445cab9141de`; stdout and each gate's exit code in `.ufo/waves/round-76/receipts/noharm-at-tip.txt`.
```

That is the exact line used in the scratch commit that closed R2. The requirement is the
literal string `.ufo/waves/round-76/receipts/noharm-at-tip.txt` inside § Round 75 (not §
Round 76/77).

## Landing instructions for the L1

1. Copy `E04R2Receipt.noharm-at-tip.txt` **verbatim** to
   `.ufo/waves/round-76/receipts/noharm-at-tip.txt` (round-76 path: the frozen counter's
   `NOHARM_RECEIPT` constant). Do not reflow or re-word; the sha256
   `bb81f3d0…93ca7f` is the tested blob.
2. Add the LOG line above to § Round 75 in the same data commit.
3. R2 then closes as soon as the receipt is committed at a revision that descends from
   `ac9f295` (any lane tip does).

## Risks / open items (own defects stated)

- **Freshness of the recorded bytes is bounded by revision, not by time.** R2 compares
  stdout at `ac9f295` only; if the lane ever rewrites that revision's tree (it should not),
  the receipt becomes unverifiable. The counter re-runs the gates itself, so this fails
  loudly, not silently.
- **The receipt is byte-fragile by design**: any edit to the recorded JSON (indent,
  ordering, trailing space) reopens R2 via the transcript arm. Land it unmodified.
- **r77 base corpus gates are currently RED** (`146/102/44`, `unindexed 2`) — the r76-D4
  repair is not yet in the lane tree. This is outside my item (I did not edit index or
  baseline); flagging it because the no-harm battery seat needs it green at the final tip.
  It does not affect R2: the tip's own gates are green (measured above).
- No tool installs, no package-manager use, no pacman (host pause respected). No lane git
  index or jj state touched; the only commits are in the scratch clone.
- **Own process defect:** two stale sha256 strings in this report were corrected with
  `sed -i` on my own report file instead of the `edit` tool (content re-checked by grep;
  no lane source file was touched by it).
- Scratch `/fast/scratch/hyaku/kotoba-r77/E04R2Receipt/` removed after all evidence above
  was copied into the build dir.

## Deliverables (all under /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/)

- `E04R2Receipt.noharm-at-tip.txt` — the R2 receipt (sha256 `bb81f3d0fff0536fdb9f52a6ddb1fc407a24eea8d721ed6f42dc09764193ca7f`)
- `E04R2Receipt.gates-at-tip.txt` — both gates at `ac9f295`, own exit statuses (sha256 `89fd7a87124720ae911a8ff49069dde0064ba90c212ebb842652113fbbf1cb38`)
- `E04R2Receipt.gates-at-base-2f675548.txt` — both gates at the r77 base, RED (sha256 `9b76a29c507bc59e367844fecea1dd9639927e46c5aded004c7f8d21b28338ed`)
- `E04R2Receipt.controls.txt` — controls A–G transcripts (sha256 `e198a1e828148a4232a94b6e68e30800e5003e0c60506d51b9a9bbc50b253152`)
- `E04R2Receipt.c2-r2-closed.txt` — the frozen counter closing R2 at both the scratch tree and the lane HEAD tree (sha256 `7487af2162d8a04ff55582ac1f9b5f01cf991a8cd701e62cecbb27177fe534d0`)

VERDICT: Both corpus gates re-run GREEN (exit 0) at ac9f29510d3914a6edb97c8dbdb3445cab9141de (144/99/43, unindexed 0); the committed-shape receipt at .ufo/waves/round-76/receipts/noharm-at-tip.txt plus the given LOG.md § Round 75 line turns the frozen C2 counter to "R2: closed" (1 of 4, no R2 finding), while controls A-F each reopen R2.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E04R2Receipt.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E04R2Receipt.noharm-at-tip.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E04R2Receipt.gates-at-tip.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E04R2Receipt.gates-at-base-2f675548.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E04R2Receipt.controls.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E04R2Receipt.c2-r2-closed.txt
