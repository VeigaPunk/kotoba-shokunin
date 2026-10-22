# ReviewSurfacesDesign — extractor identifier resolution for `S$` (omp 18.12.6)

VERDICT: HOLDS-BOUNDED — the shipped conservative rule is correct (fail-closed, loud) but cannot
reach C1 alone; recommend rule (b′) windowed-consensus extension with the fixtures in § Fixtures.
Reviewed: `verifiers/verify_surfaces.py` at `43ca0bfb` (ASSIGN_RE ~163-167, module callee comment
138-160, `constant_table` 300-313, `extract_classes` 316-330, OMP_CALL_RE 151-160) against the
installed omp 18.12.6 (sha256 `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`,
verified by re-hash). Analysis ran in my clone; the lane was not modified except this report.

## Measured ground truth (commands in § Evidence)

- Before-value reproduced from the clone: `--json` → `exit_code 1, fail 2, pass 5` (FAILs:
  `surfaces.literal_present`, `surfaces.no_uncovered_class`); `--self-test` → `0 failure(s) over
  99 assertions`, exit 0.
- Loader-shaped calls `CALLEE(v, <group>, "<file>.md")` in the live dump (generalized callee
  census): 11 total, callees `{Kl: 5, Ho: 4, bq: 2}`. All 8 declared omp loader-groups are
  present; 6 carry literal groups, 2 carry identifiers: `bq(u, v$, "AGENTS.md")` and
  `bq(u, S$, "CLAUDE.md")`.
- `v$` has exactly one dump binding (`var v$ = "agents-md";`, 73 bytes before its call) →
  resolves today.
- `S$` has exactly two dump bindings: `var S$ = "title";` at dump line 843423 (module
  `src/session/session-entries.ts`) and `var S$ = "claude-md";` at line 895604 (module
  `src/discovery/claude-md.ts`), 73 bytes before the call at line 895607; distance
  binding→call = 73 bytes, foreign binding→call = 1,496,748 bytes (521,181 lines).
- `constant_table` therefore marks `S$` conflicted → `extract_classes` emits
  `<unresolved-var:S$>/CLAUDE.md` → `no_uncovered_class` reports it undeclared and
  `literal_present` misses `(claude-md, CLAUDE.md)`. Re-pinning callees to `Kl|Ho|bq` alone
  still leaves both checks red: the S$ resolution rule is on the C1 critical path.
- opencode isolation: live opencode dump (67,839,091 bytes) has 0 CALL_RE matches, 0 identifier
  args; `surfaces.opencode_extract` passes 9/9 from 7/7 rules. The OC rules are separate regexes;
  `extract_classes`' opencode leg matches nothing, so any change to identifier resolution is
  unobservable there (see per-rule notes).

## Candidate rules

### (a) Nearest preceding binding in the same strings chunk/line

- As stated, it fixes nothing: the call's chunk is `  return bq(u, S$, "CLAUDE.md");` (32 chars,
  call at char 9); the binding sits 3 dump-lines above in its own 21-char chunk. Same-chunk or
  same-line, there is no binding to find → `S$` stays unresolved → the false red persists (M17).
- Weakened to "nearest preceding binding anywhere", it happens to give `claude-md` on this dump —
  but the winner is decided by linker chunk order, not scope. What it mis-resolves: any same-name
  assignment the linker happens to place between the true module and the call (a decoy module, or
  a string-looking assignment in intervening code) wins; nothing in the rule distinguishes the
  true module-local declaration from coincidence. Control arm that proves it (Q18/M17): a fixture
  with a same-name decoy binding placed between the true binding and the call — (a) picks the
  decoy and manufactures a pair the dump does not witness (if the decoy value equals a declared
  group, this is a silent wrong pass; no green arm can also kill it). It also reverses the
  constant table's existing first-seen direction, making extraction order-direction-dependent.
- opencode: no effect (0 matches on live dump; 9/9 preserved), for every variant.

### (b) All bindings within N bytes agree

