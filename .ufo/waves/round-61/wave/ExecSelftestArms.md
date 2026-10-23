# ExecSelftestArms — the v3 self-test arm inventory (A1–A4 killers + equivalence fixtures)

Seat: `kotoba-r61-wave-ExecSelftestArms` (executor, axis: operability). Date: 2026-10-23.
Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin` — **read-only to this seat**; the only
file written is this report. No git/jj mutation, no dispatch, no ask tool, no subagent.
Scratch (untrusted, never cited as evidence): `/fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ExecSelftestArms/probe/`.

Ground read: `plans/round-61.md` (as amended by errata **E1, E2, E2b, E2c, E2d** — the plan
is canonical over the dispatch text), `verifiers/check_scoped_rules.py` (v2, sha256
`ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`, 2567 lines),
`corpus/SOURCES.md`, `corpus/knowledge/scoped-rules-round60.md`, `corpus/lessons/round-60.md`,
`.ufo/waves/round-60/{controls,controls-v2,build,snapshots}/`,
`corpus/lessons/round-60-verifier-spotcheck.md` §7–§8, and the committed r61 wave reports
`MutV2Regress.md`, `MutA1.md`, `MutA2.md`, `MutA3.md`, `MutA4.md`, `MutFixtures.md`,
`MutWorldW5W6.md`, `CriticHollowC1.md`, `MutFixtureEscape.md`, `ScribeEntryV3.md`,
`ScribeS112–S115.md`, `ScoutFixtureBytes.md`, `RevPredicate.md`.

**Nothing here is a v3 measurement.** No v3 counter exists at the lane tip
(`cf288d84b1a6f128855ccf92178404c6a53e7bdf`); the committed counter is still v2. Every
"expected" below is a *design* expectation validated against a scratch reference model whose
per-arm predicates are quoted in full, so the L1 can implement them or reject them. Where I
measured something about committed bytes, I say so; where I designed something, I say that too.

---

## 0. Executive summary — the five findings the L1 must act on

| # | Finding | Consequence for the v3 self-test |
|---|---|---|
| **F1** | **v2's synthetic self-test world cannot be carried into v3 unchanged.** v2's world is Claude Code / Gemini CLI / VS Code / Copilot CLI with keys `paths`/`globs`/`applyTo`/`applyTo`. The frozen v3 key set (E2d) has **no Gemini CLI member** (S112–S115 cover exactly Claude Code, VS Code, Copilot CLI, Cursor). Under A1 the v2 Gemini row is rejected, so **46 of v2's 318 assertions** (8 expecting `four`, 38 expecting `three`) fail on a *correct* v3. | v3 must **re-base the synthetic world** onto the four canonical clients (Claude Code / VS Code / Copilot CLI / Cursor) and re-point the 22 assertions that name Gemini-specific fixtures. This is a *fixture* migration, not a lost assertion: all 318 remain, with renamed fixtures. |
| **F2** | **A1's key set is read from the committed S112–S115 row texts at the measured revision** (E2d). I implemented and measured that derivation: the id→client map is pinned in the counter, the **key** comes from the row's own `teaches` cell (the unique bare-identifier backticked span). On the four committed scribe drafts this yields exactly `paths`/`applyTo`/`applyTo`/`globs`; on the base-revision SOURCES it yields **empty**, which is the declared base-discriminating mechanism. | A1's canonical-set reader is a **new function with no v2 counterpart** and needs its own assertions. It is also the arm's *poisoning* surface (see F4). |
| **F3** | **The A2 killer must be the published W6 cell, not a paraphrase.** Measured on the committed bytes: the published cell *"Create the rule file in the project and add frontmatter so it loads only for the matching files."* cited at `S103:209` **passes v2's lexical gate** (`action_conjunct(...) == []`) — so it is admissible under MutFixtures' rule — and is rejected by A2 because the cited line states a **universal** scope while the cell claims an **exclusive** one. A paraphrase at a line v2 already rejects is inadmissible (the world would reject for the old reason and A2 could be deleted unnoticed). | Use the published cell as the A2 killer. **But** the claim must be asserted as *behaviour* (row rejected), not as a reason string — see F5. |
| **F4** | **A1's key set is poisoning-sensitive.** The set is read from rows, so a row that names a wrong key in its `teaches` cell would widen the set for its client. The id→client map must therefore stay **pinned in the counter** and the key extracted fail-closed (exactly one bare-identifier backticked span in `teaches`, else the client's set is empty). | The A1 assertion set must include a **fail-closed** case: a key row with 0 or ≥2 bare-identifier spans yields an **empty** set for that client, and every row of that client is then rejected. |
| **F5** | **The predicate line must be computed.** MutFixtures T9 and the L1 steering both require it. v2's self-test prints `self-test: 0 failure(s) over 318 assertions`; v3 must additionally print `worlds reject 7 of 7; eligible rows pass 4 of 4` **derived from the scored worlds**, never literal. A hard-coded print + `return 0` passes every other check. | The self-test must build the sentence from two counted integers. Add an assertion that a deliberately mis-scored world changes the sentence and the exit code. |

---

## 1. The v3 self-test structure: keep v2's 318, add the arms

### 1.1 What v2's self-test is, exactly (read, not assumed)

`check_scoped_rules.py:1270–2490` is one function, `self_test()`, with a local
`check(name, actual, expected)` helper (:1274) that prints `FAIL <name>: got …, expected …`
and counts. Measured by AST parse of the committed file:

```
$ python3 -B -c "<ast parse of self_test()>"
total check() calls parsed: 318
```

The 318 assertions fall into 26 labelled sections (`:1282` … `:2423`). The load-bearing
structure for v3 is:

* **unit section** (:1282–1668) — pure helper assertions (`rev_ok`, `token_well_formed`,
  `normalise`, `foreign_marker`, `token_span`, `quote_in_gate`, `url_key`, `host_ok`,
  `norm_page`, `row_sha`, `summary_line`, `predicate`, `scope_key`, `citations`,
  `citation_why`, `pattern_value`, `first_value_token`, `block_only`, `key_site`,
  `any_key_site`, `content_words`, `action_need`, `action_conjunct`).
* **synthetic world** (:1670–1815) — `page900…903`, `PAGES`, `QUOTES`, `OWNERS`, `URLS`,
  `src_row`, `world(pages, teaches)`, `ro(teaches)`, `base_reopen`, `REOPENS`; helpers
  `judge_world`, `backed`, `why_of`, `k_of`, `with_quote`.
* **judge-level red/green** (:1817–2163) — the ~90 assertions that mutate the synthetic
  world and assert `backed(...)` outcomes.
* **fetch policy** (:2164–2237) — `curl_argv`, `run_curl` monkeypatching, redirect rules.
* **two end-to-end `main()` paths** (:2244–2490) — real temp git repos
  (`tempfile.TemporaryDirectory(prefix="csr-main-")`, `_self_git`), a `base` commit and a
  `measured` commit, `run_curl` replaced by canned `(status, url, body)` responses.
  These two blocks are the only places the self-test exercises `git show`/history.

### 1.2 The v3 self-test layout I propose (drop-in, additive)

```
def self_test() -> int:
    # ---- BLOCK 1 (v2, carried VERBATIM) : 318 assertions, unchanged ----
    ... the whole of v2's self_test(), with ONE structural edit (F1) ...
    # ---- BLOCK 2 (v3, new) : the four arms ----
    #   A1: canonical key set (reader + membership + fail-closed)
    #   A2: clause-level support + polarity + exclusivity
    #   A3: url_key identity (re-open) + alias rendering (fresh row)
    #   A4: sha equality + verbatim quote + first-commit date + base-sha alias
    # ---- BLOCK 3 (v3, new) : the arm-killers (4) ----
    # ---- BLOCK 4 (v3, new) : the equivalence fixtures (9) ----
    # ---- BLOCK 5 (v3, new) : the seven worlds + the computed predicate line ----
    print("worlds reject %d of %d; eligible rows pass %d of %d" % (...))
    return 1 if failures else 0
