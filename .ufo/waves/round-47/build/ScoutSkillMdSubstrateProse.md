verdict: 18.12.5 / 1.19.3 falsify two present-tense body claims (dead `~/.opencode/bin/opencode`; the `_8n`/`A8n`/`K7s` string anchors), leave the `message=init count` recipe unproductive and unverifiable without running opencode, expose two over-absolute tag/`<location>` claims, and confirm both sha pins byte-for-byte — while line 151 expires the moment C2 lands.

# Scout — SKILL.md body statements exposed to the 18.12.5 / 1.19.3 substrate

Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/SKILL.md` (525 lines), BASE
`c61a973b2e02e1ded169703ddcb06466f4edd8bd`. Read-only; no production file touched.
Report author: `MoriR22R.ScoutSkillMdSubstrateProse-9` (leaf seat). All line numbers are
BASE line numbers; `git -C . status --short SKILL.md` was empty at start (exit 0).

Substrate actually used (frozen snapshot, shas re-verified against `SHA256SUMS`, exit 0):

- `bin/omp-18.12.5` sha256 `fdbc8136…da798e7e`, 256 575 456 B, mtime
  `2026-10-21 03:30:38.135013187 -0300` — identical to the live `~/.local/bin/omp`
  (`omp --version` → `omp/18.12.5`, exit 0).
- `bin/opencode-1.19.3` (npx-cache ELF) sha256 `179ca421…d3ab7ee9`, 186 013 824 B —
  identical to `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode`
  (exit 0). Binary self-identifies `1.19.3` (`opencode-1.19.3.strings` byte 447 186,
  `var n="1.19.3"`).
- `strings -n 4` dumps beside them. Offsets below are byte offsets into the raw binary for
  hashing, and `file:line` for text pulled from the line-oriented `.strings` dumps.

Method: every candidate statement was located by literal grep, then adjudicated against the
18.12.5 / 1.19.3 artifacts — not against the plan's expectations. Where the artifact is
ambiguous I say so instead of choosing. `[INFERENCE]` marks a step not directly observed.

## 0. Version numbers in the body: none

There is **no literal omp or opencode version number anywhere in SKILL.md**. A grep for
`(omp|opencode)[ /-]?v?[0-9]+\.[0-9]+`, `1.19`, `18.12`, `2.0.26` returns only the session-file
count `5842` (line 438). The substrate identity in this file is carried by **paths + string
anchors + two shas**, so C1's prose exposure is not a version bump to edit; it is those four
classes of statement below. (The version pin itself lives in `verifiers/baseline.json`
`measured_against`, outside this file's body.)

## 1. The inventory (line, text, tense, verdict)

`P` = present tense; `H` = dated history. "Holds" means I re-derived it against the snapshot.

| # | Line(s) | Statement (abridged, exact substrings) | Tense | Verdict at 18.12.5 / 1.19.3 |
|---|---------|-----------------------------------------|-------|------------------------------|
| 1 | 13–15 | "the shokunin files are not in an omp skill discovery root, so their descriptions never reach the `<skills>` router" | P | **HOLDS.** No `.agent`/`.agents`/`.claude`/`.github` `skills/` dir exists in any ancestor of the lane (checked `/home/vgpnk/Projects/shokunin/kotoba-shokunin` → `/home/vgpnk`); neither `~/.agents/skills/kotoba*` nor `~/.claude/skills/kotoba*` exists (`ls`, exit 2). |
| 2 | 22–27 | "On **omp** the `<skills>` catalogue … shows each skill as `- name: render` … `slice(0, _8n-1)` cut with `_8n=100`" | P | **RENDER HOLDS, SYMBOL STALE.** The tag/shape are live (18.12.5 session system prompt: `<skills>` then `- create-toolset: …a class of static,…`, `- godspeed: …`, 10 lines). But 18.12.5's `skill-descriptions.ts` chunk is unminified: `var v = 100` (`omp-18.12.5.strings:1066684`), `function xze(e)` (`:1066738`) = `if (t.length <= v) return t; … t.slice(0, v - 1)`. `_8n` exists only as base64/native noise (`_8n]nF`, `u"_8nR`, `H`@_8nK). |
| 3 | 28 | cache "`~/.omp/agent/skill-descriptions.db`" | P | **HOLDS.** File exists (12 288 B, +`-shm`/`-wal`); code resolves `join(e ?? Se(), "skill-descriptions.db")`; `Se()` is the agent dir (same function that resolves user-level `SYSTEM.md`). |
| 4 | 41–42 | "On **opencode** the `<available_skills>` catalogue renders the full `description` byte-for-byte plus `<location>` — no cliff." | P | **HOLDS for the v1 path; AT RISK globally.** 1.19.3 `SystemPrompt.skills` (anchor literal `skills:s.fn("SystemPrompt.skills")`, `opencode-1.19.3.strings:443883`) calls `_l.fmt(h,{verbose:!0})`; `fmt` = `oA` (anchor `function oA(j,J)`) emits `<skill><name><description><location>` and filters `description===undefined`. **But** 1.19.3 also carries a v2 `@opencode/v2/SkillGuidance` prompt section (anchors `class t_ extends KH.Service()("@opencode/v2/SkillGuidance")`, `XH.Key.make("core/skill-guidance")`) whose `Yf` renderer (anchor `Yf=(H)=>`) emits `<available_skills>` with **name+description only (no `<location>`)** and an update line "The available skills have changed. This list supersedes the previous available skills list." Which path this host's 1.19.3 injects is **unresolved** (I did not run opencode). Dump line numbers are unusable here (multi-MB lines), so anchors are literal strings; the dump itself is content-addressed by `SHA256SUMS`. |
| 5 | 79 | census "(round 22; sha256 `e046a0252cc96f17…` pinned there)" | P | **HOLDS.** `corpus/knowledge/instruction-surface-census-round13.md:328` records `body sha256 e046a0252cc96f173d148b419b7856e23fe789659cf02bc5b3237e8da26114f5` (`sed`-canonical, trailing newline). Whole-file sha is `1930ec04…` — so the literal is the absorbed body block, not the file. Minor wording: SKILL.md says "table … sha256"; the census says "body sha256". Not substrate-caused. |
| 6 | 89–90 | "Two harnesses … neither shares the other's catalogue tag" | P | **AT RISK / over-absolute.** opencode 1.19.3 has **zero** `<skills>` literals (grep `-c`, 0) — that half holds. omp 18.12.5's ELF contains **both** an `<available_skills>` + `<location>` template (`omp-18.12.5.strings:2413743–2413751`) and the `<skills>` bullet template (`:2423496–2423500`). Session evidence says the active omp catalogue is `<skills>` (see Counterexamples), so the *prediction* holds but the *artifact-level exclusivity* does not. |
| 7 | 91 | omp row: "`<skills>` (ELF template)"; "`_8n=100`"; roots "`~/.agents/skills`, `~/.omp/agent/skills`, `~/.claude/skills`, project walk-up" | P | **TAG/RENDER/ROOTS HOLD; SYMBOL STALE.** Roots trace at 18.12.5: `mte` loads `Gj(u,"skills")` + `Uj(u,"skills")` over `var HO=[".agent",".agents"]` (walk-up + home, `:19721157`), plus the provider `join(Se(),"skills")` = `~/.omp/agent/skills` (same `Se()` as the db). `.claude/skills` is a separate provider; `.github/skills` also exists. `_8n` stale as in row 2. The list omits `.agent/skills` (singular) and `.github/skills`. |
| 8 | 92 | opencode row: "`fmt(list,{verbose:true})`", "full … + `<location>` … no truncation, no cache", "last-parsed-wins under unbounded parse concurrency", "missing `description` is filtered", "a denied `skill` permission omits the whole block" | P | **HOLDS at 1.19.3.** `oA` filter + `<location>` (anchor `function oA(j,J)`); duplicate path = `if(j.skills[z.data.name]) yield logWarning("duplicate skill name",…); j.skills[z.data.name]={…}` — warning then **unguarded** assignment (anchor literal `duplicate skill name`); `{concurrency:"unbounded"}` present (anchor literal); `SystemPrompt.skills` starts with `if(de.disabled(["skill"],i.permission).has("skill"))return`. Caveat = row 4's v2 renderer. |
| 9 | 95–96 | `sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*) from skill_descriptions;"` | P | **HOLDS** (path + table name appear in 18.12.5 code and live db). |
| 10 | 102–103 | "`grep -o 'message=init count=[0-9]*' ~/.local/share/opencode/log/opencode.log`" | P | **UNPRODUCTIVE at BASE, not proven stale.** The log exists (922 614 B) but its mtime `2026-10-20 07:52` **predates** the pinned 1.19.3 ELF (`18:33`), and `message=init count` matches **0** lines. The contiguous literal `init count` is also absent from the 1.19.3 dump (0), but minified template concatenation makes absence weak evidence. Cannot resolve without running opencode, which this lane forbids. |
| 11 | 109–110 | "the omp key prefix read out of the ELF (`omp.elf.template_sha256`, 273 B)" | P | **HOLDS EXACTLY.** Raw `bin/omp-18.12.5` offset 252 816 008, 273 B starting "Compress into one routing hint…" → sha256 `c1f03c8e248eb40ec7735baab67f686f…`; next byte is NUL, template ends `Description: {{description}}\n`. Validators `var x = 160`, `var P = 12` intact (`:1066685–6686`). |
| 12 | 112–114 | "<available_skills> hits" as a check | P | **HOLDS.** `verify_harness_claims.py` `CHECKS` contains `oc.log.available_skills_hits`, `oc.log.skills_tag_hits`. |
| 13 | 131–138 | "cache-or-truncate" / "`sha256(prompt ‖ 0x00 ‖ name ‖ 0x00 ‖ loader-held description)`" / opencode "full description" | P | **HOLDS.** `function D(e){ return new Bun.CryptoHasher("sha256").update(w).update("\x00").update(e.name).update("\x00").update(e.description)… }` (`:1066736`), `w` = the 273-B prompt; `render(e)`/`snapshot(e)` do `this.#t.get(D(t)) ?? xze(t.description)`. No minified symbol named. |
| 14 | 151 | "This file's own description still carries `<skills>`; the repair is planned (`SCORECARD.md` § planned, round 47)." | P | **TRUE at BASE, expires this round.** `sed -n '/^---$/,/^---$/p' SKILL.md \| grep -c '<skills>'` → 1. Once C2 removes the token, this sentence is false in the same commit — update it with C2, do not leave "planned". |
| 15 | 419–420 | "loader strings in both harness binaries (9 opencode / 17 omp)" | H (round-7 recount) | **Dated, unreproducible as written.** No definition of "loader strings" in the body; I did not re-derive the counts. Read as history only. |
| 16 | 428–430 | log is "`message=init count=N` per instance, latest 18; `duplicate skill name` warns" and "the `<available_skills>`-vs-`<skills>` tag split (round-8/9)" | H (with present-tense framing) | Path holds; `duplicate skill name` string still in 1.19.3; init-count count is 0 today (row 10); the "tag split" is artifact-contradicted (row 6). Dated and stale-prone; do not cite as a live discriminator. |
| 17 | 431–436 | "`~/.opencode/bin/opencode` + upstream `github.com/sst/opencode` (dev): `packages/opencode/src/skill/index.ts:321-343` … `:105-139` … `:235-246` … `session/system.ts:107-119` … `tui/src/component/dialog-skill.tsx:41`" | P | **PATH DEAD; line numbers unverifiable; function shapes HOLD.** `ls /home/vgpnk/.opencode/bin/opencode` → exit 2 ("No such file"). 1.19.3's dump contains no `// packages/opencode/...` comments (0), so the cited line ranges cannot be checked and no source map was extracted. Behaviour-level: verbose `fmt` + location, warn-then-assign, unbounded concurrency, `SystemPrompt.skills` gate all verified (row 8); `dialog-skill` literal absent (0) — TUI claim not checked. |
| 18 | 438–443 | "`~/.omp/agent/sessions/**/*.jsonl` (5842 files; `session_init` records ~4032–4120 …; 32 … 23 at round 7)" | H (round 7/9) | Counts are stale as a current descriptor: `find ~/.omp/agent/sessions -name '*.jsonl' \| wc -l` → **14 487** today. The text does warn "re-run before citing", so it is honest history, but the parenthetical reads present tense. |
| 19 | 445–458 | "`~/.local/bin/omp` embedded JS (`strings -n 6`; cite anchors, not offsets…)"; "`if (t.length <= _8n)`… `_8n = 100`"; "key `A8n` = `sha256(K7s ‖ \x00 ‖ name ‖ \x00 ‖ description)`"; template "273-byte … sha256 `c1f03c8e248eb40e…`"; db "17 rows at round 9 … 27/27 checks" | P (last two clauses H) | **Path HOLDS** (`~/.local/bin/omp` is 18.12.5, sha = snapshot). **Sha HOLDS** (rows 11, 13). **Symbols STALE**: `_8n` → `v`; `A8n` → `D`; `K7s` → `w` (all three old tokens appear only inside base64 blobs / unrelated minified chunks: `A8n` 3×, `K7s` 7×, all noise). The *exported* names survive: `xze as previewSkillDescription`, `vze as createSkillDescriptionCompressor`. Row counts and "27/27" are round-9/10 history. |
| 20 | 460 | "round 10 re-verified by `verifiers/verify_harness_claims.py`, 27/27 checks" | H | Internal inconsistency with the 28 at lines 109 and 465; the live `CHECKS` dict has **28** ids. Dated, but it will read as a contradiction to a present-tense reader. |
| 21 | 467–471 | `check_substrate_pins.py` "enforces the `verifiers/baseline.json` `measured_against` pins (omp sha256 + ns-exact mtime, opencode sha256; exit 0/1/2/3 …)" | P | **HOLDS as a description.** File exists; the *values* are red at BASE (3/3 DRIFT), but that is C1's value problem, not this prose's. |
| 22 | 508–509 | `corpus/knowledge/harness-verifier-round10.md` "the facts behind each check (key prefix bytes + sha256, style-aware salt, offer-gate roots, opencode counter checks)" | P | **HOLDS** (file exists; check list matches the 28-check dict). |

