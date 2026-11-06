author: hyaku closure (non-author integrator, @m_zfl)

# Round 94 verifier spot-check (non-author closure of kotoba round 94)

Lane round 94. Base `4d3e8e4d290d67ecf94a019059f434c71f399919`, tip `b623b420bdc8c3d9eecc10ff213ca749d5942ad0`
(freeze `edc731a9`, landing `f65347a6`, record `8068e32e`, wave evidence `b623b420`). Report
`.ufo/reports/round-94/kotoba.md` (fleet repo). Closure measured 2026-11-06T00:43Z.

Driver digest (copied from the mutable `.ufo/watchdog.log`):
`2026-11-05T19:44:31-03:00 launch kotoba round=94 pgid=1842492 driver=hyaku-inline attempt=1` ·
`2026-11-05T21:41:31-03:00 complete kotoba round=94; hyaku-inline attempt=1`.

## Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report committed by lane identity | `git log --format='%an %ae %H %ci' -- .ufo/reports/round-94/kotoba.md` | `kotoba-shokunin kotoba@shokunin.local fc882e2d… 2026-11-05 21:40:51 -0300` (before the 21:41:31 complete line) | pass |
| SHONEN heading, one line per box | read report § SHONEN | 4 lines, all `[~]`, each with an evidence pointer | pass |
| cited commits exist and are ancestors of `master` | `git cat-file -t <h>; git merge-base --is-ancestor <h> refs/heads/master` for 4d3e8e4d, edc731a9, f65347a6, 8068e32e, b623b420 | all `commit`, all ancestors | pass |
| lane pushed, nothing left | `jj-lane.sh state …`; `git status --porcelain \| wc -l`; `git ls-remote origin refs/heads/master` | `ahead=0 behind=0 head=detached tracked=0 untracked=0`; 0; remote = `b623b420…` | pass |
| round commits by lane identity | `git log --format='%h %an' 4d3e8e4d..b623b420` | 4 commits, all `kotoba-shokunin` | pass |
| prompt carries the template contract | `grep -nE '^#+ ' .ufo/prompts/kotoba-round-94.md` | §1 MISSION/AXES, §2 claims, §2b frontier, §3 L2 floor, §4 report contract, §5 commit, §6 hyaku addendum, §7 scratch; committed `7936f441` 19:44:29-03:00 | pass |
| wave dispatched | `git show b623b420:.ufo/waves/round-94/r94-w1-dispatch.json \| jq -c .counts` | `{"spawn":12,"resume":0,"total":12}` | pass |
| scratch removed | `ls /fast/scratch/hyaku \| grep -c kotoba-r94` | 0 | pass |
| marker? | — | real report, 4 resolvable lane commits | not a marker → status `ok` |

Defect (status-neutral): the dispatch-evidence prompt commit `7936f441` is authored `kotoba-shokunin`, not the orchestrator/protocol identity (attribution; same pattern as round 93).

## Claim re-checks

Self-tests and the frozen counter were **evidence-verified** from committed receipts, never executed (PROTOCOL §Gate standard, Closure consequence). Code, corpus and source facts were **re-measured** over committed bytes or by re-fetching.

**Frozen-instrument integrity.** `git diff --stat edc731a9 b623b420 -- verifiers/fixtures/round-94/selftest-kills.py plans/round-94.md` → empty (counter and plan unchanged since freeze).

