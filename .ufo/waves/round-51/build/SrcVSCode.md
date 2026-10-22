# Round-51 seat report — SrcVSCode (C2 frontier source, client: VS Code)

**HOLDS — the VS Code page documents a frontmatter lever other than description wording that removes a
skill from the model's choice: `disable-model-invocation` (plus `user-invocable`); the page documents
no tie-break between two matching skills, so a disable lever is a removal from choice, not arbitration.**

C2's VS Code row is backed by S025's page, opened by ordinary means (curl, `.md` variant), fetched
twice in this session and byte-identical to the round-50 fetch. Lane base
`43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`; the lane was read-only — only this report was written
there. Artifacts in `/fast/scratch/hyaku/kotoba-r51/build/SrcVSCode/`.

## Fetch record

| route | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 2026-10-22T14:19:03Z | 200 | 22,871 | `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5` |
| same route, second fetch with headers | 2026-10-22T14:20:44Z | 200 | 22,871 | `de5ba34f…` (`cmp` exit 0, byte-identical) |
| https://code.visualstudio.com/docs/enterprise/manage-ai-settings.md (linked from the page) | 2026-10-22T14:26Z | 200 | 33,047 | `49894046232ff57b4b964550f962cbc4a9a975930e910398b9dcb540960f073f` |

The **`.md` variant** of the requested URL was used (`content-type: text/markdown; charset=UTF-8`),
395 lines. The bytes are byte-identical to the round-50 fetch in S025 — **the page has not changed
since round 50**; only the HTTP `last-modified` moved (now `Thu, 22 Oct 2026 09:16:14 GMT`).

## Findings

**F1/F2 — The lever is a frontmatter flag, not the description.** § SKILL.md file format → § Header
(required) documents two optional frontmatter fields beside `description` (`agent-skills.md:150-151`).
**F2 — `disable-model-invocation` (frontmatter field, boolean, default `false`) — the best lever.**
What it does: stops the agent loading the skill on relevance, so the model can no longer pick it; the
skill is then reachable only by a manual `/` slash command. Where it is set: the skill's own `SKILL.md`
YAML frontmatter. Quote (`agent-skills.md:151`, 12 words): "Controls whether the agent can automatically
load the skill based on relevance." Same line (13 words): "Set to `true` to require manual invocation
through the `/` slash command only." Table-row form (`agent-skills.md:295`, 17 words): "|
`disable-model-invocation: true` | Yes | No | Skills you only want to run on demand |"

**F3 — `user-invocable` (frontmatter field, boolean, default `true`).** Hides the skill from the `/`
menu while the agent may still load it — the opposite direction from F2, so it does **not** stop the
model from choosing. Quote (`agent-skills.md:150`, 20 words): "Set to `false` to hide the skill from
the `/` menu while still allowing the agent to load it automatically."

**F4 — Both flags together are the page's own "Disabled skills"** (`agent-skills.md:296`, 9 words):
"Both set | No | No | Disabled skills" — no slash command, not auto-loaded.

**F5 — Path-scoped levers are weak.** `chat.agentSkillsLocations` adds locations and is deprecated
(`:69`); `chat.useCustomizationsInParentRepositories` widens discovery to the parent repo root (`:72`);
`github.copilot.chat.skillTool.enabled` turns on the forked-context loader (`:196`). None is a per-skill
switch; no removal semantics for a location are documented.

**F6 — One off-page lever, for the L1's judgement.** The linked `/docs/enterprise/manage-ai-settings.md`
documents a managed policy `ChatStrictPluginOnlyCustomization` that blocks "standalone user and
workspace skills, agents, instructions, and MCP servers" (`manage-ai-settings.md:294`), and
`Claude3PIntegration` = `false` disables Claude Agent sessions (`:227`). Org-policy switches on a
different URL; using them needs a new `corpus/SOURCES.md` row (not drafted).

**F7 — The page states nothing about choosing BETWEEN two matching skills.** Its only arbitration
sentence concerns duplicate **names** across workspace roots, inside the experimental Codex note
(`agent-skills.md:64`, 15 words): "If skills in `.github/skills/` have duplicate names across workspace
roots, the primary root takes precedence." Same line (20 words): "Discovery makes skills available to
the model but does not guarantee that it invokes a skill for every relevant prompt." The Marketplace
paragraph (`:129`) keeps same-named skills side by side. Per the round's bound: a disable or deny lever
is a way to **remove** a skill from choice, not a documented tie-break — the page documents no rule that
picks one of two overlapping descriptions.

