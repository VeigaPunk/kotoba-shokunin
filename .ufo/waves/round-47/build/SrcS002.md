verdict: still-holds — S002's two anchors and its teaches cell are intact on the live page at 2026-10-21T15:55Z, and the live text is byte-identical to the bytes round 46 hashed once a publisher-side markdown-renderer change is undone; no status/recheck/used-by change needed.

# S002 re-open — agentskills.io "How to add skills support to your agent"

Row under test: `corpus/SOURCES.md:15` at BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`
(`git rev-parse BASE:corpus/SOURCES.md` and `git hash-object corpus/SOURCES.md` both
`a048aef0997e68881c9740e878d2fe01402bb04b` → worktree row == BASE row; `git diff --stat BASE -- corpus/SOURCES.md` exit 0, empty).

## What I opened (metadata only; bytes stayed in /tmp, nothing copied into the lane)

| fetch | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| HTML | `https://agentskills.io/client-implementation/adding-skills-support` | 2026-10-21T15:54:09Z | 200 | 438641 | `123edf8e2bfb62cf…5331` |
| markdown | `…/adding-skills-support.md` | 2026-10-21T15:55:06Z | 200 | 20349 | `79489bd252377681…e172` |
| markdown refetch | same | 2026-10-21T15:57:29Z | 200 | 20349 | `79489bd2…e172` (identical) |
| Wayback raw `id_` | `web.archive.org/web/20260914113657id_/…adding-skills-support.md` | ~2026-10-21T15:58:40Z | 200 | 20898 | `053f470d59333548…1ea6` |

No redirects (`url_effective` == requested on every live fetch). Full record:
`.ufo/waves/round-47/build/SrcS002.json`.

## Findings

**1. Both anchors exist, live HTML and markdown.**
`### Handling malformed YAML` at fetched-markdown line 119, `id="handling-malformed-yaml"` in the
HTML; `### Lenient validation` at line 130, `id="lenient-validation"`. The row's anchor cell
(`corpus/SOURCES.md:15`, "§ Handling malformed YAML, § Lenient validation") is still accurate.

**2. The teaches cell holds.** The malformed-YAML claim is quoted verbatim at md:121 (17 words):
"Skill files authored for other clients may contain technically invalid YAML that their parsers happen to accept."
Lenient name handling is verbatim at md:134 (11 words):
"Name doesn't match the parent directory name → warn, load anyway".
So "Unquoted values containing colons are technically invalid YAML; lenient clients warn and load
anyway on name mismatch" still stands as written.

**3. What clients do with an invalid description — one condition only, and it is a hard skip**
(md:136, 18 words):
"Description is missing or empty → skip the skill (a description is essential for disclosure), log the error".
And md:137: "YAML is completely unparseable → skip the skill, log the error" (11 words).
There is **no** rule about markup or tags in a description: `grep -c 'XML tag\|angle bracket\|angle-bracket'`
returns 0 on both the markdown and the HTML (grep exit 1 = no match). The catalog example does embed
the description verbatim inside `<description>` (md:173, md:178) with no escaping guidance, so
[INFERENCE] a literal tag inside a description can break the page's own XML catalog shape — but the
page neither forbids nor sanitizes it.

**4. Round 46's sha `9c0e85ee…` is reproducible from today's bytes — decisive freshness evidence.**
Today's `.md` sha is `79489bd2…`, which looked like drift. Converting the three GFM alert blocks in
today's file back to the MDX components the 2026-10-19 copy carried (`> [!NOTE]`/`> [!TIP]` →
`<Note>`/`<Tip>`) yields 20357 bytes with sha256
`9c0e85eed0c774d5af2d1082656a278f6c5848c0536d383dcd617067b72288ed` — exactly the value at
`.ufo/round-46/evidence/w2/sources/fetch-log.json` `rows[1].sha256` and `corpus/lessons/round-46.md:64`.
A 256-bit match from content-derived reconstruction is not a collision: the page text has not changed
since round 46; only the publisher's markdown exporter changed. (Counterexample to naive sha-as-freshness.)

**5. Independent cross-check against 2026-09-14.** The Wayback `id_` capture is 337 lines / 20898 bytes
(vs 337 lines / 20349 today). `diff -u` exit 1 with **4 hunks, all renderer-level**: padded tables →
compact tables, and `<Note>`/`<Tip>` → GFM alerts. Normalized (markers/table plumbing/whitespace
stripped) both versions hash to `93868c305dcc9271f6f9ba4e0337aa7d0e0700c4841122313a982a311a3d27ce`.
Prose is unchanged across five weeks.

**6. Publisher content date.** The Next.js payload in the HTML carries
`"lastModified":"2026-03-10T13:40:59.504Z"` for `originalFileLocation` `client-implementation/adding-skills-support…`
— before both reads. The HTTP `last-modified` header is *not* usable (it echoed the fetch time,
`15:57:29 GMT`).

