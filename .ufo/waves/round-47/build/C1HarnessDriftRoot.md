verdict: Of the 7 harness DRIFTs, 2 are a stale verifier model of omp's skill-description key space (`cache.misses`, `catalogue.missing_names` — the rows exist under `<bare>:<model>`), 1 is a dead binary path (`oc.roots` reads 10 instead of 11), and 4 are a deliberate host-state move (three skills born 2026-10-20T13:50:21-03:00: rows, offered, catalogue.total, verified_skills). A principled re-derivation exists and is implemented + falsified in `C1HarnessDriftRoot.patch`: **28/28, exit 0 at BASE**. Do not record `misses=3` as Q09 debt — it is not host drift.

# Axes
- freshness: the gate's substrate model (omp store key space) vs the live 18.12.5 store.
- operability: can a reader distinguish "row absent" from "row present under a model namespace" and "served preview" from "compressed"?
- calibration: which baseline numbers may be re-recorded from evidence, and which would be a copied observation.

# Observed at BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd

`python3 -B verifiers/verify_harness_claims.py --json` (repo root) → **exit 1, 21 PASS / 7 DRIFT**; matches `.ufo/waves/round-47/before/SUMMARY.md:9`.

| check | observed | baseline | verdict |
|---|---|---|---|
| omp.db.rows (`verifiers/baseline.json:22`) | 17 | 14 | DRIFT |
| omp.offered.skills (`:30`) | 10 | 7 | DRIFT |
| omp.cache.misses (`:42`) | 3 | 0 | DRIFT |
| omp.catalogue.total (`:66`) | 10 | 7 | DRIFT |
| omp.catalogue.missing_names (`:74`) | create-toolset, unreal-mcp, unreal-skill | [] | DRIFT |
| omp.cache.verified_skills (`:78`) | 10 | 7 | DRIFT |
| oc.roots.names_plus_builtin (`:86`) | 10 | 7 | DRIFT |
| omp.cache.keys_reproduced (`:38`) | 7 | 7 | PASS |
| omp.db.rows_wellformed | 14 | 14 | PASS |

# Root cause A — key space, not absence (3 skills × 1 row)

