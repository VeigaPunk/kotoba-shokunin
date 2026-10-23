Result: MIXED — `.opencode/agents` and `~/.config/opencode/agents/` hold in both S078 (V2) and `opencode.ai/docs/agents` (V1), but `SKILL.md:109` and `agent-definition-files-round56.md:48,50,52` conflate V1 and V2 (`description` is required on `opencode.ai/docs/agents`, `migrate-v1.mdx` warns against mixing V2 `permissions` with the V1 checklist's `name:`, and `singular agent/ still loads` is absent from S078).

## 1. Counterexamples and Findings (attacking `c22fdd390e10623209024c9bbc2fa86b0cdfc333`)

### F1 (Strongest Counterexample — V1/V2 schema conflation and internal `SKILL.md` checklist contradiction)
- **Attacked lines:**
  - `SKILL.md:109`: `| opencode | .opencode/agents (user ~/.config/opencode/agents/; singular agent/ still loads) | Markdown frontmatter takes agent-config fields, body is the system prompt, no key required; permissions gate tools (V2 drops legacy tools) | Apply the agent-definition checklist below, which is written for opencode |`
  - `corpus/knowledge/agent-definition-files-round56.md:48`: `opencode states no required key (S078).`
  - `SKILL.md:306-316` (`## Agent-definition fidelity checklist`, boxes `agentdef.01` and `agentdef.02`).
- **Counterexample & local evidence:**
  1. **`description` is required on the current `opencode.ai/docs/agents` (V1) page, and S078 (V2) is only silent rather than stating "no required key":**
     - On `https://opencode.ai/docs/agents.md` (`docs-agents.md:245,257`, identical in `packages/web/src/content/docs/agents.mdx:241,253` at `4e0bc522`), `### Description` states verbatim:
       - `docs-agents.md:245`: `"Use the description option to provide a brief description of what the agent does and when to use it."` [md stripped, 19 words]
       - `docs-agents.md:257`: `"This is a **required** config option."` [byte-exact, 6 words]
     - In S078 (`s078-v2-agents.mdx:51,185`), V2 does not mark any key required (`s078-v2-agents.mdx:185`: `"description explains the agent's purpose. Add it to subagents because OpenCode shows it to the model choosing which agent to launch:"` [md stripped, 21 words]), but S078 never positively states that no key is required. Writing `opencode states no required key (S078)` (`agent-definition-files-round56.md:48`) and `no key required` (`SKILL.md:109`) turns V2 silence into an affirmative statement and contradicts the live V1 `/docs/agents` page.
     - V1 and V2 also differ on the omitted `mode` default: V1 `docs-agents.md:590` says `"If no mode is specified, it defaults to all."` [md stripped, 9 words], whereas V2 `s078-v2-agents.mdx:193` says `"When omitted on a new custom agent, it defaults to primary:"` [md stripped, 11 words].
  2. **Following `SKILL.md:109`'s V2 `permissions` cell and then applying `SKILL.md:109`'s Action (`Apply the agent-definition checklist below`) produces a mixed V1/V2 file whose `name:` key V2 ignores with a warning:**
     - `SKILL.md:109` teaches V2 `permissions` (`permissions gate tools (V2 drops legacy tools)`) and directs the reader to apply `## Agent-definition fidelity checklist` (`SKILL.md:304-349`).
     - That checklist is written against V1: `SKILL.md:307,314` requires enrollment in `opencode.json` singular `agent` map (V2 uses plural `agents` in `opencode.jsonc`, `s078-v2-agents.mdx:66-71`), and `SKILL.md:312` (`agentdef.01`) requires frontmatter `name:` matching the file stem.
     - S078 line 62 (`"V1 frontmatter fields are deprecated. See [Agent files](/migrate-v1#agent-files) for how files that still use them are read."` [byte-exact, 17 words]) links to `services/www/src/docs/content/migrate-v1.mdx` at `4e0bc522`, which states at lines 504–507:
       - `s078-v2-migrate-v1.mdx:504-506`: `"A file that uses any of permissions, request, system, or disabled is read as V2, and V1 fields in it, such as name, tools, permission, or temperature, are ignored with a warning in the log."` [md stripped, 35 words -> split into ≤25-word verbatim quotes below]
       - Verbatim quote 1 (`s078-v2-migrate-v1.mdx:504-505`, 20 words, md stripped): `"A file that uses any of permissions, request, system, or disabled is read as V2, and V1 fields in it,"`
       - Verbatim quote 2 (`s078-v2-migrate-v1.mdx:505-506`, 15 words, md stripped): `"such as name, tools, permission, or temperature, are ignored with a warning in the log."`
       - Verbatim quote 3 (`s078-v2-migrate-v1.mdx:507`, 14 words, byte-exact): `"Convert a file's frontmatter all at once rather than mixing the two formats."`
     - Tradeoff classification: **fixable defect** (calibration/consistency in prose), not a C1 counter reject (`verifiers/check_agent_definitions.py` does not score column 3 or the semantic compatibility of column 4).

### F2 (`permissions` vs `permission` vs legacy `tools`)
- **Attacked lines:**
  - `SKILL.md:109`: `` `permissions` gate tools (V2 drops legacy `tools`) ``
  - `corpus/knowledge/agent-definition-files-round56.md:50`: `` `permissions` (opencode V2, which drops the legacy `tools` key) ``
- **Counterexample & local evidence:**
  1. **Omits V1's active singular `permission` map:** On `https://opencode.ai/docs/agents.md`, `tools` was already deprecated in V1 in favor of singular `permission`:
     - `docs-agents.md:392` (17 words, md stripped): `"tools is deprecated. Prefer the agent's permission field for new configs, updates and more fine-grained control."`
     - V1 Markdown agent examples use `permission:` (`docs-agents.md:218-220, 505-512`), whereas V2 uses `permissions:` (an ordered list of `{ action, resource, effect }` rules, `s078-v2-agents.mdx:12-18, 242-261`).
  2. **Overstates S078 `:344` as "V2 drops legacy `tools`":**
     - S078 line 344 states (`s078-v2-agents.mdx:344`, 22 words, byte-exact): ``Do not use legacy top-level fields such as `temperature`, `top_p`, `prompt`, `permission`, `tools`, `disable`, or `maxSteps` in new V2 agent configuration.``
     - Per `s078-v2-migrate-v1.mdx:504` (10 words, byte-exact): `"V1 agent frontmatter is deprecated but still translated automatically."` V2 only ignores `tools`/`permission` with a warning when mixed into a file that also uses a V2 key (`permissions`, `request`, `system`, `disabled`).

### F3 (Unsourced provenance in `SKILL.md:99,109` for `singular agent/ still loads`)
- **Attacked lines:**
  - `SKILL.md:99`: `Basis: corpus/knowledge/agent-definition-files-round56.md (S072–S078, S026), checked by verifiers/check_agent_definitions.py.`
  - `SKILL.md:109`: `` `.opencode/agents` (user `~/.config/opencode/agents/`; singular `agent/` still loads) ``
  - `corpus/knowledge/agent-definition-files-round56.md:1,52-53`: frontmatter `source:` lists only `S072`–`S078` and `S026`, while Finding 5 (`:52-53`) says `5. **Location history (seat ScoutChangelogSweep, not SOURCES rows).** opencode moved its folders from agent/ to agents/ on 2026-01-17 and still loads the singular form`.
- **Counterexample & local evidence:**
  - Neither S078 (`s078-v2-agents.mdx`) nor `https://opencode.ai/docs/agents` (`docs-agents.md` / `docs-agents.html`) contains the string `agent/` (0 grep hits in both files).
  - The documented support for singular `agent/` actually lives in **other** opencode pages not cited in `SOURCES.md`:
    - V1 `https://opencode.ai/docs/config.md:53` (10 words, md stripped): `"Singular names (e.g., agent/) are also supported for backwards compatibility."`
    - V2 `services/www/src/docs/content/migrate-v1.mdx:486` at `4e0bc522` (17 words, md stripped): `"V1 agent files may use agent/, agents/, mode/, or modes/. V2 still discovers all four directories."`
  - Putting `singular agent/ still loads` in `SKILL.md:109` under a table whose declared basis is `(S072–S078, S026)` attributes to S078 a claim that S078 does not contain.

### F4 (Quote provenance in `agent-definition-files-round56.md:27,33-34` and `corpus/lessons/round-56.md:20,23-24`)
- **Attacked lines:**
  - `corpus/knowledge/agent-definition-files-round56.md:27`: `| opencode | .opencode/agents | S078 | "A nested path becomes part of the agent ID: text .opencode/agents/team/reviewer.md → team/reviewer" |`
  - `corpus/knowledge/agent-definition-files-round56.md:33-34`: `S078's quote is the body of a fenced example whose info string text stays in the quote; the fence markers were removed (Srcopencode).`
  - `corpus/lessons/round-56.md:20,23-24`: same quote and note in `## Gate`.
- **Evidence:**
  - Raw bytes of `s078-v2-agents.mdx:41-45`:
    - Line 41 (21 words, byte-exact): ``OpenCode discovers project `.opencode` directories from the current directory up to the project root. A nested path becomes part of the agent ID:``
    - Line 42: blank line
    - Line 43 (1 word, byte-exact): ```` ```text ````
    - Line 44 (3 words, byte-exact): `.opencode/agents/team/reviewer.md  →  team/reviewer`
    - Line 45: ```` ``` ````
  - Why `text` appears in the quote: `verifiers/check_agent_definitions.py:686,696-700` (`norm_page`) strips backticks (`re.sub(r"[`*_]", "", s)`) and collapses whitespace (`re.sub(r"\s+", " ", s)`), turning the opening fence ```` ```text ```` on line 43 into the word `text` between `ID:` (line 41) and `.opencode/agents/team/reviewer.md` (line 44). Meanwhile, lines 37–38 of `s078-v2-agents.mdx` (`~/.config/opencode/agents/<name>.md` and `.opencode/agents/<name>.md`) could not be quoted by `Srcopencode` because `norm_page` strips `<name>` as an HTML tag (`check_agent_definitions.py:699`) while `norm(quote)` does not (`:691-693`).
  - Minor inaccuracy in the quote note (`agent-definition-files-round56.md:33-34` and `round-56.md:23-24`): the quote is **not** solely "the body of a fenced example"; it concatenates the prose clause at the end of line 41 (`A nested path becomes part of the agent ID:`), the fence info string on line 43 (`text`), and the fenced body on line 44 (`.opencode/agents/team/reviewer.md  →  team/reviewer`), while collapsing newlines and the double spaces around `→`.

---

## 2. Impacted Axes and Smallest Safe Corrections

- **Impacted axes:** **calibration** and **consistency** (and **depth** where V1 vs V2 schema differences affect how an agent definition is authored or checked). None of F1–F4 breaks the frozen C1 counter (`verifiers/check_agent_definitions.py --rev c22fdd390e10623209024c9bbc2fa86b0cdfc333 --fetch`), so these are **fixable prose/provenance defects**, not a counter tradeoff.
- **Smallest safe corrections (leaving the 9 `agentdef.*` box texts in `SKILL.md:312-349` byte-identical):**
  1. **`SKILL.md:109` (`opencode` row):**
     - Remove the unsourced `singular agent/ still loads` parenthetical from `SKILL.md:109` (or label it in `agent-definition-files-round56.md` § Limits/Findings as coming from `config.md:53` / `migrate-v1.mdx:486` rather than S078).
     - Qualify column 3 and column 4 by version so V2 `permissions` is not mixed with the V1 checklist:
       `| opencode | .opencode/agents (user ~/.config/opencode/agents/) | Markdown frontmatter + system-prompt body; V2 (S078) marks no key required and uses ordered permissions rules (not legacy permission/tools); V1 /docs/agents requires description | Apply the V1 agent-definition checklist below to V1 files; do not mix V1 name/permission keys with V2 permissions |`
  2. **`corpus/knowledge/agent-definition-files-round56.md:33-34, 48, 50, 52-53` and `corpus/lessons/round-56.md:23-24`:**
     - At `agent-definition-files-round56.md:48` (Finding 3): change `opencode states no required key (S078)` to `opencode V2 marks no key required (S078; the served V1 /docs/agents page still marks description required)`.
     - At `agent-definition-files-round56.md:50` (Finding 4): change `permissions (opencode V2, which drops the legacy tools key)` to `permissions (opencode V2, which deprecates V1 permission and tools and tells new V2 configs not to use them, S078 :62,344)`.
     - At `agent-definition-files-round56.md:33-34` and `corpus/lessons/round-56.md:23-24`: state accurately that `S078's quote spans the prose lead-in on line 41, the fence info string text on line 43 (with fence backticks removed), and the example body on line 44 (with whitespace collapsed)`.

---

## 3. Verification and Fetch Receipts

### Sandbox setup
```text
$ timeout 120s bash -c '
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
rm -rf /fast/scratch/hyaku/kotoba-r56/ReopenS078
git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-shokunin-tmp-check || true
'
```
Actual command run (exit 0):
```text
$ timeout 120s bash -c '
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
rm -rf /fast/scratch/hyaku/kotoba-r56/ReopenS078
git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r56/ReopenS078 &&
git -C /fast/scratch/hyaku/kotoba-r56/ReopenS078 checkout -q c22fdd390e10623209024c9bbc2fa86b0cdfc333 &&
git -C /fast/scratch/hyaku/kotoba-r56/ReopenS078 rev-parse HEAD
'
c22fdd390e10623209024c9bbc2fa86b0cdfc333
```
No sandbox commits were made. No tools were installed or updated.

### Source fetches (ordinary `curl`, exit 0 on both batches)
Batch 1 command and observed output (exit 0):
```text
=== FETCH 1: S078 (V2 agents.mdx at 4e0bc522) ===
Fri Oct 23 03:09:20 AM UTC 2026
HTTP_STATUS=200 FINAL_URL=https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/agents.mdx BYTES=8779
8779 s078-v2-agents.mdx
6cca5b0a5a88387e94177d9c13d2e539fb710d69b2298ca6d44b9bc465c8b57a  s078-v2-agents.mdx
=== FETCH 2: opencode.ai/docs/agents (HTML) ===
Fri Oct 23 03:09:20 AM UTC 2026
HTTP_STATUS=200 FINAL_URL=https://opencode.ai/docs/agents BYTES=183509
183509 docs-agents.html
1bddca5ba3df59505ae4ec4bb082887764ad5fe255b78100408158e5d1e70b27  docs-agents.html
=== FETCH 3: opencode.ai/docs/agents.md (V1 Markdown route) ===
Fri Oct 23 03:09:21 AM UTC 2026
HTTP_STATUS=200 FINAL_URL=https://opencode.ai/docs/agents.md BYTES=20997
20997 docs-agents.md
5d070a8ba9c2db70db759aa019e2e48e5c3cd834d4892f17ffb99ba3fc852b1b  docs-agents.md
=== FETCH 4: opencode.ai/v2/docs/agents (Accept: text/markdown) ===
Fri Oct 23 03:09:22 AM UTC 2026
HTTP_STATUS=200 FINAL_URL=https://opencode.ai/v2/docs/agents BYTES=8637
8637 v2-docs-agents.md
1f87da9eeb0e996aa42b0d8e6c7b32e1ff0cb22be1e1817a61040a35cb30fa4b  v2-docs-agents.md
=== FETCH 5: opencode.ai/docs/agents (Accept: text/markdown) ===
Fri Oct 23 03:09:23 AM UTC 2026
HTTP_STATUS=200 FINAL_URL=https://opencode.ai/docs/agents BYTES=183509
183509 docs-agents-accept.md
1bddca5ba3df59505ae4ec4bb082887764ad5fe255b78100408158e5d1e70b27  docs-agents-accept.md
```

Batch 2 command and observed output (exit 0):
```text
=== FETCH 6: V2 migrate-v1.mdx at 4e0bc522 ===
Fri Oct 23 03:10:00 AM UTC 2026
HTTP_STATUS=200 FINAL_URL=https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/migrate-v1.mdx BYTES=20805
20805 s078-v2-migrate-v1.mdx
f3d42b36cec1b498d19543b32e72a069e006ee2a4a6884e548ce3a9408fd78a0  s078-v2-migrate-v1.mdx
=== FETCH 7: V2 config.mdx at 4e0bc522 ===
Fri Oct 23 03:10:01 AM UTC 2026
HTTP_STATUS=200 FINAL_URL=https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/config.mdx BYTES=16295
16295 s078-v2-config.mdx
e20d39cbc97d802d4d987faee58922e3b29aba9a5ff3153e568c909513e75e17  s078-v2-config.mdx
=== FETCH 8: V1 config.md (opencode.ai/docs/config.md) ===
Fri Oct 23 03:10:01 AM UTC 2026
HTTP_STATUS=200 FINAL_URL=https://opencode.ai/docs/config.md BYTES=26060
26060 docs-config.md
fe28a438a1464cb5a43231a7af56f2ed16b019016731052ddfc2ae86fd54cda8  docs-config.md
=== FETCH 9: V1 agents.mdx at 4e0bc522 ===
Fri Oct 23 03:10:02 AM UTC 2026
HTTP_STATUS=200 FINAL_URL=https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/packages/web/src/content/docs/agents.mdx BYTES=21066
21066 v1-agents-at-4e0bc522.mdx
1f805f8a7cd1d877272d61ad6d59dae4d014c7b26009110d1c4b26c65a634dcc  v1-agents-at-4e0bc522.mdx
```

Exact line-range inspection on `s078-v2-agents.mdx:32-46` (exit 0):
```text
 32: '## Locations'
 33: ''
 34: 'Save Markdown agents globally for all projects or inside a project:'
 35: ''
 36: '```text'
 37: '~/.config/opencode/agents/<name>.md'
 38: '.opencode/agents/<name>.md'
 39: '```'
 40: ''
 41: 'OpenCode discovers project `.opencode` directories from the current directory up to the project root. A nested path becomes part of the agent ID:'
 42: ''
 43: '```text'
 44: '.opencode/agents/team/reviewer.md  →  team/reviewer'
 45: '```'
 46: ''
```
