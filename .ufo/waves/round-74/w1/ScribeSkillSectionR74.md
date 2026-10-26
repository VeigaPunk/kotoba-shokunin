# ScribeSkillSectionR74 — SKILL.md body-craft subsection, frame rewrite, routed row, PROVINCE + gate texts

**Verdict.** All four deliverables are drafted to the frozen plan's shape and budget, and none is landed:
(1) a 14-line `### Body craft — the specification's skill-creation guides` subsection for the end of
`SKILL.md` § Compression rules with a 7-row table (3 best-practices / 2 using-scripts / 2 quickstart, every
row carrying an in-snapshot token and a ≥5-word action); (2) a 2-line replacement for the frame sentence,
line-count neutral, carrying a command-backed client count of 11; (3) a 3-line decision row for the
cross-vendor `.agents/skills/` root in the shape of the round-52 MCP `instructions` table; (4) two
`PROVINCE.md` § Core bullets and two § Gate registry rows for `check_spec_craft.py` and
`check_sibling_reread.py`. Block text: `.ufo/waves/round-74/w1/build/ScribeSkillSectionR74/blocks.md`.

**Two blockers for the L1, both created by other seats' state, not by this draft:**
(a) the three source ids are placeholders `S<a>/S<b>/S<c>` — both `ExecSrcScriptsR74/row.md` and
`ExecSrcQuickstartR74/row.md` compute the next free id as `S223`, and `ExecSrcBestPracticesR74/row.md:1`
already drafts `S223` for best-practices, so a collision must be resolved before substitution;
(b) the C1 predicate (b) requires `status mined` while both script/quickstart seats drafted a `queued`
alternative — the table rows are unaffected, but the rows cannot count until the registry row is `mined`
(their finding, re-read here, not re-measured by this seat).

**One pointer corrected.** The seat brief says the frame sentence is at `SKILL.md:21-23`; it is at
`SKILL.md:23-24` (21 is the `#` title, 22 blank).

---

## Deliverable 1 — the subsection (14 lines added; file 570 → 584)

Insert after `SKILL.md:198` (`Trigger-fidelity checklist, line-budget box).`) and before the blank line
199, which then separates it from `## Trigger-fidelity checklist` (200). Measured section bounds:

```
$ awk 'NR>=190 && NR<=199 {printf "%d:%d:%s\n", NR, length($0), substr($0,1,60)}' SKILL.md
190:20:## Compression rules
191:0:
192:76:Six rules with their evidence: `corpus/knowledge/anatomy-and
193:72:§ Compression rules. The two that decide most edits: spend t
194:81:`description`, not the body; and one authoritative home per
195:74:a file and the skill keeps the pointer line. Also there: ver
196:81:command blocks, failure signatures inline, never restate the
197:72:and the **~600-line module bound** (round 15 applies it to t
198:45:Trigger-fidelity checklist, line-budget box).
199:0:
```

Draft (verbatim from `blocks.md`, leading blank line included):

```markdown

### Body craft — the specification's skill-creation guides
Body craft from the specification's own `skill-creation/` guides, one rule per
row; the entry is `corpus/knowledge/spec-skill-creation-craft-round74.md`.

| rule | source | what a skill author does |
|---|---|---|
| "Match the specificity of your instructions to the fragility of the task" | S<a> best-practices | Be prescriptive where a sequence is fragile; explain *why* where several approaches work |
| "Provide defaults, not menus" | S<a> best-practices | Name one default tool and one escape hatch, never four equal options |
| `SKILL.md` "under 500 lines and 5,000 tokens" | S<a> best-practices | Keep the body to every-run instructions and load the rest from `references/` on a stated trigger |
| `uvx ruff@0.8.0 check .` "reference it directly" | S<b> using-scripts | Call a published package at a pinned version instead of bundling a copy under `scripts/` |
| `--help` "the primary way an agent learns your script's interface" | S<b> using-scripts | Document flags and examples in `--help`; make missing input a named error, not a prompt |
| `.agents/skills/` "VS Code looks for skills in" | S<c> quickstart | Create the folder under `.agents/skills/` in the project; VS Code needs no config |
| "The same skill works in any compatible agent" | S<c> quickstart | Keep the body client-neutral, then load the same folder in a second harness |
```

Line count, measured on the block itself (blank + heading + 2 lead lines + blank + header + separator +
7 rows):

```
$ awk '/^### Body craft/,/^\| "The same skill works/' blocks.md | awk '{printf "%2d %3d %s\n", NR, length($0), substr($0,1,64)}'
 1  58 ### Body craft — the specification's skill-creation guides
 2  78 Body craft from the specification's own `skill-creation/` guides
 3  74 row; the entry is `corpus/knowledge/spec-skill-creation-craft-ro
 4   0
 5  44 | rule | source | what a skill author does |
 6  13 |---|---|---|
 7 190 | "Match the specificity of your instructions to the fragility o
 … rows 8-13 …
```

