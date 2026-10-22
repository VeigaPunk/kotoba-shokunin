# A26NestedOracleGap — C2 instrument boundary: nested-skill oracle gap vs the consumer-side arm

Seat: `KotobaR48.A26NestedOracleGap` (UFO-FSD critic, leaf, no delegation). Axis judged: depth.
Target: C2 depth `d1ae45830235c38320b31032b57a8323cbf90b17` (consumer sha256 `d67b1b6e…`), records
`84b9c9ba…`. Lane HEAD moved to `d28b16b` during this seat (falsify-wave corrections by another
author). That commit leaves the consumer, the oracle and the nested-gap wording unchanged.

## Verdict

- **After-value: CONFIRMED (honest).** On the landed commit the ruler reads verdict clean, 0 target
  failures, 0 behavioral mismatches, exit 0, with 13/13 cases observed. My rerun matches the committed
  receipt `after-configured-root.json` (same consumer sha256, same revision).
- **The arm as closure of the instrument boundary: DEFECT, severity LOW (fixable in the records, not a
  tradeoff to reject).** The arm kills the one routed recursive mutant, R1. It does not pin the
  direct-child scope as a class: three other non-direct-child operators (R2, R3, R4) pass both the
  frozen ruler and the landed 115-assertion self-test, and each diverges from the landed consumer on
  a real input. The claim's after-value never depended on that scope: `instrument.json` scope reads
  "Nested discovery remains unclaimed, upfront not learned from outputs". So no number changes.
  What is overstated is the framing that the arm closes the gap.

## Counterexample (strongest found)

R2: recursion (`**/SKILL.md`) only under log-named roots that are not one of the two configured roots.
It passes the ruler (exit 0, clean) and the self-test (exit 0, 0 failures over 115 assertions).
It changes the legacy log-root operator, which the oracle's `scope` says must stay
("matching the legacy instrument existing log-root operator"). It also contradicts the landed code
comment "the same operator for every root". The arm's log-named case (`cfg-logext`) has no nested
skill under the external root, and its `cfg-logsame` case names a configured root, so R2's branch
never fires.

## Evidence (private clone `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A26NestedOracleGap/clone`)

Ruler command, the plan's own command per run:
`python3 -B .ufo/round-48/tools/config-root-ruler.py --repo <clone> --revision <rev>
--consumer-sha256 <sha> --oracle …/config-root-cases.json --oracle-sha256 1d09a38c…
--scratch <seat>/ruler-<n> --baseline-receipt …/before-configured-root.json --baseline-sha256 8bec447a…`.
Self-test command: `python3 -B verifiers/verify_harness_independent.py --self-test`.
Pinned file hashes verified at `d1ae458`: ruler `01af33a6…`, oracle `1d09a38c…`, before receipt `8bec447a…`.

| Consumer | Commit | sha256 | Ruler exit / verdict | Self-test exit / summary |
|---|---|---|---|---|
| landed | `d1ae458` | `d67b1b6e…` | 0 / clean | 0 / 0 failure(s) over 115 |
| R1 rglob + is_file + parent name (routed) | `201c599` | `2866aa8b…` | 0 / clean | 1 / 6 failure(s) over 115 |
| R2 recursive under log-named non-configured roots | `97687ea` | `4366a0ea…` | 0 / clean | 0 / 0 failure(s) over 115 |
| R3 direct child plus depth-3 glob | `cfce36d` | `92dbb202…` | 0 / clean | 0 / 0 failure(s) over 115 |
| R4 direct child plus skills nested inside a skill | `930d83d` | `69ea627b…` | 0 / clean | 0 / 0 failure(s) over 115 |

In all five receipts, `consumer_sha256_before == consumer_sha256_after`, 13/13 cases are observed,
and there are no evaluation errors. Mutant generator: `<seat>/mutate.py`. The edit is one anchor in `derive()`.
R1's six red assertions on landed bytes include "a nested skill is not a name (direct children only):
got 2 want 0". This reproduces the build-wave finding (`C1RegressionArm.md` F3) on the landed commit,
not just the candidate.

Divergence probe (`<seat>/probe.py` → `<seat>/probe.out`; it imports each consumer's own
`build_configured_root_fixture` and `derive`; no oracle file touched). Two independent runs both
exited 0 with identical JSON. The first mutant batch's ruler and self-test exit codes match the
reruns in the table above. Values of `oc.roots.names_plus_builtin`:

