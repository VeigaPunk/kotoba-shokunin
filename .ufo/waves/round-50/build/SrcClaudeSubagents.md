# Round-50 seat report — SrcClaudeSubagents (C1 frontier source row; id assigned by the L1 at integration)

**ROW DRAFTED — the Claude Code subagents page opens by ordinary means (HTTP 200, `.md` variant
served), it states that the `description` field is what Claude matches a request against to
decide delegation, and it documents NO tie-break between two descriptions that both match; the
new row validates clean under the fleet instrument.**
Id: per L1 instruction the delivered row carries the placeholder `S0NN`; the contract check ran
under the temporary id `S099` (the L1 must replace it — `S0NN` itself fails E02, which requires
`S[0-9]{3,}`). Lane base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. Read-only on the lane;
only this report was written there. Fetching and mirroring happened in
`/fast/scratch/hyaku/kotoba-r50/build/src-claude-subagents/`.

## Findings

**F1 — Fetch record.** The `.md` variant is served: `https://code.claude.com/docs/en/sub-agents.md`
answers **HTTP 200**, `content-type: text/markdown` (110,784 B, 1,480 lines). The HTML route
answers **HTTP 200** (1,334,165 B) with the same prose. Each route was fetched twice; the two
fetches are byte-identical (`cmp` exit 0).

| route | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://code.claude.com/docs/en/sub-agents | 2026-10-22T12:28:26Z | 200 | 1,334,165 | `31baba2df4a0e54ad2e0a8a4651f9bb84ae96adcfe9851993ef4b740985cdc7b` |
| https://code.claude.com/docs/en/sub-agents.md | 2026-10-22T12:28:30Z | 200 | 110,784 | `89aa73eb3f28e274650634620113a19585dd09b7f40be3dd16d584800cb60aed` |
| same `.md` route, second fetch | 2026-10-22T12:31:21Z | 200 | 110,784 | `89aa73eb…` (identical) |

Header on the `.md` route (`curl -D -`): `last-modified: Thu, 22 Oct 2026 12:31:14 GMT`,
`x-vercel-cache: HIT`, `x-matched-path: /_mintlify/_markdown/_sites/[subdomain]/[[...slug]]` — the
page is rendered per request, so `last-modified` tracks the fetch, not an edit; it is **not** a
content-vintage signal and is not cited as one. Freshness is evidenced by the page's content
instead: it documents behaviour gated on Claude Code **v2.1.304** (`sub-agents.md:1130`), the
highest version string on the page.

**F2 — (a) How the `description` field decides delegation.** Four located statements, verbatim,
each ≤25 words:

- § Create custom subagents, intro (`sub-agents.md:11`): "When Claude encounters a task that matches a subagent's description, it delegates to that subagent, which works independently and returns results."
- § Create custom subagents, intro (`sub-agents.md:25`): "Claude uses each subagent's description to decide when to delegate tasks."
- § Frontmatter reference, `description` row (`sub-agents.md:299`): "When Claude should delegate to this subagent"
- § Work with subagents → § Understand automatic delegation (`sub-agents.md:839`): "Claude automatically delegates tasks based on the task description in your request, the `description` field in subagent configurations, and current context."

The matching inputs are the request's own task description, the subagent `description` field, and
current context — the `description` is one input among three, not a sole matcher.

**F3 — (b) Plain answer: the page documents NO tie-break between two subagents that both match.**
The sweep below is the negative evidence (Q14). The only arbitration the page states is over
**identity**, not over **matching**:

