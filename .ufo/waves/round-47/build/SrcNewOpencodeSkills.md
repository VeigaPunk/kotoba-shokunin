verdict: Both pages exist, fetch stable, and say quotable things — but they document two metadata keys 1.19.3 lacks and omit the singular `skill` root, the `skills.paths`/`skills.urls` roots and the `CONTEXT.md` name, so the honest row is S012/S013 at tier **B** as a naming witness, never tier A for loader behavior.

# SrcNewOpencodeSkills — opencode docs on skills and rules (round 47 build, seat MoriR22R.SrcNewOpencodeSkills-9)

Lane /home/vgpnk/Projects/shokunin/kotoba-shokunin at BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`git rev-parse HEAD`, exit 0). Production tree untouched; writes are the three files named in the acceptance plus scratch under `/fast/scratch/kotoba-r47/SrcNewOpencodeSkills/`. No tool installs or upgrades this seat.

## 1. What was opened (§ Opened, hashed, dated)

| page | fetched URL | HTTP | content-type | bytes | sha256 |
|---|---|---|---|---|---|
| Agent Skills | https://opencode.ai/docs/skills.md | 200 | `text/plain; charset=utf-8` | 5365 | `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` |
| Rules | https://opencode.ai/docs/rules.md | 200 | `text/plain; charset=utf-8` | 6684 | `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54` |
| Agent Skills (rendered) | https://opencode.ai/docs/skills | 200 | `text/html` | 73201 | `4d96fa569dd25469e085b3743ee7e5a53263792fb919b7591bd7b8397a3404f0` |
| Rules (rendered) | https://opencode.ai/docs/rules | 200 | `text/html` | 76861 | `17add737c0e36af7cf045b5024e1bef0f26767b1653e8b88633b5a9e7fd7cdc6` |

- Access: HTTP `date: Wed, 21 Oct 2026 15:54:51 GMT`; two re-fetches (≈15:56Z and `2026-10-21T15:58:26Z`) returned **byte-identical** `.md` bodies (Q10 instability check: source did not move during the run).
- Revision: no version selector and no version number on either page. The only `<select>` controls are theme (`Dark/Light/Auto`) and locale (English plus ~11 translations at `/docs/<lang>/...`); `grep -oE 'data-version|version-select'` on the HTML → no hits. Both pages carry `<time datetime="2026-10-20T22:40:11.000Z">Oct 20, 2026</time>` under `Last updated:`. The page is dated, not versioned — recorded in the `anchor` cell rather than pretending a release pin exists.
- The `.md` suffix is a real site variant (reader reported `Method: md-suffix`); spot checks confirm the same sentences in the rendered HTML (`walks up from your current working directory until it reaches the git worktree` → 1 hit; `The first matching file wins in each category` → 1 hit). `<name>` is numeric-escaped (`&#x3C;name>`) in HTML, which is why a naive literal probe of `.agents/skills/<name>/SKILL.md` against the HTML returns 0 while the six-bullet list is present at `skills.md:11-16`.

## 2. Candidate rows (ready to paste after `corpus/SOURCES.md:24`; next unused id at BASE is S012)

```
| S012 | OpenCode docs — Agent Skills — https://opencode.ai/docs/skills | docs | B | The documented skill-root layout and frontmatter contract, as a witness beside the frozen 1.19.3 loader | § Place files + § Understand discovery; page `Last updated` 2026-10-20T22:40:11Z; fetched `.md` sha256 `f10ced73…` | Six documented skill roots — project and global across `.opencode`, `.claude`, `.agents` — found by walking up to the git worktree, one `SKILL.md` per folder, `description` 1-1024 chars; omits the shipped `skill` singular root and `skills.paths`/`skills.urls` | queued | 2026-10-21 | 30d | — |
| S013 | OpenCode docs — Rules — https://opencode.ai/docs/rules | docs | B | The documented instruction-source precedence and custom-instruction merge | § Precedence + § Custom Instructions; page `Last updated` 2026-10-20T22:40:11Z; fetched `.md` sha256 `dfb242d9…` | Rules resolve in fixed precedence — walk-up `AGENTS.md` then `CLAUDE.md`, then `~/.config/opencode/AGENTS.md`, then `~/.claude/CLAUDE.md`; first match per category wins; `opencode.json` `instructions` globs and URLs merge in; never names `CONTEXT.md` | queued | 2026-10-21 | 30d | — |
```

