# Kb81S16CensusLog — census old→new log (round 81, w1)

Seat: `Kb81S16CensusLog` (leaf, no subagents). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`,
base `b284223105f4d106f7e8f56ed4fd296c643cda0e`. This file is the ledger of **every `corpus/SOURCES.md`
cell round 81 changes**, in the form `corpus/lessons/round-81.md` `## Gate` pastes (the r80 lesson's
`## Sources & frontier` shape, `corpus/lessons/round-80.md:52-63`). No lane file was edited from this
seat.

**Authoritative row text.** `Kb81S05SourcesEdits.patch` (sha256
`6d0d571795341fb99bb2ce326e48a3c6f805857376e0b93d06b5d4848ecea2c0`, `corpus/SOURCES.md`, `+4 −2`) is
the delivered row text and every value below is transcribed from it. This seat derived its own row set
before that patch landed (`Kb81S16CensusLog-SOURCES-rows.superseded.patch`, sha256
`5e2c141b85fa4627fdb2c39695a6cb48561f7407cdbb4b411fa3ca20c4767dc9`, kept only as the derivation record);
the three design deltas against the delivered patch are named in §4 so nothing is silently merged. All
numbers below were **re-measured by this seat on the delivered patch** at fixture rev
`c5753ac89eb00b6f5f3ba53ea1f2dba567c97aad` (base + patch + empty placeholders for the two `used-by`
targets) — receipt `.ufo/waves/round-81/build/Kb81S16CensusLog-census-S05.txt`.

---

## 1. Paste-ready `## Gate` block

