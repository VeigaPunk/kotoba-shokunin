# ScoutSpecCensusR74 — Q45 census for C1 (round 74, wave 1)

Seat: scout, read-only. Lane HEAD at run: `329e7d91d7d750031c35d264f0e34af1d0ce8385` (plan commit); the three pages fetched 2026-10-25 (`date -I`).

## Verdict

**`target stays 3 of 3`.** All three pages carry at least two rule tokens an entry can quote, so N_tokens_ge2 is true for each. The margin is thin on one page only: **quickstart** has 5 NEW rules, of which only 3 are strong (QS1, QS4, QS5), and QS1 overlaps routed item 5. No page is dropped.

| page | bytes (live `.md`) | N_tokens_ge2 | rules listed | with ≥2 tokens | NEW (≥2 tokens) | PARTLY HELD | HELD | margin over the 2 rows (e) needs |
|---|---|---|---|---|---|---|---|---|
| best-practices | 15,060 | **true** | 15 | 13 | **9** (+2 NEW with one token: BP1, BP13) | 3 (BP5, BP6, BP14) | 1 (BP7) | 7 |
| using-scripts | 12,078 | **true** | 12 | 12 | **11** | 1 (US2) | 0 | 9 |
| quickstart | 4,080 | **true** | 8 | 8 | **5** (strong 3: QS1, QS4, QS5; weak: QS6, QS8) | 1 (QS7) | 2 (QS2, QS3) | 3 nominal, **0–1 strict** |

"Strict" margin for quickstart: drop QS1 (item 5 may absorb the root row), QS6 and QS8, and exactly QS4 and QS5 remain, plus the PARTLY HELD QS7. The target is still reachable.

NEW means the lane's guidance holds no form of the rule. Evidence is the python sweep over `corpus/**` plus `SKILL.md` and `PROVINCE.md` (`/tmp` script, scratch deleted). The held regexes had false positives and I read the hit lines. PARTLY HELD names the nearest held rule and the delta the row must state.

## Sources opened (house form: URL, HTTP status, access date, bytes, sha256; the S212/S213 rows were read, upstream anchor `agentskills/agentskills@69ef37e`)

`curl -sL --max-time 60 -A 'Mozilla/5.0'`, 2026-10-25:

| URL | HTTP | bytes | sha256 |
|---|---|---|---|
| https://agentskills.io/skill-creation/best-practices.md | 200 | 15,060 | `ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41` |
| https://agentskills.io/skill-creation/using-scripts.md | 200 | 12,078 | `2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f` |
| https://agentskills.io/skill-creation/quickstart.md | 200 | 4,080 | `7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb` |
| https://agentskills.io/skill-creation/best-practices (no `.md`) | 200 | 389,017 | `32d67e92…` (HTML; above the 300 KB snapshot cap, so not a snapshot candidate) |
| https://agentskills.io/skill-creation/using-scripts (no `.md`) | 200 | 432,113 | `0c7bfaeb…` (HTML) |
| https://agentskills.io/skill-creation/quickstart (no `.md`) | 200 | 271,472 | `985c2786…` (HTML) |
| raw.githubusercontent.com/agentskills/agentskills/main/docs/skill-creation/best-practices.mdx | 200 | 14,608 | `a729bc1d…` |
| …/using-scripts.mdx | 200 | 12,405 | `06418578…` |
| …/quickstart.mdx | 200 | 3,844 | `a6614e81…` |

- **Upstream anchor.** `git ls-remote https://github.com/agentskills/agentskills HEAD refs/heads/main` returns `69ef37e9424c0a7ea9dd2293b559e43ec8176379` for both, the S212/S213 anchor.
- **Last commit per file.** GitHub commits API, `path=docs/skill-creation/<p>.mdx`, `per_page=1`:
  - best-practices.mdx: `b8d2613ac050aa4aa8bfb2cf28380d81cdfcd1ca`, 2026-04-19, "Point "progressive disclosure" links at `specification.mdx`".
  - using-scripts.mdx: `6102affec88b137de8e213987aa1c49fcfde48a7`, 2026-02-27.
  - quickstart.mdx: `8aeff476971ff1d4eb87a49568678c3f71c38f68`, 2026-04-19.