- § Choose the subagent scope (`sub-agents.md:156`): "When multiple subagents share the same name, Claude Code uses the one from the higher-priority location."
- Location priority table (`sub-agents.md:158-164`): managed settings 1 (highest), `--agents` CLI 2, `.claude/agents/` 3, `~/.claude/agents/` 4, plugin `agents/` 5 (lowest).
- § Choose the subagent scope, same directory (`sub-agents.md:176`): "Claude Code loads only one of them, chosen by filesystem read order rather than a documented precedence." — the page itself says there is **no** documented precedence there.
- § Managed subagents (`sub-agents.md:228`): "Managed definitions take precedence over project and user subagents with the same name."
- § Invoke subagents explicitly → plugin scoping (`sub-agents.md:890`): "If multiple plugins provide agents with the same name, pass the scoped name to disambiguate:"

Every one is a *same-name* collision resolved by file location or scope. Nothing says which of two
**different** subagents wins when both descriptions match a task: no word for overlap, ambiguity,
tie-break, conflict, or priority of match. The page's own answer to overlap is a craft instruction,
not a rule — § Example subagents → Best practices (`sub-agents.md:1293`): "Make each description specific enough to route to the right subagent" (bullet head: "Write descriptions that single out one subagent").

**F4 — Consequence for C1 and D3.** (i) The vendor's routing model is description-specific matching
with no arbitration rule — the same finding S022/S023 carry for skills: with no documented
tie-break, the only lever a description author controls is the text of each description, so naming
the sibling lane and saying who owns what is the whole mechanism. That is the craft argument for
C1's edit. (ii) For D3, the round-50 precedence ruling between the `contested` arm and the stated
split must be stated as **kotoba's own rule**: this page, like S022/S023, supplies no vendor rule
to borrow.

**F5 — Skills-relevant facts on the same page (adjacency, not skill routing).** § Frontmatter
reference, `skills` row (`sub-agents.md:306`): "The full skill content is injected, not only the description."; § Preload skills into subagents (`sub-agents.md:624`): "The full content of each listed skill is injected into the subagent's context at startup, up to the first 32 distinct names in the list." Neither arbitrates between two matching **skills**; that subject stays S022's.

**F6 — Description budget on this surface.** No character cap on a subagent `description` appears
(`1024` → 0 hits); the only cap stated is on `name` (`sub-agents.md:298`): "Unique identifier of at most 256 characters". The budget is a combined-token one — § Create custom subagents (`sub-agents.md:27`): "When the combined descriptions of your subagents, except the built-in ones, exceed 15,000 tokens"; and § Understand automatic delegation (`sub-agents.md:841`): the warning fires "and still loads every subagent". kotoba's own frontmatter `description` measures **815 characters** by YAML parse (847 with the four missing lane names added) — inside any budget this page states.

**F7 — New row, id free, contract-clean.** `grep -c '^| S0' corpus/SOURCES.md` → **23** (exit 0);
`grep -ci 'sub-agents' corpus/SOURCES.md` → 0 (exit 0, no match) and `grep -rn 'code.claude.com/docs/en/sub-agents' corpus/` → no hit (exit 1), so this is a **new row**, not a re-open. Drafted in a private clone of the lane (`.../src-claude-subagents/lane`, at `f3046466`) and checked with the fleet instrument `scripts/sources-census.sh validate --file …`: unmodified lane registry → exit 0, `ok`, three pre-existing W04 (S018, S019, S021); mirror with the draft row appended → exit 0, `ok`, the same three W04, **no E-code and no new warning** for the drafted id; the drafted line splits into **13 pipe-separated fields** (NF=13), matching every existing row and the header.

## Deliverable 1 — `corpus/SOURCES.md` row (append after the last row, before `## Paths`)

