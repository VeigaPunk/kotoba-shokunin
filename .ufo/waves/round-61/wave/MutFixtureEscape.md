# MutFixtureEscape — W8: a world that passes all four v3 arms while the landed row is false

Seat: `kotoba-r61-wave-MutFixtureEscape` (leaf; no subagent, no dispatch, no ask tool).
Date: 2026-10-23. Read revision: `c630c4cbc01ff5e5438ab0033cfadd6e19382ab1` (lane tip at
first read; plan base `f3246d1493b60ea1c0d947a19c39f9e08e92f326`). The tip carries erratum
E1 (C3 withdrawn as a counted claim); that does not touch this probe.

Lane and fleet were read-only. The only lane write is this report. Scratch
(`/fast/scratch/hyaku/kotoba-r61/MutFixtureEscape/`) is untrusted and is cited only as a
location for re-runnable scripts, never as evidence. No install was needed or made.

**Deliverable in one line.** A single-cell world (`W8`, Cursor Action cell only) in which the
v2 predecessor scores 4 of 4 backed, and which satisfies every clause of the frozen v3 arm
sentences A1, A2 and A4 unconditionally and A3 subject to a pre-existing dataset conflict
that is measured in §4.2 below. The landed cell is semantically false: it asserts a
Team-Rules-only default of **Project** Rules. Included: the honest bound sentence the entry
must carry, and the two escape variants the assignment names (stale-version content, quote
shaping with `&#124;` and wider normalizer channels).

---

## 0. Mutant / detector / output / verdict / restoration (the protocol block)

| field | value |
|---|---|
| mutant | `SKILL.md`, section `### Scoped rule files by client`, Cursor row, **Action cell only**: `Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131)` → `Rules without a glob pattern apply to every conversation (S108 :305)`. All other bytes of the four-row world are the committed r60 world. |
| expected detector | The v3 world runner (or the v2 `judge()` path the CLI uses) on the pristine world and on the mutant. Expected **mutant result: Cursor row backed, total 4 of 4 → the escape SURVIVES**. A kill would name A1/A2/A3/A4 in a reject line for Cursor. |
| actual output | pristine 4 of 4 backed; mutant 4 of 4 backed; Cursor `why == []`; escaped cell `action_conjunct == []`, five content words (`need=3`, `shared=5`), strict substring of the cited line `True` (full output §1.2). |
| verdict | **SURVIVED under v2 (measured).** **v3: NOT RUN** — no v3 source exists in the lane at read time (§1.1); survival under the landed v3 is the residual falsify call. |
| restoration | No lane byte was written. Every file used has `git hash-object` = `git rev-parse HEAD:<path>` (Annex B). The counter copy is byte-identical to the lane counter (`ca2585a4…`). "Restored" is the same run as pristine: 4 of 4. |

The direction is inverted from a kill-world by design: this world is a **survivor fixture**
for the escape class, not one of the seven kill worlds. If the L1 adds it to the self-test it
must be reported as `W8 pass 4 of 4` (a survived escape), never folded into `worlds reject
7 of 7`; folding it in would make that line false.

---

## 1. Ground, detector, and what is not run

### 1.1 The v3 source does not exist yet (so nothing here is a v3 measurement)

At read time `verifiers/` holds `check_scoped_rules.py` at v2 only:

```text
$ date -u
Fri 23 Oct 2026 07:17:26 PM UTC
$ sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  …/verifiers/check_scoped_rules.py
$ cd /fast/scratch/hyaku/kotoba-r61/MutFixtureEscape && python3 -B probe/run_world.py   # first four lines; full run in §1.2
counter copy sha256 : ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
lane counter sha256 : ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
TARGET = 3 | BASE = 31092dc6f875370bddd6eb1e4da4ca0d210c56af
lane SKILL.md sha256 : 2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909
exit=0
```

The four frozen arms exist only as sentences in `plans/round-61.md:23–39`. A2's
"supported by text" and A4's "verbatim" have no committed implementation to interrogate.
Every statement below about v3 is therefore a statement about the **frozen sentences**, and
the detector actually executed is the committed **v2** `judge()` — the same function the v2
CLI calls per row (§1.2). This is stated once and not repeated as a caveat on every line.

### 1.2 Detector actually run

