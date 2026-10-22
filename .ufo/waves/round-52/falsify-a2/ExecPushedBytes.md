Result: MIXED — The pushed master resolves to c8407a4 with the plan commit as ancestor and c8579a4c as base, and every frozen counter reproduces its claimed output from the pushed bytes alone (C1 4 of 4 exit 0, C2 5 of 7 exit 0, --fetch 5 of 5 exit 0, sweep red at base / green at head), but the pushed commit omits the round-52 scorecard credit (no `| 52 |` receipt rows, coverage/freshness axis rows still credit round 15 / round 51) and the pushed lesson cites a wave evidence file (`.ufo/waves/round-52/build-dispatch.json`) that is not in the pushed tree at all.

Seat: `KotobaR52a2.ExecPushedBytes` (executor, falsify-a2 wave).
Target: pushed bytes equal claimed bytes.
Scratch (never the lane): `/fast/scratch/hyaku/kotoba-r52a2/ExecPushedBytes/` — `remote/` (read-only clone of the remote), `base/` (checkout of the base rev), `mut/`, `mut2/`, `wt/` (copy of the lane working tree), `fetch/`.

---

## 1. Remote topology — HOLDS

Command (exit 0):

```
git clone -q https://github.com/VeigaPunk/kotoba-shokunin.git /fast/scratch/hyaku/kotoba-r52a2/ExecPushedBytes/remote
git -C .../remote rev-parse origin/master
```

```
c8407a453788df964df5a7b835dd0ce1360de882
```

`git ls-remote origin` (exit 0) gives the same sha for `HEAD` and `refs/heads/master`:

```
c8407a453788df964df5a7b835dd0ce1360de882	HEAD
c8407a453788df964df5a7b835dd0ce1360de882	refs/heads/master
```

Ancestry and base (exit 0 for both `git merge-base --is-ancestor`):

```
git merge-base --is-ancestor 4c003a4b9c7dae8ebb8ad34bbc14cd1706febeeb origin/master   # rc=0
git merge-base --is-ancestor c8579a4c5b48789e56fb9060ddd48f33569e1215 origin/master   # rc=0
git rev-parse 4c003a4b^                                                            # c8579a4c5b48789e56fb9060ddd48f33569e1215
git rev-list --count c8579a4c..origin/master                                        # 3
```

