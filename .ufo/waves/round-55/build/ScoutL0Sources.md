Result: DONE — at base f0e5de82 the append-only gate exits 1 with exactly the recorded 13 protected-cell changes (12 earlier + e792607e's S050), reproduced identically at two other revisions; the one-line L0 question is drafted in §5 (not written to the queue).

# ScoutL0Sources — the 12 earlier in-place SOURCES edits (kotoba round-55 build; L0 line draft)

Seat `KotobaR55.ScoutL0Sources` (scout, leaf; no subagents dispatched). Every run below was made in the
sandbox clone `/fast/scratch/hyaku/kotoba-r55/ScoutL0Sources`, checked out at
`f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c` (base). No file in the lane was written or executed from the
lane; no installs were needed.

## 1. The gate I ran (version pinned)

`verifiers/check_sources_append_only.py` at f0e5de82: 195 lines, sha256
`9f18f00ce488d687362cfa3e16df8f4fec56da9e580423a83d2bad6283998bd3`. It is the landed version
`bf65974c` (189 lines, sha256 `d4d1d62b…`, as recorded in `corpus/lessons/round-54.md:13`) plus
`cae8f2ea` (round-54 "append-only gate crash paths");
`git diff bf65974c f0e5de82 -- verifiers/check_sources_append_only.py` → 9 insertions, 3 deletions touching
only (a) the removed-row record shape, (b) one more self-test assertion per arm, (c) a `main()` try/except
`(UnicodeDecodeError, OSError)` → exit 2. The judging lines (what it reads, compares, counts) are unchanged.
Consequence for calibration: `--self-test` here prints `self-test: 0 failure(s) over 21 assertions` (7 arms × 3),
not M45's recorded 14 (7 × 2) — the third assertion came with `cae8f2ea`. Run: exit 0.

## 2. The run

```
cd /fast/scratch/hyaku/kotoba-r55/ScoutL0Sources
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
timeout 300 python3 -B verifiers/check_sources_append_only.py --rev f0e5de82
# exit 1
```

stdout captured to `ScoutL0Sources/append-only-at-f0e5de82.txt` — 39 lines (25 "log" notes on permitted
cells, 13 "breach" lines, 1 summary), sha256
`b1a89a1cd55ff1cf00a6dd3a00d6bf58a5ff8a514ea2f5ec71301655cee73ae1`; stderr empty (sha256
`e3b0c442…`); captured 2026-10-22T23:14:33Z (`date -u`). Summary line printed:

```
sources append-only breach 13 change(s) in 4 of 17 commits
```

**Count confirmation (the assignment's question): the gate prints 13 = the 12 earlier changes + the
`e792607e` S050 change.** Per commit: `bfd5a583a` 1, `542f51567` 6, `bf109cacc` 5 (= the 12 of M45 / routed
defect 8), `e792607e` 1. The same 13 breach lines print at three revisions:

| command | summary | exit |
|---|---|---|
| `--rev f0e5de82` (base) | `13 change(s) in 4 of 17 commits` | 1 |
| `--rev 7ad05d34` (round-54, 18:12:40 -0300) | `13 change(s) in 4 of 16 commits` | 1 |
| `--rev 58db81c4` (round-54, 18:39:07 -0300) | `4 of 17 commits` (M45 recorded this shape) | 1 |
| `--base 422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4 --rev f0e5de82` (the registered command, `SKILL.md:467`) | `rows clean: 1 commits scanned, 0 protected-cell changes` | 0 |

So the registered lane command is green over round 54's own range while the full-history scan is red —
the two facts the L0 line carries.

Coverage: 18 commits in this clone touch `corpus/SOURCES.md` (`git rev-list --no-merges --all --
corpus/SOURCES.md` → 18); all are ancestors of f0e5de82 (non-ancestor SOURCES edits → 0), and the file's
creation commit is skipped by the gate (no parent blob) → 17 scanned. Within this clone the scan sees every
SOURCES.md edit that exists.

## 3. The 13 protected-cell changes, one row each

Full hashes resolved with `git show -s --format='%H %ci %s' <short>`; the `old → new` column is the gate's
own printed window (first differing character, trimmed with `…`), byte-short by design. Cell sizes
old→new (bytes) are from a direct re-run of the gate's `parse`/`compare` over the same two blobs
(`ScoutL0Sources/breach-cells-full.txt`, sha256 `d18de5455463155f2a3923b37795d00aab6151e0f8b6d2b0f904f202fa94dc26`).

| # | commit (full) | row | cell | old → new (gate window) | bytes |
|---|---|---|---|---|---|
| 1 | `bfd5a583a9ba5e7ab702cca301ec2c44c8bf5287` (round-49 falsify-wave corrections, 2026-10-22 08:37:22 -0300) | S022 | teaches | ``Claude picks a skill by its `description` al…`` → ``The `description` is the field Claude uses t…`` | 477 → 641 |
| 2 | `542f515672306e1baefcb69ba79f1d4c18b6450e` (round-50 C1, 08:57:23 -0300) | S019 | scope | `…nd description` → `…nd description, and what the page says about…` | 52 → 179 |
| 3 | `542f51567` | S019 | anchor | `…ill structure field list, § Writing effectiv…` → ``…ill structure (`best-practices.md:146-166`),…`` | 285 → 563 |
| 4 | `542f51567` | S019 | teaches | `…scription rule` → `…scription rule; the page states no tie-break…` | 281 → 866 |
| 5 | `542f51567` | S022 | scope | ``…ption`'s role) and what the page says about …`` → ``…ption`'s role), how its skill listing is tru…`` | 201 → 251 |
| 6 | `542f51567` | S022 | anchor | ``…kills.md:389`); § Create your first skill (`…`` → ``…kills.md:389`) and `when_to_use` row (`:390…`` | 501 → 733 |
| 7 | `542f51567` | S022 | teaches | ``…ocation: true`` → ``…ocation: true`; re-opened 2026-10-22T12:28:4…`` | 641 → 1889 |
| 8 | `bf109caccccca8459d297edf09a7dc7828396d8f` (round-50 falsify corrections 2, 10:41:42 -0300) | S019 | teaches | `…he description is the only arbitration surfa…` → ``…he description, read with `name`, is the tri…`` | 866 → 923 |
| 9 | `bf109cacc` | S022 | teaches | ``…project), and a skill that fires where it sh…`` → ``…project), and nested same-name skills by the…`` | 1889 → 2006 |
| 10 | `bf109cacc` | S026 | scope | ``…iption` field decides delegation) and what t…`` → ``…iption` field is one of three inputs to dele…`` | 210 → 236 |
| 11 | `bf109cacc` | S026 | teaches | ``… it documents is over same-`name` subagents …`` → `… it documents between subagents is over same…` | 706 → 1031 |
| 12 | `bf109cacc` | S028 | teaches | `Copilot CLI is the one GitHub surface that d…` → `Copilot CLI documents name-keyed precedence …` | 419 → 543 |
| 13 | `e792607e85c78998bbf0ae4e2b5d350683eec0f7` (round-53 records/falsify corrections, 17:45:49 -0300) | S050 | anchor | ``…ctions.md` at commit `cfb894a5` (frontmatter…`` → ``…ctions.md` at zed-industries/zed@`cfb894a5` …`` | 358 → 370 |

Readings of what changed (from the full cells, so no more than the evidence says):

- #1 rewrote S022's `teaches` opening clause ("Claude picks a skill by its `description` alone — …" becomes
  "The `description` is the field Claude uses to decide whether a skill applies (…)"); the remainder of the
  cell keeps the round-49 text.
- #2–#7 (all `542f51567`, one commit): S019's `scope` gained "and what the page says about choosing between
  overlapping Skills"; S019's `anchor` replaced section names with line-ranged citations plus a re-open
  timestamp; S019's `teaches` appended the no-tie-break finding, sweep counts and the 1,024-character cap;
  S022's `scope` gained "how its skill listing is truncated and budgeted"; S022's `anchor` added the
  `when_to_use` row and more sections plus a re-open timestamp; S022's `teaches` appended text opening with
  the re-open note ("re-opened 2026-10-22T12:28:45Z, byte-identical, adding that a listing entry's combined
  `description` + `when_to_use` …"; the window shows only the first 44 characters of the appended text).
- #8 rewrote S019's `teaches` claim "the description is the only arbitration surface" → "the description,
  read with `name`, is the triggering input this page names"; #9 inserted "and nested same-name skills by
  the working directory (`skills.md:183-185`)"; #10 corrected S026's `scope` "the `description` field
  decides delegation" → "is one of three inputs to delegation"; #11 narrowed S026's `teaches` precedence
  claim to "between subagents" and added the built-in `claude` agent line; #12 rewrote S028's `teaches` head
  from "Copilot CLI is the one GitHub surface that documents a deterministic tie-break" to "Copilot CLI
  documents name-keyed precedence for duplicate components …" plus the SDK pointer.
- #13 added the `zed-industries/zed@` prefix to S050's `anchor` commit citation (routed defect 3; the
  round-54 correction row S061 is on record for it).

All 13 are cell changes; no "row present -> absent" breach was printed at any of the three revisions.

## 4. Cross-check against the lane's own records (citations read in place)

- `CORPUS.md:112-117` (contract v1 rule 2, at line 116): "Append-only. Only `status`, `recheck` and
  `used-by` change in place, and each change is logged old→new in the round lesson. A correction is a new
  row whose `teaches` opens `supersedes S0NN —`."
- `corpus/lessons/round-49.md:50-51` says "No other row moved." — while `bfd5a583a` (#1) rewrote S022's
  `teaches` in place.
- `corpus/lessons/round-50.md:76-78` discloses the `542f51567` edits as an ordinary gain ("S019 and S022
  also gain anchor, scope and teaches text for the round-50 facts (seat reports carry each old→new cell).
  No other row moved.") — it names only S019/S022; the `bf109cacc` S019/S022/S026/S028 rewrites fall under
  the same "No other row moved."
- `corpus/lessons/round-51.md:64-67` refused the same kind of edit citing the rule: "Contract v1 rule 2
  forbids editing `teaches` in place, and a superseding row with the same URL would add a W04 duplicate-URL
  warning, so the narrower cell stays and the entry carries the fuller reading."
- `corpus/lessons/round-54.md:13` (M45) records all 13 with the 12 "carried, not corrected"; `:53-58`
  ("Rows touched") records that S050 was not edited and that S061 is the correction row for `e792607e`.
- No prior L0 filing of this item exists: `grep -n "bfd5a583\|542f515\|bf109cac\|e792607\|M45\|protected-cell"
  /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` → 0 hits (file is 116 lines; its tail line is
  `mori | round-30 | …`).

## 5. Draft L0 line (one line; NOT written to the queue — integrator/operator appends it)

```
kotoba | round-55 | Ratify as recorded history or correct the 12 earlier in-place corpus/SOURCES.md protected-cell rewrites plus the already-routed e792607e S050 edit: verifiers/check_sources_append_only.py at f0e5de82 exits 1 with "13 change(s) in 4 of 17 commits" — bfd5a583a S022 teaches (1); 542f51567 S019 scope/anchor/teaches and S022 scope/anchor/teaches (6); bf109cacc S019 teaches, S022 teaches, S026 scope/teaches, S028 teaches (5) — 12 changes in three round-49/50 falsify-correction commits that the round lessons disclose only as cells that "gain anchor, scope and teaches text" with "No other row moved" (round-49.md:50-51, round-50.md:76-78), while round 51 refused the same edit citing contract v1 rule 2 ("forbids editing `teaches` in place", round-51.md:64-67); e792607e's S050 anchor rewrite is the round-53 spot-check's routed defect 3 with correction row S061 on record. CORPUS.md:116 rule 2 permits only status/recheck/used-by in place and requires a correction to be a new row opening "supersedes S0NN —"; the registered gate command is green on its pinned --base 422ffd10 range but the full-history scan is red. Operator ruling: (a) leave all 13 as recorded history (state any terms), or (b) file one correction row per change? Evidence: kotoba-shokunin/.ufo/waves/round-55/build/ScoutL0Sources.md. No lane action is taken until ruled.
```

## 6. Not verified / open

- Commit authorship and whether any of the three earlier commits' cells were disclosed anywhere beyond the
  cited lesson lines: not examined (out of scope).
- The 12 are "carried" per round-54; nothing in this round may dispose of them before the ruling — this
  seat only re-measured and drafted the line.
- The separate, already-recorded falsehood in S050 ("frontmatter only differs", `corpus/lessons/round-54.md:55-57`)
  is not part of the count and is not addressed here.
- Queue-side append order/dedup is operator-side; the line is not written.
- Process hygiene: all runs bounded by `timeout 300`; no processes left running; no lane jj/git writes and no
  lane file touched (read-only `grep`/`sed` reads only); no tool installs or upgrades were performed.