The probe imports a byte-identical copy of the committed counter and calls its own
`judge(skill, entry, sources, lesson, base_sources, snapshot_of=…)`. The inputs are the
committed lane bytes (read-only) and the committed r60 snapshots; `base_sources` is
`git show 31092dc6:corpus/SOURCES.md` — the v2 `BASE`, i.e. the table in which the four
eligible rows are *new*. No git commit, no checkout, no lane write was made.

Reproduction:

```sh
$ cd /fast/scratch/hyaku/kotoba-r61/MutFixtureEscape
$ python3 -B probe/run_world.py
```

```text
Fri 23 Oct 2026 07:21:22 PM UTC
counter copy sha256 : ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
lane counter sha256 : ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
TARGET = 3 | BASE = 31092dc6f875370bddd6eb1e4da4ca0d210c56af
lane SKILL.md sha256 : 2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909

pristine (r60)         backed 4 of 4 (Claude Code, VS Code, Copilot CLI, Cursor)
W8-min (cursor)        backed 4 of 4 (Claude Code, VS Code, Copilot CLI, Cursor)
W8-stale (claude)      backed 4 of 4 (Claude Code, VS Code, Copilot CLI, Cursor)
W8-both                backed 4 of 4 (Claude Code, VS Code, Copilot CLI, Cursor)
W8-full (all three)    backed 4 of 4 (Claude Code, VS Code, Copilot CLI, Cursor)

cursor action: conjunct=[] |W|=5 need=3 shared=5 missing=[] strict_substring=True
claude action: conjunct=[] |W|=10 need=5 shared=10 missing=[] strict_substring=True

quote shaped words: 23 | quote_why(shaped): [] | quote_why(true): []
norm('always_apply') == norm('alwaysApply'): True
literal shaped quote bytes in page: False
S106 landed quote words: 10 | literal bytes in page: False | page_plain literal: True | norm: True
entity &#124;       quote_why=[]
entity &#x7C;       quote_why=[]
entity &vert;       quote_why=[]
entity &#0000124;   quote_why=[]
cross-line window words: 18 | quote_why: [] | literal bytes: False

landed actions: strict substring of cited line and content-word coverage
  Claude Code  |W|=11 shared=10 missing=['scope'] substring=False
  VS Code      |W|= 6 shared= 5 missing=['instruction'] substring=False
  Copilot CLI  |W|=12 shared= 9 missing=['instruction', 'path', 'specific'] substring=False
  Cursor       |W|= 9 shared= 9 missing=[] substring=True

S049 URL: https://cursor.com/docs/rules.md | S108 URL: https://cursor.com/docs/rules
url_key equal: True | byte-identical: False
reopen_why (landed): []
exit=0
Fri 23 Oct 2026 07:21:22 PM UTC
```

Baseline (`pristine`) passes 4 of 4, so a 4 of 4 mutant result is conclusive against v2, not
a baseline failure. The world's own row-by-row reasons are empty; the only rejections are the
three clients the world (like the r60 world) deliberately leaves out of `K`.

### 1.3 Not run / not verifiable by me

- No v3 execution (source absent). The arm-pass argument is by construction against the
  frozen sentences, plus measured v2 behaviour.
