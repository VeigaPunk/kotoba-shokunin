# Kb82C04FalseRed — attack on loader-parser narrowing (C1 support, critic seat)

Seat: Kb82C04FalseRed (leaf; no subagent dispatch). Round 82, wave 1. 2026-10-30.
Base: `47dbe8781657de563ff867caca6244d28e3db504` (scratch `--shared` clone at
`/fast/scratch/hyaku/kotoba-r82/Kb82C04FalseRed/clone`, toplevel asserted before any git use).
Scope: attack the parser/input narrowing of the proposed loader fix — quoted vs variable
groups, repeated module vars, unresolved vars, renamed callees, non-md registrations,
decoys — and prove the accepted legitimate fixtures are preserved. Frozen dump artifact
`Kb82E12Loader-omp-18.14.0-strings.txt` (sha256 `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319`, re-verified this seat) used as data; the live binary was not re-read.

No production files mutated. No installs (pacman untouched). No after-data scored: the C1
counter was not run; the gate runs below are fixture/control worlds on committed fixture
copies plus the frozen strings dump as read-only data.

## VERDICT (up-front)

Two genuine fail-open holes in the round-52/51 loader-extraction narrowing, both
demonstrated end-to-end at the gate's own CLI against base `47dbe878`, both with red/green
controls; the smallest safe correction (2 hunks, +9/−3) flips both to loud red and keeps
the full self-test green — **0 failure(s) over 218 assertions under both base and
corrected gate** (accepted fixtures preserved). The other four attack axes reduce to
documented limits or to behavior *safer* than the docstring implies. One provenance defect
in a sibling artifact: `Kb82E01Paths-loader-pairs-18.14.0.txt`'s callee note ("ts, Ac")
omits `F9`, the callee that actually carries the two variable-group registrations.

- **HOLE A (unresolved vars)**: a new loader class whose group identifier cannot be
  settled, whose file is new, and whose callee has no declared-pair sibling call
  **silently vanishes** — exit 0, no mention anywhere. The documented grammar says an
  unresolved identifier "still surfaces as `<unresolved-var:NAME>`"; the round-52 P4
  admission narrowing (`f in declared_files`) contradicts it for exactly the
  new-class-discovery case the census exists to catch.
- **HOLE B (decoys / false provenance)**: a registration-call shape appearing on a
  `//` comment line is extracted as a compiled call — with the real registration removed,
  a single comment line mints `("claude-md","CLAUDE.md")` provenance and the gate passes
  8/8. This bundle lineage ships unminified chunks, so comment text is real attack
  surface on future bytes (absent on the current frozen dump).

## Method

`Kb82C04FalseRed-attack.py` (build artifact) imports the base gate's own functions
(`extract_classes`, `constant_table`, `module_scopes`, `scope_table`, `param_shadowed`,
`OMP_GENERIC_CALL_RE`, `ASSIGN_RE`) and runs 26 adversarial cases across the six assigned
axes, then sweeps the frozen 18.14.0 dump. `Kb82C04FalseRed-attack-corrected.py` repeats
every case against the corrected gate copy. `demo_holes.py` (kept in scratch; receipts in
build) drives the gate CLI on scratch copies of committed fixtures for the two holes.
Verdict tags: OK = behavior matches documented semantics; TRADE = documented limit or
accepted design tradeoff; HOLE = fail-open divergence from the gate's own documented
grammar.

## Findings by axis (base gate: 21 OK, 3 TRADE, 2 HOLE)

### 1. Quoted vs variable groups — OK (with two docstring corrections, not defects)

- Same callee mixing a variable group and a quoted group extracts both; the live
  mechanism is confirmed: `F9(u, nD, "AGENTS.md")` / `F9(u, rD, "CLAUDE.md")` with
  `nD`/`rD` each singly bound dump-wide (resolution "dump-wide", module fallback not
  needed); `Ac`/`ts` use quoted literals. 8/8 pairs.
- **Cross-module different-value override is impossible**: I predicted the dump-wide
  table could mis-resolve a call to another *declared* pair; the gate's drop-on-conflict
  fires dump-wide first, so a global-table entry exists only when *all* dump bindings
  agree — and then the own-module value necessarily matches. The docstring's "the
  dump-wide table wins wherever it has an entry" (lines 49–51) is **defensive-only, never
  observable**; the falsify arm (b2h) pins the real rule. Behavior is safe; the prose
  overstates a hazard that cannot occur.
