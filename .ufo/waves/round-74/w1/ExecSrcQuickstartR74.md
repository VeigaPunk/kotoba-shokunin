# ExecSrcQuickstartR74 — C1 source opening: the Agent Skills quickstart page

**Verdict.** The page is open, groundable and usable as a C1 source: fetched 2026-10-25 (`.md` form, HTTP 200,
4 080 B, sha256 `7c480b44…c32bffb`), equal to upstream docs/skill-creation/quickstart.mdx at
agentskills/agentskills@`69ef37e9424c0a7ea9dd2293b559e43ec8176379` after a documented six-class markup
mapping, and carrying **12 author rules, 10 of which hold ≥2 usable tokens**, so it clears the C1 Q45 bar with
margin. Its registry row is drafted. Two findings block a naive landing: **the staged S237 row overreads the
page** (one claim refused on an observed absence), and **two plan/predicate mismatches will make the C1 counter
fail by construction if followed literally** (drafted status vs the predicate's required status; snapshot path).
Those are L1/counter-seat decisions, not blockers on the source.

Base `1e03d19`; plan `329e7d9`; lane kotoba-shokunin; every command below ran 2026-10-25 (`date -I` →
`2026-10-25`). Seat paths are rooted at `.ufo/waves/round-74/w1/`.

## 1. What was opened (evidence)

```
curl -sL --max-time 60 -A 'Mozilla/5.0' -o page_quickstart_md.raw \
  -w 'http=%{http_code} final=%{url_effective} bytes=%{size_download}\n' \
  https://agentskills.io/skill-creation/quickstart.md
-> http=200 final=https://agentskills.io/skill-creation/quickstart.md bytes=4080

same curl against https://agentskills.io/skill-creation/quickstart   (no .md)
-> http=200 final=https://agentskills.io/skill-creation/quickstart bytes=271472

sha256sum page_quickstart_md.raw
-> 7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb

wc -lc page_quickstart_md.raw
-> 83 4080
```

No redirect in either form; the HTML form (271 472 B) carries the same two sentences —
`grep -c 'agents/skills/'` → 4, and the literal `VS Code looks for skills in <code>.agents/skills/</code> by default`
plus `Roll dice using a random number generator` are present in the HTML.

Snapshot: the fetched bytes saved verbatim as the seat's snapshot file (4 080 B) with the pin in its
`.sha256` companion, both under the seat build dir `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/`.
Nothing was reshaped (predicate (d) locates quotes after whitespace collapse only).

### Upstream source file and its commit

```
git ls-remote https://github.com/agentskills/agentskills refs/heads/main
-> 69ef37e9424c0a7ea9dd2293b559e43ec8176379	refs/heads/main

api.github.com/repos/agentskills/agentskills/commits?path=docs/skill-creation/quickstart.mdx&per_page=3
-> 8aeff47 2026-04-19 "Remove link to `what-are-skills.mdx` from `quickstart.mdx`"
   d7dba49 2026-03-23 "Replace `shuf` with `$RANDOM` in quickstart for broader compatibility"
   3fccd70 2026-03-16 "Add quickstart guide for skill creators"

api.github.com/repos/agentskills/agentskills/compare/8aeff47...69ef37e
-> status ahead, ahead_by 36, behind_by 0

raw .../69ef37e/docs/skill-creation/quickstart.mdx -> http=200, 3844 B, sha256 a6614e81…d12d8489db
raw .../8aeff47/docs/skill-creation/quickstart.mdx -> http=200, 3844 B, sha256 a6614e81…d12d8489db
```

**Is `69ef37e` still the head of the docs path?** Yes. It is the repository's `refs/heads/main`, and the path
itself has not been touched since `8aeff47` (2026-04-19), which the compare call shows to be an ancestor of the
head with 0 commits behind; the file's bytes are identical at both commits. The S212/S213 registry anchors at
agentskills/agentskills@`69ef37e` therefore still name today's bytes.

**Does the page text equal the upstream mdx modulo markup?** Yes, and the check is reproducible: a normaliser
rebuilt the site form from the mdx by six markup-only classes — frontmatter `title:`/`description:` became
`# Quickstart` plus a blockquote; the site's three-line Documentation-Index blockquote (site chrome) was
prepended; `<Note>…</Note>` became `> [!NOTE]` callouts; list markers `- ` became `* `; the fence info string
gained ` theme={null}`; site-relative links became absolute `.md` URLs. The rebuilt text then compared equal
to the fetched page:

```
NORMALIZED_EQUAL: site page text == upstream mdx after the documented markup mapping
sha256sum mdx_as_site.md page_quickstart_md.raw
-> 7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb  <both files, same hash>
```

Raw `diff mdx page` reports 41 changed lines, every one of them one of the six classes. The claim recorded is
therefore: the page text equals the mdx modulo those six markup classes, the normalised files are byte-equal.
I do not call the page itself `byte-exact` against the mdx.

## 2. The author rules (12; full table with dropped bytes and tokens in `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/rules.md`)

Each quote was produced with a `sed -n 'Np'` read of the snapshot; the bytes dropped per quote are named in
`.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/rules.md`. Line numbers are snapshot lines.

| # | line | quote (≤25 words) |
|---|---|---|
| 1 | 21 | "VS Code looks for skills in `.agents/skills/` by default." |
| 4 | 46 | "A short identifier for the skill. Must match the folder name." |
| 5 | 47 | "Tells the agent when to use this skill. This is how the agent decides whether to activate it." |
| 6 | 26 | "Roll dice using a random number generator. Use when asked to roll a die (d6, d20, etc.), roll dice, or generate a random dice roll." |
| 9 | 58 | "The agent should activate the `roll-dice` skill. It may ask for permission to run a terminal command — allow it." |
| 12 | 68 | "It read only the `name` and `description`, just enough to know when the skill might be relevant." |

The other six, all in `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/rules.md` with an action cell: line 21 sentence 1 (a skill is a folder holding a
`SKILL.md`), line 21 sentence 3 (place it in the project), line 44 ("one file, under 20 lines"), line 55 (verify
with `/skills`), line 62 (model variance explains a silent miss), line 17 (the same skill works in compatible
agents), line 74 (progressive disclosure). Token census for this page, counting distinct backticked spans plus each quoted rule sentence as one token:
10 of the 12 rules hold ≥2 tokens (rules 7 and 10 hold one quoted sentence each), so the Q45 bar for
`quickstart` — a page row with ≥2 tokens — is met with margin.

## 3. Staged claims re-grounded

Staged row S237 (SOURCES.append.md line 41 of the read-only package) is QUARANTINED. Re-read against today's
page:

| # | staged claim | verdict | evidence |
|---|---|---|---|
| G1 | anchor sections "Prerequisites" and "Create the skill" | LOCATED | headings at snapshot lines 11 and 19 |
| G2 | quote "VS Code looks for skills in `.agents/skills/` by default" | LOCATED, 9 words | line 21 |
| G3 | "The same skill works in any compatible agent, including Claude Code and OpenAI Codex." | LOCATED, 14 words | line 17 |
| G4 | "fetched as `.md` 4 080 B on 2026-10-23" | size matches; the 2026-10-23 access is not re-observable | today's fetch is 4 080 B and upstream is unchanged since 2026-04-19, so [INFERENCE] the same bytes |
| G5 | scope: "Its value is one normative default: where a compliant client looks for skills" | **ABSENT — refused** | `grep -c 'compliant'` on the snapshot → 0; the only `default` lines are 21 (subject: VS Code) and 68 ("default skill directories", unspecified). No sentence states a client-neutral root |
| G6 | teaches: "teaches `.agents/skills/` as **the** discovery root" | **over-read — refused as page text** | the page asserts VS Code's default (line 21) and portability (line 17); the cross-vendor status is the lane's own synthesis from four vendor pages, not this page |
| G7 | teaches: the description "names the trigger cases (\"roll a die (d6, d20, etc.)\")" | LOCATED | line 26 |
| G8 | the script-craft entry: the worked description is "one sentence of capability, then a list of the phrases a user might actually type" | example LOCATED (line 26); the "one sentence, then a list" *shape* is [INFERENCE] | line 47 only says the description tells when |
| G9 | the description entry: "the specification's own instance of the rule its optimizing-descriptions page states" | **ABSENT as this page's text** — the quickstart only links there | line 81 is the link; no rule sentence from that page appears here |
| G10 | the script-craft entry: "the same tutorial's skill is written to travel" | LOCATED | line 17 |
| G11 | the script-craft entry: "the specification's own tutorial teaches `.agents/skills/` as the default location" | sentence LOCATED; the possessive "specification's own" attached to the *default* is refused — the sentence's subject is VS Code | line 21; the page's one normative `must` concerns name/folder matching (case-insensitive `specification`/`must` scan → lines 46 and 82 only) |
| G12 | the script-craft entry's script half | not this page | the snapshot has 0 hits for `scripts/`, `500 lines`, `1024`; that half rests on S236 only |

Q62 discipline: G5, G6, G9 and G11 rest on observed absences (a 0-count grep and the two-line `default`
census), never on an assertion about what the tutorial should contain.

## 4. Row draft and landing notes

The seat's `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/row.md` holds the 11-cell row: id placeholder `S<next>` (the lane's highest id at base is `S222`,
so the next free lane id is `S223`; the staged package also uses `S223` through `S390`, so the package side
must be renumbered at import and the lane id never follows package numbering), kind `docs`, tier `A` scoped to
the page's own guidance, anchor = the `## Create the skill` and `## How it works` sections + commit
`69ef37e` + the fetch record (HTTP 200, 4 080 B, sha256, date), teaches = one grounded benefit, `opened`
2026-10-25, recheck `90d`, used-by = the round-74 C1 entry. The anchor quote is 9 words (predicate window
5–25) and the row splits into 11 cells (`awk -F'|'` → 13 fields including the two edges).

