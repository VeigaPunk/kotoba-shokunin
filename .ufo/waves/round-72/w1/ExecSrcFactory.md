# ExecSrcFactory — source opening for staged row S262 (Factory Droid "Skills")

Seat: ExecSrcFactory (leaf, no dispatch). Assignment: open the source behind staged S262 myself, locate
every sentence the staged row or the citing knowledge entry quotes, snapshot the fetched bytes, and give a
per-claim verdict. Access date for every fetch below: **2026-10-25**.

## Verdict

**S262 opens cleanly and its two headline quotes are verbatim today — but the staged URL is stale by two
redirects, the row's "three ways" framing is narrower than the page's own five-surface table, and the
citing entry's "middle" clause is the lane's inference, not Factory's wording.**

- Row quote 1 (`Use skills when instructions are too specific for always-on AGENTS.md`) → **located,
  verbatim prefix** of snapshot `S262-factory-droid-skills.md:9`.
- Row quote 2 (`Create reusable SKILL.md workflows … share across projects.`) → **located, verbatim
  whole line**, `:3`.
- Row item 3 (install path `.factory/skills/`) → **located**, `:17`, but it is one of nine scope roots
  the page lists (`:193-203`), not the install path as such.
- Entry claim "and, in the same sentence, too structured for a one-off prompt" → **confirmed**, same
  line `:9`.
- Entry claim "A skill is what belongs in the middle" → **not a source sentence**; Factory never writes
  "middle" or "rung". Lane inference, and the page's own ladder has five rungs, not three.
- Staged URL `https://docs.factory.ai/cli/configuration/skills` → **308 → 308 → 200** at
  `https://docs.factory.com/harness/skills`. Content still serves every quote. This is link rot on the
  host+path, **not** a content change (the `.md` export served from both forms is byte-identical).
- `opened: 2026-10-23` in the staged row → **unverifiable from the source** (the page carries no
  publication date; only the fetch `date` header). Addendum §10 holds: the package's date proves nothing,
  and nothing in this report depends on it — every quote was re-opened today.

## Snapshot identity (committed under `.ufo/waves/round-72/snapshots/`)

| file | bytes | sha256 |
|---|---|---|
| `S262-factory-droid-skills.md` | 17567 | `81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9` |
| `S262-factory-droid-skills.html` | 341251 | `1e8f1ec7da7618770966e2490c05c56248dba396f2641f8e13beecf8ccfa0a58` |
| `S262.sha256` | 192 | manifest: the two lines above, row-scoped so no sibling seat's manifest collides |

The `.md` is the page's own markdown export (MDX source with `<Steps>`/`<Tip>` components, 354 lines,
served `text/markdown` from a Vercel-hosted Next.js site). The `.html` is the rendered page (183 lines,
RSC payload on line 183). Every quote below lives literally in the `.md` and, after code-span rendering,
in the `.html`.

## Fetch record

```
$ curl -fsSL -A 'Mozilla/5.0' -w 'HTTP %{http_code} FINAL %{url_effective} SIZE %{size_download}\n' \
    'https://docs.factory.ai/cli/configuration/skills' -o page.html
HTTP 200 FINAL https://docs.factory.com/harness/skills SIZE 341251
$ sha256sum page.html
1e8f1ec7da7618770966e2490c05c56248dba396f2641f8e13beecf8ccfa0a58  page.html
```

Redirect chain (`curl -sSIL`, same URL):

```
HTTP/2 308
date: Sun, 25 Oct 2026 21:37:31 GMT
location: https://docs.factory.com/cli/configuration/skills
server: Vercel
HTTP/2 308
location: /harness/skills
HTTP/2 200
content-type: text/html; charset=utf-8
etag: "78816e88f18fd515f448c62850833971"
```

Markdown export — both URL forms resolve to the same bytes:

```
$ curl -sSL -A 'Mozilla/5.0' -w 'HTTP %{http_code} FINAL %{url_effective} SIZE %{size_download} CT %{content_type}\n' \
    'https://docs.factory.com/harness/skills.md' -o a.out
HTTP 200 FINAL https://docs.factory.com/harness/skills.md SIZE 17567 CT text/markdown; charset=utf-8
$ curl -sSL -A 'Mozilla/5.0' -w '…' 'https://docs.factory.ai/cli/configuration/skills.md' -o b.out
HTTP 200 FINAL https://docs.factory.com/harness/skills.md SIZE 17567 CT text/markdown; charset=utf-8
$ sha256sum a.out b.out
81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9  a.out
81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9  b.out
```