13 lines from the heading plus the leading blank = **14**, exactly the plan's C1 budget; lead widths 78/74
sit inside the file's 72–81 prose band in § Compression rules. Rows per page 3/2/2 clear `≥2` for each.

Token grounding — every token in the table is a literal substring of the snapshot the C1 counter will
hash (`grep -c -F` against the seats' snapshot files, re-hashed by this seat):

```
$ for t in 'Match the specificity of your instructions to the fragility of the task' \
           'Provide defaults, not menus' 'under 500 lines and 5,000 tokens'; do
    printf '%-78s bp=%s\n' "$t" "$(grep -c -F -- "$t" ExecSrcBestPracticesR74/bp-md.raw)"; done
Match the specificity of your instructions to the fragility of the task        bp=1
Provide defaults, not menus                                                    bp=1
under 500 lines and 5,000 tokens                                               bp=1

$ for t in 'uvx ruff@0.8.0 check .' 'reference it directly' '--help' \
           "the primary way an agent learns your script's interface"; do
    printf '%-60s sc=%s\n' "$t" "$(grep -c -F -- "$t" ExecSrcScriptsR74/snapshot.md)"; done
uvx ruff@0.8.0 check .                                       sc=1
reference it directly                                        sc=1
--help                                                       sc=3
the primary way an agent learns your script's interface      sc=1

$ for t in '.agents/skills/' 'VS Code looks for skills in' \
           'The same skill works in any compatible agent'; do
    printf '%-60s qs=%s\n' "$t" "$(grep -c -F -- "$t" ExecSrcQuickstartR74/snapshot.md)"; done
.agents/skills/                                              qs=3
VS Code looks for skills in                                  qs=1
The same skill works in any compatible agent                 qs=1
```

Snapshot identities re-hashed (`sha256sum`, sizes from `wc -c`):

```
ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41  ExecSrcBestPracticesR74/bp-md.raw   15060 B
2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f  ExecSrcScriptsR74/snapshot.md      12078 B
7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb  ExecSrcQuickstartR74/snapshot.md    4080 B
```

Placeholder sweep, after a peer flagged it: `.agents/skills/<name>` occurs **0** times in each of the three
snapshots (`grep -c -F -- '.agents/skills/<name>'` → `0` / `0` / `0`), so the quickstart row's action cell names the
directory and not a templated path; the tutorial's own example path `.agents/skills/roll-dice/SKILL.md` occurs 3×
(`:21/:23/:55`) and is not generalised into advice. No backticked token in the table occurs only in an HTML
rendering: every one was counted in the `.md` snapshot bytes above.

Page census (this seat's own reading, for the Q45 seat and the counter's `≥2 tokens` bar): best-practices
also carries `Calibrating control` (`bp-md.raw:94`) and `Favor procedures over declarations` (`:145`);
using-scripts also carries `npx eslint@9.0.0` (`snapshot.md:90`) and `bundle reusable scripts in a` (`:9`);
quickstart also carries `one file, under 20 lines` (`snapshot.md:44`) and `Type \`/skills\`` (`:55`). All
three pages clear two tokens, so `N == 3` is reachable on this evidence; the census seat owns the figure.

---

## Deliverable 2 — frame sentence (`SKILL.md:23-24`, 2 lines in, 2 lines out)

Observed base bytes:

```
$ sed -n '23,24p' SKILL.md
A SKILL.md is a **loader contract**: the frontmatter `description` is the
only part any router ingests — and the two harnesses here show it differently.
```

Replacement (widths 73 and 80; line count unchanged, so it spends nothing of the 14-line budget):

```
A SKILL.md is a **loader contract**: the frontmatter `description` is the
only part any router ingests — read live on omp and opencode, documented for 11.
```

The count of 11 is measured, not recalled:

```
$ { grep -oE '^\| (Claude Code|Codex|VS Code|Copilot CLI|Gemini CLI|Cursor|opencode) ' SKILL.md; \
    grep -oE 'TRAE|CodeBuddy|Kimi Code|Zhipu' PROVINCE.md; } | sed -E 's/^\| //; s/ $//' | sort -u | wc -l
11
$ … | sort -u
Claude Code
CodeBuddy
Codex
Copilot CLI
Cursor
Gemini CLI
Kimi Code
opencode
TRAE
VS Code
Zhipu
```

The seven per-client row sets of this file (Description thresholds, Explicit invocation, Agent-definition,
Custom command, Hook, Scoped rule, Trust gates) contribute the seven Western names; the round-73 Core
bullet contributes the four Chinese vendors. `opencode` is in both sets — the sentence says "documented for
11", never "11 others". `omp` is the surface the lane reads live and no corpus page documents, so the
sentence claims no page for it.

---

## Deliverable 3 — routed item 5 decision row (3 table lines + 1 blank)

Shape: the nearest existing SKILL.md table, the round-52 MCP `instructions` table in § Instruction
surfaces, `| guidance that is… | put it in | why (documented) |` (situation → placement → documented
reason). Placement: after that table, before `### Agent-definition files by client` (`SKILL.md:78`).

```markdown

| decision | what the pages say | what a skill author does |
|---|---|---|
| where a skill meant for TRAE, CodeBuddy, Kimi Code or Zhipu lives | `.agents/skills/` is read by Kimi at both scopes and by TRAE only behind an explicit switch, while CodeBuddy and Zhipu name it nowhere; TRAE's own `.trae/skills/` outranks it on a name collision (S217, S220, S221; `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md:26,35-36`) | Write to the vendor's own root; never ship a skill that travels only through `.agents/skills/` |
```

Each clause re-opened at the entry, not taken from a summary:

```
$ grep -n '\.agents/skills/\|导入设置\|first-class' corpus/knowledge/chinese-vendor-skill-surfaces-round73.md
26:| Kimi Code CLI (Moonshot) | `.kimi-code/skills/`, `.agents/skills/` | `$KIMI_CODE_HOME/skills/` (default `~/.kimi-code/skills/`), `~/.agents/skills/` | …
35:2. **A project scope outranks a user scope — but only two of the four publish that order.** … TRAE … "若你在 TRAE 内创建的技能（位于 `.trae/skills/` 目录）与 `.agents/skills/` 中的技能重名，系统将优先调用 `.trae/skills/` 目录中的技能。" (`cn-trae-skills.md:375`)
36:3. **The cross-vendor `.agents/skills/` root is read by two of the four, not all four.** TRAE reads it behind an explicit switch — "在 导入设置 部分，打开 启用 .agents 技能目录 开关。" (`cn-trae-skills.md:389`) — and lets its own root win a collision (quote above). Kimi reads it at both scopes: `~/.agents/skills/` and `.agents/skills/` (`cn-kimi-zh-skills.md:277-285`). CodeBuddy's two pages never name it and Zhipu's page never does — 0 hits on each, counts in Limits.
38:The other half of pattern 3 is the part that changes authoring practice: TRAE treats `.agents/skills/` as an imported namespace that its own directory outranks, while Kimi treats it as a first-class root alongside its own…
```

Quote shapes in the row: the two Chinese quotes are pasted from the entry's line 35/36 byte-for-byte; the
row paraphrases them in English rather than re-quoting, so no quote in `SKILL.md` exceeds 25 words.

---

## Deliverable 4 — PROVINCE § Core bullets and the two gate-registry rows

Both were written in the style of `PROVINCE.md:28-31` (round-in-parentheses title, the entry path,
`counted by <verifier>`), with `<<N>>` / `<<rev>>` left for the L1's measured values; full text in
`blocks.md` § 4a. The two registry rows follow the last four rows' 8-cell shape (verdict map carrying the
predicate and the printed figure, `--self-test`, named pins, named write scope, owner `kotoba`); full text
in `blocks.md` § 4b. Placement: alphabetically `check_sibling_reread.py` belongs after
`check_sibling_census.py` (`SKILL.md:467`) and `check_spec_craft.py` after
`check_sources_append_only.py` (`SKILL.md:468`); the round-72/73 rows are appended out of order at the file
end, so either placement is internally consistent — the L1 picks one.

