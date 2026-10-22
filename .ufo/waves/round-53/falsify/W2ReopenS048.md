Result: HOLDS — the re-opened URL is the same object the row recorded (HTTP 200, 8,730 B, sha256 `00e45ea5be05…`), and every line the S048 row and `corpus/knowledge/alwayson-rule-files-round53.md` cite says what they attribute to it; six low-severity provenance defects remain (anchor filename, unbound `:105`, name-list scope, import omissions, an inference marker, `used-by`), none of which changes a stated fact.

Seat `KotobaR53.W2ReopenS048`, round 53 wave 2 (falsify), lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin` at judged revision `c775d6823bfca8f0de8c0874032a954438b38edc` (verified by `git rev-parse HEAD`; read-only). Scope: SOURCES row S048 only, plus the lines the knowledge entry cites for it. No lane file was written; all fetched bytes live under `/fast/scratch/hyaku/kotoba-r53/w2/W2ReopenS048/`. No git write, no clone was needed (nothing wrote into a repository). No tool was installed or upgraded; no model call was made.

Revision state at read time (`git status --porcelain`, read-only): HEAD is `c775d68`, but the working tree carries in-flight L1 edits to `PROVINCE.md`, `SCORECARD.md`, `SKILL.md`, `corpus/QUALITY.md`, `corpus/README.md`, `corpus/SOURCES.md`, `corpus/knowledge/alwayson-rule-files-round53.md`, `verifiers/check_mcp_instructions.py`, plus the untracked `corpus/lessons/round-53.md`. None of those edits touches this row: `git show c775d68:corpus/SOURCES.md` line 61 hashes `6349301be50939896cfab016f89b6fc056af1c85ceaa6fd078a499fc7f852cf9`, identical to the working-tree line, and the knowledge entry's S048 row line 30 hashes `eea79637c195e7aa9ebd7cbb4c23dac66cb54b0235152fb14777b8d5996bfe11` in both. The only working-tree SOURCES change near this row is a new S052 appended after S050 and a S050 anchor tweak (`git diff c775d68 -- corpus/SOURCES.md` shows `64a65` and line 63), so S048's line number is unchanged. Everything below therefore describes the judged revision's S048 content.

## 1. Refetch receipt

| item | value |
|---|---|
| URL | `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` |
| first fetch (UTC) | 2026-10-22T20:36:38Z (`date -u`) |
| status | HTTP 200 (`curl -w 'http=%{http_code} bytes=%{size_download}'` → `http=200 bytes=8730`) |
| bytes | 8,730; response header `content-length: 8730`; `content-type: text/markdown; charset=utf-8` |
| sha256 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` |
| row's anchor cell | `fetched 2026-10-22T20:05:13Z (200, 8,730 B, sha256 00e45ea5…)` |

