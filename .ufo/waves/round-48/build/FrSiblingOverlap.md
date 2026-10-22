# FrSiblingOverlap — round 48 build, sibling-overlap scan for C1 and C2

Seat KotobaR48.FrSiblingOverlap (read-only leaf), 2026-10-22 UTC; lane base `75f671b`; scratch
`/fast/scratch/hyaku/kotoba-r48-a2/seats/FrSiblingOverlap/`.

## Findings

1. **No sibling owns the C2 ground.** I searched the `corpus/knowledge/`, `corpus/SOURCES.md`
   and `SKILL.md` files of 20 sibling lanes (chousa, tameshi, kumitate and kengaku included).
   None contains `agentskills`, `quick_validate`, `agent-skills-spec` or `allowed-tools`, and no
   sibling has a per-authority frontmatter-rule entry. Every `skills-ref` hit is game-dev-3d's
   unrelated clone path `/tmp/ue-skills-ref`. A whole-tree scan of every sibling (excluding
   `.git`, `.jj` and `node_modules`) found nothing else. The plan's "uncovered ground" holds
   fleet-wide, so kotoba must derive the authority table itself. There is no sibling row to cite
   in place of S001, S003, S012, S013 or the new `skills-ref` row.
2. **Sibling evidence to cite as observed inputs, not as authorities:**
   - `tameshi-shokunin/SKILL.md:1738` (sha256 `7d3a9e29…`, last commit `c6e827a`) records
     tameshi's own repair: an unquoted frontmatter `description:` that strict YAML rejects at the
     second `: `, fixed by quoting (RR01). This is fleet precedent for a fourth counterexample
     class, a plain scalar containing `: `, alongside the three routed classes (YAML alias,
     Unicode name, escaped value).
   - `game-dev-3d-shokunin/reports/round-101/probes/skill-frontmatter.md:79-100,270-272`
     (tracked, sha256 `309f15b9…`) is a parsed probe of three vendored Epic `SKILL.md` files
     (upstream pin `a6aa73a`). It already shows the **escaped-value** case:
     `upstream/skills/unreal-mcp/SKILL.md:3` holds 10 `\"` escapes, and a naive `strip('"')`
     leaves backslashes behind. Cite it instead of building a new escaped-value fixture.
   - The same vendored bytes are a **real shipped breach of the spec's description limit**. I
     re-measured them with PyYAML: `create-toolset` decodes to 1054 characters and `unreal-skill`
     to 1041, both above the spec's "Must be 1-1024 characters". The files are
     `game-dev-3d-shokunin/corpus/knowledge/unreal-mcp/upstream/skills/{create-toolset,unreal-skill}/SKILL.md:3`
     (sha256 `e9d05008…`, `7a0af781…`). The probe itself never compares against 1024.
3. **New observation from running the lane checker on the fleet:** **10 of 18** lane-root
   `SKILL.md` files fail `yaml.safe_load` with `mapping values are not allowed here`. The cause is
   an unquoted description containing `Rank: shonen.`, `Trigger strings:` or `Anti-trigger:`.
   The ten lanes are game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kumitate, mado, tabi and
   tsukuroi. kotoba's `trigger.frontmatter_parses` and `trigger.no_xml_tag` (HEAD bytes)
   **PASS all ten**. The lenient parser explains this: `verifiers/verify_skill_checklist.py:515-525`
   was relaxed in round 15 after 37/138 fleet files failed a stricter rule. The lane checker also
   has no description-length bound: a 1054-character description passes `check_frontmatter`.
   lore and souji have no `name:`. PyYAML accepts them, and the lane check correctly FAILs them.
   The C2 entry should record that "parses" in the lane means a structural line parse, not YAML.