- The contents of S112–S115 (A1's canonical-key ground) were not opened by me; the world
  assumes Cursor's canonical key is `globs`, as the plan's own A1 example and the r60 row
  use it. If S112–S115 say otherwise, the r60 Cursor row itself fails A1.
- The live `--fetch` path on W8 was not run; it belongs to the L1 after integration. The two
  construction GETs in §4.2 are the only network calls made, and they are recorded with date,
  status, bytes, and sha.
- The v3 fixture mechanism (self-test world builder vs `--world` flag) is not fixed in the
  lane; Annex A gives the content either way.

---

## 2. The world

### 2.1 The one behavior-bearing mutation

Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/SKILL.md`, section
`### Scoped rule files by client`, the Cursor row. Replace **only the fourth cell** of that
row. Every other byte of the four-row world is the committed r60 world (entry table,
SOURCES rows S103–S109 with their sha pins, lesson `## Gate`, committed snapshots).

Before (committed, `SKILL.md` at `c630c4cb`; extracted with `skill_rows`, full line):

```text
| Cursor | `.cursor/rules` (project rule folder for `.mdc` files, S108 :32) | `globs` (example `src/components/**/*.tsx`, S108 :85) | Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131) |
```

After (W8-min; the whole world):

```text
| Cursor | `.cursor/rules` (project rule folder for `.mdc` files, S108 :32) | `globs` (example `src/components/**/*.tsx`, S108 :85) | Rules without a glob pattern apply to every conversation (S108 :305) |
```

Nothing else changes: the entry row for Cursor still quotes S108 :32, the SOURCES S108 row
still carries the sha256 `884c67ca…` and `re-opens S049 —`, and the Gate still records the
:32 quote. In particular **the quote is a literal byte slice of the snapshot** (measured
`True` for S103/S105/S108; only S106 is not, being the `&#124;` row), so this world does not
depend on any quote normalisation at all.

### 2.2 The false proposition, and the page that contradicts it

The row's subject is fixed by its other cells: `.cursor/rules` as *project rule folder for
`.mdc` files* (Rule-files cell, S108 :32), `globs` (Scope key, S108 :85), and the entry quote
"Project rules live in `.cursor/rules`…". The escaped Action asserts, of that subject:

> **A `.cursor/rules/*.mdc` project rule with `globs` omitted is applied to every conversation.**

The page says the opposite. Selected committed lines (read at
`c630c4cb:.ufo/waves/round-60/snapshots/`):

```sh
$ date -u
Fri 23 Oct 2026 07:18:37 PM UTC
$ nl -ba S108.page | sed -n '65,70p;186p;279p;302p;304,305p'
    65	| `alwaysApply` | `description` | `globs`  | Behavior                                                         |
    66	| :------------ | :------------ | :------- | :--------------------------------------------------------------- |
    67	| `true`        | —             | —        | Always included. Globs and description are ignored.              |
    68	| `false`       | —             | provided | Auto-attached when a matching file is in context.                |
    69	| `false`       | provided      | omitted  | Agent reads the description and pulls the rule in when relevant. |
    70	| `false`       | omitted       | omitted  | Included only when you `@`-mention the rule in chat.             |
   186	If alwaysApply is true, the rule will be applied to every chat session. Otherwise, the description of the rule will be presented to the Cursor Agent to decide if it should be applied.
   279	## Team Rules
   302	### Format and how Team Rules are applied
   304	- **Content**: Team Rules are free‑form text. They do not use the folder structure of Project Rules.
   305	- **Glob patterns**: Team Rules support glob patterns for file-scoped application. When a glob pattern is set (e.g., `**/*.py`), the rule only applies when matching files are in context. Rules without a glob pattern apply to every conversation.
exit=0
Fri 23 Oct 2026 07:18:37 PM UTC
```

The mechanism boundary is explicit on the page:

- :302 `### Format and how Team Rules are applied`; :304 Team Rules "do not use the folder
  structure of Project Rules"; :281 Team Rules require Team/Enterprise plans. The sentence
  at :305 is scoped to **Team Rules** by its section and its own subject ("Team Rules support
  glob patterns…").
- For **Project Rules** the same page gives the no-glob defaults at :69–:70 (description-
  selected, or `@`-mention only) and :186 (only `alwaysApply: true` gives every chat session).
- Nothing on the page says a `.cursor/rules` `.mdc` file with `globs` omitted applies to every
  conversation. The escaped cell is therefore **false of its own row** while being a verbatim
  substring of a real line.

This is a **subject substitution**, not a negation. That matters: the Critic's A2
counterexample (`.ufo/waves/round-61/wave/CriticHollowC1.md:110–123`) is a `No`-prefixed
inversion; a polarity test could in principle catch it. No text-local test can catch W8,
because the text is affirmative, contiguous, and on the cited line — only the *subject*
(the mechanism the line is about) is wrong.

### 2.3 Why each frozen arm passes

**A1 — semantic scope-key.** Inputs unchanged by the mutation; the row is exactly the r60
eligible row that C1 must keep passing. Canonical key `globs` (the plan's per-client set
grounded in S112–S115; the r60 row uses it), and it binds a path-like value on the cited
line: `S108.page:85` is `globs: src/components/**/*.tsx`. Measured with the counter's own
`key_site(lines, 85, 'globs')` → the judge leaves Cursor's `why` empty and reports
`key_line=85` for the pristine world (§1.2 run; the mutation does not touch the scope cell).
A1 cannot see the falsehood because the falsehood is in a different cell.

**A2 — semantic action.** The cell is a **verbatim substring of the cited line** :305:
`Rules without a glob pattern apply to every conversation`. Measured: `action_conjunct == []`,
all 5 content words on the line (`apply, conversation, glob, pattern, rules`), `need=3`,
`shared=5`, and `page_plain`-normalised strict substring `True` (§1.2). It therefore passes
any A2 implementation that stays inside the frozen sentence ("every load/event claim … must
be supported by text on the committed snapshot page"): word-threshold, all-content-words,
verb-cooccurrence, and strict-substring readings all accept it.

The escape is **stronger than three of the four landed Actions** by those same measures. The
four landed cells against their own cited lines (measured; §1.2):

| row | content words | shared | missing content words | strict substring |
|---|---|---:|---|---|
| Claude Code S103:194 | 11 | 10 | `scope` | **False** |
| VS Code S105:329 | 6 | 5 | `instruction` | **False** |
| Copilot CLI S106:60 | 12 | 9 | `instruction`, `path`, `specific` | **False** |
| Cursor S108:131 (pristine) | 9 | 9 | — | True |
| **W8 escaped Cursor S108:305** | **5** | **5** | — | **True** |

Consequence: A2 **cannot** be implemented as "the Action must be a span of the cited line" or
"all the Action's content words must occur on the cited line" without failing three of the
four rows the C1 predicate requires to pass. A2 must remain a word/threshold support test
(or add a join the frozen sentence does not state — see §6). Any such test accepts W8.

**A3 — URL canonical.** W8 inherits the r60 Cursor re-open row. Under v2's `url_key` reading
the row passes (`reopen_why == []`, measured). Under the literal frozen sentence ("a re-open
row's URL must be byte-identical to its base row's URL") it does **not**: the row's URL is
`https://cursor.com/docs/rules`, S049's is `https://cursor.com/docs/rules.md`
(byte-identical `False`). This is not caused by the escape and is not fixable by the escape's
author either way — see §4.2, including the measured 404 on the base spelling. W8's A3 status
is therefore **the L1's contract decision**, not an unknown in the mutation.

**A4 — snapshot provenance.** Untouched by the mutation. Measured: SOURCES S108 prints sha256
`884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8`, equal to the committed
`S108.page` (17,403 B); the entry quote is a literal byte slice of those bytes
(`True`); the bytes were first added by the r60 data commit `7b80ae80`
(`git log --diff-filter=A -- .ufo/waves/round-60/snapshots/S108.page`) dated
`2026-10-23T09:28:13-03:00`, the row's recorded open date is `2026-10-23` (not older, same
date). All three clauses pass even under the strictest literal reading.

