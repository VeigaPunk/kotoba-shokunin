verdict: The `omp:agents-md` family still exists in omp 18.12.5 and both baseline rows are witnessable, but the extractor pinned at BASE finds 0 of the 8 omp loader-group pairs — 18.12.5 moved the callees to `lq`/`Xl`/`Fo`; re-pinning to `(lq|Xl|Fo)` restores exact 8/8 parity with no extras (verified by running the patched verifier).

# C1 per-class witness — omp loader family `agents-md`

Scope: `verifiers/surfaces-baseline.json` at BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`, frozen snapshot
`/fast/scratch/kotoba-r47/shared/{bin/omp-18.12.5,omp-18.12.5.strings}`. Read-only; no production file edited.

## Substrate identity (observed)

| fact | value |
|---|---|
| BASE HEAD | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`git rev-parse HEAD`, exit 0) |
| binary sha256 | `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e` |
| strings sha256 | `33df0aeffc4565967bc1a3b42621f8eade0e6e4c2ae8733319fcd484902fb301` |
| `sha256sum -c SHA256SUMS` | 4× OK, exit 0 |
| `strings -n 4 bin/omp-18.12.5 \| sha256sum` | `33df0ae…b301` — byte-identical to the frozen dump, exit 0 |
| `HOME=/tmp/c1home bin/omp-18.12.5 --version` | `omp/18.12.5`, exit 0; `/tmp/c1home` left empty |

The dump line numbers below are coordinates in that frozen `omp-18.12.5.strings`.

## Rows in scope

Only two baseline entries carry this family (all 38 entries inspected; 8 are `loader-group`, 23 `loader-literal`, 7 `loader-config`):

- `omp:agents-md/AGENTS.md` — `verifiers/surfaces-baseline.json:6` (entry 5–11), `context_kind: loader-group`, governed.
- `omp:agents-md-walkup/AGENTS.md` — `verifiers/surfaces-baseline.json:111` (entry 110–116), `context_kind: loader-literal`, governed.

No other baseline row maps to group `agents-md`; `omp:omp-dir/AGENTS.md`, `omp:codex/AGENTS.md`, `omp:agents/*` are different families (their loaders are separate providers, see counterexample 5).

## Row 1 — `omp:agents-md/AGENTS.md` (loader-group): class exists

Exact registration and call shape, contiguous in the dump:

```
895125  // packages/coding-agent/src/discovery/agents-md.ts
895126  var f$ = "agents-md";
895127  var D7 = "AGENTS.md";
895128  async function CBt(u) {
895129    return lq(u, f$, "AGENTS.md");
895130  Le(Al.id, {
895131    id: f$,
895132    displayName: D7,
895133    description: "Standalone AGENTS.md files (Codex/Gemini style)",
895134    priority: 10,
895135    load: CBt
```

- The `(group, file)` pair is `("agents-md","AGENTS.md")`, materialised as `lq(u, f$, "AGENTS.md")` with a single binding `f$ -> "agents-md"` (verified through the verifier's own `constant_table`, `verifiers/verify_surfaces.py:299`; `grep -c 'id: f$'` = 1 — one registration only).
- Registration target is capability `context-files`: `var Al = Jo({ id: "context-files", …})` at 892076–892079. `Le` (`verifiers`-independent source at 861904) throws `Unknown capability` when the capability is absent and inserts providers in descending `priority` (`r.findIndex(o => o.priority < t.priority)`, 861917), so this is live bundle code, not inert metadata.
- Module is reachable: `var ya = () => import("/$bunfs/root/chunks/agents-md-tpy8365r.js")` at 1262029 and the module map entry `"@oh-my-pi/pi-coding-agent/discovery/agents-md": ya` at 1264032.
- `lq(e,t,n)` is a walk-up reader (862812): starts at `u.cwd`, joins `n` in each ancestor (`c.join(k, n)`, 862831), tags items `_source: Ze(t, C, "project")` (862844), and **skips** a hit whose containing directory basename starts with `.` (`if (!D.startsWith("."))`, 862836). Consequence: this loader reads `<ancestor>/AGENTS.md` but never `<ancestor>/.omp/AGENTS.md` or `<ancestor>/.agent/AGENTS.md`; those belong to other rows.

Baseline requirement check (`verifiers/surfaces-baseline.json:2`, `$comment`): a `loader-group` row needs the `(group, file)` pair "extractable as a .md call shape from the harness dump". It is extractable — but only after resolving `f$`; the literal pair never appears adjacent (`grep -a -c -F '"agents-md", "AGENTS.md"'` → 0, exit 1).

## Row 2 — `omp:agents-md-walkup/AGENTS.md` (loader-literal): class exists, id token is a census label

```
897785  // packages/coding-agent/src/discovery/agents.ts
897787  var jo = "agents";
897788  var ku = "Agent Dirs (.agent/.agents)";
897789  var Tu = 70;
897790  var HO = [".agent", ".agents"];
...
897938  async function wte(u) {
897948      ...Gj(u, "AGENTS.md").map((T) => p(T, "project")),
897949      ...Uj(u, "AGENTS.md").map((T) => p(T, "user"))
897952  Le(Al.id, {
897953    id: jo,
897954    displayName: ku,
897955    description: "Load AGENTS.md from .agent and .agents (project walk-up + user home)",
897956    priority: Tu,
897958    load: wte
```

- `Gj` (897840) walks `u.cwd` upward to `u.repoRoot ?? u.home`, joining `HO` entries; `Uj` (897838) covers home + WSL home. Both load the literal `AGENTS.md`. The description matches the census row verbatim (`corpus/knowledge/instruction-surface-census-round13.md:95`), so the hand-declared row's evidence is accurate.
- The class-id group token `agents-md-walkup` is **not** a binary literal: `grep -n 'agents-md-walkup'` → no hits, exit 1. The runtime provider id is `"agents"` (`var jo`), shared by six registrations of `id: jo` with the same display name `Agent Dirs (.agent/.agents)` and priority 70: skills (897865), rules (897884), prompts (897908), commands (897933), context-files/AGENTS.md (897953), system prompt/SYSTEM.md (897973). Under the baseline's own rule this row only requires literal presence (`verifiers/verify_surfaces.py:61–67`), which holds; no rule may grep the class-id token.

## Family sweep (commands + 0-hits)

| command | exit | result |
|---|---|---|
| `grep -n 'agents-md\|agentsMd\|agents_md'` | 0 | loader group 895126; module comment 895125; chunk paths 513555/600896/1262029/2440707–8; symbols `agentsMdFiles` 529368, `agentsMdSearch` 541933; config scope uses (below) |
| `grep -n 'agents-md-walkup'` | 1 | 0 hits |
| `grep -a -c -F '"agents-md", "AGENTS.md"'` | 1 | 0 |
| `grep -a -c -F '"agents-md"'` | 0 | 6 |
| `grep -n 'var Pqr = "agents-md"'` | 1 | 0 (round-13 census identifier gone) |
| `grep -n 'jDe(e,Pqr'` | 1 | 0 |
| `grep -a -c -F 'lq(u, f$, "AGENTS.md")'` (dump and binary) | 0 | 1 each |

The six quoted hits, classified: 895126 is the loader group; 895631 `values: ["none","agents-md","all"]` and 982847/982937/1072219 are the `snapcompact.systemPrompt` enum/scope (a UI/compaction setting that names AGENTS.md text, not a loader). A second copy of the description at 557674 sits among capability/UI catalog strings with no `load:` field — it is metadata, not a registration.

## Extractor status at BASE, and the re-pin

At BASE, `OMP_CALL_RE` (`verifiers/verify_surfaces.py:155–159`) allows `Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo`. On the frozen 18.12.5 dump it extracts **0** pairs. The verifier run confirms:

```
python3 verifiers/verify_surfaces.py --omp-strings <frozen> --opencode-strings <frozen> \
  --check surfaces.literal_present --check surfaces.no_uncovered_class      # exit 1
FAIL surfaces.literal_present: 8 loader literal(s) not verifiable: omp:agents-md/AGENTS.md
  (no (Id|Cl|jD[ef]|Tl|dr|GW|Co|Dl|Hj|I5|Gl|Mo)(<v>, <group>, "<file>.md") call shape
  for (agents-md, AGENTS.md) in omp dump); … (all 8 loader-group rows)
FAIL surfaces.no_uncovered_class: vacuity: 0 loader class(es) extracted … while the
  baseline declares 8 loader-group class(es) …; extractor blind: 33 declared literals
```

The live generation is `lq` (walk-up, 862812), `Xl` (user-level, 862506 → `nLe`, which joins `fO[group].userAgent` under `e.home` at 862502–862505) and `Fo` (project-level, 862510–862512, joins `fO[group].projectDir` under `cwd`). A broad scan of *any* 3-arg call whose third argument is (or resolves to) a `*.md` string finds 11 distinct call sites over the whole dump, yielding exactly 8 resolved pairs — the same 8 the baseline declares, no extras.

Proposed replacement (`C1ClassAgentsMd.patch`, 7 insertions / 7 deletions): `OMP_CALL_RE` → `(?:lq|Xl|Fo)`; `CALLEE_SHAPES["omp"]` → `'(lq|Xl|Fo)(<v>, <group>, "<file>.md")'`; docstring examples and the dated callee-history comment updated to the 18.12.5 generation. `CALL_RE` (opencode) untouched — `extract_classes` selects per harness at line 322. Old names are removed, not kept: on this dump they match 0 shapes, so add-only and replace-only are equivalent in extraction, and keeping dead minified names invites future over-match.

Verified on the patch in my scratch clone (`/fast/scratch/kotoba-r47/C1ClassAgentsMd-9/lane`, detach at BASE):

```
--check surfaces.literal_present --check surfaces.no_uncovered_class        # exit 0
PASS surfaces.literal_present: 38 loader-kind entries verified against the dumps
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
```

Full patched run (both frozen dumps, BASE census): `5 PASS / 1 FAIL`, exit 1; the only failure is `surfaces.opencode_extract` (opencode 1.19.3 substrate, another seat's item). Parity check of the proposed set: pairs 8, baseline loader-group pairs 8, `missing: []`, `extra: []`.

## Counterexamples / calibration hazards

1. **No adjacent pair.** `"agents-md", "AGENTS.md"` has 0 hits; extraction *must* resolve `f$`. A quoted-adjacency check would report the class absent while it exists.
2. **Name presence is not evidence.** `jDe` survives 3× but is an unrelated encoder (`function jDe(e, t, g, B = $9)` at 818391); `var Pqr` and `jDe(e,Pqr` are 0-hit. The round-13 census text (`census:73`) still quotes `jDe(e,Pqr,"AGENTS.md")` — historical, not a pin.
3. **Literal presence is not loader evidence.** 5 of 6 `"agents-md"` hits are the snapcompact setting; a `loader-literal`-style literal probe can pass for the wrong reason. (Row 1 is `loader-group`, so it gets the stricter check; row 2 is hand-declared by design.)
4. **The callee alone does not identify the class.** `lq` is generic: a third site `const Y = await lq(u, rb, X)` at 895850 with `var rb = "custom-context"` (895819) reads config-supplied filenames. Only the `(group, file)` pair discriminates.
5. **Dot-directory skip.** `lq` refuses hits under a `.`-prefixed directory (862836), so `omp:agents-md/AGENTS.md` cannot witness `.omp/AGENTS.md` or `.agent/AGENTS.md`; those rows belong to `omp:omp-dir` and the walk-up provider respectively.
6. **Walk-up id collision.** `omp:agents-md-walkup` runs under provider id `"agents"`, shared with six registrations; any future class_id→provider-id resolution for this row would collide with `omp:agents/*`.

## What I did NOT check

- Runtime firing or injection counts: this witnesses compiled-in registration and call shape only; no omp session was launched and no session transcript was read.
- opencode 1.19.3 (this seat is omp-only); the full patched run shows `surfaces.opencode_extract` still red — outside this item.
- `verifiers/baseline.json` pins and `check_substrate_pins.py` (other C1 seat); no pin was edited.
- Census/inventory edits and table parity for this id (other seat); the full patched run happened to report `table_parity`, `literal_parity`, `kind_parity`, `excluded_reason` PASS, but that is incidental, not this seat's witness.
- The BunFS chunk `agents-md-tpy8365r.js` was not opened separately; it is covered only through the binary-wide `strings` dump (which is byte-identical to `strings -n 4` of the frozen binary).
- No `~/.local/bin/opencode` execution, no network, no host-private reads.

## Artifacts

- `.ufo/waves/round-47/build/C1ClassAgentsMd.witness.json` — machine witness (rows, line coordinates, sweep exits, extractor status, parity).
- `.ufo/waves/round-47/build/C1ClassAgentsMd.patch` — proposed `verify_surfaces.py` re-pin; generated in the scratch clone, verified PASS on the frozen dumps. Diff prefixes are `i/`/`w/` (jj-colocated clone): apply with `git apply -p1`.
- No tool was installed or upgraded for this item.