4. **C1 (opencode configured roots): no sibling authority exists, and nothing in a sibling
   contradicts the union design.** Sibling rows are host snapshots, not loader rules:
   - `kagi-shokunin/corpus/knowledge/config-layering.md:18-21` (opencode 1.18.31, 2026-09-28)
     lists the global config layers, including `agents/` (plural), but never names a skill
     directory. Lines 104-106 bind it to that version, and lines 112-128 mark it **historical**,
     so it is not citable as current.
   - `kama-shokunin/corpus/knowledge/consumer-registry.md:325` saw `~/.config/opencode/skills/`
     (plural) present on the host at the time. Today, with opencode `1.19.3`, `~/.config/opencode`
     holds only `cli.json`, `opencode.json` and `service.json`, and neither `skill/` nor `skills/`
     exists. The kama row is stale for the live host. It does not touch the fixture-driven ruler.
   - `kumitate-shokunin/corpus/knowledge/kimi-skills-plugins.md:311,336-345,353-356` gives the
     **Kimi** analogue: a skill's identity is its directory name under a scanned root; two user
     roots merge by name and one wins; the scan order is UNKNOWN. This is useful adjacency for
     "direct-child directory name, set semantics", but it is a different client and cannot be
     cited as opencode authority.
   - `mado-shokunin/corpus/knowledge/omarchy-drift-watch.md:44-48` and
     `kaidoku-shokunin/corpus/knowledge/2026-10-13-mcp-registrations.md:38` record installed skill
     roots for other clients (`~/.claude/skills`, `~/.codex/skills`, `~/.pi/agent/skills`). They
     are not opencode roots.
   - `kengaku-shokunin/SKILL.md:315` observes that opencode puts a skills catalog in its system
     envelope. That is consumption evidence, not a root rule. chousa has no relevant hit.
   - The fleet ledger `.ufo/reports/AGGREGATE.md:1199`, row D-96 ("six `*-shokunin/SKILL.md`
     inside no discovery root"), was claimed by **kotoba's own** round-12 report. It is not
     sibling knowledge, so C1 needs no sibling citation.
5. **Contradictions and tensions with the plan.** No sibling row contradicts C1 or C2 as
   declared. Three tensions should be carried explicitly:
   - **Self-tension, C2.** kotoba's S001 row (`corpus/SOURCES.md:14`) teaches "SKILL.md under 500
     lines", but the lane's own `SKILL.md` is **528** lines at HEAD. In the spec, this rule sits in
     §Progressive disclosure as advice ("Keep your main SKILL.md under 500 lines"). It is not in
     the field constraints, which are written as "Must…". The entry should classify it as guidance.
     Otherwise it reads as a rule the lane breaks.
   - **Scope, C2.** The three routed counterexamples are not the whole set. The fourth class
     (`: ` in a plain scalar) affects 10/18 fleet files and passes the lane checker. The entry
     must not imply coverage of all four classes.
   - **Custody, C1.** The lane working copy's `verifiers/verify_harness_independent.py` hashes to
     `2d824c0b…`, which equals the candidate consumer (`r48-cand`). HEAD's blob is `872993f8…`.
     The uncommitted state is the L1's, and I did not touch it. The ruler's `--revision` must
     name the landed commit, not the working tree.

## Peer corroboration (08:17 UTC; receipts read, not re-run)

Two independent validators reproduce finding 3 over the same 21 inputs:

- **Anthropic `quick_validate.py`.** Pinned blob `ed8e1ddd`, equal to the S012 pin `dbd4588`.
  Source: `C2QuickValidateFresh.md:96-109`. 14 of 21 inputs fail:
  - the same 10 lanes, with "Invalid YAML in frontmatter";
  - lore and souji, with "Missing 'name'";
  - `create-toolset` and `unreal-skill` (1054 and 1041 characters), with "Description is too long".
- **`skills-ref`.** Pinned `69ef37e9…`; its parser is `strictyaml` 1.7.3. Source:
  `C2SkillsRefSource.md:98-108,144-146`. The same 12 lanes fail and both vendored descriptions
  exceed 1024. The YAML divergence is therefore not specific to PyYAML.
- **Authority split on angle brackets (C2SkillsRefSource F1 and F6).** `skills-ref` does not ban
  `<` or `>` in a description; it HTML-escapes them. The ban exists only in S012.

Net: PyYAML, strictyaml and quick_validate all reject 10 files the lane check passes.

## Proposed move (one, bounded)

The C2 entry should add an **"observed fleet inputs"** section. It pins the 18 lane-root
`SKILL.md` files plus the 3 vendored Epic files by sibling HEAD and sha256. Each authority that
can run locally is run over those same 21 inputs: PyYAML `safe_load` as a strict-YAML proxy,
kotoba `trigger.frontmatter_parses` / `trigger.no_xml_tag`, `skills-ref` and `quick_validate`
(both already run by peers, above). Sibling paths are cited, not re-derived.

- **Axes.** Freshness improves: a fourth counterexample class and a real shipped length breach,
  both observed locally. Depth/discernment improves: the result separates lexical "parses" from
  YAML validity. The C2 count target (34 to 35 entries) is unchanged, and C1 is untouched.
- **Second-order effects.** Routed defect 3 (mirror versus parsed-value rule) gets a
  lesson-backed QUALITY criterion with a measured failing set. The 10 YAML-invalid sibling
  files are not kotoba's: route them to the integrator, as D-96 was; never edit them.
- **Risks.**
  - Sibling bytes change between rounds: pin by hash and HEAD; read the table as dated.
  - PyYAML and strictyaml are parsers, not any client's loader. Label them that way.
  - Do not claim any client refuses these files: opencode, Claude and Codex runtime behavior on
    them is unobserved here.
- **Verification.** Re-run
  `python3 -B /fast/scratch/hyaku/kotoba-r48-a2/seats/FrSiblingOverlap/fm_census.py`
  and expect 10 `YAML_ERROR=ScannerError` rows. For the lane checker, run `parse_frontmatter`
  and `check_frontmatter` from a `git show <landed>:verifiers/verify_skill_checklist.py` copy over
  the same paths. They must still PASS the ten, unless C2 deliberately changes the checker; if it
  does, that is a new claim.

## Evidence

| Command (cwd) | Exit | Result |
|---|---|---|
| `rg -n -i 'agentskills\|skills-ref\|quick_validate\|…'` over sibling corpus/knowledge, SOURCES.md, SKILL.md (fleet root) | 0 | 0 files for agentskills, quick_validate, agent-skills-spec, allowed-tools; skills-ref hits all `/tmp/ue-skills-ref` |
| whole-tree `rg -l` per sibling for `agentskills\.io\|skills-ref\|quick_validate\|agent-skills-spec` | 1 | only game-dev-3d files; `rg … \| grep -v ue-skills-ref` over game-dev-3d is empty |
| `python3 -B fm_census.py` (scratch) | 0 | output sha256 `5afd4b08…`; script `6c85b19a…`; 10 ScannerError, 2 without name |
| copy of HEAD `verify_skill_checklist.py` (sha256 `4ea2100d…`) driven in-process over 18 files | 0 | PyYAML REJECT 10; lane `trigger.frontmatter_parses` PASS 16 / FAIL 2 (lore, souji); `no_xml_tag` PASS 18 |
| PyYAML decode of 3 vendored Epic descriptions | 0 | 1054 / 1005 / 1041 characters; `unreal-mcp` raw minus decoded = 10 (escapes) |
| `git show HEAD:SKILL.md \| wc -l` (lane) | 0 | 528 |
| `sha256sum verifiers/verify_harness_independent.py`; `git show HEAD:… \| sha256sum` | 0 | `2d824c0b…` working copy, `872993f8…` HEAD |
| `ls -la ~/.config/opencode`; `opencode --version` | 0 | 3 JSON files, no skill or skills dir; `1.19.3` |

Pinned sibling `SKILL.md` files (HEAD short, sha256 prefix): game-dev-3d `89dd182b7094` `f52b988a`;
kagi `899c50b42634` `f1c59e55`; kaidoku `fafdd2834327` `cf047307`; kake `22c1669c1fec` `5e3de965`;
kama `147f5bdd3228` `c0acdb29`; kasegi `1fafde8f1145` `f74a9f33`; kumitate `fac39171ac28` `708ebc91`;
mado `e33ea30461f6` `f8f856c5`; tabi `e3cf4e0d30bb` `e39ff315`; tsukuroi `eef0b8e9a6d7` `6aeeaf79`;
lore `380ef3abc7c7` `c1954fbf`; souji `4edb25dfe262` `dc79dad9`. Knowledge sha256: kumitate
`04e6327b…`, kagi `9d4ac8c2…`, kama `c577e615…`.
Web source: https://agentskills.io/specification (HTTP 200, 2026-10-22T08:14:33Z, HTML sha256
`3eb416bb…`). Quotes: §name field "Must match the parent directory name"; §description field
"Must be 1-1024 characters"; §Progressive disclosure "Keep your main SKILL.md under 500 lines.";
§Validation names `skills-ref validate`. No fetched code was executed.

Tooling: no installs; PyYAML 6.0.3 was already present. Peer messages: one fixture pointer each
to C2SkillsRefSource and C2QuickValidateFresh. Writes: this report and scratch files only; no
git or jj write in any repository.