**F8 — The requested sweep found nothing more.** `grep -niE 'overlap|conflict|precedence|disable|deny|permission|hidden|invocation'`
counts over the fetched markdown: `overlap` 0, `conflict` 0, `deny` 0, `hidden` 0, `precedence` 1
(line 64, F7), `permission` 1 (line 277, inside an example skill's troubleshooting list, not a lever),
`disable` 5 (lines 66, 151, 289, 295, 296), `invocation` 3 (lines 149, 151, 289). Widening: `tie-break`
0, `ambig` 0, `prioriti` 0, `two skills` 0, `same name` 1 (:129), `multiple skills` 1 (:15), `choose`
2 (:28 a docs anchor, :127 the install step) — no hit describes arbitration between two skills.

**F9 — D3 input.** `SKILL.md:375-377` says the documented remedy for overlap is "a more specific
description". For VS Code that is now incomplete: the same page documents two frontmatter flags that
change who may load a skill. The D3 rewrite should cite the levers, and round-50 finding 4 is
superseded for this client.

## Deliverable (a) — `SKILL.md` § Anti-patterns, "Overlap levers by client" table row

```markdown
| VS Code | frontmatter flag that stops the agent auto-loading the skill, so the model can no longer pick it and only a manual slash command can | S025 | `disable-model-invocation` |
```

## Deliverable (b) — `corpus/knowledge/skill-overlap-levers-round51.md`, entry table row

```markdown
| VS Code | S025 | `disable-model-invocation` frontmatter: stops the agent auto-loading the skill, leaving manual `/` invocation only | "Use the `user-invocable` and `disable-model-invocation` frontmatter properties to control how each skill is accessed:" (agent-skills.md:289) |
```

The quote contains the key term `disable-model-invocation` exactly (14 words, verbatim, pipe-free so
the cell parses). Alternates: "Controls whether the agent can automatically load the skill based on
relevance." (`agent-skills.md:151`, 12 words — states the effect but **not** the key term, so it fails
C2's key-term rule alone) or "| `disable-model-invocation: true` | Yes | No | Skills you only want to
run on demand |" (`agent-skills.md:295`, 17 words — carries the key term but its pipes break the cell
unless escaped, and escaping breaks the verbatim-substring check).

## Deliverable (c) — `corpus/SOURCES.md` row S025 (no new row; S025 already covers this page)

The scope / anchor / teaches cells do **not** cover the lever, so three cell rewrites and one
`used-by` append are needed. Old -> new (cell text, one line each; the applied row is in `patch.diff`):

- **scope** old: `How VS Code / GitHub Copilot presents a skill's frontmatter \`description\` and loads the skill from it, and what the page says about skills that collide (vendor documentation, not a measurement of omp or opencode)` → new: `How VS Code / GitHub Copilot presents a skill's frontmatter \`description\` and loads the skill from it, which frontmatter flags keep a skill out of the model's choice, and what the page says about skills that collide (vendor documentation, not a measurement of omp or opencode)`
- **anchor** old: `§ SKILL.md file format → § Header (required), \`description\` row (\`agent-skills.md:148\`); … § Install a skill from the Customization Marketplace, same-name paragraph (\`agent-skills.md:129\`); fetched as https://code.visualstudio.com/docs/agent-customization/agent-skills.md (200, 22871 B, sha256 \`de5ba34f…\`) on 2026-10-22T12:29:33Z, twice byte-identical; the requested route … answers HTTP 301 to it, and its HTML renders 200, 157298 B, sha256 \`9118c27c…\`; page Last-Modified Wed, 21 Oct 2026 06:19:42 GMT; upstream source docs/agent-customization/agent-skills.md in microsoft/vscode-docs (24087 B, sha256 \`bae0c84d…\`, DateApproved 10/21/2026)` → new: `§ SKILL.md file format → § Header (required), \`description\` row (\`agent-skills.md:148\`), \`user-invocable\` row (\`:150\`) and \`disable-model-invocation\` row (\`:151\`); … § Install a skill from the Customization Marketplace, same-name paragraph (\`agent-skills.md:129\`); § Use skills as slash commands, configuration table (\`agent-skills.md:289-296\`); fetched as https://code.visualstudio.com/docs/agent-customization/agent-skills.md (200, 22871 B, sha256 \`de5ba34f…\`) on 2026-10-22T12:29:33Z, twice byte-identical, and again 2026-10-22T14:20:44Z (200, 22871 B, sha256 \`de5ba34f…\`, byte-identical to the 12:29:33Z fetch; HTTP \`last-modified\` now Thu, 22 Oct 2026 09:16:14 GMT); the requested route … answers HTTP 301 to it, and its HTML renders 200, 157298 B, sha256 \`9118c27c…\`; upstream source docs/agent-customization/agent-skills.md in microsoft/vscode-docs (24087 B, sha256 \`bae0c84d…\`, DateApproved 10/21/2026)` (the stale "page Last-Modified Wed, 21 Oct 2026 06:19:42 GMT" clause is dropped — superseded by the header value)
- **teaches** old: `Copilot matches a request against the skill's \`description\`, which must say what the skill does and when to use it, capped at 1024 characters; no tie-break between two overlapping skills is documented — the sweep on the fetched text (grep -ciE) gives overlap 0, ambig 0, tie-break 0, conflict 0, prioriti 0, truncat 0, precedence 1 (duplicate names across workspace roots), multiple skills 1 (composing skills), same name 1 (Marketplace keeps both)` → new: `Copilot matches a request against the skill's \`description\`, which must say what the skill does and when to use it, capped at 1024 characters; two frontmatter flags change who may load a skill without touching the description — \`disable-model-invocation: true\` stops the agent auto-loading the skill, leaving manual \`/\` invocation only, and \`user-invocable: false\` hides the skill from the \`/\` menu while the agent may still load it, and with both set the page calls the skill "Disabled skills"; no tie-break between two overlapping skills is documented — the sweep on the fetched text (grep -ciE) gives overlap 0, ambig 0, tie-break 0, conflict 0, prioriti 0, truncat 0, precedence 1 (duplicate names across workspace roots), multiple skills 1 (composing skills), same name 1 (Marketplace keeps both)`
- **used-by** old: `corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md` → new: `corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md, corpus/knowledge/skill-overlap-levers-round51.md`

