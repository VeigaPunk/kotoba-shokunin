# ScoutSiblingOverlap

role: connector (leaf — no subagent dispatch)
item: sibling-overlap scan of round-66 G9 citation semantics and repo-context corpus integrity against `PROVINCE.md`
judged on: coverage
tools installed: none (python3 stdlib and git; pacman paused, no install required)
production edits: none

Axes named: **coverage** (this seat). The bound below must not move **depth** (C1 G9 `clause_need`, 240 assertions) or **consistency/calibration** (C2 routed 2 of 2 and the pinned count vector). **Adjacency** is the report-don't-absorb rule the scan applies (`AXES.md:16`); it is not a round-66 claim.

## Revisions

- Pinned plan base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (`plans/round-66.md:3`). `git merge-base --is-ancestor` of that base into HEAD exits 0.
- Measured tip for this scan: `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (lane HEAD). That commit is the integrator spot-check on top of `9e75e7345574af59d0585429a0f25b6179aa375d`. The spot-check lesson still names `9e75e734` as the pre-spot-check tip (`corpus/lessons/round-66-verifier-spotcheck.md:12-13`). Do not treat HEAD as the pinned base.
- Worktree at scan time was dirty outside this file: `M .ufo/waves/round-66/w1/swarm-registry.json`, untracked `ScoutCorpusCount.md` and `ScoutS122Reopen.md`. Not touched.
- `git diff --name-only 11385e04 HEAD` is 41 lane-relative paths (r65 registries, round-66 controls/receipts, `verifiers/check_scoped_rules_v32.py`, both integrity verifiers, the C2 knowledge entry, lesson, plan, scorecard). No path leaves `kotoba-shokunin`.

## Scan

Live tree, read-only, 2026-10-24. Not the round-49 census pins and not the round-63 37-file bound. Home lane excluded. `aggregator-shokunin` is not a directory under `/home/vgpnk/Projects/shokunin` (`ABSENT`).

```text
LANE_COUNT 20
SIBLING_FILES 38
MISSING
audio-shokunin/SKILL.md
game-dev-2d-shokunin/SKILL.md
aggregator-shokunin: ABSENT
```

Lanes: audio, chousa, game-dev-2d, game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kengaku, kotodama, kumitate, lore, mado, mori, revenger, souji, tabi, tameshi, tsukuroi. Revenger now has `SKILL.md` (the round-63 scan's third missing file). Audio and game-dev-2d remain seed-form provinces only.

Strict hit = an `**Owns:**` / `**Domain:**` / `**Refuses:**` line, or a province boundary-table cell, that claims either (1) G9 one-content-word / compound-clause support on a scoped-rule Action cell or (2) lane-corpus commit resolution by a lane-then-fleet `git cat-file` lookup or code-span meta-finding exclusion. A string hit that is not that claim is not strict.

Pattern swept on all 38 files: `G9`, `g9_conjunct`, `compound-clause`, `one-content-word`, `one-word tail`, `clause_need`, `MIN_CLAUSE`, `cited line`, `forward-support`, `fleet-root`, `commit_resolves`, `repository context`, `corpus integrity`, `code-span`, `inside_code_span`, `cat-file`, `software citation`, `commit reference`.

```text
NEAREST_COUNT 45
STRICT_HITS 0
```

The 45 nearest lines are other lanes' own gates (cited-line range checks, host drift pins, `cat-file blob`, RE merge-base, fleet-root disk/census/hygiene flags). None is an Owns/Domain/Refuses claim on either round-66 item. Audio and game-dev-2d `PROVINCE.md` produced no nearest line.

## What the two items actually touch

**G9 (C1, depth).** `g9_conjunct` takes `(lines, cell, L, page_text)` and compares content words (`verifiers/check_scoped_rules_v32.py:1116-1152`). `clause_need` caps the shared-word floor by clause length (`:1072-1074`). No path is opened. `LANE_FALLBACK` is `kotoba-shokunin` only (`:320`). Kotoba `PROVINCE.md:27` already puts compound-clause citation on this lane's scoped-rule Action cells in Core and records the round-63 bound (strict hits 0). The one-word coupling is a floor change inside that instrument, not a new surface and not a sibling file.

**Repo-context integrity (C2).** `commit_resolves` runs `git cat-file -e <id>^{commit}` on the lane repo, then on `FLEET_ROOT = Path("/home/vgpnk/Projects/shokunin")` (`verifiers/verify_corpus_integrity.py:125`, `:591-603`). `iterdir` count in that file is 0. The word `sibling` there is the round-11 excluded prose shape `` `../sibling/SKILL.md` `` (`:54-55`, `:750`), not a repository walk. The independent gate uses the same two roots (`verifiers/verify_corpus_independent.py:44`, `:487-491`).

The three tokens named in `.ufo/waves/round-66/receipts/C2-independent-before.txt:6`:

| token | where cited | lane `cat-file -t` | fleet `cat-file -t` | how round 66 treats it |
|---|---|---|---|---|
| `451a02ff` | `corpus/lessons/round-54-verifier-spotcheck.md:147` nested `` `commit `451a02ff` `` | fatal, not an object | fatal, not an object | `inside_code_span` context, not a live citation |
| `def4b9fffbf59e9e121b89ef73fbeb89426bd614` | `corpus/lessons/round-62-verifier-spotcheck.md:13` "fleet commit" of the round-62 report | fatal | `commit` | fleet-root fallback |
| `7b370d54bd0e74eef4aa90b2e8b2fc9736b3d39f` | `corpus/lessons/round-65-verifier-spotcheck.md:11` "fleet commit" of the round-65 report | fatal | `commit` | fleet-root fallback |

