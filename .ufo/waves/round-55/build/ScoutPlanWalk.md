# ScoutPlanWalk — planning data-walk for C1's action cells (round 55, build wave)

Result: DONE — the existing literal-trigger proxy (round-6, prose-only, no committed script) reads opencode-side
`skill` *loads* and deliberately strips the slash invocation forms, so of the four explicit forms it counts slash
text and origin-less `skill` tool calls as implicit by default, leaves a `$` mention as a bare-name trigger, and
never sees omp reads; the seven SKILL.md action cells as landed at tip `9615579` carry the right instruction, with
two precision notes (match forms on the raw text before the round-6 cleaning; set aside per (turn, skill)) and one
live-store fact (the round-6 SQL no longer runs — the host store is opencode v2 schema).

Read-only walk. No lane file was edited; nothing was written except this report; no remote page was fetched by me
(the client pages are cited through the lane's landed rows, S065–S071); no lane code was executed, so no sandbox
clone was needed. Tip at start of walk `a10240c0` (the plan commit), tip while writing `9615579` (C1 content landed
mid-walk). `date -u`:

```
Thu 22 Oct 2026 11:24:44 PM UTC
```

Files read for this walk: `corpus/knowledge/trigger-miss-proxy-round6.md` (full), `skill-activation-telemetry.md`
(full), `frontmatter-trigger-surface.md` (full), `skill-overlap-levers-round51.md` (full),
`alwayson-checklist-round7.md` (full), `corpus/README.md` § Frontier/§ Known gaps, `SKILL.md` § tables,
`corpus/knowledge/explicit-invocation-round55.md`, `corpus/lessons/round-55.md`, `verifiers/check_explicit_invocation.py`
(header + HOSTS/TOKEN_RE), plus greps over the other 27 `grep -l -i 'activation|trigger'` knowledge entries
(`skill-listing-thresholds-round54.md`, `harness-router-models-round9.md`, `skill-selection-rules-round50.md`,
`alwayson-rule-files-round53.md` carry no explicit-invocation forms beyond what is cited below).

## 1. How the existing literal-trigger proxy decides a session invoked a skill

The proxy is the round-6 method, described only in prose (`corpus/knowledge/trigger-miss-proxy-round6.md`); no
committed verifier implements it (`grep -ln 'opencode.db' verifiers/*.py` → no output; SKILL.md keeps it as a
pointer at `SKILL.md:533-537`).

- **It decides *loaded*, never *invoked*.** Per-session skill loads are `part` rows where `$.tool='skill'`, skill
  name at `$.state.input.name` (`trigger-miss-proxy-round6.md:11-12`, recipe `:26-27`); a session counts as loaded
  iff it holds ≥1 such call (denominators 398 sessions with user text / 415 calls / 216 sessions with ≥1 load,
  `:6-7`). There is no field anywhere in the recipe that records *how* a skill came to load.
- **Intent text is joined, then cleaned.** `part(type='text')` joined `message_id → message(role='user')`, then:
  slash-command tokens stripped (the entry's own examples: `/skill:godspeed`, `/ufo` — "these are invocation
  verbs, not router intent") and injected directive blobs removed (`:13-18`).
- **The verdict is a token test on the cleaned text.** Literal-trigger session = intent text contains a trigger
  token for skill X; miss = trigger present, X never loaded (`:19-20`). The match is containment, not token
  equality — `xask` counted as present when it appeared inside a longer delegated phrase (`:56-57`).
- **Scope and granularity limits, as recorded.** Implicit-intent fidelity is unmeasured because a prompt carrying
  no literal token is invisible (`:71-73`); the unit is the session, not the prompt (`:74-76`); the store is the
  opencode side only — omp sessions are explicitly out of scope (`:77-79`), and round 6 already observed that
  where godspeed loaded, "opencode.db often shows a slash-command or directive-driven route" (`:58-64`).

An implicit (description-routed) measure built on this recipe is therefore the complement of the token test —
which is exactly the Frontier row's problem: `corpus/README.md:95` ("the literal-trigger proxy covers only prompts
that name a skill"; next probe: "the intent-labeling pass on the proven join recipe"), restated in
`corpus/README.md:142-144` and `corpus/knowledge/explicit-invocation-round55.md:14-16`.

## 2. The four explicit forms under this proxy

The question "would it currently count as implicit" has no stored answer in the recipe (there is no implicit
bucket yet). The table below is the disposition a measurer gets if the round-6 recipe is used verbatim and its
complement is called "implicit".

| Form | Where it appears (evidence) | What the round-6 recipe does with it | Counted implicit by default? |
|---|---|---|---|
| Slash command text (`/skill:godspeed`, `/ufo`, `/name`) | omp user messages carry it verbatim — random 8-file sample of the 1017 `~/.omp/agent/sessions/*/*/*.jsonl` files all opened with `Complete assignment thoroughly:\n\n/skill:godspeed\n\n…` in the first user message; fleet dispatches quote the injected leading line too | **Stripped by the cleaning step** — the form is one of the entry's own strip examples (`trigger-miss-proxy-round6.md:14-16`) | **Yes** — the marker is erased, so a slash-invoked turn has no token and falls into the "implicit" complement. Round 6 recorded slash-command-driven loads inside the loaded population (`:58-62`) |
| `$` mention (Codex `$skill`) | Client form is documented (`skill-overlap-levers-round51.md:26`, quote "explicit `$skill` invocation still works"); not present in the host store (Codex is not this host's harness; 0 of the 40 user rows' text contains `$`) | **Not stripped** — the cleaning names only slash tokens and one directive blob (`:14-18`); the token contains the skill name, and containment counts (`:19-20`, `:56-57`). [INFERENCE] because the entry records no `$`-handling at all | **No** — it survives as a bare-name trigger: counted on the *named* side, indistinguishable from a mere mention of the name |
| `skill` tool call (opencode) | The load signal itself (`:11-12`); `opencode.log` signal `message=evaluated permission=skill pattern=<name>` (`skill-activation-telemetry.md:65`); live v2 shape: assistant `content[]` part `{"type":"tool","name":"skill",…,"state":{…"input":{"id":"godspeed"}}}` | **Read as the load, with no origin field** — a call produced by a typed form and a call the model chose are the same row | **Yes, by elimination** — with the text cleaned, a call carrying no token is attributable to description routing; nothing in the row distinguishes a user-driven call |
| omp skill reads (`read` tool call, `arguments.path = skill://<name>`) | Live toolCall shape: `{"type":"toolCall",…,"name":"read","arguments":{"path":"skill://reverse-engineer-anything",…}}`; lane record: `tool_execution_start`/`toolCall` args `skill://X`, 5609 files / 5137 with ≥1 ref (`skill-activation-telemetry.md:66`) | **Outside the proxy entirely** — it reads the opencode store only (`trigger-miss-proxy-round6.md:77-79`) | **Not counted at all today.** If the join is extended with the same cleaning, the marker `/skill:` is the strip example (`:15`) and the read would be counted implicit by default |

Note on the omp side of the slash row: the load is the `read` call; the marker is the `/skill:<name>` line in the
user text. Verified on the live omp tree:

```
$ grep -o '.\{0,90\}/skill:[a-zA-Z_-]*.\{0,60\}' ~/.omp/agent/sessions/-Documents-nvhelpme/2026-10-20T11-58-22-930Z_01a1592d-4ad2-7534-9bfa-fb5712ae925d/BiosPrep.jsonl | head -2
…],"task":"Complete assignment thoroughly:\n\n/skill:godspeed\n\n# Target\nDownload directory only: …"
sage":{"role":"user","content":[{"type":"text","text":"Complete assignment thoroughly:\n\n/skill:godspeed\n\n# Target …
```

```
$ timeout 150 python3 … # bounded scan of 400 omp session files for toolCall windows containing skill://
-tmp/2026-10-22T18-22-33-748Z_01a164d9-… :: …{"type":"toolCall","id":"call_00_4ch0gd9p31gc5hunzrvxy6rs","name":"read","arguments":{"path":"skill://reverse-engineer-anything","i":"Reading RE skill instructions"}…
files scanned: 400 hits: 6
```

A trap for the future measure: a bare `skill://` grep is not a load signal — the tool documentation text in every
omp system prompt contains the literal `skill://<name>`, so all 1017 files match it. Counts over the 1017 files
(`grep -rl -m1 … | wc -l`): `"type":"toolCall"` 997; toolCall with `"arguments":{"path":"skill://` **259**. The
`skill://` count in `skill-activation-telemetry.md:66` (5137 of 5609) should be re-derived with a toolCall-anchored
filter before the labeling pass leans on it.

## 3. One action sentence per client (the C1 action cells)

The table landed at tip `9615579` (`SKILL.md:193-205`); the seven sentences below are the recommendation this walk
supports, each grounded in the landed entry rows (`corpus/knowledge/explicit-invocation-round55.md:20-28`), with
the raw-text clause from § 4 note A folded in:

1. **Claude Code** — "Set the turn aside as explicit when the raw user text starts with the skill's `/name` (the
   round-6 cleaning strips slash tokens, so match before cleaning); only turns without the form can test
   description routing." (form row `:22`; docs sentence quoted there)
2. **Codex** — "Set the turn aside as explicit when the raw user text holds `$` plus an installed skill's name;
   the remainder are the turns a description-routed measure may use." (row `:23`)
3. **VS Code** — "Set the turn aside as explicit when the raw user text starts with the skill's `/name`, even when
   task text follows the command." (row `:24`; the docs example shows trailing context)
4. **Copilot CLI** — "Set the turn aside as explicit when the raw prompt holds `/` plus a skill name; without that
   form Copilot picks from the prompt and each description." (row `:25`; the docs example is mid-sentence)
5. **Gemini CLI** — "Treat the `activate_skill` call as the activation record, not as explicit intent: count it
   only when the user's own text did not name the skill." (row `:26`; tool call, not a user-typed form)
6. **Cursor** — "Set the turn aside as explicit when the message used the skill's `/name`; with
   `disable-model-invocation: true` such a skill can only appear in these turns." (row `:27`)
7. **opencode** — "Set the turn aside as explicit when the raw prompt holds `@` plus a skill ID (on this host the
   user row's attached `skills[]` array records the same act); the model's own `skill` tool calls are what remain
   for the implicit measure." (row `:28`; store evidence in § 4)

Comparison with the landed cells (`SKILL.md:199-205`): all seven carry the same instruction; the landed cells omit
the raw-text clause (note A) and the opencode `skills[]` signal (note C). The landed Gemini CLI cell already makes
the inverted disposition explicit, matching sentence 5.

## 4. Live data-walk observations (receipts)

**Note A — the ordering defect (routed observation, not a counter change).** The recipe's cleaning strips exactly
the slash forms the new table tells the measurer to match (`trigger-miss-proxy-round6.md:14-16`); neither the
entry (`explicit-invocation-round55.md:14-16`, `:20-28`) nor the table intro (`SKILL.md:195`) says the form match
must run on the **raw** turn text before that cleaning. Without the clause, a measurer who reuses the recipe
verbatim deletes the `/name` evidence first. One clause in the table intro or the entry reading covers all
`/`-form rows.

**Note B — "the turn" vs the (turn, skill) pair.** In session `ses_ed42d6c31ffejc2Q8Hp3GMCzn7` the user row at
seq 629 carries `@tower` and an attached `skills[]` entry for `tower`; the assistant row at seq 630 (same turn)
calls the `skill` tool for **`shokunin`** — a model-chosen load. An explicit attach of one skill does not make
every load in that turn explicit; the precise set-aside is the named skill's activation. The README row and the
SKILL.md intro say "turns" (`corpus/README.md:95`, `SKILL.md:195`); the reviewer can decide whether the wording
needs the (turn, skill) qualifier.

**Note C — the store moved; the recipe's SQL no longer runs.** The live store is opencode v2 schema:

```
$ sqlite3 -readonly ~/.local/share/opencode/opencode.db "select p.session_id from part p;"
Parse error in 3rd command line argument: no such table: part        (rc=1)
$ sqlite3 -readonly ~/.local/share/opencode/opencode.db ".tables"
… session_message, session_v2, permission, instruction_entry, event, …   (no part/message tables)
```

Measured on that file (read 2026-10-22T23:2xZ): 21 sessions, 285 rows, 40 user rows; row window
`2026-10-11 16:18:22 .. 19:32:20`; the round-6-era 398-session data is not in this file. Current log is opencode
`version=2.0.26` and carries **0** `permission=skill` lines and 0 `/skill:` lines (616 "skill" lines are watcher
and discovery lines). The signals a measurer can actually use on this store:

- **Model-side loads**: 13 `skill` tool calls across 7 sessions (assistant `content[]` part `"name":"skill"`,
  id at `state.input.id`): opencode 7, godspeed 2, shokunin 2, tower 1, ufo 1.
- **User-side explicit attach**: 4 user rows carry `skills[]` — ids `opencode|OpenCode` ×2, `tower|tower`,
  `godspeed|godspeed`; the typed mention stays in the text (`@opencode`, `@tower`, `@godspeed`) and the array
  carries the skill's own text (`<skill_content name="tower">…`). This is the `@skill-id` form of
  `explicit-invocation-round55.md:28` observed on the lane's own host, one day before the round.
- The exact `/skill:` token appears in a user row only inside attached skill content, not typed:
  `select instr(json_extract(data,'$.text'),'/skill:'), instr(json_extract(data,'$.skills[0].text'),'/skill:')`
  → `0|3064` for the `tower` row.

**Note D — omp counts are bounded.** `find ~/.omp/agent/sessions -name '*.jsonl' | wc -l` → 6510; the glob
`sessions/*/*/*.jsonl` covers 1017 of them. All omp statements above are bounded to those 1017 files; the deeper
files were not counted.

## 5. What this walk did not check / limits

- No client page was refetched; every client-form statement here is a citation through the lane's landed rows
  (S065–S071 in `corpus/lessons/round-55.md:12-21`, quotes in `explicit-invocation-round55.md:20-28`), not my own
  fetch.
- The `$`-survives-cleaning statement is [INFERENCE]: the round-6 entry records slash tokens and one directive
  blob only.
- opencode-store counts are one small file (21 sessions); omp counts are one bounded glob; neither is a fleet
  measure.
- The counter's current v2 token rule (`verifiers/check_explicit_invocation.py:81,145`: a user-typed `/ $ @`
  segment) was read, not run; whether each landed cell satisfies it is the C1 mutator/counter seats' work, not
  this walk's.
- Nothing here changes any counter, table or predicate; Notes A–C are routed observations for the L1. If Note A's
  clause is taken, it is craft text in `SKILL.md`/the entry, not a judging line of the counter.