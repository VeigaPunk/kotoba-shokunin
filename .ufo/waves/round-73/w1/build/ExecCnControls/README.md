# C1 shortcut worlds — ExecCnControls (kotoba round 73, wave 1)

Seven committed worlds for the frozen C1 predicate in
`plans/round-73.md` § C1. Each world is the cheapest input that would satisfy a
counter reading only the *form* of the predicate; each must read below 4 of 4.

**Headline.** Six of the seven worlds score below 4 of 4 under both readers.
World 5 does not: the wave-1 counter draft
(`../ExecCnCounter/check_cn_vendor_surfaces.py`) reads **4 of 4, exit 0** on it,
because `token_forms()` strips a leading `~/`, letting the project root
`.trae/skills/` back the never-stated user root `~/.trae/skills/`. Under the
plan's kill rule (“any shortcut world scoring 4 means the counter is wrong;
fixed before data”) the counter needs that one-line fix before any seat scores
C1 data.

| world | conjunct attacked | own reading | counter draft |
|---|---|---|---|
| base (do-nothing) | — | 0 of 4, exit 1 | 0 of 4, exit 1 |
| 1-staged-entry-unchanged | (a) trio, (b), (c) | 0 of 4, exit 1 | 0 of 4, exit 1 |
| 2-rows-queued | (b) status | 0 of 4, exit 1 | 0 of 4, exit 1 |
| 3-invented-root | (a) token | 3 of 4, exit 1 | 3 of 4, exit 1 |
| 4-tampered-snapshot | (c) pin | exit 2 | exit 2 |
| 5-token-stuffed | (a) token | 3 of 4, exit 1 | **4 of 4, exit 0** |
| 6-entry-outside-knowledge | (a) frozen path | 0 of 4, exit 1 | 0 of 4, exit 1 |
| 7-staged-rows-as-is | (b) + schema | 0 of 4, exit 1 | 0 of 4, exit 1 |

## Layout

    _common/tree/            honest scaffold: frozen entry, six mined rows,
                             six sha256-pinned snapshots, MANIFEST.sha256
    <world>/tree/            one overlay per world (lane-relative paths)
    <world>/README.md        the world's defect, conjunct, reading, replay
    own-reading.py           an independent re-read of the four conjuncts
    replay.sh                replays a world in a fresh fleet-shaped sandbox
    readings.txt             measured output of `bash replay.sh` (all worlds)

World 1 and world 7 are applied on the bare base (they carry the staged entry,
no scaffold); worlds 2-6 apply `_common/tree` first and then their overlay.
World 6 additionally deletes the frozen-path entry after copying.

`_common` is the honest baseline, not a candidate submission: it reads 4 of 4
in both readers and its registry is census-clean (exit 0, 20 pre-existing W04
warnings), which is what makes each world's failure attributable to its own
defect. It is also what the real entry/rows must still look like when the Scribe
lands them; only the L1 decides whether to reuse any of this text.

## Assumptions a reviewer must check

1. **Snapshot file names.** Pin table convention: `<S###>.page` under
   `.ufo/waves/round-73/snapshots/` (the lane's round-59/round-60 convention),
   with `MANIFEST.sha256` lines `<sha256>  <bare filename>`. The counter's
   `snapshot_name()` resolves a cited id by that filename prefix, so a manifest
   that pinned repo-root-relative paths would need the counter and the manifest
   changed together.
2. **Quote placement.** Each `source: S###` line carries one
   `located quote "…"` span (the lane's r67-r72 convention and the counter's
   `quote_for()`), 5-25 whitespace-separated words, verbatim from the snapshot
   after whitespace collapse only.
3. **Snapshots are byte copies of this wave's fetches** (`SNAP_SRC` in
   `build_worlds.py`): ExecSrcTrae, ExecSrcCodebuddyIde, ExecSrcCodebuddyCli,
   ExecSrcKimiEn and ExecSrcZhipu page texts, plus ScoutCnCensus's Kimi Chinese
   page text. Their sha256 values are the pins in `MANIFEST.sha256`.
4. **`own-reading.py` is not the counter.** It reads the four conjuncts
   independently so a disagreement is visible. Where it disagrees with the
   counter draft, the counter wins until the plan says otherwise — except that
   the plan's kill rule (world 5) is exactly such a case.