## Quote-by-quote location

Line numbers are in the committed `.md` snapshot. Each quote is pasted from `sed -n '<L>p'` output;
dropped bytes are named.

| # | quoted by | sentence | located | section heading | line | quote (pasted) | dropped bytes |
|---|---|---|---|---|---|---|---|
| Q1 | row S262, entry L17 | decision boundary | **yes** | `# Skills` (page lead; the next heading `## Create your first skill` is at `:11`) | `:9` | `Use skills when instructions are too specific for always-on \`AGENTS.md\`, too structured for a one-off prompt, and useful enough to reuse.` (21 words) | none — this is the whole line. The row and the entry truncate after `AGENTS.md`; both drop `, too structured for a one-off prompt, and useful enough to reuse.` The entry also drops the backticks around `AGENTS.md` (formatting only; the rendered page wraps it in `<code>`, `.html:39`) |
| Q2 | row S262 | discover/invoke/share | **yes** | `# Skills` (page lead) | `:3` | `Create reusable SKILL.md workflows that Droid can discover, invoke, and share across projects.` (13 words) | none — whole line; also served as the page's `meta name="description"` (`.html:1`, visible lead paragraph `.html:36`, payload copy `.html:183`) |
| Q3 | row S262 | install path | **yes** | `### Create a skill manually` → `## Create your first skill` | `:17` | `Put team-shared skills under \`.factory/skills/\` in your repository:` (8 words) | dropped: 4-space MDX indent (the line sits inside `<Steps><Step title="Create a skill directory">`, `:15-16`) |
| Q4 | entry L18 | "in the same sentence" | **yes** | same as Q1 | `:9` | `…too structured for a one-off prompt, and useful enough to reuse.` (fragment of the Q1 line) | the entry quotes this clause out of its sentence; it is genuinely the same sentence as Q1 |

Nothing the row or the entry quotes is missing from today's page.

## Claim verdicts (entry `skill-vs-always-on-boundary.md`)

| entry claim | line | verdict |
|---|---|---|
| `Factory: "Use skills when instructions are too specific for always-on AGENTS.md"` | L17 | **confirmed** (verbatim prefix of `:9`; code-span backticks dropped) |
| "and, in the same sentence, too structured for a one-off prompt" | L18 | **confirmed** (verbatim in `:9`) |
| "A skill is what belongs in the middle." | L18-19 | **absent from the source** — Factory uses neither "middle" nor "rung"; this is the lane's inference from the page's ordering (`:110-114`). Must not be quoted as Factory |
| "a skill is for instructions that are too specific to sit in an always-on file and too shaped to be a one-off prompt, and that do not need to be executable integrations" | L49-51 | **confirmed-after-shaping** — clauses 1-2 reshape `:9`; clause 3 ("executable integrations") is **pi (S263)**, not this page. The page keeps `MCP server` as a separate surface (`:114`), which is consistent with the clause but does not state it |
| "It is now stated, in those words, by three of them" (three-rung ladder) | L12-15 | **confirmed-after-shaping** — Factory states three *conditions* in one sentence and a *five*-surface table (`:110-114`), not a three-rung ladder. The reduction to three rungs is the lane's |
| "the 'Skills' page under the Droid harness" (row scope) | row | **confirmed-after-shaping** — `<title>Skills</title>`, `# Skills` at `:1`, final URL `…/harness/skills`. True today; the row's path (`/cli/configuration/`) no longer resolves directly |
| "the clearest first-party statement of the decision boundary between the three ways to give an agent instructions" (row `teaches`) | row | **confirmed-after-shaping, over-narrowed** — the page names **five** surfaces: `AGENTS.md`, `Skill`, `Custom slash command`, `Custom droid`, `MCP server` (`:110-114`) |

## Adjacent located evidence (not part of the staged quotes; for the L1's A4/A1 judgement)

The page carries two blocks the row does not quote that bear directly on C1's rung rule and on the
name-precedence rule. All are `sed -n` pastes from the committed snapshot.

