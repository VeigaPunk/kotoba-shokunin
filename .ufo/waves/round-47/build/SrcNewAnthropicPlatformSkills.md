verdict: Draft S012 admits the Anthropic Skills API guide as docs/A for the no-XML-tag rule as a documented upload requirement, but the stronger claim "upload/API validation rejects a tagged description" is stated by none of the 30 platform skill pages swept nor the API error catalogue — C2 may cite the rule, not the rejection.

# SrcNewAnthropicPlatformSkills — round-47 build scout

**Assignment:** candidate NEW `corpus/SOURCES.md` row for the Anthropic platform skills
API/overview docs; assess whether upload/API validation enforces the `description`
no-XML-tag rule (C2's strongest source). **BASE:** `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.
**Outcome:** admit `S012` (`docs`, tier `A`, `queued`) for the *upload requirement*; record the
*enforcement* claim as not stated, with the sweep in §4. No production file was edited.

## 1. Source identity and fetch evidence

Primary page: **Using Agent Skills with the API** (the Skills API guide).
Requested `https://platform.claude.com/docs/en/build-with-claude/skills-guide.md`; the server's
`x-middleware-rewrite: /docs/as-markdown/en/build-with-claude/skills-guide` confirms this is the
docs site's own markdown reader text, not a scraped render. The legacy link printed in
`code.claude.com/docs/en/skills.md:425` (`https://docs.claude.com/en/api/skills-guide`) redirects
301 → 307 to this page (checked 2026-10-21T15:58:27Z).

| field | value |
|---|---|
| URL fetched | `https://platform.claude.com/docs/en/build-with-claude/skills-guide.md` |
| final URL | same (no redirect) |
| HTTP status | `200` |
| content type / bytes | `text/markdown; charset=utf-8` / `144610` |
| accessed (UTC) | `2026-10-21T15:58:21Z` |
| sha256 of fetched bytes | `76a440b2aff54e1b1a6e0c0ed4102437da4c7a759c00290f4d81e97acadbbe7f` |
| stability | first fetch `15:54:32Z` (batch start), refetch `15:58:21Z`: byte-identical (`cmp` exit 0); same sha both times |
| revision | no page-level `dateModified`/"Last updated" in the markdown or the HTML shell; `cache-control: no-store`; the sha256 is the revision identity this row pins |
| anchor | § Managing custom Skills → `### Creating a Skill` (line 1965) → `**Requirements:**` (line 2258) → `* YAML frontmatter requirements:` (line 2266), `description` bullet at line 2269; repeated at § Limits and constraints → `### Request limits` (lines 3547–3558) |
| quote (8 words) | "`description`: Maximum 1024 characters, non-empty, no XML tags" |
| quote location | `skills-guide.md` line 2269, under the Requirements list that follows the `POST /v1/skills` examples; identical text at line 3558 under Limits and constraints → Request limits |

The page's own text calls these "the **Requirements** list following the examples for the full
constraints" (line 1967), which is what makes this an *upload* precondition rather than generic
authoring advice. The page does **not** say the service rejects a non-compliant description, does
not name an error string, and does not define what counts as an XML tag.

## 2. Draft `corpus/SOURCES.md` row

Insert after `S011` (`corpus/SOURCES.md:24`); at BASE it becomes line 25, before `## Paths`
(`corpus/SOURCES.md:26`). Contract shape: 11 populated cells, no `|` inside any cell.

```markdown
| S012 | Using Agent Skills with the API — https://platform.claude.com/docs/en/build-with-claude/skills-guide | docs | A | Skills API upload requirements for SKILL.md YAML frontmatter (`name`, `description`) | § Managing custom Skills → Creating a Skill → **Requirements** → YAML frontmatter requirements (lines 2258–2269); § Limits and constraints → Request limits (lines 3549–3558); no page date; revision = fetched markdown sha256 76a440b2… (2026-10-21) | The Skills API lists "no XML tags" for `description` and `name` among upload requirements — a documented precondition; no rejection behavior or tag grammar is stated | queued | 2026-10-21 | 90d | — |
```

Field notes:

- **kind `docs`, tier `A`:** official Anthropic API documentation, authoritative for the
  *documented upload requirements* scope. `community` is not involved, so the never-A rule is
  not in play.
- **Not redundant with S003** (`corpus/SOURCES.md:16`): S003 is the *authoring* page
  (`best-practices`) and grounds the rule as an Anthropic authoring convention; S012 is the
  *API surface* page and grounds it as a requirement of `POST /v1/skills`. Different scope,
  different claim strength.
- **status `queued`, used-by `—`:** nothing cites it at BASE. If C2 lands and
  `SKILL.md:151`'s portability-floor citation is extended to `S012`, contract rule 2 flips
  `status` to `mined` and `used-by` to `SKILL.md`, logged old→new in the round lesson. That
  flip is the integrator's call, not this seat's.
- **recheck `90d`:** live third-party docs; a sha change is the only reliable revision signal
  (no page date).

## 3. Gate record for the round-47 lesson `## Gate` § Sources

Row for the same table shape used in `corpus/lessons/round-46.md:61-73`:

```markdown
| S012 | https://platform.claude.com/docs/en/build-with-claude/skills-guide.md | 2026-10-21T15:58:21Z | `76a440b2aff54e1b…` | "`description`: Maximum 1024 characters, non-empty, no XML tags" | § Creating a Skill → Requirements → YAML frontmatter requirements (line 2269); repeated § Request limits (line 3558) |
```

Gate prose to carry with it:

> **Sources.** Considered: the 30 Skill-related pages listed in
> `https://platform.claude.com/llms.txt` (sha256 `3f8ed26a…`), all fetched 2026-10-21.
> Admitted: 1 row (`S012`, docs/A/queued) for the Skills API upload requirement. Rejected
> rows: 0. Rejected **claim**: "upload/API validation rejects a description containing an XML
> tag" — not stated by any of the 30 pages (sweep in §4); the only primary statement tying
> the rule to upload is the requirement bullet. Quote re-open: `grep -n -F` on the literal
> `description`: Maximum 1024 characters, non-empty, no XML tags — exactly the two lines
> cited.
>
> **Existing-record correction (append-only, no round-46 edit).** `corpus/lessons/round-46.md:65`
> and `.ufo/round-46/evidence/w2/sources/fetch-log.json:29` map S003's quote to
> "description rules (line 155; name repeats at 162)". At the pinned sha
> `727f3fa1168eb1c3…` the mapping is the reverse: line 155 is the fourth `name` bullet,
> line 162 is the fourth `description` bullet (`sed -n '145,168p'`). The rule holds for both
> fields, so no S003 verdict changes; record the corrected location in the round-47 gate rather
> than rewriting the round-46 record.

## 4. Does the source say upload/API validation enforces the rule?

| claim | verdict | evidence |
|---|---|---|
| `description` cannot contain XML tags (authoring) | **SUPPORTED** | `best-practices.md` S003, line 162; `overview.md` line 223; `skills-guide.md` lines 2269 and 3558 |
| The no-XML-tag rule is a Skills API **upload requirement** | **SUPPORTED** | `skills-guide.md` lines 2258–2269 (Requirements under Creating a Skill, after `POST /v1/skills` examples); repeated lines 3549–3558 |
| Upload/API **validation rejects** a tagged description, or returns an XML-tag error | **NOT STATED** | 30-page sweep below: 0 pages say "upload fails" for tags, 0 pages pair 400/error with frontmatter or XML, 1 page says "validation rules" about the authoring fields (rules, not server behavior) |

Cross-checked pages: the overview
`https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md` (HTTP 200, sha
`d4ee7be3d5500100…`, § Skill structure line 223) and S003
`https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md` (HTTP 200,
sha `727f3fa1168eb1c3…`, line 162) both repeat the rule; neither states enforcement.

What the page actually says about failure is generic: "A request that fails because of a Skill
problem returns HTTP 400. The `error.message` field … describes the problem"
(`skills-guide.md:4274`, § Error handling). It never says an XML tag is such a problem. The
`POST /v1/skills` reference lists only `files` and `display_name` body parameters
(`api/skills/create.md`, fetched sha `c066aba9…`) and enumerates no frontmatter validation or
error.

### Negative-claim sweep

- Population: every Skill-related URL in `https://platform.claude.com/llms.txt`
  (sha256 `3f8ed26a0694f917e5ed5bba6e3f48b439774aa850eb1947652c9dcff24fcf04`);
  `grep -o 'https://platform\.claude\.com/docs/en/[^)]*\.md' llms.txt | grep -i skill | sort -u`
  → **30** URLs; all 30 returned HTTP 200 (see `SrcNewAnthropicPlatformSkills.json`
  `sweep.pages` for per-page status and sha256).
- `grep -l -i 'xml tag' *.md | wc -l` → **3** pages: `best-practices`, `overview`,
  `skills-guide`.
- `grep -n -i 'xml tag' *.md` → **10** lines, every one a field-requirement bullet
  (`name` ×3 pages, `description` ×3 pages, best-practices repeats both in § YAML frontmatter
  requirements at lines 1133–1134). No prose about upload behavior.
- `grep -i -c 'upload fail' *.md | awk …` → **0**.
- `grep -i 'validat' *.md | grep -i -c 'frontmatter'` → **1**: `best-practices.md:1131`
  "fields with specific validation rules" — describes the authoring rules, not a server
  validator.
- `grep -n -i 'reject' *.md` → **2** lines, both in the analytics API docs
  (`api/beta/organization/analytics/skills*`) about unsupported `filter[]` products, unrelated
  to SKILL.md validation.
- No page pairs `400` with `frontmatter` or `xml` (0 lines), and `grep -i 'error' | grep -i
  -c` gives **0** for `frontmatter` and **0** for `xml tag`.
- ±2-line context around each of the 10 XML-tag lines, regex
  `error|reject|fail|invalid|400|not allowed|must not`: **0/10** hits (script exit 0). The
  requirement bullets are not adjacent to any failure language.
- Broadened terms `invalid|refused|denied|not allowed|must not|hard error|fails` near
  `frontmatter|description|xml tag`: the only hit is "invalidate the cached prefix"
  (`skills-guide.md:4266`, prompt caching), unrelated to upload validation.

**Conclusion:** the primary docs establish the rule as a *documented upload requirement* and
stop there. An enforcement claim would need a different source. A web search surfaced
third-party issue reports (`anthropics/claude-code#80469`, `vercel-labs/agent-skills#214`) that
quote an error like "description cannot contain XML tag"; those are community-tier leads, were
**not opened** this round, and are not evidence in this report.

**Rejected claim (not a row).** `REJECTED: the page lists "no XML tags" as a frontmatter
requirement but never states that upload/API validation rejects a tagged description, and no
platform skill page or API error catalogue adds that behavior; flip: an Anthropic primary page
or the API error catalogue states the rejection or an error message for a tagged description.`
Not written as a `rejected` SOURCES row because the same page is admitted for the narrower true
claim; a second row with the same URL would obscure that the source does teach something. The
sweep above is the required support for this absence.

Cross-check, not a row: `code.claude.com/docs/en/skills.md:425` says the Agent Skills spec and
"the Skills API requirements define everything else those paths validate", and `:419` says
packaging/upload fails hard for *unexpected frontmatter keys*. That is generic validation
language, not XML-tag-specific, and the page links to the same skills guide. The platform API
error catalogue (`https://platform.claude.com/docs/en/api/errors.md`, HTTP 200, sha
`b67a0f8df4340e6a…`, 33306 bytes) has **0** lines containing `xml` or `skill` — no error code
or message there either.

## 5. Relevance to C2 (operability)

1. **Citation:** C2 can cite S003 (authoring rule) **plus** S012 (API upload requirement). Do
   not write "the API rejects" or "upload validation enforces" on this source; the strongest
   supported wording is "a documented requirement for uploads through the Skills API".
2. **Tag grammar is undefined.** The docs say "no XML tags" but give no grammar and no
   examples. The verifier must state its model. A tag-shaped `<skills>` must fail; a bare
   `a < b` is not tag-shaped (no closing `>`) and the docs do not call it one. If the check
   flags *any* angle bracket, label that as a stricter reading than the documented rule (or
   cite the community error reports as tier C, which this round did not open).
3. **Scope of the value:** the page constrains the frontmatter `name` and `description` values
   and states no body restriction. The check should read the parsed description value, which
   is what `verifiers/verify_skill_checklist.py:1176` `check_frontmatter` already does; a
   raw-file grep would false-positive on body XML. `[INFERENCE]` that body XML is permitted —
   the page is silent, not permissive.
4. **Current lane state at BASE:** `verifiers/verify_skill_checklist.py` has no XML/tag check
   (`grep -n -i 'xml'` hits only the cmark-oracle comments at lines 1551 and 1894);
   `SKILL.md:14` carries `<skills>` inside the description; `SKILL.md:151` already states the
   rule and names this repair. S012 strengthens that sentence's provenance without changing
   the planned check.

## 6. Counterexamples and defects found

1. **S003 location swap (existing record, append-only).**
   `corpus/lessons/round-46.md:65` says "description rules (claude-bp.md line 155; name field
   repeats it line 162)"; at the pinned sha `727f3fa1…`, line 155 is the `name` bullet and
   line 162 is the `description` bullet. The same swap is in
   `.ufo/round-46/evidence/w2/sources/fetch-log.json:29`. The rule holds for both fields, so
   no verdict changes; this is a location-attribution defect, not a rule defect. Do not edit
   the round-46 record — log the correction in round-47's gate.
