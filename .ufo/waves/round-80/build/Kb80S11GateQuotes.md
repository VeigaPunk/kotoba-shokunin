# Kb80S11GateQuotes — located-quote ledger (kotoba round 80 w1)

Seat: Kb80S11GateQuotes (leaf scribe). Wave: round 80 w1, v2 (64 seats).
Date/access: 2026-10-27. Lane base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`
(HEAD `c2f69d4f7b5887c409d7c3975d6aebc2e312c406`, the r80 plan/freeze commit, is
base+1; every offset below was measured on bytes that hash to the pins).
Scope: every source row this round touches — the six C2 re-opens S226–S231 and the
S232+ rejection rows — with the located quote, the exact snapshot file + line and
UTF-8 byte offset where it occurs, and the access date. Read-only work: no lane
file was edited; outputs are this ledger plus receipts under
`.ufo/waves/round-80/build/`.

Two quote layers exist for S226–S231 and both are verified here:

- **Source-row quote** — the `located quote "..."` string inside each committed
  `corpus/SOURCES.md` row (lines 167–172 at base; only the `used-by` cell moves
  this round per `Kb80S05SourcesEdits.md`).
- **Entry-table quote** — the string in the r79 row reports (S226–S231), which the
  round-80 entry carries "verbatim" per the Kb80E08C2Entry brief; this is the
  string the C2 counter's (d) conjunct reads.

## 1. Committed snapshots — pins and freshness

Directory `.ufo/waves/round-79/snapshots/` (18 committed files at base: six
snapshots, six `S2xx.fetch.json`, six `S2xx.manifest`; **no `MANIFEST.sha256`** —
see finding F2). Each snapshot's sha256 was recomputed by me and equals its
per-id `.manifest` pin:

| id | file | bytes | sha256 (pin = recomputed) |
|---|---|---|---|
| S226 | S226-spec.md | 7608 | `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` |
| S227 | S227-claude.md | 117962 | `31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9` |
| S228 | S228-factory.md | 17567 | `81409d890cb1b07f6a5a85db19610d4706866e5f4f668d4e26dd032002fed0c9` |
| S229 | S229-msaf.html | 157339 | `34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2` |
| S230 | S230-pi.md | 4793 | `5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5` |
| S231 | S231-vibe.md | 77634 | `fc48a5dbafe572fedd1457cffba8442aacd296dddaf50833ac3104252cb016b0` |

Live re-fetch by this seat around 2026-10-27T23:20Z (`curl -sSL -A
'Mozilla/5.0' --max-time 60`; the `date -u` printed right after the first
four-page batch is 23:20:25Z and the last two pages were fetched immediately
after it, so the bound is the batch instant, not a per-page second):

- S226 (agentskills.io/specification.md), S227 (code.claude.com/docs/en/skills.md),
  S228 (docs.factory.com/harness/skills.md), S230 (pi-mono raw skills.md) and S231
  (mistral-vibe raw README.md) are **byte-identical to the pins** (same bytes, same
  sha256).
- S229 returns the same byte count (157339) but sha256 `20fd76d8…`, differing from
  the pin only on 4 lines (`diff` lines 161, 209, 216, 3262): a static-asset version
  string (`0.4.03574.8308-9505b1c8` → `0.4.03585.8328-71cc54cb`, twice) and an
  Akamai script/pixel id (`41ddb17` → `41ddb15`, twice). The field row and the
  located quote are unchanged (`allowed-tools` raw hits 1; quote fragment present).
  The pin remains the committed 21:41Z bytes; content-level freshness holds, byte
  identity does not (rotating asset token, not editorial change).

All six pages were fetched originally on 2026-10-27 (fetch records: 21:41–21:43Z);
this seat's access date for every row below is **2026-10-27**.

The round's re-open seat published its receipt as
`.ufo/waves/round-80/w1/Kb80R03ReopenSix.md` (the plan names the path
`.ufo/waves/round-80/w1/Kb80ReopenSix.md` — a file-name difference for the L1 to
reconcile). Its live checks agree with this seat's independent re-fetch: S226, S227,
S230 and S231 (and S228's `.md` route) byte-identical to the r79 snapshots, S229
differing only in the same four instrumentation lines (Akamai beacon token and
static-asset version); it also resolved S230's `main` to `85c2ee3e…` with an
unchanged blob and S231's `main` unmoved at `7bb48f21…`.

## 2. S226–S231 re-opens — source-row quotes (corpus/SOURCES.md)

Word count is whitespace tokens (`" ".join(s.split()).split()`). "Layer" names the
least-shaped view in which the quote occurs: `raw` = exact snapshot bytes;
`view` = the counter's declared text view (HTML: script/style removed, tags→space,
entities decoded; Markdown: backticks deleted, unordered-list marker removed;
whitespace collapsed, empty lines dropped); `view+ticks` = the same view with
backticks kept. "Counter-view" is the index after the counter's own retry rule
(quote as written, else with backticks deleted). All offsets are true UTF-8 byte
offsets; character indices are noted where the r79 reports cite them as "bytes".

**S226** — quote (15 words):
``The optional `allowed-tools` field: A space-separated string of tools that are pre-approved to run Experimental.``
- Layer `view+ticks`: char index 4432, view lines 141–143. Counter view (backticks
  deleted): char index 4267, view lines 139–141, 1 occurrence.
- Raw provenance: anchor line 174 col 0 (``The optional `allowed-tools` field:``),
  byte offset 4586; the quote spans raw lines 174, 176, 177 (blank line 175).
- Raw occurrence of the quote as written: 0 (backticks and `* ` markers intervene).
- Access 2026-10-27.

**S227** — quote (25 words):
`allowed-tools field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval.`
- Layer `view` (backticks deleted): char index 67523, view line 395, 1 occurrence.
- Raw provenance: line 617; the quote's token starts at raw char 68988 = **byte
  69040** (line start, `The ` before it, is byte 69036).
- Access 2026-10-27.

**S228** — quote (22 words):
``` `allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces ```
- Layer `raw`: byte offset 12928, raw line 282, 1 occurrence (counter view: char
  index 12533, view line 207, 1 occurrence).
