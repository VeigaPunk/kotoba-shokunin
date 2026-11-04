# RevengerPrecedence — round 86 w1 report

Full probe: `.ufo/waves/round-86/w1/RevengerPrecedence/probe.md`; receipt: `.ufo/waves/round-86/w1/RevengerPrecedence/receipt-precedence.txt`.

**Verdict:** `other rule: provider-priority first-registration keeps the bare name; a later copy with a different body/frontmatter is kept as "<namespace>/<name>" (not dropped); same-realpath or identical (body + deepEquals frontmatter) copies are dropped; custom directories and non-skillshare copies displace an earlier copy`. The fixture does not show any precedence case.

## Findings
1. All 215 fixture lines come from two roots with **0 names in common**: `~/.omp/plugins/node_modules/ecc-pi-core/skills` gives 132 names (exactly the base's 132 `not-discovered`), and `~/.agents/skills` gives 83. Predicting each line from its read copy (bare-key cache row, else `preview`) matches 215 of 215. No fixture name contains `/`.
2. 132 fixture names have at least two distinct-realpath host copies with different descriptions. Every rendered line matches the read-root copy. In 102 of these names that copy is the only one that matches, so the name tells copies apart. The other 30 cannot: a differing copy produces the same line. None of the differing copies sits in a root omp 18.15.0 reads with default settings.
3. Nearest real test: 19 names also have a differing copy under `~/.claude/plugins/cache`. That is the claude-plugins provider, priority 70, registered before agents at the same priority. If omp read it, the source rule would give the bare name to that copy and render an `agents/<name>` line. That does not happen: 18 of 19 render the `~/.agents` copy (the 19th can't tell the copies apart) and no namespaced line appears. This is consistent with claude-plugins being an opt-out source that is off. It tests whether a source is enabled, not which root wins.
4. The code that decides (ELF offsets; each quote occurs exactly once):
   - `Fe` at 172,771,631 keeps providers in descending priority.
   - `Be` at 172,773,835 uses first-key-wins and marks later copies `_shadowed`. `Dp` bypasses this because it iterates `he.all` (177,500,886).
   - Same-realpath skip at 177,502,514.
   - `u0e`: identical copies dropped at 177,496,938; displacement branch at 177,497,011; differing-copy rename warning at 177,497,979.
   - The skill key is `name` (173,700,262).
   - Priorities: native 100, skillshare 95, omp-plugins 90, claude 80, agent-plugins 75, claude-plugins / agents / codex 70, opencode 55, github 30, omp-managed 5.
5. Where the lane model differs (reported for ExecModel, not patched):
   - `discover_skills` is first-wins and drops differing copies; omp keeps them as namespaced copies.
   - `USER_ROOTS` order is not omp's priority order.
   - `preview`'s word cut has no `o >= 40` floor; omp's `dnt` has one. No fixture line is affected.

## Risks
- The tie order among the three priority-70 providers assumes modules evaluate in bundle byte order [INFERENCE].
- Attributing the ecc-pi-core root to omp-plugins (90) rather than agent-plugins (75) is [INFERENCE]. Either way the verdict holds, because the two roots share no name.
- The source was read statically, not run. Per the revenger bound, no omp session was started; only `--help` ran, in a read-only bwrap.