- **Stable fetch.** A second `.md` fetch gave identical sha prefixes for all three. The byte counts equal the staged rows S232, S236 and S237 (15 060, 12 078, 4 080, 2026-10-23): no drift in 2 days.
- **`.md` vs `.mdx`.** Every token in the table below was located word-bounded in both the `.md` and the `.mdx` (the `md=`/`mdx=` columns of the scratch run were equal on all 80+ tokens). The `.md` is the better snapshot: 15 KB, markup stripped of components. The `.mdx` wraps examples in `<Tabs>`/`<Note>`. The HTML contains the rule text too (`grep -c 'Provide defaults, not menus' best-practices.html` returned 3).
- **Fence and line counts.** Fenced blocks: best-practices 14 over 277 lines, using-scripts 20 over 304, quickstart 3 over 83.
- **Inline backticked tokens outside fences** (unique): best-practices 8, using-scripts 42, quickstart 7.
- **Double-quoted spans of ≥5 words as printed in the page prose** (straight ASCII quotes): best-practices 6, using-scripts 1, quickstart 0.
  - Do not read conjunct (a) as "tokens must be double-quoted *in the page*". The plan's wording is the entry's quote located in the page. Read the page-literal way, quickstart would score 0 and using-scripts 1, and the target would fall to 1 of 3. Say in the counter docstring that the quote is the entry's, located in the page.

## Rule tables (quote lines pasted from `sed -n '<n>p'` on the live `.md`, cut at 150 chars)

### Rules — best-practices.md

