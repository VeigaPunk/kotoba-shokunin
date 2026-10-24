# Is there an opencode-side skill-offer trace? — round 8 verdict

Sourced 2026-09-28 (round 8), scout lane `OpencodeOfferTrace`. All probes read-only
(`sqlite3 -readonly`, `find`, `grep`, `strings`, `curl`); nothing outside
`kotoba-shokunin` was written. Host: this workstation, opencode
`~/.opencode/bin/opencode` (ELF, 185030784 B, mtime 2026-09-14, BuildID
`c30f169b1bef81fa57467cd091ba53aab5235468`); db session versions
1.18.23 / 1.18.25 / 1.18.31.

## Verdict

**There is no per-session *record* of what opencode offered, but the offer is
*measurable* two ways short of a record** — a per-run rediscovery count in the
log, plus a deterministic reconstruction of the offered name set from the
global skill roots. Both agree.

- **No verbatim offer persists anywhere.** opencode builds the skill catalogue
  inside the system prompt at request time and hands it straight to the LLM;
  it is never written to the db, the log, or any state file.
- **Trace A (stored, offer-side):** `~/.local/share/opencode/log/opencode.log`
  logs `message=init count=N` once per instance, emitted by the skill-discovery
  module after loading — it is the size of the loaded skill registry.
- **Trace B (reconstructible):** the offered *names* = union of `SKILL.md`
  files under the global roots (`~/.claude/skills/**`, `~/.agents/skills/**`,
  `~/.config/opencode/{skill,skills}/**`) + the builtin `customize-opencode`.
  Reconstruction matches every observed `count` value (17 on disk + 1 builtin = 18
  today = the last logged count).

**godspeed offer count on opencode: 387/387 attested sessions (100%); 399/399 by
reconstruction.** Activation: **205/399 sessions = 51.4%** (239 calls) — i.e. the
round-6 "51.5% godspeed coverage" is a model-choice gap on opencode, exactly as
round 7 found for omp (there it was 3911/3911 offered).

## Correction to the round-6/7 marker assumption

The round-6 probe searched for the literal `<skills>`. That is the **omp**
catalogue tag. **opencode's catalogue tag is `<available_skills>`** — verbose
render (upstream `skill/index.ts` `fmt(list,{verbose:true})`, lines 321–338):

```
<available_skills>
  <skill>
    <name>godspeed</name>
    <description>…</description>
    <location>/home/vgpnk/.agents/skills/godspeed/SKILL.md</location>
  </skill>
  …
</available_skills>
```

A `<skills>` grep on opencode can therefore never hit, and an
`<available_skills>` grep hits only incidental copies (below). Also note the
non-verbose render is `## Available Skills` + `- **name**: description`
(upstream `fmt` non-verbose branch; also used by the TUI).

## Searched surface — what exists and what it contains

| Surface | Size | Offer content |
|---|---|---|
| `~/.local/share/opencode/opencode.db` | 1.98 GB | **none** (only activation) |
| ├ `message` (3623 rows) | | `data` JSON keys = `time,role,agent,tokens,providerID,path,parentID,modelID,mode,cost,finish,variant,model,summary,error` — **no `system` key on any row** |
| ├ `part` (22126 rows) | | types `tool 9980 / reasoning 4575 / step-start 2967 / step-finish 2908 / text 1456 / patch 201 / compaction 34 / file 5` — no system/prompt part |
| ├ `event` (90037 rows) | | types `message.part.updated.1 72550 / message.updated.1 12780 / session.updated.1 4308 / session.created.1 399` — pure mirror of message/part |
| ├ `session` (399) | | `metadata` all NULL; `permission` never mentions `skill` (0 rows) |
| ├ `session_context_epoch` | **0 rows** | schema exists (`baseline`,`snapshot`,`baseline_seq`) but never populated |
| ├ `session_input` | **0 rows** | prompt-delivery queue, unused |
| ├ `session_message` | **0 rows** | unused |
| ├ `control_account` / `account` / `credential` / `permission` / `workspace` / `account_state` | 0 rows | empty |
| ├ `event_sequence` (399) / `todo` (28) / `project` (3) / `project_directory` (2) / `migration` (38) / `data_migration` (0) | | no prompt data |
| `~/.local/share/opencode/log/opencode.log` | 9.49 MB, one file, no rotations | **Trace A only**: 1918 `duplicate skill name` warns, 471 `evaluated permission=skill`, 190 `init count=` lines. `grep -c`: `<available_skills>` **0**, `Skills provide specialized` **0**; the 2 `system prompt` hits are permission lines quoting an agent's own grep/bash patterns (lines 5284, 6625) |
| `~/.local/share/opencode/tool-output/` | 15 files, 25 MB | no skill markers |
| `~/.local/share/opencode/snapshot/` (2 hashes), `repos/` (empty) | | git object store for file snapshots — no prompts |
| `~/.local/share/opencode/auth.json` | | credentials only |
| `~/.local/state/opencode/` | 68 KB | `prompt-history.jsonl` (50 user inputs, **0** skill markers), `kv.json` (TUI prefs), `model.json` (recents/favorites), `session.json` (pinned), `locks/` — no offer data |
| `~/.config/opencode/` | | config/agents/plugin/skills symlinks — inputs to discovery, not session state |
| `~/.cache/opencode/bin` | empty | — |

