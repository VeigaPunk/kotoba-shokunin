verdict: PARTIAL — the append-only + 42-id parity contract in `corpus/knowledge/instruction-surface-census-round13.md` HOLDS exactly (5/5 moved rows byte-identical, 0 prose rewrites, 42/42/42 parity), but four live prose statements in the same file were made false or left false by the round-47 change (stale rule/id counts, an emptied § B table, a "not live classes" claim the new ledger contradicts, and § A's omp evidence quotes that are 0-occurrence in the pinned omp 18.12.5).

Target: `corpus/knowledge/instruction-surface-census-round13.md`
Attacked commit: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`)
Scratch clone: `/fast/scratch/kotoba-r47/w2/W2CensusAppendOnly/kotoba-shokunin` (detached at 7ad7fad); no writes to the production repo outside this report + the `W2CensusAppendOnly.*` artifacts.
Tooling: system python3 3.14.8, git 2.56.0, sha256sum 0.8.0. **No tool was installed or upgraded by this lane** (nothing needed installing; no pacman transaction).

---

## A. The three acceptance checks — ALL HOLD

### A1. Every removed line reappears byte-identical; no v2.0.26 prose line rewritten

`git diff c61a973 7ad7fad -- corpus/knowledge/instruction-surface-census-round13.md` → `93 +++++---` (88 insertions, 5 deletions). The 5 deleted lines are **all table rows**, no prose:

```
-| `opencode:project/AGENTS.md` | AGENTS.md | loader-literal | AGENTS.md row | `ConfigInstructionPlugin.projectSource` + `targets:["AGENTS.md"]` all-match walk (OC-1) |
-| `opencode:config/AGENTS.md` | AGENTS.md | loader-config | AGENTS.md row | `j5(r.config,"AGENTS.md")` global candidate (OC-2) |
-| `opencode:read-hook/AGENTS.md` | AGENTS.md | loader-literal | Cross-tool rule files | `ReadTool.Plugin` + `targets:[a$]` + `SessionInstructions.load` → `Instructions from:` (OC-4) |
-| `opencode:api-entries/instructions` | instructions | loader-config | § Instruction surfaces → Declared instruction list | `/instructions/entries` + `session.instructions.entry.put` (OC-6) |
-| `opencode:config/instructions` | instructions | loader-config | Schema-declared "ambient instructions" list in v2.0.26; **no loader consumer proven** in the binary — only the read-hook publishes file contents (round-18 re-derivation, OC-3 witness only) |
```

Programmatic check (python3, exit 0): each of the 5 removed strings is **byte-identical** to a line in the added set, occurs **exactly once** in the new file, and occurred exactly once in the old file. No `v2.0.26` prose line was touched.

**Stronger residual test (append-only proof).** Removing *only* (a) the 5 moved rows, (b) the new `### B′` block, (c) the new `## Superseded class rows…` section, and (d) the 5-line round-47 errata paragraph inserted at § B, the residual old file and the residual new file are **identical line-for-line** (`RESIDUAL OLD-vs-NEW identical: True`, exit 0). ⇒ the diff is strictly additive apart from the 5 row moves; no existing prose was rewritten, reordered, or trimmed.

### A2. The moved rows now sit outside `## Class inventory`

- `## Class inventory` = census:64; the section runs to the next `^## ` heading = census:287 (`## Superseded class rows and the round-47 opencode ledger (not inventory)`), i.e. census:65–286 (`verify_surfaces.py:171-172,505-524`).
- The 5 moved rows now live at census:**296, 297, 298, 299** (4-row table) and census:**303** (the former § C row) — all **> 287**, i.e. outside the counted section. ✓
- § B′'s 9 live rows (census:249-257) are inside the section. ✓

### A3. table_parity / literal_parity / kind_parity still count exactly the 42 baseline ids

```
$ python3 verifiers/verify_surfaces.py --repo . \
    --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
    --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings
PASS surfaces.literal_present: 42 loader-kind entries verified against the dumps
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
EXIT=0
```

Independent recomputation (not via the verifier's own code): backticked ids in `|`-led rows of census:65–286 = **42**, set-equal to `verifiers/surfaces-baseline.json` `classes` = **42** (33 `omp:` + 9 `opencode:`), `equal: True`. Baseline: BASE 38 classes / 5 opencode → HEAD 42 / 9.

`verifiers/verify_surfaces.py --self-test` → `0 failure(s) over 99 assertions`, exit 0.
`verifiers/verify_corpus_integrity.py --json` → exit 0.

---

## B. Freshness / calibration attacks that PASSED (findings in their own right)

### B1. Every ledger anchor count re-derives exactly (20/20)

Re-ran the census's own count command (`d.count(anchor)` on the frozen 1.19.3 dump) for all 20 anchors asserted in § B′ / the round-47 ledger — **all match, zero drift** (artifact `W2CensusAppendOnly.ledger-counts.json`, `"all_match": true`):

`ConfigInstructionPlugin.projectSource` 0 · `X.join(r.config,"AGENTS.md")` 1 · `j5(r.config,` 0 · `ReadTool.Plugin` 0 · `SessionInstructions.load` 0 · `SessionInstructions` 0 · `session.instructions.entry.put` 0 · `instructions:{entry:{list:` 1 · `for(let O of T.instructions)` 1 · `CONTEXT.md` 1 · `X.join(r.home,".claude","CLAUDE.md")` 1 · `Instructions from: ` 4 · `fn("Instruction.resolve")` 1 · `fn("ReadTool.execute")` 1 · `InstructionContext.observe` 1 · `system-context-builtins` 1 · `disableClaudeCodePrompt` 3 · `InstructionDiscovery` 0 · `<system-reminder>` 18 · `var n="1.19.3"` 1 · `2.0.26` 0.

### B2. Every cited dump line number is exact

`443993` → `y=["AGENTS.md",` / `n=[X.join(r.config,"AGENTS.md")` / `X.join(r.home,".claude","CLAUDE.md")` / `for(let O of T.instructions)` / the `https://` filter / `globUp(T,d.directory,d.worktree)` / `"CONTEXT.md"]` / `!t.disableClaudeCodePrompt?["CLAUDE.md"]:[]` — all on that one line. `443995` → `fn("Instruction.resolve")` and `while(G.startsWith(N)&&G!==N)`. `444228` → `fn("ReadTool.execute")`. `445481` → `Key.make("core/instructions")`; `445482` → `InstructionContext.observe` + `jX(L.config,"AGENTS.md")` + `targets:["AGENTS.md"]`; `445487` → `system-context-builtins`. The cited range 445481-445487 is exactly the 7-line window that carries all four OC-6 anchors. ✓

### B3. Substrate identity is fresh and pinned

- `sha256sum -c /fast/scratch/kotoba-r47/shared/SHA256SUMS` → 4/4 OK, exit 0.
- Live npm binary `~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` → `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9` = census:215 (B′ "Substrate") = SHA256SUMS. ✓ (I did **not** execute the `~/.local/bin/opencode` wrapper; I hashed the npx ELF the wrapper resolves to.)
- `~/.opencode/bin` (the v2.0.26 channel) is gone, matching census:218.
- `omp --version` → `omp/18.12.5`; frozen `bin/omp-18.12.5` sha256 `fdbc8136…` matches SHA256SUMS and `verifiers/baseline.json`'s `round47_note`. ✓

### B4. The relocation is load-bearing and the isolation is real (mutation matrix, exit codes captured)

| mutation | artifact | result |
|---|---|---|
| Re-insert the 4 v2.0.26 rows inside § B (i.e. back inside `## Class inventory`) | `W2CensusAppendOnly.mut-A2_rows_back_in_inventory.md` | **exit 1** — `FAIL surfaces.table_parity: extra row(s) not in baseline: opencode:api-entries/instructions, opencode:project/AGENTS.md, opencode:read-hook/AGENTS.md` |
| Demote the Superseded heading `##` → `###` (rows fall back into the inventory section) | `…mut-D_heading_demoted.md` | **exit 1** — table_parity + literal_parity (9 rows) + kind_parity (9 rows) FAIL |
| Demote the Superseded heading `##` → `#` | `…mut-E_heading_h1.md` | **exit 1** — same three FAILs |
| Insert a fabricated id row **inside** the Superseded section | `…mut-B2_bogus_row_in_superseded.md` | **exit 0**, 7/7 PASS — confirms the section's own claim "`verify_surfaces.py` does not count them" is TRUE |
| Rewrite a § B′ literal cell (`CONTEXT.md` → `WRONG.md`) | `…mut-C_literal_drift.md` | **exit 1** — `FAIL surfaces.literal_parity: opencode:instructions/CONTEXT.md (line 251)` |

⇒ the section boundary is the load-bearing mechanism, and it is honoured exactly.

### B5. The round-14 evidence file the census cites is (again) accurate

`corpus/knowledge/opencode-extraction-round14.md` is **unchanged BASE→HEAD** (last touched at `29c17be`, round-14) yet its live-tree row (`:106`) reads verbatim `7/7 PASS, exit 0 … 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)` — byte-equal to what the live verifier prints today. So the round-47 re-derivation restored the round-14 rule set the file already documented; the census's pointer (census:374, 428) resolves to a current artifact.

---

## C. FINDINGS (defects)

### C-1 [MEDIUM] § "Honest ceiling" still describes the round-18 instrument (6 rules / 5 ids) — round 47 changed the instrument and left this live prose stale

`corpus/knowledge/instruction-surface-census-round13.md:370-372`:

```
  `surfaces.opencode_extract` — six code-shape rules (OC-1…OC-6, anchors and
  derive-vs-witness stated per rule) that must reproduce all 5 declared opencode
  class ids, must produce no undeclared id, must each match, and must not produce
```

Live at 7ad7fad: **7** rules (`OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6`) and **9** declared opencode class ids — verifier output line 3 above, and `verifiers/verify_surfaces.py:454,464,471,475,482,490,497` (7 `rule(...)` calls) vs `:471,:475` splitting the old `OC-3` into `OC-3a`/`OC-3b`.

At BASE this line was TRUE (BASE verifier had 6 `rule(...)` calls at `414,419,425,432,437,442` and the BASE baseline had 5 opencode ids). Round 47 changed the rule set **and** the baseline (5→9 opencode ids) and did not correct or erratum this line. Repro:

```
$ cd /fast/scratch/kotoba-r47/w2/W2CensusAppendOnly/kotoba-shokunin
$ grep -n 'rule("OC-' verifiers/verify_surfaces.py | wc -l        # → 7
$ git show c61a973:verifiers/verify_surfaces.py | grep -c 'rule("OC-'  # → 6
$ python3 verifiers/verify_surfaces.py --repo . --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
      --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings --check surfaces.opencode_extract
# PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)
```

Same class of defect, secondary site: census:27-29 (the "Round-14 amendment" paragraph) still says "opencode is covered by its own machine check … (six code-shape rules, two-way parity, zero-extraction FAILs)". That paragraph is explicitly dated 2026-09-28 so it reads as history; census:370-371 does not.

### C-2 [MEDIUM] The round-18 errata's pointer to "§ B's table" is now dangling — § B's table is empty at 7ad7fad

`corpus/knowledge/instruction-surface-census-round13.md:18-22`:

```
are all gone from the new binary; the five old class ids in § B's table are
historical (falsified-pointer preservation — they describe the 2026-09-28
binary, not the current one). The round-13/14 quotes of § B prose remain as
historical records; the table and the prose above it now describe the live
binary. Binaries at re-derivation: omp `ff59fc1b48…`,
```

At 7ad7fad § B's table is a **header + separator with zero body rows** (census:209 `| class_id | literal | kind | governed by | evidence |`, census:210 `|---|---|---|---|---|`, then census:211 blank). The five rows are at census:296-299 and 303, i.e. in the new `## Superseded class rows…` section. So:

- "the five old class ids in § B's table" — there is no longer any row in § B's table;
- "the table and the prose above it now describe the live binary" — § B's prose describes **v2.0.26**, not the live 1.19.3 binary; § B′ (census:212+) is what describes the live binary.

Round 47 added its own errata at census:164-167 pointing forward to § B′, so a careful reader recovers the truth — but the file now carries two errata paragraphs making opposite claims about the same table, and the older one is the one a reader reaches first (preamble, line 10). Repro: `awk 'NR>=205 && NR<=214' corpus/knowledge/instruction-surface-census-round13.md` (see §A2 above for the empty table).

### C-3 [MEDIUM] § B's "not live classes" sentence is contradicted by the file's own round-47 ledger

`corpus/knowledge/instruction-surface-census-round13.md:176-180`:

```
declared — `opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md`,
`opencode:claude-home/CLAUDE.md`, `opencode:config/instructions-remote`,
`opencode:read-hook/instructions`, `opencode:instruction-context/AGENTS.md` —
are superseded-revision claims preserved as historical, not live classes.
```

Those five ids are exactly the ids the round-47 ledger at census:315-321 marks **`resurrected`**, and they are 5 of the 9 live opencode baseline ids (§ B′ rows census:249-257). The sentence was true at BASE (v2.0.26 had none of them) and became false with round 47's substrate move. The § B errata at census:164-167 does not mention it, and the sentence sits 32 lines above the § B′ heading (census:212), so it reads as a live statement about the current ids. Repro:

```
$ grep -n 'resurrected' corpus/knowledge/instruction-surface-census-round13.md   # census:315-321
$ grep -n 'not live classes' corpus/knowledge/instruction-surface-census-round13.md  # census:180
```

### C-4 [MEDIUM, freshness] § A's omp evidence quotes are 0-occurrence in the pinned omp 18.12.5, and § A's substrate is a binary that is no longer pinned

Census:73-80 (the § A table) cite these omp call shapes in the `evidence` column:

`jDe(e,Pqr,"AGENTS.md")`, `Pqr = "agents-md"`, `jDe(e,BWr,"CLAUDE.md")`, `BWr = "claude-md"`, `Id(e,"opencode","AGENTS.md")`, `Id(e,"gemini","GEMINI.md")`, `Cl(e,"gemini","GEMINI.md")`, `Id(e,"gemini","system.md")`, `Cl(e,"gemini","SYSTEM_TEMPLATE.md")`, `Cl(e,"github","copilot-instructions.md")`, `Id(e,"windsurf","memories/global_rules.md")`.

Every one of them occurs **0** times in `/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` (the pinned substrate, sha256 `fdbc8136…`). The real 18.12.5 shapes are `Xl(u,"opencode","AGENTS.md")`, `Fo(u,"gemini","GEMINI.md")`, `Fo(u,"gemini","system.md")`, `Xl(u,"gemini","system.md")`, `Fo(u,"gemini","SYSTEM_TEMPLATE.md")`, `Xl(u,"gemini","SYSTEM_TEMPLATE.md")`, `Fo(u,"github","copilot-instructions.md")`, `Xl(u,"windsurf","memories/global_rules.md")` — i.e. the **third** minifier generation (`lq|Xl|Fo`), matching `verifiers/verify_surfaces.py:144` ("lq/Xl/Fo (2026-10-21, 18.12.5: discovery helpers)").

Related stale pointers in the same file: census:22 still names omp `ff59fc1b48…` as "Binaries at re-derivation" (not the pinned `fdbc8136…`), and census:13-14 still describes the omp callee generation as "`Id|Cl|jDe` → `Tl|dr|GW`, allowlist re-pinned in the verifier".

The **class set is unaffected** — `surfaces.no_uncovered_class` extracts exactly the 8 declared loader-group pairs from the 18.12.5 dump and the parity checks are green — so this is not a parity break. It is a live evidence-column quote that cannot be verified against the substrate the same round pinned. Note the asymmetry: round 47 gave opencode a full fresh "Substrate" paragraph (§ B′) and a fresh ledger, but gave omp nothing — while `corpus/README.md:76` itself records "the omp extractor is a callee-name allowlist, so the next minifier rename is a red gate plus a hand re-derivation", i.e. the corpus knows § A's substrate note is the stale half. Repro:

```
$ python3 - <<'EOF'
d=open('/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings',errors='replace').read()
for a in ['jDe(e,Pqr,"AGENTS.md")','Pqr = "agents-md"','Id(e,"opencode","AGENTS.md")',
          'Cl(e,"github","copilot-instructions.md")','Id(e,"windsurf","memories/global_rules.md")']:
    print(a, '->', d.count(a))
EOF
# all -> 0
```

### C-5 [LOW] `--self-test` assertion count in the census is 75; live is 99

`corpus/knowledge/instruction-surface-census-round13.md:355` (Reconciliation table, "After (round 13)" column): "…exit 0/1/2/3, `--self-test` 75 assertions". Live: `python3 verifiers/verify_surfaces.py --self-test` → `0 failure(s) over 99 assertions`, exit 0. The same stale 75 appears at `corpus/knowledge/opencode-extraction-round14.md:107`. The census row is labelled as round-13/14 history, so this is a presentational staleness rather than a false claim — but it is the only place the census states the instrument's assertion count, and the round-47 verifier work changed it. Left as LOW because the row is explicitly a "what the skill said" snapshot.

### C-6 [LOW, cosmetic] § B is left with an empty table

Census:209-210 keep the `| class_id | literal | kind | governed by | evidence |` header and separator with **no body rows** after the 4 rows were moved out. Verifier-neutral (the header row's first cell is `class_id`, so `ROW_ID_CELL_RE` does not match and the row carries no backticked id — `literal_parity`/`kind_parity` skip it), but § B now renders an empty table in a document whose § B′ is the live one. A reader can mistake the header for an empty inventory.

---

## D. Residual risk / verification gaps — what I did NOT check

1. **Runtime behaviour.** Everything above is strings-level. Whether the opencode 1.19.3 instruction service or the `instruction-context` subsystem actually fires is undecided by this method (the census itself declares this ceiling at census:232 — "Whether either subsystem fires at runtime is not decided by strings (§ Honest ceiling)" — and in § Honest ceiling, census:361-362). No opencode session was launched; the `~/.local/bin/opencode` wrapper was never executed (it can swap the binary under `npx --prefer-online`); I read the frozen snapshot and hashed the npx ELF instead.
2. **The two unchecked census columns.** `governed by` and `evidence` have no machine counterpart in `surfaces-baseline.json` (the census says so itself, census:402-406). I verified the *opencode* `evidence` cell anchors by hand (B1/B2 above) but I did **not** adjudicate whether each of the 9 opencode ids is *correctly* mapped to its SKILL.md craft row — only that id/literal/kind match the baseline.
3. **§ A beyond the 8 loader-group rows.** I checked the 8 machine-extracted omp rows' quoted call shapes; I did **not** re-derive the 25 hand-declared omp `loader-literal`/`loader-config` rows (e.g. `omp:provider-gate/enabledProviders`, `omp:agent-system-prompt/SYSTEM.md`) against the 18.12.5 dump, so C-4's stale-quote class may extend further into § A than the 8 rows I sampled.
4. **omp runtime and omp § A2/A3.** The provider-priority table (census:106-131) and the wire-level probe (census:132+) are round-13 single-lane derivations; I did not re-run the merge on 18.12.5.
5. **Out of scope by assignment (other lanes):** C2 (`trigger.no_xml_tag`, `SKILL.md` description `<skills>` loss), C3 (`GOVERNANCE_ERRATA` LOG.md:2111, `corpus/README.md` indexing, `corpus-baseline.json` 58→60, the fault-harness planter fix), the round-47 before/after battery, and the other 44 files in the round-47 diff.
6. **Not run:** the round-47 `before/SUMMARY.md` battery, `check_substrate_pins.py`, `verify_skill_checklist.py`; I only ran `verify_surfaces.py` (live + `--self-test`) and `verify_corpus_integrity.py`.
7. **Frozen substrate assumed read-only** (mode `r--r--r--`); I verified `sha256sum -c` on it once, at the start. I did not re-verify after the fact.

## E. Artifacts (this lane)

- `W2CensusAppendOnly.ledger-counts.json` — 20/20 re-derived anchor counts, `all_match: true`.
- `W2CensusAppendOnly.mut-A2_rows_back_in_inventory.md` — 4 rows re-inserted inside `## Class inventory` → verifier exit 1.
- `W2CensusAppendOnly.mut-D_heading_demoted.md` — Superseded heading `##`→`###` → verifier exit 1.
- `W2CensusAppendOnly.mut-E_heading_h1.md` — Superseded heading `##`→`#` → verifier exit 1.
- `W2CensusAppendOnly.mut-B2_bogus_row_in_superseded.md` — fabricated id row inside the Superseded section → verifier exit 0 (section is not counted).
- `W2CensusAppendOnly.mut-C_literal_drift.md` — § B′ literal rewritten → verifier exit 1 on `literal_parity`.