- **Surface table** — `## When to use a skill`, `:106-114`:

  ```
  :110  | `AGENTS.md` | Always-on repository instructions, commands, conventions, and safety rules. |
  :111  | Skill | Reusable workflow Droid can choose or the user can invoke. |
  :112  | Custom slash command | Simple user-invoked prompt or executable shortcut. |
  :114  | MCP server | External tools and services Droid can call. |
  ```

  Clean word counts (`sed -n '<L>p' … | sed -E 's/[|`*]//g' | wc -w`): `:110` 9, `:111` 11, `:112` 9 —
  the first token of each is the surface name, so the sentences alone are 8, 10 and 6 words. All are
  registry-quote-sized (5-25 words). This is a vendor stating
  the always-on / skill / prompt boundary as three distinct surfaces — the closest thing on the page to the
  lane's ladder, and it names two surfaces the lane's ladder omits (custom droid, MCP server).

- **Progressive disclosure (the resident index, without the word "index")** — `## Discovery and loading`,
  `:143-147`:

  ```
  :145  Droid uses progressive disclosure so skill bodies stay out of context until needed:
  :147  1. **Discovery:** Droid finds `SKILL.md` files and reads each skill's `name` and `description`.
  ```

  `:145` is 13 words; `:147` is 12 words. **The page never uses the word `index`** — `grep -n -i index
  S262-factory-droid-skills.md` returns nothing. So S262 can source the *rung* and the *resident-portion*
  idea but **cannot** source A4's `index` token; that token has to come from Vercel/Chroma/S255, as the
  entry `context-rot-and-always-on-context.md` already argues.

- **Resolution precedence (A1-adjacent)** — `### Resolution precedence`, `:207-227`:

  ```
  :209  When multiple sources provide the same sanitized skill name, Droid keeps one effective
  :210  version and shows the others as overridden.
  :226  If two skills in the same source share a name, Droid ignores one of them and
  :227  `/diagnostics` reports the ignored copy. Rename or remove the duplicate.
  ```

  `:209-210` is 20 words; `:226-227` is 20 words. A1 is frozen to the round-69 entry, so this cannot be
  cited for A1 — but it is a second vendor corroborating that a same-named skill is silently overridden,
  and it is the sharpest statement the lane has that a duplicate inside one source is *dropped*, not
  merged.

- **Invocation decision as configuration** — `## Control who invokes a skill`, `:267-278`: the page makes
  the rung-two/rung-three boundary an explicit per-skill switch (`disable-model-invocation: true`,
  `user-invocable: false`, `enabled: false`, `:271-274`). The citing entry says that boundary "is the
  invocation decision, and it fails more often than anything else the lane has measured"; Factory's
  answer is to make it declared metadata rather than model judgement. Useful for the round-72 lesson.

## Findings

**F1 — the staged URL is two redirects stale; the canonical URL moved host *and* path.** Command and
output in the fetch record above: `308 → https://docs.factory.com/cli/configuration/skills`, then
`308 → /harness/skills`, then `200`. If the L1 appends S262 verbatim, the registry's `source` cell will
carry a URL that never returns 200 on its own. **Recommendation:** register the canonical
`https://docs.factory.com/harness/skills` (the `.ai` host is retained only as a redirector; its `.md`
form redirects too). Host+path for duplicate detection: **`docs.factory.com` `/harness/skills`**
(formerly `docs.factory.ai` `/cli/configuration/skills`).

**F2 — no lane duplicate.** `grep -rn "S262\|factory.ai\|factory.com" corpus/SOURCES.md corpus/knowledge/
SKILL.md` → no output. `grep -ril "factory" --exclude-dir=.ufo --exclude-dir=.git .` → only
`verifiers/verify_surfaces.py:624` (`1.19.4 renamed the key factory from Key.make to …` — an unrelated
prose use of the word). Lane registry max id is `S213`
(`grep -o '^| S[0-9]\{3\}' corpus/SOURCES.md | sort -u | tail -3` → `S211 S212 S213`), so `S262` is free
and no lane row cites Factory. Within the staged package, `grep -n -i factory SOURCES.append.md` returns
only S245 (an `agentskills` client-showcase row, different host) and S262.

