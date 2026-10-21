verdict: draft entry is placeholder-free and its recheck runs now (2026-10-21, exit 0 for both commands); admission waits on the L1 landing the README row and S012, and on the post-C2 counts listed in §6, which are not in the entry.

# Scoped findings — KnowDescriptionRule (round 47 BUILD)

Lane: leaf member, read-only on production. No production file was edited; no code patch was produced (the draft is prose, so there is no `.patch`). Scratch clone: `/fast/scratch/kotoba-r47/KnowDescriptionRule/lane` (detached at BASE). Artifacts beside this file:

- `KnowDescriptionRule.s001-specification.md` — S001 fetch, 7608 bytes, sha256 `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`
- `KnowDescriptionRule.s002-adding-skills-support.md` — S002 fetch, 20349 bytes, sha256 `79489bd252377681a31958e75ee3e6e96f7f791719eaac3b3e870a0d193be172`
- `KnowDescriptionRule.s003-best-practices.md` — S003 fetch, 42028 bytes, sha256 `727f3fa1168eb1c33ce6a3cbfc94a02ef1dfd647388f6ca9daf7cb6294762f42`
- `KnowDescriptionRule.selftest.txt` — canonical `verify_skill_checklist.py --self-test` output
- `KnowDescriptionRule.checklist.json` — canonical `verify_skill_checklist.py --json` output

## 1. Findings (path:line at BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd)

**F1 — the rule is in Anthropic's doc, absent from the open spec.** S003 states it twice: `name` "Cannot contain XML tags" (S003 markdown line 155) and `description` "Cannot contain XML tags" (line 162), inside the `<Note>` at lines 148–165. S001 has no such rule: the sweep returns 0 for `xml` and 0 for `angle`. SOURCES.md:16 (S003) already says "an Anthropic-only rule the open spec lacks"; the measurement confirms it.

**F2 — the lane states the rule in prose but enforces nothing.** `SKILL.md:151` says "no XML tags (Anthropic rule)" in the portability floor, and `SKILL.md:14` still carries `<skills>` inside the frontmatter `description`. `verifiers/verify_skill_checklist.py` has no tag rule: `grep -n -i xml` matches only the cmark-oracle comments at lines 1551 and 1894, and `check_frontmatter` (line 1176) and `check_literal_trigger` (line 1209) test presence, not content. This is the M13 class in `corpus/lessons/round-46.md` (structural frontmatter gate mistaken for semantic) and is covered by QUALITY.md:19 (Q08).

**F3 — folded YAML: the tag sits on a continuation line.** `SKILL.md:3` is `description: >`; the `<skills>` token is on indented line 14. A column-0 line check misses it: `grep -c '^description:.*<' SKILL.md` → 0, exit 1, while the frontmatter block holds 1 tag (awk over lines 1–16, same command family). The structural parser folds continuation lines with a single space (`verify_skill_checklist.py:513`; `parse_frontmatter` at line 472). For this file the parser value and the PyYAML 6.0.3 value agree (both 814 chars, both contain `<skills>`).

