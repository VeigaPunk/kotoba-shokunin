Result: MIXED — the declared-pair admission rule holds on group renames and on the frozen counter's alias decoy, but it BREAKS in three ways that the round-50/51 allowlist rule did not. A callee whose every call has an unresolved variable group is silently dropped (a wrong pass on a shape the live 18.12.6 dump really has). A real loader called as a member (`o.Xl(...)`) is invisible. Any identifier call carrying a declared pair now proves a loader, so a decoy can stand in for a vanished one.

Seat: KotobaR52a2.CriticC1Escape (critic). Target: C1 rule escapes in `verifiers/verify_surfaces.py` at `c8407a453788df964df5a7b835dd0ce1360de882`.
Sandbox: `/fast/scratch/hyaku/kotoba-r52a2/CriticC1Escape` (git clone of the lane, `git rev-parse HEAD` = `c8407a453788df964df5a7b835dd0ce1360de882`). Nothing was written in the lane except this file.
Run window: 2026-10-22 17:49Z–17:58Z. No tools were installed or updated.

## Method

Every probe is a mutation of a committed fixture, run through the CLI with the self-test's argv (`verify_surfaces.py` self_test (b2c), lines 1088-1093):

    python3 -B verifiers/verify_surfaces.py --repo verifiers/fixtures/surfaces \
      --omp-strings <probe dump> --opencode-strings verifiers/fixtures/surfaces/strings-opencode-clean.txt \
      --baseline verifiers/fixtures/surfaces/baseline-18.12.5.json \
      --inventory verifiers/fixtures/surfaces/inventory-clean.md \
      --check surfaces.literal_present --check surfaces.no_uncovered_class

Each probe ran twice on the same bytes:
- **Declared mode** is the CLI as shipped.
- **Allowlist mode** is the same module with `OMP_CALLEE_MODE = "allowlist"` (the round-51 rule, whose `OMP_CALL_RE` already lists `lq/Xl/Fo/Kl/Ho/bq`). This tells a regression apart from an old limit.

Scripts and output (sandbox, sha256):
- `probes/run_probes.py` `977b40f246b02abe52532bcbfe72aa313b890bdc251f9b744ff5bb10fd734374`
- `probes/run_p4_live.py` `3f765a855ec7e6f7c7d7e544fc20755840166a957e8180ba08c903ceba8561c8`
- `probes/live_inventory.py` `e2eb0f5f93f8820b0cf07b3265b160b460450094771eae9c1acc3ea713c3a554`
- `probes/probes.out` `a47d12f60e304ada9a60f00322cbe1e3e9a2cecf816db3ced8db01d0a8a0e9af`
- `probes/p4live.out` `4c33ea7560535e8539fe5deceb1265df9d64c03fad8df5d1d9db5f508bb6e109`

Each mutated dump is kept under `probes/cases/`.

Rule under attack (`verify_surfaces.py:512-513`):

    admitted = {c for c, g, f in calls if (g, f) in declared}
    return {(g, f) for c, g, f in calls if c in admitted}

`OMP_GENERIC_CALL_RE` (`:234-238`) has the lookbehind `(?<![A-Za-z0-9_$.])`. The `.` is new; `OMP_CALL_RE` (`:211-215`) has `(?<![A-Za-z0-9_$])`.

## Probe table (exit codes observed)

