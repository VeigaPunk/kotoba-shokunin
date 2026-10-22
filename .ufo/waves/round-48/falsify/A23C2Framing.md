# A23C2Framing — round 48 falsify: the C2 records (SCORECARD depth row, LOG C2 bullet)

Seat `KotobaR48.A23C2Framing` (leaf critic, no delegation). Target: committed `84b9c9b` — `SCORECARD.md:28`, the first bold
"round 48" clause, and `LOG.md:2350`, the C2 bullet. The lane working copy has uncommitted edits to `SCORECARD.md` (in the move log only; the depth row is byte-equal to HEAD), `corpus/QUALITY.md` and the lesson. I judged the committed bytes.
Private clone: `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A23C2Framing/clone`, with worktrees `wt-75f671b` and `wt-d1ae458`.

## Verdict

**DEFECT (MEDIUM).** Every number in both records re-derives exactly. "Does not resolve routed defect 1" is honest, and "depth holds 9" is honest. But the records omit three facts that the round had or could cheaply get, and each one changes how the move reads:
1. **A new run-abort class introduced by the fix, not recorded.** This is harm under Q05.
2. **The singular-root hazard was dropped.** The build critic proposed it, and I reproduced it.
3. **The live disagreement on the routed row is now 10 versus 12, with a second cause that is not named.** The "Not claimed" list omits that cause's root. Q21 asks for a re-measure of the cause, and the records do not carry one.

A fourth issue is framing only: the nested "discriminator" pins behaviour that the round's own S016 source contradicts.
"improved-bounded" fits Q01 as a label. It is not "harm none" until finding 1 is repaired or recorded.

## Re-derivation (all exact)

| Record value | Re-derived | Command / evidence |
|---|---|---|
| ruler `01af33a6…` | `01af33a6724c…` | `git show 84b9c9b:.ufo/round-48/tools/config-root-ruler.py \| sha256sum` |
| oracle `1d09a38c…` | `1d09a38ce04d…` | `sha256sum .ufo/round-48/oracle/config-root-cases.json` |
| before receipt `8bec447a…` @ `197b5a4` | `8bec447aa538…`, `revision` `197b5a40…` | sha256sum + JSON `revision` field |
| consumer same at `197b5a4`/`c0185da`/`75f671b` | `872993f8…` ×3; `d1ae458` = `d67b1b6e…` | `git show <rev>:verifiers/verify_harness_independent.py \| sha256sum` |
| target failures 5 → 0, ruler exit 1 → 0 | base **exit 1**, `failed`, 5 failures; landed **exit 0**, `clean`, 0 failures, 0 mismatches, 0 errors | ruler run from the committed bytes (`$S/ruler.py`), base without baseline and landed with `--baseline-receipt …/before-configured-root.json --baseline-sha256 8bec447a…`; scratch `$S/ruler-{base,landed}` |
| 0 non-target value/status changes | my receipts equal the committed before/after receipts on `checks`, `statuses`, `observed_count` and `exit` in 13/13 cases each. `stdout_sha256` differs in 13/13 cases because outputs embed scratch paths. | Python diff of the receipts |
| self-test 104 → 115 | `0 failure(s) over 104 assertions` (exit 0) → `… over 115 assertions` (exit 0) | `python3 -B verifiers/verify_harness_independent.py --self-test` in each worktree |
| floor 104 → 115 | `check_assertion_floors.py` exit 0, 9 PASS, `harness_independent observed=115 floor=115` | worktree `wt-d1ae458` |
| arm kills the recursive mutant | `rglob("SKILL.md")` + `parent.name` mutant: exit 1, `6 failure(s) over 115 assertions` (all 6 are round-48 arms) | copy `$S/mut`, one edit in `derive()` |
| "both configured roots absent, live row unchanged" | `~/.config/opencode/{skill,skills}`: ENOENT. Live IND row 10 at base and at landed, all 28 values identical | `verify_harness_independent.py --json --catalogue-carrier <empty dir>` in both worktrees, exit 0 |

The receipts do not record the ruler's exit code. Exit 1 and exit 0 follow from the ruler's code (`return … 1 if failed …`, `:328`) and from my runs.

## Findings

**F1 — Harm: an unreadable configured root now aborts the whole instrument (MEDIUM, fixable).** I materialized one ruler case with
`--oc-config/skills` mode 000 (`$S/unreadable_probe.py`, sha256 `f94cc170…`):
base `75f671b` exit 0, row 2, all 28 rows published; landed `d1ae458` **exit 2**,
`SUBSTRATE [Errno 13] Permission denied: …/.config/opencode/skills`, no rows.
The frozen contract says "Enumerate **readable** direct child SKILL.md files" (oracle `contract.new_behavior`), but `derive()` calls `path.iterdir()` on every configured root, with no readability guard. The exit-2 path already existed for log-named roots, because the same loop is used, but at base an unlogged configured root was never touched. C2 extends that class to a new input. Q05 says "a new crash class introduced by the fix is harm".
The depth row disclaims only "full no-harm" in general. It names no measured harm. The uncommitted working-copy "Next: round 49" line mentions this exit 2, which shows a sibling found it too, but no committed record carries it.

