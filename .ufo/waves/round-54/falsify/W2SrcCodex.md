Result: MIXED — every S054/S063 receipt, quote, word count, location and counter condition holds against a fresh byte-identical re-fetch, but the SKILL.md Codex threshold cell says `skills.max_context_tokens` "raises the default" where both cited pages and the lane's own S021 record say only that it *sets/overrides* a budget capped at 10,000 tokens — one direction-only word beyond its evidence.

Seat: `KotobaR54.W2SrcCodex` (leaf, FALSIFY). Scope: C1's `Codex` rows landed in `5a097e1`: SOURCES `S054`/`S063`, the entry row in `corpus/knowledge/skill-listing-thresholds-round54.md` § Per-client record, the two Gate rows in `corpus/lessons/round-54.md`, and the `SKILL.md` § Description thresholds by client row. Lane read-only; this report is the only lane file written. Sandbox clone `/fast/scratch/hyaku/kotoba-r54/W2SrcCodex` at `58db81c4465b0e9b07ef2485b87d8970683afac6`; fetched bytes kept in `/fast/scratch/hyaku/kotoba-r54/W2SrcCodex-fetches/`. No installs needed (curl, sha256sum, python3 already present); no model calls.

## 1. Re-fetch receipts (own fetches, UTC stamps from `date -u`)

