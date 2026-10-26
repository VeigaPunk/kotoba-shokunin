# ExecSrcScriptsR74 — source opening for C1: `agentskills.io/skill-creation/using-scripts.md`

Round 74, wave 1, lane kotoba. Seat: `ExecSrcScriptsR74`. Base `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908`,
plan frozen at `329e7d91d7d750031c35d264f0e34af1d0ce8385` (lane tip at the time of writing; `git rev-parse HEAD`
in the lane returns that sha, working tree clean apart from untracked `.ufo/waves/round-74/*` dispatch files).
No lane file, no `shokuknow` file, no fleet file was modified. One `mktemp -d` scratch
(`/tmp/k74w1-ExecSrcScriptsR74.YxPu`) held every probe and was deleted before this report was filed.

## Verdict

**The page exists, is live, and is byte-unchanged since the staged read.** Staged row **S236 is re-opened and its
quarantine reason is falsified by an observation, not by an argument**: the URL answers
`HTTP 200`, `12 078 B`, `sha256 2cd77271…` on 2026-10-25 — the same byte count the staged row records from
2026-10-23. The staged quote is located verbatim at line 9. The page's upstream source is
`docs/skill-creation/using-scripts.mdx`, and its bytes at the lane's registry anchor commit `69ef37e` are
**byte-identical** to its only touching commit `6102aff`; `69ef37e` is **still `refs/heads/main` today**
(`git ls-remote`, 2026-10-25T22:37:34-03:00). The live `.md` equals that `.mdx` **modulo markup**, and I name every
byte class the shaping removed. 12 rules a skill author acts on are listed with located quotes. Every staged claim
that rests on this page is located except **one clause**, which I refuse: `rather than for a human` — the word
`human` occurs **0 times** in the page. A census-conformant registry row is drafted and shape-proved (`NF=13`,
`validate` → `ok`, exit 0).

One conflict must be resolved by the L1 before the row lands: this seat's assignment says `status queued`, the
frozen C1 predicate (b) requires `status mined`. `queued` cannot satisfy (b) — measured, not judged. See § 7.

---

## 1. Fetch record

| # | URL requested | HTTP | final URL (redirects) | bytes | sha256 | `date -I` |
|---|---|---|---|---|---|---|
| A | `https://agentskills.io/skill-creation/using-scripts.md` | 200 | same (no redirect; `url_effective` printed the requested URL) | 12 078 | `2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f` | 2026-10-25 |
| B | `https://agentskills.io/skill-creation/using-scripts` (no `.md`) | 200 | same | 432 113 | `0c7bfaeba8f0cfca54546385bf6c8887a3dc8db97f05564ff18feb7f2556a2bc` | 2026-10-25 |
| C | `https://agentskills.io/llms.txt` (docs index) | 200 | same | 1 374 | `d9b01a3a13b79bb04ee0bc25125087d92e393f0c7e8f028c4c5fa4c217f1fbfb` | 2026-10-25 |

Command (A; B and C are the same form with the other URL):

```
curl -sL --max-time 60 -A 'Mozilla/5.0' \
  -w '\n__HTTP:%{http_code} URL:%{url_effective} SIZE:%{size_download}\n' \
  -o using-scripts.md https://agentskills.io/skill-creation/using-scripts.md
```

Observed:

```
__HTTP:200 URL:https://agentskills.io/skill-creation/using-scripts.md SIZE:12078
2cd7727106b423a758b4b6b1ab3545da74845a98e68e6718279846f89d62ad1f  using-scripts.md
12078 using-scripts.md
```

Route B exists and carries the same prose (cross-check, not the citation):

```
grep -c 'Skills can instruct agents to run shell commands and bundle reusable scripts in a' using-scripts-nomd.html
2
```

The docs index advertises the page and bounds the `skill-creation/` set at **5** pages:

```
grep -n 'using-scripts' llms.txt          ->  12:- [Using scripts in skills](https://agentskills.io/skill-creation/using-scripts.md): How to run commands and bundle executable scripts in your skills.
grep -c 'skill-creation/' llms.txt        ->  5
grep -o 'skill-creation/[a-z-]*\.md' llms.txt | sort
   skill-creation/best-practices.md
   skill-creation/evaluating-skills.md
   skill-creation/optimizing-descriptions.md
   skill-creation/quickstart.md
   skill-creation/using-scripts.md
```

