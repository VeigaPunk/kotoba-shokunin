# Kb81E12Census — census + SOURCES mechanics (executor, leaf)

Round 81 w1. Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, base `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
No lane file was edited, no lane git mutation (read-only `rev-parse`/`status` only). No tool was installed
(pacman untouched; brief says the host is paused). Scratch: `/fast/scratch/hyaku/kotoba-r81/Kb81E12Census`
(five lane clones + fixture driver, removed on exit).

## What this seat owned

Run the fleet census at base, then apply the round's SOURCES edits (S249 row, S250 supersede row, S248
`used-by` old->new) in a scratch clone and re-run census + counts, publishing before/after blocks with the
exact edits; confirm every new row parses to 11 cells (`NF==13`); confirm the S230 supersede text cites the
**verified** repository, not the row's own old attribution.

The rows were drafted by `Kb81S05SourcesEdits` while this seat was deriving its own; I validated **their**
bytes (the drafted deliverable) and published my derivation separately as a cross-check. Which one was used
is stated in the receipt (§2, F9).

## Evidence (own exit capture; full log in the receipt)

| step | command | result |
|---|---|---|
| census at base | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | **exit 0**, 31 W04 + `kotoba ok` |
| counts at base | `... census --root ... kotoba` | **exit 0**: rows 174, A135/B22/C17, mined149/queued8/rejected17, invalid 0, missing 0 |
| rows at base | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | 174 |
| apply drafted edits | `git apply --binary build/Kb81S05SourcesEdits.patch` (final sha256 `6d0d5717…`, 3+/1-; the earlier draft `94606f8f…` measured identically) | exit 0, `corpus/SOURCES.md` only |
| schema | `awk -F'|' '/^\| S24[89] |^\| S250 /{…}'` | S248/S249/S250 each **NF=13, 11 cells** |
| validate, targets absent | `... validate <clone>` | **exit 1**, exactly 3 E11 (S249 entry, S249 lesson, S250 lesson) |
| validate, targets present | same, with entry+lesson fixtures | **exit 0**, `clone5 ok`, 32 W04, **0 E-codes** |
| counts after | `... census <clone5>` | **exit 0**: rows **176**, A**137**/B22/C17, mined**151**/queued8/rejected17, invalid 0, missing 0 |
| recheck cadence | `... overdue` base and after | exit 0 both, 173 cadence lines both, no new overdue |
| commit classes | `verifiers/verify_corpus_integrity.py --repo <tree> --json --no-baseline` | `commit_total` **46->46**, `commit_unresolvable` **2->2** (same sites `SOURCES.md:171,172`), `commit_nonhash` 0, `commit_truncated` **4->5** (new `SOURCES.md:191` `25cc5c7b…`), `commit_quoted_excluded` 6 |
| correction sweep | `verifiers/check_correction_sweep.py --root .` | exit 0, `0 stale block(s)`, no S230/pi-mono entry |

Both census forms behave the same: the `--root … kotoba` form at base, the script's own directory target
(`validate <clone>`, which maps `<dir>/corpus/SOURCES.md` and uses `<dir>` as the E11 root) at after.

## The three edits, and why each is safe

* **S249** (docs, tier A, `mined`, opened 2026-10-27, recheck 90d) — same canonical URL as S248, so the
  validator's E04 arm is only avoided because the **scope cell differs** (query-config `allowedTools` /
  `allowed_tools` channel + `allowManagedPermissionRulesOnly` override, vs S248's frontmatter scope).
  Measured: copying S248's scope into S249 gives `E04 S249 duplicate url … within scope …`, exit 1.
  used-by names the C2 entry and the round lesson; both must exist (E11).
* **S250** (own-work, tier A, `mined`) — no URL in the source cell (own-work precedent S020), teaches opens
  exactly `supersedes S230 — `. It adds **no** `commit \`<hex>\`` token, so the plan's "both hex
  occurrences" arithmetic holds; measured counterfactual: writing the id in that grammar adds a third
  unresolvable site (`SOURCES.md:191`, total 47/3) under base instruments.
* **S248** `used-by` `—` -> `corpus/knowledge/allowed-tools-sdk-round81.md`; status stays `queued`, no other
  cell moves. Because the row is `queued`, E11 does **not** path-check it (measured, M3) — see F4.

## Verified binding (S230 -> mistralai/mistral-vibe), re-derived here

