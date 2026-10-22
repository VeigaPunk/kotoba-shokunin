# SrcCopilotCli — round-51 build seat (C2 source: GitHub Copilot CLI)

**Result (one line): HOLDS — GitHub Copilot CLI documents per-skill removal levers other than description wording; the best is the frontmatter field `disable-model-invocation` (cli-command-reference.md:1278), which requires a NEW SOURCES row (S031) for the CLI command reference page because the existing S028 row's page (cli-plugin-reference.md) does not contain the lever.**

## Fetch record (ordinary means: `curl -sSL`; no browser, no bot challenge; `.md` variants served and used)

| file | URL | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| cli-plugin-reference.md | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference`.md` | 2026-10-22T14:19:08Z & 14:47:34Z (re-fetch byte-identical) | 200 | 47,200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` |
| cli-command-reference.md | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference`.md` | 2026-10-22T14:19:21Z | 200 | 461,944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` |
| add-skills.md | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills`.md` | 2026-10-22T14:19:37Z | 200 | 10,057 | `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0` |
| cli-config-dir-reference.md | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference`.md` | 2026-10-22T14:20:27Z | 200 | 166,811 | `8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0` |
| create-skills.html | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-skills (no suffix) | 2026-10-22T14:19:37Z | 301 → add-skills; final 200 | 625,849 | `d35b8526c2bb5c70849f1e537541b37402c2093616aa1af43e94886f239dc2ca` |
| create-skills.md | same URL + `.md` | 2026-10-22T14:19:37Z | 404 | 502 | (GitHub 404 body) |
| cli-command-reference.html | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference (no suffix) | 2026-10-22T14:47:34Z | 200 | 1,971,126 | `fbc28449733cb1f4e0df2dbe1d4f872f52418d055a9202291349c8b39f8bf379` |

The how-to URL the assignment named (`create-skills`) is a 301 alias of `add-skills`; its `.md` variant is 404. The CLI skills how-to linked from the reference (`add-skills`) was used instead. The `.md` routes are the text of record; the CLI command reference `.md` was used for all line numbers cited.

## S028 (existing row) line, verbatim column shape

```
| S028 | GitHub Docs — GitHub Copilot CLI plugin reference — https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference | docs | A | The precedence rules GitHub Copilot CLI states for duplicate component names, including skills, and the length caps it states for manifest descriptions (vendor documentation for GitHub Copilot CLI, not a measurement of omp or opencode) | § Loading order and precedence (`cli-plugin-reference.md:411-421`); § Optional metadata fields (`:195`); § Plugin entry fields (`:349`); fetched as .../copilot-cli-reference/cli-plugin-reference.md (200, 47,200 B, sha256 `d0d362cc…`) on 2026-10-22T12:31:51Z | Copilot CLI documents name-keyed precedence for duplicate components (the Copilot SDK page also documents one: a same-name provider skill replaces a file-based skill, SDK `skills.md:685`): agents and skills use first-found-wins precedence, skills are deduplicated by the `name` field inside `SKILL.md`, and a plugin cannot override project-level or personal configurations; the page's 1,024-character cap sits under legacy plugin-manifest fields (`:195`); the page states no cap for the SKILL.md `description` | mined | 2026-10-22 | 90d | corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md |
```

## Levers documented by GitHub Copilot CLI (other than description wording)

