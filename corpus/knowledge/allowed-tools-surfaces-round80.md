source: S226 — Agent Skills — Specification — https://agentskills.io/specification.md — § Frontmatter and § `allowed-tools` field — located quote "The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental." (snapshot `S226-spec.md`)
source: S227 — Claude Code — Extend Claude with skills — https://code.claude.com/docs/en/skills.md — § Frontmatter reference and § Pre-approve tools for a skill — located quote "`allowed-tools` field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval." (snapshot `S227-claude.md`)
source: S228 — Factory — Skills — https://docs.factory.com/harness/skills — § Frontmatter reference and § Declare intended tools — located quote "`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces" (snapshot `S228-factory.md`)
source: S229 — Microsoft Agent Framework — Agent skills — https://learn.microsoft.com/en-us/agent-framework/agents/skills — § SKILL.md format — located quote "allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations." (snapshot `S229-msaf.html`)
source: S230 — badlogic/pi-mono — coding-agent docs: skills.md — https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md — § Write portable frontmatter — located quote "allowed-tools \| Experimental pre-approved tool list" (snapshot `S230-pi.md`)
source: S231 — Mistral Vibe — README (skills system) — https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md — § Creating Skills, § Custom Agent Configurations and § Tool Management — located quote "user-invocable: true allowed-tools: read grep ask_user_question" (snapshot `S231-vibe.md`)
verified-at: 2026-10-27
recheck: 30d — `for p in 'https://agentskills.io/specification.md|Space-separated string of pre-approved tools' 'https://code.claude.com/docs/en/skills.md|without asking permission during the turn' 'https://docs.factory.com/harness/skills|does not add tools' 'https://learn.microsoft.com/en-us/agent-framework/agents/skills|Space-delimited list of pre-approved tools' 'https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md|Experimental pre-approved tool list' 'https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md|allowed-tools:'; do u=${p%%|*}; q=${p#*|}; printf '%s ' "$(curl -fsSL -A Mozilla/5.0 --max-time 60 "$u" | grep -c -F -- "$q")"; done` — prints `1 1 2 1 1 1` on 2026-10-27 (command exit 0), in the order spec, claude, factory, msaf, pi, vibe; any 0 means the page moved or the fetch failed, which is a re-open, never a silent edit. The factory URL is the canonical page; the assigned `docs.factory.ai/cli/configuration/skills` 308s here via `docs.factory.com/cli/configuration/skills`. The factory anchor token occurs twice in the served HTML and once in the same page's Markdown route `docs.factory.com/harness/skills.md`; the numbers above are printed from the canonical URL. The recheck counts anchor tokens, not digests: the Microsoft Agent Framework page is served non-deterministically, so its digest can never be the recheck predicate.
ground: no knowledge entry states what the `allowed-tools` frontmatter field means in a named client at base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`: `git grep -lE 'allowed-tools|allowed_tools' 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93 -- corpus/knowledge SKILL.md` (run 2026-10-27) prints two files — `corpus/knowledge/frontmatter-rule-authorities-round48.md` (2 hits) and `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` (5 hits) — and `git grep -c 'allowed-tools' 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93 -- SKILL.md` exits 1 with 0 hits. Neither entry maps the field to a grant: the first repeats the specification's own value form, the second records the key as one CodeBuddy frontmatter name among fourteen.

# `allowed-tools` in six clients: one field name, three value forms, four grant semantics

The lane's corpus names this frontmatter key twice and never says what a client does with it. Six pages opened on 2026-10-27 do state it, and they disagree on both halves of the field.
The value form differs: a space-separated string in the open specification and a "space-delimited list" in Microsoft Agent Framework, a "space- or comma-separated string, or a YAML list" in Claude Code, and a YAML block sequence in the worked examples of Factory and Mistral Vibe, while pi's page prints the field with a one-line purpose and no form at all.
The grant differs more sharply: Claude Code documents a per-turn permission pre-approval that expires with your next message and, in the same paragraph, says it "does not restrict which tools are available"; Factory documents review metadata that "does not add tools or sandbox standard skill invocation" and is explicitly "not a security boundary"; the specification, Microsoft Agent Framework and pi carry "pre-approved" together with "Experimental"; and Vibe's example writes the field without stating any semantics for it anywhere on the page.

Everything below is documentary: six pages fetched and pinned, no client installed, loaded, routed or refused.
"Pre-approved", "does not add tools" and "Experimental" are the pages' own words, quoted from the snapshots, never observations of a runtime.
The entry also records a page-internal tension rather than resolving it — Vibe says it follows the Agent Skills specification for format and then prints the list form the specification's own field table calls a space-separated string — because no page read here says which form Vibe parses.

Source-register provenance note: S230's inherited `SOURCES.md` anchor currently attributes revision id `7bb48f21…` to `badlogic/pi-mono`, but this round's S230 fetch record gives the pi-mono main head as `bb65e3e4…` and the last path-touching revision as `25cc5c7b…`; S231's fetch record identifies `7bb48f21…` with Mistral Vibe. The rows are append-only and the anchor cell is not rewritten here; the documentary claim above rests on the pinned S230 snapshot and URL, not the suspect upstream revision attribution. A future correction must add a superseding source row under CORPUS rule 2.

Text view: a `.html` snapshot has its `script` and `style` blocks removed, its tags replaced by one space and its entities decoded; a Markdown snapshot has every backtick byte deleted and an unordered-list marker removed at a line start; every snapshot then has its whitespace collapsed to single spaces.
Every located quote below is stated in that view, and each was re-located in its own snapshot's committed bytes before this entry was written.
Citation form: each line below names one pinned snapshot file, and the pinned file is named by its registry id (`S226` → `S226-spec.md`, and so on for the other five); the divergence matrix carries the file-and-line map.

## The six surfaces

| surface | source | page tokens | grant | located quote |
|---|---|---|---|---|
| Open specification | S226 | `allowed-tools`, `space-separated`, `pre-approved`, `Experimental` | experimental | located quote "The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental." |
| Claude Code | S227 | `allowed-tools`, `space- or comma-separated string`, `YAML list`, `without prompting you for approval` | pre-approves | located quote "`allowed-tools` field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval." |
| Factory | S228 | `allowed-tools`, `Grep`, `metadata` | metadata-only | located quote "`allowed-tools` records the tools the skill is designed to use. Droid stores it as skill metadata and shows it in skill surfaces" |
| Microsoft Agent Framework | S229 | `allowed-tools`, `Space-delimited`, `pre-approved`, `Experimental` | experimental | located quote "allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations." |
| pi | S230 | `allowed-tools`, `pre-approved`, `Experimental` | experimental | located quote "allowed-tools \| Experimental pre-approved tool list" |
| Mistral Vibe | S231 | `allowed-tools`, `allowed-tools:`, `ask_user_question`, `user-invocable` | unstated | located quote "user-invocable: true allowed-tools: read grep ask_user_question" |

## Divergence matrix

| surface | value form the page prints | grant semantics the page states | where |
|---|---|---|---|
| Open specification | space-separated string; example `allowed-tools: Bash(git:*) Bash(jq:*) Read` | "pre-approved to run"; "Experimental. Support for this field may vary between agent implementations" | `S226-spec.md:35`, `:176-177`, example `:182` |
| Claude Code | "Accepts a space- or comma-separated string, or a YAML list" | per-turn grant: "without asking permission during the turn that invokes this skill", "The grant clears when you send your next message", and "It does not restrict which tools are available: every tool remains callable"; deny/ask rules override it; the restricting key is `disallowed-tools` | `S227-claude.md:404`, `:617`, `:405` |
| Factory | YAML block sequence (`- Read`, `- Grep`, `- Glob`) in both places the page prints it | "It is metadata for review, packaging, and UI display; it does not add tools or sandbox standard skill invocation"; "standard skill invocation is not a runtime sandbox"; "Do not rely on `allowed-tools` as a security boundary for skills" | `S228-factory.md:235-238`, `:254`, `:282`, `:298`, `:339` |
| Microsoft Agent Framework | "Space-delimited list of pre-approved tools the skill may use" | "Experimental - support may vary between agent implementations"; and "a collection where a scalar field is expected" prevents the skill from loading | `S229-msaf.html:818-820`, `:825` |
| pi | none stated: the page lists the field in a purpose table and stops | "Experimental pre-approved tool list" — no grant sentence beyond that line | `S230-pi.md:78` |
| Mistral Vibe | YAML block sequence under `allowed-tools:` in the page's worked `code-review` skill | none stated for the key; the page's tool gating is configured elsewhere: `disabled_tools`, per-tool `permission`, and an `allowlist` under `[tools.read_file]` | `S231-vibe.md:725-728`, `:969`, `:972-976`, `:1039-1040` |

**Three value forms under one name, and only one page states its tolerance.**
The specification calls the value a space-separated string of tools (`S226-spec.md:176`).
Claude Code is the only page that says which forms it accepts, and it accepts all three — "space- or comma-separated string, or a YAML list" (`S227-claude.md:404`).
Factory prints a block sequence in its own example, with no sentence on accepted forms (`S228-factory.md:235-238`).
Vibe prints a block sequence in its own example too, again with no sentence on accepted forms (`S231-vibe.md:725-728`).
Microsoft Agent Framework's field table says "space-delimited list" and its next paragraph says "a collection where a scalar field is expected" prevents loading (`S229-msaf.html:818`, `:825`), so the list form those two examples use is a load risk on that page's own wording.
None of the six pages states what happens to an unknown tool name in the list.

**The name promises restriction; four pages do not grant it.**
Claude Code states the negative in the same paragraph as the grant: the field pre-approves during one turn and "does not restrict which tools are available: every tool remains callable" (`S227-claude.md:617`).
Factory states it twice, and adds the enforcement path — a custom droid tool policy or a restricted subagent (`S228-factory.md:254`, `:282`, `:298`).
The specification qualifies the promise with "Experimental" (`S226-spec.md:177`).
Microsoft Agent Framework qualifies it the same way (`S229-msaf.html:818`).
pi qualifies it the same way (`S230-pi.md:78`).
Vibe's page never promises anything for the key.
Where a restricting mechanism is documented, it is a different field or file.
On Claude Code that is `disallowed-tools` plus permission settings (`S227-claude.md:405`, `:617`).
On Vibe it is `disabled_tools`, per-tool `permission` and an `[tools.read_file] allowlist` (`S231-vibe.md:969`, `:972-976`, `:1039-1040`).

**Vibe claims the specification and prints a list.**
The page's own sentence is "Vibe follows the [Agent Skills specification](https://agentskills.io/specification) for skill format and structure" (`S231-vibe.md:712`), and its example four lines later writes `allowed-tools:` as a block sequence of three items (`:725-728`).
The form the specification's field table calls a space-separated string is spelled that way on the specification's own page (`S226-spec.md:35`).
Both are page bytes; which form Vibe's parser follows is not stated anywhere in the fetched bytes, so this entry records the tension and assigns the reading to review.

**What survives a move between clients.**
Claude Code's distribution table keeps `allowed-tools` when a skill leaves Claude Code — claude.ai uploads, the Skills API and `package_skill.py` accept exactly the six specification fields, `allowed-tools` among them (`S227-claude.md:420-425`) — and any other Claude Code field hard-errors with a message that lists those six names (`:432`).
The field that restricts, `disallowed-tools`, is not on that list.
A body that carries both therefore keeps the pre-approval and loses the restriction on that path, by the page's own table.

**Per-client grant semantics, in the client's own words.**
Open specification: the value is "A space-separated string of tools that are pre-approved to run" and the support "may vary between agent implementations" (`S226-spec.md:176-177`).
Claude Code: "grants permission for the listed tools during the turn that invokes the skill", the grant "clears when you send your next message", and "It does not restrict which tools are available" (`S227-claude.md:617`).
Factory: "It is metadata for review, packaging, and UI display; it does not add tools or sandbox standard skill invocation" and "standard skill invocation is not a runtime sandbox" (`S228-factory.md:254`, `:282`).
Microsoft Agent Framework: "Space-delimited list of pre-approved tools the skill may use", marked "Experimental - support may vary between agent implementations" (`S229-msaf.html:820`).
pi: "Experimental pre-approved tool list" — the whole of the page's statement (`S230-pi.md:78`).
Mistral Vibe: the key appears once, in a worked example, with no semantics stated for it anywhere on the page (`S231-vibe.md:725`).

## The cross-client conflict: a skill that relies on `allowed-tools` for restriction is wrong on at least one client

The field's name reads as a restriction and its pages mostly read as a pre-approval, so a skill body that lists a tool in `allowed-tools` and relies on the rest being blocked is contradicted on at least one client, and on two of the six it is contradicted twice over.

- **Claude Code** grants the listed tools for one turn and says in the same paragraph that it "does not restrict which tools are available: every tool remains callable" (`S227-claude.md:617`).
- The restriction on that client is a different key — `disallowed-tools` — with its own clearing rule (`S227-claude.md:405`).
- **Factory** says the field "does not add tools or sandbox standard skill invocation" (`S228-factory.md:254`), and "standard skill invocation is not a runtime sandbox" (`S228-factory.md:282`).
- Factory closes the section with the instruction "Do not rely on `allowed-tools` as a security boundary for skills. To enforce tool access, use a custom droid with a tool policy or run the workflow in a restricted subagent" (`S228-factory.md:298`).
- Its troubleshooting item repeats the negative: "`allowed-tools` does not grant new tools" (`S228-factory.md:339`).
- **Microsoft Agent Framework** marks the grant "Experimental", so even the pre-approval is not a promise of behaviour (`S229-msaf.html:818`).
- **pi** marks its one line the same way (`S230-pi.md:78`).
- **The open specification** promises only "pre-approved to run" and says support "may vary between agent implementations" (`S226-spec.md:176-177`); it never says the field removes anything.
- **Mistral Vibe** states nothing, so it is the one client of the six on which the question cannot be answered from the page at all (`S231-vibe.md:725`).

So the reading that holds across the whole set is the narrow one: `allowed-tools` is, at most, a per-turn pre-approval on one client, review metadata on another, an experimental hint on three, and an unstated example on the sixth.
Where a skill needs a tool absent from the session, or needs the other tools blocked, listing a tool in `allowed-tools` is the wrong mechanism on every client that says anything about it.

## What an author should do

- **Treat the field as pre-approval, never as a sandbox.** Claude Code grants it for one turn and then clears it, and says it "does not restrict which tools are available" (`S227-claude.md:617`).
- Factory says it "does not add tools or sandbox standard skill invocation" and is "not a security boundary" (`S228-factory.md:254`, `:298`).
- A workflow that needs a tool absent from the session is not fixed by listing it (`S228-factory.md:282`).
- **Put the restriction where the page puts it.** Claude Code's `disallowed-tools` plus permission settings (`S227-claude.md:405`, `:617`).
- Vibe's `disabled_tools`, per-tool `permission` and `[tools.read_file] allowlist` (`S231-vibe.md:969`, `:972-976`, `:1039-1040`).
- Listing a tool in `allowed-tools` and expecting the rest to be blocked is contradicted by the first page and unsupported by the other five.
- **Write the form the target page prints, and prefer the scalar.** The specification's space-separated string is the scalar form (`S226-spec.md:176`).
- That scalar is what Microsoft Agent Framework's bytes call a scalar, and that page says a collection where a scalar is expected prevents loading (`S229-msaf.html:825`).
- The list form is what Factory prints in its example (`S228-factory.md:235-238`).
- The list form is also what Vibe prints in its example (`S231-vibe.md:725-728`).
- It is also what Claude Code says it accepts (`S227-claude.md:404`).
- Choose per client, and do not assume the list form travels.
- **Budget for one turn, not one session, on Claude Code.** The grant clears when you send your next message, and the page names permission settings for a session-wide allow rule (`S227-claude.md:617`); a skill that needs standing approval is relying on the wrong mechanism.
- Under managed settings the grant does not apply at all, and the page states the version floor for that rule (`S227-claude.md:305`, `:643`).
- **If the skill ships to claude.ai or the Skills API, keep the frontmatter to the specification's six fields.** `allowed-tools` survives that path; every other Claude Code-only key hard-errors (`S227-claude.md:421-432`).

## Limits

- **Documentary evidence only.** Six pages were fetched and pinned on 2026-10-27; no client was installed, loaded or run, and no claim here is about observed parsing, acceptance, refusal or enforcement.
- "Supports" and "parses" appear only where a page says so.
- **The Microsoft Agent Framework page is not byte-stable, so its pin is the snapshot, not the URL.** The served page carries Akamai Bot Manager instrumentation whose per-response seed changes between fetches.
- An independent fetch on 2026-10-27 returned the same 157339 B but a different digest (`20fd76d8…` against the pinned `34016233…`), and `diff -u` against the committed snapshot showed five changed lines: two asset-version lines (`/static/assets/0.4.03574.8308-…` → `/static/assets/0.4.03585.8328-…`), the bot-manager script tag (`/akam/13/41ddb17` → `/akam/13/41ddb15`) and the noscript pixel path beside it.
- The r79 sentinel measured the same class earlier in the day at a different size (156963 B, `8fc249df…`).
- No credential is involved — it is a server-issued bot-detection seed and beacon URL.
- The consequence is that a fetch-and-compare-digest recheck can never pass for this page; the recheck predicate is the anchor-token count, and the pin is the committed snapshot's digest (`S229-msaf.html`).
- **`main`-branch raw URLs move; the pin names the opened snapshot.** The pi-mono and the mistral-vibe files are `raw.githubusercontent.com` files served from a branch head, not a versioned URL.
- The fetch records resolve the heads, but no record carries a commit field: the served revision is named in the `note` prose, and the record's other fields are the URL, the status, the byte count, the digest, the fetch time and the user agent. The pi-mono `main` head at fetch time was newer than the last change to the fetched path (2026-09-22), so the served blob was already older than the head (`S230-pi.md`, record `S230.fetch.json`).
- The mistral-vibe README was served from the repository head named in that page's fetch record, and the revision-pinned raw URL served the same bytes (`S231-vibe.md`, record `S231.fetch.json`).
- Every citation here is to the pinned snapshot, not to the URL.
- **Snapshot forms differ, and so do the line numbers and the text view.** One snapshot is the raw served HTML and its line numbers are HTML lines (the field row is a `<td>` cell at `:818`, in a `<h3 id="skillmd-format">` section opened at `:771`) (`S229-msaf.html`).
- The other five are Markdown, except that one of them is a Markdown route of a canonical page.
- The open specification's snapshot is Markdown (`S226-spec.md`).
- Claude Code's snapshot is Markdown (`S227-claude.md`).
- pi's snapshot is Markdown (`S230-pi.md`).
- Vibe's snapshot is Markdown (`S231-vibe.md`).
- Factory's snapshot is the Markdown route `docs.factory.com/harness/skills.md` of the canonical page `docs.factory.com/harness/skills` (`S228-factory.md`); the assigned `docs.factory.ai/cli/configuration/skills` 308s there through `docs.factory.com/cli/configuration/skills`.
- A snapshot is the raw fetched bytes, and every quote above is read in a declared text view of it, not as a rendered page: for the `.html` snapshot script/style blocks are removed, tags become one space and entities are decoded; for Markdown snapshots every backtick byte is deleted and an unordered-list marker is removed; then whitespace is collapsed.
- Fenced code blocks are not removed, because two of the six pages document the field only inside a worked example (`S231-vibe.md:725-728`).
- **Line numbers drift.** Every citation is to the 2026-10-27 snapshot, not to a live URL: the page can change without the URL changing, which is why the recheck counts anchor tokens instead of trusting the address.
- **Pi's located quote is the source page's own table row.** Pi names the field exactly once, inside a markdown table row, so its located quote necessarily carries the page's `|` separators as text (6 words, 3 separators; the escape `\|` in the table above is Markdown escaping, and the quote text itself contains a literal bar) (`S230-pi.md`).
- The other five rows use pipe-free prose spans (specification 15 words, Claude Code 25, Factory 22, Microsoft Agent Framework 19, Vibe 6 — each with zero separators and one occurrence in its own shaped view).
- A reader that splits entry cells on `|` must treat pi's separators as page data.
- **Population and its margin.** Eighteen skill pages were fetched for the round-79 census and six state the field; a client silent in that census is a client that was not checked, not a client without the field.
- The negative sweep is not restated here: it is re-run in round 80 and belongs to that round's own rows.
- **The grant-semantics reading is documentary and per-page.** The labels in the surface table are the frozen vocabulary for this entry — `experimental`, `pre-approves`, `metadata-only`, `unstated` — and each is true of the page it names, read as that page's own words.
- They are not a ranking, and no label asserts what any client does at runtime.

## Scope

Per-client documentary semantics of one frontmatter key: the value form each page prints and the grant each page states, for six pages that state it.
Not claimed: a client's runtime behaviour with the field (none observed), a trust model for untrusted bodies (`corpus/knowledge/client-trust-gates-round68.md`), a conformance verdict on any vendor's parser, or a market census beyond the eighteen pages the round-79 census fetched.

## Related

- `corpus/knowledge/frontmatter-rule-authorities-round48.md` — the field's specification-format rule and the validator's allowed-key set; this entry takes the value form from the same specification page and adds the per-client grant.
- `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` — records `allowed-tools` as a CodeBuddy frontmatter key and compares spellings; this entry answers what the key grants, which that one leaves open.
- `corpus/knowledge/client-trust-gates-round68.md` — what a client does with a body it did not place; the Claude Code workspace-trust sentence is one negative for that map (this field is applied even in an untrusted folder, `S227-claude.md:619`).