```

**The 318 baseline is preserved as 318.** v3's counter prints
`self-test: 0 failure(s) over <N> assertions` where `N = 318 + (new)`. The new-arm count is
the L1's to fix once the arm assertions are drafted; my inventory below names **4 arm-killers
+ 9 equivalence fixtures + 1 computed-predicate assertion = 14 new assertions**, so the
expected total is **332** if the L1 adopts exactly this set.

### 1.3 F1 in detail — the synthetic world must be re-based, and here is the exact list

The v2 synthetic world's four clients are Claude Code, **Gemini CLI**, VS Code, Copilot CLI.
The frozen v3 key set has members for Claude Code, VS Code, Copilot CLI and **Cursor**. Gemini
CLI is a *negative* client (its r60 row says "no scoped rule file"). So under A1 the v2
Gemini row is rejected and every assertion that expects a backed Gemini row fails.

Measured (AST parse of the committed file, expected argument of each `check` call):

```
assertions whose EXPECTED is the `four` list: 8
assertions whose EXPECTED is the `three` list: 38
total list-dependent: 46

assertions naming a Gemini-specific fixture id/token: 22
   1308 green: .gemini/rules/
   1368 normalise strips one trailing /
   1383 a gemini token is not foreign to Gemini CLI
   1581 citations: both forms are read
   1588 citation: another row's id is a named failure
   1824 a second entry row does not disqualify a good one
   1832 no entry row for the client is not backed
   1885 a malformed rule token is not backed and leaves K
   1892 a rule cell without a backticked token is not backed
   1895 a token carrying another client's marker is not backed
   1898 the foreign marker is reported as such
   1935 an entry source cell that is not one S### id is not backed
   1938 an S### absent from SOURCES.md is not backed
   1951 E4: an entry Rule files cell that differs from SKILL.md is not backed
   1955 E4: a backticked Rule files cell still backs
   1958 E4: the raw ./ form in the cell still backs
   1962 E4: the normalised form is not the raw cell of a ./ token
   1969 a missing snapshot is not backed
   1973 a missing snapshot is reported as missing
   2069 a scope key citing another row's source is not backed
   2074 an action citing another row's source is not backed
   2431 v2 fixture: two of the three measured rows are re-opens
```

**The migration, exactly:** in the synthetic world, replace the **Gemini CLI** row with a
**Cursor** row (`S901`→`S904` slot, token `.cursor/rules`, key `globs`, the r60 Cursor quote
and page), and re-point the 22 Gemini-named assertions at the new slot. The 46 list-dependent
assertions keep their *shape* — the `four`/`three` list literals simply become
`["Claude Code", "VS Code", "Copilot CLI", "Cursor"]` and
`["VS Code", "Copilot CLI", "Cursor"]`. **No assertion is dropped; the count stays 318.**

This is also what the plan's own equivalence requirement implies: MutFixtures S6 says the four
eligible rows must be the **real r60 rows** (Claude/VS Code/Copilot CLI/Cursor), and the
synthetic S900–S903 world's Gemini row is not one of them.

**Two unit assertions are unaffected and must NOT be re-pointed:** `green: .gemini/rules/`
(:1308) and `normalise strips one trailing /` (:1368) test the *token grammar*, not the
world; `.gemini/rules/` is a legal token and stays a legal token. Only the **world-level**
assertions move.

---

## 2. The arm-killers — four fixtures, each failing ONLY if its own arm is deleted or inverted

Each killer below is stated as: the fixture bytes, the arm that must reject it, the **exact
expected failure line**, the paired positive that must pass in the same run, and the
deletion matrix that proves single-defectness.

### 2.0 The single-defect property, and how it is proved

> An **arm-killer** for arm *i* is a fixture whose row is **rejected** when arm *i* is
> present, and whose row **flips to backed** when arm *i* is deleted *or* inverted, while
> deleting any *other* arm leaves it rejected.

I built a scratch reference model of the four arms (full source in §7) on top of the
committed v2 helpers, and ran the **deletion matrix** — pristine, each arm off in turn, and
each arm inverted in turn:

```
$ cd /fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ExecSelftestArms/probe
$ python3 -B matrix.py
arm  client        pristine   A1off      A2off      A3off      A4off
----------------------------------------------------------------------------
A1   VS Code       REJ        BACK       REJ        REJ        REJ
     inverted A1   -> BACK (want BACK)
A2   Claude Code   REJ        REJ        BACK       REJ        REJ
     inverted A2   -> BACK (want BACK)
A3   Claude Code   REJ        REJ        REJ        BACK       REJ
     inverted A3   -> BACK (want BACK)
A4   Claude Code   REJ        REJ        REJ        REJ        BACK
     inverted A4   -> BACK (want BACK)

MATRIX OK
```

Every killer is single-defect: it flips **only** under its own arm, deleted or inverted.

### 2.1 KILLER A1 — the scope key is outside the client's canonical set

**Fixture bytes** (the SKILL.md `### Scoped rule files by client` row, VS Code). The
committed r60 row is:

```
| VS Code | `.github/instructions/**/*.instructions.md` (Local-harness targeted instructions, S105 :32) | `applyTo` (`**/*.py`, S105 :164) | Use multiple instruction files per topic and apply them selectively (S105 :329) |
```

The killer replaces **only** the Scope-key cell:

```
| VS Code | `.github/instructions/**/*.instructions.md` (Local-harness targeted instructions, S105 :32) | `sessions` (S105 :32) | Use multiple instruction files per topic and apply them selectively (S105 :329) |
```

**Why `sessions` and not a synthetic key.** `sessions` is *form-valid on the real page* —
measured on the committed `S105.page`:

```
key_site(S105,32,'sessions') = True
scope_conjunct = []
line 32: '> **For Local harness sessions:** Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`. Targeted instructions can use `.g…'
```

so **v2's form test passes** and only A1's canonical-set membership can reject the row. It is
also one of the six keys `ExecKeyForms.md` measured as passing v2 end-to-end, so it is the
recorded W5 class, not a new invention. (MutFixtures warns against a six-name deny-list; the
arm here is *set membership per client*, so a deny-list would fail the paired positive and the
held-out case in §3.)

**Expected failure line** (exact, for the `reject <client>: <reasons>` line the counter
prints):

```
reject VS Code: entry row S105: A1 scope key 'sessions' is not in the canonical key set for VS Code
```

**Paired positive, same run:** the committed VS Code row with `applyTo` at `S105:164` — backed.

**Deletion matrix row:** A1 off → BACK; A2/A3/A4 off → REJ. **Measured: as above.**

### 2.2 KILLER A2 — the Action cell contradicts the cited line

**Fixture bytes** — the committed r60 Claude Code row with **only the Action cell** replaced
by the **published W6 cell** (`build/ExecKeyForms.md` Part 2 / `MutWorldW5W6.md`):

```
| Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `paths` (e.g. `src/api/**/*.ts`, S103 :198) | Create the rule file in the project and add frontmatter so it loads only for the matching files. (S103 :209) |
```

**Admissibility, measured on the committed bytes** — the killer must pass v2's lexical gate,
or the world would reject for the old reason and A2 could be deleted unnoticed:

```
$ python3 -B <probe>
=== the PUBLISHED W6 cell on the real S103 bytes ===
  v2 action_conjunct at :209 = []    <- empty means v2's lexical gate ACCEPTS it (admissible)
  A2 why = ["A2 the action claim 'Create the rule file in the project and add frontmatter so i' contradicts the cited line 209 (the line states a universal scope)"]
  paired positive (real cell at :194): A2 why = []
```

The cited line `S103.page:209` reads:

```
Rules without a `paths` field are loaded unconditionally and apply to all files. A path-scoped rule loads when Claude uses the Read, Write, or Edit tool on a matching file. …
```

The cell claims the rule loads **only** for matching files; the line says it applies to
**all** files (and that rules *without* `paths` load unconditionally). That is an
exclusivity-vs-universality contradiction — a semantic defect no vocabulary threshold can
see, which is exactly what the frozen A2 sentence demands ("not vocabulary matching alone").

**Expected failure line:**

```
reject Claude Code: entry row S103: A2 the action claim 'Create the rule file in the project and add frontmatter so it loads only for the matching files.' contradicts the cited line 209 (the line states a universal scope)
```

**Paired positive, same run:** the committed Claude Code Action cell
`Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194)` — backed.

**A held-out second A2 killer** (the L1 should carry both, so the arm cannot be a phrase
match): the **CriticHollowC1 polarity inversion** at the same line —

```
| Claude Code | `.claude/rules/` (multi-file instructions, scoped to matching files; S103 :168) | `paths` (e.g. `src/api/**/*.ts`, S103 :198) | No path-scoped rule loads when Claude uses the Read, Write, or Edit tool on a matching file. (S103 :209) |
```

Expected line: `reject Claude Code: entry row S103: A2 the action claim 'No path-scoped rule loads when Claude uses the Read, Write, …' contradicts the cited line 209`.
**Measured:** it also passes v2's lexical gate (`action_conjunct == []`) and is rejected by A2.

**Deletion matrix row:** A2 off → BACK; A1/A3/A4 off → REJ. **Measured: as above.**

### 2.3 KILLER A3 — the row's URL is an alias rendering of a URL the lane already holds

**A3 is two clauses** after E2 + E2b:
* **(a) re-open rows:** the row's URL must have the same `url_key` as its **base row's** URL
  (E2 — *not* byte identity; MutA3 proved byte identity unsatisfiable on S108/S049).
* **(b) fresh rows:** the row's URL must not be an alias rendering of an existing same-host
  row's URL — differing only by a **locale path segment** (`/de/`, `/ja/`, …) or an
  **`@version`/`enterprise` suffix** (E2b).

**Fixture bytes.** The recorded W2 alias URLs are *fresh* rows (not re-opens) — the recorded
W2 world is `CtlReopenHeldKey b`, whose German and enterprise URLs were "fetched without
redirect to a base URL". So clause (a) never evaluates them, and **clause (b) is the A3
killer**. The fixture is a fresh Claude Code row whose URL is the German rendering of the
URL the lane already holds:

```
| S103 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/de/memory.md | docs | A | … | … | re-opens S043 — … | mined | 2026-10-23 | 90d | … |
```

with the **real** German page bytes (sha256
`c568aae2c633029aa6a8b612de437f275bbe8f39c5866ef7382f89073e7f9c43`, 63,447 B — the digest
recorded in `.ufo/waves/round-60/controls-v2/CtlReopenHeldKey.md`), the real German
quote/key/action lines, and the real `paths` key at the German page's key site. The URL
differs from the lane's `https://code.claude.com/docs/en/memory.md` by exactly one path
segment, `en` → `de`.

**Expected failure line:**

```
reject Claude Code: entry row S103: A3 row URL 'https://code.claude.com/docs/de/memory.md' is an alias rendering of a URL the lane already holds
```

**Paired positive, same run:** the committed Claude Code row (S103, URL
`…/docs/en/memory.md`, re-opens S043) — backed.

**A second A3 killer for clause (a)** (url_key identity on a re-open): a re-open row naming a
base row whose URL has a **different `url_key`** — e.g. a re-open of S043 whose URL is
`https://code.claude.com/docs/de/memory.md` (different key → rejected under both v2's
`reopen_why` and A3(a)) versus the *same-key-different-bytes* pair
`https://cursor.com/docs/rules` vs `https://cursor.com/docs/rules.md` (same key → **accepted**;
that pair is the E2 limit and must be an equivalence fixture, §3.7).

**Deletion matrix row:** A3 off → BACK; A1/A2/A4 off → REJ. **Measured: as above.**

### 2.4 KILLER A4 — the row's snapshot digest is already recorded in the base table