- Access 2026-10-27.

**S229** — quote (19 words):
`allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations.`
- Layer `view`: char index 3938, view lines 96–98, 1 occurrence.
- Raw provenance: anchor line 818 (`<td><code>allowed-tools</code></td>`), byte
  offset 28413.
- Access 2026-10-27.

**S230** — quote (4 words):
`Experimental pre-approved tool list`
- Layer `raw`: byte offset 3578, raw line 78, 1 occurrence (counter view: char
  index 3430, view line 48).
- Note: this source-row quote carries no `allowed-tools` token and is below the
  entry-row 5-word floor; it is a cell fragment of the row
  ``| `allowed-tools` | Experimental pre-approved tool list |``. The entry quote
  (§3) is the one the C2 counter reads and it does carry the key.
- Access 2026-10-27.

**S231** — quote (6 words):
`user-invocable: true allowed-tools: read grep ask_user_question`
- Layer `view`: char index 37473, view lines 544–548, 1 occurrence. Raw provenance:
  anchor line 724 (`user-invocable: true` + `allowed-tools:` on the next line; the
  string `user-invocable: true` also occurs at line 702, which is why the two-line
  anchor pins 724), byte offset 39434.
- Access 2026-10-27.

## 3. S226–S231 — entry-table quotes (the C2 counter's (d) input)

These are the r79 row-report strings the round-80 entry is instructed to carry
verbatim. All six locate in their pinned snapshots; all are 5–25 words and contain
`allowed-tools`; Q70 is the `quote_location` predicate run on the r79 counter bytes,
which are byte-identical to the published round-80 copy (sha256
`74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`, `cmp` rc=0).

| id | words | layer | location (counter view) | raw provenance | raw occurrences | Q70 (r79 draft) |
|---|---|---|---|---|---|---|
| S226 | 15 | view | char 4267; lines 139–141 | anchor L174, byte 4586 | 0 | pass |
| S227 | 25 | raw | char 67523; line 395 | byte 69040 (char 68988), L617 | 1 | pass |
| S228 | 22 | raw | char 12533; line 207 | byte 12928, L282 | 1 | pass |
| S229 | 19 | view | char 3938; lines 96–98 | anchor L818, byte 28413 | 0 | **fail — "first-heading block (Q70)"** |
| S230 | 6 | view | char 3414; line 48 | anchor L78, byte 3558 | 0 | pass |
| S231 | 6 | view | char 37473; lines 544–548 | anchor L724, byte 39434 | 0 | pass |

