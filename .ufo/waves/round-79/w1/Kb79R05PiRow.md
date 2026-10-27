# Kb79R05PiRow — S230 `pi` source row (C2, wave w1, round 79)

Seat: scriber for C2 source row S230, surface `pi`. Draft only — this seat wrote neither
`corpus/SOURCES.md` nor `corpus/knowledge/allowed-tools-surfaces-round79.md`, and scored nothing on
the C2 counter (it does not exist yet; per the plan the L1 freezes it after w1 before any data is
scored).

## Deliverables

- `kotoba-shokunin/.ufo/waves/round-79/snapshots/S230-pi.md` — raw fetched bytes, 4793 B, 93 lines
- `kotoba-shokunin/.ufo/waves/round-79/snapshots/S230.manifest` — `5b9805525b19…69e5  S230-pi.md`
  (`sha256sum -c S230.manifest` → `S230-pi.md: OK`, rc=0)
- `kotoba-shokunin/.ufo/waves/round-79/snapshots/S230.fetch.json` — the fetch record
- `kotoba-shokunin/.ufo/waves/round-79/build/Kb79R05PiRow.rows.md` — the six required items
  (registry row, entry row, Q53, Q70, reading/label, injection sweep)

## Fetch, verbatim

```
$ URL='https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md'
$ curl -sSL -A 'Mozilla/5.0' --max-time 60 -o pi-1.md -w '%{http_code}' "$URL"
fetch1 time=2026-10-27T21:41:14Z curlrc=0 http=200 bytes=4793 sha256=5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5
fetch2 time=2026-10-27T21:41:14Z curlrc=0 http=200 bytes=4793 sha256=5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5
$ cmp pi-1.md pi-2.md; echo rc=$?
rc=0
```

Two fetches, identical sha256 — the page did not change between them. Snapshot extension `.md`
(raw markdown page). `final_url` = the requested URL: `curl -w '%{num_redirects}'` → 0.

## Revision resolution (the raw URL is a main-branch file, so it moves)

```
$ printf 'blob %s\0' 4793 | cat - pi-1.md | sha1sum          # == git hash-object pi-1.md
19d2bf28910ce49caaaf4dde86d1e96330ca7b31  -
$ curl -s https://api.github.com/repos/badlogic/pi-mono/contents/packages/coding-agent/docs/skills.md?ref=main
{"sha":"19d2bf28910ce49caaaf4dde86d1e96330ca7b31","size":4793,…}   http=200
$ curl -s https://api.github.com/repos/badlogic/pi-mono/commits/main
{"sha":"bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923","commit":{"committer":{"date":"2026-10-27T21:31:47Z"…
$ curl -s 'https://api.github.com/repos/badlogic/pi-mono/commits?path=packages/coding-agent/docs/skills.md&sha=main&per_page=1'
[{"sha":"25cc5c7bf4cbc76b2e134c729eb8d57d521ed749","commit":{"committer":{"date":"2026-09-22T14:48:19Z"}…   http=200
```