Row-shape proof (scratch copy, `/fast/scratch/kotoba-r47/SrcNewOpencodeSkills/census`): `13` rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`), malformed `0` (`NF!=13` awk → 0), tier histogram `A=10 B=2 C=1`, status histogram `mined=4 queued=8 rejected=1`, duplicate ids empty, enum/tier-inflation empty, mined `used-by` missing empty (with `SKILL.md` present in the scratch root; the four `missing: SKILL.md` lines seen before copying it were my scratch cwd, not a row defect). The patch is `SrcNewOpencodeSkills.patch` (two added lines, no other hunk).

If another seat lands S012 first in this wave, renumber both; the ordering is not load-bearing.

## 3. Gate record (contract v1 rule 1 — URL, access, ≤25-word quote, location)

| id | URL | accessed (UTC) | HTTP | sha256 (fetched bytes) | quote | location | words |
|---|---|---|---|---|---|---|---|
| S012 | https://opencode.ai/docs/skills | 2026-10-21T15:54:51Z | 200 | `f10ced73…f8561` | "For project-local paths, OpenCode walks up from your current working directory until it reaches the git worktree." | § Understand discovery, `skills.md:22` | 17 |
| S013 | https://opencode.ai/docs/rules | 2026-10-21T15:54:51Z | 200 | `dfb242d9…3cb54` | "The first matching file wins in each category." | § Precedence, `rules.md:98` | 8 |

Supporting quotes (not the gate quote, same rows):
- S012 `skills.md:9` "OpenCode searches these locations:" followed by the six bullets at `:11-16` (`.opencode/skills`, `~/.config/opencode/skills`, `.claude/skills`, `~/.claude/skills`, `.agents/skills`, `~/.agents/skills`).
- S013 `rules.md:94` "**Local files** by traversing up from the current directory (`AGENTS.md`, `CLAUDE.md`)" (markdown emphasis normalized), with items 2 and 3 at `:95-96`; `rules.md:102-128` covers `instructions` (globs, remote URLs, "Remote instructions are fetched with a 5 second timeout." at `:124`, "All instruction files are combined with your `AGENTS.md` files." at `:126`).

`kind:docs` both. `recheck:30d` both — an unversioned page that already diverges from the pinned release cannot be rechecked on-release (there is no release edge to hang it on).

## 4. Why tier B, not A

Tier A is "primary or authoritative for that scope" (fleet `CORPUS.md:93-97`). These pages are authoritative for *what opencode's docs say*; they are **not** authoritative for what opencode ships, and the difference is measurable today:

| probe (frozen `opencode-1.19.3.strings`) | count | docs page |
|---|---|---|
| `autoinvoke` | **0** (`grep -qF`, exit 1) | `skills.md` 5 hits — documents `metadata[opencode/autoinvoke]` |
| `opencode/slash` | **0** | `skills.md` 3 hits — documents `metadata[opencode/slash]` |
| `CONTEXT.md` | 1 | 0 hits on either page |
| `{skill,skills}/**/SKILL.md` | 1 | absent; page names only `skills/` |
| `skills?.paths` / `skills?.urls` | 1 / 1 | absent (the binary's own embedded config doc has them) |
| `OPENCODE_DISABLE_EXTERNAL_SKILLS` | 2 | absent |

Observed facts: the npm `latest` release is `1.19.3`, published `2026-10-16T12:32:00.280Z` (`npm view opencode-ai version` → `1.19.3`, exit 0; `npm view opencode-ai time --json`), and the page was last updated `2026-10-20T22:40:11Z` — four days later. `[INFERENCE]` the site is generated from the main branch, so it documents at least one feature (`opencode/slash`, `opencode/autoinvoke`) that no `latest` release carries.

Consequence for the lane: a row admitting these pages at A would license "opencode supports `opencode/slash`" as an A-tier fact about the installed harness. It does not. B, with the scope cell narrowed to "what the docs state", is the calibrated cell; flip to A-for-doc-scope only if a version selector appears (then `recheck` becomes `on-release`).

## 5. Relevance to C1 — which classes the docs corroborate, which they mislead on

C1 (`plans/round-47.md:20-24`) must re-derive the opencode instruction classes against 1.19.3, where the plan records OC-1/OC-4/OC-6 matching nothing. My private replay of the verifier's anchors against the frozen dump (`verifiers/verify_surfaces.py:353-442`) reproduces exactly that split — **OC-1 false, OC-2 true, OC-3 true, OC-4 false, OC-5 true, OC-6 false** — with OC-2 matching the single literal `join(r.config,"AGENTS.md")`.

| doc statement | class id it touches | 1.19.3 evidence | verdict |
|---|---|---|---|
| `rules.md:92-98` project walk-up, `AGENTS.md` then `CLAUDE.md` | `opencode:project/AGENTS.md` (`surfaces-baseline.json:245`) | `globUp` ×3, `y=["AGENTS.md", "CLAUDE.md", "CONTEXT.md"]`, `findUp` ×9 — the name-priority array **is present** in 1.19.3 | class survives; OC-1's `ConfigInstructionPlugin.projectSource` anchor is a 2.x shape (0 hits) and must be re-anchored |
| `rules.md:95` `~/.config/opencode/AGENTS.md` | `opencode:config/AGENTS.md` (`:252`) | `join(r.config,"AGENTS.md")` | corroborated |
| `rules.md:102-128` `instructions` globs + remote URLs, 5 s timeout | `opencode:config/instructions` (`:273-278`) | `Instruction.system` consumes `T.instructions`, globs local paths, fetches `http(s)` with `timeout(5000)`, renders `Instructions from: …` | **counterexample to the `excluded` verdict on 1.19.3** (see below) |
| `rules.md:72-80` Claude Code compat, `~/.claude/CLAUDE.md` | none in the baseline (round 18 dropped `opencode:claude-home/CLAUDE.md`) | global candidate array `n=[join(r.config,"AGENTS.md"), join(home,".claude","CLAUDE.md")]`, `disableClaudeCodePrompt` ×2, `OPENCODE_DISABLE_CLAUDE_CODE*` ×5 | a class the current baseline no longer carries is live again in 1.19.3 |
| `skills.md:6-16,20-26` six skill roots | not an instruction class (the `skill` tool's discovery) | `bA=".claude"`, `xA=".agents"`, `GA="skills/**/SKILL.md"`, `SA="{skill,skills}/**/SKILL.md"`, `KA="**/SKILL.md"` | corroborates `.claude/skills` and `.agents/skills`; **narrows** the config roots to plural while the loader accepts both |
| `skills.md:108-131` `<available_skills>` tool description | the offer surface already mined in `corpus/knowledge/opencode-offer-trace-round8.md` | `available_skills` ×3 | corroborated; no new class |

The load-bearing counterexample: `verifiers/surfaces-baseline.json:273-278` carries `opencode:config/instructions` as **`excluded`** with reason "no loader consumer proven in the 2.x binary", repeated at `verifiers/verify_surfaces.py:369-372` and `corpus/knowledge/instruction-surface-census-round13.md:223`. In 1.19.3 the consumer is present and is exactly what `rules.md:102-128` documents (`Instruction.system`: `for(let O of T.instructions){…glob…}`; `(T.instructions??[]).filter(http)` fetched with `timeout(5000)`). This is not proof of a lane defect — the baseline's own `assembled` note (`surfaces-baseline.json:3`) says round 18 derived against a **2.x** binary (sha `d9123b9b…`), a different lineage from 1.19.3 — but it is a live class under the substrate C1 is re-pinning, and a re-derivation that copies round 18's exclusions would carry an exclusion the binary contradicts. C1's owner should re-verdict it, not inherit it.

## 6. Calibration traps this source invites

1. **Doc-only re-derivation invents classes.** Building the class set from `skills.md` yields `opencode/slash` and `opencode/autoinvoke` as "metadata-driven behaviour" that the shipped binary cannot execute. Any class admitted from a docs page must carry a binary witness line or be marked unshipped.
2. **Doc-only re-derivation also loses classes.** The page never mentions `CONTEXT.md`, the `{skill,skills}` brace root, `skills.paths`, `skills.urls`, or `OPENCODE_DISABLE_EXTERNAL_SKILLS`. Reading the page as a spec understates the loader by five surfaces.
3. **A named-but-absent literal is not a contradiction.** `~/.config/opencode/skills` has 0 literal hits in the dump because it is assembled from a discovered config-directory entry (`ConfigSkillPlugin` feeds `DirectorySource` from `e.entries()`); absence of the joined path is expected and must not be scored as a doc/binary disagreement.
4. **The docs already embed the correct shape in the binary.** The binary's own embedded config document says `skill(s)` and lists `skills.paths`/`skills.urls` (`opencode-1.19.3.strings:446068-446070`, `:446178`) — the website is the *weaker* witness of the two. That inverts the usual tier intuition.

## 7. What would flip the verdict

- A published `snapshot-*` build carrying `autoinvoke`: the "docs are ahead of shipped" reading narrows to "ahead of `latest`", and the `recheck` cadence should become `on-release` of whichever channel ships it. Unchecked (see §8).
- `opencode.ai/docs` gaining a version selector: tier A for that version's scope, `recheck:on-release`.
- The `config/instructions` class being re-verdicted `governed` in C1: this row's §5 table needs no change; the row's `teaches` never asserts the exclusion.

## 8. What I did NOT check

- No `snapshot-*` npm build was downloaded or grepped, so "no published artifact carries `autoinvoke`" is **not** claimed — only "absent from 1.19.3, which is `latest`".
- No non-author verification of these rows (I am the author; contract rule 1 wants an independent re-open).
- I did not run `verifiers/verify_surfaces.py` or any lane-wide gate; the OC-1…OC-6 replay in §5 is my own Python re-implementation of the anchors, not the verifier's output. The plan's recorded gate numbers are untouched and unconfirmed by me.
- I did not exercise the loader (no opencode execution, no wrapper; the contract forbids the wrapper and I did not run the snapshot ELF either), so "1.19.3 loads `.opencode/skill/` singular" is inferred from the glob literal `{skill,skills}/**/SKILL.md` and the `DirectorySource` registration of both `join(root,"skill")` and `join(root,"skills")`, not from a live discovery run.
- I did not verify every sentence of either page against the HTML rendering (three sentences spot-checked).
- Only the English page was read. The site serves ~11 translated locales (`/docs/<lang>/skills/` in the locale `<select>`); a translation could differ, and none was opened.
- I did not sweep for a versioned-docs endpoint; one guessed probe (`/changelog.md`) returned **404**, exit 0-on-curl with a 5307-byte HTML error body — recorded so nobody reads it as a changelog.
- No `name`-mismatch enforcement test: `NameMismatchError` exists as an exported class in the 1.19.3 skill module, but I did not establish whether a mismatched folder name errors, warns, or loads — relevant to S002's "lenient clients warn and load" and left open.

## 9. Commands run (exit codes as observed)

- `curl -sSL -o <p>.html -w '%{http_code} %{size_download}' https://opencode.ai/docs/{skills,rules}` → `200 73201`, `200 76861` (exit 0).
- `curl -sS -D <p>.md.hdr -o <p>.md https://opencode.ai/docs/<p>.md` → `200 5365`, `200 6684` (exit 0); headers show `content-type: text/plain; charset=utf-8`, `date: Wed, 21 Oct 2026 15:54:51 GMT`.
- `cmp -s skills.md final-skills.md && cmp -s rules.md final-rules.md` → identical (exit 0); third fetch at `2026-10-21T15:58:26Z`.
- `sha256sum` on both `.md` and both `.html` → the four hashes in §1.
- `sha256sum -c SHA256SUMS` in `/fast/scratch/kotoba-r47/shared` → `4/4 OK` (binary + dump integrity before every probe below).
- `grep -cF '<literal>' opencode-1.19.3.strings` for the §4/§5 literals → counts as tabulated; `grep -qF autoinvoke` → exit 1, `grep -qF ConfigInstructionPlugin` → exit 1.
- `python3` replay of `OC_PROJECT_FN`/`OC_PROJECT_TARGETS`/`OC_GLOBAL_JOIN_RE`/`OC_AMBIENT_SCHEMA`/`OC_READ_*`/`OC_ENV_*`/`OC_API_*` against the dump → OC-1 F, OC-2 T (1 match), OC-3 T, OC-4 F, OC-5 T, OC-6 F.
- `npm view opencode-ai version` → `1.19.3` (exit 0); `npm view opencode-ai time --json` → 1.19.3 at `2026-10-16T12:32:00.280Z` (exit 0).
- Census block from `/home/vgpnk/Projects/shokunin/CORPUS.md` over the scratch copy → rows 13, malformed 0, `A=10 B=2 C=1`, `mined=4 queued=8 rejected=1`, dup empty, enum empty, used-by empty.
- `diff -u -L a/corpus/SOURCES.md -L b/corpus/SOURCES.md …` → exit 1 (expected: differences), patch 2980 bytes, one hunk at `@@ -22,6 +22,8 @@`.
- `python3 -m json.tool .ufo/waves/round-47/build/SrcNewOpencodeSkills.json` → exit 0 (valid).

Artifacts: `SrcNewOpencodeSkills.md` (this file), `SrcNewOpencodeSkills.json` (fetch metadata, stability, parity probes, census), `SrcNewOpencodeSkills.patch` (the two-row insertion).
