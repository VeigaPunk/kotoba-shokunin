# ExecSrcSpecOnePager — S255 source opening (round 72, wave 1)

**Verdict:** S255 opened by this seat on 2026-10-25 — `https://agentskills.io/skill.md`, HTTP 200,
final URL unchanged, **16 035 B**, sha256 `624f1c7f14a89481823f156aad5b665064a3c595cd9682e73c26f48db88994fc`,
234 lines, served as `text/markdown`. Snapshot written at
`.ufo/waves/round-72/snapshots/S255-agent-skills-skill-md.md` (byte-identical to the fetched bytes).
**Both quotes in the staged row are located byte-exact** (L15, L22), as is the entry quote in
`context-rot-and-always-on-context.md` (L15). **One staged claim is false:** the row's scope cell says
the one-pager is "the only first-party place the lane holds that states the cross-client discovery
convention and the per-skill metadata cost together" — the lane's own **S002** (same document as S256)
states both, so the uniqueness qualifier must be dropped before the row is appended. **One anchor is
shaped:** "Key files and paths" is a bold label at L17, not a heading. **One source-internal
divergence:** the L22 bullet calls `.agents/skills/` the cross-client standard, while the page's own
table (L76–83) labels the *user-level* `~/.agents/skills/` row "Cross-client standard" and the
project-level one "Highest (overrides user-level)". Details, commands and observed output below.

---

## 1. Fetch record

```
S=$(mktemp -d /tmp/k72w1-ExecSrcSpecOnePager.XXXX)
curl -sS -A 'Mozilla/5.0' -D headers-skill.md.txt -o skill.md.body \
     -w 'http=%{http_code} final=%{url_effective} bytes=%{size_download}\n' https://agentskills.io/skill.md
```
observed: `http=200 final=https://agentskills.io/skill.md bytes=16035`

```
sha256sum skill.md.body   ->  624f1c7f14a89481823f156aad5b665064a3c595cd9682e73c26f48db88994fc
wc -lc skill.md.body      ->  234 16035
```

Headers observed (excerpt): `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`,
`server: Vercel`, `x-matched-path: /_sites/[subdomain]/skill.md`, `cf-cache-status: HIT`,
`x-vercel-cache: MISS`, `date: Sun, 25 Oct 2026 21:36:55 GMT`,
`last-modified: Sun, 25 Oct 2026 07:31:25 GMT`, `age: 84987`.

Cache-busted refetch (freshness check, not a second opinion):

```
curl -sS -A 'Mozilla/5.0' -H 'Cache-Control: no-cache' -o skill.md.nocache https://agentskills.io/skill.md
sha256sum skill.md.nocache skill.md.body
624f1c7f…94fc  skill.md.nocache
624f1c7f…94fc  skill.md.body
cmp -s skill.md.nocache skill.md.body && echo IDENTICAL   ->  IDENTICAL
```

Snapshot write and verification:

```
mkdir -p .ufo/waves/round-72/snapshots
cp <scratch>/skill.md.body .ufo/waves/round-72/snapshots/S255-agent-skills-skill-md.md
sha256sum …/S255-agent-skills-skill-md.md -> 624f1c7f…94fc ; wc -lc -> 234 16035
cmp -s <scratch>/skill.md.body …/S255-agent-skills-skill-md.md && echo IDENTICAL-TO-FETCHED -> IDENTICAL-TO-FETCHED
git status --porcelain -- .ufo/waves/round-72/snapshots/S255-agent-skills-skill-md.md
?? .ufo/waves/round-72/snapshots/S255-agent-skills-skill-md.md
```

`.ufo` is tracked (`.gitignore:1` ignores only `.ufo/interactive-sessions/`); round-70 snapshots are
committed (`git ls-tree -r --name-only c69711e -- .ufo/waves | grep -c '/snapshots/'` → `26`), so the
C1(d) "committed snapshot" conjunct is satisfiable by the L1's commit. Access date: **2026-10-25**.

## 2. What form the quote lives in (rendered page vs `.md`)

There is **no rendered page** for this document:

```
GET https://agentskills.io/skill            -> http=404 ct=text/html; charset=utf-8 bytes=122032
GET https://agentskills.io/skill/           -> http=308 redirect=https://agentskills.io/skill
GET https://agentskills.io/skill.md?raw=true-> http=200 ct=text/markdown; charset=utf-8 bytes=16035
GET https://agentskills.io/                 -> http=308 redirect=https://agentskills.io/home
```

The quote therefore lives in the **`.md` export only**; `?raw=true` returns the same 16 035 bytes.
The document is also **not listed in the site's docs index**: `https://agentskills.io/llms.txt`
(1 374 B, 200) lists `home.md`, `specification.md`, `clients.md`, `skill-creation/quickstart.md`,
`skill-creation/best-practices.md`, `skill-creation/optimizing-descriptions.md`,
`skill-creation/evaluating-skills.md`, `skill-creation/using-scripts.md`,
`client-implementation/adding-skills-support.md` — **no `skill.md`**; the rendered home page has no
`href="/skill"` and no `skill.md` string (`grep -c` → `0`, `0`). Recorded so the L1 does not hunt for
a rendered URL when a recheck falls due.

**URL for duplicate detection:** host `agentskills.io`, path `/skill.md`.
Lane registry grep: `grep -rn 'agentskills.io/skill\.md' corpus/ SKILL.md` → **0 hits**; the lane's
`agentskills.io` rows are S001/S018 (`/specification`), S002 (`/client-implementation/adding-skills-support`),
S209/S212 (`/skill-creation/evaluating-skills.md`), S210/S213 (`/skill-creation/optimizing-descriptions.md`).
No URL duplicate.

## 3. Located quotes (snapshot line numbers)

Full table with dropped bytes: `.ufo/waves/round-72/w1/build/ExecSrcSpecOnePager/s255-located-quotes.md`.
Pin record for the counter: `.ufo/waves/round-72/w1/build/ExecSrcSpecOnePager/s255-pin.json`.

`sed -n '15p'` (snapshot):
`Agents load skills through **progressive disclosure**: at startup they load only the name and description of each skill (~50-100 tokens per skill); when a task matches a skill's description, they load the full `SKILL.md` body into context; if the instructions reference supporting files, those load individually as needed.`

`sed -n '22p'` (snapshot):
`- Discovery paths: `.agents/skills/` (cross-client standard), `.<client>/skills/` (client-specific).`

`sed -n '17p'` → `**Key files and paths:**`  ·  `sed -n '11p'` → `## Product summary`

```
sed -n '18p' ->
- `SKILL.md` — Required. Contains YAML frontmatter (`name`, `description`, optional `license`, `compatibility`, `metadata`, `allowed-tools`) followed by markdown instructions.
```

```
sed -n '43,44p' ->
| `name` | Yes | 1-64 chars, lowercase + numbers + hyphens, no leading/trailing/consecutive hyphens, must match parent directory | Unique skill identifier |
| `description` | Yes | 1-1024 chars, non-empty | Tells agents when to use the skill. Carries the entire burden of triggering. |
```

```
sed -n '80,83p' ->
| Project-level | `.agents/skills/` | Highest (overrides user-level) |
| Project-level | `.<client>/skills/` | Client-specific |
| User-level | `~/.agents/skills/` | Cross-client standard |
| User-level | `~/.<client>/skills/` | Client-specific |
```

Byte-exactness was tested with fixed-string grep on the snapshot, each returning `1`:

```
grep -cF 'at startup they load only the name and description of each skill (~50-100 tokens per skill)'          -> 1
grep -cF 'Discovery paths: `.agents/skills/` (cross-client standard), `.<client>/skills/` (client-specific)'    -> 1
grep -cF 'only the name and description of each skill (~50-100 tokens per skill)'                               -> 1
grep -cF '`name`, `description`, optional `license`, `compatibility`, `metadata`, `allowed-tools`'              -> 1
grep -cF '**cross-client standard**'                                                                            -> 0
```