- On the measured dump, any N in roughly [90, 1.49M] resolves `S$` → `claude-md` and leaves `v$`
  resolved; N=256 gives 3.5× headroom over the 73-byte binding→call geometry and sits 5,800×
  under the foreign binding. The window is byte distance in the strings dump — the same
  substrate the instrument already operates on; no new input class (comments, module markers)
  is required. (A module-comment-delimited variant would be stronger on this dump — the bundle
  keeps `// packages/...` path comments — but couples extraction to comment survival across
  bundler configs; rejected as more coupled, not more correct.)
- Mis-resolve mode: a genuinely conflicting binding inside the window (dense minified region) →
  unresolved, loud — a false red, never a wrong extraction. Control arm (Q18): fixture with two
  disagreeing in-window bindings must stay unresolved and name the class. Second control arm:
  the promised second-declarator class (`var A = "x", zou = "claude-md";`, ASSIGN_RE docstring)
  inside the window must stay green.
- Q18/M17 hard requirement: the rule must be monotone-widening — a unique global binding far
  outside the window resolves today (that is how `v$`-style singletons behave) and must keep
  resolving, or the change silently narrows accepted input. So (b) must EXTEND
  `constant_table`, not replace it: unique-global → resolve (unchanged); conflicted-global →
  resolve iff ≥1 binding of that name in the preceding window `[k−N, k)` and all in-window
  bindings agree; else unresolved (unchanged). Under this shape no input resolved today becomes
  unresolved — zero new false reds by construction.
- opencode: no effect (0 matches on live dump; 9/9 preserved). The committed 99-assertion
  self-test is the standing green control.

### (c) Pinned per-version alias table in the baseline

- No runtime mis-resolution, but it pins the answer, not the mechanism. Unvalidated, it overrides
  the dump: a future bundle where `S$` means something else still yields
  `omp:claude-md/CLAUDE.md` — a silent laundering path that contradicts the extractor's own
  invariant ("unresolvable ones surface as `<unresolved-var:NAME>` so they cannot pass silently").
  Control arm that decides it: a fixture whose dump binds `S$` only to a foreign value while the
  alias pins `claude-md` — unvalidated (c) exits 0 (proven harmful), a validated alias (resolve
  only if the pinned value actually occurs as a binding of that name in the dump) exits 1.
- Validated (c) is safe but degenerates: among conflicting bindings it still picks by fiat, and
  it adds a second manual per-version pin beside the callee allowlist — which the round-21
  comment already flags as "the FIRST thing to re-pin on a binary bump". Baseline schema change
  is additive (`load_baseline` ignores unknown keys) and opencode is untouched (9/9 preserved),
  but the maintenance cost buys nothing over (b′).

## Recommendation

