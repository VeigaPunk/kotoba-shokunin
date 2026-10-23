# ReviewC1Counter — C1 counter v2 independent review

Result: DONE — `check_plugin_manifests.py` v2 at `01312a77` implements frozen C1 rules (plan C1 + Erratum 1) and the round-56 R4/R5 fixes; `--self-test` 0 failures over 235 assertions (exit 0); nothing in scope is looser than v1.3 except one cosmetic ASCII-only boundary edge and the frozen OWN_ROOTS→MARKERS guard replacement (documented below).

## Setup and identity

- Sandbox clone `/fast/scratch/hyaku/kotoba-r57/ReviewC1Counter` checked out at `01312a77e36317feb6e961aba77841ddab1225ca`; counter sha256 `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` — equals the frozen v2 hash (Erratum 1).
- `python3 -B verifiers/check_plugin_manifests.py --self-test` → `counter sha256 …` / `self-test: 0 failure(s) over 235 assertions`, exit 0.
- Comparison target `verifiers/check_agent_definitions.py` sha256 `2f672bd155a4c125…` is byte-identical at `f897d18a`, `47c05558` and `01312a77` — i.e. exactly the round-56 v1.3 counter. Diff method: AST top-level map, per-function unified diff, plus direct runtime probes on both modules (imported from the sandbox).

## Diff inventory vs v1.3

Byte-identical (verified): `EnvError, boundary_ok, cells, clean, client_name, entry_rows, gate_section, host_ok, is_separator, lane_dir, norm, quote_in_gate, section_lines, source_ids, sources_table, strip_quotes, tables, urls_of, verify_rev, ws`; constants `HOSTS, CLIENTS, TRACKER_SEGMENTS, BOUNDARY_PREV, TRIM_CHARS`.

Behaviourally equivalent (refactor/docstring only): `_plain`→`page_plain` (v2:792-799) with identical string ops; `norm_page` = `norm_page_case`+lower (v2:818-822) with identical tag stripping; `url_key` (v2:461-481) identical semantics; `git` gains `data` param (v2:311) for `cat-file`; `url_is_tracker` (v2:497-502) identical; `skill_rows` heading constant only.

Stricter than v1.3 (each only adds failures, per Erratum 1):
1. E1 token grammar — final segment must end `.json` and carry the plugin/extension word; token must have ≥2 segments or hold its own client marker (v2:535-559). v1.3 `token_well_formed` had no `.json`/final-segment requirement.
2. E7 — no non-final segment may contain a dot except as first char (v2:548-550) — blocks host/version-shaped tokens.
3. E4 — entry `Manifest` cell must equal the SKILL.md token or its normalise()d form, exact case (v2:628-633, used at 657-659).
4. E5 — shared-token disqualification: casefold(normalise(first backticked span)) used by rows of ≥2 distinct client names disqualifies every listed user (v2:634-644, applied 736-742; unlisted names count as users).
5. E2 — held-ground test is case-insensitive at path-segment boundaries (v2:960-992), replacing v1.3 `git grep -i -F -c` substring counting (which held `.claude/AGENTS.md` as `.claude/agents` — R4). Blob scan replaces grep; `.ufo/` excluded by path (v2:904-925); NUL binary blobs skipped (v2:994-998).
6. E6 — quote word floor 3→6 (v2:218; check at 666-669).
7. E3 — SOURCES URL path containing `changelog|release|releases|news|blog` (decoded, case-insensitive) rejected, both at row level (v2:691-693) and on the post-redirect final URL (v2:884-886).
8. `NEW_TARGET` 2→3 (v2:217); `OPENED` narrowed to `2026-10-23` (v2:220).
9. Quote/token matching case-sensitive: `token_span` first case-sensitive raw-or-normalised occurrence (v2:584-598); `token_at_boundary` finds case-sensitively (v2:830-849); `found_on_page` uses case-preserving `norm_page_case` for the token (v2:894-901). v1.3 lowered both sides.
10. `new_ground` counts distinct casefold values (v2:1040-1048); v1.3 counted distinct exact norms with per-token grep counts — G cannot be inflated by case spellings.

Looser than v1.3 — two items:
- **A (minor, code-level):** `token_at_boundary` right boundary uses ASCII `ASCII_ALNUM` (v2:270, 844-846) where v1.3 used Unicode-aware `text[j].isalnum()` (v1.3:720). Probe: token followed by Cyrillic `а` or `é` is accepted as a boundary by v2, rejected by v1.3. Only affects non-ASCII continuations of a token on a live page; low practical impact, not blocking, but it is a genuine loosening of the boundary guard.
- **B (frozen spec):** `OWN_ROOTS` membership (v1.3:455-463, `owned_by`) is replaced by `foreign_marker` (v2:561-568) + E5. Probe: `.config/plugin/plugin.json` is well-formed for opencode under v2 (no own-marker required once ≥2 segments, no foreign marker) whereas v1.3 rejected it for opencode and Cursor. Erratum 1 requires exactly this guard; flagging it as the one axis where v2 is permissive relative to v1.3 (not a defect — the counter matches the frozen spec).