### 2.4 The arm-pass summary

| arm | W8-min status | evidence |
|---|---|---|
| A1 | pass | unchanged r60 scope cell; key `globs` binds `src/components/**/*.tsx` at S108:85 |
| A2 | pass | cell is a verbatim substring of S108:305; all 5 content words on the line |
| A3 | conditional | v2 url_key pass; literal byte-identity fails on the r60 dataset (§4.2) |
| A4 | pass | sha pin matches; quote is a literal byte slice; first commit not older than open date |

### 2.5 The world under the probe

Already pasted in full in §1.2. The Cursor row's `why` is `[]` in every variant; the
`backed 4 of 4` line is the detector output. The escaped cell's direct measures:

```text
cursor action: conjunct=[] |W|=5 need=3 shared=5 missing=[] strict_substring=True
```

---

## 3. The three escape means, each measured

The assignment names quote shaping with `&#124;` (r60 defect 5), true-but-misleading cells,
and stale-but-plausible content. §2 is the true-but-misleading member. This section adds the
other two as single-cell variants of the same world, and gives the measurements that show
which arm could see them (none of A1–A4 as frozen).

### 3.1 Stale-but-plausible content (W8-stale)

Target: `SKILL.md`, Claude Code row, Action cell only.

```text
| Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `paths` (e.g. `src/api/**/*.ts`, S103 :198) | Rules that load on demand, including path-scoped rules and rules in nested `.claude/rules/` directories, loaded even when `project` was excluded. (S103 :190) |
```

The source line, with the qualifier the cell drops:

```text
   190	Project rules are skipped if you exclude `project` from [`--setting-sources`](/docs/en/cli-reference). Before v2.1.211, rules that load on demand, including path-scoped rules and rules in nested `.claude/rules/` directories, loaded even when `project` was excluded.
```