- **Comment-line bindings cannot mis-resolve either**: a `// var nD = "…"` line feeds
  `ASSIGN_RE`; in the same module it *conflicts* with the real binding → unresolved
  (loud); in another module it adds a dump-wide conflict → own module still settles.
  Pollution can only over-conservatize. Live dump: **0** `ASSIGN_RE` matches on `//`
  lines (latent vector, not live).

### 2. Repeated module vars — OK

- One var reused by two callees in a module: both calls resolve. Identical rebind in one
  module (`var nD = "agents-md"; var nD = "agents-md";`): no conflict, resolves.
  Different-value rebind in one module: conflict → unresolved (b2g arm, confirmed).
- Own-module binding settles the call even when two other modules carry conflicting
  bindings (b2h-settled semantics confirmed with a declared value). A repeated module
  marker between binding and call splits the spans and the call falls back to the
  conflicted global table → unresolved — also loud, arguably over-strict for bundlers
  that re-emit markers, but fail-closed.

### 3. Unresolved vars — HOLE A (fail-open), fixable

- Declared-file case behaves: unresolved group + declared file admits the callee and
  surfaces `omp:<unresolved-var:S$>/CLAUDE.md` (b2j arm).
- **HOLE A**: unresolved group (`Z$` conflicted across two session modules) + **new file**
  (`NEWAGENT.md`) + callee `Q7` with no declared-pair call → the call is never admitted,
  never extracted, and never mentioned. CLI on `holeA-vanish.txt` (18.12.6 fixture + one
  appended synthetic module): **exit 0**, both loader checks PASS, `NEWAGENT` absent from
  output (`holeA-vanish.log`). The vacuity guard is silent (the other 7 pairs extract);
  `literal_present` only covers *declared* rows; a genuinely new loader class on a future
  binary would pass unnoticed — the exact discovery failure class the census gate exists
  to prevent. Control with the same loader registering a *declared* file:
  **exit 1**, `FAIL surfaces.no_uncovered_class: … omp:<unresolved-var:Z$>/AGENTS.md`
  (`holeA-declared-file-control.log`) — the `declared_files` qualifier is the whole
  difference. Adjacent tradeoff (not part of the hole): a brand-new callee with a quoted
  new pair also vanishes (`Q9(u,"brand-new","BRANDNEW.md")`, exit 0) — admission is a
  junk filter (the dump's `__accessCheck(obj, member, "read from private field")`-style
  3-arg calls force it), and that tradeoff is documented design. The fixable boundary is
  the unresolved case, where the documented grammar promises surfacing without a file
  qualifier.
- **Smallest safe correction** (hunk 2 of the proposed patch): admit any callee with an
  unresolved-group call, whatever the file —
  `or g.startswith("<unresolved-var:")` in place of the `declared_files` conjunction.
  Under it: hole A demo → **exit 1**, `FAIL … omp:<unresolved-var:Z$>/NEWAGENT.md`
  (`Kb82C04FalseRed-corrected-holeA.log`); b2j semantics unchanged (same red naming);
  all 218 self-test assertions still pass; attack harness vs corrected gate: HOLE 0.

### 4. Renamed callees — OK on live data; 1 TRADE

- Frozen-dump sweep: **0** `.md` registration shapes under any historical allowlist name
  (`Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo|lq|Xl|Fo|Kl|Ho|bq`) — the 18.14.0 rotation to
  `Ac/F9/ts` is total; the round-52 any-callee-admitted rule is what keeps working, and
  the E10/E13 conclusion "do not resurrect a callee allowlist" is correct.
- Dollar-suffixed callee (`d$`) matches the identifier grammar. TRADE: the callee
  character class is ASCII-only; an ES2015 non-ASCII callee (`éc(u, "gemini",
  "GEMINI.md")`) extracts nothing — alone it trips the vacuity guard (loud), alongside
  ASCII callees its pairs go missing → `literal_present` loud. The ASCII assumption is
  not written into the documented grammar; minified bundles are ASCII in every observed
  generation, so this is a documentation tradeoff, not a live defect.

### 5. Non-md registrations — TRADE (documented), live-absence note for the census refresh