DB read-only: `sqlite3 'file:/home/vgpnk/.omp/agent/skill-descriptions.db?mode=ro'` → `skill_descriptions(key TEXT PRIMARY KEY, description TEXT NOT NULL)`, 17 rows, mtime `2026-10-21 00:31:27.255 -0300` (= `03:31:27Z`, 12 s before the round's session dir `2026-10-21T03-31-39-302Z`; earliest jsonl in it is `00:53:30 -0300`).

The verifier loads every row into a dict keyed by the full key (`verifiers/verify_harness_claims.py:286`) and asks only for the **bare** key `sha256(template|0x00|name|0x00|description)` (`:224`, `:309`). The store now has two key spaces:

- 14 rows bare (`<64-hex>`), the legacy generation;
- 3 rows `<64-hex>:anthropic/claude-haiku-5-5`.

For each new skill the 64-hex prefix is **byte-identical** to `omp_key(template, name, current description)`:
`create-toolset 570dc3ee…`, `unreal-mcp c0ca4c40…`, `unreal-skill e4a4d0fe…` (all `:anthropic/claude-haiku-5-5`). Their values are **byte-identical to `preview(description)`** — 88 / 99 / 97 chars, 15 / 16 / 16 words — and the newest captured `<skills>` block (`2026-10-21T15:54:26.314Z`, …/MoriR22R.SrcCensusDryRun-9.jsonl) has the same three previews verbatim.

Source-read in the frozen 18.12.5 dump (`/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings`):
- offset `26178035`: `Bun.CryptoHasher("sha256").update(w).update("\x00").update(e.name).update("\x00").update(e.description)` — the bare key the verifier models.
- offset `26176991`: `modelKey()` returns `` `${provider}/${id}` ``.
- offset `26182852`: writer guard `if (d !== undefined && e.get(d) !== undefined) return;`; offset `26183535`: `e.put(d, xze(r.description))` with `d = `${t}:${p}`` — i.e. **the preview is deliberately cached under `<bare>:<model>`** when compression output fails validation; offset `8773760`: the log line `Skill description compression unusable; keeping the preview for this model`.

So `cache.misses=3` and `catalogue.missing_names=[…]` are reader defects: the store holds all three entries, and the rendered catalogue lines equal those stored previews. What is served is a *preview*, not a compressed hint. A successful compression would have written the bare key (`e.put(t, u)`), and the guard above means the fallback is not retried for this model.

Timeline caveat, stated precisely: the three rows were written at `03:31:27Z` by the build installed then; the on-disk 18.12.5 ELF has mtime `2026-10-21 03:30:38 -0300` = `06:30:38Z`, three hours *later*. The model-scoped fallback therefore predates 18.12.5 (18.12.3 per `plans/round-47.md:8`); 18.12.5 still ships the identical code path (source-read above). Do not write "18.12.5 introduced it".

# Root cause B — three host skills, one delta each

`stat -c '%w'` (birth):
- `~/.agents/skills/create-toolset` → `2026-10-20 13:50:21.148532955 -0300`
- `~/.agents/skills/unreal-mcp` → `2026-10-20 13:50:21.147087335 -0300`
- `~/.agents/skills/unreal-skill` → `2026-10-20 13:50:21.148549185 -0300`

All three contain `SKILL.md` with `description:` on line 3 (quoted, 1054 / 1005 / 1041 chars, over the 100-char cliff); folder name == declared name; no dangling links. They are the only entries newer than the 7 in `verifiers/baseline.json:11` (godspeed 2026-10-06, ufo 2026-10-11, …).

Derivation of every count (baseline value + one named cause, not "read the tool output"):
- `offered 7 → 10`: +3 directories with `SKILL.md` under `USER_ROOTS` (`verify_harness_claims.py:62`).
- `db.rows 14 → 17`: +1 model-scoped fallback row per new skill; 14 = 7 skills × 2 generations (`baseline.json:11`); verified that exactly 3 rows carry the new namespace and each prefix maps 1:1 to a new skill.
- `catalogue.total 7 → 10` and `catalogue.matched 7 → 10`: 10 lines in the newest block, each byte-equal to a store value (3 of them the fallbacks).
- `verified_skills 7 → 10`: 10 offered − 0 unmodelled − 0 no-description.
- `oc.roots.names_plus_builtin 7 → 11`: 10 live names (`~/.agents/skills`; `~/.config/opencode/skills` absent; `~/.claude/skills` has no top-level `SKILL.md`) **+ 1** builtin marker — see the trap below.

# Counterexamples / traps for a naive re-baseline

1. **`oc.roots.names_plus_builtin` at BASE = 10 is hollow.** The default `OC_BIN` is `~/.opencode/bin/opencode` (`verify_harness_claims.py:55`), which does not exist; `oc_observations` then reports `builtin_names=0` (`:478`) — "unreadable" silently becomes "absent". With the npx ELF (`~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode`, sha256 `179ca421…`, 1.19.3) the same run gives `builtin 1`, `roots_plus_builtin 11`; the frozen 1.19.3 dump contains `customize-opencode` 2×. Pinning 10 records the dead-path artifact; pin 11 with a resolver, or leave it unobservable and say so.
2. **`cache.misses=0` after the fix does not mean "all descriptions compressed".** 3 of 10 are preview fallbacks (15–16 words), which is why `db_rows_wellformed` stays 14. A gate that reads only `misses` overstates health; `cache_preview_fallbacks` must be reported (not gated — it is compressor quality, and the host/model produced an unusable answer).
3. **`keys_reproduced` should stay 7, not move to 10.** Counting fallback rows as reproduced keys would erase the compressed/fallback distinction and make `db_rows_wellformed=14` inexplicable. The derived invariant is `keys_reproduced + cache_preview_fallbacks + cache_misses == verified_skills` (7+3+0=10).
4. **`db_rows_wellformed=14` is a real pass but a fragile pin**: it equals 17 rows − 3 fallbacks only because all three new values are previews. It is not a skill-set invariant; keep the note (`C1HarnessDriftRoot.patch` adds one).
5. **`oc.log.skills_rescan_max=3` is stale-but-green**: the opencode log was last written `2026-10-20 07:52 -0300`, before the 13:50 install, so opencode never observed the new skills. Not a drift, but the check cannot corroborate them.
6. `omp.descriptions.over_cliff` is `positive` mode, so 10 ≥ 7 passes whether one skill's description shrinks or not. It is a floor, not a claim about the 10.

# Recommendation: re-baseline with evidence (not Q09 debt)

Q09 (`corpus/QUALITY.md:20`) requires a re-derivation and re-pin; "no rebaseline" is open debt, not a pass. Here a re-derivation **is** shown: every delta is 1:1 with a named host event, and three of the seven reds are a reader defect. The patch at `.ufo/waves/round-47/build/C1HarnessDriftRoot.patch` (sha256 `8e6bec3d…`, against BASE, written from my scratch clone; not applied to production) does two separable things:

1. **Model fix (no baseline pins move at this step):**
   - `cache_lookup(rows, bare)` → `("compressed", value)` | `("preview-fallback", value)` | `None`; rows are read `order by key` for determinism.
   - `cached_by_name` includes both kinds; `cache_misses` = neither key exists; new observations `cache_preview_fallbacks` and `catalogue_preview_lines`.
   - `resolve_oc_bin()`: explicit `--oc-bin` wins, else the legacy path, else the newest npx package ELF (so `builtin_names` is not silently 0).
2. **Baseline re-record with the mechanism named** (`baseline.json`): rows 17, offered 10, catalogue.total 10, catalogue.matched 10, verified_skills 10, oc roots 11; `keys_reproduced` 7, `cache.misses` 0, `rows_wellformed` 14 unchanged; `omp_round47_note` + two note updates carry the evidence.

Verified in the scratch clone (`/fast/scratch/kotoba-r47/C1HarnessDriftRoot-9/lane`, detached at BASE):
- `python3 -B verifiers/verify_harness_claims.py --self-test` → `self-test: 0 failure(s) over 13 assertions`, exit 0.
- `python3 -B verifiers/verify_harness_claims.py` → `28/28 checks pass`, exit 0; `keys_reproduced=7 fallbacks=3 misses=0`, catalogue `10/10`, `3` preview lines, `names+builtin=11`.
- Falsification with a synthetic store containing **only** the three suffixed rows → `keys_reproduced 0, fallbacks 3, misses 7`; the lookup still reports genuine absence as absence.

If the L1 keeps the harness gate out of scope this round (it is "Not claimed", `plans/round-47.md:41-45`), record Q09 **with this decomposition** and the patch as prerequisite — but never pin `misses=3`, `catalogue.missing_names=[3 names]`, or `oc.roots=10`: those three would encode the reader defect and the dead binary path as expected truth. A baseline-only re-record without the model fix leaves 3 false DRIFTs (`misses`, `missing_names`, `matched` vs 10) and cannot reach 28/28.

# Commands run

| command | exit | key output |
|---|---|---|
| `python3 -B verifiers/verify_harness_claims.py --json` (repo) | 1 | 21 PASS / 7 DRIFT; values above |
| `sqlite3 'file:~/.omp/agent/skill-descriptions.db?mode=ro' '.schema'` / count | 0 | 1 table, 17 rows, key lengths 64/91 |
| `python3 … --json --oc-bin <npx 1.19.3 ELF>` | 1 | builtin 1, roots_plus_builtin 11 |
| `stat -c '%w %y'` on 3 skills + db + omp | 0 | birth 2026-10-20T13:50:21-03:00; db 03:31:27Z; omp 03:30:38-03:00 |
| `sha256sum ~/.local/bin/omp /fast/.../omp-18.12.5` | 0 | both `fdbc8136084c…` |
| `python3 - <<source strings offsets>>` over `omp-18.12.5.strings` | 0 | key hash 26178035, modelKey 26176991, fallback put 26183535 |
| patched `--self-test` / default / synthetic falsification | 0 / 0 / 0 | 13 assertions / 28-28 / 0-3-7 |

No tools installed or upgraded; no network fetch; no omp session launched; the `~/.local/bin/opencode` wrapper was not executed.

# What I did NOT check

- The **render** lookup order (bare vs `<bare>:<model>`) — only the writer path and the captured catalogue were read; since both paths yield the same preview bytes, the catalogue check is unaffected, but "the renderer consumed the suffixed row" is `[INFERENCE]`.
- A real **successful** compression (no smol/tiny output was usable on this host); the compressed-key branch is evidenced only by the 7 legacy rows.
- Whether `anthropic/claude-haiku-5-5` comes from config or the built-in `smol`/`tiny` list; only the `` `${provider}/${id}` `` shape is proven.
- Per-row insertion times (no timestamp column): the 3-row attribution rests on exact key-prefix equality and value equality, not on a timestamp.
- Any gate other than `verify_harness_claims.py`; no lane-wide run; no production edit; no `git add/commit` anywhere except the detached scratch clone.
- The opencode live rescan log for the three skills (log mtime predates the install; nothing to observe).