**A4 has four conjuncts** after E2c: (i) recorded sha256 = committed bytes; (ii) the located
quote occurs verbatim in them; (iii) the earliest commit introducing those bytes is no older
than the row's recorded open date (consistency only); (iv) **the row's full 64-hex snapshot
sha256 must not already be recorded in the base-revision SOURCES table**, unless the teaches
cell declares byte-identity via `supersedes S###`.

**The killer targets (iv)** — the new conjunct, which is the only one that rejects the real
W1. Measured on the committed bytes:

```
=== A4(iv) discriminator: is the FULL 64-hex sha recorded in BASE SOURCES? ===
  S103 Claude                    full64-in-base=False  prefix8-occurrences-in-base=0
  S105 VS Code                   full64-in-base=False  prefix8-occurrences-in-base=0
  S106 Copilot                  full64-in-base=False  prefix8-occurrences-in-base=1
  S108 Cursor                   full64-in-base=False  prefix8-occurrences-in-base=1
  W1 r53 Claude (S043 pin)      full64-in-base=True   prefix8-occurrences-in-base=1
```

(BASE here = the counter's pinned base `31092dc6…`.) The four eligible rows alias their bases
only by an **8-hex prefix**; W1's forged S103 row pins `971d75bf…` **in full**, which base row
S043 also records in full → A4(iv) rejects.

**Fixture bytes** — the W1 world, rebuilt: the three d-world rows (Claude `paths`, Copilot
`applyTo`, Cursor `globs`), real quote/key/action lines, the round-53 scratch bytes as the
snapshots (Claude `971d75bf…`, 51,971 B; Copilot `00e45ea5…`; Cursor `884c67ca…`), the SOURCES
rows pinning those digests in full, and the retained forged claim
`Fetched 2026-10-23T12:06:23Z`. **One defect only:** the Claude row's teaches cell declares
**no** `supersedes S###` byte-identity.

**Expected failure line:**

```
reject Claude Code: entry row S103: A4 the row's full snapshot sha256 is already recorded in the base-revision SOURCES table
```

**Paired positive, same run:** the same row with teaches cell
`supersedes S043 — byte-identical reuse of the recorded page bytes` → **backed** (the S110
precedent the plan names).

**Deletion matrix row:** A4 off → BACK; A1/A2/A3 off → REJ. **Measured: as above.**

**Three further A4 killers the L1 must add** (each conjunct needs its own single-defect
fixture; only (iv) is covered by the W1 world):

| # | defect | fixture | expected rejection |
|---|---|---|---|
| A4-i | sha ≠ committed bytes | any eligible row, snapshot byte flipped | `A4 snapshot … sha256 does not equal the SOURCES row sha256` |
| A4-ii | quote not verbatim in the bytes | any eligible row, quote reworded so it is absent | `A4 the located quote does not occur in the committed snapshot bytes` |
| A4-iii | first commit older than the opened date | a **two-commit** fixture repo: commit A (2026-10-22) adds the blob, commit B (2026-10-23) adds the rows | `A4 the earliest commit introducing the snapshot bytes is dated 2026-10-22, older than the row's opened date 2026-10-23` |

A4-iii **requires a real git history** — it cannot be exercised by `judge()` over in-memory
bytes. v2's self-test already has the machinery (`_self_git`, two temp-repo commits at
`:2281` and `:2434`); the A4-iii fixture reuses it with **fixed receipt dates**, never the
host clock (MutFixtures T8). The paired positive is the same world with the blob-add commit
dated 2026-10-23 → backed.

---

## 3. The equivalence fixtures — nine benign rows that must keep their verdicts

An **equivalence fixture** is a benign row whose verdict must be **identical** under v3 and
under v2. They are the no-harm half of the inventory: if v3 changes one of these verdicts, the
redesign has regressed, whether or not the arm-killers still pass.

