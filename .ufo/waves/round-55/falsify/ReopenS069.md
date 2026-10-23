Result: HOLDS — S069 (Gemini CLI) re-opened byte-identical; lesson Gate quote is byte-exact at the stated lines, and the teaches, knowledge reading, and SKILL.md cells each say no more than the fetched pages.

# Scope

SOURCES row S069 (`corpus/SOURCES.md:82`) and its uses: the Gate quote in
`corpus/lessons/round-55.md:18`, the Per-client record row in
`corpus/knowledge/explicit-invocation-round55.md:26`, and the
`### Explicit invocation by client` row in `SKILL.md:203`. Tip under test:
f0e6b695b746775823b65a8c45de7d50ea33e84f. Read-only on the lane; fetched bytes
kept under `/fast/scratch/hyaku/kotoba-r55/ReopenS069/`.

# Re-open receipt

URL: `https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/skills-getting-started.md`

- `date -u` before: `Fri 23 Oct 2026 12:10:06 AM UTC`; after: `12:10:06 AM UTC`.
- curl: `HTTP 200 | 5855 bytes`; `wc -c` = 5855.
- sha256: `111e8bfa1b99c2d2e2728864d092728334f73eb4fc9ce2998f6cf6ba3ca1c167`.
- Matches the row's recorded receipt (`fetched 2026-10-22T23:15:25Z, HTTP 200, 5,855 B, sha256 111e8bfa…`, `corpus/SOURCES.md:82`) byte-for-byte.

Supporting fetches (to bound the "pages read"/"no user-typed form" wording — see SKILL row check below):

- `https://geminicli.com/docs/cli/skills.md` (S029's page): opened 2026-10-23T00:13:27Z, HTTP 200, 5,763 B, sha256 `8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590` — identical size/hash to S029's recorded fetch (`corpus/SOURCES.md:42`).
- `https://geminicli.com/docs/cli/using-agent-skills.md` (linked from both pages; fetched 2026-10-23T00:14:38Z, HTTP 200, 3,052 B, sha256 `9e61fb7cb289263a102e937849f7019efc860e961da1dbcdf3ce36056e9df708`).

# Cell verdicts

## 1. Lesson Gate quote — HOLDS

Lesson row (`corpus/lessons/round-55.md:18`): `"description and calls the `activate_skill` tool."` at `skills-getting-started.md:127-129`.

- `grep -n 'description and calls the `activate_skill` tool' s069.md` → line 128, one hit: `    description and calls the `activate_skill` tool.` — byte-exact substring (leading 4-space indent precedes; the quote itself carries the page's backticks and terminal period, unstripped, consistent with the lesson's note that only S071's backticks are dropped, `corpus/lessons/round-55.md:22-24`).
- Line 128 lies inside the stated range 127–129: 127 is `2.  **Activation**: Gemini identifies that the request matches the `api-auditor``, 128 is the quote line, 129 is `3.  **Consent**: You will see a confirmation prompt. Type **y** to approve.`
- 6 whitespace-separated words — inside the 3–25 bound. The clause is a fragment of a numbered step, but the lesson discloses exactly that ("a clause from a numbered step"). No unstated normalisation.

## 2. SOURCES `teaches` cell — HOLDS

Cell (6th of 11, `corpus/SOURCES.md:82`): `Gemini CLI's documented path from a request to loading a named skill (the model-side tool call; no user-typed form found)` — 20 words ≤ 25.

- "documented path from a request to loading a named skill": page lines 123–132 give the full sequence — ask a question (trigger) → `activate_skill` tool call → consent → skill active ("How to use the skill", `s069.md:121-132`). "Loading … a named skill" is a fair paraphrase of "activate"/"activated" in a section whose purpose is using the skill.
- "the model-side tool call": page line 127–128 attributes the call to Gemini (the model), not the user — accurate.
- "no user-typed form found": bounded as found-in-page, not client-silence. Verified on the fetched bytes: the only `/`-prefixed tokens are `/skills list`, `/skills reload`, `/trust`, `gemini skills <verb>` — all discovery/management (`s069.md:88-101, 147-149`); the lone activation path is "trigger its activation by asking a relevant question" (123-124), a natural-language request, not a token naming the skill. No `@`-/`$`-/`#`-form and no "type the skill name" instruction anywhere in the file (grep for `(^| |"|()/$@#<letter>` and for `type|ask|invoke|trigger|activat`, output in report transcript).

## 3. Knowledge `reading` cell — HOLDS

`corpus/knowledge/explicit-invocation-round55.md:26`: `The model calls the tool after the request matches a skill description; the tutorial then asks the user to consent. It is not a user-typed form.`

- Each clause maps to the bytes: model calls the tool (127–128), consent ask (129). "It is not a user-typed form" is verified in §2 — nothing the page doesn't show.
- The row's quote cell is byte-identical to the lesson's, verified above; location cell matches.

## 4. SKILL.md `### Explicit invocation by client` row — HOLDS

`SKILL.md:203`: `| Gemini CLI | `activate_skill` (model tool call) | Loads the named skill after a description match, then asks the user to consent; the pages read document no user-typed form | Treat this call as the activation record, not as explicit intent: count it implicit unless the user's own text named the skill |`

- **Explicit form** — HOLDS: `` `activate_skill` `` is byte-exact on the page (128); "(model tool call)" matches "calls the `activate_skill` tool" with the caller being Gemini.
- **What it does** — HOLDS: "after a description match" ≡ "the request matches the `api-auditor` description" (127–128); "asks the user to consent" ≡ step 3 (129). "the pages read document no user-typed form" is scoped to pages read, not the client. This seat fetched all three Gemini skills pages the corpus records as read — S069's tutorial (no user-typed form; §2), S029's `skills.md` (activation is the model's `activate_skill` call, lines 23–24; every `/skills` subcommand is list/link/disable/enable/reload, lines 88–96; no invocation form), and the linked `using-agent-skills.md` (management only; "the agent must ask for permission to activate it", line 79). The plural is grounded; no page read documents a user-typed form.
- **Action** — HOLDS: a routing directive consistent with the page's own ordering (consent follows the tool call). "unless the user's own text named the skill" is a conditional, not a claim that the client documents such a form — it asserts nothing the page must support.

# Non-defects and residual notes

- Consistent-by-design exclusion: the frozen C1 counter self-test asserts `form_tokens("`activate_skill`")` → `[]` ("v2: tool name is not a user-typed token", `verifiers/check_explicit_invocation.py:493`), matching the lesson's erratum 1 (S069 is a model-side call, not counted as a user-typed form). The SKILL.md row still satisfies the counter's separate form-cell rule (identifier holding `_` passes TOKEN_RE, `:29`). Not a finding; noted so a falsifier doesn't re-raise it.
- Minor wording note (not a defect): the teaches cell's "loading" and the SKILL row's "Loads" paraphrase the page's "activate"/"activated"; the page does not literally say "load". The paraphrase is faithful to a tutorial section titled "How to use the skill".
- The `what-it-does` cell's plural "pages read" is satisfied by the three Gemini skills pages recorded or linked in the corpus; if a future round records a fourth Gemini page showing a typed form, this cell needs revisiting — [INFERENCE] none exists in the corpus today.

Verdict: S069 and all four claim-side cells HOLD.

Report: .ufo/waves/round-55/falsify/ReopenS069.md