The cell is a verbatim substring of :190 **after** the comma following `Before v2.1.211,`:
all 10 content words are on the line (`missing=[]`), strict substring `True`, v2
`action_conjunct == []`, and the whole world still backs 4 of 4 (§1.2). Its proposition —
current Claude Code path-scoped rules load even when `project` is excluded — is false for
v2.1.211 and later, whose rule the same line states first ("Project rules are skipped if you
exclude `project`"). The arm sees fresh bytes, a real quote, a real key and a verbatim
action; it cannot see that the sentence is **version-gated** and that the gate was dropped.
A4's commit-date clause is the wrong instrument: the bytes are genuinely fresh, the sentence
is genuinely current text, and its truth is conditional on a version the arm does not parse.

### 3.2 Quote shaping (W8-q) — `&#124;` and three wider channels

W8's landed S106 row already depends on `&#124;`. Measured, on committed bytes:

```text
S106 landed quote words: 10 | literal bytes in page: False | page_plain literal: True | norm: True
```

(That line is the actual output of the §1.2 probe run; the quote cell is read from the
committed entry table.)

So "the quote occurs verbatim in the snapshot" is, on the landed data, **normalization-
equality**, not byte equality. The normalizer is `page_plain`/`norm`/`norm_page` in the
committed counter: `html.unescape`, delete every backtick, `*` and `_`, fold curly quotes,
collapse whitespace (page side additionally strips HTML comments/tags/script/style). Three
channels follow, each measured passing `quote_why` on committed S108/S106 bytes:

1. **Entity alphabet.** `&#124;`, `&#x7C;`, `&vert;`, and `&#0000124;` all pass (the probe
   prints `[]` for each). The documented one, `&#124;`, is not special: any entity that
   `html.unescape` maps to the page's character is accepted.
2. **Identifier misspelling via `_` deletion.** A 23-word quote of `S108.page:42` with
   `alwaysApply` written `always_apply` passes (`quote_why == []`), because `_` is deleted on
   both sides (`norm('always_apply') == norm('alwaysApply') == True`). The literal bytes are
   **not** in the page. The landed row would then quote a key spelling Cursor does not read
   (the page's key is `alwaysApply`); a reader who copies the quoted key writes a frontmatter
   key the client ignores.
3. **Cross-line windows.** An 18-word quote spanning `S108.page:32` through the blank line
   into `:34` (`…included based on relevance. Use project rules to:`) passes
   (`quote_why == []`, literal bytes `False`): whitespace collapse makes a window that crosses
   a paragraph boundary indistinguishable from a contiguous sentence. The `&#124;` variant is
   the visible artefact of the same flattening at a table-cell boundary.

W8-q is the same world with the Cursor **entry** Quote cell (and the matching Gate line)
replaced by the `always_apply` quote; measured 4 of 4 backed as part of `W8-full` (§1.2):

```text
| Cursor | `.cursor/rules` | S108 | A plain `.md` file in `.cursor/rules` is ignored by the rules system because it has no frontmatter to specify `description`, `globs`, and `always_apply`. |
```

Caveat that the residual call must hold: **W8-q is conditional on A4 normalising.** If v3
implements A4's "verbatim" as literal byte containment *and* the S106 row is rewritten to a
pipe-free literal quote (ExecKeyForms measured that alternative: folder token
`.github/instructions` with the line-56 quote), then channel 2 and channel 3 die and channel 1
dies with the `&#124;` row. W8-min does **not** depend on this: its quote is a literal byte
slice of S108:32 (measured `True`), so it survives literal A4.

### 3.3 The composite world

`W8-full` = W8-min + W8-stale + W8-q in one world. Measured 4 of 4 backed (§1.2). The three
false cells live in three different rows and three different cells, so no unrelated conjunct
masks any of them: each is a single-cell delta from a world that passes.

---

## 4. Two integration traps found while grounding (these bite C1 regardless of W8)

### 4.1 If the v3 counter bumps `BASE` to the r61 base, C1 measures 0 of 4

`BASE` in v2 is `31092dc6` (round-59 spot-check), which is *before* the r60 rows; that is why
S103–S109 are "new" and eligible. The r61 plan's base is `f3246d14`, which already contains
S103–S109. A natural "update BASE to the current base" edit silently rejects all four rows:

```text
$ date -u
Fri 23 Oct 2026 07:22:08 PM UTC
$ cd /fast/scratch/hyaku/kotoba-r61/MutFixtureEscape && python3 -B probe/base_bump.py
S103 in base@f3246d14: True
backed with BASE=f3246d14: 0
Claude Code why: ['entry row S103: S103 is already a SOURCES row at base']
exit=0
Fri 23 Oct 2026 07:22:08 PM UTC
```

The v3 counter must keep `BASE = 31092dc6` (or move the rows to new ids); otherwise the
four-eligible-rows half of the predicate is unsatisfiable. This is a contract/data decision
the L1 must state before measurement, like A3's.

### 4.2 A3-as-written is unsatisfiable on the Cursor row today, in every spelling

Measured with the frozen curl UA/Accept and a 30 s cap (`date -u` before and after each run):

```text
Fri 23 Oct 2026 07:17:52 PM UTC
url=https://cursor.com/docs/rules.md
writeout=404 https://cursor.com/docs/rules.md exit=0 bytes=389 sha256=4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1
url=https://cursor.com/docs/rules
writeout=200 https://cursor.com/docs/rules exit=0 bytes=17403 sha256=884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
Fri 23 Oct 2026 07:17:52 PM UTC
```

- The base row's URL (`rules.md`, S049) is **dead (404)**.
- The row's URL (`rules`, S108) is live and its bytes are exactly the committed snapshot
  (`884c67ca…`).

Therefore, on the committed data:
- Use S049's bytes (`rules.md`) to satisfy A3-literally → the row's live fetch is 404, so the
  Cursor row cannot be counted in "four of four live" (F falls to 3; the exit-0 predicate can
  still pass at `3 ≥ TARGET`, but the row-level claim cannot).
- Use the live URL (`rules`) as the row has it → A3-literally rejects it (byte inequality;
  v2's `url_key` accepts it, and W2's alias rejection would then need a different mechanism).

This corroborates the sibling in-flight finding `MutA3.md` (A3/S108 byte inequality) and adds
the 404 receipt. Suggested contract resolutions for the L1 (a decision, not a repair I made):
(a) define A3 as byte equality against the base row's *current canonical* URL recorded in a
superseding row, and move `BASE` accordingly; (b) define A3 as `url_key` equality plus a
content check (the row's snapshot sha equals the base page's recorded sha where one exists);
(c) exempt a re-open whose base URL is unreachable when the row's snapshot bytes equal the
named base page's recorded bytes. Each changes the frozen sentence and must be a pre-data
erratum, not a silent implementation choice. W8's escape does not depend on which is chosen.

---

## 5. The honest bound sentence the entry must carry

Placement: `corpus/knowledge/scoped-rules-round60.md`, under `## Not held`, as the first
bullet (or as a new `## Counter limits` subsection immediately after `## Quote shaping`).
Mirror the one-line version in the r61 report/LOG where "provenance-authenticating" is used.

### 5.1 Canonical sentence (entry-ready)

> **Counter limits (v3).** The four arms authenticate cell provenance, not row truth — A1
> that a canonical key occurs in key form with a path-like value on the cited line, A2 that
> the Action cell's load/event words are present on the cited page (support by text, not
> entailment), A3 that a re-open row's URL is the
> base row's URL (byte-identical as frozen; substitute the amended comparison if the L1
> amends A3), and A4 that the recorded sha256 equals the committed snapshot bytes, that
> the quote occurs in them after `html.unescape`, deletion of backticks/`*`/`_`, curly-quote
> folding and whitespace collapse (never byte equality — the S106 `&#124;` quote is not a
> literal byte slice), and that the bytes' first commit is no older than the open date — and
> no arm tests that the key, rule-file token and action describe the same documented
> mechanism, that the action is true of the row's own rule class, that a quoted statement is
> current-version behaviour, or that the fetch happened at the recorded wall-clock time (the
> declared A4 limit); a row of this shape passes all four arms with an Action cell that is
> false of its row (W8).

