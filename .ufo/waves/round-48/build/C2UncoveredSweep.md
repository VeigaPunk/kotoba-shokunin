# C2UncoveredSweep — critic, claim C2 (round 48, attempt 2)

Seat: `KotobaR48.C2UncoveredSweep`, read-only critic. Lane base `75f671b109d8eddd0d64c1429bd6379fe577175a`.
Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2UncoveredSweep/`. Tools installed or updated: none.

## Findings

1. **The counter is right: 34 before, 35 after if exactly one entry lands.** `git ls-tree` at
   `75f671b` prints 34 (exit 0). The directory holds 35 files, but the 35th is the JSON
   companion `sibling-citation-routing-round16.json`. This matches the round-47 spot-check:
   "35 tracked knowledge files include one JSON routing record".
2. **The ground is uncovered in `corpus/knowledge/` and in the coverage map, but it is not
   empty in the lane. The plan's sweep is too narrow to show that.** The plan searched only for
   source names (`agentskills|skills-ref`). A search on rule content finds an existing merged
   rule list at `SKILL.md:151`, the "Portability floor". It already says which rule comes from
   which authority: S001/S002/S003/S008 are cited, `name` ≤64 lowercase-hyphen chars equal to
   the directory, `description` ≤1024 chars, "no XML tags (Anthropic rule)", the YAML `: ` and
   ` #` quoting rule, `trigger.no_xml_tag` gating `name` and `description`, and "Anthropic's
   reference packager (S012) is stricter and refuses any `<`/`>`". The checker's own detail
   string (`verify_skill_checklist.py:1306-1307`) says the same. None of the 34 knowledge
   entries carries this, and no README coverage-map row holds per-authority validity:
   `corpus/README.md:9` covers trigger craft, and `:77` covers loader-rule freshness.
   **Counterexample:** an entry that tabulates the `SKILL.md:151` sentences plus the SOURCES
   "teaches" cells would pass the 34 to 35 counter while adding no knowledge. That is filler
   which relocates existing claims, like the round-15 craft-rule move.
3. **Genuinely uncovered rules exist. I opened them this session, and they are absent from
   every swept file:**
   - Anthropic's reserved words on `name`. The grep `reserved word|"claude"|"anthropic"`
     returned 0 hits. S003 says: "Cannot contain reserved words: "anthropic", "claude"".
   - skills-ref's closed field set. The grep `allowed-tools` returned 0 hits. The
     `ALLOWED_FIELDS` set holds 6 keys: name, description, license, allowed-tools, metadata
     and compatibility.
   - skills-ref name rules: NFKC normalisation, Unicode `isalnum`, no leading or trailing
     hyphen, and no `--`. The grep `unicode|NFKC|non-ascii` returned 0 hits, and
     `SKILL.md:151` says only "lowercase-hyphen".
   - **A cross-authority disagreement, from a transcription of the predicate (not the packaged
     validator):** `claude-tools`, `résumé` and `名前` all pass skills-ref's name rules, but
     `claude-tools` breaks S003's reserved words. Fullwidth `ｓｋｉｌｌ` is normalised to
     `skill` and accepted. Only `a--b` is rejected.
4. **Axis mismatch (a tradeoff for the judge, not a fixable defect).** AXES.md:14 defines
   freshness as "skill claims re-verified against live surfaces; stale items flagged or fixed".
   AXES.md:21 maps new entries to expansion (coverage + adjacency), and LEARNING.md:33 makes
   "admitted `knowledge/` entries on ground the coverage map did not hold" the expansion
   observable. The 34 to 35 number is an expansion count. It is not freshness evidence.
   Scored alone, it is premature saturation of the freshness claim.
5. **Q12 is unmet by 32 of the 34 entries, so they are not a precedent.** Only
   `harness-independent-round41-census.md` and `sibling-citation-routing-round16.md` open with
   `source:`, `verified-at:` and `recheck:`. The new entry MUST follow those two and MUST NOT
   copy the house style of the other 32.

## What the entry must contain to count as admitted knowledge

- **Q12:** The first three lines are `source:`, `verified-at:` and `recheck:`. `source:` names
  every external S### row plus its URL and anchor, at least one row opened this round (for
  example skills-ref pinned to a commit, as the plan's C2 line and round-prompt step 4
  require). The `recheck:` command must run today (Q04), for example the lane checker over the
  counterexample fixtures, plus the `ls-tree` count.
- **Q13:** Every number is written as `<number> — <command> <date>`. That covers the 64, 1024,
  6 allowed fields, the per-authority rule count and the 34/35 counter.
