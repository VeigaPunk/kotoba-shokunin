Result: MIXED — the lane's corpus records 24 statements about always-on rule-file resolution; 6 are present-tense and now false against the three clients' current docs, 3 more carry stale counts or a doc-vs-code tension, 7 hold, and the Q30 third leg is complete with a decisive result: the corpus records **no** per-client statement about Claude Code, Codex or Gemini CLI rule-file resolution, so it can support neither a "documents nothing" negative nor a redirect-form claim.

Round 53 C2 scout, seat `KotobaR53.ScoutLaneCorpusAlwaysOn`, measured 2026-10-22T20:04–20:20Z on the lane at `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`. Read-only: no lane file edited, no git/jj write, no sandbox clone needed (every probe below is a read). No installs or upgrades this seat.

Method note: no `lsp` device is exposed in this session's tool inventory, and every target of this slice is prose (corpus markdown, a downloaded doc, one ELF literal count) — there is no definable symbol to resolve. Text grep is the applicable method here, not a fallback from an available server, and is recorded as literal search rather than semantic proof.

---

## Part A — the three documents opened (fresh fetch, this seat)

All fetched by `curl -sS -L`; UTC from the response `date` header; scratch copies under `/fast/scratch/hyaku/kotoba-r53/ScoutLaneCorpusAlwaysOn/src/`. Line numbers below are lines **in the fetched bytes**, not in the rendered page.

| # | URL | UTC | HTTP | bytes | sha256 | file cited as |
|---|---|---|---|---|---|---|
| D1 | `https://code.claude.com/docs/en/memory.md` | 2026-10-22T20:04:50Z | 200 (`text/markdown`) | 51,971 | `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff` | `claudecode-memory.md` |
| D2 | `https://developers.openai.com/codex/guides/agents-md` | 2026-10-22T20:04:50Z | **308** → | — | — | (redirect only) |
| D2b | `https://learn.chatgpt.com/docs/agent-configuration/agents-md` (target of D2) | 2026-10-22T20:04:50Z | 200 (`text/html`, `last-modified: 2026-10-22T19:13:01Z`) | 409,154 | `1ffc12a3f3a797f6380e5ff23207d23664f610939c441b9218d53cec79c0ea8a` | — |
| D2c | `https://learn.chatgpt.com/docs/agent-configuration/agents-md.md` | 2026-10-22T20:05:02Z | 200 (`text/markdown`) | 9,149 | `9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e` | `codex-agents-md.md` |
| D3 | `https://opencode.ai/docs/rules.md` | 2026-10-22T20:05:02Z | 200 (`text/plain`) | 6,684 | `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54` | `opencode-rules.md` |
| D3b | `https://opencode.ai/docs/rules/` (rendered twin) | 2026-10-22T20:04:50Z | 200 (`text/html`) | 76,861 | `05a6070925ba6a0a74fe23bde1b2cc0329bf7dae8e00ba39cf373001967128e2` | — |

The Codex guide's canonical location is now `learn.chatgpt.com` (a `308` from the `developers.openai.com` path the assignment names); the lane's round-48 authority file already cites `learn.chatgpt.com` for Codex (S021), so this is a redirect, not a moved subject.

The current rules, verbatim and attributed:

**Claude Code (D1).**
- Directory walk and concatenation: `:64` "CLAUDE.md and CLAUDE.local.md files in the directory hierarchy above the working directory are loaded at launch"; `:144` "All discovered files are concatenated into context rather than overriding each other".
- **AGENTS.md is now read natively, and only when no CLAUDE.md counts.** `:352` says a repo "already set up for other coding agents works without adding a `CLAUDE.md`, an import, or a setting"; `:356` "An `AGENTS.md`, and no `CLAUDE.md` or `CLAUDE.local.md` in your working directory or above it" → "Your `AGENTS.md`"; `:357` with both present → "Your `CLAUDE.md` files only". `:364` "Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later."
- Which files *count* for suppressing AGENTS.md: `:370` "a `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` in your working directory or any directory above it"; user-scope and managed files and `.claude/rules/` do not count.
- Explicit negatives: `:378` "Not read: `AGENTS.local.md`, `AGENTS.override.md`, or anything under a `.agents/` directory" — **this covers the host's `~/.agents/AGENTS.md` for Claude Code.**
- Imports: `:102` `@path/to/import` expanded and loaded at launch; `:104` "Relative paths resolve relative to the file containing the import" and "maximum depth of four hops"; `:112` code spans and fenced blocks are skipped; `:134–138` external imports need one per-project approval, user-scope files are trusted except in Cowork.
- Redirect forms (the C2 basis): `:442` "putting an `@AGENTS.md` import in a `CLAUDE.md` next to it"; `:455` "ln -s AGENTS.md CLAUDE.md"; `:458–461` constraints — Edit/Write refuse to write through the symlink, and on Windows a committed symlink checks out as a plain text file.
- Size: `:88` "target under 200 lines per CLAUDE.md file"; no hard cap. (Do **not** conflate this with `:549`, the 200-line / 25 KB read limit measured on `MEMORY.md`, the auto-memory file.)
- Duplicate suppression: `:391` "Claude Code skips an `AGENTS.md` it has already loaded"; `:437` a `CLAUDE.md` symlinked to `AGENTS.md` is read once.
- Nearest dated-text rule: `:90` "remove outdated or conflicting instructions" and `:94` `/doctor prompt-audit` for "outdated or conflicting content". **"outdated" ≠ "dated"** — no date-stamp rule is stated.
- `GEMINI`: **0** occurrences (`grep -ci GEMINI` → 0, exit 1). Claude Code documents nothing about `GEMINI.md`.

**Codex (D2c).**
- `:11` "Codex reads `AGENTS.override.md` if it exists. Otherwise, Codex reads `AGENTS.md`." — global scope, `CODEX_HOME`; "only the first non-empty file at this level".
- `:12` project scope walks root → cwd, checking "`AGENTS.override.md`, then `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`"; "Codex includes at most one file per directory".
- `:13` merge is additive: "Files closer to your current directory override earlier guidance", by position.
- `:15` size is a hard stop: "stops adding files once the combined size reaches the limit defined by `project_doc_max_bytes` (32 KiB by default)".
- `GEMINI`: **0** occurrences.

**opencode (D3).**
- `:76` "Project rules: `CLAUDE.md` in your project directory (used if no `AGENTS.md` exists)"; `:77` "`~/.claude/CLAUDE.md` (used if no `~/.config/opencode/AGENTS.md` exists)"; gates at `:83–85` (`OPENCODE_DISABLE_CLAUDE_CODE{,_PROMPT,_SKILLS}`).
- `:94` "Local files by traversing up from the current directory (`AGENTS.md`, `CLAUDE.md`)" then the global file, then the Claude Code file; `:98` "if you have both `AGENTS.md` and `CLAUDE.md`, only `AGENTS.md` is used".
- `:132` "opencode doesn't automatically parse file references in `AGENTS.md`" — so an `@AGENTS.md` line is **not** a redirect for opencode; the config `instructions` list (`:102`–`:126`, 5 s remote timeout at `:124`) is its composition mechanism.
- No size limit anywhere (`KiB|max_bytes|line limit` → 0), no dated-text rule (`dated|stale|outdated|date\b` → 0), symlink mentioned once (`:177`) only for manual sharing, not loader behaviour.
- `GEMINI`: **0** occurrences.

---

## Part B — every always-on resolution statement the lane records

"Client" is the client the sentence is about, not the file's author. "Round/date" is the file's own sourcing line unless noted.