Lane-side coverage at the tip (recomputed, not quoted from the plan):

```
grep -cE 'agentskills\.io/skill-creation' corpus/SOURCES.md   ->  4     (S209, S210, S212, S213)
grep -c 'using-scripts' corpus/SOURCES.md                    ->  0
```

So the lane holds rows for **2 of the 5** `skill-creation/` pages (`evaluating-skills` twice, `optimizing-descriptions`
twice) and **0** for `using-scripts`. The do-nothing figure the plan freezes as `held at base: 0` reproduces at the
plan tip — the phrase sweep is empty:

```
grep -nE 'one-off commands|pipx run|uvx ruff|npx eslint@9|bunx' SKILL.md PROVINCE.md corpus/SOURCES.md
   (no output)
```

## 2. Upstream source identity — and whether `69ef37e` is still the head

```
curl -sL ... 'https://api.github.com/repos/agentskills/agentskills/commits?path=docs/skill-creation/using-scripts.mdx&per_page=5'
python3 -c "..."   # print sha, committer date, subject
   6102affec88b137de8e213987aa1c49fcfde48a7  2026-02-27T21:52:36Z  Add "Using scripts" guide for skill creators (#196)
   (1 entry — this is the ONLY commit that has touched the path)
```

```
curl -sL ... https://api.github.com/repos/agentskills/agentskills/commits?per_page=3
   69ef37e9424c0a7ea9dd2293b559e43ec8176379  2026-08-09T20:36:04Z  docs: add OpenClaw to client showcase (#492)
   29a8a89f30760b95b9953a9317b63345f73646af  2026-08-09T17:34:08Z  Merge pull request #491 ...
```

```
timeout 90 git ls-remote https://github.com/agentskills/agentskills refs/heads/main
   69ef37e9424c0a7ea9dd2293b559e43ec8176379	refs/heads/main
```

```
raw.githubusercontent.com/agentskills/agentskills/{6102aff,69ef37e}/docs/skill-creation/using-scripts.mdx
   6102aff: HTTP 200, 12405 B, 298 lines, sha256 064185783e0f848a9cad2cf5866902d5c46cbddc71235a124b3abbf3ebd7c02d
   69ef37e: HTTP 200, 12405 B, 298 lines, sha256 064185783e0f848a9cad2cf5866902d5c46cbddc71235a124b3abbf3ebd7c02d
```

**Answer to the question posed in the assignment.** `agentskills/agentskills@69ef37e` (the anchor S212/S213 use)
**is still the head of the repository** — `refs/heads/main` resolved to it today, 2026-10-25T22:37:34-03:00 — and
the docs page `using-scripts.mdx` is **byte-identical** at that head and at its only touching commit `6102aff`
(same sha256, same byte count). The path therefore has not moved since 2026-02-27, and the anchor is not stale.

**`.md` vs `.mdx` — equal modulo markup, with the classes named.** Content-line comparison after removing exactly
these classes: frontmatter (`title`, `sidebarTitle`, `description`), `<Tabs>`/`<Tab title="…">` wrappers (their
titles surface as `**uvx**` etc. on the live page), the 4-space indentation inside tab bodies,
`- ` list bullets (live: `* `), ` theme={null}` on fence info strings, `>` blockquote prefixes, and the injected
`> ## Documentation Index` block.

```
mdx content lines 189 / live content lines 191 / remaining diff lines 4
-* **State prerequisites** ... [`compatibility` frontmatter field](/specification#compatibility-field).
+* **State prerequisites** ... [`compatibility` frontmatter field](https://agentskills.io/specification#compatibility-field).
+[!NOTE]
+>
```

Two residual differences only: (i) the mdx uses a site-relative link and the served `.md` absolutizes it to
`https://agentskills.io/specification#compatibility-field`; (ii) the `<Note>` MDX component renders as a
`[!NOTE]` blockquote. Nothing else diverges — so the live page is current with the repository, not a stale export.

## 3. The rules a skill author acts on (12, each quoted at its line)