The row's `status` is already `mined`, `kind` `docs`, `tier` `A`, so C2's "a `mined` row whose
`used-by` names the entry" is satisfied by the rewrite above; no new id is needed, registry stays at 29 rows.

## Evidence (commands, exit codes, paths)

- Fetch: `curl -sSL -D headers.txt -o agent-skills.md -w 'status=%{http_code} size=%{size_download}'` →
  `status=200 size=22871`; `sha256sum` → `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5`;
  `wc -l -c` → `395 22871`; second fetch `cmp` → exit 0; headers → `HTTP/2 200`,
  `content-type: text/markdown; charset=UTF-8`, `last-modified: Thu, 22 Oct 2026 09:16:14 GMT`.
  `curl -sSL -o manage-ai-settings.md …/docs/enterprise/manage-ai-settings.md` → `status=200 size=33047`.
- Quote verification: every quote in F2-F4 and F7 checked with `grep -qF` against the fetched bytes —
  8 of 8 matched, each located to its line (289, 151, 151, 150, 295, 296, 64, 64), word counts 9-20
  (all ≤ 25). Sweep: `grep -ciE` per term → `overlap` 0, `conflict` 0, `deny` 0, `hidden` 0,
  `precedence` 1, `permission` 1, `disable` 5, `invocation` 3, `tie-break` 0, `ambig` 0, `prioriti` 0,
  `two skills` 0, `same name` 1, `multiple skills` 1, `choose` 2; located lines in F8.
- Registry: `awk 'NR==38' corpus/SOURCES.md` → the S025 row (13 pipe-separated fields, `mined`); the
  edited clone row also splits into 13 fields.
- Validator: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md`
  on the unmodified lane → exit 0, `ok`, three pre-existing W04 (S018, S019, S021); the same validator
  on the private clone with the (c) edits applied → exit 0, `ok`, the same three W04, **no E-code and
  no new warning**. Negative: with the new entry file absent from the clone, the same run → exit 1,
  `E11 S025 missing used-by corpus/knowledge/skill-overlap-levers-round51.md` — row and entry file
  must land together.

## Out of scope

- Editing `corpus/SOURCES.md`, `SKILL.md` or `corpus/knowledge/skill-overlap-levers-round51.md` in the
  lane: drafts only (read-only lane bound; the L1 integrates); the wording of `SKILL.md:375-377` (D3),
  the table's other six clients, and a `corpus/SOURCES.md` row for `manage-ai-settings.md` (F6) are
  not this seat's; measuring real VS Code or Copilot arbitration is out of scope (documentation only).

## Artifacts

- `/fast/scratch/hyaku/kotoba-r51/build/SrcVSCode/agent-skills.md` — the fetched markdown (22,871 B,
  sha256 `de5ba34f…`), plus `agent-skills-2.md` (second fetch), `headers.txt`, `manage-ai-settings.md`;
  `lane/` — private clone of the lane at `43ca0bfb` with the (c) edits applied and a stub entry file;
  `patch.diff` — unified diff of those edits against `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10` (23
  lines: the SOURCES.md row plus the stub entry file). The L1 may take the row from it; the stub file
  is not a deliverable.

## Tooling

None installed or upgraded this session; `curl`, `grep`, `awk`, `cmp`, `sha256sum`, `wc`, `date`, `git`
and the fleet's `scripts/sources-census.sh` were already present. No `pacman`, `uv tool`, `cargo` or
`npm -g` transaction was run and no host service was restarted (pacman is paused host-wide this round).
