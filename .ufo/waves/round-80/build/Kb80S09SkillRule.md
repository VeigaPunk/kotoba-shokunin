# Kb80S09SkillRule — `allowed-tools` rule line, gate-registry row, placement

Round 80 (attempt 1), wave w1, seat `Kb80S09SkillRule`, 2026-10-27. Base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Drafts only: nothing here is applied to the lane tree. The L1 integrates and is the only committer. Deliverables are
the two paste blocks below, their placement, and the evidence that each passes the predicates that read it.

Companion files: `Kb80S09SkillRule.patch` (fallback application of both blocks, sha256 `9ad16e05cf43460c…`),
`Kb80S09SkillRule-receipts.txt` (commands, exits, selected output). Seat report: `.ufo/waves/round-80/w1/Kb80S09SkillRule.md`.

---

## 1. The rule line (one physical line, 920 characters, no `|`)

**sha256 of the line as measured in the fixture:** `6468c797e521cf77de2c539bd7c1affc6830ea235c078df4ebe87cf88bc2a60d`

**Insertion point:** `SKILL.md` § `## Frontmatter craft — the trigger surface` (base line 158), after the
`Portability floor (spec + vendor + YAML, …)` paragraph that ends on base line 162, before
`### Description thresholds by client` (base line 164). Insert one blank line, then the rule line: **+2 lines**
(the blank line counts — `verify_skill_checklist.py` `trigger.line_budget` counts every line of the file).

```
Treat `allowed-tools` as pre-approval, never as a sandbox (entry `corpus/knowledge/allowed-tools-surfaces-round80.md`, S226–S231): the open specification calls it an experimental space-separated string of pre-approved tools whose support varies between agent implementations (S226); Claude Code applies it as a per-turn permission grant taking a space- or comma-separated string or a YAML list and still leaves every tool callable (S227); Factory stores it as review and UI metadata that does not add tools or sandbox standard skill invocation (S228); Microsoft Agent Framework and pi each call it experimental (S229, S230); Mistral Vibe's own example writes a YAML list it explains no further (S231) — so write the specification's space-separated string, put the restriction in `disallowed-tools` or the client's own settings, and never rely on this field to restrict: a skill that does is wrong on at least one client.
```

Why one physical line: conjunct (g) of `verifiers/check_allowed_tools.py` is a line predicate —
`skill_rule_ok()` scans every rendered line for the entry path plus three or more surface names. Keeping the entry
path and all six surface names on the same physical line makes the conjunct findable by any line-level reading,
and costs 2 lines of the 600-line module bound instead of a 9-line per-client table.

### Clause → page bytes