| # | fixture | committed bytes | v2 verdict | v3 verdict (required) |
|---|---|---|---|---|
| **E-1** | the four eligible r60 rows | `SKILL.md:141,143,144,146`; entry rows 15–18; S103/S105/S106/S108 | 4 of 4 backed | **4 of 4 backed** |
| **E-2** | Codex row (negative client) | `SKILL.md:142`; `S104.page` | rejected: `SKILL.md rule-files cell holds no backticked token; no entry row names the client` | **same rejection** |
| **E-3** | Gemini CLI row (negative client) | `SKILL.md:145`; `S107.page` | same as E-2 | **same rejection** |
| **E-4** | opencode row (negative client) | `SKILL.md:147`; `S109.page` | same as E-2 | **same rejection** |
| **E-5** | a re-open row whose **base row already holds K** | synthetic: base row S022's line holds `paths`; row re-opens S022 | rejected: `base row S022 already records key paths` | **same rejection** (E1 sub-rule 4 of 5) |
| **E-6** | a re-open row with a **byte-identical** base URL | the S103 re-open of S043 | backed | **backed** |
| **E-7** | the **same-key-different-bytes** pair | `https://cursor.com/docs/rules` vs base `…/rules.md` | accepted (v2's `url_key` normalises `.md`) | **accepted** — this is the **E2 disclosed limit**; A3(a) is url_key identity, so this pair must NOT be rejected |
| **E-8** | the four **canonical-equivalence spellings** of a base URL | trailing `/`, `.md` drop, query, fragment, scheme/host case, `www.`, default port, percent path, http downgrade, path case (MutA3's table, 11 spellings) | accepted | **accepted** — the E2 limit, pinned as an equivalence row so a future tightening is a declared change, not a silent one |
| **E-9** | the **Gate-quote** rule (inherited from r59, unnamed by A1–A4) | `corpus/lessons/round-60.md` `## Gate` | quote must appear in the Gate | **must still be required** (see §4.3) |

### 3.1 E-1 measured on the committed bytes

I scored the real r60 rows with the reference model (committed `SKILL.md`, entry,
`SOURCES.md`, lesson and the four committed snapshots):

```
$ python3 -B real.py
### A1 canonical key set read from the committed S112-S115 row texts
  without S112-S115 (base)     {}
  with S112-S115 (data rev)    {'Claude Code': ['paths'], 'VS Code': ['applyTo'], 'Copilot CLI': ['applyTo'], 'Cursor': ['globs']}

### real r60 rows under the candidate arms (committed lane bytes)
  -- data SOURCES (with key rows)
     Claude Code  row=S103  key=paths    BACK
     Codex        row=None  key=None     rej   SKILL.md rule-files cell holds no backticked token; no entry row names the client
     VS Code      row=S105  key=applyTo  BACK
     Copilot CLI  row=S106  key=applyTo  BACK
     Gemini CLI   row=None  key=None     rej   SKILL.md rule-files cell holds no backticked token; no entry row names the client
     Cursor       row=S108  key=globs    BACK
     opencode     row=None  key=None     rej   SKILL.md rule-files cell holds no backticked token; no entry row names the client
     backed: 4 of 7
```

**4 of 4 eligible backed; 3 negative clients rejected** — E-1…E-4 confirmed against the
committed bytes.

### 3.2 E-5 measured

```
=== equivalence E-5: re-open whose base row already holds K ===
  backed: False
   - entry row S901: S901 URL '…/claude-directory.md' is already a base SOURCES URL; base row S022 already records key paths
```

### 3.3 E-7 / E-8 — the A3 limits are pinned as equivalence rows

These two rows are the **price of erratum E2**, and they are what stops a later v3 from
quietly re-tightening A3 back to byte identity. The exact spelling list and the
same-key-different-bytes pair are in MutA3's table (19 documented verdicts). They must be
asserted as **accepted**, so that a byte-identity re-tightening shows up as an E-7/E-8
failure, not as a silent "more secure" change.

### 3.4 The negative-client rows are *negative* fixtures, not equivalence failures

E-2…E-4 are the rows where the client has **no scoped rule file** (Codex, Gemini CLI,
opencode). Their verdict must stay "rejected". Under A1 these are the rows that prove the
canonical set is **per client** and that a client with **no** key-set member cannot be backed:
a client absent from S112–S115 has an **empty** canonical set, so any row claiming a scope
key for it is rejected. This is the fail-closed property of F4.

---

## 4. The subsumption map — which v2 assertions A1–A4 absorb, so nothing double-counts

MutV2Regress measured, by deleting one v2 conjunct per copy, which assertions kill each
conjunct. That is the port list. I add the **subsumption** column: which v3 arm now owns
each group, so the L1 does not write a second assertion for behaviour v2 already pins.

| v2 group | v2 assertions | killed by (MutV2Regress) | v3 owner | subsumed? |
|---|---|---|---|---|
| scope conjunct (form + path-like value) | 9 (`a scope key on a line with no pattern drops the row`, `the no-pattern key is reported with its key and line`, `a description whose value mentions a pattern still fails`, `the Cursor table-cell line is not a key form for description` / `for alwaysApply`, `a key only inside a longer identifier drops the row`, `an off-by-one citation to a line without the key drops the row`, `the off-by-one is reported at the cited line`, `a block value four lines down drops the row`) | M1 (9 kills) | **A1** (the *form* half) | **Yes** — A1's form half is v2's conjunct; v3 must keep these 9 as-is and add the *membership* half. Do not re-assert the form half under A1. |
| action conjunct (word threshold) | 8 (`an action on a citation line out of range is not backed`, `an action sharing one content word is not backed`, `the action shortfall is reported with its counts`, `an action with two content words is not backed`, `the thin action is reported with its count`, `a longer action needs half of its words, not two`, `the half threshold is reported with its counts`, `action: one shared word fails`) | M2 (8 kills) | **A2** (the *threshold* half) | **Yes** — A2 keeps the threshold as a floor and adds the support/polarity/exclusivity half. These 8 must not be re-asserted as "A2's new behaviour". |
| E1 re-open gate (static) | 9 (`a base URL is not backed`, `a base URL reached by a path-case alias is not backed`, `v2: base URLs without the re-open prefix are not backed`, `v2: the missing re-open is named`, `v2: the re-open prefix is a prefix, not a mention mid-cell`, `v2: a re-open naming a base row whose URL differs is not backed`, `v2: a re-open whose base row line already holds K is not backed`, `v2: the key collision is named`, `v2: a re-open naming a non-base id is not backed`) **+ the 2 accept assertions** (`v2: a base URL re-opened by its base id backs`, `v2: a plain hyphen is the same re-open separator`) | M3 (9 kills) | **A3(a)** + the **E1 sub-rules the L1 must port** | **Yes** — the URL-identity half of E1 *is* A3(a) under E2's url_key wording. The prefix-anchoring, target-is-base-row and held-key sub-rules are **E1's, not A3's** and must be ported verbatim (L1 steering: *all five*). |
| E1 live-fetch own-key gate | 2 (`fetch: a redirect to a base SOURCES URL fails`, `fetch v2: a redirect to a different base key fails`) | M3b (2 kills) | inherited (live leg) | **Yes** — keep, do not re-assert. |
| sha256 pin equality | 2 (`a snapshot whose sha256 differs is not backed`, `a snapshot sha mismatch is reported as such`) | M4 (2 kills) | **A4(i)** | **Yes** — A4(i) *is* v2's sha pin; these 2 must be kept, not duplicated. |
| snapshot quote occurrence | 2 (`quote absent from the page`, `a snapshot without the quote is reported as such`) | M5b (2 kills) | **A4(ii)** | **Yes** — A4(ii) *is* v2's snapshot quote check, with "verbatim" read at the counter's documented normalisation (html-unescape, backtick/`*`/`_` drop, curly-quote fold, whitespace collapse). Keep; do not duplicate. |
| Gate-section quote requirement | 7 (`quote absent from the Gate`, `an empty Gate records no quote`, `a quote missing from the Gate is not backed`, `the Gate failure is reported as such`, `the broken world exits 1`, `the broken world prints the three-of-four line`, `the broken world names the Gate on the reject line`) | M5 (7 kills) | **inherited from r59, unnamed by A1–A4** | **No** — this is the silent-loss risk MutV2Regress names. **Keep or declare its removal before the measurement; never delete silently.** It is E-9 in my equivalence set. |
| token grammar, foreign marker, host pins, tracker/change-note URL rejection, quote word bounds, `Rule files` exact match, base-row/`mined`/status | the remaining 256 assertions | not probed by MutV2Regress (not assigned) | unchanged inherited rules | **No** — v3 changes none of them; they stay as they are. |

**Net count.** 318 carried + 14 new (4 arm-killers + 9 equivalence + 1 computed-predicate) =
**332** expected assertions, of which **318 are v2's unchanged baseline**.

**The double-counting rule for the L1:** A1–A4 *add* a conjunct to v2's existing ones, they do
not replace them. Concretely — A1 = v2's form conjunct **+** canonical-set membership; A2 =
v2's word-threshold conjunct **+** clause-level support/polarity/exclusivity; A3 = E1's
five sub-rules with the URL criterion moved to url_key identity **+** the fresh-row alias
clause; A4 = v2's sha pin **+** verbatim quote **+** first-commit bound **+** base-sha alias.
Every v2 assertion in the table above is therefore **already** the arm's floor — the new
assertions must target only what the table says is *new*.

---

## 5. The predicate line must be computed — and it must not be v2's line

The frozen C1 predicate (plan §C1) is:

```
python3 -B verifiers/check_scoped_rules.py --self-test   prints
worlds reject 7 of 7; eligible rows pass 4 of 4                                       and exits 0
```

v2's self-test prints `self-test: 0 failure(s) over 318 assertions` and **nothing else**.
So v3's self-test must print **both** lines, and the worlds line must be **derived**:

```python
worlds = [W1, W2, W3, W4, W5, W6, W7]          # scored, never assumed
rejected = sum(1 for w in worlds if not w.passes)
eligible = [S103, S105, S106, S108]            # the REAL r60 rows (S6)
passed   = sum(1 for r in eligible if r.backed)
print("worlds reject %d of %d; eligible rows pass %d of %d"
      % (rejected, len(worlds), passed, len(eligible)))
return 1 if (rejected != len(worlds) or passed != len(eligible)) else 0
```

**T9 (MutFixtures) — the sentence must change when a world changes.** The L1 should add one
assertion that scores a deliberately repaired world and requires the printed sentence to
change and the exit to become 1. A hard-coded `print("worlds reject 7 of 7; …"); return 0`
passes every other check in the inventory and is the cheapest hollow self-test; this
assertion is the only thing that catches it.

**The `eligible rows pass 4 of 4` half is a *committed-bytes* measurement, not a synthetic
one.** The four must be the real r60 rows S103/S105/S106/S108 with their committed
snapshots (`82d60341…`, `a45c9e9f…`, `00e45ea5…`, `884c67ca…` — measured in §3.1 and in
`ScoutFixtureBytes.md`), **not** v2's synthetic S900–S903 world (S6). The four eligible rows
pass under the reference model on the committed bytes (§3.1).

**A1's key set makes the base clause work.** At the base revision the S112–S115 rows do not
exist, the key set is **empty**, no row can satisfy A1, `found = 0 < TARGET`, exit 1 — the
E2d mechanism, measured in §3.1 (`without S112-S115 (base) {}`).

---

## 6. The four arm predicates, as implemented in the reference model

This is the text the L1 can drop into v3 (it reuses the committed v2 helpers verbatim). It is
**scratch**, written by me for validation; the L1 owns the landed form.

### 6.1 A1 — canonical scope-key set

```python
# The id -> client map is PINNED in the counter.  The rows are located by id, so
# an untrusted row cannot re-declare which client it speaks for (MutA1's
# poisoning concern).  The KEY comes from the row's own text.
KEY_ROW_IDS = {"S112": "Claude Code", "S113": "VS Code",
               "S114": "Copilot CLI", "S115": "Cursor"}
BARE_IDENT = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")


def canonical_key_set(sources_text: str) -> dict:
    """Per-client canonical key set derived from the S112-S115 row texts.

    FAIL-CLOSED: no row, no row text, or a teaches cell with zero or many
    bare-identifier spans yields an EMPTY set for that client, so every row
    for that client is rejected.  (A client absent from S112-S115 is empty by
    construction -- that is the base-revision discriminator.)
    """
    out = {c: frozenset() for c in KEY_ROW_IDS.values()}
    rows = v2.sources_table(sources_text)
    for sid, client in KEY_ROW_IDS.items():
        row = rows.get(sid)
        if not row or len(row) < 7:
            continue
        spans = [t for t in v2.BACKTICK_RE.findall(row[6]) if BARE_IDENT.match(t)]
        if len(spans) == 1:
            out[client] = frozenset(spans)
    return out


def a1_why(client: str, key, canon: dict) -> list:
    if not key:
        return []
    allowed = canon.get(client, frozenset())
    if key not in allowed:
        return ["A1 scope key %r is not in the canonical key set for %s"
                % (key, client)]
    return []
```

**Measured on the four committed scribe drafts** (`ScribeS112–S115.md` row texts): the
`teaches` cell of each row carries exactly one bare-identifier backticked span —
`paths` (S112), `applyTo` (S113), `applyTo` (S114), `globs` (S115) — so the reader yields
exactly the frozen per-client set, and the fail-closed rule never fires on the drafted rows.

**The L1 must confirm the landed row texts still satisfy the reader** before freezing: if the
L1 rewords a `teaches` cell to contain two bare identifiers, that client's set goes empty and
its eligible row stops backing. That is a *safe* failure (fail-closed) but it would silently
cost the `4 of 4`. A dedicated assertion is warranted: assert
`canonical_key_set(measured_sources) == {"Claude Code": {"paths"}, "VS Code": {"applyTo"},
"Copilot CLI": {"applyTo"}, "Cursor": {"globs"}}` at the data revision.

### 6.2 A2 — clause-level support, polarity and exclusivity

```python
LOAD_VERBS = r"(?:load|loads|loaded|loading|attach|attaches|attached|" \
             r"include|includes|included|apply|applies|applied|read|reads|" \
             r"activate|activates|activated|trigger|triggers|triggered)"
NEGATION  = re.compile(r"(?i)\b(?:no|not|never|none|neither|nor|cannot|can't|"
                       r"does\s+not|do\s+not|doesn't|don't|without)\b")
EXCLUSIVE = re.compile(r"(?i)\b(?:only|just|exclusively|solely|merely)\b")
UNIVERSAL = re.compile(r"(?i)\b(?:unconditionally|always|every|all\s+files|"
                       r"all\s+applicable|regardless|any\s+file)\b")
CLAIM_RE  = re.compile(r"(?i)\b" + LOAD_VERBS + r"\b")


def _sentences(line: str) -> list:
    return [p for p in re.split(r"(?<=[.;])\s+", line.strip()) if p.strip()]


def a2_why(cell: str, page_text: str, line_no: int | None) -> list:
    """A2: every load/event claim in the Action cell must be SUPPORTED by the
    cited committed line -- not vocabulary matching alone.

    1. CLAUSE-LEVEL SUPPORT: each clause carrying a load/event verb must be
       supported by ONE sentence of the cited line (at least half the clause's
       content words, the counter's own tokenizer, v2's threshold shape).
    2. POLARITY: a negated clause must be supported by a sentence that is ALSO
       negated; a negated claim over an affirmative sentence contradicts it.
    3. EXCLUSIVITY vs UNIVERSAL: a clause claiming the rule fires ONLY for some
       files contradicts a cited line that says it applies to ALL files.  This
       comparison is against the WHOLE cited line, because a contradicting
       universal statement anywhere on that line defeats the claim made about
       it.
    A cell with no load/event claim is outside A2 by construction.
    """
```

**Measured against the committed pages** — the discrimination this buys:

```
REAL Claude S103:194             pass
REAL VS Code S105:329             pass
REAL Copilot S106:60              pass
REAL Cursor S108:131              pass
W6 invented S103:209              REJ: … contradicts the cited line 209 (the line states a universal scope)
CriticHollowC1 S103:209          REJ: … contradicts the cited line 209
MutFixtureEscape W8 S108:305     pass
```

**Read the last line as a limit, not a pass.** `MutFixtureEscape` showed a *subject
substitution* cell (a verbatim substring of `S108:305` asserting "Rules without a glob
pattern apply to every conversation") survives **every** text-local reading of A2 — word
threshold, all-words, verb-cooccurrence, strict-substring. My A2 rejects it too. No
text-local A2 can catch it; only a claim-entailment test could, and the plan's A2 sentence
is a *support* sentence, not an entailment sentence. **The L1 must record this as A2's
declared limit** (as the entry draft's "Not held" section already does), and the W8 cell must
be reported as a **survivor fixture**, not an eighth kill world — exactly as
`MutFixtureEscape` §4 item 4 requires. The frozen predicate counts **seven** worlds; adding
an eighth would break the printed sentence.

### 6.3 A3 — URL canonical (E2 + E2b)

```python
LOCALE_SEGMENTS = frozenset(("de", "ja", "fr", "es", "it", "pt", "ru", "zh",
                              "ko", "nl", "pl", "tr", "ar", "hi", "sv", "da",
                              "fi", "nb", "cs", "el", "he", "th", "vi", "id"))


def is_alias_rendering(url: str, others: list) -> bool:
    """Does `url` differ from some `others` URL only by a locale path segment
    or an @version/enterprise suffix, on the same host?"""
    # (b1) same segment count, exactly one differing segment, and exactly one
    #      side of that difference is a locale code;
    # (b2) the last segment carries an @version/enterprise suffix on one side
    #      only, and the suffix-stripped last segments are equal.


def a3_why(row_teaches: str, url: str, base_rows: dict, measured_rows: dict) -> list:
    """A3(a): a re-open row's URL must have the same url_key as its base row's
    URL (E2: url_key identity, NOT byte identity -- MutA3 proved byte
    identity unsatisfiable on the committed S108/S049 pair).

    A3(b): a FRESH row whose URL is an alias rendering of a same-host URL the
    lane already holds is rejected (E2b; the recorded W2 world is a fresh row,
    so A3(a) never evaluates it).
    """
```

**Two clauses, two killers** — the L1 must carry one fixture per clause (§2.3).

### 6.4 A4 — snapshot provenance (four conjuncts)

```python
SUPERSEDES_RE = re.compile(r"^supersedes\s+(S\d{3,})")


def a4_why(sid, sha, quote, opened, teaches, snapshot_bytes, base_sources,
           first_commit_date) -> list:
    """A4(i)   the recorded sha256 equals the committed snapshot bytes;
    A4(ii)  the located quote occurs verbatim in them (at the counter's
             documented normalisation);
    A4(iii) the earliest commit introducing those bytes is no older than the
             row's recorded open date -- CONSISTENCY ONLY, not acquisition
             authentication (the plan's declared limit; CriticA4Limit's
             forgery class: commit dates are author-settable);
    A4(iv)  the row's FULL 64-hex snapshot sha256 is not already recorded in
             the base-revision SOURCES table, unless the teaches cell declares
             byte-identity via `supersedes S###` (the S110 precedent).
    """
```

---

## 7. Reference model — the exact scratch source used for the measurements

Full text of `/fast/scratch/hyaku/kotoba-r61/kotoba-r61-wave-ExecSelftestArms/probe/arms.py`
(416 lines) and `killers.py`, `matrix.py`, `real.py` in the same directory. The parts the
L1 needs verbatim are §6.1–§6.4 above; the world builder that produced the measured output
is:

```python
KEY_ROWS = [   # the S112-S115 rows the reader consumes; each contributes ONE
               # bare-identifier backticked span in its `teaches` cell
    "| S112 | Claude Code Docs - canonical scope key - https://code.claude.com/docs/en/claude-directory.md | docs | A | s | a | The frontmatter field map lists `paths` for `rules/*.md`, the Claude Code rule-file scope key | mined | 2026-10-23 | 90d | y |",
    "| S113 | VS Code docs source - canonical scope key - https://raw.githubusercontent.com/microsoft/vscode-docs/x/docs/agent-customization/custom-instructions.md | docs | A | s | a | VS Code's own docs source lists `.github/instructions/**/*.instructions.md` as a targeted instructions path and shows `applyTo` as the matching-file glob key | mined | 2026-10-23 | 90d | y |",
    "| S114 | GitHub Docs - canonical scope key - https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | docs | A | s | a | re-opens S048 - canonical scope-key set: Copilot CLI documents `.github/instructions/**/*.instructions.md` as modular repository instructions and `applyTo` as the frontmatter key | mined | 2026-10-23 | 90d | y |",
    "| S115 | Cursor Docs - canonical scope key - https://cursor.com/docs/rules | docs | A | s | a | re-opens S108 - Cursor project rule files live under `.cursor/rules` as `.mdc` files, and `globs` scopes rules to specific files or directories | mined | 2026-10-23 | 90d | y |",
]
```

**A caveat the L1 must weigh:** the reader in §6.1 extracts the key from the *first* bare
identifier backticked in `teaches`. The committed scribe drafts satisfy that, but the landed
rows are the L1's to write. **The landed `teaches` cells must keep exactly one
bare-identifier backticked span each**, or the fail-closed reader empties that client's set.
This is a real coupling between the row wording and the counter, and the L1 should fix it
deliberately (either by pinning the reader's extraction to a labelled marker, or by
constraining the row wording) rather than by accident.

---

## 8. Anti-generator-keying rules for the arm-killers (MutFixtures' admission battery)

Each rule is stated so the L1 can check the landed self-test against it.

| # | rule | applies to |
|---|---|---|
| **T1** | score every world alone, in reverse, and in a seeded shuffle; the `world -> verdict` matrix must be identical | all |
| **T2** | rename every S-ID, every fixture directory and every commit message, reverse the row order inside every table; the matrix must be identical | all |
| **T3** | `grep -n` the counter's **production** path (`entry_row_verdict`, `judge`, `fetch`, `reopen_why`, the arm predicates) for every distinctive fixture token (ids, sha prefixes, `sessions`, the invented-cell phrases, the alias URL fragments); any occurrence in a branch/condition is a red flag | all |
| **T4** | reword every reject message; `--self-test` must still pass. **The only literal that must stay exact is the frozen predicate sentence.** This is why the arm-killers assert **rejection behaviour**, not the reason string. | all |
| **T5** | delete or invert exactly one arm; exactly that arm's killer must flip, and the self-test must fail naming it; every other killer must keep its verdict | all four |
| **T6** | commit the expected `world -> cause` table **before** v3 exists, derived from the plan and the r60 receipts; no fixture manifest may carry an `expected`/`verdict`/`pass`/`fail`/`mutant` field the counter reads | worlds |
| **T7** | `grep -n '__file__\|read_text\|inspect\.\|getsource\|__doc__' $C` — `self_sha()` is the only allowed use; the verdict path must contain none | all |
| **T8** | `grep -n 'time\.\|datetime\|now()' $C` in the fixture/self-test builder — every date is a receipt literal | all (A4-iii especially) |
| **T9** | mutate one world's defect; the printed sentence must change and the exit must become 1 | predicate line |
| **T10** | **the four arm-killers must be scored through the same `judge`/`--rev` path as real rows**, with the expected value being the **verdict** (and the arm cause), not a source grep. The exact anti-tautology the assignment names — `Path(__file__).read_text()` inside a `check()` — dies here. | all four |

**The single-defect rule, restated as an admission test.** A killer whose row is rejected for
**two** reasons is not that arm's killer: deleting the arm leaves the other rejecting, so the
killer never flips. This is why W3 (`CtlReopenHeldKey a`) is **double-caused** under v3 —
A1 (`rules` ∉ `{globs}`) *and* the retained held-base rule — and is therefore a **world-level
reject but not an arm-killer for either arm** (MutFixtures S3). The four killers in §2 were
each checked for single-defectness against this rule, and the deletion matrix in §2.0 is the
evidence.

---

## 9. What I could not verify (honesty)

1. **No v3 counter exists.** Every "expected rejection line" in this report is a *design*
   expectation produced by a scratch reference model, not observed v3 output. The L1 must
   re-derive them against the landed source. The line texts are therefore offered as
   **templates with the offending value interpolated**, and per T4 the assertions should
   key on behaviour (rejected / not rejected) plus the arm attribution, not the prose.
2. **The arm predicates in §6 are my design**, not a frozen contract. The plan freezes the
   arm *sentences*; the mechanisation is the implementation rider's. Where the plan left
   latitude (how "supported by text" is computed, how an alias rendering is recognised, how
   the first-commit date is walked) I chose a determinate rule and measured it against the
   committed bytes. The L1 may substitute another mechanisation — **but then the four
   killers must be re-derived**, because a different A2 may or may not reject the published
   W6 cell.
3. **The world fixtures W1–W7 are not rebuilt here.** The seven worlds are the
   `ExecWorldFixtures` seat's deliverable; my §5 specifies only how the self-test must
   *score* them and how the sentence must be computed. I did not build the world trees, did
   not run the seven worlds, and did not verify any world's v3 verdict.
4. **A4-iii is unvalidated end-to-end.** I specified the two-commit fixture and the expected
   comparison, but I did not construct the back-dated repo and measure a rejection. The
   commit-date walk (`git log --diff-filter=A` over the measured revision's ancestry) is
   specified, not measured.
5. **The A2 killer's rejection depends on my exclusivity rule.** If the L1 implements A2
   without the exclusivity-vs-universality clause, the published W6 cell is **not** rejected
   and W6 does not reject — I measured this directly (`W6 invented S103:209 → pass` under the
   support+polarity-only variant). This is a hard coupling: **W6's rejection requires an A2
   that can see a scope contradiction.**
6. **A3's alias clause (b) is a string-surgery rule over committed row URLs** (E2b's own
   wording). I measured it against the two recorded W0b alias URLs and the S108/S049 pair. I
   did not measure it against a held-out alias; the L1 should, because a two-literal
   deny-list (`/de/`, `enterprise-cloud@latest`) would pass my fixtures and fail a third.
7. **I did not measure the S112–S115 rows as landed.** The four key-set rows exist only as
   scribe drafts in wave reports; the reader was measured against those draft texts. If the
   L1 lands different `teaches` wording, the reader's output must be re-measured (F4, §7).

---

## 10. Hand-off checklist for the L1

- [ ] Re-base v2's synthetic self-test world onto the four canonical clients; re-point the 22
      Gemini-named assertions; keep all 318 (F1, §1.3).
- [ ] Land A1's reader (id→client pinned, key from the row text, fail-closed) and assert the
      landed key set equals the frozen per-client map at the data revision (F2, §6.1).
- [ ] Land A2 with clause-level support **+ polarity + exclusivity**; without the exclusivity
      clause the published W6 cell is not rejected (limitation 5, §6.2).
- [ ] Land A3 as two clauses — url_key identity on re-opens (E2) and fresh-row alias
      rendering (E2b) — with **one killer per clause** (§2.3).
- [ ] Land A4 as four conjuncts with **four single-defect killers**; A4-iii needs a
      two-commit temp repo with fixed dates, never the host clock (§2.4).
- [ ] Carry the nine equivalence fixtures, including E-7/E-8 (the E2 limits) and E-9 (the
      inherited Gate-quote rule, keep or declare removal) (§3, §4).
- [ ] Compute the predicate sentence; add the T9 assertion that a repaired world changes the
      sentence and the exit code (§5).
- [ ] Record A2's declared limit (the subject-substitution cell survives) and report W8 as a
      survivor fixture, not an eighth kill world (§6.2).
- [ ] Run the admission battery T1–T10 against the landed self-test (§8).

---

**Installs:** no installs. Nothing was missing; no tool, version or channel was changed; the
host-wide pacman pause was not touched.

**Blockers:** none. The two items that could become blockers are decisions, not
obstructions: (a) the L1 must confirm the landed S112–S115 `teaches` wording keeps exactly
one bare-identifier backticked span per row, or A1's fail-closed reader empties that
client's set (F4, §7); (b) if the L1 implements A2 without the exclusivity clause, the W6
killer does not reject and the A2 killer must be re-derived (limitation 5, §6.2). Neither
requires action from this seat.

**Produced:** the v3 self-test arm inventory — four single-defect arm-killers (A1–A4) with
their fixture bytes and expected rejection lines, nine equivalence fixtures, the v2→v3
subsumption map for all 318 baseline assertions, the computed-predicate-line requirement, and
the anti-generator-keying admission battery; validated by a deletion matrix on a scratch
reference model built over the committed v2 helpers.

**Report:** `.ufo/waves/round-61/wave/ExecSelftestArms.md`