```markdown
| S0NN | Claude Code — Create custom subagents — https://code.claude.com/docs/en/sub-agents | docs | A | Claude Code's documented delegation rule for subagents (the `description` field decides delegation) and what the page says when two subagents collide (vendor documentation, not a measurement of omp or opencode) | § Frontmatter reference, `description` row (`sub-agents.md:299`); § Understand automatic delegation (`sub-agents.md:839`); § Choose the subagent scope, same-name and priority paragraphs (`sub-agents.md:156`, `:176`); § Example subagents → § Best practices (`sub-agents.md:1293`); fetched as https://code.claude.com/docs/en/sub-agents.md (200, 110784 B, sha256 `89aa73eb…`) on 2026-10-22T12:28:30Z; the HTML route (200, 1334165 B, sha256 `31baba2d…`) serves the same prose and did not redirect | The `description` is one of three matching inputs (request text, description field, current context) Claude Code uses to decide delegation, and the page's answer to two matching descriptions is specificity, not arbitration — "Make each description specific enough to route to the right subagent" (`:1293`); the only precedence it documents is over same-`name` subagents (location priority table, `:158-164`), and even there two files in one directory are chosen "by filesystem read order rather than a documented precedence" (`:176`); it states no rule for two descriptions that both match (sweeps: `overlap` 0, `tie[- ]?break` 0, `conflict` 0, `multiple skills` 0, `prioriti` 0 over the fetched 110,784 B) | mined | 2026-10-22 | 90d | SKILL.md, corpus/knowledge/sibling-overlap-census-round49.md |
```

Rows 23 → 24 after landing. Landing constraint (not mine to land): `used-by` names `SKILL.md` and
`corpus/knowledge/sibling-overlap-census-round49.md`, so the census entry's appended section that
cites this row and the C1 description edit must land in the same landing as the row, and the
citation must use the id the L1 assigns (a dangling id would be an E11-class defect).

## Deliverable 2 — round-lesson `## Gate` access-record line

```markdown
| S0NN | https://code.claude.com/docs/en/sub-agents | 2026-10-22T12:28:30Z | "When Claude encounters a task that matches a subagent's description, it delegates to that subagent, which works independently and returns results." (§ Create custom subagents, `sub-agents.md:11`) — seat `.ufo/waves/round-50/build/SrcClaudeSubagents.md` |
```

Reserve quote for the tie-break half (17 words, verbatim, § Choose the subagent scope, `sub-agents.md:176`): "Claude Code loads only one of them, chosen by filesystem read order rather than a documented precedence."

## Evidence (commands, exit codes, paths)

Sweep (Q14 negative evidence) — `for t in …; do grep -ciE "$t" fetch_md_1; done`, file =
`/fast/scratch/hyaku/kotoba-r50/build/src-claude-subagents/fetch_md_1` (110,784 B, 1,480 lines, sha256 `89aa73eb…`):

```
overlap          0
ambigu           1
precedence       6
tie[- ]?break    0
conflict         0
multiple skills  0
same name        4
prioriti         0
1024             0
truncat          2
```

Every non-zero count is located, and none is a tie-break rule: `ambigu` 1 → `:890` "pass the scoped name to disambiguate:" (plugin **name** collision); `precedence` 6 → `:176` (the sentence saying there is *no* documented precedence), `:228` (managed over project/user, same name), `:316` (prompt-cache lifetime), `:390` (`CLAUDE_CODE_SUBAGENT_MODEL`), `:417` (effort level), `:604` (permissions among rules/hooks/mods); `same name` 4 → `:156`, `:176`, `:228`, `:890` — all identity collisions, none about matching; `truncat` 2 → `:709`, `:1454` — SQL `TRUNCATE` in example shell snippets. Near-miss variants checked so the negative is not a pattern artefact: `priorit` 3 (`:156` "higher-priority location", `:158` the table header "Priority", `:1326` "Provide feedback organized by priority"), `priority` 3, `ambig` 1, `overlap(s|ping|ped)` 0, `1024|1,024` 0 — the page has no priority word in the matching sense either.

The same ten patterns over the HTML route (`fetch_html_1`, 1,334,165 B): `overlap` 2, `ambigu` 2, `precedence` 8, `same name` 5, `conflict` 1, `1024` 4, `truncat` 6, `tie[- ]?break` 0, `multiple skills` 0, `prioriti` 0 — the extra hits are site chrome, not prose (`overlap`: a CSS comment on the panels at HTML `:1505` and the JS bundle at `:2477`; `conflict`: JS bundle `:2477`; `1024`: `@media (min-width: 1024px)` `:1024`/`:1046`; `truncat`: `:112`, `:1631`, `:1942`, `:2457`, `:2476`, `:2477`). The `.md` route is the swept and quotable text.