If W8 is **not** integrated into the v3 self-test, drop the final clause and end at the
semicolon; do not assert a fixture result that was not run. If W8 is integrated and observed
passing, keep it and cite the receipt line.

### 5.2 One-line version (report / SCORECARD)

> The v3 arms are cell-provenance checks, not semantic proof — a canonical key, page-word
> support, URL equality, and sha/quote/commit provenance can all hold while the Action is
> false of its own row (W8); "provenance-authenticating" must not be read as byte-exact,
> fresh-fetch, current-version, or entailment authentication.

### 5.3 What each clause rests on (so the residual call can check it)

| clause | measured ground |
|---|---|
| "cell provenance, not row truth" | §2.2–§2.3; the escaped cell passes every textual-support reading while asserting a Team-Rules default of Project Rules |
| A2 wording "words occur on the cited page line" | the four landed Actions are paraphrases (three not substrings) with missing content words; a stricter A2 fails the data (§2.3 table) |
| "never byte equality — the S106 `&#124;` quote is not a literal byte slice" | `literal quote bytes in page: False` for the landed S106 quote; `True` for S103/S105/S108 (§1.2) |
| "after `html.unescape`, deletion of backticks/`*`/`_`, curly-quote folding and whitespace collapse" | `page_plain`/`norm`/`norm_page` in the committed counter; channels measured in §3.2 |
| "no arm tests … same documented mechanism / true of the row's own rule class" | §2.2 (Team Rules vs Project Rules on S108); §3.1 (version-gated clause on S103) |
| "not … wall-clock" | the plan's own declared A4 limit (`plans/round-61.md:35–38`) |

