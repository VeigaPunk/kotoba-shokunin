# ConnSourcesCross — cross-source pattern scan (round 72 wave 1)

Seat: ConnSourcesCross (leaf, read-only). Scope: staged rows cited by the two assimilation
entries — `skill-vs-always-on-boundary.md` (staged S261 S262 S263 S264) and
`context-rot-and-always-on-context.md` (staged S248 S254 S255 S256) — versus the lane registry
`corpus/SOURCES.md` (base `c69711e`) and the knowledge entries it holds. No file modified.
Staged package: `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` (read-only).

## Verdict

**All eight staged rows are new URLs to the lane registry (grep count 0 each) except S256,
whose document is already held as S002 under a URL spelling without the `.md` suffix. None of
the eight would add a census W04 duplicate-URL warning under the current normalizer. Two of the
eight (S248, S256) rest on URLs that the lane's own quarantine ledger previously refused
(payload-absent) — those refusals must be resolved before the rows can ground C1-A4.**

## Commands and observed output

Census baseline (re-run, read-only, exit 0, 20 W04 — matches committed `census-before.txt`):

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S207 duplicate url opencode.ai/docs/skills across scopes
kotoba	W04	S208 duplicate url learn.microsoft.com/en-us/agent-framework/agents/skills across scopes
kotoba	W04	S212 duplicate url agentskills.io/skill-creation/evaluating-skills.md across scopes
kotoba	W04	S213 duplicate url agentskills.io/skill-creation/optimizing-descriptions.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
```

URL holder check per staged row (`grep -n '<host+path>' corpus/SOURCES.md`):

| staged id | staged URL (host+path) | grep pattern | result |
|---|---|---|---|
| S248 | vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals | `vercel\.com/blog/agents-md` | no matches (count 0) |
| S254 | research.trychroma.com/context-rot | `trychroma\.com` | no matches (count 0) |
| S255 | agentskills.io/skill.md | `agentskills\.io/skill\.md` | no matches (count 0) |
| S256 | agentskills.io/client-implementation/adding-skills-support.md | `client-implementation/adding-skills-support` | 1 match: **S002** (line 15), URL without `.md` |
| S261 | docs.letta.com/letta-code/skills/ | `letta\.com` | no matches (count 0) |
| S262 | docs.factory.ai/cli/configuration/skills | `factory\.ai` | no matches (count 0) |
| S263 | raw.githubusercontent.com/badlogic/pi-mono/.../skills.md | `pi-mono` | no matches (count 0) |
| S264 | hermes-agent.nousresearch.com/docs/user-guide/features/skills | `nousresearch\.com` | no matches (count 0) |

Registry rows holding `agentskills.io` URLs: S001, S002, S018 (specification, specification,
specification supersede), S209, S210, S212, S213 (skill-creation pages). None holds
`agentskills.io/skill.md`.

## Per-row findings

- **S248 (Vercel eval)** — URL not held. *Cross-source conflict:* the lane's quarantine ledger
  (`assimilation/quarantine-slice-full.txt` line 3) records a round-5 refusal **S168** for this
  exact URL with verdict `payload-absent`: "cited source, companion URLs and local artifacts were
  all checked; the quote is in none of them". The staged row re-mines the same URL with new
  quotes ("In 56% of eval cases, the skill was never invoked."; 100% vs 79%). The refusal and
  the staged row cannot both stand: before S248 can ground A4, the L1 must re-fetch the page and
  pin a sha256 snapshot containing the quote (A4(d) already demands this for cited rows).
- **S254 (Chroma context-rot)** — URL not held; no prior refusal; new aspect (degradation-curve
  measurement) absent from all held rows.
- **S255 (agentskills.io/skill.md one-pager)** — URL not held; distinct document from held
  S001/S018 (specification). Adds the cross-client discovery convention + per-skill token cost
  together, a combination no held row carries.
- **S256 (adding-skills-support.md)** — *same document already held as S002* (same host+path,
  S002's URL has no `.md` suffix). Claim overlap: S002 already teaches the lenient-validation
  policy ("lenient clients warn and load anyway on name mismatch"); staged S256 adds the
  three-tier token budgets (~50–100 catalog / <5000 instructions) and behavioural-instruction
  blocks. Not an exact duplicate, not a contradiction — a deeper cut of the same page.
  **Provenance defect:** staged S256's scope cell cites "the round-4 row S164" — no S164 exists
  in the registry (grep 0; `reg-ids` has none); the round-4 row for this URL in the quarantine
  ledger is **S167** (refused, payload-absent). The S164 reference is dangling and must be
  corrected or dropped.
- **S261 (Letta)** — URL not held; adds a three-scope model (project / agent-scoped MemFS /
  computer) + portability claim naming four compatible agents; no held row carries either.
- **S262 (Factory Droid)** — URL not held; carries the decision-boundary sentence the new rung
  rule (A4) leans on; no held row states it.
- **S263 (pi-mono)** — URL not held; second-vendor statement of the same boundary, naming the
  three rungs (prompt template / skill / executable integration); new.
- **S264 (Hermes Agent)** — URL not held; house authoring standard with ≤60-char description
  limit vs the specification's 1024; new.

**Contradictions:** S248 vs quarantine refusal S168; S256's "S164" reference vs no such row
(and vs refusal S167/S176 for the same URL). **Supersessions:** none of the eight supersedes a
held row. **Exact duplicates:** none byte-exact.

## W04 impact

Current registry: 20 W04 warnings. The normalizer (`sources-census.sh` `url_of`, lines
600-605) strips scheme, fragment and trailing slash but **not** a `.md` suffix. Therefore none
of the eight staged URLs normalizes equal to a held URL: S256's `...adding-skills-support.md` ≠
S002's `...adding-skills-support`. **Appending all eight adds 0 new W04.** Caveats:
(1) staged S247 and S256 (both in the append, same `.md` URL, different scope prose) would add 1
W04 if both are appended; (2) if the normalizer ever strips `.md`, S256 would become an E04
against S002 (same scope, non-rejected, teaches carries no `supersedes`), so the L1 should
prefer citing the held S002 or matching its URL spelling.

## Held rows the new rung rule (C1-A4) leans on

Registry rows (SOURCES.md line numbers) and the knowledge entries that hold them:

- **S123** (line 134) — OpenAI Model Spec ladder; "Instructions with higher authority override
  those with lower authority."; used by `instruction-authority-ladder-round67.md` (line 1).
- **S129** (line 136) — Many-Tier hierarchy; fixed few-level models inadequate, ~40% frontier
  accuracy; used by `instruction-authority-ladder-round67.md` (line 3).
- **S198** (line 139) — VT Code: "Skill content is untrusted resource data; host tool and
  sandbox policy remains authoritative."
- **S199** (line 140) — Parallel Works: two independent gates; model invocation can never grant.
- **S200** (line 141) — Kilo Code: embedded commands execute only from trusted locations.
- **S201** (line 142) — Microsoft Agent Framework: "Agent Skills should be treated like any
  third-party code"; approval by default.
- **S202** (line 143) — Mistral AI Vibe: "Standard Agent Skills path (project root, trusted
  folders only)".
- **S203** (line 144) — Roo Code: "Project skills override global skills, mode-specific override
  generic".
- **S204** (line 145) — Amp: "Local skills mask repository skills with the same name."
- **S205** (line 146) — Deep Code: "only the highest-priority one is kept".
- **S206** (line 147) — Junie: "the project-level skill takes precedence and the user-level
  skill is ignored."
- **S207** (line 148) — opencode V1: "Ensure skill names are unique across all locations".
- **S208** (line 149) — Microsoft Agent Framework: "All three skill tools require approval by
  default."; supersedes S201's anchor.

S198–S202 and S208 are held by `client-trust-gates-round68.md` (lines 1-6); S203–S207 by
`skill-name-precedence-round69.md` (lines 1-5); S123/S129 by `instruction-authority-ladder-round67.md`
(lines 1,3). All three entries exist at base and carry `source:` lines naming those ids —
satisfying C1(b)/(c) for A1–A3. The A4 entry (`corpus/knowledge/resident-index-and-rungs-round72.md`)
does not exist yet (grep 0), as expected; its cited rows are the staged S248/S254/S255/S256/
S261/S262/S263/S264, none of which is in the registry yet, so A4's `used-by`/`source:` closure
cannot be completed until the staged rows are appended (renumbered where needed) — see below.

## Id-collision note (adjacent to the eight)

The staged package reuses ids S203–S213 that already exist as registry rows (collisions file
lists S203–S213). The eight rows scanned here (S248, S254–S256, S261–S264) are > S213 and are
free in `reg-ids`, so they need no renumbering; the earlier staged block does. Also note the
staged S255 scope cell's claim "the only first-party place the lane holds…" presupposes its own
append and is not a statement about the current state.
