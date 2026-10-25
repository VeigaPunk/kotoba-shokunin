# ScoutQuarantine — round 70, wave 1

**Verdict: slice CONFIRMED (byte-identical); id half CONFIRMED (0 of 13 ids appended); URL half
REFUTED for 1 of 13 — register S151's cited URL `https://agentskills.io/skill-creation/optimizing-descriptions.md`
was appended this round as lane row S210.** The S151 *defect* (its absent quote) is not carried:
S210 cites a different quote that is present in its sha256-pinned snapshot, and the register's S151
quotes are absent from it. So no quarantined payload was admitted, but the lesson's sentence "none
is appended" (`corpus/lessons/round-70.md:105-106`) is true by id only, and the lesson's own rule
("the URL is the evidence; the id follows it", `:44`) makes S210 the same document as register S151.
Confidence: high on all observed facts; the namespace finding below is inference from two observed
mismatches.

Base `7d51253f`, tip `16b212a3` (`git rev-parse HEAD` = tip). Read-only throughout; no tools
installed or upgraded. Scratch files `/tmp/k70-sq-*.txt` deleted.

## F1 — slice re-derivation matches the staged file byte-for-byte

```
awk -F'|' -v l='kotoba' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' \
  /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md > /tmp/k70-sq-derived.txt
cmp /tmp/k70-sq-derived.txt .ufo/waves/round-70/assimilation/quarantine-slice   # exit 0
sha256sum both  # 0141c203d993e812c85c6d9ee7a8cdf6b44b5d2aca2113bab7ef607de38d7916 (both)
```

13 lines each: 7 `payload-absent` (S151 S167 S168 S172 S176 S180 S185) and 6 "the cited source
could not be fetched, so no quote was checked" (S236 S237 S238 S239 S243 S169). The source rows are
register lines 103, 108, 110, 111, 114, 116, 117, 327–332.

Format quirk (observed, faithfully reproduced): register lines 327–332 carry a 6-cell row whose id
cell ends in a stray backtick (`| S236\` | the cited source could not be fetched… | https://skills.sh/docs |`)
and have no class cell. So `$5` there is the meaning text, not a class token, and the slice prints
`S236\``. The register's header lists only `payload-absent` (194 rows) in its Totals table, so these
6 rows sit outside its own class taxonomy. Round 69 recorded them as `unreachable` (`corpus/lessons/round-69.md:119-120`).

## F2 — SOURCES.md diff over the round adds exactly S209, S210, S211

```
git -C kotoba-shokunin diff --no-ext-diff -U0 7d51253f… 16b212a3… -- corpus/SOURCES.md
# 3 insertions, 0 deletions: rows S209, S210, S211 only
```

Per-id and per-URL check (ids and URLs taken from register cells `$4`/`$6`; "added" means a `+`
line in the diff above; base and tip counts come from `git show <rev>:corpus/SOURCES.md`):

| register id | register URL | id row added | URL in added lines | URL lines base→tip |
|---|---|---|---|---|
| S151 | agentskills.io/skill-creation/optimizing-descriptions.md | 0 | **1 (S210)** | **0→1** |
| S167 | agentskills.io/client-implementation/adding-skills-support.md | 0 | 0 | 0→0 |
| S168 | vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals | 0 | 0 | 0→0 |
| S172 | junie.jetbrains.com/docs/agent-skills.html | 0 | 0 | 1→1 (S206, pre-existing) |
| S176 | agentskills.io/client-implementation/adding-skills-support.md | 0 | 0 | 0→0 |
| S180 | web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja | 0 | 0 | 0→0 |
| S185 | docs.roocode.com/features/skills | 0 | 0 | 1→1 (S203, pre-existing) |
| S236 | skills.sh/docs | 0 | 0 | 0→0 |
| S237 | skills.sh/audits | 0 | 0 | 0→0 |
| S238 | code.claude.com/docs/en/security.md | 0 | 0 | 0→0 |
| S239 | skills.sh/agent | 0 | 0 | 0→0 |
| S243 | skills.sh/docs/api | 0 | 0 | 0→0 |
| S169 | ai.google.dev/gemini-api/docs/coding-agents | 0 | 0 | 0→0 |

No id is appended, and no `| S1xx |`/`| S2xx |` row for any of the 13 ids exists at base or tip. The
lane registry holds S001–S211 (137 rows at tip), and none of S151…S243 appears as a row there. One
URL is new this round (S151 → S210). Two URLs (S172, S185) were already present at base as S206 and
S203, opened in round 69 (`corpus/lessons/round-69.md:122-124`), so they are not this round's appends.

## F3 — S210 is register S151's document under the lane's renumbering

- `corpus/lessons/round-70.md:43-46`: "**Renumber map, by document** (the URL is the evidence; the id
  follows it): … staged S231 (`agentskills.io/skill-creation/optimizing-descriptions.md`) → **S210**".
- `quote-lint-full-v5.json`, the register's source, has `{"lane":"kotoba","round":"round3","id":"S151","verdict":"ABSENT","url":"https://agentskills.io/skill-creation/optimizing-descriptions.md",…}`
  (python3 walk over `findings`, 4 hits).
- Staged S231 in `shokuknow/lanes/kotoba/round3/SOURCES-PROPOSED.md:21` and `merge/kotoba/SOURCES.append.md:35`
  has the same URL.

The round-70 lesson's quarantine paragraph (`:103-106`) lists "staged S151" as quarantined and says
"none is appended". It never notes that S210 shares S151's URL. The plan (`plans/round-70.md`) has
no mention of quarantine, S151 or `optimizing-descriptions`; `grep` returns 0 hits.

## F4 — the S151 defect is not carried into S210

```
git show 16b212a3:.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md | sha256sum
# 7cc54fbb…bd837  == pin at verifiers/check_skill_evals.py:50-52; 13 403 B (matches lesson :56-57)
grep -cF 'A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default).'  → 1
grep -cE '37.44 points|80K skills'                    → 0
grep -cF '不明なフロントマターフィールドは無視されます'      → 0
```

The register's S151 "quotes" are spans of lane prose: the v5 `line` field quotes ``corpus/SOURCES.md:207`
still reads "metadata-only routing loses 37–44 points…"`` and a `CANNOT-ANSWER.md` note. That looks
like a mis-bound quote, not a fabricated page fact [INFERENCE]. S210 carries none of them. Its quote
is located in the pinned page. The quarantine on S151's *row and quote* holds; the *document* was
re-opened fresh.

## F5 — the register ids are not in the lane's or the staging's id namespace [INFERENCE]

`shokuknow/lanes/kotoba/ID-REMAP.md` (per-round old→new map) does not reconcile the register.
Register round4 S167 cites `adding-skills-support.md`, but its remap target S240 cites
`arxiv.org/abs/2602.11988`. Register round10 S236 cites `skills.sh/docs`, which is the URL of remap
target S316, the target of round10 **S243**. Nine of the 13 (round, id) pairs have no remap row
(shell loop over `ID-REMAP.md` and `merge/kotoba/SOURCES.append.md`). So "the 13 staged ids" are
register-local ids. An id-only join against lane `corpus/SOURCES.md` passes vacuously; only the URL
join tests anything. That is why F3 is the operative finding.

## Remaining unknowns

- Whether the quarantine is meant to bind the row and quote (S210 is clean) or the document (S210
  breaches it). Neither the plan nor the register states its scope. The register's own "what a
  reader does" column says "correct the quote or refuse the row", which supports a row and quote
  scope [INFERENCE].
- The register's misnumbering (F5) was not traced to its cause in `renumber-staged.py` or
  `absent-defect-register.py`. Out of scope.