## Rule-by-rule verdict (frozen spec)

- Token grammar, marketplace ban, foreign-name guard, E1/E7: implemented as specified; self-test carries a must-fail arm for each (v2:1240-1400).
- Held test: case-insensitive, segment-bounded; `held_right_ok` (v2:982-992) rejects alnum/`_`/`-`/dot-alnum continuations; left set `HELD_PREV` includes `` ` " ' ( [ < / ~ = `` + ws/line-start (v2:271, 968-976). Distinct G = casefold values. Matches Erratum 1 (not the older plan sentence that said "case-sensitively"; the erratum supersedes).
- Quote checks: 6–25 words (E6); verbatim token present case-sensitive; plugin/extension word outside the token span (`plugin_word_outside` v2:600-606); quote recorded in `## Gate` of `corpus/lessons/round-57.md` at measured rev (`quote_in_gate` v2:621-626).
- Host pins: `HOSTS` unchanged from v1.3 (verified equal); `host_ok` segment-exact host/path prefix, subdomain allowed, dot-dot rejected.
- Base-URL re-citation: `url_key` + `base_url_keys` (v2:461-491) reject any row URL equal to a base SOURCES URL (path-case, `www.`, scheme, trailing-slash/`.md`, fragment, query normalised); fetch also refuses a redirect landing on a base URL (v2:881-883).
- Tracker/docs rejection: `url_is_tracker` (issues/PR/discussion/commit/compare) unchanged; `kind=docs` required; E3 change-note path rejection (row + final redirect).
- Fetch boundary: 30 s timeout, ≤5 MiB, one retry, UA `kotoba-shokunin-counter/57`, pins enforced on the final URL; quote matched under the normalisation, token case-sensitive at a boundary on the case-preserving page.
- Gate check, K/F/G semantics, predicate line and exit codes: `summary_line`/`predicate` (v2:1022-1038) match the frozen sentence `plugin manifests found on the live page F of K; new ground G`, F≥5 and G≥3, exit 0; 2 = could-not-evaluate with no traceback (v2:1782-1850).

## R4/R5

- R4: implemented (case-insensitive segment-bounded held; distinct casefold G) with self-test arms: case-difference holds, `.claude/AGENTS.md` does not hold `.claude/agents`, both spellings count once, `my.claude-plugin/plugin.json` not held, `x/.claude-plugin/plugin.json` held.
- R5: self-test expanded from 184 (v1.3) to 235 assertions, each v2 guard has a must-fail arm. The w0 kill table (72/73, 1 verdict-neutral survivor) is control-seat recorded evidence; I did not re-run the mutation generator ([INFERENCE] — not independently verified here).

## Residual risks / verification gaps

1. Non-ASCII continuation boundary (finding A): decide whether to add a Unicode arm if round 58 touches the counter.
2. OWN_ROOTS removal (finding B): the seven supported root paths themselves (`.claude-plugin/`, `.codex-plugin/`, `.github/plugin/`, `gemini-extension.json`, `.cursor/plugin/`, `.opencode/plugins/`… existing are not enforced; a future seat could cite a real documented path that is not vendor-canonical. For the round-57 data, this is bounded by pins + E5 + token grammar; watch in falsify.
3. `url_is_change_note` substring matching may false-positive a legitimate docs path containing `blog`/`news`/`release` (stricter only; no validity hole).
4. Held scan reads symlink blobs as text (link targets) — can only over-hold (understate G), never inflate.
5. Tooling: no packages installed/updated (stdlib + git only); nothing to record per the tooling directive.

## Evidence pointers

- v2 file: `/fast/scratch/hyaku/kotoba-r57/ReviewC1Counter/verifiers/check_plugin_manifests.py` (lines cited above; sha256 `bf11a4ef…`).
- v1.3 file: `verifiers/check_agent_definitions.py` at `01312a77` (sha256 `2f672bd1…`).
- Self-test run: `python3 -B verifiers/check_plugin_manifests.py --self-test` → exit 0, `0 failure(s) over 235 assertions`.
- Probes (imported modules): `HOSTS` equal; `TRACKER_SEGMENTS`/`BOUNDARY_PREV`/`TRIM_CHARS` equal; `token_at_boundary("x .claude-plugin/plugin.json\u0430", …)` True (v2) vs False-under-v1.3 semantics; `token_well_formed(".config/plugin/plugin.json","opencode")` True, `foreign_marker` None, v1.3 `owned_by` False.
