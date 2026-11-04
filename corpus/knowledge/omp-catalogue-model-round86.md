source: S255 — omp 18.15.0 embedded TypeScript (bun bundle inside `/home/vgpnk/.local/bin/omp`, 276 785 328 B, sha256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`; upstream `github.com/can1357/oh-my-pi` tag `v18.15.0`, HTTP 200) — modules `extensibility/skill-descriptions.ts`, `extensibility/skills.ts`, `discovery/*.ts`, `capability/index.ts` — read in place with python `mmap` + `re`, nothing copied out (fetch record `.ufo/waves/round-86/w1/ScribeSources/fetch-record.txt`; located root quotes `.ufo/waves/round-86/w1/ScoutRootsSource/source-packet.md`)
verified-at: 2026-11-04
recheck: on-release — on any omp upgrade, `omp --version` and `sha256sum ~/.local/bin/omp` must print `omp/18.15.0` and the digest above; otherwise re-locate every quote below in the new ELF (byte offsets drift across builds; minified names do too) and re-run the counter in § 4.
ground: S255's source is the code that renders this host's `<skills>` catalogue; the counter in § 4 reproduces all 215 lines of a real 18.15.0 catalogue from that reading. This note describes omp 18.15.0 on this Linux host at the default settings recorded below, not other builds or other configurations.

# The omp catalogue model, re-derived against omp 18.15.0 (round 86)

Byte offsets are 0-based positions of the quoted bytes in the pinned ELF. The bundle is
minified: function names (`dnt`, `A`, `O`, `Dp`, `Ba`) are this build's, not stable
identifiers. Each quote has 25 words or fewer and is the exact ELF text at the stated offset.

## 1. What omp 18.15.0 renders per skill

The catalogue template is still `- {{name}}: {{description}}` inside `<skills>` (offset
273944362; `<skills>` at 273944336). The `description` slot is filled per skill by
`render` in `extensibility/skill-descriptions.ts` (module header at 178767936):

| step | located source line | offset |
|---|---|---|
| constants | `var k = 100;` · `var E = 40;` · `var T = 160;` · `var _ = 12;` | 178768292 · 178768305 · 178768317 · 178768330 |
| cache key `A` | `.update(v).update("\x00").update(e.name)` (then `.update("\x00").update(e.description)`; `v` = the embedded `compress-description.md` prompt) | 178770025 |
| cache lookup | `o = t?.get(n);` | 178774093 |
| miss → preview | `o = dnt(r.description);` | 178774255 |
| preview: whitespace collapse | `const t = e.replace(/\s+/g, " ").trim();` | 178770140 |
| preview: ≤ 100 verbatim, else cut | `const r = t.slice(0, k - 1);` | 178770218 |
| preview: first sentence | `const n = r.match(/^.*?[.!?](?=\s|$)/)?.[0];` | 178770249 |
| preview: kept only if ≥ 40 | `if (n && n.length >= E)` | 178770296 |
| preview: word cut, floored at 40 | `const c = o >= E ? r.slice(0, o).trimEnd() : r;` | 178770368 |
| preview: ellipsis | ``return `${c}\u2026`;`` | 178770418 |
| compressor acceptance `O` | `if (!t \|\| /[\r\n]/.test(t) \|\| t.length > T)` · `if (t.split(/\s+/).length > _)` | 178770481 · 178770544 |

(In the table `\|` is a Markdown escape; the ELF bytes have a bare `|`.)

So each line is `- name: render`, where render is:

1. **The cached one-liner**, if the store holds a row under key
   `sha256(prompt ‖ 0x00 ‖ name ‖ 0x00 ‖ description)`. `description` is the frontmatter
   string as loaded, and `A` does no whitespace normalisation. A row is written only if the
   model's output passes `O`: one line, ≤ 160 chars, ≤ 12 words.
2. **Otherwise the deterministic preview `dnt`**: collapse whitespace; if ≤ 100 chars, keep it
   verbatim; else take `r` = the first 99 chars. If the first `.`/`!`/`?` sentence in `r` is
   ≥ 40 chars, return it with no ellipsis. Else cut `r` at its last space only when that space
   sits at index ≥ 40, otherwise keep all of `r`, then append `…`. Lengths are UTF-16 units.

Two details are absent from the earlier lane statements in § 3: the **40-char floor on the word
cut**, and the **model-keyed fallback row**. When compression returns an unusable line, omp stores
the *preview* under `` `${key}:${modelKey}` `` (`e.put(u, dnt(r.description));`, offset
178775605, inside `#r`). That stops the same model from retrying; the row never serves a
render, because `render` looks up the bare key. In the round-86 fixture, 186 of the 228 cache
rows are such `…:anthropic/claude-haiku-5-5` rows and 42 are bare-key rows.

Cache location: `P(e)` → `axt(e)` = `c.agentSubdir(p, "skill-descriptions.db", "data")` (offset
166896000). The data dir is `$XDG_DATA_HOME/omp` only when that directory exists; otherwise it
is the agent dir. A legacy `<agentDir>/skill-descriptions.db` is adopted by `VACUUM INTO`
(`N(g.join(e ?? we(), "skill-descriptions.db"), t);`, offset 178771285). On this host
`XDG_DATA_HOME=/home/vgpnk/.local/share` but `~/.local/share/omp` does not exist, so the store
is still `~/.omp/agent/skill-descriptions.db` (86 016 B, mtime 2026-10-31 19:08).

## 2. Which roots omp reads, in what order and precedence

Entry point `Dp` (export alias `loadSkills`) in `extensibility/skills.ts` (header 177495678).
It collects every provider registered for the `skills` capability. Providers run in priority
order; ties keep registration order (`const s = r.findIndex((o) => o.priority < t.priority);`,
172771631). Each root is scanned one level deep by `Ba` (`<root>/<name>/SKILL.md`, dot
entries skipped, dir or symlink accepted). Full located table:
`.ufo/waves/round-86/w1/ScoutRootsSource/source-packet.md`.

| priority | provider | roots | default on this host |
|---|---|---|---|
| 100 | native | `{cwd}…/.omp/skills` (walk-up to git root), then `~/.omp/agent/skills` | on (`enablePiProject`/`enablePiUser` default true) |
| 95 | skillshare | lock-driven `skills.lock.json` installs | on; no lock file on host |
| 90 | omp-plugins | `<pkg>/skills` of each installed plugin under `~/.omp/plugins/node_modules` (`dir: Zo.join(R.path, "skills"),`, 173914936) | on |
| 80 | claude | `{cwd}…/.claude/skills` on; `~/.claude/skills` | user root **off** (`id: "skills.enableClaudeUser", type: "boolean", default: false`, 172765316) |
| 75 | agent-plugins | `<root>/skills` of plugin roots with a valid `plugin.json` | on; none on host |
| 70 | claude-plugins · agents · codex | marketplace plugins (Claude-origin user roots opt-in); `{cwd}…/.agent/skills`, `{cwd}…/.agents/skills`, `~/.agent/skills`, `~/.agents/skills`; `{cwd}/.codex/skills`, `~/.codex/skills` | agents on; codex user **off** (`id: "skills.enableCodexUser", type: "boolean", default: false`, 172765236) |
| 55 | opencode | `{cwd}/.opencode/skills`; `~/.config/opencode/skills` | user root **off** (opt-in `zi("opencode")`) |
| 30 | github | `{cwd}/.github/skills` | on |
| after all | custom | `skills.customDirectories` (default `[]`) | none configured |
| 5, last | managed | `~/.omp/agent/managed-skills`, only for names no enabled provider has | on; absent on host |

Precedence is **not first-root-wins**. A SKILL.md whose realpath was already accepted is
skipped. A same-name copy with identical body and frontmatter is dropped. A same-name copy with
different content is **kept, renamed** `<ns>/<name>` (`let re = `${_}/${x.name}`;`, 177497593).
A custom-directory skill displaces an earlier one instead (177497011). The final list is sorted
by name, case-insensitively first (`Et.sort((et, Ye) => dne(et.name, et.filePath, Ye.name, Ye.filePath));`,
177505946). A skill with `hide: true` or `disableModelInvocation: true` is discovered but not
rendered (178835365).

Host state (read-only, ScoutRootsSource § Host state): `~/.omp/agent/config.yml` has no
`skills`, `extensions`, `enabledProviders` or `disabledProviders` key, so every gate is at its
default. The fleet cwd `/home/vgpnk/Projects/shokunin` is its own git root and holds no project
skills dir. The 215-line catalogue is therefore `~/.agents/skills` (83) +
`~/.omp/plugins/node_modules/ecc-pi-core/skills` (132), with 0 shared names.

The lane's model after C1 (`verifiers/verify_harness_claims.py`, sha256 `bd793b6c…2b30ab7`)
lists `WALKUP_REL` = `.omp`, `.claude`, `.agent`, `.agents`, `.codex`, `.opencode` and
`.github` `/skills` (cwd only, which equals the walk-up at a repo root). Its `USER_ROOTS` are
`~/.omp/agent/skills`, the omp-plugin `<pkg>/skills` roots, `~/.agent/skills`,
`~/.agents/skills` and `~/.omp/agent/managed-skills`. Every root is cited in
`verifiers/omp-skill-roots.tsv` (sha256 `36021309…c7c7800`, header
`root_pattern<TAB>binary_quote`, 12 rows):

| root_pattern | binary_quote |
|---|---|
| `{cwd}/.omp/skills` | Native OMP configuration from ~/.omp and .omp/ |
| `{cwd}/.claude/skills` | Load skills from .claude/skills/*/SKILL.md |
| `{cwd}/.agent/skills` | Load skills from .agent/skills and .agents/skills (project walk-up + user home) |
| `{cwd}/.agents/skills` | Load skills from .agent/skills and .agents/skills (project walk-up + user home) |
| `{cwd}/.codex/skills` | Load skills from ~/.codex/skills and .codex/skills/ |
| `{cwd}/.opencode/skills` | Load skills from ~/.config/opencode/skills/ and .opencode/skills/ |
| `{cwd}/.github/skills` | Load skills from .github/skills/*/SKILL.md |
| `~/.omp/agent/skills` | Native OMP configuration from ~/.omp and .omp/ |
| `~/.omp/plugins/node_modules/*/skills` | var Gh = ".omp"; |
| `~/.agent/skills` | Load skills from .agent/skills and .agents/skills (project walk-up + user home) |
| `~/.agents/skills` | Load skills from .agent/skills and .agents/skills (project walk-up + user home) |
| `~/.omp/agent/managed-skills` | Auto-generated managed skills from ~/.omp/agent/managed-skills |

Where the model simplifies omp: it keeps first-root-wins (`offered.setdefault`) where omp
namespaces a differing same-name copy. The two agree on a host whose duplicates are all the same
file. The model also leaves out skillshare, claude-plugins, agent-plugins and custom
directories, none of which contributes a line here. The ledger proves that each quote is
*located* in the ELF, not that it is the code that reads the root. For example, the plugin row
cites the config-dir constant `var Gh = ".omp";`, not the `uie` scan line quoted in the table
above.

## 3. What changed since the lane last looked

Pointers are file:line in the working tree on 2026-11-04 (SKILL.md lines ≥ 522 are one line
below base `e5d966b`; `verify_harness_claims.py` lines are at base `e5d966b`, since C1 rewrites
that file). These files are not edited here; the L1 adds errata.

| file:line | earlier claim (quoted) | verdict | omp 18.15.0 evidence |
|---|---|---|---|
| `SKILL.md:28-29` | "`cache.get(key) ?? previewSkillDescription`: a cached LLM one-liner if the async compressor landed" | **holds** | `o = t?.get(n);` (178774093) then `o = dnt(r.description);` (178774255); a per-session memo map sits in front |
| `SKILL.md:29-30` | "a deterministic prefix cut (round-85 source: `k=100`, `slice(0,k-1)`…), plus last-space/`…` fallback" | **changed** (incomplete) | the last-space cut is floored: `const c = o >= E ? r.slice(0, o).trimEnd() : r;` (178770368) |
| `SKILL.md:32` | "`~/.omp/agent/skill-descriptions.db`" | **holds on this host**, changed in general | path is `agentSubdir(…, "data")`, i.e. `$XDG_DATA_HOME/omp` when it exists (166896000); `~/.local/share/omp` absent here |
| `SKILL.md:32-35` | "**18 at round 13** … with **all 17 live keys still reproducing**" | **now-wrong** as present state (dated history) | fixture: 228 rows (42 bare-key, 186 `key:model` preview rows) |
| `SKILL.md:576-577` | "all 17 keys reproduce, newest catalogue 17/17 cache, 0 truncations" | **now-wrong** | newest catalogue has 215 lines; 151 renders end in `…` (fixture `entries`) |
| `verify_harness_claims.py:61` (base) | "Verified 2026-09-28 against the 17-name catalogue in this host's" | **now-wrong** | catalogue is 215 names; the base model reproduces 83 (§ 4) |
| `verify_harness_claims.py:63-68` (base) | `USER_ROOTS` = `.agents/skills`, `.omp/agent/skills`, `.config/opencode/skills`, `.claude/skills` | **now-wrong** | two of the four are off by default (`enableClaudeUser` default false; opencode user opt-in); the omp-plugin root that supplies 132 names is missing |
| `verify_harness_claims.py:69` (base) | `WALKUP_REL = [".agents/skills", ".agent/skills"]` | **changed** | project roots also include `.omp`, `.claude`, `.codex`, `.opencode`, `.github` (`dir: fr.join(k, Ou.projectDir, "skills"),`, 173819979) |
| `verify_harness_claims.py:375-376` (base) | "every line of the newest block must byte-equal a cached description" | **now-wrong** | a miss renders `dnt`; the plan counts 15 of 215 lines as cached (`plans/round-86.md:110`) |
| `corpus/knowledge/anatomy-and-compression.md:211` | "deterministic truncator (`_8n=100`; first sentence if ≥40 chars, else last-space cut + `…`)" | **changed** | value 100 holds (now `var k = 100;`); the word cut has the 40 floor; the listed `~/.claude/skills` root is off by default |
| `corpus/knowledge/anatomy-and-compression.md:215` | "sqlite3 -readonly ~/.omp/agent/skill-descriptions.db" | **holds on this host** | as `SKILL.md:32` |
| `corpus/knowledge/harness-router-models-round9.md:19-20` | "sqlite3 -readonly ~/.omp/agent/skill-descriptions.db" | path **holds on host**; count dated | 228 rows in the fixture |
| `corpus/knowledge/harness-router-models-round9.md:49` | "authority: readable embedded JS (A8n/H7s/ldl), round 10" | **changed** | this build names them `A`, `dnt`, `O` |
| `corpus/knowledge/harness-router-models-round9.md:69-73` | "`len <= _8n` (`_8n=100`) → verbatim … else cut at the last ASCII space + U+2026 `…`" | **changed** | values hold (`k`/`E`/`T`/`_` = 100/40/160/12); the word cut has the 40 floor |
| `corpus/knowledge/harness-router-models-round9.md:95` | "sqlite3 -readonly ~/.omp/agent/skill-descriptions.db" | **holds on this host** | bare-key and `key:model` rows now share the table |
| `corpus/knowledge/harness-verifier-round10.md:42` | "function H7s(e) { // previewSkillDescription" | **changed** | now `function dnt(e) {`, same module |
| `corpus/knowledge/harness-verifier-round10.md:48` | "const n = s.slice(0, s.lastIndexOf(" ")).trimEnd();" | **now-wrong** for 18.15.0 | `const c = o >= E ? r.slice(0, o).trimEnd() : r;` (178770368) |
| `corpus/knowledge/harness-verifier-round10.md:60-61` | "`nV.render` is exactly `cache.get(key) ?? previewSkillDescription` followed by a fire-and-forget `#o()` write" | **holds** in substance | `e1.render`: memo → `t?.get(n)` → `dnt`, then the async `this.#r(t, n, r)` |
| `corpus/knowledge/harness-verifier-round10.md:193-194` | "with 17/17 keys cached, no offered skill takes that path" | **now-wrong** | the preview path renders most lines (151 of 215 end in `…`) |
| `corpus/knowledge/render-mechanism-round7.md:15-16` | "`previewSkillDescription` (H7s), strings line 684191-684199, ELF region @177145052:" | **changed** | now `function dnt(e) {` at 178770120; offsets drift per build |
| `corpus/knowledge/render-mechanism-round7.md:20` | "Constants @177147479: `_8n=100, idl=160, adl=12`." | **changed** (names, offset); values **hold** | `var k = 100;` 178768292, `var T = 160;` 178768317, `var _ = 12;` 178768330 |
| `corpus/knowledge/render-mechanism-round7.md:26-27` | "key = `sha256(prompt_template \0 name \0 ws-normalised description)`" | **changed** | `A` hashes `e.description` as loaded; no whitespace collapse in `A` (178770025) |
| `corpus/knowledge/render-mechanism-round7.md:29-32` | "the render that misses the cache emits H7s … description field = `cache.get(key) ?? H7s(description)`" | **holds** (renamed) | `o = dnt(r.description);` (178774255); unusable compressions now write a `key:model` preview row |
| `corpus/knowledge/render-mechanism-round7.md:31` | "**Catalogue template** @283082932: `- {{name}}: {{description}}`" | template **holds**; offset changed | `- {{name}}: {{description}}` at 273944362 |
| `corpus/knowledge/frontmatter-trigger-surface.md:65-69` | "row exists in `~/.omp/agent/skill-descriptions.db` … first sentence wins if ≥40 chars, else last-space cut + `…`" | **changed** | the word cut has the 40 floor; path holds on host |
| `corpus/knowledge/frontmatter-trigger-surface.md:137` | "H7s is ~10 lines" | **changed** | the function is `function dnt(e) {` (178770120), 12 lines including braces |
| `corpus/knowledge/sibling-description-rewrites-round8.md:21-24` | "deterministic truncator `previewSkillDescription` (H7s): ws-collapse; if `len <= 100` keep; else `s = t.slice(0, 99)`" | **holds**, but the word cut that follows lacks the 40 floor → **changed** | 178770218, 178770368 |
| `corpus/knowledge/skill-activation-telemetry.md:36` | "the truncator is a deterministic `slice(0,99)` + last-space `…`" | **holds** in substance | as `SKILL.md:28-29`; floor as `SKILL.md:29-30` |
| `corpus/knowledge/claim-scope-audit-round9.md:72` · `claim-census-round12.md:79` | "sqlite3 -readonly ~/.omp/agent/skill-descriptions.db" | path **holds on this host**; the counts there are dated history | as `SKILL.md:32` |
| `corpus/knowledge/harness-router-models-round9.md:180` · `opencode-offer-trace-round8.md:292` | "17-name sets" | **out of scope** | these concern opencode's `init` sets, not omp |

## 4. Measured before → after

Counter (frozen predicate, `plans/round-86.md:46-48`; counter as amended before candidate data
in `plans/round-86-addendum-1.md`, sha256 `39a014f2f3142096b43031faedb0ea9819995fb2926138c3ebf2b194002e4520`):

    python3 -B verifiers/check_omp_catalogue_repro.py --rev <rev>

| model | rev | result | receipt |
|---|---|---|---|
| base | `e5d966b51494f4177868ad5f46806a204783ef6c` | `omp catalogue lines reproduced 83 of 215`; `guard G4 roots FAIL (1): verifiers/omp-skill-roots.tsv absent at the revision`; `exit=1` | `.ufo/waves/round-86/receipts/c1-K0-base-a1.txt` |
| candidate (scratch commit on `b9ee548`) | `903bd78e18c0dbb6d4013d9726d89dbe7c190bcd` | `guard G1 no-echo PASS` · `guard G2 provenance PASS` · `guard G3 fixture PASS` · `guard G4 roots PASS` · `omp catalogue lines reproduced 215 of 215` · `exit=0` | `.ufo/waves/round-86/w1/ExecModel/score.txt` |

The candidate files scored there have the same digests as the lane working tree
(`verify_harness_claims.py` `bd793b6c8edcb67ab59d9a310d151eb66fdb44fc1fbc57ad6bc74795a2b30ab7`,
`omp-skill-roots.tsv` `360213095b274d28d980b172a88216e9c74b7575f184227cc5b813875c7c7800`). The
landing-commit number is the L1's to record. Whether each ledger quote is the code that makes
omp read its root is assigned to non-author review (`plans/round-86.md:80-82`), and this note
does not settle it.