Snapshot: `.ufo/waves/round-74/w1/build/ExecSrcScriptsR74/snapshot.md` — the fetched bytes copied verbatim
(304 lines, 12 078 B, whitespace preserved, ≤ 300 KB) and pinned in `snapshot.sha256`;
`sha256sum -c snapshot.sha256` → `snapshot.md: OK`.

Commands and observed output (one batch; the file is the saved snapshot):

```
for n in 9 13 50 90 91 92 96 237 254 284 295 299 302 304; do printf 'L%s|' "$n"; sed -n "${n}p" using-scripts.md; done
L9|Skills can instruct agents to run shell commands and bundle reusable scripts in a `scripts/` directory. This guide covers one-off commands, self-contained scripts with their own dependencies, and how to design script interfaces for agentic use.
L13|When an existing package already does what you need, you can reference it directly in your `SKILL.md` instructions without a `scripts/` directory. Many ecosystems provide tools that auto-resolve dependencies at runtime.
L50|* Pin versions with `npx package@version` for reproducibility.
L90|* **Pin versions** (e.g., `npx eslint@9.0.0`) so the command behaves the same over time.
L91|* **State prerequisites** in your `SKILL.md` (e.g., "Requires Node.js 18+") rather than assuming the agent's environment has them. For runtime-level requirements, use the [`compatibility` frontmatter field](https://agentskills.io/specification#compatibility-field).
L92|* **Move complex commands into scripts.** A one-off command works well when you're invoking a tool with a few flags. When a command grows complex enough that it's hard to get right on the first try, a tested script in `scripts/` is more reliable.
L96|Use **relative paths from the skill directory root** to reference bundled files. The agent resolves these paths automatically — no absolute paths needed.
L237|This is a hard requirement of the agent execution environment. Agents operate in non-interactive shells — they cannot respond to TTY prompts, password dialogs, or confirmation menus. A script that blocks on interactive input will hang indefinitely.
L254|`--help` output is the primary way an agent learns your script's interface. Include a brief description, available flags, and usage examples:
L284|Prefer structured formats — JSON, CSV, TSV — over free-form text. Structured formats can be consumed by both the agent and standard tools (`jq`, `cut`, `awk`), making your script composable in pipelines.
L295|**Separate data from diagnostics:** send structured data to stdout and progress messages, warnings, and other diagnostics to stderr. This lets the agent capture clean, parseable output while still having access to diagnostic information when needed.
L299|* **Idempotency.** Agents may retry commands. "Create if not exists" is safer than "create and fail on duplicate."
L302|* **Meaningful exit codes.** Use distinct exit codes for different failure types (not found, invalid arguments, auth failure) and document them in your `--help` output so the agent knows what each code means.
L304|* **Predictable output size.** Many agent harnesses automatically truncate tool output beyond a threshold (e.g., 10-30K characters), potentially losing critical information. ...
```

Word counts are `len(quote.split())` over the exact strings below; every one is inside 6–25.
`byte-exact` is claimed only where the quote is a literal substring of `snapshot.md` (verified by `in`
over the saved bytes); three quotes drop the `**` emphasis pairs and the leading `* ` bullet, and say so.