Verdict: **HOLDS, exact.** Bytes equal, sha256 full value begins `00e45ea5` (row's 8-hex prefix), status 200. Corroboration [INFERENCE] that the row's timestamp names the same object: the first response carried `x-cache: HIT, HIT` with `age: 1885`; 20:36:38Z − 1,885 s = 2026-10-22T20:05:13Z, exactly the row's fetch time.

Two further opens, to rule out a stale CDN object masking a change:

```
curl -H 'Cache-Control: no-cache' -H 'Pragma: no-cache' <URL>   # 20:37:41Z
  http=200 bytes=8730  x-cache: HIT, MISS  age: 63  content-length: 8730
  sha256 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
curl '<URL>?cb=20261022T2038Z'                                   # 20:38Z, cache-busted
  http=200 bytes=8730
  sha256 00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
```

`cmp` reports all three bodies identical (`same-as-first(body3)`, `same-as-first(body4)`). The page text has not moved since 20:05:13Z.

Independent cross-checks, all 2026-10-22:

- Rendered HTML page (same URL without `.md`): 20:37:58Z, 200, 603,412 B, sha256 `b50db26e7450a6a3b884fcc3d4f00708a0be31ec5f643d8624e23e0a7acbe64b`. The cited sentences are present there too: `combines their instructions` ×3, `does not define a general precedence order` ×3, `Copilot CLI also uses` ×3 (multiplicity is page payload duplication, not a contradiction). Zero hits for `no longer than N pages`, `size limit` or `character limit`.
- Docs source file `content/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` on `github/docs` `main`: 20:37:15Z, 200, 5,684 B, sha256 `ed823a4fd8e6d1fda61c8971262b2ad92360c1cf420284fad45ac91afa6dd1e8` — same hash the wave-1 seat recorded at 20:05:22Z, so the source tree did not move either. (Unpinned `main`; the row does not claim a commit pin. [INFERENCE] the live branch is acceptable here only because the row pins the rendered bytes instead.)

## 2. Per-line verdicts

Line numbers are of the fetched `.md` body (`body.md`, 8,730 B), matching the row's numbering.

| cited by | line | text observed (quote ≤25 words) | claim it must support | verdict |
|---|---|---|---|---|
| row anchor, note header (`:11-22`) | 11 | "discovers repository and agent instruction files in the standard locations: the repository root, the current working directory" | discovery model behind "which names it reads" | HOLDS |
| row anchor `:11-22`, note `:11-22` | 17 | "Repository-wide instructions, discovered in the standard locations." | `.github/copilot-instructions.md` is a read name | HOLDS |
| row anchor `:11-22`, note `:11-22` | 18 | "Modular repository instructions, discovered in the standard locations but not intermediate directories." | `*.instructions.md` is a read name | HOLDS (condition omitted — defect D3) |
| row anchor `:11-22`, note `:11-22` | 19 | "Agent instructions, discovered in the standard locations." | `AGENTS.md` is read as agent instructions | HOLDS |
| row anchor `:11-22`, note `:11-22` | 20 | "Copilot CLI also uses `.claude/CLAUDE.md`." | "`CLAUDE.md` (also `.claude/CLAUDE.md`)" | HOLDS |
| row anchor `:11-22`, note `:11-22` | 21 | "Agent instructions, discovered in the standard locations." | `GEMINI.md` is read as agent instructions | HOLDS |
| row anchor `:11-22`, note `:11-22` | 22 | "Directories listed in `COPILOT_CUSTOM_INSTRUCTIONS_DIRS`" — "Additional `AGENTS.md` and `*.instructions.md` files." | not claimed (omission — D3) | HOLDS as text |
| row anchor `:30-32`, note `:30` | 30 | "Copilot CLI combines their instructions." and "does not define a general precedence order between these files" | both verbatim claims in the teaches cell and the note's "both" column | HOLDS — both quoted fragments are verbatim |
| row anchor `:30-32` | 32 | "Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with." | nothing in the row states it; it qualifies `*.instructions.md` | HOLDS as text (D3 evidence) |
| row anchor `:48-50`, note `:48` | 48 | "use `@` followed by a relative path to include another file" | `@`-relative-path import expands in `AGENTS.md` / `CLAUDE.md` (and also `copilot-instructions.md`) | HOLDS (teaches omits the third file — D4) |
| row anchor `:48-50`, note `:50` | 50 | "File references are not expanded in `GEMINI.md` or `*.instructions.md` files." | imports do not expand in `GEMINI.md` | HOLDS (second excluded class omitted — D4) |
| row anchor `:105` | 105 | "Changes you make to custom instructions files are not immediately available for use in active CLI sessions" | no statement in the row uses it | HOLDS as text; **unbound citation — D2** |

Section labels match the page exactly: `## Types of custom instructions` :7, `## How multiple instruction files interact` :28, `### Referencing other files` :46, `## Custom instructions in use` :103. No heading typo.

Knowledge-entry lines, checked one by one:

- `source: S048 (…, :11-32, 48-50)` — the union covers every cited line above; HOLDS.
- note row 30, "names read": "`AGENTS.md`, `CLAUDE.md` (also `.claude/CLAUDE.md`), `GEMINI.md`, `.github/copilot-instructions.md` and others (`:11-22`)" — every named file is in the cited range; "and others" correctly covers lines 15, 16 and 22. HOLDS.
- note row 30, "both in one directory": '"Copilot CLI combines their instructions" with no precedence order (`:30`)' — HOLDS verbatim. The note's column header says "in one directory" while the page's subject is "multiple applicable user-level and repository instruction files" (no directory wording); see observation O1.
- note row 30, redirect: "`@` plus a relative path in `AGENTS.md`, `CLAUDE.md` or `copilot-instructions.md` (`:48`); not in `GEMINI.md` (`:50`)" — both exact. HOLDS; line 50 also excludes `*.instructions.md`, which the note drops (D4, note is incomplete, not wrong).
- note §2 "A `CLAUDE.md` whose redirect line is `@AGENTS.md` is expanded by … Copilot CLI (S048)" — line 48 documents the generic form only (D5).
- note §1 "VS Code, Copilot CLI and Cursor read both (S047–S049)" — supported by line 30's "combines". HOLDS.
- note §4 "`GEMINI.md` and `.github/copilot-instructions.md` are further names" — lines 21 and 17. HOLDS.
- note §6 "Copilot CLI: no rule-file size limit documented" — grep of the 8,730 B for `size|limit|characters|too large|truncat` returns zero hits; the HTML page likewise has none. HOLDS for this page.
- note §5 (dated text) — the note does not cite S048 there; the page states no dating rule, so no conflict.

## 3. Defects (severity, fix)

**D1 — low — anchor names a file that does not exist on the source side, with render-side line numbers.**
The anchor cell and the note-lessons gate write `copilot-cli-custom-instructions.md:11-22`. That filename is the wave-1 seat's scratch name for the fetched render (`ScribeCopilotCli.md:15`, `:165` lists it under `…/fetch/`), not a docs file: `raw.githubusercontent.com/github/docs/main/…/customize-copilot/copilot-cli-custom-instructions.md` → **404 (14 B)**, while `…/add-custom-instructions.md` → **200 (5,684 B, `ed823a4f…`)**. The source file also carries 16 lines of frontmatter and a `{% data reusables.copilot.custom-instructions-path %}` include at source `:67`, so render and source line numbers diverge: render `:11` = source `:24`, `:30` = `:43`, `:48` = `:61`, `:50` = `:63`, `:105` = `:71`. The cited numbers are correct **only** against the URL's served bytes; a reader following the anchor's filename cannot reproduce them. Other round-53 docs rows name either the URL's own last segment (S043 `memory.md`, S044 `agents-md.md`, S045 `rules.mdx`, S049 `rules.md`, S050 `instructions.md`) or a pinned source file (S047 `custom-instructions.md` at `fd64d648`); S048's name is neither — it is the scratch name of the downloaded render. Fix: drop the filename and say "served markdown (:11-22)" as the note header already effectively does, or cite the source file at a commit with the +13/+34 offsets. Same string is at `corpus/lessons/round-53.md:28`, so the fix must cover both.

**D2 — low — `:105` is an unbound anchor citation.**
No clause of the teaches cell rests on line 105; the fact it supports (edits are not live in a session) appears only in the seat report, `ScribeCopilotCli.md:72` §2.5, as evidence that the vendor documents *session* transience, not dated text. Two acceptable fixes: add the session-reload fact to the teaches cell (it is the one place the page touches transience, relevant to `alwayson.04`), or remove `:105` so every anchor line backs a stated claim. As written the anchor overstates what the row uses, which is the same class of looseness round 53 is policing.

**D3 — low — the name list is not the always-on list, and it is not complete.**
Row scope is "which always-on rule-file names GitHub Copilot CLI reads". Line 11 inside the row's own cited range says modular files are "path-specific—a file with an `applyTo` value applies only to matching files", and line 32 repeats that they load only on a match; the teaches cell nevertheless lists `*.instructions.md` flat beside the always-on names and without that condition. Conversely the cell lists only project-level names while line 15 (`$HOME/.copilot/copilot-instructions.md`), line 16 (`$HOME/.copilot/instructions/**/*.instructions.md`) and line 22 (`COPILOT_CUSTOM_INSTRUCTIONS_DIRS`) are also names the CLI reads, unmentioned. The note's table column is bounded ("project level") and says "and others", so the note is safe; the SOURCES row is not. Fix: append "(the `*.instructions.md` files are path-gated by `applyTo`)" and add "plus user-level `$HOME/.copilot/…`" or say "project-level names".

**D4 — low — the import sentence drops one included file and one excluded class.**
Line 48 includes `.github/copilot-instructions.md` alongside `AGENTS.md` and `CLAUDE.md`; line 50 excludes `*.instructions.md` alongside `GEMINI.md`. The row's "(…but not in `GEMINI.md`)" is true but reads as exhaustive when the same line names a second exclusion, and it leaves out the third file that does expand. The note's redirect cell repairs the first omission (it names `copilot-instructions.md`) but keeps the second. Fix: "…in `.github/copilot-instructions.md`, `AGENTS.md` and `CLAUDE.md`, but not in `GEMINI.md` or `*.instructions.md`".

**D5 — low — the note states an inference as documented.**
Note §2: "A `CLAUDE.md` whose redirect line is `@AGENTS.md` is expanded by Claude Code (S043) and Copilot CLI (S048)" (identical at `c775d68` and in the working tree; lines 45-46). For S048, line 48 documents `@` + relative path, never the token `@AGENTS.md`; the seat report itself marks that step `[INFERENCE]` (`ScribeCopilotCli.md:97`). The working-tree edit adds an `[INFERENCE]` marker on the same paragraph, but it attaches to the clause about the clients that do *not* expand the import (VS Code, Cursor), not to this expansion claim. The step is safe, but the entry still states a documented fact where the seat kept a marker. Fix: add `[INFERENCE]` or phrase it as "line 48 makes `@AGENTS.md` an instance of the documented `@`+relative-path form".

**D6 — low — `used-by` omits the lessons gate, which is not yet in the judged revision.**
`corpus/lessons/round-53.md:28` reproduces this row's quote and location, but S048's `used-by` cell lists only `corpus/knowledge/alwayson-rule-files-round53.md`. That lessons file is untracked at `c775d68` (`git cat-file -e c775d68:corpus/lessons/round-53.md` fails; `git status --porcelain` shows `?? corpus/lessons/round-53.md`), so the omission is expected at the judged revision and becomes a gap only once the file lands: rows S040–S042 set the precedent of listing `corpus/lessons/round-52.md` beside the entry, and S043–S050 would all need the round-53 lessons pointer added with it.

**O1 — observation, not a defect.** Row scope and note column say "in one directory"; line 30's rule is stated for "multiple applicable user-level and repository instruction files" across the standard locations. Combining all applicable files entails combining two that share a directory, so the narrowing is true a fortiori, but the page's unit is the discovery set, not the directory. Say "several applicable at once" if the wording is revised.

**O2 — observation.** No instrument consumes S048: `grep -rniE 'copilot|S048' verifiers/*.py` finds Copilot only in `check_mcp_instructions.py`, `check_overlap_levers.py` and `check_correction_sweep.py` (none about always-on files), and `verifiers/verify_alwayson.py` cites no source row. So none of D1–D6 can move C2's `2 of 8`; they are provenance and readability defects only.

## 4. Unknowns

- Whether docs.github.com will keep serving the same bytes after its CDN TTL; the row's `recheck: 90d` is the only guard, and the page is unpinned. Nothing in this check can settle that.
- The served `.md` and the live source `main` agree today; no pinned commit for the CLI page exists, so I cannot replay the 20:05:13Z state independently of the hash the row records. The hash match plus the `age: 1885` arithmetic is the available proof.
- The docs source path was tested at the one directory the wave-1 seat reported; I did not enumerate the whole `github/docs` tree for a stray `copilot-cli-custom-instructions.md` elsewhere (GitHub code search needs auth; the REST tree call was already 403 for the wave-1 seat). The 404 at the page's own source directory is the evidence used.
