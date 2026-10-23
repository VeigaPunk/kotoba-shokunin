# MutA1 — arm A1 (semantic scope-key): rows that satisfy A1's letter while smuggling a wrong key

Seat: `kotoba-r61-wave-MutA1` (mutation-tester, leaf; no dispatch). Measurement date:
2026-10-23 UTC. Report path (relative to the lane):
`.ufo/waves/round-61/wave/MutA1.md`.

Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (read-only to me; I wrote no lane,
fleet, sibling, `.ufo/state` or jj/git-index file). Base declared in the tasking
`f3246d1493b60ea1c0d947a19c39f9e08e92f326`; the lane's actual HEAD when this seat started was
`c630c4cbc01ff5e5438ab0033cfadd6e19382ab1` (base + round-61 plan freeze `7827628` + erratum E1
`c630c4c`; erratum withdraws C3 as a counted claim before data — C1 still rests on S112–S115).
The committed C1 counter is unchanged across those commits:

```
$ sha256sum verifiers/check_scoped_rules.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
```

All probe work is a `cp -a` copy of the lane at
`/fast/scratch/hyaku/kotoba-r61/MutA1/sandbox`. Scratch is untrusted and is cited here only as
the location of the run, never as evidence; every output pasted below was produced by the
committed counter bytes (sha above) or by the literal A1 reference implementation printed in
§5.

## 1. Detector and method

The frozen A1 sentence (plan §C1): *"a row's Scope key must be in the canonical per-client key
set grounded in S112–S115 (opened this round), and must bind a path-like value on the cited
line."* The r60 ground for the wrong-key class is
`.ufo/waves/round-60/build/ExecKeyForms.md` Part 1: 16 passing `(K, line)` pairs over the four
eligible pages, 9 of them on a key that is not the client's scope key
(`paths`:198/231 REAL; `patterns`:238 and `claudeMdExcludes`:339 extra on Claude Code;
`sessions`:32/128/221/228 and `Sync`:287 extra on VS Code; `globs`:85 REAL, `rules`:146 and
`order`:307 extra on Cursor; Copilot CLI clean).

The canonical sets used in every model below are the ones the S112–S115 scribe drafts land
(S112 §A1 key-set: `"Claude Code": frozenset({"paths"})`; S113: `"VS Code": {"applyTo"}`;
S114: `Copilot CLI -> applyTo`; S115: `"Cursor": frozenset({"globs"})`, with an explicit warning
that a cross-client union is not a valid per-client set):

```python
CANON = {"Claude Code": {"paths"}, "VS Code": {"applyTo"},
         "Copilot CLI": {"applyTo"}, "Cursor": {"globs"}}
```

