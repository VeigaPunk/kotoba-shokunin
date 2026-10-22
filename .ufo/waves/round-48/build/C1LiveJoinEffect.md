# Round 48 build — C1 live-join effect (seat C1LiveJoinEffect)

Author: seat `KotobaR48.C1LiveJoinEffect` (leaf executor). Host: linux 7.2.11-arch1-1, x64.
Private clones: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1LiveJoinEffect/base` @ `75f671b109d8eddd0d64c1429bd6379fe577175a`, `.../cand` @ `26035dcec54d8e42f3a8b47ae8ca551c18aec295` (only diff between the two trees: `verifiers/verify_harness_independent.py`, +13/-8).

## Findings

1. **`oc.roots.names_plus_builtin` value: identical 10 at base and candidate** (default arguments). The only difference is the row's evidence string (base's wording counts log-named source dirs present; candidate's separates that from the configured roots that are present).
2. **Neither `~/.config/opencode/skill` nor `~/.config/opencode/skills` exists on this host.** `~/.config/opencode/` contains only `cli.json`, `opencode.json`, `service.json` (names; contents not read). The opencode log names six source directories; only `/home/vgpnk/Projects/opencodeufo/.opencode/skills` exists (contains `shokunin`, `tower`), and both its names are already inside the agents-root set of 10. Hence the candidate's configured-root union is vacuous here.
3. **C1 does not change the live join on this host.** Explicit default joins at base and candidate produce byte-identical reports (diff is only the recorded independent-command path): same exit code sequence, same protocol/strict counts, same 6-disagreement set including `oc.roots.names_plus_builtin` (live 12 vs independent 10, unchanged). The disagreement is the known definitional one (the live side counts the `customize-opencode` built-in marker plus `.claude/skills` names; the independent instrument fixes built-ins to 0 by declaration and does not read `.claude/skills`) — explicitly not resolved by C1 per the plan.
4. **Default live join is nondeterministic.** First run at each exit exited 2 (`false blocker` stale-snapshot race on the four `omp.catalogue.*` scope probes: declared `candidate_blocks` 5535 vs recomputed 5537 at base, 5574 vs 5576 at cand — the live session tree mutates between the independent instrument's probe census and the driver's recomputation). Reruns minutes later exited 1 (race did not fire). Round-47's recorded "default live join exit 2" reproduces. A frozen-carrier run (HOME pointed at a static copy of `~/.omp/agent/sessions`) gives exit 1 at both with identical counts.
5. **Current protocol/strict counts: 18/24 protocol, 14/24 strict, 4 adjudicated, 4 scoped out, 6 disagreements at both base and candidate** (frozen carrier and second live run agree exactly). Round-47 recorded 21/24 → 20/24 on a frozen *synthetic* 2-file carrier against the round-47 host state; the absolute counts moved because the host drifted since (offered skills 10→11, kimi-webbridge present in `.claude/skills`, npx ELF now the default OC binary → live `r_plus_builtin` 11→12). The base-vs-candidate identity is the finding that matters.
6. **The fix's mechanism is correct but inert on this host.** Controlled fixture: with `--oc-config` pointing at a scratch root holding `skill/alpha-skill` and `skills/beta-skill` that the log does NOT name → base 10, candidate 12 (fix adds them). When the same roots ARE named in a synthetic log → both 12 (base already enumerates log-named roots). This matches the committed ruler oracle (`.ufo/round-48/oracle/config-root-cases.json`: singular/plural/both-unlogged raise the count; already-logged cases do not).
7. **Self-test:** `--self-test` exits 0 at both base and candidate, 0 failures over 104 assertions. The candidate ships no new assertion count (Q05 regression-arm gap is separate-seat material, noted only).

## Evidence (commands, exit codes, paths, hashes)

All hashes are SHA-256 of the named artifact.

| Measurement | Command | Exit | Artifact (hash) |
|---|---|---|---|
| Base independent run | `python3 -B verifiers/verify_harness_independent.py --json` (cwd=base clone) | 0 | `base.json` (`4017c38e24d1d7a35946c9a8279e9d2b7ae8b45e045b7f297dd2bf04f6a507a8`) |
| Candidate independent run | same, cwd=cand clone | 0 | `cand.json` (`0edc19cf5942c8ffffad0551c3ba90f22e556b7d34a68aa6871b62390ee0136b`) |
| Base default join | `python3 -B verifiers/compare_harness_independent.py --json` (cwd=base) | 2 first, 1 rerun | `cmp-base.err`; `cmp2-base.json` (`ed917766969e23264a53a135f1c27bb9bd459d1380506f612145aa20be57399c`) |
| Candidate default join | same, cwd=cand | 2 first, 1 rerun | `cmp-cand.err`; `cmp2-cand.json` (`ea88b8b81a15186de8d2a54379b3e59e0d99988f58ac257830853f82dad76953`) |
| Base frozen-carrier join | `HOME=<frozen> python3 -B verifiers/compare_harness_independent.py --json` | 1 | `frozen-base.json` (`ed917766969e23264a53a135f1c27bb9bd459d1380506f612145aa20be57399c`) |
| Candidate frozen-carrier join | same, cwd=cand | 1 | `frozen-cand.json` (`ea88b8b81a15186de8d2a54379b3e59e0d99988f58ac257830853f82dad76953`) |
| Controlled fixture (unlogged roots) | base/cand with `--oc-config <fake>` (skill+skillsills, alpha-skill/beta-skill), real log | 0 / 0 | `ctrl2-base.json` value 10 (`d83fa31d2e4fb4c89c588d6005b7938556f09009a2d42891e768204a3eade4ea`); `ctrl2-cand.json` value 12 (`56df7c41f22b03502518f3933eb9dd7683daf9ec1cd1e6a5ca911b2eb3c3f2f9`) |
| Controlled fixture (logged roots) | same but synthetic log names both roots | 0 / 0 | `ctrl4-base.json` value 12; `ctrl4-cand.json` value 12 |
| Self-test | `python3 -B verifiers/verify_harness_independent.py --self-test` | 0 / 0 | `selftest-base.out` = `selftest-cand.out` = `0 failure(s) over 104 assertions` (`564d3cf8359deb6dd11ef573d4be88c8c5a1839141c84c871ed277e027d9342d`) |

Row detail (base then candidate), `oc.roots.names_plus_builtin`:
- base: value 10, evidence `"distinct skill names enumerated under the roots the opencode log names as sources (1 configured dirs present: none) plus the shared agents root (10 names); built-in names: 0 by declaration"`.
- candidate: value 10, evidence `"distinct skill names enumerated under the roots the opencode log names as sources (1 present) and the configured --oc-config roots (present: none) plus the shared agents root (10 names); built-in names: 0 by declaration"`.

Join report numbers (identical at base and candidate, both frozen-carrier and live rerun): exit 1; headline `mode-aware protocol 18/24`; `n_agree_protocol=18`, `n_agree_strict=14`, `n_adjudicated=4`, `n_disagree=6`, `n_scoped_out=4`, `n_uncovered=0`, `n_unknown=0`; live checks 28, independent checks 28; live exit 1 (baseline drift), independent exit 0. Disagreements: `oc.roots.names_plus_builtin` (live 12, ind 10), `omp.cache.misses` (4 vs 3), `omp.cache.verified_skills` (11 vs 7), `omp.descriptions.over_cliff` (11 vs 10), `omp.descriptions.unmodelled` (0 vs 3), `omp.offered.skills` (11 vs 10). Adjudicated: `oc.dup.onesided_roots`, `oc.roots.plugins_cache`, `omp.descriptions.missing`, `omp.names.mismatches`.

First-run default-join failure (both base and candidate): `compare_harness_independent: ERROR: false blocker: scoped row omp.catalogue.found declares observable {...,"candidate_blocks": 5535,...} but recomputation gives {"candidate_blocks": 5537,...}` (same for `matched`, `missing_names`, `total`; candidate declared 5574 vs 5576). Class matches the round-47 stale-snapshot race; it is the live peer-tree mutating between the two reads, not a C1 defect.

Host ground truth used: `~/.agents/skills` (10 dirs, all with SKILL.md), `~/.claude/skills` (`kimi-webbridge`, `omarchy` have SKILL.md; `synced` does not), `~/.config/opencode/skills` absent, `~/.config/opencode/skill` absent, opencode log mtime 2026-10-20 07:52 names `directory:` entries: `~/.config/opencode/{skill,skillsills}`, `~/.opencode/{skill,skillsills}`, `Projects/opencodeufo/.opencode/{skill,skillsills}` (only the last plural exists).

## Risks / notes

- The default join's exit code is not stable (2 when the carrier mutates mid-run, else 1); any gate that treats exit 2 as a clean C1 signal should freeze the carrier.
- C1's union is fully redundant on this host because the log already names both configured-root paths and neither exists; the claim's oracle-driven fixture battery (not the live join) is where its behavior is observable.
- No tools installed or updated this session (nothing beyond stock python3/git required).
- Lane bounds honored: no lane-repo edits besides this report; no git/jj writes in lane, fleet, or sibling lanes.
