verdict: substrate re-census = held ground (quality at best; expansion MUST stay `unchanged` for it — opencode 1.19.3 is the round-13/14 v1 instruction model the corpus already holds and marked historical, omp 18.12.5 is a fifth callee rename of the same 8 classes); description-rule entry = expansion-eligible ONLY if it adds a new coverage-map row and leads with own-work measurements sourced to a `mined` own-work row — as drafted, its headline fact restates SOURCES.md:16 / SKILL.md:151 / QUALITY.md:19 and its own-work row (S010) is `queued`, so it scores `unchanged`.

# CritExpansionClaim — round 47 BUILD (critic, leaf)

Lane-authored advice, not non-author closure. BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. All path:line cites are at BASE unless marked as a wave-47 build artifact. Production files were not edited; no scratch clone was needed (read-only probes only).

## Axes

- **Expansion (LEARNING trend, the attacked claim).** `/home/vgpnk/Projects/shokunin/LEARNING.md:33` defines `improved` as "net new admitted entries on uncovered ground, each citing its coverage-map row", with each `source:` citing a `mined` `corpus/SOURCES.md` row (own-work rows included).
- **Impacted round axes:** calibration (calling a quality move "expansion" mis-records the trend), freshness (the substrate entry is C1's record) and operability (the description entry is C2's record).

## Finding 1 — the substrate re-census entry sits on ground the coverage map already holds

**Counterexample (strongest available): opencode 1.19.3 is not a successor to the v2.0.26 the corpus describes. It is the round-13/14 v1 model coming back.**

The anchor counts come from `rg -c -F <anchor> /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings` (exit 0, 2026-10-21; a missing value means 0).

The v1 anchors that the corpus declares "gone" are present again:

| v1 anchor | count |
|---|---|
| `CONTEXT.md` | 1 |
| `Instruction.resolve` | 1 |
| `disableClaudeCodePrompt` | 2 |
| `instruction-context` | 1 |
| `InstructionContext` | 2 |
| `system-context-builtins` | 1 |
| `Key.make("core/instructions")` | 1 |
| `targets:["AGENTS.md"]` | 1 |
| `<system-reminder>` | 15 |
| `` `Instructions from: ${ `` | 4 |

The round-18 v2.0.26 anchors are absent:

| v2.0.26 anchor | count |
|---|---|
| `InstructionDiscovery` | 0 |
| `SessionInstructions` | 0 |
| `ConfigInstructionPlugin` | 0 |
| `instructions rescanned` | 0 |
| `2.0.26` | 0 |

`1.19.3` itself occurs 2 times.

The byte context (python `find` on the dump) shows the round-14 OC-1/OC-2 shapes verbatim:

    n=[X.join(r.config,"AGENTS.md"),...!t.disableClaudeCodePrompt?[X.join(r.home,".claude","CLAUDE.md")]:[]],y=["AGENTS.md",...!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],"CONTEXT.md"]

It also shows `s.fn("Instruction.find")`, `s.fn("Instruction.resolve")`, `M.fn("InstructionContext.observe")` and `i({name:"instruction-context",…})`.

One shape has drifted: round-14 OC-5's `globUp(<v>.directory,<v>.worktree)` and `globUp(<v>.config,<v>.config)` both give 0 (regex, python, exit 0), and `globUp(` occurs only once.

The corpus already holds this exact model:

- `corpus/knowledge/opencode-extraction-round14.md:38-47` has the OC-1…OC-6 v1 rule table, keyed on the same literals.
- `corpus/knowledge/instruction-surface-census-round13.md:164-175` is the § B historical note. It names these anchors and declares the ids `opencode:instructions/{AGENTS,CLAUDE,CONTEXT}.md`, `opencode:claude-home/CLAUDE.md`, `opencode:config/instructions-remote`, `opencode:read-hook/instructions` and `opencode:instruction-context/AGENTS.md` "historical, not live classes".
- `corpus/knowledge/instruction-surface-census-round13.md:10-23` (round-18 errata) and `opencode-extraction-round14.md:3-12` (errata) say these subsystems are "gone".
- The coverage map indexes both entries: `corpus/README.md:39` (opencode extraction rules) and `corpus/README.md:40` (instruction-surface census).

What this means:

- A new `substrate-recensus-round47.md` that describes the 1.19.3 classes restates held ground.
- Worse, it would become a **third live authority** over opencode § B: the census § B "v2.0.26 model" at `:176-209`, the extraction file's historical v1 body, and the new file.
- The correct record is an **append-only re-verdict**: the historical v1 ids are live again (rule by rule; OC-5's globUp pair is not), and the § B v2.0.26 table is stale.

That re-verdict belongs in the two held entries. It is the LEARNING `quality` trend ("stale entries re-verify … an entry found false or stale and left unmarked" = harmed, `LEARNING.md:34`), not expansion.

**Peer artifact cross-check.** `.ufo/waves/round-47/build/KnowSubstrateRecensus.probe-oc.out.txt` (the scribe's probe) reports `OC-1 array 0`. That count is a regex miss: the array is present in spread form (above). I messaged the scribe (`agent://MoriR22R.KnowSubstrateRecensus-9`).

**Identity change, not freshness.**

- The pinned path `/home/vgpnk/.opencode/bin/opencode` is gone (`ls` → "No such file or directory").
- `~/.local/bin/opencode` is a bash npx wrapper for `package="opencode-ai"`. Its mtime is `Oct  3 17:44`, which predates the round-18 v2.0.26 re-derivation dated 2026-10-14 (`instruction-surface-census-round13.md:10`).
- [INFERENCE] Two opencode distributions coexisted, and the pins tracked the `~/.opencode/bin` one. Re-pinning to the npx-cache ELF (sha256 `179ca421…`, confirmed by `sha256sum`, exit 0) switches the pin to a different distribution channel, and possibly a different product line (1.19.3 < 2.0.26).
- The entry must say this outright. Otherwise "re-pinned to the current opencode" sounds like an upgrade, and that would be false provenance.

**omp 18.12.5 adds no ground.**

- A python regex over `/fast/scratch/kotoba-r47/shared/bin/omp-18.12.5` (exit 0) finds the same `.md` registrations under new callees `Fo`/`Xl`. The scribe's probe adds `lq` for the variable-group `agents-md`/`claude-md` pair: "baseline 8 loader ids reproduced by generic shape: 8 / 8 … extra ids: []".
- The registry descriptions persist: `Standalone AGENTS.md` 2, `Load skills from` 12, `Load rules from` 10.
- This is the fifth recorded rename. The predecessors are `Id|Cl|jD[ef]`, then `Tl|dr|GW` (`instruction-surface-census-round13.md:13-15`), then `Co/Dl/Hj` (`verifiers/baseline.json:7`), then `I5/Gl/Mo` (`verifiers/baseline.json:8`), with the allowlist at `verifiers/verify_surfaces.py:156,161`.
- The precedent home for an omp re-derivation is a `measured_against` note plus a census erratum, not a knowledge file.
- `corpus/knowledge/substrate-pin-guard-round23.md:65-67` already prescribes the shape: "re-recording the pin **plus a mechanism note** (what moved and why)".

**What would make the substrate entry expansion (none is in its brief):**

1. **Enter the MCP/plugin frontier row** (`corpus/README.md:73`): run its "next probe", a per-harness census that separates loader-class presence from configured instances. It would have to cite a mined own-work row and add a coverage-map row.
2. **State a cross-round principle as a new `Understanding` entry.** The omp callee rename recurs at every patch release (5 shapes across rounds 13, 18, 21, 44, 47), and the verifier answers each with an ever-growing allowlist (`verify_surfaces.py:156`). That is "connect entries, state the principle" (`LEARNING.md:16-18`). It is quality/understanding, still not expansion, but at least not a restatement.

Without one of these, expansion stays `unchanged` for this entry.

## Finding 2 — the description-rule entry is partly new ground and partly restatement

**It does not restate `frontmatter-trigger-surface.md`.** `rg -c -i xml` gives 0, and `portab` and `1024` give 0 too (exit 0/1, 2026-10-21). The same holds for `anatomy-and-compression.md` and `checklist-execution-round15.md`. The twelve craft rules (`frontmatter-trigger-surface.md:85-155`) are about trigger content, not format validity. No coverage-map row holds "frontmatter validity/portability": `corpus/README.md:9` is trigger surfaces, and `:60-61` index QUALITY/SOURCES as files, not knowledge.

**It does restate held statements in its headline fact.** Draft Fact 1 (`.ufo/waves/round-47/build/KnowDescriptionRule.md:85-88`, "the rule is Anthropic's; the open spec lacks it") is already held in all of these places:

- `corpus/SOURCES.md:16` (S003 *teaches*: "an Anthropic-only rule the open spec lacks")
- `corpus/SOURCES.md:30` (path prose)
- `SKILL.md:151` (portability floor: "no XML tags (Anthropic rule)")
- `corpus/QUALITY.md:19` (Q08)
- `corpus/lessons/round-46.md:31` (M13)
- `corpus/lessons/round-46-verifier-spotcheck.md:12`

The draft's Fact 3 and F4 (folded scalars; a structural parse accepts invalid YAML) restate held entries:

- `corpus/knowledge/checklist-execution-round15.md:259-260`: "`frontmatter_parses` is a structural parse, not YAML-semantic validation".
- `corpus/knowledge/sibling-description-rewrites-round8.md:103-110`: folded block scalar semantics, `yaml.safe_load` fold-back, the more-indented-line hazard.
- `corpus/knowledge/harness-verifier-round10.md:84-92`: scalar style decides the loader-held value.

**Source gap.**

- S003 never defines "XML tag": `KnowDescriptionRule.s003-best-practices.md:146-166` is the `<Note>`, and `:1133-1134` repeats the rule; 12 `xml` lines in total, none a definition. So the draft's tag pattern and its controls (`KnowDescriptionRule.md:90-96`) are a **lane decision**, i.e. own-work.
- The only own-work row on the checker is S010, status `queued` (`corpus/SOURCES.md:23`). Its *teaches* cell says "with no XML-tag rule", which C2 falsifies on landing.
- So as drafted, every new fact in the entry is sourced to a non-mined row, and the one mined row (S003) backs only the restated fact.
- Under `LEARNING.md:33` that is not expansion, and it risks the `harmed` clause ("an admitted entry fails the bar it was admitted under") against Q12 (`corpus/QUALITY.md:23`).

**What the description entry must contain to count as expansion:**

1. **A new coverage-map row.** For example, "Frontmatter validity floor (round 47)", with a basis cell citing S003 and the own-work row. Name the row inside the entry: `LEARNING.md:33` "each citing its coverage-map row". The draft names no row.
2. **A `mined` own-work source** for the landed C2 check. Append a new S row, or log a status flip of S010 per contract rule 2 in the round lesson's `## Gate`, with `used-by` naming the entry. The entry's `source:` must cite it beside S003.
3. **A headline that is the unheld ground, all measured:**
   - the tag-shape decision with its discriminating non-tag controls: autolink `<https://…>`, `a < b and c > d`, `\<`, plus an explicit ruling on `<!-- -->` and `<?xml?>`;
   - value-vs-line semantics: `grep -c '^description:.*<' SKILL.md` gives 0 on a file whose frontmatter holds 1 (`KnowDescriptionRule.md:45-46`);
   - the fold-split non-tag (`a <` / `skills>`);
   - the fleet sweep, 1 of 18 sibling SKILL.md (`KnowDescriptionRule.md:29`).
4. **Pointers instead of restatements** for Fact 1 (to SOURCES.md:16 / SKILL.md:151) and for the fold and parse ceilings (to the three held entries above).
5. **No `<C2-…>` placeholder left at admission, and a `recheck:` that runs without one.** The draft's second recheck embeds `<C2-SELFTEST-ASSERTIONS>` (`KnowDescriptionRule.md:80`), which fails Q04 (`corpus/QUALITY.md:15`) while unfilled. The placeholders are also tag-shaped tokens in an entry about tags.
6. **A `## Gate` record** in the round-47 lesson. LEARNING requires gating plus a non-author spot-check (`LEARNING.md:42-47`); the r46 spot-check is still "pending" (`corpus/lessons/round-46.md:81`).

If rows 1–3 are not met, the entry is knowledge backing for an already-folded rule (`SKILL.md:151` is in § Frontmatter craft). That is a `quality` deepening, and expansion stays `unchanged`.

## Finding 3 — the frontier row both entries would "enter" was already entered, and its numbers are stale

- `corpus/README.md:74` and `PROVINCE.md:21` list "Loader-rule freshness" with "surfaces 5/7 and pins 1/3".
- BASE before-values: surfaces exit 2 at the default resolution, 4 PASS / 3 FAIL with the 1.19.3 binary passed explicitly; pins exit 2, 3/3 failed (`.ufo/waves/round-47/before/SUMMARY.md:3-5`).
- The row was entered at round 46. Landing C1/C2 moves it Frontier → Core, and that is C1/C2's axis work.
- "Frontier areas entered" sits in the *Observable* column, but `improved` needs the admitted-entry condition (`LEARNING.md:33`). So frontier movement alone does not make expansion `improved`.
- Neither entry should cite the frontier row's numbers.

## Finding 4 — corpus-index coupling with C3

- `verifiers/corpus-baseline.json` pins `tracked_files` (58 at BASE; `git ls-files 'corpus/*.md' | wc -l` → 58, exit 0).
- C3 re-baselines it for `lessons/round-46-verifier-spotcheck.md`.
- Each admitted knowledge entry adds a tracked file and needs an index row. If either entry lands after C3's re-record, `verify_corpus_integrity.py` returns to DRIFT, and C3's "0 DRIFT" after-target breaks.
- The draft notes this (`KnowDescriptionRule.md:22`); the substrate entry is subject to it as well.

## Smallest safe correction

1. **Substrate:** do not admit a standalone knowledge file.
   - Append dated errata to `instruction-surface-census-round13.md` (§ B: v1 ids re-verdicted rule by rule, v2.0.26 table marked stale) and to `opencode-extraction-round14.md` (header).
   - Add `omp_round47_note` / `opencode_round47_note` to `verifiers/baseline.json`.
   - Name the distribution and identity switch (npx `opencode-ai` cache ELF; the `~/.opencode/bin` install is gone).
   - Record it as LEARNING `quality: improved` (stale entries re-verify and are marked), `expansion: unchanged`.
2. **Description:** admit only with corrections 1–6 of Finding 2; otherwise fold the measurements into `frontmatter-trigger-surface.md` as an appended rule (quality).
3. **Report:** do not claim `expansion: improved` for either entry unless Finding 2 rows 1–3 hold at landing.

## Commands run (2026-10-21; all read-only)

| command | exit | key output |
|---|---|---|
| `git rev-parse HEAD` (lane) | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| `fd -HI -t f '^LEARNING.md$' .` (fleet root) | 0 | `/home/vgpnk/Projects/shokunin/LEARNING.md` (not in the lane) |
| `rg -n -i 'xml.?tag\|xml.?token\|angle.bracket\|<skills>' corpus SKILL.md PROVINCE.md SCORECARD.md README.md` | 0 | rule held at SOURCES.md:16/:30, QUALITY.md:19, SKILL.md:151, round-46.md:31, README.md:74, PROVINCE.md:21; 0 in frontmatter-trigger-surface.md |
| `rg -c -i xml\|portab\|1024` on frontmatter-trigger-surface / anatomy-and-compression / checklist-execution-round15 | 1 | 0 / 0 / 0 each |
| `rg -n -i 'structural parse\|block scalar\|folded\|plain scalar\|safe_load' corpus/knowledge` | 0 | checklist-execution-round15.md:259; sibling-description-rewrites-round8.md:103-110,473; harness-verifier-round10.md:86 |
| `rg -c -F <anchor> opencode-1.19.3.strings` (18 anchors) | 0 | table in Finding 1 |
| python `find` context for CONTEXT.md / Instruction.resolve / instruction-context / system-context-builtins / disableClaudeCodePrompt | 0 | v1 arrays and `fn(...)` names quoted in Finding 1 |
| python regexes for round-14 OC-3a / OC-5 / `Instructions from` shapes | 0 | OC-3a 1; OC-5 globUp pairs 0 / 0; `Instructions from: ${` 4 |
| `rg -c -F` registry descriptions in omp-18.12.5.strings | 0 | Standalone AGENTS.md 2, Standalone CLAUDE.md 2, Load skills from 12, Load rules from 10, Load prompts from 4, managed-skills 10 |
| python `.md` call-shape regex over `bin/omp-18.12.5` | 0 | 9 literal hits under `Fo`/`Xl` (gemini ×3 names, github, opencode, windsurf) |
| `ls -la ~/.local/bin/opencode /home/vgpnk/.opencode/bin/opencode`; `file`; `head -c 600` (read, not executed) | 2 (ls) | pinned path absent; wrapper is a bash npx script, `package="opencode-ai"`, mtime Oct 3 17:44 |
| `sha256sum` npx-cache opencode ELF; `omp --version`; `sha256sum ~/.local/bin/omp` | 0 | `179ca421…`; `omp/18.12.5`; `fdbc8136…` (= SHA256SUMS) |
| `git ls-files 'corpus/*.md' \| wc -l` | 0 | 58 |
| `sed -n 146,166p` + `rg -n -i xml` on `KnowDescriptionRule.s003-best-practices.md` | 0 | no definition of "XML tag"; rule at 155, 162, 1133, 1134 |

No tools were installed or updated.

## Addendum — re-check of the revised drafts (2026-10-21, after both scribes replied)

I re-read both revised drafts with `rg -n` and `awk` (exit 0).

**`KnowDescriptionRule.md`**

- Finding 2, correction 1 is met as a proposal: §8 drafts a README row.
- Correction 2 is met as a proposal: §8 drafts an S012 own-work row.
- Correction 4 is accepted: §8 replaces the restatements with pointers to the held entries.
- The tag pattern is now labelled a lane decision.
- **Correction 5 is still open.** The draft `recheck:` (`KnowDescriptionRule.md:80`) still embeds `<C2-SELFTEST-ASSERTIONS>`. Fact 4 (`:109-111`) still carries `<C2-FM-TAG-COUNT>`, `<C2-CHECKLIST-PASS>` and `<C2-CHECKLIST-FAIL>`. They must be filled before admission.
- **The S012 row must land as `mined`** with `used-by` naming the entry. A `queued` row does not satisfy `LEARNING.md:33`. Tier C is allowed, but the status must still be `mined`.
- **Corrections 1–2 are L1 fills, not landed.** Until they land, expansion is `unchanged`.

**Second re-check (2026-10-21, after the scribe reported the entry placeholder-free)**

Extracted the draft entry (§5) and re-ran its checks:

- Placeholders: `rg -n '<C2-|<L1|TODO|TBD'` on the §5 entry → no match (exit 1). **Correction 5 is met.**
- Recheck, first half: `curl -sSL …/best-practices.md | grep -c -i 'cannot contain xml tags'` → 2 (exit 0).
- Recheck, second half: `python3 -B verifiers/verify_skill_checklist.py --self-test` → `0 failure(s) over 1597 assertions` (exit 0).
- S012 row: status `mined`, tier C, used-by names the entry (`KnowDescriptionRule.md:152`).

Two items remain open:

- **The entry's `source:` line does not cite S012.** `rg -c S012` on the §5 entry → 0 (exit 1). The line cites only S003 and S001. Correction 2 needs S012 named beside S003, because S012 is the row that backs the own-work facts.
- **§8 contradicts itself on tier.** The lead-in at `KnowDescriptionRule.md:149` says "tier A" while the row at `:152` says C. Cosmetic, but the L1 copies from it.

**Third re-check (2026-10-21, 16:04 UTC): both items closed.**

- The §5 `source:` line now cites S001, S003 and S012: `rg -o 'S0[0-9]+'` on that line → `S001 S003 S012`.
- `KnowDescriptionRule.md:149` now reads "tier C", matching the row.
- Placeholders are still absent (`rg -c` exit 1).
- **The draft meets all six Finding 2 corrections as a proposal.** Expansion becomes `improved` only when the L1 lands:
  - the README coverage row,
  - the S012 row in `corpus/SOURCES.md`,
  - the corpus index re-record (Finding 4),
  - the round-47 `## Gate` record with a non-author spot-check.

  Until then, expansion is `unchanged`.

**`KnowSubstrateRecensus.md`**

- It now cites the OC-1 array at dump line 443993 (`:90`).
- It refines my OC-5 point (§B.4 table row `:85`; draft-entry §4 `:170`). In 1.19.3 the switch is a 3-argument `globUp(T,d.directory,d.worktree)` rather than absent. Finding 1's "0/0" therefore means the round-14 two-argument shape is gone, not that the switch is gone.
- Errata placement is recorded as an L1 fill (`:207`).
- My verdict stands: this is quality (an append-only re-verdict), and expansion is `unchanged`.

## What I did NOT check

- I did not re-derive OC-1…OC-6 or run `verify_surfaces.py` / `check_substrate_pins.py`. Rule-by-rule match status beyond the literal and shape counts above belongs to C1's executors.
- I did not determine whether opencode `1.19.3` and `v2.0.26` are the same product line. That one is a downgrade or a different fork is [INFERENCE] from the version ordering and the disjoint anchor sets.
- I did not read the Anthropic "Skills overview" page linked from S003 for a definition of "XML tag".
- I did not read the final `KnowSubstrateRecensus.md` draft; it was not yet written when I checked (only its probes and snapshots existed). Finding 1 rests on the snapshot and the scribe's probe outputs.
- I did not run `verify_corpus_integrity.py` with the entries added, so the Finding 4 coupling is reasoned from the baseline field and the r46 precedent, not executed.
- I did not check the MCP/plugin frontier probe (Finding 1, "what would make it expansion") for feasibility on 18.12.5 / 1.19.3.
- I did not check `PROVINCE.md` Core-move wording or SCORECARD trend lines; those are peer scopes (ConnProvinceFrontier, ConnLearningTrends).