**F2 — The singular-root hazard is missing (MEDIUM, wording).** `C1ClaimCritic.md` F2 proposed this row text: "Known hazard: the producer counts only the plural configured root … can now cancel the built-in +1 and make this row agree by coincidence". The landed row drops it.
I reproduced the hazard (`$S/join_probe.py`, sha256 `90adea29…`). The producer is `verify_harness_claims.oc_observations` with HOME set to the fixture. Its roots are `~/.agents/skills`, `~/.config/opencode/skills` and `~/.claude/skills` (`:472`).
- Unlogged `skill/zeta` **with** the marker: producer 3, IND base 2, IND landed **3**. The row moves from disagree to **agree**. Upstream-faithful is 4, so both sides are wrong and agree by coincidence.
- Unlogged `skill/zeta` **without** the marker: producer 2, IND base 2, IND landed 3. The row moves from agree to **disagree**, a new red. The landed value equals upstream, so this red is a real producer gap that is now exposed.
- Nested `skills/group/eta`: producer, base and landed all read 2 (no marker) or 3/2/2 (marker). Upstream reads 3 or 4.

**F3 — The routed row's live gap is 2, not 1, and the second cause is unnamed (MEDIUM, Q21).** Live producer `roots_plus_builtin` = **12**: 10 agents names, plus `kimi-webbridge` from `~/.claude/skills` (directory mtime 2026-10-22T02:36Z, during the round), plus marker 1. Live IND = 10.
`C1NoHarmBattery.md`, as committed in `84b9c9b`, already shows `oc.roots.names_plus_builtin (expected 10, observed 12)`. The records still say only "the round-47 join drop is the producer's `customize-opencode` byte probe". That is true for round 47's 10 → 11 (`.ufo/waves/round-47/falsify/W2DepthNoHarm.md:177`), but it is not today's decomposition.
Upstream loads `~/.claude/skills/**`: I re-opened the source (see below). The "Not claimed" list names recursion, `skills.paths`/`skills.urls` and frontmatter identity. It omits the external `~/.claude`/`~/.agents` pattern and multiple config directories, and the first of those drives the live gap today. Q21 asks the record to "re-measure that cause". The round measured it in a build report but did not carry it into the C2 records.

**F4 — "a nested-skill discriminator kills the recursive mutant" (LOW, framing).** The arm asserts "a nested skill is not a name". The round's own tier-A source S016 says opencode scans `{skill,skills}/**/SKILL.md`, so the "mutant" is the behaviour that matches upstream. The row does disclose "Not claimed: recursive … parity". Even so, calling the arm a discriminator that kills a mutant presents a pinned divergence as a strength. A future parity fix must invert 6 of these assertions (F-mutant output above).

**No overclaim found on:** resolving defect 1 (explicitly denied in the row; in the LOG it is denied in the bullet before the C2 bullet and in the title); loader parity (denied); no-harm (scoped to the 13 synthetic cases; "full no-harm" disclaimed). The LOG C2 bullet gives after-values only. Its before-value (5 failures, exit 1) appears only in the plan and in SCORECARD (minor, Q13).

## Q01 / Q21 judgment

- **Q01.** C2 is not a closure claim, and closing the declared 5-case payload while surviving shapes remain (recursion, external roots, `skills.paths`, unreadable roots) is exactly what Q01 calls `improved-bounded`. The label is honest. Holding depth at 9 is honest: there is no live effect on this host (F3), and the improvement is synthetic only.
- **Q21.** "Says it does not resolve the routed defect": met. "Re-measures that cause": partly met. The IND side was re-measured (10 → 10). The producer side and the second gap unit (F3) were measured but not recorded.
- **Godspeed or Q05, "harm none":** not met at the committed bytes (F1). Either repair it, or the label should read "improved-bounded, with one recorded harm".

## Smallest safe correction (append-only; no score move)

1. Repair F1: in the configured-root loop, skip or record an unreadable configured root, matching the contract's word "readable", and add a self-test arm (mode-000 root: exit 0, row unchanged). Bump the floor in step and re-run the ruler on the new commit. If it is not repaired, append to the depth row: "harm: unreadable `--oc-config/skill(s)` → whole-instrument exit 2 (base exit 0)".
2. Append the C1ClaimCritic hazard sentence (F2), with the probe values.
3. Append the live decomposition of the routed row: IND 10 versus producer 12 = 10 + `~/.claude/skills/kimi-webbridge` + marker. Add the external `~/.claude`/`~/.agents` `skills/**` roots and multiple config directories to "Not claimed".
4. Reword F4: "pins the frozen direct-child contract against a recursive variant (which matches upstream S016)".

## Web source (re-opened, fetch only)

`https://raw.githubusercontent.com/anomalyco/opencode/e3c4eb242585dcd77be1a867391b7c25fd47ce52/packages/opencode/src/skill/index.ts`
— accessed 2026-10-22T08:57:41Z, `curl` exit 0, sha256 `91dce57f…` (equal to C1ClaimCritic's fetch). Lines 23–24:
"const EXTERNAL_SKILL_PATTERN = "skills/**/SKILL.md"" / "const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"".

## Impacted axes

depth (owned: no-harm on the move, F1); consistency/calibration (records omit measured facts, F2–F4).

## Custody and tooling

Lane writes: this report only. No git or jj writes in the lane or the fleet repo. All gates ran in `$S` = `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A23C2Framing/`. Tooling: none installed or upgraded (stock `python3`, `git`, `curl`).
