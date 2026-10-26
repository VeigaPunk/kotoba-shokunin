# Gate notes — round 73, ExecIdNormalize (assimilation scratch)

Ten staged Chinese-vendor rows, renumbered by document into the lane's 11-column registry. Nothing
here is landed: the append block is a draft for the L1, and the census run is against the mirror
`assimilation/validate/`.

## What changed in each row (and nothing else)

Cells rewritten, per row: `id` (by document, see `renumber-map.tsv`), `recheck` (prose stripped to
its cadence — the prose moves into this file, below), `used-by` (re-pointed to the admitted entry, or
to the round lesson for the four Qwen rows). Every other cell is the package cell verbatim.
`status` = `mined` (already), `opened` = the staged date `2026-10-23` (kept: it is the package's
opening day; this round's re-open is `2026-10-25` and belongs in the entry's `verified-at:`, not in the
row). Every row has exactly 11 cells and contains no literal or escaped `|` in any cell (checked).

## Stripped `recheck` prose (kept here as the Gate note)

| lane id | staged id | recheck | stripped prose |
|---|---|---|---|
| S217 | S205 | 30d | re-fetch the English page and confirm the five frontmatter keys and the `paths`/`hooks` sections are still present (ran 2026-10-23) |
| S218 | S206 | 30d | re-fetch the Chinese page and re-count the `skills.directories` and `.agents` occurrences against the English page (ran 2026-10-23) |
| S219 | S207 | 30d | re-fetch the Japanese page and re-count the `skills.directories` and `.agents` occurrences against the English page (ran 2026-10-23) |
| S220 | S208 | 90d | re-fetch the post and confirm the GA wording and the v0.6.0/v0.9.0 versions (ran 2026-10-23) |
| S221 | S214 | 60d | re-fetch and confirm the `.agents` toggle and the rules-vs-skills paragraph are unchanged (ran 2026-10-23) |
| S222 | S216 | 60d | re-fetch and confirm the ~100-word and <5k-word budgets are unchanged (ran 2026-10-23) |
| S223 | S217 | 60d | re-fetch and confirm the frontmatter example and the two discovery roots are unchanged (ran 2026-10-23) |
| S224 | S218 | 60d | re-fetch the `main` branch file and confirm the system-prompt injection sentence and the two discovery groups are unchanged (ran 2026-10-23) |
| S225 | S219 | 60d | re-fetch and confirm the nesting limit and the `whenToUse` alias list are unchanged (ran 2026-10-23) |
| S226 | S221 | 60d | re-fetch and confirm the system-prompt sentence and the single-responsibility rule are unchanged (ran 2026-10-23) |

## Quote status against this round's bytes

Checked with `grep -qF` (literal substring) and, where the literal missed, a whitespace-collapse
compare. Evidence: `quote-check.tsv` (per fragment) and the snapshots named below. A `located`
verdict means this seat found the string in the bytes it read; it is not a transfer of any other
seat's claim.

Snapshots read (`wc -c`):

- S217 (staged S205): `build/ExecIdNormalize/qwen-src/snapshot-en.txt (33 060 B, fetched 2026-10-25)`
- S218 (staged S206): `build/ExecIdNormalize/qwen-src/snapshot-zh.txt (30 306 B, fetched 2026-10-25)`
- S219 (staged S207): `build/ExecIdNormalize/qwen-src/snapshot-ja.txt (41 893 B, fetched 2026-10-25)`
- S220 (staged S208): `build/ExecIdNormalize/qwen-src/snapshot-blog.txt (10 204 B, fetched 2026-10-25)`
- S221 (staged S214): `build/ExecSrcTrae/snapshot.md (13 351 B)`
- S222 (staged S216): `build/ExecSrcCodebuddyIde/snapshot.md (3 887 B)`
- S223 (staged S217): `build/ExecSrcCodebuddyCli/snapshot.md (25 241 B)`
- S224 (staged S218): `build/ExecSrcKimiEn/snapshot.md (13 528 B)`
- S225 (staged S219): `build/ExecSrcKimiZh/snapshot.md (6 928 B)`
- S226 (staged S221): `build/ExecSrcZhipu/snapshot.md (7 381 B)`

| lane id | fragments | located | collapse-only | not found |
|---|---|---|---|---|
| S217 | 7 | 4 | 2 | 1 |
| S218 | 8 | 4 | 1 | 3 |
| S219 | 5 | 3 | 2 | 0 |
| S220 | 3 | 1 | 1 | 1 |
| S221 | 7 | 7 | 0 | 0 |
| S222 | 6 | 5 | 0 | 1 |
| S223 | 3 | 3 | 0 | 0 |
| S224 | 7 | 7 | 0 | 0 |
| S225 | 5 | 5 | 0 | 0 |
| S226 | 4 | 4 | 0 | 0 |