| Probe | Input (mutation of 18.12.5 fixture unless noted) | Declared exit | Allowlist exit | Right? |
|---|---|---|---|---|
| P0a | 18.12.5 fixture as committed | 0 | 0 | yes (control) |
| P0b | 18.12.6 fixture as committed | 0 | 0 | yes (control) |
| P1a | + `dz(u,"agents-md","AGENTS.md"); dz(u,"notes","NOTES.md")` | 1 (`omp:notes/NOTES.md` undeclared) | 0 | acceptable: fails closed on a decoy |
| P1b | all `lq(` lines deleted; + a string literal `'example: dz(u, "agents-md", "AGENTS.md") or dz(u, "claude-md", "CLAUDE.md")'` | **0** | 1 | **NO: wrong pass** |
| P1c | all `lq(` lines deleted, no decoy (control for P1b) | 1 | 1 | yes |
| P1d | 18.12.6 + an unrelated module reusing `Kl(x,"readme","README.md")` | 1 | 1 | same as before (loud) |
| P2a | + `o.Xl(u, "newgroup", "NEWFILE.md")` | **0** | 1 | **NO: wrong pass** |
| P2b | every `Xl(u,` → `o.Xl(u,` | **1** (opencode, windsurf not verifiable) | 0 | **NO: wrong fail** |
| P2c | 18.12.6, every `bq/Kl/Ho(u,` → `ns.<callee>(u,` | **1** (vacuity, 8 missing) | 0 | **NO: wrong fail** |
| P3a | `"gemini"` → `"gemini2"` in the dump only | 1 (3 missing; 3 `gemini2` undeclared) | 1 | yes |
| P3b | gemini renamed in the dump and the baseline | 0 | 0 | yes |
| P3c | `"agents-md"`, `"claude-md"` renamed in the dump only (`lq`'s only groups) | 1 (literal_present only; `no_uncovered_class` PASS, new names not shown) | 1 (names `agentsmd2`, `claudemd2`) | exit right, diagnosis worse |
| P3d | the same rename in the dump and the baseline | 0 | 0 | yes |
| P3e | every group renamed in the dump | 1 (vacuity and extractor-blind) | 1 | yes |
| P4a | `f$` and `m$` rebound in their scope, so `lq` has only `<unresolved-var>` groups | 1 (literal_present only; `no_uncovered_class` PASS, no `<unresolved-var>` shown) | 1 (names `<unresolved-var:f$>`, `<unresolved-var:m$>`) | exit right, diagnosis worse |
| P4b | P4a + `Xl(u,"agents-md","AGENTS.md")`, `Xl(u,"claude-md","CLAUDE.md")` | **0** | 1 | **NO: wrong pass** |
| P4c | + `Xl(u, W$, "WHATEVER.md")` (admitted callee, unresolved call) | 1 | 1 | yes |
| P4d | 18.12.6: `zBt(u, v$)`, `XBt(u, S$)`, so `bq` has only parameter-shadowed groups | 1 (no `<unresolved-var>` shown) | 1 (names both) | exit right, diagnosis worse |
| P4e | P4d + `Kl(u,"agents-md","AGENTS.md")`, `Kl(u,"claude-md","CLAUDE.md")` | **0** | 1 | **NO: wrong pass** |
| P4f | 18.12.6, only `S$` shadowed (the self-test b2i shape) | 1 (names `<unresolved-var:S$>`) | 1 | yes |
| P5a | fixture (keeps `q(u,"evil","EVIL.md")`) + `q(u, "agents-md", "AGENTS.md")` | 1 (`omp:evil/EVIL.md` undeclared) | 0 | yes in JS terms (see finding 4) |
| P5b | fixture as committed (`const q = Xl; q(u,"evil","EVIL.md")`) | 0 | 0 | as the frozen counter requires; a real aliased registration is missed |
| P5c | alias registers only `("agents-md","AGENTS.md")` | 0 | 0 | yes |
| P5d | alias registers `("cursor-rules","CURSOR.md")` | 0 | 0 | same as P5b |

Probe output is verbatim in `probes/probes.out` and `probes/p4live.out`. For example, P4e declared mode:

    PASS surfaces.literal_present: 8 loader-kind entries verified against the dumps
    PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared

and the same bytes in allowlist mode:

    FAIL surfaces.no_uncovered_class: 2 loader class(es) undeclared in baseline: omp:<unresolved-var:S$>/CLAUDE.md, omp:<unresolved-var:v$>/AGENTS.md

## Live-dump grounding

`strings -n 4 ~/.local/bin/omp` was dumped to the sandbox (`omp/18.12.6`; binary sha256 `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`; 48148449 bytes of strings). `probes/live_inventory.py` (exit 0) runs the shipped regex over the dump:
- The full generic-shape match set is 11 calls from three callees: `Ho` ×4, `Kl` ×5, `bq` ×2.
- **`bq`'s raw pairs are `[('$S$', 'CLAUDE.md'), ('$v$', 'AGENTS.md')]`.** The live `agents-md`/`claude-md` loader admits only through variable resolution, so it is exactly the P4 shape.
- The dump has 0 member-call shapes (`.<name>(<v>, <group>, "<file>.md")`).
- `declared_loader_pairs` returns 33 omp pairs. 25 of them are not `loader-group` (for example `('codex','AGENTS.md')`, `('omp-dir','AGENTS.md')`, `('agent-system-prompt','SYSTEM.md')`).

## Findings

### 1. BREAKS — Medium — callee with only unresolved-variable groups is silently dropped (P4b, P4e; P4a, P4d diagnosis)

**Counterexample.** On the 18.12.6 fixture (the live shape), parameter-shadow both of `bq`'s group variables, and let any admitted callee also register `agents-md/AGENTS.md` and `claude-md/CLAUDE.md`. The gate exits 0. The allowlist rule exits 1 naming both `<unresolved-var>` classes.

**Why.** An `<unresolved-var:NAME>` group can never be a declared pair, so a callee whose every call is unresolved is never admitted. Its calls then vanish from the extraction entirely. Without the second registration (P4a, P4d), the gate still exits 1, but only through `literal_present`. The unresolved variables are no longer named.

**Evidence.** The `extract_classes` docstring (`verify_surfaces.py:480-481`) promises unresolvable groups "surface as a `<unresolved-var:NAME>` group so they cannot pass silently". The probes falsify that promise. The self-test only covers the one-shadowed case (b2i, `:1286-1303`), where `bq` stays admitted through `v$`.

**Axes.** freshness (C1 claims robustness on this exact callee); regression against the round-51 behaviour.

**Smallest safe correction** (applied in the sandbox only, `probes/correction.diff`, sha256 `b34baa2871b5b9421244398b90fd6dfd165a94bbce39c10487a5e9e3b336c977`): also admit a callee when one of its calls has an unresolved group whose file is a declared file.

    declared_files = {f for _, f in declared}
    admitted = {c for c, g, f in calls
                if (g, f) in declared
                or (g.startswith("<unresolved-var:") and f in declared_files)}

Measured with the correction in the sandbox:
- `--self-test` → `0 failure(s) over 129 assertions`, exit 0.
- `check_callee_rename.py --root <sandbox>` → `callee-rename robust 4 of 4 fixtures`, exit 0, for `--seed 52`, `7` and `1234`.
- Live dump (`--omp-strings probes/omp-live.strings`, the two omp checks) → PASS/PASS, exit 0.
- P4a and P4d exit 1 and name both `<unresolved-var>` classes again.
- P4b and P4e exit 1.
- Every other probe has the same exit code as before.

A self-test arm for the P4e shape should land with it.

### 2. BREAKS — Low-Medium — a real loader called as a member is invisible (P2a wrong pass; P2b, P2c wrong fail)

**Counterexample.**
- `o.Xl(u, "newgroup", "NEWFILE.md")` added to the 18.12.5 fixture exits 0. Allowlist mode exits 1, naming `omp:newgroup/NEWFILE.md`.
- If a bundle emits every loader call as a member, the declared rule FAILs: P2b exit 1, and P2c exit 1 with vacuity. Allowlist mode passes both, exit 0.

**Why.** The new `.` in the lookbehind (`:235`) was added on purpose. The self-test locks it in with `admission: member call not matched` (`:1207-1209`). Before round 52, `OMP_CALL_RE` matched `x.bq(`, so this is a regression in both directions. It is not listed under "What this does not survive" (`:228-231`).

**Live today.** There are 0 member-call shapes in the 18.12.6 dump, so the gate is not wrong today. [INFERENCE] A namespace-import or object-export bundling change would hit it.

**Smallest safe correction** (either one):
- (a) Drop the `.` from the lookbehind and flip the `:1207-1209` arm to expect the member call to be matched. Measured in the sandbox together with correction 1 (`probes/correction2.diff`):
  - Self-test fails only that one arm (`self-test FAIL: admission: member call not matched: got [('agents-md', 'AGENTS.md')]`, 1 failure over 129).
  - The counter prints 4 of 4 for seeds 52, 7 and 1234.
  - The live dump PASS/PASS, exit 0.
  - P2a exits 1; P2b and P2c exit 0; P1b is unchanged.
  - Tradeoff: member-call decoys that register a declared pair also admit their name.
- (b) Keep the rule and add member calls to the documented limits at `:228-231`.

### 3. BREAKS (tradeoff) — Medium — any identifier call with a declared pair proves a loader, so a decoy masks a vanished loader (P1b)

**Counterexample.** Delete both real `lq` registrations from the 18.12.5 fixture. Add one string literal containing `dz(u, "agents-md", "AGENTS.md") or dz(u, "claude-md", "CLAUDE.md")`. Declared mode: `PASS surfaces.literal_present: 8 loader-kind entries verified`, exit 0. Allowlist mode: exit 1, both rows "not verifiable". The control without the decoy (P1c) exits 1 in both modes.

**Why.** Admission and `literal_present` both accept any callee name. The registration shape is no longer bound to a loader identity at all, and because the source is a `strings` dump, text inside string literals counts.

**Live today.** Not exploited: the live dump has only the 11 real calls.

**Impacted axes.** freshness (C1 trades loader identity for rename robustness), calibration (the C1 statement and `SCORECARD.md` "Not covered: a change of call shape" do not mention it).

**Smallest safe correction.** This is a tradeoff, not a defect the frozen counter can see; it is the judge's call. At minimum, add it to the documented limits (`:228-231`) and to the SCORECARD "Not covered" cell. [INFERENCE] A cheap mitigation would require an admitted callee to have at least two call sites, or a function definition `function <name>(` in the dump. Not tested.

### 4. HOLDS against the frozen counter, false provenance in the label — Low — the "alias decoy" is a real alias (P5)

`const q = Xl; q(u, "evil", "EVIL.md")` is, in JavaScript, a call to the loader `Xl`: a real registration of `evil/EVIL.md`. The rule keeps it out only because `q` happens to register no declared pair:
- P5b and P5d exit 0 and silently miss it.
- Give `q` one declared pair (P5a) and `evil` surfaces, exit 1.

So the decoy is excluded by accident of what it registers, not by identity. The allowlist rule missed it too, so this is not a regression, and arm A of the frozen counter requires `evil` to stay out. The defect is the wording:
- `verify_surfaces.py:225-226` calls it "an alias decoy … a callee with no declared pair".
- The `baseline-18.12.5.json` `$comment` says it "must NOT extract".

**Correction.** Reword both to "an alias of a real loader that registers no declared pair; its registrations are not seen (a known miss, required by the frozen counter's arm A)".

### 5. HOLDS — declared group renamed (P3a, P3b, P3d, P3e)

- A rename in the dump alone fails loud, and names the new group whenever the callee stays admitted (P3a).
- A consistent rename in the dump and the baseline passes (P3b, P3d).
- Renaming every group trips vacuity and extractor-blind (P3e).
- Low diagnostic gap (P3c): when the rename strips a callee's only declared pairs, `no_uncovered_class` does not name the new groups (the allowlist rule did). The exit is still 1 through `literal_present`. Correction 1 does not cover this.

### 6. HOLDS — decoy registering one declared pair plus a new one (P1a), and name reuse (P1d)

- P1a fails closed (exit 1, names `omp:notes/NOTES.md`). That is a loud false alarm on a non-loader, which is acceptable.
- P1d behaves exactly as the allowlist rule did (exit 1).

### 7. Comment drift — Low — admission is described as `loader-group` only

`verify_surfaces.py:222-224` says a callee is admitted by a pair "the baseline declares for omp as `loader-group`". `declared_loader_pairs` (`:516-530`) uses every omp class id regardless of kind: 33 pairs, 25 of them not `loader-group`. The docstring there explains why (the rekind arms). The `:222-224` comment should say "any kind".

## Out-of-target observation for the L1 (no-harm guard, not C1 harm)

The plan's no-harm guard (`plans/round-52.md:34-35`) and the uncommitted `SCORECARD.md` freshness cell (working-tree diff, the `round 52 (C1 …` line: "No harm: live gate `pass 7`, exit 0 on omp 18.12.6") do not reproduce at 17:54Z:

    cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B verifiers/verify_surfaces.py --json   # read-only, HEAD c8407a45
    → exit 1; surfaces.opencode_extract FAIL ("declared opencode class(es) produced by no rule: opencode:instruction-context/AGENTS.md, opencode:read-hook/instructions; rule(s) matched nothing: OC-4 …; OC-6 …"); other 6 PASS

The base gate (`git archive c8579a4c… verifiers corpus/knowledge` into the sandbox) fails identically (exit 1, the same opencode_extract FAIL), so C1 did not cause it. The opencode substrate is `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`:
- sha256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`
- 214522032 bytes
- mtime 2026-10-22T14:50:30 (local)

The gate's generation note (`:551-553`) records the earlier lineage as sha `179ca421…`. [INFERENCE] The opencode binary drifted; the "pass 7" cell should be re-measured before it is committed, or reworded to the two omp checks.

## Checks the L1 should run after any fix

- `python3 -B verifiers/verify_surfaces.py --self-test` (tally ≥ the 129 floor, plus new arms for the P4e and P2a shapes)
- `python3 -B verifiers/check_callee_rename.py --rev <new rev>` with `--seed 7` and `--seed 1234`
- the live two-check run on omp 18.12.6
- `python3 -B verifiers/check_assertion_floors.py`