| id | line | status vs lane | rule (what an author does differently) | `sed -n '<n>p'` (first 150 chars) |
|---|---|---|---|---|
| BP1 | 78 | NEW | omit what the agent already knows; test each piece with the "would the agent get this wrong" question | `` Ask yourself about each piece of content: "Would the agent get this wrong without this instruction?" If the answer is no, cut it. If you're unsure, te `` |
| BP2 | 96 | NEW | match specificity to fragility: exact command + do-not-modify for fragile ops; freedom plus the why otherwise | `` Not every part of a skill needs the same level of prescriptiveness. Match the specificity of your instructions to the fragility of the task. `` |
| BP3 | 129 | NEW | one default plus a named escape hatch, never a menu | `` When multiple tools or approaches could work, pick a default and mention alternatives briefly rather than presenting them as equal options. `` |
| BP4 | 161 | NEW | procedure over declaration: teach the approach, keep specifics as templates/constraints | `` This doesn't mean skills can't include specific details — output format templates (see [Templates for output format](#templates-for-output-format)), c `` |
| BP5 | 183 | PARTLY HELD (anatomy-and-compression rule 4 "Failure signatures inline") | gotchas live in SKILL.md body, not a reference file; every correction you make becomes a gotcha | `` Keep gotchas in `SKILL.md` where the agent reads them before encountering the situation. A separate reference file works if you tell the agent when to `` |
| BP6 | 92 | PARTLY HELD (rule 2 "the skill keeps the pointer line") | a pointer states WHEN to load the file (condition), not "see references/" | `` The key is telling the agent *when* to load each file. "Read `references/api-errors.md` if the API returns a non-200 status code" is more useful than  `` |
| BP7 | 90 | HELD (SOURCES.md:14,16; frontmatter-rule-authorities-round48.md:49; SKILL.md:170) | SKILL.md under 500 lines / 5,000 tokens | `` The [specification](https://agentskills.io/specification.md#progressive-disclosure) recommends keeping `SKILL.md` under 500 lines and 5,000 tokens — j `` |
| BP8 | 191 | NEW | give a template for output format; long/rare ones in assets/ referenced from SKILL.md | `` When you need the agent to produce output in a specific format, provide a template. This is more reliable than describing the format in prose, because `` |
| BP9 | 231 | NEW | validation loop: do, validate, fix, repeat until it passes | `` Instruct the agent to validate its own work before moving on. The pattern is: do the work, run a validator (a script, a reference checklist, or a self `` |
| BP10 | 249 | NEW | plan-validate-execute for batch/destructive work; validator error lists the valid names | `` For batch or destructive operations, have the agent create an intermediate plan in a structured format, validate it against a source of truth, and onl `` |
| BP11 | 216 | NEW | explicit progress checklist for multi-step workflows with dependencies | `` An explicit checklist helps the agent track progress and avoid skipping steps, especially when steps have dependencies or validation gates. `` |
| BP12 | 82 | NEW | scope a skill as one coherent unit (not too narrow, not too broad) | `` Deciding what a skill should cover is like deciding what a function should do: you want it to encapsulate a coherent unit of work that composes well w `` |
| BP13 | 44 | NEW | read execution traces, not just outputs; three named causes of wasted steps | `` > Read agent execution traces, not just final outputs. If the agent wastes time on unproductive steps, common causes include instructions that are too `` |
| BP14 | 86 | PARTLY HELD (rules 1 and 6 spend/size) | moderate detail: stepwise guidance + one working example | `` Overly comprehensive skills can hurt more than they help — the agent struggles to extract what's relevant and may pursue unproductive paths triggered  `` |
| BP15 | 268 | NEW | script it once when traces show the agent reinventing logic | `` When [iterating on a skill](https://agentskills.io/skill-creation/evaluating-skills.md), compare the agent's execution traces across test cases. If yo `` |

### Rules — using-scripts.md

| id | line | status vs lane | rule (what an author does differently) | `sed -n '<n>p'` (first 150 chars) |
|---|---|---|---|---|
| US1 | 90 | NEW | pin versions in one-off commands | `` * **Pin versions** (e.g., `npx eslint@9.0.0`) so the command behaves the same over time. `` |
| US2 | 91 | PARTLY HELD (SKILL.md:232-234 fail-closed path / `metadata.requires`) | state prerequisites in the body; runtime-level ones in `compatibility` | `` * **State prerequisites** in your `SKILL.md` (e.g., "Requires Node.js 18+") rather than assuming the agent's environment has them. For runtime-level r `` |
| US3 | 92 | NEW | move a hard-to-get-right command into a tested script | `` * **Move complex commands into scripts.** A one-off command works well when you're invoking a tool with a few flags. When a command grows complex enou `` |
| US4 | 96 | NEW | script paths relative to the skill directory root | `` Use **relative paths from the skill directory root** to reference bundled files. The agent resolves these paths automatically — no absolute paths need `` |
| US5 | 98 | NEW | list available scripts in SKILL.md, then instruct the run | `` List available scripts in your `SKILL.md` so the agent knows they exist: `` |
| US6 | 129 | NEW | self-contained script: inline deps (PEP 723), run with uv run | `` When you need reusable logic, bundle a script in `scripts/` that declares its own dependencies inline. The agent can run the script with a single comm `` |
| US7 | 237 | NEW | no interactive prompts; missing input = error naming the flag | `` This is a hard requirement of the agent execution environment. Agents operate in non-interactive shells — they cannot respond to TTY prompts, password `` |
| US8 | 254 | NEW | --help is the interface; keep it short | `` `--help` output is the primary way an agent learns your script's interface. Include a brief description, available flags, and usage examples: `` |
| US9 | 275 | NEW | error says what went wrong, what was expected, what to try | `` When an agent gets an error, the message directly shapes its next attempt. An opaque "Error: invalid input" wastes a turn. Instead, say what went wron `` |
| US10 | 295 | NEW | structured data on stdout, diagnostics on stderr | `` **Separate data from diagnostics:** send structured data to stdout and progress messages, warnings, and other diagnostics to stderr. This lets the age `` |
| US11 | 299 | NEW | idempotent commands (create-if-not-exists) | `` * **Idempotency.** Agents may retry commands. "Create if not exists" is safer than "create and fail on duplicate." `` |
| US12 | 304 | NEW | dry-run, exit codes, confirm flags, bounded output (--offset/--output) | `` * **Predictable output size.** Many agent harnesses automatically truncate tool output beyond a threshold (e.g., 10-30K characters), potentially losin `` |

### Rules — quickstart.md

| id | line | status vs lane | rule (what an author does differently) | `sed -n '<n>p'` (first 150 chars) |
|---|---|---|---|---|
| QS1 | 21 | NEW (overlaps routed item 5 root row) | spec tutorial default root `.agents/skills/<name>/SKILL.md` | `` A skill is a folder containing a `SKILL.md` file. VS Code looks for skills in `.agents/skills/` by default. Create `.agents/skills/roll-dice/SKILL.md` `` |
| QS2 | 46 | HELD (SKILL.md:157 name equal to the directory; S018) | name must match folder name | `` * **`name`** — A short identifier for the skill. Must match the folder name. `` |
| QS3 | 26 | HELD in substance (frontmatter-trigger-surface.md:89 rule 2 quote trigger strings; SKILL.md Anti-patterns row 1) | description: capability sentence then "Use when asked to ..." phrasings | `` description: Roll dice using a random number generator. Use when asked to roll a die (d6, d20, etc.), roll dice, or generate a random dice roll. `` |
| QS4 | 55 | NEW | verify discovery with `/skills` (VS Code) and check the path against the project root | `` 4. Type `/skills` to confirm that `roll-dice` appears in the list. If it doesn't, check that the file is at `.agents/skills/roll-dice/SKILL.md` relati `` |
| QS5 | 62 | NEW | tool-use reliability varies by model: try another model before blaming the skill | `` > Tool-use reliability varies across models — some follow skill instructions and run commands consistently, while others may attempt to answer on thei `` |
| QS6 | 68 | NEW to SKILL.md (SOURCES-only mentions of the concept) | discovery reads name+description only; activation loads body | `` 1. **Discovery** — When the chat session started, the agent scanned default skill directories and found your skill. It read only the `name` and `descr `` |
| QS7 | 40 | PARTLY HELD (rule 3 verbatim-copyable, no guessing placeholders) | literal command with `<sides>` placeholder plus a Replace line; bash and PowerShell variants | `` Replace `<sides>` with the number of sides on the die (e.g., 6 for a standard `` |
| QS8 | 44 | NEW but weak (an observation, no author action) | a skill can be one file under 20 lines | `` That's it — one file, under 20 lines. Here's what each part does: `` |

### Tokens per rule (word-bounded in the live `.md`; counted by the scratch census script)

- **best-practices:** BP1 1 (+`pdfplumber`, an example, not a rule token); BP2 3; BP3 2; BP4 3; BP5 3 (2 raw, 1 when the page's backticks around `SKILL.md` are kept); BP6 2; BP7 2; BP8 2 (the `store them in assets/` form needs the page's backticks); BP9 2; BP10 3; BP11 2; BP12 2; BP13 1; BP14 2; BP15 2.
- **using-scripts:** US1 4; US2 3; US3 2; US4 3; US5 2; US6 4; US7 3; US8 2; US9 2; US10 4; US11 2; US12 6.
- **quickstart:** QS1 3; QS2 2; QS3 2; QS4 3; QS5 2; QS6 2; QS7 3; QS8 2.

Command: `python3 /tmp/k74w1-census.py` (scratch, deleted). It was run against the files named above; its stdout matched the counts here.

## Held-ness evidence (Q38/Q43; the lane's own files)

- **Base phrase sweep.** On the lane tree at `329e7d9`, a Python sweep (case-insensitive, over `corpus/**`, `SKILL.md`, `PROVINCE.md`) found 0 hits for each of: `degrees? of freedom`, `too many options`, `gotchas?`, `validation loops?`, `plan-validate-execute`, `moderate detail`, `already knows?`, `would the agent get this wrong`, `defaults?,? not menus`, `fragil`, `prescriptive`, `procedures? over declarations`, `coherent unit`, `execution traces?`, `real expertise`, `dry-run`, `idempoten`, `PEP 723`, `uv run`, `uvx`, `pipx`, `bunx`, `structured output`, `meaningful exit codes?`, `separate data from diagnostics`, `pin(ning)? versions?`, `relative paths? from the skill`, `skill directory root`, `Available scripts`, `roll-dice`, `references/api-errors`. `npx` hits only the baseline pin (`SKILL.md:517`).
- **S019 holds the Anthropic form of two rules.** The live page `…/agent-skills/best-practices.md` (200, 42,155 B, sha256 `a1145a06cdf3dbd0c152165d759290ae69f5c72a4cfa47de161cc2bd94de1259`, 2026-10-25) has `sed -n '61p'` → `### Set appropriate degrees of freedom`, `sed -n '859p'` → `### Avoid offering too many options`, and `sed -n '867p'` → `**Good example: Provide a default** (with escape hatch):`. So BP2 and BP3 are held as an opened source, but nothing in the lane's guidance carries them (0 phrase hits). **Label: NEW to the guidance, held under another wording in S019's source page.** The row must say so (Q38/Q43) and cite S019 beside the agentskills.io id.
- **S019 drift.** The S019 row records 42,169 B, sha256 `f0a5d61b…`, fetched 2026-10-22. Live now: 42,155 B, `a1145a06…`. The page changed by 14 bytes. I did not diff it. This is a freshness fact for whoever re-opens S019.
- **HELD.**
  - BP7: `SOURCES.md:14` and `:16`, `knowledge/frontmatter-rule-authorities-round48.md:49`, `SKILL.md:170` (the 5,000-token warning).
  - QS2: `SKILL.md:157` ("equal to the directory"), `SOURCES.md:14`.
  - QS3: `knowledge/frontmatter-trigger-surface.md:89` ("2. **Quote literal trigger strings.**") and `SKILL.md` Anti-patterns row 1 ("description without trigger strings").
- **PARTLY HELD (the rule differs; the row must state the delta).**
  - `corpus/knowledge/anatomy-and-compression.md` rule 4 "Failure signatures inline": "Be careful" without a signature is noise (BP5; the delta is "gotchas stay in SKILL.md, every correction is added").
  - Rule 2: the skill keeps the pointer line (BP6; the delta is "the pointer states the load condition").
  - Rule 3: "No placeholders that require guessing the shape" (QS7; the delta is a placeholder is fine with an explicit Replace line).
  - Rules 1 and 6: token spend and the 600-line bound (BP14).
  - `SKILL.md:232-234` (checklist: a procedure's tool has a fail-closed path or is declared in `metadata.requires`) (US2).

## Hazards for the counter and the entry (found while locating tokens)

1. **Do not use `\b` for word-bounded location.** Observed: `re.search(r'\b\.agents/skills/\b', 'VS Code looks for skills in `.agents/skills/` by default.')` → `False`; with `(?<![\w-])…(?![\w-])` → `True`. `\b--dry-run\b` is `False` on the page text, the lookaround form `True`. Tokens that begin with `.` or `-`, or end with `/`, `?` or `.`, are lost by `\b`. The plan says "word-bounded" without a definition; fix it in the docstring before data.
2. **Markup in quote text.** Conjunct (d) permits "whitespace collapse only". Page sentences carry `*emphasis*`, `**bold**` or `\_` (best-practices lines 54, 96-100, 147, 161, 264; using-scripts line 96). A quote that drops the markup fails to locate. Pick sentences without markup, or keep the page's backticks verbatim: BP5 line 183 and US2 line 91 only match with the backticks around `SKILL.md`.
3. **Escaped underscores.** `Field 'signature\_date' not found` (best-practices:264) cannot be matched by the unescaped form.
4. **Fence info lines.** `theme={null}` is in the page text of fence openers; do not quote across a fence opener.
5. **Quote length (d).** 5–25 words. I did not word-count every sentence; BP5's line 183 sentence is about 14 words and the QS3 description about 19. The BP1 line 78 sentence is followed by more sentences, so quote only the first. Count with the counter's own tokenizer.
6. **Rule tokens as tokens.** `stdout`, `stderr`, `field_values.json` and `Pin versions` hit many times: legal, but a counter that requires "exactly one location" fails them. State that ≥1 location is enough.

## SKILL.md-side view (where the rules go, without duplicating)

- **Current homes** (`grep -n '^## \|^### ' SKILL.md`):
  - `## Frontmatter craft — the trigger surface` is lines 153-189. It holds the portability floor (157), `### Description thresholds by client` (159) and `### Explicit invocation by client` (173). Line 188 is the bullet "Testing a skill — the Agent Skills guides' artefacts" (S212/S213).
  - `## Compression rules` is lines 190-198, a nine-line pointer to `corpus/knowledge/anatomy-and-compression.md` § Compression rules (six rules; line 195 names "verbatim-copyable command blocks, failure signatures inline").
- **Placement.** The plan's `### Body craft — the specification's skill-creation guides` belongs under `## Compression rules` (insert after line 198), not under Frontmatter craft. These rules are about the body and scripts of a skill, and Frontmatter craft is the trigger surface (name, description, listing). Only QS1/QS2/QS3 touch the frontmatter or root, and QS2 and QS3 are HELD. Frontmatter craft's line 188 bullet already links to the testing guide, so BP13 (traces) and BP15 (script once) can cross-reference it in a cell, not repeat.
- **Rows to omit as duplicates:** BP7, QS2, QS3. Rows that must state their delta: BP5, BP6, BP14, QS7, US2 (above).
- **Budget** (plan: +14 lines for C1). Twelve rows exceed it. Suggested set of 7-8 one-line rows, 2+ per page: BP2 (fragility), BP3 (default), BP9/BP10 (validation loop and plan-validate-execute, one row), BP12 (coherent unit); US1+US3 (pin, script it), US7 (no prompts), US10+US12 (stdout/stderr, dry-run, bounded output); QS1 (root; coordinate with routed item 5, not both), QS4+QS5 (verify with `/skills`, retry on another model). `SKILL.md` is 570 lines and 74 lines exceed 300 characters at base, so keep each row under 300 characters.
- **Client scope.** QS4 (`/skills`) and QS5 are VS Code tutorial facts. The page says "This tutorial uses VS Code" (quickstart:17). A row must say VS Code, not "all clients" (Q27).

## Unobserved / limits

- Rule truth against each page is a reviewer judgement the counter cannot make (plan Bound, Q26/Q51). I only located tokens and compared against the lane's text.
- I did not diff the S019 page against the lane's earlier copy.
- I wrote no committed lane file and saved no snapshots (the sources seats own them). The scratch dir (`mktemp -d /tmp/k74w1-ScoutSpecCensusR74.XXXX`) is deleted below. Tools installed: none.