**7. Citation boundary for C2 (calibration).** S002 supplies the colon-space YAML clause and the
lenient/skip table; it supplies **nothing** about XML tags. `corpus/SOURCES.md:16` (S003, Anthropic)
is the only row carrying "The description cannot contain XML tags". `SKILL.md:151` lists S001–S003 +
S008 collectively, but tags the clause inline as "(Anthropic rule)", so no misattribution is written
today — the risk is a round-47 lesson paraphrase that credits the ban to S002. Likewise the ` #`
plain-scalar case is S008 (`corpus/SOURCES.md:21`), not S002; S002 names only colons (md:121–125).

**8. Cell gap worth fixing.** The teaches cell says lenient clients "warn and load anyway" without the
two hard skips (md:136–137). A lesson drawn from it overstates client leniency: an *empty* description
is not a cosmetic issue, the client refuses to disclose the skill at all.

## Commands run (all exit codes as observed)

- `grep -n S002 corpus/SOURCES.md` → 0 (rows 15, 24, 28 printed)
- `git show BASE:corpus/SOURCES.md | grep -n S002` → 0; `git diff --stat BASE -- corpus/SOURCES.md` → 0, empty
- `date -u`; `curl -sS -o … -w 'HTTP:%{http_code} SIZE:%{size_download} URL:%{url_effective}' …` → 0, `HTTP:200 SIZE:438641`
- `sha256sum /tmp/SrcS002_fetch.html` → 0, `123edf8e…5331`
- `curl … adding-skills-support.md` → 0, `HTTP:200 SIZE:20349`; `sha256sum` → `79489bd2…e172`
- refetch + `sha256sum` → identical hash
- `grep -o 'id="[^"]*\(malformed\|lenient\)[^"]*"'` → 0, both ids
- `grep -c 'XML tag\|angle bracket\|angle-bracket'` on `.md`/`.html` → exit 1; each file reports 0 matches (`:0`)
- `curl 'http://web.archive.org/cdx/search/cdx?url=…adding-skills-support.md&output=json'` → 0; last `.md` capture 20260914113657
- `curl --compressed …/20260914113657id_/…` → 0, 20898 bytes, `053f470d…1ea6`
- `diff -u archive live > diff` → 1 (differences expected), 4 hunks, renderer-only
- python3 3.14.8 inverse-render + hashes → 0, transformed sha `9c0e85ee…` (match)

No tools installed or upgraded; `pacman` untouched.

## Recommended row changes (old → new)

- `status`: `mined` → `mined` (no change)
- `recheck`: `90d` → `90d` (no change; page lastModified 2026-03-10, prose stable 2026-09-14→2026-10-21)
- `used-by`: `SKILL.md` → `SKILL.md` (no change)
- `opened`: `2026-10-19` → `2026-10-19` (no change; the re-open date belongs in the round-47 lesson)
- anchor cell (optional): `§ Handling malformed YAML, § Lenient validation; live page opened 2026-10-19`
  → `§ Handling malformed YAML (#handling-malformed-yaml), § Lenient validation (#lenient-validation); live page opened 2026-10-19, re-opened 2026-10-21`
- teaches cell (recommended): `…lenient clients warn and load anyway on name mismatch, so a strict local gate is stricter…`
  → `…lenient clients warn and load on name mismatch or >64 chars, but skip on missing/empty description or unparseable YAML; a strict local gate is stricter…`
- recheck method (recommended, for the lesson's Gate): stop treating the raw `.md` sha256 as the freshness
  signal — the exporter changed twice in five weeks (table padding, then MDX→GFM alerts) with zero prose
  change. Recheck on (a) the two heading strings, (b) payload `lastModified`, (c) normalized-text sha256
  `93868c30…`.

## What I did NOT check

- No browser/JS render; the HTML was read as bytes, and the rendered page was not inspected in a browser.
- Did not re-open S001, S003, S008, or any other row; the S003/S008 citations above are from `corpus/SOURCES.md`, not from a fresh fetch.
- Did not run any verifier: `grep -rn 'recheck\|SOURCES' verifiers/verify_corpus_integrity.py verifiers/verify_corpus_independent.py` → exit 1, no matches, i.e. no gate parses this column. No lane gate was run at all.
- Did not locate the site's source repo/changelog; the renderer-change attribution rests on the inverse-render hash match plus the Wayback diff.
- Did not verify round 46's HTTP status/time beyond its own fetch log; only its sha was proven byte-equivalent.
- BASE citations are line numbers from `git show BASE:<path>`; the URL citations are line numbers of the fetched markdown identified by sha `79489bd2…e172`, which is not stored in the lane (metadata only, per Q11).
