# CriticSemanticsR87 — attack on C1's root semantics (read-only)

Seat: critic (leaf). No subagents. No lane file outside this report and
`.ufo/waves/round-87/w3/CriticSemanticsR87/` was written; `verifiers/`, `plans/round-87*.md`,
`corpus/SOURCES.md`, `corpus/QUALITY.md`, `LOG.md`, `SCORECARD.md`, `SKILL.md` untouched.
Receipts: `.ufo/waves/round-87/w3/CriticSemanticsR87/` (`attrib.py`, `worlds.sh` are copied there).

## 0. Tip status (the brief's tip is no longer master)

At seat start `git -C …/kotoba-shokunin rev-parse master` printed the brief's
`760e1c5edfdefb4767420f711d08f669952de013`. During the seat another seat advanced master to
`d1c031833c37af99196f72f84a6643f84eec129a` ("round-87 attempt 2 …"). The worktree is **detached**
(`git symbolic-ref HEAD` → `fatal: ref HEAD is not a symbolic ref`; `status -sb` → `## HEAD (no
branch)`), currently at the same `d1c0318`.

Both revisions measured; `d1c0318` differs from `760e1c5` in `.ufo/waves/**`, `LOG.md`,
`SCORECARD.md`, `corpus/QUALITY.md`, `corpus/lessons/round-87.md` only — **no verifier and no
ledger changed** (`git diff --name-only 760e1c5 d1c0318 -- verifiers plans/round-87.md …` → those
four files). Receipt: `c1-tip.txt`.

    $ python3 -B verifiers/check_omp_root_semantics.py --rev 760e1c5edf…
    omp root semantics grounded 12 of 12
    exit=0                                   EXIT=0
    $ python3 -B verifiers/check_omp_root_semantics.py --rev d1c03183…
    omp root semantics grounded 12 of 12
    exit=0                                   EXIT=0

`--self-test` on the frozen counter: `0 failure(s) over 35 assertions`, exit 0 (`selftest.txt`).
The arithmetic is reproducible at both tips.

## 1. Are the 12 `reader_quote`s code? — yes, all 12, verified byte-wise

Method: `grep -aob` for each quote, `od -A d -c` around it, and a nearest-header probe
(`attrib.py`: all 3131 `// packages/<module>` headers, then bisect per quote). Full dumps in
`elf-bytes.txt`, `attribution.txt`.

| row | root_pattern | quote offset | enclosing bytes read as | verdict |
|---|---|---|---|---|
| 9 | `~/.omp/plugins/node_modules/*/skills` | 173914936 | `async function uie(u){ const p = await vd(u,"skills"); … p.map((R)=>Ba(u,{ dir: Zo.join(R.path, "skills"), providerId: xo, level: R.level, …` | **executable** function body |
| 6,7 | `{cwd}/.opencode/skills`, `{cwd}/.github/skills` | 172785704 | `function os(e,t,n){ const r = ZO[t]; if(!r.projectDir) return null; return d.join(e.cwd, r.projectDir, n); }` | **executable**; literals in the `ZO` table 500–900 B earlier (`.opencode`@172784794, `.github`@172785178) |
| 5 | `{cwd}/.codex/skills` | 173879095 | `function ul(u){ return Xr.join(u.cwd, ".codex"); }` | **executable**, but a **prefix** (see §5) |
| 1,8 | `{cwd}/.omp/skills`, `~/.omp/agent/skills` | 173819979 / 173820135 | `for await (const {dir:k} of dFe(u)) { … dir: fr.join(k, Ou.projectDir, "skills") … }` / `dir: fr.join(we(), "skills"),` | **executable** function bodies |
| 12 | `~/.omp/agent/managed-skills` | 173809938 | `function w9(u = we()){ return Zm.join(u, "managed-skills"); }` | **executable** |
| 2 | `{cwd}/.claude/skills` | 173840364 | walk-up loop `while(true){ … dir: Fr.join(k, eh, "skills"), … k = Fr.dirname(k) }` with `var eh = ".claude"` 6 lines earlier in the chunk | **executable** |
| 3,4 | `{cwd}/.agent/skills`, `{cwd}/.agents/skills` | 173865724 | `function V9(u,...p){ … for (const _ of y1) { x.push(Rs.join(R, _, ...p)); } … }`, `y1 = [".agent",".agents"]`@173864226 | **executable** |
| 10,11 | `~/.agent/skills`, `~/.agents/skills` | 173865523 | `function z9(u,...p){ return Wne(u).flatMap((x)=> y1.map((R)=> Rs.join(x, R, ...p))); }` | **executable** |

No row is a doc or literal-table line. The ELF embeds the pretty-printed transpiled bundle
(3131 module chunks, 166.87–194.31 MB), not a string table of prose; every quote sits inside a
function body and the surrounding bytes carry `function`/`const`/`return`/`map(` syntax. Item 1
**passes for all twelve rows**, including the plugin root and every `{cwd}/` row.

