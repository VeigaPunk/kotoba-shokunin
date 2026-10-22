# Round-50 seat report — SrcVSCodeSkills (C1 frontier source row; id assigned by the L1 at integration)

**ROW DRAFTED — the VS Code / GitHub Copilot agent-skills page opens by ordinary means (HTTP 200),
it states the `description` is the field Copilot matches a request against, and it documents
no tie-break between two overlapping skills; the new row (23 → 24 rows) validates clean.**
Id: the L1 assigns ids at integration, so the delivered row carries the placeholder `S0NN`;
`S024` was the next free numeric id at fetch time and is what the contract check was run under.

Scope: open the page myself, record what it says about (a) how the description is used to load a
skill, (b) the description length cap, (c) overlap/precedence rules; sweep the fetched text for
the ten arbitration terms; draft one `corpus/SOURCES.md` row and the round-lesson `## Gate`
access line. Lane base `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`; read-only on the lane, only
this report was written there. Fetching and mirroring in
`/fast/scratch/hyaku/kotoba-r50/build/src-vscode-skills/`.

## Findings

**F1 — The requested URL redirects; the `.md` variant lives at the final route, not the old one.**
`https://code.visualstudio.com/docs/copilot/customization/agent-skills` answers **HTTP 301** with
`location: /docs/agent-customization/agent-skills` (curl without `-L`, exit 0). The `.md` variant of
the *requested* path is a **404** (9 B body); the `.md` variant of the final path
`https://code.visualstudio.com/docs/agent-customization/agent-skills.md` is **200, 22871 B** and is
the quotable route (395 lines). The HTML route renders the same prose (200, 157298 B).

**F2 — Fetch record (every URL fetched twice; byte-identical on both fetches).**

| route | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|
| …/copilot/customization/agent-skills (no `-L`) | 2026-10-22T12:28:56Z | 301 → `/docs/agent-customization/agent-skills` | — | — |
| …/copilot/customization/agent-skills (follow) | 2026-10-22T12:29:33Z | 200 | 157,298 | `9118c27c63dd86f2c8ed0795614710923e75c55ffcf1fa1d35f30b47e082fba7` |
| …/copilot/customization/agent-skills.md | 2026-10-22T12:29:33Z | 404 | 9 | `0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5` |
| …/agent-customization/agent-skills.md | 2026-10-22T12:29:33Z | 200 | 22,871 | `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5` |
| raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/agent-skills.md | 2026-10-22T12:29:34Z | 200 | 24,087 | `bae0c84d97f58b24a60611250db17d125fcccfe7217379494e055702167a8ccb` |

The repo file is the upstream source of the same page (`DateApproved: 10/21/2026`, `{% data variables… %}`
placeholders the site expands); the site copy is its rendering. Header
`last-modified: Wed, 21 Oct 2026 06:19:42 GMT` — the page is one day old at access, so the freshness
axis rests on an in-date vendor page.

**F3 — (a) The description is the field Copilot matches a request against.** § How Copilot uses
skills, step 1 Discovery (`agent-skills.md:302`): "Copilot reads the skill's `name` and `description` from the YAML frontmatter." Same section (`:308`):
"This three-level loading system means you can install many skills without consuming context." Header table, `description` row (`:148`): "Be specific about both capabilities and use cases to help Copilot decide when to load the skill."

**F4 — (b) The length cap is 1024 characters for `description`; `name` caps at 64.** § Header
(required), `description` row (`agent-skills.md:148`): "Maximum 1024 characters." Same table, `name` row (`:147`): "Must match the parent directory name. Maximum 64 characters." Bearing on C1: kotoba's
current frontmatter `description` is **815 characters** (YAML parse of the lane `SKILL.md`), **847**
with the four missing lane names (`chousa`, `kama`, `kotodama`, `tameshi`) — inside the only budget
the page states. The C1 counter on the lane base measures **5** of 9 (`git show f3046466:SKILL.md |
awk … | grep -oiwE … | sort -u | wc -l` → `5`), matching the plan's before-value.

**F5 — (c) Plain answer: the page does NOT document a tie-break between two overlapping skills.**
Its only arbitration sentence concerns duplicate **names** across workspace roots, inside the
experimental OpenAI Codex NOTE (§ Create a skill, `agent-skills.md:64`): "If skills in `.github/skills/` have duplicate names across workspace roots, the primary root takes precedence." That is scoped to
same-named skills in the Codex integration, not to two skills whose descriptions overlap; the same
line adds "Discovery makes skills available to the model but does not guarantee that it invokes a skill for every relevant prompt." The Marketplace paragraph (`:129`) keeps
same-named skills side by side: "If another supported location contains a skill with the same name, both skills appear on the **Skills** page." Nothing on the page says which of two
overlapping descriptions wins, how ambiguity is resolved, or how a description is shortened under a
budget (sweep below: `overlap` 0, `ambig` 0, `tie[- ]?break` 0, `conflict` 0, `prioriti` 0,
`truncat` 0). Bearing on D3: the round-50 precedence ruling must be stated as **kotoba's own rule** —
no vendor source may be cited as its authority.