### Fragments not found as written

Six fragments across four rows: one in lane `S217` (staged S205), three in `S218` (staged S206), one
in `S220` (staged S208), one in `S222` (staged S216, a footer claim). The other six rows (`S219`,
`S221`, `S223`, `S224`, `S225`, `S226`) hit every fragment literally.

1. **Lane S217 (staged S205)** — anchor heading `"Optional: enforce a rule deterministically (hooks:)"`.
   The page carries the heading across an inline code span and renders the parenthesis separately:
   `snapshot-en.txt:1212` "Optional: enforce a rule deterministically (" + `:1213` "hooks:" + `:1214` ")".
   After whitespace collapse the bytes read `Optional: enforce a rule deterministically ( hooks: )`.
   The staged rendering drops the spaces the collapse rule preserves.
2. **Lane S218 (staged S206)** — anchor heading `"可选：通过文件路径限制 Skill (paths:)"` and
   `"可选：确定性强制执行规则 (hooks:)"`: the page uses **full-width** parentheses for the second
   (`snapshot-zh.txt:708` `可选：确定性强制执行规则（`), so the ASCII `(hooks:)` in the staged anchor is a
   transcription, not the page's bytes. The first matches only through the code-span split
   (`snapshot-zh.txt:702` `可选：通过文件路径限制 Skill (` + `paths:` + `)`).
3. **Lane S218 (staged S206)** — quote `"使 description 具体化：同时包含 Skill 的 功能和 使用时机"`.
   The page (`snapshot-zh.txt:1044-1050`) reads, across an inline code span,
   `使 description 具体化：同时包含 Skill 的功能和使用时机（用户自然会提到的关键词）` — no spaces around
   `功能`/`和`; the staged quote inserts two spaces that the page does not carry, so it fails even
   after whitespace collapse.
4. **Lane S222 (staged S216)** — footer claim `最后更新: Pager`: `grep -c '最后更新'` over
   `ExecSrcCodebuddyIde/snapshot.md` returns **0**. The page footer this round does not exist in the
   snapshot; the claim is unbacked and should be dropped from the anchor or re-located.
5. **Lane S220 (staged S208)** — `"✨ 新增特性 → Agent Skills 正式转正"` is a **heading path**, not a
   quote: both headings exist separately (`snapshot-blog.txt:612` `✨ 新增特性`, `:614`
   `Agent Skills 正式转正`, repeated in the body at `:662`/`:664`). Read as a path it is fine; read as a
   quote it is not a page string.

## `used-by`: why the four Qwen rows do not name the C1 entry

The package entry `chinese-client-skill-surfaces.md` cites **six** ids (its six `source:` lines) and
**zero** Qwen ids — its opening paragraph says "None of them is the Qwen Code surface already held from
wave 1", and the lane holds no `qwenlm.github.io` row (`grep -n 'qwen' corpus/SOURCES.md` → no output).
So the frozen C1 entry cannot honestly be the `used-by` of the Qwen rows, and citing them from it
would also put a Qwen host in front of C1 predicate (b), which admits only the four vendors' hosts.
Their `used-by` is therefore `corpus/lessons/round-73.md` — the plan's own statement that this round's
Gate quotes live in the round lesson — and the mirror carries a stub of that file so E11 resolves.
If the L1 wants the single-entry reading instead, the delta is four `used-by` cells (S217–S220 → the
entry path) **and** the entry must then cite them, which breaks (b) unless the counter scopes the
host check to the vendor table.

## Two load-bearing transformations, shown able to fail

Appending the package rows unchanged into the mirror (only `used-by` repointed, so E11 stays quiet)
gives `6 × E03` (`S205`, `S206`, `S207`, `S208`, `S214`, `S216` — the lane's own rows own those ids) and
`10 × E09` (every staged `recheck` carries prose). Evidence: `assimilation/guard-proof/mirror-e03.txt`.

## Non-collision renumbering, stated plainly

Staged `S217`, `S218`, `S219`, `S221` are **free** in the lane registry at `072048f`; they were still
renumbered (to `S223`, `S224`, `S225`, `S226`) because the block is allocated contiguously from the
lane's next free id `S217` in the append file's document order. This is allocation policy, not a
collision requirement: keeping those four at their staged ids would also validate, with lane ids
`S217` (CodeBuddy CLI), `S218` (Kimi EN), `S219` (Kimi ZH), `S221` (Zhipu) and the six colliding rows at
`S220`, `S222`–`S226`. The map (`renumber-map.tsv`) is directional: staged → lane, resolved by URL.

