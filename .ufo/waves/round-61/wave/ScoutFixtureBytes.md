# ScoutFixtureBytes — W1 recycled bytes and the four eligible r60 pages

Seat: kotoba-r61-wave-ScoutFixtureBytes. Read-only. No installs. No git/jj writes.
Measured 2026-10-23. Lane /home/vgpnk/Projects/shokunin/kotoba-shokunin.
Plan base f3246d1493b60ea1c0d947a19c39f9e08e92f326.
HEAD at measurement 7827628a939b0333c89892dfcedc72e390ccfb60 (base is an ancestor; merge-base --is-ancestor exit 0).
The four eligible snapshot blobs are identical at the plan base and at that HEAD.

Confidence: high on every sha (sha256sum and cmp). Lane absence of the old Claude blob is git cat-file -e plus a size search, not a full object walk.

## What W1 is

Plan C1 world W1 is CtlReopenForged d (`.ufo/waves/round-60/controls-v2/SUMMARY.md`; seat report `.ufo/waves/round-60/controls-v2/CtlReopenForged.md` lines 127-133 and 379-392). Variant d copied three round-53 scratch files into a three-client sandbox and kept the pristine row's `Fetched 2026-10-23T12:06:23Z` claim. Re-hash on 2026-10-23 matches the seat's paste.

That sandbox is not the committed seven-page round-60 tree. Snapshot ids inside it were remapped:

| sandbox path at d | client in the d world | lane file with the same bytes |
|---|---|---|
| `.ufo/waves/round-60/snapshots/S103.page` | Claude Code (only page that differs from sandbox pristine) | none |
| `.ufo/waves/round-60/snapshots/S104.page` | Copilot CLI | lane `S106.page` (not lane `S104.page`) |
| `.ufo/waves/round-60/snapshots/S105.page` | Cursor | lane `S108.page` (not lane `S105.page`) |

Lane `S104.page` is Codex (`9d1f87a2…`, not eligible). Lane `S105.page` is VS Code (`a45c9e9f…`, eligible). Copying those two lane files does not reproduce W1.

## W1 byte table

`cmp` of each scratch file against `git -C /fast/scratch/hyaku/kotoba-r60/CtlReopenForged show 7f05968a085ddf9fb9155b0a1047808d616b7b1b:PATH` exited 0.

