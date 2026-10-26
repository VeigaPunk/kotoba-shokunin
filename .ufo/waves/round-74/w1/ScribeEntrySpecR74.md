# ScribeEntrySpecR74 — C1 knowledge entry draft (round 74, wave 1)

**Verdict.** The entry is drafted at
`.ufo/waves/round-74/w1/build/ScribeEntrySpecR74/entry.md` (141 lines, 13 739 B): three `source:` lines,
`verified-at:`, `recheck:`, `ground:`, prose on all three pages, and exactly **one rule table with one row
per page and three located tokens per row**. Against the page bytes the L1 will commit — the ExecSrc seat
snapshots, whose sha256s are identical to my own independent fetches today — my own mechanical check passes
predicate **(a)** (front-matter order, one row per page, ≥ 2 tokens each located word-bounded) and
predicate **(d)** (quote 5–25 words, found after whitespace collapse). Predicates **(b)**, **(c)**, **(e)**,
**(f)** are landing conjuncts and are **not measurable now**: `verifiers/check_spec_craft.py` does not exist
yet (`ls verifiers/ | grep -iE 'spec_craft|sibling_reread'` → no line, exit 1) and
`.ufo/waves/round-74/snapshots/` does not exist (`ls` → `No such file or directory`). Nothing in this
report claims a count from a counter that was not run.

Seat identity: `ScribeEntrySpecR74` (suffix `R74`); every path cited is lane-local
(`/home/vgpnk/Projects/shokunin/kotoba-shokunin`) except the read-only staged package and the frozen plan.

## 1. What I opened first (house form and the frozen predicate)

```
$ read plans/round-74.md                      # § C1 predicate (a)-(f), shortcut controls, seat spec
$ read corpus/knowledge/client-trust-gates-round68.md      # house form: source/verified-at/recheck,
$ read corpus/knowledge/skill-name-precedence-round69.md   #   per-client table, Limits, Scope, Related
$ read corpus/knowledge/chinese-vendor-skill-surfaces-round73.md  # + ground:, snapshot `:line` refs
```

The three readings fix the form used: `source:` lines carrying `S id — title — URL — section — located
quote`, a `verified-at`, a `recheck` that is a runnable command, a `ground:` line, then per-surface prose,
a table, `Limits`, `Scope`, `Related`. The r73 entry also fixes the convention of citing the snapshot line
next to a quote, which this entry follows.

## 2. The three pages, opened by me (2026-10-25, `.md` route)

```
$ for p in best-practices using-scripts quickstart; do curl -sL --max-time 60 -A 'Mozilla/5.0' \
    -o $D/$p.md -w 'HTTP:%{http_code} SIZE:%{size_download} URL:%{url_effective}\n' \
    "https://agentskills.io/skill-creation/$p.md"; done
HTTP:200 SIZE:15060 URL:https://agentskills.io/skill-creation/best-practices.md
HTTP:200 SIZE:12078 URL:https://agentskills.io/skill-creation/using-scripts.md
HTTP:200 SIZE:4080  URL:https://agentskills.io/skill-creation/quickstart.md
$ sha256sum $D/*.md
ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41  best-practices.md
7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb  quickstart.md
2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f  using-scripts.md
$ date -I
2026-10-25
$ wc -lc best-practices.md using-scripts.md quickstart.md
  277 15060 best-practices.md
  304 12078 using-scripts.md
   83  4080 quickstart.md
  664 31218 total
```

**The seat's own snapshots agree byte for byte** with the ExecSrc seats' `snapshot.md` (command, output):

```
$ sha256sum ExecSrcBestPracticesR74/snapshot.md ExecSrcScriptsR74/snapshot.md ExecSrcQuickstartR74/snapshot.md
ab9f3b60…  ExecSrcBestPracticesR74/snapshot.md
2cd77271…  ExecSrcScriptsR74/snapshot.md
7c480b44…  ExecSrcQuickstartR74/snapshot.md
```