- **Q14:** Every absence claim (for example "S001 has no XML rule", "lane checker does not
  check reserved words", "no prior knowledge entry covers this") pastes its sweep command and
  hit count. The sweep below can be reused.
- **LEARNING.md expansion bar:** the ground must be absent from the coverage map, and the entry
  must add a README coverage-map row. Under CORPUS.md, an index row is a claim, so write the
  row only after the file lands. `source:` must cite a row marked `mined`.
- **Learning-claim bar (falsifiable, located, not opinion):** a per-rule × per-authority matrix
  with these columns:
  - spec (S001)
  - skills-ref (new row, pinned commit)
  - Anthropic docs (S003)
  - `quick_validate.py` (S012)
  - Codex (S013, versioned semantics)
  - what `trigger.no_xml_tag` actually executes

  Each cell is a located quote or `file:line`. The routed counterexamples (YAML alias, Unicode
  name, escaped value) must be observed by running the lane checker, with exit codes. At least
  one cell must be a disagreement that `SKILL.md:151` does not state (finding 3).
- **It is filler if:** it restates `SKILL.md:151` and the SOURCES teaches cells; it cites only
  rows from round 46 or 47; its counterexamples are argued instead of run; it claims universal
  validator coverage (spot-check item 3 forbids that); or the README row lands before the file.

## Smallest safe corrections

- In the plan's C2 sweep, add the rule-content grep. Name `SKILL.md:151` as existing coverage
  that the entry supersedes or points to. That follows "one authoritative home per fact"
  (`SKILL.md:173`), so `SKILL.md:151` becomes a pointer and the matrix does not become a second
  authority.
- Keep 34 to 35 as the expansion count. Give C2 a freshness observable as well: "N of M
  `SKILL.md:151` clauses re-verified against a live authority opened this round, K flagged
  stale". Alternatively, re-declare C2's axis. Either way, the judge sees the mismatch.

## Evidence

Grep sweep, set `T="corpus/knowledge/*.md SKILL.md corpus/README.md"`, `rg -c -i -e <p> $T`
(all exit 0). Hits are summed lines, and files are the files that matched:

| pattern | hits | files | substantive location |
|---|---|---|---|
| `agentskills` | 0 | 0 | — |
| `skills-ref` | 0 | 0 | — |
| `quick_validate` | 0 | 0 | — |
| `allowed-tools` | 0 | 0 | — |
| `reserved word\|"claude"\|"anthropic"` (and more) | 0 | 0 | — |
| `unicode\|NFKC\|non-ascii` | 0 | 0 | — |
| `no_xml_tag` | 3 | 2 | SKILL.md:123,151; README:77 |
| `S001\|S003\|S012\|S013` | 3 | 2 | SKILL.md:151; README:63,64 (lesson index) |
| `64 char\|≤ ?64` (and more) | 1 | 1 | SKILL.md:151 |
| `1024\|1,024` | 2 | 2 | SKILL.md:151; render-mechanism-round7:24 (maxTokens, unrelated) |
| `hyphen-case\|kebab\|lowercase` | 3 | 3 | SKILL.md:151 only substantive |
| `XML tag\|angle bracket` (and more) | 2 | 2 | SKILL.md:151; harness-system-prompt:28 (anti-injection, unrelated) |
| `validator\|validate` | 12 | 11 | none per-authority |
| `authorit` | 13 | 11 | none per-authority |
| `frontmatter` | 85 | 19 | trigger craft and render; validity only at SKILL.md:151 |
| `yaml alias\|alias\|anchor` | 87 | 18 | all "anchor" as a citation anchor; narrowed YAML-alias grep returned 0 |
| `escape\|escaped` | 47 | 12 | harness-verifier-round10:165 (scalar forms), not a per-authority rule |

- The plan's own sweep, reproduced: `rg -i -c 'agentskills|skills-ref' corpus/ SKILL.md README.md`
  (exit 0) hits only `lessons/round-46.md` (2), `round-47.md` (1),
  `round-47-verifier-spotcheck.md` (1) and `SOURCES.md` (3). That confirms the plan's claim, and
  it also shows the claim is a source-name sweep, not a rule sweep.
- The count: `git -C <lane> ls-tree -r --name-only 75f671b corpus/knowledge | grep -c '\.md$'`
  printed `34`, exit 0. HEAD = master = `75f671b109d8…`. `ls corpus/knowledge | wc -l` printed
  35, and the extra file is the `.json`.
- Provenance-trio scan: `head -5 <f> | rg -c '^(source|verified-at|recheck):'` gives a value of
  3 for 2 files and 0 for the other 32.
- `trigger.no_xml_tag` (`verifiers/verify_skill_checklist.py:404-409,1294-1313`): it searches
  only parsed `name` and `description`, and the tag name must start with `[A-Za-z_]`. Unicode
  tag names (`<名>`) therefore fall outside `XML_TAG_RE` [INFERENCE from the regex; not run]. It
  catches YAML escapes `\x3c`, `\u003c` and `\U0000003c`, and has no reserved-word or field-set
  check.
- Lane `SKILL.md` frontmatter keys: `name` and `description` only (awk/rg, exit 0). Both are
  inside skills-ref's allowed set.
- Web source 1, skills-ref:
  - Fetched with `curl` on 2026-10-22T08:12:09Z, HTTP 200, from
    https://raw.githubusercontent.com/agentskills/agentskills/main/skills-ref/src/skills_ref/validator.py
    with sha256 `b5ee3d85…f6c5`.
  - The last commit touching the path is `547831f3a23724ba64a9b79bbf59c5e0bc8f2d1a`
    (2025-12-18, GitHub API).
  - Quote at lines 37 and 54: `name = unicodedata.normalize("NFKC", name.strip())`; and
    `if not all(c.isalnum() or c == "-" for c in name):`.
  - Not executed.
- Web source 2, Claude docs:
  - Fetched with `curl` on 2026-10-22T08:12:09Z, HTTP 200, from
    https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md, the
  `name:` field list, lines 153-156.
  - Quote: "Maximum 64 characters / Must contain only lowercase letters, numbers, and hyphens /
    Cannot contain XML tags / Cannot contain reserved words".
- Predicate probe: a `python3` heredoc transcribing skills-ref lines 37-57, run in scratch,
  exit 0. `résumé`, `名前`, `ｓｋｉｌｌ` (normalised to `skill`) and `claude-tools` pass;
  `a--b` is rejected. This is a transcription, not the packaged validator. The entry should
  rerun it with `skills-ref validate` if it cites this.
- Not run: the lane checker on the alias, Unicode and escaped fixtures (that belongs to the
  entry's author), and `skills-ref` itself.