| role | reproduce-from (scratch; seat-cited) | bytes | sha256 | git blob |
|---|---|---:|---|---|
| W1 Claude (d's S103) | `/fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md` | 51971 | `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff` | `bbb7d6f4e7350c51069f1f12bc0b26ec252e4a5b` |
| W1 Copilot (d's S104) | `/fast/scratch/hyaku/kotoba-r53/ScribeCopilotCli/fetch/copilot-cli-custom-instructions.md` | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | `56a6ad07c0eec9583847973af7b903a34e4f143f` |
| W1 Cursor (d's S105) | `/fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/gate.4524a03e99d4` | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | `47c1554d6fb3be35e292f7dd525d3241fd2ff21e` |

Claude blob `bbb7d6f4` is absent from the lane (`git cat-file -e` failed; `find` of size 51971c under the lane printed nothing). It is stored only as sandbox commit `7f05968a085ddf9fb9155b0a1047808d616b7b1b` path `.ufo/waves/round-60/snapshots/S103.page`, plus the scratch file. Copilot blob `56a6ad07` is lane `S106.page`. Cursor blob `47c1554d` is lane `S108.page`. Both `cmp` exit 0 against those lane files.

Sandbox repo `/fast/scratch/hyaku/kotoba-r60/CtlReopenForged`. d commit parent `358e43d1d3839158865eb9a8d25bf75852cb7489`, committer time `2026-10-23T09:08:42-03:00`, subject `round60 CtlReopenForged d-copied-base-snapshots`. Not a lane commit. Sandbox HEAD at measurement was restored commit `3c8dabfb85017d5a6d4c89fb3e4574fbecf1c227`, whose `S103.page` is the fresh page `82d60341…` (54043 B), not W1. Copy the scratch path or `git show 7f05968a`, not the sandbox worktree.

Same Claude bytes also at scratch copies (not the path the seat cited): `/fast/scratch/hyaku/kotoba-r53/CriticC2Sizing-fetch/memory.md`, `ScoutClaudeBehaviour/memory.md`, `CriticDrift/scratch/memory.md`, `w2/W2CriticHeldOut/fetch/memory.md`, `w2/W2ReopenS043/memory.md`, `w2/W2CriticDrift/fetch/memory.md`. Two other `memory.md` files under `kotoba-r53` differ (`3b5ea6cc…`, `f441a575…`).

S043 in `corpus/SOURCES.md` records this full sha and 51,971 B, fetched `2026-10-22T20:04:43Z`. d pinned `971d75bf…` while the row still claimed `Fetched 2026-10-23T12:06:23Z`. Copilot and Cursor copies match the r60 pages, so the seat's before/after table changes only S103 (`971d75bf…` vs pristine `82d60341…`).

## Four eligible r60 snapshot pages (SOURCES pins)

Eligibility is the r60 census after erratum E1, not every file in `snapshots/`. Build dispatch (`.ufo/waves/round-60/build-dispatch.json`): Claude Code S103, VS Code S105, Copilot CLI S106, Cursor S108. Codex S104, Gemini CLI S107, and opencode S109 are the not-eligible siblings in the same directory.

`sha256sum` of the committed pages equals the full sha on the SOURCES row. Blobs are `git rev-parse f3246d1493b60ea1c0d947a19c39f9e08e92f326:.ufo/waves/round-60/snapshots/FILE` and the same id at HEAD `7827628a`.

| client | row | path at base f3246d14 | bytes | sha256 | git blob | SOURCES pin |
|---|---|---|---:|---|---|---|
| Claude Code | S103 | `.ufo/waves/round-60/snapshots/S103.page` | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` | `022dc3bab2728a6525b78e4a02365d396f3682be` | equal (S103: 54,043 B, fetched 2026-10-23T12:08:16Z) |
| VS Code | S105 | `.ufo/waves/round-60/snapshots/S105.page` | 23715 | `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f` | `0400f45312eb5e0381b2d8c857c06712e0d2f18d` | equal (S105: 23,715 B, fetched 2026-10-23T12:08:55Z) |
| Copilot CLI | S106 | `.ufo/waves/round-60/snapshots/S106.page` | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | `56a6ad07c0eec9583847973af7b903a34e4f143f` | equal (S106: 8,730 B, fetched 2026-10-23T12:08:47Z) |
| Cursor | S108 | `.ufo/waves/round-60/snapshots/S108.page` | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` | `47c1554d6fb3be35e292f7dd525d3241fd2ff21e` | equal (S108: 17,403 B, fetched 2026-10-23T12:09:11Z) |

Introducing commit of those four paths at the plan base: `7b80ae80cda69a95b6fc90879395113a99a57912`, committer time `2026-10-23T09:28:13-03:00`, subject `round-60: C1 data — SKILL § Scoped rule files by client, entry, S103-S111, snapshots, lesson, Q52-Q55, budget move, index rows; controls-v2 summary`.

`cmp` exit 1: scratch `ScribeClaudeCode/memory.md` vs lane `S103.page` (51971 vs 54043; `971d75bf…` vs `82d60341…`). That is the only W1 page that is not already an eligible r60 snapshot.

## Fixture-builder recipe

1. Eligible pass set: copy the four lane paths in the table above. Do not substitute sandbox `S104.page` or `S105.page`.
2. W1 Claude page: copy `/fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md`, or `git -C /fast/scratch/hyaku/kotoba-r60/CtlReopenForged show 7f05968a085ddf9fb9155b0a1047808d616b7b1b:.ufo/waves/round-60/snapshots/S103.page`. Expected sha `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`, 51971 bytes. There is no lane blob to show.
3. W1 Copilot and Cursor pages: lane `S106.page` and `S108.page` are byte-identical to the scratch files the seat copied. In the d world those bytes were filed under the names `S104.page` and `S105.page`.

## Observed vs inference

Observed: the three scratch paths, their shas, sizes, cmp against sandbox commit `7f05968a`, lane snapshot shas at base and HEAD, SOURCES full pins for S103/S105/S106/S108, blob absence of `bbb7d6f4`, empty lane find of size 51971c, sandbox HEAD restored to the fresh Claude page.

Inference: none required for the tables. Not claimed: that scratch will still be present later; that `7f05968a` is reachable from any lane ref; live-page equality (not fetched).

## Unresolved

- No lane-history copy of the W1 Claude page. If `/fast/scratch/hyaku/kotoba-r53/` and the CtlReopenForged sandbox are deleted, those 51971 bytes are not recoverable from this lane.
- Did not re-read S048/S049 anchor cells for a full 64-hex pin (the r60 seat said those rows store prefixes). The files that resolve the prefixes were hashed in full, and those full digests equal S106 and S108.

## Measurements

```text
$ date -u
Fri 23 Oct 2026 07:09:20 PM UTC
$ sha256sum /fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md /fast/scratch/hyaku/kotoba-r53/ScribeCopilotCli/fetch/copilot-cli-custom-instructions.md /fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/gate.4524a03e99d4
971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff  /fast/scratch/hyaku/kotoba-r53/ScribeClaudeCode/memory.md
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  /fast/scratch/hyaku/kotoba-r53/ScribeCopilotCli/fetch/copilot-cli-custom-instructions.md
884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  /fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/gate.4524a03e99d4
$ wc -c of those three
51971 8730 17403
$ sha256sum lane/.ufo/waves/round-60/snapshots/S103.page S105.page S106.page S108.page
82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7  S103.page
a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f  S105.page
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980  S106.page
884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8  S108.page
$ wc -c of those four
54043 23715 8730 17403
exit 0
```

```text
$ date -u
Fri 23 Oct 2026 07:09:47 PM UTC
$ cmp -s scratch/memory.md lane/S103.page ; echo exit
1
$ cmp -s scratch/copilot-cli-custom-instructions.md lane/S106.page ; echo exit
0
$ cmp -s scratch/gate.4524a03e99d4 lane/S108.page ; echo exit
0
$ git -C lane hash-object of the three scratch files
bbb7d6f4e7350c51069f1f12bc0b26ec252e4a5b
56a6ad07c0eec9583847973af7b903a34e4f143f
47c1554d6fb3be35e292f7dd525d3241fd2ff21e
$ git -C lane rev-parse HEAD
7827628a939b0333c89892dfcedc72e390ccfb60
$ git -C /fast/scratch/hyaku/kotoba-r60/CtlReopenForged cat-file -t 7f05968a085ddf9fb9155b0a1047808d616b7b1b
commit
exit 0
```

```text
$ date -u
Fri 23 Oct 2026 07:10:07 PM UTC
$ git -C lane rev-parse f3246d1493b60ea1c0d947a19c39f9e08e92f326:.ufo/waves/round-60/snapshots/S103.page
022dc3bab2728a6525b78e4a02365d396f3682be
# S105 0400f45312eb5e0381b2d8c857c06712e0d2f18d
# S106 56a6ad07c0eec9583847973af7b903a34e4f143f
# S108 47c1554d6fb3be35e292f7dd525d3241fd2ff21e
# HEAD: same four ids
$ git -C lane cat-file -t bbb7d6f4e7350c51069f1f12bc0b26ec252e4a5b
fatal: git cat-file: could not get object info
$ git -C sandbox show 7f05968a:.ufo/waves/round-60/snapshots/S103.page | sha256sum
971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff
$ git -C sandbox show 7f05968a:.ufo/waves/round-60/snapshots/S104.page | sha256sum
00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
$ git -C sandbox show 7f05968a:.ufo/waves/round-60/snapshots/S105.page | sha256sum
884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
$ git -C sandbox log -1 --format='%H %P %cI %s' 7f05968a085ddf9fb9155b0a1047808d616b7b1b
7f05968a085ddf9fb9155b0a1047808d616b7b1b 358e43d1d3839158865eb9a8d25bf75852cb7489 2026-10-23T09:08:42-03:00 round60 CtlReopenForged d-copied-base-snapshots
$ git -C lane log -1 --format='%H %cI' f3246d14 -- the four eligible pages
7b80ae80cda69a95b6fc90879395113a99a57912 2026-10-23T09:28:13-03:00
exit 0
```

```text
$ date -u
Fri 23 Oct 2026 07:10:36 PM UTC
$ cmp -s scratch/memory.md vs git show 7f05968a S103.page ; echo exit
0
$ cmp -s scratch/copilot vs git show 7f05968a S104.page ; echo exit
0
$ cmp -s scratch/gate vs git show 7f05968a S105.page ; echo exit
0
$ git -C lane cat-file -e bbb7d6f4e7350c51069f1f12bc0b26ec252e4a5b
absent
$ date -u
Fri 23 Oct 2026 07:10:58 PM UTC
$ find lane -type f -size 51971c -print
(no output)
$ find lane -type f -size 54043c -print
lane/.ufo/waves/round-60/snapshots/S103.page
exit 0
```

installs: no installs
blockers: none
Attacked: W1 CtlReopenForged d round-53 scratch bytes (sha verified; Claude page absent from the lane) and the four eligible r60 snapshot pages (S103/S105/S106/S108) against their SOURCES pins.