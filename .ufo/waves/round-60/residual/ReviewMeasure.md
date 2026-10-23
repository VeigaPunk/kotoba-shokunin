Result: HOLDS — independent re-measure of C1 reproduces `4 of 4, exit 0` with `--fetch` at `7b80ae80cda69a95b6fc90879395113a99a57912` and at the lane tip (identical hash at run time); exit 1 without `--fetch` is the script's designed no-live behavior; script sha, all 7 committed snapshots, census exit 0, and SOURCES append-only all check.

Seat: KotobaR60.ReviewMeasure (reviewer). UTC window: 2026-10-23T18:10:09Z – 2026-10-23T18:13:26Z (`date -u` pasted below with the runs). No tools installed or updated; no web pages opened by me directly (the live fetch happened only inside the counter under test, its own ordinary-fetch path). Lane untouched (read-only git with `--no-optional-locks` only); all execution in the sandbox clone labelled below.

## Sandbox

`/fast/scratch/hyaku/kotoba-r60/ReviewMeasure` already existed (a lane clone at the right rev with foreign scratch: a `tip/` subdir and `sources_rows_115_123.txt`, not mine). I left it untouched and cloned fresh into my namespace:

```
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r60/ReviewMeasure/rm2 && git -C .../rm2 checkout -q 7b80ae80cda69a95b6fc90879395113a99a57912
→ CLONE2_OK / HEAD 7b80ae80cda69a95b6fc90879395113a99a57912
```

sandbox `7b80ae80…` checkout (/fast/scratch/hyaku/kotoba-r60/ReviewMeasure/rm2) — no sandbox commits made, nothing pushed.

## 1. Counter runs (v2)

`timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 7b80ae80cda69a95b6fc90879395113a99a57912 --fetch` — **exit 0**:

```
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 7b80ae80cda69a95b6fc90879395113a99a57912
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
EXIT=0
```

(All lines above byte-verbatim as printed; `EXIT=` is the shell's echo of `$?` after the command.)

Same command without `--fetch` — **exit 1**:

```
scoped rule files backed on committed snapshots 4 of 4; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 7b80ae80cda69a95b6fc90879395113a99a57912
reject Codex: … reject Gemini CLI: … reject opencode: … (same three lines as above)
EXIT=1
```

Designed behavior, not a failure: the frozen predicate is "exit 0 iff fetching and F ≥ TARGET" (verifiers/check_scoped_rules.py:1246-1249, docstring verbatim at :214-217); without `--fetch` it prints `live not run` and exits 1.

At the lane tip — `git -C <lane> rev-parse master` = `7b80ae80cda69a95b6fc90879395113a99a57912`, read immediately before and re-read immediately after the run (same value both times; tip == data rev at 2026-10-23T18:13Z), so the tip run is the same full-hash command:

```
timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 7b80ae80cda69a95b6fc90879395113a99a57912 --fetch
→ identical output to run 1; EXIT=0
tip at run time: 7b80ae80cda69a95b6fc90879395113a99a57912
Fri 23 Oct 2026 06:13:26 PM UTC
```

Side observation (designed strictness, recorded honestly): `--rev master` (symbolic) is refused — `could-not-evaluate: --rev 'master' is not a full 40-hex commit hash`, exit 2. The tip must be passed by full hash.

Semantics check: F = found on live page, K = snapshot-backed key count (print at :1235-1237); predicate exit 0 iff `--fetch` and F ≥ TARGET; `TARGET = 3` at :249. Observed F=4 ≥ 3 → exit 0. Consistent with plan round-60.md:62,115 ("TARGET = 3", receipt `C1 predicate: --fetch exit 0 (F>=TARGET)`). Minor drift, content-only: plan:115 cites "line 232" for TARGET; in the committed script it is line 249. The script sha is exactly the declared one (below), so this is a stale line citation in the plan prose, not a content mismatch.

Per C1's declared EXPLORATORY depth and plan erratum E2, this counter output is supporting evidence only; the semantic re-read lives with the L1/other seats. My verdict covers reproduction and artifact integrity.

## 2. Verifier script sha at both revs

`git show <rev>:verifiers/check_scoped_rules.py | sha256sum`:

- at data rev `7b80ae80…`: `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  -`
- at lane tip `master`: `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  -`

Both equal the declared `ca2585a4…cdb8c04a`. The counter's self-printed sha also matches (runs above).

## 3. Snapshots vs SOURCES rows (S103–S111)

SOURCES rows read at the data rev (corpus/SOURCES.md:115-123). Seven snapshot blobs exist at the rev (`.ufo/waves/round-60/snapshots/S103.page` … `S109.page`); `git show <rev>:<path> | sha256sum`:

| snapshot | blob sha256 at rev | SOURCES row sha | match |
|---|---|---|---|
| S103.page | 82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7 | 82d60341…7bb6e7 (:115) | ✓ |
| S104.page | 9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e | 9d1f87a2…383e8e (:116) | ✓ |
| S105.page | a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f | a45c9e9f…56caa1f (:117) | ✓ |
| S106.page | 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980 | 00e45ea5…57bb2c980 (:118) | ✓ |
| S107.page | e5fbfd6d580643a300b5ee0e622d9e2d8f97d4d23460e6b08e1c656251c2f2c2 | e5fbfd6d…c2f2c2 (:119) | ✓ |
| S108.page | 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8 | 884c67ca…21546bc8 (:120) | ✓ |
| S109.page | dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54 | dfb242d9…f5f93cb54 (:121) | ✓ |

7/7 exact. S110/S111 have no `.page` snapshot files at the rev; their rows claim byte-identity with S096/S097 rather than committing snapshots, and the shas match textually exactly: S110 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` = S096's recorded sha (:122 vs :108); S111 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` = S097's (:123 vs :109). I did not re-open the live URLs to re-derive those shas (out of my item's scope); recorded as row-internal consistency only.