- Same-shape non-md calls (`Ac(u,"cursor","rules")`, `"gemini"/"settings.json"`) are
  invisible by design; the frozen dump contains **no** 3-arg non-md registration shapes
  at all — the invisible set (`cursor/rules`, `gemini/settings.json`, `vscode/mcp.json`)
  is registered through non-call shapes on this lineage, so the census hand-declared
  rows cannot be extractor-verified and their continued truth is a manual check. Per the
  round-82 plan ("never silently delete a census class"), if the round-82 census refresh
  observes absence of any of these literals on 18.14.0, it must be documented as observed
  absence, not dropped.
- TRADE: the file argument is lowercase `.md` only; uppercase `.MD`/spaced file literals
  exist on the frozen dump only inside prose/CLI-example lines (973773, 974786, 977546,
  1189324, 1302288–89), never in a call shape. A case-insensitive-platform registration
  would be invisible; documented-limit wording says ".md-suffixed" without a case note —
  acceptable, worth one docstring word.

### 6. Decoys — HOLE B (false provenance), fixable; rest OK

- Confirmed existing defenses: member calls `o.x(...)` extract nothing (Q18); the
  alias decoy `q(u,"evil","EVIL.md")` is never admitted; wrong-arity/unquoted-file/
  trailing-space/empty-arg shapes do not match; escaped-string-embedded shapes do not
  match; case-variant group literals (`Claude-md` etc.) have zero occurrences on the
  frozen dump.
- TRADE: the any-callee rule has no reserved-word filter — the *text*
  `function(u, "gemini", "GEMINI.md")` extracts `("gemini","GEMINI.md")`. Not present in
  the frozen dump (11 shapes total); adjacent to HOLE B (text minting provenance) but
  reachable only via embedded docs/test strings.
- **HOLE B**: the call regex is not line-anchored. On `holeB-comment.txt` (real
  claude-md registration removed, one comment line `// bq(u, "claude-md", "CLAUDE.md");`
  added to the 18.12.6 fixture copy): extraction still yields the pair, the gate passes
  **exit 0**, 8/8 (`holeB-comment.log`). Control without the comment: **exit 1**,
  `FAIL surfaces.literal_present: … omp:claude-md/CLAUDE.md (no … call shape …)`
  (`holeB-control.log`). The round-21 note for this lineage says the bundle ships
  *unminified source chunks* — comments are retained bytes, so on future dumps a stale
  or docs comment can witness a loader that was deleted. Provenance rule violated: a
  compiled-in call shape is supposed to prove the loader path exists in the binary; a
  comment proves nothing. On the current frozen dump the exposure is latent: all 11
  shapes sit on non-comment lines in `src/discovery/*.ts` (verified line-by-line).
- **Smallest safe correction** (hunk 1 of the proposed patch): skip matches whose line
  prefix (text from the last newline to the match) lstrip-starts with `//` or `/*`.
  Real registration calls cannot live on comment lines, so this cannot reject a true
  positive. Verified: hole B demo → **exit 1** naming the missing class
  (`Kb82C04FalseRed-corrected-holeB.log`); no committed fixture has any shape or
  assignment on a comment line (checked all omp fixture files), so all 218 self-test
  assertions still pass; attack harness vs corrected gate: HOLE 0.

## Provenance defect in a sibling artifact (not the gate)

`Kb82E01Paths-loader-pairs-18.14.0.txt` records "active registration callees observed:
ts, Ac (literal-group forms)". The frozen dump carries **three** callees: `Ac` ×5,
`ts` ×4, and `F9` ×2 — and `F9` is precisely the callee of the two *variable-group*
registrations (`nD`/`rD`), while `Ac`/`ts` are the literal-group ones. The 8 pairs in the
artifact are correct (E10/E13/this seat agree 8/8 both directions), but the parenthetical
is wrong on both counts. If its text is reused in the S251 loader-refresh entry or Gate
quote, it must read "Ac, F9, ts — Ac/ts literal-group; F9 carries the variable-group
registrations nD→agents-md, rD→claude-md" (or be recomputed from
`Kb82E10Loader-probe-report.json` / `Kb82E13Loader-probe-report.json`, which have it
right).

## Corrected-gate validation summary (fixtures preserved)

