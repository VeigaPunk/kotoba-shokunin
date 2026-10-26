# ExecCnControls — C1 shortcut worlds (kotoba round 73, wave 1)

**Verdict.** All seven shortcut worlds are built as committed-file bundles with
replay steps, and all seven were replayed in fresh fleet-shaped `--shared` clones
of base `072048f`. **By my own reading of the frozen conjuncts no world reads
4 of 4** (best: 3 of 4, worlds 3 and 5; world 4 is exit 2). **Under the wave-1
counter draft exactly one does: world 5 reads `vendor skill surfaces backed 4
of 4`, exit 0** — a plan kill-rule hit (`plans/round-73.md` § C1: "any shortcut
world scoring 4 means the counter is wrong; fixed before data"). The cause is
one shaping rule in `token_forms()` (`../ExecCnCounter/check_cn_vendor_surfaces.py:337-346`
in draft sha256 `051d3e2d…`): a token with a leading `~/` is also tried without
it, so the never-stated user root `~/.trae/skills/` is backed by the page's
project root `.trae/skills/`. The delta that clears it: drop the `~/`-strip
form (keep the trailing-slash form). Nothing else in the seven worlds scores 4.

## Delivered

Under `.ufo/waves/round-73/w1/build/ExecCnControls/` (all new, untracked; the
L1 commits):

    README.md                  index, headline, assumptions
    build_worlds.py            deterministic generator of every bundle
    own-reading.py             independent re-read of conjuncts (a)-(d)
    replay.sh                  replays a world in a sandbox; used for readings.txt
    readings.txt               measured output of `bash replay.sh` (base + 7 worlds)
    _common/README.md          scaffold status, snapshot provenance, manifest convention
    _common/tree/              honest scaffold: entry, six mined rows, six pinned
                               snapshots, MANIFEST.sha256
    <world>/tree/              one overlay per world (lane-relative paths)
    <world>/README.md          defect, conjunct, predicted reading, replay steps

## Measured readings (base + seven worlds)

Command (from the bundle root): `bash replay.sh` — output committed byte-for-byte
in `readings.txt`; the file's header records the counter draft sha256
`051d3e2dca9ef34c44f27d1f8e11f2ca264814e641430fb6ba96baa346df22ce` with the
draft's own filled `SELF_SHA` `b4ca05cf…` (the local copy replay.sh ran was
byte-identical to that draft). The draft moved during the wave
(an earlier measurement at `786a39d1…` gave identical readings for all worlds;
the `token_forms` body was unchanged).

| world | own reading | counter draft | census `validate --file` |
|---|---|---|---|
| base (do-nothing) | 0 of 4, exit 1 | 0 of 4, exit 1 | exit 0 (20 W04) |
| 1-staged-entry-unchanged | 0 of 4, exit 1 | 0 of 4, exit 1 | exit 0 |
| 2-rows-queued | 0 of 4, exit 1 | 0 of 4, exit 1 | exit 0 |
| 3-invented-root | 3 of 4, exit 1 | 3 of 4, exit 1 | exit 0 |
| 4-tampered-snapshot | exit 2 | exit 2 | exit 0 |
| 5-token-stuffed | 3 of 4, exit 1 | **4 of 4, exit 0** | exit 0 |
| 6-entry-outside-knowledge | 0 of 4, exit 1 | 0 of 4, exit 1 | exit 0 |
| 7-staged-rows-as-is | 0 of 4, exit 1 | 0 of 4, exit 1 | exit 1 |

The scaffold (`_common` alone) reads **4 of 4, exit 0** in both readers and its
registry is census-clean — that is what makes each world's failure attributable
to its own defect:

```
$ python3 -B /tmp/…/counter-frozen.py --repo "$R" --rev 9c8e77f1535d04057c6b784380b177e98284e4cb
measured-rev: 9c8e77f1535d04057c6b784380b177e98284e4cb
vendor skill surfaces backed 4 of 4
held at base: 0
$ python3 -B own-reading.py --repo "$R" --rev 9c8e77f…   -> "vendor skill surfaces backed 4 of 4" (exit 0)
$ bash ../scripts/sources-census.sh validate --file "$R/corpus/SOURCES.md"   -> exit 0 (20 W04)
```