So the remote master is exactly the judged revision named in the context, the plan commit `4c003a4b` is its ancestor, and `c8579a4c` is its base (the plan commit's own parent). The three commits above the base are exactly the plan, C1 (`c2107ec`), and C2+repairs (`c8407a4`).

Pushed tree == local committed tree (exit 0):

```
git rev-parse c8407a4^{tree}                       # 3f9fecdaa692f4ffa2041aedfbb743de8f294bad
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD^{tree}   # 3f9fecdaa692f4ffa2041aedfbb743de8f294bad
```

The remote clone is clean (`git status --porcelain` empty) and its `master` == `origin/master` == `HEAD` == `c8407a4`.

Frozen-counter integrity — the counters are byte-identical between the plan commit and the head, so nothing was widened after the freeze (exit 0):

```
git rev-parse 4c003a4b:verifiers/check_callee_rename.py   # f50297fb4ffb1a9003e01714f33b642586504a20
git rev-parse c8407a4:verifiers/check_callee_rename.py     # f50297fb4ffb1a9003e01714f33b642586504a20
git rev-parse 4c003a4b:verifiers/check_mcp_instructions.py # 0023d8f5bbde69dece1cdeae568c5d6a4da35551
git rev-parse c8407a4:verifiers/check_mcp_instructions.py  # 0023d8f5bbde69dece1cdeae568c5d6a4da35551
```

`check_correction_sweep.py` is new at `c8407a4` (absent at `4c003a4b`), which is the M36 fix the plan asked for; it is not a frozen plan counter.

## 2. Counter replay from the pushed bytes — HOLDS

All five commands run from the pushed clone, `python3 -B`, exit codes captured separately from the pipe:

| command (in `.../remote`) | last line(s) | exit |
|---|---|---|
| `verifiers/check_callee_rename.py --rev c8407a4` | `callee-rename robust 4 of 4 fixtures` | 0 |
| `verifiers/check_callee_rename.py --rev c8407a4 --seed 99` | `callee-rename robust 4 of 4 fixtures` | 0 |
| `verifiers/check_mcp_instructions.py --rev c8407a4` | `mcp instructions backed 5 of 7 clients` | 0 |
| `verifiers/check_mcp_instructions.py --rev c8407a4 --fetch` | `mcp instructions backed 5 of 7 clients` / `mcp instructions found on the live page 5 of 5` | 0 |
| `verifiers/check_correction_sweep.py --rev c8579a4c` | `FAIL r51-c2-readme corpus/README.md:119 …` / `FAIL r51-c2-scorecard-lead SCORECARD.md:28 …` / `FAIL r51-c2-province PROVINCE.md:17 …` / `correction sweep: 3 stale block(s)` | 1 |
| `verifiers/check_correction_sweep.py --rev c8407a4` | `correction sweep: 0 stale block(s)` | 0 |

Every claimed value in the context reproduces byte-for-byte from the pushed bytes: C1 `0 of 4` at base and plan → `4 of 4` at `c8407a4` (also with `--seed 99`, and with seeds 52/7/1234 at `c2107ec`), C2 `0 of 7` at base → `5 of 7` at `c8407a4` with `--fetch` `5 of 5`, and the M36 sweep red at base / green at head. No difference from the local results stated in the context — **no BREAK on the replay**.

Supporting counter detail:

- `check_callee_rename.py` reads its fixtures from `FIXTURE_REV = "c8579a4c5b48789e56fb9060ddd48f33569e1215"` (`verifiers/check_callee_rename.py:61`), and the four fixture blobs are byte-identical between base and head (verified by `git rev-parse` per blob), so the C1 result is not an artifact of changed fixtures.
- `--fetch` was re-verified independently: I re-fetched the five admitted URLs at 2026-10-22T17:53:27Z–17:53:28Z and the recorded quotes are present on the live bytes (Claude Code quote at live line 1488, VS Code at 1114, spec at 463, Codex at 197, Gemini at 1315). The four rejection pages re-fetch at 18:14:13Z–18:14:14Z are byte-identical to the recorded digests (opencode 13,941 B `12ed2af6…`, mdx 14,015 B `ad6e6687…`, Copilot add-mcp-servers 14,240 B `640035aa…`, `context/mcp.md` 404 page 502 B), and `grep -ci instructions` on them gives 0/0/1 as recorded.

## 3. Findings against the pushed bytes

### F1 — MEDIUM. The pushed commit carries no round-52 scorecard credit.

`SCORECARD.md` at `c8407a4` (pushed) contains zero `| 52 |` receipt rows (`git show c8407a4:SCORECARD.md | grep -c "^| 52 |"` → `0`); the receipts table ends at round 51 (`SCORECARD.md:256-259`). The two axis rows the round claims are still credited to older rounds:

- `SCORECARD.md:30` — `| coverage | 8.5 — was 8.0 | **round 15 — re-measure of round 14's landed move …`
- `SCORECARD.md:32` — `| freshness (advisory) | 8 | **round 51 (C1 — omp 18.12.6 re-derived and re-pinned …`

and `SCORECARD.md:126` still reads `**Next: round 52** — re-measure every before-value first (Q19)`. The pushed `LOG.md` likewise has no round-52 section (`git show c8407a4:LOG.md | grep -c -i "round.52"` → `0`), while the pushed `corpus/README.md:79` index row for "Round-52 lessons" claims a "LOG.md round-52 entry" and the pushed `corpus/lessons/round-52.md:4` says "LOG.md § Round 52". So a reader of the pushed tree finds a round-52 lesson, a round-52 SOURCES block (S032–S038), a round-52 SKILL.md table, and round-52 PROVINCE rows — but no scorecard receipt and no LOG entry for the round.

Impact on the judged axes: the coverage and freshness scores a judge reads off the pushed `SCORECARD.md` (`coverage 8.5 — round 15`, `freshness 8 — round 51`) do not reflect the round-52 work at all. The round-52 numbers exist only in the lane's uncommitted working tree (the attempt-1 L1's leftover `SCORECARD.md` diff, which adds exactly the `| 52 | freshness |` / `| 52 | coverage |` rows and a "Round 52 completed" paragraph). Not in the pushed bytes.