Adopt (b′) — windowed-consensus extension of `constant_table`, fail-closed, N=256, window
`[k−N, k)` over raw dump offsets, name-scoped (only bindings of the identifier in question):
1. global table has one distinct value → resolve (today's behavior, unchanged);
2. global table conflicted → resolve iff ≥1 binding of that name in `[k−N, k)` and all in-window
   bindings agree;
3. otherwise unresolved (today's behavior; `<unresolved-var:NAME>` keeps surfacing loudly).
Record N in a named constant with the two measured numbers (73; 1,496,748) and the fixture-bound
invariant 73 ≤ N < ~1,200. Scoped note: implement in `constant_table`/`extract_classes` (shared
code), prove opencode inertness with the existing arms rather than a harness fork.

## Fixtures (exact, all in `verifiers/fixtures/surfaces/`, distilled style matching
`strings-omp-18.12.5.txt`; run through the existing `--self-test` harness)

1. `strings-omp-18.12.6.txt` — GREEN arm (the round-51 generation fixture). Distilled live
   geometry: `var S$ = "title";` line in a foreign module 300–1,200 bytes before the call;
   claude-md module (`var S$ = "claude-md";` then `return bq(u, S$, "CLAUDE.md");`);
   `var v$ = "agents-md";` + `bq(u, v$, "AGENTS.md")`; Kl and Ho gemini pairs (both callees, as
   measured); `github`/`windsurf`/`opencode` literal-group calls; the committed decoy line
   (`var decoy = q(u, "evil", "EVIL.md")`) kept out by the allowlist. Reuses
   `baseline-clean.json`/`inventory-clean.md` (same 8 loader-groups). Assert: exit 0,
   `PASS surfaces.literal_present`, `PASS surfaces.no_uncovered_class`. Bounds N from both sides:
   N<73 (shrink mutation) → unresolved → exit 1; N≥~1,200 (grow mutation) → foreign `title`
   enters the window → disagree → exit 1.
2. `strings-omp-window-decoy.txt` — NEVER-GUESS arm. Same module but two disagreeing `S$`
   bindings inside the window (`var S$ = "gemini";` ~80 bytes before the call,
   `var S$ = "claude-md";` ~200 bytes before). Assert: exit 1 and the detail names the class —
   either `undeclared in baseline: omp:<unresolved-var:S$>/CLAUDE.md` or the literal_present
   `(claude-md, CLAUDE.md)` message. Kills nearest-in-window and any guessing upgrade of (b′).
3. `strings-omp-window-second-declarator.txt` — Q18 green arm. Sole binding in the promised
   second-declarator form (`var A = "x", zou = "claude-md";`) inside the window.
   Assert: exit 0, `PASS surfaces.literal_present`.
4. No new baseline keys; opencode arms untouched — the full self-test (99 existing assertions +
   the new arms) must stay 0 failures, which is itself the 9/9-from-7/7 control.
   Note for the executor: the "must fail with the round-50 callee allowlist" direction (Q25) is
   carried by the recorded red base run (5/7 at `43ca0bfb`, reproduced above); within one commit
   both allowlists cannot hold, so do not fake it with a second fixture.

## Residual risk and verification gaps

- Fixtures are specified, not executed: no (b′) implementation exists yet; the executor must add
  the code + fixtures and the falsify wave should mutation-test N (64 and 4096 must both turn
  fixture 1 red).
- (b′) window semantics assume top-level `var` bindings execute before loader calls in dump
  order (true in the measured bundle); a hoisted-after-binding pattern within a module would be
  unwindowed and stays on today's path (unique → resolve, conflicted → unresolved loud). No
  observed instance; noted as a documented limit, not a defect.
- The Kl/Ho double registration of the three gemini pairs (both callees, same (group, file)) is
  unexplained upstream duplication; set-extraction tolerates it. Out of scope.
- `check_substrate_pins.py` (omp sha/mtime) is the companion drift gate; not re-verified here
  beyond the hash match of the binary this analysis used.

## Evidence

- `sha256sum /home/vgpnk/.local/bin/omp` → `85d9daf3…ccfa4` (exit 0; matches the plan pin);
  `omp --version` → `omp/18.12.6`.
- Clone: `git clone` + `checkout 43ca0bfb` into
  `/fast/scratch/hyaku/kotoba-r51/build/ReviewSurfacesDesign/lane` (exit 0).
- `python3 -B verifiers/verify_surfaces.py --json` in the clone → exit 1,
  `{"exit_code": 1, "fail": 2, "pass": 5}` (matches the plan's Q19 before-value).
- `python3 -B verifiers/verify_surfaces.py --self-test` in the clone → `0 failure(s) over
  99 assertions`, exit 0.
- Census (python, on `strings -n 4` of the live binary, dump kept in scratch):
  11 loader-shaped calls, callees Kl×5/Ho×4/bq×2; S$ bindings at offsets 18159460 (`"title"`,
  line 843423) and 19656135 (`"claude-md"`, line 895604); calls at 19655920 (v$) and 19656208
  (S$); distances −73 / −1,496,748; opencode live dump 0 CALL_RE matches, extraction 0 pairs.
- Tooling directive: no tools installed or upgraded (python3, git, binutils `strings` sufficed).
- Lane writes: this report only.
