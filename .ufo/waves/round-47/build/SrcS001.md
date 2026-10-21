verdict: S001 CONTENT still-holds at 2026-10-21 (page text byte-identical to a 2026-10-16 snapshot) but the row's ANCHOR is mislabeled ("§ Skill metadata table" does not exist) and the `.md` reader bytes changed 4c649bdf…→9a67de89…, so a byte-level recheck will false-alarm; the open spec confirms description is constrained by length/non-emptiness only — zero "xml"/"tag" occurrences — which is exactly the negative half C2 needs.

# S001 — agentskills.io/specification — round-47 re-open

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (working tree clean for tracked files; `git status --porcelain` → only `?? .ufo/waves/`, `?? plans/round-47.md`).
Row under test: `corpus/SOURCES.md:14`.

## 1. Fetch record (UTC, status, sha256 — metadata only in lane)

| url | HTTP | bytes | sha256 |
|---|---|---|---|
| `https://agentskills.io/specification` | 200 | 459866 | `3d4955d339d6a160a853187a0428c0c004ecf34a5762bda11c3903f707119e57` |
| `https://agentskills.io/specification.md` | 200 | 7608 | `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` |

Access UTC `2026-10-21T15:54:19Z`, corroborated by the origin's own `date: Wed, 21 Oct 2026 15:54:19 GMT`; server `Vercel`, `x-served-version: dpl_8AUWT8nFRmT7D3RgoEGEPVymfFQP`, `etag: W/"j06n6swtos9ur8"`, `x-nextjs-prerender: 1` (prerendered HTML, no JS execution needed).
Record file: `.ufo/waves/round-47/build/SrcS001.json` (6864 B, metadata only; page bytes stayed in `/fast/scratch/kotoba-r47/SrcS001/`).

## 2. Still-holds vs changed

**Content: still-holds.** I rendered the live HTML to text (`<script>/<style>` stripped, tags→space, entities unescaped, whitespace collapsed) and did the same to the Wayback raw snapshot `20261016083235` of the same URL:

- live text 7272 chars, sha256 `5ae3a105a462f946ad16edffc4e2ea99a717f5a06c6fa16ed4d8cbb354db0c11`
- snapshot text 7272 chars, **same sha256**, `difflib` non-equal opcodes **0**.
- Every marker the row relies on is present exactly once in both: `Must be 1-1024 characters`, `Max 1024 characters. Non-empty.`, `Must match the parent directory name`, `Keep your main SKILL.md under 500 lines`.

[INFERENCE] Round-46 opened on 2026-10-19, between those two identical endpoints; no Wayback HTML capture exists 2026-10-17…10-20 (CDX), so "identical on the 19th" is inferred from identical endpoints on the 16th and 21st, not observed on the 19th.

**Bytes: changed, and the old bytes are unrecoverable.** `specification.md` was `4c649bdf0e0a51c9e215d9f91009ecdca05ee9d073edb6f37c20265bbd829e11` at round-46 (`ufo/round-46/evidence/w2/sources/fetch-log.json` rows[0], accessed `2026-10-19T18:40:53Z`, no bytes retained) and is `9a67de89…` now. I tried ten normalizations of the current `.md` (`theme={null}` stripped, Documentation-Index preamble dropped, both, strip, whitespace-collapse, CRLF, HTML text) — **none** reproduces the old hash, and Wayback CDX has no capture of the `.md` endpoint at all. So the drift is real at byte level but its cause cannot be located at byte level.

**Calibration that the mismatch is not a method artefact.** I refetched four controls whose round-46 hashes were recorded by the same author: S003 `727f3fa1…`, S005 `c85f56cc…`, S006 `61a5378f…`, S008 `2fe1bf40…` — **all four match round-46 exactly** → round-46 hashed raw fetched bytes, so S001's mismatch is drift, not a changed hashing convention. Control S002 (`adding-skills-support.md`) **also** drifted (`9c0e85ee…`→`79489bd2…`) while its round-46 cited sentence — "Skill files authored for other clients may contain technically invalid YAML that their parsers happen to accept." — is still present (`grep -c` = 1, `s002.md:119` § Handling malformed YAML). [INFERENCE] the agentskills.io Mintlify `.md` renderer/preamble churns independently of document content; the HTML text of the spec page is the stable artefact.