**F6 — What the page offers instead of a tie-break: description specificity, plus a manual-only
switch.** The `description` row's own instruction (`:148`) is the vendor's answer to overlap, and
`disable-model-invocation` (`:151`) is the documented escape: "Controls whether the agent can automatically load the skill based on relevance." This is the adjacency argument for
C1's edit: naming the nine sibling lanes in the description is exactly the "when *not* to use
kotoba" signal VS Code asks for, and no documented rule forbids naming many siblings.

**F7 — New row; the id is the L1's to assign.** `grep -c '^| S0' corpus/SOURCES.md` → **23** (exit 0),
registry ends at S023; `grep -c '^| S024 ' corpus/SOURCES.md` → 0 (exit 1, unclaimed at fetch time);
`grep -in 'visualstudio\|VS Code' corpus/SOURCES.md` → no hit (exit 1); `grep -rln 'visualstudio' corpus/knowledge/`
→ no file (exit 1) — a new row, not a re-open. Drafted in a private clone of the lane
(`…/src-vscode-skills/lane`, at `f3046466`) and checked with the fleet instrument
`scripts/sources-census.sh validate --file …`:
- unmodified lane registry → exit 0, `ok`, three pre-existing W04 (S018, S019, S021);
- mirror with the draft row under the numeric id `S024` → exit 0, `ok`, the same three W04, **no
  E-code and no new warning for the row**; the drafted line splits into **13 pipe-separated fields**
  (NF=13), matching every existing row and the header;
- mirror with the placeholder id `S0NN` → exit 1, `E02 S0NN` (the validator's id rule is
  `S[0-9]{3,}`) — the placeholder is a drafting convenience, not a landing form.

Landing constraint (not mine to land): the row's `used-by` names
`corpus/knowledge/sibling-overlap-census-round49.md`, so the census entry's appended section citing
S0NN must land with the row (the file exists today, so no E11 fires; a dangling citation would).

## Deliverable 1 — `corpus/SOURCES.md` row (append after S023, before `## Paths`)

```markdown
| S0NN | VS Code — Use Agent Skills in VS Code — https://code.visualstudio.com/docs/agent-customization/agent-skills | docs | A | How VS Code / GitHub Copilot presents a skill's frontmatter `description` and loads the skill from it, and what the page says about skills that collide (vendor documentation, not a measurement of omp or opencode) | § SKILL.md file format → § Header (required), `description` row (`agent-skills.md:148`); § How Copilot uses skills, step 1 Discovery (`agent-skills.md:302`) and the three-level note (`:308`); § Create a skill → NOTE on duplicate names across workspace roots (`agent-skills.md:64`); § Install a skill from the Customization Marketplace, same-name paragraph (`agent-skills.md:129`); fetched as https://code.visualstudio.com/docs/agent-customization/agent-skills.md (200, 22871 B, sha256 `de5ba34f…`) on 2026-10-22T12:29:33Z, twice byte-identical; the requested route https://code.visualstudio.com/docs/copilot/customization/agent-skills answers HTTP 301 to it, and its HTML renders 200, 157298 B, sha256 `9118c27c…`; page Last-Modified Wed, 21 Oct 2026 06:19:42 GMT; upstream source docs/agent-customization/agent-skills.md in microsoft/vscode-docs (24087 B, sha256 `bae0c84d…`, DateApproved 10/21/2026) | Copilot matches a request against the skill's `description`, which must say what the skill does and when to use it, capped at 1024 characters; no tie-break between two overlapping skills is documented — the sweep on the fetched text (grep -ciE) gives overlap 0, ambig 0, tie-break 0, conflict 0, prioriti 0, truncat 0, precedence 1 (duplicate names across workspace roots), multiple skills 1 (composing skills), same name 1 (Marketplace keeps both) | mined | 2026-10-22 | 90d | SKILL.md, corpus/knowledge/sibling-overlap-census-round49.md |
```

Rows 23 → 24 after landing (`grep -c '^| S0' corpus/SOURCES.md`); the numeric id for `S0NN` is
assigned by the L1 at integration.

## Deliverable 2 — round-lesson `## Gate` access-record line