`git ls-remote https://github.com/mistralai/mistral-vibe refs/heads/main` = `7bb48f213ac677f943d5c791199ed3dddf302f00`;
`git ls-remote https://github.com/badlogic/pi-mono` = 4,120 refs, **0** carrying the id; GitHub commits API
answers 200 for mistral-vibe and **422 "No commit found for SHA"** for pi-mono's current repository id;
commit-pinned raw README 200 / 77,634 B / sha256 `fc48a5db…`, byte-identical to the r79 receipt. This
matches `Kb81E03ExtManifest.json` (hash-keyed, one entry), so the class covers every occurrence of the hash
rather than one line. The S250 anchor text and the `supersedes S230 —` sentence agree with these bytes.

Also verified the S249 pin end-to-end: snapshot `.ufo/waves/round-81/snapshots/S249.md` = 28,395 B, sha256
`ac62c2df…`, identical to `S249.manifest`, to `S249.fetch.json`, to S248's earlier record, and to **my own**
fetch (`curl -sSL … /agent-sdk/skills.md` HTTP 200, 28,395 B, same digest). The row's 10-word quote, the
entry's 13-word quote and the 23-word alternative each occur exactly once in the snapshot's text view
(links -> text, backticks deleted) on raw line 348, after the first heading (line 5).

## Findings for the L1 / other seats

1. **Same-commit landing is mandatory**: rows without the C2 entry and round-81 lesson = validator exit 1
   with three E11 lines; with them, exit 0.
2. **`commit_truncated` 4->5** (new `SOURCES.md:191` `25cc5c7b…`, pi-mono's path commit). Green INFO class,
   but any receipt that pins "commit_truncated 4" at the r81 tip must read 5.
3. **Calibration gap (C2 conjunct e)**: E11 checks `mined` rows only. A queued S248 whose used-by points at
   a nonexistent path still validates exit 0 (M3). `check_sdk_allowed_tools.py` must assert the path exists,
   not only that the cell names the entry.
4. **Text-view convention is load-bearing**: S248's inherited 23-word quote occurs **1** time under
   links->text and **0** under link-targets-kept. The entry's "occurs 0 times in the text view" claim is
   true only for the latter; the C2 counter must declare its view.
5. **Freshness, now stated in the row**: `badlogic/pi-mono` redirects (api.github.com 301 -> repository
   `1035029907` = `earendil-works/pi`; that repository's commit lookup 422; commit-pinned raw page path
   **404 with 0 redirects**; mistral-vibe pinned raw README 200 / 77,634 B). I re-verified every clause the
   final patch adds. The served pi page blob is unchanged (sha256 `5b980552…`, 4,793 B).
6. **Two lesson drifts were found and the lesson seat fixed both while this wave ran** (S248 cell wording;
   "32 W04" -> 31). One residual wording item (quote word count) was itself resolved by the seat: the row
   carries 10 words, the entry 13, and the lesson now names both.
7. **Q29 checked, not assumed**: the correction sweep is scope-limited to README/SCORECARD/SKILL/PROVINCE/
   knowledge; an append-only SOURCES supersede row is the audit trail, so S250 creates no unregistered
   correction there (`0 stale block(s)`, exit 0).

## Risks / blockers

* None blocking. The receipt's after-state rests on the drafted patch (final sha256 `6d0d5717…`; the
  earlier draft `94606f8f…` measured the identical vector); if the L1
  integrates different row bytes, re-run `validate <tree>` — the E04/E11/E01 arms are the ones that move.
* My "after" tree carries two clearly-marked fixture files (entry, lesson) so E11 could be exercised;
  `unindexed 1->3` and `tracked_files 155->157` in the gate reading are those fixtures, not the patch.
* C1's own counter output and C2's counter output were **not** measured by this seat (other seats own those
  bytes); everything here is the registry side.

VERDICT: The drafted SOURCES edits parse to 11 cells each, move the census 174->176 rows with exit 0 in both census and validate (one new W04, zero E-codes) when the C2 entry and round-81 lesson land in the same commit, add no commit token (unresolvable stays 2 at SOURCES.md:171/172, truncated 4->5), and the S230 supersede text cites the re-verified mistralai/mistral-vibe binding.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E12Census.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E12Census-mutations.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E12Census-derived-alternative.patch; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E12Census.md