| # | path:line | statement (compressed) | client | date/round | vs current docs |
|---|---|---|---|---|---|
| 1 | `corpus/knowledge/agents-md-and-dispatch-surfaces.md:10` | AGENTS.md = 6 identical-shape files under `/home/vgpnk/projects/shokunin/*/` + `~/.agents/AGENTS.md`; "Always injected for sessions rooted in the repo" | unnamed (omp/opencode era) | 2026-09-28 (:3) | **FALSE** — see F1 |
| 2 | `…agents-md-and-dispatch-surfaces.md:15-17` | six child files share one 5-line template; md5s differ only in the repo-name line | fleet, not a client | 2026-09-28 | stale count: 17 files, of which 12 keep the 5-line template (17 measured here; the 12/4/3 split is round-21 `.ufo/reports/round-21/scouts/K01.md:31`) |
| 3 | `…agents-md-and-dispatch-surfaces.md:26-29` | `~/.agents/AGENTS.md` "~60 lines"; posture rules "name the axes"/"iterate cheap in parallel", ban "no worktrees"; "Zero procedures" | host file, unnamed client | 2026-09-28 | **FALSE** — see F2 |
| 4 | `corpus/README.md:12` | index row: "6 child AGENTS.md + `~/.agents/AGENTS.md` + 8 `.ufo/prompts/*-L1.md`" | — | index, undated | **FALSE** — F3 |
| 5 | `corpus/knowledge/alwayson-checklist-round7.md:15-16` | AC-4 "No dated/transient text; dates and live-state go to status files" | none (lane rule) | round 7 | no client states it (nearest: D1 `:90`) |
| 6 | `…alwayson-checklist-round7.md:20-21` | AC-7 "check repo root for both `AGENTS.md` + `CLAUDE.md`; one canonical owner or explicit redirect" | none (lane rule) | round 7 | **holds**, and is now vendor-sourced (D1 `:442`, `:455`) |
| 7 | `…alwayson-checklist-round7.md:22-23` | AC-8 size: local default = the 5-line template; expansion must be every-session constraints | none | round 7 | no numeric cap recorded; documented caps exist (F10) |
| 8 | `…alwayson-checklist-round7.md:25-30` | "6/6 shokunin AGENTS.md PASS"; host "(75 lines, 3781 B)" FAIL AC-1/2/4/5 at `:18`/`:55` | host file | round 7 | **FALSE** — F4 |
| 9 | `corpus/knowledge/claude-md-surface.md:8-11` | loader literals: opencode `CLAUDE.md` 9, omp 17; `AGENTS.md` 30/35; `CONTEXT.md` 1 → "CLAUDE.md is a recognized rules-file name on this host" | opencode + omp | round 6, 2026-09-28 | counts stale (F9); conclusion holds |
| 10 | `…claude-md-surface.md:12-17` | zero captured injections; no session ran in a CLAUDE.md dir → "cold channel" | omp/opencode | round 6 | dated record; already re-measured at round 21 |
| 11 | `…claude-md-surface.md:33-34` | "Same load semantics as AGENTS.md (always-on when present in the repo)" | Claude Code (implicit) + all | round 6 | **FALSE** — F5 |
| 12 | `…claude-md-surface.md:36-39` | dual-name collision: "two files, one channel; pick one owner, redirect the other" | generic | round 6 | **holds**; forms documented at D1 `:442`/`:455`, but the redirect is client-specific (F6b) |
| 13 | `…claude-md-surface.md:40-42` | file-name ≠ loader contract; a dispatch template named `claude.md` is never rules | generic | round 6 | holds |
| 14 | `…claude-md-surface.md:48-51` | open: "whether omp injects CLAUDE.md … is unverified" | omp | round 6 | still open; narrowed by census `:478` |
| 15 | `corpus/knowledge/instruction-surface-census-round13.md:113-118` | omp registry priority table; exactly one file wins per directory depth | omp | round 13, one lane, marked unconfirmed (:121-130) | unchanged; neither doc speaks for omp |
| 16 | `…census-round13.md:146-147` | `Cl(e,"gemini","GEMINI.md")` resolved to `cwd/.gemini/GEMINI.md` only, no walk-up | omp | round 13, wire probe | unchanged (omp-side measurement) |
| 17 | `…census-round13.md:474` | AGENTS.md "Always-on: injected into every session in its repo" | unnamed, stated as general | round 13 | **FALSE** as general — F7 |
| 18 | `…census-round13.md:478` | omp reads CLAUDE.md *alongside* AGENTS.md; opencode reads it only when no AGENTS.md exists, gated by the env vars | omp + opencode | round 13 | **holds** — matches D3 `:76`, `:98` |
| 19 | `…census-round13.md:479` | cross-tool family: "keep AGENTS.md, redirect or delete the rest" | harnesses | round 13 | holds; add the Claude Code inversion (F7) |
| 20 | `…census-round13.md:251` | `opencode:instructions/CONTEXT.md` id from the 1.19.3 dump (1 occurrence) | opencode (code) | round 13 | holds; measured 1 occurrence in 1.19.4 too |
| 21 | `corpus/knowledge/instruction-surface-remeasure-round13.md:23` | opencode CLAUDE.md is a loader gated by `OPENCODE_DISABLE_CLAUDE_CODE{,_PROMPT}` | opencode | round 13 | holds (D3 `:83-85` lists the same names) |
| 22 | `…remeasure-round13.md:24` | opencode walk = first existing name per directory, `AGENTS.md` → `CLAUDE.md` → `CONTEXT.md` | opencode | round 13 | holds vs code; docs now name only two (F8) |
| 23 | `corpus/SOURCES.md:17` (S004) | agents.md FAQ: "the closest AGENTS.md to the edited file wins and explicit user chat prompts override everything" — status `queued`, opened 2026-10-19 (fetch recorded at `corpus/lessons/round-46.md:66`) | open format, all clients | 2026-10-19 | **misleading if admitted** — F6 |
| 24 | `corpus/knowledge/opencode-extraction-round14.md:50-56` | OC-1…OC-6 rule anchors incl. `CONTEXT.md` in the priority array | opencode (code) | round 14 | C1's surface, not corpus staleness; unchanged |