so every quote in the entry is a literal substring of the bytes the L1 copies into
`.ufo/waves/round-74/snapshots/{best-practices,using-scripts,quickstart}.md` (names confirmed by the L1 in
message, not assumed from the counter seat's text; see § 6 F4).

I took rules and quotes from the ExecSrc candidate files where they existed —
`ExecSrcBestPracticesR74/rules-table.md` (13 candidate rules) and `ExecSrcQuickstartR74/rules.md` (12
candidate rules) — and located each chosen quote myself in the bytes (`sed -n '<L>p'`, outputs in § 3).
The `using-scripts` seat had published only its registry row at the time of writing (`row.md`,
`snapshot.md`, `snapshot.sha256`; no rules file), so that page's rule and quote are my own location over
the same snapshot bytes, not a transcription of a sibling claim. I did not use the staged package's text
for any quote.

## 3. The entry's rule table, and every token located

Delivered table (verbatim from the entry):

| page | S id | rule | quote | tokens | action |
|---|---|---|---|---|---|
| best-practices | S<a> | Prescriptiveness is per part: grade each instruction by how fragile its step is, not by taste; name a default rather than a menu | "Match the specificity of your instructions to the fragility of the task." | `references/api-errors.md`; `python scripts/migrate.py --verify --backup`; `references/schema.yaml` | give the agent freedom and say why where several approaches work, and pin the exact command plus its prohibition where the step is fragile |
| using-scripts | S<b> | Reference an existing package before bundling a script, pin the version, and write the script's interface for an agent caller | "When an existing package already does what you need, you can reference it directly in your `SKILL.md` instructions without a `scripts/` directory." | `uvx ruff@0.8.0 check .`; `pipx run 'black==24.10.0' .`; `npx package@version` | reach for the tool with an explicit version first, state the prerequisite in the body, and move a command into a tested script only once it is too complex to get right first try |
| quickstart | S<c> | The tutorial's minimal shape: one `SKILL.md` in the project's `.agents/skills/` tree, name plus description only, under twenty lines | "VS Code looks for skills in `.agents/skills/` by default." | `.agents/skills/roll-dice/SKILL.md`; `.agents/skills/`; `/skills` | place the first skill in that tree, keep it under twenty lines, and confirm the name with `/skills` before trusting the path |

Locations (each a line of the corresponding snapshot; `sed -n` output pasted in § 4 where the claim is
prose, here via `grep -n`):

```
$ grep -n 'Match the specificity' best-practices.md
96:Not every part of a skill needs the same level of prescriptiveness. Match the specificity of your instructions to the fragility of the task.
$ grep -n 'migrate.py --verify' best-practices.md
119:python scripts/migrate.py --verify --backup
$ grep -n 'references/api-errors.md\|references/schema.yaml' best-practices.md
92:The key is telling the agent *when* to load each file. "Read `references/api-errors.md` if the API returns a non-200 status code" …
$ grep -n 'reference it directly' using-scripts.md
13:When an existing package already does what you need, you can reference it directly in your `SKILL.md` instructions without a `scripts/` directory. …
$ grep -n "uvx ruff@0.8.0" using-scripts.md        → 20:uvx ruff@0.8.0 check .
$ grep -n "pipx run 'black==24.10.0'" using-scripts.md → 32:pipx run 'black==24.10.0' .
$ grep -n 'Pin versions with' using-scripts.md    → 50:* Pin versions with `npx package@version` for reproducibility.
$ grep -n 'looks for skills' quickstart.md        → 21:A skill is a folder containing a `SKILL.md` file. VS Code looks for skills in `.agents/skills/` by default. …
$ grep -n '.agents/skills/roll-dice/SKILL.md' quickstart.md → 21, 23, 55
$ grep -n '/skills' quickstart.md                 → 21, 55, 57-58 (the tutorial's own listing step)
```

Word-bounded presence and counts, one sweep over the three snapshot files:

```
$ for pair in 'best-practices|references/api-errors.md' 'best-practices|python scripts/migrate.py --verify --backup' \
    'best-practices|references/schema.yaml' 'using-scripts|uvx ruff@0.8.0 check .' \
    "using-scripts|pipx run 'black==24.10.0' ." 'using-scripts|npx package@version' \
    'quickstart|.agents/skills/roll-dice/SKILL.md' 'quickstart|/skills'; do … printf '%s\n' "$(grep -c -F -- "$t" …/$p.md)"; done
best-practices  references/api-errors.md                     1
best-practices  python scripts/migrate.py --verify --backup  1
best-practices  references/schema.yaml                       1
using-scripts   uvx ruff@0.8.0 check .                       1
using-scripts   pipx run 'black==24.10.0' .                  1
using-scripts   npx package@version                          1
quickstart      .agents/skills/roll-dice/SKILL.md            3
quickstart      /skills                                      4
```

That loop is the entry's `recheck:` command, run here against scratch copies of the same bytes; the entry
carries the committed path. Predicate (a)/(d) self-check over the draft (my scratch script, not the
counter):

```
$ python3 <check>            # parses the entry, not a verifier; see § 7 for what it does not check
front keys: ['source', 'source', 'source', 'verified-at', 'recheck', 'ground']
src ids ['S<a>', 'S<b>', 'S<c>']
table data rows 3
best-practices  sid=S<a> words=12 tokens=3 located=3 action_words=24 row_bad_backticks=[]
using-scripts   sid=S<b> words=22 tokens=3 located=3 action_words=34 row_bad_backticks=[]
quickstart      sid=S<c> words=9  tokens=3 located=3 action_words=22 row_bad_backticks=[]
pages ['best-practices', 'quickstart', 'using-scripts']
OK predicate (a)+(d) shape
```

`row_bad_backticks=[]` is the deliberate check that **no** backticked span anywhere in a row (rule, quote,
tokens, action) is absent from that row's snapshot — the Q37 real-text shortcut, caught on the author side
before landing.

## 4. Prose claims, each with the line I read

Every line number in the entry was opened; the ones whose content is not self-evident from their own
sentence:

```
$ awk 'NR==96||NR==111||NR==119||NR==122||NR==129||NR==147||NR==169||NR==183||NR==231||NR==249 {print NR": "$0}' best-practices.md
96: … Match the specificity of your instructions to the fragility of the task.
111: **Be prescriptive** when operations are fragile, consistency matters, or a specific sequence must be followed:
119: python scripts/migrate.py --verify --backup
122: Do not modify the command or add additional flags.
129: When multiple tools or approaches could work, pick a default and mention alternatives briefly rather than presenting them as equal options.
147: A skill should teach the agent *how to approach* a class of problems, not *what to produce* for a specific instance. …
169: The highest-value content in many skills is a list of gotchas — environment-specific facts that defy reasonable assumptions.
183: Keep gotchas in `SKILL.md` where the agent reads them before encountering the situation. …
231: Instruct the agent to validate its own work before moving on. The pattern is: do the work, run a validator …
249: For batch or destructive operations, have the agent create an intermediate plan in a structured format, …

$ awk 'NR==13||NR==64||NR==76||NR==92||NR==96||NR==135||NR==153||NR==237||NR==252||NR==295||NR==301||NR==304 {print NR": "$0}' using-scripts.md
13: When an existing package already does what you need, you can reference it directly …
64: **deno run**
76: **go run**
92: * **Move complex commands into scripts.** …
96: Use **relative paths from the skill directory root** to reference bundled files. …
135: [PEP 723](https://peps.python.org/pep-0723/) defines a standard format for inline script metadata. …
153: uv run scripts/extract.py
237: This is a hard requirement of the agent execution environment. Agents operate in non-interactive shells …
252: ### Document usage with `--help`
295: **Separate data from diagnostics:** send structured data to stdout and progress messages, warnings, … to stderr.
301: * **Dry-run support.** For destructive or stateful operations, a `--dry-run` flag lets the agent preview what will happen.
304: * **Predictable output size.** Many agent harnesses automatically truncate tool output beyond a threshold …

$ awk 'NR==13||NR==17||NR==21||NR==23||NR==26||NR==44||NR==46||NR==47||NR==55||NR==62||NR==68 {print NR": "$0}' quickstart.md
13: * [VS Code](https://code.visualstudio.com/) with [GitHub Copilot](…)
17: > … The same skill works in any compatible agent, including Claude Code and OpenAI Codex.
21: A skill is a folder containing a `SKILL.md` file. VS Code looks for skills in `.agents/skills/` by default. …
23: ````markdown .agents/skills/roll-dice/SKILL.md theme={null}
26: description: Roll dice using a random number generator. Use when asked to roll a die (d6, d20, etc.), …
44: That's it — one file, under 20 lines. Here's what each part does:
46: * **`name`** — A short identifier for the skill. Must match the folder name.
47: * **`description`** — Tells the agent when to use this skill. This is how the agent decides whether to activate it.
55: 4. Type `/skills` to confirm that `roll-dice` appears in the list. …
62: > Tool-use reliability varies across models — some follow skill instructions and run commands consistently, …
68: 1. **Discovery** — When the chat session started, the agent scanned default skill directories and found your skill. …
```

The `Must` sweep the Limits section carries, run against the same bytes:

```
$ for p in best-practices using-scripts quickstart; do printf '%s must=%s hard=%s\n' $p \
    "$(grep -c -iE '\bmust\b' …/$p.md)" "$(grep -c -F 'hard requirement' …/$p.md)"; done
best-practices must=2 hard=0
using-scripts must=1 hard=1
quickstart must=1 hard=0
$ grep -n -iE '\bmust\b' …
best-practices.md:111: … a specific sequence must be followed:
best-practices.md:174:- The `users` table uses soft deletes. Queries must include
using-scripts.md:278:Error: --format must be one of: json, csv, table.
quickstart.md:46:* **`name`** — A short identifier for the skill. Must match the folder name.
```

So the entry's sentence "the only hard requirement any of the three states is using-scripts'
non-interactivity rule" rests on `hard=1` on one page only, and "two of the four `must` hits sit inside
examples" rests on the four lines above.

## 5. Dropped — staged package sentences the live pages do not carry, and why

The staged entries `spec-script-craft-rules.md` (S236/S237) and `spec-description-trigger-discipline.md`
(S231/S232) supplied the theme. Not carried into the entry:

1. **The vendor comparison around `.agents/skills/`** (TRAE toggle, Kimi groups, opencode tiers, Qwen Code
   root, "the specification's own answer to its own portability problem"). The quickstart says only
   "The same skill works in any compatible agent, including Claude Code and OpenAI Codex."
   (`quickstart.md:17`). The four-vendor readings are lane-owned (S217-S222,
   `chinese-vendor-skill-surfaces-round73.md`) and are not these pages' bytes. The entry carries the
   sentence, not the comparison.
2. **"the last unheld page of the `skill-creation/` set"** (staged, about using-scripts) — a claim about
   the package's inventory, not about the page. Not carried; the entry's `ground:` line states the lane's
   own 0-row baseline with its command instead.
3. **"the skill itself does not understand your code logic, it only perceives input and output"** —
   staged attributes this to TRAE while discussing S236; it is not on any of the three pages
   (`grep -c -F 'code logic' using-scripts.md` → `0`). Dropped.
4. **The staged eval-design numbers (20 queries, 8–10 should-trigger)** — those rest on
   `optimizing-descriptions.md` (S231), which is not one of the three pages this entry cites. Not carried;
   the entry names S213 as a sibling it does not re-open.
5. **The staged `recheck` dates (2026-10-23) and byte counts** — replaced by my own 2026-10-25 fetch and
   sha256s. The package's sizes still match exactly (`15 060 / 12 078 / 4 080` B), which is why the staged
   reads are consistent with today's bytes; the entry cites today's fetches, not the package's.

Also not carried, for the same reason (it is not these pages' text): the staged framing "the specification's
own trigger discipline" as a three-way tension with TRAE and Chiba Prefecture. That tension belongs to the
description entry (S213's ground), not to this one.

## 6. Findings for the L1 and for wave 2

**F1 — the C1 counter does not exist yet, so no C1 number can be printed.**
`ls verifiers/ | grep -iE 'spec_craft|sibling_reread'` → no line, exit `1`; `.ufo/waves/round-74/snapshots/`
→ `ls: cannot access …: No such file or directory`. The entry is therefore *draft-complete*, not
measured. The L1 must land `verifiers/check_spec_craft.py`, the three snapshots and `MANIFEST.sha256`
before any seat scores C1.

**F2 — the best-practices candidate's line labels point at headings, not at the quoted lines.**
`ExecSrcBestPracticesR74/rules-table.md` labels rule 1 `§ Match specificity to fragility (L98)`; the quote
is at L96 and L98 is the heading:

```
$ sed -n '96p;98p' ExecSrcBestPracticesR74/snapshot.md
96: Not every part of a skill needs the same level of prescriptiveness. Match the specificity of your instructions to the fragility of the task.
98: ### Match specificity to fragility
```

The same slip appears in rules 2 (`L88` is `### Structure large skills with progressive disclosure`, the
quoted sentence is L90) and 7 (`L145` is `### Favor procedures over declarations`, the quoted sentence is
L147). Rows 3, 4, 5, 6 (`L92`, `L111`, `L122`, `L129`) are correct. My entry cites 96/90/147, i.e. the
quote lines; if the L1 copies the candidate file's labels into the registry row's anchor or into
`SKILL.md` rows, three of them will be wrong by two lines.

**F3 — the two registry-row drafts disagree on `status`, and the predicate admits only one of them.**
`ExecSrcBestPracticesR74/row.md` ends `… | queued | 2026-10-25 | 90d | corpus/knowledge/spec-skill-creation-craft-round74.md |`;
`ExecSrcScriptsR74/row.md` gives `mined` as primary and `queued` as an alternative, with its own measured
reason: plan § C1 (b) requires `mined`, and its census probe printed
`file	E11	S900 missing used-by corpus/knowledge/spec-skill-creation-craft-round74.md` for `mined` with the
entry absent and `file	ok	…` once the entry is present. Since the entry lands in the same commit, `mined`
is the coherent choice for all three rows — but that is the L1's decision, and as of this writing the three
rows would land with two different statuses if copied as-is.

**F4 — snapshot naming: confirmed, not assumed.** The counter seat's text names
`.ufo/waves/round-74/snapshots/<page>.md`; the L1 confirmed in message that the names are exactly
`best-practices.md`, `using-scripts.md`, `quickstart.md`. The entry's `recheck:` and its line-number
citations use those names. If the names change, only the `recheck:` line needs a one-token edit.

**F5 — S-id placeholders are deliberate and the L1 owns the substitution.** The entry carries `S<a>`,
`S<b>`, `S<c>` in the three `source:` lines and in the table's `S id` column, plus the mapping implied by
page order. L1 decision (message): keep the placeholders; the L1 substitutes the minted ids before
measurement, because the counter reads real `S###` ids only. **If the counter is ever run on the entry
before that substitution, (a) and (b) will fail by construction** — that is the substitution's purpose, not
a defect in the entry.

**F6 — `best-practices.md` contains fenced pseudo-headings.** A heading scan of the page sees sections the
page does not have:

```
$ grep -n '^##' ExecSrcBestPracticesR74/snapshot.md
58:## Extract PDF text
65:## Extract PDF text
172:## Gotchas
```

All three sit inside ```` ```markdown ```` example fences (58 is the "too verbose" example, 65 the "better"
one, 172 the gotchas example). Any row anchor, reviewer or counter that derives sections by heading line
without fence-stripping will record them as page structure. My entry cites the real sections (`:48`,
`:52`, `:84`, `:88`, `:94`, `:127`, `:145`, `:167`, `:189`, `:214`, `:229`, `:247`, `:266`) and the one
example I cite by line (`:174`) is cited as an example, not a section.

**F7 — Q45 census information, not a census verdict.** Per-page usable rule tokens in the rows I checked:
best-practices ≥ 6 distinct (`references/` alone 4 hits), using-scripts ≥ 8, quickstart ≥ 4 — every page
clears "≥ 2" with margin, so `N == 3` looks satisfiable *for this seat's choice of tokens*. The census
number belongs to the Q45 census seat; this paragraph is information for it, not a claim of it.

## 7. Limits of this seat's work (what a reader should not infer)

- **No counter was run** (absent, F1) and **no lane gate was run.** No lane file was edited, so the
  no-harm battery is unaffected by this seat; the entry cannot change any measured number until the L1
  lands it.
- **My § 3 self-check is not the verifier.** It parses the draft and the snapshot bytes; it does not
  implement the registry checks (b), the manifest (c), the `SKILL.md` rows (e) or `PROVINCE.md` (f), and it
  is not committed. Its output is evidence about the draft's shape only.
- **No client was installed or run.** Everything here is what three pages state.
- **The pages can change without the URL changing.** The recheck line counts tokens rather than trusting
  the URL; the sha256s above are today's bytes only.
- **I did not verify the sibling claims** in `ExecSrcBestPracticesR74/row.md` about upstream mdx identity
  (`docs/skill-creation/best-practices.mdx` at `69ef37e…`); that seat carries its own command. My entry
  cites the `.md` route only.
- **Quote equality is literal against the fetched `.md` bytes** and `byte-exact` is used nowhere in the
  entry.

## 8. Files touched

- Drafted: `.ufo/waves/round-74/w1/build/ScribeEntrySpecR74/entry.md` (deliverable; placeholders intact).
- Written: this report, `.ufo/waves/round-74/w1/ScribeEntrySpecR74.md`.
- Scratch `/tmp/k74w1-ScribeEntrySpecR74.*` (three fetched pages, a scratch lane tree with the three
  snapshots, the wrapped seat spec) — deleted before return.
- Nothing else. No lane file edited; no git write; no `jj`; no fleet or sibling-lane write; no
  `/home/vgpnk/Projects/shokuknow` write.
- Tooling: no install or upgrade was performed (`curl`, `grep`, `awk`, `sed -n`, `python3` were already
  present); no `pacman` transaction was attempted.
