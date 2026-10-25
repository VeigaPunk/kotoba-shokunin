author: hyaku closure (non-author integrator, @m_opus)

# kotoba round 52 — verifier spot-check (non-author closure)

Base `c8579a4c5b48789e56fb9060ddd48f33569e1215`, lane tip `0c9180a69017c47d36b5f032c4bb27ed1d131908`, plan commit
`4c003a4b9c7dae8ebb8ad34bbc14cd1706febeeb`. Report `.ufo/reports/round-52/kotoba.md` (fleet `251d0b80`). The landed
whole is judged against the claims as declared at the plan commit. Measurements were run 2026-10-22 18:57–19:01Z in a
scratch clone of the lane at the tip; the lane's gates were not executed (§Gate standard, Closure consequence).

Driver digest (copied from `.ufo/watchdog.log`):

```
2026-10-22T12:48:39-03:00 launch kotoba round=52 pgid=3875350 driver=hyaku-inline attempt=1
2026-10-22T14:30:02-03:00 lane-dead-no-report kotoba round=52; retry same round (hyaku-inline attempt=1: omp process restart at 17:26Z; no landed report; fresh successor inherits work)
2026-10-22T14:30:04-03:00 launch kotoba round=52 pgid=1002393 driver=hyaku-inline attempt=2
2026-10-22T15:56:52-03:00 complete kotoba round=52; hyaku-inline attempt=2
```

## 1. Conformance (step 1)

| check | command | observed | result |
|---|---|---|---|
| report author | `git log --format='%an %H' -- .ufo/reports/round-52/kotoba.md` | `kotoba-shokunin 251d0b80…`, `kotoba-shokunin 27b2a3f7…` | pass |
| SHONEN heading | report `## SHONEN` | 4 lines, one per box, each with an evidence pointer | pass |
| cited hashes | `merge-base --is-ancestor <h> master` for `4c003a4b c2107ecf c8407a45 a44196d8 0c9180a6 c8579a4c` | all ancestors; all five round commits authored `kotoba-shokunin` | pass |
| pushed | `jj-lane.sh state` | `local=remote=0c9180a6… ahead=0 behind=0 tracked=0 untracked=0`; `ls-remote` = `0c9180a6…` | pass |
| leftovers | `git status --porcelain` (lane) | empty | pass |
| prompt contract | `.ufo/prompts/kotoba-round-52.md` vs `templates/round-prompt.md` | §§1–5 byte-exact modulo lane/round/root; hyaku §6 addendum present; no L2 route map quoted; committed (`b144bf2`, `0697c2b`) | pass |
| frozen counters | `git diff 4c003a4b 0c9180a6 -- verifiers/check_callee_rename.py verifiers/check_mcp_instructions.py` | empty | pass |
| SOURCES append-only | `git diff c8579a4c 0c9180a6 -- corpus/SOURCES.md \| grep '^-\|'` | no removed row | pass |

Conformance defect (status-neutral): the plan's wave shape (`plans/round-52.md`: build wave 32–40 seats, then a falsify
wave only if the build yields ≥32 attack items) did not run. The build was L1-inline with no grant (M37), and the only
wave was a 34-seat falsify wave in attempt 2. This is disclosed in the report and in LOG.md:2432, and was forced by capacity.

## 2. Claims (re-measured on committed bytes with the frozen counters; scratch clone at the tip)

**C1 — freshness.** Declared: `callee-rename robust 0 of 4 fixtures` → `4 of 4`.

```
python3 -B verifiers/check_callee_rename.py --rev c8579a4c   → callee-rename robust 0 of 4 fixtures, exit 1
python3 -B verifiers/check_callee_rename.py --rev 4c003a4b   → 0 of 4
python3 -B verifiers/check_callee_rename.py --rev c2107ecf   → 4 of 4
python3 -B verifiers/check_callee_rename.py --rev 0c9180a6   → 4 of 4, exit 0; --seed 7 → 4 of 4, exit 0; --seed 1234 → 4 of 4, exit 0
```

**Re-measured; verified as declared.**