2. **No revision date.** Neither the markdown nor the HTML shell exposes `dateModified` or
   "Last updated"; a recheck must compare the sha256, not a date. The row's anchor records the
   fetched sha for exactly this reason.
3. **"No XML tags" ≠ "no angle brackets".** The docs never define a tag. A verifier that
   rejects `a < b` is not enforcing the literal documented rule; if that is intended, say so
   and ground it in a different (community) source, or choose a tag-shaped regex and document
   the choice.
4. **Requirement vs validation.** The Requirements section is a precondition list, not an
   error catalogue. Reading it as proof of server rejection is an inference, not a quote.

## 7. Commands run (all exit 0 unless noted)

```text
$ curl -sS -L --max-time 40 -o final-skills-guide.md -w 'http=%{http_code} final=%{url_effective} size=%{size_download} ct=%{content_type}\n' \
    https://platform.claude.com/docs/en/build-with-claude/skills-guide.md
http=200 final=https://platform.claude.com/docs/en/build-with-claude/skills-guide.md size=144610 ct=text/markdown; charset=utf-8

$ sha256sum final-skills-guide.md
76a440b2aff54e1b1a6e0c0ed4102437da4c7a759c00290f4d81e97acadbbe7f  final-skills-guide.md

$ cmp -s final-skills-guide.md bb8839a8.md && echo IDENTICAL_TO_FIRST_FETCH
IDENTICAL_TO_FIRST_FETCH
# (first fetch 15:54:32Z; refetch 15:58:21Z)

$ grep -n -F '`description`: Maximum 1024 characters, non-empty, no XML tags' final-skills-guide.md
2269:  * `description`: Maximum 1024 characters, non-empty, no XML tags
3558:  * `description`: Maximum 1024 characters, non-empty, no XML tags

$ awk 'NR==155||NR==162 {printf "%d: %s\n", NR, $0}' sweep/agents-and-tools_agent-skills_best-practices.md
155:   * Cannot contain XML tags
162:   * Cannot contain XML tags
# context 145-168 confirms 155 is under `name`, 162 under `description`

$ grep -l -i 'xml tag' sweep/*.md | wc -l
3

$ grep -i -c 'xml tag' sweep/*.md | awk -F: '{s+=$2} END{print s}'
10

$ grep -i -c 'upload fail' sweep/*.md | awk -F: '{s+=$2} END{print s}'
0

$ grep -i 'validat' sweep/*.md | grep -i -c 'frontmatter'
1
# best-practices.md:1131 "fields with specific validation rules"

$ grep -n -i 'xml' verifiers/verify_skill_checklist.py
1551:# pinned values were derived from the cmark 0.31.2 oracle (`cmark --to xml
1894:    # Pinned values derive from the cmark 0.31.2 oracle (`cmark --to xml
# no description XML-tag check exists at BASE