## Findings

**F1 — the do-nothing figure reproduces.** Counter on the bare base
(`bash replay.sh base`): `measured-rev: 072048f…`, `vendor skill surfaces backed
0 of 4`, `held at base: 0`, exit 1; own-reading identical. The registry at base
holds no vendor host (`plans/round-73.md:60` freezes the print
`"vendor skill surfaces backed N of 4"`). The draft also runs directly as
committed: `python3 -B ../ExecCnCounter/check_cn_vendor_surfaces.py --rev 072048f…`
prints `vendor skill surfaces backed 0 of 4`, `held at base: 0`, exit 1.

**F2 — world 1 (staged entry unchanged) dies at the entry's first line.** The
staged entry opens with a `# ` title, so the counter returns 0 of 4 with:
`entry does not open with source: lines` … `cited S221 absent from the entry's
own source: lines`. No registry rows and no snapshots exist in that world
either; a counter that only counted table rows would still have to invent them.

**F3 — world 2 (rows `queued`) is invisible to the census.** Counter:
`TRAE: S217: status 'queued' (want 'mined')` (and one per row), 0 of 4, exit 1.
`census validate` exits 0: `queued` is a legal status, so the census cannot be
the second evidence for (b). (It can only reject the schema, never the claim.)

**F4 — world 3 (invented root) isolates the token test.** TRAE row
(`3-invented-root/tree/corpus/knowledge/chinese-vendor-skill-surfaces-round73.md:19`)
names `.bytedance/skills/`, absent from `S217.page`; both readers print 3 of 4,
exit 1, with `TRAE: token '.bytedance/skills/' does not occur word-bounded in the
snapshot(s) of S217`.

**F5 — world 4 (tampered snapshot) exits 2 in both readers, as the predicate
demands.** `S217.page` gains an appended comment; the manifest keeps the old pin:
`environment error: snapshot_tampered: .ufo/waves/round-73/snapshots/S217.page`,
exit 2. Census exits 0 — no schema gate sees the pin.

**F6 — world 5 (token-stuffed row) is the kill-rule hit.**
`5-token-stuffed/tree/corpus/knowledge/chinese-vendor-skill-surfaces-round73.md:19`
adds `~/.trae/skills/` to a row whose other three roots are honest. The page
never states that root:

```
$ grep -cF -- '~/.trae/skills'  _common/tree/.ufo/waves/round-73/snapshots/S217.page
0
$ grep -cF -- '.trae/skills/'   _common/tree/.ufo/waves/round-73/snapshots/S217.page
3
```

The counter still reads 4 of 4, exit 0, because of its own shaping:

```
$ sed -n '337,346p' ../ExecCnCounter/check_cn_vendor_surfaces.py
def token_forms(token: str) -> list[str]:
    """The token itself, without a leading ``~/``, and each without a trailing ``/``."""
    forms = [token]
    if token.startswith("~/"):
        forms.append(token[2:])
```

`~/.trae/skills/` → `.trae/skills/` → present, so the invented user root is
"backed" by the project root. Own-reading (token as written only) prints 3 of 4.
**Required before data:** delete the `~/`-strip form (keep the trailing-slash
one), or require the tilde form to occur literally. World 5 is the red anchor
for that fix; it must go from exit 0 to 3 of 4.

**F7 — world 6 (entry outside `corpus/knowledge/`) is caught only by the frozen
path.** The entry sits at `corpus/chinese-vendor-skill-surfaces-round73.md` and
every registry `used-by` follows it, so the registry is internally consistent:
counter `entry corpus/knowledge/chinese-vendor-skill-surfaces-round73.md absent
at <rev> (the frozen path is the entry's only home)`, 0 of 4, exit 1; census
exit 0. A counter that globbed `**/*vendor-skill-surfaces*` would read 4 of 4
here.

**F8 — world 7 (campaign schema, staged rows as-is) is rejected by the census.**
Six package rows appended verbatim (S214, S216, S217, S218, S219, S221) under the
staged entry. On the committed sandbox tree:

```
$ bash ../scripts/sources-census.sh validate --file "$R/corpus/SOURCES.md"
exit 1 — E03 x2, E09 x6, E11 x15, W04 x20
```