| evidence | base gate | corrected gate |
|---|---|---|
| `--self-test` | exit 0, `0 failure(s) over 218 assertions` | exit 0, `0 failure(s) over 218 assertions` |
| attack harness (26 cases) | 21 OK / 3 TRADE / 2 HOLE | 23 OK / 3 TRADE / 0 HOLE |
| HOLE A CLI demo | exit 0, class invisible | exit 1, names `omp:<unresolved-var:Z$>/NEWAGENT.md` |
| HOLE B CLI demo | exit 0, comment provenance | exit 1, names `omp:claude-md/CLAUDE.md` |
| HOLE A/B controls | exit 1 (both) | exit 1 (both, unchanged) |

Suggested new self-test arms for L1 (encode the counterexamples; both fail on base, pass
on corrected): (1) append `// x.ts\nfunction f(u){ return Q7(u, Z$, "NEWAGENT.md"); }`
with `Z$` conflicted across two other modules to the 18.12.6 fixture, expect exit 1
naming `omp:<unresolved-var:Z$>/NEWAGENT.md`; (2) same fixture with the real claude-md
registration replaced by a `//` comment carrying the shape, expect exit 1
`FAIL surfaces.literal_present` naming `omp:claude-md/CLAUDE.md`.

## Boundaries / non-claims

- The opencode rule extractor (OC-1..OC-6) is out of this seat's scope; no claim on it.
- The two holes are **latent on the current host bytes**: the frozen 18.14.0 dump shows
  0 unresolved-var shapes, 0 comment-line shapes, 8/8 pairs via Ac/F9/ts. Nothing here
  re-scores C1 or touches the counter; the re-pin predicate remains L1's unchanged
  round-72 counter run.
- TRADE items (ASCII callee class, lowercase `.md` only, non-md outside set, admission
  junk filter, keyword-shaped text) are documented-limit or accepted-tradeoff class;
  the canonical judge should reject treating them as defects, and reject any "fix" that
  drops the admission filter (would mint classes from `__accessCheck`-style junk).
- No subagents, no commits/pushes, no jj mutation, no production file touched; scratch
  clone deleted after receipts copied.

## Receipts (build artifacts; hashes in `Kb82C04FalseRed-SHA256.txt`)

- `Kb82C04FalseRed-attack.py` / `Kb82C04FalseRed-attack-report.json` — 26-case harness vs base gate
- `Kb82C04FalseRed-attack-corrected.py` / `Kb82C04FalseRed-attack-corrected-report.json` — same vs corrected gate
- `Kb82C04FalseRed-proposed-fix.patch` — 2 hunks, +9/−3 (comment-line guard; unresolved admission widened to any file)
- `Kb82C04FalseRed-selftest-base.log` / `Kb82C04FalseRed-selftest-corrected.log` — 218/218 both
- `holeA-vanish.log`, `holeA-declared-file-control.log`, `holeB-comment.log`, `holeB-control.log` — base-gate CLI receipts
- `Kb82C04FalseRed-corrected-holeA.log`, `Kb82C04FalseRed-corrected-holeB.log` — corrected-gate CLI receipts
- `holeA-vanish.txt`, `holeA-declared-file.txt`, `holeB-comment.txt`, `holeB-control.txt`, `baseline-with-newagent.json` — demo inputs (scratch copies of committed fixtures + synthetic modules)

Measurement evidence: frozen dump sha256 `81277d3572277febcaf0853f10cf8778c64920f58a13fba98ef0accbb70a8319`; clone at `47dbe8781657de563ff867caca6244d28e3db504` (toplevel asserted); no installs; pacman untouched.

VERDICT: 2 fixable fail-open holes in the loader-parser narrowing (unresolved-var new-class vanishes; comment-line shape mints provenance), each demonstrated end-to-end with red/green controls; minimal +9/−3 correction flips both loud and preserves all 218 accepted fixture assertions; 4 axes reduce to documented limits; sibling artifact Kb82E01Paths callee note ("ts, Ac") is wrong — F9 is the third callee and carries both variable-group registrations.

DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82C04FalseRed.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C04FalseRed-attack.py ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C04FalseRed-attack-report.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C04FalseRed-attack-corrected.py ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C04FalseRed-attack-corrected-report.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C04FalseRed-proposed-fix.patch ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C04FalseRed-selftest-base.log ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C04FalseRed-selftest-corrected.log ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C04FalseRed-corrected-holeA.log ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C04FalseRed-corrected-holeB.log ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/holeA-vanish.log ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/holeA-declared-file-control.log ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/holeB-comment.log ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/holeB-control.log ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82C04FalseRed-SHA256.txt