Adjacent, outside the strict ticket but same Sources block and same failure mode (host migration,
not substrate version) — all present tense, all dead at BASE:

| Line | Statement | Observed |
|------|-----------|----------|
| 48, 399 | "`~/.config/opencode/skills/ufo/SKILL.md`" | `ls` exit 2; no `skills/` under `~/.config/opencode`. |
| 409 | "`~/.config/opencode/agents/*.md` (18 files, 14–197 lines)" | glob expands to 0 files; `~/.config/opencode` holds only `cli.json`, `opencode.json`, `service.json`. |
| 415 | "`~/.config/opencode/command/*.md` (3 files)" | 0 files. |
| 230 | "`~/.config/opencode/opencode.json`" | exists (95 B, keys `$schema`,`theme`,`autoupdate`) — holds. |

## 2. Counterexamples (hypotheses that the evidence killed)

1. **"omp 18.12.5 flipped its catalogue to `<available_skills>`."** I first read the
   `<available_skills>` + `<location>` template at `:2413743` and expected the body's tag claim
   to be dead. It is not. Of 6 667 session files dated 2026-10-21, **6 656 contain `<skills>`**;
   a fresh 15:28 session (`-tmp/…/OpenCodeModel.jsonl`, `runtime.version 18.12.5`) renders
   `- name: description` bullets under `<skills>`. Of 63 files containing `<available_skills>`,
   only 4 have `<skill>` within 400 chars and all 4 are pasted transcript text (a peer grepping
   the dumps; one is my own lane's history). **No injected `<available_skills>` catalogue was
   found.** The template is present in the ELF but its owner/activation is unresolved — do not
   rewrite the tag row on its strength, but do stop asserting exclusivity (row 6).
2. **"`~/.omp/agent/skills` is a phantom root."** Literal `.omp/agent/skills` has 0 hits in the
   dump, but the loader joins `Se()+"skills"` (`:19679…`/`CZ`), and `Se()` is the agent dir —
   the same function that resolves the db that really exists at `~/.omp/agent/`. Root holds;
   absence of a literal is not absence of a root.
3. **"The 273-byte prompt sha moved with the build."** It did not: 273 bytes at raw offset
   252 816 008 hash to the pinned `c1f03c8e…` exactly. `[INFERENCE]` the cache key space is
   therefore still valid at 18.12.5; I did not re-run the verifier to confirm row-level keys.
4. **"The 99-cliff applies to every rendered line."** It applies to cache misses. A cache hit
   (`reverse-engineer-anything`) renders **101 chars** with no ellipsis; `create-toolset`
   renders **88 chars ending in `…`** (last-space cut), exactly the documented fallback. The
   body's "hard 99-char cliff" is correct for the truncator, not for cached rows — as written.
5. **"`_8n` is just a stale comment."** No: the *values* are unchanged (100/99, 160, 12), so the
   only stale thing is the grep anchor. A reader following "cite anchors" at 18.12.5 would grep
   `_8n` and land in base64 noise — operability loss, not behaviour loss.

## 3. Recommended prose deltas (advice; no edits made)

1. Line 25–26, 91, 447–449: replace `_8n` with the exported name + constant, e.g. "`previewSkillDescription`
   (`var v = 100` in 18.12.5; the symbol was `_8n` in ≤18.12.2 builds)". Values stay 100/99/≥40.
2. Line 451: replace "key `A8n` = `sha256(K7s ‖ …)`" with "key helper (`D` in 18.12.5, was `A8n`)
   = `sha256(prompt ‖ \x00 ‖ name ‖ \x00 ‖ description)`, prompt = the 273-B template (`w`, was `K7s`)".
   The sha `c1f03c8e…` is still exact — keep it.
3. Line 431: replace `~/.opencode/bin/opencode` with the resolved npx-cache ELF path
   (`~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode`, sha `179ca421…`)
   and say the `~/.local/bin/opencode` wrapper must not be executed for evidence (it runs
   `npx --prefer-online`). Mark the `index.ts:NNN` ranges as upstream-dev line numbers, not
   local-file citations, or drop the numbers and keep the function shapes.
4. Line 89–90 / 430: soften to "opencode has no `<skills>` tag; omp's active catalogue is
   `<skills>` (18.12.5 sessions), though the 18.12.5 ELF also carries a dormant/unresolved
   `<available_skills>` template — never infer the harness from a tag alone at artifact level."
5. Line 41–42 / 92: qualify `<location>` with "in the v1 `SystemPrompt.skills` renderer"; note
   the 1.19.3 v2 `SkillGuidance` section emits `<available_skills>` without `<location>` and can
   supersede itself mid-session (which also breaks "no cache / frozen" if that path is active).
6. Line 103: replace the init-count grep with a probe that is checkable without executing the
   wrapper, or state that it requires a post-1.19.3 log; currently it returns 0 lines.
7. Line 151: fold into C2 — after the description loses `<skills>`, delete "still carries" or
   rewrite as "the `<skills>` token was removed in round 47".
8. Line 460: change "27/27" to "27/27 at round 10; 28 checks now" (or delete the number).
9. Line 91 roots: add `.agent/skills` (singular) and `.github/skills` for completeness; both are
   live providers at 18.12.5.

## 4. What I did NOT check

- **No verifier runs** (`verify_surfaces.py`, `verify_harness_claims.py`,
  `check_substrate_pins.py`): lane gate restriction; C1's seat owns those, and I used
  `.ufo/waves/round-47/before/SUMMARY.md` for their BASE state (surfaces exit 2 / 4 PASS 3 FAIL;
  pins exit 2 3/3; harness 21/28). Consequently the "omp vacuity 0/8 loader classes" statement
  is cited, not re-derived.
- **Did not execute `opencode`** (contract: the wrapper runs `npx --prefer-online`, a network
  fetch). So: the 1.19.3 runtime log format, TUI `dialog-skill` whitespace behaviour, and which
  of v1 `SystemPrompt.skills` vs v2 `SkillGuidance` this host injects are unresolved. The v2
  finding is presence-only.
- **No version diff**: 18.12.2/18.12.3 and opencode 2.0.26 binaries are not retained, so I
  cannot attribute the anchor renames to a specific build. The 18.12.4 and 18.12.5 changelog
  sections contain no skill-render/description entry; 18.12.3 has only an `omp skill list`
  `customDirectories` fix and a pi-compat `formatSkillsForPrompt` import fix. `[INFERENCE]`
  the tag/anchor state may predate 18.12.3.
- **Did not resolve the owner/activation of the omp `<available_skills>` template**; only its
  presence and the absence of session evidence for it.
- **Did not re-derive** the "9 opencode / 17 omp loader strings" count (line 419) — the body
  never defines the extraction.
- **Did not audit** the opencode config-surface migration (rows 48/399/409/415) beyond existence
  checks; that is host state, not the pinned substrate.
- Did not read `verifiers/` bodies beyond the check-id lists and `CHECKS` dict; no full-file
  review of the verifiers (other seats).

## 5. Commands run (key ones, with exit codes)

| Command | Exit | Key output |
|---------|------|------------|
| `git -C <lane> rev-parse HEAD`; `git -C <lane> status --short SKILL.md` | 0; 0 | `c61a973b…`; empty |
| `sha256sum /home/vgpnk/.local/bin/omp` | 0 | `fdbc8136…da798e7e` (== snapshot) |
| `omp --version` | 0 | `omp/18.12.5` |
| `sha256sum <npx>/opencode-linux-x64/bin/opencode` | 0 | `179ca421…d3ab7ee9` (== snapshot) |
| `ls /home/vgpnk/.opencode/bin/opencode` | 2 | "No such file or directory" |
| `sha256sum corpus/knowledge/instruction-surface-census-round13.md` | 0 | `1930ec04…` (whole file); `:328` holds body sha `e046a025…` |
| python: 273 B at raw offset 252 816 008 of `bin/omp-18.12.5` | 0 | `c1f03c8e248eb40e…` (== pin) |
| `grep -c -F '1.19.3' opencode-1.19.3.strings` | 0 | 2 (`var n="1.19.3"`, user-agent) |
| `grep -c -F 'init count' opencode-1.19.3.strings` | 1 | 0 |
| `grep -o 'message=init count=[0-9]*' ~/.local/share/opencode/log/opencode.log \| wc -l` | 0 | 0 (log mtime 2026-10-20 07:52 < ELF 18:33) |
| `find ~/.omp/agent/sessions -name '*.jsonl' \| wc -l` | 0 | 14 487 |
| today-session tag census (`grep -l -F … $recent`) | 0 | `<skills>` 6 656 / 6 667; "omitted from the system prompt" 2; `<available_skills>` 63 (all transcript text) |
| `sed -n '/^---$/,/^---$/p' SKILL.md \| grep -c -F '<skills>'` | 0 | 1 |
| python: count `verify_harness_claims.py` `CHECKS` ids | 0 | 28 |
| `ls ~/.config/opencode/agents/*.md \| wc -l`; `…/command/*.md \| wc -l` | 0; 0 | 0; 0 |

No tools installed or upgraded; no pacman transactions (host-wide pause respected); no writes
outside this report path.