`E03` = S214/S216 already in the lane (the plan's collision table), `E09` = each
row's `recheck` is prose, e.g. `60d — re-fetch and confirm the `.agents` toggle
and the rules-vs-skills paragraph are unchanged (ran 2026-10-23)`
(`sed -n '18p'` of `SOURCES.append.md`, cell 11), `E11` = the rows' `used-by`
package paths do not exist in the lane. Counter: 0 of 4, exit 1 (entry trio,
then `used-by`). Running the same command against the bundle's partial
`tree/corpus/SOURCES.md` also exits 1 but reports 228 E11 because the bundle has
no `SKILL.md`/`corpus/knowledge/` files; use the sandbox copy for attribution.

**F9 — "escaped pipes" is not what the staged rows carry.** The assignment text
and the plan's shortcut name say the campaign rows use escaped pipes; observed:

```
$ grep -c '\\|' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
0
$ awk -F'|' 'NR==18{print NF-2}' …   -> 11      # the six lines are 11 cells, unescaped
```

The campaign schema's real defect is prose `opened`/`recheck` cells and
package-relative `used-by` paths, plus id collisions — not pipe escaping.

**F10 — predicate calibration hazards the L1 should freeze deliberately.**
(a) The quote rule ("5–25 words") plus the counter's `MIN_QUOTE_WORDS = 5`
(`check_cn_vendor_surfaces.py:140`, word-split at `:370`) is hostile to the
Chinese pages: the package's own quotes are 1 word (TRAE: `智能体不会在任务开始时一次性读取所有技能的完整内容`)
and 4 words (Zhipu). If ScribeCnEntry copies those quotes, (d) fails for three
vendors. My scaffold's quotes reach 6–16 whitespace words only by spanning
bullets/sentences. (b) The plan never fixes the snapshot filename convention;
the counter resolves a cited id by manifest-prefix (`S217…`), so the manifest
must pin bare `<S###>.page` names (my bundles do; `_common/README.md` states
it). (c) The census cannot see entries at all (worlds 1, 6 exit 0), accepts
`queued` rows (world 2), and cannot see snapshot tampering (world 4): it is a
schema gate, not a second evidence for C1's form. (d) The counter's own
`entry_problems()` is entry-level: one broken `source:` trio fails all four
vendors — correct per the plan's "single surface", but it means no vendor can be
backed while the trio is defective.

**F11 — provenance and limits.** I fetched nothing over the network; the six
snapshots are byte copies of this wave's seat fetches (`ExecSrcTrae`,
`ExecSrcCodebuddyIde`, `ExecSrcCodebuddyCli`, `ExecSrcKimiEn`, `ExecSrcZhipu`,
`ScoutCnCensus`), with byte counts and sha256 pins recorded in
`_common/README.md`. Their upstream access records are those seats' reports, not
mine — a reviewer must confirm them before the L1 commits the snapshots. The
counter draft changed mid-wave (`786a39d1…`, `SELF_SHA` all zeros → `051d3e2d…`,
`SELF_SHA` filled); readings were re-measured on the later one, so the draft is
runnable as committed without a local edit.

**F12 — contract compliance.** Writes: this report plus
`.ufo/waves/round-73/w1/build/ExecCnControls/**`. `git status --porcelain` in
the lane shows only that untracked directory (filtered output empty for every
other path). Every git write happened inside `mktemp -d /tmp/k73fleet-*` clones
with a throwaway identity; `git -C "$R" rev-parse --show-toplevel` was checked
before the first commit of each. Sandboxes and scratch were deleted before
return. No tool was installed; no pacman transaction; the longest single command
was the 8-world replay at ~18 s.

## Risks

- World 5's counter reading depends on the draft's current `token_forms`; if the
  counter is fixed, re-run `bash replay.sh 5-token-stuffed` and expect 3 of 4.
- World 4's exit 2 is the predicate's "missing or tampered snapshot is exit 2";
  a counter that folded tampering into a content 3 of 4 would pass the other six
  worlds and silently accept an edited page.
- The scaffold entry text is not a submission. If the Scribe lands different
  prose, the worlds still isolate their defects only if the honest baseline
  keeps reading 4 of 4; re-derive `_common` against the landed entry before any
  data run.