Operational consequence: no verifier reads the registry's row hashes — `grep -rni "sources\.md\|fetch-log" verifiers/` hits only a prose note in `verifiers/corpus-baseline.json:57`, and `verify_corpus_integrity.py` treats `corpus/SOURCES.md` as a tracked repo file, not as upstream evidence — so this drift breaks no gate today. But any future "re-verify the recorded sha256" check would fail forever on living Mintlify pages. Record content hash, not endpoint hash (§6).

## 3. Does the open spec constrain description characters/tags? — NO

Quote (20 words), § `description` field, `specification.md:99-102` (section name is the durable locator; `.md` line numbers are not):

> "The required `description` field: • Must be 1-1024 characters • Should describe both what the skill does and when to use it"

(the source's `*` bullets are shown as `•` so the quote does not render as bold.) The same page's Frontmatter table agrees and adds only non-emptiness: `specification.md:31` — "| `description` | Yes | Max 1024 characters. Non-empty. Describes what the skill does and when to use it. |".

Negative evidence, measured on the **whole rendered page text** for both the live page and the 2026-10-16 snapshot: case-insensitive `xml` → **0** occurrences; word-boundary `tag`/`tags` → **0** occurrences. The `description` section contains exactly three bullets (length, what+when, keywords); no character-set or tag rule exists anywhere on the page.

Cross-source consequence for C2: S003's hash is byte-identical to round-46 and still reads "Cannot contain XML tags" (`s003.md:155` and `:162`), so `corpus/SOURCES.md:16` ("an Anthropic-only rule the open spec lacks") holds with an independent negative confirmation. Removing `<skills>` from `SKILL.md:14` is **required** by the Anthropic rule and merely **permitted** by the open spec — the verifier's message should say so rather than implying the open spec forbids tags. This also corroborates `corpus/SOURCES.md:24` (S011 rejected partly because it credits an angle-bracket ban to a spec with "0 mentions").

## 4. Anchor cell — mislabeled, recommend replacement

Claimed: `§ Skill metadata table, § Progressive disclosure; live page opened 2026-10-19`.
Measured: `skill metadata` occurs **0** times in the rendered text and **0** times in the `.md`; there is no such heading. Real, navigable sections are `## SKILL.md format` → `### Frontmatter` (field table), `#### name field`, `#### description field`, and `## Progressive disclosure` (the 500-line sentence is `:237`). The embedded "opened 2026-10-19" is also stale after this re-open.

## 5. Teaches cell — holds, three precision notes

`Name is 1-64 lowercase-hyphen chars matching its directory; description 1-1024 chars saying what and when; SKILL.md under 500 lines with detail moved to reference files` (`corpus/SOURCES.md:14`):

- name: `specification.md:61-67` also allows digits (`a-z`, `0-9`), forbids leading/trailing **and consecutive** hyphens, and says "Must match the **parent** directory name" — the row's "matching its directory" is loose but not wrong.
- description: `:99-102`, as quoted above; holds as written.
- 500 lines: `:237` verbatim. Note the 500-line body and "< 5000 tokens recommended" (`:233`) are **recommendations**, not validation rules — do not let C2's checker promote them to failures.
- The cell omits the one fact C2 needs; hence the optional teaches edit in §6.

## 6. Recommended row deltas (old → new) for the round-47 lesson

- `status`: `mined` → **unchanged** (`mined`; still the authoring source for `SKILL.md:151`).
- `opened`: `2026-10-19` → **`2026-10-21`** (re-opened this round; `E08` accepts it).
- `recheck`: `on-release` → **`90d`**. The page carries no release or version identifier (no version string in `.md` or HTML; only `/llms.txt`), so `on-release` has no observable trigger and the fleet `scripts/sources-census.sh` will report it as an undated symbolic cadence forever. `90d` is E09-legal and date-actionable.
- `used-by`: `SKILL.md` → **`SKILL.md; verifiers/verify_skill_checklist.py`**. Post-C2 that verifier consumes S001 as the *negative* half of its rule (spec constrains length only) and S003 as the positive half.
- `anchor`: `§ Skill metadata table, § Progressive disclosure; live page opened 2026-10-19` → **`§ SKILL.md format › Frontmatter field table and \`description\` field bullets; § Progressive disclosure ("under 500 lines"); live page re-opened 2026-10-21`**. (Section names + verbatim lead-ins, no line numbers — the `.md` line numbers move.)
- `teaches` (optional, only if L1 wants the negative recorded at the registry): → **`Name is 1-64 chars of a-z/0-9/hyphens, no leading/trailing/consecutive hyphen, matching its parent directory; description 1-1024 chars saying what and when, with no character or XML-tag restriction; SKILL.md under 500 lines with detail moved to reference files`**.

Lesson-grade calibration sentence (evidence above): *a live-page recheck is content-level, not byte-level — record the rendered-text sha256 (7272 chars, `5ae3a105…` here) or a Wayback snapshot id beside the endpoint hash; a `.md` hash mismatch alone is not evidence of a content change (S001 and S002 both drifted within two days while every cited claim held).*

## 7. Commands run (all from `/fast/scratch/kotoba-r47/SrcS001`, exit 0 unless noted)

1. `curl -sS -L -D headers.txt -o spec.html -w ... https://agentskills.io/specification` → `http_code=200 size=459866` (0)
2. `sha256sum spec.html` → `3d4955d3…` (0)
3. `curl … -o spec.md https://agentskills.io/specification.md` → `md_http=200 size=7608` (0); `sha256sum` → `9a67de89…`
4. controls `curl` S005/S006/S008 → 200; hashes `c85f56cc… / 61a5378f… / 2fe1bf40…` all equal round-46 (0)
5. controls `curl` S003 → 200, `727f3fa1…` equal; S002 → 200, `79489bd2…` **≠** `9c0e85ee…` (0)
6. `curl "http://web.archive.org/cdx/search/cdx?url=agentskills.io/specification*&from=20261001&to=20261022&output=json…"` → snapshot list, 0 `.md` captures (0)
7. `curl "http://archive.org/wayback/available?url=agentskills.io/specification.md&timestamp=20261019"` → **exit 28** (40 s timeout; retried via CDX which answered)
8. `curl -L --compressed -o wb.html …/20261016083235id_/https://agentskills.io/specification` → 200, 43604 B, `05fce2d2…` (0)
9. python text-diff live vs snapshot → `identical True`, `opcodes_non_equal 0` (0)
10. python normalization sweep vs `4c649bdf…` → 10 variants, 0 match (0)
11. python counts → `xml_ci 0`, `tag_word 0` on both texts; `skill metadata 0` (0)
12. `grep -rni "sources\.md\|fetch-log" verifiers/` → 1 hit, prose only in `corpus-baseline.json:57` (0); `grep -rn "SOURCES" verifiers/*.py` → no hits (1, expected empty)
13. `python3 -c json.load(.ufo/.../SrcS001.json)` → parsed, 16 top-level keys (0)

Counterexample worth keeping: the first Wayback attempt without `--compressed` produced a 43604-byte mojibake blob hashing `7fb32e8e…`; a pipeline that hashes the wire bytes of an `id_` capture records garbage. Also, `curl`'s `size_download` for the compressed response equaled the uncompressed size, so size alone cannot detect this.

## 8. What I did NOT check

- `skills-ref` (the validator the page links): whether it enforces more than the page text (e.g. tag bans). The page only says it "checks that your SKILL.md frontmatter is valid and follows all naming conventions" — the implementation is a different source and is not S001.
- The `.md` endpoint between 2026-10-19 and 2026-10-21: no archived copy exists, so the drift cause is [INFERENCE], not observed.
- Wayback coverage 2026-10-17…10-20 (gap); content equality on the 19th is inferred.
- Full content diff of S002 beyond its cited sentence (used only as a drift control), and no other agentskills.io page this round.
- Any lane verifier (`verify_surfaces.py`, `check_substrate_pins.py`, `verify_skill_checklist.py`, `verify_corpus_*`) — not run; out of this item's scope.
- "tag" in the sense of HTML elements inside the `compatibility` field or elsewhere: no such rule found, but I searched the rendered text, not every linked sub-page.
- Installs/upgrades: **none**; no pacman transaction, no `~/.local/bin/opencode` execution, no omp session.