### False positives found (and why they are not the catalogue)

- `instr(data,'<skills>')>0` → `part` **6**, `event` **6**, `message` 0. All six
  parts are `tool` parts whose *output* quotes omp/kimi transcripts under
  `/tmp/ufo-omp-r03/…jsonl` that themselves contain omp's `<skills>` block.
- `instr(data,'available_skills')>0` → `part` **8**, `event` **16**. Four `read`
  parts of `/home/vgpnk/.kimi-code/config.toml` (`merge_all_available_skills = true`),
  three `bash` parts inspecting kimi config, one `reasoning` part where the model
  writes the phrase while planning. None is an injected opencode catalogue.
- `instr(data,'Available Skills')>0` → `part` **1**: a `grep` tool output over
  `~/.grok/**`.
- `Skills provide specialized` / `skill tool to load` / `skill-guidance` →
  **0 hits** in `message`, `part`, `event` (and 0 in every log/state file).

## Commands / queries used (reproducible)

```bash
sqlite3 -readonly ~/.local/share/opencode/opencode.db ".tables"
for t in account account_state control_account credential data_migration event \
         event_sequence migration part permission project project_directory \
         session session_context_epoch session_input session_message \
         session_share todo workspace message; do \
  printf "%s=" $t; sqlite3 -readonly ~/.local/share/opencode/opencode.db "select count(*) from $t;"; done

# system-prompt key enumeration (decisive: no `system` key anywhere)
sqlite3 -readonly ~/.local/share/opencode/opencode.db \
 "select json_each.key, count(*) from message, json_each(message.data) group by 1 order by 2 desc;"
sqlite3 -readonly ~/.local/share/opencode/opencode.db \
 "select json_extract(data,'\$.type') t, count(*) from part group by 1 order by 2 desc;"
sqlite3 -readonly ~/.local/share/opencode/opencode.db \
 "select type,count(*) from event group by type order by 2 desc;"

# marker scans (see table above)
sqlite3 -readonly ~/.local/share/opencode/opencode.db \
 "select count(*) from part where instr(data,'<skills>')>0;"
sqlite3 -readonly ~/.local/share/opencode/opencode.db \
 "select count(*) from part where instr(data,'available_skills')>0;"
sqlite3 -readonly ~/.local/share/opencode/opencode.db \
 "select count(*) from message where instr(data,'Skills provide specialized')>0;"

# activation census
sqlite3 -readonly ~/.local/share/opencode/opencode.db \
 "select json_extract(data,'\$.state.input.name') n, count(*) c, count(distinct session_id) s \
  from part where json_extract(data,'\$.tool')='skill' group by 1 order by 2 desc;"

# log / state scans
grep -c '<skills>' ~/.local/share/opencode/log/opencode.log          # 0
grep -o 'message="[^"]*"' ~/.local/share/opencode/log/opencode.log | sort | uniq -c | sort -rn
grep -o 'message=init count=[0-9]*' ~/.local/share/opencode/log/opencode.log | sort | uniq -c
ls -laR ~/.local/state/opencode ~/.local/share/opencode/{log,tool-output,snapshot,repos}

# binary static analysis (offer mechanism, v1 + v2 code paths)
strings -n 6 ~/.opencode/bin/opencode > /tmp/ocstr.txt       # 432418 lines
grep -n '<available_skills>\|SystemPrompt.skills\|@opencode/v2/SkillGuidance\|session_context_epoch' /tmp/ocstr.txt
```

## Mechanism — where the offer lives, and why it evaporates

Local binary (strings line numbers in the extraction above):

- `SystemPrompt.skills` (line 243714): if the `skill` permission is disabled for
  the agent, return nothing; else
  `["Skills provide specialized instructions and workflows for specific tasks.",
   "Use the skill tool to load a skill when a task matches its description.",
   Bl.fmt(available, {verbose:!0})].join("\n")`.
- The skill tool's own description is **static text** (line ~244155):
  `"Load a specialized skill when the task at hand matches one of the skills
  listed in the system prompt. … The skill name must match one of the skills
  listed in your system prompt."` — so the catalogue exists **only** in the
  system prompt, not in the tool schema the db stores.