| # | line | quote (words) | rule tokens | action an author performs |
|---|---|---|---|---|
| 1 | 9 | “Skills can instruct agents to run shell commands and bundle reusable scripts in a `scripts/` directory.” (16, byte-exact) | `scripts/` | Decide the deterministic half of the skill: a documented command list, or one bundled script per reusable step. |
| 2 | 13 | “When an existing package already does what you need, you can reference it directly in your `SKILL.md` instructions without a `scripts/` directory.” (22, byte-exact) | `SKILL.md`, `scripts/` | Before bundling anything, check whether an existing package does the job; if so, cite the command in the body and ship no script. |
| 3 | 50 | “Pin versions with `npx package@version` for reproducibility.” (7, byte-exact) | `npx package@version` | Write every one-off command with an explicit version, never a bare package name. |
| 4 | 90 | “Pin versions (e.g., `npx eslint@9.0.0`) so the command behaves the same over time.” (13; bytes dropped: the two `**` pairs and the leading `* `) | `npx eslint@9.0.0` | Same rule stated as the page's own summary — the version pin buys temporal stability, so state *why* next to the command. |
| 5 | 91 | “State prerequisites in your `SKILL.md` (e.g., "Requires Node.js 18+") rather than assuming the agent's environment has them.” (17; bytes dropped: two `**` pairs, leading `* `) | `SKILL.md`, `"Requires Node.js 18+"` | Declare the runtime the command needs in the body instead of assuming it; for runtime-level needs, put it in the `compatibility` frontmatter field. |
| 6 | 92 | “When a command grows complex enough that it's hard to get right on the first try, a tested script in `scripts/` is more reliable.” (24, byte-exact) | `scripts/` | Apply the crossover test: a few flags → inline one-off command; hard-to-get-right → tested script. |
| 7 | 96 | “Use relative paths from the skill directory root to reference bundled files.” (12; bytes dropped: two `**` pairs) | `skill directory root` | Reference bundled files by skill-root-relative path (`scripts/validate.sh`), never by absolute path. |
| 8 | 237 | “A script that blocks on interactive input will hang indefinitely.” (10, byte-exact) | `interactive input` | Remove every prompt from a bundled script: take input from flags, env vars or stdin, and fail with guidance when a flag is missing. |
| 9 | 254 | “`--help` output is the primary way an agent learns your script's interface.” (12, byte-exact) | `--help` | Ship a `--help` with a one-line description, the flags and usage examples — this is the interface as the agent sees it. |
| 10 | 284 | “Prefer structured formats — JSON, CSV, TSV — over free-form text.” (11, byte-exact) | `jq`, `cut`, `awk` (line 284, second sentence) | Emit JSON/CSV/TSV so the output is machine-consumable and pipeable, not whitespace-aligned tables. |
| 11 | 295 | “send structured data to stdout and progress messages, warnings, and other diagnostics to stderr” (14, byte-exact) | `stdout`, `stderr` | Split channels: data on stdout, diagnostics on stderr, so the agent parses clean bytes and still reads warnings. |
| 12 | 302 | “Use distinct exit codes for different failure types (not found, invalid arguments, auth failure)” (14, byte-exact) | `exit codes`, `--help` | Give each failure class its own exit code and document the codes in `--help`. |

Three more agent-interface rules in the same section are worth tokens for the entry (each byte-exact, all inside
the snapshot): line 299 “Create if not exists” is safer than “create and fail on duplicate.” (idempotency, since
agents retry); line 301 “a `--dry-run` flag lets the agent preview what will happen.”; line 304 “support flags like
`--offset`” / “pass an `--output` flag” (harnesses truncate output around 10–30K characters).

## 4. Staged claims grounded against the live page

Sources re-read: `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` line 40 (row S236),
`/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-script-craft-rules.md` (44 lines).
`spec-description-trigger-discipline.md` cites S231 and S232 only, so **no claim in it rests on this page** — it is
outside this seat's grounding duty.