### F2 — MEDIUM. The pushed lesson cites a wave-evidence file that the pushed tree does not contain.

`corpus/lessons/round-52.md:11` (M37) cites `.ufo/waves/round-52/build-dispatch.json` as the evidence for the seat-gate and route-outage event. `git ls-tree -r --name-only c8407a4 -- .ufo/waves/round-52/` returns **0 files**; the whole `.ufo/waves/round-52/` tree is untracked in the lane (`git status --porcelain` → `?? .ufo/waves/round-52/`). By contrast the previous round's wave evidence is fully committed (`.ufo/waves/round-51/` → 81 tracked files at `c8407a4`). The pushed lesson's own text also says the fetched copies "are scratch, not evidence; the values above are the record" (`corpus/lessons/round-52.md:42-43`), which is fine for the source digests, but M37's evidence pointer is a claim that a reader of the pushed tree cannot follow at all.

### F3 — LOW/MEDIUM. Two of the seven admitted source pages have already drifted from the recorded digests.

Recorded in the pushed lesson (`corpus/lessons/round-52.md:20-25`) and `corpus/SOURCES.md:46-47`, re-fetched live at 2026-10-22T17:53:27Z–17:53:28Z:

| row | recorded (lesson) | live now (2026-10-22T17:53Z) | delta |
|---|---|---|---|
| S033 code.claude.com/docs/en/mcp.md | 127,022 B, sha256 `9a42e98f…` | 128,298 B, sha256 `9ec4942d…` | +1,276 B; a new section "Mark tools that are safe to call twice" inserted at line 1408, pushing the quoted line 1468 → 1488 |
| S034 code.visualstudio.com/updates/v1_104 | 179,440 B, sha256 `19d9259e…` | 179,457 B, sha256 `ee92f645…` | +17 B; one `awa-expId` A/B meta tag |

The other five (S032, S035, S036, S037, S038) and the four rejection pages were byte-identical on re-fetch. Both quotes themselves still verify on the live bytes, so the C2 counter is unaffected; but the pinned digest/line anchors for S033 and S034 no longer reproduce against the live pages, and the pushed SOURCES anchor text for S033 (`mcp.md:1468`) no longer names the quote's live line. A second S033 re-fetch at 18:37:15Z returned yet another digest (`4333de9d…`, 128,697 B), so that page is actively changing.

### F4 — LOW. The pushed SOURCES row for S038 does not record the row it supersedes in a machine-checkable field, and the pushed corpus still contains the superseded "7 of 7" phrasing the M36 sweep is supposed to police.

`corpus/SOURCES.md:51` (S038) supersedes S031 in prose ("supersedes S031 — …"), and the S031 row at `corpus/SOURCES.md:44` is unchanged. That matches the append-only rule and the lesson's "Rows touched (old → new): None of S001–S031 changed in place" (`corpus/lessons/round-52.md:62`), so this is compliant. The residual point: the stale phrase "overlap levers backed 7 of 7 clients" survives in the pushed tree at `corpus/README.md:153` and `PROVINCE.md:17`, and the sweep's registry only detects it because the *block* also carries "4 of 7" — i.e. the check is satisfied by a co-located token, not by a corrected claim.

