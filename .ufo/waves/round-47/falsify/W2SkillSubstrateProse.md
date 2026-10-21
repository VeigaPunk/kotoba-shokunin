verdict: PARTIAL — both round-47 SKILL.md edits (opencode bullet at :431, Portability floor at :151) survive; the sweep finds one round-47-induced falsehood in the same file (`10 checks` at :122, actually 11) plus stale omp 18.12.5 anchors/roots and opencode 1.19.3 recipes/populations that the file still states in the present tense.

# Substrate and method

- Tree: detached clone of `/home/vgpnk/Projects/shokunin/kotoba-shokunin` at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` in `/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2SkillSubstrateProse-2/kotoba-shokunin` (canonical sibling symlinks; `git status --porcelain` empty; `git rev-parse HEAD` = 7ad7fad…).
- Frozen bytes: `sha256sum -c SHA256SUMS` in `/fast/scratch/kotoba-r47/shared` → all four `OK`, exit 0. Live pins equal the frozen bytes (`check_substrate_pins.py` PASS 3/3).
- All omp/opencode claims below are static: the frozen `.strings` dumps and raw ELFs, plus raw `grep -a` on the ELF where a `strings` filter could hide a literal. The `~/.local/bin/opencode` wrapper was never executed (contract).
- Production files were not modified; this report is my only write.

# The two round-47 edits under attack

## 1. Portability floor, `SKILL.md:151` — HOLDS

> `verifiers/verify_skill_checklist.py` `trigger.no_xml_tag` gates the XML-tag rule on `name` and `description`; Anthropic's reference packager (S012) is stricter and refuses any `<`/`>`.

Evidence:

- The check exists and scans both parsed fields: `verifiers/verify_skill_checklist.py:1294-1313` (`present = [k for k in ("name", "description") ...]`; `XML_TAG_RE` or `YAML_ANGLE_ESCAPE_RE` over each). Live run: `python3 verifiers/verify_skill_checklist.py --json` → exit 0, `PASS trigger.no_xml_tag: evaluated 2 — no XML tag in name, description`.
- The parsed frontmatter really lost the tag: at `7ad7fad`, `SKILL.md:1-15` has zero `<skills>`; at BASE `c61a973b…` the folded description carried it at line 14 (`git show c61a973…:SKILL.md | sed -n '1,15p' | grep -n '<skills>'` → 1). The description parses to 814 chars, name `kotoba-shokunin` (15), so the ≤1024/≤64/quoted rules hold.
- S012 is exact: `curl` of `raw.githubusercontent.com/anthropics/skills/dbd4588f…/skills/skill-creator/scripts/quick_validate.py` → HTTP 200; lines 79-81 are `# Check for angle brackets` / `if '<' in description or '>' in description:` / `return False, "Description cannot contain angle brackets (< or >)"`. Same rule as `corpus/SOURCES.md:25`.
- One precision caveat, not a falsehood: S012's angle-bracket check is scoped to **description only** (its `name` block at lines 60-71 checks kebab-case and length, not brackets). The sentence's juxtaposition ("gates … on `name` and `description`; S012 is stricter") can be read as S012 policing both fields. It is stricter on description, silent on name — the verifier is the broader gate. No repair needed unless the sentence is meant as a field-by-field comparison.

## 2. opencode bullet, `SKILL.md:431-434` — HOLDS

> opencode — npm `opencode-ai` 1.19.3 since round 47 (the `~/.local/bin/opencode` npx wrapper; pinned ELF and lineage in `verifiers/baseline.json` and `corpus/knowledge/instruction-surface-census-round13.md` § B′; the round-8/18 `~/.opencode/bin` install is gone) …

Evidence:

- Wrapper is a bash script (`file` → "Bourne-Again shell script"), resolves `node` via `mise`, warms the cache with `npx --yes --prefer-online --package opencode-ai -- true`, then resolves via `npx --yes --package opencode-ai -- which opencode-ai` (fallback `which opencode`) and execs the resolved bin.
- Resolved package is 1.19.3: `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/package.json` → `"version": "1.19.3"`.
- Pinned ELF matches: `sha256sum …/opencode-ai/bin/opencode.exe` → `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`; `verifiers/baseline.json` `opencode_binary_sha256` is the same, and the `round47_note` records the channel move and `~/.opencode/bin` removal.
- `~/.opencode/bin` → `ENOENT`; `~/.local/bin/opencode` exists.
- `corpus/knowledge/instruction-surface-census-round13.md:212-219` § B′ names the same path + sha and the round-14 loader lineage; the loader anchors are measured on that dump.
- Caveat [INFERENCE], not a false claim: the wrapper passes `--prefer-online`, so the pinned ELF is the bytes cached at round 47, not a constraint on what the wrapper may fetch on a later run. The default pin path in `verifiers/check_substrate_pins.py:66` is the npx ELF; the pin is a snapshot pin, which the script's own doc (`:43`) acknowledges ("the wrapper itself is never the [pin]").