Quotes, exactly as in the r79 row reports:

- **S226** (15): `The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental.`
- **S227** (25): ``` `allowed-tools` field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval. ```
- **S228** (22): ``` `allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces ```
- **S229** (19): `allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations.`
- **S230** (6): `allowed-tools | Experimental pre-approved tool list` (the source row writes the pipe escaped as `\|`)
- **S231** (6): `user-invocable: true allowed-tools: read grep ask_user_question`

Access date for all six: 2026-10-27.

## 4. S232–S235 rejection rows (round-80 negative sweep, S05's new candidates)

S05 (`Kb80S05SourcesEdits.md` § 2) claims ids **S232–S235 rejected** and **S236
queued**; the 12 NegSweep clients map to **S237+** at L1 integration. Quotes below
were located by me in pages I fetched myself on 2026-10-27 (bodies copied into
`build/Kb80S11GateQuotes-<slug>.<ext>`; sha256 per row). Offsets are raw byte
offsets/lines of the located span, found through the declared HTML view
(script/style removed, tags→space, entities decoded, whitespace collapsed). Refusal grounds are observed
facts about the fetched bytes (Q62), never statements about what a source "lacks"
in the abstract.

**S232 — Cline, Skills** — `https://docs.cline.bot/customization/skills`
- Fetch: 2026-10-27T23:17:20Z, HTTP 200, **228466 B**, sha256
  `ef602792f4d2074678eadcd39f1d506d604dbed4bbee69df05865792e6c57fdc` (equals S05's
  record).
- Quote (14 words): `Metadata Always (at startup) ~100 tokens per skill name and description from YAML frontmatter`
  — located once, view char 2072, raw bytes **98270–98439**, raw line **446**.
- Observed ground for refusal: the fetched bytes contain **0** case-insensitive
  occurrences of `allowed[-_ ]tools`; the quoted progressive-loading line names the
  skill name and description from YAML frontmatter only.

**S233 — Windsurf Cascade Skills** — `https://docs.windsurf.com/windsurf/cascade/skills`
- Fetch: 2026-10-27T23:17:21Z, HTTP 200, **471336 B**, sha256
  `a7e33f3a12363a33fd96e26e6a26e1d1f412dfc1c2a18d2715eb64f22f7cb85b` (equals S05's
  record). `curl -L` final URL is `https://docs.devin.ai/desktop/cascade/skills`
  (the census URL redirects; the body bytes are the same ones S05 pinned).
- Quote (22 words): `name : Unique identifier for the skill (displayed in UI and used for @-mentions) description : Brief explanation shown to the model`
  — located once, view char 3744, raw bytes **132119–132305**, raw lines **472–475**.
- Observed ground: **0** raw `allowed[-_ ]tools` occurrences; the quoted
  required-frontmatter text names `name` and `description` only.

**S234 — LangChain Deep Agents: Skills** — `https://docs.langchain.com/oss/python/deepagents/skills`
- Fetch: 2026-10-27T23:17:21Z, HTTP 200, **2085218 B**, sha256
  `dfaa7d2bd9a1fabf245bdc9e4b2a61a4ea2bf002a9de497cbae3d945c5ad6b52` (equals S05's
  record).
- Quote (15 words): `They are unrelated to the spec’s allowed-tools field, which pre-approves tools rather than adding them`
  — located once, view char 15471, raw bytes **259811–260016**, raw line **1233**.
- Observed ground: **6** raw `allowed[-_ ]tools` occurrences, all inside this
  contrast sentence; the quote names the field only to disclaim the page's own
  `metadata.include_tools`, so no allowed-tools behavior is stated.

**S235 — anthropics/claude-code issue #18737** — `https://github.com/anthropics/claude-code/issues/18737`
- Fetch: 2026-10-27T23:17:22Z, HTTP 200, **327422 B**, sha256
  `bdf5e6e2cbf5b422dcaed17284382eba10af9a26222b258a381ed454a0cfab1c`. **This does
  not equal S05's anchor** (`7774040f99f84da2b9f26ab7dc0c78973388c84e9e11eabf041a51e2b8c15688`,
  327421 B): the GitHub issue page changed between S05's fetch and mine (see F5).