---

## 6. What the residual falsify call must decide

1. **Run W8 through the landed v3 runner** (fixture content in Annex A; expected output:
   `W8 pass 4 of 4`). This is the one execution I could not do — no v3 source exists at read.
2. **If W8 passes all four arms**, the escape class is open. The C1 claim may still say
   "provenance-authenticating", but only with the §5.1 sentence carried in the entry and with
   "provenance" read as cell provenance. Do not strengthen the claim to semantic, byte-exact,
   fresh-fetch, or current-version authentication; the entry's own S106 row falsifies
   "byte-exact".
3. **If W8 is rejected**, the L1 must name the arm clause that did it in source. Given that
   A1's and A4's inputs are unchanged and A3 is the separate conflict of §4.2, the only way
   A2 can reject W8-min is a **join the frozen sentence does not state**: the cited action
   line must also name the row's token or canonical key, or lie in the same page
   section/mechanism as the token. That is a contract extension; declare it in the plan
   (pre-data) and extend the bound sentence to say the join exists. Do not report it as A2's
   frozen wording.
4. **Record W8 as a survivor fixture, not an eighth kill world.** If the self-test prints
   `worlds reject 7 of 7`, W8 must be a separate line (`escape W8 pass 4 of 4`); if the
   implementation prints `8 of 8`, the join from (3) must be shown.
5. **Resolve §4.1 (`BASE`) and §4.2 (A3/S049 404) before the data measurement.** Both can zero
   or skew the measured half of C1 independently of the escape class.

---

## Annex A — fixture recipe (content, not a lane edit)

Two equivalent forms; either runs the same row content.

**A.1 Lane-application world (what I measured).** Take the committed four-row world as-is;
replace the Cursor Action cell with the line in §2.1. Run the v3 judge/CLI with
`base_sources = git show 31092dc6:corpus/SOURCES.md` (the v2 `BASE`) and the committed r60
snapshots as `snapshot_of`. Expected: 4 of 4 backed, Cursor `why == []`.
Add the Claude Action cell (§3.1) for W8-stale, and the entry/Gate quote (§3.2) for W8-q.

**A.2 Self-contained fixture (for the v3 self-test).** Reuse the counter's own self-test
world builder: a base SOURCES table with one Cursor row whose URL bytes **equal** the
fixture row's URL (this sidesteps §4.2 inside the fixture), a re-open row carrying
`re-opens S9xx — …` and the sha256 of `.ufo/waves/round-60/snapshots/S108.page`, the SKILL
row of §2.1, the entry row of the committed entry, and a `## Gate` line recording the same
quote. The base row's raw line must not contain the identifier `globs` (v2's `reopen_why`
tests that). Open date `2026-10-23`; snapshot bytes first committed on that date (the
committed r60 blob satisfies this). Expected: Cursor backed; with the other three clients'
pristine rows, 4 of 4.

**A.3 Exact replacement strings** (for a fixture driver; one occurrence each in `SKILL.md`):

```text
OLD  Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131)
NEW  Rules without a glob pattern apply to every conversation (S108 :305)

OLD  Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194)
NEW  Rules that load on demand, including path-scoped rules and rules in nested `.claude/rules/` directories, loaded even when `project` was excluded. (S103 :190)
```

