# MutR1Keying — mutation test of the R1 keying repair (round 49 falsify)

**Verdict: HOLDS-BOUNDED** — applies to the R1 repair in
`verifiers/verify_harness_independent.py` at `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`. The
repair's *code* does implement the frontmatter-name operator; the *self-test battery* pins only
part of the contract it claims. Three of the five assigned mutants are killed; two survive
unchanged (`--self-test` exit 0) — coverage findings, not contract errors: the lesson's words
"keys **every** root by the frontmatter name" and "the directory name **only** as the
fallback" are **not measured** by any arm.

**What I attack.** The R1 keying change: `skill_identity()` / `read_frontmatter()` (new), the
`derive()` root loop, and the four new self-test arms (`build_frontmatter_key_fixture`,
`build_frontmatter_fallback_fixture`, the `fk` / `fk-control` / `fb` / `fl` arms).

## Setup (read-only on the lane; all writes in my own scratch)

- Scratch `/fast/scratch/hyaku/kotoba-r49/falsify/MutR1Keying/`; private clone `repo/` of the
  lane at `c48793d` (`git rev-parse` → `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`). The lane
  was written to only for this report; no git/jj write ran in the lane, fleet root or a sibling.
- Detector (bounded, identical for every run), in the scratch clone:
  `python3 -B verifiers/verify_harness_independent.py --self-test`.
- Pristine file SHA-256 `54f9c95b69b7f23048e31d534636dac2b71fdaa714db5330da5ef4eeeae4b3e5`;
  pristine baseline → **exit 0**, `0 failure(s) over 123 assertions`. No tool installed or upgraded.

## Mutants and verdicts

| # | Mutation (in `derive` / `skill_identity`) | Detector output | Exit | Verdict |
|---|---|---|---|---|
| M1 | configured roots keyed by **directory** (`names.add(entry.name if directory in configured else …)`) | `FAIL round 49: one identity offered by two roots under two directory names is counted once: got 4 want 3` / `1 failure(s) over 123 assertions` | 1 | **killed** |
| M2 | log-named roots keyed by **directory** (`… if directory not in configured else …`) | `FAIL round 49: a log-named root keys its skills by the frontmatter name too: got 4 want 3` / `1 failure(s) over 123 assertions` | 1 | **killed** |
| M3 | **fallback always uses the directory** (`skill_identity` → `return dir_name`) | `FAIL … counted once: got 4 want 3` + `FAIL … a log-named root keys its skills by the frontmatter name too: got 4 want 3` / `2 failure(s) over 123 assertions` | 1 | **killed** |
| M4 | **fallback never applies** (`… else ""`, empty name counted as `''`) | `0 failure(s) over 123 assertions` | 0 | **SURVIVED** |
| M5 | **agents root keyed by directory** (`names = {skill["dir"] for skill in offered}`) | `0 failure(s) over 123 assertions` | 0 | **SURVIVED** |

Mutated-file SHA-256 (each mutated, run, then restored): M1 `624d1d94516868ffa17e50df668fec02426d58f34c9036070ad6d770e5f13e52` ·
M2 `f1ff973c856984734281a7e0135b91adaa13d7256cc47a1543c654b7dbe1ed95` · M3 `d54b5b1de4a8aeded2b47eddc4abb8e916ccef6fda6ec9470beffb42f75eb822` ·
M4 `7430f21af1210cdce1e16e57c8afe09c9e2bbcb52d994e94610931ac6ae1984c` · M5 `57ae818070c77fc26a9768dbd94f60b5048d11a0ff2207ef805e05ddd4ff1f15`.

## Survivors and the fixture that would kill each

**M4 survives — the fallback arm measures a COUNT, not the identity.** The `fb` arm asserts
`oc.roots.names_plus_builtin == 3` for a configured skill whose SKILL.md has no frontmatter
`name`. Correct operator: names = {alpha, beta, "dir-noname"} (3). M4: names = {alpha, beta, ""}
(3). A count cannot tell `''` from `'dir-noname'`, so "the directory name is the fallback" is
unmeasured; the arm proves only "a nameless skill contributes exactly one name". Killing
fixture (proved, `probe_kill.py` PROBE-A): add a **second** nameless SKILL.md in the configured
root, `skills/dir-noname-2/SKILL.md` (no `name`), so the two nameless skills must be two
distinct names — pristine → count **4**, M4 → count **3** (both collapse to `''`). A smaller
kill: assert the helper directly, `skill_identity(read_frontmatter(<no-name SKILL.md>),
"dir-noname") == "dir-noname"` (M4 returns `''`).