| key term (code token) | what it does, per the page | where it is set | verbatim quote (≤25 words) + location |
|---|---|---|---|
| `disable-model-invocation` | prevents the agent from automatically invoking that skill — automatic choice off, while `/SKILL-NAME` user invocation remains (field is per-skill) | `SKILL.md` YAML frontmatter (skill author) | "Prevent the agent from automatically invoking this skill. Default: `false`." (`cli-command-reference.md:1278`) |
| `copilot skill disable <name>` | disables a skill by name (not loaded / not offered) | CLI command (`copilot skill disable`) | "Enable or disable a skill by name." (`cli-command-reference.md:1313`) |
| `disabledSkills` | "Listed skills are discovered but not loaded" — removed everywhere by name | settings file (`~/.copilot/settings.json` user; `.github/copilot/settings.json` repository-level union) | "Skill names to disable. Listed skills are discovered but not loaded." (`cli-config-dir-reference.md:461`); repo-level: "Skills discovered but not loaded." (`:566`) |
| `ignoredSkillsLocations` | excludes directories (and descendants) from discovery regardless of the location that would surface them — scope/outside-a-scope by path | settings file | "Skill directories (and their descendants) excluded from discovery, regardless of which location would otherwise surface them." (`cli-config-dir-reference.md:473`) |
| `/skills` dashboard Enable/Disable | interactive toggle (same operation as `copilot skill disable`) | interactive session | "Enable or disable specific skills: use the command `/skills` … choose **Enable** or **Disable**." (`add-skills.md:139`) |
| `copilot plugin disable NAME` | disables a whole plugin (plugin-level; removes all skills of that plugin, not one of two) | CLI command | "Disable a plugin without uninstalling it." (`cli-plugin-reference.md:21`) |
| `enabledPlugins` managed-policy overlay | org/MDM policy pins a plugin's activation; cannot be re-enabled/disabled/repointed locally | policy/settings overlay | "A plugin or marketplace pinned by an organization or MDM managed policy (`enabledPlugins`, `extraKnownMarketplaces`) can't be re-enabled, disabled, or repointed locally—the managed value wins." (`cli-plugin-reference.md:31`) |

## Does the page state anything about choosing BETWEEN two matching skills? — No.

The requested sweep `grep -niE 'overlap|conflict|precedence|disable|deny|permission|hidden|invocation'`:
- `cli-plugin-reference.md` → **18 hits** (all listed verbatim below); none concerns two differently named skills whose descriptions both match.
- `cli-command-reference.md` → **137 hits**; the skill-relevant hits are at `:1278` (`disable-model-invocation`), `:1300` (`ignoredSkillsLocations`), `:1302` (plugin-qualified same-name coexistence), `:1313` (`copilot skill disable`), `:1324` (bash example), `:1330` (list `--json` shape), `:1334` (commands alternative format). Everything else is CLI-flag/plugin/`--config-dir` chrome.
- `add-skills.md` → **3 hits**: `:73` (`allowed-tools` pre-approval), `:139` (`/skills` Enable/Disable), `:149` (`copilot skill disable SKILL-NAME`).

The only arbitration rules documented are **name-keyed**: first-found-wins for duplicate names (`cli-plugin-reference.md:415-417`; diagram `:447` "AGENT SKILLS - FIRST LOADED IS USED (dedup by name)"; `cli-command-reference.md:1282`), and same-named skills from two plugins coexist under plugin-qualified invocation names with the bare name routing to the higher-priority plugin (`cli-command-reference.md:1302`). Comp:

 skill selection is description-framed, not tick-broken: "Copilot will decide when to use your skills based on your prompt and the skill's description." (`add-skills.md:121`).

**Bound:** all disable/deny levers above are removal levers — they take a skill out of choice; they are NOT a documented tie-break between two matching skills. No page says otherwise.

## Single best lever + drafts

### Best lever
`disable-model-invocation` — frontmatter field, skill-author held, effect **automatic choice off**: it stops the model from choosing that one skill while keeping it user-invocable. It is in the counter's reviewed lever list for GitHub Copilot CLI and is a verbatim code span on the CLI command reference page.

### (a) SKILL.md table row — NOTE CONFLICT WITH CURRENT COUNTER
The assignment's requested row shape is **4 columns**: `| GitHub Copilot CLI | <lever, plain words> | <S### row> | `<key term>` |`. The counter as it now stands (`verifiers/check_overlap_levers.py`, SKILL_HEADER = client|lever|held by|effect|row|key term) requires **6 columns**; the 4-column form parses as "SKILL.md table absent" (verified: `UNBACKED: SKILL.md table absent (GitHub Copilot CLI)`). Land the 6-column row:
```
| GitHub Copilot CLI | frontmatter flag that turns off the agent's own invocation of one skill | skill author | automatic choice off | S031 | `disable-model-invocation` |
```