## 2. Module attribution — honest rows are correctly attributed; the check is only ordering

`attrib.py` computes, per row, the nearest preceding header of **any** module and the nearest
following header:

    row  1 nearest preceding header (any) @173814223 coding-agent/src/discovery/builtin.ts    (== module)
    …
    row 12 nearest preceding header (any) @173809642 coding-agent/src/autolearn/managed-skills.ts (== module)

All 12: `nearest preceding header == row module`, and each quote occurs **exactly once**. So the
landed attribution is not "nearest header by luck of offset" — each quote really is inside the
chunk its module cell names. Upstream confirms the same mapping (§4).

But that is a fact about the data, not about the conjunct. Conjunct 3 only tests
`first_reader >= last_header(module)`, so a quote in a *different* module passes whenever it lies
later in the bundle. Measured (`forgery-worlds.txt`, world 3): row 12
`~/.omp/agent/managed-skills` set to the omp-plugins quote at 173914936 — 105 KB and several
modules after `managed-skills.ts`'s only header — still reads **12 of 12, exit 0**.
No landed row's attribution is doubtful; the attribution *check* is unsound.

## 3. The invited falsification — yes, the counter passes a wrong quote

I built four worlds in a scratch clone (`git clone --shared`, toplevel asserted; ledger cells
mutated; frozen counter run through its documented `--repo`/`--rev`), each committed with the
forged cells shown in `forgery-ledger-diffs.txt`:

| world | change | counter |
|---|---|---|
| `w_cross_row7` | row 7 `{cwd}/.github/skills` quote := `return Xr.join(u.cwd, ".codex");` (module cell left `helpers.ts`) | **12 of 12, exit 0** |
| `w_subdir_row9` | row 9 plugin-skills quote := `Zo.join(R.path, "commands")` (the same module's *commands* subdir) | **12 of 12, exit 0** |
| `w_misattr_row12` | row 12 quote := `dir: Zo.join(R.path, "skills"),` (different module chunk) | **12 of 12, exit 0** |
| `w_renderline_row6` | row 6 quote := `**Tags:** ${t.tags.join(", ")}` (markdown-rendering template, Array#join) | **12 of 12, exit 0** |

So a row passes all four conjuncts while the quoted call constructs a different path than
`root_pattern` names — three distinct ways. This is decisive against the *evidence standard*, not
against the landed ledger: the counter is a presence+ordering test, and a quote that names no
segment of the row is indistinguishable from one that names it.

`w_renderline_row6` also falsifies conjunct 2's docstring claim ("a doc/string-table line cannot
satisfy it"): `JOIN_TOKENS` includes `.join(`, which matches `Array#join` at ELF 188589625 inside a
markdown template literal. `resolve(` likewise matches `Promise.resolve()` (52 private-field lines,
e.g. `#e = Promise.resolve();` at 895876). The token set is not path-qualified.

## 4. What would settle it mechanically, and what is available this round

- **Upstream source diff — available and used.** `raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/…`
  fetched read-only: `omp-plugins.ts` 15 362 B sha256 `4e66819cf706b81c…` — **byte-identical to
  S256's pin**. Upstream confirms every honest row: `path.join(root.path, "skills")` (oms-plugins
  line 70), `getProjectPath` = `path.join(ctx.cwd, paths.projectDir, subpath)` with
  `".github"`/`".opencode"` in `SOURCE_PATHS` (helpers.ts:88-96,130-135),
  `codexDir = …` + `projectSkillsDir = path.join(codexDir, "skills")` (codex.ts:267-268),
  `path.join(dir, PATHS.projectDir, "skills")` / `path.join(getAgentDir(), "skills")`
  (builtin.ts:310-327). Receipt: `upstream.txt`.
- **Live load probe — not available this round.** `omp --help` exposes no discovery dump:
  `--skills=<glob>` only filters, `--no-skills` disables, and the `skill` command is the Skillshare
  registry CLI. A probe would need a model session and, even then, would only show that a placed
  `SKILL.md` is found — it cannot separate "quote builds root" from "table names root".
- **Decompiler pass — unnecessary.** The bundle is not bytecode to decompile; it is transpiled JS
  source text embedded in the ELF, which is what I read. The residual gap is a Bun source↔executed-
  unit correspondence proof, which none of the three probes supplies either.

## 5. Row-level semantics: where the quote does not build the named path

The claim's strong reading is "the quoted call constructs `root_pattern`". Under that reading:

- **Row 5 (`{cwd}/.codex/skills`) — definite gap.** The quote builds `{cwd}/.codex` only. The
  `skills` segment is a *different* statement 3 098 B later in the same chunk:
  `const k = Xr.join(R, "skills");` @173882193 with `R = ul(u)`; upstream codex.ts:267-268 is
  `codexDir = getProjectCodexDir(ctx)` then `projectSkillsDir = path.join(codexDir, "skills")`.
  The ledger could have quoted the exact skills join; it quoted its parent. 12/12 is unaffected.
- **Row 9 (plugin) — composite.** The quote builds `<pkg>/skills`; the
  `~/.omp/plugins/node_modules` prefix is `yo.join(u, "node_modules")` @173767158 in
  `extensibility/plugins/loader.ts`, with the roots supplied by `X9(u)`/`Iu`/`extensionRoots`.
  The row's module cell names only the terminal join.
- **Rows 6/7 — composite but same module.** Generic `cwd + projectDir + subpath`; the literals
  `.opencode`/`.github` are `SOURCE_PATHS` entries in the same chunk, before the quote. The quote
  alone would equally "ground" `.vscode`, `.cursor` or `.claude`.
- **Rows 1/8/12 — base composite.** `.omp` is `Gh` in `utils/src/dirs.ts` @166884553 and
  `we()` is `return c.agentDir;` @166891738 (profile-aware config property), so the `~/` base is
  not in the quoted line.
- Rows 2, 3, 4, 10, 11 — literal in the same chunk (`eh`, `y1`), quote is the join; acceptable
  under the weaker "the code that joins the path" wording.

The counter cannot express any of this: conjunct 1 never looks at the quote, and 2/3/4 never look
at the pattern.

## 6. C2 context measured (not my item; context for the wave)

    $ python3 -B verifiers/check_r86_routed_repairs.py --rev d1c03183…
    PASS d1 … PASS d2 … PASS d3 … PASS d4
    FAIL d5  verifiers/verify_corpus_integrity.py red set ['corpus.pointers.commit_unresolvable'],
             want exactly ['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead']
    r86 routed defects closed 4 of 5        EXIT=1

Confirming the brief: `report_dead` healed to 0. Two structural notes for the wave, not repairs:
D5(iii)'s truth depends on a **fleet-root** file outside this lane, so the claim can flip with no
lane commit; and addendum-1 §A1.2's guard compares `git rev-parse master`, not the worktree's
checked-out commit — observed `## HEAD (no branch)` detached at d1c0318 (equal today, so no
divergence today).

## Findings (frozen counter — findings only, nothing edited)

1. **F1 — conjuncts 2+3 do not bind quote to pattern** (measured, four worlds at 12/12). The
   predicate cannot detect a wrong quote; it detects presence, a join token and file order.
2. **F2 — the doc-exclusion is false as implemented**: `JOIN_TOKENS` matches `Array#join` and
   `Promise.resolve` (markdown template line @188589625 passes as a "reader").
3. **F3 — row 5's landed `reader_quote` is a strict prefix** of its pattern (missing `/skills`);
   the knowledge entry's table overstates that row under its own wording.
4. **F4 — module attribution is only ordering**: a quote 105 KB later in another module passes
   (measured). Honest rows are lucky/attributed correctly, which I verified independently.

Smallest safe correction (for a later round; not applied): require the row's root-naming token to
co-occur within a bounded window of the quote (row 6/7: `.github`/`.opencode` at ±1 KB — measured
at 172785178 / 172784794), and make `JOIN_TOKENS` path-qualified (drop bare `.join(`, or require
`path.join(`/`<ns>.join(` where `<ns>` is a path import); for the plugin row, where no literal
exists, add a second cell carrying the prefix builder (`yo.join(u, "node_modules")` +
`loader.ts`) rather than weakening the row. Row 5 should quote `const k = Xr.join(R, "skills");`.

## Verdict

**semantics: partially-grounded** — the twelve landed quotes are executable join code inside the
modules the ledger names (independently confirmed against upstream v18.15.0, `omp-plugins.ts`
sha256 equal to S256), and the 12/12 reading reproduces at both tips. But the frozen conjuncts do
not establish the claim per row: a wrong or partial quote passes (four measured worlds at
`12 of 12, exit 0`), the doc-exclusion is false as implemented, and row 5's quote builds a strict
prefix of its pattern.

Rows carrying the doubt: **5** (definite: `{cwd}/.codex` vs `{cwd}/.codex/skills`), **9**
(prefix `~/.omp/plugins/node_modules` built in `loader.ts`), **6, 7** (generic `projectDir` join,
literals in `SOURCE_PATHS`), **1, 8, 12** (base `c.agentDir` in `utils/src/dirs.ts`).

## Risks

- The 12/12 number is reproducible but is a presence test; a forged ledger reads identically
  (demonstrated). Anyone reading C1 as proof of per-row semantics reads more than the counter tests.
- C2's D5(iii) can flip on another actor's fleet commit (measured: 4 of 5 now, 5 of 5 in the
  round's receipt).
- The D5 worktree guard does not pin the worktree's checked-out commit (detached HEAD observed).