**M5 survives — the agents root's keying is pinned by no arm.** Every fixture gives the agents
root skills whose **directory name equals the frontmatter name** (`build_fixture`: `alpha`/`alpha`,
`beta`/`beta`; the R1 fixture adds `agents/x` with `name: x`), so keying the agents root by
directory is indistinguishable from keying it by frontmatter name; "every root" therefore covers
only the configured and log-named roots. Killing fixture (proved, `probe_kill.py` PROBE-B): in the
R1 fixture rename the agents root's skill directory `x` → `dir-y` while keeping `name: x`, so the
agents root's *directory* name collides with the configured root's directory `dir-y` (frontmatter
`name: x`) — pristine → count **3** (one identity `x`), M5 → count **4** (`dir-y` + `x`). That
arm must also expect `omp.names.mismatches == 1` (it is 0 in the current fixture).

Proof the proposed fixtures kill (scratch `probe_kill.py`, exit codes verbatim): pristine →
`PROBE-A count=4 … identity='dir-noname'` / `PROBE-B count=3 … omp.names.mismatches=1` /
`PROBES-ALL-PASS` **exit 0**; M4 → `PROBE-A count=3 (correct=4) identity='' (correct='dir-noname')`
/ `PROBES-FAIL` **exit 1**; M5 → `PROBE-B count=4 (correct=3)` / `PROBES-FAIL` **exit 1**.

## Secondary finding: the "ONE operator" clause is false for an unreadable SKILL.md

`skill_identity`'s docstring and the `derive` comment claim every root shares one operator and
that "the directory name is the fallback … including when the SKILL.md cannot be read at all,
**which is the case the agents root has always fallen back to**". That last clause is false:
`Substrate.offered()` **drops** a skill whose SKILL.md cannot be read (`except OSError: continue`),
while `read_frontmatter()` returns `{}` for the same file in a configured/log-named root, so that
skill is kept under its **directory** name. Probe `probe_unreadable.py` on the landed bytes (uid
1000, so mode-000 really is unreadable): one unreadable SKILL.md in each root family gives
`roots count = 3` (alpha+beta plus only the configured-root one; both would be 4, neither 2),
`offered.skills = 2`, `agents-root unreadable skill offered? False`, `identity of the config-root
unreadable skill = 'unreadable-config'`. This asymmetry is **not** an R1 regression (the base
had it too), but it is a false statement in R1's new comment, and no arm covers an unreadable
**file** (the only unreadable-root arm is a mode-000 *directory*).

## Live effect of the survivors (this host)

`python3 -B verifiers/verify_harness_independent.py --derive` → `oc.roots.names_plus_builtin`:
pristine **10**, M4 **10**, M5 **10** (`omp.names.mismatches` = 0; `omp.offered.skills` = 10 — every
live skill's directory name equals its frontmatter name; both configured roots are absent here).
So M4/M5 are coverage gaps, not live wrong numbers; the lesson's "no live effect on this host"
statement is confirmed for the whole R1 change.

## Restoration evidence

After the last mutant: `git checkout -- verifiers/verify_harness_independent.py` in the scratch
clone → SHA-256 `54f9c95b69b7f23048e31d534636dac2b71fdaa714db5330da5ef4eeeae4b3e5` (== pristine),
`git status --porcelain` empty, final `--self-test` → **exit 0**, `0 failure(s) over 123 assertions`.

## Recommendation (no change made; the contract is not mine to restate)

1. Add a **second** nameless skill to `build_frontmatter_fallback_fixture` (or assert the
   identity, not the count) → kills M4.
2. Rename the agents root's skill directory in `build_frontmatter_key_fixture` so it differs
   from its frontmatter name → kills M5 and makes "every root" true of the battery.
3. Correct the `skill_identity` docstring / `derive` comment: the agents root does **not** fall
   back to the directory name for an unreadable SKILL.md, it drops the skill; or make the two
   families agree deliberately (the contract owner's call, not a falsify seat's).

## Evidence commands (exit codes verbatim)

```
python3 -B verifiers/verify_harness_independent.py --self-test   # pristine exit 0 (0/123); per-mutant exits in the table
python3 -B probe_kill.py <verifier>       # pristine exit 0 ; M4 exit 1 ; M5 exit 1
python3 -B probe_unreadable.py <verifier> # exit 0 (roots count = 3, asymmetry shown)
python3 -B verifiers/verify_harness_independent.py --derive  # pristine 10 / M4 10 / M5 10
```

Scratch artefacts: `/fast/scratch/hyaku/kotoba-r49/falsify/MutR1Keying/{repo,probe_kill.py,probe_unreadable.py,r1.diff}`.

Report: `.ufo/waves/round-49/falsify/MutR1Keying.md`