- The db stores only `part.state.input.name` for a `skill` call (the activation),
  never the offer.
- v2 code is present but the epoch table is dead here: `@opencode/v2/SkillGuidance`
  (line 245219) would materialise a keyed block `core/skill-guidance`
  (JSON array of `{name,description}`, baseline/update/removed renderers), and
  `session_context_epoch` (`baseline`,`snapshot`,`baseline_seq`) exists in the
  schema — but `session_context_epoch` appears **only in migration code**
  (`20260605003541_add_session_context_snapshot`, `…reset_v2_session_state`
  DELETE, `20260622142730_simplify_session_context_epoch` DROP COLUMN) and holds
  **0 rows**. Traces of a v2 path that *would* have persisted a skill-guidance
  snapshot.

Upstream corroboration (`github.com/sst/opencode@dev`, read 2026-09-28):

- `packages/opencode/src/session/prompt.ts` ~1260–1279: `const system = [...env,
  ...instructions, ...(mcpInstructions?[mcpInstructions]:[]), ...(skills?[skills]:[])]`
  passed straight into `handle.process({system, …})`. Nothing written to a message row.
- `packages/opencode/src/session/system.ts` 107–119: `SystemPrompt.skills` is
  exactly the local implementation; `Skill.fmt(list,{verbose:true})` is the
  `<available_skills>` block.
- `packages/opencode/src/skill/index.ts`: roots are
  `CLAUDE_EXTERNAL_DIR=".claude"`, `AGENTS_EXTERNAL_DIR=".agents"`,
  `EXTERNAL_SKILL_PATTERN="skills/**/SKILL.md"`, `OPENCODE_SKILL_PATTERN="{skill,skills}/**/SKILL.md"`;
  external dirs are auto-scanned unless `disableExternalSkills` /
  `disableClaudeCodeSkills` (lines 185–203). `fmt` drops every skill whose
  `description === undefined` before rendering — **description is the offer gate**.
- This host's dup warnings confirm the doc table inside the binary: existing
  `/home/vgpnk/.claude/skills/<name>/SKILL.md`, duplicate
  `/home/vgpnk/.agents/skills/<name>/SKILL.md` and
  `/home/vgpnk/.config/opencode/skills/<name>/SKILL.md`; dedupe is by `name`,
  first-scanned copy wins.

Craft contrast for this project's domain: **opencode's offer is untruncated** —
the model receives the full frontmatter `description` byte-for-byte plus the
absolute `location`, with no 99-char cliff and no LLM render cache (cf.
`render-mechanism-round7.md`). The only ways a skill fails to be offered on
opencode are: no `description`; permission denial of the `skill` tool; invalid
frontmatter / name≠folder; or being the losing duplicate of a same-named skill.

## Trace A — `message=init count=N` (offer-side, stored)

Emitted by the discovery module right after loading each match into the registry
(binary line 242788 region:
`…yield*A.logInfo("init",{count:Object.keys(j.skills).length})` inside
`@opencode/Skill`). One line per instance, immediately after that instance's
`duplicate skill name` warn block.

Observed series over the whole log (2026-08-28 15:51 → 2026-09-28 19:44):

| value | lines | first seen |
|---|---|---|
| 15 | 1 | 2026-08-28T15:51:52 |
| 16 | 141 | 2026-08-28T21:11:57 |
| 17 | 34 | 2026-08-29T23:08:57 |
| 18 | 14 | 2026-09-17T00:14:06 |

Monotone, never decreasing → **no run in the window ever started with fewer than
15 skills, and godspeed (present on disk since 2026-08-21 20:19:37) is in every
one of those sets.** Coverage: 187/219 runs produced an `init count` line;
191 runs created an instance (4 instances produced no count). 387/399 db
sessions carry at least one `init count ≥ 16` attestation from a run that
mentions their id; the 12 unattested sessions are all root sessions with no log
trail at all.

**Semantics validated, not assumed:** the current on-disk set below reconstructs
to 17 unique names; plus the builtin `customize-opencode` = **18**, which is
exactly the last logged value. The 15/16/17 values are consistent with the same
union at earlier dates (only additions: `xbrd-ask` becoming valid, `ufo`,
`kimi-webbridge`; every transition is +1 and later in time than the mtime that
explains it — `kimi-webbridge` created 2026-09-12, first count=18 at the next
run 2026-09-17). [INFERENCE: exact attribution of the 16→17 step.]

## Trace B — reconstruction recipe (offered name set)