**F3 — the staged row's "three ways" framing narrows the vendor's five-surface table.** `:110-114` names
`AGENTS.md`, `Skill`, `Custom slash command`, `Custom droid`, `MCP server`. The `teaches` cell's "between
the three ways to give an agent instructions" is the lane's ladder projected onto the page. Verdict
`confirmed-after-shaping`; the appended row should say five surfaces or say that the row quotes the
sentence, not the table.

**F4 — the entry's "middle" clause is unattributable to Factory.** `grep -n -i "middle"` on
`S262-factory-droid-skills.md` returns nothing; on the `.html` the only 14 hits are the CSS utility
`align-middle` (`grep -o '[A-Za-z-]*middle[A-Za-z-]*' … | sort | uniq -c` → `14 align-middle`), and a
tag-strip of the visible text finds no `middle` at all. The entry's L18-19 sentence must not survive
assimilation as a Factory quotation; the verdict is *absent as a quote / lane inference*. Same for
"three-step instruction ladder" (L12-13) and "rung". Vocabulary absence, measured on the `.md` snapshot:
`rung` 0, `ladder` 0, `three-step` 0, `index` 0, `middle` 0 (`grep -c -i` for each).

**F5 — the `.factory/skills/` install path is one of nine scope roots.** `:193-203` lists Project,
Folder-specific, Personal (`~/.factory/skills/`), Compatibility (`.agents/skills/`, `.agent/skills/`),
Personal compatibility, Mission, Automation, Plugin, Built-in. The row's `.factory/skills/` is the project
root only; a rule that says "the install path is `.factory/skills/`" would be incomplete. If A3
(install-path trust) ever needs Factory, this is the caveat.

**F6 — `opened: 2026-10-23` is unverifiable from the source.** The page exposes no publication or
modified date (headers carry only `date:` = fetch time, `etag: "78816e88…"`). The row's date is the
package's assertion. Every quote here was re-opened 2026-10-25, so the content claim stands independently.

**F7 — the entry cited by the assignment for cross-check, `context-rot-and-always-on-context.md`, does
not cite S262 at all** (its `source:` lines are S254 and S248, L4-5). It also has a provenance gap of its
own: the body cites **S255** (L27) and **S256** (L29) with no `source:` line for either — if the L1
assimilates that entry, C1(c)'s "opens with `source:` lines naming every cited id" would fail as written.
Only `skill-vs-always-on-boundary.md` cites S262 (`grep -rln "S262" knowledge/` → that one file).

**F8 — quote forms.** The quotes live in **both** forms: literally in the `.md` export (backticks intact)
and in the rendered page with code spans (`.html:39` for Q1, `.html:36` for the lead sentence, `.html:42`
for the install-path step, `.html:1` for the meta description, `.html:183` for the RSC payload copy). For
C1(d)'s word-bounded snapshot check, the `.md` is the right artifact: Q1 and Q2 each appear twice in the
`.html` (visible markup + flight payload; Q2 a third time in `<meta>`), which would make a naive
`count == 1` assertion fail.

## Risks / blockers for the L1

1. **C1(d) snapshot pinning:** the snapshot directory now holds `S262-factory-droid-skills.md`,
   `S262-factory-droid-skills.html`, `S262.sha256`. If A4 cites S262, the quote cell must be one of the
   `:9`, `:110`, `:111`, `:112`, `:145`, `:147`, `:209-210`, `:226-227` strings (all 5-25 words), and the
   snapshot sha256 must be pinned to `81409d89…` (`.md`) — the `.html` copy is the same content but
   duplicate-occurrence-bearing.
2. **A4's `index` token cannot be sourced from S262** (zero occurrences of "index"). Do not cite S262 for
   it; the entry `context-rot-and-always-on-context.md` carries that half.
3. **Registry URL:** use `https://docs.factory.com/harness/skills`, not the staged `.ai` path, or record
   both with the redirect noted.
4. No blocker on the row's tier (`B`, one vendor's implementation) or kind (`docs`).

## Hygiene

- Scratch `/tmp/k72w1-ExecSrcFactory.iSkZ` created for the fetches and deleted before return.
- Writes made: the three files under `.ufo/waves/round-72/snapshots/` (the one permitted committed-file-
  shaped write) and this report. No lane file, no fleet file, no `shokuknow` write, no git or jj
  mutation, no gate run.
- Tools installed or upgraded: **none** (curl, sha256sum, sed, grep, wc were sufficient).