| Input shape (added to the arm's flat fixture) | landed | R1 | R2 | R3 | R4 |
|---|---|---|---|---|---|
| `skill/group/zeta/SKILL.md` (the arm's shape) | 5 | 6 | 5 | 5 | 5 |
| log-named external root with `group/deep/SKILL.md` | 6 | 7 | **7** | 6 | 6 |
| `skill/a/b/c/SKILL.md` (depth 3) | 5 | 6 | 5 | **6** | 5 |
| `skill/solo-s/sub/SKILL.md` (skill inside a skill) | 5 | 6 | 5 | 5 | **6** |

Each survivor departs from the landed consumer exactly on its own shape. The arm covers one shape:
depth 2, under a non-skill directory, under a configured root.

Floors guard: `check_assertion_floors.py:514` passes when the assertion count is at least the floor,
there are 0 failures, and the return code is 0. R2, R3 and R4 meet all three
([INFERENCE]: guard not run on the mutants).

Upstream behavior, re-opened: https://raw.githubusercontent.com/anomalyco/opencode/v1.19.3/packages/opencode/src/skill/index.ts
(lane row S016), fetched 2026-10-22T08:55:48Z with `curl` exit 0, sha256 `91dce57f…`. Line 24 reads:
"const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"". Opencode itself discovers recursively,
so R1 is closer to the real loader than the landed consumer. The direct-child rule is a declared
bound on the instrument, not a fact about opencode.

## Answers to the assignment

1. **Adequate closure for the claim as declared (ruler target failures 5 → 0)?** Yes for the claim.
   No for the instrument boundary. The declared measure is satisfied and honest. But the ruler
   cannot tell direct-child from any recursive operator, so "0 target failures" certifies the union
   and set semantics only. The arm is a lane-authored, consumer-side regression test. It sits
   outside the declared claim command and pins one nested shape. It is the Q05 regression arm the
   plan asked for, not a substitute for the oracle case the frozen contract's own `scope` text
   (direct child only, no recursion policy) leaves unmeasured.
2. **What the report must say:**
   - C2's after-value is a reading over a 13-case matrix with no case below a root's direct child.
     The ruler is blind to the scope the oracle declares.
   - The direct-child scope is pinned only by the consumer's own self-test, which is not an
     independent instrument, and only for depth-2-under-a-non-skill-directory under a configured
     root. Name the survivors: recursion under log-named external roots (R2), depth 3 and deeper
     (R3), and a skill nested inside a skill (R4).
   - "Kills the recursive mutant the frozen ruler passes" (LOG round-48 entry; SCORECARD depth row)
     is true for one mutant. It must not be read as "recursion class closed".
   - "Recursive mutant" is a test label, not a defect claim. Per S016, recursive discovery is
     opencode's real behavior. Landed `names_plus_builtin` undercounts opencode whenever a
     configured root holds nested skills, by declared scope.
   - The round-49 oracle amendment (already in SCORECARD "Next: round 49") should list all four
     shapes above, including the log-named-root shape, so the legacy operator is pinned as well.
3. **Is the after-value still honest?** Yes. 0 target failures and exit 0 are reproduced on the
   landed bytes and match the committed receipt. The scope was disclaimed before outputs existed
   (`instrument.json` `scope`, `unproved_limits` "recursive loader parity"). It stays honest only
   with the qualification in point 2. SCORECARD per-round row `| 48 | depth |` ("0 target failures,
   ruler exit 0 @ d1ae458; self-test 104 → 115") carries no blind-spot note, while the top depth
   row does. Append the qualification to the per-round row too.

## Impacted axes

depth (instrument discrimination: the oracle and the arm leave three operators unpinned); calibration
(the record wording "kills the recursive mutant" invites a class reading). Freshness and C1 are untouched.

## Smallest safe correction

Records only, append-style: qualify the LOG C2 bullet and the SCORECARD `| 48 | depth |` row as in
point 2, and extend the round-49 amendment list with the four shapes. Optional, consumer-side, does
not change the claim: add the log-named-external-nested and skill-in-skill shapes to the arm, which
kills R2 and R4. Changing the oracle needs a prospective amendment. It is not a repair for this
round.

## Custody and tooling

- Lane: only this report was written. No git or jj write ran in the lane, the fleet repo, or any
  sibling. The lane's `git status --porcelain` at write time shows other seats' files only.
- Scratch: mutant branches `mut-R1`…`mut-R4`, worktrees `wt-R2`…`wt-R4`, receipts `ruler-*`,
  `ruler2-*`, and `selftest*.out`, all under `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A26NestedOracleGap/`.
- Tooling: nothing was installed or upgraded. Used `python3 3.14.8`, `git 2.56.0`, and `curl`
  (already present). No fetched code was executed.