# Sweep findings

## F1 — round-47 regression: `SKILL.md:122` says "10 checks"; the gate runs 11

`SKILL.md:121-126`:

> `python3 verifiers/verify_skill_checklist.py` executes this file's own checklist: **10 checks** (`checklist.box_map_complete` + the eight boxes marked `(executed: …)` below + `governance.citation_resolves` over the two root governance files) …

Repro:

```
$ python3 verifiers/verify_skill_checklist.py --json | jq '.exit_code, (.checks|length)'
0
11
$ python3 verifiers/verify_skill_checklist.py --json | jq -r '.checks[].id'
checklist.box_map_complete
trigger.frontmatter_parses
trigger.name_directory
trigger.literal_trigger_string
trigger.anti_trigger_clause
trigger.no_xml_tag
trigger.line_budget
trigger.no_placeholder
trigger.command_binary_resolves
trigger.citation_resolves
governance.citation_resolves
```

The sentence's own arithmetic is 1 + 8 + 1 = 10; `trigger.no_xml_tag` is the 11th and is not enumerated. `verifiers/checklist-baseline.json` still holds 8 `executed:` boxes (no box is bound to `trigger.no_xml_tag`), so `checklist.box_map_complete` passes on its documented rule ("every `executed:<id>` must name a check"; it does not require every check to be box-bound — `verify_skill_checklist.py:50-66`). The box count sentence at `:126` ("all 41 boxes (8 executed, 0 delegated, 33 unexecuted)") is still true.

This is the C2 edit landing without its prose update: the C3 claim's "11/11" (and the live run) is right, the file says 10. Repair: `**11 checks** (… + `trigger.no_xml_tag` …)`, and decide whether the new gate deserves a checklist box (it currently has none, while the Portability floor presents it as this file's gate).

## F2 — omp truncator/key anchors `_8n`, `A8n`, `K7s` are gone from 18.12.5

Cited at `SKILL.md:26`, `:91`, `:451-452`, `:456`. The mechanism and every number survive; the identifiers do not.

Repro (raw ELF, not the filtered dump):

```
$ grep -ac 'A8n=' /fast/scratch/kotoba-r47/shared/bin/omp-18.12.5   # 0
$ grep -ac 'K7s=' …                                                # 0
$ grep -ac '_8n=' …                                                # 0
$ grep -ac 'var v = 100' …                                         # 2
```

The 18.12.5 source chunk (`// packages/coding-agent/src/extensibility/skill-descriptions.ts`) reads:

```
var v = 100;
var x = 160;
var P = 12;
function xze(e) {
  const t = e.replace(/\s+/g, " ").trim();
  if (t.length <= v) return t;
  const r = t.slice(0, v - 1);
  const n = r.match(/^.*?[.!?](?=\s|$)/)?.[0];
  if (n && n.length >= 40) return n;
  const o = r.slice(0, r.lastIndexOf(" ")).trimEnd();
  return `${o || r}\u2026`;
function D(e) {
  return new Bun.CryptoHasher("sha256").update(w).update("\x00").update(e.name).update("\x00").update(e.description).digest("hex");
```

So: `_8n` → `v`, `A8n` → `D`, `K7s` → `w`. The 3 `_8n`, 3 `A8n`, 7 `K7s` hits in the dump are substrings inside unrelated minified/binary fragments (e.g. `…3qA8nVCZ6…`, `_8n]nF`), not identifiers. Everything the prose claims about behavior still checks: `v = 100` (99-char cut), first-sentence `^.*?[.!?](?=\s|$)` kept if ≥40, last-space + `…`, validator `x = 160` chars / `P = 12` words; the 273-byte template sha256 `c1f03c8e248eb40e…` is verified PASS by `verify_harness_claims.py` (`omp.elf.template_sha256`, `omp.elf.template_bytes` 273/273). Exported names `previewSkillDescription` and `createSkillDescriptionCompressor` are present, so the anchor *list's* headings hold; the inline code identifiers are one build behind.

Impact: this file's own rule (`SKILL.md:51-53`: "Cited line numbers are points-in-time. Verify before trusting: if a cited line has drifted, re-read the file and update the citation"; `:448`: "cite anchors, not offsets") is violated by the fragment it cites as the 18.12.5 mechanism. A reader grepping `_8n` in 18.12.5 gets only unrelated blob hits.