```bash
cd ~
{ find -L .claude/skills -maxdepth 2 -name SKILL.md -print
  find -L .agents/skills -maxdepth 2 -name SKILL.md -print
  find -L .config/opencode/skills .config/opencode/skill -maxdepth 2 -name SKILL.md -print
} | while read f; do [ -e "$f" ] && echo "$(basename $(dirname "$f"))|$f"; done | sort -u
# + builtin skill "customize-opencode" (ships in the binary, counted by init)
```

`-L` is required (the bailian skills are symlinked dirs); `[ -e ]` drops the
dangling `~/.agents/skills/{sekhmet,xbrd}` symlinks (0 contributions, matching
round 7). Today: 17 unique names —
`bailian-cli, bailian-docs-llm-wiki, bailian-finetune, bailian-gen,
bailian-managed-agent, bailian-model-recommend, bailian-protocol,
bailian-sandbox, bailian-train-deploy, bailian-web-search, godspeed,
kimi-webbridge, omarchy, sekhmet-l3, ufo, wwkd, xbrd-ask` (+ builtin
`customize-opencode`). For a historical session, evaluate the same union against
each `SKILL.md` mtime and cross-check the reconstructed size against that run's
`init count` in the log.

## Numbers

Offer (opencode side):

- godspeed: **387/387 attested db sessions (100%)**, `init count ≥ 16` in every
  run, godspeed never a duplicate loser, its only root copy
  `~/.agents/skills/godspeed/SKILL.md` (694 B, mtime 2026-08-21 20:19:37 −0300)
  predates the earliest session (2026-08-28 21:09:09Z). Reconstruction: 399/399.
- Offered-set size per run: 16 → 17 → 18 (never 0, never a drop).

Activation (opencode side, `part` rows with `$.tool='skill'`):

- 415 calls over 216 sessions (round-6 figure reproduced exactly).
- godspeed 239 calls / 205 sessions = **51.4%** of 399 sessions
  (53.0% of the 387 attested sessions). wwkd 52/51, ufo 51/47,
  customize-opencode 27/27, bailian-protocol 15/15, bailian-cli 13/13,
  xbrd-ask 8/8, sekhmet-l3 4/4, omarchy 4/4, xbgst-surface 1/1,
  bailian-docs-llm-wiki 1/1.
- Per-agent (sessions / sessions with a godspeed call): raw 124/27, ufo 38/10,
  scout 31/20, planner 26/20, reviewer 25/19, labrat 24/14, executor 22/15,
  connector 21/17, sentinel 19/18, critic 16/11, distiller 13/4, revenger 12/11,
  simplifier 9/8, mutation-tester 8/4, orch 4/2, scribe 3/3, build 3/2, janitor 1/0.
- Supplementary activation trace: the log's per-call permission line
  `evaluated permission=skill pattern=<name>` (471 total; godspeed 277) is
  run-scoped and timestamped. It does not reduce to the 415 parts cleanly
  (run↔session is many-to-many; 61 log sessions are absent from the db), so it is
  a corroborating, not a canonical, activation count.

## What would be needed for a verbatim offer trace

Nothing on this host can answer "which names/descriptions did session X see?"
directly. To make it a stored fact, one of:

1. **Persist the resolved system prompt** (or at least the `SystemPrompt.skills`
   string) on the user/assistant message row, or as a `part` of a new type —
   currently `system` is assembled inline in `prompt.ts` and discarded.
2. **Turn on the v2 `SkillGuidance` epoch path** so `session_context_epoch`
   (`baseline`/`snapshot`) is populated with `core/skill-guidance` — the code and
   the table both exist; this build only ship-create-and-wipe migrations
   (`…reset_v2_session_state`), so the table is empty.
3. **Log the discovered names, not just the count** — the discovery module
   already logs `init {count}`; `count` → `names` is a one-line change, and it
   would be run-scoped, which the db is not.
4. Per-request LLM request dumping (`logLevel: DEBUG` is configured-able via
   `opencode.json` `logLevel`) — **not verified to emit prompt bodies on this
   build**; the current log contains no request payload lines (only
   `message=stream`/`llm runtime selected` metadata). [INFERENCE]

## Unknowns

- Set attribution: the exact content of the 16-name and 17-name sets (only
  the 15/18 endpoints were enumerated exactly); affects nothing in the verdict —
  godspeed is in all four by construction.
- Whether the Aug-28-era binary (1.18.23, since overwritten) rendered the offer
  identically: the `SystemPrompt.skills` code path, the roots, and the
  `init count` line all exist in the deployed binary and the dup-warning +
  permission-eval logs from 2026-08-28 match today's format. [INFERENCE]
- 38 godspeed permission evals (277 log vs 239 parts) are unattributed; likely
  sessions pruned from the db / run-session attribution skew, not double-logging
  (run `8ccab1cf`: 43 evals vs 43 parts; `522c7973`: 35 vs 36).