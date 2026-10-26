# ExecIdNormalize — round 73, wave 1 (assimilation scratch pipeline)

Seat: `ExecIdNormalize`. Lane `kotoba-shokunin`, base `072048f`, lane HEAD during the work
`ac8fc59` (plan, addendum 1 and the wave-1 spec are the only commits above the base; read-only
`git log --oneline -3`). Nothing tracked was modified: `git status --porcelain` shows only untracked
`.ufo/waves/round-73/…` paths.

## Verdict

The ten Chinese-vendor staged rows are built in the lane's 11-column schema, renumbered **by document**
(staged → lane `S217`–`S226`), and the validated mirror passes:

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
      --file .ufo/waves/round-73/assimilation/validate/corpus/SOURCES.md
file	W04	S018 duplicate url agentskills.io/specification across scopes
… (19 more W04 lines, the same 20 the base registry emits)
file	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/assimilation/validate/corpus/SOURCES.md
[exit 0]
```

`152` registry rows (base `142` + 10), `status.mined` `134 → 144`, tier.B `10 → 20`, no `E` line, no
duplicate id. The guard is proven once on a one-space-indented row; both transformations are shown able
to fail (append unchanged → `6 × E03` + `10 × E09`). Five anchor defects in the package rows are named
with line pointers. No tool installed; four network fetches recorded in §7.

## 1. Guard proof — the extraction pattern and the maintained parser agree on indentation

Fixture `assimilation/guard-proof/registry.md` holds one column-zero row (`S001` line 12) and one
**one-space-indented** row (` | S234` line 13):

```
$ grep -nE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' -o -- …/guard-proof/registry.md
12:| S001
13: | S234
$ grep -nE '^\|[[:space:]]*S[0-9]{3,}' -o -- …/guard-proof/registry.md
12:| S001
```

The column-zero-only pattern loses the indented row; the 0–3-space pattern keeps both. The census
parses the indented row as a row (`file ok`, exit 0, `S234` counted), and the four-space boundary
fixture is ignored by **both** the pattern and the parser (only `S001` counted), which matches
`sources-census.sh:40-41` ("accepts 0–3 leading ASCII spaces … 4 or more spaces are indented code").
Mutants prove the parser still refuses what the pipeline must prevent:

```
$ … sources-census.sh validate --file …/mutant-e03.md     # staged id appended unchanged
file	E03	S214 duplicate id
[exit 1]
$ … sources-census.sh validate --file …/mutant-e04.md     # same document twice in one scope
file	E04	S002 duplicate url guard-proof.example/same-doc within scope same scope
[exit 1]
```

Full transcript: `assimilation/guard-proof/proof.txt` (8 commands, 69 lines); `mirror-e03.txt` is §4.

## 2. What the transformation changes (four cells; every other cell is package bytes)

| cell | change | why |
|---|---|---|
| `id` | by document → lane id | 14 package ids collide with the lane's own (`S203`–`S216`) |
| `recheck` | `NNd — prose` → `NNd`; prose kept as the Gate note in `gate-notes.md` | E09: the staged prose is not a cadence |
| `used-by` | → `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` (six cn rows) / `corpus/lessons/round-73.md` (four Qwen rows) | see §8 |
| `status` | already `mined` — kept | C1 predicate (b) |

Checked for every row: exactly 11 cells (`NF=13`), no literal or escaped `|` in any cell (a `\|` would
raise `NF`), `opened` a valid past ISO date (`2026-10-23` for all ten, carried from the staged row),
no new id already present in the lane registry, no block URL already in the lane registry (114
distinct registry URLs compared), no duplicate URL inside the block. `opened` is not bumped to
`2026-10-25`: that is this round's re-open date and belongs in the entry's `verified-at:`.

## 3. Id lists and collisions — re-derived, not accepted

```
$ wc -l < .ufo/waves/round-73/assimilation/{reg-ids,staged-ids,collisions}
142
188
14
$ comm -12 <(sort -u reg-ids) <(sort -u staged-ids) | wc -l
14
$ comm -12 …                       # the 14
S203 S204 S205 S206 S207 S208 S209 S210 S211 S212 S213 S214 S215 S216
$ diff <(sort -u reg-ids) <(grep -oE '^ {0,3}\|[[:space:]]*S[0-9]+' corpus/SOURCES.md | tr -d ' |' | sort -u)
(no output — reg-ids is the live registry's id set)
$ diff <(sort -u staged-ids) <(grep -oE '^\|[[:space:]]*S[0-9]+' …/SOURCES.append.md | tr -d ' |' | sort -u)
(no output — staged-ids is the package registry's id set)
```

Lane ids in use: `142`, max `S216`. The lane does not fill its low gaps (`S092`, `S116`, `S125`–`S197`
are unused in `S001`–`S216`), so "next free" is max+1: **`S217`** — the frozen hint is reproduced.
`grep -oE '^ {0,3}\|[[:space:]]*S[0-9]+' corpus/SOURCES.md | sort -u | tail -3` → `S214`, `S215`,
`S216`.

## 4. Renumber map (by URL; `renumber-map.tsv` is the machine copy)

| staged | lane | document | recheck | used-by |
|---|---|---|---|---|
| S205 | S217 | `https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/` | 30d | `corpus/lessons/round-73.md` |
| S206 | S218 | `https://qwenlm.github.io/qwen-code-docs/zh/users/features/skills/` | 30d | `corpus/lessons/round-73.md` |
| S207 | S219 | `https://qwenlm.github.io/qwen-code-docs/ja/users/features/skills/` | 30d | `corpus/lessons/round-73.md` |
| S208 | S220 | `https://qwenlm.github.io/qwen-code-docs/zh/blog/updates/weekly-update-2026-02-09` | 90d | `corpus/lessons/round-73.md` |
| S214 | S221 | `https://docs.trae.cn/ide_skills` | 60d | entry |
| S216 | S222 | `https://www.codebuddy.ai/docs/zh/ide/Features/Skills` | 60d | entry |
| S217 | S223 | `https://www.codebuddy.ai/docs/zh/cli/skills` | 60d | entry |
| S218 | S224 | `https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md` | 60d | entry |
| S219 | S225 | `https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html` | 60d | entry |
| S221 | S226 | `https://docs.bigmodel.cn/cn/managed-agents/skills.md` | 60d | entry |

Citations are re-pointed per source line, never by a constant: `citation-rewrites.md` resolves each
citation site of the package entry by the URL on its line (or the vendor name, for the four
vendor-table rows), and every cited staged id had exactly one candidate lane id — asserted, not
assumed. Two prose sites (`entry:33`, `entry:34`) carry neither URL nor vendor on their own line and
are marked `context (per-id unique map)`. Note the direction: `S217` staged is CodeBuddy CLI, `S217`
lane is the Qwen English page — a find-and-replace would corrupt the entry.

Staged `S217`, `S218`, `S219`, `S221` are free in the lane, so their renumbering is **allocation
policy** (contiguous block from `S217` in the append file's order), not a collision requirement; the
alternative (keep those four, allocate the six colliding rows around them) also validates and is
stated in `gate-notes.md` for a critic to overrule cheaply.

## 5. The two transformations are load-bearing (shown able to fail)

Appending the ten package rows to the mirror **unchanged** — only `used-by` repointed so E11 stays
quiet — and running the same validate:

```
file	E03	S205 duplicate id          … E03 for S206 S207 S208 S214 S216   (6 collisions)
file	E09	S205 recheck=30d — re-fetch the English page and confirm …      (all 10 rows)
[exit 1]
```

Transcript: `assimilation/guard-proof/mirror-e03.txt`. That is the refusal the brief asks for: without
the renumber the ids collide; without the cadence strip every row is E09.

## 6. Mirror and census output

`assimilation/validate/corpus/` is a byte copy of the lane's `corpus/` (136 files, 2.2 MB) plus the ten
rows appended at the end of the `## Registry` table, plus `SKILL.md` at the mirror root (11 `used-by`
cells name `SKILL.md`, which E11 resolves against the registry's parent directory), plus two clearly
marked stubs: `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` and
`corpus/lessons/round-73.md`.

```
$ … sources-census.sh census --file …/assimilation/validate/corpus/SOURCES.md
file	rows	152        FLEET	rows	152
file	tier.A	131      file	tier.B	20      file	tier.C	1
file	status.mined	144  status.queued	7  status.rejected	1
FLEET	missing	0
```

Against the lane's own file (read-only) the same command gives `rows 142`, `status.mined 134`,
20 W04 lines, exit 0 (`census-base-lane.txt`) — so the block adds ten rows and changes no other count.
The ten appended rows are byte-identical in the mirror and in `append-block.md` (compared line-wise).

## 7. Quotes: what this seat verified itself

I re-opened the four Qwen pages (my own fetch) and read the six source-opening seats' snapshots
directly; every fragment of every anchor was tested with `grep -qF`, then with a whitespace-collapse
compare (`quote-check.tsv`, 55 fragments).

Network record (2026-10-25, `curl -sL --max-time 60 -A 'Mozilla/5.0'`, HTTP 200, sha256 of the fetched
bytes):

| URL | bytes | sha256 |
|---|---|---|
| qwen-code-docs/en/users/features/skills/ | 607 888 | `6c15b3d8…` |
| qwen-code-docs/zh/users/features/skills/ | 592 311 | `3c7ff8cd…` |
| qwen-code-docs/ja/users/features/skills/ | 623 622 | `b507d57f…` |
| qwen-code-docs/zh/blog/updates/weekly-update-2026-02-09 | 391 928 | `7f1d2195…` |

Text-extracted snapshots (≤42 KB each) and the fetch log are in
`build/ExecIdNormalize/qwen-src/`; the raw HTML was deleted to respect the 300 KB snapshot bound (its
sha256 is in the log). Of the 55 fragment checks, 43 are `literal`, 6 are `collapse-only` and 6 are
**not found as written**:

1. lane `S217` (staged S205) `"Optional: enforce a rule deterministically (hooks:)"` — the page splits
   it across an inline code span (`snapshot-en.txt:1212` + `:1213` `hooks:` + `:1214` `)`); collapsed
   bytes read `( hooks: )`.
2. lane `S218` (staged S206) `"可选：确定性强制执行规则 (hooks:)"` — the page uses **full-width**
   parentheses (`snapshot-zh.txt:708` `可选：确定性强制执行规则（`); the ASCII rendering is a
   transcription, not the page.
3. lane `S218` (staged S206) `"可选：通过文件路径限制 Skill (paths:)"` — same code-span split
   (`snapshot-zh.txt:702`).
4. lane `S218` (staged S206) quote `"使 description 具体化：同时包含 Skill 的 功能和 使用时机"` — the
   page (`snapshot-zh.txt:1044-1050`) reads `…同时包含 Skill 的功能和使用时机（用户自然会提到的关键词）`
   without the two spaces the staged quote inserts, so it fails even collapsed. The page text is the
   quote to use.
5. lane `S222` (staged S216) footer `最后更新: Pager` — `grep -c '最后更新'` over
   `ExecSrcCodebuddyIde/snapshot.md` is **0**: this round's bytes do not carry that footer.
6. lane `S220` (staged S208) `"✨ 新增特性 → Agent Skills 正式转正"` is a **heading path**, not a page
   string: both headings exist separately (`snapshot-blog.txt:612`, `:614`, repeated `:662`, `:664`).

So three of the four Qwen rows (`S217`, `S218`, `S220`) and the CodeBuddy IDE row (`S222`) cannot be
landed as-is if the counter's rule (d) is read strictly over every quoted fragment; the fixes are one
cell each and are listed per fragment in `gate-notes.md`. No placeholder `<<quote>>` was inserted: the package's own anchor text is preserved
verbatim so the correction is visible as a difference, not silently invented.

## 8. `used-by` for the four Qwen rows — why not the C1 entry

The package entry `chinese-client-skill-surfaces.md` cites exactly six ids (its `source:` lines 4–9)
and **zero** Qwen ids; its opening paragraph says "None of them is the Qwen Code surface already held
from wave 1", and the lane holds no `qwenlm.github.io` row (`grep -n 'qwen' corpus/SOURCES.md` → no
output, so that clause is false for this lane and the entry seat should correct it). Naming the entry
as `used-by` for `S217`–`S220` would therefore be a citation the entry does not make — and, if the
entry were edited to cite them, C1 predicate (b) ("a URL whose host is one of `V`'s hosts") would fail
on a `qwenlm.github.io` row unless the counter scopes the host check to the vendor table only. Their
`used-by` is `corpus/lessons/round-73.md`, which the plan itself names as where this round's Gate
quotes live; the mirror carries a stub so E11 resolves. Flipping to the single-entry reading is four
cell edits, listed in `gate-notes.md`.

## 9. Rows deliberately not in the block

The brief enumerates the URLs; these package rows are Chinese-vendor surfaces but are **not** in that
enumeration and are not appended: staged `S215` (TRAE authoring best practice, `docs.trae.cn`),
`S220` (Kimi hosted-agent platform, `platform.kimi.com`), `S225`/`S226` (TRAE international build,
`docs.trae.ai`), `S233` (Zhipu OpenClaw, `docs.bigmodel.cn`). Each is a one-line addition to the same
block if the L1 wants it (`S215` would take `S227`, and so on by document order).

## 10. Artifacts and bounds

- `assimilation/guard-proof/`: `registry.md`, `registry-4space.md`, `mutant-e03.md`, `mutant-e04.md`,
  `proof.txt`, `mirror-e03.txt`.
- `assimilation/validate/`: `corpus/SOURCES.md` (mirror + block), `corpus/` copy, two stubs,
  `SKILL.md`.
- `build/ExecIdNormalize/`: `append-block.md` (10 rows, ready to insert above `## Paths`),
  `renumber-map.tsv`, `citation-rewrites.md` (per-site table + rewritten entry review copy),
  `gate-notes.md`, `quote-check.tsv`, `census-validate.txt`, `census-counts.txt`,
  `census-base-lane.txt`, `guard-mirror-e03.txt`, `qwen-src/`.

Scratch (`/tmp/k73w1-ExecIdNormalize.*`) deleted. No lane gate was run that needs the fleet-shaped
`../` sandbox (the census with `--file` reads only the given tree). No tool installed; no pacman
transaction. Two empty directories that a mistyped `mkdir` created in the fleet root
(`shokunin/guard-proof`, `shokunin/validate`) were removed immediately; nothing else outside the
assigned paths was touched.

## 11. Risks / open items for the L1

1. **C1 predicate (c)** wants snapshots under `.ufo/waves/round-73/snapshots/` with a
   `MANIFEST.sha256` pin; this seat's snapshots sit in `w1/build/ExecIdNormalize/qwen-src/` and the
   source seats' in `w1/build/ExecSrc*/`. Until a seat pins them at the frozen path, the C1 counter
   exits 2 — not a row defect.
2. **Landing order:** `corpus/lessons/round-73.md` must exist when the append lands, or E11 fires on
   the four Qwen rows.
3. **Anchor fixes** (§7 items 1–5) must be applied by the entry/row owner; three of them are
   transcription, one is an inserted-space quote, one is an unbacked footer.
4. **Entry path:** the rows' `used-by` names the frozen predicate path
   `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`, while the plan's assimilation sentence
   and the package name `chinese-client-skill-surfaces.md`. One path must win before the rows land.
5. The entry's "already held from wave 1" Qwen sentence is false for the lane and should be corrected
   by the entry seat (it is also what makes the four Qwen rows homeless).