Every clause is a sentence or a literal phrase of one of the six committed snapshots
`.ufo/waves/round-79/snapshots/S226…S231` (round-79 dir, per `plans/round-80.md` § C2). I read those committed
bytes; I did **not** re-fetch the pages (the live re-open is `Kb80ReopenSix`'s seat), so no clause here claims
anything about a page as of today.

| clause in the rule line | page sentence (literal) | snapshot:line |
|---|---|---|
| "experimental space-separated string of pre-approved tools" | "Space-separated string of pre-approved tools the skill may use. (Experimental)" | `S226-spec.md:35` |
| "whose support varies between agent implementations" | "Experimental. Support for this field may vary between agent implementations" | `S226-spec.md:177` |
| "per-turn permission grant taking a space- or comma-separated string or a YAML list" | "Tools Claude can use without asking permission during the turn that invokes this skill. The grant clears when you send your next message. Accepts a space- or comma-separated string, or a YAML list." | `S227-claude.md:404` |
| "still leaves every tool callable" | "It does not restrict which tools are available: every tool remains callable" | `S227-claude.md:617` |
| "review and UI metadata that does not add tools or sandbox standard skill invocation" | "It is metadata for review, packaging, and UI display; it does not add tools or sandbox standard skill invocation." | `S228-factory.md:254` |
| "Microsoft Agent Framework … call it experimental" | "Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations." | `S229-msaf.html:820` |
| "pi … call it experimental" | "Experimental pre-approved tool list" | `S230-pi.md:78` |
| "Mistral Vibe's own example writes a YAML list it explains no further" | `allowed-tools:` then `- read` / `- grep` / `- ask_user_question`; the page states no semantics for the key | `S231-vibe.md:725-728` |
| "put the restriction in `disallowed-tools` or the client's own settings" | "Tools removed from Claude's available pool while this skill is active." | `S227-claude.md:405`, `:632` |
| "wrong on at least one client" | the two negatives above: Claude Code's "does not restrict which tools are available" (`:617`) and Factory's "standard skill invocation is not a runtime sandbox" (`:282`) | `S227-claude.md:617`, `S228-factory.md:282` |

Line precision on `S229-msaf.html`: raw line 818 holds the `<code>allowed-tools</code>` field-name cell and raw
line 820 the description cell quoted here — same `<tr>` row, different lines. This citation is to the sentence's own
line, and the claim does not depend on any admissible-quote reading of the page: it is `SKILL.md` prose, not an entry
quote, so the counter's Q70 heading rule never reads it.

Snapshot bytes those lines sit in (sha256, read 2026-10-27): `S226-spec.md`
`9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`, `S227-claude.md`
`31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9`, `S228-factory.md`
`81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9`, `S229-msaf.html`
`34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2`, `S230-pi.md`
`5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5`, `S231-vibe.md`
`fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0`.

### What the line deliberately does not claim

- Not that any client enforces or parses the field as a restriction — two of the six pages say the opposite, and no
  page was run.
- Not that the space-separated form is accepted everywhere — only the specification states a form and Claude Code
  states tolerance; the specification's `allowed-tools` row is itself marked "(Experimental)" (`S226-spec.md:35`).
- Not that `disallowed-tools` exists outside Claude Code — the line attributes it to "the client's own settings".

---

## 2. The gate-registry row (one line, 1373 characters, 8 cells)

**sha256 of the row as measured in the fixture:** `4bf7b71bd765a8b23a0ef1da7801ba813132b09f1b519bf999917b7c19de1a1a`

**Insertion point:** last row of `SKILL.md` § `## Gate registry`, immediately after the
`verifiers/check_sibling_reread.py` row (base line 512) and before the blank line that closes the table.
No blank line between rows — a blank line ends the table for `check_gate_registry.py`'s `registry_rows()`.

```
| `verifiers/check_allowed_tools.py` | gate | `python3 -B verifiers/check_allowed_tools.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-80 C2 counter (depth, sourced; the form backbone is measured, the grant-semantics matrix is exploratory): committed bytes only; each of the six `allowed-tools` surfaces (Open specification, Claude Code, Factory, Microsoft Agent Framework, pi, Mistral Vibe) is documented when the entry `corpus/knowledge/allowed-tools-surfaces-round80.md` carries its row in the frozen five-cell table with ≥3 backticked tokens located in its sha256-pinned snapshot, a 5-to-25-word located quote after a heading and carrying `allowed-tools`, an 11-cell `S###` row at the surface's frozen host and path prefix, the frozen grant label plus its page token, and `opened` equal to the entry's `verified-at:`; the tree conjuncts are one `SKILL.md` rule line naming ≥3 surfaces plus this row and exactly one `PROVINCE.md` `## Core` bullet naming the entry; prints `allowed-tools surfaces documented N of 6` with the mechanical scrape's own score beside it (`generator world: M of 6`, Q71/Q74) and exits 0 only at N == 6 | `--self-test` | in-file SELF_SHA; `.ufo/waves/round-79/snapshots/MANIFEST.sha256` | none (reads committed bytes via `git show <rev>:<path>`; `--self-test` writes isolated fixture repos under `$TMPDIR`, removed) | kotoba |
```

Cell map (the eight the header demands): Name / Kind `gate` / Entry command with the script path / Verdict map
`0=clean`, `1=failed`, `2=could-not-evaluate` (each code once — `check_gate_registry.py` `PAIR_RE`, and a `gate`
must carry `0=clean` and `1=failed`) / Self-test `` `--self-test` `` (an exact `add_argument("--self-test")` exists
in the r79 draft at `check_allowed_tools.py:2229`) / Pinned values (`in-file SELF_SHA` plus the one manifest path the
counter reads) / Write scope / Owner `kotoba`.

### Measured conformance (fixture clone, base + these three lines + the counter copy)

```
$ cd "$S/clone" && python3 -B verifiers/check_gate_registry.py --rev HEAD          # 593-line SKILL.md
gate registry rows conformant 61 of 63 lane verifiers; phantom 0                  exit=1
$ cd "$S/clone" && python3 -B verifiers/check_gate_registry.py --rev HEAD~1        # pristine base
gate registry rows conformant 60 of 62 lane verifiers; phantom 0                  exit=1
```

Both runs name the same two failures — `verifiers/check_desc_craft.py` and
`verifiers/check_r75_routed_repairs.py`, each "registry rows naming it: 0 (need 1)" — which are exactly the two rows
`Kb79E01Registry.patch` adds. The new row is `"conformant": true`, `"why": []` in the `--json` report. The delta is
`+1` conformant row, `+1` lane verifier, `phantom` still 0.

Conjunct (g) of the counter itself, measured by importing the r79 draft counter (the round-80 counter's base) and
rebinding its `ENTRY` constant in memory to the round-80 entry path — no file edit, no repo write:

```
surfaces named on the rule line: 6
skill_rule_ok(live SKILL.md)      : True
registry_home_ok(live SKILL.md)   : True
cells in the row                  : 8
CONTROL rule without entry path   : False (want False)
CONTROL rule with 2 surfaces      : False (2 named, want False)
CONTROL row with 7 cells          : False (want False)
CONTROL row with kind probe       : False (want False)
CONTROL empty text                : False False (want False False)                 exit=0
```

### DIFF against E01's third row — one row only

- `Kb79E01Registry.patch` carries **two** rows (`check_desc_craft.py`, `check_r75_routed_repairs.py`) and **no**
  `check_allowed_tools.py` row — measured from the patch bytes, not from the plan's summary.
- `Kb80E01Registry` had published nothing when this draft was written (`.ufo/waves/round-80/build/` listing and the
  seat's `agent://` status, both captured in the receipts), so **I derived the row myself**; the r79 draft counter
  and the plan's § C2 freeze are its source.
- **Integration rule:** the lane tree must hold exactly one row for `verifiers/check_allowed_tools.py`. If E01's
  patch carries one when it lands, **keep E01's row and discard mine** — its cells were reviewed together with the
  two withdrawn rows, and a second row makes `judge()` report `registry rows naming it: 2 (need 1)` for the file.
  Two rows is a red gate, not a merge conflict to split.
- If both patches are applied, the two hunks both anchor on `check_sibling_reread.py` + blank + `## Sources`;
  apply with `git apply --3way` or place rows by hand, then assert `grep -c '^| `verifiers/check_allowed_tools.py`'
  SKILL.md` prints `1`.

---

## 3. Placement rationale — `## Frontmatter craft — the trigger surface`

The field is frontmatter, and `## Frontmatter craft` is the only section that holds field-level rules and the
per-field per-client tables (`### Description thresholds by client`, `### Explicit invocation by client`). The line
sits directly under the closest precedent in register: the `Portability floor` paragraph, a prose rule that names
its authorities inline, states the authoring consequence, and hands depth to an entry. `allowed-tools` is the same
shape of fact — a field whose meaning differs per client, with one entry holding the page bytes.

Sections considered and rejected:

| section | why not |
|---|---|
| `## Instruction surfaces — pick the file before the fix` | answers *which file* to write a body into; its rows are routing decisions (`.agents/skills/` vs a vendor root), not field semantics |
| `## Compression rules` (`### Body craft`) | the round-74 table's register is the *style* this line borrows (rule → authorities → action), but its subject is how to write a body, not what a frontmatter field grants; the entry itself is not a skill-creation guide page |
| `## Anti-patterns` | the 18-row anti-pattern table moved to `corpus/knowledge/fail-closed-and-anti-patterns.md` in round 15; the distilled table left here is a subset and does not carry per-client evidence |
| `## Trigger-fidelity checklist` | a pre-ship checklist of checkable items; this rule is a statement of what a field means, and its evidence is a knowledge entry, not a file read |

Placement also keeps the counter's two reading surfaces apart on purpose: the rule line in § Frontmatter craft,
the counter's row in § Gate registry — so a reader who changes one cannot silently satisfy the other.

---

## 4. Landing constraints (what must exist at the measured tip)

1. `corpus/knowledge/allowed-tools-surfaces-round80.md` — the entry. Both my pointers (`SKILL.md:164`, `:515`) fail
   `trigger.citation_resolves` while it is absent; that is the conjunct-(g) target, not a defect of the row.
2. `.ufo/waves/round-79/snapshots/MANIFEST.sha256` — the row's pinned path and the counter's `MANIFEST` constant.
   It does **not** exist at base `398cbe1` (the six `S22x` snapshot files do, added by the round-80 freeze commit
   `c2f69d4`), so the entry seats must commit it with the entry; without it this row reds
   `check_gate_registry.py` ("pinned path … does not exist") and C2 cannot pass at all.
3. `verifiers/check_allowed_tools.py` — the row's `exists()` leg and the `--self-test` handler it reads; the row must
   land in the same commit as the counter, or `check_gate_registry.py` counts a phantom row.
4. Line budget: base 590 lines + 2 (this rule line and its blank) + 1 (this row) + 2 (E01's two withdrawn rows) =
   **595**, within the box's 600 (`verify_skill_checklist.py` `trigger.line_budget`). Measured now at 593 with
   `PASS trigger.line_budget: evaluated 593 — 593 lines within budget 600 (from box at line 287)`.
5. `PROVINCE.md` § Core needs exactly one bullet naming the entry (the counter's `province_state`), which is
   `Kb80S10Province`'s deliverable, not mine; my two blocks add none.

---

## 5. Limits

- **No claim after-values scored.** I measured the gates this draft feeds (registry, line budget, citation
  resolution, the two adjacent section gates), never a C1/C2 after-value, and never `check_tip_battery.py`.
- **Snapshot bytes, not live pages.** Every page sentence above is a line of the committed round-79 snapshot named
  beside it; the live re-open belongs to `Kb80ReopenSix`. If a page moved, the snapshot still grounds this line and
  the entry will carry the fetch record.
- **The published round-80 counter is still the r79 draft — measured, not assumed.**
  `.ufo/waves/round-80/build/check_allowed_tools.py` and `.ufo/waves/round-79/build/check_allowed_tools.py` are
  byte-identical (sha256 `74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`): `ENTRY =
  corpus/knowledge/allowed-tools-surfaces-round79.md`, `TARGET = 5`, `TOTAL = 6`, `BASE_REV = b10bcbc6…`, headline
  `allowed-tools surfaces backed N of 6`, world line `script-only world: M of 6`. On my two blocks those bytes read
  `skill_rule_ok → False` (the predicate hunts the round-79 path) and `registry_home_ok → True`; with `ENTRY` rebound
  in memory to `…round80.md` the same bytes read `True` and see 6 surfaces and 8 cells. So my blocks pass conjunct (g)
  **only after** `Kb80E07C2Counter` publishes `ENTRY = …round80.md`, the `documented` / `generator world:` wording and
  an exit predicate at `N == 6`; until then this row's description cell describes the plan's freeze, not the bytes.
- **The counter copy in my fixture is the r79 draft.** `check_gate_registry.py` reads only the AST for `--self-test`
  and the row's cells, so the copy is sufficient for that conformance measurement; it is *not* evidence about the
  round-80 counter's own output.
- **`check_spec_craft.py` is red at base in this fixture for an environment reason** ("corpus/SOURCES.md is not
  census-conformant at HEAD" and at `HEAD~1`, `0 of 3`, exit 1 in both runs) — identical before and after my lines,
  so it isolates nothing of mine and is out of scope here.
- **One defect of my own, reported:** my first `git show … > /fast/scratch/skill-base.md` wrote outside my scratch
  dir (`/fast/scratch/skill-base.md`, 1 file). Removed in the next command (`ls` confirms absent). No tracked or
  fleet file was touched.