So the bytes served are the blob `19d2bf28910ce49caaaf4dde86d1e96330ca7b31` (sha1-verified against
the received bytes and equal to the API's blob sha), inside main head
`bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923`; the path itself last moved at
`25cc5c7bf4cbc76b2e134c729eb8d57d521ed749` (2026-09-22). The page states no revision of its own
(no last-modified, no version).

## Freshness findings (report, do not repair here)

1. **The repository alias moved.** `badlogic/pi-mono` is now canonical at `earendil-works/pi`: the
   API response for the contents call names `html_url: https://github.com/earendil-works/pi/…` and
   `download_url: https://raw.githubusercontent.com/earendil-works/pi/…`. The frozen surface host
   prefix `raw.githubusercontent.com/badlogic/pi-mono` still answers HTTP 200 with **zero**
   redirects, so the frozen predicate is unaffected today; if GitHub retires the alias the pin in
   `.ufo/waves/round-79/snapshots/` keeps the bytes but the URL breaks. The row's anchor cell
   records the alias fact.
2. **The body is unchanged since round 72.** `corpus/SOURCES.md:155` (S215, same URL) records
   `4793 B, sha256 5b980552…` for its 2026-10-25 access — the same byte count and the same sha256
   prefix as today's fetch. The path's last commit is 2026-09-22, so nothing in the served body has
   moved for the whole of rounds 72–79. That is a freshness measurement, not an assumption.
3. **One page, one occurrence.** `grep -c -F 'allowed-tools'` on the snapshot → 1 (line 78).
   Sweep of the whole `packages/coding-agent/docs/` directory at the same commit (44 files fetched
   with `curl -sSL --max-time 45`, batch rc=0, 0 files were 404 bodies, 480 K):
   `grep -l -F 'allowed-tools' *` → `skills.md` only, 1 of 44. So no pi page prints a value form
   for the field — a swept negative, not an assertion.

## The row (draft, 11 cells, `NF=13`; measured on the written file)

```
$ awk -F'|' '/^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|/ {print "NF="NF}' Kb79R05PiRow.rows.md
NF=13
$ awk -F'|' '…NF==13 {…print "id="i" kind="k" tier="t" status="s}'
id=S230 kind=docs tier=B status=mined
```

Opened 2026-10-27, recheck `90d`, used-by `corpus/knowledge/allowed-tools-surfaces-round79.md`.
Tier **B** because the source is one harness vendor's documentation of its own product: it is
authoritative for what *that vendor states* and is not the open specification, so it carries no
conformance claim and (per the plan's surface table) the open-spec row S226 takes tier A. S230 is
free in `corpus/SOURCES.md` (`grep -cE '^\|[[:space:]]*S230[[:space:]]*\|'` → 0) and no S226–S231
row exists yet, so the L1's stitch is the first write. S215 (same URL) is not a duplicate: its
scope is the skill rung and the resident index, this row's is the `allowed-tools` field.

## Entry row draft, and the two mechanics the counter resolved

Row (5 cells, escape-aware parse measured):

| pi | S230 | `allowed-tools`, `pre-approved`, `Experimental` | experimental | located quote "allowed-tools \| Experimental pre-approved tool list" |

Revised 2026-10-27 after the counter seat (`Kb79X01CounterBuild`) reported the amended text view
(`plans/round-79.md` § C2, commits `d9d01c2` + `60ba11f`): for Markdown snapshots the view deletes
every backtick byte, removes a leading unordered-list marker, then collapses whitespace. The quote
is therefore written backtick-free and matches the view (measured `view_hits=1`); the old
backticked form matches nothing in the view (`raw_hits=0`).

- **Hazard 1 — the quote crosses a table-cell delimiter; the counter handles it.** The page names
  the field only inside a markdown table row, so every 5–25-word quote containing `allowed-tools`
  also contains the row's vertical bar, and that character is banned inside a SOURCES cell. The
  draft writes it as the Markdown escape `\|` in the entry cell; measured: escape-aware split
  (`(?<!\\)\|`) → 5 cells, naive `split('|')` → 6. Per the counter seat, the C2 counter splits
  escape-aware and unescapes `\|` → `|` before the (d) comparison, so no further change is needed
  from this side. Kept as a fallback if a later counter compares raw bytes: the same quote on the
  entry's `S230` `source:` line with a literal vertical bar (a `source:` line is not a table row,
  and the round-73 counter's `LOCATED_RE` reads it unchanged).
- **Hazard 2 — `pi` prints the value as words, not as a syntax (measured negative), and that is
  enough.** The amended token rule wants a value-form token. Nothing on this page or in the
  repository paths this seat reached prints a syntax: 44/44 `packages/coding-agent/docs` pages
  fetched at main → token in `skills.md` only (1 of 44); `.pi/skills/` (4 files), `AGENTS.md`, both
  READMEs → 0 hits each (7 fetches, all HTTP 200); `packages/coding-agent/schemas` holds no skill
  schema. The single occurrence's value cell is the descriptive words "Experimental pre-approved
  tool list" — no example value, no list. The counter seat's `token_role` classifies a non-key,
  non-grant bare word (`^[A-Za-z][A-Za-z0-9_.@/-]*$`) as the value-form role, so `pre-approved`
  fills it legally and **no L1 relaxation is needed**; the seat added this exact row shape as a
  permanent self-test arm and it scores the honest world 6 of 6. The absence of a syntax stays in
  the entry as content (a declared limit of the pi surface), not as a gap in the row.

### The counter's verification of this row shape (receipt read, not repeated here)

`.ufo/waves/round-79/build/selftest.txt` (4808 B, 2026-10-27 18:57), written by the counter seat:

```
$ sed -n '70p' selftest.txt
PASS S230 row shape: a pipe-bearing table-row quote with a bare word as the value form: exit 0
$ sed -n '1p' selftest.txt
PASS honest world scores 6 of 6: exit 0
$ tail -1 selftest.txt
self-test: 0 failure(s) over 231 assertions in 80 world(s)
```

So under the frozen counter as built, `pi` is backed with the row exactly as drafted (quote
`allowed-tools \| Experimental pre-approved tool list`, tokens `allowed-tools` / `pre-approved` /
`Experimental`, grant `experimental`), and N ≥ 5 is reachable at 6 of 6. This seat measured the
page-side facts above; the counter-side result is the counter seat's, quoted from its receipt.

## Q70 and quote grounding (measured)

```
$ Q='allowed-tools | Experimental pre-approved tool list'      # backtick-free: the amended Markdown view deletes backticks
                                    raw bytes / amended view, grep -c -F "$Q"
S226-spec.md        7608 B          0 / 0
S227-claude.md    117962 B          0 / 0
S228-factory.md    17567 B          0 / 0
S229-msaf.html    157339 B          0 / 0      (html view: script/style removed, tags -> one space, entities decoded)
S231-vibe.md       77634 B          0 / 0
S230-pi.md          4793 B          0 / 1      (own page: the quote exists only in the transformed view)
```

The five siblings are the snapshots already written by the other C2 row seats under
`.ufo/waves/round-79/snapshots/` (same day, same fetch recipe), so this is a check against
committed drafts rather than a re-fetch. The earlier raw-bytes formulation of the same check (with
backticks, and with the five surface URLs fetched directly) also returned 0 on all five.

Quote is 6 words (cap 5–25), lives at line 78 inside § Write portable frontmatter (heading line
67) — not the `# Skills` preamble, not a banner, not repeated on the page. Token counts in the
amended view: `allowed-tools` 1, `pre-approved` 1, `Experimental` 1.

## What the page says / does not say; is `experimental` true

The row sits under "The Agent Skills specification defines these fields:" (line 69) and the page
opens by deferring to the spec ("Pi implements the Agent Skills specification", line 7). The page
says the value is an "Experimental pre-approved tool list" (line 78) and nothing else about it: no
value syntax, no example, no statement that pi enforces, narrows or restricts tools, no scope, no
precedence against `disable-model-invocation`, no behaviour for an unknown tool name, no sandbox
claim. Its only Limits wording is generic — "Most invalid fields produce warnings rather than
stopping startup" (line 7) — and its one security sentence is about project skills, not this field
(line 65). The frozen label **`experimental` is true of the page**: the page's own word is
"Experimental"; no contradicting line exists, so no label change is proposed. Reading in full: § (5)
of `Kb79R05PiRow.rows.md`.

### The value-form negative, with its sweep (added after the counter seat's token rule)

```
44/44 files of packages/coding-agent/docs at main fetched (curl -sSL --max-time 45, batch rc=0,
  0 files were 404 bodies, 480 K): grep -l -F 'allowed-tools' *  ->  skills.md only, 1 of 44
.pi/skills/add-llm-provider.md 3826 B  -> 0     .pi/skills/github-work.md    1327 B -> 0
.pi/skills/interactive-testing.md 930 B -> 0    .pi/skills/release.md        4812 B -> 0
AGENTS.md 8845 B -> 0    packages/coding-agent/README.md 4080 B -> 0    README.md 10635 B -> 0
packages/coding-agent/schemas -> keybindings, models, settings, theme; no skill schema
```

So the only place pi writes the token is `skills.md:78`, and it writes it as a description
("Experimental pre-approved tool list"), never as an example value. No syntactic value form exists
in pi's reachable docs or repo files.

## Injection and credential sweep

`grep -n -iE 'ignore (all|previous)|disregard|you are an? (ai|agent|assistant)|system prompt|curl |wget |run the following|execute the following|api[_-]?key|op://|secret|password|BEGIN [A-Z ]*PRIVATE' S230-pi.md`
→ one hit, line 43, product prose ("adds each skill's name, description, and path to the system
prompt"). Nothing in the page addresses a fetcher, model or tool-runner; nothing was followed. No
credential material, session URL or `op://` reference in the page or in these artifacts. Fetched
pages were treated as data throughout; no command from a page was run.

## Scope, hygiene, and what this seat did not do

- Wrote only: the three `S230*` files under `.ufo/waves/round-79/snapshots/` and
  `build/Kb79R05PiRow.rows.md` (plus this report). No lane file, no `corpus/`, no `MANIFEST.json`,
  no templates/scripts/.ufo/state, no fleet-root file; no lane git/jj mutation of any kind (the
  amended plan text and commits `d9d01c2`/`60ba11f` were read with read-only `git show`/`sed`).
- No tool installed or upgraded; `pacman` not run (host pause honoured); nothing created in any
  PATH directory.
- Scratch `/fast/scratch/hyaku/kotoba-r79/Kb79R05PiRow` removed before yield (trap pattern); the
  only bytes kept are the committed-artifact copies above.
- Not done, deliberately: no scoring on `verifiers/check_allowed_tools.py` (not built yet — wave-1
  seats draft data only); no claim about whether pi *enforces* the field beyond what its docs say
  (no client was installed or run); no sweep of pi docs outside `packages/coding-agent/docs/`.
- For the L1's stitch: `MANIFEST.sha256` needs the pin
  `5b9805525b194474ef1fe5455a0917ef15ed7f710aa9bec2eee11879556469e5  S230-pi.md`, and the entry's
  `verified-at:` must be `2026-10-27` to match the row's `opened` cell (conjunct (e)).
- **Open L1 item (not mine to land, flagged by the counter seat and re-checked here):**
  `.ufo/waves/round-79/snapshots/MANIFEST.sha256` does not exist yet — only the six per-seat
  `S###.manifest` fragments, mine included. I dry-ran the counter seat's merge outside the lane
  (no lane file written): six fragments, all six lines conform to `<sha256>  <basename>`, and
  `sha256sum -c` on the merged content returns `OK` for S226 spec, S227 claude, S228 factory,
  S229 msaf, S230 pi and S231 vibe (rc=0), so
  `cat .ufo/waves/round-79/snapshots/S*.manifest | sort -k2 > .ufo/waves/round-79/snapshots/MANIFEST.sha256`
  is mechanical. Until it lands, the counter exits 2 by design, so no measurement can be scored.

VERDICT: S230 `pi` row drafted, grounded and counter-backed — snapshot 4793 B sha256 5b980552…69e5 (two identical fetches), blob 19d2bf28… at main bb65e3e4…, token once at line 78 and absent from the other 43 pi docs pages and 7 further repo files; quote `allowed-tools | Experimental pre-approved tool list` (6 words, backtick-free, cell written `\|`) matches the amended view once and the other five surfaces' snapshots zero times; `experimental` is true of the page; the counter seat's receipt records this row shape PASS and the honest world 6 of 6 (0 failures / 231 assertions / 80 worlds), so `pi` is backed as drafted; the page prints no value syntax, which is recorded as a surface limit rather than invented.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79R05PiRow.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R05PiRow.rows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S230-pi.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S230.manifest, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S230.fetch.json