Quoted lines read with `sed -n '<n>p'` on the fetched `.md`: 11, 25, 27, 156, 158-164, 176, 228,
298, 299, 306, 624, 839, 841, 890, 1293.

Registry facts — `grep -c '^| S0' corpus/SOURCES.md` → 23 (exit 0); `grep -ci 'sub-agents' corpus/SOURCES.md` → 0 (exit 0, no match); `grep -rn 'code.claude.com/docs/en/sub-agents' corpus/` → no hit (exit 1).

Validation — `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md` (lane, unmodified) → exit 0, `ok`, W04 × 3 (S018, S019, S021). Same instrument on the scratch mirror with the draft row appended (temporary id `S099`) → exit 0, `ok`, the same three W04, no E-code, no new warning; draft line NF=13.

C1 counter on the lane base (read-only `git show`) → **5**, matching the plan's before-value:
`git show f3046466:SKILL.md | awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f' | grep -oiwE 'chousa|kagi|kake|kama|kasegi|kengaku|kotodama|kumitate|tameshi' | sort -u | wc -l` → `5` (exit 0).

Description length — Python `yaml.safe_load` of the lane `SKILL.md` frontmatter → 815 characters; 815 + 32 for the four missing lane names → 847.

## Out of scope

- Editing `corpus/SOURCES.md`, `corpus/lessons/round-50.md` or the census entry: this seat delivers drafts only (read-only lane bound; the L1 integrates).
- The D3 precedence ruling itself: this source shows there is no vendor rule to borrow, so the ruling must be stated as kotoba's own — the ruling's text belongs to the D3 seat.
- Skill-vs-skill arbitration between two matching skills: that subject is S022's; this page documents subagent delegation and only mentions skill preloading.
- Measuring omp's or opencode's real arbitration; the scope cell says this row is vendor documentation, not a measurement of omp or opencode.
- Other Claude Code pages (the skills page itself, agent-teams, workflows): the sweep's negative claim covers this page only.

## Artifacts

- `/fast/scratch/hyaku/kotoba-r50/build/src-claude-subagents/fetch_md_1` — the swept, quotable text (110,784 B, 1,480 lines, sha256 `89aa73eb…`); `fetch_md_2` — second fetch, byte-identical.
- `/fast/scratch/hyaku/kotoba-r50/build/src-claude-subagents/fetch_html_1`, `fetch_html_2` — the two HTML fetches (1,334,165 B, sha256 `31baba2d…`); `headers_md.txt` — the `.md` response headers.
- `/fast/scratch/hyaku/kotoba-r50/build/src-claude-subagents/lane/` — private clone of the lane at `f3046466` with the draft row appended (mirror only; the real lane was not touched).
- `/fast/scratch/hyaku/kotoba-r50/build/src-claude-subagents/draft_row.md`, `draft_gate_line.md` — the two deliverables as files; `sweep.txt` — the ten sweep counts with the command per line.
- `/fast/scratch/hyaku/kotoba-r50/build/src-claude-subagents/patch.diff` — `git -C lane diff f3046466 -- corpus/SOURCES.md` (12 lines, 1 insertion) with the row under the temporary id `S099`; the L1 must substitute the assigned id before landing.

## Tooling

None installed or upgraded this session; `curl`, `grep`, `sed`, `cmp`, `sha256sum`, `date`, `git`,
`python3` (stdlib `yaml`) and the fleet's `scripts/sources-census.sh` were already present. No
`pacman`, `uv tool`, `cargo` or `npm -g` transaction was run, and no host service was restarted.