No sibling object database is consulted. The two resolved objects are parent-fleet report commits. The third is absent from both declared repositories and is excluded as a code span.

## Verdict

**STRICT_HITS 0.** Neither item crosses a sibling boundary as an owned province.

Kotoba's own map agrees for G9 and does not yet name the fleet hop:

- `PROVINCE.md:27` — Core, this lane's Action cells, round-63 sibling bound attached.
- `PROVINCE.md:49` — chousa is `adjacent`: kotoba cites the research method, never re-derives it.
- `PROVINCE.md:59` — kumitate routes "Prompt and skill craft → kotoba"; kotoba does not own the runtime.
- `PROVINCE.md:64` — souji is `none`: fleet repository hygiene, no split on scope surfaces.
- `PROVINCE.md:66` — tameshi is `adjacent`: fixture and mutation method; every lane's gate remains its own.
- `AGENTS.md:3` — work only inside this repo and `PROVINCE.md`.

## Contested scope (named, not closed)

These share words with the round-66 work. They are not strict hits. No arbitrator is appointed here.

1. **chousa hop vs this gate's "hop".** `chousa-shokunin/PROVINCE.md:5-6` owns "citation chaining and hop resolution; claim-vs-source verification" as research method. `chousa-shokunin/SKILL.md:19` defines the hop: "follow each hop to the cited artifact and resolve its anchor there." `verify_corpus_integrity.py:594` calls the fleet fallback "the report-pointer hop's commit analogue." Same word, different operation: research anchor chain versus `git cat-file -e` on one parent repository. `corpus/knowledge/fleet-commit-resolution-round66.md:9` already says the gate is local evidence integrity, not research citation policy. Reading chousa's sentence as owning D2 would re-derive the research method, which `PROVINCE.md:49` forbids. Contested at the word only.

2. **souji fleet-root hygiene vs a fleet `cat-file` read.** `souji-shokunin/PROVINCE.md:3-9` owns stray checkpoint/scratch files, quarantine, and dry-run removal lists. `souji-shokunin/SKILL.md:90-92` classifies fleet-root commits that land checkpoint blobs, for removal receipts. The resolver does not add, delete, or classify fleet files. It is still a read outside the lane checkout, which `AGENTS.md:3` does not mention. That is a lane-rule tension, not a souji Owns claim on citation integrity. Contested as a read of souji's work surface, not as absorption of the hygiene craft.