- Quote (15 words): `The allowed-tools frontmatter field in SKILL.md is only supported when using Claude Code CLI directly.`
  — located once **in my fetched bytes**, view char 3013, raw bytes
  **273965–274160**, raw lines **651–653**.
- Observed ground: the sentence is present in the issue body (my fetch: 40 raw
  `allowed-tools` hits; S05 recorded 58 on its bytes). The refusal rests on S05's
  recorded observation that the cited `platform.claude.com/docs/en/agent-sdk/skills`
  route served an application shell (200, 433168 B, sha256 `6da45f95…`), so the
  quoted sentence could not be re-located in the page it cites; **I did not re-fetch
  that route** and make no claim about it.

Access date for S232–S235: 2026-10-27.

## 5. S236 queued row (context; not a rejection)

**S236 — Claude Code Agent SDK: Agent Skills** — `https://code.claude.com/docs/en/agent-sdk/skills.md`
(same small 28395 B file S05 pinned: sha256
`ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`; my fetch
2026-10-27T23:17:43Z matches it).

- Quote A (23 words): `In SDK sessions, you can pre-approve tools for a project or personal skill with the skill's allowed-tools frontmatter or with the allowedTools option`
  — occurs **once only after a link-stripped view** (`[text](url)` → text, then
  backticks deleted, whitespace collapsed): raw **line 348**, byte **19723** (char
  19713). It occurs **0** times under the counter's declared Markdown view (which
  deletes backticks and list markers but does not strip link markup; raw line 348
  is ``> In SDK sessions, … the skill's [`allowed-tools`](https://…) frontmatter …``).
- Quote B (11 words): `The list pre-approves the named tools rather than restricting the others.`
  — occurs once in unmodified bytes (raw line **389**, bytes **21640–21712**).

S236 is queued, so no C2 claim rests on these quotes this round; the link-stripped
dependence is recorded because it would matter if S236 were promoted (F6).

## 6. S237+ — the 12 negative-sweep rejection rows (client-keyed)

Source: `.ufo/waves/round-80/build/Kb80R01NegSweep.md` (12/12 NEGATIVE, two fetch
passes 2026-10-27T23:13:14Z and 23:13:43–44Z, four grep patterns each). These rows
carry **no located quote by construction**; their Q62 ground is the fetch record
plus the zero-hit count on the fetched bytes. Ids: S05 states the negative-sweep
seat "claims no ids and publishes client-keyed records only, so its rows map to
S237+ at L1 integration".

| client | url | status | bytes | sha256 (pass 1) | `allowed[-_ ]tools` hits |
|---|---|---|---|---|---|
| codex | developers.openai.com/codex/skills → learn.chatgpt.com/docs/build-skills | 200 | 417416 | `e657e0e3fd937024fa6d686b28b6d54f9dfc637279a71eb564e93532d27f3860` | 0 |
| vscode | code.visualstudio.com/docs/copilot/customization/agent-skills → /docs/agent-customization/agent-skills | 200 | 157102 | `4b40d645823df78c69cd55519aa5492262c7738aa197e7ee01e1ebfdb91547af` | 0 |
| opencode | opencode.ai/docs/skills/ | 200 | 71581 | `3dfbef2163f9d05d4606209ba9a22194d5ab4fd74f50d350fd01767870124f6a` | 0 |
| gemini | geminicli.com/docs/cli/skills/ | 200 | 114148 | `b17895012da7cbefb20291d6210a3b016d0680a53d6fbc4eaed703d9b0f98640` | 0 |
| ghcopilot | docs.github.com/en/copilot/concepts/agents/about-agent-skills → /concepts/customizations/agent-skills | 200 | 566781 | `e99da06055ca858c486cec1e834bc7353fb3b93525036ad2e10a032ea8e6eaea` | 0 |
| cursor | cursor.com/docs/context/skills → /docs/skills | 200 | 490061 | `abb0613a5403df0137472a0828e507f1129d939107876b3cf1657a0c703a2f1d` | 0 |
| amp | ampcode.com/docs/customize/skills | 200 | 105308 | `d8a8eeb0b2fa7f9089113d34d1a408bc2e918946432f998803e3f05d3deddc07` | 0 |
| roo | docs.roocode.com/features/skills → roocodeinc.github.io/Roo-Code/features/skills/ | 200 | 71129 | `fe801910f82e07631b3b5af3a2349fd75950eaabeda0280348b51c1aa92753e2` | 0 |
| kilo | kilo.ai/docs/customize/skills | 200 | 138104 | `2ed06ad1c20c546d315c120849e35b6861ece1ec1526da9186ce2f04a5ba7353` | 0 |
| junie | junie.jetbrains.com/docs/agent-skills.html | 200 | 38509 | `a44a510e30445815b2f911fbaa77ca42e8f0504b3c4694507f053eb9425e9d21` | 0 |
| goose | block.github.io/goose/docs/guides/context-engineering/using-skills/ | **404** | 932 | `c5b27efd5464711cad2593489c9d56b6dd3b098428ea52d46fac4e35c4aeba34` | 0 (404 body) |
| hermes | hermes-agent.nousresearch.com/docs/user-guide/features/skills | 200 | 206631 | `6817301c1b1a345c31c0c0f57e512b3f9d20d8fda2744f8757f30b9efae19a85` | 0 |