Line budget: 570 + 14 (subsection) + 2 (registry rows) + 4 (item 5) = 590 of 600, matching the plan's stated
figure; the frame rewrite is net 0.

---

## Provenance of what this seat read

| item | observed |
|---|---|
| `curl -sL --max-time 60 -A 'Mozilla/5.0' -o using-scripts.md -w 'HTTP:%{http_code} SIZE:%{size_download}\n' https://agentskills.io/skill-creation/using-scripts.md` | `HTTP:200 SIZE:12078`, `date -I` → `2026-10-25`, `sha256sum using-scripts.md` → `2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f`; saved at `.ufo/waves/round-74/w1/build/ScribeSkillSectionR74/using-scripts.md` |
| independent-fetch cross-check | my fetch's sha256 equals `ExecSrcScriptsR74/snapshot.md`'s pin exactly (`2cd77271…ad1f`) — two seats, two fetches, one byte string |
| best-practices | not fetched by this seat; seat header `bp-md.hdr` reads `HTTP:200 URL:https://agentskills.io/skill-creation/best-practices.md SIZE:15060`, and I re-hashed the bytes: `ab9f3b60…fb41`, 15 060 B |
| quickstart | not fetched by this seat; `ExecSrcQuickstartR74/fetch-record.md` records `http=200 … bytes=4080` with no redirect and the no-`.md` form at 271 472 B; I re-hashed `snapshot.md`: `7c480b44…bffb`, 4 080 B |
| lane files read only | `SKILL.md`, `PROVINCE.md`, `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`, `plans/round-74.md`, `.ufo/waves/round-74/assimilation/staged-ids`; no write to any of them |
| staged package read only | `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-script-craft-rules.md` (its `>>`-less header rows S236/S237 name the two pages the seat brief calls using-scripts and quickstart) |

