# ScoutPatternsR87 — re-derive the skill-root pattern set from the installed binary

Seat: ScoutPatternsR87 (scout, r87-w3). Scope: item 1 — derive the skill-root pattern set
from `/home/vgpnk/.local/bin/omp` (sha256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`)
read-only, then compare three ways: derived vs the round-86 ledger's `root_pattern` cells vs
the round-87 ledger's.

Nothing was edited. No verifier, plan, corpus or ledger file was touched. Receipts:
`.ufo/waves/round-87/w3/ScoutPatternsR87/`.

---

## 0. Method and the lane tip moved under me

**The lane tip is no longer the frozen statement's tip.** `git rev-parse master` printed
`760e1c5edfdefb4767420f711d08f669952de013` at the start of the seat and printed
`3c8902a7f2bd6977a7f9520a363013248a08b127` by the end; it advanced twice mid-run
(`d1c031833c37af99196f72f84a6643f84eec129a`, then `3c8902a7f2bd6977a7f9520a363013248a08b127`),
both landing round-87 attempt-2 commits. I measured **C1 at all three revisions** (it is
revision-addressed: it reads both ledgers with `git show`) and **C2 at the current tip only**
(C2 asserts `worktree tip == --rev` per addendum A1.2, so at any other rev it is exit 2,
"could-not-evaluate", not a verdict). Results in §4.

**Derivation was done before reading either ledger.** The method: a byte-offset regex scan
over the whole 276 785 328-byte ELF for the literal path segments, cross-checked with
`grep -aob`; then, for every root, the *composing code site* (the `path.join` that builds it)
was located in the embedded JS source region (~offset 173 M) and the resulting directory
was traced back to its base constant. The ledgers were read only afterwards, for the
comparison.

**A note on the item brief's arithmetic.** It says "the round-86 ledger's 13 `root_pattern`
cells vs the round-87 ledger's 12". Both files carry **12 data rows** (13 *lines* including the
header). `plans/round-87-addendum-1.md` § A1.1 already made exactly this correction ("The
plan's 13 is the ledger **file's** line count (header + 12)"), and the frozen counter's
`TOTAL = 12`. So r86 and r87 carry the **same 12 patterns**; the round-87 ledger is
*additive in columns* (it adds `module` and `reader_quote`), not in rows. I verified this:

```
$ diff <(cut -f1 verifiers/omp-skill-roots.tsv | tail -n +2) \
       <(cut -f1 verifiers/omp-skill-roots-semantics.tsv | tail -n +2)
(no output: identical)
```

---

## 1. The derivation

### 1.1 The literal path segments the ELF carries (`grep -aob`)

```
[.claude/skills]           114489017, 173847176
[.agent/skills]            114490041, 173866337
[.agents/skills]           114490059, 173866355
[.codex/skills]            114490735, 114490753, 173887174, 173887192
[.opencode/skills]         114492098, 114492120, 173905710, 173905732
[.github/skills]           114492709, 173911227
[.claude/plugins/cache/]   114489520, 173861919
[managed-skills]           114486708, 173809681, 173809957, ... (12 hits)
[.omp/skills]              (no hit)
[omp/skills]               (no hit)
```

The two offsets in each pair are the *string-table copy* (~114–116 M, the `Load skills from …`
description strings) and the *JS-source copy* (~173 M). Both are the same string in two places.

**`.omp/skills` does not exist as a contiguous string anywhere in the ELF.** The native root is
composed at runtime: `fr.join(k, Ou.projectDir, "skills")` with `Ou.projectDir` bound to
`var Gh = ".omp"` (offset 166 884 553). Likewise `.omp/plugins` has **zero** hits — the plugin
root is `h.join(p, qh(), "plugins")` + `h.join($o(p), "node_modules")` (offsets 166 892 325,
166 892 485), i.e. it never appears as one literal. This is the CF1 fact the round-86 closure
recorded, and it is why the round-87 ledger had to move to a *reader* quote.

### 1.2 The composing code site of every root

```
{cwd}/.omp/skills                [173819979]   dir: fr.join(k, Ou.projectDir, "skills"),
~/.omp/agent/skills              [173820135]   dir: fr.join(we(), "skills"),
~/.omp/agent/managed-skills      [173809938]   return Zm.join(u, "managed-skills");
{cwd}/.claude/skills             [173840364]   dir: Fr.join(k, eh, "skills"),
~/.claude/skills                 [173840218]   const x = p ? Fr.join(p, "skills") : null;
{cwd}/.agent(s)/skills           [173865724]   x.push(Rs.join(R, _, ...p));
~/.agent(s)/skills               [173865523]   return Wne(u).flatMap((x) => y1.map((R) => Rs.join(x, R, ...p)));
{cwd}/.codex/skills              [173882193]   const k = Xr.join(R, "skills");
~/.codex/skills                  [173882129]   const x = p ? Xr.join(p, "skills") : null;
{cwd}/.opencode/skills           [172785704]   return d.join(e.cwd, r.projectDir, n);
~/.config/opencode/skills        [172785499]   return d.join(e.home, r.userAgent, n);
{cwd}/.github/skills             [172785704]   return d.join(e.cwd, r.projectDir, n);
<plugin-root>/skills             [173914936]   dir: Zo.join(R.path, "skills"),
<agent-plugin>/skills            [173778070]   const _ = await FS(u, Ym.join(u, "skills"));
<claude-plugin>/skills           [173851107]   const k = li.join(u.path, p.fallback);
~/.omp/skillshare/@scope/*/*     [173923798]   function VH(u, p, x) {
```

Base constants (`var ZO = {` at 172 784 276) give each provider's `userBase`/`userAgent`/`projectDir`:

| provider | userBase / userAgent | projectDir |
|---|---|---|
| native | `qh()` = `.omp` (or `$PI_CONFIG_DIR`) | `.omp` |
| claude | `.claude` | `.claude` |
| codex | `.codex` | `.codex` |
| gemini | `.gemini` | `.gemini` |
| opencode | `.config/opencode` | `.opencode` |
| cursor | `.cursor` | `.cursor` |
| windsurf | `.codeium/windsurf` | `.windsurf` |
| cline | `.cline` | `null` |
| github | `null` | `.github` |
| vscode | `.vscode` | `.vscode` |

The binary registers **11 skill providers** (`Fe(zl.id, …)` — the `skills` capability):
`agent-plugins`, `native`, `managed-skills`, `claude`, `claude-plugins`, `agents`, `codex`,
`opencode`, `github`, `omp-plugins`, `skillshare`. Only `claude`, `agents`, `codex`, `opencode`
and `github` have a *fixed* literal `.X/skills` shape; the other four derive their root from a
plugin/extension/skillshare path.

---

## 2. `derived | r86 | r87`

18 derived roots. Offsets are the composing `path.join` site in the ELF.

| # | derived root | ELF offset | r86 | r87 |
|---|---|---|---|---|
| 1 | `{cwd}/.omp/skills` | 173819979 | yes | yes |
| 2 | `{cwd}/.claude/skills` | 173840364 | yes | yes |
| 3 | `{cwd}/.agent/skills` | 173865724 | yes | yes |
| 4 | `{cwd}/.agents/skills` | 173865724 | yes | yes |
| 5 | `{cwd}/.codex/skills` | 173882193 | yes | yes |
| 6 | `{cwd}/.opencode/skills` | 172785704 | yes | yes |
| 7 | `{cwd}/.github/skills` | 172785704 | yes | yes |
| 8 | `~/.omp/agent/skills` | 173820135 | yes | yes |
| 9 | `~/.omp/plugins/node_modules/*/skills` | 173914936 | yes | yes |
| 10 | `~/.agent/skills` | 173865523 | yes | yes |
| 11 | `~/.agents/skills` | 173865523 | yes | yes |
| 12 | `~/.omp/agent/managed-skills` | 173809938 | yes | yes |
| 13 | `~/.claude/skills` | 173840218 | **NO** | **NO** |
| 14 | `~/.codex/skills` | 173882129 | **NO** | **NO** |
| 15 | `~/.config/opencode/skills` | 172785499 | **NO** | **NO** |
| 16 | `~/.omp/skillshare/@scope/*/*` | 173923798 | **NO** | **NO** |
| 17 | `<plugin-root>/skills` (claude marketplace) | 173851107 | **NO** | **NO** |
| 18 | `<plugin-root>/skills` (agent plugins) | 173778070 | **NO** | **NO** |

**Every pattern r86 carries, r87 carries; r87 adds no pattern and drops none.** r86∩r87 = 12,
r86∩derived = 12, r87∩derived = 12.

### 2.1 Patterns one set has and another lacks

* **r86 vs r87: none.** The pattern columns are byte-identical (diff above). The round-87
  ledger is a strict column-superset of the round-86 ledger; it adds `module` and
  `reader_quote` only. This is exactly what the counter's guard S3 demands
  (`seen != root_patterns` → S3 FAIL), so S3 PASS *is* the statement that r87 did not
  re-scope the claim. The two ledgers cannot disagree about the pattern set without the
  counter refusing to run.
* **derived vs r86/r87:** six derived roots are absent from both (rows 13–18 above).

### 2.2 The commands that found nothing

* `grep -aob -- '.omp/skills' /home/vgpnk/.local/bin/omp` → no output.
* `grep -aob -- 'omp/skills' /home/vgpnk/.local/bin/omp` → no output.
* `grep -aoc -- '.omp/plugins' /home/vgpnk/.local/bin/omp` → `0`.
* `grep -aob -- '~/.omp/plugins/node_modules' /home/vgpnk/.local/bin/omp` → no output (the
  literal never exists; it is `$o()` + `"node_modules"`).
* `grep -aob -- '~/.claude/skills'` / `'~/.agent/skills'` / `'~/.agents/skills'` /
  `'~/.omp/agent/skills'` → no output. Only `~/.codex/skills` (114490733, 173887172),
  `~/.config/opencode/skills` (114492089, 173905701) and
  `~/.omp/agent/managed-skills` (114486695, 173820739, 274359845) exist as contiguous
  user-home literals.

---

## 3. Coverage holes and false rows

### 3.1 Holes — derived skill roots the round's model does not carry

**H1 — `~/.claude/skills` (offset 173840218).** `claude.ts` `Zte()` builds *two* roots: the
project walk-up `Fr.join(k, eh, "skills")` (173840364) and the user root
`Fr.join(p, "skills")` where `p = dl(u) = jp(home).configDir = ~/.claude` (the `jp()` helper is
at 170545531: `{ configDir: i.join(o, ".claude"), … }`). The user root is a real skills
directory the reader scans at `level: "user"`. The ledger carries only the `{cwd}` half.
**Not carried by r86 or r87.**

**H2 — `~/.codex/skills` (offset 173882129).** `codex.ts` `mre()` likewise builds both
`Xr.join(p, "skills")` with `p = Ia(u) = join(home, ZO.codex.userBase) = ~/.codex` (the
`Ia()` helper at 173879206) and the project `Xr.join(R, "skills")` (173882193). **Not carried.**

**H3 — `~/.config/opencode/skills` (offset 172785499).** `helpers.ts` `V$e()` /
`Ac()` builds the user root `d.join(e.home, r.userAgent, n)` with
`userAgent = ".config/opencode"`, and `os()` builds the project root
`d.join(e.cwd, r.projectDir, n)` with `projectDir = ".opencode"`. `opencode.ts` `Bre()`
scans both. **Not carried.**

> **H1–H3 are the sharpest form of the hole, because the ledgers' own `binary_quote` cells
> name them and the `root_pattern` column still omits them.** Row 5's quote is
> *"Load skills from `~/.codex/skills` and `.codex/skills/`"* and row 6's is *"Load skills from
> `~/.config/opencode/skills/` and `.opencode/skills/`"* — the quote cell asserts the
> user-home root exists in the binary, while the pattern cell carries only the `{cwd}` half of
> the same sentence. The same shape holds for the agents provider (rows 3/4/10/11), where
> both halves *are* carried, so the omission is not a uniform rule about user-level roots —
> it is an asymmetry between providers.
>
> Consequence for the counter: `check_omp_root_semantics.py` scores a row by four conjuncts
> (pattern equality, reader quote on a `join(` line, module header ordering, bound). It never
> asks whether the ledger is *complete*. So H1–H3 do not make C1 read less than 12/12 — they
> are invisible to the frozen predicate. That is a **model coverage hole for a later round**,
> not a counter defect: the predicate is "every row of the ledger is grounded", and every row
> is.

**H4 — `~/.omp/skillshare/@scope/*/*` (offset 173923798).** The `skillshare` provider
(`Mge`, registered at 173927899, description *"Registry skills installed with `omp skill
install` (skills.lock.json)"*) resolves each skill's store directory as
`VH(scope, name, version) = join(Tie(), "@"+scope, name, version)` where
`Tie() = join(dirname(we()), "skillshare")` (173923729) — i.e. `~/.omp/skillshare/@scope/name/version`,
each holding a `SKILL.md`. It is a genuine skill root; neither ledger carries it.

**H5 — `<claude-plugin-root>/skills` (offset 173851107).** The `claude-plugins` provider
(`qo`, *"Load skills from Claude Code marketplace plugins (~/.claude/plugins/cache/)"*)
resolves each plugin's skills dir as `li.join(u.path, p.fallback)` with `fallback = "skills"`.
The literal `.claude/plugins/cache/` is present (114489520, 173861919). The root is
*variable* (one per marketplace plugin), so it does not fit the ledger's fixed-shape
vocabulary — but it is a skill root the model does not describe.

**H6 — `<agent-plugin-root>/skills` (offset 173778070).** The `agent-plugins` provider
(`eb`, *"Portable Agent Plugins packages (plugin.json, skills/, mcp.json) per agent-plugins.org"*)
scans `Ym.join(u, "skills")` under each agent-plugin root. Same variable-root caveat as H5.

**Not a hole:** `~/.omp/plugins/cache/plugins/<name>___<ver>___<hash>/skills` is the *omp*
marketplace cache (registry.ts `If()` at 181916285, `P_()` shape at 181947465). It is a
marketplace plugin root, not a literal root string, and it is not covered by row 9's pattern
either (verified: `fnmatch` of `/home/u/.omp/plugins/cache/plugins/foo___1.0.0___abc/skills`
against `/home/u/.omp/plugins/node_modules/*/skills` → `False`). Listed here only to note that
row 9 covers the *npm* plugin root and not the *marketplace* plugin root.

### 3.2 False rows — carried rows that are not a skill root

**None.** All 12 carried patterns are real skill roots in the installed binary, and each has a
`path.join` site that composes it:

* rows 1–8, 10–12 — each confirmed by the offset in the table and by the base constant it
  resolves to (`.omp`, `.claude`, `.agent`/`.agents`, `.codex`, `.opencode`, `.github`,
  `agentDir`, `managed-skills`);
* row 9 `~/.omp/plugins/node_modules/*/skills` — the npm plugin root is
  `$o()/node_modules` (166892383 + 166892485) and `omp-plugins.ts` `uie()` composes
  `Zo.join(R.path, "skills")` (173914936) for each. The `*` in the first-segment position is
  the *only* wildcard in the whole table and it is in a non-first segment, which is what
  `pattern_problem()` allows (it forbids a wildcard only in the first segment).

So: **the ledgers are sound in what they assert** (no false row); they are **incomplete in
what they cover** (six holes). The incompleteness is not detectable by the frozen C1 predicate,
which is a *grounding* predicate, not a *coverage* predicate.

---

## 4. Counter measurements (read-only)

Full output: `.ufo/waves/round-87/w3/ScoutPatternsR87/counter-measurements.txt`.

| counter | rev | result | exit |
|---|---|---|---|
| C1 `check_omp_root_semantics.py` | base `223ae62424f8ab1eb365d733eb648d6228ddd7e8` | `grounded 0 of 12`, S3 FAIL | 1 |
| C1 | `760e1c5edfdefb4767420f711d08f669952de013` (frozen statement's tip) | `grounded 12 of 12`, S1–S3 PASS | 0 |
| C1 | `d1c031833c37af99196f72f84a6643f84eec129a` | `grounded 12 of 12`, S1–S3 PASS | 0 |
| C1 | `3c8902a7f2bd6977a7f9520a363013248a08b127` (current tip) | `grounded 12 of 12`, S1–S3 PASS | 0 |
| C2 `check_r86_routed_repairs.py` | `3c8902a7f2bd6977a7f9520a363013248a08b127` (current tip) | `r86 routed defects closed 4 of 5`; D1–D4 PASS, **D5 FAIL** | 1 |
| C2 | any non-tip rev (e.g. `d1c0318…`) | `could-not-evaluate: worktree tip … != measured revision …` | 2 |

C1's 12 row offsets are reproducible and identical at every rev (row 1 `@173819979` … row 12
`@173809938`). The base reading is `0 of 12` for the right reason: the semantics ledger does
not exist at the base rev, so S3 fails — a content verdict, not an environment error.

**C2's D5 drift is confirmed and unchanged.** The D5 red set at the current tip is
`['corpus.pointers.commit_unresolvable']` while the frozen predicate requires exactly
`['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead']` — i.e. `report_dead`
healed to 0 (the `.ufo/reports/round-84/kama.md` fleet report landed), so the red set is
*short* one member and the equality fails. This matches the frozen statement's description
exactly and is a **finding, not a repair** for this wave. Note the counter only measures the
worktree tip, so the "after-receipt at `35a395a9aabfe…`" measurement cannot be reproduced now
without a checkout at that rev (which would be a lane mutation and is out of scope for this
seat).

---

## 5. Risks and caveats

* **R1 — the tip moved twice under the seat.** Any receipt that names `760e1c5…` as "the tip"
  is stale; the C2 measurement is only reproducible at the then-current worktree tip, and
  `check_r86_routed_repairs.py` exits 2 (not 1) at any other rev, which a reader could
  misread as "the gate could not be evaluated" rather than "the gate is red".
* **R2 — the hole count depends on the ledger's vocabulary.** H1–H3 are unambiguous (fixed
  user-home roots the code composes). H5–H7 are *variable* roots (one per plugin package);
  the round-86/87 `root_pattern` vocabulary has no fixed-shape slot for them, and row 9's
  `*` shows the lane already resorts to a wildcard for the npm case. A later round must
  decide whether "a root per plugin package" is in scope before the hole count is fixed.
* **R3 — my derived set is a lower bound on the *string-table* view.** It is a complete set
  for the `skills` capability of the 11 registered providers, but I did not chase the
  `memory`/`skills` join sites at offsets 175861470 / 175864247 (the mnemopi memory-rollout
  `skills/` directory, `packages/mnemopi`), which is a *rollout artifact* directory, not a
  discovery root — excluded on that reading, and no reader in the ledger family points at it.
* **R4 — the ledger's `binary_quote` column is never checked by the counter.** `score()`
  unpacks `cells[0]`, `cells[2]`, `cells[3]` only; `cells[1]` (`binary_quote`) is parsed for
  arity but never matched against the ELF. All 12 `binary_quote` cells do occur verbatim in
  the ELF (verified, offsets in §1.1 and in the receipt), so nothing is false today — but a
  future row could carry a wrong `binary_quote` and still read GROUND. Worth a later round's
  attention; not a defect against the frozen predicate, which does not claim to check it.
* **R5 — no tool was installed.** No pacman transaction, no `uv tool install`, no new binary:
  the whole item is answerable with `grep`, `python3` and read-only `git`, all present. Per
  the operator tooling directive of 2026-10-19 there is therefore no tool/version/channel
  record to report.

---

## 6. Closing line

```
coverage: 18 derived, 12 matched, holes=[~/.claude/skills, ~/.codex/skills, ~/.config/opencode/skills, ~/.omp/skillshare/@scope/*/*, <claude-plugin-root>/skills, <agent-plugin-root>/skills], false=[]
```

Both ledgers carry 12 patterns, identically; all 12 are genuine skill roots in the installed
binary (no false row); six derived skill roots are absent from both (coverage holes for a
later round, three of them — H1–H3 — named verbatim by the ledgers' own `binary_quote` cells
while their `root_pattern` cells omit them). C1 reads 12 of 12 (exit 0) at every revision
measured; C2 reads 4 of 5 (exit 1) at the current tip, blocked by the D5 red-set drift.