**C2 — coverage (learning claim, sourced claim).** Declared: `mcp instructions backed 0 of 7 clients` → at least
`3 of 7`, exit 0, and `--fetch` finds at least 3.

```
python3 -B verifiers/check_mcp_instructions.py --rev c8579a4c          → backed 0 of 7, exit 1
python3 -B verifiers/check_mcp_instructions.py --rev c8407a45 --fetch  → backed 5 of 7; found on the live page 5 of 5, exit 0
python3 -B verifiers/check_mcp_instructions.py --rev 0c9180a6          → backed 7 of 7
```

**Re-measured; verified as declared.** Ruling: only the declared target counts. That target is "at least 3", and the
declared after-state is 5 of 7 at `c8407a45`, which meets it. The 7 of 7 at the tip comes from the same frozen counter
(the diff is empty) after S041 and S042 were added. It is a second measurement on unchanged tables, so it neither widens
nor replaces the claim. It is credited as a quality correction (M38), not as the claim. This is not the round-51 failure
mode, where the counter was widened after the plan. The part the counter does not measure (whether each quote says what
its `reading` cell says) is checked in §4 for S035, S041 and S042: agree.

No-harm: `git diff c8579a4c 0c9180a6 -- SCORECARD.md` shows no score change on any axis. Score cells: depth 9,
consistency 10, coverage 8.5, operability 8.5, freshness 8, calibration 8.5, adjacency 8.0. Row texts were rewritten:
the depth lead was corrected (round-51 routed defect 2), and the coverage and freshness rows gained round-52 leads. The
rest of the no-harm check was verified from committed evidence, without running any gate.
`.ufo/waves/round-52/falsify-a2/ExecGateMatrix.md` covers 17 lane gates at base and head: no gate goes from exit 0 to
nonzero, and every red row at head is red at base. The only self-test change is a rise: `surfaces` 119 → 129.
`git show 0c9180a6:verifiers/floors-registry.json` gives floor 129. `verify_corpus_integrity` is 5 of 9 at both base and
head, but the DRIFT set changed: `unindexed` was fixed, and `commit_total` is new because the baseline was not re-recorded.

Host-drift ruling: not harm. The reported change (opencode 1.19.3 → 1.19.4 at 17:50:30Z) is corroborated by a reviewer
seat: the npx `opencode.exe` mtime is `14:50:30 -0300`, `package.json` says 1.19.4, and `opencode --version` prints 1.19.4.
Per ExecGateMatrix, the plan's guards (`verify_surfaces.py --json` pass 7; `check_substrate_pins.py` OK 3/3) now read pass
6 (`surfaces.opencode_extract` FAIL) and DRIFT 1/3 at base and head alike, and the committed-fixture control is still pass
7 on both revisions. The lane did not cause this. It is a red gate routed to its owner (§Gate standard, Closure
consequence) and changes no status.

Swarm-total ruling: 34 seats, upheld. Neither attempt-1 wave had a grant: `build-gate.txt` and `falsify-gate.txt` are
0 bytes, both registries list members with `agentId: null` (34 and 36), and the attempt-1 L1 transcript contains no
`task` call and no subagent transcripts. The attempt-2 L1 has 34 seat transcripts, and 34 reports are committed under
`falsify-a2/`, with the gate line `granted … seats=34 live=50`. The build was L1-inline, so it adds no seats.

## 3. Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| freshness | improved | C1 re-measured 0 → 4 of 4 (three seeds) |
| coverage | improved | C2 re-measured 0 → 5 of 7 declared (≥3); `--fetch` 5 of 5 |
| depth, consistency, operability, calibration, adjacency | unchanged | no score cell moved; ExecGateMatrix shows no exit flip |

## 4. Discernment spot-check (`corpus/lessons/round-52.md` § Gate)