No credential material, cookie, session URL or `op://` reference is recorded; no tool was installed
(no `pacman`, no `uv tool`, no `npx`).

## Conflicts recorded verbatim for the canonical judge

1. **Frame-sentence location.** Seat brief: "the SKILL.md intro (lines 21-23, read them)". Observed:
   line 21 is `# kotoba-shokunin — prompt & skill craft`, line 22 blank, and the sentence occupies 23–24
   (`grep -n 'loader contract' SKILL.md` → `23:`; `grep -n 'two harnesses here' SKILL.md` → `24:`).
   The draft therefore replaces 23–24.
2. **Next registry id.** `ExecSrcBestPracticesR74/row.md:1` drafts `S223` for best-practices;
   `ExecSrcQuickstartR74/row.md:3-5` says "the next free lane id is `S223`"; `ExecSrcScriptsR74/row.md`
   carries `S<next>` and its cell table says "`S<next>` = `S223`". Three seats, one free id — the L1 must
   assign by document order before substituting into the table.
3. **Registry status.** `ExecSrcQuickstartR74/row.md` § Landing notes: "This draft carries `queued` as the
   seat instruction directs, but plan § C1 predicate (b) requires `status `mined``" and
   `ExecSrcScriptsR74/row.md` § Alternative: "`queued` also removes the census `E11` check … so it is the
   cheaper row, not the weaker one." This seat did not re-measure the census; it is recorded as the two
   seats wrote it.

## Landing couplings reported by `ExecSkillGatesR74` (recorded, not re-measured here)

That seat's pre-test measured two couplings and a green landing shape
(`.ufo/waves/round-74/w1/build/ExecSkillGatesR74/landing-shape.patch`; I read the patch and hashed it, I did not
run its gates). Measured here, not taken on report: the patch's bytes are 165 lines and hash
`a3a2863552c103e4ee925c52e19a0d31ccda2a8c2cb7f5f834b3aa0dabc8cb64`, equal to the pin in
`landing-shape.patch.sha256`; `landing-rev.txt` names the sandbox rev
`55287654883ed0ac1e3b6fdd2f421937f2673217`. The two hashes that seat quoted name **different objects**, not
two revisions of one — measured here in a throwaway `--shared` clone at `329e7d9` (`git apply --check` OK, then
applied, directory deleted):

```
$ sha256sum landing-shape.patch; cat landing-shape.patch.sha256; wc -c landing-shape.patch
a3a2863552c103e4ee925c52e19a0d31ccda2a8c2cb7f5f834b3aa0dabc8cb64  landing-shape.patch
a3a2863552c103e4ee925c52e19a0d31ccda2a8c2cb7f5f834b3aa0dabc8cb64  /…/build/ExecSkillGatesR74/landing-shape.patch
12634 landing-shape.patch

$ cat landing-rev.txt
55287654883ed0ac1e3b6fdd2f421937f2673217

$ sha256sum SKILL.md; wc -lc SKILL.md        # at 329e7d9, before apply
c105b874a8166542747ffa67b60810301c9bf94d32cf584252e96a4f9533f5ab  SKILL.md
  570 74174 SKILL.md                          # matches the plan's before-value 570 / 74,174 B

$ git apply landing-shape.patch; sha256sum SKILL.md; wc -lc SKILL.md
dee61faf9849d71e32400692f65fef5fb942d6305df894f20b3933cc5ad2b595  SKILL.md
  590 77132 SKILL.md
```