The runnable probe (read-only over the lane) is
`/fast/scratch/hyaku/kotoba-r61/MutFixtureEscape/probe/run_world.py`; it reproduces every
number in this report. Scratch is untrusted and is not evidence; the evidence is the
committed bytes and the pasted output.

## Annex B — hashes and restoration evidence

```text
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && date -u
Fri 23 Oct 2026 07:17:52 PM UTC
$ git status --porcelain -- SKILL.md corpus verifiers plans .ufo/waves/round-60 .ufo/waves/round-61/controls
(no output: no tracked change in any file this seat used)
$ for p in SKILL.md corpus/knowledge/scoped-rules-round60.md corpus/SOURCES.md corpus/lessons/round-60.md verifiers/check_scoped_rules.py .ufo/waves/round-60/snapshots/S108.page; do
    printf '%-55s work=%s head=%s\n' "$p" "$(git hash-object "$p")" "$(git rev-parse "HEAD:$p")"; done
SKILL.md                                                work=46e7bc9a3c47cbccc534470f583cb70ef8a3eba1 head=46e7bc9a3c47cbccc534470f583cb70ef8a3eba1
corpus/knowledge/scoped-rules-round60.md                work=74d75eb76f00342adc201ba155aa9bd14f3a9313 head=74d75eb76f00342adc201ba155aa9bd14f3a9313
corpus/SOURCES.md                                       work=d3a385273f4ed77f026d5faea1c1a36b569f255d head=d3a385273f4ed77f026d5faea1c1a36b569f255d
corpus/lessons/round-60.md                              work=5a6f94718d52a41b724af6a66980ea8cb5741776 head=5a6f94718d52a41b724af6a66980ea8cb5741776
verifiers/check_scoped_rules.py                         work=9d2195e9ad41d857bbd8f987e863cca248d55c51 head=9d2195e9ad41d857bbd8f987e863cca248d55c51
.ufo/waves/round-60/snapshots/S108.page                 work=47c1554d6fb3be35e292f7dd525d3241fd2ff21e head=47c1554d6fb3be35e292f7dd525d3241fd2ff21e
exit=0
```

Counter copy vs lane counter (both runs): `ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`.
Snapshot sha256 of the committed working bytes (read by this seat; full digests, matching
the SOURCES pins for S103–S109):

```text
S103 82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7
S104 9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e
S105 a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f
S106 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
S107 e5fbfd6d580643a300b5ee0e622d9e2d8f97d4d23460e6b08e1c656251c2f2c2
S108 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
S109 dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54
```

The four eligible pins are enforced by the judge (their rows back); S104/S107/S109 are read
and matched against their SOURCES rows but are outside the backed set (no token).
No lane, fleet, sibling, `.ufo/state`, or jj/git-index file was written; no git/jj mutation
was made; the four siblings' untracked wave reports I read (`MutA3.md`,
`CriticHollowC1.md`, `MutWorldW5W6.md`, `MutV2Regress.md`) are cited as in-flight reports,
not as lane evidence.

## Annex C — what I could not verify

- v3's actual acceptance/rejection of W8 (source absent at read; the whole point of the
  residual call).
- The exact mediation of A2 ("supported by text") the v3 author will implement; §2.3 proves
  the escaped cell passes every reading that keeps the four landed rows passing.
- A3 resolution and the `--fetch` row-level result on the world (L1 measurement).
- S112–S115 contents (A1's canonical-key grounding); the world uses `globs`, as the plan's
  A1 example and the r60 row do.
- The live page beyond the two construction GETs in §4.2; no `--fetch` of the full world was
  run by this seat.

---

**Installs:** none (no tool needed; pacman untouched).
**Blockers:** none for this deliverable. Two lane-level blockers were *found*, not hit:
`BASE` bump (§4.1) and A3-vs-live-URL (§4.2); both need an L1 pre-data decision.
**What I attacked / produced:** attacked the frozen v3 arm claim with a survivor world —
designed W8 (`CtlSemanticEscape`), a one-cell Cursor Action substitution that passes all four
arms' sentences with a landing action false of its Project-Rules row, plus measured
stale-version and quote-shaping variants and the entry-bound sentence that keeps
"provenance-authenticating" from overstating; measured v2 survivor 4 of 4 with no lane write.