## F3 — `~/.omp/agent/skills` is not an omp discovery root (`SKILL.md:91`)

The router-model table says: "Ship the dir under an omp discovery root (`~/.agents/skills`, `~/.omp/agent/skills`, `~/.claude/skills`, project walk-up)". Three of the four hold; the second does not exist as a root in 18.12.5.

Repro / evidence:

```
$ grep -c '.omp/agent/skills' /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings   # 0
$ ls -d ~/.omp/agent/*skills*                                                        # ENOENT
$ grep -o 'Load skills from [^\\]*' …                                                # .agent/skills and .agents/skills (project walk-up + user home)
                                                                                     # .claude/skills/*/SKILL.md
$ grep -o 'Auto-generated managed skills from [^\\]*' …                              # ~/.omp/agent/managed-skills
```

`~/.omp/agent` contains no `skills` dir; `agentSubdir` storage paths are `agent.db, blobs, commands, custom-session-files, history.db, last-changelog-version, memories, models.db, modules, omp-crash.log, prompts, sessions, skill-descriptions.db, terminal-sessions, themes, tools` — no `skills`. The census's own excluded-class row (`instruction-surface-census-round13.md` § C) names `~/.omp/agent/managed-skills`, not `~/.omp/agent/skills`.

Impact: a skill placed at `~/.omp/agent/skills` would not be discovered; the parenthetical also omits `.agent/skills` (the user-home half of the documented pair). Repair: `~/.agent/skills`, `~/.agents/skills`, `~/.claude/skills`, project walk-up; managed skills are `~/.omp/agent/managed-skills`.

## F4 — the opencode log recipe is dead on 1.19.3 (`SKILL.md:103`, `:429-430`)

`SKILL.md:103` instructs: "on opencode read the global roots and `grep -o 'message=init count=[0-9]*' ~/.local/share/opencode/log/opencode.log`." The bullet at `:429-430` presents the same grammar as current ("`message=init count=N` per instance, latest 18; `duplicate skill name` warns").

Repro:

```
$ grep -o 'message=init count=[0-9]*' ~/.local/share/opencode/log/opencode.log ; echo $?
1                       # no output
$ grep -c 'init count' ~/.local/share/opencode/log/opencode.log
0
$ grep -c 'init count' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings
0
$ grep -ac 'init count' /fast/scratch/kotoba-r47/shared/bin/opencode-1.19.3
0
```

The literal is absent from the 1.19.3 binary, so no new run can emit it; the current log is entirely 2.0.26 (`head -1`/`tail -1` both `message="cli starting" version=2.0.26 …`; mtime 2026-10-20 07:52, before the 1.19.3 npx cache at 18:33) and contains 0 occurrences. The live analogue is `message="skills rescanned"` (log lines 1803-1805, 2026-10-11, with the six `sources="[...directory:…]"` roots) — exactly what `verifiers/baseline.json`'s `round18_move` already recorded. `duplicate skill name` survives in 1.19.3 (1 occurrence in the dump, confirmed at the `logWarning("duplicate skill name"…)` site), so only the `init count` half and the "latest 18" count are dead.

Impact: the opencode verification recipe returns nothing and a reader concludes "no offer trace"; the round-8/9 provenance of the numbers is hidden by the present tense.

## F5 — the opencode config surfaces are gone (`SKILL.md:399`, `:409-417`)

Claims: `~/.config/opencode/skills/ufo/SKILL.md` as an exemplar (`SKILL.md:45`, `:399`); `~/.config/opencode/agents/*.md` (18 files, 14–197 lines); `~/.config/opencode/command/*.md` (3 files).

Repro:

```
$ ls -la ~/.config/opencode/
cli.json  opencode.json  service.json          # no subdirectories
$ ls ~/.config/opencode/agents/*.md | wc -l     # 0 (no such directory)
$ ls ~/.config/opencode/command/*.md | wc -l    # 0
$ ls ~/.config/opencode/skills/ufo/SKILL.md     # ENOENT
```

The config JSONs carry no `agent` map (`jq` keys of `opencode.json` = `$schema, theme, autoupdate`; `cli.json` = `$schema, session, tabs`). The live agent-definition surface is `~/.omp/agent/agents/*.md` (13 files now; the census § C row at `instruction-surface-census-round13.md:464` records 37 at round 13). Impact: the "Instruction surfaces" evidence list cites three dead roots; the agent-definition checklist still has a live target, but not the one the file names. The `ufo` exemplar citation at `:399` is also dead.