| URL | fetched (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://learn.chatgpt.com/docs/build-skills.md | 2026-10-22T21:56:59Z | 200 | 11,035 | `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` |
| https://learn.chatgpt.com/docs/config-file/config-reference.md | 2026-10-22T21:56:59Z | 200 | 136,297 | `fe48af085a53345cf171cf492f3147eb2bb297b8ab28f83e67b8e9e62f715a21` |

Both are **byte-identical** to the values recorded in the SOURCES anchor cells (`corpus/SOURCES.md:67`, `:76`), the Gate rows (`corpus/lessons/round-54.md:24`, `:33`) and the seat report (`.ufo/waves/round-54/build/SrcCodex.md:40,42`). The bytes the lane recorded at 21:15–21:16Z are exactly the bytes served at 21:56:59Z. Receipt cells: **HOLDS**.

## 2. Quote verbatim and at the stated location

- S054 quote — `"this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown"`: the fetched file has it spanning `build-skills.md:38-39` (the line breaks after `model's`). 20 words (3–25 bound), double-quoted in the entry. After the counter's own normalisation (tags/tags dropped, emphasis stripped, whitespace collapsed) it is a substring of the page: `True`. Cited location `build-skills.md:38-39` is exact; the SOURCES anchor's wider range `md:33-46` is accurate (budget :38-39, shorten/omit :40-41, override :43-44, scope :46, advice :101-103 — each verified). **HOLDS**.
- S063 quote — `"Token budget for the available-skills catalog. Defaults to 2% of the model's context window. Explicit values are capped at `10000` tokens."`: verbatim at `config-reference.md:378` (inside the `skills.max_context_tokens` block :374-379), 21 words, on the page after normalisation: `True`. **HOLDS**.
- The `skills.max_context_tokens` key block sits at config-reference.md `:375-379` exactly as the anchor records (`key` :375, `type: "integer (positive)"` :376, `description` :378).

## 3. Is the number about the skill description / listing (erratum-3 check)?

Yes. The 2% / 8,000 pair bounds the *initial skills list*, whose contents are name + description + file path (`build-skills.md:34-35`, `:37`); the 10,000 cap bounds the override for the same list. `grep -n '[0-9]'` on the fetched page returns no other topical number — no name cap, no per-description authoring maximum (seat's enumerated table, `SrcCodex.md:9-16`, confirmed independently). The counted numbers are listing-budget numbers, not another field's. **HOLDS** — the area claim (listing budget, not a render cut) is the right reading.

## 4. Cell-by-cell HOLDS/BREAKS

### SOURCES rows

- **S054** (`SOURCES.md:67`): 11 cells, kind `docs`, tier `A`, status `mined`, opened `2026-10-22`, host `learn.chatgpt.com` ∈ Codex pinned hosts (`check_description_thresholds.py` HOSTS), used-by names the entry and the lesson. `teaches` = the initial-list budget only — exactly the recorded Gate quote's content. **HOLDS**.
- **S063** (`SOURCES.md:76`): 11 cells, `docs`, `A`, `mined`, `2026-10-22`, same host, used-by correct. `teaches` restates the config quote faithfully (default 2%, cap `10000`). **HOLDS**.

### Entry row (`skill-listing-thresholds-round54.md:40`)

- client/row cells: `Codex` | `S054` — one `S###`, correct. **HOLDS**.
- quote cell: verbatim, 20 words, contains the SKILL.md number tokens `2%` and `8,000` as whole tokens. **HOLDS**.
- location cell `build-skills.md:38-39 (past-it md:40-41; scope md:46)`: accurate. **HOLDS**.
- reading cell — "A listing budget over the whole initial skills list, not an authoring maximum on one description and not a documented per-entry cut: past it Codex shortens skill descriptions first and, for large skill sets, may omit skills from the initial list with a warning, while the full SKILL.md still loads once the skill is selected." Each clause maps to a line: list scope :37-38/`46`; shorten-first :40; omit-with-warning :40-41; full SKILL.md on selection :46; "no documented per-entry cut"/"no authoring maximum" is the seat's enumerated absence (the page's only numbers bound the list, §3). **HOLDS**.
- Findings bullet 2 (`:23-26`): same support, plus "may then omit skills with a warning" (:40-41). **HOLDS**, except the shared `raises` wording flagged below.
- Findings/Limits honesty: entry states these are documentation statements, not measured behaviour; consistent with the seat's limits (`SrcCodex.md` §11). **HOLDS**.

### Gate rows (`round-54.md:24`, `:33`)

- S054: URL, stamp `2026-10-22T21:15:49Z`, bytes/sha256, 20-word quote at `build-skills.md:38-39`, seat `SrcCodex` — all match my re-fetch and the seat report. **HOLDS**.
- S063: URL, stamp `2026-10-22T21:16:19Z`, bytes/sha256, 21-word quote at `config-reference.md:378` — all match. **HOLDS**.

### SKILL.md row (`SKILL.md:186`)

- Past-the-threshold cell — "Codex shortens skill descriptions first, then for large skill sets may omit skills from the initial list and show a warning; selecting the skill still reads the full `SKILL.md`": direct paraphrase of `build-skills.md:40-41,46`. **HOLDS**.
- Action cell — "Front-load the use case and trigger words in `description` so matching survives shortening; do not rely on a long tail": the first clause is the page's own advice verbatim-adjacent (`:101-103`, "Front-load the key use case and trigger words so a host can still match the skill if descriptions are shortened"); "do not rely on a long tail" is a bounded authoring restatement, appropriate for an action cell. **HOLDS**.
- Documented-threshold cell, first clause — "Initial skills list: 2% of the model's context window, or 8,000 characters when the context window is unknown": verbatim-faithful. **HOLDS**.
- Documented-threshold cell, second clause — **`skills.max_context_tokens` raises the default, capped at 10,000 tokens": BREAKS (low severity, direction word over-wide).** `build-skills.md:43-44` says only "set a *different* budget, up to 10,000 tokens"; `config-reference.md:378` says "Defaults to 2% … Explicit values are *capped* at `10000` tokens." Neither page says the setting *raises* the default, and the cited pages give no minimum window size from which raising follows: where 2% of the window already exceeds 10,000 tokens, an explicit value can only *lower* the budget. The lane's own prior record of the same page is stricter — S021 teaches "`skills.max_context_tokens` *overrides* it (up to 10,000 tokens)" (`SOURCES.md:34`), and the seat's own reading says "Override" / "set a different budget" (`SrcCodex.md:34`, `:22`). The new cell loosens the lane's own wording beyond the evidence. The same over-wide word sits in the entry's Findings bullet 2: "`skills.max_context_tokens` raises it, capped at 10,000 tokens (S063)".
  - Corrected SKILL.md text: `` `skills.max_context_tokens` sets a different budget, capped at 10,000 tokens `` (or S021's word: "overrides the default, capped at 10,000 tokens").
  - Corrected entry text: "`skills.max_context_tokens` overrides it, capped at 10,000 tokens (S063)".
  - Counter impact: none — the counter checks only that a number token is present; the fix removes no token.

## 5. Contradiction sweep against older lane rows and entries

- S013 (`queued`, 2026-10-21) and S021 (`mined`, 2026-10-22) are the *same page*: same sentence quoted at `corpus/lessons/round-47.md:36` and `round-48.md:36`; S021's fetch hash `ed6e324f…` equals today's bytes. S054 restates the same budget — no contradiction; the entry's Relation bullet (`:56-57`) honestly states the numbers were previously only in SOURCES and are new as entry content. S054 does not claim `supersedes`, correctly — it adds nothing over S021 except the entry/Gate linkage. **HOLDS**.
- `frontmatter-rule-authorities-round48.md:51` records that Codex CLI 0.163.0's shipped parser truncates catalog descriptions at 1,024 chars (measured, `C2CodexOpencodeDocs.md`, no source row pins the code). The new row says "not a *documented* per-entry cut" — scoped to documentation, so it does not contradict the measured finding; readers cross-referencing both could still collide, since the table nowhere mentions the measured 1,024 cut. Residual nuance only, not a break.
- `mcp-server-instructions-round52.md:29` (S035, 512-char self-contained advice) is about MCP server `instructions`, not skill `description` — no clash. `skill-overlap-levers-round51.md:26` (implicit-invocation lever) is orthogonal and consistent. `alwayson-rule-files-round53.md` (S044) is a different surface. **HOLDS** — no contradiction found.

## 6. Counter re-run and guards

- `python3 -B verifiers/check_description_thresholds.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6 --json` in the sandbox clone → `description thresholds backed 7 of 7 clients`, exit 0; Codex `backed: true, row S054, why: []`.
- Guard (a): `git show e3371548…:corpus/SOURCES.md | grep -cE 'S054|S063'` → `0` (absent at plan commit, opened this round).
- Guard (b): `2%`, `8,000`, `10,000` each grep-count `0` in `SKILL.md` at `e3371548` — new ground.
- Guard (c): the entry quote is found verbatim on today's live bytes (§2) — the `--fetch` form of the check holds for Codex.

## 7. Residual risk

- The single break is a direction word ("raises") that no gate reads; severity low, fix is one word. Everything else about the Codex cells — receipts, verbatim quotes, locations, reading, lack of contradiction — held under independent re-fetch and re-read. Residual unknowns the seat itself declared (no binary read; HTML Last-Modified moved while `.md` bytes stayed identical; docs tree = site's own `llms.txt`, no public repo mirror) remain as stated, not contradicted.