$ grep -c '<skills>' SKILL.md
8
# includes line 14, the description value (frontmatter-only count is 1)

$ git rev-parse HEAD
c61a973b2e02e1ded169703ddcb06466f4edd8bd

$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
11
# highest id S011; S012 is the next unused

$ curl -sS -L --max-time 40 -o llms.txt -w 'http=%{http_code} size=%{size_download}\n' https://platform.claude.com/llms.txt
http=200 size=89081
$ sha256sum llms.txt
3f8ed26a0694f917e5ed5bba6e3f48b439774aa850eb1947652c9dcff24fcf04  llms.txt

$ cd sweep && : > fetch.tsv && while read -r u; do \
    f="$(echo "$u" | sed 's#https://platform.claude.com/docs/en/##; s#/#_#g')"; \
    code=$(curl -sS -L --max-time 40 -o "$f" -w '%{http_code}' "$u"); \
    sha=$(sha256sum "$f" | cut -d' ' -f1); sz=$(stat -c%s "$f"); \
    printf '%s\t%s\t%s\t%s\n' "$code" "$sha" "$sz" "$u" >> fetch.tsv; \
  done < urls.txt
$ awk -F'\t' '{print $1}' fetch.tsv | sort | uniq -c
30 200
# loop exit 0; per-page sha256/size in SrcNewAnthropicPlatformSkills.json sweep.pages