### F5 — LOW. The M36 sweep's judgment table is satisfied by an unrelated "4 of 7" token (mutation-proven in my own scratch clone).

`verifiers/check_correction_sweep.py` matches a stale block by searching for the declared pattern `4 of 7` anywhere in the same block (`verifiers/check_correction_sweep.py:73-74`). Mutation, in `/fast/scratch/hyaku/kotoba-r52a2/ExecPushedBytes/mut` (scratch clone of the pushed tree, never the lane):

- **M2** — replace the entire real README correction block (`corpus/README.md:158-167`, which states the declared result and the corrected lever set) with the unrelated sentence `**Round 52 correction (append-only):** see the table 4 of 7 rows above.` → `python3 -B verifiers/check_correction_sweep.py --root .` prints `correction sweep: 0 stale block(s)`, exit 0. **The check passes with the substantive correction deleted.**
- **M1** — delete the README correction block outright → `FAIL r51-c2-readme corpus/README.md:133 stale claim without the declared result` / `correction sweep: 1 stale block(s)`, exit 1. So the check does still fail on total removal, but not on a hollow correction.

This is a real weakness in the M36 fix's strength (it can be satisfied by a token), not a falsification of its red-at-base/green-at-head result. The lesson's own M36 row and criterion Q29 (`corpus/QUALITY.md:40`) state the intent — "the superseded claim's stale phrase and its declared result go into the registry in the same commit as the correction, and the sweep must exit 0 before the round's report" — which the shipped pattern does satisfy; the gap is that the pattern does not require the *declared result to be stated as a correction of that stale claim*.

### F6 — INFO. Host substrate drift makes two plan no-harm guards red on the pushed bytes, independently of the round.

`verifiers/check_substrate_pins.py` (exit 1) and `verifiers/verify_surfaces.py --json` (exit 1, `pass 6 fail 1`, `surfaces.opencode_extract` FAIL) are red on the pushed tree *and* identically red at the base checkout in my scratch `base/` clone. Cause: the installed opencode moved 1.19.3 → 1.19.4 (`package.json` version `1.19.4`, binary sha256 `538fcb1b…`, mtime 2026-10-22T17:50:30Z), while `verifiers/baseline.json:10` pins `179ca421…`. This is host drift, not a round-52 regression; the plan's C1 no-harm guard "stays `OK 3/3`" cannot be re-measured on this host today. Recorded so the L1's no-harm matrix does not attribute it to the round.

### F7 — INFO. Corpus census drift is unchanged by the round, but the pushed commit adds two corpus files without a baseline re-record.

`verifiers/verify_corpus_integrity.py` on the pushed tree (exit 1): `5/9 checks pass; DRIFT: corpus.index.tracked_files (observed 75 expected 72), corpus.pointers.report_total (47/46), corpus.pointers.report_dead (3/0), corpus.pointers.commit_total (31/30)`. At the base checkout the same gate reports `observed 73 expected 72` for tracked_files and the same three other drifts. The round adds two tracked corpus files (the entry and the lesson) without re-recording `verifiers/corpus-baseline.json` (last changed in round 51 at `59903b2`). The fleet-root census `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin` exits 0 with `kotoba ok`.

## 4. What I did not change

No lane file was edited; the only file I wrote is this report. The lane working tree moved during my run (other seats editing `SCORECARD.md`, `corpus/SOURCES.md`, `SKILL.md`, `PROVINCE.md`, `corpus/QUALITY.md`, `corpus/README.md`, the entry, the lesson, `verifiers/check_correction_sweep.py`, `verifiers/verify_surfaces.py`, and the 18.12.6 fixture) — those are the L1's/siblings' in-flight edits, not mine. I did not push, and I did not run any git write in the lane (read-only `git`/`jj --ignore-working-copy` only).

## 5. Suggested next actions (L1 owns these)