## 4. Sources census

`timeout 300 /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` — **exit 0**. Output: 13 `W04 duplicate url … across scopes` warnings (S018, S019, S021, S054, S055, S056, S065, S086, and new rows S103, S104, S106, S110, S111), then `kotoba ok /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`. Warnings are informational; validator exits 0.

## 5. Append-only SOURCES (31092dc6 → 7b80ae80)

`git diff 31092dc6 7b80ae80cda69a95b6fc90879395113a99a57912 -- corpus/SOURCES.md | grep -c '^-[^-]'` → `0` (grep exit 1, the expected code for a zero count). Diffstat: `9 insertions(+)`, `0 deletions` — exactly the nine new rows S103–S111, no row modified or removed.

## Findings by severity

- None (no breaks). All acceptance checks pass.

Minor notes (non-blocking):
1. Plan `plans/round-60.md:115` cites TARGET at "line 232"; actual line in the committed (sha-verified) script is 249. Stale prose citation only.
2. Counter rejects symbolic `--rev` values with exit 2; tip must be given as a full hash. Recorded so future runs pass the hash.
3. Census W04 duplicate-url warnings include all five re-open rows (S103, S104, S106, S110, S111) — expected, since re-opens reuse a prior scope's URL; exit stays 0.
4. S110/S111 keep no snapshot bytes in-repo; their identity claim rests on the recorded S096/S097 row shas matching exactly (verified textually here), not on committed snapshots. If byte-level proof is ever demanded, a snapshot commit would be needed.

## Residual risk / verification gaps

- The `--fetch` runs exercised the live pages through the counter's own fetch path twice (18:10–18:13 UTC), both yielding F=4 of 4; I did not independently open the URLs, so a same-minute coordinated page change between the two runs is not excluded by me (irrelevant to C1's snapshot-backed claim, which is what K=4 measures).
- Per E2, two of the four passing keys passed the v2 counter via forged provenance; nothing here re-validates provenance — the counter output is supporting evidence only, as declared.
- Lane tip could move after 18:13 UTC; my tip equality statement is timestamped to that moment.

sandbox `7b80ae80…` checkout (/fast/scratch/hyaku/kotoba-r60/ReviewMeasure/rm2), unmodified working tree.