### (b) Entry table row (matches counter's ENTRY_HEADER: client|row|lever|quote)
```
| GitHub Copilot CLI | S031 | frontmatter flag that turns off the agent's own invocation of one skill | "`disable-model-invocation` | boolean             | No       | Prevent the agent from automatically invoking this skill." (cli-command-reference.md:1278) |
```
(Pipes inside the quote cell must be escaped as `\|` in the markdown table; the counter's split_row unescapes them. Word count 14 ≤ 25; code span `disable-model-invocation` present; quote is a verbatim byte substring of line 1278 and is found live by `--fetch`.)

### (c) Registry change — S028's cells do NOT cover the lever; a NEW row is required
S028's page (`cli-plugin-reference.md`) does not contain `disable-model-invocation` (0 hits), `copilot skill disable` (0 hits), or `disabledSkills`. Its scope/anchor/teaches cover name-keyed precedence and description caps only. Per SOURCES contract v1 rule 2 (append-only: only `status`/`recheck`/`used-by` change in place; a correction is a new row whose `teaches` opens "supersedes S0NN —"), S028's scope/anchor/teaches must NOT be edited in place; the lever lives on a different page, so its row is a distinct source, not a correction.

Full new row (11-column registry shape; id S031 is free after S030 is taken by the Copilot SDK seat — the L1 assigns final ids):

```
| S031 | GitHub Docs — GitHub Copilot CLI command reference — https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference | docs | A | The per-skill removal levers GitHub Copilot CLI documents for agent skills in its command reference, and the name-keyed arbitration rules it repeats (vendor documentation for GitHub Copilot CLI, not a measurement of omp or opencode) | § Skills reference → § Skill frontmatter fields (`cli-command-reference.md:1269-1279`); § Skill locations (`:1281-1302`); § Managing skills non-interactively (`:1304-1330`); fetched as .../cli-command-reference.md (200, 461,944 B, sha256 `c61997ef…`) on 2026-10-22T14:19:21Z | Copilot CLI documents a frontmatter field `disable-model-invocation` (default `false`) that prevents the agent from automatically invoking the skill while `/SKILL-NAME` stays available, a `copilot skill disable` command, a `disabledSkills` settings key and `ignoredSkillsLocations`; duplicate-NAME arbitration is first-found-wins, and same-named skills from two plugins coexist under plugin-qualified names with the bare name routing to the higher-priority plugin | mined | 2026-10-22 | 90d | corpus/knowledge/skill-overlap-levers-round51.md |
```

S028 `used-by` old → new (in-place, allowed, must be logged in the round-51 lesson § Gate) if the new entry cites S028 for the first-found-wins fact:
- old: `corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md`
- new: `corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md, corpus/knowledge/skill-overlap-levers-round51.md`

## Counter verification (run on scratch fixture; fixture only, no lane writes)

- `python3 -B verifiers/check_overlap_levers.py --root /fast/scratch/hyaku/kotoba-r51/build/SrcCopilotCli/final` → `BACKED GitHub Copilot CLI`; `overlap levers backed 1 of 7 clients` (exit 1 — only the one client row exists in the fixture).
- `--fetch` → `FETCH GitHub Copilot CLI: quote found (https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)`; `quotes found on live pages 1 of 1`.
- `scripts/sources-census.sh validate <fixture> --today 2026-10-22` → exit 0; only E11 lines for S028's pre-existing round-49/50 used-by paths (absent in the scratch fixture, not a defect of S031); S031 row itself clean (new URL, mined, used-by names the entry, NF=13).
- Negative control: key term `copilot plugin disable NAME` → `UNBACKED: key term not a reviewed overlap lever (GitHub Copilot CLI)`; S031 URL = add-skills + fixture's fabricated quote → `BACKED` offline but `FETCH … quote not found` live (add-skills.md has 0 occurrences of `disable-model-invocation`). **Finding for the L1:** the counter's own `_control_world` fixture pairs the CLI client with the add-skills URL and a fabricated quote that is not on that page; a landed S031 pointing at add-skills would fail `--fetch`. The cli-command-reference URL is the one whose page carries the quote.

## Out-of-scope / notes
- SDK skills page (`sdk-skills.md`) is the SrcCopilotSdk seat's client; fetched here only for row-id collision check (S030 claimed by that seat).
- `about-agent-skills` concept page: `.md` variant 404; HTML 200 with 0 mentions of the reviewed levers (recorded for completeness).
- No tooling installed this session; no lane files modified (report file only).