**C1 — depth (battery `--self-test` kills k1/k2/k3).**
- Re-measured: `git show <rev>:verifiers/check_mutation_battery.py | grep -c 't\.check('` → 31 at `4d3e8e4d`, 38 at `f65347a6` and `b623b420` (matches the reported 31 → 38 assertions). `git diff 4d3e8e4d f65347a6 -- verifiers/check_mutation_battery.py` touches only `self_test()`: two k2 checks on G1 refusals (`"kill-set-size" not in out`), one k3 live-manifest appended-row check, and four rev-path arms (k3 added row exits 2 naming `kill-set-size` with `observed N+1 kill rows`; k2 anchor miss exits 2 without the label; k1 dirty-worktree precondition and committed-bytes-govern exit 0). Every new arm drives `run_main`/`run_evaluate`/`kill_set_check` on built fixtures — behavioural, not source reads. Sniff-token count (`grep -cE '__file__|inspect\.|getsource|tokenize'`) is 4 at base and 4 at landing: no new self-reading introduced.
- Evidence-verified: `receipts/redbefore-c1-base.txt` → `C1 targets killed 0 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3` `C1-PREDICATE-UNMET rc=1`; `receipts/landing/c1-counter.txt` → `3 of 3 … decoys held 3 of 3` `C1-PREDICATE-MET rc=0`; `forgery-c1-run.txt` → `decoys held 0 of 3` UNMET; `landing/bat-selftest.txt` → `lane rev f65347a6…`, `0 failure(s) over 38 assertions rc=0`.
- Bound agreed (A2): a comment-skipping sniffer can satisfy the frozen predicate; my code reading above is the independent behavioural check. **Verified.**

**C2 — consistency / calibration sub-axis (tip self-test covers every BATTERY pin key).**
- Re-measured: `BATTERY` at `f65347a6` lines 178-185 holds 6 scripts; the diff replaces the 2-arm loop (3 checks each = 6) with `keydrop-0..5` plus `keyswap` (7 arms × 4 checks = 28), +22 → the reported 80 → 102 is arithmetically consistent. The new `names only that key` check requires exactly one `has no INSTRUMENT_PINS key` line naming the dropped path. Self-test only; no production change.
- Evidence-verified: `redbefore-c2-base.txt` → p1/p2 `SURVIVED` over 80 assertions, `C2-PREDICATE-UNMET rc=1`; `landing/c2-counter.txt` → p1 killed at `keydrop-4`, p2 at `keydrop-0`, decoys held 2 of 2, `C2-PREDICATE-MET rc=0`; `forgery-c2-run.txt` → `decoys held 0 of 2` UNMET; `landing/tip-selftest.txt` → `0 failure(s) over 102 assertions rc=0` at `f65347a6`. **Verified.**

**No-harm.**
- `git diff 4d3e8e4d b623b420 -- SCORECARD.md` → append-only: round-94 annotations + round-95 intentions; no score changed.
- `git diff --stat 4d3e8e4d b623b420 -- SKILL.md PROVINCE.md SHONEN.md corpus/QUALITY.md` → empty.
- Evidence-verified receipts at `f65347a6`: round-93 `c1-killpin` and `c2-pinkey` `PREDICATE-MET`; round-92 controls `shortcuts refused 2 of 2; honest held 2 of 2`; gate registry `74 of 74 … phantom 0`; floors self-test `0 failure(s) over 176 assertions`.
- Tip battery `2 of 6` (round-93 landing `3 of 6`): the added red is `check_assertion_floors.py exit none wall 280.0s (timeout)` in `landing/tip-battery.txt`. Re-measured: the 19 instrument paths in `verifiers/floors-registry.json` at `f65347a6` intersect `git diff --name-only 4d3e8e4d f65347a6` in **none**, and `git diff --stat 4d3e8e4d f65347a6 -- verifiers/floors-registry.json verifiers/check_assertion_floors.py <19 paths>` is empty; `landing/floors-gate-standalone.txt` → `rc=0 wall 309s` at load ≈ 90. Ruled environmental (timeout under fleet load), **not harm**; routed.
- Receipt-check fix (mined mistake): `landing/receipt-hdr-*-before.txt` rc 2 → `*-a1.txt` rc 1 naming `MALFORMED` for hex41/indented/hex39/scratch-hex41/double-decl, `good` rc 0; round-93 receipts still resolve.

## Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| depth | improved | C1 re-measured (31 → 38 behavioural arms) + counter receipts 0/3 → 3/3 |
| consistency | improved | C2 re-measured (2 → 7 pin arms, 80 → 102) + counter receipts 0/2 → 2/2 |
| coverage | unchanged | no knowledge/ entry; one SOURCES row on already-held ground |
| operability | unchanged | SKILL.md byte-identical |
| freshness | unchanged | no row re-dated; S262's page re-fetched byte-identical (sha below) |
| calibration | unchanged | C2 is scored under consistency (round-93 precedent) |
| adjacency | unchanged | PROVINCE.md unchanged; sibling census red carried |

## Discernment spot-check (lesson `round-94.md` § Gate)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S269 PIT "Basic concepts" | admit (tier A, `mined`) | `curl -sSL https://pitest.org/quickstart/basic_concepts/` → `200 12155`, sha256 `c51d8423…92b3a` (equal to the row); line 175 `<p><strong>Killed</strong> means a test caught the mutation successfully.</p>`; lines 166-185 list Killed…Run error, "may time out", non-viable definition | agree (with caveat) | Quote present at the cited line, 8 words ≤ 25. The row's scope (meaning of classes for a kill rule; Non viable ≠ kill) is grounded. Caveat: same page as S262 → 34th `W04`; the lane's own scout advised against a second row, and the row exists because the frozen plan named it. The D7 correction (page does not ground the timeout rule) is correct: the page says only "may time out". |
| mutmut docs index | reject | `curl -sSL https://mutmut.readthedocs.io/en/latest/` → `200 51074`, sha256 `07453b3fdb3b962a4cc5aff66d7614a11016c9ce0ea482654c99e17688ec9cad` (equal to the lesson); `grep -ic` equiv 0, killed 0, survived 0 | agree | No outcome class is defined on the page; nothing for the counter to rest on. |
| Cosmic Ray concepts/theory | reject | concepts.html → `200 18482`, sha256 `d4da7008…adae7f` (equal); lines 170-176 "the test is killed, and the mutant is marked incompetent"; theory.html → `200 5939`, line 41 "is “incompetent”" | agree | Cosmic Ray folds timeouts into `incompetent`; its class set differs from PIT's, so it cannot ground the Killed / Non viable / Timed Out split. |

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, final `kotoba ok …/corpus/SOURCES.md`, 34 `W04` (new: `S269 duplicate url pitest.org/quickstart/basic_concepts across scopes`), no `E`. Rows `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 194 at `4d3e8e4d`, 195 at `b623b420` (matches report).

## Trend verdicts

- **expansion: unchanged** — no `knowledge/` entry admitted; S269 covers ground S262 already held.
- **quality: improved** — two self-tests now kill five base survivors (receipts above, code re-read); the receipt check fails closed on five malformed-header shapes (before rc 2 → after rc 1); S262/S269 page bytes re-verified identical by re-fetch. No admitted entry failed re-check.
- **discernment: improved** — this outside spot-check agrees with the gate on the admit and both rejects; the attack-seat disagreement (D7, timeout not grounded by S269) became a recorded lesson correction and addendum A3.

## Routed defects (lane fixes next round)

1. Fold or scope-justify the S269/S262 same-URL duplicate (34th `W04`); a frozen plan naming a row must not force an admit the scout argued against — record the rule in `QUALITY.md` if kept.
2. Counter scores any non-zero self-test exit as KILLED (D8; PIT lists `Run error` separately) — separate run error from kill.
3. Decoy guard misses comment-skipping sniffers (A2/D4) — add a code decoy.
4. Battery survivors N1, N5, N11 and receipt declarations not starting a line (D3).
5. Tip-battery floors gate timeout (280 s) under fleet load — make the timeout or the gate robust, then re-show `3 of 6` or better at a committed revision.
6. Attribution: prompt commit `7936f441` authored by the lane identity.

Operator note: SHONEN boxes remain `[~]`; promotion is operator-owned — nothing here promotes.