The base blob is the same object at the assigned base and at the plan commit — checked here from the committed
objects, not from the working tree:

```
$ for r in 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908 329e7d91d7d750031c35d264f0e34af1d0ce8385; do
    git show $r:SKILL.md | sha256sum | cut -d' ' -f1; done
c105b874a8166542747ffa67b60810301c9bf94d32cf584252e96a4f9533f5ab
c105b874a8166542747ffa67b60810301c9bf94d32cf584252e96a4f9533f5ab
$ git cat-file -p 329e7d9 | head -2
tree 12ec3bfda4e630f31fba2a56ab31cc5164cd75ee
parent 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908
```

Same blob at both revs (74,174 B, 570 lines) and the plan commit's parent is the assigned base, so the
landing pre-test transfers from `1e03d19` to `329e7d9` without qualification: `SKILL.md` is byte-identical
across them. The two trees differ in exactly the plan's twelve files, none of them `SKILL.md`:

```
$ git diff --stat 1e03d19 329e7d9 | tail -1
 12 files changed, 690 insertions(+), 2 deletions(-)
$ git diff --name-only 1e03d19 329e7d9
.ufo/waves/round-74/assimilation/{collisions,quarantine-slice,reg-ids,staged-ids}
.ufo/waves/round-74/receipts/{base-battery-l1,base-sweeps,census-before,sibling-heads-freeze,sibling-staleness-base}
corpus/README.md   plans/round-74.md   verifiers/corpus-baseline.json
$ git diff --name-only 1e03d19 329e7d9 | grep -c 'SKILL.md'
0
```

So the only functional deltas for the landing pre-test are the closure index row in `corpus/README.md` and
`verifiers/corpus-baseline.json` — which is why the sandbox runs could differ only at the corpus gates.

So for the L1's record: **patch pin** `a3a28635…cb64` (12,634 B, 165 lines); **applied-file check**
`dee61faf…b595` (590 lines / 77,132 B, rebuilt by applying that patch to `329e7d9`). Neither is a second pin
and there is no contradiction between them.