```markdown
| S0NN | https://code.visualstudio.com/docs/agent-customization/agent-skills | 2026-10-22T12:29:33Z | "Copilot reads the skill's `name` and `description` from the YAML frontmatter." (§ How Copilot uses skills, step 1 Discovery, `agent-skills.md:302`) — seat `.ufo/waves/round-50/build/SrcVSCodeSkills.md` |
```

Second located quote, in reserve for the cap half of the scope (19 words, verbatim, § Header
(required), `description` row, `agent-skills.md:148`):

> "Be specific about both capabilities and use cases to help Copilot decide when to load the skill. Maximum 1024 characters."

## Evidence (commands, exit codes, paths)

- Fetch log: `date -u +%Y-%m-%dT%H:%M:%SZ` before each `curl -sS -L -o <file> -w '%{http_code} %{size_download} %{url_effective}' <url>`; sha256 by `sha256sum`. Old HTML 200/157298 B `9118c27c…`; old `.md` 404/9 B `0019dfc4…`; new `.md` 200/22871 B `de5ba34f…` (twice, `cmp` identical, exit 0); repo raw 200/24087 B `bae0c84d…`; `curl -D -` on the old route → `HTTP/2 301`, `location: /docs/agent-customization/agent-skills` (exit 0); `curl -D -` on the new `.md` → `HTTP/2 200`, `last-modified: Wed, 21 Oct 2026 06:19:42 GMT` (exit 0).
- Q14 sweep, `for t in …; do grep -ciE "$t" fetch2/new_md; done`, file `/fast/scratch/hyaku/kotoba-r50/build/src-vscode-skills/fetch2/new_md` (22,871 B, 395 lines): `overlap` 0, `ambig` 0, `precedence` 1, `tie[- ]?break` 0, `conflict` 0, `multiple skills` 1, `same name` 1, `prioriti` 0, `1024` 1, `truncat` 0. The same sweep over the HTML route gives `conflict` 2; both hits are site chrome, not skill prose (`grep -niE 'conflict' fetch2/new_html` → lines 914 and 1400, links to "Merge Conflicts" in the source-control nav). Every non-zero count is located: `precedence` → `:64`; `multiple skills` → `:15` ("Combine multiple skills to build complex workflows"); `same name` → `:129`; `1024` → `:148`.
- Quoted lines read with `sed -n '<n>p'`: 15, 64, 129, 147, 148, 151, 302, 308.
- Registry: `grep -c '^| S0' corpus/SOURCES.md` → 23 (exit 0); `grep -c '^| S024 ' corpus/SOURCES.md` → 0 (exit 1); `grep -in 'visualstudio\|VS Code' corpus/SOURCES.md` → no match (exit 1); `grep -rln 'visualstudio' corpus/knowledge/` → no file (exit 1).
- Validation: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md` (lane, unmodified) → exit 0, `ok`, W04 × 3 (S018, S019, S021). Mirror + draft row under `S024` → exit 0, `ok`, same three W04, no E-code, no new warning; mirror with `S0NN` → exit 1, `E02 S0NN`.
- C1 counter on the lane base (read-only `git show`) → `5`.
- Description length: `yaml.safe_load` of the lane `SKILL.md` frontmatter → 815 characters; +32 for " chousa, kama, kotodama, tameshi" → 847, under the documented 1024 cap.

## Out of scope

- Editing `corpus/SOURCES.md`, `corpus/lessons/round-50.md` or the census entry: drafts only
  (read-only lane bound; the L1 integrates).
- The D3 precedence ruling's text: this source shows there is no vendor rule to borrow, so the
  ruling must be stated as kotoba's own — that wording belongs to the D3 seat.
- Measuring omp's or opencode's real arbitration; the scope cell says this row is vendor
  documentation, not a measurement of omp or opencode.
- Other VS Code pages (parent-repository discovery, plugin skills): the sweep's negative claim
  covers this page only.

## Artifacts

- `…/src-vscode-skills/fetch2/new_md` — the swept text (22,871 B, sha256 `de5ba34f…`); sibling files `fetch2/{old_html,old_md,new_html,repo_raw}`.
- `…/src-vscode-skills/draft_row.md` — the drafted row, byte-for-byte as delivered above.
- `…/src-vscode-skills/lane/` — private clone of the lane at `f3046466` with the draft row appended (mirror only; the real lane was not touched).

## Tooling

None installed or upgraded this session; `curl`, `grep`, `sed`, `cmp`, `sha256sum`, `date`, `git`
and the fleet's `scripts/sources-census.sh` were already present. No `pacman`, `uv tool`, `cargo` or
`npm -g` transaction was run, and no host service was restarted.