| staged claim (verbatim fragment) | verdict | observed fact |
|---|---|---|
| frontmatter: “fetched as `.md` 12 078 B on 2026-10-23” | **LOCATED** | today's fetch: `SIZE:12078`, `sha256 2cd77271…` — the byte count is unchanged across two days |
| quote: “Skills can instruct agents to run shell commands and bundle reusable scripts in a `scripts/` directory.” | **LOCATED**, byte-exact | snapshot line 9 |
| “One-off commands” and “Using scripts in skills” opening paragraph (anchor) | **LOCATED** | `## One-off commands` at line 11; opening paragraph at line 9 |
| “reference an existing package directly (uvx, pipx, npx, bunx) when it already does the job” | **LOCATED** | line 13 (“you can reference it directly … without a `scripts/` directory”); worked examples at lines 20 (`uvx ruff@0.8.0 check .`), 32 (`pipx run 'black==24.10.0' .`), 44 (`npx eslint@9 --fix .`), 57 (`bunx eslint@9 --fix .`); the page also covers `deno run` (line 69) and `go run` (line 81) |
| “pin versions (`npx eslint@9 --fix .`) for reproducibility” | **LOCATED** | line 50 states the rule; line 44 shows the pinned `npx` form |
| “with self-contained scripts carrying their own dependencies” | **LOCATED** | `## Self-contained scripts` line 127; PEP 723 block lines 137-142; `uv run scripts/extract.py` line 153 |
| “design a script's interface for an agent to call” | **LOCATED** (section heading + body) | `## Designing scripts for agentic use` line 231; line 233 “A few design choices make scripts dramatically easier for agents to use.” |
| “**rather than for a human**” (same clause) | **ABSENT — refused** | `grep -ic 'human' snapshot.md` → `0`. The page never frames the contrast as agent-vs-human; the antithesis is the staged author's construction, not the page's. The rule survives; the wording does not. |
| staged entry: “S236) is the last unheld page of the `skill-creation/` set” | **ABSENT — refused** | (i) it is a claim about the lane, not about the page, so the page cannot ground it; (ii) it contradicts the entry's own second `source:` line, which cites S237 `quickstart.md` as also unheld (`spec-script-craft-rules.md:3-4`); (iii) observed: the index lists 5 pages and the lane holds rows for 2 (S209/S210/S212/S213), so **3** are unheld, not 1 |
| package row: “the page is not held by the lane and completes the `skill-creation/` set” | **LOCATED for the lane half** | `grep -c 'using-scripts' corpus/SOURCES.md` → `0` (not held). “Completes the set” is true only at package granularity: the package stages 4 distinct pages (S231 optimizing, S232 best-practices, S236 using-scripts, S237 quickstart) and the lane already holds the fifth (`evaluating-skills`) |
| package row status `mined`, `opened 2026-10-23`, `recheck 90d — re-fetch … (ran 2026-10-23)` | **not census-conformant as written** | probed verbatim in a minimal registry: `file	E09	S236 recheck=90d — re-fetch the `.md` and confirm the one-off-command list and the script-interface rules are unchanged (ran 2026-10-23)` and `file	E11	S236 missing used-by corpus/knowledge/spec-script-craft-rules.md` — the prose in the `recheck` cell and the staged entry path must both be normalised |

Quarantine register, read at the lane (`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-74/assimilation/quarantine-slice:8`):

```
 S236`   the cited source could not be fetched, so no quote was checked
```

That reason is **observed false today** for this page (200 / 12 078 B / quote located at line 9). S236 is not in the
lane-id collision set (`grep -n 'S23[0-9]' collisions` → no match), so it needs only the normalisation above.

## 5. Row draft

`.ufo/waves/round-74/w1/build/ExecSrcScriptsR74/row.md` — primary row with status `mined` (frozen C1 predicate (b)),
plus a labelled `queued` alternative. Cell-by-cell grounding is in that file. Shape proof — the row was extracted
from `row.md`, `S<next>` substituted to `S223` (next free: 148 rows, max id `S222`), and run through the fleet census:

```
awk -F'|' 'NR==7{print NF}'  ->  13            (11 cells + leading/trailing pipe)
scripts/sources-census.sh validate --file .../corpus/SOURCES.md
   file	ok	/tmp/k74w1-ExecSrcScriptsR74.YxPu/fix3/corpus/SOURCES.md
   EXIT=0