## F6 — cache/live-set counts: 7 is actually 10; "never pruned" is contradicted by the file's own history

`SKILL.md:29-33`: "5/17 rows at round 7, 17 rows at round 9, **18 at round 13** … all 17 live keys still reproducing … (2026-10-14 errata — the live set is now 7 …). The count is not a coverage meter: rows are keyed per `(name, description-as-loaded)` and never pruned, so the 18th row is a project-scoped `ufo` copy …".

Repro:

```
$ ls -d ~/.agents/skills/*/ | xargs -n1 basename | tr '\n' ' '
create-toolset godspeed omarchy reverse-engineer-anything shokunin swarm tower ufo unreal-mcp unreal-skill
$ sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*) from skill_descriptions;"
17
$ python3 verifiers/verify_harness_claims.py
DRIFT omp.db.rows: observed=17 expected=14
DRIFT omp.offered.skills: observed=10 expected=7
DRIFT omp.cache.misses: observed=3 expected=0
DRIFT omp.catalogue.total: observed=10 expected=7
DRIFT omp.catalogue.missing_names: observed=['create-toolset', 'unreal-mcp', 'unreal-skill'] expected=[]
DRIFT omp.cache.verified_skills: observed=10 expected=7
DRIFT oc.roots.names_plus_builtin: observed=11 expected=7
21/28 checks pass; exit=1
```

The live set is 10, not 7; the cache has 17 rows now, while `verifiers/baseline.json`'s `round18_move` says the db held **14** rows at round 18 and this file says **18** at round 13. A never-pruned, append-only cache cannot go 18 → 14 → 17. The binary has migration/adoption machinery (`legacyPath`, `VACUUM INTO ?`, "Skill description cache not adopted" — dump window at the `skill-descriptions.db` literals), so [INFERENCE] the db was replaced/adopted across an upgrade and the "never pruned" sentence is false across that boundary, or the round-13 count was wrong. At 17 rows the claimed 18th project-scoped `ufo` row is absent.

## F7 — lowercase `/home/vgpnk/projects` paths and stale populations (`SKILL.md:303`, `:401`, `:403`, `:405`)

```
$ ls -ld /home/vgpnk/projects
ls: cannot access '/home/vgpnk/projects': No such file or directory
$ ls -ld /home/vgpnk/Projects
drwxr-xr-x … /home/vgpnk/Projects
$ ls /home/vgpnk/Projects/shokunin/*/AGENTS.md | wc -l
17
$ ls /home/vgpnk/Projects/shokunin/.ufo/prompts/*-L1.md | wc -l
8
$ ls /home/vgpnk/Projects/shokunin/.ufo/prompts/*-round-*.md | wc -l
263
```

The host is case-sensitive; the lowercase root does not exist as a path, so the three citations fail as pasted. The `*/AGENTS.md` glob matches 17 files, not 6. The L1 count (8) holds; the round-file count (50) is the round-9 recount against 263 live, and the repo's own `checklist-baseline.json` box map already records 89 prompt files at round 15. This is pre-existing (BASE has the same lowercase paths), not a round-47 regression — but it is a present-tense root claim in the file's evidence base.

## F8 — session/capture populations are stale (`SKILL.md:422-426`, `:441-445`)

```
$ sqlite3 -readonly ~/.local/share/opencode/opencode.db "select count(*) from session_v2;"
21
$ sqlite3 -readonly ~/.local/share/opencode/opencode.db "select count(distinct session_id) from session_message;"
21
$ sqlite3 -readonly ~/.local/share/opencode/opencode.db ".tables"
account account_state control_account credential event event_sequence instruction_blob instruction_entry instruction_state kv migration permission project project_directory session_inbox session_message session_pending session_v2 workspace worktree
$ find ~/.omp/agent/sessions -name '*.jsonl' | wc -l
15125
$ ls ~/.omp/logs/http-400-requests/*.json | wc -l
9
```

The file claims "over 398 sessions / 415 skill calls" (opencode.db), "5842 files" (omp sessions), and "32 … / 23 at round 7" (http-400 captures). The opencode DB has 21 sessions and no `session`/`part` tables, so the round-9 query shape is gone; the omp session tree is 2.6× the claimed count; the capture directory is 9. The file itself says the counter moves ("re-run before citing"), but the numbers are presented as the current evidence base. This is a freshness defect, not a fabricated claim.

## F9 — minor: the `--json` field path in `SKILL.md:99-101` is nested under `observed`

> take the two fields the verifier already resolves: `python3 verifiers/verify_harness_claims.py --json` → `omp.catalogue_path` / `omp.catalogue_timestamp`.