`SKILL.md` restates the checklist verbatim at `:370` (AC-4), `:375-376` (AC-7), `:377-378` (AC-8), and carries two population claims at `:363-364` and `:461-462`; `PROVINCE.md` carries no resolution or precedence claim at all (`:3` domain line, `:13` Core pointer, `:46` kagi row citing `$HOME/.agents/AGENTS.md` as a shared read). `AGENTS.md` (the lane's own rule file) names no rule-file mechanics.

---

## Part C — present-tense statements now false (each measured)

**F1 — `corpus/knowledge/agents-md-and-dispatch-surfaces.md:10`: path, count and the "always" clause are all wrong.**
`ls -d /home/vgpnk/projects` → exit 2, `No such file or directory` (case-sensitive host; the capital-P root is real). `ls /home/vgpnk/Projects/shokunin/*/AGENTS.md | wc -l` → `17`. "Always injected for sessions rooted in the repo" is falsified for Claude Code by D1 `:356-357` (with any `CLAUDE.md` in cwd or above, only CLAUDE.md files are read) and for opencode by the lane's own `census:478`. The sentence names no client, so it reads as a general law; it is not one.

**F2 — `…agents-md-and-dispatch-surfaces.md:26-29`: the quoted bytes are gone.**
`wc -l /home/vgpnk/.agents/AGENTS.md` → `14`; `wc -c` → `949`; mtime `Oct 20 09:18`. `grep -c` for `name the axes` → 0, `iterate cheap in parallel` → 0, `no worktrees` → 0. The file now opens `# Operator tooling directive — 2026-10-19` and carries "Before installing, read `/home/vgpnk/.omp/agent/RULES.md`" — a cross-file procedure, against "Zero procedures". It also carries a **date in its first line**, so the file now fails AC-4 on its own bytes.

**F3 — `corpus/README.md:12`: "6 child AGENTS.md" → 17** (`ls … | wc -l` → 17). Same number as F1.

**F4 — `corpus/knowledge/alwayson-checklist-round7.md:29-30` and `SKILL.md:363-364`: "75 lines, 3781 B".**
Measured 14 lines / 949 B. The host-file lines it cites (`:18`, `:55`) no longer exist. The verdict (FAIL AC-4) survives by accident: the current file's line 1 is a date. The `6/6 … PASS` cell is a 6-file statement in a 17-file world. This is the same 75→14 drift the population scout recorded independently (`ScoutAlwaysOnPop.md:1`); reported here as a corpus statement, not re-derived.

**F5 — `corpus/knowledge/claude-md-surface.md:33-34`: "Same load semantics as AGENTS.md".**
False in both directions for the clients that matter. Claude Code: CLAUDE.md **suppresses** AGENTS.md (D1 `:357`); opencode: CLAUDE.md is a **fallback** used only when no AGENTS.md exists (D3 `:76`). The two names are not co-equal channels, so "same constraint-survival rule applies" is the right craft outcome reached from a wrong premise — the premise matters because C2's instrument must decide what a "canonical owner" is.

**F6 — `corpus/SOURCES.md:17` (S004): "the closest AGENTS.md … wins" as a cross-tool rule.**
It is not cross-tool. Claude Code concatenates and does not override (D1 `:144`); opencode picks by **name first**, not proximity (D3 `:94`, `:98`); only Codex layers root→cwd with later files overriding (D2c `:13`). S004 is `queued`, never admitted, so nothing shipped rests on it — but if a round admits it, the row needs this bound. Not counted among the 6 falsified present-tense statements because its status is already candidate-only.

**F6b — the redirect forms are client-specific, and one of the two documented forms is inert on opencode.**
D1 `:442`/`:455` give import and symlink for Claude Code. D3 `:132` says opencode does not parse file references, so a `@AGENTS.md` line inside `CLAUDE.md` is literal text to opencode — harmless (AGENTS.md wins there by name) but not load-bearing. Any instrument that treats "a `@AGENTS.md` line" as a universal redirect overstates the source. `[INFERENCE]` on the harmlessness: that the literal line reaches opencode's context as text follows from `:126` ("All instruction files are combined") plus `:132`; I did not run opencode to observe it.

**F7 — `corpus/knowledge/instruction-surface-census-round13.md:474`: "injected into every session in its repo".**
Falsified as a general claim by D1 `:356-357`, `:370`, and by a stricter negative the lane has never recorded: D1 `:378` says anything under a `.agents/` directory is **not read**, which excludes the host's own `~/.agents/AGENTS.md` from Claude Code entirely. The row is the one place the lane states an always-on law without naming a client.

**F8 — `…census-round13.md:479` + `remeasure-round13.md:24`: the third fallback name is no longer documented.**
Code still carries it — `grep -ac 'CONTEXT.md'` on the 1.19.4 binary (`sha256 538fcb1b…`, matches the plan's pin) → `1`, and I measured `AGENTS.md` 16, `CLAUDE.md` 8, `GEMINI` 2 in the same ELF. The opencode docs now list two names (D3 `:94`). So the lane's code-derived statement holds and the vendor's rendered page under-describes its own loader; a doc-vs-code note belongs on the row rather than a correction. Flagged because a reader taking D3 as the authority would call the lane wrong.

**F9 — `SKILL.md:477-481`: unlabelled live-tense loader counts.**
"loader strings in both harness binaries (9 opencode / 17 omp)" carries a round-7 label only on the preceding clause (`18 hits at round-7 recount`), and the opencode binary it counts no longer exists on this host (the round-8/18 `~/.opencode/bin` install is gone; the lane runs the npx 1.19.4 binary). Measured on 1.19.4: `CLAUDE.md` 8, `AGENTS.md` 16 — not 9 and not the round-21 readings either. The class-level conclusion ("seventh surface class, cold channel") is unaffected; the integers are stale and unlabelled.

**F10 — silence where the lane has no size number at all (gap, not a false statement).**
`alwayson-checklist-round7.md:22-23` and `SKILL.md:377-378` bound size by judgment ("5-line template", "distinct every-session constraints") with no numeric cap. Documented caps now exist and are unrecorded anywhere in the lane (Part D sweep): Claude Code target <200 lines (D1 `:88`), Codex hard stop 32 KiB combined and `project_doc_max_bytes` (D2c `:15`), opencode none. The one trap: D1 `:549`'s 200-line/25 KB figure is the **auto-memory `MEMORY.md`** limit, not a CLAUDE.md limit — an instrument that quotes "200 lines" for CLAUDE.md as a *read limit* would be citing the wrong object.

---

## Part D — the Q30 third leg (lane-corpus grep), run and printed

Q30 (`corpus/QUALITY.md:41`) requires three legs for any "client X documents nothing about Y" negative: the vendor's changelog/release notes, the current docs source tree, and a grep of the lane's own corpus. This seat supplies the third leg and the current-docs leg for three clients; it does **not** supply changelogs (out of slice) — so no client can be recorded `silent` on my evidence, only `not checked`.

Leg 3a — mechanisms the three docs rely on, searched in the lane:
```
grep -rnE 'AGENTS\.override|project_doc_fallback|CODEX_HOME|@AGENTS|200 lines|32 KiB|project_doc_max_bytes|fallback filename|GEMINI CLI' \
  corpus/knowledge corpus/lessons corpus/README.md corpus/QUALITY.md corpus/SOURCES.md SKILL.md PROVINCE.md AGENTS.md README.md
```
→ no output, **exit 1**. Zero hits. The lane records none of: Codex's `AGENTS.override.md` precedence, Codex's fallback-name list, `CODEX_HOME`, Claude Code's `@AGENTS.md` import form, Claude Code's 200-line target, Codex's 32 KiB cap or `project_doc_max_bytes`, or Gemini CLI as a client.

Leg 3b — mechanisms the lane does record: `grep -rnE 'first matching|first existing name|walk-up|priority|symlink|redirect|explicit redirect' corpus/knowledge corpus/SOURCES.md SKILL.md PROVINCE.md | wc -l` → `59` lines. All of them are omp-side or opencode-side loader facts, or the AC-7 rule; none is a per-client statement about Claude Code, Codex, Gemini CLI, Copilot or Cursor rule-file resolution.

Leg 3c — the only line in the lane where "AGENTS.md" and "Claude Code" co-occur:
```
grep -rnE 'AGENTS\.md.*Claude Code|Claude Code.*AGENTS\.md' corpus/knowledge corpus/lessons corpus/README.md SKILL.md PROVINCE.md
```
→ one hit, `corpus/knowledge/instruction-surface-census-round13.md:478`, and it names omp and opencode; "Claude Code" appears there only inside the omp registry description (`"Standalone CLAUDE.md files (Claude Code style)"`), which is omp's label, not a claim about Claude Code.

What the leg establishes, and what it forbids:
1. The corpus leg is **complete and negative** for Claude Code, Codex and Gemini CLI resolution: the lane holds no statement to contradict the docs, and none to support a "documents nothing" negative either. A C2 entry that cites the lane for a per-client negative would be citing nothing.
2. The corpus leg does **contradict** the current docs in two places (F5, F7), both of which over-generalise an omp/opencode measurement into a law. Those are the self-inflicted defects this round's C2 can fix by attribution.
3. Any client not opened by a seat this round is `not checked`. My three legs cover Claude Code, Codex and opencode only; the changelog leg is missing for all three, so even those are `current docs opened, changelog not checked` — the lane's own round-52 wording ("which revision each client speaks was not checked", `corpus/knowledge/mcp-server-instructions-round52.md:74`) is the honest precedent.
4. `GEMINI.md`: the lane's only statements are omp-side class measurements (`census:76`, `:146-147`, `:479`). No lane statement claims Gemini CLI reads `GEMINI.md`; D1 and D2c both have 0 occurrences. The client-side subject simply is not in the corpus.

---

## Part E — what this gives the C2 instrument (evidence, not design)

The two boxes' case sets can now be sourced instead of invented; the anchors exist, and one of them (`@AGENTS.md`) is only sourced from a document the lane has never cited.

- **alwayson.07 PASS, AGENTS.md alone:** D1 `:356` (Claude reads AGENTS.md when no CLAUDE.md counts) plus D3 `:76` (opencode uses AGENTS.md when present).
- **alwayson.07 PASS, the `@AGENTS.md` import:** D1 `:442` — the sentence also gives the exact pretext action (put Claude-specific text *below* the import).
- **alwayson.07 PASS, the symlink redirect:** D1 `:455`; the accompanying constraints at `:458-461` are the discriminating material — a committed symlink on a Windows clone degrades to a plain text file, i.e. a file whose whole body is `AGENTS.md` without `@`, which is a **FAIL** shape under any reading of `:442`.
- **alwayson.07 FAIL, prose mention that is not an import:** D1 `:436` "Claude sees `AGENTS.md` only if it decides to open the file" — the vendor's own statement that a mention is not a redirect.
- **alwayson.07 FAIL, both files with no redirect:** D1 `:357` — the AGENTS.md bytes are silently unread.
- **alwayson.07 scope caveat:** every client walks *above* the repo root as well as inside it (D1 `:370`, D2c `:12`, D3 `:94`). The AC-7 wording "check repo root" (`alwayson-checklist-round7.md:20-21`) is narrower than all three; a root-only check under-reports, it does not over-report.
- **alwayson.04 (dated or transient text):** no client documents this rule. AC-4 (`alwayson-checklist-round7.md:15-16`, `SKILL.md:370`) is the lane's own criterion and must be attributed that way (Q23). The nearest documented neighbours are D1 `:90` "remove outdated or conflicting instructions" and `:94` "outdated or conflicting content" — different predicate; a check built on "date string present" approximates neither, and if the entry calls it a client rule the attribution is unsourced. The lane's own live evidence still exists for the box: `~/.agents/AGENTS.md:1` now carries `2026-10-19` in its heading.

---

## Holdings worth keeping (so they are not re-reported as defects)

- `census:478` and `remeasure-round13.md:23` (opencode CLAUDE.md = fallback, env-gated) agree with D3 `:76`, `:83-85`, `:98` on every clause.
- `census:479`'s harness split ("omp reads every registered class while opencode reads one name per directory") is still the sharpest correct statement in the corpus on this subject.
- `claude-md-surface.md:40-42` ("file-name ≠ loader contract") is unchanged and still the right rule; D3 `:132` is a second witness for it.
- `corpus/README.md:87` (always-on checklist has no executed or delegated box) is true at base and is C2's premise, not a defect.
- `claude-md-surface.md:36-39`'s redirect advice is now vendor-documented, so AC-7 has a source it has never cited: D1 `:442`, `:455`.

## Limits (what this seat did not verify)

- Changelog/release-notes leg for all three clients was not opened. No client is recorded `silent` on my evidence; all three are `current docs opened, changelog not opened`.
- The opencode **source tree** was not read from GitHub this seat; the code-vs-docs difference at F8 rests on the shipped 1.19.4 ELF literal count (1 occurrence of `CONTEXT.md`) plus the lane's round-14 OC-1 anchors, not on a source read.
- Gemini CLI, Copilot, Cursor, Windsurf and the `agents.md` site were not opened; S004's precedence claim is assessed against the three clients I did open, and is marked misleading-if-admitted rather than false.
- Host-population numbers are quoted from this seat's own probes (14 lines / 949 B, 17 sibling files) and agree with `ScoutAlwaysOnPop.md:1`; that seat owns the population finding.
- Whether omp reads a symlinked `CLAUDE.md` or honours `@` imports in a rule file beyond the depth-5 note at `census:119-121` was not probed — it stays `claude-md-surface.md:48-51`'s open question.
- No lane or fleet file was written except this report; probes ran read-only, no sandbox clone was created because nothing needed to be mutated.