Round-start census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit 0, `kotoba ok`, **31** W04 duplicate-URL warnings, **174** rows (`.ufo/waves/round-81/receipts/census-before.txt`, whose 32 lines are 31 W04 + the `ok` line — the lesson draft's "32 W04" is a line count, not a warning count; re-run `.ufo/waves/round-81/build/Kb81S16CensusLog-census-base.txt`, `grep -c $'\tW04\t'` → `31`). Row-count command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → `174`, exit 0. After the source edits the same command over the base tree plus this round's SOURCES changes → exit 0, `ok`, **32** W04 warnings, **176** rows (`grep -cE …` → `176`), **0** E-codes (`.ufo/waves/round-81/build/Kb81S16CensusLog-census-S05.txt`, measured at fixture rev `c5753ac89eb00b6f5f3ba53ea1f2dba567c97aad` with `Kb81S05SourcesEdits.patch` applied and placeholders for the two used-by targets; the round-end reading is the L1's post-integration run).

Rows added by tier: A=2 (S249, S250), B=0, C=0; row count **174 → 176**; histogram `tier.A 135→137 / tier.B 22 / tier.C 17`, `mined 149→151 / queued 8 / rejected 17`. Existing rows touched old→new: one — S248 `used-by`. No status, anchor or recheck cell of any existing row changes; S230 stays untouched as the audit trail (CORPUS rule 2, append-only).

- S248 `used-by`: `—` → `corpus/knowledge/allowed-tools-sdk-round81.md` (the C2 entry cites S248's page as the r80 rung of the same surface; C2 conjunct (e) requires the entry to be named; census `E11` = 0 with the target present — `Kb81S16CensusLog-census-S05.txt`).
- S249 `source`/`kind`/`tier`: `(no row)` → `Claude Code Agent SDK — Skills — https://code.claude.com/docs/en/agent-sdk/skills.md` / `docs` / `A` (the SDK vendor's own statement of its own `allowedTools`/`allowed_tools` query-configuration channel and of the `allowManagedPermissionRulesOnly` override — primary for *that* scope; S248's tier B stays scoped to the spec-owned `SKILL.md` frontmatter field).
- S249 `scope`/`anchor`: `(no row)` → the allowedTools/allowed_tools query-configuration grant channel and the managed-settings override, anchored at § Pre-approve tools for skills, blockquote raw line 348 (grant note line 389), snapshot `.ufo/waves/round-81/snapshots/S249.md` + fetch record `.ufo/waves/round-81/snapshots/S249.fetch.json` (fetched 2026-10-28T02:27:26Z, HTTP 200, 28,395 B, sha256 `ac62c2df…`, two fetches `cmp`-identical, 0 redirects; host-local date 2026-10-27, TZ −03); located quote `the allowedTools option (allowed_tools in Python) in your query configuration` (10 words, key token present; 1 occurrence under both the link-preserving and the label-only text view — `Kb81S16CensusLog-s249-quotes.txt`). C2 conjuncts (c)/(d).
- S249 `teaches`/`status`/`opened`/`recheck`/`used-by`: `(no row)` → the grant channel is frontmatter **or** the query option, both ignored when managed settings set `allowManagedPermissionRulesOnly` / `mined` / `2026-10-27` / `90d` / `corpus/knowledge/allowed-tools-sdk-round81.md, corpus/lessons/round-81.md` (C2 conjunct (b): `mined`, tier A/B, canonical URL, `used-by` naming the entry).
- S250 `source`/`kind`/`tier`: `(no row)` → `kotoba own work — git ls-remote, GitHub commit API and commit-pinned raw probes, mistralai/mistral-vibe versus badlogic/pi-mono, run 2026-10-27 exit 0` / `own-work` / `A` (the lane's own re-runnable probe output, which the contract admits as tier A; plans/round-81.md § C1 repair 5).
- S250 `scope`/`anchor`: `(no row)` → which repository holds the token `7bb48f21…`, and what pi-mono's head and served blob are; anchored on `git ls-remote` (mistral-vibe `refs/heads/main` = `7bb48f21…`, rc 0, 2026-10-28T02:28:05Z), the GitHub commits API (mistral-vibe at that sha → HTTP 200 with equal sha; pi-mono → HTTP 301 to repository 1035029907 `earendil-works/pi`, whose commits API at that sha → HTTP 422 `No commit found for SHA`), the commit-pinned raw README (HTTP 200, 77,634 B, sha256 `fc48a5db…`, equal to the committed `S231-vibe.md`), pi-mono heads `bb65e3e4…` (r79) → `85c2ee3e…` (r80 reopen) → `a9228305…` (now) and path commit `25cc5c7b…`; receipts `.ufo/waves/round-81/build/Kb81S05SourcesEdits-binding.txt`, `.ufo/waves/round-80/build/Kb80R03ReopenSix-S230.fetch.json`.
- S250 `teaches`/`status`/`opened`/`recheck`/`used-by`: `(no row)` → **opens `supersedes S230 — `** and records that the commit S230's anchor attributes to pi-mono is mistral-vibe's `refs/heads/main` and absent from pi-mono (commits API 422), while pi-mono's head moved through three values with its served page blob (`sha1 19d2bf28…`) unchanged, so no pi-mono commit identifies the served bytes / `mined` / `2026-10-27` / `90d` / `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-81.md` (CORPUS rule 2 correction-row form; `used-by` restricted by the contract to knowledge entries or lessons).

Token and pointer accounting for the same block: the three touched rows add **0** `.ufo/reports/` pointers and **0** counted commit citations — `commit_total` stays `46` in both corpus gates; the one new ``commit `<hex>` `` shape is `commit `25cc5c7b…``, which ends in `…` and lands in the existing `commit_truncated` class (`0→1`, an INFO/observable counter that no baseline check holds — `verifiers/corpus-baseline.json` carries only `commit_total`/`commit_unresolvable`/`commit_nonhash`). `report_total` stays `111`; `report_dead`/`commit_unresolvable`/`commit_nonhash` are unchanged from base (`1` / `2` / `0`), so the R4 baseline refresh is driven by `tracked_files`/`unindexed` and the r80 lesson's index row, not by these cells.

---

## 2. Per-cell ledger

Old values are the committed bytes at `b2842231`; rows S249/S250 do not exist there (old = `(no row)`).
New values are the cells of `Kb81S05SourcesEdits.patch`.

### S248 — one cell changed (line 189 at base)

| cell | old | new | why | receipt |
|---|---|---|---|---|
| `used-by` | `—` | `corpus/knowledge/allowed-tools-sdk-round81.md` | C2 conjunct (e) — the entry must be named; the round lesson records the change without being a `used-by` path (see F3) | `Kb81S16CensusLog-census-S05.txt` (E11 = 0 with the entry present, 3 E11 lines without it — S05's receipt §1) |

Unchanged in S248: `id`, `source`, `kind`, `tier` (`B`), `scope`, `anchor`, `teaches`, `status`
(`queued`), `opened`, `recheck`. F3 records the `queued`-with-`used-by` tension rather than repairing it.

### S249 — new row, 11 cells

| cell | old | new |
|---|---|---|
| `id` | `(no row)` | `S249` |
| `source` | `(no row)` | `Claude Code Agent SDK — Skills — https://code.claude.com/docs/en/agent-sdk/skills.md` |
| `kind` | `(no row)` | `docs` |
| `tier` | `(no row)` | `A` |
| `scope` | `(no row)` | the `allowedTools`/`allowed_tools` query-configuration grant channel and the managed-settings override that disables it, as the SDK vendor's own statement of that option |
| `anchor` | `(no row)` | § Pre-approve tools for skills, blockquote raw line 348 (grant note line 389); snapshot `.ufo/waves/round-81/snapshots/S249.md` + `.fetch.json`; fetched 2026-10-28T02:27:26Z, HTTP 200, 28,395 B, sha256 `ac62c2df…`, two fetches `cmp`-identical, 0 redirects; located quote = the 10-word `allowedTools option` span |
| `teaches` | `(no row)` | frontmatter `allowed-tools` **or** query option `allowedTools` (`allowed_tools` in Python); `allowManagedPermissionRulesOnly` in managed settings makes Claude Code ignore both |
| `status` | `(no row)` | `mined` |
| `opened` | `(no row)` | `2026-10-27` |
| `recheck` | `(no row)` | `90d` |
| `used-by` | `(no row)` | `corpus/knowledge/allowed-tools-sdk-round81.md, corpus/lessons/round-81.md` |

### S250 — new correction row, 11 cells

| cell | old | new |
|---|---|---|
| `id` | `(no row)` | `S250` |
| `source` | `(no row)` | `kotoba own work — git ls-remote, GitHub commit API and commit-pinned raw probes, mistralai/mistral-vibe versus badlogic/pi-mono, run 2026-10-27 exit 0` |
| `kind` | `(no row)` | `own-work` |
| `tier` | `(no row)` | `A` |
| `scope` | `(no row)` | which repository the token `7bb48f213ac677f943d5c791199ed3dddf302f00` belongs to, and what pi-mono's head and served page blob are |
| `anchor` | `(no row)` | ls-remote mistral-vibe → `7bb48f21…` (rc 0, 2026-10-28T02:28:05Z); commits API mistral-vibe at sha → 200 equal; commits API pi-mono → 301 to repo 1035029907 `earendil-works/pi`, then 422 `No commit found for SHA`; commit-pinned raw README → 200, 77,634 B, `fc48a5db…`, equal to committed `S231-vibe.md`; pi-mono heads `bb65e3e4…`→`85c2ee3e…`→`a9228305…`, path commit `25cc5c7b…` |
| `teaches` | `(no row)` | **opens `supersedes S230 — `**; S230's token is mistral-vibe's `refs/heads/main` and absent from pi-mono (422), while pi-mono's head moved three times with the served blob (`19d2bf28…`) unchanged → no pi-mono commit identifies the served bytes |
| `status` | `(no row)` | `mined` |
| `opened` | `(no row)` | `2026-10-27` |
| `recheck` | `(no row)` | `90d` |
| `used-by` | `(no row)` | `corpus/knowledge/allowed-tools-surfaces-round80.md, corpus/lessons/round-81.md` |

Both rows are 11 cells / `NF=13` with no `|` inside any cell (S05's receipt §4 and this seat's
`Kb81S16CensusLog-census-S05.txt`: `cells=11` for S248, S249, S250).

---

## 3. Row-count lines and their commands

| reading | command | value | receipt |
|---|---|---|---|
| rows before | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | `174` (exit 0) | `Kb81S16CensusLog-census-base.txt` |
| rows after | same, on the delivered patch | `176` (exit 0) | `Kb81S16CensusLog-census-S05.txt` |
| census before | `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | exit 0, `kotoba ok`, 31 W04 | `receipts/census-before.txt`; `Kb81S16CensusLog-census-base.txt` |
| census after | same, delivered patch | exit 0, `ok`, 32 W04, 0 E | `Kb81S16CensusLog-census-S05.txt` |
| histogram before | `sources-census.sh census --root … kotoba` | `rows 174 / A 135 / B 22 / C 17 / mined 149 / queued 8 / rejected 17` | `Kb81S16CensusLog-census-base.txt` |
| histogram after | same, delivered patch | `rows 176 / A 137 / B 22 / C 17 / mined 151 / queued 8 / rejected 17` | `Kb81S16CensusLog-census-S05.txt` |
| patch shape | `git apply --check` / `git apply` at base | exit 0 / exit 0; `+4 −2` on one file | `Kb81S05SourcesEdits.patch` (sha256 `6d0d5717…`) |

Lane tip at write time: `e6d48e6a9b11da4660df8145bd2f28c3238c5b83` (the L1's plan-freeze commit,
`plans/round-81.md` +62 only — `git diff --stat b284223105f4d106f7e8f56ed4fd296c643cda0e..HEAD -- corpus/ verifiers/`
prints nothing), so the base readings above hold unchanged at the tip and `corpus/SOURCES.md` at the tip is
still 174 rows with no S249/S250.

The W04 delta is exactly one line and it is pre-declared:

```text
clone	W04	S249 duplicate url code.claude.com/docs/en/agent-sdk/skills.md across scopes
```

`W04` is a warning and never changes the exit status (`scripts/sources-census.sh:6-8`, `:645`). It
exists because S249 is the same page as S248 at a different scope — the C2 design, not a defect. **Do not
"fix" it by re-scoping S249 to S248's scope**: an identical scope cell plus a `teaches` cell that does not
open `supersedes S24?` raises `E04` and exits 1 (`scripts/sources-census.sh:646-649`). Measured: 0
E-codes as written.

---

## 4. Constraints the cells were written against (operability)

1. **11 cells, `NF=13`, no `|` inside any cell** (E01, `scripts/sources-census.sh:626`). Verified on the
   delivered patch: 0 E01.
2. **`mined` rows need resolvable `used-by` paths** (E11, `scripts/sources-census.sh:538-571`: every comma
   item is checked with `-e` against the lane root, for `mined` rows only). Both new rows are `mined`, so
   the entry and the lesson **must land in the same commit**: with the targets absent the census exits 1
   with three E11 lines (S05's receipt §1); with placeholders present it exits 0 (this seat's receipt).
3. **`used-by` is "knowledge entries or lessons"** (`CORPUS.md` § SOURCES.md → `used-by`). Hence S248 names
   the entry only, and S250 names the r80 entry + the round lesson; the `external-commits.json` manifest is
   not a permissible `used-by` value even though it consumes the binding.
4. **Quote view.** The S249 row quotes the 10-word span `the allowedTools option (allowed_tools in
   Python) in your query configuration`: `raw_occ=0` (the page backticks the option name) and `occ=1`
   under **both** the link-preserving view the C2 probe declares and label-only stripping — view-safe
   either way. The lesson draft's 23-word rendering is `occ=0` under the link-preserving view (see F2).
5. **`opened` date.** `2026-10-27` is the host-local date (TZ −03) of the 2026-10-28T02:27Z fetch, and the
   S249 anchor spells the conversion out; `E08` accepts it under either reading of "today"
   (`scripts/sources-census.sh:659-661`).
6. **No new counted citations / pointers.** `commit_total` stays 46; the one added ``commit `25cc5c7b…` ``
   is a truncated token (`commit_truncated 0→1`, not a baseline key); `UFO_POINTER_RE` (only
   `.ufo/reports/round-N/*.md`) matches 0 in the touched rows, so `report_total` stays 111.
7. **Design deltas against this seat's superseded derivation** (recorded, not merged): S249 tier `A` vs `B`
   (the delivered A is justified by scope — vendor's own statement of its own option — and S248's B stays
   scoped to the spec-owned field); S250 `own-work` (lane probe) vs `code` (the mistral-vibe repo) — the
   delivered form adds the commits-API 422 disproof and the 301 alias, so it is strictly stronger; S248
   `used-by` entry-only vs entry+lesson; S250 `used-by` r80-entry+lesson vs lesson-only.

---

## 5. What this seat did not measure

The `after` readings are a clone carrying the delivered rows and **empty placeholders** for the two
`used-by` targets, not the integrated lane: the real `corpus/knowledge/allowed-tools-sdk-round81.md` and
`corpus/lessons/round-81.md` are other seats' deliverables, and the C2 counter
(`verifiers/check_sdk_allowed_tools.py`) was absent from the lane and from `build/` when this seat ran
(`ls verifiers/check_sdk_allowed_tools.py` → no such file; `grep -rln check_sdk_allowed_tools .` → plans,
lesson/log/report drafts only). The L1's post-integration census run is the first scored `after` number; if
it prints anything other than exit 0 / 176 rows / 32 W04 / 0 E / A 137 · B 22 · C 17, that divergence is the
finding.