**F4 — structural parse accepts what strict YAML rejects.** Probe (`python3 -B`, parser imported from the canonical verifier; PyYAML 6.0.3 already on the host, not installed by me): `description: Audits. Triggers: "skill file"` as a plain scalar → parser problem `''` (accepted); `yaml.safe_load` → `ScannerError: mapping values are not allowed here`. This is the S002 "technically invalid YAML" case and the S008 §7.3.3 plain-scalar rule. It is a calibration gap, not a SKILL.md defect (the lane's description is `>`-folded). It also constrains C2: `verify_skill_checklist.py` imports only stdlib (lines 253–267), so a `yaml.safe_load` check would add a third-party dependency; the plain-scalar `: ` rule has to be a hand-written check.

**F5 — the checklist verdict depends on the checkout directory name (counterexample to "9 PASS / 1 FAIL").** Canonical root: `--json` → exit 1, `pass 9 / fail 1` (`governance.citation_resolves`, LOG.md:2111). The same script in the scratch clone at directory `lane`: exit 1, `pass 7 / fail 3`, adding `trigger.name_directory` (`name 'kotoba-shokunin' != directory 'lane'`) and `trigger.citation_resolves` (`../.ufo/reports/round-7/kotoba.md` does not resolve from the clone). So the gate's verdict is a function of where the lane sits on disk. C2's fixtures must not inherit this; the recheck in the draft runs from the canonical root.

**F6 — the corpus index will go DRIFT when this entry is admitted.** `before/verify_corpus_integrity.py.out`: `tracked_files: 59` (checker expects 58) and `unindexed_detail: ["corpus/lessons/round-46-verifier-spotcheck.md"]`. Adding `corpus/knowledge/description-xml-tag-rule-round47.md` adds one tracked file and one unindexed path unless the index row lands in the same change (C3 scope). Not fixed here.

**F7 — an honest counterexample to the parser's fold semantics.** A tag split across a fold, `description: >` / `  Audits a <` / `  skills> file.`, folds to `Audits a < skills> file.` in both the parser and YAML: no tag. That is the correct answer if the rule is applied to the value the router ingests (which is the proposed rule, §Draft 2). A raw-line reading would not see a tag either. So fold-split is not a bypass under value semantics; it would be one only under a raw-text rule that counts `<` followed by a name anywhere in the block.

**F8 — sibling sweep (scope of the claim).** `for f in /home/vgpnk/Projects/shokunin/*-shokunin/SKILL.md` frontmatter `<` count: kotoba 1, the other 17 with a SKILL.md → 0 each; 3 of 21 `*-shokunin` directories have no SKILL.md (`audio-shokunin`, `game-dev-2d-shokunin`, `revenger-shokunin`; awk fatal, not counted). So the tag problem is this lane's alone at the time of the sweep (2026-10-21).

## 2. Commands run (exit codes; all at 2026-10-21)

| # | command | exit | key output |
|---|---|---|---|
| 1 | `git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/kotoba-r47/KnowDescriptionRule/lane && git -C …/lane checkout -q --detach c61a973b…` | 0 | HEAD `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| 2 | `python3 -B verifiers/verify_skill_checklist.py --self-test` (canonical, and scratch) | 0 | `0 failure(s) over 1597 assertions` |
| 3 | `python3 -B verifiers/verify_skill_checklist.py --json` (canonical) | 1 | pass 9 / fail 1; `governance.citation_resolves` LOG.md:2111 |
| 4 | same, scratch clone at `lane/` | 1 | pass 7 / fail 3 (F5) |
| 5 | `curl -sSL …/agent-skills/best-practices.md -o …` | 0 | HTTP 200, 42028 bytes, sha256 `727f3fa1…` |
| 6 | `grep -c -i 'cannot contain xml tags' KnowDescriptionRule.s003-best-practices.md` | 0 | 2 (lines 155, 162) |
| 7 | `curl -sSL https://agentskills.io/specification.md \| grep -c -i 'xml'` | 1 | 0 (grep exits 1 on zero matches; see §4) |
| 8 | `… \| grep -c -i 'angle'` on the same fetch | 1 | 0 |
| 9 | `grep -c '<' KnowDescriptionRule.s001-specification.md` | 0 | 1, and that is line 234 `\< 5000 tokens` (a Markdown escape, not a tag) |
| 10 | `curl … adding-skills-support.md` | 0 | HTTP 200, 20349 bytes, sha256 `79489bd2…`; `<` hits only at lines 51–53 (path placeholders) and 170–181 (`<available_skills>` catalogue example) |
| 11 | `grep -c '^description:.*<' SKILL.md` | 1 | 0 |
| 12 | `awk` frontmatter `<` count, `SKILL.md` (lines 1–16) | 0 | 1 |
| 13 | `grep -c '<skills>' SKILL.md` | 0 | 8 (whole file: lines 14, 22, 91, 96, 99, 111, 151, 430 — only 14 is in the frontmatter) |
| 14 | `grep -n -i xml verifiers/verify_skill_checklist.py` | 0 | 1551, 1894 only (cmark oracle comments) |
| 15 | `grep -rn -i 'xml\|angle' verifiers/fixtures/checklist/*/SKILL.md` | 1 | no lines (no fixture exercises a tag or the rule) |
| 16 | `ls corpus/knowledge/*.md \| wc -l` | 0 | 34 |
| 17 | `grep -lE '^[[:space:]]*source:' corpus/knowledge/*.md \| wc -l` | 0 | 2 |
| 18 | `sha256sum verifiers/verify_skill_checklist.py SKILL.md corpus/SOURCES.md corpus/QUALITY.md` | 0 | `214ae44d…`, `c8b245b7…`, `ef331658…`, `40a0cc34…` (pins for C2's diff) |
| 19 | parser-vs-YAML probe, six cases (F4, F7, §Draft 2) | 0 | see §3 |
| 20 | `curl -sSL …best-practices.md \| grep -c -i 'cannot contain xml tags'` (verbatim recheck, §Draft) | 0 | 2 |

## 3. Probe table (parser = `verify_skill_checklist.parse_frontmatter`; yaml = PyYAML 6.0.3 `safe_load`)

| case | parser problem | parser tag hits (`</?[A-Za-z][A-Za-z0-9_:.-]*(?:\s[^<>]*)?/?>`) | yaml value |
|---|---|---|---|
| planted `Audits. <skills> tail` (folded) | none | `<skills>` | same |
| `See <https://agentskills.io/specification> for rules.` (autolink) | none | none | same |
| `Fires when a < b and c > d.` (comparison) | none | none | same |
| `Audits a <` / `skills> file.` (fold-split) | none | none | `a < skills> file.` |
| `"Audits <skills> files."` (quoted) | none | `<skills>` | same |
| `Audits. Triggers: "skill file"` (plain, colon-space) | none (accepted) | none | `ScannerError` |

## 4. Negative claims and their sweeps

- "The open spec has no XML-tag rule": `curl … specification.md | grep -c -i 'xml'` → 0 and `grep -c -i 'angle'` → 0 (commands 7–8, 2026-10-21, 7608 bytes).
- "No lane checker enforces a tag rule": `grep -n -i xml verifiers/verify_skill_checklist.py` → only 1551/1894 (command 14); no `def` named for tags in the 2248-line file.
- "No other fleet SKILL.md carries a tag in frontmatter": the sibling sweep (F8).
- "No fixture exercises the rule": command 15.
- Caution for recheck authors: `grep -c` prints 0 and exits 1 on a zero count. A `recheck:` that expects 0 must test the output, not the exit (QUALITY Q04).

## 5. Draft entry — `corpus/knowledge/description-xml-tag-rule-round47.md` (NOT in corpus/; L1 admits)

```markdown
source: Claude Docs — Agent Skills best practices, § Skill structure (`<Note>` block) — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices (S003, tier A; markdown alternate lines 148–165); the open spec is S001 (https://agentskills.io/specification, § `description` field), contrast only; the own-work facts (tag pattern, sibling sweep, fold-split probe) are S012 (kotoba own work, tier C, mined)
verified-at: 2026-10-21 (S003 re-opened today; the S003 row's `opened` cell still reads 2026-10-19 until L1 updates it)
recheck: curl -sSL https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md | grep -c -i 'cannot contain xml tags' — expect 2 (2 — same command 2026-10-21); and `python3 -B verifiers/verify_skill_checklist.py --self-test` from the canonical root — expect exit 0 and a final line `0 failure(s) over N assertions` (N = 1597 at BASE, 2026-10-21)
```

### Fact 1 — the rule is Anthropic's, not the open spec's

- S003 bans XML tags in `name` and `description` (`corpus/SOURCES.md:16`; S003 markdown lines 155, 162; 2 — `grep -c -i 'cannot contain xml tags'`, 2026-10-21). S003 never defines "XML tag": of its 12 `xml` hits, 8 are OOXML/XML-file prose (lines 370, 373, 376, 559, 560, 563, 566, 737) and 2 are restated limits (1133–1134). The pattern in Fact 2 is therefore a lane decision, not a vendor definition.
- The open spec has no such rule (0 `xml`, 0 `angle` — S001 sweep, 2026-10-21; `corpus/SOURCES.md:14`). Vendor-only scope: `corpus/SOURCES.md:30`; the lane's own floor is `SKILL.md:151`; the checker gap is `corpus/QUALITY.md:19` (Q08).
- [INFERENCE] the reason is that a tagged catalogue entry nests the description (catalogue example in S002 lines 170–181; row `corpus/SOURCES.md:15`). No document states it.

### Fact 2 — what counts as a tag

Decision: the rule is applied to the **parsed description value** (the string a router ingests), with the tag-shaped pattern `</?[A-Za-z][A-Za-z0-9_:.-]*(?:\s[^<>]*)?/?>`.

- Counted: `<skills>`, `</x>`, `<br/>`, `<a href="x">`, and a tag inside quotes (`"Audits <skills> files."`).
- Not counted (must stay green — a false red is harm, QUALITY Q18): `a < b and c > d`; `<https://agentskills.io/specification>` (autolink; the `/` breaks the name class); `\<` (Markdown escape); `<!-- … -->` and `<?xml …?>` (not element tags — a stricter reading would count them and needs its own decision).
- A tag split across a folded line break (`a <` / `skills> file.`) folds to `a < skills>` and is not counted under value semantics (measured 2026-10-21).

### Fact 3 — folded YAML and structural parsing

The mechanics are already recorded; this entry cites them rather than restating:

- Folded `>` scalars fold continuation lines and put the tag off column 0; a column-0 check is blind to it. The fold-to-single-space rule and the measured 814-character agreement with PyYAML 6.0.3 (2026-10-21) are in `corpus/knowledge/sibling-description-rewrites-round8.md:104–110` and `corpus/knowledge/checklist-execution-round15.md:259–261`.
- A structural parse accepts plain scalars with `: ` that a strict loader rejects (`ScannerError`, measured 2026-10-21); the stdlib-only limit is `checklist-execution-round15.md:259–261`, and the loader-held-value consequence is `corpus/knowledge/harness-verifier-round10.md:84–92`.
- Fold-split (`a <` / `skills> file.`) folds to `a < skills>` in both parser and YAML and is not a tag under value semantics (measured 2026-10-21).

### Fact 4 — this lane's measured state

| measure | value at BASE | command, date |
|---|---|---|
| tag in frontmatter `description` | 1 (`SKILL.md:14`) | `awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f' SKILL.md \| grep -c '<'`, 2026-10-21 |
| checklist self-test | `0 failure(s) over 1597 assertions` | `python3 -B verifiers/verify_skill_checklist.py --self-test` — exit 0, 2026-10-21 |
| checklist `--json` | 9 PASS / 1 FAIL (`governance.citation_resolves`, `LOG.md:2111`) | `python3 -B verifiers/verify_skill_checklist.py --json` — exit 1, 2026-10-21 |
| sibling `*-shokunin` frontmatter tags | 1 of 18 SKILL.md (kotoba); 17 at 0 | the sibling `awk` sweep, 2026-10-21 (3 of 21 directories have no SKILL.md) |
| checker tag rule | absent at BASE (0 matches for a tag check in `verify_skill_checklist.py`) | `grep -n -i xml verifiers/verify_skill_checklist.py` → 1551, 1894 only, 2026-10-21 |

### Limits

- Anthropic's runtime enforcement is not observed here: no upload, no Claude surface. The entry states what the doc says.
- The checkout-directory dependence of the lane's own gate (scratch `lane/` → 7/3) is a separate defect and is not fixed by this entry.
- Verified at 2026-10-21 only; S003 has no version field, so the recheck is the freshness signal.

## 6. Placeholders for L1 (filled from C2's landed run, nothing else)

- `<C2-FM-TAG-COUNT>` — frontmatter tag count after C2 removes `<skills>` from `SKILL.md:14`; expected 0.
- `<C2-SELFTEST-ASSERTIONS>` — the self-test assertion count after the planted-tag fixtures land.
- `<C2-CHECKLIST-PASS>` / `<C2-CHECKLIST-FAIL>` — `--json` counts after C2. C2 alone adds one check (11 total: 10 PASS / 1 FAIL until C3 registers the erratum); C2 + C3 is the plan target 11 / 0 — fill from the run, do not assume.

Every other number above is measured in §2 and carries its command and date.

## 7. What I did NOT check

- Anthropic's loader behaviour with a tagged description (no live Claude/omp session; the instruction was not to launch omp sessions).
- The Anthropic "Skills overview" page that S003 links to; not opened, so no claim about it.
- The `skills-ref` validator named in S001 § Validation; not installed or run (no tool install was needed for this lane).
- The C2 diff and the C3 erratum registry; both are other lanes' artifacts and I did not edit or run them.
- Whether the 3 siblings without `SKILL.md` have a skill under another filename.
- The `corpus/knowledge/harness-*` files for any statement about how omp or opencode render descriptions; I cite only what §Fact 1 measures, and I did not re-derive the render claims.
- Tool installs: none. PyYAML 6.0.3 was already on the host and was used only for the probe in §3.

## 8. Revision after CritExpansionClaim review (proposed rows; production untouched)

Accepted: (a) expansion needs a coverage-map row; (b) own-work facts need a mined own-work S row; (c) S003 does not define "XML tag", so the Fact 2 pattern is a lane decision; (d) Fact 1 and the fold/parse points now cite `SOURCES.md:16/:30`, `SKILL.md:151`, `QUALITY.md:19`, `checklist-execution-round15.md:259–261`, `sibling-description-rewrites-round8.md:104–110`, `harness-verifier-round10.md:84–92` instead of restating them. I am read-only on `corpus/`, so the two rows below are drafts for L1 to land. S010 (`corpus/SOURCES.md:23`) is not edited here; C2 makes its "no XML-tag rule" clause stale and L1 decides its status change.

**Proposed `corpus/README.md` coverage row** (insert after the `Frontmatter trigger surfaces` row, README line 9):

```
| Description XML-tag rule (round 47) | `knowledge/description-xml-tag-rule-round47.md` | S003 vendor-only rule vs open spec (S001); tag pattern is a lane decision (S003 does not define "XML tag"); counts from `verify_skill_checklist.py --self-test` and the frontmatter sweep, 2026-10-21; C2 fills the post-landing counts |
```

**Proposed own-work S row** (new id `S012`, tier C, own-work; SOURCES row format per `corpus/SOURCES.md:12`):

```
| S012 | kotoba own work — the description tag pattern, the 1/18 sibling sweep and the fold-split probe, 2026-10-21 | own-work | C | Lane decision on what counts as a description tag, and the observed sibling spread | Tag-shaped regex `</?[A-Za-z][A-Za-z0-9_:.-]*(?:\s[^<>]*)?/?>` on the parsed value; sweep `awk` frontmatter `<` count → kotoba 1, 17 siblings 0 (18 SKILL.md of 21 dirs); fold-split `a <`/`skills> file.` → `a < skills>`, no tag | mined | 2026-10-21 | on-commit | description-xml-tag-rule-round47.md |
```

Reply to the review: S012 is tier C and status `mined` with used-by naming the entry, per the review. Its tier is C because the pattern is a lane decision, not an external source; the probe results are the only evidence behind it.