1. Land the scorecard credit with the rest: `SCORECARD.md` needs `| 52 | freshness |` and `| 52 | coverage |` receipt rows plus refreshed coverage/freshness axis rows, and `LOG.md` needs its round-52 section, before the round can be judged on coverage/freshness from the pushed tree (F1).
2. Commit the round-52 wave evidence (or drop the M37 pointer) so the pushed lesson's evidence is followable (F2).
3. Re-open S033/S034 to refresh the recorded digests and the `mcp.md:1468` anchor, or mark the rows as drift-prone (F3).
4. Harden the sweep's registry entry so the declared result must be phrased as a correction of the stale claim, not merely co-located (F5).

## 6. Sources opened (curl, no browser), with UTC access time, bytes and sha256

All fetched 2026-10-22 between 17:53Z and 18:37Z with `-A "kotoba-shokunin-counter/52"`; bodies saved under `/fast/scratch/hyaku/kotoba-r52a2/ExecPushedBytes/fetch/`.

| URL | UTC | bytes | sha256 |
|---|---|---|---|
| https://modelcontextprotocol.io/specification/2025-11-25/schema.md | 2026-10-22T17:53:27Z | 130,800 | `5ab7cfcd5ea05c7491637e76122362cc4416201ea0c81482f6747f59343f1691` |
| https://code.claude.com/docs/en/mcp.md | 2026-10-22T17:53:27Z | 128,298 | `9ec4942d35fba402f5c246303748d53d88852736d825862c0a5e0efc22266428` |
| https://code.claude.com/docs/en/mcp.md (re-fetch) | 2026-10-22T18:37:15Z | 128,697 | `4333de9d8b9e337bbc5594445a42f82336ca06ddbba271c8cc841fe828aa136c` |
| https://code.visualstudio.com/updates/v1_104 | 2026-10-22T17:53:28Z | 179,457 | `ee92f6454fb1e19ad9c85e605ee490a4128c8aeb3c672ec400f6c3c18b256e59` |
| https://developers.openai.com/codex/mcp.md | 2026-10-22T17:53:28Z | 26,995 | `c78df8c70b7f31f73557f77ad4208ff97656808fb423e6f4eb81151f8b009284` |
| https://geminicli.com/docs/tools/mcp-server.md | 2026-10-22T17:53:28Z | 43,656 | `4aefc4dc30c329cbbd16ca24fe294fb0d91ec87e8f61baca7116c19b6a1a14fd` |
| https://blog.modelcontextprotocol.io/posts/2025-11-03-using-server-instructions/ | 2026-10-22T17:53:28Z | 49,781 | `96794ff9735768eacfe54e3cf6d2de5493f5fab4b2deed54feae99aaaa72e050` |
| https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md | 2026-10-22T17:53:28Z | 461,944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` |
| https://opencode.ai/docs/mcp-servers.md | 2026-10-22T18:14:13Z | 13,941 | `12ed2af6c5f48701160ab6e1abe79fedbe293e55c5889c447be57ff79cd14de0` |
| https://raw.githubusercontent.com/sst/opencode/dev/packages/web/src/content/docs/mcp-servers.mdx | 2026-10-22T18:14:14Z | 14,015 | `ad6e6687ab4c8b535471ff176957fc7623b5f06230efc848b854c5c96acd70f5` |
| https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers.md | 2026-10-22T18:14:14Z | 14,240 | `640035aa0936ffb83ee8dd7034370019224c43cf03ee9560103a3a9cd190433b` |
| https://docs.github.com/en/copilot/concepts/context/mcp.md | 2026-10-22T18:14:14Z | 502 (404) | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |
| https://code.visualstudio.com/updates/v1_104.md | 2026-10-22T18:21:44Z | 19,510 (404) | `3c7efcaf106cf4615272e49727c964bc5d1888860dff2fff4cd33eb6c54c5e95` |

No tool installs were performed by this seat; nothing was needed for the checks above (git, python3, curl, sha256sum were already present).