`amp` pass 2 differs from pass 1 (`2bfc32145ec34fda3cf41796a691beb22863106e7509154a1ee146f7e1c0ca70`)
only in rotating CSP `nonce=` attributes; every other page is byte-identical across
passes. The broad sweep `grep -oiE 'allowed.{0,2}tools'` is 0 on all 12 bodies.

**Independent re-verification of one rejection (codex), required by this seat:**
I fetched the census URL twice myself (batch completed by
2026-10-27T23:14:34Z, the `date -u` printed right after it; `curl -sSL -A
'Mozilla/5.0' --max-time 60`): both **HTTP 200, 417416 B, sha256
`e657e0e3…f3860`**, `cmp` rc=0; final URL `https://learn.chatgpt.com/docs/build-skills`
(301 from the census URL); `allowed[-_ ]tools` hits **0** and
`allowed.{0,2}tools` hits **0**. This reproduces NegSweep's pass records for codex.
Receipt: `build/Kb80S11GateQuotes-codex-reverify.txt`.

Access date for all 12 rows: the fetch records are 2026-10-27 (NegSweep); my codex
re-fetch 2026-10-27.

## 7. Findings

- **F1 (counter seam, S229 Q70).** The r79-draft predicate `quote_location()` on
  the S229 snapshot returns `False — "quote lies in the first-heading block (Q70)"`:
  for `.html` the text view strips tags, so the page's `<h1>` leaves no `#`; the
  first line starting with `#` in the view is a code comment at view line 169
  (`# Auto-approve load_skill and read_skill_resource, but not run_skill_script.`),
  while the quote starts at view line 96. The rule `idx <= first_head + 1` therefore
  rejects a quote that precedes the first literal `#`. S229 has exactly one
  `allowed-tools` occurrence (fetch record), so no alternative quote exists. On a
  verbatim port the measured headline would print 5 of 6 (or mark S229 not backed)
  for a page that does document the field. The published round-80 counter
  (`build/check_allowed_tools.py`, 2026-10-27T23:19Z, sha256
  `74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`) is
  **byte-identical to the r79 draft** (`cmp` rc=0) and reproduces the rejection —
  so this is live for the round-80 bytes, not only for the draft source. Reported to
  Kb80E07C2Counter with the reproduction receipt
  (`Kb80S11GateQuotes-q70-draft.txt`); the counter is not mine to edit.