**Word-boundary trap for C1(d) (measured, not predicted):** Q1 ends with `)`, so a `\b…\b` test fails —

```
grep '\bat startup they load only the name and description of each skill \(~50-100 tokens per skill\)\b'   -> No matches found
grep '(?<!\w)at startup they load only the name and description of each skill \(~50-100 tokens per skill\)(?!\w)' -> match at line 15
```

If `check_author_rules.py` wraps the quote cell in `\b…\b`, every quote ending in `)` or `"` reads as
absent and the A4 rule fails on a correct snapshot. Use lookarounds.

## 4. Verdict per claim

**Staged row S255** (`SOURCES.append.md:59`):

| claim in the row | verdict | evidence |
|---|---|---|
| quote "at startup they load only the name and description of each skill (~50-100 tokens per skill)" | **confirmed** (byte-exact substring) | snapshot L15 |
| quote "Discovery paths: `.agents/skills/` (cross-client standard), `.<client>/skills/` (client-specific)" | **confirmed** (byte-exact substring) | snapshot L22 |
| anchor "Product summary" | **confirmed** — `## Product summary` | snapshot L11 |
| anchor "Key files and paths" | **confirmed-after-shaping** — the page carries it as a bold paragraph label `**Key files and paths:**`, not as a heading; the row lists it beside a real H2 | snapshot L17 |
| teaches: canonical frontmatter `name`, `description`, optional `license`, `compatibility`, `metadata`, `allowed-tools` | **confirmed** — same list at L18, and as a table at L39–48 (`name`/`description` Required, the other four No) | snapshot L18, L43–48 |
| teaches: "the metadata cost quantified at ~50-100 tokens per skill" | **confirmed** | snapshot L15 |
| teaches: "the cross-client standard being `.agents/skills/` with client-specific roots beside it" | **confirmed for the bullet**, with a source-internal divergence (below) | snapshot L22 vs L76–83 |
| "it is a distinct document from the specification page the lane holds" | **confirmed** — `/specification.md` is 7 608 B, contains neither `.agents/skills/` nor `50-100` | `curl … /specification.md` → `bytes=7608`; `grep -c` → `0`, `0`, `0` |
| "it is the only first-party place the lane holds that states the cross-client discovery convention and the per-skill metadata cost together" | **absent (contradicted)** — the lane's S002 states both | §5 |
| "fetched as `.md` 16 035 B on 2026-10-23" | size **confirmed today** (16 035 B); the 2026-10-23 date is **not verifiable from the package** and is not relied on — this seat opened it 2026-10-25 | §1 |
| recheck "confirm the frontmatter list, the discovery paths and the ~50-100 token figure are unchanged" | **satisfiable today** — all three present at L18/L22/L15 | snapshot |

**Entry `context-rot-and-always-on-context.md`** (the one my item names):

| claim | verdict | evidence |
|---|---|---|
| L27–29: the one-pager "states that at startup an agent loads 'only the name and description of each skill (~50-100 tokens per skill)'" | **confirmed** — the quoted span is byte-exact; the entry's framing word "an agent" replaces the source's "they" *outside* the quote | snapshot L15 |
| L27: attribution "(S255)" | **confirmed** as the document, but the entry has **no `source: S255` line** — its `source:` lines are S254 (L3) and S248 (L4) only | entry L3–4, L27 |

**Entry `skill-vs-always-on-boundary.md`** (the other entry my item names): it does **not** cite S255.
Its `source:` lines are S261–S264 only (lines 4–7), and `grep -c S255` on it → 0. So the entry check
runs on `context-rot-and-always-on-context.md` (above) plus the two entries the row's `used-by` names.

