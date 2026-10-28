# Kb80K01 — cross-lane overlap for C2 (round 80, w1)

Axes: C2 depth (per-client `allowed-tools` semantics). C1 is not touched by this seat. This is an overlap and boundary scan with a live cross-check. It is not a claim score and not a counter run.

## 1. Sibling sweep (fresh)

`.ufo/waves/round-80/build/Kb80R04SiblingScan.md` was not present, so I ran the sweep myself. Command, run from `/home/vgpnk/Projects/shokunin`:

```
python3 -c 'import glob,os,re; root="/home/vgpnk/Projects/shokunin"; p=re.compile(r"allowed-tools|allowed_tools",re.I); files=[]
for lane in glob.glob(root+"/*-shokunin"):
  if lane.endswith("/kotoba-shokunin"): continue
  files += [x for x in [lane+"/SKILL.md",lane+"/PROVINCE.md",lane+"/corpus/README.md"] if os.path.isfile(x)]+glob.glob(lane+"/corpus/knowledge/*")
...'
```

Output: `FILES_SCANNED 1032`, `ALLOWED_TOOLS_HITS 0`, exit 0. The r79 sweep covered 1031 files with the same selection, and it also returned zero hits. Receipt: `.ufo/waves/round-80/build/Kb80K01-receipts.txt`.

Scope limit: this sweep covers only `SKILL.md`, `PROVINCE.md`, `corpus/README.md` and `corpus/knowledge/*` in the sibling lanes. It does not cover sibling `verifiers/`, `corpus/lessons/` or other paths. Absence is therefore only claimed for the swept paths.

Sibling result: no sibling lane holds `allowed-tools` semantics. The C2 overlap is with the shokuknow merge staging area, not with a sibling lane.

## 2. Overlap with the staged shokuknow entry

The staged entry is `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/client-frontmatter-and-discovery-divergence.md`. It is the entry the r79 staging note `Kb79S06AssimStaged.md` cross-checked.

`grep -n allowed-tools` on that entry returns one hit, line 14: "optional `license`, `compatibility`, `metadata`, `allowed-tools` (S255)". That is a field-list mention only. The entry contains no per-client `allowed-tools` semantics. It is silent on Claude Code, Factory, Microsoft, pi and Vibe.

Verdict on adjacency: the overlap with C2 is named. The staged entry absorbed nothing from C2. C2's rows (S226–S231) are not copied, and no shokuknow row was copied into kotoba.

## 3. Claim-by-claim cross-check against live pages

Fetched read-only with `curl -sSL` (user-agent `Mozilla/5.0 (kotoba-r80-readonly)`), 2026-10-27. Page files are in the scratch dir and their sha256 values are in the receipt. "Live" means the bytes I fetched now.