```

## 6. Falsifiers run against the C1 predicate's own assumptions

| probe | command | observed |
|---|---|---|
| lane registry is census-clean at the plan tip | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | `kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`, `EXIT=0`, with the 20 `W04` duplicate-URL warnings only (S018, S019, S021, S054-S056, S065, S086, S103, S104, S106, S110, S111, S114, S115, S118, S207, S208, S212, S213) — matches the plan's `census-before.txt` |
| a row appended **after** the registry table | `printf ... >> corpus/SOURCES.md; validate --file …` | `file	E12	S999 row outside Registry section` — append inside the table or the `used-by` is never even checked |
| `mined` + `used-by` path absent (minimal registry, 3 arms) | `validate --file` on `fix2` | A `mined`/absent → `file	E11	S900 missing used-by corpus/knowledge/spec-skill-creation-craft-round74.md`, `EXIT_A=1`; B `queued`/absent → `file	ok`, `EXIT_B=0`; C `mined`/present → `file	ok`, `EXIT_C=0` |
| staged row verbatim (S236 cells) | `validate --file` on `fix4` | `E09` (prose recheck cell) + `E11` (staged entry path), exit 1 |
| the page's own kind/tier vocabulary | `grep -n 'kind !~' scripts/sources-census.sh` | `if (kind !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/)` → `docs` valid; statuses `queued\|mined\|rejected` |

**Consequence for landing (measured, not inferred).** C1 predicate (b) demands `status mined` *and* a `used-by`
naming the frozen entry, while `E11` fires for a `mined` row whose `used-by` path is not on disk. The registry row and
`corpus/knowledge/spec-skill-creation-craft-round74.md` must therefore land in the **same commit** (or the entry
first). Neither file exists in the lane yet — `ls corpus/knowledge/ | grep -E '^spec-\|round74'` → no match.

## 7. Risks and blockers

1. **Assignment vs frozen plan on `status` (needs one L1 token).** The assignment says draft with `status queued`;
   frozen plan § C1 predicate (b) says the page is backed only when its row is `status mined`, and the plan's own
   shortcut list names “rows appended with status `queued`” as a world that must score below 3. A `queued` row is a
   guaranteed `held`, so `row.md` carries `mined` as primary and `queued` as a labelled alternative. If the L1 flips
   it back to `queued`, C1 cannot reach `3 of 3` for this page.
2. **`E11` ordering** (§ 6) — the row cannot land alone.
3. **C1 predicate (c) needs a second copy of the snapshot.** My snapshot is at
   `.ufo/waves/round-74/w1/build/ExecSrcScriptsR74/snapshot.md`; the frozen predicate reads
   `.ufo/waves/round-74/snapshots/` and a `snapshots/MANIFEST.sha256` pin. `row.md` gives the exact copy + pin
   commands and the hash (`2cd77271…`). Snapshot bytes I did not alter; `sha256sum -c` → `snapshot.md: OK`.
4. **Scope of this page's tier A.** It is A for *this page's own guidance* (what the format maintainers instruct an
   author to do). It is **not** a measurement of any client's behaviour: the page says what a skill *should* do
   (e.g. pin versions, avoid prompts) and nowhere measures whether a given harness truncates at 10–30K characters —
   line 304 says “Many agent harnesses … (e.g., 10-30K characters)”, which is the page's claim, not a measurement.
   An entry that presents it as measured host behaviour would be a scope error.
5. **Staged-entry defects to route, not silently absorb** (§ 4): the “rather than for a human” clause (0 occurrences
   of `human`), “the last unheld page” (3 of 5 unheld; contradicted by the entry's own S237 line), and the
   census-invalid `recheck`/`used-by` cells of the staged row. Q62 applies: each refusal rests on the observed fact
   named above, and a correction is an appended notice or a new row, never a rewrite of the staged text (which is
   read-only to this seat in any case).
6. **Not observed / not claimed.** I did not measure any client's actual behaviour with a bundled script, did not
   run any lane gate (no `check_spec_craft.py` exists yet in `verifiers/` — `ls verifiers/ | grep spec_craft` → no
   match; the C1 counter is another seat's build), and did not verify whether wave-2 reviewers agree that the 12
   rules are the strongest; that selection is a judgement, and the plan assigns the truth-of-a-rule judgement to
   named wave-2 seats.

## 8. Hand-off

- Files written (deliverable drafts, mine): `.ufo/waves/round-74/w1/build/ExecSrcScriptsR74/snapshot.md`,
  `snapshot.sha256`, `row.md`; this report.
- Checks the L1 should run at integration: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
  (expect `ok`, exit 0) after appending the row **and** landing the entry in the same commit;
  `sha256sum -c .ufo/waves/round-74/snapshots/MANIFEST.sha256`; then the round's C1 counter and the tip battery.
- Tool installs/upgrades: **none** (no `pacman`, no `uv tool`, no `npx`; the task needed only `curl`, `git
  ls-remote`, `grep`, `awk`, `sha256sum`, `python3`).
- Scratch: `/tmp/k74w1-ExecSrcScriptsR74.YxPu` (fix/fix2/fix3/fix4 fixture registries, fetched pages, API JSON)
  deleted; no fixture repo was initialised, so no commit was made anywhere.