3. **Nearest, already refused by the sibling.** `tameshi-shokunin/PROVINCE.md:14-15` keeps every lane's gate its own; C1's kill arms mutate kotoba's self-test, not tameshi's method. `kengaku-shokunin/SKILL.md:3` keeps measured capability effects and leaves prompt/skill craft to kotoba; C2's calibration sub-axis is the lane scorecard, not eval calibration. `kumitate-shokunin/PROVINCE.md:27` routes prompt and skill craft to kotoba; D1's blobs are `.ufo/waves/round-65/{w1,w2}/swarm-registry.json` inside this lane, not the ufo-fsd runtime. `kama-shokunin/SKILL.md:420` (`git cat-file blob`) and `kaidoku-shokunin/SKILL.md:790` (merge-base/cat-file for RE custody) are those lanes' own comparators.

## Contradiction (not smoothed)

- Round-63 `PROVINCE.md:27` says strict hits 0 on 37 files. This scan is 38 files because `revenger-shokunin/SKILL.md` now exists. The older sentence is not this measurement. Both negatives can stand; they are not one count.
- The integrity comment says "hop" and chousa owns "hop resolution." Collapsing those into "no overlap" would hide the word collision. The operations differ, as cited above.
- `AGENTS.md:3` says stay in this repo. `commit_resolves` reads a second git directory. The read is the fleet root, not a `*-shokunin` sibling. It does not write.

## Proposed move (not applied)

One sentence, appended to the existing paragraph in `corpus/knowledge/fleet-commit-resolution-round66.md` (the file is already tracked; do not add a corpus file). Do not edit `clause_need`, `commit_resolves`, `PROVINCE.md:27`, the 240-assertion suite, or the 2-of-2 counter.

```text
Allowed repositories stay the lane checkout and the fleet root only; a sibling `*-shokunin` object database is not a third lookup. Chousa's hop follows a research citation to an anchor; this gate only tests `git cat-file -e <id>^{commit}`. Souji's fleet-root hygiene classifies stray files for removal; this gate does not write the fleet repository.
```

That names the non-overlap on the coverage surface the round already admits, without moving depth or calibration. It also blocks the widening (walk every sibling odb until a hash hits) that would cross the boundary this scan found clear.

## Risks

- Landing the sentence with a backticked `commit <hex>` or a `.ufo/reports/` token would move `commit_total` or `report_total` and harm the frozen C2 vector (`tracked_files` 118, `commit_total` 37, `commit_unresolvable` 0). The sentence above has neither.
- Editing `PROVINCE.md:27` to "clarify" G9 would reopen a bound the round-63 scan already closed and is not needed for the one-word floor.
- Treating souji's hygiene list as a veto on `cat-file -e` would force the two fleet report commits back to unresolved and reopen D2. The contest is to name the read, not to delete the fallback.
- Treating chousa's hop as the owner would re-derive research method inside a corpus gate.

## Verification (for the L1; not run as a production edit)

1. Re-run the 38-file sweep. Expect `STRICT_HITS 0`, `aggregator-shokunin: ABSENT`, missing `audio-shokunin/SKILL.md` and `game-dev-2d-shokunin/SKILL.md`.
2. Re-run the three `git -C <lane|fleet> cat-file -t` probes. Expect lane fatal/fatal/fatal and fleet fatal/`commit`/`commit` in the table order.
3. If the sentence is appended, `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` must still show tracked 118, unindexed 0, report_total 79, report_dead 0, commit_total 37, commit_unresolvable 0, commit_nonhash 0, and `check_r66_routed_repairs.py` must still print `2 of 2` at the tip and `0 of 2` at `11385e04`. Do not treat this report as that measurement.