| item | decision | re-opened source (2026-10-22 ~18:59Z) | agree/disagree | reason |
|---|---|---|---|---|
| S035 Codex | admit | https://developers.openai.com/codex/mcp.md — 200, 26,995 B, sha256 `c78df8c7…` (= Gate) | agree | `:197` carries the quote verbatim; it is vendor docs (tier A), and the reading cell matches |
| S041 opencode | admit (attempt 2) | raw `anomalyco/opencode@cdf1c200…/mcp-servers.mdx` — 200, 15,476 B, sha256 `fd3b05ea…` (= Gate) | agree | `:429` is verbatim; `:431-437` has the `<mcp_instructions>` block and `:441` the deny-all omission, as the row's `teaches` and the entry's reading say |
| S042 Copilot CLI | admit (attempt 2) | raw `github/copilot-cli@7ea98dfc…/changelog.md` — 200, 289,859 B, sha256 `c4b793bd…` (= Gate) | agree | `:1157` and `:2895` are verbatim under § 1.0.66 and § 0.0.400 |
| opencode (old docs path) | reject | https://opencode.ai/docs/mcp-servers.md (13,941 B, `12ed2af6c5f4…`) and raw `sst/opencode/dev/…/mcp-servers.mdx` (14,015 B, `ad6e6687ab4c…`) | agree on the page, disagree on the client verdict | the hashes match the Gate record and `grep -ci instructions` gives 0 on both, so these pages are correctly not admitted. The client-level "silent" verdict was a false negative, which the lane already corrected (S041, M38) |
| Copilot CLI (add-mcp-servers) | reject | https://docs.github.com/…/add-mcp-servers.md (14,240 B, `640035aa0936…`) | agree on the page, disagree on the client verdict | the one `instructions` hit (`:22`) is about installation instructions; the client verdict was a false negative, corrected by S042 (M38) |

SOURCES row re-opened: S042. Its `teaches` cell quotes "to optionally include instructions from all MCP servers in
system prompts" (11 words, at most 25), and that text is verbatim at `changelog.md:1157`. Agree.

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → `W04 S018`, `W04 S019`,
`W04 S021` (duplicate URL across scopes, carried), then `kotoba ok`, exit 0. Row count (the report's awk): 31 @ `c8579a4c` → 38 @
`c8407a45` → 42 @ `a44196d8` = 42 @ tip.

## 5. Trend verdicts

- **expansion: improved.** `git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'` goes from 38 to 39.
  SOURCES grows from 31 to 42 rows, and the MCP server `instructions` item moved to PROVINCE Core.
- **quality: improved.** Two stale rows are superseded with fresh located quotes (S038 → S031, S039 → S024). Round-51
  routed defects 1 and 2 are corrected, and a sweep check now pins them and can fail (`check_correction_sweep.py`
  exit 1 @ base per the report and ExecGateMatrix; evidence-verified, not executed here). The two false negatives were
  corrected inside the round.
- **discernment: unchanged.** All 3 sampled admits agree. Both sampled rejects are correct at page level but were
  false negatives at client level. The lane's own falsify wave caught them, not the lane's first-pass judgment.

## 6. Routed defects (the lane fixes these next round)

1. Re-derive and re-pin opencode 1.19.4 (`surfaces.opencode_extract` FAIL; `check_substrate_pins.py` DRIFT 1/3), which is host drift since 17:50:30Z.
2. Re-record the `verify_corpus_integrity` baseline (`commit_total` DRIFT is new at head; the gate is 5 of 9).
3. Add a self-test arm for each of the two attempt-2 C1 fixes in `verify_surfaces.py` (unresolved-group admission and the empty-baseline fallback). Both are untested today.
4. Tighten the C2 counter class: the loose host pins and the substring Gate rule (`MutMcpCounter` M12, M16 survived) apply to the next counter written.
5. The drift sentinel trips: "a record wider than what was verified" recurred in rounds 50, 51 and 52 (M39, M40). Round 53 must work a different frontier area, as the lane's own SCORECARD "Next" block says.
6. The C2 sweep missed opencode and Copilot CLI (M38). Before an absence is recorded, Q30 must also open changelogs and the current docs-source path.

SHONEN: all four boxes remain `[~]` with pointers. Box 4 has fresh non-author-checkable evidence (`ConnSiblingOverlap`).
Boxes 2 and 3 still lack a fresh non-author run, so not all four are checkable by a non-author. Promotion is operator-owned.