One commit invariant, unchanged by any shape decision (that seat's close, recorded): the counters with their
exact `--self-test` handlers, the entry, the `corpus/README.md` index row, these `SKILL.md` rows, and
`corpus.index.tracked_files` 139 → 140 in `verifiers/corpus-baseline.json` land together, and then
`check_tip_battery.py --rev <rev>` must print `guards 5 of 5` and `6 of 6`; any split lands red at exactly one
place.

1. **Entry and rows must be one commit.** A backticked `corpus/knowledge/spec-skill-creation-craft-round74.md`
   in `SKILL.md` fails `verify_skill_checklist` check `trigger.citation_resolves` until that entry exists at
   the measured rev. My subsection's second lead line backticks exactly that path, so the C1 block cannot land
   before the entry.
2. **Baseline re-record in the same commit.** The entry plus its `corpus/README.md` index row move
   `corpus.index.tracked_files` from 139 to 140; without re-recording `verifiers/corpus-baseline.json:15`,
   `verify_corpus_integrity` reads exit 1 and the tip battery 4 of 6. Their measured green: guards 5 of 5,
   tip battery 6 of 6 at sandbox rev `5528765`.

Shape reconciliation — two routes to the same 590, neither cancelling the other. The landing arithmetic is
the same total by different placement; the L1 picks a route and must not blend them halfway.

| | this draft | `ExecSkillGatesR74` (measured) |
|---|---|---|
| insertion anchor | end of `SKILL.md:198`, before the existing blank 199 | after the blank 199 |
| subsection block | 14 lines, no trailing blank; the file's blank 199 separates it from `## Trigger-fidelity checklist` | 15 lines including its own trailing blank |
| block content | 7 rows (3 / 2 / 2), brief's header | 6 placeholder rows, its own header, plus a closing note |
| frame rewrite | 2 lines in, 2 out — 0 | 1 line -> 3 lines — +2 |
| item 5 | standalone 3-column table: header + separator + row + blank — 4 | one row appended inside the MCP `instructions` table — +1 |
| total | 570 + 14 + 2 + 4 + 0 = **590** | 570 + 15 + 2 + 1 + 2 = **590** |
| measured? | not run (scribe seat runs no gate) | `guards 5 of 5; tip battery exit 0: 6 of 6`, sandbox rev `5528765` |

Two mechanical conditions on this route, both markdown and neither gate-checked (peer-measured, recorded
as reported): (a) the insertion anchor must be the end of line 198, not after blank 199, or the file lands
two blank lines and the saved line disappears; (b) a closing note added under the table needs its own
preceding blank (592 then), because a flush paragraph would be absorbed into the table as a one-cell row.
Its standalone item-5 table is gate-free for the same reason the subsection header is: no verifier counts
tables or lines, and the block sits in `## Instruction surfaces`, a section with no `- [ ]` boxes, so no
nearest-heading rule re-sections it.

### Citation shift this route causes (measured, not a gate input)

Inserting 14 lines at the end of `SKILL.md:198` moves every `SKILL.md:<N>` citation that points at line 199 or
below. Full sweep of the corpus:

```
$ grep -rhoE 'SKILL\.md:[0-9]+' corpus/ | awk -F: '{print $2}' | sort -n > c; wc -l < c
111
$ awk '$1>=199' c | wc -l
45
$ awk '$1<199' c | wc -l
66
```

So 45 of 111 corpus citations would need `+14` on this route (their route, 15 lines, would need `+15`); 66
point above the insertion and are untouched. The sibling seat's earlier 97 was scope, not arithmetic, and the
gap is entirely one non-prose file — re-measured here:

```
$ grep -c -oE 'SKILL\.md:[0-9]+' corpus/knowledge/sibling-citation-routing-round16.json
14
$ grep -rhoE 'SKILL\.md:[0-9]+' corpus/*.md corpus/knowledge/*.md corpus/lessons/*.md | wc -l
97
```

97 prose citations in the direct-child `.md` files + 14 JSON routing rows = 111 on the recursive sweep. Two
further measured classes neither seat had at the start:

```
$ grep -rhoE 'SKILL\.md:24\b' corpus/ | wc -l
3        # citations naming the frame sentence itself — these go stale on BOTH routes because its text changes
$ grep -rhoE 'SKILL\.md:[0-9]+' corpus/ | awk -F: '$2>570' | wc -l; … | sort -n | tail -1
13       # already past EOF at base (570 lines; highest cited line 720)
```

The 13 are the proof that these citations are points-in-time labels, not live anchors, so only the ones a
reader actually follows need re-pointing. No gate reads any of them; the canonical command for the landing rev
is the recursive sweep above (`grep -rhoE 'SKILL\.md:[0-9]+' corpus/ | awk -F: '{print $2}' | sort -n`), run
by the L1 rather than inherited from either seat's figure.

Two things the L1 must decide, not blend: the subsection table header is fixed by this seat's brief as
`| rule | source | what a skill author does |`, so the patch's header changes if my rows are substituted; and
the patch's frame rewrite carries no client count, while this brief requires one counted with a command
(`11`, § Deliverable 2). The patch's rows are explicit placeholders — they are not the landed text.

## Not done, on purpose

- No gate run, no `--self-test`, no counter written: this seat drafts text; the counters are the
  ExecCounter*/ExecControl* seats' and the L1 runs the battery.
- No entry written (`corpus/knowledge/spec-skill-creation-craft-round74.md` does not exist yet — the
  tokens above are ready for it, but the entry's `source:`/`verified-at:`/`recheck:` trio and its rule
  table belong to the entry seat).
- No snapshot copied to `.ufo/waves/round-74/snapshots/` and no manifest written.
- No id substituted anywhere: `S<a>/S<b>/S<c>` are literals in `blocks.md` on purpose.

## Artifacts

- `.ufo/waves/round-74/w1/build/ScribeSkillSectionR74/blocks.md` — the four blocks plus grounding.
- `.ufo/waves/round-74/w1/build/ScribeSkillSectionR74/using-scripts.md` — my independent fetch (12 078 B,
  sha256 `2cd77271…ad1f`).
- `.ufo/waves/round-74/w1/build/ScribeSkillSectionR74/fetch-date.txt` — `2026-10-25`.
- This report: `.ufo/waves/round-74/w1/ScribeSkillSectionR74.md`.

Report: .ufo/waves/round-74/w1/ScribeSkillSectionR74.md