**Other package entries that cite S255** (opened for completeness, since the row's `used-by` names them):

| entry:line | claim | verdict |
|---|---|---|
| `client-frontmatter-and-discovery-divergence.md:14` | "lists the canonical frontmatter as `name`, `description`, and optional `license`, `compatibility`, `metadata`, `allowed-tools`" | **confirmed** (L18/L43–48); the word "canonical" is the entry's, not the page's |
| `client-frontmatter-and-discovery-divergence.md:6` / `client-loading-and-distribution-models.md:7` | anchor `` `# Key files and paths` `` | **confirmed-after-shaping** — same label-vs-heading issue as the row (L17) |
| `client-loading-and-distribution-models.md:13–14` | quote with bold: "Discovery paths: `.agents/skills/` (**cross-client standard**), `.<client>/skills/` (client-specific)." | **confirmed-after-shaping** — words verbatim; `grep -cF '**cross-client standard**'` on the snapshot → **0**, so the emphasis is the entry's |
| `client-loading-and-distribution-models.md:30` | `.<client>/skills/` convention "(S255)" | **confirmed** (L22) |
| `client-implementation-loading-model-amendment-2026-10-23.md:26` | "the same figure the format one-pager repeats (S255)" | **confirmed** (L15) |

## 5. The uniqueness claim is false — the lane's own S002 states both facts

`corpus/SOURCES.md:15` holds **S002** = `https://agentskills.io/client-implementation/adding-skills-support`
(tier A, `mined`). That URL returns the rendered HTML of the *same document* the package stages as S256:

```
GET https://agentskills.io/client-implementation/adding-skills-support -> http=200 ct=text/html; charset=utf-8 bytes=388444
grep -o '50-100 tokens per skill' s002.html | wc -l  -> 2
grep -o 'cross-client' s002.html | wc -l             -> 4
grep -o '\.agents/skills/' s002.html | wc -l         -> 20
```

and its `.md` export (`https://agentskills.io/client-implementation/adding-skills-support.md`, 20 446 B,
200) carries both facts in one document:

```
sed -n '26p'  ->  | 1. Catalog | Name + description | Session start | \~50-100 tokens per skill |
sed -n '56p'  ->  The `.agents/skills/` paths have emerged as a widely-adopted convention for cross-client skill sharing. While the Agent Skills specification does not mandate where skill directories live (it only defines what goes inside them), scanning `.agents/skills/` means skills installed by other compliant clients are automatically visible to yours, and vice versa.
sed -n '186p' ->  Each skill adds roughly 50-100 tokens to the catalog. Even with dozens of skills installed, the catalog remains compact.
```

(quote taken from L56 above: the first sentence, 13 words; dropped bytes named: the rest of that line,
from "While …" to "… and vice versa.")

So the row's scope cell must be narrowed (e.g. "the only *one-pager* form of the figure" or "the
first place the lane holds the figure *and* the discovery paths in a single compact document") before
it is appended; as written it is contradicted by a row the lane already holds. The facts themselves
are not in doubt — only the "only" is.

## 6. Source-internal divergence worth recording (not a lane defect)

L22 (bullet, under `**Key files and paths:**`) calls `.agents/skills/` "cross-client standard" for both
scopes; the page's own table at L76–83 assigns "Cross-client standard" only to the **user-level**
`~/.agents/skills/`, gives the **project-level** `.agents/skills/` the priority note
"Highest (overrides user-level)", and marks both `.<client>/skills/` rows "Client-specific". An entry
that quotes L22 as *the* precedence rule over-reads it; the precedence rule is in the table, not the
bullet. Relevant to C1's A1 (name uniqueness / precedence): the page states
`name` … "Unique skill identifier" (L43) and a project-over-user precedence (L80), which **corroborates**
A1 — but A1's frozen entry is the round-69 entry, whose `source:` lines are S203–S207, so under the
frozen predicate S255 cannot supply A1's cited id. Use it as corroboration in prose only.

## 7. C1 interface notes for the L1

1. **Pin tuple** for `check_author_rules.py` (matches the round-70 convention in
   `verifiers/check_skill_evals.py:46-55`): `("S255", "S255-agent-skills-skill-md.md",
   "624f1c7f14a89481823f156aad5b665064a3c595cd9682e73c26f48db88994fc", "https://agentskills.io/skill.md")`.
2. **Word-bounded ≠ `\b…\b`** (§3). The row's quote cell ends with `)`.
3. **A4 token coverage:** the snapshot contains `skill` and `prompt` but **no** `always-on`, **no**
   `index`, **no** `catalog`, **no** `resident` (`grep -oi … | wc -l` → 0 each). S255 can support A4's
   on-demand/resident split (L15) but cannot supply the `always-on`/`index` tokens; those must come
   from the rows that state them (Vercel S248, Chroma S254, the four vendor rows S261–S264).
4. **The id is free.** `.ufo/waves/round-72/assimilation/collisions` lists 11 collisions
   (`S203`–`S213`) and none is S255; the lane registry holds 139 ids with S213 the highest
   (`reg-ids`), while S255 is staged id 53 (`staged-ids`). Note the id *spaces* differ: the lane's
   S203–S207 are Roo Code / Amp / Deep Code / Junie / opencode (`corpus/knowledge/skill-name-precedence-round69.md:1-5`),
   not the package's S203–S207 (Model Spec / skill-creator / Qwen ×3 / Qwen weekly). A1's frozen entry
   cites the **lane** ids, so S255 is not in A1's id set.
5. **The row's quote cell holds two quoted spans, not one.** Splitting on the straight double
   quotes in `SOURCES.append.md:59` yields exactly two: the 16-word one (L15) and the 7-word one
   (L22), with the word `also` between them. A counter that treats the whole cell as a single quote
   will see ~40 words and fall outside the 5–25 range; split on `"…"` and require every span to
   locate, or designate one span as the row's canonical quote.
6. **`used-by` must be extended on append.** The staged row lists
   `corpus/knowledge/client-frontmatter-and-discovery-divergence.md, corpus/knowledge/client-loading-and-distribution-models.md`;
   the package has **four** entries citing S255 — `context-rot-and-always-on-context.md:27` and
   `client-implementation-loading-model-amendment-2026-10-23.md:26` are unlisted. C1(b) requires the
   cited row's `used-by` to list the cited entry path, so whichever entries the L1 lands must appear there.

## 8. Freshness note

`last-modified: Sun, 25 Oct 2026 07:31:25 GMT` — the page was rebuilt **today**, after the staged
2026-10-23 fetch, yet the byte count is identical to the row's `16 035 B` and the no-cache refetch is
byte-identical (`cmp` → IDENTICAL). Content therefore appears unchanged, but the package records **no
sha256** for its 2026-10-23 fetch, so cross-date equality rests on size + the presence of all quoted
strings, not on a digest. The 90-day recheck is satisfiable from this snapshot: all three things it
names (frontmatter list, discovery paths, ~50-100 figure) are present at L18/L22/L15.

## 9. Not verified / risks

- The staged row's `opened: 2026-10-23` and its "fetched as `.md` 16 035 B on 2026-10-23" are **not
  verified** — the package records the size but stores neither the 2026-10-23 bytes nor a digest, so
  only today's bytes were observed; the 16 035 B agreement is consistent with, not proof of, an
  unchanged page.
- I did not check whether any sibling lane (not this one) holds `agentskills.io/skill.md`; my duplicate
  grep covered only this lane's `corpus/` and `SKILL.md`.
- `context-rot-and-always-on-context.md` is staged-only (the lane has no such entry:
  `grep -rn 'S255' corpus/` → 0 hits), so its missing `source: S255` line is a package defect the L1
  inherits only if it admits the entry.
- No gate was run by this seat (source-opening item; gates are the L1's post-integration step), and no
  tool was installed or upgraded.

## 10. Files written

- `.ufo/waves/round-72/snapshots/S255-agent-skills-skill-md.md` — the fetched bytes, 16 035 B,
  sha256 `624f1c7f…94fc` (untracked; L1 commits).
- `.ufo/waves/round-72/w1/build/ExecSrcSpecOnePager/s255-pin.json` — pin record for the counter.
- `.ufo/waves/round-72/w1/build/ExecSrcSpecOnePager/s255-located-quotes.md` — located-quote table with
  dropped bytes.
- This report. Scratch dir `/tmp/k72w1-ExecSrcSpecOnePager.*` deleted before return.