| # | Staged claim (entry lines) | Live check | Result |
|---|---|---|---|
| 1 | Spec canonical frontmatter list includes optional `allowed-tools` (lines 12–15, cites S255) | `https://agentskills.io/skill.md`, line 18: "Contains YAML frontmatter (`name`, `description`, optional `license`, `compatibility`, `metadata`, `allowed-tools`)". Line 48 table row: "Pre-approved tools the skill may use (experimental)". Size 16035 B, matching the row. | AGREE |
| 2 | Deep Code marks `name` and `description` Recommended; missing `name` → directory name with `_`→`-` (lines 14–16, S250) | `https://deepcode.vegamo.cn/en/docs/configuration/agent-skills`, SKILL.md Frontmatter table: `name` Recommended, "If missing, Deep Code uses the directory name and converts `_` to `-`". `description` Recommended. | AGREE |
| 3 | Deep Code `metadata.allow-implicit-invocation` "excludes" a skill (lines 17–18) | Same page: "When set to `false`, the skill is excluded from automatic matching but can still be selected manually." | AGREE (the entry's word "excludes" is a paraphrase of this) |
| 4 | Junie `name` required, `description` optional (lines 19–20, S252) | `https://junie.jetbrains.com/docs/agent-skills.html`, Frontmatter fields: `name` String Yes, `description` String No. | AGREE |
| 5 | Deep Code five-rank scan order and precedence quote (lines 42–45) | Same page, Scan Locations: 1 `./.deepcode/skills/`, 2 `./.agents/skills/`, 3 `~/.deepcode/skills/`, 4 `~/.agents/skills/`, 5 built-in. "If multiple skills resolve to the same name, only the highest-priority one is kept." | AGREE |
| 6 | Junie project-level skill wins over user-level; user-level is ignored (lines 46–47, 53–55) | Junie page: "the project-level skill takes precedence and the user-level skill is ignored." | AGREE |
| 7 | Junie `--skill-default-locations false` switches default locations off, `.agents/skills/` included (lines 48–50) | Junie page: default project and user locations "including the `.agents/skills/` directories — can be disabled with `--skill-default-locations false`". | AGREE |
| 8 | Junie `--skill-location` / `config.json` custom folders (line 47) | Page has a "Skill locations and configuration" section and `config.json` appears in the page. I did not read the exact clause. | NOT FULLY VERIFIED |
| 9 | Kiro has only `.kiro/skills/` and `~/.kiro/skills/`, with no `.agents` root (lines 50–51, S251) | Kiro page (`https://kiro.dev/docs/skills/`, 310883 B): the scope table lists only `.kiro/skills/` (Workspace) and `~/.kiro/skills/` (Global). The string `.agents` does not occur. | AGREE, scoped to what the page states |
| 10 | Kiro workspace skill overrides global on a name collision (lines 53–55) | Kiro page: "When skills share the same name, workspace skills take priority over global skills." | AGREE |
| 11 | Lenient validation: warn-and-load for name mismatch and length; skip only when description is missing or YAML unparseable (lines 25–31, S256) | `https://agentskills.io/client-implementation/adding-skills-support.md` (20446 B): "Name doesn't match the parent directory name → warn, load anyway", "Name exceeds 64 characters → warn, load anyway", "Description is missing or empty → skip", "YAML is completely unparseable → skip". The quotes "defines strict constraints on the `name` field" and "deliberately relaxes these to improve compatibility with skills authored for other clients" also match. | AGREE |
| 12 | Design advice: keep the description under 1024 characters (line 64) | Spec `description` row: "1-1024 chars, non-empty"; MS page: "Max 1024 characters". | AGREE |
| 13 | "No client yet has been found that states a rule covering a native and a shared root in the same project scope" (lines 56–59) | Deep Code's own page, which the entry cites, lists rank 1 `./.deepcode/skills/` (native, Project) and rank 2 `./.agents/skills/` (shared, Project). One rule covers both: "only the highest-priority one is kept." The entry itself describes this rule as "keeps the highest-priority scan rank" (line 54). | DISAGREE. The entry contradicts its own S250 citation. Junie's page does not state a native-vs-shared precedence within project scope, so the disagreement rests on Deep Code. |

Summary of claims: 10 agree, 1 partly verified (row 8), 1 scoped agreement (row 9), 1 disagreement (row 13). The one disagreement is internal to the entry and bears on its own design claim. It does not touch `allowed-tools`.

## 4. The six C2 pages (cross-check of the S226–S231 rows)

The staged entry does not cite these, so the table below is my independent check of the rows C2 depends on. It is not a re-open receipt; `Kb80ReopenSix` owns that. Here "sha" means the sha256 of the bytes I fetched by the bare URL.

| Row | Page (fetched URL) | Size B (row / live) | sha256 (row / live) | allowed-tools semantics seen live |
|---|---|---|---|---|
| S226 | agentskills.io/specification.md | 7608 / 7608 | match (9a67de89…) | optional, "Experimental. Support for this field may vary" |
| S227 | code.claude.com/docs/en/skills.md | 117962 / 117962 | match (31623035…) | per-turn grant; "It does not restrict which tools are available" |
| S228 | docs.factory.com/harness/skills (assigned URL redirects here) | 17567 (.md route) / 341384 (HTML) | not comparable: the row hashes the `.md` route, I fetched the HTML route | metadata for review; "is not a runtime sandbox" |
| S229 | learn.microsoft.com/en-us/agent-framework/agents/skills | 157339 / 157339 | **MISMATCH**: row 34016233…, live 20fd76d8… | space-delimited list, "Experimental" |
| S230 | raw.githubusercontent.com/badlogic/pi-mono/.../skills.md | 4793 / 4793 | match (5b980552…) | "Experimental pre-approved tool list" (label only) |
| S231 | raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md | 77634 / 77634 | match (fc48a5db…) | YAML block list; no semantics; defers to the spec |

S229: the size is identical and the hash differs. The fetch route is the same as the row's URL, but I cannot establish why the bytes differ. Recommend `Kb80ReopenSix` re-fetch and record the route. Do not treat the row as verified until that is done.

S228 URL of record: the r79 staging note (`Kb79S06AssimStaged.md`) gives `docs.factory.ai/cli/configuration/skills`. That URL redirects to `docs.factory.com/harness/skills`. The row's canonical URL is correct. The r79 note should not be cited as the URL of record.

## 5. Per-client `allowed-tools` semantics elsewhere in shokuknow (outside the named entry)

These are not the named staged entry. They are reported because they overlap C2's semantics territory.

- `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/chinese-client-skill-surfaces.md:34-35` says "wave 1 established that Qwen Code reads `allowedTools` and **ignores** `allowed-tools`". This is a stronger per-client claim than the kotoba record. kotoba's `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md:66` says "The Qwen Code tool-allowlist trap is not carried here". It records that the Qwen English page says only that an `allowed-tools` field written for another agent "is ignored". I did not fetch the Qwen page (not one of the six). Status: unverified in this seat, with a documented disagreement between the two lanes.
- `skill-body-authority-and-enforcement.md:33-34` repeats the `allowedTools` reading.
- `japanese-client-layer-round8.md:26` (S295 Claude Japanese page) says invoking a skill runs its `allowed-tools` without a further prompt. This agrees with live S227.
- `client-surface-census-extension.md:45` makes a generic remark about foreign `allowed-tools` fields. No semantics asserted.

## 6. Id-namespace collision (material for the C2 frontier)

`/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` reuses ids that kotoba's `corpus/SOURCES.md` already holds for different sources:

- Overlapping ids: S203 through S231 (29 ids) appear in both files. Same id, different URL. Examples: S226 is TRAE in shokuknow and the Agent Skills specification in kotoba. S228 is a Claude zh-TW page in shokuknow and Factory in kotoba. S231 is the agentskills description-optimizing page in shokuknow and Mistral Vibe in kotoba.
- kotoba's `corpus/SOURCES.md` has 157 rows, with a maximum id of S231.
- shokuknow's append file runs S203 through S390 and beyond (188 unique ids in the file). It holds S232 (Agent Skills best practices), S240 (arXiv AGENTS.md), S250 (Deep Code), S255 (skill.md) and others.
- The staged entry's ids S250, S252, S255 and S256 are unused in kotoba. They are shokuknow-namespace ids.

Consequence: C2's planned rejection rows "from S232" would collide with shokuknow's S232–S299 range on merge. Any merge must renumber, or keep an explicit id map, before the S232+ rows are minted. I have not minted any id. Candidate rejection rows (for example, the Qwen `allowedTools` claim in section 5) need a fresh kotoba id once the collision is resolved.

## 7. Frontier (C2) — what this seat recommends

1. Mint S232+ rejections only after the id collision with shokuknow's append file is resolved (section 6).
2. Re-open S229 and record the fetch route. The live hash differs from the row (section 4).
3. Verify the Qwen `allowedTools` claim live, or leave it out of C2. It is a candidate rejection row, not an absorbed one (section 5).
4. Repair the staged entry's row-13 claim before any merge. As written it contradicts its own S250 citation (section 3).

## 8. Absorbed / changed

- Absorbed from shokuknow: nothing.
- Lane files changed: none. The only write is the receipt `.ufo/waves/round-80/build/Kb80K01-receipts.txt` and this report.
- Tools installed or upgraded: none.
- Scratch: `/fast/scratch/hyaku/kotoba-r80/Kb80K01Overlap/` (pages and sweep output). Removed before yield.

VERDICT: Overlap named, absorbed nothing. The sibling sweep returns 0 hits over 1032 files. The staged entry's sole `allowed-tools` content is a field-list mention that is confirmed live. One of its claims contradicts its own Deep Code citation. The shokuknow id namespace collides with kotoba's S203–S231 and would collide with planned S232+ rejections.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80K01Overlap.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80K01-receipts.txt