Each mutant is an independent commit in the sandbox: the tracked world is reset to the pristine
commit, one Scope cell and/or one appended page line (+ that snapshot's SOURCES sha) is changed,
then the real CLI is run:

```
python3 -B verifiers/check_scoped_rules.py --rev <commit>
```

No `--fetch` was run: A1's conjunct is offline (snapshot bytes), no network was used, and the
live half is not claimed here (see §7). An offline run exits 1 by construction because the
frozen predicate requires `--fetch`; the discriminator is the `backed` count and the reject
line, exactly as in the r60 receipts.

Seven literal models of A1 were scored on the same worlds:

| model | what it represents |
|---|---|
| `exact` | A1 as written: exact per-client set + v2's `key_site` binding |
| `casefold` | implementation slip: membership and key lines lower-cased |
| `prefix` | slip: membership by prefix (`path` matches `paths`) |
| `widened` | slip: set derived from "keys that take globs on the page" / union |
| `strictline` | the letter read literally: value must be on the cited line (no block lookahead) |
| `boldguard` | value grammar tightened only against `**`+letter |
| `guarded` | the proposed complete arm (§5) |

## 2. Baseline — pristine world

```
=== V0-pristine  c630c4cbc01f ===
  note: the committed world, no change
  cli exit=1
  cli: scoped rule files backed on committed snapshots 4 of 4; live not run
  cli: counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev c630c4cbc01ff5e5438ab0033cfadd6e19382ab1
  cli: reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  cli: reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  cli: reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
  v2 backed: Claude Code, VS Code, Copilot CLI, Cursor
  Claude Code  key='paths'    line=198 spans=['paths']  exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=rej boldguard=PASS guarded=PASS
  VS Code      key='applyTo'  line=164 spans=['applyTo']  exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=PASS guarded=PASS
  Copilot CLI  key='applyTo'  line=66  spans=['applyTo']  exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=PASS guarded=PASS
  Cursor       key='globs'    line=85  spans=['globs']    exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=PASS guarded=PASS
```

The baseline is green under the committed counter (4 of 4) and under `exact`/`guarded` (4 of 4),
so the mutants below are valid mutants, not baseline failures. The one yellow cell is the
`strictline` rejection of the real Claude Code row — that is the letter problem in §3.4, not a
counter failure.

Exact cited bytes (from the committed snapshots at `c630c4c`):

```
S103:198  'paths:'
S103:199  '  - "src/api/**/*.ts"'
S103:231  'paths:'
S103:232  '  - "src/**/*.{ts,tsx}"'
S105:164  "applyTo: '**/*.py'"
S106:66   '   applyTo: "app/models/**/*.rb"'
S106:94   '   applyTo: "**"'
S108:85   'globs: src/components/**/*.tsx'
S103:238  'Each brace group multiplies the number of expanded patterns: `src/*.{ts,tsx}` expands to two patterns, …'
S103:339  '  "claudeMdExcludes": ['
S103:340  '    "**/monorepo/CLAUDE.md",'
S105:32   '> **For Local harness sessions:** Project instructions can use `.github/copilot-instructions.md`, …'
S108:146  'There are two ways to create rules:'
S108:307  '- **Precedence**: Rules are applied in this order: **Team Rules → Project Rules → User Rules**. …'
```

## 3. The fifteen mutants (plus the baseline world)

### 3.1 Summary

`v2` = committed counter; `exact` = A1 as written; `guarded` = proposed arm (§5).
"letter" = survives A1 exactly as written; "slip" = survives only a plausible implementation
slip.

| # | mutant | v2 | A1 exact | guarded | class |
|---|---|---|---|---|---|
| V1 | Scope cell `PATHS`, page `paths:` | killed (3/4) | killed | rejected | case (slip only) |
| V1b | Scope cell `PATHS`, page line `PATHS: …` | **backs 4/4** | killed | rejected | case (slip only) |
| V2 | `paths` **and** `patterns` in one cell | **backs 4/4** | **survives** | rejected | letter: multi-key |
| V2b | `paths` + cited `claudeMdExcludes` | **backs 4/4** | **survives** | rejected | letter: multi-key |
| V13 | `paths` + `applyTo` (cross-client) | **backs 4/4** | **survives** | rejected | letter: multi-key |
| V3 | page `paths: the files listed below` | killed (3/4) | killed | rejected | non-path value (caught) |
| V3b | page `paths: **see the note below**` | **backs 4/4** | **survives** | rejected | letter: value grammar |
| V0 | real `paths:` :198, glob on :199 | backs 4/4 | survives | PASS | letter says "on the cited line" — false for the real row |
| V5 | `patterns` @ S103:238 | **backs 4/4** | killed | rejected | lookalike (slip only: widened set) |
| V6 | `claudeMdExcludes` @ S103:339 | **backs 4/4** | killed | rejected | lookalike (slip only: widened set) |
| V7 | `sessions` @ S105:32 | **backs 4/4** | killed | rejected | lookalike (slip only: widened set) |
| V8 | `path` (singular) @ appended line | **backs 4/4** | killed | rejected | lookalike (slip only: prefix) |
| V9 | `# paths: src/legacy/**/*.ts` | **backs 4/4** | **survives** | rejected | letter: commented key |
| V10 | `Do not set paths: …` | **backs 4/4** | **survives** | rejected | letter: negated key |
| V11 | `applyTo='src/legacy/**/*.py'` | **backs 4/4** | **survives** | rejected | letter: equals form |
| V12 | cell example `` `see below` `` | **backs 4/4** | **survives** | rejected | letter: unchecked example |

Eight mutants survive A1 exactly as written; five more (the ones v2 admits) survive only an
implementation slip; the remaining two (V1, V3) are killed by v2 and by exact A1. All fifteen
mutants are rejected by the proposed guarded arm on the mutated client while the pristine world
passes 4 of 4.

### 3.2 Family 1 — case variants (`PATHS`)

**V1 — cell `PATHS`, page lowercase `paths:`**

Exact input (Claude Code row, Scope cell):

```
`PATHS` (e.g. `src/api/**/*.ts`, S103 :198)
```

Expected catcher: the canonical-set membership check (exact, case-sensitive). Actual:

```
cli: scoped rule files backed on committed snapshots 3 of 4; live not run
cli: reject Claude Code: entry row S103: snapshot .ufo/waves/round-60/snapshots/S103.page:
     scope key 'PATHS' is not in key form with a path pattern at line 198
Claude Code key='PATHS' line=198  exact=rej casefold=PASS prefix=rej widened=rej strictline=rej boldguard=rej guarded=rej
```

Verdict: killed by v2 (the binding is case-sensitive) and by exact A1. It survives only if an
implementation lower-cases both the set and the page lines (`casefold` PASS) — an
implementation slip, not a letter hole.

**V1b — cell `PATHS`, page line `PATHS:` (appended at S103:665, SOURCES sha re-pinned)**

Exact input: appended line `PATHS: src/legacy/**/*.ts`; Scope cell `` `PATHS` (S103 :665) ``.

```
cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='PATHS' line=665  exact=rej casefold=PASS prefix=rej widened=rej strictline=rej boldguard=rej guarded=rej
      exact why: A1: key 'PATHS' not in the canonical set for Claude Code
```

Verdict: **survives v2** (the form check is case-sensitive and finds `PATHS:`), killed by exact
A1, survives the case-fold slip. This is the pure membership-slip mutant. Guard G2: compare
`key in CANON[client]` with no lowering; keep `key_occurrences` case-sensitive. Do not call
`str.lower()`/`casefold()` anywhere in A1.

### 3.3 Family 2 — canonical key, non-path value

**V3 — straight non-path value (caught)**

Appended page line: `paths: the files listed below` (S103:665); cell `` `paths` (S103 :665) ``.

```
cli: scoped rule files backed on committed snapshots 3 of 4; live not run
cli: reject Claude Code: entry row S103: snapshot .ufo/waves/round-60/snapshots/S103.page: scope key 'paths' is not in key form with a path pattern at line 665
Claude Code key='paths' line=665  exact=rej casefold=rej prefix=rej widened=rej strictline=rej boldguard=rej guarded=rej
```

Verdict: caught by v2 and by A1. No action needed beyond keeping the value test.

**V3b — markdown-bold value (letter bypass)**

Appended page line: `paths: **see the note below**` (S103:665); cell `` `paths` (S103 :665) ``.

```
cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='paths' line=665  exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=rej guarded=rej
      guarded why: A1g: key 'paths' has no clean colon-form site with a path-like value at S103:665
```

Expected catcher: a path-value grammar that distinguishes a glob from markdown emphasis. None
in A1 as written: `first_value_token` strips `-`, `[`, quotes and spaces but not `*`, so the
token is `**see`; it contains `*` and matches `^[A-Za-z0-9_./*{},!-]+$`, so `pattern_value`
accepts it (`--self-test` line 1605 asserts a bare `**` is a pattern; the same grammar accepts
`**see`). The r60 sweep hit this mechanism on non-canonical keys (`sessions:**`, `order: **Team`,
`rules:` → `- **…`); with a canonical key the key set cannot catch it.

Verdict: **letter bypass** (path-like is form-only). Guard G5: the strict value test in §5 —
unquoted `**` is rejected, asterisk tokens with no `/` and no `.` are rejected, inline-code
values are rejected; quoted `"**"` and `**/*.ts` stay legal. This guard also kills the whole r60
bold-marker family independently of the key set.

### 3.4 Family 3 — multi-key rows where the second key is wrong

Three variants, all backed by v2 and all surviving A1 exactly as written. Root cause:
`scope_key` (counter line 759) returns only the **first** backticked span, and the committed
self-test enshrines that (`line 1572: check("key: the FIRST backticked span is the key",
scope_key("`alwaysApply` and `paths` (S900 :5)")[0], "alwaysApply")`). Put the canonical key
first and a wrong key second and the wrong key is never examined.

**V2 — `paths` + `patterns`:**

```
`paths` and `patterns` (e.g. `src/api/**/*.ts`, S103 :198)

cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='paths' line=198 spans=['paths', 'patterns'] exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=PASS guarded=rej
      guarded why: A1g: scope cell names 2 key identifier(s) ['paths', 'patterns'] (need exactly 1)
```

**V2b — `paths` + a cited `claudeMdExcludes`** (both keys cited; `citation_why` takes the first
own-source citation, :198, so the key line stays valid):

```
`paths` (S103 :198; the page also shows `claudeMdExcludes`, S103 :339)

cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='paths' line=198 spans=['paths', 'claudeMdExcludes'] exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=PASS guarded=rej
      guarded why: A1g: scope cell names 2 key identifier(s) ['paths', 'claudeMdExcludes'] (need exactly 1)
```

**V13 — cross-client second key** (`paths` for Claude Code + `applyTo`, VS Code's key):

```
`paths` (S103 :198) or `applyTo` (S105 :164)

cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='paths' line=198 spans=['paths', 'applyTo'] exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=PASS guarded=rej
      guarded why: A1g: scope cell names 2 key identifier(s) ['paths', 'applyTo'] (need exactly 1)
```

Expected catcher: a multiplicity rule — the row's Scope cell must name exactly one key
identifier. None exists in A1 as written; the singular phrase "a row's Scope key" is
implemented as "the first span". Verdict: **letter bypass**. Guard G1 (multiplicity), which also
subsumes the V2b/V13 cases. Cost: the self-test assertion at line 1572 must become a rejection
test (its fixture names two identifiers).

### 3.5 Family 4 — key line cited correctly, value glob absent

The eligible Claude Code row cites `S103 :198`, whose bytes are exactly `paths:`; the glob is
`S103 :199` (`  - "src/api/**/*.ts"`). A1's letter says the key "must bind a path-like value on
the cited line". A literal implementation of that sentence rejects the real row:

```
V0 pristine, Claude Code: strictline=rej   (all other clients: strictline=PASS)
```

The committed counter passes it only because `value_after` reads the first non-blank line among
the next three and accepts a block list item (counter lines 838-853; self-test line 1616 asserts
"a block value two lines down passes"). Two consequences for v3:

1. A1 must say "on the cited line **or in its block value**"; otherwise the claim is false for
   the eligible Claude Code row and the arm kills a required passing row.
2. Once the block lookahead is kept, a block value that is not the key's own value is the
   residual risk. The lookahead is bounded (3 lines) and requires the next non-blank line to
   start with `-`, `"`, `'` or a backtick, so a prose line between the key and a list disables it
   (self-test line 1623). I found no reachable case on the four committed pages where a
   canonical key's lookahead reaches a glob belonging to another key; the risk is authored
   fixture pages, not the vendor bytes.

Verdict: letter inconsistency, not a bypass; guard G9 (define the block binding explicitly).

### 3.6 Family 5 — YAML-key lookalikes

All four are backed by v2 at 4 of 4 (the r60 ExecKeyForms ground reproduced offline):

**V5 — `patterns` at the real prose-colon line `S103 :238`**

```
`patterns` (S103 :238)
cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='patterns' line=238 spans=['patterns'] exact=rej casefold=rej prefix=rej widened=PASS strictline=rej boldguard=rej guarded=rej
      exact why: A1: key 'patterns' not in the canonical set for Claude Code
      guarded why: A1g: key 'patterns' not in the canonical set for Claude Code; A1g: key 'patterns' has no clean colon-form site with a path-like value at S103:238
```

`patterns`@238 passes v2 because the prose colon is followed by an inline-code glob
(`src/*.{ts,tsx}`); the guarded value test also rejects it as inline code.

**V6 — `claudeMdExcludes` at the real JSON key `S103 :339` (block value `:340`,
`"**/monorepo/CLAUDE.md"`)**

```
`claudeMdExcludes` (S103 :339)
cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='claudeMdExcludes' line=339 spans=['claudeMdExcludes'] exact=rej casefold=rej prefix=rej widened=PASS strictline=rej boldguard=rej guarded=rej
      exact why: A1: key 'claudeMdExcludes' not in the canonical set for Claude Code
      guarded why: A1g: key 'claudeMdExcludes' not in the canonical set for Claude Code
```

This is the sharpest **set-grounding** hazard: `claudeMdExcludes` genuinely binds a path pattern
(it excludes CLAUDE.md files from loading), so a canonical set built as "keys on this page that
take path patterns" admits it. Only a literal per-client set defined by the *matching-work-file
scope* semantics excludes it. The guarded value test cannot catch it (the value is a real path);
the set must.

**V7 — `sessions` at `S105 :32`** (VS Code's real line `> **For Local harness sessions:** …`;
the token is the bold `**` and v2 reads it as a pattern):

```
`sessions` (S105 :32)
cli: scoped rule files backed on committed snapshots 4 of 4; live not run
VS Code key='sessions' line=32 spans=['sessions'] exact=rej casefold=rej prefix=rej widened=PASS strictline=rej boldguard=rej guarded=rej
      exact why: A1: key 'sessions' not in the canonical set for VS Code
      guarded why: A1g: key 'sessions' not in the canonical set for VS Code; A1g: key 'sessions' has no clean colon-form site with a path-like value at S105:32
```

**V8 — singular `path`** (appended `path: src/legacy/**/*.ts`, S103:665):

```
cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='path' line=665 spans=['path'] exact=rej casefold=rej prefix=PASS widened=rej strictline=rej boldguard=rej guarded=rej
      exact why: A1: key 'path' not in the canonical set for Claude Code
```

Expected catcher: exact membership. Verdict: killed by exact A1; survives only a prefix/plural
implementation slip (`paths`.startswith(`path`)). Guard G3: set membership is exact string
equality; no prefix, plural, alias or normalisation table.

Note on V5–V7: `MutWorldW5W6` already rebuilt these three as committed W5 worlds and measured
the live half (`build/ExecKeyForms.md` ground: backed end-to-end, 4 of 4 live, exit 0). My runs
are the offline discriminator only; no claim is made here about their live behavior. The plan's
W5 world must reject all three under A1; V5–V7 give the exact fixture inputs and line cites.

### 3.7 Family 6 — binding-context smuggling (right key name, not a real binding)

These keep the canonical key name, so the set check cannot catch them; the cited line merely
contains the key in a context that is not a configuration binding.

**V9 — commented key form.** Appended `# paths: src/legacy/**/*.ts` (S103:665); cell cites it.

```
cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='paths' line=665  exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=PASS guarded=rej
      guarded why: A1g: key line 665 is commented out
```

`key_occurrences` requires only identifier boundaries; a leading `#` is not one. Verdict:
**letter bypass**. Guard G6: reject a cited line whose first non-space characters are `#`,
`//` or `<!--`.

**V10 — negated prescription.** Appended
`Do not set paths: src/legacy/**/*.ts in a rule that should load for every file.` (S103:665).

```
cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='paths' line=665  exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=PASS guarded=rej
      guarded why: A1g: key 'paths' has no clean colon-form site with a path-like value at S103:665
```

The line documents the opposite of what the row's key claims, and A1 accepts it. This is the
A1 analogue of the A2 negation limit the plan already pre-registers ("a cell built from the
line's own words passes even if it inverts the line's meaning"). Verdict: **letter bypass**.
Guard G7: within 60 characters before the key site, `not|never|avoid|instead` or `n't` rejects
the site. No committed eligible line contains a negation before its key, so the guard costs
nothing on the pristine world (measured: guarded PASS on all four).

**V11 — equals form.** Appended `applyTo='src/legacy/**/*.py'` (S105:368); VS Code cell cites
it. v2's `KEY_SUFFIX_RE` accepts `=` (self-test line 1657: "an equals sign is a key form").

```
cli: scoped rule files backed on committed snapshots 4 of 4; live not run
VS Code key='applyTo' line=368  exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=PASS guarded=rej
      guarded why: A1g: key 'applyTo' has no clean colon-form site with a path-like value at S105:368
```

Verdict: **letter bypass** ("binds a path-like value" is satisfied by a shell-style
assignment). No committed vendor example on the four eligible pages uses `=`; all use `:`.
Guard G8: A1's binding requires the colon form. Cost: the self-test assertion at line 1657
would have to change or move to a v2-compatibility note. If the L1 prefers not to change it,
record the residual risk (a `=`-form line in a docs page can ground a row) rather than claiming
A1 covers it.

**V12 — unchecked example in the Scope cell.** Cell `` `paths` (e.g. `see below`, S103 :198) ``;
cited line unchanged (the real `paths:` block).

```
cli: scoped rule files backed on committed snapshots 4 of 4; live not run
Claude Code key='paths' line=198  exact=PASS casefold=PASS prefix=PASS widened=PASS strictline=PASS boldguard=PASS guarded=rej
      guarded why: A1g: scope cell span 'see below' is neither a key, a citation nor a path-like example
```

The real cells carry a path example (`src/api/**/*.ts`, `**/*.py`, `app/models/**/*.rb`,
`src/components/**/*.tsx`), but no check reads it. Verdict: **letter bypass** (row-level display
claim). Guard G4: every backticked span in the Scope cell that is not the key and not an
`S### :L` citation must pass the strict path-value test. Lower severity than G1–G3.

## 4. Per-client detail of the guarded verdicts

The guarded arm rejects only the mutated client in every variant; the other three keep the
pristine verdicts (PASS). For each mutant the guarded arm rejects, the exact rejection text is:

```
V2  A1g: scope cell names 2 key identifier(s) ['paths', 'patterns'] (need exactly 1)
V2b A1g: scope cell names 2 key identifier(s) ['paths', 'claudeMdExcludes'] (need exactly 1)
V13 A1g: scope cell names 2 key identifier(s) ['paths', 'applyTo'] (need exactly 1)
V3b A1g: key 'paths' has no clean colon-form site with a path-like value at S103:665
V9  A1g: key line 665 is commented out
V10 A1g: key 'paths' has no clean colon-form site with a path-like value at S103:665
V11 A1g: key 'applyTo' has no clean colon-form site with a path-like value at S105:368
V12 A1g: scope cell span 'see below' is neither a key, a citation nor a path-like example
V1  A1g: key 'PATHS' not in the canonical set for Claude Code; A1g: key 'PATHS' has no clean colon-form site with a path-like value at S103:198
V1b A1g: key 'PATHS' not in the canonical set for Claude Code
V5  A1g: key 'patterns' not in the canonical set for Claude Code; A1g: key 'patterns' has no clean colon-form site with a path-like value at S103:238
V6  A1g: key 'claudeMdExcludes' not in the canonical set for Claude Code
V7  A1g: key 'sessions' not in the canonical set for VS Code; A1g: key 'sessions' has no clean colon-form site with a path-like value at S105:32
V8  A1g: key 'path' not in the canonical set for Claude Code
```

## 5. Proposed guard (code, validated)

The guarded model used in §3 is below. It is a *proposal* for the v3 arm, not integrated code;
`c.` names the committed counter's own helpers. It keeps v2's `pattern_value` untouched (so
existing self-test assertions remain true) and adds a new value helper plus context rules.

```python
# A1 v3 proposal — canonical set, exact case, one key, colon form, real binding
CANON = {"Claude Code": {"paths"}, "VS Code": {"applyTo"},
         "Copilot CLI": {"applyTo"}, "Cursor": {"globs"}}

QT = re.compile(r"^[ \t\-\[\|>]*([\"\'])")


def path_value_strict(raw):
    """A1 value test (new helper; v2's pattern_value is untouched).

    Rejects the markdown/prose families the r60 sweep found: inline-code
    values, an unquoted bare `**`, and asterisk tokens that are neither a
    slash/dot-bearing glob nor all asterisks (`**Team`, `Configure**`)."""
    raw = raw or ""
    tok = c.first_value_token(raw)
    if not tok or "*" not in tok or c.PATTERN_TOKEN_RE.match(tok) is None:
        return False
    if raw.lstrip()[:1] == "`":
        return False
    quoted = QT.match(raw) is not None
    if set(tok) <= {"*"}:
        return quoted
    if "/" not in tok and "." not in tok:
        return False
    return True


def a1_guarded(ctx):
    """A1: exact set, one key span, colon form, no comment, no negation,
    strict path-like block value, path-like examples only."""
    if "error" in ctx:
        return [ctx["error"]]
    cell, client = ctx["scope_cell"], ctx["client"]
    why = []
    spans = c.BACKTICK_RE.findall(cell)
    idents = [s.strip() for s in spans if c.KEY_IDENT_RE.match(s.strip())]
    if len(idents) != 1:
        why.append("A1g: scope cell names %d key identifier(s) %r (need exactly 1)"
                   % (len(idents), idents))
        return why
    key = idents[0]
    if key not in CANON[client]:
        why.append("A1g: key %r not in the canonical set for %s" % (key, client))
    for sv in spans:
        sv = sv.strip()
        if sv == key or c.KEY_IDENT_RE.match(sv) or c.CITE_RE.fullmatch(sv):
            continue
        if not path_value_strict(sv):
            why.append("A1g: scope cell span %r is neither a key, a citation "
                       "nor a path-like example" % sv)
    L, lines = ctx["key_line"], ctx["lines"]
    if L is None or not (1 <= L <= len(lines)):
        why.append("A1g: no key line")
        return why
    line = lines[L - 1]
    if re.match(r"^\s*(#|//|<!--)", line):
        why.append("A1g: key line %s is commented out" % L)
        return why
    good = False
    for i, j in c.key_occurrences(line, key):
        m = re.match(r"[\"'`]?[ \t]*:", line[j:])      # colon form only
        if m is None:
            continue
        pre = line[max(0, i - 60):i].lower()
        if re.search(r"\b(not|never|avoid|instead)\b|n't", pre):
            continue
        rest = line[j + m.end():]
        if c.block_only(rest):                          # G9: keep the block value
            src = None
            for nxt in lines[L:L + 3]:
                if nxt.strip():
                    src = nxt
                    break
            if src is None or not src.lstrip().startswith(("-", '"', "'", "`")):
                continue
        else:
            src = rest
        if path_value_strict(src):
            good = True
            break
    if not good:
        why.append("A1g: key %r has no clean colon-form site with a path-like "
                   "value at %s:%s" % (key, ctx["sid"], L))
    return why
```

Guard list and costs:

| guard | rule | cost / assertion to change |
|---|---|---|
| G1 | exactly one backticked key identifier in the Scope cell | self-test line 1572's two-identifier fixture becomes a rejection test |
| G2 | exact-case canonical membership; no `.lower()`/`casefold()` in A1 | none |
| G3 | exact string membership; no prefix/plural/alias | none |
| G4 | every non-key, non-citation backticked span in the cell is path-like | none on the four eligible cells |
| G5 | strict value grammar (`path_value_strict`) | keep `pattern_value` for v2 compatibility; new assertions only |
| G6 | reject a commented key line (`#`, `//`, `<!--`) | none |
| G7 | reject a key site preceded (60 chars) by not/never/avoid/instead/n't | none on the eligible lines |
| G8 | colon form only for A1's binding | self-test line 1657 (`=` is a key form) must change or the risk must be declared |
| G9 | keep v2's block-value lookahead, and say so in the arm text | none; without it the Claude row fails |

Measured validation of the guarded model: pristine world 4 of 4 PASS; all fifteen mutants
rejected on the mutated client; see §3 and the pasted `guarded=` marks.

## 6. Integration hazards this attack exposes

1. **The set citation is not the binding citation.** S112's own report says its line 94 (the
   frontmatter-field table row) "names the key but contains no concrete path-pattern value"; the
   value example is S103:198-199. A1's membership is grounded in S112–S115, but the per-row
   binding must stay on a real key site. Do not move the Claude Code Scope citation to S112:94:
   that line is a table-cell form and has no path value. Similarly, S115:131 is prose
   ("Use `globs` to scope a rule…", no colon after the key); the Cursor row must keep :85
   (frontmatter example). S114:66 is a real key site in the committed S106 bytes (identical
   sha256); S113:177 is a key-form YAML example per the uncommitted S113 draft
   (`applyTo: '**/*.py'`, `sed -n '177p'` in `ScribeS113.md`), not bytes I could verify in the
   lane.
2. **The committed self-test's synthetic world cannot survive the per-client set unchanged.**
   `self_test` builds a four-client world whose fourth client is **Gemini CLI** with key
   `globs` (`check_scoped_rules.py:1807-1815`: `four = [... "Gemini CLI"]`; expected
   `[("paths",5),("applyTo",4),("applyTo",4),("globs",4)]`). The real per-client set from
   S112–S115 has no Gemini entry (S107 documents directory discovery, no path-pattern key), and
   the real eligible four are Claude Code / VS Code / Copilot CLI / Cursor. A literal A1
   implementation therefore drops that fixture from 4 backed to 3 and breaks at least the
   assertions at lines 1809, 1812, 1815 and the downstream `three = [...]` uses. The v3
   self-test must mirror the real four (Cursor, not Gemini) or carry an explicit, justified
   fixture-only mapping.
3. **Existing self-test assertions that the guards touch:** line 1572 (first span is the key),
   line 1605 (bare `**` is a pattern — keep, because `applyTo: "**"` is real; the new helper is
   quote-aware), line 1616 (block value two lines down passes — keep), line 1657 (`=` is a key
   form — G8 changes the A1 binding, not necessarily `key_site`), line 1824 (a second entry row
   does not disqualify a good one — unchanged; entry rows carry no Scope key).
4. **`applyTo` is canonical for two clients.** A1's set cannot distinguish VS Code from Copilot
   CLI by key name; the host pin does (`HOSTS["VS Code"]` has no `docs.github.com`, and
   `HOSTS["Copilot CLI"]` has no `code.visualstudio.com`). Do not describe A1 as
   client-authenticating on its own; it is per-client *given* the host pin.
5. **A1 does not read the Action cell.** A wrong key named in the Action text (e.g. "set
   `patterns:`…") is outside A1. If the L1 wants that covered, it belongs to A2's action
   support, not A1; state the boundary rather than widening A1 silently.
6. **The "held table" caution.** CriticC1Scope's point stands: the four key decisions were
   already held at the r61 base. A1-v3's contribution is discrimination (the r60 counterexamples
   now reject), not new key discovery. My mutants are the discrimination evidence; they are not
   a novelty claim.

## 7. What I did not verify

- No v3 counter existed in the wave directory when this ran (`.ufo/waves/round-61/wave/` had no
  `ExecCounterV3.md`; no `ExecCounterV3` scratch directory). The A1 verdicts here are from the
  literal reference implementation in §5 over the same world bytes, scored alongside the
  committed v2 CLI. They are not a measurement of the integrated v3.
- No `--fetch` and no network. The live half of the C1 predicate is not claimed here; the
  ground for it is the r60 receipts and `MutWorldW5W6`'s W5 live runs (4 of 4, exit 0), which I
  did not re-run.
- The page-mutated mutants (V1b, V3, V3b, V8, V9, V10, V11) append authored fixture lines to
  committed snapshots and re-pin the SOURCES sha. They are fixture worlds, not claim that those
  lines exist on the live vendor pages today. A4's provenance arm is not modeled here; an
  authored fixture committed on the row's open date would not be caught by A4's date test
  either (that arm's declared limit).
- The guarded implementation was not reviewed or integrated; its correctness beyond these 16
  worlds (baseline + 15 mutants) is unverified. I did not modify the frozen claim, the predicate sentence, or W5's
  required outcome.

## 8. Restoration evidence

Sandbox only; the lane was never written. After the fifteen variant commits the tracked files
were restored from the pristine commit, committed as `291aeb730b09bc3a87b3c98b527c82eb2bec2b44`
(`mutA1: restore pristine tracked bytes after the attack probes`):

```
$ git diff --stat c630c4cbc01ff5e5438ab0033cfadd6e19382ab1
(no output)
$ git status --porcelain | grep -v '^??' | wc -l
0
$ sha256sum SKILL.md corpus/SOURCES.md .ufo/waves/round-60/snapshots/S103.page .ufo/waves/round-60/snapshots/S105.page
2d2c1d5f78bc3d5f6dcb4ee30b40ccc647c286bf63a76f49127e60558b9a3909  SKILL.md
ddc5bfe0e86c178a266457d045107ee952fd3dd5f022be721da9c782dfc711de  corpus/SOURCES.md
82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7  .ufo/waves/round-60/snapshots/S103.page
a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f  .ufo/waves/round-60/snapshots/S105.page
```

The four hashes equal the before-values recorded at the start of the probe: SKILL.md
`2d2c1d5f…`, SOURCES.md `ddc5bfe0…`, S103 `82d60341…`, S105 `a45c9e9f…` (the same four digests printed above); they are unchanged. CLI at the restored commit:

```
scoped rule files backed on committed snapshots 4 of 4; live not run
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a; rev 291aeb730b09bc3a87b3c98b527c82eb2bec2b44
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
```
(exit 1: the offline predicate needs `--fetch`, as declared in §1.)

The restore run's before/after file hashes and the per-variant commit ids are in the probe
record (`/fast/scratch/hyaku/kotoba-r61/MutA1/attack.out`, run at
`Fri Oct 23 07:18:35 PM UTC 2026`, script exit 0; restore at `07:19:49 PM UTC`).

## 9. Fixture bundle (drop-in inputs for the v3 self-test / W5)

Exact deltas; "append S103:665" means one line appended to
`.ufo/waves/round-60/snapshots/S103.page` (664 lines before append) with the S103 SOURCES
sha re-pinned; "append S105:368" the same for S105 (367 lines before).

| id | Scope cell (exact) | page delta | expected A1 v3 |
|---|---|---|---|
| V1 | `` `PATHS` (e.g. `src/api/**/*.ts`, S103 :198) `` | none | reject (set/binding) |
| V1b | `` `PATHS` (S103 :665) `` | append `PATHS: src/legacy/**/*.ts` | reject (set) |
| V2 | `` `paths` and `patterns` (e.g. `src/api/**/*.ts`, S103 :198) `` | none | reject (multiplicity) |
| V2b | `` `paths` (S103 :198; the page also shows `claudeMdExcludes`, S103 :339) `` | none | reject (multiplicity) |
| V13 | `` `paths` (S103 :198) or `applyTo` (S105 :164) `` | none | reject (multiplicity) |
| V3 | `` `paths` (S103 :665) `` | append `paths: the files listed below` | reject (value) |
| V3b | `` `paths` (S103 :665) `` | append `paths: **see the note below**` | reject (value grammar) |
| V5 | `` `patterns` (S103 :238) `` | none | reject (set) |
| V6 | `` `claudeMdExcludes` (S103 :339) `` | none | reject (set) |
| V7 | VS Code: `` `sessions` (S105 :32) `` | none | reject (set/value) |
| V8 | `` `path` (S103 :665) `` | append `path: src/legacy/**/*.ts` | reject (set) |
| V9 | `` `paths` (S103 :665) `` | append `# paths: src/legacy/**/*.ts` | reject (comment) |
| V10 | `` `paths` (S103 :665) `` | append `Do not set paths: src/legacy/**/*.ts in a rule that should load for every file.` | reject (negation) |
| V11 | VS Code: `` `applyTo` (S105 :368) `` | append `applyTo='src/legacy/**/*.py'` | reject (colon/form) |
| V12 | `` `paths` (e.g. `see below`, S103 :198) `` | none | reject (example) |

V5–V7 are the frozen W5 class (`sessions`/`patterns`/`claudeMdExcludes`); the rest are the
additional letter-level and slip-level arms this seat contributes.

## 10. Installs, blockers, one line

Installs: no installs (nothing was missing; no pacman transaction was attempted, per the
host-wide pause).

Blockers: none.

One line: Attacked arm A1 by building fifteen row+world mutants against the committed v2
counter (13 of the 15 backed 4 of 4 under v2; eight survive A1 exactly as written), measured the case-fold,
prefix, widened-set and strict-line slips, and validated a guarded A1 that keeps the pristine
world at 4 of 4 while rejecting all fifteen — with exact bytes restored and re-hashed.
