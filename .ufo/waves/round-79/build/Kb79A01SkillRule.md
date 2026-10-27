# C2 author-facing draft set 1 — SKILL.md rule, gate-registry row, PROVINCE bullet, README row

Seat Kb79A01SkillRule, round 79 wave 1, 2026-10-27. Drafts only: the L1 integrates into the lane tree after the
wave (freeze discipline). Nothing in this file is scored on a counter — `verifiers/check_allowed_tools.py` is
built in this wave and frozen by the L1 afterwards.

Read for this draft: `SKILL.md` (sections: 60 Instruction surfaces, 153 Router model, 158 Frontmatter craft,
195 Compression rules, 218/309/355/389 the four checklists, 413 Anti-patterns, 436 Refusals, 445 Gate registry,
514 Sources), `plans/round-79.md` § C2, `corpus/knowledge/spec-skill-creation-craft-round74.md` (how a
per-page rule set is carried as a table with a `Basis:` line), `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`
(how four vendor pages were carried as one decision row + one PROVINCE bullet + one README row + one registry row).

Own fetches, 2026-10-27 (raw bytes, `curl -sSL -A 'Mozilla/5.0'`): receipt
`.ufo/waves/round-79/build/Kb79A01SkillRule-fetch-receipt.txt` — HTTP code, bytes, sha256 and occurrence count per
page, plus the located quotes and the negative sweeps. Six rows back at 200; the `learn.microsoft.com` `.md` route
is 404 and the plain path on the same host and path prefix is 200 (receipt § the one URL-form deviation).

---

## 1. `SKILL.md` rule line (one physical line; insert with one blank line above it)

**Placement:** `SKILL.md` § `## Frontmatter craft — the trigger surface` (line 158), immediately after the
`Portability floor (spec + vendor + YAML, …)` paragraph that ends on line 162 and before
`### Description thresholds by client` (line 164). Insert after line 162: one blank line, then the rule line.

**Why that section and not another:**

- The field is frontmatter. § Frontmatter craft is the only section that holds field-level rules and the two
  per-client field tables (`### Description thresholds by client`, `### Explicit invocation by client`), so a
  third per-client field statement belongs beside them rather than in a checklist.
- The line sits directly under the closest precedent in register: `Portability floor (spec + vendor + YAML,
  `corpus/SOURCES.md` S018, S002, S019, S008)` — a prose rule that names its authorities inline, states the
  authoring consequence and hands depth off to an entry. `allowed-tools` portability is the same shape of fact.
- `## Instruction surfaces — pick the file before the fix` answers *which file* to write, not *what a field
  means*; its round-73 row is a routing decision (`.agents/skills/` vs a vendor root), not field semantics.

**Paste block (the rule is one line; the blank line above it is the paragraph separator):**

```

`allowed-tools` restricts nothing by itself: the Open specification calls it an experimental space-separated string of pre-approved tools whose support varies between agent implementations (S226); Claude Code treats it as a per-turn permission grant taking a space- or comma-separated string or a YAML list, leaves every tool callable and ignores it under `allowManagedPermissionRulesOnly` (S227); Factory stores it as review, packaging and UI metadata that adds no tools and does not sandbox standard invocation (S228); Microsoft Agent Framework and pi each call it experimental (S229, S230); and Mistral Vibe's example writes it as a YAML list it explains no further (S231) — so write the spec's space-separated string form, never rely on the field for restriction (a deny rule, a tool policy or `disallowed-tools` is where restriction lives), and state what the skill needs in the body. Basis: `corpus/knowledge/allowed-tools-surfaces-round79.md` (S226–S231, documentary evidence, no client run).
```

**Why one physical line, not a wrapped paragraph or a table:** plan § C2 conjunct (g) reads "`SKILL.md` carries
one rule line citing the entry path and naming ≥3 surfaces". Keeping the entry path and all six surface names on
the same physical line means any line-level reading of that conjunct finds both. A per-client table would need
heading + blank + header + separator + six rows (9 lines) and would spend the line budget § 5 computes.