Repro:

```
$ python3 verifiers/verify_harness_claims.py --json | jq -r '.omp.catalogue_path'
null
$ python3 verifiers/verify_harness_claims.py --json | jq -r '.observed.omp.catalogue_path'
/home/vgpnk/.omp/agent/sessions/…/KotobaR47-2.W2Matrix2x2-2.jsonl
```

Top-level JSON keys are `observed`, `results`, `modes`, `verdicts`, `summary_paths`; the two fields live under `observed`. The fields exist and resolve, but the sentence's path notation sends a jq user to `null`. Low severity; repair the notation to `observed.omp.catalogue_path` / `observed.omp.catalogue_timestamp`.

# Claims that survived the attack (findings, not padding)

- `<skills>` is still the omp catalogue tag in 18.12.5 (1 occurrence), and the template is `- {{name}}: {{description}}`, matching `SKILL.md:22-23`; `<available_skills>` is also present (2 occurrences), so the tag-split sentence at `:430` holds.
- The opencode catalogue row (`SKILL.md:92`) holds at 1.19.3, including `<location>`: the system-prompt builder calls `_l.fmt(h,{verbose:!0})` (window at the `SystemPrompt.skills` function), and the verbose formatter emits `<available_skills><skill><name>…<description>…<location>…</location></skill></available_skills>`. The separate `@opencode/v2/SkillGuidance` baseline template (`Yf`) omits `<location>`, but it is not the system-prompt renderer the row describes. The literal `fmt(list,{verbose:true})` is minified to `_l.fmt(h,{verbose:!0})`; `fmt` is real, so this is source-shape paraphrase, not a dead anchor.
- The omp key/template mechanism holds: key function `D(e) = sha256(w ‖ \x00 ‖ name ‖ \x00 ‖ description)`, template 273 bytes, sha256 `c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51` — `verify_harness_claims.py` reports `omp.elf.template_sha256` PASS and `omp.elf.template_bytes` 273/273.
- C1 after battery holds at default resolution: `verify_surfaces.py` exit 0, 7/7 checks; `check_substrate_pins.py` exit 0, `OK 3/3 pins hold`; `before/SUMMARY.md` records surfaces exit=2 (old `~/.opencode/bin` default) and pins exit=2 DRIFT 3/3.
- `verify_surfaces.py` is 7 checks; `verify_harness_claims.py` is 28 checks (21 pass / 7 live drifts; exit 1 on drift as documented); `checklist-baseline.json` is 41 boxes (8 executed / 0 delegated / 33 unexecuted) — all three counts hold.
- The C2 frontmatter claim holds: description `<skills>` count 1 at BASE → 0 at tip; `trigger.no_xml_tag` PASS evaluated 2; name 15 chars equal to the directory; description 814 chars.
- The round-47 opencode bullet's install facts hold: wrapper, 1.19.3 package, ELF sha `179ca421…`, baseline pin, census § B′, `~/.opencode/bin` gone.

# What I did NOT check

- Upstream `github.com/sst/opencode` dev-branch source line numbers cited at `SKILL.md:432-441` (`packages/opencode/src/skill/index.ts:321-343`, `:105-139`, `:235-246`, `session/system.ts:107-119`, `tui/src/component/dialog-skill.tsx:41`): no local checkout; these are upstream-dev citations, not the pinned 1.19.3 binary. I checked the 1.19.3 mechanism at the corresponding sites, not the line numbers.
- The omp catalogue census numbers at `SKILL.md:441-447` (3911/3911 offered, 4056+ records, 14 catalogues) and the trigger-miss analysis at `:422-426` (0 misses, 51.5% coverage, 387/387, 205/399): not re-derived; I checked only the current catalogue/offered set and the DB schema/session count.
- `verify_harness_claims.py --self-test` and `verify_skill_checklist.py --self-test` were not run; the C3 corpus/GOVERNANCE_ERRATA/fault-harness claims are outside my SKILL.md-prose slice.
- opencode 1.19.3 runtime behavior: the wrapper was not executed (contract), so all opencode render/offer claims are static string/source evidence, not observed sessions.
- When the `_8n`/`A8n`/`K7s` identifiers moved (18.12.2 → 18.12.5): I verified absence in 18.12.5 and the replacement code, not the build where the rename happened.
- The `~/.omp/agent/sessions` JSONL content (`session_init` counts, catalogue blocks): file counts only; no session body was read.

Tool installs/updates: none. No pacman/uv/npx install was run; only read-only probes and the four repo verifiers.