$ curl -sSI -L https://docs.claude.com/en/api/skills-guide
HTTP/2 301 -> HTTP/2 307 location: /docs/en/build-with-claude/skills-guide
```

Fetch log for all 30 sweep pages (status, sha256, size) is the `sweep` object in
`SrcNewAnthropicPlatformSkills.json`.

## 8. What I did NOT check

- **No tool installs or upgrades.** Host `curl`, `grep`, `awk`, `sha256sum`, and `python3`
  sufficed; nothing was installed, so there is no tool/version/channel record to add.
- **No live API call or upload.** I did not send a tagged SKILL.md to `POST /v1/skills`; that
  needs credentials and would be an external mutation. The enforcement question is therefore
  answered only at the documentation layer.
- **No local validator run.** I did not run `skills-ref validate` or the Claude Code upload
  path against a tagged description.
- **No third-party issue opened.** The GitHub reports that quote the error string
  (`anthropics/claude-code#80469`, `vercel-labs/agent-skills#214`) are unopened leads, not
  evidence; they were not admitted as sources and have no registry row or tier.
- **No non-English/PDF variants.** I did not open the localized pages or
  `resources.anthropic.com`'s "Complete Guide to Building Skills for Claude" PDF.
- **No docs history.** I did not check when the XML-tag bullet was added or whether an older
  revision stated enforcement.
- **No rendered-HTML diff.** The canonical HTML page returned 200, but I did not diff its
  visible text against the markdown reader text; the markdown is what the row pins.
- **No lane gate run.** I did not run `verify_skill_checklist.py` or any lane-wide gate; C2's
  before-state is taken from `.ufo/waves/round-47/before/SUMMARY.md` and source inspection.
- **No `corpus/knowledge/` sweep** for other XML-tag claims; this seat's question was the
  SOURCES row and C2's provenance only.

## 9. Integration note for L1

- Insert the §2 row after `corpus/SOURCES.md:24`; no other registry edit.
- Use the §3 gate row + prose in `corpus/lessons/round-47.md` `## Gate`; the S003 location
  correction belongs there as an append-only note, not as an edit to round 46.
- If C2 lands, flip S012 `queued` → `mined` / `used-by —` → `SKILL.md` only if `SKILL.md:151`
  actually cites it; log the old→new pair per contract rule 2.
- Keep C2's wording at "documented upload requirement". If the round needs the stronger
  "the API rejects", that needs a source this round did not open.