**Clause → source (each clause maps to bytes I fetched; line numbers are of my fetch, not the row seats' snapshots):**

| clause in the rule line | page sentence | my fetch line |
|---|---|---|
| "experimental space-separated string of pre-approved tools whose support varies between agent implementations" | "Space-separated string of pre-approved tools the skill may use. (Experimental)" and "Experimental. Support for this field may vary between agent implementations" | `specification.md:35`, `:175` |
| "per-turn permission grant … space- or comma-separated string or a YAML list" | "Tools Claude can use without asking permission during the turn that invokes this skill. The grant clears when you send your next message. Accepts a space- or comma-separated string, or a YAML list." | `skills.md:404` |
| "leaves every tool callable" | "It does not restrict which tools are available: every tool remains callable" | `skills.md:617` |
| "ignores it under `allowManagedPermissionRulesOnly`" | "When your organization sets `allowManagedPermissionRulesOnly` in managed settings, Claude Code ignores `allowed-tools` in project and personal skills" | `skills.md:643` |
| "`disallowed-tools` is where restriction lives" | "`disallowed-tools` … Tools removed from Claude's available pool while this skill is active." | `skills.md:632`, table `:405` |
| "review, packaging and UI metadata that adds no tools and does not sandbox standard invocation" | "Declares the tools the skill is designed to use. It is metadata for review, packaging, and UI display; it does not add tools or sandbox standard skill invocation." | factory page (tag-stripped), plus "standard skill invocation is not a runtime sandbox" |
| "each call it experimental" (msaf, pi) | "Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations." / "Experimental pre-approved tool list" | msaf page; `skills.md:78` (pi) |
| "Writes it as a YAML list it explains no further" | the `~/.vibe/skills/code-review/SKILL.md` example's `allowed-tools:` with `- read` `- grep` `- ask_user_question`; the page explains `user-invocable` and `disable-model-invocation` and says nothing about this field | `README.md:725-728` (vibe) |

Nothing in the rule line goes beyond those sentences. Two claims that would go beyond them and are therefore
**not** in the line: that any client enforces the field (Factory explicitly says it does not; Claude Code says it
grants rather than restricts), and that the space-separated form is accepted everywhere (only the spec and
Claude Code state a form; Vibe shows a list).

---

## 2. Gate-registry row for `verifiers/check_allowed_tools.py`

Form copied from the neighbouring rows (line 509 `check_cn_vendor_surfaces.py`, line 510
`check_report_pointers.py`): eight cells, `kind` = `gate`, entry command carrying the script path, a
`0=clean, 1=failed, 2=could-not-evaluate` verdict map (`check_gate_registry.py` `PAIR_RE` reads
`0=clean`/`1=failed`), a backticked `--self-test`, pinned values, write scope, owner `kotoba`. No cell contains a
`|` character.

**Paste block (append as the last row of the `## Gate registry` table, after the `check_sibling_reread.py` row):**

```
| `verifiers/check_allowed_tools.py` | gate | `python3 -B verifiers/check_allowed_tools.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-79 C2 counter (depth, sourced): committed bytes only; the entry `corpus/knowledge/allowed-tools-surfaces-round79.md` must back the six `allowed-tools` surfaces (open specification, Claude Code, Factory, Microsoft Agent Framework, pi, Mistral Vibe) with one row per surface in a frozen-header table, at least three backticked tokens per row located ASCII-word-bounded in its sha256-pinned snapshot, a 5-to-25-word located quote carrying `allowed-tools`, an 11-cell `S###` registry row whose host and path prefix equal the surface's frozen host, one frozen grant label per surface, and `opened` equal to the entry's `verified-at:`, all opened this round; `SKILL.md` carries the rule line citing the entry, `PROVINCE.md` § Core names the entry, and this registry row exists; `allowed-tools surfaces backed N of 6`, exit 0 at N >= 5 | `--self-test` | in-file SELF_SHA; `.ufo/waves/round-79/snapshots/MANIFEST.sha256` | none (reads `git show <rev>:<path>`; a `--self-test` writes isolated fixture repos under `$TMPDIR`, removed) | kotoba |
```

**Landing constraint (measured in `check_gate_registry.py`, not assumed):** `judge()` requires exactly one row
per lane verifier and computes `phantom` rows — a row whose Name cell is a `verifiers/…` path absent from the
file set fails. So this row must ship in the same commit as `verifiers/check_allowed_tools.py`, and the
backticked pinned-values path `.ufo/waves/round-79/snapshots/MANIFEST.sha256` must exist at the measured
revision (`judge_row` → `exists(p)`). Round 73 landed the same pair (`check_cn_vendor_surfaces.py` row +
`round-73/snapshots/MANIFEST.sha256`).

---

## 3. `PROVINCE.md` `## Core` bullet

**Placement:** append after the current last Core bullet, `- Sibling census re-pin (round 74, freshness): …`
(`PROVINCE.md:33`), i.e. immediately before `## Frontier` (line 34). One line, no blank line inserted inside the
list.

**Paste block:**

```
- Allowed-tools semantics by client (round 79): what six pages document about a skill's `allowed-tools` frontmatter field — experimental with support that varies between implementations (Open specification, Microsoft Agent Framework, pi), a per-turn permission grant that leaves every tool callable and is ignored under managed-only permission rules (Claude Code), review, packaging and UI metadata that adds no tools and does not sandbox standard invocation (Factory), and a YAML list with no stated semantics (Mistral Vibe) (S226–S231; documentary evidence, no client run). Acted on in `SKILL.md` § Frontmatter craft and counted by `verifiers/check_allowed_tools.py --rev <rev>`.
```

Two sentences: the documentary finding, then the action and the counter. "Documentary evidence, no client run" is
the round-73 bullet's wording and stays true here — no client was installed, loaded, routed or refused.

---

## 4. `corpus/README.md` coverage-map row

**Placement:** the coverage map's third-column table (`| Area | File | Basis |`, header line 5); append after the
last round-74 row `| Sibling census re-pin (round 74) | …` (line 146).

**Paste block:**

```
| Allowed-tools surfaces (round 79) | `knowledge/allowed-tools-surfaces-round79.md` | what six pages say a skill's `allowed-tools` frontmatter field means and what it does not (S226-S231; documentary evidence, no client run): the Open specification, Microsoft Agent Framework and pi call it experimental with support that varies between implementations, Claude Code a per-turn permission grant that leaves every tool callable and is ignored under managed-only permission rules, Factory review/packaging/UI metadata that adds no tools and does not sandbox standard invocation, Mistral Vibe a YAML list with no semantics stated; acted on in `../SKILL.md` § Frontmatter craft; counted by `../verifiers/check_allowed_tools.py --rev <rev>` (`allowed-tools surfaces backed N of 6`, exit 0 at N >= 5, `0 of 6` at base `b10bcbc`); the six page snapshots are pinned in `../.ufo/waves/round-79/snapshots/MANIFEST.sha256` |
```

The row cites the entry path the other rows use (`knowledge/…`, not `corpus/knowledge/…`) and the counter by its
`../verifiers/…` lane-relative path, matching rows 142 and 145.

---

## 5. `SKILL.md` line budget — arithmetic and what would have to give

Measured on committed bytes. The lane `HEAD` moved while I worked (`daa3a09` → `d9d01c2` → `60ba11f`, the
L1's pre-data freeze commits); `git show HEAD:SKILL.md | wc -l` printed 590 at each of them, seat S07 reports
590 at base `b10bcbc` (`.ufo/waves/round-79/w1/Kb79S07BudgetCensus.md`), and `SKILL.md`, `PROVINCE.md` and
`corpus/README.md` were clean in the working tree (`git status --porcelain` → 0 lines):

```
$ git show HEAD:SKILL.md | wc -l
590
$ git show HEAD:SKILL.md | grep -c 'allowed-tools'
0
$ git show HEAD:SKILL.md | sed -n '/^## Gate registry/,/^## Sources/p' | grep -cE '^\| `verifiers/'
60
```

Budget: **590 + 2 (C1's two registry rows) + 1 (this registry row) + 2 (blank line + rule line) = 595**, inside
the 600-line bound with **5 lines of headroom**. The bound is real: `verify_skill_checklist.py`
`check_line_budget` uses `n = len(lines)` over the whole file with `--max-lines` default 600, so blank lines
count, and § 1's insertion costs 2 lines, not 1.

If the round needs those 5 lines back, these are the existing lines I would shorten — **named only, not edited**
(nobody shortens them in this draft):

- `SKILL.md:508` and `:511-512` — the `check_tip_battery.py`, `check_agentdef_boxes.py`, `check_infoless_fences.py`
  and `check_sweep_mutants.py` registry rows. Their verdict-map cells restate the guard list and the withdrawn-claim
  history that `verifiers/README.md` already holds, and the section's own preamble points at that file
  ("what each one checks: `verifiers/README.md`"), so a shorter cell loses no pointer.
- `SKILL.md:509` — the `check_cn_vendor_surfaces.py` row repeats the four vendor names that `PROVINCE.md` § Core and
  the README row already carry; trimming the enumeration keeps the entry path and the counter name.
- `SKILL.md:193` — the "Testing a skill — the Agent Skills guides' artefacts" bullet (782 characters) repeats the
  row-count and comparator detail that `corpus/knowledge/skill-eval-artefacts-round70.md` holds behind its pointer.

I am not proposing to shorten the `Portability floor` paragraph (line 162): every token there is a rule or a row id.

---

## 6. Which lane gates read the `SKILL.md` sections I touch, and which count the lines I add

`grep -n 'SKILL.md' verifiers/*.py | wc -l` prints 433 across the checklists, the per-client counters and the corpus
gates. Restricting to what my two SKILL.md changes touch (a paragraph in § Frontmatter craft; one row in
§ Gate registry):

| gate | reads | does it count my lines? |
|---|---|---|
| `verifiers/verify_skill_checklist.py` | the whole file (`trigger.line_budget`, `trigger.citation_resolves`, `trigger.no_placeholder`) | **Yes** — `check_line_budget` counts every line of the file against `--max-lines` (default 600). My +2 and the registry rows move 590 → 595. |
| `verifiers/check_gate_registry.py` | `## Gate registry` (`HEADING = "## Gate registry"`), header tuple, one row per lane verifier, phantom rows | **Counts the row, not lines**: the row must exist exactly once and must not name a missing script; the pinned-values backticked path must exist at the measured rev. |
| `verifiers/check_cn_vendor_surfaces.py` | its own `## Instruction surfaces` section / decision row, its own registry row (`registry_home_ok`), `PROVINCE.md` bullets | No — it counts rows and tokens in the sections it names; a paragraph in § Frontmatter craft and a new registry row are outside its predicates. |
| `verifiers/check_spec_craft.py` | `§ Compression rules` rows citing the round-74 entry | No — different section; my insertion does not touch it. |
| `verifiers/check_author_rules.py` | four rendered boxes in § Trigger-fidelity checklist | No — different section. |
| `verifiers/check_agentdef_boxes.py`, `check_alwayson_boxes.py` | their own checklist sections | No — different sections. |
| `verifiers/check_assertion_floors.py` | `verifiers/*.py` instruments via `verifiers/floors-registry.json` | No — the floors are per verifier file, not per SKILL.md line. |
| `verifiers/check_tip_battery.py` | six BATTERY scripts, `INSTRUMENT_PINS`, and a no-deletion guard that names `SKILL.md` | No — the `LINE_CAP = 40` instrument-size guard applies to the instrument scripts, not to `SKILL.md`; `SKILL.md` appears only in the deletion guard. |

So exactly one gate counts the lines I add: `verify_skill_checklist.py`'s `trigger.line_budget`.

---

## 7. Findings the L1 and the row seats need

1. **S229 needs the alternate URL form, recorded.** `https://learn.microsoft.com/en-us/agent-framework/agents/skills.md`
   is HTTP 404 (17 969 B error page, 0 `allowed-tools` occurrences); `https://learn.microsoft.com/en-us/agent-framework/agents/skills`
   on the same host and path prefix is HTTP 200 (157 339 B, 1 occurrence). The C2 brief permits the second form for
   a seat whose first form returns no usable text; the row seat must say which form its snapshot is, and the frozen
   host check is `learn.microsoft.com` either way.
2. **The factory page's frozen quote token is on the page.** `does not add tools` occurs (twice — the Next.js
   payload and the rendered DOM both carry the sentence, one statement, not a banner); `not a runtime sandbox` and
   `as a security boundary` likewise. So the `metadata-only` label and its page token are consistent with live bytes.
3. **Claude Code's page is served as Markdown** at `docs/en/skills.md` (my fetched bytes open with the site's
   `>` documentation-index lines, then `# Extend Claude with skills`; no HTML), so the snapshot is Markdown text;
   the `Pre-approve tools for a skill` section (`:617`) is a body section, not a banner (Q70).
4. **Vibe says nothing about the field** — a single `allowed-tools` occurrence, inside the `~/.vibe/skills/code-review`
   example; the adjacent bullets explain `user-invocable` and `disable-model-invocation` only. `unstated` is the
   right label on my bytes; the receipt carries the sweep.
5. **The rule line is only true as a joint statement.** Three of the six pages (spec, msaf, pi) hedge with
   "experimental"; two (Claude Code, Factory) state a mechanism that does not restrict; one (Vibe) states nothing.
   An author-facing line that said "clients honour `allowed-tools` as a restriction" would be false against
   Claude Code (`:617`) and Factory (security-boundary sentence) on my own bytes.
6. **Registry row and counter must land together** (§ 2), and the row's `MANIFEST.sha256` path must be committed
   before the row is measured — otherwise `check_gate_registry.py` reports a phantom row or a dead pinned path.

## 8. Limits

- Drafts only: I did not edit `SKILL.md`, `PROVINCE.md` or `corpus/README.md` (wave-1 freeze discipline).
- I did not run `verifiers/check_allowed_tools.py` (not built yet) and scored nothing on it.
- I did not pin snapshots into `.ufo/waves/round-79/snapshots/` — the row seats own those; my page bytes are
  transient and my scratch dir is removed, so the receipt's sha256 values are the only durable record of my fetches.
- I ran no lane gate; the only numbers here are `wc -l` / `grep -c` reads of committed bytes and my own curl results.
- No client was installed or run: every statement above is documentary.