- **F2 (missing snapshot manifest).** `.ufo/waves/round-79/snapshots/MANIFEST.sha256`
  does not exist at base `398cbe1` or at HEAD `c2f69d4` (`git ls-tree -r` lists 18
  files: six snapshots, six `S2xx.fetch.json`, six `S2xx.manifest`). The r79-draft
  counter hardcodes `MANIFEST = ".ufo/waves/round-79/snapshots/MANIFEST.sha256"` and
  `Repo.manifest()` raises `EnvError` when it is absent ("snapshots are unpinned, so
  (c) cannot be evaluated"). The published round-80 copy
  (`build/check_allowed_tools.py`, sha256 `74e067cc…`) is byte-identical to the r79
  draft, so the gap applies unchanged. At base the draft prints `allowed-tools
  surfaces backed 0 of 6` and exits 1 only because the entry file is absent, so the
  manifest error is latent; once rows exist, (c) cannot be evaluated unless a
  `MANIFEST.sha256` with the six pins is committed (or the counter reads an existing
  manifest path). Reported to Kb80E07C2Counter and Kb80E08C2Entry. Receipt:
  `build/Kb80S11GateQuotes-draft-counter-base.txt` (`exit=1`).
- **F3 (two quote layers disagree in shape).** The S230 source-row quote
  (`Experimental pre-approved tool list`, 4 words, no `allowed-tools`) is a cell
  fragment; the entry quote (`allowed-tools | Experimental pre-approved tool list`,
  6 words, contains the key) is the one the C2 counter's (d) conjunct reads. A
  reader conflating the layers could wrongly conclude S230 fails the 5-word/key
  floor. All six entry quotes pass 5–25 words and all contain `allowed-tools`.
- **F4 (r79 "byte offset" was a character index).** The r79 row report calls 68 988
  a "byte offset" of S227; it is the character index. The true UTF-8 byte offset is
  **69 040** (52 bytes of earlier multibyte characters). This ledger reports true
  byte offsets and notes the character index wherever the r79 report's number is
  cited, so both can be checked.
- **F5 (S235 pin not reproducible; page is dynamic).** My 2026-10-27 fetch of the
  GitHub issue is 327422 B / `bdf5e6e2…`, while S05's record is 327421 B /
  `7774040f…`; token hits differ too (mine 40, S05's 58). The quoted sentence is
  still present once (raw lines 651–653). The row's fetch record is S05's; my
  verification is against my own bytes, and the variance is reported, not smoothed.
- **F6 (S236 quote needs a view the counter does not declare).** The queued row's
  23-word quote occurs only after stripping Markdown links (and backticks); the
  counter's declared Markdown view keeps link URLs, so the quote is found 0 times
  there. S236 is queued, so nothing rests on it this round; if promoted, either the
  quote or the view must change. Receipt:
  `build/Kb80S11GateQuotes-verify-rejections.json` (`S236` row, `view_occurrences:
  0`; link-stripped check printed `occurrences 1` at char 11733).
- **F7 (freshness).** Five of six C2 pages are byte-identical to their pins on
  2026-10-27T23:20Z (batch bound 23:20:25Z); S229's live bytes differ only in rotating asset/Akamai
  tokens and keep the quoted field row. Confirms the snapshot date without
  overstating byte identity.
- **F8 (S230 anchor cites the wrong repository's commit).** The committed
  `corpus/SOURCES.md:171` S230 anchor says pi-mono `main` "resolved to
  `badlogic/pi-mono` commit `7bb48f213ac677f943d5c791199ed3dddf302f00`", but
  `.ufo/waves/round-79/snapshots/S230.fetch.json` records `main` at fetch time =
  `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923`; `7bb48f21…` is the mistral-vibe
  commit recorded in `S231.fetch.json`. Reproduced by reading both fetch records
  (`grep -o` over the two files; the two hashes occur exactly once each, in the
  files named). The anchor cell is not edited this round (frontier/round rule; also
  the M45 pattern) — it belongs in the round-80 lesson as an erratum. The S230
  located quotes and their offsets are unaffected.

## 8. Limits

- Documentary only: no client was installed, loaded or run; "pre-approves",
  "metadata" and "Experimental" are page words, not observed behaviour.
- The six snapshot quotes are verified against committed pinned bytes (S226–S231).
  The S232–S236 quotes are verified against bodies this seat fetched on 2026-10-27
  and copied into `build/`; **no committed snapshot exists for them**, so the
  pinned-bytes standard of §1 does not yet apply to those rows.
- S235's own row fetch record is S05's; my bytes differ (F5). I did not re-fetch
  `platform.claude.com/docs/en/agent-sdk/skills` and rely on S05's recorded
  app-shell observation for that leg only.
- The round-80 entry (`build/allowed-tools-surfaces-round80.md`, revised
  2026-10-27T20:33 local, 24726 B, sha256
  `037c3b61774a0eca7fb88b062f095f54ec3ff2645898273f96cd5d24f4823531`) still
  carries the six source-line quotes and the six row quotes **byte-identical to the
  set verified in §3** (`Kb80S11GateQuotes-entry-crosscheck.txt`, re-run on these
  bytes: `source == verified: True`, `rows == verified: True`, exit 0), so the
  offsets above apply to the entry as published. The revision removed the full-hex
  third-repository citation that an earlier draft carried at line 125 and fixed the
  one-pinned-basename-per-line rule (E08's report); neither change touched a quote.
- No count in this ledger is a pipeline's exit status: every verdict was captured
  as `cmd > file 2>&1; rc=$?`.

## 9. Commands and receipts (direct exit capture)

```
# snapshot pins (all match)
$ sha256sum S226-spec.md S227-claude.md S228-factory.md S229-msaf.html S230-pi.md S231-vibe.md
$ python3 -B Kb80S11GateQuotes-verify.py > Kb80S11GateQuotes-verify.json 2>&1; echo exit=$?
exit=0   # 12 records: sources + entry quote sets
$ python3 -B Kb80S11GateQuotes-verify-rejections.py > Kb80S11GateQuotes-verify-rejections.json 2>&1; echo exit=$?
exit=0   # S232-S235 + S236 quotes in this seat's fetched bodies
$ # r79-draft = published round-80 counter, byte-identical
$ sha256sum /.../round-80/build/check_allowed_tools.py /.../round-79/build/check_allowed_tools.py
74e067cc...  (both)   ; cmp -s ... ; echo $?
0
$ # the same predicate on the published round-80 bytes, S229
$ python3 -c "<import build/check_allowed_tools.py; text_view + quote_location>"
round-80 counter quote_location S229 -> (False, 'quote lies in the first-heading block (Q70)')
$ # r79-draft Q70 predicate on the six entry quotes (import of check_allowed_tools.py)
$ cat Kb80S11GateQuotes-q70-draft.txt
S226 True / S227 True / S228 True / S229 False "quote lies in the first-heading block (Q70)" / S230 True / S231 True
$ python3 -B check_allowed_tools.py --repo <lane> --rev 398cbe1 --work <scratch> > Kb80S11GateQuotes-draft-counter-base.txt 2>&1; echo exit=$?
exit=1   # "allowed-tools surfaces backed 0 of 6" (entry absent; manifest gap latent, F2)
$ git ls-tree -r --name-only 398cbe1 -- .ufo/waves/round-79/snapshots/ | wc -l
18       # no MANIFEST.sha256 at base
$ curl -sSL -A 'Mozilla/5.0' --max-time 60 <six C2 URLs>      # live pins, 2026-10-27T23:20Z
$ curl -sSL -A 'Mozilla/5.0' --max-time 60 <codex URL> x2    # 417416 B, sha e657e0e3, cmp rc=0, 0 hits
```

Receipts (all under `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/`):
- `Kb80S11GateQuotes-verify.py`, `Kb80S11GateQuotes-verify.json` + `.json.rc` (`0`)
- `Kb80S11GateQuotes-verify-rejections.py`, `Kb80S11GateQuotes-verify-rejections.json` + `.json.rc` (`0`)
  (both `.json` files are strict JSON; the command's own exit status is in the
  adjacent `.rc` file, so a parser and the rc can each be checked)
- `Kb80S11GateQuotes-q70-draft.txt` (draft counter sha256 `74e067cc…`)
- `Kb80S11GateQuotes-entry-crosscheck.txt` (entry quotes == verified set, exit 0)
- `Kb80S11GateQuotes-draft-counter-base.txt` (exit 1 at base)
- `Kb80S11GateQuotes-codex-reverify.txt` (independent rejection re-check)
- fetched bodies: `Kb80S11GateQuotes-cline.html`, `-windsurf.html`, `-langchain.html`,
  `-issue.html`, `-agentsdk.md`

VERDICT: All six S226–S231 re-opens are located quote-for-quote at exact UTF-8 byte/line offsets in their pinned snapshots (entry quotes 6–25 words, all containing `allowed-tools`); S232–S235 rejection quotes are located in independently fetched bodies with observed-fact grounds; the 12 S237+ sweep pages carry 0-hit fetch records with codex re-verified by me; two counter seams (S229 Q70 on the draft predicate, missing round-79 `MANIFEST.sha256`) are reported, not repaired.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S11GateQuotes.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S11GateQuotes-verify.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S11GateQuotes-verify.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S11GateQuotes-verify-rejections.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S11GateQuotes-verify-rejections.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S11GateQuotes-q70-draft.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S11GateQuotes-draft-counter-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S11GateQuotes-codex-reverify.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S11GateQuotes-{cline,windsurf,langchain,issue}.html, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80S11GateQuotes-agentsdk.md