## 5. Findings for the L1 and the counter seat (plan attacks)

**F1 — the seat-assigned status contradicts C1 predicate (b).** The draft carries `queued` as this seat's
instruction directs, but predicate (b) requires the page's registry row to be "status `mined`, tier `A`" for
the page to count. Landed as `queued`, the counter rejects `quickstart` by construction; the r73 precedent is
`mined` (`corpus/SOURCES.md:153`, S213, opened 2026-10-25). Decide before any seat scores data: land `mined`, or
amend (b) in a committed addendum (Q28). The conflict is written into the row draft's landing notes.

**F2 — the predicate's snapshot baseline does not exist and is not the seat's path.** `ls` on the round-74
snapshots directory prints `No such file or directory` at base, and predicate (c) names two different
baselines in one sentence (a `.ufo/waves/round-74/` snapshots directory, then "the committed manifest
`snapshots/MANIFEST.sha256`"). The r73 shape settles it: `.ufo/waves/round-73/snapshots/FETCH-LOG.tsv` and
`.ufo/waves/round-73/snapshots/MANIFEST.sha256` beside the per-page snapshots. The L1 must copy my snapshot
bytes (sha256 `7c480b44…c32bffb`, 4 080 B) into the round-74 snapshots dir and pin them there — not re-fetch,
not reshape.

**F3 — a `\b`-wrapped token search reports present tokens ABSENT.** Predicate (a) says tokens are "located
word-bounded in the committed snapshot"; tokens that begin or end with a non-word character fail `\b`.
Observed on the snapshot:

```
'.agents/skills/'    substring=True  \b-wrapped=False  lookaround-word=True
'`/skills`'          substring=True  \b-wrapped=False  lookaround-word=True
'SKILL.md'           substring=True  \b-wrapped=True   lookaround-word=True
'one file, under 20 lines'  substring=True  \b-wrapped=True  lookaround-word=True
```

The quickstart's most natural token, `.agents/skills/`, is exactly the failing class — a `\b` implementation
would make the page unbackable with its own best token, and would also weaken the shortcut-controls world "a
rule token invented and absent from its snapshot" (a punctuation token would read ABSENT even when present).
Use `(?<!\w)tok(?!\w)`, or plain containment after whitespace collapse.

**F4 — predicate (a)'s "exactly one row for `P` in its rule table" makes the 12-rule table unlandable as-is.**
The seat's rules file is raw material for the *entry*, not the entry's table shape: the entry must carry
exactly one quickstart row with ≥2 tokens, so the other rules go in prose or are dropped. Copying the table
wholesale fails (a) by construction.

**F5 — the snapshot is bound to nothing live.** Predicate (c)/(d) read committed bytes only, so a snapshot and a
matching manifest written in the same commit pass without the page ever having been fetched; the plan's shortcut
control only covers "a snapshot hand-edited with the manifest hash left". The honest bindings are the row's
anchor carrying the fetch's byte size, sha256 and date (done), plus a named wave-2 seat that re-fetches. Record
this as a stated bound (Q51), not a counter defect.

**F6 — routed item 5 and C1 can double-count one `SKILL.md` row.** The plan folds "one decision row on the
cross-vendor `.agents/skills/` root" into `SKILL.md` as a routed item *not* counted, while predicate (e) counts
`SKILL.md` rows carrying a snapshot token — and `.agents/skills/` is the token both would use. Either the
routed row uses a different token, or the L1 records that the two are one row and which claim owns it.

**F7 — C1's tier-A scope must not absorb the tutorial's client default.** The page's only normative `must` is
name/folder matching (line 46); everything else is tutorial prose about VS Code. The row's scope is therefore
"the page's own first-skill tutorial … it states no client-neutral discovery root", never a format rule.

## 6. Bounds and non-claims

- Not measured here: whether any rule is true of the page's own client (no VS Code run); whether the guidance is
  good (reviewer judgement); the other two C1 pages (separate seats).
- Live-vs-staged identity of the 2026-10-23 fetch is [INFERENCE] from size equality plus upstream immutability
  since 2026-04-19; the lane stores no 2026-10-23 snapshot of this page (`grep -rn` for the page URL across
  corpus, SKILL.md, PROVINCE.md and README.md → 0 hits).
- No lane file, no byte of the read-only package, no fleet-repo byte was modified. Scratch dir under /tmp was
  deleted; no git write happened anywhere (none was needed); no jj command was run.
- Tooling: none installed or upgraded; no channel used.

## 7. Files written

- `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/snapshot.md` (page bytes, 4 080 B)
- `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/snapshot.sha256`
- `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/fetch-record.md`
- `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/rules.md`
- `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/row.md`
- `.ufo/waves/round-74/w1/ExecSrcQuickstartR74.md` (this report)
